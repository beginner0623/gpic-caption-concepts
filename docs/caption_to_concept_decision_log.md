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
