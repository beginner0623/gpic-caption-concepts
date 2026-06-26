# Nominal Reference Resolver Audit

이 리포트는 단어별 땜빵이 아니라 reference cue class와 antecedent scoring으로 `one/other/both/each`류 후보를 처리한 결과입니다.

## Settings
- raw_concepts: `reports\raw_concepts_sample_100_trf_current.jsonl`
- output_jsonl: `reports\nominal_reference_resolution_sample_100_trf_current.jsonl`
- spacy_model: `en_core_web_trf`
- max_antecedent_tokens: `80`
- min_score: `45`
- ambiguous_margin: `15`
- references_seen: `9`

## Reference Classes
| item | count |
| --- | ---: |
| `singular_substitute` | 4 |
| `contrastive_reference` | 3 |
| `group_reference` | 1 |
| `distributive_reference` | 1 |

## Status
| item | count |
| --- | ---: |
| `resolved` | 8 |
| `ambiguous` | 1 |

## Confidence
| item | count |
| --- | ---: |
| `high` | 8 |
| `low` | 1 |

## Recommendations
| item | count |
| --- | ---: |
| `link_singular_reference` | 3 |
| `link_contrastive_reference` | 3 |
| `copy_antecedent_type_apply_modifiers` | 1 |
| `manual_review_ambiguous_reference` | 1 |
| `link_distributive_reference` | 1 |

## Audit Rows
| case | reference | class | modifiers | antecedent | score | margin | status | confidence | recommendation | reasons |
| ---: | --- | --- | --- | --- | ---: | ---: | --- | --- | --- | --- |
| 15 | `One` | `singular_substitute` |  | Two men | 118 | 70 | `resolved` | `high` | `link_singular_reference` | recent, previous_sentence, plural_source_for_substitute, has_quanti... |
| 15 | `other` | `contrastive_reference` |  | Two men | 128 | 45 | `resolved` | `high` | `link_contrastive_reference` | nearby, previous_sentence, plural_group_match, has_quantity_signal,... |
| 16 | `others` | `contrastive_reference` |  | Children | 118 | 31 | `resolved` | `high` | `link_contrastive_reference` | nearby, previous_sentence, plural_group_match, agent_like_anteceden... |
| 40 | `one` | `singular_substitute` | red | Several cars | 127 | 42 | `resolved` | `high` | `copy_antecedent_type_apply_modifiers` | very_recent, same_sentence, plural_source_for_substitute, has_quant... |
| 62 | `Both` | `group_reference` |  | A man and a woman | 126 | 9 | `ambiguous` | `low` | `manual_review_ambiguous_reference` | reachable, two_sentences_back, plural_group_match, coordination_gro... |
| 63 | `One` | `singular_substitute` |  | Two men | 118 | 41 | `resolved` | `high` | `link_singular_reference` | recent, previous_sentence, plural_source_for_substitute, has_quanti... |
| 63 | `other` | `contrastive_reference` |  | Two men | 128 | 53 | `resolved` | `high` | `link_contrastive_reference` | nearby, previous_sentence, plural_group_match, has_quantity_signal,... |
| 89 | `one` | `singular_substitute` |  | Two men | 119 | 77 | `resolved` | `high` | `link_singular_reference` | very_recent, same_sentence, plural_source_for_substitute, has_quant... |
| 98 | `each` | `distributive_reference` |  | Four people | 130 | 104 | `resolved` | `high` | `link_distributive_reference` | recent, same_sentence, plural_group_match, has_quantity_signal, age... |

## Policy
- `resolved`: Stage 9에서 reference edge 후보로 사용할 수 있습니다.
- `ambiguous`: 후보는 찾았지만 margin이 낮으므로 자동 적용하지 않습니다.
- `unresolved`: object count에서 surface reference를 제외하고, 별도 unresolved로 남깁니다.
- `singular_substitute` with modifiers: `a red one`처럼 antecedent type을 복사하고 reference modifier를 attribute 후보로 붙입니다.
- bare `singular_substitute`: `One wears...`처럼 새 object를 만들지 않고 antecedent/member reference link로만 남깁니다.
- `group_reference` / `distributive_reference`: 단일 object로 collapse하지 않고 group/distribution link로 남깁니다.
