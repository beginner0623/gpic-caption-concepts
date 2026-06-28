# Raw Concept Extraction Summary

- input: `data\gpic_captions_1k_val00002_00011\val\gpic_val_00002_00011_merged_1000.jsonl.gz`
- output: `reports\raw_concepts_1k_val00002_00011_trf_plural_v1.jsonl`
- model: `en_core_web_trf`
- max_records: `1000`
- batch_size: `64`
- n_process: `1`
- records_written: `1000`
- mask_quotes: `True`
- quote_handling: `raw_quote_retokenize`
- merge_object_mwes: `True`
- merge_hyphen_spans: `True`
- object_mwe_lexicon: `resources\lexicons\object_noun_mwe_clean_core.tsv`
- parse_tag_lists: `True`

## Caption Shapes
| item | count |
| --- | ---: |
| `multi-sentence` | 552 |
| `sentence-like` | 241 |
| `tag-list-like` | 207 |

## Parse Paths
| item | count |
| --- | ---: |
| `sentence` | 792 |
| `tag_list` | 208 |

## Concept Types
| item | count |
| --- | ---: |
| `object` | 6533 |
| `attribute` | 4122 |
| `action` | 2294 |
| `context` | 671 |
| `quantity` | 415 |
| `reference` | 133 |
| `particle` | 27 |
| `group` | 7 |
| `unknown` | 2 |

## Mention Roles
| item | count |
| --- | ---: |
| `noun_chunk_root` | 5582 |
| `verb_predicate` | 2294 |
| `color_attribute` | 1098 |
| `modifier_attribute` | 1073 |
| `segment_head` | 901 |
| `scene_context` | 451 |
| `compound_modifier` | 442 |
| `attribute` | 381 |
| `size_attribute` | 320 |
| `visual_attribute` | 308 |
| `exact_quantity` | 232 |
| `material_attribute` | 223 |
| `spatial_region` | 206 |
| `state_attribute` | 137 |
| `approximate_quantity` | 125 |
| `quote_text` | 102 |
| `contrastive_reference` | 79 |
| `floating_attribute` | 38 |
| `indefinite_quantity` | 34 |
| `singular_substitute` | 33 |
| `phrasal_particle` | 27 |
| `context_word` | 14 |
| `with_absolute_recovered_object` | 14 |
| `distributive_quantity` | 13 |
| `relation_head` | 11 |
| `distributive_reference` | 9 |
| `tag_list_person_object_override` | 9 |
| `group_quantity` | 8 |
| `coordination_group` | 7 |
| `group_reference` | 7 |
| `verb_object` | 6 |
| `ambiguous_segment_head` | 5 |
| `generic_structure_reference` | 4 |
| `lowercase_propn_as_object` | 3 |
| `zero_quantity` | 3 |
| `unclassified_segment_root` | 2 |
| `nominal_reference_instance` | 1 |
| `verb_subject` | 1 |
| `generic_object_reference` | 1 |

## Edge Types
| item | count |
| --- | ---: |
| `has_attribute` | 3970 |
| `relation` | 3382 |
| `agent` | 2302 |
| `patient` | 874 |
| `has_context` | 465 |
| `has_quantity` | 376 |
| `refers_to` | 133 |
| `candidate_has_attribute` | 51 |
| `has_particle` | 27 |
| `has_member` | 14 |
| `scene_contains` | 14 |
| `derived_from` | 1 |

## Relation Evidence
| item | count |
| --- | ---: |
| `in` | 723 |
| `with` | 691 |
| `on` | 475 |
| `of` | 165 |
| `at` | 141 |
| `near` | 123 |
| `under` | 121 |
| `by` | 113 |
| `behind` | 109 |
| `to` | 69 |
| `beside` | 58 |
| `against` | 55 |
| `in_front_of` | 51 |
| `along` | 37 |
| `across` | 34 |
| `above` | 32 |
| `from` | 32 |
| `include` | 31 |
| `through` | 28 |
| `into` | 27 |
| `over` | 25 |
| `around` | 25 |
| `next_to` | 21 |
| `inside` | 20 |
| `for` | 19 |
| `toward` | 18 |
| `during` | 12 |
| `like` | 11 |
| `between` | 10 |
| `below` | 8 |
| `among` | 8 |
| `down` | 7 |
| `past` | 6 |
| `base_of` | 5 |
| `side_region_of` | 5 |
| `atop` | 5 |
| `along_edge_of` | 4 |
| `at_front_of` | 4 |
| `edge_of` | 4 |
| `onto` | 3 |
| `alongside` | 3 |
| `center_of` | 3 |
| `at_top_of` | 3 |
| `beneath` | 3 |
| `about` | 3 |
| `beyond` | 2 |
| `near_center_of` | 2 |
| `near_edge_of` | 2 |
| `behind; repaired_self_edge_target from them->man` | 2 |
| `behind; repaired_self_edge_source from jet` | 1 |
| `before` | 1 |
| `around; repaired_self_edge_target from them->Tables` | 1 |
| `beside; repaired_self_edge_source from People` | 1 |
| `out` | 1 |
| `behind; repaired_self_edge_target from them->mountains` | 1 |
| `behind; repaired_self_edge_target from them->bushes` | 1 |
| `right_of` | 1 |
| `near_base_of` | 1 |
| `near_top_of` | 1 |
| `beside; repaired_self_edge_target from them->person` | 1 |
| `corner_of` | 1 |
| `beside; repaired_self_edge_target from them->machine` | 1 |
| `out_of` | 1 |
| `beside; repaired_self_edge_source from man` | 1 |
| `beside; repaired_self_edge_target from them->man` | 1 |
| `behind; repaired_self_edge_source from building` | 1 |
| `as` | 1 |
| `off` | 1 |
| `away_from` | 1 |
| `end_of` | 1 |
| `behind; repaired_self_edge_target from them->mountain` | 1 |
| `after` | 1 |
| `beside; repaired_self_edge_target from them->boy` | 1 |

## Skipped Edges
| item | count |
| --- | ---: |
| `self_edge_after_coref` | 25 |
| `pronoun_resolved_to_action_agent` | 11 |

## Confidence
| item | count |
| --- | ---: |
| `mention:high` | 11736 |
| `edge:medium` | 6135 |
| `edge:high` | 5423 |
| `mention:medium` | 2466 |
| `edge:low` | 51 |
| `mention:low` | 2 |
