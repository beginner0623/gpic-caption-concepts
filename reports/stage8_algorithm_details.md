# Stage 8 Raw Concept Extractor Algorithm Details

- 기준일: 2026-06-25
- 구현 대상: caption text -> raw concept candidates
- 관련 코드:
  - `scripts\raw_concept_extractor.py`
  - `scripts\tag_list_parser.py`
  - `scripts\extract_raw_concepts.py`
  - `scripts\inspect_spacy_parse.py`
- 현재 범위: 8단계 raw extraction
- 아직 범위 밖: 9단계 canonicalization, 10단계 final scene graph construction

## 0. 전체 목적

이 단계의 목표는 spaCy가 만든 2~7단계 linguistic parse 결과를 그대로 저장하는 것이 아니라, 이후 count 가능한 schema로 변환하는 것이다.

즉 입력은 다음과 같다.

```text
caption
-> token
-> POS
-> lemma
-> dependency parse
-> noun chunks
```

출력은 다음과 같다.

```text
concept_mentions
edges
```

현재 extractor는 정답 scene graph를 만드는 것이 아니라, 9단계 canonicalization 전에 가능한 많은 정보를 잃지 않고 보존하는 raw candidate layer다.

## 1. 전체 처리 흐름

`scripts\extract_raw_concepts.py`는 GPIC caption JSONL을 읽고 각 caption마다 다음 순서로 처리한다.

```text
1. caption row 읽기
2. caption_id 추출
3. raw quote retokenization 적용 여부 확인
4. parsing에 사용할 parse_caption 생성
5. tag-list caption인지 판정
6. tag-list면 tag-list branch로 처리
7. 일반 문장이면 sentence branch로 처리
8. concept_mentions와 edges를 JSONL record로 저장
9. summary count table 생성
```

의사코드:

```python
nlp = spacy.load(model)
if mask_quotes:
    ensure_raw_quote_merger(nlp)

for row in caption_jsonl:
    caption = row["caption"]
    caption_id = row["key"]

    parse_caption = caption
    if mask_quotes:
        quote_mentions = collect_quoted_text(caption)
    else:
        quote_mentions = []

    if parse_tag_lists and is_tag_list_row(row, parse_caption):
        result = parse_tag_list(nlp, parse_caption)
        parse_path = "tag_list"
    else:
        doc = nlp(parse_caption)
        result = extract_raw_concepts(doc)
        parse_path = "sentence"

    write_jsonl({
        "caption": caption,
        "parse_caption": parse_caption,
        "parse_path": parse_path,
        "quote_mentions": quote_mentions,
        "concept_mentions": result.concept_mentions,
        "edges": result.edges,
    })
```

## 2. 출력 schema

### 2.1 ConceptMention

`ConceptMention`은 caption 안에서 발견된 concept 후보 1개다.

```json
{
  "mention_id": "m0",
  "concept_type": "object",
  "text": "flowers",
  "lemma": "flower",
  "source_tag": "chunk0",
  "source_token_i": 3,
  "role": "noun_chunk_root",
  "confidence": "high"
}
```

필드 의미:

| field | 의미 |
|---|---|
| `mention_id` | caption 내부 mention id |
| `concept_type` | `object`, `attribute`, `action`, `relation`, `context`, `quantity`, `negation` 등 |
| `text` | 원문 token/span text |
| `lemma` | lemma 기반 정규화 문자열 |
| `source_tag` | 어떤 source에서 나온 mention인지. 예: `chunk0`, `doc`, `t3` |
| `source_token_i` | spaCy token index. tag-list branch에서는 segment 내부 token index |
| `role` | 더 구체적인 역할. 예: `color_attribute`, `noun_chunk_root` |
| `confidence` | `high`, `medium`, `low` |

### 2.2 ConceptEdge

`ConceptEdge`는 mention 사이의 raw relation 후보 1개다.

```json
{
  "edge_id": "e1",
  "edge_type": "has_attribute",
  "source": "m0",
  "target": "m2",
  "confidence": "high",
  "evidence": "chunk0 compound -> flowers"
}
```

필드 의미:

| field | 의미 |
|---|---|
| `edge_id` | caption 내부 edge id |
| `edge_type` | `has_attribute`, `relation`, `agent`, `patient`, `has_context`, `has_quantity`, `negates` 등 |
| `source` | source mention id |
| `target` | target mention id |
| `confidence` | edge confidence |
| `evidence` | 어떤 rule/dependency에서 나왔는지 |

## 3. Sentence Branch 알고리즘

일반 문장 caption은 `scripts\raw_concept_extractor.py`의 `RawConceptExtractor`가 처리한다.

실행 순서:

```python
_extract_noun_chunk_objects()
_extract_contexts()
_extract_actions()
_extract_preposition_relations()
_extract_negations()
```

내부적으로 다음 map을 유지한다.

| map | 목적 |
|---|---|
| `object_by_token_i` | 같은 object token을 중복 mention으로 만들지 않기 |
| `action_by_token_i` | action mention과 verb token 연결 |
| `context_by_token_i` | context/spatial region 중복 방지 |

## 4. Noun Chunk -> Object / Attribute / Quantity

### 4.1 object 후보 생성

spaCy noun chunk를 순회한다.

```text
for chunk in doc.noun_chunks:
    root = chunk.root
```

root가 object POS로 보이면 object mention을 만든다.

현재 object 후보 POS:

```python
OBJECT_POS = {"NOUN", "PROPN", "PRON"}
```

또한 Penn tag 기준으로 `NN`, `NNS`, `NNP`, `NNPS`도 object 후보로 허용한다.

예시:

```text
Bright orange glass flowers
```

spaCy noun chunk:

```text
chunk = Bright orange glass flowers
root = flowers
```

raw concept:

```text
object: flowers / lemma flower / role noun_chunk_root
```

### 4.2 modifier 후보 생성

noun chunk 안에서 root가 아닌 token을 modifier 후보로 본다.

skip 하는 dependency:

```python
SKIP_MODIFIER_DEPS = {"det", "punct", "case", "cc", "mark"}
```

modifier로 볼 수 있는 조건:

```text
POS가 ADJ/ADV/NUM
또는 dep가 amod/compound/nummod/poss/acl/advmod
또는 color/material/size/visual lexicon에 있음
```

### 4.3 modifier role 분류

modifier token은 `_add_modifier()`에서 role이 정해진다.

우선순위:

```text
1. nummod 또는 NUM -> quantity
2. COLOR_WORDS 안에 있음 -> color_attribute
3. MATERIAL_WORDS 안에 있음 -> material_attribute
4. SIZE_WORDS 안에 있음 -> size_attribute
5. VISUAL_WORDS 안에 있음 -> visual_attribute
6. dep == compound -> compound_modifier
7. tag가 VBG/VBN -> state_attribute
8. 그 외 -> modifier_attribute
```

예시:

```text
Bright orange glass flowers
```

spaCy trf가 다음처럼 잘못 보더라도:

```text
orange = NOUN / compound
glass = NOUN / compound
flowers = NOUN / nsubj
```

8단계에서는 lexicon으로 재해석한다.

```text
flowers -> object
orange -> attribute / color_attribute
glass -> attribute / material_attribute
```

edge:

```text
flowers --has_attribute--> orange
flowers --has_attribute--> glass
```

## 5. POS를 그대로 믿지 않는 이유

현재 구현의 중요한 원칙은 다음이다.

```text
POS tag는 raw evidence일 뿐, 최종 concept type이 아니다.
```

예를 들어:

```text
blue jersey
```

spaCy가 lowercase `blue jersey`를 `PROPN`으로 보더라도, 8단계에서는 다음처럼 재해석할 수 있어야 한다.

```text
blue -> color_attribute
jersey -> object
```

현재 sentence branch에서는 color/material/size lexicon으로 modifier를 다시 분류한다.

tag-list branch는 아직 일부 role이 generic `attribute`로 남아 있어서, 다음 개선에서 sentence branch와 같은 lexicon role을 공유해야 한다.

## 6. Context Extraction

`_extract_contexts()`는 caption 안에서 scene-level context word를 찾는다.

현재 context lexicon은 `tag_list_parser.py`의 `CONTEXT_TAGS`를 공유한다.

예시:

```text
indoors
outdoors
background
foreground
day
night
```

출력:

```text
context: indoors
edge: scene --has_context--> indoors
```

주의:

현재 context는 object와 다르게 scene-level clue로 보존된다. 9단계에서 scene/environment concept으로 canonicalize할 수 있다.

## 7. Action Extraction

`_extract_actions()`는 verb predicate를 action mention으로 만든다.

조건:

```text
token.pos_ == VERB
token.dep_ != aux
token.dep_ != amod
```

`amod`를 제외하는 이유:

```text
quoted text
```

에서 `quoted`가 `VERB/VBN`으로 나오더라도 실제 action이라기보다 attribute이기 때문이다.

예시:

```text
A person sits at a table.
```

raw concept:

```text
action: sits / lemma sit
```

## 8. Agent / Patient Edge

action token의 child dependency를 보고 agent/patient를 연결한다.

subject dependency:

```python
SUBJECT_DEPS = {"nsubj", "nsubjpass"}
```

object dependency:

```python
OBJECT_DEPS = {"dobj", "obj", "attr", "oprd", "pobj"}
```

예시:

```text
One person holds a red snack bag.
```

spaCy dependency:

```text
person --nsubj--> holds
bag --dobj--> holds
```

raw edge:

```text
hold --agent--> person
hold --patient--> bag
```

### 8.1 Conjunct target expansion

dependency parse에서 subject/object/relation target이 coordination을 가질 수 있다.

예시:

```text
filled with groceries and bags
```

spaCy 구조:

```text
groceries --pobj--> with
bags --conj--> groceries
```

기존 규칙은 `groceries`에만 relation edge를 만들 수 있었다. 현재 구현은 target token에서 `conj` child를 재귀적으로 확장한다.

```text
targets = [groceries, bags]
```

출력:

```text
cart --with--> groceries
cart --with--> bags
```

같은 확장은 action의 subject/object target에도 적용된다.

## 9. Preposition / Spatial Relation Extraction

`_extract_preposition_relations()`는 전치사 기반 relation edge를 만든다.

기본 구조:

```text
source --relation--> target
```

예시:

```text
person with dreadlocks
```

edge:

```text
person --with--> dreadlocks
```

예시:

```text
flowers stand in a garden bed
```

edge:

```text
flowers --in--> bed
```

현재 relation은 `edge_type = relation`, 실제 relation 이름은 `evidence`에 저장한다.

```json
{
  "edge_type": "relation",
  "source": "m0",
  "target": "m4",
  "evidence": "in"
}
```

## 10. Multi-word Relation 처리

`in front of`, `on top of`, `at top of`, `from side of` 같은 relation은 spaCy가 보통 여러 token으로 쪼갠다.

예시:

```text
woman speaking in front of an audience
```

spaCy는 대략 다음처럼 본다.

```text
speaking -> in -> front -> of -> audience
```

그대로 쓰면 `front`가 object로 잡히거나 relation이 `in`, `of`로 쪼개진다.

현재 구현은 다음 패턴을 탐지한다.

```text
ADP + {top, front, back, side, middle, center, edge} + of
```

그리고 relation 이름을 하나로 합친다.

```text
in_front_of
at_top_of
from_side_of
```

예시 출력:

```text
woman --in_front_of--> audience
```

추가로 `front`, `top` 같은 중간 token은 object mention으로 세지 않도록 한다.

## 11. Spatial Region 처리

가끔 `in front`처럼 `of 대상`이 생략된다.

예시:

```text
A sedan is parked in front.
```

이때 `front`를 object로 세면 이상하다.

현재 구현은 이런 경우:

```text
front -> context / spatial_region
```

으로 보존한다.

edge:

```text
sedan --in--> front
```

여기서 `front`는 object가 아니라 spatial region context다.

## 12. Negation 처리

`_extract_negations()`는 dependency label이 `neg`인 token을 찾는다.

예시:

```text
not standing
no people
```

현재 규칙:

```text
neg token의 head가 action이면 action에 negates edge
neg token의 head가 object이면 object에 negates edge
```

출력:

```text
negation: not
edge: not --negates--> standing
```

현재 100개 샘플에서는 negation이 주요하게 나타나지 않았지만, schema는 들어가 있다.

## 13. Tag-list Branch 알고리즘

tag-list caption은 일반 문장처럼 dependency parse하면 구조가 쉽게 망가진다.

예시:

```text
roller skaters, helmet, referee, court, blue jersey
```

그래서 `parse_tag_list()`에서 별도 처리한다.

### 13.1 tag-list 판정

`is_tag_list_row()` 기준:

```text
1. row["caption_type"] == "tag"이면 tag-list
2. 또는 comma가 2개 이상이고 .!? 문장부호가 없으면 tag-list-like
```

### 13.2 segment 분리

쉼표 기준으로 segment를 나눈다.

```text
t0 = roller skaters
t1 = helmet
t2 = referee
t3 = court
t4 = blue jersey
```

각 segment는 독립적으로 spaCy parse한다.

### 13.3 segment별 concept 생성

규칙:

```text
context lexicon에 있으면 context
단일 ADJ/VBN/VBG이면 floating attribute
noun/proper noun이 있으면 마지막 noun을 object head
head 앞 modifier는 attribute
```

예시:

```text
blue jersey
```

출력:

```text
object: jersey
attribute: blue
edge: jersey --has_attribute--> blue
```

예시:

```text
indoor
```

출력:

```text
context: indoor
edge: scene --has_context--> indoor
```

예시:

```text
large
```

출력:

```text
attribute: large / floating_attribute / medium
edge: previous_object --candidate_has_attribute--> large / low
```

### 13.4 tag-list POS raw/norm 분리

tag-list caption은 문장이 아니라 label 나열이므로 spaCy POS가 특히 흔들린다.

예시:

```text
blue jersey
```

spaCy trf raw:

```text
blue   -> PROPN / NNP
jersey -> PROPN / NNP
```

현재 tag-list token output은 원본과 보정값을 함께 저장한다.

```text
blue   -> pos_raw=PROPN, pos_norm=ADJ,  tag_raw=NNP, tag_norm=JJ
jersey -> pos_raw=PROPN, pos_norm=NOUN, tag_raw=NNP, tag_norm=NN
```

이렇게 하는 이유:

```text
pos_raw는 모델 오류 분석용으로 보존
pos_norm은 downstream rule/schema 판단용으로 사용 가능
```

아직 concept role 자체는 tag-list branch에서 일부 generic `attribute`로 남아 있다. 다음 개선에서 sentence branch의 color/material/size role 분류와 공유해야 한다.

## 14. Raw Quote Retokenization과의 연결

raw quote retokenization은 8단계 자체는 아니지만, 8단계 전에 parse를 안정화하는 전처리다.
quote를 `the quoted text` 같은 placeholder로 바꾸지 않고, 원문 `"..."` span 자체를 tokenizer 직후 하나의 token으로 merge한다.

예시:

```text
A screen shows the text "Closing the Access Divide."
```

retokenization 후 parser 입력:

```text
A screen shows the text "Closing the Access Divide."
```

merged token:

```text
"Closing the Access Divide."
```

원본 quote는 `quote_mentions`에 따로 저장된다.

이렇게 하는 이유:

```text
quote 내부 title/text가 여러 단어와 문장부호로 쪼개져 object/action/relation 후보를 오염시키는 것을 막기 위해서
```

8단계 raw extraction에서는 merged quote token이 object처럼 남을 수 있지만, 9단계에서는 이를 일반 object로 세지 않고 `TEXT_SPAN(qid)` 또는 `LABEL_VALUE(qid)`로 canonicalize해야 한다.

## 15. 현재 confidence 정책

현재 confidence는 대략 다음처럼 둔다.

| confidence | 의미 |
|---|---|
| `high` | 비교적 직접적인 lexical/dependency 근거가 있음 |
| `medium` | 정보는 유용하지만 semantic role이 불확실함 |
| `low` | 후보 관계로만 보존해야 함 |

예시:

```text
red -> color_attribute -> high
glass -> material_attribute -> high
shopping -> compound_modifier -> medium
large in tag-list -> floating_attribute -> medium
candidate_has_attribute -> low
```

## 16. 현재 100개 샘플 결과

`reports\raw_concepts_sample_100_trf_summary.md` 기준:

Concept type count:

| type | count |
|---|---:|
| `object` | 731 |
| `attribute` | 471 |
| `action` | 209 |
| `context` | 49 |
| `quantity` | 16 |

Edge count:

| edge | count |
|---|---:|
| `has_attribute` | 466 |
| `relation` | 333 |
| `agent` | 158 |
| `patient` | 83 |
| `has_context` | 38 |
| `has_quantity` | 16 |
| `candidate_has_attribute` | 5 |

주요 relation evidence:

| relation | count |
|---|---:|
| `with` | 86 |
| `in` | 69 |
| `on` | 42 |
| `near` | 16 |
| `of` | 15 |
| `under` | 14 |
| `at` | 10 |
| `behind` | 8 |
| `in_front_of` | 4 |

## 17. 현재 한계

### 17.1 compound modifier가 너무 넓다

현재 `compound`는 기본적으로 attribute로 보존한다.

예:

```text
shopping cart
soccer ball
power line
music stand
trash can
```

하지만 일부는 object phrase 자체다.

```text
shopping cart -> object phrase
soccer ball -> object phrase
trash can -> object phrase
```

반면 일부는 material/part/domain attribute에 가깝다.

```text
glass wall -> material/object modifier
brick wall -> material/object modifier
```

따라서 다음 단계에서 object MWE / compound role classifier가 필요하다.

### 17.2 tag-list branch와 sentence branch의 role 체계가 아직 다르다

sentence branch:

```text
blue -> color_attribute
glass -> material_attribute
```

tag-list branch:

```text
blue -> pos_raw=PROPN, pos_norm=ADJ, concept role=attribute
glass -> pos_raw=NOUN, pos_norm=NOUN, concept role=attribute
```

POS raw/norm은 분리했지만, concept role은 아직 sentence branch의 `color_attribute`, `material_attribute`와 완전히 공유하지 않는다. 다음 개선에서 lexicon role 함수를 공유해야 한다.

### 17.3 pronoun 처리

현재는 `her`, `it`도 object mention으로 남는다.

장점:

```text
relation target을 잃지 않는다.
```

단점:

```text
count table에서 object로 세면 노이즈가 된다.
```

다음에 pronoun policy가 필요하다.

가능한 정책:

```text
1. pronoun을 object로 유지하되 role=pronoun_object
2. 별도 concept_type=pronoun으로 분리
3. coreference를 하지 않으면 aggregate count에서 제외
```

### 17.4 inclusion 표현

`including`이 action과 relation 양쪽에 잡힐 수 있다.

예:

```text
objects including cars
```

현재는 dependency에 따라 `include` relation evidence가 나올 수 있다.

다음 정책:

```text
including -> includes relation
또는 action에서 제외
```

### 17.5 dependency 오류 전파

spaCy dependency가 틀리면 8단계 relation도 틀릴 수 있다.

예:

```text
wrong attachment
ellipsis
coordination error
```

현재 extractor는 이를 완전히 고치지 않는다. 대신 confidence와 candidate edge로 일부 uncertainty를 남기는 방향이다.

## 18. 다음 구현 우선순위

가장 먼저 할 일:

```text
object MWE / compound role classifier
```

이유:

```text
현재 100개 샘플에서도 compound_modifier가 65개로 많이 나온다.
이 중 일부는 attribute가 아니라 object phrase 자체다.
```

그 다음:

```text
1. sentence/tag-list branch의 modifier role 함수 통합
2. pronoun policy 추가
3. including/include 처리
4. 500개 샘플로 재평가
5. 9단계 canonicalization 설계
```

## 19. 요약

현재 구현은 다음을 수행한다.

```text
caption
-> spaCy parse
-> noun chunk root에서 object 추출
-> modifier에서 attribute/quantity 추출
-> verb에서 action 추출
-> subject/object dependency에서 agent/patient edge 추출
-> preposition에서 relation edge 추출
-> in front of 같은 multi-word relation 복원
-> context word 추출
-> tag-list caption은 별도 branch로 segment-level extraction
-> JSONL로 raw concept 후보 저장
```

아직 최종 concept graph는 아니지만, 100M caption을 countable schema로 만들기 위한 8단계 raw extraction의 기본 골격은 이 문서의 알고리즘으로 구현되어 있다.
