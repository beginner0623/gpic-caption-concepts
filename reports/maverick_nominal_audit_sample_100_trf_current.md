# Maverick Nominal-Anaphoric Audit

이 리포트는 Maverick `predefined_mentions`를 사용해 `one/other/others/both/each`류 nominal-anaphoric 후보가 이전 object/group 후보와 같은 cluster로 묶이는지 확인합니다.

## Settings
- raw_concepts: `reports\raw_concepts_sample_100_trf_current.jsonl`
- output_jsonl: `reports\maverick_nominal_audit_sample_100_trf_current.jsonl`
- spacy_model: `en_core_web_trf`
- maverick_model: `sapienzanlp/maverick-mes-ontonotes`
- device: `cuda`
- nominal_candidates_seen: `9`
- broad_cluster_threshold: `8`

## Nominal Subtypes
| item | count |
| --- | ---: |
| `one_anaphor` | 4 |
| `other_anaphor` | 3 |
| `group_both` | 1 |
| `distributive_each` | 1 |

## Resolution Status
| item | count |
| --- | ---: |
| `resolved_to_candidate` | 7 |
| `unresolved` | 2 |

## Cluster Quality
| item | count |
| --- | ---: |
| `broad_cluster_check_manually` | 6 |
| `compact_cluster` | 3 |

## Recommendations
| item | count |
| --- | ---: |
| `manual_group_resolution` | 4 |
| `copy_antecedent_type_apply_modifiers` | 3 |
| `exclude_from_object_count_unresolved` | 2 |

## Audit Rows
| case | nominal | subtype | antecedent | antecedent type | quality | cluster | status | recommendation |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- |
| 15 | `One` | `one_anaphor` | a bathroom | `object_chunk` | `broad_cluster_check_manually` | the camera ; camera ; a bathroom ; bathroom ; One ; a ves... | `resolved_to_candidate` | `copy_antecedent_type_apply_modifiers` |
| 15 | `other` | `other_anaphor` | a vest and red scarf | `coordination_group` | `broad_cluster_check_manually` | the camera ; camera ; a bathroom ; bathroom ; One ; a ves... | `resolved_to_candidate` | `manual_group_resolution` |
| 16 | `others` | `other_anaphor` | white dresses and shirts | `coordination_group` | `broad_cluster_check_manually` | Children ; white dresses ; white dresses and shirts ; dre... | `resolved_to_candidate` | `manual_group_resolution` |
| 40 | `one` | `one_anaphor` | Several cars | `object_chunk` | `broad_cluster_check_manually` | A curved brick building ; building ; large windows ; wind... | `resolved_to_candidate` | `copy_antecedent_type_apply_modifiers` |
| 62 | `Both` | `group_both` | A man and a woman | `coordination_group` | `compact_cluster` | A man and a woman ; Both | `resolved_to_candidate` | `manual_group_resolution` |
| 63 | `One` | `one_anaphor` |  | `` | `compact_cluster` | One ; other | `unresolved` | `exclude_from_object_count_unresolved` |
| 63 | `other` | `other_anaphor` |  | `` | `compact_cluster` | One ; other | `unresolved` | `exclude_from_object_count_unresolved` |
| 89 | `one` | `one_anaphor` | Two men | `object_chunk` | `broad_cluster_check_manually` | Two men ; men ; one ; food ; a pan ; pan ; Another fire ;... | `resolved_to_candidate` | `copy_antecedent_type_apply_modifiers` |
| 98 | `each` | `distributive_each` | Four people | `object_chunk` | `broad_cluster_check_manually` | Four people ; people ; white lab coats ; lab coats ; a ta... | `resolved_to_candidate` | `manual_group_resolution` |

## Interpretation
- `compact_cluster`: Maverick cluster가 작아서 audit signal로 비교적 보기 쉽습니다.
- `broad_cluster_check_manually`: cluster가 넓게 뭉쳐 false positive 위험이 큽니다. 자동 치환하지 말고 rule 기반 후보로만 봐야 합니다.
- `copy_antecedent_type_apply_modifiers`: `a red one -> car + red`처럼 antecedent object type을 복사하고 nominal modifier를 attribute 후보로 붙일 수 있습니다.
- `link_discourse_other`: `other/others`는 object count에 넣지 말고 discourse link로만 둡니다.
- `manual_group_resolution`: `both/each` 또는 coordination group은 단일 object로 collapse하지 않습니다.
- `exclude_from_object_count_unresolved`: antecedent가 불확실하므로 surface nominal은 count에서 제외합니다.
