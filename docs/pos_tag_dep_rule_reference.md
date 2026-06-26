# POS / Tag / Dependency Rule Reference

Last updated: 2026-06-26 KST

이 문서는 현재 `gpic-caption-concepts` 코드에서 실제로 쓰는 `POS`, `tag`, `dep` 조건을 표로 정리한 reference다.

핵심 구분:

```text
spaCy가 하는 일:
  tokenization, POS tagging, fine tag, dependency parsing, noun chunking

우리 rule이 하는 일:
  spaCy 결과를 읽어서 object / attribute / action / relation / context / recovered object를 만든다.
```

즉 대부분의 조건은 POS/tag/dep를 새로 예측하는 것이 아니라, spaCy가 이미 만든 값을 읽어서 Stage 8 schema로 옮기는 규칙이다.

---

## 1. 용어

| 용어 | 예시 | 누가 만듦 | 의미 | 코드에서 쓰는 방식 |
|---|---|---|---|---|
| `POS` | `NOUN`, `VERB`, `ADP`, `SCONJ` | spaCy | coarse POS, 큰 품사 | object/action/relation 후보 필터 |
| `tag` | `NN`, `NNS`, `VBN`, `IN`, `UH` | spaCy | fine-grained Penn Treebank tag | POS가 애매할 때 보조 판단 |
| `dep` | `nsubj`, `pobj`, `amod`, `prep`, `mark` | spaCy dependency parser | token이 head와 맺는 syntactic relation | edge 생성, modifier 판단, recovery 판단 |
| `noun_chunks` | `red curtains`, `a blue lake` | spaCy noun chunk iterator | dependency 결과 위에서 만든 명사구 span | 기본 object 추출 source |
| `pos_norm`, `tag_norm` | `INTJ/UH -> NOUN/NN` | 우리 rule, tag-list branch만 | tag-list 전용 normalized POS/tag | tag-list schema 판단용 |

---

## 2. Sentence Branch: `raw_concept_extractor.py`

일반 문장형 caption은 `scripts/raw_concept_extractor.py`의 `RawConceptExtractor`가 처리한다.

### 2.1 Global Sets

| set 이름 | 값 | 쓰는 곳 | 의미 |
|---|---|---|---|
| `OBJECT_POS` | `NOUN`, `PROPN`, `PRON` | noun chunk object, relation source/target | object로 볼 수 있는 coarse POS |
| object fallback tags | `NN`, `NNS`, `NNP`, `NNPS` | noun chunk root, `_object_for_token`, with recovery | POS가 틀려도 noun tag면 object 후보 |
| `ACTION_POS` | `VERB` | action extraction | action predicate 후보 |
| `MODIFIER_DEPS` | `amod`, `compound`, `nummod`, `poss`, `acl`, `advmod` | `_looks_like_modifier()` | object에 붙는 modifier 후보 |
| `SUBJECT_DEPS` | `nsubj`, `nsubjpass` | action agent edge | verb의 주어 |
| `OBJECT_DEPS` | `dobj`, `obj`, `attr`, `oprd`, `pobj` | action patient edge | verb의 object/patient 후보 |
| `SKIP_MODIFIER_DEPS` | `det`, `punct`, `case`, `cc`, `mark` | modifier extraction | determiner, punctuation, conjunction 등은 attribute로 만들지 않음 |
| `MULTIWORD_RELATION_MIDS` | `top`, `front`, `back`, `side`, `middle`, `center`, `edge` | `on top of`, `in front of` 처리 | multi-word relation 중간 명사 |

### 2.2 Basic Object Extraction

| 단계 | 조건 | 통과하면 | 실패하면 | 보수적인 이유 |
|---|---|---|---|---|
| noun chunk root 확인 | `root.pos_ in OBJECT_POS` 또는 `root.tag_ in {NN,NNS,NNP,NNPS}` | object mention 생성 | 해당 chunk skip | noun chunk 전체가 아니라 root가 noun-like일 때만 object |
| multi-word relation 중간 token 제외 | `top/front/...`가 ADP 아래 있고 `of` prep child가 있음 | object가 아니라 relation middle로 제외 | 계속 진행 | `top`을 object로 세지 않기 위함 |
| spatial region anchor 처리 | `top/front/...`가 ADP 아래 있음 | context `spatial_region`으로 저장 | 계속 진행 | `front`, `back` 같은 공간 anchor를 물체로 세지 않음 |
| lowercase PROPN 보정 | `token.pos_ == PROPN` and `token.text.islower()` | role=`lowercase_propn_as_object`, confidence=`medium` | 일반 object | `blue jersey` 같은 lowercase PROPN 오인 완화 |

### 2.3 Noun Chunk Modifier to Attribute

| 조건 | 처리 | 예시 | 비고 |
|---|---|---|---|
| token이 chunk root와 같음 | skip | `curtains` in `red curtains` | root는 object |
| `token.dep_ in SKIP_MODIFIER_DEPS` | skip | `a`, `the`, `and` | function word 제외 |
| `token.pos_ in {ADJ, ADV, NUM}` | modifier 후보 | `red`, `large`, `two` | `_looks_like_modifier()` |
| `token.dep_ in MODIFIER_DEPS` | modifier 후보 | `compound`, `amod`, `nummod` | noun compound도 attribute 후보 |
| lemma가 color/material/size/visual lexicon에 있음 | modifier 후보 | `blue`, `wooden`, `large` | POS가 흔들려도 lexicon으로 보완 |

### 2.4 Modifier Role Mapping

| 조건 | concept type | role | edge | confidence |
|---|---|---|---|---|
| `token.dep_ == nummod` 또는 `token.pos_ == NUM` | `quantity` | `quantity` | `has_quantity` | high |
| lemma in `COLOR_WORDS` | `attribute` | `color_attribute` | `has_attribute` | high |
| lemma in `MATERIAL_WORDS` | `attribute` | `material_attribute` | `has_attribute` | high |
| lemma in `SIZE_WORDS` | `attribute` | `size_attribute` | `has_attribute` | high |
| lemma in `VISUAL_WORDS` | `attribute` | `visual_attribute` | `has_attribute` | medium |
| `token.dep_ == compound` | `attribute` | `compound_modifier` | `has_attribute` | medium |
| `token.tag_ in {VBG, VBN}` | `attribute` | `state_attribute` | `has_attribute` | medium |
| 나머지 modifier | `attribute` | `modifier_attribute` | `has_attribute` | medium |

### 2.5 Context Extraction

| 조건 | 처리 | 예시 |
|---|---|---|
| `token.lemma_.lower() in CONTEXT_TAGS` | context mention 생성, `scene --has_context--> context` | `indoor`, `background`, `outdoor` |
| 이미 context로 등록된 token | skip | 중복 방지 |

### 2.6 Action Extraction

| 조건 | 처리 | 예시 |
|---|---|---|
| `token.pos_ in ACTION_POS` | action mention 후보 | `run`, `stand`, `kick` |
| `token.dep_ in {aux, amod}` | action에서 제외 | auxiliary, modifier verb 제외 |
| child `dep in SUBJECT_DEPS` | `action --agent--> object` | `man stands` |
| child `dep in OBJECT_DEPS` | `action --patient--> object` | `kick ball` |
| subject/object child가 `conj`를 가짐 | conjunct target도 확장 | `man and woman stand` |

### 2.7 Relation Extraction

| 조건 | 처리 | 예시 | 비고 |
|---|---|---|---|
| token이 relation cue | `token.pos_ == ADP` 또는 `token.dep_ == prep` | `on`, `in`, `behind` | ADP가 아니어도 dep이 prep이면 사용 |
| prep child `dep in {pobj, pcomp}` | relation target 후보 | `on table`의 `table` | `_preposition_object()` |
| relation source가 verb/action | verb subject를 source로 선택 | `man stands on field` | `man --on--> field` |
| relation source가 object | object를 source로 선택 | `man with hat` | `man --with--> hat` |
| target이 `conj`를 가짐 | target 확장 | `walls and beams` | 같은 relation을 conj target에도 적용 |
| relation in `SPATIAL_RELATIONS` 또는 relation에 `_` 포함 | confidence high | `on`, `in_front_of` | 나머지는 medium |

### 2.8 Multi-word Relation

| 패턴 | 조건 | 결과 |
|---|---|---|
| `on top of`류 outer prep | prep child lemma가 `top/front/...`이고 그 child에 `of` prep이 있음 | outer prep은 skip, inner `of`에서 relation 생성 |
| inner `of` prep | `of`의 head가 `top/front/...`, 그 head의 head가 ADP | relation name을 `on_top_of`처럼 생성 |
| middle token object 방지 | middle token이 `top/front/...`이고 ADP 아래 있으며 `of` child가 있음 | object로 세지 않음 |

### 2.9 Negation

| 조건 | 처리 | 예시 |
|---|---|---|
| `token.dep_ == neg` | negation mention 생성 | `not`, `n't` |
| neg head가 action/object로 이미 등록됨 | `negation --negates--> target` | `not standing` |
| target을 못 찾음 | skip | 과잉 negation 방지 |

---

## 3. With-absolute Recovery

이 부분은 noun chunk 누락을 보정하기 위한 Stage 8 후처리다.
spaCy POS/dependency/noun chunk를 다시 돌리지 않고, 이미 생성된 값을 읽는다.

### 3.1 With Cue 조건

| 조건 | 값 | 이유 |
|---|---|---|
| surface | `token.lower_ == "with"` | with 구문만 대상 |
| fine tag | `token.tag_ == "IN"` | preposition/subordinator 계열 |
| dependency | `token.dep_ == "mark"` | 일반 `with a hat`이 아니라 with-absolute 계열만 대상 |

일반 `with a hat`, `with large windows`는 보통 `ADP/prep`로 잡히므로 이 recovery가 작동하지 않는다.

### 3.2 Candidate Object 조건

| 조건 | 허용값 | 제외값 | 이유 |
|---|---|---|---|
| 위치 | with 뒤쪽 같은 sentence 안 | sentence 밖 | local recovery만 허용 |
| 기존 object 여부 | 기존 object가 아니어야 함 | 이미 noun chunk root로 잡힌 token | 중복 방지 |
| 기존 context 여부 | 기존 context가 아니어야 함 | `background`, `foreground` 등 | context를 object로 중복 생성하지 않음 |
| dep 허용 | `advcl`, `conj`, `dep`, `nsubj`, `nsubjpass` | 그 외 | 문제 case에서 noun head가 나타난 dep만 허용 |
| dep 제외 | 제외 set에 없어야 함 | `amod`, `compound`, `poss`, `det`, `cc`, `punct`, `case`, `mark` | modifier/function word를 object로 만들지 않음 |
| POS/tag | `NOUN`, `PROPN` 또는 `NN`, `NNS`, `NNP`, `NNPS` | `PRON`, `ADJ`, `ADV`, `VERB` 등 | pronoun/attribute/action을 object로 오인하지 않음 |
| relation middle | 아니어야 함 | `top/front/...` relation middle | `top` 같은 공간 anchor 제외 |

### 3.3 Recovery Output

| 생성물 | 값 |
|---|---|
| concept type | `object` |
| role | `with_absolute_recovered_object` |
| confidence | `medium` |
| source tag | `with_absolute{with_token_i}` |
| edge | `scene --scene_contains--> recovered_object` |
| edge confidence | `medium` |

`scene_contains`로 약하게 붙이는 이유는 `helicopter --with--> mountains` 같은 강한 relation을 만들지 않기 위해서다.

### 3.4 Recovered Object Modifier 조건

| 조건 | 처리 | 이유 |
|---|---|---|
| modifier dep in `amod`, `compound`, `nummod`, `poss`, `acl` | attribute 후보 | noun에 직접 붙는 modifier만 허용 |
| modifier dep in `advmod` | 제외 | `above -> trees` 같은 부작용 방지 |
| modifier가 `_looks_like_modifier()` 통과 | `_add_modifier()`로 role mapping | 기존 attribute logic 재사용 |

### 3.5 문제 케이스 결과

| case | 기존 누락 | recovery 결과 |
|---|---|---|
| 29 | `mountains`가 noun chunk에서 빠짐 | `mountains` 회수, `snow-capped -> mountains` |
| 42 | `workers`, `equipment`가 noun chunk에서 빠짐 | `workers`, `equipment` 회수 |
| 43 | `trees`, `sky`가 noun chunk에서 빠짐 | `trees`, `sky` 회수, `overcast -> sky` |

### 3.6 정상 케이스 regression

아래 기존 정상 케이스에서는 추가 recovery가 0개였다.

| case | 이미 잡힌 object | recovery 추가 |
|---|---|---|
| 16 | `red curtains`, `blue chairs` | 0 |
| 27 | `wires`, `switches` | 0 |
| 37 | `houses` | 0 |
| 40 | `trees`, `other buildings` | 0 |
| 49 | `grass`, `sunlight` | 0 |
| 67 | `spectators`, `tents` | 0 |
| 77 | `ceiling`, `ventilation ducts` | 0 |
| 97 | `hillside` | 0 |

---

## 4. Tag-list Branch: `tag_list_parser.py`

tag-list caption은 문장이 아니라 comma-separated segment에 가깝기 때문에 sentence branch와 별도로 처리한다.

### 4.1 Tag-list Global Sets

| set 이름 | 값 | 쓰는 곳 | 의미 |
|---|---|---|---|
| `ATTRIBUTE_POS` | `ADJ`, `ADV` | floating attribute, modifier | tag-list에서 독립 attribute 후보 |
| `OBJECT_POS` | `NOUN`, `PROPN`, `PRON` | segment head | tag-list object head 후보 |
| `MODIFIER_DEPS` | `amod`, `compound`, `nummod`, `poss`, `acl` | segment modifier | object head에 붙는 modifier |
| `CONTEXT_TAGS` | `indoor`, `outdoor`, `background`, ... | context segment | scene context |
| `PERSON_OBJECT_WORDS` | `man`, `woman`, `people`, `child`, ... | single person segment override | `man`이 `INTJ/UH`로 잡혀도 object로 보정 |

### 4.2 Object Head Selection

| 우선순위 | 조건 | 결과 | 비고 |
|---:|---|---|---|
| 1 | single-token segment가 person lexicon에 있음 | 그 token을 head로 선택 | `man` tag-list 문제 해결 |
| 2 | segment 안에 `pos_ in OBJECT_POS` token 있음 | 마지막 noun-like token을 head로 선택 | `blue shirt`의 `shirt` |
| 3 | root가 `pos_ in OBJECT_POS` | root 선택 | 일반 segment |
| 4 | single-token이고 root tag가 `JJ/JJR/JJS/VBN`이 아님 | root 선택 | ambiguous segment fallback |
| 5 | 위 조건 없음 | unknown 처리 가능 | low confidence |

### 4.3 `pos_norm` / `tag_norm`

| 조건 | pos_norm/tag_norm | 이유 |
|---|---|---|
| head이고 person override | `NOUN/NN` 또는 plural이면 `NOUN/NNS` | tag-list의 단독 `man`, `men` 보정 |
| lemma in color/size words | `ADJ/JJ` | `blue`, `large`는 attribute로 보기 위함 |
| lowercase `PROPN` | head면 `NOUN/NN`, 아니면 `ADJ/JJ` | `blue jersey`류 PROPN 오인 완화 |
| `pos_ in {VERB,AUX}` and `tag_ in {VBN,VBG}` and not head | `ADJ/VBN` 또는 `ADJ/VBG` | participle modifier 보정 |
| 나머지 | spaCy raw POS/tag 유지 | 과잉 보정 방지 |

`pos_raw/tag_raw`는 항상 저장한다.
`pos_norm/tag_norm`은 tag-list branch의 downstream 판단용이다.

### 4.4 Context Segment

| 조건 | 처리 |
|---|---|
| segment norm in `CONTEXT_TAGS` | context mention |
| single-token lemma in `CONTEXT_TAGS` | context mention |

### 4.5 Floating Attribute

| 조건 | 처리 | 예시 |
|---|---|---|
| segment 길이 1 | floating attribute 검사 | `large`, `indoor` |
| token.pos in `ADJ/ADV` | attribute | `large` |
| token.tag in `JJ/JJR/JJS/VBN` | attribute | `arched`, `rusted` |
| token.tag == `VBG` and lemma/text in state words | state attribute | `standing`, `sitting` |
| 이전 object가 있음 | `candidate_has_attribute` low edge | nearby segment에 약하게 연결 |

### 4.6 Segment Modifier

| 조건 | modifier 후보 |
|---|---|
| `token.head == head` and `token.dep_ in MODIFIER_DEPS` | yes |
| `token.head == head` and `token.pos_ in ATTRIBUTE_POS` | yes |
| `token.i < head.i` and `token.pos_ in {ADJ,NOUN,PROPN,NUM,VERB}` | yes |

modifier가 `tag in {VBG,VBN}`이면 role은 `state_attribute`, 아니면 일반 `attribute`다.

---

## 5. Retokenizer / POS Override Components

### 5.1 Object MWE POS Corrector

| 조건 | 처리 | 이유 |
|---|---|---|
| token extension `is_object_mwe == True` | `pos = NOUN`, `tag = NN`, lemma = canonical | `trash can`, `music stands`, `soccer ball` 같은 object MWE가 ADJ/VERB로 흐르는 것 방지 |
| 일반 token | 아무것도 안 함 | MWE lexicon precision에만 의존 |

이 컴포넌트는 parser 전에 들어간다.
따라서 object MWE token은 parser가 보기 전에 noun-like token으로 보정된다.

### 5.2 Hyphen Span Merger

hyphen span merger는 POS/tag/dep 조건을 쓰지 않는다.
텍스트 형태만 본다.

| 조건 | 처리 |
|---|---|
| alphabetic-ish token들이 plain hyphen으로 연결 | span merge |
| 숫자-only part가 포함됨 | merge 안 함 |

예:

```text
snow-capped -> single token
black-and-white -> single token
2007-06-09 -> not merged
```

---

## 6. "보수적"이라는 말의 정확한 뜻

| 원칙 | 실제 구현 |
|---|---|
| raw parse를 고치지 않는다 | spaCy POS/tag/dep/noun_chunks는 그대로 둔다 |
| 이미 잡힌 object는 건드리지 않는다 | `object_by_token_i`, noun chunk root와 중복되면 skip |
| branch를 좁힌다 | with recovery는 `with/IN/mark`에서만 작동 |
| pronoun을 object로 회수하지 않는다 | with recovery candidate POS는 `NOUN/PROPN` 또는 noun tag만 허용 |
| modifier를 object로 회수하지 않는다 | `compound`, `amod`, `poss`, `det`, `cc` 등 제외 |
| relation을 강하게 만들지 않는다 | recovered object는 `scene_contains` medium edge |
| 부사성 modifier를 붙이지 않는다 | with recovery modifier에서 `advmod` 제외 |
| source를 남긴다 | `source_tag = with_absolute{token_i}` |
| confidence를 낮춘다 | recovered object는 `medium` |

---

## 7. 한 줄 요약

현재 코드는 이렇게 나뉜다.

| 층위 | 누가 함 | 설명 |
|---|---|---|
| POS/tag/dep 예측 | spaCy | 학습 기반 parser/tagger |
| noun chunk 생성 | spaCy | dependency 기반 noun chunk iterator |
| object/action/relation/attribute 생성 | 우리 Stage 8 rule | spaCy 결과를 schema로 변환 |
| tag-list POS 보정 | 우리 tag-list rule | `pos_raw`는 보존하고 `pos_norm`만 보정 |
| object MWE POS 보정 | 우리 retokenizer component | lexicon 기반 MWE token만 `NOUN/NN`으로 보정 |
| with-absolute 누락 object 회수 | 우리 Stage 8 rule | noun chunk에서 빠진 noun-like token만 보수적으로 복구 |

