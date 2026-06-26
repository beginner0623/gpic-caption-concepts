# Raw Concept Extraction Summary

- input: `data\gpic_captions_eval\val\gpic_val_00000.jsonl.gz`
- output: `reports\raw_concepts_sample_100_trf_current.jsonl`
- model: `en_core_web_trf`
- max_records: `100`
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
| `object` | 730 |
| `attribute` | 412 |
| `action` | 208 |
| `context` | 49 |
| `quantity` | 30 |

## Mention Roles
| item | count |
| --- | ---: |
| `noun_chunk_root` | 632 |
| `verb_predicate` | 208 |
| `color_attribute` | 114 |
| `modifier_attribute` | 112 |
| `segment_head` | 91 |
| `attribute` | 38 |
| `compound_modifier` | 36 |
| `visual_attribute` | 35 |
| `context_word` | 34 |
| `material_attribute` | 31 |
| `size_attribute` | 26 |
| `exact_quantity` | 15 |
| `state_attribute` | 15 |
| `spatial_region` | 11 |
| `approximate_quantity` | 8 |
| `floating_attribute` | 5 |
| `with_absolute_recovered_object` | 5 |
| `scene_context` | 4 |
| `group_quantity` | 4 |
| `distributive_quantity` | 2 |
| `tag_list_person_object_override` | 2 |
| `indefinite_quantity` | 1 |

## Edge Types
| item | count |
| --- | ---: |
| `has_attribute` | 407 |
| `relation` | 331 |
| `agent` | 155 |
| `patient` | 79 |
| `has_context` | 38 |
| `has_quantity` | 28 |
| `candidate_has_attribute` | 5 |
| `scene_contains` | 5 |

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
| `over` | 2 |
| `onto` | 2 |
| `among` | 2 |
| `through` | 2 |
| `above` | 1 |
| `toward` | 1 |
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
| `mention:high` | 1169 |
| `edge:medium` | 543 |
| `edge:high` | 500 |
| `mention:medium` | 260 |
| `edge:low` | 5 |
