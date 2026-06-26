# Caption-to-Concept Decision Log

Last updated: 2026-06-26 KST

이 파일은 `gpic-caption-concepts` 프로젝트의 단일 시계열 정리 파일이다.
앞으로 caption-to-concept 파이프라인에서 어떤 결정을 했고, 어떤 실험을 했고, 어떤 결과가 나왔고, 무엇을 보류했는지는 이 파일에 계속 누적한다.

기존의 개별 정리 파일들은 삭제하지 않는다. 대신 이 파일이 canonical log 역할을 하고, 다른 문서는 세부 증거/샘플/원본 리포트로 둔다.

---

## 0. 프로젝트 목표

### 연구 목적

GPIC dataset의 caption만 사용해서 caption을 countable concept schema로 변환한다.
이후 DiT 기반 T2I 모델 checkpoint마다 어떤 concept을 얼마나 학습했을 때 generalization, memorization, 또는 다른 capability가 언제 발현되는지 추적하는 것이 목적이다.

### 제약 조건

- image는 보지 않는다.
- GPIC dataset의 caption만 concept으로 만든다.
- caption 안의 유용한 정보를 가능한 많이 보존하되, countable한 schema로 정리해야 한다.
- 100M captions를 3일 안에 처리할 수 있어야 한다.
- 사용 가능 자원은 H200 16장 조건을 전제로 한다.
- LLM 기반 full extraction은 비용과 속도 때문에 기본 경로로 쓰지 않는다.
- 우선은 rule + parser 기반으로 최대한 가고, 필요하면 나중에 LLM은 audit/refinement 용도로만 검토한다.

### 현재 큰 방향

caption을 바로 하나의 scene graph로 “해석 완료”하려고 하지 않는다.
먼저 가능한 안정적인 중간 산출물인 raw concept mentions와 raw edges를 만든 뒤, 이후 canonicalization과 scene graph/count table로 넘긴다.

현재 파이프라인은 다음 방향이다.

```text
raw caption
  -> optional noise cleanup
  -> quote retokenization
  -> object MWE retokenization
  -> generic hyphen span retokenization
  -> spaCy transformer/tagger/parser/lemmatizer
  -> noun chunks / dependency / POS / lemma
  -> Stage 8 raw concept extraction
  -> Stage 9 canonicalization
  -> Stage 10 scene graph / aggregate count table
```

---

## 1. 초기 문제 설정과 논문 조사

### 결정

caption-to-concept는 단순 keyword extraction이 아니라, caption 안의 object, attribute, relation, action, quantity, negation, style/medium, context 등을 countable하게 뽑는 문제로 정의했다.

### 논문 조사에서 확인한 점

- SPICE 계열은 object / attribute / relation tuple을 평가용 scene graph로 만든다.
- Stanford Scene Graph Parser는 textual scene graph extraction의 고전적인 baseline에 가깝다.
- T2I-CompBench, Structured Diffusion, SynGen, DSG류 논문은 prompt/caption의 compositional structure, relation, binding을 평가하거나 활용하지만, 모든 정보를 넓은 schema로 뽑는 완성형 off-the-shelf parser를 제공하지는 않는다.
- LLM 기반 structured extraction은 넓은 coverage를 얻기는 쉽지만, 100M captions / 3일 조건에는 기본 경로로 무겁다.
- 비LLM 기반으로 넓은 범위의 raw tuple extraction을 완전히 해결해주는 표준 도구는 사실상 없다. 각 논문도 목적에 맞춘 custom rule 또는 custom parser를 사용한다.

### 이 단계에서의 결론

논문에 있는 방법을 그대로 복붙해서 끝낼 수 있는 상황은 아니다.
따라서 다음 전략이 현실적이라고 판단했다.

1. linguistic parser로 token/POS/lemma/dependency/noun chunk를 만든다.
2. 논문들의 object/attribute/relation graph extraction 원리를 참고한다.
3. Stage 8 raw tuple extraction은 프로젝트 목적에 맞게 직접 구현한다.
4. Stage 9 canonicalization과 Stage 10 scene graph/count table은 별도 단계로 분리한다.

---

## 2. 파이프라인 단계 정리

### 초기 10단계 버전

처음에는 다음 단계로 정리했다.

1. noise 성분 제거
2. tokenization
3. POS tagging
4. predicate span detecting
5. other words lemmatize
6. dependency parsing
7. noun chunking
8. raw tuple extractor
9. canonicalization
10. scene graph 구축

### 이후 수정된 이해

dependency parsing은 raw tuple extraction이 아니다.

dependency parsing은 token 사이의 syntactic head/dependency label을 주는 단계다.
예를 들면 `dog -> on -> sofa` 같은 구조를 얻는다.

raw tuple extraction은 그 dependency tree를 해석해서 다음처럼 연구용 schema에 맞는 tuple/edge로 바꾸는 별도 단계다.

```text
object(dog)
object(sofa)
relation(dog, on, sofa)
```

즉 dependency parser는 재료를 만들고, raw tuple extractor는 그 재료를 concept schema로 번역한다.

### predicate span 용어 정리

초기에 `predicate span detecting`이라고 불렀지만, 실제로는 주로 다음을 포함한다.

- multi-word relation: `in front of`, `on top of`, `next to`
- phrasal verb / verb-preposition: `look at`, `stand on`, `sit in`
- comparative expression: `larger than`, `smaller than`

따라서 “predicate = 전치사”라는 뜻이 아니다.
문장 의미에서 relation/action predicate로 작동하는 span을 잡는 단계로 이해해야 한다.

현재 구현에서는 모든 predicate span을 parser 이전에 무조건 한 단어로 합치지는 않는다.
특히 `on top of`는 dependency parse 이후 Stage 8에서 relation span으로 재구성하는 방향이 더 안전하다.

---

## 3. spaCy를 기본 parser로 검토한 이유

### 결정

기본 linguistic parser는 spaCy를 중심으로 실험한다.

### 이유

spaCy는 한 pipeline 안에서 다음을 제공한다.

- tokenization
- POS tagging
- lemmatization
- dependency parsing
- noun chunking
- retokenizer
- PhraseMatcher / Matcher / DependencyMatcher
- batch processing
- GPU에서 transformer model 실행

따라서 2~7단계를 하나의 `Doc` 객체 안에서 이어서 처리하기 좋다.

### 단, 중요한 한계

spaCy 자체가 Stage 8 raw tuple extraction을 제공하지는 않는다.
즉 spaCy를 쓴다고 해서 object / attribute / relation / action / quantity tuple이 자동으로 나오지 않는다.
Stage 8은 우리가 직접 구현해야 한다.

### Stanford CoreNLP / Stanza와의 관계

- Stanford CoreNLP와 Stanza는 같은 Stanford 계열이지만, 출력 형식과 parser 생태계가 다르다.
- Stanford Scene Graph Parser는 Stanford CoreNLP 위에서 돌아가는 raw tuple extractor에 가깝다.
- Stanza는 UD 기반 parser에 가깝고, Stanford Scene Graph Parser와 바로 호환되는 같은 층위의 도구가 아니다.
- spaCy / Stanza / CoreNLP는 linguistic parser 층위다.
- Stanford Scene Graph Parser는 raw tuple extractor 층위다.

---

## 4. GPIC caption 샘플 확인

### 진행

GPIC caption을 받아보고 20개 샘플을 눈으로 확인했다.

### 관찰

caption은 일반적인 완성 문장만 있는 것이 아니었다.

다음 유형이 섞여 있었다.

- 정상 문장
- multi-sentence caption
- comma-separated tag list
- title/text/sign/banner가 포함된 caption
- quote가 포함된 caption
- 복합명사 / hyphenated expression
- 생략구문
- coordination이 복잡한 caption

이 때문에 단일 sentence parser만 믿으면 안 된다는 것이 확인되었다.

---

## 5. spaCy 모델 비교

### 비교한 모델

- `en_core_web_sm`
- `en_core_web_md`
- `en_core_web_lg`
- `en_core_web_trf`

### 초기 속도 관찰

초기 실험에서 CPU 기준으로 대략 다음 수준을 봤다.

```text
sm: 109 docs/sec
md: 101 docs/sec
lg: 99 docs/sec
trf: 47 docs/sec
```

이 값은 당시 설정과 CPU 실행 조건의 값이다.
이후 GPU / batch size / retokenizer 구성에 따라 값이 크게 달라졌다.

### 품질 관찰

20개 샘플에서 발견된 대표 오류는 다음과 같다.

- `trash can`에서 `can`을 조동사로 오인
- `music stands`에서 `stands`를 동사로 오인
- comma-separated tag list를 문장처럼 dependency parse하여 구조가 무너짐
- `blue jersey`를 PROPN으로 오인하는 경우
- `arched windows`에서 `arched`를 동사처럼 보는 경우
- `road ... runs ...` 구조에서 root/attachment가 이상해지는 경우
- quote 안의 title/text가 문장 구조를 망가뜨리는 경우
- coordination attachment 오류
- ellipsis 복원 실패

### 모델별 결론

- `sm`: 빠르지만 어려운 caption에서 오류가 많다.
- `md`: `sm` 대비 큰 개선이 적었다.
- `lg`: 일부 POS/root/coordination이 개선된다.
- `trf`: 가장 안정적이지만 완벽하지 않다.

현재 기본 후보는 `trf`다.
다만 `trf`도 Stage 8 extraction과 전처리/retokenization 없이는 안정적이라고 보기 어렵다.

---

## 6. tag-list caption 처리

### 문제

다음과 같은 caption은 문장이 아니라 tag list에 가깝다.

```text
brown boot, brick wall, display, indoor, large
```

이것을 일반 문장처럼 dependency parse하면 `display`, `large`, `indoor` 등이 이상하게 붙는다.

### 결정

tag-list caption은 sentence branch와 분리해서 처리한다.
단, 출력 schema는 sentence branch와 최대한 맞춘다.

### 처리 방향

1. caption shape를 판단한다.
2. comma-separated segment로 분리한다.
3. 각 segment를 짧은 noun phrase / attribute / context 후보로 본다.
4. dependency tree를 과신하지 않는다.
5. object / attribute / context mention과 약한 edge를 만든다.

### 결과

4개 tag-list caption 샘플에서 sm/lg/trf가 동일한 count를 냈다.

```text
objects: 19
attributes: 10
contexts: 1
has_attribute edges: 9
has_context edges: 1
candidate_has_attribute edges: 1
```

### 현재 판단

tag-list branch는 반드시 필요하다.
이 branch가 없으면 parser 품질 문제가 아니라 입력 형식 mismatch 때문에 결과가 망가진다.

---

## 7. Stage 8 raw concept extractor 구현

### 결정

Stage 8은 spaCy의 내장 기능이 아니라 직접 구현한다.

### 추가된 주요 파일

- `scripts/raw_concept_extractor.py`
- `scripts/extract_raw_concepts.py`
- `scripts/inspect_spacy_parse.py`

### 현재 Stage 8 산출물

`concept_mentions`

- object
- attribute
- quantity
- action
- relation
- context
- negation

`edges`

- has_attribute
- relation
- agent
- patient
- has_context
- has_quantity
- candidate_has_attribute
- negates

### 추출 방식 요약

- noun chunk root를 object 후보로 본다.
- noun chunk 내부 modifier를 attribute 후보로 본다.
- color/material/size/visual 등 modifier lexicon을 이용해 attribute role을 나눈다.
- verb를 action 후보로 본다.
- `nsubj`, `dobj`, `pobj`, `prep` 등 dependency label을 이용해 agent/patient/relation edge를 만든다.
- `in front of`, `on top of` 같은 multi-word relation은 dependency와 token span을 보고 Stage 8에서 재구성한다.
- tag-list caption은 별도 branch로 처리한다.

### 100 caption 초기 summary

초기 raw extraction sample 100개에서 관찰한 결과:

```text
caption shapes:
  multi-sentence: 57
  sentence-like: 22
  tag-list: 21

parse paths:
  sentence: 79
  tag_list: 21

concept_mentions:
  object: 731
  attribute: 471
  action: 209
  context: 49
  quantity: 16

edges:
  has_attribute: 466
  relation: 333
  agent: 158
  patient: 83
  has_context: 38
  has_quantity: 16
  candidate_has_attribute: 5
```

### 현재 판단

이 단계는 “최종 정답”이 아니라 raw 후보 생성 단계다.
Stage 9에서 canonicalization, merge, filtering, parent concept mapping을 해야 한다.

---

## 8. quote 처리

### 문제

quote 안의 title/text/sign/banner 내용이 parser를 망가뜨렸다.

예:

```text
near a "ROYAL CANIN" banner
with the number "1709-1"
Text reads "BANG GOES THE KNIGHTHOOD"
```

### 처음 검토한 방법

처음에는 quote span을 placeholder로 바꾸는 방법을 검토했다.

```text
"ROYAL CANIN" -> the quoted text
```

### placeholder 방식의 문제

일부 문맥에서 문법이 깨졌다.

```text
near a "ROYAL CANIN" banner
-> near a the quoted text banner
```

```text
with the number "1709-1"
-> with the number the quoted text
```

placeholder를 문맥별로 다르게 만들 수도 있지만, 계속 rule patch가 늘어날 가능성이 컸다.

### 최종 결정

placeholder로 바꾸지 않고, 원문 quote span 자체를 tokenizer 직후 retokenizer로 merge한다.

즉 `"ROYAL CANIN"`을 실제 token 하나처럼 다루되, 표면형은 원문을 보존한다.

### 구현 방향

- `raw_quote_merger` component를 parser 이전에 넣는다.
- quote span token에는 quote metadata를 확장 속성으로 붙인다.
- 기존 CLI 호환을 위해 `--mask-quotes` flag는 유지하되, 실제 동작은 raw quote retokenization이다.

### 실험 결과

비교한 전략:

- placeholder masking
- raw quote merge before parser
- raw quote merge after parser
- raw quote merge first

현재는 `raw_merge_first`가 가장 안정적이었다.

### Stage 9에서 해야 할 일

quote token은 최종 object로 그대로 두면 안 된다.
Stage 9에서 다음과 같이 정규화해야 한다.

```text
quoted token q0
-> TEXT_SPAN(q0) 또는 LABEL_VALUE(q0)
```

그리고 다음처럼 edge도 더 semantic하게 바꿔야 한다.

```text
reads --patient--> text
```

보다는

```text
source_object --reads_text--> q0
```

가 더 맞다.

---

## 9. modifier -> attribute lexicon

### 문제

caption의 modifier를 단순 attribute로만 뽑으면 count는 되지만 의미 subtype이 약하다.

예:

```text
red dress
wooden table
large umbrella
striped shirt
dirty wall
```

모두 attribute이지만 역할은 다르다.

### 초기 hard-coded set

처음에는 다음과 같은 작은 set을 직접 만들었다.

- color words
- material words
- size words
- visual words
- spatial relation words

### 사용자의 지적

이런 list가 전부일 수 없고, 100M captions를 처리하려면 외부 사전/데이터셋에서 가져와야 한다.

### 이후 검토한 외부 source

- Visual Attributes in the Wild
- COCO Attributes
- SUN Attributes
- Visual Genome attributes
- Open Images relationships
- XKCD colors
- Getty AAT
- WordNet

### 현재 clean attribute role 후보

현재는 다음 11개 subtype을 중심으로 정리했다.

```text
color_attribute
material_attribute
size_attribute
shape_attribute
pattern_attribute
texture_attribute
brightness_attribute
condition_attribute
state_attribute
pose_attribute
weather_attribute
```

### 현재 결정

무분별하게 attribute vocabulary를 확장하지 않는다.
role이 비교적 명확한 clean attribute만 우선 사용한다.

COCO high-confidence attribute도 clean 후보에 합치는 방향으로 정리했다.

---

## 10. multi-word relation lexicon

### 문제

`on top of`, `in front of`, `next to` 같은 relation은 여러 단어가 합쳐져 하나의 visual relation으로 작동한다.

### 중요한 결정

이것을 parser 이전에 반드시 한 token으로 merge해야 하는 것은 아니다.
오히려 parser가 본 구조를 Stage 8에서 재구성하는 편이 안전한 경우가 많다.

### 검토한 source

multiword relation lexicon은 다음 계층으로 만들기로 했다.

```text
multiword_relation_lexicon
├─ source: PDEP / TPP
│  └─ phrasal preposition surface forms
├─ source: SNACS / STREUSLE
│  └─ semantic subtype
├─ source: UD fixed/MWE
│  └─ collapse rule 기준
└─ source: VG/GQA/OpenImages
   └─ visual relation frequency / whitelist
```

### 현재 판단

Stage 8 relation extraction에서 multi-word relation span을 만들어야 한다.
Stage 9에서 canonical relation label로 정규화한다.

예:

```text
on top of -> on_top_of
in front of -> in_front_of
next to -> next_to
```

---

## 11. object MWE 문제

### 문제

spaCy가 복합명사를 잘못 POS/dependency 처리하는 경우가 있었다.

대표 예:

```text
trash can
music stands
hot dog
traffic light
wine glass
```

`trash can`에서 `can`이 AUX/MD로 잡히면 이후 noun chunk, dependency, raw extraction이 모두 꼬인다.

`music stands`에서 `stands`가 VERB로 잡히면 “악보대”가 아니라 “음악이 서 있다”처럼 해석된다.

### 초기 seed list

처음에는 작은 hand-written seed list를 만들었다.

예:

```text
trash can
wine glass
traffic light
tennis court
fire hydrant
hot dog
cell phone
```

### 결정

hand-written seed list는 삭제했다.
대신 high-confidence object MWE lexicon을 외부 source에서 만들기로 했다.

### 사용한 source

- COCO category fallback
- LVIS categories
- Open Images boxable labels
- Visual Genome object synsets
- WordNet noun MWEs

### 생성된 파일

- `resources/lexicons/object_noun_mwe_clean_core.tsv`
- `reports/object_noun_mwe_lexicon_summary.md`
- `scripts/build_object_mwe_lexicon.py`

### 첫 결과

처음에는 약 4,010개 phrase가 생성되었다.

이후 modifier attribute lexicon을 이용해 compositional adjective+noun phrase를 일부 제거했다.
그 결과 현재 clean core는 다음 수준이다.

```text
rows: 3,548
unique canonical: 1,828
plural/surface variants: 1,792
```

source membership 대략:

```text
lvis: 1,277
openimages: 331
visual_genome: 2,602
wordnet: 3,096
plural_variant: 1,792
coco: 30
```

### 제거/보류한 유형

다음과 같은 phrase는 object MWE로 합치면 attribute 정보를 잃을 수 있다.

```text
blue sky
yellow jacket
young woman
stone wall
third person
```

예를 들어 `stone wall`을 하나의 object MWE로 합치면 `stone`이라는 material attribute가 사라질 수 있다.

따라서 false merge가 false miss보다 위험하다고 판단했다.

### strict audit 파일

사용자가 검토 파일을 제공했다.

- `object_noun_mwe_clean_core_strict_pass.tsv`
- `object_noun_mwe_clean_core_audit_flags.tsv`

검토 결과 strict pass는 useful하지만 아직 적용하지 않기로 했다.

이유:

- strict pass를 적용하면 `music stand(s)`가 빠진다.
- 그러면 기존 핵심 error case인 `music stands`가 다시 망가진다.

현재 결정:

```text
strict_pass는 아직 적용하지 않는다.
audit_flags는 나중에 review 후보로 쓴다.
```

---

## 12. object MWE retokenizer 구현

### 추가 파일

- `scripts/object_mwe_retokenizer.py`

### 구현 방향

`PhraseMatcher`로 object MWE phrase를 찾고, spaCy `Doc.retokenize()` + `retokenizer.merge()`로 parser 이전에 하나의 token처럼 만든다.

### pipeline 위치

현재 큰 흐름:

```text
raw_quote_merger
-> object_mwe_merger
-> hyphen_span_merger
-> transformer/tagger/parser/lemmatizer
```

### 중요한 버그

처음에는 object MWE lexicon에서 공백이 있는 phrase만 로드했다.
그래서 `t-shirt`, `band-aid` 같은 hyphen-only object term이 빠졌다.

이후 space 또는 hyphen이 포함된 term을 모두 로드하도록 수정했다.

### POS regression 문제

object MWE를 merge했는데도 tagger가 merged token을 ADJ로 잡는 문제가 있었다.

예:

```text
American flag
acoustic guitar
```

이러면 object mention에서 빠질 수 있다.

### 보정 컴포넌트

`object_mwe_pos_corrector`를 추가했다.

pipeline:

```text
raw_quote_merger
-> object_mwe_merger
-> transformer
-> tagger
-> object_mwe_pos_corrector
-> parser
```

역할:

- object MWE lexicon에서 merge된 token인지 확인한다.
- 해당 token의 POS/TAG/lemma를 object noun으로 보정한다.
- 일반 token에는 적용하지 않는다.

### 판단

이 보정은 case-by-case patch가 아니라, high-confidence object MWE lexicon에 포함된 token에만 적용하는 general rule이다.
다만 lexicon precision이 낮아지면 위험해진다.

### 실험 결과

100 sample에서 object MWE bad POS가 다음처럼 줄었다.

```text
before: 2
after: 0
```

`American flag`, `acoustic guitar`가 object mention으로 회복되었다.

---

## 13. hyphen span 처리

### 문제

caption에 hyphenated expression이 많다.

예:

```text
t-shirt
hot-air balloon
well-dressed
bare-shouldered
two-story
black-and-white
2007-06-09
```

### 사용자의 질문

명사/형용사/동사 tag는 나중에 붙이더라도, 일단 `-`로 이어진 span은 parser 전에 merge하는 것이 맞는지 검토했다.

### 결정

두 계층으로 나눈다.

1. object MWE lexicon에 있는 hyphen phrase는 object MWE로 merge하고 noun 보정을 적용한다.
2. 나머지 plain hyphen span은 generic hyphen span으로 merge하되 POS는 강제하지 않는다.

### 추가 파일

- `scripts/hyphen_span_retokenizer.py`

### 현재 pipeline

```text
raw_quote_merger
-> object_mwe_merger
-> hyphen_span_merger
-> transformer/tagger
-> object_mwe_pos_corrector
-> parser
-> attribute_ruler
-> lemmatizer
-> ner
```

### generic hyphen merge rule

- alphabetic-ish token들이 plain hyphen으로 연결된 경우 merge한다.
- 숫자-only part가 포함된 날짜/번호류는 merge하지 않는다.

예:

```text
black-and-white -> merge
well-dressed -> merge
bare-shouldered -> merge
two-story -> merge
2007-06-09 -> skip
```

### 예시 검증

```text
t-shirt
  -> object MWE
  -> single token
  -> NOUN object

hot-air balloon
  -> object MWE
  -> full phrase merge
  -> NOUN object

well-dressed
  -> generic hyphen span
  -> VBN/amod modifier

bare-shouldered
  -> generic hyphen span
  -> ADJ

two-story
  -> generic hyphen span
  -> NUM/CD

black-and-white
  -> generic hyphen span
  -> ADJ

2007-06-09
  -> not merged
```

### 100 sample 결과

```text
object MWE tokens: 28
unique object MWE: 24
hyphen span tokens: 14
unique hyphen spans: 12
object MWE bad POS: 0
```

hyphen examples:

```text
black-and-white
close-up
bare-shouldered
chain-link
green-lit
light-colored
lit-up
Mercedes-Benz
orange-brown
snow-capped
snow-covered
thumbs-up
```

### close-up 관련 메모

`close-up`은 명사로 쓰일 수 있다.
다만 schema 관점에서는 physical object라기보다 shot / composition / view type에 가깝다.

따라서 Stage 8 또는 Stage 9에서 별도 role이 필요할 수 있다.

예:

```text
close-up -> view_or_composition_concept
```

---

## 14. 속도 벤치마크

### 기존 10k trf GPU baseline

초기 기준:

```text
reports/spacy_benchmark_10k_trf_gpu0_bs128_fixed.json
  docs/sec: 202.5608
  parse_seconds: 49.3679

reports/spacy_benchmark_10k_trf_gpu0_bs256_fixed.json
  docs/sec: 202.2128
  parse_seconds: 49.4528
```

### benchmark script 수정

`scripts/benchmark_spacy_parse.py`에 다음 option을 추가했다.

```text
--mask-quotes
--merge-object-mwes
--merge-hyphen-spans
--object-mwe-lexicon
```

또한 결과 JSON에 `pipe_names`를 기록하도록 했다.

### 현재 retokenizer 포함 10k trf GPU 결과

```text
reports/spacy_benchmark_10k_trf_gpu0_bs128_mwe_hyphen.json
  docs/sec: 226.7499
  parse_seconds: 44.1014

reports/spacy_benchmark_10k_trf_gpu0_bs256_mwe_hyphen.json
  docs/sec: 235.4477
  parse_seconds: 42.4723
```

같은 세션에서 retokenizer 없는 current baseline:

```text
reports/spacy_benchmark_10k_trf_gpu0_bs256_current_baseline.json
  docs/sec: 237.7223
  parse_seconds: 42.0659
```

### 해석

초기 기준 202 docs/sec와 비교하면 현재 retokenizer 포함 pipeline이 느려지지 않았다.
같은 세션 baseline 237.7 docs/sec와 비교하면 retokenizer overhead는 약 1% 수준이다.

token 수는 retokenization으로 줄었다.

```text
baseline tokens: 274,500
retokenized tokens: 263,500
```

현재 병목은 retokenizer가 아니라 transformer parser다.

### 주의

이 10k benchmark는 현재 20개 caption을 반복한 형태일 가능성이 있다.
따라서 실제 GPIC unique 10k/100k sample에서도 다시 측정해야 한다.

---

## 15. 현재 pipeline 상태

### 현재 구현된 것

- GPIC caption 일부 추출/검토
- spaCy 모델별 parse sample 생성
- tag-list branch
- raw quote retokenization
- object MWE lexicon build
- object MWE retokenization
- object MWE POS correction
- generic hyphen span retokenization
- Stage 8 partial raw concept extraction
- parse/error report들
- speed benchmark script

### 현재 기본 추천 pipeline

```text
1. noise cleanup
   - 현재는 기본 off 또는 최소화

2. raw quote retokenization
   - quote span 자체 merge
   - placeholder 치환 안 함

3. object MWE retokenization
   - high-confidence object MWE lexicon 기반
   - parser 이전 merge

4. generic hyphen span retokenization
   - object MWE가 아닌 hyphen span merge
   - POS 강제 없음

5. spaCy trf parsing
   - token/POS/lemma/dependency/noun chunk

6. object MWE POS correction
   - object MWE lexicon에서 온 merged token만 NOUN 보정

7. Stage 8 raw concept extraction
   - object/attribute/action/relation/quantity/context/negation
   - tag-list branch 포함

8. Stage 9 canonicalization
   - 아직 본격 구현 전

9. Stage 10 scene graph / count table
   - 아직 본격 구현 전
```

---

## 16. 아직 해결해야 할 문제

### Stage 8 관련

- coordination attachment repair
- ellipsis handling
- pronoun policy
- relation attachment confidence
- `close-up` 같은 shot/composition noun 처리
- `text reads X`, `sign says X`, `number X` 같은 text/label event 처리
- tag-list branch와 sentence branch의 attribute role sharing
- object MWE false positive / false negative audit

### Stage 9 canonicalization 관련

아직 본격 구현하지 않았다.

해야 할 것:

- surface form -> canonical concept
- plural/singular 통일
- quote token -> TEXT_SPAN / LABEL_VALUE
- object alias 통일
- relation label canonicalization
- attribute subtype canonicalization
- parent concept 연결
- parent concept을 raw caption에 직접 넣지 않기
- raw concept과 canonical concept을 둘 다 보존하기

중요한 원칙:

```text
raw caption에 있는 표현은 raw concept으로 남긴다.
parent concept은 별도 필드나 count level로 추가한다.
```

예:

```text
raw: golden retriever
canonical: golden_retriever
parent: dog / animal
```

parent를 caption 안에 직접 끼워 넣으면 원문 정보가 훼손된다.

### Stage 10 scene graph / count table 관련

아직 본격 구현하지 않았다.

해야 할 것:

- caption-level graph
- concept mention table
- edge table
- canonical concept count table
- checkpoint-wise tracking 가능한 aggregate schema
- confidence / source / parser model metadata 보존

---

## 17. 현재 보류한 결정

### strict object MWE audit 적용

보류.

이유:

- strict pass가 false positive를 줄이는 데는 좋아 보인다.
- 하지만 `music stand(s)` 같은 필요한 MWE가 빠진다.
- 현재 핵심 error case regression을 만들 수 있다.

### LLM extractor 사용

기본 경로에서는 보류.

이유:

- 100M captions / 3일 조건에는 부담이 크다.
- 다만 audit, gold sample 생성, rule refinement에는 유용할 수 있다.

### Stanford Scene Graph Parser로 회귀

보류.

이유:

- object/attribute/relation 기본형에는 유용하지만, 현재 목표 schema 전체를 커버하지 않는다.
- Java/CoreNLP 기반이라 현재 Python/spaCy 파이프라인과 운영 복잡도가 커진다.

### 모든 MWE를 parser 전에 merge

보류.

이유:

- false merge가 attribute/relation 정보를 잃게 할 수 있다.
- object MWE와 generic hyphen span만 우선 처리한다.

---

## 18. 참고해야 할 기존 파일들

이 파일은 다음 문서/리포트들의 핵심 내용을 합친 것이다.
세부 샘플이나 원본 표가 필요하면 아래 파일을 본다.

### docs

- `docs/parser_error_cases_and_mitigations.md`
- `docs/spacy_model_comparison_20_samples.md`

### reports

- `reports/tag_list_branch_summary.md`
- `reports/model_success_rate_summary.md`
- `reports/stage8_algorithm_details.md`
- `reports/stage8_minimal_raw_extractor_review.md`
- `reports/object_noun_mwe_lexicon_summary.md`
- `reports/quote_retokenizer_experiment.md`
- `reports/raw_concepts_sample_100_trf_summary.md`
- `reports/relation_span_lexicon_summary.md`
- `reports/multiword_relation_layers_summary.md`
- `reports/modifier_attribute_lexicon_summary.md`
- `reports/attribute_clean_candidate_summary.md`
- `reports/coco_attribute_subtype_tagging.md`
- `reports/coco_vg_attribute_overlap.md`
- `reports/spacy_benchmark_10k_trf_gpu0_bs128_fixed.json`
- `reports/spacy_benchmark_10k_trf_gpu0_bs256_fixed.json`
- `reports/spacy_benchmark_10k_trf_gpu0_bs128_mwe_hyphen.json`
- `reports/spacy_benchmark_10k_trf_gpu0_bs256_mwe_hyphen.json`
- `reports/spacy_benchmark_10k_trf_gpu0_bs256_current_baseline.json`

### scripts

- `scripts/inspect_spacy_parse.py`
- `scripts/benchmark_spacy_parse.py`
- `scripts/extract_raw_concepts.py`
- `scripts/raw_concept_extractor.py`
- `scripts/build_object_mwe_lexicon.py`
- `scripts/object_mwe_retokenizer.py`
- `scripts/hyphen_span_retokenizer.py`

### resources

- `resources/lexicons/object_noun_mwe_clean_core.tsv`

---

## 19. 앞으로 이 파일 업데이트 규칙

새로운 실험이나 결정이 생기면 아래 형식으로 이 파일에 추가한다.

```markdown
## YYYY-MM-DD - 짧은 제목

### 배경

왜 이 실험/결정을 했는지.

### 한 일

무엇을 바꿨는지.

### 결과

정량 결과, 샘플 결과, 발견한 문제.

### 결정

채택 / 보류 / 폐기 중 무엇인지.

### 후속 작업

다음에 해야 할 일.
```

중요한 원칙:

- 성공한 것만 쓰지 않는다.
- 실패한 전략도 기록한다.
- 왜 버렸는지 남긴다.
- 벤치마크 숫자는 파일명과 함께 남긴다.
- schema나 parser 관련 용어가 바뀌면 이전 용어와 새 용어를 함께 적는다.

---

## 20. 다음 작업 후보

현재 가장 자연스러운 다음 단계는 다음 중 하나다.

1. Stage 8 extractor를 object MWE / quote / hyphen pipeline 기준으로 다시 100 sample audit
2. unique GPIC 1k/10k sample로 속도와 품질 재측정
3. Stage 9 canonicalization 설계
4. quote/text/sign/number event를 Stage 8/9에서 정리
5. `close-up`, `side view`, `front view`, `aerial view` 같은 composition/view concept 처리
6. ellipsis/coordination repair rule 추가
7. object MWE lexicon audit를 precision-first로 다시 정리

현재 우선순위는 1 -> 2 -> 3 순서가 가장 안전하다.

---

## 2026-06-26 - tag-list 단일 person segment POS 보정

### 배경

tag-list caption에서 단일 segment `man`이 spaCy에서 `INTJ/UH`로 잡히는 문제가 있었다.

문장에서는 `Man, that is huge.`처럼 `man`이 실제 감탄사로 쓰일 수 있다.
하지만 tag-list caption의 단일 segment `man`은 거의 항상 image object tag로 봐야 한다.

### 결정

`man` 하나만 hard coding하지 않고, tag-list branch 전용 lexical override rule로 처리한다.

핵심 원칙:

```text
sentence caption에서는 적용하지 않는다.
tag-list caption에서만 적용한다.
pos_raw / tag_raw는 spaCy 결과를 보존한다.
pos_norm / tag_norm만 downstream schema 판단용으로 보정한다.
```

### 구현

`scripts/tag_list_parser.py`에 person object lexicon을 추가했다.

예:

```text
man, men, woman, women, person, people, boy, girl, child, children,
baby, kids, player, rider
```

tag-list segment가 단일 token이고 해당 token 또는 segment norm이 person object lexicon에 있으면:

```text
pos_raw: spaCy 원본
tag_raw: spaCy 원본
pos_norm: NOUN
tag_norm: NN 또는 NNS
concept_type: object
confidence: high
```

raw POS가 이미 object로 잡힌 경우 role은 기존처럼 `segment_head`로 둔다.
spaCy가 `INTJ/UH`처럼 object로 보지 못한 경우에만 role을 `tag_list_person_object_override`로 남긴다.

### 이유

이 처리는 parser의 일반 POS 결과를 덮어쓰는 것이 아니라, tag-list라는 입력 형식에서는 segment classifier를 우선한다는 결정이다.

즉:

```text
hard-coded exception X
tag-list-only lexical normalization O
```

### 후속 작업

- person lexicon을 너무 넓히지 않는다.
- 나중에 object single-word lexicon을 따로 만들 경우, person override와 일반 object override를 분리한다.
- sentence caption에는 같은 override를 적용하지 않는다.

---

## 2026-06-26 - with-absolute missing object recovery

### 배경

with-absolute 구문에서 spaCy가 `with`를 `SCONJ/mark`로 보고, 뒤쪽 noun이 noun chunk에서 빠지는 문제가 있었다.

대표 문제 케이스:

```text
case 29: with snow-capped mountains in the distance
case 42: with workers and equipment in the distance
case 43: with trees and an overcast sky above
```

### 비교한 방법

A안:

```text
parser 전에 with를 ADP/IN으로 강제
```

B안:

```text
raw parse는 그대로 두고 Stage 8에서 with-absolute 뒤쪽 missing noun-like token만 보수적으로 회수
```

### 실험 결과

현재 retokenizer pipeline 기준으로 case 29, 42, 43을 다시 확인했다.

```text
A안:
  dependency parse 변화 없음
  noun chunk 변화 없음

B안:
  case 29 -> mountains 회수, snow-capped attribute 연결 가능
  case 42 -> workers, equipment 회수
  case 43 -> trees, sky 회수, overcast attribute 연결 가능
```

기존 정상 케이스 16, 27, 37, 40, 49, 67, 77, 97에서는 B안 recovery가 추가 object를 만들지 않았다.

### 결정

A안은 폐기한다.
with POS를 강제로 ADP로 바꿔도 parser/noun chunk가 개선되지 않았다.

B안을 채택한다.
단, 매우 좁은 조건에서만 작동한다.

### 구현

`scripts/raw_concept_extractor.py`에 `_recover_with_absolute_objects()`를 추가했다.

작동 조건:

```text
with token:
  lower == "with"
  tag == IN
  dep == mark

candidate token:
  with 뒤쪽 같은 sentence 안에 있음
  기존 object/context로 잡히지 않음
  dep in {advcl, conj, dep, nsubj, nsubjpass}
  POS/TAG가 noun-like
  context word가 아님
  compound/poss/amod/det/cc 등 modifier token이 아님
```

회수된 object는 다음처럼 기록한다.

```text
concept_type: object
role: with_absolute_recovered_object
confidence: medium
edge: scene_contains(scene, recovered_object)
```

회수된 object에 직접 붙은 modifier는 기존 `_add_modifier()` 로직을 재사용해 attribute로 연결한다.
단, with-absolute recovery에서는 부작용을 줄이기 위해 `advmod` 같은 부사성 modifier는 attribute로 붙이지 않고, `amod`, `compound`, `nummod`, `poss`, `acl`만 허용한다.

예:

```text
snow-capped -> mountains
overcast -> sky
```

### 원칙

- spaCy raw POS/dependency/noun chunk는 수정하지 않는다.
- 기존 noun chunk root로 잡힌 object는 건드리지 않는다.
- relation을 강하게 붙이지 않고 `scene_contains`로 약하게 둔다.
- Stage 9에서 필요하면 canonical graph edge로 재해석한다.

---

## 2026-06-26 - fastcoref sidecar audit for pronoun/anaphoric references

### 배경

100개 caption raw concept 결과에서 `he`, `she`, `it`, `they`, `them`, `that`, `who`, `both`, `each`, `others` 같은 reference 표현이 그대로 `object`로 들어가는 문제가 확인됐다.

예:

```text
The duck swims... It glides...
object: duck
object: it
agent(glides, it)
```

이 상태로 concept count를 만들면 실제 object가 아니라 문법적 reference가 count에 섞인다.

### 실험한 도구

`fastcoref==2.1.6`의 `FCoref`를 sidecar로 붙였다.

중요한 호환성:

```text
fastcoref + transformers 5.x -> 모델 로딩 실패
fastcoref + transformers<5 -> CPU inference 성공
```

따라서 `environment.yml`에는 `fastcoref==2.1.6`, `transformers<5`를 추가한다.

처음에는 로컬 Windows GPU 실행이 `cudnnGetVersion` 로딩 문제로 실패했다.
원인은 `scripts/run_python.ps1`이 micromamba env를 활성화하지 않고 `python.exe`만 직접 실행해, env 안의 `Library\bin` CUDA/cuDNN DLL보다 시스템 CUDA DLL이 먼저 잡힐 수 있었기 때문이다.

해결:

```text
run_python.ps1에서 .mamba/env, Scripts, Library/bin, Library/usr/bin, Library/mingw-w64/bin을 PATH 앞에 추가
```

수정 후 확인:

```text
torch cuda: 13.0
device: NVIDIA GeForce RTX 5080 Laptop GPU
cudnn version: 92301
fastcoref FCoref(device="cuda:0") smoke test 성공
```

현재 fastcoref audit 기본 device는 `cuda:0`이다.
H200 서버에서는 같은 wrapper 원칙을 유지하되, multi-GPU sharding을 별도 구현해야 한다.

### 구현

`scripts/audit_fastcoref_resolution.py`를 추가했다.

역할:

```text
raw concept JSONL
  -> caption별 fastcoref cluster 생성
  -> raw concept 안의 pronoun/anaphoric mention 탐지
  -> coref antecedent span 탐색
  -> antecedent span 안의 기존 object mention과 연결 가능한지 audit
```

이 스크립트는 기존 raw concept JSONL을 직접 수정하지 않는다.
현재는 보정 전 검토용 sidecar report만 생성한다.

### 100개 샘플 결과

실행 파일:

```text
reports/fastcoref_audit_sample_100_trf_current.md
reports/fastcoref_audit_sample_100_trf_current.jsonl
```

결과:

```text
reference_mentions_seen: 45
resolved_to_object: 34
unresolved: 11
```

reference type:

```text
pronoun_reference: 23
possessive_reference: 13
nominal_reference: 7
relative_reference: 2
```

추천 처리:

```text
redirect_edges_to_antecedent: 20
attach_possessor_metadata: 13
exclude_from_object_count_unresolved: 9
prefer_dependency_rule: 2
manual_nominal_resolution: 1
```

### 중요한 수정

처음 구현에서는 fastcoref antecedent span 안의 마지막 object를 고르는 문제가 있었다.

예:

```text
A man in a blue shirt -> shirt
A paved road with a yellow line -> line
```

이건 잘못된 연결이다.
현재는 antecedent span과 겹치는 첫 noun chunk의 root를 우선 선택한다.

수정 후:

```text
A man in a blue shirt -> man
A paved road with a yellow line -> road
A tall glass of latte macchiato -> glass
A small artifact with a rounded top and flat base -> artifact
```

### 현재 결정

fastcoref는 Stage 8 raw extraction 앞단에 넣지 않는다.
caption을 rewrite하지도 않는다.

현재 채택할 구조:

```text
spaCy parse / raw concept extraction
  -> fastcoref sidecar
  -> pronoun object는 count에서 제외
  -> coref가 안정적으로 antecedent object를 찾은 경우 edge만 redirect 후보로 기록
```

`that/who/which` relative pronoun은 fastcoref보다 dependency rule로 처리하는 쪽이 더 안전하다.

예:

```text
a sign that reads "MILE 0"
```

여기서는 `that`을 object로 세지 않고, Stage 8 rule에서 `sign --reads_text--> quote` 같은 구조로 바꾸는 방향이 맞다.

### 남은 문제

- `a red one`, `the other`, `others`, `both`, `each` 같은 nominal reference는 fastcoref만으로 충분하지 않다.
- plural/group antecedent에서 `both -> man and woman`처럼 단일 object로 collapse하면 정보가 손실된다.
- possessive reference는 object redirect가 아니라 possessor metadata로 남길지 결정이 필요하다.

---

## 2026-06-26 - Maverick predefined-mention audit for nominal anaphora

### 배경

fastcoref는 `he/she/it/they` 같은 일반 pronoun에는 도움이 됐지만, `one/other/others/both/each` 같은 nominal-anaphoric reference에는 충분하지 않았다.

예를 들면 다음과 같은 caption에서는 surface form만 보면 object인지 reference인지 애매하다.

```text
Several cars are parked nearby, including a red one.
Two men smile for the camera. One wears a vest, the other a yellow shirt.
Children sit on chairs. One child holds a violin, while others are seated.
Four people sit at a table, each holding a glass.
```

그래서 외부 coreference 도구 중 Maverick을 추가로 실험했다.

### 설치와 호환성

`maverick-coref==1.0.7`을 설치했다.

Windows에서는 설치 중 build 로그 출력 때문에 cp949 decoding error가 났고, `PYTHONUTF8=1`을 켠 뒤 설치가 성공했다.

또 PyTorch 2.6 이후 `torch.load()`의 기본값이 `weights_only=True`로 바뀌면서 Maverick checkpoint 로딩이 실패했다.
현재 audit script에서는 Maverick wrapper를 얇게 감싸 `load_from_checkpoint(..., weights_only=False)`로 로딩한다.

이 설정은 신뢰하는 공식 Maverick checkpoint를 로컬에서 읽기 위한 compatibility patch다.
임의의 checkpoint를 받을 때는 그대로 쓰면 안 된다.

### 중요한 발견

Maverick을 그냥 실행하면 `a red one` 같은 nominal mention을 안정적으로 잡지 못했다.

하지만 우리가 만든 object candidate와 nominal candidate를 `predefined_mentions`로 넣으면 다음처럼 cluster를 만들 수 있었다.

```text
cars <-> a red one
```

즉 Maverick은 여기서 end-to-end resolver가 아니라, 우리가 만든 후보 mention들이 같은 coreference cluster로 묶일 수 있는지 확인하는 sidecar audit 도구에 가깝다.

### 구현

추가한 script:

```text
scripts/audit_maverick_nominal_references.py
```

입력:

```text
reports/raw_concepts_sample_100_trf_current.jsonl
```

출력:

```text
reports/maverick_nominal_audit_sample_100_trf_current.md
reports/maverick_nominal_audit_sample_100_trf_current.jsonl
```

처리 흐름:

```text
raw concept JSONL
  -> spaCy trf + quote/object-MWE/hyphen retokenizer
  -> object mention 후보 구성
  -> coordination group 후보 구성
  -> one/other/others/both/each nominal 후보 구성
  -> Maverick predefined_mentions로 cluster 생성
  -> antecedent 후보를 rule로 선택
  -> audit report 작성
```

### 100 sample 결과

현재 sample 100개 기준 nominal 후보는 9개였다.

```text
one_anaphor: 4
other_anaphor: 3
group_both: 1
distributive_each: 1
```

resolution 결과:

```text
resolved_to_candidate: 7
unresolved: 2
```

하지만 resolved 7개를 그대로 성공으로 보면 안 된다.
Maverick cluster가 너무 넓게 뭉치는 경우가 있어서 false positive 위험이 크다.
그래서 report에는 `quality_flag`를 추가했다.

```text
compact_cluster
broad_cluster_check_manually
no_cluster
```

`broad_cluster_check_manually`는 자동 치환 금지 신호다.

### 관찰된 사례

좋은 신호:

```text
Several cars ... a red one
-> one 후보가 cars 계열과 연결됨
```

```text
A man and a woman ... Both
-> Both가 coordination group과 연결됨
```

```text
Four people ... each
-> each가 Four people과 연결됨
```

위험한 신호:

```text
One wears a vest...
```

여기서 `One`은 사람 reference인데, cluster가 너무 넓으면 `bathroom` 같은 엉뚱한 antecedent가 후보로 잡힐 수 있다.

```text
others are seated...
```

`others`는 보통 이전 children/people group을 가리키지만, cluster가 넓으면 clothing group 쪽으로 잘못 붙을 수 있다.

### 결정

Maverick은 production Stage 8 resolver로 바로 넣지 않는다.

현재 결정:

```text
Maverick = nominal anaphora audit sidecar
```

사용 방식:

1. raw concept extraction은 기존 spaCy/rule pipeline으로 수행한다.
2. `one/other/others/both/each` 후보만 별도 audit한다.
3. Maverick cluster가 compact하고 antecedent가 명확할 때만 Stage 9 후보로 넘긴다.
4. broad cluster는 자동 merge/redirect하지 않는다.
5. `both/each`는 단일 object로 collapse하지 말고 group/distributive semantics를 보존한다.

### 다음 작업

nominal-anaphoric reference는 외부 도구만으로 해결하지 말고, 다음 rule을 같이 만들어야 한다.

```text
one + modifier
  -> 가까운 이전 plural object type을 복사하고 modifier를 attribute로 붙이는 후보

the other / others
  -> discourse contrast link
  -> object count에는 직접 넣지 않음

both
  -> coordination group link
  -> 단일 object로 collapse하지 않음

each
  -> distributive group link
  -> group member별 relation 후보로 확장 가능
```

따라서 다음 우선순위는 Maverick 적용 확대가 아니라, nominal reference 전용 conservative rule layer를 설계하는 것이다.

---

## 2026-06-26 - ambiguous quantity cue handling

### 배경

`several`, `few`, `many`, `multiple` 같은 수량 표현이 단순 modifier/attribute로 분류될 수 있다는 문제가 확인됐다.

기존 Stage 8 rule은 quantity를 거의 다음 조건으로만 잡았다.

```text
token.dep_ == nummod
or token.pos_ == NUM
```

하지만 spaCy는 다음 표현들을 항상 `NUM/nummod`로 주지 않는다.

```text
several cars
few dogs
many cats
some people
both men
each glass
no people
```

이 표현들은 caption-to-concept에서 단순 attribute가 아니라 count/group/distribution signal이다.

### 결정

공통 quantity lexicon을 만들고, sentence branch와 tag-list branch가 같이 사용하게 했다.

추가한 파일:

```text
scripts/quantity_lexicon.py
```

현재 quantity role:

```text
exact_quantity
approximate_quantity
indefinite_quantity
group_quantity
distributive_quantity
zero_quantity
partitive_quantity
```

예시:

```text
Three people -> exact_quantity
several cars -> approximate_quantity
some people -> indefinite_quantity
both men -> group_quantity
each glass -> distributive_quantity
no people -> zero_quantity
most people -> partitive_quantity
```

### 구현

sentence branch:

```text
scripts/raw_concept_extractor.py
```

변경점:

1. noun chunk modifier 처리 전에 `quantity_role(token)`을 먼저 확인한다.
2. `det`로 붙은 `some/all/every/no`도 quantity이면 skip하지 않는다.
3. `with_absolute` recovery modifier에서도 같은 quantity rule을 사용한다.
4. `each/both/all/some`처럼 noun chunk root 자체가 quantity/reference인 경우 object로 만들지 않는다.
5. action subject/object 처리에서도 root-only quantity token은 object로 승격하지 않는다.

tag-list branch:

```text
scripts/tag_list_parser.py
```

변경점:

1. tag segment modifier 후보를 모을 때 quantity token은 POS/dep와 무관하게 후보로 올린다.
2. modifier가 quantity이면 `attribute`가 아니라 `quantity` mention을 만들고 `has_quantity` edge를 붙인다.

### Smoke test

확인한 예시:

```text
Several cars are parked nearby, including a red one.
-> Several: approximate_quantity
-> cars --has_quantity--> Several
```

```text
A few dogs and many cats sit near no people.
-> few: approximate_quantity
-> many: approximate_quantity
-> no: zero_quantity
```

```text
Both men hold each glass.
-> Both: group_quantity
-> each: distributive_quantity
```

```text
several cars, many cats, no people
-> tag-list branch에서도 has_quantity edge 생성
```

### 100 sample 결과

재생성한 파일:

```text
reports/raw_concepts_sample_100_trf_current.jsonl
reports/raw_concepts_sample_100_trf_current_summary.md
```

요약:

```text
object: 730
attribute: 412
action: 208
context: 49
quantity: 30
```

quantity role:

```text
exact_quantity: 15
approximate_quantity: 8
group_quantity: 4
distributive_quantity: 2
indefinite_quantity: 1
```

edge:

```text
has_quantity: 28
```

`Four people ..., each holding ...` case에서는 `each`가 더 이상 object로 들어가지 않고 `distributive_quantity`로만 남는다.

### 남은 문제

root-only quantity는 Stage 8에서 object로 세지 않는 것이 맞지만, 일부 relation은 Stage 9에서 다시 연결해야 한다.

예:

```text
Four people ..., each holding a glass flask
```

Stage 8에서는 다음 정도까지만 안전하다.

```text
people --has_quantity--> Four
quantity(each, distributive_quantity)
action(holding)
object(flask)
```

Stage 9에서는 다음 rule이 필요하다.

```text
each + action
  -> antecedent group을 찾음
  -> distributive action 후보로 연결
```

즉 이번 변경은 quantity detection 문제를 해결한 것이고, distributive/event binding은 다음 단계에서 별도로 처리한다.

---

## 2026-06-26 - class-based nominal reference resolver

### 배경

`one/other/others/both/each` 같은 nominal-anaphoric 표현을 처리해야 하지만, 단어별/문장별 땜빵 rule을 계속 늘리는 방식은 피하기로 했다.

따라서 다음 원칙으로 Stage 8.5 sidecar resolver를 만들었다.

```text
word-specific patch X
reference cue class + antecedent scoring O
```

### 추가한 파일

```text
scripts/reference_lexicon.py
scripts/nominal_reference_resolver.py
reports/nominal_reference_resolution_sample_100_trf_current.md
reports/nominal_reference_resolution_sample_100_trf_current.jsonl
```

### Reference cue class

현재 reference cue는 다음 class로만 분류한다.

```text
singular_substitute
  examples: one, ones

contrastive_reference
  examples: other, others, another

group_reference
  examples: both, all

distributive_reference
  examples: each, every
```

중요한 점:

```text
one person
both men
other buildings
each glass
```

처럼 뒤의 noun을 직접 수식하는 경우는 reference로 보지 않는다.
이 경우는 quantity/modifier 쪽에서 처리한다.

반대로 다음처럼 standalone argument로 쓰이면 reference 후보로 본다.

```text
One wears a vest.
the other a yellow shirt.
others are seated.
Both look toward the camera.
each holding a flask.
```

### Antecedent scoring feature

후보 antecedent는 raw concept의 object mention과 dependency 기반 coordination group에서 만든다.
점수는 단어 의미 리스트가 아니라 다음 구조적 feature로 계산한다.

```text
distance / recency
sentence gap
plural or group signal
has_quantity signal
coordination group 여부
agent_like antecedent 여부
patient_like candidate penalty
syntactic salience
reference modifier presence
```

`agent_like`는 raw edge에서 해당 object가 action의 `agent`로 등장했는지 본다.
`patient_like`는 action의 `patient`로 등장했는지 본다.

이 기준을 넣은 이유:

```text
Two men ... One wears a vest and red scarf, the other ...
```

에서 `vest and red scarf`는 가까운 coordination group이지만 patient-like object이다.
반면 `Two men`은 이전 sentence의 agent-like plural group이다.
따라서 `the other`는 `vest/scarf`가 아니라 `Two men` 쪽으로 가야 한다.

마찬가지로:

```text
A man and a woman ... wearing a top and earrings. Both look ...
```

에서 `top and earrings`는 가까운 patient-like coordination group이고,
`A man and a woman`은 더 멀지만 agent-like coordination group이다.

### Conservative policy

자동 적용을 너무 쉽게 하지 않기 위해 margin threshold를 둔다.

현재 기본값:

```text
min_score: 45
ambiguous_margin: 15
max_antecedent_tokens: 80
```

정책:

```text
resolved
  -> Stage 9 후보로 사용 가능

ambiguous
  -> 후보는 있지만 자동 적용하지 않음

unresolved
  -> object count에서 surface reference 제외 후보로 남김
```

singular substitute는 modifier 유무에 따라 다르게 다룬다.

```text
a red one
  -> antecedent type 복사 + red modifier 반영 후보

bare one
  -> 새 object를 만들지 않음
  -> antecedent/member reference link만 남김
```

### 100 sample 결과

재생성한 파일:

```text
reports/nominal_reference_resolution_sample_100_trf_current.md
reports/nominal_reference_resolution_sample_100_trf_current.jsonl
```

결과:

```text
references_seen: 9
resolved: 8
ambiguous: 1
unresolved: 0
```

reference class:

```text
singular_substitute: 4
contrastive_reference: 3
group_reference: 1
distributive_reference: 1
```

주요 case:

```text
case 15
One -> Two men
recommendation: link_singular_reference
other -> Two men

case 16
others -> Children

case 40
a red one -> Several cars
recommendation: copy_antecedent_type_apply_modifiers

case 62
Both -> A man and a woman
status: ambiguous
reason: margin 9, automatic application 보류

case 63
One -> Two men
recommendation: link_singular_reference

case 89
one -> Two men
recommendation: link_singular_reference

case 98
each -> Four people
```

### Maverick과의 관계

Maverick은 predefined_mentions를 넣으면 일부 cluster signal을 주지만, cluster가 넓게 뭉치는 문제가 있었다.
따라서 현재 기본 결정은 다음과 같다.

```text
nominal_reference_resolver.py
  -> 기본 Stage 8.5 sidecar

Maverick audit
  -> 비교/검증용 external signal
```

### 남은 작업

이 resolver는 아직 raw concepts를 직접 수정하지 않는다.
다음 단계에서는 Stage 9에서 다음 edge 후보를 만들 수 있다.

```text
reference_link(reference, antecedent)
substitute_type(one, antecedent_object_type)
contrastive_link(other, antecedent_group)
group_link(both, antecedent_group)
distributive_link(each, antecedent_group)
```

단, `ambiguous`는 자동 적용하지 않는다.

---

## 2026-06-26: raw concept에서 pronoun/reference object와 possessive pronoun attribute 제외

### 문제

100개 상세 리포트 검토에서 다음 두 가지 잔여 오류가 확인됐다.

```text
1. pronoun / relative pronoun / anaphoric nominal object가 raw object로 들어감
   examples: it, them, who, one, other, others, both, each

2. possessive pronoun이 attribute로 들어감
   examples: her phone -> her가 attribute
```

이 둘은 countable visual concept으로 직접 세면 안 된다.
특히 `one/other/both/each`류는 Stage 8 object가 아니라 Stage 8.5 nominal reference resolver에서 antecedent link 후보로 처리해야 한다.

### 결정

Sentence branch와 tag-list branch 모두 같은 정책으로 정리했다.

```text
raw object 후보:
  allow:
    POS in {NOUN, PROPN}
    or tag in {NN, NNS, NNP, NNPS}

  exclude:
    POS == PRON
    tag in {PRP, WP, WP$, WDT}
    reference_class(token) != None
    root-only quantity cue

raw attribute 후보:
  exclude:
    dep == poss and tag in {PRP$, WP$}
    dep == poss and POS == PRON
```

즉 `it`, `them`, `who`, `which` 같은 pronoun/relative pronoun은 object count에서 제외한다.
`one`, `other`, `others`, `both`, `each` 같은 anaphoric nominal/reference cue도 object count에서 제외한다.
`her`, `his`, `their`, `whose` 같은 possessive pronoun은 visual attribute로 세지 않는다.

### 구현 파일

```text
scripts/raw_concept_extractor.py
scripts/tag_list_parser.py
docs/pos_tag_dep_rule_reference.md
```

### 100 sample 검증

재생성한 파일:

```text
reports/raw_concepts_sample_100_trf_current.jsonl
reports/raw_concepts_sample_100_trf_current_summary.md
reports/case_detail_sample_100_trf_current.md
reports/nominal_reference_resolution_sample_100_trf_current.md
reports/nominal_reference_resolution_sample_100_trf_current.jsonl
```

검증 결과:

```text
pronoun_or_reference_objects: 0
possessive_pronoun_attributes: 0
```

raw concept count:

```text
object: 704
attribute: 399
action: 208
context: 49
quantity: 30
```

nominal reference resolver:

```text
references_seen: 9
resolved: 8
ambiguous: 1
unresolved: 0
```

### 해석

Stage 8 raw concept는 이제 surface reference를 countable object로 직접 세지 않는다.
대신 Stage 8.5에서 reference cue와 antecedent scoring으로 별도 sidecar를 만든다.

따라서 `a red one`은 raw object `one`으로 세지 않고,
Stage 8.5에서 `one -> Several cars`처럼 antecedent 후보를 찾은 뒤
Stage 9 canonicalization에서 `car + red` 쪽으로 반영하는 구조가 맞다.

반대로 15/63/89 같은 bare `one`은 `man` 같은 새 object type으로 복사하지 않는다.
이 경우는 raw object에서 제외하고, Stage 8.5 sidecar에서 antecedent/member reference link로만 남긴다.

---

## 2026-06-26: pronoun blocking 순서 수정 - 먼저 antecedent로 rewiring한 뒤 object count에서 제외

### 문제

직전 구현은 pronoun/reference token을 object에서 바로 제외했다.
이 덕분에 object count 오염은 줄었지만, pronoun이 subject/object/relation target으로 쓰인 edge까지 같이 사라졌다.

대표 오류:

```text
case 35
He has red nail polish...

잘못된 상태:
  action(has)
  patient(has, nail_polish)
  agent 없음

원하는 상태:
  agent(has, man)
  patient(has, nail_polish)
```

```text
case 03
An American flag is behind her

잘못된 상태:
  relation 없음

원하는 상태:
  relation(American flag, behind, woman)
```

```text
case 51
a stone sign that reads "MILE 0 VICTORIA BC"

원하는 상태:
  agent(reads, sign)
  patient(reads, quote_text)
```

### 결정

Stage 8 sentence branch의 순서를 수정했다.

```text
1. object noun chunk 생성
2. context 생성
3. reference_object_by_token_i 생성
   - pronoun/relative pronoun token -> 기존 object id
4. action / relation edge 추출
   - subject/object/relation target이 pronoun이면 antecedent object id로 치환
5. pronoun/reference surface 자체는 object mention으로 만들지 않음
```

즉 blocking을 먼저 하는 것이 아니라,
edge에서 쓸 antecedent rewiring map을 먼저 만든 뒤 object count에서는 제외한다.

### 구현

```text
scripts/raw_concept_extractor.py
```

새로 추가된 핵심 구조:

```text
reference_object_by_token_i:
  token_i(He)   -> object_id(man)
  token_i(her)  -> object_id(woman)
  token_i(them) -> object_id(person/people)
  token_i(that) -> object_id(sign)
```

personal pronoun은 다음 feature를 보수적으로 점수화한다.

```text
recency / distance
candidate가 subject였는지
person/gender/number match
same/previous sentence
context penalty
```

relative pronoun은 fastcoref보다 dependency rule을 우선한다.

```text
that -> reads -> relcl -> sign
-> agent(reads, sign)
```

### 100 sample 검증

재생성한 파일:

```text
reports/raw_concepts_sample_100_trf_current.jsonl
reports/raw_concepts_sample_100_trf_current_summary.md
reports/case_detail_sample_100_trf_current.md
```

object count 오염:

```text
pronoun_reference_objects: 0
```

대표 case 결과:

```text
case 03
relation(American flag, behind, woman)

case 28
relation(lights, behind, person)

case 35
agent(has, man)

case 41
agent(stands, man)
relation(curtains, behind, man)

case 51
agent(reads, sign)
patient(reads, "MILE 0 VICTORIA BC")
```

edge count 변화:

```text
relation: 302 -> 328
agent: 144 -> 153
patient: 78 -> 79
```

object count는 그대로 유지됐다.

```text
object: 704
```

### fastcoref와의 관계

fastcoref는 이미 `He -> man`, `her -> woman`, `them -> person/people` 후보를 찾을 수 있음을 audit으로 확인했다.
하지만 100M caption 처리 기본 경로에 fastcoref를 직접 넣으면 비용이 커진다.

따라서 현재 기본 Stage 8은 다음처럼 간다.

```text
production default:
  dependency/recency 기반 lightweight rewiring

fastcoref:
  audit 또는 high-risk subset 검증용
```

필요하면 이후 옵션으로 `--use-fastcoref-rewiring` 같은 batch resolver를 별도 stage로 붙일 수 있다.

### 보정: nominal reference는 raw rewiring에서 제외

처음 lightweight rewiring을 넣을 때 `both/each`가 personal pronoun처럼 raw edge에 직접 연결되는 문제가 있었다.
예를 들어 `Both look...`이 `agent(look, woman)`처럼 단일 object로 잘못 collapse될 수 있었다.

그래서 raw rewiring 대상에서 `reference_class(token) != None`인 token은 제외했다.

```text
raw rewiring 허용:
  he / she / him / her / it / they / them / that / which / who ...

raw rewiring 제외:
  one / other / others / both / each / all / every ...
```

이후 policy:

```text
relative pronoun:
  raw edge rewiring 허용
  example: that reads -> sign reads

personal pronoun:
  raw edge rewiring 허용
  example: He has -> man has

nominal/anaphoric reference:
  raw edge rewiring 보류
  Stage 8.5 nominal_reference_resolver sidecar에서 처리
```
## 2026-06-26: quote span은 object에서 제외하고 quote_text attribute로 보존

### 문제

raw quote retokenization 이후에도 quote span이 noun chunk root로 잡히면 object count에 들어가는 경우가 있었다.

대표 예:

```text
case 03: "Closing the Access Divide."
case 08: "BANG GOES THE KNIGHTHOOD"
case 32: "BORDERLINE BIENNALE ..."
case 47: “edición, diversidad cultural y desarrollo.”
case 51: "MILE 0 VICTORIA BC"
case 78: “Assembleia Legislativa do Estado do Espírito Santo”
```

이 값들은 실제 visual object가 아니라 화면/간판/포스터/번호 등에 적힌 text value다.
따라서 object count에 들어가면 concept frequency를 오염시킨다.

### 결정

quote span은 다음 정책으로 처리한다.

```text
1. 원문 quote span 자체를 tokenizer 직후 Retokenizer로 merge한다.
2. merged quote token에 is_raw_quote metadata를 붙인다.
3. Stage 8 object candidate에서는 quote token을 제외한다.
4. quote token은 attribute / quote_text mention으로 반드시 1회 보존한다.
5. parser가 안정적으로 연결한 edge는 유지한다.
6. quote token의 syntactic head가 이미 object이면 carrier edge를 추가한다.
```

즉 quote는 object가 아니다.
하지만 caption에 적힌 유용한 정보이므로 버리지 않고 `quote_text` attribute로 보존한다.

### 구현

```text
scripts/quote_retokenizer.py
scripts/raw_concept_extractor.py
scripts/tag_list_parser.py
```

핵심 구현:

```text
quote_retokenizer:
  RAW_QUOTE_FLAG = is_raw_quote
  retokenizer.merge(span, attrs={"LEMMA": ..., "_": {"is_raw_quote": True}})

raw_concept_extractor:
  _extract_quote_attributes()
  _extract_quote_carrier_edges()
  _is_object_candidate_token(token)에서 quote token 제외
  _object_for_token(quote) -> quote_text attribute id 반환

tag_list_parser:
  quote token을 segment object head에서 제외
  단독 quote segment는 floating attribute / quote_text로 처리
```

### 100 sample 검증

```text
quote metadata count: 13
quote_text attribute count: 13
quote object count: 0
```

대표 edge 보존:

```text
case 08:
  patient(reads, "BANG GOES THE KNIGHTHOOD")

case 25:
  banner --has_attribute--> "ROYAL CANIN"

case 03:
  text --has_attribute--> "Closing the Access Divide."

case 32:
  patient(reads, "BORDERLINE BIENNALE ...")

case 51:
  patient(reads, "MILE 0 VICTORIA BC")

case 90:
  number --has_attribute--> "1709-1"
```

남은 주의점:

```text
case 90:
  with the number "1709-1"

현재는 "1709-1" 자체가 quote_text attribute로 보존되고,
`appos -> number` 구조를 이용해 `number --has_attribute--> quote_text`까지 복원된다.
다만 더 복잡한 text-bearing structure는 Stage 9 canonicalization에서
number/sign/text/banner -> quote_text로 추가 보강하는 편이 안전하다.
```
## 2026-06-26: non-finite / subject-ellipsis action agent inheritance

### 문제

기존 Stage 8 action extraction은 action token의 직접 child에 `nsubj` / `nsubjpass`가 있을 때만 agent edge를 만들었다.
하지만 caption에는 다음처럼 표면 주어가 생략된 non-finite verb가 자주 나온다.

```text
A woman stands at a podium speaking...
-> speaking의 agent는 woman

A man stands nearby, watching the dog.
-> watching의 agent는 man

A female soccer player stands..., preparing to kick a ball.
-> preparing의 agent는 soccer player
-> kick의 agent도 soccer player
```

이전 rule에서는 action 자체와 patient는 잡히지만 agent가 비어 있었다.

### 결정

직접 subject가 없는 action에 한해서, 다음 일반 rule로 agent를 상속한다.

```text
acl / relcl:
  action head noun을 agent 후보로 사용

advcl / xcomp / ccomp / conj / acomp:
  parent verb의 subject를 agent 후보로 사용
  parent verb도 subject가 없으면 재귀적으로 상위 action에서 찾음

including 계열 prep action:
  head noun을 agent 후보로 사용
```

명시적 subject가 이미 있으면 inheritance를 적용하지 않는다.
nominal/anaphoric reference, 예: `one`, `other`, `both`, `each`,는 raw 단계에서 억지로 collapse하지 않고 sidecar에 남긴다.

### 구현

```text
scripts/raw_concept_extractor.py
```

핵심 helper:

```text
_inherited_action_agent_tokens()
_allows_agent_inheritance()
_verb_subjects()
```

### 100 sample 검증

```text
before:
  action without agent: 64

after:
  inherited agent edges: 61
  action without agent: 4
```

대표 복원:

```text
case 03: agent(speaking, woman)
case 25: agent(watching, man)
case 30: agent(sharing, man), agent(sharing, woman)
case 41: agent(singing, man)
case 43: agent(preparing, soccer player), agent(kick, soccer player)
case 44: agent(positioned, hockey player), agent(looking, hockey player)
case 48: agent(holding, man), agent(smiling, woman)
```

남은 4개는 raw agent inheritance 문제가 아니라 nominal/anaphoric reference 문제다.

```text
case 15: One wears...
case 62: Both look...
case 63: One is on top, controlling...
case 63: other who is lying...
```

이들은 Stage 8.5 nominal reference sidecar와 Stage 9 canonicalization에서 처리하는 편이 안전하다.

### 추가 수정

non-finite inheritance가 case 44의 기존 pronoun bug를 드러냈다.

```text
They hold...
bad: They -> shorts
desired: They -> hockey player
```

원인은 `hockey_player`처럼 object MWE lemma가 underscore로 합쳐지면서 `player`를 person lemma로 인식하지 못한 것이다.
따라서 person candidate 판정에서 underscore/hyphen으로 나뉜 lemma part도 확인하도록 수정했다.

```text
hockey_player -> player -> person candidate
soccer_player -> player -> person candidate
```
## 2026-06-26: self-edge drop and self-resolution guards

### 문제

pronoun/reference rewiring 이후 relation source와 target이 같은 object로 collapse되는 self-edge가 남았다.

대표 오류:

```text
case 39: relation(spoon, beside, spoon)
case 44: relation(hockey player, in_front_of, hockey player)
case 47: relation(person, in_front_of, person)
case 98: relation(woman, beside, woman)
```

또한 neutral pronoun `it`이 가장 가까운 noun이나 같은 action의 subject로 잘못 붙는 문제가 있었다.

```text
case 22:
  bad: agent(glides, head)
  desired: agent(glides, duck)

case 32:
  bad: patient(surrounding, light)
  desired: patient(surrounding, eye)
```

### 결정

Stage 8에서 다음 방어 rule을 적용한다.

```text
1. relation edge에서 source == target이면 drop
2. non-reflexive pronoun-resolved patient가 같은 action의 agent와 같으면 reject
3. locomotion/posture action의 subject pronoun은 body part antecedent를 강하게 감점
4. pronoun object가 같은 action의 subject로 resolve되는 self-like 후보도 강하게 감점
```

reflexive pronoun은 예외다.

```text
itself, himself, herself, themselves, ...
```

### 구현

```text
scripts/raw_concept_extractor.py
scripts/extract_raw_concepts.py
scripts/inspect_spacy_parse.py
```

핵심 구조:

```text
RawConceptExtractionResult.skipped_edges
RawConceptExtractor.skip_edge()
_is_self_resolved_action_target()
_is_nonreflexive_self_resolution_candidate()
_pronoun_controls_whole_agent_action()
_is_body_part_candidate()
```

`extract_raw_concepts.py`는 JSONL record에 `skipped_edges`를 저장하고 summary에 reason별 count를 기록한다.
`inspect_spacy_parse.py`는 case 상세 md에 `Skipped Raw Concept Edges` 표를 추가한다.

### 100 sample 검증

```text
self_edges_remaining: 0
skipped self_edge_after_coref: 4
```

대표 결과:

```text
case 22:
  agent(glides, duck)

case 32:
  patient(surrounding, eye)

case 39:
  drop relation(spoon, beside, spoon)

case 44:
  drop relation(hockey player, in_front_of, hockey player)

case 47:
  drop relation(person, in_front_of, person)

case 98:
  drop relation(woman, beside, woman)
```

현재는 repair 가능한 경우는 resolution scoring에서 먼저 고치고,
그래도 self-edge가 생기는 relation만 drop한다.

## 2026-06-26: 전치사 MWE 전용 lexicon 분리

### 문제

기존 `resources/lexicons/multiword_relation_*` 파일은 전치사 MWE만 담은 파일이 아니었다.
`in front of`, `on top of`, `next to` 같은 clean adposition뿐 아니라 `attached to`, `covered with`, `looking at`, `lying on` 같은 predicate + preposition 표현도 섞여 있었다.

이 파일을 그대로 Stage 8 전치사 relation 처리에 쓰면 다음 두 층위가 섞인다.

```text
전치사 MWE: in front of, on top of, next to, inside of
predicate span: attached to, looking at, covered with, made of
```

따라서 전치사 MWE는 명사 MWE처럼 별도 clean core 파일로 관리하기로 결정했다.

### 결정

전치사 MWE 전용 파일을 새로 만들었다.

```text
resources/lexicons/preposition_mwe_clean_core.tsv
```

이 파일에는 전치사/부사적 전치사구로 볼 수 있는 항목만 넣는다.

포함:

```text
in front of
on top of
next to
inside of
outside of
close to
near to
left of / right of
in the middle of / in the center of
```

제외:

```text
attached to
covered with
looking at
lying on
made of
connected to
```

제외한 항목들은 전치사 MWE가 아니라 predicate span / action relation 후보이므로, 이후 별도 predicate lexicon에서 관리한다.

### 구현

새 loader를 추가했다.

```text
scripts/preposition_mwe_lexicon.py
```

`scripts/raw_concept_extractor.py`는 더 이상 hardcoded `top/front/back/side/middle/center/edge` 목록에 의존하지 않고, `preposition_mwe_clean_core.tsv`를 읽어서 multi-word preposition relation을 판단한다.

현재 지원하는 주요 패턴:

| pattern | 예시 | 처리 |
|---|---|---|
| `adp_mid_of` | `on top of`, `in front of` | inner `of`에서 하나의 relation으로 collapse |
| `adp_det_mid_of` | `in the front of`, `on the side of` | determiner 포함 surface를 우선 매칭 |
| `mid_of` | `front of`, `left of` | bare region phrase로 매칭 |
| `adp_adp` | `next to`, `close to`, `across from` | head + final ADP surface로 매칭 |
| `adp_of` | `inside of`, `outside of` | canonical `inside` / `outside`으로 매핑 |

### 검증

스모크 테스트:

```text
A cat sits on top of a table.
  -> relation(cat, on_top_of, table)

A microphone is in front of a person.
  -> relation(microphone, in_front_of, person)

A chair is next to a table.
  -> relation(chair, next_to, table)

A toy is inside of a box.
  -> relation(toy, inside, box)

A cup is close to a plate.
  -> relation(cup, near, plate)
```

100 sample 재생성 결과:

```text
relation edges: 320
self_edge_after_coref skipped: 4
```

확인된 MWE relation evidence:

```text
in_front_of: 2
next_to: 1
inside: 1
bottom_of: 1
side_of: 1
at_top_of: 1
```

### 현재 정책

전치사 MWE lexicon은 "문법적으로 전치사 역할을 하는 multi-word expression"만 관리한다.
`attached to`, `looking at`, `covered with`처럼 predicate 의미가 핵심인 표현은 이 파일에 넣지 않는다.

## 2026-06-26: 전치사 MWE lexicon 확장 - candidate / clean / audit 구조

### 문제

초기 `preposition_mwe_clean_core.tsv`는 매우 보수적으로 시작해서 36개 항목만 담고 있었다.
`in front of`, `on top of`, `next to` 같은 핵심 표현은 처리했지만, GPIC caption에서 나올 수 있는 region phrase 계열 coverage가 부족했다.

### 결정

전치사 MWE를 손으로 직접 추가하지 않고 builder를 통해 관리한다.

새 스크립트:

```text
scripts/build_preposition_mwe_lexicon.py
```

생성 파일:

```text
resources/lexicons/preposition_mwe_candidates.tsv
resources/lexicons/preposition_mwe_clean_core.tsv
resources/lexicons/preposition_mwe_audit_flags.tsv
```

extractor는 계속 `preposition_mwe_clean_core.tsv`만 참조한다.
`candidates`는 검토용 전체 후보이고, `audit_flags`는 clean에서 제외한 후보를 기록한다.

### 확장 source

```text
1. generated_region_pattern
   top/bottom/front/back/side/edge/center/middle/left/right/corner/end/base/surface + of
   at/on/in/from/near/along/to/by + (the) + region + of

2. manual_clean_adposition
   across from, adjacent to, ahead of, out of, off of, up against 등

3. mixed_relation_collapse_rules
   기존 multiword_relation_collapse_rules.tsv 중
   complex_preposition_phrase / multiword_adposition_phrase만 후보로 import
```

### reject rule

다음은 전치사 MWE clean core에서 제외한다.

```text
predicate head로 시작:
  leaning against
  surrounded by
  attached to
  covered with
  looking at

non-visual adposition:
  because of
  due to
  according to
  instead of
```

이번 build에서 실제 audit로 빠진 항목:

```text
leaning against -> predicate_head_not_preposition_mwe
surrounded by   -> predicate_head_not_preposition_mwe
```

### 결과

```text
before clean_core: 36
candidate: 143
after clean_core: 141
audit_flags: 2
```

pattern 분포:

```text
adp_mid_of: 55
adp_det_mid_of: 55
mid_of: 14
adp_adp: 10
adp_of: 7
```

source 분포:

```text
generated_region_pattern: 124
mixed_relation_collapse_rules: 29
manual_clean_adposition: 17
```

### 스모크 테스트

```text
A sign stands at the edge of a road.
  -> relation(sign, at_edge_of, road)

A vase sits near the corner of a table.
  -> relation(vase, near_corner_of, table)

A person stands to the left of a car.
  -> relation(person, left_of, car)

A box is out of a bag.
  -> relation(box, out_of, bag)

A cup is adjacent to a plate.
  -> relation(cup, next_to, plate)

A poster hangs from the side of a building.
  -> relation(poster, from_side_of, building)
```

### 100 sample 재검증

```text
records_written: 100
relation edges: 318
self_edge_after_coref skipped: 4
```

이전보다 object mention은 줄고 context mention은 늘었다.
이는 `side/end/base/top` 같은 region noun이 독립 object가 아니라 multi-word preposition 내부 토큰으로 처리되기 때문이다.

```text
object: 674
context: 65
```

새로 확인된 MWE relation evidence:

```text
near_end_of: 1
from_side_of: 1
base_of: 1
```

## 2026-06-26: front/side 계열 전치사 MWE safety rule

### 문제

`front of` / `side of` 계열은 object-object spatial relation과 object-region relation이 섞인다.

```text
in front of the car
  -> object가 car 앞에 있음
  -> in_front_of

the front of the car
  -> car의 앞부분
  -> front_region_of

logo on the front of the shirt
  -> shirt 앞부분 표면 위의 logo
  -> in_front_of가 아님
```

초기 확장 lexicon에서는 다음 항목들이 너무 공격적으로 canonicalize되어 있었다.

```text
front of        -> in_front_of
on front of     -> in_front_of
on the front of -> in_front_of
side of         -> side_of
on side of      -> side_of
on the side of  -> side_of
```

### 결정

clean 자동 적용 범위를 줄였다.

```text
in front of -> in_front_of, high
front of    -> front_region_of, medium
side of     -> side_region_of, medium
```

다음은 clean core에서 제외하고 audit/review로 보낸다.

```text
in the front of
on front of
on the front of
on side of
on the side of
```

이 표현들은 나중에 Stage 9에서 region node를 명시적으로 만들 때 다시 다루는 편이 안전하다.

### 구현

```text
scripts/build_preposition_mwe_lexicon.py
scripts/preposition_mwe_lexicon.py
scripts/raw_concept_extractor.py
```

builder에는 두 정책을 추가했다.

```text
SURFACE_REGION_CANONICAL_OVERRIDES:
  front of -> front_region_of, medium
  side of  -> side_region_of, medium

SURFACE_REGION_REVIEW_TERMS:
  in the front of
  on front of
  on the front of
  on side of
  on the side of
```

또한 audit로 빠진 긴 표현이 extractor에서 짧은 `front of` / `side of`로 fallback되지 않도록,
`preposition_mwe_audit_flags.tsv`의 reject term을 loader가 읽고 raw extractor에서 block한다.

### 결과

```text
clean_core: 136
audit_flags: 7
```

audit reason:

```text
ambiguous_surface_region_phrase: 5
predicate_head_not_preposition_mwe: 2
```

스모크 테스트:

```text
A person stands in front of a car.
  -> relation(person, in_front_of, car), high

A logo is on the front of a shirt.
  -> no in_front_of collapse
  -> relation(logo, on, front)
  -> relation(front, of, shirt)

The front of the car is red.
  -> relation(front, front_region_of, car), medium

The side of the building is brick.
  -> relation(side, side_region_of, building), medium
```

100 sample 재검증:

```text
records_written: 100
object: 674
context: 65
relation edges: 318
self_edge_after_coref skipped: 4
```

## 2026-06-26: spatial/prepositional self-edge repair

### 문제

기존 self-edge 처리는 precision 방어만 했다.

```text
relation(source, target)
if source == target:
  skip self_edge_after_coref
```

이 방식은 `person in_front_of person` 같은 잘못된 relation을 count하지 않는 장점은 있지만,
원래 caption에 있던 relation recall도 같이 사라진다.

대표 케이스:

```text
case 47
Each person has a microphone and nameplate in front of them.

bad:
  relation(person, in_front_of, person) -> skip

desired:
  relation(microphone, in_front_of, person)
  relation(nameplate, in_front_of, person)
```

### 결정

모든 self-edge를 복구하지 않고, spatial/prepositional relation에 한정해서 보수적 repair를 적용한다.

적용 조건:

```text
edge_type == relation
source == target
relation in spatial/preposition relation whitelist
target token is pronoun/reference
```

repair 방식은 두 가지다.

```text
1. alternate source repair
   - have/hold/position/show/display 같은 predicate 아래에 relation phrase가 붙었고
   - relation phrase 왼쪽 가까이에 object 후보가 있으면
   - source를 그 object 후보로 교체

2. alternate target repair
   - source는 가까운 clause subject로 보존하는 편이 자연스럽고
   - target pronoun이 plural/group pronoun이면
   - source 이전의 plural/person antecedent를 다시 찾음
```

중립 단수 `it`은 아직 repair하지 않는다.
`it`은 glass/tray/table/doily처럼 후보가 너무 쉽게 갈라져서, 현재 rule로 자동 복원하면 오히려 잘못된 relation을 만들 가능성이 높다.

### 구현

```text
scripts/raw_concept_extractor.py
```

추가된 주요 helper:

```text
_repair_self_edge_relation()
_prefers_alternate_relation_source()
_alternate_relation_source_ids()
_alternate_relation_target_id()
_local_relation_source_candidates()
_coordination_group_tokens()
```

repair evidence는 원래 relation 이름 뒤에 명시적으로 남긴다.

```text
in_front_of; repaired_self_edge_source from person
beside; repaired_self_edge_target from them->woman
```

### 100 sample 결과

```text
before:
  relation edges: 318
  self_edge_after_coref skipped: 4

after:
  relation edges: 322
  self_edge_after_coref skipped: 1
```

복원된 케이스:

```text
case 44:
  relation(hockey_stick, in_front_of, hockey_player)

case 47:
  relation(microphone, in_front_of, person)
  relation(nameplate, in_front_of, person)

case 98:
  relation(woman, beside, man)
```

보류한 케이스:

```text
case 39:
  A spoon and sugar packet are beside it.

  remaining skip:
    relation(spoon, beside, spoon)

  reason:
    neutral it의 target 후보가 glass/tray/table/doily 등으로 갈라짐.
    현재 rule로 자동 repair하면 packet beside spoon 같은 잘못된 복원이 생길 수 있어 skip 유지.
```

## 2026-06-26: scene_context retyping and duplicate merge

### 문제

`background`, `foreground`, `distance`, `scene`, `setting` 같은 단어는 물리적 object라기보다 caption 전체의 scene-level context에 가까운 경우가 많다.
그런데 기존 extractor는 noun chunk root를 먼저 object로 만들고, 이후 `_extract_contexts()`에서 같은 token을 context로 다시 만들었다.

대표 예시:

```text
in the background
against a dark background
Pine trees frame the foreground.
blurred background
```

이 경우 raw concept에 다음처럼 중복이 생겼다.

```text
object(background)
context(background)
```

object count table 관점에서는 `background/foreground`가 실제 object 빈도에 섞이는 것이 문제다.

### 결정

scene_context는 작고 보수적인 lexicon + syntax 조건으로 처리한다.
`surface`, `ground`, `wall`, `sky`, `field`, `area`, `side`, `edge`, `corner`처럼 실제 scene element/object로 셀 수 있는 단어는 이번 rule에서 제외했다.

현재 high-confidence scene context head:

```text
background
foreground
scene
setting
distance
indoors
outdoors
dusk
dawn
```

soft context head:

```text
day
daytime
evening
indoor
morning
night
nighttime
outdoor
sunset
```

soft head는 modifier로 쓰이면 context로 보지 않는다.
예를 들어 `night sky`, `outdoor table` 같은 경우 token이 `compound/amod`로 붙으면 scene_context로 올리지 않는다.

### 구현

추가 파일:

```text
scripts/scene_context_lexicon.py
```

추가/수정한 핵심 함수:

```text
scene_context_role(token)
is_scene_context_lemma(lemma)
RawConceptExtractor._ensure_scene_context()
RawConceptExtractor._merge_duplicate_scene_context_objects()
RawConceptExtractor._add_chunk_modifiers()
```

sentence branch에서는 noun chunk root가 scene_context로 판정되면 object를 만들지 않고 context mention을 만든다.
modifier는 버리지 않고 context에 그대로 붙인다.

```text
blurred background
-> context(background)
-> has_attribute(background, blurred)
```

기존 object/context 중복이 이미 만들어진 경우에는 token 기준 alias merge를 수행한다.

```text
object(background) + context(background)
-> context(background)
```

tag-list branch에도 같은 원칙을 적용했다.

```text
orange flower, green leaves, blurred background
-> object(flower), object(leaves), context(background)
-> has_attribute(background, blurred)
```

### 100 sample 검증

기준 리포트:

```text
reports/raw_concepts_sample_100_trf_current_summary.md
reports/case_detail_sample_100_trf_current.md
```

변경 후 요약:

```text
object: 643
context: 71
scene_context role: 44
relation edges: 322
self_edge_after_coref skipped: 1
```

변경 직전 대비:

```text
object: 647 -> 643
context: 70 -> 71
scene_context: 40 -> 44
relation: 322 -> 322
self_edge_after_coref skipped: 1 -> 1
```

`background/foreground/distance/scene/setting/indoors/outdoors/dusk/dawn` 계열이 100개 상세 리포트에서 object mention으로 남지 않는 것을 확인했다.
관계 edge 수와 self-edge repair 결과는 유지되어, scene_context retyping이 relation extraction을 크게 흔들지는 않았다.

## 2026-06-26: nominal reference 복원 본류 적용

### 실수

`one/other/both/each` 같은 nominal/anaphoric reference에 대해 이전 구현은 다음 상태였다.

```text
오염 방지:
  reference_class(token) != None인 token을 object 후보에서 제외

복원:
  scripts/nominal_reference_resolver.py sidecar audit에서만 수행
  raw_concept_extractor 본류에는 미적용
```

따라서 40번 예시가 raw concept에서 누락됐다.

```text
Several cars, including a red one

bad current raw:
  object(cars)
  quantity(several)
  action(including)

missing:
  one -> cars
  red one -> red car
```

이건 sidecar audit 결과를 본류 적용 결과로 착각한 것이다.

### 결정

nominal reference는 raw extractor 본류에서 high-confidence일 때만 복원한다.

기본 원칙:

```text
1. one/other/both/each 자체를 object로 세지 않는다.
2. 항상 reference mention을 만든다.
3. antecedent가 확실하면 refers_to edge를 만든다.
4. a red one처럼 modifier가 있는 singular substitute는 antecedent type을 복사한 derived object를 만든다.
5. bare One/the other는 새 object를 만들지 않고 antecedent에 link만 건다.
6. Both/each가 coordination group을 가리키면 group mention을 만든다.
```

### 구현

수정 파일:

```text
scripts/raw_concept_extractor.py
```

추가한 핵심 함수:

```text
_resolve_nominal_reference_tokens()
_nominal_reference_resolution()
_nominal_reference_candidates()
_nominal_coordination_group_candidates()
_nominal_reference_score()
_ensure_nominal_reference_instance()
_nominal_reference_candidate_mention_id()
```

추가 mention / edge:

```text
concept_type:
  reference
  group

roles:
  singular_substitute
  contrastive_reference
  group_reference
  distributive_reference
  nominal_reference_instance
  coordination_group

edges:
  refers_to
  derived_from
  has_member
```

### 40번 결과

```text
Several cars, including a red one

reference(one)
object(red car)
refers_to(one, cars)
derived_from(red car, cars)
has_attribute(red car, red)
patient(including, red car)
relation(cars, include, red car)
```

즉 `one` 자체는 object가 아니고, `red car`가 derived object로 살아난다.

### Both 오처리 수정

초기 본류 적용 직후 62번에서 문제가 생겼다.

```text
A man and a woman ... Both look toward the camera

bad:
  Both -> earrings
```

원인:

```text
nearest plural object인 earrings가 score에서 이김
coordination group candidate를 만들지 않았음
```

수정:

```text
A man and a woman
-> group(A man and a woman)
-> has_member(group, man)
-> has_member(group, woman)

Both
-> refers_to(group)
-> agent(look, group)
```

또한 `both/each`가 human-action subject인데 후보가 non-person object이면 강한 penalty를 준다.

### 100 sample 검증

기준 리포트:

```text
reports/raw_concepts_sample_100_trf_current_summary.md
reports/case_detail_sample_100_trf_current.md
```

변경 후 summary:

```text
reference: 8
group: 1
nominal_reference_instance: 1
refers_to edges: 8
derived_from edges: 1
has_member edges: 2
```

대표 복원:

```text
case 15:
  One -> men
  other -> men
  agent(wears, men)

case 40:
  one -> cars
  red one -> red car

case 62:
  Both -> A man and a woman
  agent(look, A man and a woman)

case 63:
  One -> men
  other -> men
```

### 남은 한계

case 63은 아직 완전 해결이 아니다.

```text
One is on top, controlling the other...
```

현재는 `One`과 `other`가 둘 다 `men` antecedent로 붙는다.
따라서 `one man controls other man`처럼 두 개의 distinct member instance로 split하지는 못한다.

이 문제는 단순 reference link가 아니라 entity splitting / member-level anaphora 문제다.
다음 단계에서 `Two men -> member_1/member_2` 같은 member instance 생성이 필요하다.

## 2026-06-27 - generic definite NP reference resolver 적용

### 배경

100개 샘플에서 `The object`, `The structure`, `The individual` 같은 generic definite NP가 새 object로 count되는 문제가 남아 있었다.
대표 케이스는 38, 49, 57, 73, 80이다.
이 문제는 Maverick/Coref 같은 무거운 외부 coreference model을 100M caption production path에 넣기보다, spaCy parse 결과 위에서 high-confidence case만 빠르게 alias하는 방식으로 처리하기로 결정했다.

### 적용한 방식

`RawConceptExtractor.run()` 순서를 다음처럼 조정했다.

```text
scene_context merge
-> pronoun/reference token 1차 resolve
-> generic definite NP resolve
-> pronoun/reference token 2차 resolve
-> nominal reference resolve
-> action/relation extraction
```

새 resolver는 다음 조건을 모두 만족할 때만 동작한다.

```text
1. noun chunk root가 generic trigger head이다.
   - object/item/thing/entity/artifact/fragment/piece
   - structure
   - individual/figure

2. NP가 definite이다.
   - the/this/that/these/those + noun chunk
   - plural-like root는 제외
   - compound/amod로 다른 명사를 수식하는 token은 제외

3. antecedent 후보가 앞에 나온 object mention이다.
   - max token distance: 90
   - person/structure/object role compatibility를 score에 반영
   - 첫 문장 subject와 첫 object를 discourse topic 후보로 가산
   - score >= 72, runner-up과 margin >= 14일 때만 resolve
```

resolve가 성공하면 새 object로 세지 않고 다음처럼 변환한다.

```text
object(The object) 제거
reference(The object) 생성
refers_to(reference, antecedent) 생성
기존 edge의 source/target을 antecedent로 alias rewrite
reference_object_by_token_i도 alias 반영
```

중요한 세부 결정:

```text
artifact/fragment/piece는 generic trigger로는 허용하지만,
antecedent 후보에서 generic placeholder로 penalize하지 않는다.
이유: case 57처럼 첫 문장의 artifact는 실제 object이고, 뒤의 The object가 그것을 가리킨다.

antecedent skip head는 object/thing/item/entity/individual/structure/figure처럼 placeholder 성격이 강한 head로 제한한다.
```

### 100개 eval shard 결과

입력:

```text
data/gpic_captions_eval/val/gpic_val_00000.jsonl.gz
```

갱신 파일:

```text
reports/raw_concepts_sample_100_trf_current.jsonl
reports/raw_concepts_sample_100_trf_current_summary.md
reports/case_detail_sample_100_trf_current.md
```

summary 변화:

```text
object: 644 -> 639
reference: 8 -> 13
refers_to edge: 8 -> 13
```

확인된 개선:

| case | 이전 문제 | 현재 결과 |
|---:|---|---|
| 38 | `The structure`가 object로 count됨 | `reference(The structure) -> building` |
| 49 | `The individual`이 object로 count됨 | `reference(The individual) -> person` |
| 57 | `The object`가 object로 count됨 | `reference(The object) -> artifact` |
| 73 | `the structure`가 object로 count됨 | `reference(the structure) -> building` |
| 80 | `The object`가 object로 count됨 | `reference(The object) -> slab` |

남은 한계:

```text
case 80의 마지막 it appears stationary는 아직 it -> edges로 resolve된다.
이건 generic definite NP 문제가 아니라 pronoun resolution에서 body/part noun보다 whole object를 선호해야 하는 selectional preference 문제다.
별도 이슈로 다루는 것이 맞다.
```