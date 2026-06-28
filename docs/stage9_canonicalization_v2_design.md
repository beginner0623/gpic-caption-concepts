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

## Event role count collapse

Stage 9 v2의 count-facing event role은 `agent`와 `patient`만 사용한다. 여기서 `agent`는 의도적 행위자만 뜻하지 않고, active-voice normalization 이후 subject-side argument를 뜻한다. 따라서 `snow covers road`, `trees surround building`, `sunlight lights room`에서 `snow`, `trees`, `sunlight`는 모두 count schema상 `agent`로 둔다.

정책:

| raw/internal role | count-facing role | 설명 |
|---|---|---|
| `agent` | `agent` | 능동태 subject-side argument |
| `patient` | `patient` | 능동태 object-side argument |
| `theme` | `patient` | passive subject / 상태나 배치의 중심 대상 |
| `by_agent_or_causer` | `agent` | passive `by` phrase를 active subject-side argument로 정규화 |

출력 정책:

- `canonical_events[].roles[].role`은 `agent` 또는 `patient`만 사용한다.
- 디버깅/감사용으로 `raw_role`을 남긴다.
- passive 정규화는 `voice_normalization=passive_to_active`로 표시한다.
- reference 복원 role은 `voice_normalization=reference_recovery`로 표시한다.
- relation/location 정보는 event role로 늘리지 않고 기존 `relation` fact로 유지한다.

예시:

```text
The building is surrounded by trees.

canonical event role:
  surround patient building
  surround agent trees

trace:
  patient <- raw_role: theme, voice_normalization: passive_to_active
  agent   <- raw_role: by_agent_or_causer, voice_normalization: passive_to_active
```

## 2026-06-28: Stage 9 lexicon expansion v1

목표:

```text
Stage 9 canonicalization을 단순 lemma 정규화에서 끝내지 않고,
raw concept -> canonical representative -> parent concept 형태로 더 많이 count 가능하게 만든다.
```

이번 결정:

```text
기존 seed 파일을 직접 크게 섞지 않고, expansion v1 파일을 별도로 둔다.
Stage 9 loader는 base seed + expansion seed를 함께 읽는다.
```

새 파일:

```text
resources/lexicons/stage9_object_synonym_expansion_v1.tsv
resources/lexicons/stage9_object_parent_expansion_v1.tsv
resources/lexicons/stage9_action_parent_expansion_v1.tsv
resources/lexicons/stage9_attribute_synonym_seed.tsv
resources/external/nltk_data/corpora/wordnet.zip  # local cache, gitignored
resources/external/nltk_data/corpora/omw-1.4.zip  # local cache, gitignored
```

source 정책:

- object synonym은 WordNet synset + caption visual audit가 모두 명확한 high-confidence alias만 우선 적용한다.
- object parent는 WordNet hypernym, COCO object label, 명확한 project visual ontology audit를 근거로 둔다.
- action parent는 accepted phrasal action whitelist와 WordNet verb synset 기반으로 보강한다.
- attribute synonym은 exact attribute type은 유지하되, countable 대표어가 필요한 색상/재질 alias만 별도 적용한다.
- GPIC target caption을 보고 whitelist를 고르지는 않는다.

예시:

| raw | canonical | parent | source |
|---|---|---|---|
| `puppy`, `canine` | `dog` | `animal|living_thing` | WordNet synset + Stage 9 audit |
| `cab`, `taxicab` | `taxi` | `vehicle` | WordNet synset/hypernym + Stage 9 audit |
| `lady` | `woman` | `person|human` | WordNet synset + Stage 9 audit |
| `tv` | `television` | `device|artifact` | COCO object label + WordNet |
| `tree` | `tree` | `plant|living_thing` | WordNet hypernym |
| `building` | `building` | `structure|artifact` | WordNet synset |
| `navy` | `blue` | `color_attribute|color|visual_attribute` | CSS/VG overlap + basic color audit |
| `wooden` | `wood` | `material_attribute|material|visual_attribute` | material lexicon + audit |
| `blow_out` | `blow_out` | `state_change_action|visual_action` | phrasal action whitelist |
| `surround` | `surround` | `spatial_configuration_action|visual_action` | WordNet verb synset + audit |

구현 변경:

```text
scripts/stage9_lexical_canonicalizer.py
  - object/action/parent expansion TSV를 기본 로딩 경로에 추가
  - attribute synonym map 추가
  - TSV reader를 utf-8-sig로 변경해 BOM 있는 TSV도 안전하게 처리

scripts/canonicalize_raw_concepts.py
  - 새 expansion lexicon CLI 인자 추가
  - summary에 expansion lexicon 경로 기록
```

검증:

```text
compileall scripts: passed

lexicon load count:
  object_synonyms: 7110
  object_parents: 179
  action_parents: 75
  attribute_synonyms: 19
  attributes: 622

sample100 current entity parent none: 316
alt100 current entity parent none: 308
```

출력 재생성:

```text
reports/canonical_concepts_sample100_val00000_trf_stage9_canonical_v2.jsonl
reports/canonical_concepts_sample100_val00000_trf_stage9_canonical_v2_summary.md
reports/case_detail_sample100_val00000_trf_stage9_canonical_v2.md

reports/canonical_concepts_alt100_val00001_trf_stage9_canonical_v2.jsonl
reports/canonical_concepts_alt100_val00001_trf_stage9_canonical_v2_summary.md
reports/case_detail_alt100_val00001_trf_stage9_canonical_v2.md
```

남은 과제:

- WordNet/OEWN 전체를 바로 auto-apply하지 말고 candidate TSV를 만든 뒤 audit해서 v2로 승격한다.
- Open Images hierarchy, LVIS/COCO supercategory를 object parent 후보로 추가한다.
- VerbNet/FrameNet 기반 action parent 후보를 만든다.
- `turquoise`, `teal`, `magenta`처럼 basic color collapse가 애매한 색은 아직 자동 적용하지 않는다.
