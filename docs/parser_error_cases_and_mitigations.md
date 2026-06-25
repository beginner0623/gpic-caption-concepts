# Parser Error Cases and Mitigations

이 문서는 GPIC caption을 spaCy 기반 pipeline으로 처리할 때 관측되는 오류와 대응 전략을 계속 누적하기 위한 작업 로그다.

목표는 spaCy parser output을 그대로 믿는 것이 아니라, 어떤 오류가 어떤 단계에서 생기는지 분리하고, 8단계 raw tuple extraction 전에 어떤 보정이 필요한지 명시하는 것이다.

## 현재 Pipeline 기준

```text
1. noise 제거
2. tokenization
3. POS tagging
4. lemmatization
5. dependency parsing
6. noun chunking
7. raw tuple extraction + repair rules
8. canonicalization
9. graph/count table 구축
```

중요한 분리:

```text
object MWE
  trash can, music stand, traffic light
  -> parser 전에 merge하는 대책 후보였지만, 현재 모델 비교 단계에서는 비활성화

relation MWE
  in front of, on top of, next to
  -> parser 전에 merge하지 않고 span만 기록하는 쪽이 안전

attribute + object phrase
  wooden door, red bow, blue jersey
  -> merge하지 말고 attribute(object, attr)로 남기는 것이 보통 더 좋음
```

## 에러 유형 Taxonomy

| 코드 | 유형 | 주로 생기는 단계 | 핵심 대책 |
|---|---|---|---|
| `MWE_OBJECT_POS` | multi-word object가 깨지며 POS 오분류 | 3, 4, 6 | object MWE pre-merge |
| `RELATION_MWE` | multi-word relation이 여러 token으로 흩어짐 | 6, 8 | relation span detect 후 8단계에서 relation label로 사용 |
| `COORD_ATTACH` | coordination attachment 오류 | 6, 7, 8 | coordination split/reattach rule |
| `PARTICIPLE_ATTACH` | participle/acl attachment 오류 | 6, 8 | animate subject/action repair |
| `TAG_LIST` | comma-separated tag caption을 문장처럼 parsing | 0, 6, 7 | caption type classifier + tag-list parser |
| `VBN_ADJ` | 과거분사형 adjective를 verb로 오분류 | 4, 6, 8 | VBN adjective repair |
| `ELLIPSIS` | 생략 구문 복원 실패 | 6, 8 | local ellipsis pattern repair |
| `TEXT_MENTION` | 따옴표/간판/스크린 텍스트 처리 실패 | 1, 8 | quoted text extractor + text_mention tuple |
| `ROOT_FAILURE` | 문장 root/head 구조 자체가 잘못 잡힘 | 6, 8 | fallback SVO/root repair |
| `ADV_CONTEXT` | 장소/상태 부사를 object처럼 처리 | 4, 6, 8 | context/location predicate로 분리 |
| `HYPHEN_ADJ` | hyphenated adjective가 이상하게 분리됨 | 1, 4, 8 | hyphenated adjective normalization |

## 20개 샘플에서 보이는 핵심 패턴

현재 20개 샘플에서 반복적으로 보이는 실패 패턴은 크게 네 가지다.

### 1. 복합명사 오인

예:

```text
trash can
music stands
```

문제:

```text
trash can -> can을 조동사로 오인
music stands -> stands를 동사로 오인
```

해석:

이 유형은 POS tagging이 먼저 틀리고, 그 오류가 dependency parsing과 noun chunking으로 전파된다. 따라서 dependency parsing 이후에 고치기보다 parser 전에 high-confidence object MWE를 merge하는 것이 효과적이다.

대책:

```text
object MWE pre-merge
  trash can
  music stand / music stands
  hot dog
  traffic light
  fire hydrant
```

### 2. 쉼표 나열형 tag-list caption

예:

```text
06. smiling couple, formal party, british flags, chandelier, wine glasses
10. roller skaters, helmet, referee, court, blue jersey
14. brown boot, indoor, brick wall, display, large
17. glass wall, worker, sidewalk, building, reflection, grass
```

문제:

이런 caption은 문장이라기보다 keyword/tag list에 가깝다. 이 경우 dependency의 `dep`, `head`, `conj`, `appos` 구조를 의미 relation으로 해석하면 안 된다.

대책:

```text
caption type classifier
  -> tag-list-like 감지

tag-list parser
  -> comma segment 단위로 object/attribute/context 후보 추출
```

### 3. 병렬 구조 오류

예:

```text
dreadlocks and a red bow
a gray roof and arched windows
a vest and red scarf
```

문제:

spaCy가 coordination scope를 잘못 잡거나, 두 개의 병렬 object를 하나의 noun chunk로 뭉개는 경우가 있다.

대책:

```text
coordination split/reattach rule
  with A and B
  NOUN and ADJ NOUN
  object1 and object2
```

목표 output:

```text
relation(person, with, dreadlocks)
relation(person, with, bow)
attribute(bow, red)

object(roof)
attribute(roof, gray)
object(window)
attribute(window, arched)

object(vest)
object(scarf)
attribute(scarf, red)
```

### 4. 생략구문/제목/따옴표 처리 약함

예:

```text
the other a yellow shirt
"Closing the Access Divide"
"BANG GOES THE KNIGHTHOOD"
```

문제:

문장 생략은 parser가 원래 복원하기 어렵고, 따옴표 안의 텍스트는 실제 scene action/relation이 아니라 written text인데도 일반 token처럼 dependency에 섞인다.

대책:

```text
ellipsis repair
  one wears X, the other Y

text mention extractor
  screen shows "..."
  poster reads "..."
  sign says "..."
```

목표 output:

```text
relation(other_person, wear, yellow shirt)
text_mention(screen, "Closing the Access Divide")
text_mention(poster, "BANG GOES THE KNIGHTHOOD")
```

### 보조 패턴: root/participle attachment 실패

예:

```text
woman ... speaking
road ... runs
```

문제:

일부 문장에서 핵심 action의 subject나 root가 잘못 잡힌다. 이 유형은 완전히 자동 복구하기 어렵지만, caption domain에서 자주 나오는 패턴은 fallback rule로 완화할 수 있다.

대책:

```text
animate subject repair
root fallback rule
```

## 신뢰도 해석

이 20개 샘플만 놓고 보면 spaCy 결과는 다음처럼 써야 한다.

```text
믿을 수 있는 것:
  tokenization, lemma 후보, 많은 단순 noun chunk, 단순 amod/prep relation

그대로 믿으면 위험한 것:
  tag-list caption의 dependency
  ambiguous compound noun
  coordination scope
  quoted text 내부 dependency
  ellipsis
  일부 root/action attachment
```

따라서 현재 전략은 spaCy output을 정답으로 쓰는 것이 아니라, 8단계 raw tuple extractor의 입력 feature로 쓰고, caption type 분기와 repair rule로 방어하는 것이다.

## 관측된 에러 케이스

현재 근거 파일:

- `reports/spacy_parse_sample_20.md`

| case | 문제 유형 | spaCy가 한 분석 | 왜 문제인지 | 대책 | 적용 위치 | 상태 |
|---:|---|---|---|---|---|---|
| 01 | `COORD_ATTACH` | `a red bow`가 `person`의 `conj`로 붙음 | 원문은 `dreadlocks and a red bow`가 둘 다 `with`의 대상에 가까움. 그대로 쓰면 `person and bow` 병렬처럼 보일 수 있음. | `with` preposition scope 아래 coordination을 복구. `relation(person, with, dreadlocks)`, `relation(person, with, bow)`, `attribute(bow, red)` 생성. | 8단계 repair | 예정 |
| 03 | `PARTICIPLE_ATTACH` | `speaking`이 `podium`의 `acl`로 붙음 | 의미상 말하는 주체는 podium이 아니라 woman. | `VERB-ing`가 무생물 noun에 붙고 가까운 animate subject가 있으면 action subject를 animate noun으로 재부착. | 8단계 repair | 예정 |
| 03 | `TEXT_MENTION` | `"Closing the Access Divide"`에서 `Closing`을 동사처럼 분석 | 스크린에 적힌 문구는 일반 object/action이 아니라 text mention. | 따옴표 내부를 `text_mention(screen, "Closing the Access Divide")`로 별도 추출. | 1단계 또는 8단계 | 예정 |
| 08 | `MWE_OBJECT_POS` | `trash can`에서 `can`을 `AUX/MD`로 봄 | `a black trash can` 전체가 명사구인데 `a black trash`까지만 chunk로 잡힘. | object MWE lexicon에서 `trash can`을 parser 전에 merge하는 대책이 가능하지만, 현재는 모델 비교를 위해 비활성화. | pre-parser protection 후보 | 비활성 |
| 08 | attachment 오류 | `with a silhouette`가 `GOES` 쪽에 붙고, `in a hat`도 `man`이 아니라 `silhouette` 쪽에 붙음 | quoted text 내부의 `GOES`가 실제 scene relation의 head처럼 작동하면 안 됨. | quoted text를 먼저 보호하거나 text mention으로 분리한 뒤 scene relation extraction에서 제외. | 1단계 또는 8단계 | 예정 |
| 09 | `ADV_CONTEXT` | `indoors`를 `NOUN/NNS`, `dobj`로 분석 | `appears indoors`에서 `indoors`는 object가 아니라 장소/상태 context. | `indoors/outdoors/inside/outside` 류를 context/location attribute로 처리. | 8단계 repair | 예정 |
| 09 | `HYPHEN_ADJ` | `bare-shouldered`가 `bare` + `shouldered`로 다소 이상하게 분리됨 | `bare-shouldered`는 child/person attribute에 가까움. | hyphenated adjective를 attribute candidate로 보존. | 1단계 normalization 또는 8단계 | 예정 |
| 10 | `TAG_LIST` | `blue jersey`를 `PROPN/NNP`로 분석 | comma-separated tag list라 dependency의 `conj/appos` 구조를 의미적으로 신뢰하기 어려움. | caption type을 `tag-list-like`로 분류하고 comma segment별 object/attribute 후보 추출. | 0단계 classifier + tag parser | 예정 |
| 11 | `VBN_ADJ` | `arched`를 `VERB/VBD`, `windows`를 `dobj`로 분석 | `arched windows`는 명사구이고 `arched`는 attribute. | `VBN/VBD + plural noun`이 noun chunk 내부/coordination 내부에 있으면 attribute로 복구. | 8단계 repair | 예정 |
| 14 | `TAG_LIST` | noun chunk가 `brown boot` 하나만 잡힘 | `brick wall`, `display`도 독립 tag 항목인데 dependency/noun chunk에 잘 반영되지 않음. | comma segment별로 `brown boot`, `indoor`, `brick wall`, `display`, `large`를 독립 후보로 처리. | 0단계 classifier + tag parser | 예정 |
| 15 | `COORD_ATTACH` | `a vest and red scarf`를 하나의 chunk로 잡고 root를 `scarf`로 둠 | 실제 의미는 `vest`와 `red scarf`가 병렬 객체에 가까움. | noun chunk 내부 `NOUN and ADJ NOUN` 패턴을 split. `object(vest)`, `object(scarf)`, `attribute(scarf, red)`. | 8단계 repair | 예정 |
| 15 | `ELLIPSIS` | `the other a yellow shirt`를 생략된 `wears`로 복원하지 못함 | 실제 의미는 `the other [wears] a yellow shirt`. | `one wears X, the other Y` 패턴에서 두 번째 wear relation 복원. | 8단계 repair | 예정 |
| 16 | `MWE_OBJECT_POS` | `music stands`를 `music` + 동사 `stands`로 분석 | `music stands`는 악보대라는 복합명사. | object MWE lexicon에 `music stand/music stands` 추가 후 pre-merge하는 대책 후보. 현재는 모델 비교를 위해 비활성화. | pre-parser protection 후보 | 비활성 |
| 19 | `ROOT_FAILURE` | `road`를 `ROOT`, `runs`를 `pobj`로 분석 | 핵심 동사는 `runs`, 주어는 `road`여야 함. | sentence root가 noun이고 근처 finite verb가 있으면 fallback root/action rule 적용. | 8단계 repair | 예정 |

## 대책별 구현 방침

### 1. Caption Type Classifier

목적:

```text
sentence-like
multi-sentence
tag-list-like
short-list-like
```

tag-list-like caption은 dependency parsing 결과를 강하게 믿지 않는다.

초기 rule:

```text
comma_count >= 2 and sentence_marks == 0 -> tag-list-like
word_count <= 8 and comma_count >= 1 -> short-list-like
```

대응:

```text
tag-list-like:
  comma segment 단위로 object/attribute 후보 추출

sentence-like:
  dependency 기반 tuple extraction 사용

multi-sentence:
  sentence별 graph 추출 후 caption-level merge
```

### 2. Object MWE Pre-Merge

목적:

```text
trash can
music stand
hot dog
traffic light
fire hydrant
```

처럼 하나의 object인데 POS/dependency가 깨질 위험이 큰 phrase를 parser 전에 보호한다.

현재 상태:

```text
MWE pre-merge prototype은 제거함.
모델끼리 순수 parser 성능을 비교하는 동안에는 사용하지 않음.
```

나중에 다시 켠다면 사용할 수 있는 spaCy 도구:

```text
PhraseMatcher
Doc.retokenize()
retokenizer.merge()
Doc extension
```

주의:

```text
wooden door
red bow
blue jersey
large building
```

같은 `attribute + object`는 pre-merge하면 정보가 사라질 수 있으므로 object MWE merge list에 넣지 않는 것이 원칙이다.

### 3. Relation MWE Span Detection

대상:

```text
in front of
on top of
next to
to the left of
to the right of
in the middle of
```

방침:

```text
parser 전에 merge하지 않음
span만 기록
8단계에서 dependency chain과 span을 함께 보고 relation label로 사용
```

예상 output:

```text
relation(woman, in front of, building)
relation(cat, on top of, table)
```

### 4. Dependency Repair Rules

8단계 raw tuple extraction에서 적용한다.

초기 rule 후보:

| rule | 입력 패턴 | 출력 |
|---|---|---|
| PP coordination repair | `with A and B` | `relation(head, with, A)`, `relation(head, with, B)` |
| noun chunk split | `NOUN and ADJ NOUN` | object 2개와 attribute 분리 |
| VBN adjective repair | `VBN/VBD + NOUN`이 명사구 위치 | `attribute(noun, vbn)` |
| animate participle repair | `animate noun ... VERB-ing` | `action(animate noun, verb)` |
| ellipsis repair | `one wears X, the other Y` | 두 번째 wear relation 복원 |
| root fallback | noun ROOT + finite verb nearby | finite verb를 action root 후보로 사용 |

### 5. Text Mention Extractor

대상:

```text
"Closing the Access Divide"
"BANG GOES THE KNIGHTHOOD"
```

방침:

```text
따옴표 내부 문자열은 일반 dependency extraction에서 제외하거나 약화
poster/screen/sign/read/show/text 류와 연결해 text_mention tuple 생성
```

예상 output:

```text
text_mention(screen, "Closing the Access Divide")
text_mention(poster, "BANG GOES THE KNIGHTHOOD")
```

## 현재 우선순위

| 우선순위 | 작업 | 이유 |
|---:|---|---|
| 1 | object MWE list 정리 | `trash can`, `music stands` 같은 명확한 오류를 parser 전에 줄임 |
| 2 | tag-list parser | GPIC caption에 comma-separated tag caption이 실제로 존재 |
| 3 | relation MWE span detector | `in front of`, `on top of`는 relation tuple 품질에 직접 영향 |
| 4 | text mention extractor | poster/screen/sign caption에서 scene object와 written text를 분리 |
| 5 | coordination repair | object/attribute/relation recall 개선 |
| 6 | root/participle repair | 어려운 문장 오류 보정 |

## 계속 추가할 형식

새 에러를 발견하면 아래 형식으로 추가한다.

```text
case:
caption:
observed_spaCy_parse:
expected_interpretation:
error_type:
pipeline_stage:
mitigation:
status:
```

표에 추가할 때는 아래 열을 유지한다.

```text
case | 문제 유형 | spaCy가 한 분석 | 왜 문제인지 | 대책 | 적용 위치 | 상태
```
