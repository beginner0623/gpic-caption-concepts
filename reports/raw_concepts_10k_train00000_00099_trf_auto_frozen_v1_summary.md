# Raw Concept Extraction Summary

- input: `data\gpic_captions_10k_train00000_00099\train\gpic_train_00000_00099_merged_10000.jsonl.gz`
- output: `reports\raw_concepts_10k_train00000_00099_trf_auto_frozen_v1.jsonl`
- model: `en_core_web_trf`
- max_records: `10000`
- batch_size: `256`
- n_process: `1`
- records_written: `10000`
- mask_quotes: `True`
- quote_handling: `raw_quote_retokenize`
- merge_object_mwes: `True`
- merge_hyphen_spans: `True`
- object_mwe_lexicon: `resources\lexicons\object_noun_mwe_clean_core.tsv`
- parse_tag_lists: `True`

## Caption Shapes
| item | count |
| --- | ---: |
| `multi-sentence` | 6282 |
| `sentence-like` | 3612 |
| `tag-list-like` | 104 |
| `short-list-like` | 2 |

## Parse Paths
| item | count |
| --- | ---: |
| `sentence` | 9896 |
| `tag_list` | 104 |

## Concept Types
| item | count |
| --- | ---: |
| `object` | 86560 |
| `attribute` | 59390 |
| `action` | 35670 |
| `context` | 9981 |
| `quantity` | 5559 |
| `reference` | 1665 |
| `particle` | 369 |
| `group` | 85 |
| `negation` | 6 |

## Mention Roles
| item | count |
| --- | ---: |
| `noun_chunk_root` | 85443 |
| `verb_predicate` | 35670 |
| `modifier_attribute` | 19319 |
| `color_attribute` | 15914 |
| `compound_modifier` | 7126 |
| `scene_context` | 5967 |
| `size_attribute` | 4588 |
| `visual_attribute` | 4456 |
| `spatial_region` | 3728 |
| `material_attribute` | 3393 |
| `exact_quantity` | 2770 |
| `state_attribute` | 2289 |
| `quote_text` | 2131 |
| `approximate_quantity` | 1515 |
| `contrastive_reference` | 877 |
| `indefinite_quantity` | 628 |
| `singular_substitute` | 488 |
| `segment_head` | 462 |
| `phrasal_particle` | 369 |
| `group_quantity` | 294 |
| `context_word` | 286 |
| `with_absolute_recovered_object` | 268 |
| `relation_head` | 178 |
| `zero_quantity` | 174 |
| `distributive_quantity` | 167 |
| `attribute` | 158 |
| `group_reference` | 133 |
| `verb_object` | 106 |
| `generic_structure_reference` | 88 |
| `coordination_group` | 85 |
| `distributive_reference` | 60 |
| `nominal_reference_instance` | 32 |
| `verb_subject` | 31 |
| `inherited_action_subject` | 17 |
| `floating_attribute` | 16 |
| `partitive_quantity` | 11 |
| `generic_object_reference` | 10 |
| `generic_human_reference` | 9 |
| `negation_cue` | 6 |
| `prep_object` | 6 |
| `ambiguous_segment_head` | 5 |
| `tag_list_person_object_override` | 5 |
| `relation_subject` | 4 |
| `lowercase_propn_as_object` | 3 |

## Edge Types
| item | count |
| --- | ---: |
| `has_attribute` | 57079 |
| `relation` | 50948 |
| `agent` | 35687 |
| `patient` | 14574 |
| `has_context` | 6253 |
| `has_quantity` | 4967 |
| `refers_to` | 1665 |
| `has_particle` | 369 |
| `scene_contains` | 268 |
| `has_member` | 170 |
| `derived_from` | 32 |
| `candidate_has_attribute` | 26 |
| `negates` | 6 |

## Relation Evidence
| item | count |
| --- | ---: |
| `with` | 10660 |
| `in` | 10086 |
| `on` | 6473 |
| `of` | 2943 |
| `near` | 1955 |
| `at` | 1742 |
| `under` | 1694 |
| `behind` | 1608 |
| `by` | 1582 |
| `to` | 1022 |
| `from` | 748 |
| `across` | 727 |
| `against` | 696 |
| `beside` | 586 |
| `in_front_of` | 583 |
| `through` | 538 |
| `along` | 530 |
| `into` | 490 |
| `next_to` | 476 |
| `above` | 462 |
| `include` | 452 |
| `around` | 416 |
| `toward` | 397 |
| `over` | 339 |
| `during` | 333 |
| `for` | 327 |
| `like` | 276 |
| `inside` | 229 |
| `among` | 215 |
| `between` | 204 |
| `below` | 148 |
| `beneath` | 142 |
| `down` | 134 |
| `side_region_of` | 110 |
| `as` | 95 |
| `right_of` | 95 |
| `edge_of` | 87 |
| `outside` | 86 |
| `left_of` | 72 |
| `beyond` | 63 |
| `atop` | 63 |
| `center_of` | 59 |
| `alongside` | 58 |
| `near_edge_of` | 51 |
| `along_edge_of` | 49 |
| `past` | 49 |
| `about` | 42 |
| `away_from` | 42 |
| `near_center_of` | 41 |
| `at_top_of` | 39 |
| `near_base_of` | 39 |
| `onto` | 38 |
| `base_of` | 35 |
| `corner_of` | 31 |
| `off` | 27 |
| `along_side_of` | 25 |
| `up` | 20 |
| `out_of` | 19 |
| `surface_of` | 18 |
| `bottom_of` | 17 |
| `within` | 17 |
| `before` | 17 |
| `near_side_of` | 16 |
| `on_top_of` | 14 |
| `at_front_of` | 13 |
| `end_of` | 12 |
| `near_top_of` | 12 |
| `near_corner_of` | 11 |
| `front_region_of` | 9 |
| `from_side_of` | 9 |
| `behind; repaired_self_edge_target from them->man` | 8 |
| `near_front_of` | 7 |
| `at_edge_of` | 7 |
| `near_bottom_of` | 7 |
| `without` | 6 |
| `beside; repaired_self_edge_source from woman` | 6 |
| `throughout` | 5 |
| `beside; repaired_self_edge_target from them->man` | 5 |
| `middle_of` | 5 |
| `behind; repaired_self_edge_target from them->people` | 5 |
| `behind; repaired_self_edge_target from them->person` | 4 |
| `besides` | 4 |
| `with; repaired_self_edge_source from people` | 4 |
| `beside; repaired_self_edge_source from women` | 3 |
| `behind; repaired_self_edge_target from them->woman` | 3 |
| `beside; repaired_self_edge_target from them->woman` | 3 |
| `beside; repaired_self_edge_source from men` | 3 |
| `near_end_of` | 3 |
| `behind; repaired_self_edge_target from them->child` | 3 |
| `beside; repaired_self_edge_source from man` | 3 |
| `beside; repaired_self_edge_source from child` | 3 |
| `beside; repaired_self_edge_source from people` | 3 |
| `between; repaired_self_edge_target from them->woman` | 2 |
| `beside; repaired_self_edge_target from them->person` | 2 |
| `via` | 2 |
| `ahead_of` | 2 |
| `below; repaired_self_edge_source from plaque` | 2 |
| `beside; repaired_self_edge_target from them->adult` | 2 |
| `behind; repaired_self_edge_source from person` | 2 |
| `out` | 2 |
| `behind; repaired_self_edge_target from them->People` | 2 |
| `across_from` | 2 |
| `from_bottom_of` | 2 |
| `despite` | 2 |
| `from_back_of` | 2 |
| `behind; repaired_self_edge_source from adults` | 2 |
| `behind; repaired_self_edge_source from fighter jet` | 2 |
| `behind; repaired_self_edge_source from people` | 2 |
| `beside; repaired_self_edge_source from boys` | 2 |
| `after` | 2 |
| `above; repaired_self_edge_source from women` | 2 |
| `from_center_of` | 2 |
| `behind; repaired_self_edge_source from airplane` | 2 |
| `at_back_of` | 2 |
| `over; repaired_self_edge_source from man` | 2 |
| `with; repaired_self_edge_source from men` | 2 |
| `next_to; repaired_self_edge_target from them->person` | 2 |
| `next_to; repaired_self_edge_source from women` | 2 |
| `behind; repaired_self_edge_target from them->adults` | 2 |
| `behind; repaired_self_edge_target from them->trees` | 2 |
| `in_front_of; repaired_self_edge_source from player` | 2 |
| `amid` | 2 |
| `behind; repaired_self_edge_target from them->lights` | 1 |
| `beneath; repaired_self_edge_source from beetle` | 1 |
| `near; repaired_self_edge_target from them->woman` | 1 |
| `behind; repaired_self_edge_source from women` | 1 |
| `beside; repaired_self_edge_target from them->player` | 1 |
| `between; repaired_self_edge_source from man` | 1 |
| `behind; repaired_self_edge_source from boat` | 1 |
| `next_to; repaired_self_edge_source from bag` | 1 |
| `beside; repaired_self_edge_source from person` | 1 |
| `beside; repaired_self_edge_target from them->leaf` | 1 |
| `around; repaired_self_edge_target from them->water` | 1 |
| `beside; repaired_self_edge_source from girls` | 1 |
| `behind; repaired_self_edge_target from them->Trees` | 1 |
| `behind; repaired_self_edge_source from caliper` | 1 |
| `behind; repaired_self_edge_source from board` | 1 |
| `behind; repaired_self_edge_target from them->boy` | 1 |
| `in_front_of; repaired_self_edge_source from man` | 1 |
| `beneath; repaired_self_edge_source from body` | 1 |
| `against; repaired_self_edge_target from them->waves` | 1 |
| `behind; repaired_self_edge_target from them->women` | 1 |
| `behind; repaired_self_edge_source from girls` | 1 |
| `from_front_of` | 1 |
| `behind; repaired_self_edge_target from them->peaks` | 1 |
| `with; repaired_self_edge_target from them->men` | 1 |
| `around; repaired_self_edge_source from lighting` | 1 |
| `with; repaired_self_edge_source from runners` | 1 |
| `behind; repaired_self_edge_target from them->spectators` | 1 |
| `behind; repaired_self_edge_source from player` | 1 |
| `around; repaired_self_edge_target from them->bubbles` | 1 |
| `between; repaired_self_edge_target from them->child` | 1 |
| `around; repaired_self_edge_target from them->women` | 1 |
| `next_to; repaired_self_edge_target from them->child` | 1 |
| `below; repaired_self_edge_target from them->notices` | 1 |
| `above; repaired_self_edge_source from billboard` | 1 |
| `with; repaired_self_edge_source from players` | 1 |
| `next_to; repaired_self_edge_target from them->woman` | 1 |
| `behind; repaired_self_edge_source from woman` | 1 |
| `around; repaired_self_edge_source from surface` | 1 |
| `behind; repaired_self_edge_target from them->lighting` | 1 |
| `behind; repaired_self_edge_source from airplanes` | 1 |
| `in_front_of; repaired_self_edge_target from them->sculptures` | 1 |
| `near; repaired_self_edge_source from sign` | 1 |
| `beside; repaired_self_edge_source from fork` | 1 |
| `beneath; repaired_self_edge_source from logo` | 1 |
| `around; repaired_self_edge_target from them->lights` | 1 |
| `in_front_of; repaired_self_edge_target from them->tree trunk` | 1 |
| `behind; repaired_self_edge_source from van` | 1 |
| `behind; repaired_self_edge_target from them->window` | 1 |
| `beside; repaired_self_edge_target from them->women` | 1 |
| `behind; repaired_self_edge_target from them->screen` | 1 |
| `above; repaired_self_edge_target from them->space` | 1 |
| `in_front_of; repaired_self_edge_target from them->baby` | 1 |
| `next_to; repaired_self_edge_source from person` | 1 |
| `behind; repaired_self_edge_source from boy` | 1 |
| `between; repaired_self_edge_target from them->man` | 1 |
| `behind; repaired_self_edge_target from them->rider` | 1 |
| `behind; repaired_self_edge_source from men` | 1 |
| `side_of` | 1 |
| `behind; repaired_self_edge_source from skyscrapers` | 1 |
| `behind; repaired_self_edge_target from them->wall` | 1 |
| `beside; repaired_self_edge_target from them->men` | 1 |
| `across; repaired_self_edge_source from shadows` | 1 |
| `behind; repaired_self_edge_target from them->wakes` | 1 |
| `above; repaired_self_edge_source from entrance` | 1 |
| `below; repaired_self_edge_target from them->patch` | 1 |
| `with; repaired_self_edge_source from Players` | 1 |
| `per` | 1 |
| `from_edge_of` | 1 |
| `above; repaired_self_edge_target from them->Lights` | 1 |
| `behind; repaired_self_edge_target from them->Spectators` | 1 |
| `between; repaired_self_edge_target from them->lawn` | 1 |
| `behind; repaired_self_edge_target from them->buildings` | 1 |
| `behind; repaired_self_edge_target from them->guitarist` | 1 |
| `around; repaired_self_edge_source from players` | 1 |
| `behind; repaired_self_edge_target from them->structures` | 1 |

## Skipped Edges
| item | count |
| --- | ---: |
| `self_edge_after_coref` | 308 |
| `pronoun_resolved_to_action_agent` | 104 |

## Confidence
| item | count |
| --- | ---: |
| `mention:high` | 158579 |
| `edge:medium` | 99509 |
| `edge:high` | 72509 |
| `mention:medium` | 40706 |
| `edge:low` | 26 |
