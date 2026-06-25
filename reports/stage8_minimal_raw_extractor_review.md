# Stage 8 Minimal Raw Extractor Review

- 기준일: 2026-06-25
- model: `en_core_web_trf`
- input sample: `data\gpic_captions_eval\val\gpic_val_00000.jsonl.gz`
- sample size: 100 captions
- raw JSONL: `reports\raw_concepts_sample_100_trf.jsonl`
- summary: `reports\raw_concepts_sample_100_trf_summary.md`
- inspection report: `reports\spacy_parse_sample_100_trf_raw_concepts.md`

## 현재 구현한 것

이번 구현은 본격적인 9단계 canonicalization이나 10단계 scene graph가 아니라, 7단계 spaCy linguistic parse 결과를 countable schema 후보로 바꾸는 최소 8단계다.

구현 위치:

| file | 역할 |
|---|---|
| `scripts\raw_concept_extractor.py` | 일반 문장 caption용 minimal raw concept extractor |
| `scripts\extract_raw_concepts.py` | caption JSONL -> raw concept JSONL 변환 CLI |
| `scripts\inspect_spacy_parse.py` | `--extract-raw-concepts` 옵션으로 markdown inspection에 8단계 출력 추가 |
| `scripts\tag_list_parser.py` | 기존 tag-list 전용 partial raw extraction branch |

## 8단계에서 뽑는 단위

| type | 의미 | 예시 |
|---|---|---|
| `object` | noun chunk root 기반 object 후보 | `person`, `flower`, `jersey` |
| `attribute` | object modifier 기반 속성 후보 | `red`, `glass`, `large`, `wooden` |
| `quantity` | 수량/개수 후보 | `three`, `two` |
| `action` | verb predicate 후보 | `sit`, `stand`, `hold` |
| `relation` edge | 전치사/공간/소유 관계 후보 | `on`, `with`, `in_front_of` |
| `context` | 장면/공간 문맥 후보 | `indoor`, `background`, `front` |

## 중요한 일반 규칙

POS 결과를 그대로 concept type으로 쓰지 않는다.

예를 들어 `trf`가 `orange glass flowers`에서 `orange`를 `NOUN/compound`로 보더라도, 8단계에서는 color lexicon을 보고 다음처럼 재분류한다.

```text
object: flower
attribute.color: orange
attribute.material: glass
```

현재 들어간 보정 규칙:

| rule | 이유 |
|---|---|
| color/material/size lexicon | POS가 틀려도 `blue`, `orange`, `glass`, `wooden`, `large`를 속성으로 보존 |
| lowercase PROPN object downgrade | `blue jersey`처럼 lowercase인데 PROPN으로 나온 object를 medium-confidence object로 보존 |
| compound modifier 보존 | `shopping cart`, `soccer ball`처럼 compound 정보를 버리지 않음 |
| multi-word relation detection | `in front of`, `at top of`, `from side of` 같은 relation span 보존 |
| spatial region context | `in front`, `on top`처럼 대상이 생략된 spatial anchor를 object가 아니라 context로 보존 |
| quote masking 연동 | quote 내부 제목/문구가 dependency parse를 망가뜨리지 않게 함 |
| tag-list branch 연동 | comma-separated tag caption은 전체 문장 dependency를 믿지 않고 segment 단위로 처리 |

## 100개 샘플 결과

Caption shape:

| shape | count |
|---|---:|
| `multi-sentence` | 57 |
| `sentence-like` | 22 |
| `tag-list-like` | 21 |

Parse path:

| path | count |
|---|---:|
| `sentence` | 79 |
| `tag_list` | 21 |

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
| `relation` | 296 |
| `agent` | 150 |
| `patient` | 70 |
| `has_context` | 38 |
| `has_quantity` | 16 |
| `candidate_has_attribute` | 5 |

주요 relation evidence:

| relation | count |
|---|---:|
| `with` | 64 |
| `in` | 64 |
| `on` | 41 |
| `of` | 14 |
| `under` | 14 |
| `near` | 13 |
| `at` | 10 |
| `behind` | 8 |
| `in_front_of` | 4 |

## 현재 해석

이제 7단계 출력만 보는 상태는 벗어났다. 일반 문장 caption도 최소한 object, attribute, action, relation, context, quantity 후보로 변환된다.

특히 `orange`, `blue`, `glass`, `wooden`처럼 POS가 흔들리던 modifier를 countable attribute로 다시 살리는 방향은 잘 작동한다. `in front of`도 단일 relation evidence로 묶인다.

다만 아직 “정답 scene graph”는 아니다. 현재 출력은 9단계 canonicalization 전 raw 후보 layer다.

## 남은 문제

| 문제 | 예시 | 필요한 다음 규칙 |
|---|---|---|
| compound modifier가 너무 넓음 | `shopping cart`, `soccer ball`, `power line` | object MWE / compound role classifier |
| tag-list attribute role이 아직 덜 세분화됨 | tag-list의 `blue jersey`가 generic `attribute` | tag-list branch에도 color/material/size role 공유 |
| pronoun이 object로 남음 | `her`, `it` | pronoun/coreference policy |
| inclusion 표현이 action/relation에 중복될 수 있음 | `including` | inclusion relation으로 둘지 action으로 둘지 결정 |
| dependency 오류는 여전히 전파됨 | ellipsis, wrong attachment | confidence 낮추기 + repair rule |
| object phrase와 object head가 분리 안 됨 | `trash can`, `music stand` | phrase-level object mention 추가 |

## 다음 우선순위

바로 다음은 sample을 더 보는 것보다 object/compound 쪽을 정리하는 게 좋다.

1. object MWE / compound role classifier 추가
2. tag-list branch와 sentence branch의 lexicon role 통합
3. pronoun/coreference policy 결정
4. 500개 샘플로 재측정

현재 상태에서 바로 production 100M으로 가기에는 이르다. 하지만 8단계의 기본 골격은 잡혔고, 이제 개선해야 할 문제가 parser 자체가 아니라 schema 변환 규칙 쪽으로 이동했다.
