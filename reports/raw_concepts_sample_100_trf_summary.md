# Raw Concept Extraction Summary

- input: `data\gpic_captions_eval\val\gpic_val_00000.jsonl.gz`
- output: `reports\raw_concepts_sample_100_trf.jsonl`
- model: `en_core_web_trf`
- max_records: `100`
- records_written: `100`
- mask_quotes: `True`
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
| `object` | 731 |
| `attribute` | 471 |
| `action` | 209 |
| `context` | 49 |
| `quantity` | 16 |

## Mention Roles
| item | count |
| --- | ---: |
| `noun_chunk_root` | 636 |
| `verb_predicate` | 209 |
| `color_attribute` | 121 |
| `modifier_attribute` | 117 |
| `segment_head` | 91 |
| `compound_modifier` | 65 |
| `attribute` | 41 |
| `visual_attribute` | 38 |
| `context_word` | 34 |
| `material_attribute` | 31 |
| `state_attribute` | 27 |
| `size_attribute` | 26 |
| `quantity` | 16 |
| `spatial_region` | 11 |
| `floating_attribute` | 5 |
| `scene_context` | 4 |
| `relation_head` | 2 |
| `ambiguous_segment_head` | 2 |

## Edge Types
| item | count |
| --- | ---: |
| `has_attribute` | 466 |
| `relation` | 296 |
| `agent` | 150 |
| `patient` | 70 |
| `has_context` | 38 |
| `has_quantity` | 16 |
| `candidate_has_attribute` | 5 |

## Relation Evidence
| item | count |
| --- | ---: |
| `with` | 64 |
| `in` | 64 |
| `on` | 41 |
| `of` | 14 |
| `under` | 14 |
| `near` | 13 |
| `at` | 10 |
| `behind` | 8 |
| `by` | 6 |
| `beside` | 6 |
| `to` | 5 |
| `across` | 5 |
| `into` | 5 |
| `in_front_of` | 4 |
| `during` | 3 |
| `around` | 3 |
| `from` | 3 |
| `against` | 3 |
| `beyond` | 2 |
| `down` | 2 |
| `for` | 2 |
| `toward` | 2 |
| `over` | 2 |
| `onto` | 2 |
| `among` | 2 |
| `include` | 2 |
| `above` | 1 |
| `along` | 1 |
| `between` | 1 |
| `from_side_of` | 1 |
| `below` | 1 |
| `inside` | 1 |
| `past` | 1 |
| `at_top_of` | 1 |
| `through` | 1 |

## Confidence
| item | count |
| --- | ---: |
| `mention:high` | 1177 |
| `edge:medium` | 560 |
| `edge:high` | 476 |
| `mention:medium` | 299 |
| `edge:low` | 5 |
