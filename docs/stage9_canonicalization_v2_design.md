# Stage 9 Canonicalization v2 설계 메모

## 핵심 정정

Stage 9의 핵심은 lemmatization이 아니다. Lemmatization은 `dogs -> dog`, `sitting -> sit` 같은 형태소 정규화이고, Stage 9에서 필요한 canonicalization은 다음 두 층을 분리해서 다룬다.

| 층 | 역할 | 예시 | 현재 상태 |
|---|---|---|---|
| synonym/alias canonicalization | 서로 다른 표현을 같은 main concept으로 묶음 | `kid -> child`, `bike -> bicycle`, `mobile_phone -> cell_phone` | split lexicon으로 분리 완료 |
| parent/ontology mapping | canonical concept을 coarse parent로 연결 | `child -> person|human`, `bicycle -> vehicle` | split lexicon으로 분리 완료, coverage 확장 필요 |

따라서 Stage 9 v2부터는 `canonical_source`와 `parent_source`를 따로 기록한다. 기존의 `source/confidence`도 호환 목적으로 남겨두지만, 분석할 때는 `canonical_source`, `parent_source`를 우선 봐야 한다.

## 이번 구현 변경

혼합 seed였던 아래 파일은 보존하되, 새 기본 동작은 split lexicon을 사용한다.

| 새 파일 | 의미 | 생성 방식 |
|---|---|---|
| `resources/lexicons/stage9_object_synonym_seed.tsv` | object synonym/alias만 관리 | 기존 object seed에서 `term != canonical`만 추출 |
| `resources/lexicons/stage9_object_parent_seed.tsv` | object parent/ontology만 관리 | 기존 object seed의 `canonical -> parent_chain` 추출 |
| `resources/lexicons/stage9_action_synonym_seed.tsv` | action synonym/alias만 관리 | 기존 action seed에서 `term != canonical`만 추출 |
| `resources/lexicons/stage9_action_parent_seed.tsv` | action parent/ontology만 관리 | 기존 action seed의 `canonical -> parent_chain` 추출 |

추가로 object canonical lookup은 `object_noun_mwe_clean_core.tsv`도 읽는다. 이 파일은 COCO/LVIS/Open Images/Visual Genome/WordNet 계열에서 온 object noun MWE canonical source로 사용된다.

## 현재 검증 결과

검증 대상:

```text
reports/raw_concepts_sample100_val00000_trf_stage9_reference_v1_input.jsonl
reports/raw_concepts_alt100_val00001_trf_stage9_reference_v1_input.jsonl
```

출력:

```text
reports/canonical_concepts_sample100_val00000_trf_stage9_canonical_v2.jsonl
reports/canonical_concepts_sample100_val00000_trf_stage9_canonical_v2_summary.md
reports/case_detail_sample100_val00000_trf_stage9_canonical_v2.md

reports/canonical_concepts_alt100_val00001_trf_stage9_canonical_v2.jsonl
reports/canonical_concepts_alt100_val00001_trf_stage9_canonical_v2_summary.md
reports/case_detail_alt100_val00001_trf_stage9_canonical_v2.md
```

중요한 확인 사항:

- `sit`처럼 이미 canonical인 action은 더 이상 `seat -> sit` synonym source로 잘못 표시되지 않는다.
- 상세 md의 entity/event/relation table에 `canonical_source`, `parent_source` 컬럼을 추가했다.
- summary에 entity/action/relation별 canonical source와 parent source count를 추가했다.

## 현재 coverage 해석

sample100 기준:

```text
Entity canonical sources:
  raw_lemma: 693
  external object MWE/synset sources: 27
  stage9 synonym seed: 4

Entity parent sources:
  none: 460
  stage9 parent seed: 236
  semantic_type_fallback: 28

Action canonical sources:
  raw_action: 206
  stage9 synonym seed: 2

Action parent sources:
  stage9 parent seed: 112
  visual_action_fallback: 96
```

해석:

- 구조 분리는 성공했지만 synonym canonicalization coverage는 아직 낮다.
- parent 없는 entity가 많기 때문에 parent ontology 확장이 다음 핵심이다.
- action parent도 fallback이 많아 VerbNet/WordNet/FrameNet류 후보 확장이 필요하다.

## 다음 확장 원칙

1. GPIC caption을 보고 whitelist를 만들지 않는다.
2. 외부 source에서 synonym/parent 후보를 만든다.
3. 후보는 자동 audit 또는 수동 audit을 거쳐 frozen lexicon으로 승격한다.
4. `canonical_source`와 `parent_source`를 항상 분리해서 기록한다.
5. lemmatization 결과는 fallback key로만 쓰고, synonym canonicalization의 근거로 둔갑시키지 않는다.

추천 확장 source:

| 대상 | source 후보 | 목적 |
|---|---|---|
| object synonym/alias | Visual Genome object aliases/synsets, Open Images labels, LVIS/COCO labels, WordNet/OEWN synsets | `sofa/couch`, `bike/bicycle` 같은 alias 확장 |
| object parent | WordNet/OEWN hypernym, Open Images hierarchy, COCO/LVIS supercategory | `bench -> furniture`, `tree -> plant` 같은 parent 확장 |
| action synonym | phrasal action whitelist, WordNet verb synsets, VerbNet class members | `seat -> sit`, `dress -> wear` 같은 action canonical 확장 |
| action parent | VerbNet classes, FrameNet/PropBank mappings, WordNet verb hypernyms | `run/walk/swim -> locomotion_action` 같은 parent 확장 |
| relation canonical | 현재 `relation_span_clean_core.tsv`, `preposition_mwe_clean_core.tsv` 유지 | 이미 source/provenance 분리되어 있음 |
| attribute canonical | 현재 `attribute_clean_core_typed_candidate.tsv` 유지 | 이미 type/source 분리되어 있음 |

## 구현 파일

```text
scripts/stage9_lexical_canonicalizer.py
scripts/canonicalize_raw_concepts.py
scripts/render_stage9_case_detail.py
scripts/split_stage9_seed_lexicons.py
```
