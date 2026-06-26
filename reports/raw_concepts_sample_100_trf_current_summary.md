# Raw Concept Extraction Summary

- input: `data\gpic_captions_eval\val\gpic_val_00000.jsonl.gz`
- output: `reports\raw_concepts_sample_100_trf_current.jsonl`
- model: `en_core_web_trf`
- max_records: `100`
- batch_size: `256`
- n_process: `1`
- records_written: `100`
- mask_quotes: `True`
- quote_handling: `raw_quote_retokenize`
- merge_object_mwes: `True`
- merge_hyphen_spans: `True`
- object_mwe_lexicon: `resources\lexicons\object_noun_mwe_clean_core.tsv`
- parse_tag_lists: `True`

## Caption Shapes
| item | count |
| --- | ---: |
| `multi-sentence` | 57 |
| `sentence-like` | 22 |
| `tag-list-like` | 21 |

## Parse Paths
| item | count |
| --- | ---: |
| `sentence` | 79 |
| `tag_list` | 21 |

## Concept Types
| item | count |
| --- | ---: |
| `object` | 639 |
| `attribute` | 411 |
| `action` | 208 |
| `context` | 71 |
| `quantity` | 30 |
| `reference` | 13 |
| `group` | 1 |

## Mention Roles
| item | count |
| --- | ---: |
| `noun_chunk_root` | 542 |
| `verb_predicate` | 208 |
| `color_attribute` | 120 |
| `modifier_attribute` | 95 |
| `segment_head` | 89 |
| `scene_context` | 44 |
| `attribute` | 37 |
| `compound_modifier` | 36 |
| `visual_attribute` | 34 |
| `material_attribute` | 30 |
| `spatial_region` | 27 |
| `size_attribute` | 26 |
| `exact_quantity` | 15 |
| `state_attribute` | 15 |
| `quote_text` | 13 |
| `approximate_quantity` | 8 |
| `floating_attribute` | 5 |
| `with_absolute_recovered_object` | 5 |
| `singular_substitute` | 4 |
| `group_quantity` | 4 |
| `contrastive_reference` | 2 |
| `generic_structure_reference` | 2 |
| `distributive_quantity` | 2 |
| `generic_object_reference` | 2 |
| `tag_list_person_object_override` | 2 |
| `nominal_reference_instance` | 1 |
| `generic_human_reference` | 1 |
| `coordination_group` | 1 |
| `group_reference` | 1 |
| `indefinite_quantity` | 1 |
| `distributive_reference` | 1 |

## Edge Types
| item | count |
| --- | ---: |
| `has_attribute` | 392 |
| `relation` | 328 |
| `agent` | 217 |
| `patient` | 81 |
| `has_context` | 44 |
| `has_quantity` | 28 |
| `refers_to` | 13 |
| `candidate_has_attribute` | 7 |
| `scene_contains` | 5 |
| `has_member` | 2 |
| `derived_from` | 1 |

## Relation Evidence
| item | count |
| --- | ---: |
| `with` | 85 |
| `in` | 68 |
| `on` | 42 |
| `near` | 14 |
| `under` | 14 |
| `of` | 12 |
| `at` | 10 |
| `behind` | 8 |
| `by` | 8 |
| `to` | 5 |
| `across` | 5 |
| `beside` | 4 |
| `include` | 4 |
| `into` | 4 |
| `during` | 3 |
| `over` | 3 |
| `from` | 3 |
| `against` | 3 |
| `in_front_of` | 2 |
| `beyond` | 2 |
| `down` | 2 |
| `for` | 2 |
| `toward` | 2 |
| `around` | 2 |
| `in_front_of; repaired_self_edge_source from person` | 2 |
| `onto` | 2 |
| `among` | 2 |
| `through` | 2 |
| `above` | 1 |
| `bottom_of` | 1 |
| `between` | 1 |
| `near_end_of` | 1 |
| `in_front_of; repaired_self_edge_source from hockey player` | 1 |
| `from_side_of` | 1 |
| `next_to` | 1 |
| `below` | 1 |
| `inside` | 1 |
| `past` | 1 |
| `base_of` | 1 |
| `beside; repaired_self_edge_target from them->woman` | 1 |
| `at_top_of` | 1 |

## Skipped Edges
| item | count |
| --- | ---: |
| `self_edge_after_coref` | 1 |
| `pronoun_resolved_to_action_agent` | 1 |

## Confidence
| item | count |
| --- | ---: |
| `mention:high` | 1149 |
| `edge:medium` | 560 |
| `edge:high` | 551 |
| `mention:medium` | 224 |
| `edge:low` | 7 |
