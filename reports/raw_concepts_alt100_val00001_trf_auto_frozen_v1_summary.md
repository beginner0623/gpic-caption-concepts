# Raw Concept Extraction Summary

- input: `data\gpic_captions_eval_alt\val\gpic_val_00001.jsonl.gz`
- output: `reports\raw_concepts_alt100_val00001_trf_auto_frozen_v1.jsonl`
- model: `en_core_web_trf`
- max_records: `100`
- batch_size: `64`
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
| `multi-sentence` | 48 |
| `sentence-like` | 30 |
| `tag-list-like` | 22 |

## Parse Paths
| item | count |
| --- | ---: |
| `sentence` | 78 |
| `tag_list` | 22 |

## Concept Types
| item | count |
| --- | ---: |
| `object` | 628 |
| `attribute` | 403 |
| `action` | 200 |
| `context` | 51 |
| `quantity` | 39 |
| `reference` | 21 |
| `particle` | 4 |
| `group` | 1 |

## Mention Roles
| item | count |
| --- | ---: |
| `noun_chunk_root` | 522 |
| `verb_predicate` | 200 |
| `color_attribute` | 117 |
| `segment_head` | 100 |
| `modifier_attribute` | 99 |
| `compound_modifier` | 47 |
| `attribute` | 47 |
| `scene_context` | 35 |
| `size_attribute` | 27 |
| `visual_attribute` | 25 |
| `exact_quantity` | 19 |
| `state_attribute` | 18 |
| `spatial_region` | 16 |
| `approximate_quantity` | 15 |
| `material_attribute` | 12 |
| `contrastive_reference` | 12 |
| `quote_text` | 9 |
| `singular_substitute` | 8 |
| `indefinite_quantity` | 4 |
| `phrasal_particle` | 4 |
| `with_absolute_recovered_object` | 3 |
| `tag_list_person_object_override` | 2 |
| `floating_attribute` | 2 |
| `group_quantity` | 1 |
| `coordination_group` | 1 |
| `group_reference` | 1 |
| `verb_object` | 1 |

## Edge Types
| item | count |
| --- | ---: |
| `has_attribute` | 388 |
| `relation` | 330 |
| `agent` | 198 |
| `patient` | 71 |
| `has_context` | 35 |
| `has_quantity` | 34 |
| `refers_to` | 21 |
| `has_particle` | 4 |
| `scene_contains` | 3 |
| `candidate_has_attribute` | 2 |
| `has_member` | 2 |

## Relation Evidence
| item | count |
| --- | ---: |
| `with` | 71 |
| `in` | 67 |
| `on` | 49 |
| `near` | 15 |
| `at` | 13 |
| `under` | 12 |
| `of` | 12 |
| `beside` | 6 |
| `to` | 6 |
| `from` | 6 |
| `through` | 6 |
| `by` | 6 |
| `next_to` | 5 |
| `around` | 5 |
| `into` | 4 |
| `behind` | 4 |
| `include` | 4 |
| `like` | 3 |
| `across` | 3 |
| `over` | 3 |
| `toward` | 3 |
| `among` | 3 |
| `along` | 3 |
| `above` | 2 |
| `inside` | 2 |
| `against` | 2 |
| `in_front_of` | 2 |
| `between` | 2 |
| `during` | 1 |
| `past` | 1 |
| `as` | 1 |
| `behind; repaired_self_edge_source from men` | 1 |
| `before` | 1 |
| `away_from` | 1 |
| `edge_of` | 1 |
| `bottom_of` | 1 |
| `for` | 1 |
| `corner_of` | 1 |
| `down` | 1 |

## Skipped Edges
| item | count |
| --- | ---: |
| `self_edge_after_coref` | 8 |
| `pronoun_resolved_to_action_agent` | 2 |

## Confidence
| item | count |
| --- | ---: |
| `mention:high` | 1112 |
| `edge:medium` | 560 |
| `edge:high` | 526 |
| `mention:medium` | 235 |
| `edge:low` | 2 |
