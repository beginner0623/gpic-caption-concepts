# Raw Concept Extraction Summary

- input: `data\gpic_captions_eval\val\gpic_val_00000.jsonl.gz`
- output: `reports\raw_concepts_sample_100_trf.jsonl`
- model: `en_core_web_trf`
- max_records: `100`
- records_written: `100`
- mask_quotes: `True`
- quote_handling: `raw_quote_retokenize`
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
| `object` | 729 |
| `attribute` | 455 |
| `action` | 209 |
| `context` | 49 |
| `quantity` | 16 |

## Mention Roles
| item | count |
| --- | ---: |
| `noun_chunk_root` | 634 |
| `verb_predicate` | 209 |
| `color_attribute` | 121 |
| `modifier_attribute` | 117 |
| `segment_head` | 91 |
| `compound_modifier` | 61 |
| `attribute` | 41 |
| `visual_attribute` | 38 |
| `context_word` | 34 |
| `material_attribute` | 31 |
| `size_attribute` | 26 |
| `quantity` | 16 |
| `state_attribute` | 15 |
| `spatial_region` | 11 |
| `floating_attribute` | 5 |
| `scene_context` | 4 |
| `relation_head` | 2 |
| `ambiguous_segment_head` | 2 |

## Edge Types
| item | count |
| --- | ---: |
| `has_attribute` | 450 |
| `relation` | 332 |
| `agent` | 158 |
| `patient` | 79 |
| `has_context` | 38 |
| `has_quantity` | 16 |
| `candidate_has_attribute` | 5 |

## Relation Evidence
| item | count |
| --- | ---: |
| `with` | 86 |
| `in` | 69 |
| `on` | 42 |
| `near` | 16 |
| `of` | 15 |
| `under` | 14 |
| `at` | 10 |
| `behind` | 8 |
| `by` | 8 |
| `beside` | 6 |
| `to` | 5 |
| `across` | 5 |
| `into` | 5 |
| `in_front_of` | 4 |
| `during` | 3 |
| `around` | 3 |
| `from` | 3 |
| `against` | 3 |
| `include` | 3 |
| `beyond` | 2 |
| `down` | 2 |
| `for` | 2 |
| `toward` | 2 |
| `over` | 2 |
| `onto` | 2 |
| `among` | 2 |
| `through` | 2 |
| `above` | 1 |
| `along` | 1 |
| `between` | 1 |
| `from_side_of` | 1 |
| `below` | 1 |
| `inside` | 1 |
| `past` | 1 |
| `at_top_of` | 1 |

## Confidence
| item | count |
| --- | ---: |
| `mention:high` | 1175 |
| `edge:medium` | 566 |
| `edge:high` | 507 |
| `mention:medium` | 283 |
| `edge:low` | 5 |
