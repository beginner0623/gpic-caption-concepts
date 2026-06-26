# fastcoref Pronoun Resolution Audit

이 리포트는 기존 raw concept 결과를 직접 수정하지 않고, fastcoref cluster가 pronoun/anaphoric mention을 어디로 연결하는지 확인하는 sidecar audit입니다.

## Settings
- raw_concepts: `reports\raw_concepts_sample_100_trf_current.jsonl`
- output_jsonl: `reports\fastcoref_audit_sample_100_trf_current.jsonl`
- spacy_model: `en_core_web_trf`
- fastcoref_device: `cuda:0`
- max_tokens_in_batch: `4096`
- records_processed: `100`
- reference_mentions_seen: `45`

## Reference Types
| item | count |
| --- | ---: |
| `pronoun_reference` | 23 |
| `possessive_reference` | 13 |
| `nominal_reference` | 7 |
| `relative_reference` | 2 |

## Resolution Status
| item | count |
| --- | ---: |
| `resolved_to_object` | 34 |
| `unresolved` | 11 |

## Recommendations
| item | count |
| --- | ---: |
| `redirect_edges_to_antecedent` | 20 |
| `attach_possessor_metadata` | 13 |
| `exclude_from_object_count_unresolved` | 9 |
| `prefer_dependency_rule` | 2 |
| `manual_nominal_resolution` | 1 |

## Lemmas
| item | count |
| --- | ---: |
| `it` | 8 |
| `they` | 8 |
| `its` | 5 |
| `his` | 4 |
| `he` | 4 |
| `she` | 3 |
| `other` | 3 |
| `her` | 3 |
| `one` | 2 |
| `that` | 1 |
| `their` | 1 |
| `both` | 1 |
| `who` | 1 |
| `each` | 1 |

## Audit Rows
| case | mention | type | current concept | antecedent | linked object | status | recommendation |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 3 | `her` | `pronoun_reference` | `object:noun_chunk_root` | A woman | woman | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 4 | `One` | `nominal_reference` | `quantity:quantity` |  |  | `unresolved` | `exclude_from_object_count_unresolved` |
| 12 | `his` | `possessive_reference` | `attribute:modifier_attribute` | A man in a white shirt | man | `resolved_to_object` | `attach_possessor_metadata` |
| 16 | `One` | `nominal_reference` | `quantity:quantity` |  |  | `unresolved` | `exclude_from_object_count_unresolved` |
| 16 | `others` | `nominal_reference` | `object:noun_chunk_root` |  |  | `unresolved` | `exclude_from_object_count_unresolved` |
| 19 | `it` | `pronoun_reference` | `object:noun_chunk_root` | A paved road with a yellow line | road | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 21 | `her` | `possessive_reference` | `attribute:modifier_attribute` | The woman in the center | woman | `resolved_to_object` | `attach_possessor_metadata` |
| 21 | `her` | `possessive_reference` | `attribute:modifier_attribute` | The woman in the center | woman | `resolved_to_object` | `attach_possessor_metadata` |
| 22 | `its` | `possessive_reference` | `attribute:modifier_attribute` | A brown duck | duck | `resolved_to_object` | `attach_possessor_metadata` |
| 22 | `Its` | `possessive_reference` | `attribute:modifier_attribute` | A brown duck | duck | `resolved_to_object` | `attach_possessor_metadata` |
| 22 | `it` | `pronoun_reference` | `object:noun_chunk_root` | A brown duck | duck | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 28 | `them` | `pronoun_reference` | `object:noun_chunk_root` | A person in a blue and pink costume | person | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 32 | `it` | `pronoun_reference` | `object:noun_chunk_root` | The eye | eye | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 33 | `her` | `possessive_reference` | `attribute:modifier_attribute` | A woman | woman | `resolved_to_object` | `attach_possessor_metadata` |
| 35 | `He` | `pronoun_reference` | `object:noun_chunk_root` | A man with dark hair and a goatee | man | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 39 | `it` | `pronoun_reference` | `object:noun_chunk_root` | A tall glass of latte macchiato | glass | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 40 | `other` | `nominal_reference` | `attribute:modifier_attribute` |  |  | `unresolved` | `exclude_from_object_count_unresolved` |
| 41 | `He` | `pronoun_reference` | `object:noun_chunk_root` | A man in a blue shirt | man | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 41 | `him` | `pronoun_reference` | `object:noun_chunk_root` | A man in a blue shirt | man | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 41 | `his` | `possessive_reference` | `attribute:modifier_attribute` | A man in a blue shirt | man | `resolved_to_object` | `attach_possessor_metadata` |
| 44 | `They` | `pronoun_reference` | `object:noun_chunk_root` |  |  | `unresolved` | `exclude_from_object_count_unresolved` |
| 44 | `them` | `pronoun_reference` | `object:noun_chunk_root` |  |  | `unresolved` | `exclude_from_object_count_unresolved` |
| 47 | `them` | `pronoun_reference` | `object:noun_chunk_root` | Four people | people | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 47 | `them` | `pronoun_reference` | `object:noun_chunk_root` | Each person | person | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 48 | `him` | `pronoun_reference` | `object:noun_chunk_root` | A man in a tuxedo | man | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 51 | `that` | `relative_reference` | `object:noun_chunk_root` |  |  | `unresolved` | `prefer_dependency_rule` |
| 52 | `other` | `nominal_reference` | `attribute:modifier_attribute` |  |  | `unresolved` | `exclude_from_object_count_unresolved` |
| 57 | `it` | `pronoun_reference` | `object:noun_chunk_root` | A small, weathered orange-brown artifact with a roun... | artifact | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 57 | `its` | `possessive_reference` | `attribute:modifier_attribute` | A small, weathered orange-brown artifact with a roun... | artifact | `resolved_to_object` | `attach_possessor_metadata` |
| 58 | `their` | `possessive_reference` | `attribute:modifier_attribute` | Tall trees with rough bark | trees | `resolved_to_object` | `attach_possessor_metadata` |
| 60 | `its` | `possessive_reference` | `attribute:modifier_attribute` | A stone church with a cross on its tower | church | `resolved_to_object` | `attach_possessor_metadata` |
| 62 | `Both` | `nominal_reference` | `object:noun_chunk_root` | A man and a woman | man | `resolved_to_object` | `manual_nominal_resolution` |
| 63 | `who` | `relative_reference` | `object:noun_chunk_root` |  |  | `unresolved` | `prefer_dependency_rule` |
| 63 | `them` | `pronoun_reference` | `object:noun_chunk_root` | Two men in camouflage uniforms | men | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 68 | `It` | `pronoun_reference` | `object:noun_chunk_root` | A long, rusty metal pipe | pipe | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 74 | `his` | `possessive_reference` | `attribute:modifier_attribute` | A man in a blue suit | man | `resolved_to_object` | `attach_possessor_metadata` |
| 74 | `his` | `possessive_reference` | `attribute:modifier_attribute` | a man in a gray suit | man | `resolved_to_object` | `attach_possessor_metadata` |
| 74 | `They` | `pronoun_reference` | `object:noun_chunk_root` |  |  | `unresolved` | `exclude_from_object_count_unresolved` |
| 77 | `She` | `pronoun_reference` | `object:noun_chunk_root` | A woman in a black, American flag-themed outfit | woman | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 77 | `her` | `pronoun_reference` | `object:noun_chunk_root` | A woman in a black, American flag-themed outfit | woman | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 80 | `it` | `pronoun_reference` | `object:noun_chunk_root` | The object | object | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 80 | `Its` | `possessive_reference` | `attribute:modifier_attribute` | The object | object | `resolved_to_object` | `attach_possessor_metadata` |
| 80 | `it` | `pronoun_reference` | `object:noun_chunk_root` | The object | object | `resolved_to_object` | `redirect_edges_to_antecedent` |
| 98 | `each` | `nominal_reference` | `object:noun_chunk_root` |  |  | `unresolved` | `exclude_from_object_count_unresolved` |
| 98 | `them` | `pronoun_reference` | `object:noun_chunk_root` | Three men | men | `resolved_to_object` | `redirect_edges_to_antecedent` |

## Interpretation
- `resolved_to_object`: coref antecedent span 안에 기존 object mention이 있어서 edge redirect 후보로 쓸 수 있습니다.
- `resolved_text_only`: antecedent text는 찾았지만 기존 object mention과 직접 겹치지 않아 보수적으로 자동 redirect하지 않는 편이 좋습니다.
- `unresolved`: coref cluster가 없거나 antecedent가 없어 object/attribute count에서 제외 후보입니다.
- `attach_possessor_metadata`: possessive reference는 visual attribute로 세지 말고 possessor link 후보로만 둡니다.
- `manual_nominal_resolution`: `both/each/one/other`류는 group/cardinality 손실 위험이 있어 자동 redirect하지 않습니다.
- `prefer_dependency_rule`: `that/who/which` relative는 coref보다 dependency 기반 antecedent 치환이 더 안전합니다.
