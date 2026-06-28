# Stage 9 PP Source v1 Case Detail - alt100 val00001

- input: `reports\canonical_concepts_alt100_val00001_trf_stage9_pp_source_v1.jsonl`
- max_records: `100`
- contents: raw concept mentions/edges + Stage 9 canonical entities/events/relations

## 01

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `009d83aeeeb75b5ff2d8c8ee94d79d04f26d67e91f609efc71471b7e63cf6814`
**parse_path:** `sentence`

> Several colorful posters are mounted on a white wall above a desk. A computer monitor displays an image, and various bottles and art supplies sit on the desk in front of it.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | posters | poster | noun_chunk_root | chunk0 | 2 | high |
| m1 | quantity | Several | several | approximate_quantity | chunk0 | 0 | medium |
| m2 | attribute | colorful | colorful | modifier_attribute | chunk0 | 1 | medium |
| m3 | object | wall | wall | noun_chunk_root | chunk1 | 8 | high |
| m4 | attribute | white | white | color_attribute | chunk1 | 7 | high |
| m5 | object | desk | desk | noun_chunk_root | chunk2 | 11 | high |
| m6 | object | computer monitor | computer_monitor | noun_chunk_root | chunk3 | 14 | high |
| m7 | object | image | image | noun_chunk_root | chunk4 | 17 | high |
| m8 | object | bottles | bottle | noun_chunk_root | chunk5 | 21 | high |
| m9 | quantity | various | various | approximate_quantity | chunk5 | 20 | medium |
| m10 | object | supplies | supply | noun_chunk_root | chunk6 | 24 | high |
| m11 | attribute | art | art | compound_modifier | chunk6 | 23 | medium |
| m12 | object | desk | desk | noun_chunk_root | chunk7 | 28 | high |
| m13 | action | mounted | mount | verb_predicate | doc | 4 | high |
| m14 | action | displays | display | verb_predicate | doc | 15 | high |
| m15 | action | sit | sit | verb_predicate | doc | 25 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | medium | chunk0 quantity -> posters |
| e1 | has_attribute | m0 | m2 | medium | chunk0 amod -> posters |
| e2 | has_attribute | m3 | m4 | high | chunk1 amod -> wall |
| e3 | has_quantity | m8 | m9 | medium | chunk5 quantity -> bottles |
| e4 | has_attribute | m10 | m11 | medium | chunk6 compound -> supplies |
| e5 | agent | m13 | m0 | medium | nsubjpass -> mounted |
| e6 | agent | m14 | m6 | medium | nsubj -> displays |
| e7 | patient | m14 | m7 | medium | dobj -> displays |
| e8 | agent | m15 | m8 | medium | nsubj -> sit |
| e9 | agent | m15 | m10 | medium | nsubj -> sit |
| e10 | relation | m0 | m3 | high | on |
| e11 | relation | m3 | m5 | high | above |
| e12 | relation | m8 | m12 | high | on |

### Skipped Raw Concept Edges
| type | source | target | confidence | reason | evidence |
| --- | --- | --- | --- | --- | --- |
| relation | m8 | m8 | high | self_edge_after_coref | in_front_of |

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | poster | posters | object | m0 | raw_mention |  |  |  |
| ent_m3 | object | wall | wall | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | desk | desk | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | computer_monitor | computer monitor | object | m6 | raw_mention |  |  |  |
| ent_m7 | object | image | image | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | bottle | bottles | object | m8 | raw_mention |  |  |  |
| ent_m10 | object | supply | supplies | object | m10 | raw_mention |  |  |  |
| ent_m12 | object | desk | desk | object | m12 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m13 | mounted | mount | mount |  | theme:m0->ent_m0 |  |
| ce1 | m14 | displays | display | display |  | agent:m6->ent_m6; patient:m7->ent_m7 |  |
| ce2 | m15 | sit | sit | sit |  | agent:m8->ent_m8; agent:m10->ent_m10 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | mount | theme | m0 | ent_m0 | medium | e5 | nsubjpass -> mounted |  |  |
| ce1 | display | agent | m6 | ent_m6 | medium | e6 | nsubj -> displays |  |  |
| ce1 | display | patient | m7 | ent_m7 | medium | e7 | dobj -> displays |  |  |
| ce2 | sit | agent | m8 | ent_m8 | medium | e8 | nsubj -> sit |  |  |
| ce2 | sit | agent | m10 | ent_m10 | medium | e9 | nsubj -> sit |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | on | high | e10 | False | False |  |  |
| cr1 | m3 | m5 | ent_m3 | ent_m5 | above | high | e11 | False | False |  |  |
| cr2 | m8 | m12 | ent_m8 | ent_m12 | on | high | e12 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m13 | e5 | m0 |  |  | {"action_mention_id": "m13", "kind": "passive_subject_to_theme", "raw_edge_id": "e5", "target": "m0"} |

## 02

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `0111d88df23c0d12152d10e6b2250862b564dbdb78be57af836eb78663930014`
**parse_path:** `sentence`

> A stone church with pointed towers and arched walkway stands beside a grassy garden with trimmed hedges and pink flowers.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | church | church | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | stone | stone | material_attribute | chunk0 | 1 | high |
| m2 | object | towers | tower | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | pointed | pointed | modifier_attribute | chunk1 | 4 | medium |
| m4 | object | walkway | walkway | noun_chunk_root | chunk2 | 8 | high |
| m5 | attribute | arched | arched | visual_attribute | chunk2 | 7 | medium |
| m6 | object | garden | garden | noun_chunk_root | chunk3 | 13 | high |
| m7 | attribute | grassy | grassy | modifier_attribute | chunk3 | 12 | medium |
| m8 | object | hedges | hedge | noun_chunk_root | chunk4 | 16 | high |
| m9 | attribute | trimmed | trim | state_attribute | chunk4 | 15 | medium |
| m10 | object | flowers | flower | noun_chunk_root | chunk5 | 19 | high |
| m11 | attribute | pink | pink | color_attribute | chunk5 | 18 | high |
| m12 | action | stands | stand | verb_predicate | doc | 9 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 compound -> church |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> towers |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> walkway |
| e3 | has_attribute | m6 | m7 | medium | chunk3 amod -> garden |
| e4 | has_attribute | m8 | m9 | medium | chunk4 amod -> hedges |
| e5 | has_attribute | m10 | m11 | high | chunk5 amod -> flowers |
| e6 | agent | m12 | m0 | medium | nsubj -> stands |
| e7 | relation | m0 | m2 | high | with |
| e8 | relation | m0 | m4 | high | with |
| e9 | relation | m0 | m6 | high | beside |
| e10 | relation | m6 | m8 | high | with |
| e11 | relation | m6 | m10 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | church | church | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | tower | towers | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | walkway | walkway | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | garden | garden | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | hedge | hedges | object | m8 | raw_mention |  |  |  |
| ent_m10 | object | flower | flowers | object | m10 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | stands | stand | stand |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e6 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e7 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | high | e8 | False | False |  |  |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | beside | high | e9 | False | False |  |  |
| cr3 | m6 | m8 | ent_m6 | ent_m8 | with | high | e10 | False | False |  |  |
| cr4 | m6 | m10 | ent_m6 | ent_m10 | with | high | e11 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 03

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `0196fc48ceb03b00a74261b2545370fca46dd97426e91b30193376102e523414`
**parse_path:** `tag_list`

> orange tricycle, man, smiling, outdoor, green trees

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | tricycle | tricycle | segment_head | t0 | 1 | high |
| m1 | attribute | orange | orange | attribute | t0 | 0 | high |
| m2 | object | man | man | tag_list_person_object_override | t1 | 0 | high |
| m3 | attribute | smiling | smile | floating_attribute | t2 | 0 | medium |
| m4 | context | outdoor | outdoor | scene_context | t3 | 0 | high |
| m5 | object | trees | tree | segment_head | t4 | 1 | high |
| m6 | attribute | green | green | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> tricycle |
| e1 | candidate_has_attribute | m2 | m3 | low | t2 adjacent floating attribute |
| e2 | has_context | scene | m4 | high | t3 context tag |
| e3 | has_attribute | m5 | m6 | high | t4 internal amod -> trees |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | tricycle | tricycle | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | man | man | person | m2 | raw_mention |  |  |  |
| ent_m4 | context | outdoor | outdoor | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | tree | trees | object | m5 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 04

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `02c946ea0b2e9479de9d69341333a30547d9be6f8b097766bcbe63dae0f94c14`
**parse_path:** `sentence`

> An older man and woman walk together on a city street, holding hands near a large building.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | older | old | visual_attribute | chunk0 | 1 | medium |
| m2 | object | woman | woman | noun_chunk_root | chunk1 | 4 | high |
| m3 | object | street | street | noun_chunk_root | chunk2 | 10 | high |
| m4 | attribute | city | city | compound_modifier | chunk2 | 9 | medium |
| m5 | object | hands | hand | noun_chunk_root | chunk3 | 13 | high |
| m6 | object | building | building | noun_chunk_root | chunk4 | 17 | high |
| m7 | attribute | large | large | size_attribute | chunk4 | 16 | high |
| m8 | action | walk | walk | verb_predicate | doc | 5 | high |
| m9 | action | holding | hold | verb_predicate | doc | 12 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> man |
| e1 | has_attribute | m3 | m4 | medium | chunk2 compound -> street |
| e2 | has_attribute | m6 | m7 | high | chunk4 amod -> building |
| e3 | agent | m8 | m0 | medium | nsubj -> walk |
| e4 | agent | m8 | m2 | medium | nsubj -> walk |
| e5 | agent | m9 | m0 | medium | inherited agent advcl -> walk |
| e6 | agent | m9 | m2 | medium | inherited agent advcl -> walk |
| e7 | patient | m9 | m5 | medium | dobj -> holding |
| e8 | relation | m0 | m3 | high | on |
| e9 | relation | m0 | m6 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | woman | woman | person | m2 | raw_mention |  |  |  |
| ent_m3 | object | street | street | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | hand | hands | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | building | building | object | m6 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | walk | walk | walk |  | agent:m0->ent_m0; agent:m2->ent_m2 |  |
| ce1 | m9 | holding | hold | hold |  | agent:m0->ent_m0; agent:m2->ent_m2; patient:m5->ent_m5 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | walk | agent | m0 | ent_m0 | medium | e3 | nsubj -> walk |  |  |
| ce0 | walk | agent | m2 | ent_m2 | medium | e4 | nsubj -> walk |  |  |
| ce1 | hold | agent | m0 | ent_m0 | medium | e5 | inherited agent advcl -> walk |  |  |
| ce1 | hold | agent | m2 | ent_m2 | medium | e6 | inherited agent advcl -> walk |  |  |
| ce1 | hold | patient | m5 | ent_m5 | medium | e7 | dobj -> holding |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | on | high | e8 | False | False |  |  |
| cr1 | m0 | m6 | ent_m0 | ent_m6 | near | high | e9 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 05

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `032d1400e70fdb9548f61e378f2ab55781a01ee044a329d1b8adb85bf7f43414`
**parse_path:** `sentence`

> A flooded street with water covering the road and submerging stop signs. A green digital sign stands in the background, with bare trees and a grassy hill visible beyond the floodwaters. The sky is overcast and gray.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | street | street | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | flooded | flooded | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | water | water | noun_chunk_root | chunk1 | 4 | high |
| m3 | object | road | road | noun_chunk_root | chunk2 | 7 | high |
| m4 | object | stop signs | stop_sign | noun_chunk_root | chunk3 | 10 | high |
| m5 | object | sign | sign | noun_chunk_root | chunk4 | 15 | high |
| m6 | attribute | green | green | color_attribute | chunk4 | 13 | high |
| m7 | attribute | digital | digital | modifier_attribute | chunk4 | 14 | medium |
| m8 | context | background | background | scene_context | chunk5 | 19 | high |
| m9 | object | trees | tree | noun_chunk_root | chunk6 | 23 | high |
| m10 | attribute | bare | bare | visual_attribute | chunk6 | 22 | medium |
| m11 | object | hill | hill | noun_chunk_root | chunk7 | 27 | high |
| m12 | attribute | grassy | grassy | modifier_attribute | chunk7 | 26 | medium |
| m13 | object | floodwaters | floodwater | noun_chunk_root | chunk8 | 31 | high |
| m14 | object | sky | sky | noun_chunk_root | chunk9 | 34 | high |
| m15 | action | covering | cover | verb_predicate | doc | 5 | high |
| m16 | action | submerging | submerge | verb_predicate | doc | 9 | high |
| m17 | action | stands | stand | verb_predicate | doc | 16 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> street |
| e1 | has_attribute | m5 | m6 | high | chunk4 amod -> sign |
| e2 | has_attribute | m5 | m7 | medium | chunk4 amod -> sign |
| e3 | has_context | scene | m8 | high | scene_context token background |
| e4 | has_attribute | m9 | m10 | medium | chunk6 amod -> trees |
| e5 | has_attribute | m11 | m12 | medium | chunk7 amod -> hill |
| e6 | agent | m15 | m2 | medium | nsubj -> covering |
| e7 | patient | m15 | m3 | medium | dobj -> covering |
| e8 | agent | m16 | m2 | medium | inherited agent conj -> covering |
| e9 | patient | m16 | m4 | medium | dobj -> submerging |
| e10 | agent | m17 | m5 | medium | nsubj -> stands |
| e11 | relation | m5 | m8 | high | in |
| e12 | relation | m5 | m9 | high | with |
| e13 | relation | m5 | m11 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | street | street | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | water | water | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | road | road | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | stop_sign | stop signs | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | sign | sign | document | m5 | raw_mention |  |  |  |
| ent_m8 | context | background | background | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | tree | trees | object | m9 | raw_mention |  |  |  |
| ent_m11 | object | hill | hill | object | m11 | raw_mention |  |  |  |
| ent_m13 | object | floodwater | floodwaters | object | m13 | raw_mention |  |  |  |
| ent_m14 | object | sky | sky | object | m14 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | covering | cover | cover |  | agent:m2->ent_m2; patient:m3->ent_m3 |  |
| ce1 | m16 | submerging | submerge | submerge |  | agent:m2->ent_m2; patient:m4->ent_m4 |  |
| ce2 | m17 | stands | stand | stand |  | agent:m5->ent_m5 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | cover | agent | m2 | ent_m2 | medium | e6 | nsubj -> covering |  |  |
| ce0 | cover | patient | m3 | ent_m3 | medium | e7 | dobj -> covering |  |  |
| ce1 | submerge | agent | m2 | ent_m2 | medium | e8 | inherited agent conj -> covering |  |  |
| ce1 | submerge | patient | m4 | ent_m4 | medium | e9 | dobj -> submerging |  |  |
| ce2 | stand | agent | m5 | ent_m5 | medium | e10 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m5 | m8 | ent_m5 | ent_m8 | in | high | e11 | False | False |  |  |
| cr1 | m5 | m9 | ent_m5 | ent_m9 | with | high | e12 | False | False |  |  |
| cr2 | m5 | m11 | ent_m5 | ent_m11 | with | high | e13 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 06

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `03736f3c4bc91505f93827beba8298b54e23d2d307312341f8de4f039291e014`
**parse_path:** `sentence`

> Three football players in blue and black uniforms stand on a grass field with white lines. They wear helmets and gloves, with snow visible along the sidelines and orange cones nearby. The background shows dark trees and a fence under dim lighting.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | football players | football_player | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Three | three | exact_quantity | chunk0 | 0 | high |
| m2 | object | uniforms | uniform | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | blue | blue | color_attribute | chunk1 | 3 | high |
| m4 | attribute | black | black | color_attribute | chunk1 | 5 | high |
| m5 | object | field | field | noun_chunk_root | chunk2 | 11 | high |
| m6 | attribute | grass | grass | compound_modifier | chunk2 | 10 | medium |
| m7 | object | lines | line | noun_chunk_root | chunk3 | 14 | high |
| m8 | attribute | white | white | color_attribute | chunk3 | 13 | high |
| m9 | object | helmets | helmet | noun_chunk_root | chunk5 | 18 | high |
| m10 | object | gloves | glove | noun_chunk_root | chunk6 | 20 | high |
| m11 | object | snow | snow | noun_chunk_root | chunk7 | 23 | high |
| m12 | object | sidelines | sideline | noun_chunk_root | chunk8 | 27 | high |
| m13 | object | cones | cone | noun_chunk_root | chunk9 | 30 | high |
| m14 | attribute | orange | orange | color_attribute | chunk9 | 29 | high |
| m15 | context | background | background | scene_context | chunk10 | 34 | high |
| m16 | object | trees | tree | noun_chunk_root | chunk11 | 37 | high |
| m17 | attribute | dark | dark | visual_attribute | chunk11 | 36 | medium |
| m18 | object | fence | fence | noun_chunk_root | chunk12 | 40 | high |
| m19 | object | lighting | lighting | noun_chunk_root | chunk13 | 43 | high |
| m20 | attribute | dim | dim | modifier_attribute | chunk13 | 42 | medium |
| m21 | action | stand | stand | verb_predicate | doc | 7 | high |
| m22 | action | wear | wear | verb_predicate | doc | 17 | high |
| m23 | action | shows | show | verb_predicate | doc | 35 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> football players |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> uniforms |
| e2 | has_attribute | m2 | m4 | high | chunk1 conj -> uniforms |
| e3 | has_attribute | m5 | m6 | medium | chunk2 compound -> field |
| e4 | has_attribute | m7 | m8 | high | chunk3 amod -> lines |
| e5 | has_attribute | m13 | m14 | high | chunk9 compound -> cones |
| e6 | has_context | scene | m15 | high | scene_context token background |
| e7 | has_attribute | m16 | m17 | medium | chunk11 amod -> trees |
| e8 | has_attribute | m19 | m20 | medium | chunk13 amod -> lighting |
| e9 | agent | m21 | m0 | medium | nsubj -> stand |
| e10 | agent | m22 | m0 | medium | nsubj -> wear; resolved They -> football players |
| e11 | patient | m22 | m9 | medium | dobj -> wear |
| e12 | patient | m22 | m10 | medium | dobj -> wear |
| e13 | agent | m23 | m15 | medium | nsubj -> shows |
| e14 | patient | m23 | m16 | medium | dobj -> shows |
| e15 | patient | m23 | m18 | medium | dobj -> shows |
| e16 | relation | m0 | m2 | high | in |
| e17 | relation | m0 | m5 | high | on |
| e18 | relation | m5 | m7 | high | with |
| e19 | relation | m0 | m11 | high | with |
| e20 | relation | m0 | m13 | high | with |
| e21 | relation | m16 | m19 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | football_player | football players | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | uniform | uniforms | clothing | m2 | raw_mention |  |  |  |
| ent_m5 | object | field | field | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | line | lines | object | m7 | raw_mention |  |  |  |
| ent_m9 | object | helmet | helmets | clothing | m9 | raw_mention |  |  |  |
| ent_m10 | object | glove | gloves | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | snow | snow | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | sideline | sidelines | object | m12 | raw_mention |  |  |  |
| ent_m13 | object | cone | cones | object | m13 | raw_mention |  |  |  |
| ent_m15 | context | background | background | object | m15 | raw_mention |  |  |  |
| ent_m16 | object | tree | trees | object | m16 | raw_mention |  |  |  |
| ent_m18 | object | fence | fence | object | m18 | raw_mention |  |  |  |
| ent_m19 | object | lighting | lighting | object | m19 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m21 | stand | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m22 | wear | wear | wear |  | agent:m0->ent_m0; patient:m9->ent_m9; patient:m10->ent_m10 |  |
| ce2 | m23 | shows | show | show |  | agent:m15->ent_m15; patient:m16->ent_m16; patient:m18->ent_m18 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e9 | nsubj -> stand |  |  |
| ce1 | wear | agent | m0 | ent_m0 | medium | e10 | nsubj -> wear; resolved They -> football players |  |  |
| ce1 | wear | patient | m9 | ent_m9 | medium | e11 | dobj -> wear |  |  |
| ce1 | wear | patient | m10 | ent_m10 | medium | e12 | dobj -> wear |  |  |
| ce2 | show | agent | m15 | ent_m15 | medium | e13 | nsubj -> shows |  |  |
| ce2 | show | patient | m16 | ent_m16 | medium | e14 | dobj -> shows |  |  |
| ce2 | show | patient | m18 | ent_m18 | medium | e15 | dobj -> shows |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | high | e16 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | high | e17 | False | False |  |  |
| cr2 | m5 | m7 | ent_m5 | ent_m7 | with | high | e18 | False | False |  |  |
| cr3 | m0 | m11 | ent_m0 | ent_m11 | with | high | e19 | False | False |  |  |
| cr4 | m0 | m13 | ent_m0 | ent_m13 | with | high | e20 | False | False |  |  |
| cr5 | m16 | m19 | ent_m16 | ent_m19 | under | high | e21 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 07

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `0457258811eff6ad31c0677c3d521527c46bd865e03f9c7a0f87b0f8f6229414`
**parse_path:** `sentence`

> Two people stand on a paved plaza near a tall green spire building under a clear blue sky. Several parked cars line the street to the right, with a parking sign visible beside a gray lamppost.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Two | two | exact_quantity | chunk0 | 0 | high |
| m2 | object | plaza | plaza | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | paved | paved | visual_attribute | chunk1 | 5 | medium |
| m4 | object | building | building | noun_chunk_root | chunk2 | 12 | high |
| m5 | attribute | tall | tall | size_attribute | chunk2 | 9 | high |
| m6 | attribute | green | green | color_attribute | chunk2 | 10 | high |
| m7 | attribute | spire | spire | compound_modifier | chunk2 | 11 | medium |
| m8 | object | sky | sky | noun_chunk_root | chunk3 | 17 | high |
| m9 | attribute | clear | clear | visual_attribute | chunk3 | 15 | medium |
| m10 | attribute | blue | blue | color_attribute | chunk3 | 16 | high |
| m11 | object | cars | car | noun_chunk_root | chunk4 | 21 | high |
| m12 | quantity | Several | several | approximate_quantity | chunk4 | 19 | medium |
| m13 | attribute | parked | park | state_attribute | chunk4 | 20 | medium |
| m14 | object | street | street | noun_chunk_root | chunk5 | 24 | high |
| m15 | context | right | right | spatial_region | chunk6 | 27 | medium |
| m16 | object | sign | sign | noun_chunk_root | chunk7 | 32 | high |
| m17 | attribute | parking | parking | compound_modifier | chunk7 | 31 | medium |
| m18 | object | lamppost | lamppost | noun_chunk_root | chunk8 | 37 | high |
| m19 | attribute | gray | gray | color_attribute | chunk8 | 36 | high |
| m20 | action | stand | stand | verb_predicate | doc | 2 | high |
| m21 | action | line | line | verb_predicate | doc | 22 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> people |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> plaza |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> building |
| e3 | has_attribute | m4 | m6 | high | chunk2 amod -> building |
| e4 | has_attribute | m4 | m7 | medium | chunk2 compound -> building |
| e5 | has_attribute | m8 | m9 | medium | chunk3 amod -> sky |
| e6 | has_attribute | m8 | m10 | high | chunk3 amod -> sky |
| e7 | has_quantity | m11 | m12 | medium | chunk4 quantity -> cars |
| e8 | has_attribute | m11 | m13 | medium | chunk4 amod -> cars |
| e9 | has_attribute | m16 | m17 | medium | chunk7 compound -> sign |
| e10 | has_attribute | m18 | m19 | high | chunk8 amod -> lamppost |
| e11 | agent | m20 | m0 | medium | nsubj -> stand |
| e12 | agent | m21 | m11 | medium | nsubj -> line |
| e13 | patient | m21 | m14 | medium | dobj -> line |
| e14 | relation | m0 | m2 | high | on |
| e15 | relation | m0 | m4 | high | near |
| e16 | relation | m0 | m8 | high | under |
| e17 | relation | m11 | m15 | medium | to |
| e18 | relation | m11 | m16 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | plaza | plaza | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | building | building | object | m4 | raw_mention |  |  |  |
| ent_m8 | object | sky | sky | object | m8 | raw_mention |  |  |  |
| ent_m11 | object | car | cars | vehicle | m11 | raw_mention |  |  |  |
| ent_m14 | object | street | street | object | m14 | raw_mention |  |  |  |
| ent_m15 | context | right | right | object | m15 | raw_mention |  |  |  |
| ent_m16 | object | sign | sign | document | m16 | raw_mention |  |  |  |
| ent_m18 | object | lamppost | lamppost | object | m18 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m20 | stand | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m21 | line | line | line |  | agent:m11->ent_m11; patient:m14->ent_m14 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e11 | nsubj -> stand |  |  |
| ce1 | line | agent | m11 | ent_m11 | medium | e12 | nsubj -> line |  |  |
| ce1 | line | patient | m14 | ent_m14 | medium | e13 | dobj -> line |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | high | e14 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | near | high | e15 | False | False |  |  |
| cr2 | m0 | m8 | ent_m0 | ent_m8 | under | high | e16 | False | False |  |  |
| cr3 | m11 | m15 | ent_m11 | ent_m15 | to | medium | e17 | False | False |  |  |
| cr4 | m11 | m16 | ent_m11 | ent_m16 | with | high | e18 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 08

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `047a4714002c7230c85d87adf7034ef1251a492dfd3e627182dd93db89a3ec14`
**parse_path:** `sentence`

> A woodpecker with black, white, and red feathers perches on a broken log in tall grass.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woodpecker | woodpecker | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | feathers | feather | noun_chunk_root | chunk1 | 9 | high |
| m2 | attribute | black | black | color_attribute | chunk1 | 3 | high |
| m3 | attribute | white | white | color_attribute | chunk1 | 5 | high |
| m4 | attribute | red | red | color_attribute | chunk1 | 8 | high |
| m5 | object | log | log | noun_chunk_root | chunk2 | 14 | high |
| m6 | attribute | broken | broken | modifier_attribute | chunk2 | 13 | medium |
| m7 | object | grass | grass | noun_chunk_root | chunk3 | 17 | high |
| m8 | attribute | tall | tall | size_attribute | chunk3 | 16 | high |
| m9 | action | perches | perch | verb_predicate | doc | 10 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> feathers |
| e1 | has_attribute | m1 | m3 | high | chunk1 conj -> feathers |
| e2 | has_attribute | m1 | m4 | high | chunk1 conj -> feathers |
| e3 | has_attribute | m5 | m6 | medium | chunk2 amod -> log |
| e4 | has_attribute | m7 | m8 | high | chunk3 amod -> grass |
| e5 | agent | m9 | m0 | medium | nsubj -> perches |
| e6 | relation | m0 | m1 | high | with |
| e7 | relation | m0 | m5 | high | on |
| e8 | relation | m0 | m7 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woodpecker | woodpecker | animal | m0 | raw_mention |  |  |  |
| ent_m1 | object | feather | feathers | object | m1 | raw_mention |  |  |  |
| ent_m5 | object | log | log | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | grass | grass | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | perches | perch | perch |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | perch | agent | m0 | ent_m0 | medium | e5 | nsubj -> perches |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | high | e6 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | high | e7 | False | False |  |  |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | in | high | e8 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 09

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `05e4cae85e91c5da230d50cb73b2525765091495a133f78a2330c5848367cc14`
**parse_path:** `tag_list`

> woman, purple pants, stone steps, classical building, autumn trees

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | segment_head | t0 | 0 | high |
| m1 | object | pants | pant | segment_head | t1 | 1 | high |
| m2 | attribute | purple | purple | attribute | t1 | 0 | high |
| m3 | object | steps | step | segment_head | t2 | 1 | high |
| m4 | attribute | stone | stone | attribute | t2 | 0 | high |
| m5 | object | building | building | segment_head | t3 | 1 | high |
| m6 | attribute | classical | classical | attribute | t3 | 0 | high |
| m7 | object | trees | tree | segment_head | t4 | 1 | high |
| m8 | attribute | autumn | autumn | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | t1 internal amod -> pants |
| e1 | has_attribute | m3 | m4 | high | t2 internal compound -> steps |
| e2 | has_attribute | m5 | m6 | high | t3 internal amod -> building |
| e3 | has_attribute | m7 | m8 | high | t4 internal compound -> trees |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | pant | pants | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | step | steps | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | building | building | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | tree | trees | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 10

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `06b01b3b3226df78be43c09a85d68cb1ddd08979194fea12f21255cab3d63c14`
**parse_path:** `tag_list`

> yellow sweater, child, drawing, green lockers

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | sweater | sweater | segment_head | t0 | 1 | high |
| m1 | attribute | yellow | yellow | attribute | t0 | 0 | high |
| m2 | object | child | child | segment_head | t1 | 0 | high |
| m3 | object | drawing | drawing | segment_head | t2 | 0 | high |
| m4 | object | lockers | locker | segment_head | t3 | 1 | high |
| m5 | attribute | green | green | attribute | t3 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> sweater |
| e1 | has_attribute | m4 | m5 | high | t3 internal amod -> lockers |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sweater | sweater | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | child | child | person | m2 | raw_mention |  |  |  |
| ent_m3 | object | drawing | drawing | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | locker | lockers | object | m4 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 11

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `06d84e7d9080d4a002071d8fc8f84e1108c9a315ae767d2c7c7015cad57c3414`
**parse_path:** `sentence`

> The image shows a page from a book with Russian text, listing numbered sections and titles like "Симбирская губерния" and "Войсковая система."

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "Симбирская губерния" | симбирская_губерния | quote_text | doc_quote | 18 | high |
| m1 | attribute | "Войсковая система." | войсковая_система. | quote_text | doc_quote | 20 | high |
| m2 | object | image | image | noun_chunk_root | chunk0 | 1 | high |
| m3 | object | page | page | noun_chunk_root | chunk1 | 4 | high |
| m4 | object | book | book | noun_chunk_root | chunk2 | 7 | high |
| m5 | object | text | text | noun_chunk_root | chunk3 | 10 | high |
| m6 | attribute | Russian | russian | modifier_attribute | chunk3 | 9 | medium |
| m7 | object | sections | section | noun_chunk_root | chunk4 | 14 | high |
| m8 | attribute | numbered | number | state_attribute | chunk4 | 13 | medium |
| m9 | object | titles | title | noun_chunk_root | chunk5 | 16 | high |
| m10 | action | shows | show | verb_predicate | doc | 2 | high |
| m11 | action | listing | list | verb_predicate | doc | 12 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m5 | m6 | medium | chunk3 amod -> text |
| e1 | has_attribute | m7 | m8 | medium | chunk4 amod -> sections |
| e2 | agent | m10 | m2 | medium | nsubj -> shows |
| e3 | patient | m10 | m3 | medium | dobj -> shows |
| e4 | agent | m11 | m2 | medium | inherited agent advcl -> shows |
| e5 | patient | m11 | m7 | medium | dobj -> listing |
| e6 | patient | m11 | m9 | medium | dobj -> listing |
| e7 | relation | m3 | m4 | medium | from |
| e8 | relation | m4 | m5 | high | with |
| e9 | relation | m9 | m0 | medium | like |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m2 | object | image | image | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | page | page | document | m3 | raw_mention |  |  |  |
| ent_m4 | object | book | book | document | m4 | raw_mention |  |  |  |
| ent_m5 | object | text | text | document | m5 | raw_mention |  |  |  |
| ent_m7 | object | section | sections | object | m7 | raw_mention |  |  |  |
| ent_m9 | object | title | titles | object | m9 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | shows | show | show |  | agent:m2->ent_m2; patient:m3->ent_m3 |  |
| ce1 | m11 | listing | list | list |  | agent:m2->ent_m2; patient:m7->ent_m7; patient:m9->ent_m9 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | m2 | ent_m2 | medium | e2 | nsubj -> shows |  |  |
| ce0 | show | patient | m3 | ent_m3 | medium | e3 | dobj -> shows |  |  |
| ce1 | list | agent | m2 | ent_m2 | medium | e4 | inherited agent advcl -> shows |  |  |
| ce1 | list | patient | m7 | ent_m7 | medium | e5 | dobj -> listing |  |  |
| ce1 | list | patient | m9 | ent_m9 | medium | e6 | dobj -> listing |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m3 | m4 | ent_m3 | ent_m4 | from | medium | e7 | False | False |  |  |
| cr1 | m4 | m5 | ent_m4 | ent_m5 | with | high | e8 | False | False |  |  |
| cr2 | m9 | m0 | ent_m9 |  | like | medium | e9 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 12

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `06decbdc22a2a9dc4dc57771004ad26736931badec1cbcd8ddfb1c57ac76c814`
**parse_path:** `tag_list`

> dancing people, indoor party, floral dress, denim jacket, raised arms

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | segment_head | t0 | 1 | high |
| m1 | attribute | dancing | dance | state_attribute | t0 | 0 | high |
| m2 | object | party | party | segment_head | t1 | 1 | high |
| m3 | attribute | indoor | indoor | attribute | t1 | 0 | high |
| m4 | object | dress | dress | segment_head | t2 | 1 | high |
| m5 | attribute | floral | floral | attribute | t2 | 0 | high |
| m6 | object | jacket | jacket | segment_head | t3 | 1 | high |
| m7 | attribute | denim | denim | attribute | t3 | 0 | high |
| m8 | object | arms | arm | segment_head | t4 | 1 | high |
| m9 | attribute | raised | raise | state_attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> people |
| e1 | has_attribute | m2 | m3 | high | t1 internal compound -> party |
| e2 | has_attribute | m4 | m5 | high | t2 internal compound -> dress |
| e3 | has_attribute | m6 | m7 | high | t3 internal compound -> jacket |
| e4 | has_attribute | m8 | m9 | high | t4 internal amod -> arms |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | party | party | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | dress | dress | clothing | m4 | raw_mention |  |  |  |
| ent_m6 | object | jacket | jacket | clothing | m6 | raw_mention |  |  |  |
| ent_m8 | object | arm | arms | object | m8 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 13

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `073090fa7e0c6c80f67ed0c260aa4cedcef5e326343311c80603a39aa3347014`
**parse_path:** `sentence`

> Players in red and maroon jerseys skate on an ice rink during a hockey game. A goalie stands near the net, while others maneuver with sticks across the ice, with “Oceanside Ice Arena” visible overhead.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “Oceanside Ice Arena” | oceanside_ice_arena | quote_text | doc_quote | 32 | high |
| m1 | object | Players | player | noun_chunk_root | chunk0 | 0 | high |
| m2 | object | jerseys | jersey | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | red | red | color_attribute | chunk1 | 2 | high |
| m4 | attribute | maroon | maroon | color_attribute | chunk1 | 4 | high |
| m5 | object | ice rink | ice_rink | noun_chunk_root | chunk2 | 9 | high |
| m6 | object | game | game | noun_chunk_root | chunk3 | 13 | high |
| m7 | attribute | hockey | hockey | compound_modifier | chunk3 | 12 | medium |
| m8 | object | goalie | goalie | noun_chunk_root | chunk4 | 16 | high |
| m9 | object | net | net | noun_chunk_root | chunk5 | 20 | high |
| m10 | object | sticks | stick | noun_chunk_root | chunk7 | 26 | high |
| m11 | object | ice | ice | noun_chunk_root | chunk8 | 29 | high |
| m12 | reference | others | other | contrastive_reference | nominal_reference | 23 | high |
| m13 | action | skate | skate | verb_predicate | doc | 6 | high |
| m14 | action | stands | stand | verb_predicate | doc | 17 | high |
| m15 | action | maneuver | maneuver | verb_predicate | doc | 24 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | chunk1 amod -> jerseys |
| e1 | has_attribute | m2 | m4 | high | chunk1 conj -> jerseys |
| e2 | has_attribute | m6 | m7 | medium | chunk3 compound -> game |
| e3 | refers_to | m12 | m1 | high | contrastive_reference others -> Players; score=100; margin=20 |
| e4 | agent | m13 | m1 | medium | nsubj -> skate |
| e5 | agent | m14 | m8 | medium | nsubj -> stands |
| e6 | agent | m15 | m1 | medium | nsubj -> maneuver; resolved others -> Players |
| e7 | relation | m1 | m2 | high | in |
| e8 | relation | m1 | m5 | high | on |
| e9 | relation | m1 | m6 | medium | during |
| e10 | relation | m8 | m9 | high | near |
| e11 | relation | m1 | m10 | high | with |
| e12 | relation | m1 | m11 | high | across |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | player | Players | person | m1 | raw_mention |  |  |  |
| ent_m2 | object | jersey | jerseys | clothing | m2 | raw_mention |  |  |  |
| ent_m5 | object | ice_rink | ice rink | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | game | game | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | goalie | goalie | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | net | net | object | m9 | raw_mention |  |  |  |
| ent_m10 | object | stick | sticks | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | ice | ice | object | m11 | raw_mention |  |  |  |
| eref_m12 | complement_subset | player | others | person | m12 | stage9_reference | ent_m1 |  | many |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m12 | eref_m12 | m1 | ent_m1 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m13 | skate | skate | skate |  | agent:m1->ent_m1 |  |
| ce1 | m14 | stands | stand | stand |  | agent:m8->ent_m8 |  |
| ce2 | m15 | maneuver | maneuver | maneuver |  | agent:m1->eref_m12 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | skate | agent | m1 | ent_m1 | medium | e4 | nsubj -> skate |  |  |
| ce1 | stand | agent | m8 | ent_m8 | medium | e5 | nsubj -> stands |  |  |
| ce2 | maneuver | agent | m1 | eref_m12 | medium | e6 | nsubj -> maneuver; resolved others -> Players |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | in | high | e7 | False | False |  |  |
| cr1 | m1 | m5 | ent_m1 | ent_m5 | on | high | e8 | False | False |  |  |
| cr2 | m1 | m6 | ent_m1 | ent_m6 | during | medium | e9 | False | False |  |  |
| cr3 | m8 | m9 | ent_m8 | ent_m9 | near | high | e10 | False | False |  |  |
| cr4 | m1 | m10 | ent_m1 | ent_m10 | with | high | e11 | False | False |  |  |
| cr5 | m1 | m11 | ent_m1 | ent_m11 | across | high | e12 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 14

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `074828240e5fe34cfa12b6a1e086f86792df9fb2aaea04ed2986bdf95ae0c014`
**parse_path:** `sentence`

> A flowing river rushes over rocks through a forested area. Autumn leaves in shades of orange and brown line the banks, with trees and bushes visible along the shoreline. The water moves quickly, creating white rapids as it flows past the rocky edge.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | river | river | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | flowing | flow | state_attribute | chunk0 | 1 | medium |
| m2 | object | rocks | rock | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | area | area | noun_chunk_root | chunk2 | 9 | high |
| m4 | attribute | forested | forested | modifier_attribute | chunk2 | 8 | medium |
| m5 | object | leaves | leaf | noun_chunk_root | chunk3 | 12 | high |
| m6 | attribute | Autumn | autumn | compound_modifier | chunk3 | 11 | medium |
| m7 | object | shades | shade | noun_chunk_root | chunk4 | 14 | high |
| m8 | attribute | orange | orange | color_attribute | chunk5 | 16 | high |
| m9 | attribute | brown | brown | color_attribute | chunk6 | 18 | high |
| m10 | object | banks | bank | noun_chunk_root | chunk7 | 21 | high |
| m11 | object | trees | tree | noun_chunk_root | chunk8 | 24 | high |
| m12 | object | bushes | bush | noun_chunk_root | chunk9 | 26 | high |
| m13 | object | shoreline | shoreline | noun_chunk_root | chunk10 | 30 | high |
| m14 | object | water | water | noun_chunk_root | chunk11 | 33 | high |
| m15 | object | rapids | rapid | noun_chunk_root | chunk12 | 39 | high |
| m16 | attribute | white | white | color_attribute | chunk12 | 38 | high |
| m17 | context | edge | edge | spatial_region | chunk14 | 46 | medium |
| m18 | action | rushes | rush | verb_predicate | doc | 3 | high |
| m19 | action | line | line | verb_predicate | doc | 19 | high |
| m20 | action | moves | move | verb_predicate | doc | 34 | high |
| m21 | action | creating | create | verb_predicate | doc | 37 | high |
| m22 | action | flows | flow | verb_predicate | doc | 42 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> river |
| e1 | has_attribute | m3 | m4 | medium | chunk2 amod -> area |
| e2 | has_attribute | m5 | m6 | medium | chunk3 compound -> leaves |
| e3 | has_attribute | m15 | m16 | high | chunk12 amod -> rapids |
| e4 | agent | m18 | m0 | medium | nsubj -> rushes |
| e5 | agent | m19 | m5 | medium | nsubj -> line |
| e6 | patient | m19 | m10 | medium | dobj -> line |
| e7 | agent | m20 | m14 | medium | nsubj -> moves |
| e8 | agent | m21 | m14 | medium | inherited agent advcl -> moves |
| e9 | patient | m21 | m15 | medium | dobj -> creating |
| e10 | agent | m22 | m11 | medium | nsubj -> flows; resolved it -> trees |
| e11 | relation | m0 | m2 | high | over |
| e12 | relation | m0 | m3 | medium | through |
| e13 | relation | m5 | m7 | high | in |
| e14 | relation | m11 | m17 | medium | past |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | river | river | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | rock | rocks | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | area | area | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | leaf | leaves | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | shade | shades | object | m7 | raw_mention |  |  |  |
| ent_m10 | object | bank | banks | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | tree | trees | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | bush | bushes | object | m12 | raw_mention |  |  |  |
| ent_m13 | object | shoreline | shoreline | object | m13 | raw_mention |  |  |  |
| ent_m14 | object | water | water | object | m14 | raw_mention |  |  |  |
| ent_m15 | object | rapid | rapids | object | m15 | raw_mention |  |  |  |
| ent_m17 | context | edge | edge | object | m17 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | rushes | rush | rush |  | agent:m0->ent_m0 |  |
| ce1 | m19 | line | line | line |  | agent:m5->ent_m5; patient:m10->ent_m10 |  |
| ce2 | m20 | moves | move | move |  | agent:m14->ent_m14 |  |
| ce3 | m21 | creating | create | create |  | agent:m14->ent_m14; patient:m15->ent_m15 |  |
| ce4 | m22 | flows | flow | flow |  | agent:m11->ent_m11 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | rush | agent | m0 | ent_m0 | medium | e4 | nsubj -> rushes |  |  |
| ce1 | line | agent | m5 | ent_m5 | medium | e5 | nsubj -> line |  |  |
| ce1 | line | patient | m10 | ent_m10 | medium | e6 | dobj -> line |  |  |
| ce2 | move | agent | m14 | ent_m14 | medium | e7 | nsubj -> moves |  |  |
| ce3 | create | agent | m14 | ent_m14 | medium | e8 | inherited agent advcl -> moves |  |  |
| ce3 | create | patient | m15 | ent_m15 | medium | e9 | dobj -> creating |  |  |
| ce4 | flow | agent | m11 | ent_m11 | medium | e10 | nsubj -> flows; resolved it -> trees |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | over | high | e11 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | through | medium | e12 | False | False |  |  |
| cr2 | m5 | m7 | ent_m5 | ent_m7 | in | high | e13 | False | False |  |  |
| cr3 | m11 | m17 | ent_m11 | ent_m17 | past | medium | e14 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 15

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `077ba6d8a231652e13b4231ec399624846c49c8e63d9d155fe9ed8275c884414`
**parse_path:** `sentence`

> Tall cacti and spiky plants grow inside a glass greenhouse.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | cacti | cactus | noun_chunk_root | chunk0 | 1 | high |
| m1 | attribute | Tall | tall | size_attribute | chunk0 | 0 | high |
| m2 | object | plants | plant | noun_chunk_root | chunk1 | 4 | high |
| m3 | attribute | spiky | spiky | modifier_attribute | chunk1 | 3 | medium |
| m4 | object | greenhouse | greenhouse | noun_chunk_root | chunk2 | 9 | high |
| m5 | attribute | glass | glass | material_attribute | chunk2 | 8 | high |
| m6 | action | grow | grow | verb_predicate | doc | 5 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> cacti |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> plants |
| e2 | has_attribute | m4 | m5 | high | chunk2 compound -> greenhouse |
| e3 | agent | m6 | m0 | medium | nsubj -> grow |
| e4 | agent | m6 | m2 | medium | nsubj -> grow |
| e5 | relation | m0 | m4 | high | inside |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | cactus | cacti | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | plant | plants | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | greenhouse | greenhouse | object | m4 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m6 | grow | grow | grow |  | agent:m0->ent_m0; agent:m2->ent_m2 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | grow | agent | m0 | ent_m0 | medium | e3 | nsubj -> grow |  |  |
| ce0 | grow | agent | m2 | ent_m2 | medium | e4 | nsubj -> grow |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | inside | high | e5 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 16

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `07c7561dff94b993369989b7144c59ce2fcd6473050e61d7fa93b75382bcf014`
**parse_path:** `sentence`

> A harvested field of dry wheat stretches toward a line of green trees, with a distant town visible on the horizon.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | field | field | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | harvested | harvest | state_attribute | chunk0 | 1 | medium |
| m2 | object | wheat | wheat | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | dry | dry | modifier_attribute | chunk1 | 4 | medium |
| m4 | object | line | line | noun_chunk_root | chunk2 | 9 | high |
| m5 | object | trees | tree | noun_chunk_root | chunk3 | 12 | high |
| m6 | attribute | green | green | color_attribute | chunk3 | 11 | high |
| m7 | object | town | town | noun_chunk_root | chunk4 | 17 | high |
| m8 | attribute | distant | distant | modifier_attribute | chunk4 | 16 | medium |
| m9 | object | horizon | horizon | noun_chunk_root | chunk5 | 21 | high |
| m10 | action | stretches | stretch | verb_predicate | doc | 6 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> field |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> wheat |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> trees |
| e3 | has_attribute | m7 | m8 | medium | chunk4 amod -> town |
| e4 | agent | m10 | m0 | medium | nsubj -> stretches |
| e5 | relation | m0 | m2 | medium | of |
| e6 | relation | m0 | m4 | medium | toward |
| e7 | relation | m4 | m5 | medium | of |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | field | field | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | wheat | wheat | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | line | line | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | tree | trees | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | town | town | object | m7 | raw_mention |  |  |  |
| ent_m9 | object | horizon | horizon | object | m9 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | stretches | stretch | stretch |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stretch | agent | m0 | ent_m0 | medium | e4 | nsubj -> stretches |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | of | medium | e5 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | toward | medium | e6 | False | False |  |  |
| cr2 | m4 | m5 | ent_m4 | ent_m5 | of | medium | e7 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 17

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `09c8d891bb19dae925f67bbfa36ab9cbab8992b837627c05b2737d7f93d0dc14`
**parse_path:** `tag_list`

> stained glass, crucifix, altar, church interior, wooden pews, candle

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | glass | glass | segment_head | t0 | 1 | high |
| m1 | attribute | stained | stained | attribute | t0 | 0 | high |
| m2 | object | crucifix | crucifix | segment_head | t1 | 0 | high |
| m3 | object | altar | altar | segment_head | t2 | 0 | high |
| m4 | object | interior | interior | segment_head | t3 | 1 | high |
| m5 | attribute | church | church | attribute | t3 | 0 | high |
| m6 | object | pews | pew | segment_head | t4 | 1 | high |
| m7 | attribute | wooden | wooden | attribute | t4 | 0 | high |
| m8 | object | candle | candle | segment_head | t5 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> glass |
| e1 | has_attribute | m4 | m5 | high | t3 internal compound -> interior |
| e2 | has_attribute | m6 | m7 | high | t4 internal compound -> pews |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | glass | glass | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | crucifix | crucifix | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | altar | altar | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | interior | interior | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | pew | pews | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | candle | candle | object | m8 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 18

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `09da0bd4c73bd7a26a8c552230082783f6c4e7edebcdb4ebf9015e90bfc5f814`
**parse_path:** `sentence`

> A person in a white Stormtrooper costume sits on the ground next to two children dressed as Pikachu. One child is fully in a yellow Pikachu outfit, while another wears a yellow hooded costume with red stripes. They are outdoors on a paved surface near a glass building with a yellow lamp nearby.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | costume | costume | noun_chunk_root | chunk1 | 6 | high |
| m2 | attribute | white | white | color_attribute | chunk1 | 4 | high |
| m3 | attribute | Stormtrooper | stormtrooper | compound_modifier | chunk1 | 5 | medium |
| m4 | object | ground | ground | noun_chunk_root | chunk2 | 10 | high |
| m5 | object | children | child | noun_chunk_root | chunk3 | 14 | high |
| m6 | quantity | two | two | exact_quantity | chunk3 | 13 | high |
| m7 | object | Pikachu | pikachu | noun_chunk_root | chunk4 | 17 | high |
| m8 | object | child | child | noun_chunk_root | chunk5 | 20 | high |
| m9 | quantity | One | one | exact_quantity | chunk5 | 19 | high |
| m10 | object | outfit | outfit | noun_chunk_root | chunk6 | 27 | high |
| m11 | attribute | yellow | yellow | color_attribute | chunk6 | 25 | high |
| m12 | attribute | Pikachu | pikachu | compound_modifier | chunk6 | 26 | medium |
| m13 | object | costume | costume | noun_chunk_root | chunk8 | 35 | high |
| m14 | attribute | yellow | yellow | color_attribute | chunk8 | 33 | high |
| m15 | attribute | hooded | hooded | modifier_attribute | chunk8 | 34 | medium |
| m16 | object | stripes | stripe | noun_chunk_root | chunk9 | 38 | high |
| m17 | attribute | red | red | color_attribute | chunk9 | 37 | high |
| m18 | object | paved surface | paved_surface | noun_chunk_root | chunk11 | 45 | high |
| m19 | object | building | building | noun_chunk_root | chunk12 | 49 | high |
| m20 | attribute | glass | glass | material_attribute | chunk12 | 48 | high |
| m21 | context | outdoors | outdoors | scene_context | doc | 42 | high |
| m22 | reference | another | another | contrastive_reference | nominal_reference | 30 | high |
| m23 | action | sits | sit | verb_predicate | doc | 7 | high |
| m24 | action | dressed | dress | verb_predicate | doc | 15 | high |
| m25 | action | wears | wear | verb_predicate | doc | 31 | high |
| m26 | object | lamp | lamp | with_absolute_recovered_object | with_absolute50 | 53 | medium |
| m27 | attribute | yellow | yellow | color_attribute | with_absolute50 | 52 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> costume |
| e1 | has_attribute | m1 | m3 | medium | chunk1 compound -> costume |
| e2 | has_quantity | m5 | m6 | high | chunk3 quantity -> children |
| e3 | has_quantity | m8 | m9 | high | chunk5 quantity -> child |
| e4 | has_attribute | m10 | m11 | high | chunk6 amod -> outfit |
| e5 | has_attribute | m10 | m12 | medium | chunk6 compound -> outfit |
| e6 | has_attribute | m13 | m14 | high | chunk8 amod -> costume |
| e7 | has_attribute | m13 | m15 | medium | chunk8 amod -> costume |
| e8 | has_attribute | m16 | m17 | high | chunk9 amod -> stripes |
| e9 | has_attribute | m19 | m20 | high | chunk12 compound -> building |
| e10 | has_context | scene | m21 | high | scene_context token outdoors |
| e11 | refers_to | m22 | m5 | high | contrastive_reference another -> children; score=108 |
| e12 | agent | m23 | m0 | medium | nsubj -> sits |
| e13 | agent | m24 | m5 | medium | inherited agent acl -> children |
| e14 | agent | m25 | m5 | medium | nsubj -> wears; resolved another -> children |
| e15 | patient | m25 | m13 | medium | dobj -> wears |
| e16 | scene_contains | scene | m26 | medium | with_absolute50 recovered lamp |
| e17 | has_attribute | m26 | m27 | high | with_absolute50 amod -> lamp |
| e18 | relation | m0 | m1 | high | in |
| e19 | relation | m0 | m4 | high | on |
| e20 | relation | m0 | m5 | high | next_to |
| e21 | relation | m5 | m7 | medium | as |
| e22 | relation | m8 | m10 | high | in |
| e23 | relation | m13 | m16 | high | with |
| e24 | relation | m8 | m18 | high | on |
| e25 | relation | m18 | m19 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | costume | costume | object | m1 | raw_mention |  |  |  |
| ent_m4 | object | ground | ground | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | child | children | person | m5 | raw_mention |  |  |  |
| ent_m7 | object | pikachu | Pikachu | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | child | child | person | m8 | raw_mention |  |  |  |
| ent_m10 | object | outfit | outfit | object | m10 | raw_mention |  |  |  |
| ent_m13 | object | costume | costume | object | m13 | raw_mention |  |  |  |
| ent_m16 | object | stripe | stripes | object | m16 | raw_mention |  |  |  |
| ent_m18 | object | paved_surface | paved surface | object | m18 | raw_mention |  |  |  |
| ent_m19 | object | building | building | object | m19 | raw_mention |  |  |  |
| ent_m21 | context | outdoors | outdoors | object | m21 | raw_mention |  |  |  |
| ent_m26 | object | lamp | lamp | object | m26 | raw_mention |  |  |  |
| eref_m22 | contrastive_instance | child | another | person | m22 | stage9_reference | ent_m5 |  | 1 |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m22 | eref_m22 | m5 | ent_m5 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m23 | sits | sit | sit |  | agent:m0->ent_m0 |  |
| ce1 | m24 | dressed | dress | dress |  | agent:m5->ent_m5 |  |
| ce2 | m25 | wears | wear | wear |  | agent:m5->eref_m22; patient:m13->ent_m13 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m0 | ent_m0 | medium | e12 | nsubj -> sits |  |  |
| ce1 | dress | agent | m5 | ent_m5 | medium | e13 | inherited agent acl -> children |  |  |
| ce2 | wear | agent | m5 | eref_m22 | medium | e14 | nsubj -> wears; resolved another -> children |  |  |
| ce2 | wear | patient | m13 | ent_m13 | medium | e15 | dobj -> wears |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e18 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | high | e19 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | next_to | high | e20 | False | False |  |  |
| cr3 | m5 | m7 | ent_m5 | ent_m7 | as | medium | e21 | False | False |  |  |
| cr4 | m8 | m10 | ent_m8 | ent_m10 | in | high | e22 | False | False |  |  |
| cr5 | m13 | m16 | ent_m13 | ent_m16 | with | high | e23 | False | False |  |  |
| cr6 | m8 | m18 | ent_m8 | ent_m18 | on | high | e24 | False | False |  |  |
| cr7 | m18 | m19 | ent_m18 | ent_m19 | near | high | e25 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 19

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `0b00d4baf64284f327aac70f21757bae78d0d363b89b04dd1d20d9c90b864814`
**parse_path:** `sentence`

> Two hockey players skate on the ice, one in a white jersey with number 93 and another in blue, near the goal.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hockey players | hockey_player | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Two | two | exact_quantity | chunk0 | 0 | high |
| m2 | object | ice | ice | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | jersey | jersey | noun_chunk_root | chunk2 | 11 | high |
| m4 | attribute | white | white | color_attribute | chunk2 | 10 | high |
| m5 | object | number | number | noun_chunk_root | chunk3 | 13 | high |
| m6 | object | goal | goal | noun_chunk_root | chunk5 | 22 | high |
| m7 | reference | one | one | singular_substitute | nominal_reference | 7 | high |
| m8 | reference | another | another | contrastive_reference | nominal_reference | 16 | high |
| m9 | action | skate | skate | verb_predicate | doc | 2 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> hockey players |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> jersey |
| e2 | refers_to | m7 | m0 | high | singular_substitute one -> hockey players; score=103 |
| e3 | refers_to | m8 | m0 | high | contrastive_reference another -> hockey players; score=112 |
| e4 | agent | m9 | m0 | medium | nsubj -> skate |
| e5 | relation | m0 | m2 | high | on |
| e6 | relation | m0 | m3 | high | in |
| e7 | relation | m3 | m5 | high | with |
| e8 | relation | m0 | m6 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hockey_player | hockey players | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | ice | ice | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | jersey | jersey | clothing | m3 | raw_mention |  |  |  |
| ent_m5 | object | number | number | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | goal | goal | object | m6 | raw_mention |  |  |  |
| eref_m7 | instance | hockey_player | one | object | m7 | stage9_reference | ent_m0 |  | 1 |
| eref_m8 | contrastive_instance | hockey_player | another | object | m8 | stage9_reference | ent_m0 |  | 1 |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m7 | eref_m7 | m0 | ent_m0 | high |  |
| refers_to | m8 | eref_m8 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | skate | skate | skate |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | skate | agent | m0 | ent_m0 | medium | e4 | nsubj -> skate |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | high | e5 | False | False |  |  |
| cr1 | m0 | m3 | eref_m7 | ent_m3 | in | high | e6 | False | False |  |  |
| cr2 | m3 | m5 | ent_m3 | ent_m5 | with | high | e7 | False | False |  |  |
| cr3 | m0 | m6 | eref_m8 | ent_m6 | near | high | e8 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 20

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `0bac1dd05b619aba37f1d15eedf4547bcfa902922da302c5d48e27264e25dc14`
**parse_path:** `sentence`

> A woman in a striped skirt and black blazer walks beside a man in a blue suit, both wearing face masks. They are in a large indoor hall with seated attendees, some wearing masks and holding papers, while others stand nearby.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | skirt | skirt | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | striped | striped | modifier_attribute | chunk1 | 4 | medium |
| m3 | object | blazer | blazer | noun_chunk_root | chunk2 | 8 | high |
| m4 | attribute | black | black | color_attribute | chunk2 | 7 | high |
| m5 | object | man | man | noun_chunk_root | chunk3 | 12 | high |
| m6 | object | suit | suit | noun_chunk_root | chunk4 | 16 | high |
| m7 | attribute | blue | blue | color_attribute | chunk4 | 15 | high |
| m8 | quantity | both | both | group_quantity | chunk5 | 18 | high |
| m9 | object | face masks | face_mask | noun_chunk_root | chunk6 | 20 | high |
| m10 | object | hall | hall | noun_chunk_root | chunk8 | 28 | high |
| m11 | attribute | large | large | size_attribute | chunk8 | 26 | high |
| m12 | attribute | indoor | indoor | modifier_attribute | chunk8 | 27 | medium |
| m13 | object | attendees | attendee | noun_chunk_root | chunk9 | 31 | high |
| m14 | attribute | seated | seat | state_attribute | chunk9 | 30 | medium |
| m15 | quantity | some | some | indefinite_quantity | chunk10 | 33 | medium |
| m16 | object | masks | mask | noun_chunk_root | chunk11 | 35 | high |
| m17 | object | papers | paper | noun_chunk_root | chunk12 | 38 | high |
| m18 | group | a striped skirt and black blazer | skirt_and_blazer | coordination_group | nominal_reference | 5 | medium |
| m19 | reference | both | both | group_reference | nominal_reference | 18 | medium |
| m20 | action | walks | walk | verb_predicate | doc | 9 | high |
| m21 | action | wearing | wear | verb_predicate | doc | 19 | high |
| m22 | action | wearing | wear | verb_predicate | doc | 34 | high |
| m23 | action | holding | hold | verb_predicate | doc | 37 | high |
| m24 | action | stand | stand | verb_predicate | doc | 42 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 amod -> skirt |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> blazer |
| e2 | has_attribute | m6 | m7 | high | chunk4 amod -> suit |
| e3 | has_attribute | m10 | m11 | high | chunk8 amod -> hall |
| e4 | has_attribute | m10 | m12 | medium | chunk8 amod -> hall |
| e5 | has_attribute | m13 | m14 | medium | chunk9 amod -> attendees |
| e6 | has_member | m18 | m1 | medium | coordination_group |
| e7 | has_member | m18 | m3 | medium | coordination_group |
| e8 | refers_to | m19 | m18 | medium | group_reference both -> a striped skirt and black blazer; score=77 |
| e9 | agent | m20 | m0 | medium | nsubj -> walks |
| e10 | agent | m21 | m18 | medium | nsubj -> wearing; resolved both -> a striped skirt and black blazer |
| e11 | patient | m21 | m9 | medium | dobj -> wearing |
| e12 | agent | m22 | m0 | medium | inherited agent advcl -> are |
| e13 | patient | m22 | m16 | medium | dobj -> wearing |
| e14 | patient | m23 | m17 | medium | dobj -> holding |
| e15 | agent | m24 | m0 | medium | inherited agent advcl -> are |
| e16 | relation | m0 | m1 | high | in |
| e17 | relation | m0 | m3 | high | in |
| e18 | relation | m0 | m5 | high | beside |
| e19 | relation | m5 | m6 | high | in |
| e20 | relation | m0 | m10 | high | in |
| e21 | relation | m10 | m13 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | skirt | skirt | clothing | m1 | raw_mention |  |  |  |
| ent_m3 | object | blazer | blazer | clothing | m3 | raw_mention |  |  |  |
| ent_m5 | object | man | man | person | m5 | raw_mention |  |  |  |
| ent_m6 | object | suit | suit | clothing | m6 | raw_mention |  |  |  |
| ent_m9 | object | face_mask | face masks | object | m9 | raw_mention |  |  |  |
| ent_m10 | object | hall | hall | object | m10 | raw_mention |  |  |  |
| ent_m13 | object | attendee | attendees | person | m13 | raw_mention |  |  |  |
| ent_m16 | object | mask | masks | clothing | m16 | raw_mention |  |  |  |
| ent_m17 | object | paper | papers | document | m17 | raw_mention |  |  |  |
| ent_m18 | group | skirt_and_blazer | a striped skirt and black blazer | group | m18 | raw_mention |  |  |  |
| eref_m19 | group | skirt_and_blazer | both | person | m19 | stage9_reference_group_repair | ent_m18 |  | 2 |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m19 | eref_m19 | m18 | ent_m18 | medium |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m20 | walks | walk | walk |  | agent:m0->ent_m0 |  |
| ce1 | m21 | wearing | wear | wear |  | agent:m18->eref_m19; patient:m9->ent_m9 |  |
| ce2 | m22 | wearing | wear | wear |  | agent:m0->ent_m0; patient:m16->ent_m16 |  |
| ce3 | m23 | holding | hold | hold |  | patient:m17->ent_m17 |  |
| ce4 | m24 | stand | stand | stand |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | walk | agent | m0 | ent_m0 | medium | e9 | nsubj -> walks |  |  |
| ce1 | wear | agent | m18 | eref_m19 | medium | e10 | nsubj -> wearing; resolved both -> a striped skirt and black blazer |  |  |
| ce1 | wear | patient | m9 | ent_m9 | medium | e11 | dobj -> wearing |  |  |
| ce2 | wear | agent | m0 | ent_m0 | medium | e12 | inherited agent advcl -> are |  |  |
| ce2 | wear | patient | m16 | ent_m16 | medium | e13 | dobj -> wearing |  |  |
| ce3 | hold | patient | m17 | ent_m17 | medium | e14 | dobj -> holding |  |  |
| ce4 | stand | agent | m0 | ent_m0 | medium | e15 | inherited agent advcl -> are |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e16 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | in | high | e17 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | beside | high | e18 | False | False |  |  |
| cr3 | m5 | m6 | ent_m5 | ent_m6 | in | high | e19 | False | False |  |  |
| cr4 | m0 | m10 | ent_m0 | ent_m10 | in | high | e20 | False | False |  |  |
| cr5 | m10 | m13 | ent_m10 | ent_m13 | with | high | e21 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 21

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `0cd0a6340659d0c6e6c98e141a5f55de3e04855c63a4223534c3a901cda62014`
**parse_path:** `sentence`

> A purple and white flower grows in the ground among brown leaves and green stems. The petals are slightly blurred, with a leaf visible to the right of the bloom. The setting appears to be outdoors on soil covered with fallen foliage.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | flower | flower | noun_chunk_root | chunk0 | 4 | high |
| m1 | attribute | purple | purple | color_attribute | chunk0 | 1 | high |
| m2 | attribute | white | white | color_attribute | chunk0 | 3 | high |
| m3 | object | ground | ground | noun_chunk_root | chunk1 | 8 | high |
| m4 | object | leaves | leaf | noun_chunk_root | chunk2 | 11 | high |
| m5 | attribute | brown | brown | color_attribute | chunk2 | 10 | high |
| m6 | object | stems | stem | noun_chunk_root | chunk3 | 14 | high |
| m7 | attribute | green | green | color_attribute | chunk3 | 13 | high |
| m8 | object | petals | petal | noun_chunk_root | chunk4 | 17 | high |
| m9 | object | leaf | leaf | noun_chunk_root | chunk5 | 24 | high |
| m10 | object | bloom | bloom | noun_chunk_root | chunk7 | 31 | high |
| m11 | context | setting | setting | scene_context | chunk8 | 34 | high |
| m12 | object | soil | soil | noun_chunk_root | chunk9 | 40 | high |
| m13 | object | foliage | foliage | noun_chunk_root | chunk10 | 44 | high |
| m14 | attribute | fallen | fallen | modifier_attribute | chunk10 | 43 | medium |
| m15 | context | outdoors | outdoors | scene_context | doc | 38 | high |
| m16 | action | grows | grow | verb_predicate | doc | 5 | high |
| m17 | action | appears | appear | verb_predicate | doc | 35 | high |
| m18 | action | covered | cover | verb_predicate | doc | 41 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> flower |
| e1 | has_attribute | m0 | m2 | high | chunk0 conj -> flower |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> leaves |
| e3 | has_attribute | m6 | m7 | high | chunk3 amod -> stems |
| e4 | has_context | scene | m11 | high | scene_context token setting |
| e5 | has_attribute | m13 | m14 | medium | chunk10 amod -> foliage |
| e6 | has_context | scene | m15 | high | scene_context token outdoors |
| e7 | agent | m16 | m0 | medium | nsubj -> grows |
| e8 | agent | m17 | m11 | medium | nsubj -> appears |
| e9 | agent | m18 | m12 | medium | inherited agent acl -> soil |
| e10 | relation | m0 | m3 | high | in |
| e11 | relation | m0 | m4 | medium | among |
| e12 | relation | m0 | m6 | medium | among |
| e13 | relation | m11 | m12 | high | on |
| e14 | relation | m12 | m13 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | flower | flower | object | m0 | raw_mention |  |  |  |
| ent_m3 | object | ground | ground | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | leaf | leaves | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | stem | stems | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | petal | petals | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | leaf | leaf | object | m9 | raw_mention |  |  |  |
| ent_m10 | object | bloom | bloom | object | m10 | raw_mention |  |  |  |
| ent_m11 | context | setting | setting | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | soil | soil | object | m12 | raw_mention |  |  |  |
| ent_m13 | object | foliage | foliage | object | m13 | raw_mention |  |  |  |
| ent_m15 | context | outdoors | outdoors | object | m15 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | grows | grow | grow |  | agent:m0->ent_m0 |  |
| ce1 | m17 | appears | appear | appear |  | agent:m11->ent_m11 |  |
| ce2 | m18 | covered | cover | cover |  | agent:m12->ent_m12 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | grow | agent | m0 | ent_m0 | medium | e7 | nsubj -> grows |  |  |
| ce1 | appear | agent | m11 | ent_m11 | medium | e8 | nsubj -> appears |  |  |
| ce2 | cover | agent | m12 | ent_m12 | medium | e9 | inherited agent acl -> soil |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | in | high | e10 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | among | medium | e11 | False | False |  |  |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | among | medium | e12 | False | False |  |  |
| cr3 | m11 | m12 | ent_m11 | ent_m12 | on | high | e13 | False | False |  |  |
| cr4 | m12 | m13 | ent_m12 | ent_m13 | with | high | e14 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 22

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `0ceed50090c9ce8a5cd15726d04e79d1a6dc4cacd28d488f8beceb4d54d88014`
**parse_path:** `tag_list`

> dewy spiderweb, tree branch, natural setting

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | spiderweb | spiderweb | segment_head | t0 | 1 | high |
| m1 | attribute | dewy | dewy | attribute | t0 | 0 | high |
| m2 | object | tree branch | tree_branch | segment_head | t1 | 0 | high |
| m3 | context | setting | setting | scene_context | t2 | 1 | high |
| m4 | attribute | natural | natural | attribute | t2 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> spiderweb |
| e1 | has_context | scene | m3 | high | t2 context tag |
| e2 | has_attribute | m3 | m4 | high | t2 internal amod -> setting |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | spiderweb | spiderweb | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | tree_branch | tree branch | object | m2 | raw_mention |  |  |  |
| ent_m3 | context | setting | setting | object | m3 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 23

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `0d9d490cb1767dc4b6125b1e58afff17e0debdfdc2972d218ea1b3295c06b014`
**parse_path:** `tag_list`

> night street, brick building, lit windows, traffic light, moon

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | street | street | segment_head | t0 | 1 | high |
| m1 | attribute | night | night | attribute | t0 | 0 | high |
| m2 | object | building | building | segment_head | t1 | 1 | high |
| m3 | attribute | brick | brick | attribute | t1 | 0 | high |
| m4 | object | windows | window | segment_head | t2 | 1 | high |
| m5 | attribute | lit | light | state_attribute | t2 | 0 | high |
| m6 | object | traffic light | traffic_light | segment_head | t3 | 0 | high |
| m7 | object | moon | moon | segment_head | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> street |
| e1 | has_attribute | m2 | m3 | high | t1 internal compound -> building |
| e2 | has_attribute | m4 | m5 | high | t2 internal amod -> windows |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | street | street | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | building | building | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | window | windows | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | traffic_light | traffic light | object | m6 | raw_mention |  |  |  |
| ent_m7 | object | moon | moon | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 24

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `0e22fd047812a642d9f5242be9ab5c1cacb81612bccb491c644cc77359b91814`
**parse_path:** `sentence`

> Several men run along a dirt path surrounded by trees. One in a black shirt is in the foreground, while another in a red shirt runs slightly behind him to the right.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | men | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Several | several | approximate_quantity | chunk0 | 0 | medium |
| m2 | object | path | path | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | dirt | dirt | compound_modifier | chunk1 | 5 | medium |
| m4 | object | trees | tree | noun_chunk_root | chunk2 | 9 | high |
| m5 | object | shirt | shirt | noun_chunk_root | chunk3 | 15 | high |
| m6 | attribute | black | black | color_attribute | chunk3 | 14 | high |
| m7 | context | foreground | foreground | scene_context | chunk4 | 19 | high |
| m8 | object | shirt | shirt | noun_chunk_root | chunk6 | 26 | high |
| m9 | attribute | red | red | color_attribute | chunk6 | 25 | high |
| m10 | context | right | right | spatial_region | chunk8 | 33 | medium |
| m11 | reference | another | another | contrastive_reference | nominal_reference | 22 | high |
| m12 | action | run | run | verb_predicate | doc | 2 | high |
| m13 | action | surrounded | surround | verb_predicate | doc | 7 | high |
| m14 | action | runs | run | verb_predicate | doc | 27 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | medium | chunk0 quantity -> men |
| e1 | has_attribute | m2 | m3 | medium | chunk1 compound -> path |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> shirt |
| e3 | has_context | scene | m7 | high | scene_context token foreground |
| e4 | has_attribute | m8 | m9 | high | chunk6 amod -> shirt |
| e5 | refers_to | m11 | m0 | high | contrastive_reference another -> men; score=110; margin=22 |
| e6 | agent | m12 | m0 | medium | nsubj -> run |
| e7 | agent | m13 | m2 | medium | inherited agent acl -> path |
| e8 | agent | m14 | m0 | medium | nsubj -> runs; resolved another -> men |
| e9 | relation | m0 | m2 | medium | along |
| e10 | relation | m2 | m4 | medium | by |
| e11 | relation | m0 | m8 | high | in |
| e12 | relation | m8 | m0 | medium | behind; repaired_self_edge_source from men |
| e13 | relation | m0 | m10 | medium | to |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | men | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | path | path | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | tree | trees | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | shirt | shirt | clothing | m5 | raw_mention |  |  |  |
| ent_m7 | context | foreground | foreground | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | shirt | shirt | clothing | m8 | raw_mention |  |  |  |
| ent_m10 | context | right | right | object | m10 | raw_mention |  |  |  |
| eref_m11 | contrastive_instance | man | another | person | m11 | stage9_reference | ent_m0 |  | 1 |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m11 | eref_m11 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | run | run | run |  | agent:m0->ent_m0 |  |
| ce1 | m13 | surrounded | surround | surround |  | agent:m2->ent_m2 |  |
| ce2 | m14 | runs | run | run |  | agent:m0->eref_m11 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | run | agent | m0 | ent_m0 | medium | e6 | nsubj -> run |  |  |
| ce1 | surround | agent | m2 | ent_m2 | medium | e7 | inherited agent acl -> path |  |  |
| ce2 | run | agent | m0 | eref_m11 | medium | e8 | nsubj -> runs; resolved another -> men |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | along | medium | e9 | False | False |  |  |
| cr1 | m2 | m4 | ent_m2 | ent_m4 | by | medium | e10 | False | False |  |  |
| cr2 | m0 | m8 | eref_m11 | ent_m8 | in | high | e11 | False | False |  |  |
| cr3 | m8 | m0 | ent_m8 | ent_m0 | behind; repaired_self_edge_source from men | medium | e12 | False | False |  |  |
| cr4 | m0 | m10 | ent_m0 | ent_m10 | to | medium | e13 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 25

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `0e5e8ad31536aeeecbdd2699187c6ab85dbe278b1be0430def4d0f36428d3c14`
**parse_path:** `tag_list`

> brown couch, tiled floor, man, child, living room

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | couch | couch | segment_head | t0 | 1 | high |
| m1 | attribute | brown | brown | attribute | t0 | 0 | high |
| m2 | object | floor | floor | segment_head | t1 | 1 | high |
| m3 | attribute | tiled | tile | state_attribute | t1 | 0 | high |
| m4 | object | man | man | tag_list_person_object_override | t2 | 0 | high |
| m5 | object | child | child | segment_head | t3 | 0 | high |
| m6 | object | living room | living_room | segment_head | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> couch |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> floor |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | couch | couch | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | floor | floor | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | man | man | person | m4 | raw_mention |  |  |  |
| ent_m5 | object | child | child | person | m5 | raw_mention |  |  |  |
| ent_m6 | object | living_room | living room | object | m6 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 26

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `0f8f058deb2e280719cd84a3bbe67a8e80c6a0098904dfef002b76f2c49e4814`
**parse_path:** `sentence`

> A snow-covered staircase with rusted metal railings leads upward. Snow piles on both sides, and bare trees stand beside the steps under a cloudy sky. A building with shutters is visible in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | staircase | staircase | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | snow-covered | snow-covered | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | railings | railing | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | rusted | rusted | modifier_attribute | chunk1 | 4 | medium |
| m4 | attribute | metal | metal | material_attribute | chunk1 | 5 | high |
| m5 | object | piles | pile | noun_chunk_root | chunk2 | 11 | high |
| m6 | attribute | Snow | snow | compound_modifier | chunk2 | 10 | medium |
| m7 | context | sides | side | spatial_region | chunk3 | 14 | medium |
| m8 | object | trees | tree | noun_chunk_root | chunk4 | 18 | high |
| m9 | attribute | bare | bare | visual_attribute | chunk4 | 17 | medium |
| m10 | object | steps | step | noun_chunk_root | chunk5 | 22 | high |
| m11 | object | sky | sky | noun_chunk_root | chunk6 | 26 | high |
| m12 | attribute | cloudy | cloudy | modifier_attribute | chunk6 | 25 | medium |
| m13 | object | building | building | noun_chunk_root | chunk7 | 29 | high |
| m14 | object | shutters | shutter | noun_chunk_root | chunk8 | 31 | high |
| m15 | context | background | background | scene_context | chunk9 | 36 | high |
| m16 | action | leads | lead | verb_predicate | doc | 7 | high |
| m17 | action | stand | stand | verb_predicate | doc | 19 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> staircase |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> railings |
| e2 | has_attribute | m2 | m4 | high | chunk1 compound -> railings |
| e3 | has_attribute | m5 | m6 | medium | chunk2 compound -> piles |
| e4 | has_attribute | m8 | m9 | medium | chunk4 amod -> trees |
| e5 | has_attribute | m11 | m12 | medium | chunk6 amod -> sky |
| e6 | has_context | scene | m15 | high | scene_context token background |
| e7 | agent | m16 | m0 | medium | nsubj -> leads |
| e8 | agent | m17 | m8 | medium | nsubj -> stand |
| e9 | relation | m0 | m2 | high | with |
| e10 | relation | m5 | m7 | high | on |
| e11 | relation | m8 | m10 | high | beside |
| e12 | relation | m8 | m11 | high | under |
| e13 | relation | m13 | m14 | high | with |
| e14 | relation | m13 | m15 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | staircase | staircase | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | railing | railings | object | m2 | raw_mention |  |  |  |
| ent_m5 | object | pile | piles | object | m5 | raw_mention |  |  |  |
| ent_m7 | context | side | sides | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | tree | trees | object | m8 | raw_mention |  |  |  |
| ent_m10 | object | step | steps | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | sky | sky | object | m11 | raw_mention |  |  |  |
| ent_m13 | object | building | building | object | m13 | raw_mention |  |  |  |
| ent_m14 | object | shutter | shutters | object | m14 | raw_mention |  |  |  |
| ent_m15 | context | background | background | object | m15 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | leads | lead | lead |  | agent:m0->ent_m0 |  |
| ce1 | m17 | stand | stand | stand |  | agent:m8->ent_m8 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | lead | agent | m0 | ent_m0 | medium | e7 | nsubj -> leads |  |  |
| ce1 | stand | agent | m8 | ent_m8 | medium | e8 | nsubj -> stand |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e9 | False | False |  |  |
| cr1 | m5 | m7 | ent_m5 | ent_m7 | on | high | e10 | False | False |  |  |
| cr2 | m8 | m10 | ent_m8 | ent_m10 | beside | high | e11 | False | False |  |  |
| cr3 | m8 | m11 | ent_m8 | ent_m11 | under | high | e12 | False | False |  |  |
| cr4 | m13 | m14 | ent_m13 | ent_m14 | with | high | e13 | False | False |  |  |
| cr5 | m13 | m15 | ent_m13 | ent_m15 | in | high | e14 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 27

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `0fabd5c8b164bc555ab91c3009991f7f72fba0b91c0f61887d48ead2cf639814`
**parse_path:** `sentence`

> A German Shepherd with a red collar walks forward on a paved surface. Several other dogs are nearby, including one lying down and others standing or moving around. A person in jeans stands in the background near a large black tunnel.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | Shepherd | shepherd | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | German | german | compound_modifier | chunk0 | 1 | medium |
| m2 | object | collar | collar | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | red | red | color_attribute | chunk1 | 5 | high |
| m4 | object | paved surface | paved_surface | noun_chunk_root | chunk2 | 11 | high |
| m5 | object | dogs | dog | noun_chunk_root | chunk3 | 15 | high |
| m6 | quantity | Several | several | approximate_quantity | chunk3 | 13 | medium |
| m7 | attribute | other | other | modifier_attribute | chunk3 | 14 | medium |
| m8 | object | person | person | noun_chunk_root | chunk5 | 31 | high |
| m9 | object | jeans | jean | noun_chunk_root | chunk6 | 33 | high |
| m10 | context | background | background | scene_context | chunk7 | 37 | high |
| m11 | object | tunnel | tunnel | noun_chunk_root | chunk8 | 42 | high |
| m12 | attribute | large | large | size_attribute | chunk8 | 40 | high |
| m13 | attribute | black | black | color_attribute | chunk8 | 41 | high |
| m14 | reference | one | one | singular_substitute | nominal_reference | 20 | high |
| m15 | reference | others | other | contrastive_reference | nominal_reference | 24 | high |
| m16 | action | walks | walk | verb_predicate | doc | 7 | high |
| m17 | action | including | include | verb_predicate | doc | 19 | high |
| m18 | action | lying | lie | verb_predicate | doc | 21 | high |
| m19 | action | standing | stand | verb_predicate | doc | 25 | high |
| m20 | action | moving | move | verb_predicate | doc | 27 | high |
| m21 | action | stands | stand | verb_predicate | doc | 34 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 compound -> Shepherd |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> collar |
| e2 | has_quantity | m5 | m6 | medium | chunk3 quantity -> dogs |
| e3 | has_attribute | m5 | m7 | medium | chunk3 amod -> dogs |
| e4 | has_context | scene | m10 | high | scene_context token background |
| e5 | has_attribute | m11 | m12 | high | chunk8 amod -> tunnel |
| e6 | has_attribute | m11 | m13 | high | chunk8 amod -> tunnel |
| e7 | refers_to | m14 | m5 | high | singular_substitute one -> dogs; score=103 |
| e8 | refers_to | m15 | m5 | high | contrastive_reference others -> dogs; score=102 |
| e9 | agent | m16 | m0 | medium | nsubj -> walks |
| e10 | agent | m17 | m5 | medium | inherited agent prep -> dogs |
| e11 | agent | m18 | m5 | medium | inherited agent acl -> one |
| e12 | agent | m19 | m5 | medium | inherited agent acl -> others |
| e13 | agent | m20 | m5 | medium | inherited agent conj -> standing |
| e14 | agent | m21 | m8 | medium | nsubj -> stands |
| e15 | relation | m0 | m2 | high | with |
| e16 | relation | m0 | m4 | high | on |
| e17 | relation | m8 | m9 | high | in |
| e18 | relation | m8 | m10 | high | in |
| e19 | relation | m8 | m11 | high | near |

### Skipped Raw Concept Edges
| type | source | target | confidence | reason | evidence |
| --- | --- | --- | --- | --- | --- |
| patient | m17 | m5 | medium | pronoun_resolved_to_action_agent | pobj -> including; resolved one -> dogs |
| patient | m17 | m5 | medium | pronoun_resolved_to_action_agent | pobj -> including; resolved others -> dogs |
| relation | m5 | m5 | medium | self_edge_after_coref | include |
| relation | m5 | m5 | medium | self_edge_after_coref | include |

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | shepherd | Shepherd | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | collar | collar | clothing | m2 | raw_mention |  |  |  |
| ent_m4 | object | paved_surface | paved surface | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | dog | dogs | animal | m5 | raw_mention |  |  |  |
| ent_m8 | object | person | person | person | m8 | raw_mention |  |  |  |
| ent_m9 | object | jean | jeans | object | m9 | raw_mention |  |  |  |
| ent_m10 | context | background | background | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | tunnel | tunnel | object | m11 | raw_mention |  |  |  |
| eref_m14 | instance | dog | one | animal | m14 | stage9_reference | ent_m5 |  | 1 |
| eref_m15 | complement_subset | dog | others | animal | m15 | stage9_reference | ent_m5 |  | many |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m14 | eref_m14 | m5 | ent_m5 | high |  |
| refers_to | m15 | eref_m15 | m5 | ent_m5 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | walks | walk | walk |  | agent:m0->ent_m0 |  |
| ce1 | m17 | including | include | include |  | agent:m5->ent_m5; patient:m5->eref_m14; patient:m5->eref_m15 |  |
| ce2 | m18 | lying | lie | lie |  | agent:m5->eref_m14 |  |
| ce3 | m19 | standing | stand | stand |  | agent:m5->eref_m15 |  |
| ce4 | m20 | moving | move | move |  | agent:m5->eref_m15 |  |
| ce5 | m21 | stands | stand | stand |  | agent:m8->ent_m8 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | walk | agent | m0 | ent_m0 | medium | e9 | nsubj -> walks |  |  |
| ce1 | include | agent | m5 | ent_m5 | medium | e10 | inherited agent prep -> dogs |  |  |
| ce1 | include | patient | m5 | eref_m14 | medium |  | pobj -> including; resolved one -> dogs | pronoun_resolved_to_action_agent |  |
| ce1 | include | patient | m5 | eref_m15 | medium |  | pobj -> including; resolved others -> dogs | pronoun_resolved_to_action_agent |  |
| ce2 | lie | agent | m5 | eref_m14 | medium | e11 | inherited agent acl -> one |  |  |
| ce3 | stand | agent | m5 | eref_m15 | medium | e12 | inherited agent acl -> others |  |  |
| ce4 | move | agent | m5 | eref_m15 | medium | e13 | inherited agent conj -> standing |  | conj_agent_inherited_from_reference_canonical_target |
| ce5 | stand | agent | m8 | ent_m8 | medium | e14 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e15 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | high | e16 | False | False |  |  |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | in | high | e17 | False | False |  |  |
| cr3 | m8 | m10 | ent_m8 | ent_m10 | in | high | e18 | False | False |  |  |
| cr4 | m8 | m11 | ent_m8 | ent_m11 | near | high | e19 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| skipped_reference_role_recovered | m17 |  |  | eref_m14 | pronoun_resolved_to_action_agent | {"action_mention_id": "m17", "canonical_target": "eref_m14", "kind": "skipped_reference_role_recovered", "reason": "pronoun_resolved_to_action_agent", "role": "patient"} |
| skipped_reference_role_recovered | m17 |  |  | eref_m15 | pronoun_resolved_to_action_agent | {"action_mention_id": "m17", "canonical_target": "eref_m15", "kind": "skipped_reference_role_recovered", "reason": "pronoun_resolved_to_action_agent", "role": "patient"} |
| conj_agent_reference_target_inherited | m20 |  |  | eref_m15 |  | {"action_mention_id": "m20", "canonical_target": "eref_m15", "kind": "conj_agent_reference_target_inherited", "source_action_mention_id": "m19"} |

## 28

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `0fadd618f87235c9ee60220033aa5ac51148647eec5e8beb535c4eb6a4a4f814`
**parse_path:** `sentence`

> Three water polo players swim in a pool, with one wearing a black cap marked '12'.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | players | player | noun_chunk_root | chunk0 | 3 | high |
| m1 | quantity | Three | three | exact_quantity | chunk0 | 0 | high |
| m2 | attribute | water | water | compound_modifier | chunk0 | 1 | medium |
| m3 | attribute | polo | polo | compound_modifier | chunk0 | 2 | medium |
| m4 | object | pool | pool | noun_chunk_root | chunk1 | 7 | high |
| m5 | object | cap | cap | noun_chunk_root | chunk2 | 14 | high |
| m6 | attribute | black | black | color_attribute | chunk2 | 13 | high |
| m7 | reference | one | one | singular_substitute | nominal_reference | 10 | high |
| m8 | action | swim | swim | verb_predicate | doc | 4 | high |
| m9 | action | wearing | wear | verb_predicate | doc | 11 | high |
| m10 | action | marked | mark | verb_predicate | doc | 15 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> players |
| e1 | has_attribute | m0 | m2 | medium | chunk0 compound -> players |
| e2 | has_attribute | m0 | m3 | medium | chunk0 compound -> players |
| e3 | has_attribute | m5 | m6 | high | chunk2 amod -> cap |
| e4 | refers_to | m7 | m0 | high | singular_substitute one -> players; score=103 |
| e5 | agent | m8 | m0 | medium | nsubj -> swim |
| e6 | agent | m9 | m0 | medium | inherited agent acl -> one |
| e7 | patient | m9 | m5 | medium | dobj -> wearing |
| e8 | agent | m10 | m5 | medium | inherited agent acl -> cap |
| e9 | relation | m0 | m4 | high | in |

### Skipped Raw Concept Edges
| type | source | target | confidence | reason | evidence |
| --- | --- | --- | --- | --- | --- |
| relation | m0 | m0 | high | self_edge_after_coref | with |

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | player | players | person | m0 | raw_mention |  |  |  |
| ent_m4 | object | pool | pool | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | cap | cap | clothing | m5 | raw_mention |  |  |  |
| eref_m7 | instance | player | one | person | m7 | stage9_reference | ent_m0 |  | 1 |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m7 | eref_m7 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | swim | swim | swim |  | agent:m0->ent_m0 |  |
| ce1 | m9 | wearing | wear | wear |  | agent:m0->eref_m7; patient:m5->ent_m5 |  |
| ce2 | m10 | marked | mark | mark |  | agent:m5->ent_m5 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | swim | agent | m0 | ent_m0 | medium | e5 | nsubj -> swim |  |  |
| ce1 | wear | agent | m0 | eref_m7 | medium | e6 | inherited agent acl -> one |  |  |
| ce1 | wear | patient | m5 | ent_m5 | medium | e7 | dobj -> wearing |  |  |
| ce2 | mark | agent | m5 | ent_m5 | medium | e8 | inherited agent acl -> cap |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | in | high | e9 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 29

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `10de106710cb2aaf0f5016f7ee9ac5f8e67a647da0dc248e18da28947b17a014`
**parse_path:** `sentence`

> A diagram shows different views of a futuristic aircraft with labeled parts and directional arrows.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | diagram | diagram | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | views | view | noun_chunk_root | chunk1 | 4 | high |
| m2 | attribute | different | different | modifier_attribute | chunk1 | 3 | medium |
| m3 | object | aircraft | aircraft | noun_chunk_root | chunk2 | 8 | high |
| m4 | attribute | futuristic | futuristic | modifier_attribute | chunk2 | 7 | medium |
| m5 | object | parts | part | noun_chunk_root | chunk3 | 11 | high |
| m6 | attribute | labeled | label | state_attribute | chunk3 | 10 | medium |
| m7 | object | arrows | arrow | noun_chunk_root | chunk4 | 14 | high |
| m8 | attribute | directional | directional | modifier_attribute | chunk4 | 13 | medium |
| m9 | action | shows | show | verb_predicate | doc | 2 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 amod -> views |
| e1 | has_attribute | m3 | m4 | medium | chunk2 amod -> aircraft |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> parts |
| e3 | has_attribute | m7 | m8 | medium | chunk4 amod -> arrows |
| e4 | agent | m9 | m0 | medium | nsubj -> shows |
| e5 | patient | m9 | m1 | medium | dobj -> shows |
| e6 | relation | m1 | m3 | medium | of |
| e7 | relation | m1 | m5 | high | with |
| e8 | relation | m1 | m7 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | diagram | diagram | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | view | views | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | aircraft | aircraft | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | part | parts | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | arrow | arrows | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | shows | show | show |  | agent:m0->ent_m0; patient:m1->ent_m1 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | m0 | ent_m0 | medium | e4 | nsubj -> shows |  |  |
| ce0 | show | patient | m1 | ent_m1 | medium | e5 | dobj -> shows |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m3 | ent_m1 | ent_m3 | of | medium | e6 | False | False |  |  |
| cr1 | m1 | m5 | ent_m1 | ent_m5 | with | high | e7 | False | False |  |  |
| cr2 | m1 | m7 | ent_m1 | ent_m7 | with | high | e8 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 30

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `11d48be4d3ad5ca7a05c8076bc307685d865102be7417777129b9bff63465414`
**parse_path:** `sentence`

> An ornate stone archway with carvings is set into a beige building wall. To its left, a red-framed window and a black chalkboard sign stand beside a small metal trash can. A green plaque is mounted on the right side of the arch.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | archway | archway | noun_chunk_root | chunk0 | 3 | high |
| m1 | attribute | ornate | ornate | modifier_attribute | chunk0 | 1 | medium |
| m2 | attribute | stone | stone | material_attribute | chunk0 | 2 | high |
| m3 | object | carvings | carving | noun_chunk_root | chunk1 | 5 | high |
| m4 | object | wall | wall | noun_chunk_root | chunk2 | 12 | high |
| m5 | attribute | beige | beige | color_attribute | chunk2 | 10 | high |
| m6 | attribute | building | building | compound_modifier | chunk2 | 11 | medium |
| m7 | context | left | left | spatial_region | chunk3 | 16 | medium |
| m8 | object | window | window | noun_chunk_root | chunk4 | 20 | high |
| m9 | attribute | red-framed | red-framed | modifier_attribute | chunk4 | 19 | medium |
| m10 | object | sign | sign | noun_chunk_root | chunk5 | 25 | high |
| m11 | attribute | black | black | color_attribute | chunk5 | 23 | high |
| m12 | attribute | chalkboard | chalkboard | compound_modifier | chunk5 | 24 | medium |
| m13 | object | trash can | trash_can | noun_chunk_root | chunk6 | 31 | high |
| m14 | attribute | small | small | size_attribute | chunk6 | 29 | high |
| m15 | attribute | metal | metal | material_attribute | chunk6 | 30 | high |
| m16 | object | plaque | plaque | noun_chunk_root | chunk7 | 35 | high |
| m17 | attribute | green | green | color_attribute | chunk7 | 34 | high |
| m18 | context | side | side | spatial_region | chunk8 | 41 | medium |
| m19 | object | arch | arch | noun_chunk_root | chunk9 | 44 | high |
| m20 | action | set | set | verb_predicate | doc | 7 | high |
| m21 | action | stand | stand | verb_predicate | doc | 26 | high |
| m22 | action | mounted | mount | verb_predicate | doc | 37 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> archway |
| e1 | has_attribute | m0 | m2 | high | chunk0 compound -> archway |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> wall |
| e3 | has_attribute | m4 | m6 | medium | chunk2 compound -> wall |
| e4 | has_attribute | m8 | m9 | medium | chunk4 amod -> window |
| e5 | has_attribute | m10 | m11 | high | chunk5 amod -> sign |
| e6 | has_attribute | m10 | m12 | medium | chunk5 compound -> sign |
| e7 | has_attribute | m13 | m14 | high | chunk6 amod -> trash can |
| e8 | has_attribute | m13 | m15 | high | chunk6 compound -> trash can |
| e9 | has_attribute | m16 | m17 | high | chunk7 amod -> plaque |
| e10 | agent | m20 | m0 | medium | nsubjpass -> set |
| e11 | agent | m21 | m8 | medium | nsubj -> stand |
| e12 | agent | m21 | m10 | medium | nsubj -> stand |
| e13 | agent | m22 | m16 | medium | nsubjpass -> mounted |
| e14 | relation | m0 | m3 | high | with |
| e15 | relation | m0 | m4 | medium | into |
| e16 | relation | m8 | m7 | medium | to |
| e17 | relation | m8 | m13 | high | beside |
| e18 | relation | m16 | m18 | high | on |
| e19 | relation | m18 | m19 | medium | of |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | archway | archway | object | m0 | raw_mention |  |  |  |
| ent_m3 | object | carving | carvings | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | wall | wall | object | m4 | raw_mention |  |  |  |
| ent_m7 | context | left | left | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | window | window | object | m8 | raw_mention |  |  |  |
| ent_m10 | object | sign | sign | document | m10 | raw_mention |  |  |  |
| ent_m13 | object | trash_can | trash can | object | m13 | raw_mention |  |  |  |
| ent_m16 | object | plaque | plaque | document | m16 | raw_mention |  |  |  |
| ent_m18 | context | side | side | object | m18 | raw_mention |  |  |  |
| ent_m19 | object | arch | arch | object | m19 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m20 | set | set | set |  | theme:m0->ent_m0 |  |
| ce1 | m21 | stand | stand | stand |  | agent:m8->ent_m8; agent:m10->ent_m10 |  |
| ce2 | m22 | mounted | mount | mount |  | theme:m16->ent_m16 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | set | theme | m0 | ent_m0 | medium | e10 | nsubjpass -> set |  |  |
| ce1 | stand | agent | m8 | ent_m8 | medium | e11 | nsubj -> stand |  |  |
| ce1 | stand | agent | m10 | ent_m10 | medium | e12 | nsubj -> stand |  |  |
| ce2 | mount | theme | m16 | ent_m16 | medium | e13 | nsubjpass -> mounted |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | with | high | e14 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | into | medium | e15 | False | False |  |  |
| cr2 | m8 | m7 | ent_m8 | ent_m7 | to | medium | e16 | False | False |  |  |
| cr3 | m8 | m13 | ent_m8 | ent_m13 | beside | high | e17 | False | False |  |  |
| cr4 | m16 | m18 | ent_m16 | ent_m18 | on | high | e18 | False | False |  |  |
| cr5 | m18 | m19 | ent_m18 | ent_m19 | of | medium | e19 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m20 | e10 | m0 |  |  | {"action_mention_id": "m20", "kind": "passive_subject_to_theme", "raw_edge_id": "e10", "target": "m0"} |
| passive_subject_to_theme | m22 | e13 | m16 |  |  | {"action_mention_id": "m22", "kind": "passive_subject_to_theme", "raw_edge_id": "e13", "target": "m16"} |

## 31

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `12961bafd17111c4818794da65cc4639924bca427bfced0b4ea1fb386e7d1c14`
**parse_path:** `sentence`

> A vibrant pink flower with long petals stands tall against a blurred green background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | flower | flower | noun_chunk_root | chunk0 | 3 | high |
| m1 | attribute | vibrant | vibrant | modifier_attribute | chunk0 | 1 | medium |
| m2 | attribute | pink | pink | color_attribute | chunk0 | 2 | high |
| m3 | object | petals | petal | noun_chunk_root | chunk1 | 6 | high |
| m4 | attribute | long | long | size_attribute | chunk1 | 5 | high |
| m5 | context | background | background | scene_context | chunk2 | 13 | high |
| m6 | attribute | blurred | blurred | modifier_attribute | chunk2 | 11 | medium |
| m7 | attribute | green | green | color_attribute | chunk2 | 12 | high |
| m8 | action | stands | stand | verb_predicate | doc | 7 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> flower |
| e1 | has_attribute | m0 | m2 | high | chunk0 amod -> flower |
| e2 | has_attribute | m3 | m4 | high | chunk1 amod -> petals |
| e3 | has_context | scene | m5 | high | scene_context token background |
| e4 | has_attribute | m5 | m6 | medium | chunk2 amod -> background |
| e5 | has_attribute | m5 | m7 | high | chunk2 amod -> background |
| e6 | agent | m8 | m0 | medium | nsubj -> stands |
| e7 | relation | m0 | m3 | high | with |
| e8 | relation | m0 | m5 | high | against |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | flower | flower | object | m0 | raw_mention |  |  |  |
| ent_m3 | object | petal | petals | object | m3 | raw_mention |  |  |  |
| ent_m5 | context | background | background | object | m5 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | stands | stand | stand |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e6 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | with | high | e7 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | against | high | e8 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 32

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `12d151d075972300fd5e1b992ae54d639244f6449ccc9366e108de100c416814`
**parse_path:** `tag_list`

> women, protest, banner, trees, rainbow dress

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | women | woman | segment_head | t0 | 0 | high |
| m1 | object | protest | protest | segment_head | t1 | 0 | high |
| m2 | object | banner | banner | segment_head | t2 | 0 | high |
| m3 | object | trees | tree | segment_head | t3 | 0 | high |
| m4 | object | dress | dress | segment_head | t4 | 1 | high |
| m5 | attribute | rainbow | rainbow | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m4 | m5 | high | t4 internal compound -> dress |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | women | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | protest | protest | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | banner | banner | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | tree | trees | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | dress | dress | clothing | m4 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 33

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `138cd27f18aae997ac6ac36cae743a4f9bd1ef3fff2d732038d504da5b456014`
**parse_path:** `tag_list`

> woman, soap, bathtub, mirror, white tiles

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | segment_head | t0 | 0 | high |
| m1 | object | soap | soap | segment_head | t1 | 0 | high |
| m2 | object | bathtub | bathtub | segment_head | t2 | 0 | high |
| m3 | object | mirror | mirror | segment_head | t3 | 0 | high |
| m4 | object | tiles | tile | segment_head | t4 | 1 | high |
| m5 | attribute | white | white | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m4 | m5 | high | t4 internal amod -> tiles |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | soap | soap | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | bathtub | bathtub | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | mirror | mirror | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | tile | tiles | object | m4 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 34

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `13f49f32bbfec63699d6ffbf711593bce779463a6349b0f1ff1b201fa50da014`
**parse_path:** `sentence`

> A blurry view of a forest with tall trees and dense underbrush. Green and brown leaves cover the ground, with tree trunks rising upward into a bright, out-of-focus sky. The motion blur suggests movement through the woods.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | view | view | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | blurry | blurry | visual_attribute | chunk0 | 1 | medium |
| m2 | object | forest | forest | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | trees | tree | noun_chunk_root | chunk2 | 8 | high |
| m4 | attribute | tall | tall | size_attribute | chunk2 | 7 | high |
| m5 | object | underbrush | underbrush | noun_chunk_root | chunk3 | 11 | high |
| m6 | attribute | dense | dense | modifier_attribute | chunk3 | 10 | medium |
| m7 | object | leaves | leaf | noun_chunk_root | chunk4 | 16 | high |
| m8 | attribute | Green | green | color_attribute | chunk4 | 13 | high |
| m9 | attribute | brown | brown | color_attribute | chunk4 | 15 | high |
| m10 | object | ground | ground | noun_chunk_root | chunk5 | 19 | high |
| m11 | object | tree trunks | tree_trunk | noun_chunk_root | chunk6 | 22 | high |
| m12 | object | out-of-focus | out-of-focus | noun_chunk_root | chunk7 | 29 | high |
| m13 | attribute | bright | bright | visual_attribute | chunk7 | 27 | medium |
| m14 | object | sky | sky | noun_chunk_root | chunk8 | 30 | high |
| m15 | object | blur | blur | noun_chunk_root | chunk9 | 34 | high |
| m16 | attribute | motion | motion | compound_modifier | chunk9 | 33 | medium |
| m17 | object | movement | movement | noun_chunk_root | chunk10 | 36 | high |
| m18 | object | woods | wood | noun_chunk_root | chunk11 | 39 | high |
| m19 | action | cover | cover | verb_predicate | doc | 17 | high |
| m20 | action | rising | rise | verb_predicate | doc | 23 | high |
| m21 | action | suggests | suggest | verb_predicate | doc | 35 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> view |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> trees |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> underbrush |
| e3 | has_attribute | m7 | m8 | high | chunk4 amod -> leaves |
| e4 | has_attribute | m7 | m9 | high | chunk4 conj -> leaves |
| e5 | has_attribute | m12 | m13 | medium | chunk7 amod -> out-of-focus |
| e6 | has_attribute | m15 | m16 | medium | chunk9 compound -> blur |
| e7 | agent | m19 | m7 | medium | nsubj -> cover |
| e8 | patient | m19 | m10 | medium | dobj -> cover |
| e9 | agent | m20 | m11 | medium | nsubj -> rising |
| e10 | agent | m21 | m15 | medium | nsubj -> suggests |
| e11 | patient | m21 | m17 | medium | dobj -> suggests |
| e12 | relation | m0 | m2 | medium | of |
| e13 | relation | m2 | m3 | high | with |
| e14 | relation | m2 | m5 | high | with |
| e15 | relation | m11 | m12 | medium | into |
| e16 | relation | m17 | m18 | medium | through |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | view | view | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | forest | forest | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | tree | trees | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | underbrush | underbrush | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | leaf | leaves | object | m7 | raw_mention |  |  |  |
| ent_m10 | object | ground | ground | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | tree_trunk | tree trunks | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | out-of-focus | out-of-focus | object | m12 | raw_mention |  |  |  |
| ent_m14 | object | sky | sky | object | m14 | raw_mention |  |  |  |
| ent_m15 | object | blur | blur | object | m15 | raw_mention |  |  |  |
| ent_m17 | object | movement | movement | object | m17 | raw_mention |  |  |  |
| ent_m18 | object | wood | woods | object | m18 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m19 | cover | cover | cover |  | agent:m7->ent_m7; patient:m10->ent_m10 |  |
| ce1 | m20 | rising | rise | rise |  | agent:m11->ent_m11 |  |
| ce2 | m21 | suggests | suggest | suggest |  | agent:m15->ent_m15; patient:m17->ent_m17 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | cover | agent | m7 | ent_m7 | medium | e7 | nsubj -> cover |  |  |
| ce0 | cover | patient | m10 | ent_m10 | medium | e8 | dobj -> cover |  |  |
| ce1 | rise | agent | m11 | ent_m11 | medium | e9 | nsubj -> rising |  |  |
| ce2 | suggest | agent | m15 | ent_m15 | medium | e10 | nsubj -> suggests |  |  |
| ce2 | suggest | patient | m17 | ent_m17 | medium | e11 | dobj -> suggests |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | of | medium | e12 | False | False |  |  |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | with | high | e13 | False | False |  |  |
| cr2 | m2 | m5 | ent_m2 | ent_m5 | with | high | e14 | False | False |  |  |
| cr3 | m11 | m12 | ent_m11 | ent_m12 | into | medium | e15 | False | False |  |  |
| cr4 | m17 | m18 | ent_m17 | ent_m18 | through | medium | e16 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 35

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `141781ae9aed9737cb5b87309987b0a531ef8ec36b80f5df514fc9cc613a3014`
**parse_path:** `sentence`

> A small dark mouse eats seeds from a green plastic lid on a wooden surface.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | mouse | mouse | noun_chunk_root | chunk0 | 3 | high |
| m1 | attribute | small | small | size_attribute | chunk0 | 1 | high |
| m2 | attribute | dark | dark | visual_attribute | chunk0 | 2 | medium |
| m3 | object | seeds | seed | noun_chunk_root | chunk1 | 5 | high |
| m4 | object | lid | lid | noun_chunk_root | chunk2 | 10 | high |
| m5 | attribute | green | green | color_attribute | chunk2 | 8 | high |
| m6 | attribute | plastic | plastic | material_attribute | chunk2 | 9 | high |
| m7 | context | surface | surface | spatial_region | chunk3 | 14 | medium |
| m8 | action | eats | eat | verb_predicate | doc | 4 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> mouse |
| e1 | has_attribute | m0 | m2 | medium | chunk0 amod -> mouse |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> lid |
| e3 | has_attribute | m4 | m6 | high | chunk2 compound -> lid |
| e4 | agent | m8 | m0 | medium | nsubj -> eats |
| e5 | patient | m8 | m3 | medium | dobj -> eats |
| e6 | relation | m0 | m4 | medium | from |
| e7 | relation | m4 | m7 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | mouse | mouse | object | m0 | raw_mention |  |  |  |
| ent_m3 | object | seed | seeds | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | lid | lid | object | m4 | raw_mention |  |  |  |
| ent_m7 | context | surface | surface | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | eats | eat | eat |  | agent:m0->ent_m0; patient:m3->ent_m3 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | eat | agent | m0 | ent_m0 | medium | e4 | nsubj -> eats |  |  |
| ce0 | eat | patient | m3 | ent_m3 | medium | e5 | dobj -> eats |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | from | medium | e6 | False | False |  |  |
| cr1 | m4 | m7 | ent_m4 | ent_m7 | on | high | e7 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 36

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `14b68438947aaa187dd5a08cd9df57dd702dd3450c54c8042dfd4d32e7ea2014`
**parse_path:** `sentence`

> A woman speaks at a podium with "UNIP" branding, standing before an audience in a lecture hall.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "UNIP" | unip | quote_text | doc_quote | 7 | high |
| m1 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m2 | object | podium | podium | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | branding | branding | noun_chunk_root | chunk2 | 8 | high |
| m4 | object | audience | audience | noun_chunk_root | chunk3 | 13 | high |
| m5 | object | hall | hall | noun_chunk_root | chunk4 | 17 | high |
| m6 | attribute | lecture | lecture | compound_modifier | chunk4 | 16 | medium |
| m7 | action | speaks | speak | verb_predicate | doc | 2 | high |
| m8 | action | standing | stand | verb_predicate | doc | 10 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m5 | m6 | medium | chunk4 compound -> hall |
| e1 | agent | m7 | m1 | medium | nsubj -> speaks |
| e2 | agent | m8 | m1 | medium | inherited agent advcl -> speaks |
| e3 | relation | m1 | m2 | medium | at |
| e4 | relation | m2 | m3 | high | with |
| e5 | relation | m1 | m4 | medium | before |
| e6 | relation | m1 | m5 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | woman | woman | person | m1 | raw_mention |  |  |  |
| ent_m2 | object | podium | podium | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | branding | branding | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | audience | audience | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | hall | hall | object | m5 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | speaks | speak | speak |  | agent:m1->ent_m1 |  |
| ce1 | m8 | standing | stand | stand |  | agent:m1->ent_m1 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | speak | agent | m1 | ent_m1 | medium | e1 | nsubj -> speaks |  |  |
| ce1 | stand | agent | m1 | ent_m1 | medium | e2 | inherited agent advcl -> speaks |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | at | medium | e3 | False | False |  |  |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | with | high | e4 | False | False |  |  |
| cr2 | m1 | m4 | ent_m1 | ent_m4 | before | medium | e5 | False | False |  |  |
| cr3 | m1 | m5 | ent_m1 | ent_m5 | in | high | e6 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 37

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `14bcd3b32d58bbb5a4a6e7a74c9e2a2122879e32a6df7a32e57f096c2e9d0414`
**parse_path:** `sentence`

> A woman in a white, orange, and blue cycling jersey smiles. She wears a red and blue collar with "Rabobank" printed on it.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "Rabobank" | rabobank | quote_text | doc_quote | 22 | high |
| m1 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m2 | object | jersey | jersey | noun_chunk_root | chunk1 | 11 | high |
| m3 | attribute | white | white | color_attribute | chunk1 | 4 | high |
| m4 | attribute | orange | orange | color_attribute | chunk1 | 6 | high |
| m5 | attribute | blue | blue | color_attribute | chunk1 | 9 | high |
| m6 | attribute | cycling | cycling | compound_modifier | chunk1 | 10 | medium |
| m7 | object | collar | collar | noun_chunk_root | chunk3 | 20 | high |
| m8 | attribute | red | red | color_attribute | chunk3 | 17 | high |
| m9 | attribute | blue | blue | color_attribute | chunk3 | 19 | high |
| m10 | action | smiles | smile | verb_predicate | doc | 12 | high |
| m11 | action | wears | wear | verb_predicate | doc | 15 | high |
| m12 | action | printed | print | verb_predicate | doc | 23 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | chunk1 amod -> jersey |
| e1 | has_attribute | m2 | m4 | high | chunk1 conj -> jersey |
| e2 | has_attribute | m2 | m5 | high | chunk1 conj -> jersey |
| e3 | has_attribute | m2 | m6 | medium | chunk1 compound -> jersey |
| e4 | has_attribute | m7 | m8 | high | chunk3 amod -> collar |
| e5 | has_attribute | m7 | m9 | high | chunk3 conj -> collar |
| e6 | agent | m10 | m1 | medium | nsubj -> smiles |
| e7 | agent | m11 | m1 | medium | nsubj -> wears; resolved She -> woman |
| e8 | patient | m11 | m7 | medium | dobj -> wears |
| e9 | agent | m12 | m0 | medium | nsubj -> printed |
| e10 | relation | m1 | m2 | high | in |
| e11 | relation | m0 | m1 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | woman | woman | person | m1 | raw_mention |  |  |  |
| ent_m2 | object | jersey | jersey | clothing | m2 | raw_mention |  |  |  |
| ent_m7 | object | collar | collar | clothing | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | smiles | smile | smile |  | agent:m1->ent_m1 |  |
| ce1 | m11 | wears | wear | wear |  | agent:m1->ent_m1; patient:m7->ent_m7 |  |
| ce2 | m12 | printed | print | print |  | agent:m0->None |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | smile | agent | m1 | ent_m1 | medium | e6 | nsubj -> smiles |  |  |
| ce1 | wear | agent | m1 | ent_m1 | medium | e7 | nsubj -> wears; resolved She -> woman |  |  |
| ce1 | wear | patient | m7 | ent_m7 | medium | e8 | dobj -> wears |  |  |
| ce2 | print | agent | m0 |  | medium | e9 | nsubj -> printed |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | in | high | e10 | False | False |  |  |
| cr1 | m0 | m1 |  | ent_m1 | on | high | e11 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 38

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `14cda51b33a33137a7819417ba7cbfe200dc2b9f347129c3797fbdfb8be6b814`
**parse_path:** `sentence`

> An older man in a white shirt smiles with his eyes closed, hand near his chin. Another man stands behind him near a red flag.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | older | old | visual_attribute | chunk0 | 1 | medium |
| m2 | object | shirt | shirt | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | white | white | color_attribute | chunk1 | 5 | high |
| m4 | object | eyes | eye | noun_chunk_root | chunk2 | 10 | high |
| m5 | object | chin | chin | noun_chunk_root | chunk3 | 16 | high |
| m6 | object | man | man | noun_chunk_root | chunk4 | 19 | high |
| m7 | object | flag | flag | noun_chunk_root | chunk6 | 26 | high |
| m8 | attribute | red | red | color_attribute | chunk6 | 25 | high |
| m9 | action | smiles | smile | verb_predicate | doc | 7 | high |
| m10 | action | closed | close | verb_predicate | doc | 11 | high |
| m11 | action | stands | stand | verb_predicate | doc | 20 | high |
| m12 | object | hand | hand | with_absolute_recovered_object | with_absolute8 | 13 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> man |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> shirt |
| e2 | has_attribute | m7 | m8 | high | chunk6 amod -> flag |
| e3 | agent | m9 | m0 | medium | nsubj -> smiles |
| e4 | agent | m10 | m4 | medium | nsubj -> closed |
| e5 | agent | m11 | m6 | medium | nsubj -> stands |
| e6 | scene_contains | scene | m12 | medium | with_absolute8 recovered hand |
| e7 | relation | m0 | m2 | high | in |
| e8 | relation | m12 | m5 | high | near |
| e9 | relation | m6 | m7 | high | near |

### Skipped Raw Concept Edges
| type | source | target | confidence | reason | evidence |
| --- | --- | --- | --- | --- | --- |
| relation | m6 | m6 | high | self_edge_after_coref | behind |

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | shirt | shirt | clothing | m2 | raw_mention |  |  |  |
| ent_m4 | object | eye | eyes | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | chin | chin | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | man | man | person | m6 | raw_mention |  |  |  |
| ent_m7 | object | flag | flag | object | m7 | raw_mention |  |  |  |
| ent_m12 | object | hand | hand | object | m12 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | smiles | smile | smile |  | agent:m0->ent_m0 |  |
| ce1 | m10 | closed | close | close |  | agent:m4->ent_m4 |  |
| ce2 | m11 | stands | stand | stand |  | agent:m6->ent_m6 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | smile | agent | m0 | ent_m0 | medium | e3 | nsubj -> smiles |  |  |
| ce1 | close | agent | m4 | ent_m4 | medium | e4 | nsubj -> closed |  |  |
| ce2 | stand | agent | m6 | ent_m6 | medium | e5 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | high | e7 | False | False |  |  |
| cr1 | m12 | m5 | ent_m12 | ent_m5 | near | high | e8 | False | False |  |  |
| cr2 | m6 | m7 | ent_m6 | ent_m7 | near | high | e9 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 39

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `14ce6ea91f458477c952f4c1ae223be78e62c40f49c03f1b1b0ea52ca062a014`
**parse_path:** `sentence`

> Two men smile at the camera, standing close together indoors. One wears a blue shirt with a bandana around his neck, while the other in a white shirt has a black face mask hanging from his collar. A window and colorful wall art are visible behind them.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | men | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Two | two | exact_quantity | chunk0 | 0 | high |
| m2 | object | camera | camera | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | shirt | shirt | noun_chunk_root | chunk2 | 16 | high |
| m4 | attribute | blue | blue | color_attribute | chunk2 | 15 | high |
| m5 | object | bandana | bandana | noun_chunk_root | chunk3 | 19 | high |
| m6 | object | neck | neck | noun_chunk_root | chunk4 | 22 | high |
| m7 | object | shirt | shirt | noun_chunk_root | chunk5 | 30 | high |
| m8 | attribute | white | white | color_attribute | chunk5 | 29 | high |
| m9 | object | face mask | face_mask | noun_chunk_root | chunk6 | 34 | high |
| m10 | attribute | black | black | color_attribute | chunk6 | 33 | high |
| m11 | object | collar | collar | noun_chunk_root | chunk7 | 38 | high |
| m12 | object | window | window | noun_chunk_root | chunk8 | 41 | high |
| m13 | object | art | art | noun_chunk_root | chunk9 | 45 | high |
| m14 | attribute | colorful | colorful | modifier_attribute | chunk9 | 43 | medium |
| m15 | attribute | wall | wall | compound_modifier | chunk9 | 44 | medium |
| m16 | context | indoors | indoors | scene_context | doc | 10 | high |
| m17 | reference | One | one | singular_substitute | nominal_reference | 12 | high |
| m18 | reference | other | other | contrastive_reference | nominal_reference | 26 | high |
| m19 | action | smile | smile | verb_predicate | doc | 2 | high |
| m20 | action | standing | stand | verb_predicate | doc | 7 | high |
| m21 | action | wears | wear | verb_predicate | doc | 13 | high |
| m22 | action | has | have | verb_predicate | doc | 31 | high |
| m23 | action | hanging | hang | verb_predicate | doc | 35 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> men |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> shirt |
| e2 | has_attribute | m7 | m8 | high | chunk5 amod -> shirt |
| e3 | has_attribute | m9 | m10 | high | chunk6 amod -> face mask |
| e4 | has_attribute | m13 | m14 | medium | chunk9 amod -> art |
| e5 | has_attribute | m13 | m15 | medium | chunk9 compound -> art |
| e6 | has_context | scene | m16 | high | scene_context token indoors |
| e7 | refers_to | m17 | m0 | high | singular_substitute One -> men; score=102 |
| e8 | refers_to | m18 | m0 | high | contrastive_reference other -> men; score=110 |
| e9 | agent | m19 | m0 | medium | nsubj -> smile |
| e10 | agent | m20 | m0 | medium | inherited agent advcl -> smile |
| e11 | agent | m21 | m0 | medium | nsubj -> wears; resolved One -> men |
| e12 | patient | m21 | m3 | medium | dobj -> wears |
| e13 | agent | m22 | m0 | medium | nsubj -> has; resolved other -> men |
| e14 | patient | m22 | m9 | medium | dobj -> has |
| e15 | agent | m23 | m9 | medium | inherited agent acl -> face mask |
| e16 | relation | m0 | m2 | medium | at |
| e17 | relation | m3 | m5 | high | with |
| e18 | relation | m5 | m6 | high | around |
| e19 | relation | m0 | m7 | high | in |
| e20 | relation | m9 | m11 | medium | from |
| e21 | relation | m12 | m0 | high | behind |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | men | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | camera | camera | device | m2 | raw_mention |  |  |  |
| ent_m3 | object | shirt | shirt | clothing | m3 | raw_mention |  |  |  |
| ent_m5 | object | bandana | bandana | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | neck | neck | object | m6 | raw_mention |  |  |  |
| ent_m7 | object | shirt | shirt | clothing | m7 | raw_mention |  |  |  |
| ent_m9 | object | face_mask | face mask | object | m9 | raw_mention |  |  |  |
| ent_m11 | object | collar | collar | clothing | m11 | raw_mention |  |  |  |
| ent_m12 | object | window | window | object | m12 | raw_mention |  |  |  |
| ent_m13 | object | art | art | object | m13 | raw_mention |  |  |  |
| ent_m16 | context | indoors | indoors | object | m16 | raw_mention |  |  |  |
| eref_m17 | instance | man | One | person | m17 | stage9_reference | ent_m0 |  | 1 |
| eref_m18 | contrastive_instance | man | other | person | m18 | stage9_reference | ent_m0 |  | 1 |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m17 | eref_m17 | m0 | ent_m0 | high |  |
| refers_to | m18 | eref_m18 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m19 | smile | smile | smile |  | agent:m0->ent_m0 |  |
| ce1 | m20 | standing | stand | stand |  | agent:m0->ent_m0 |  |
| ce2 | m21 | wears | wear | wear |  | agent:m0->eref_m17; patient:m3->ent_m3 |  |
| ce3 | m22 | has | have | have |  | agent:m0->eref_m18; patient:m9->ent_m9 |  |
| ce4 | m23 | hanging | hang | hang |  | agent:m9->ent_m9 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | smile | agent | m0 | ent_m0 | medium | e9 | nsubj -> smile |  |  |
| ce1 | stand | agent | m0 | ent_m0 | medium | e10 | inherited agent advcl -> smile |  |  |
| ce2 | wear | agent | m0 | eref_m17 | medium | e11 | nsubj -> wears; resolved One -> men |  |  |
| ce2 | wear | patient | m3 | ent_m3 | medium | e12 | dobj -> wears |  |  |
| ce3 | have | agent | m0 | eref_m18 | medium | e13 | nsubj -> has; resolved other -> men |  |  |
| ce3 | have | patient | m9 | ent_m9 | medium | e14 | dobj -> has |  |  |
| ce4 | hang | agent | m9 | ent_m9 | medium | e15 | inherited agent acl -> face mask |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | at | medium | e16 | False | False |  |  |
| cr1 | m3 | m5 | ent_m3 | ent_m5 | with | high | e17 | False | False |  |  |
| cr2 | m5 | m6 | ent_m5 | ent_m6 | around | high | e18 | False | False |  |  |
| cr3 | m0 | m7 | eref_m18 | ent_m7 | in | high | e19 | False | False |  |  |
| cr4 | m9 | m11 | ent_m9 | ent_m11 | from | medium | e20 | False | False |  |  |
| cr5 | m12 | m0 | ent_m12 | ent_m0 | behind | high | e21 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 40

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `1605f6676e726e65314c65203f0a83685636c214d328bfb75aae0031df0b8014`
**parse_path:** `sentence`

> A historic cathedral with a tall tower and a red dome stands under a bright blue sky.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | cathedral | cathedral | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | historic | historic | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | tower | tower | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | tall | tall | size_attribute | chunk1 | 5 | high |
| m4 | object | dome | dome | noun_chunk_root | chunk2 | 10 | high |
| m5 | attribute | red | red | color_attribute | chunk2 | 9 | high |
| m6 | object | sky | sky | noun_chunk_root | chunk3 | 16 | high |
| m7 | attribute | bright | bright | visual_attribute | chunk3 | 14 | medium |
| m8 | attribute | blue | blue | color_attribute | chunk3 | 15 | high |
| m9 | action | stands | stand | verb_predicate | doc | 11 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> cathedral |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> tower |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> dome |
| e3 | has_attribute | m6 | m7 | medium | chunk3 amod -> sky |
| e4 | has_attribute | m6 | m8 | high | chunk3 amod -> sky |
| e5 | agent | m9 | m0 | medium | nsubj -> stands |
| e6 | relation | m0 | m2 | high | with |
| e7 | relation | m0 | m4 | high | with |
| e8 | relation | m0 | m6 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | cathedral | cathedral | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | tower | tower | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | dome | dome | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | sky | sky | object | m6 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | stands | stand | stand |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e5 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e6 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | high | e7 | False | False |  |  |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | under | high | e8 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 41

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `16a2207dbb6320b5f61e69daeac0aa557b0398dd8d0a4e09c3d38f79dd0dc814`
**parse_path:** `sentence`

> A brightly lit bridge with traditional Chinese architecture spans a river at night, its lights reflecting on the water.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | bridge | bridge | noun_chunk_root | chunk0 | 3 | high |
| m1 | attribute | brightly | brightly | modifier_attribute | chunk0 | 1 | medium |
| m2 | attribute | lit | light | visual_attribute | chunk0 | 2 | medium |
| m3 | object | architecture | architecture | noun_chunk_root | chunk1 | 7 | high |
| m4 | attribute | traditional | traditional | modifier_attribute | chunk1 | 5 | medium |
| m5 | attribute | Chinese | chinese | modifier_attribute | chunk1 | 6 | medium |
| m6 | object | river | river | noun_chunk_root | chunk2 | 10 | high |
| m7 | context | night | night | scene_context | chunk3 | 12 | medium |
| m8 | object | lights | light | noun_chunk_root | chunk4 | 15 | high |
| m9 | object | water | water | noun_chunk_root | chunk5 | 19 | high |
| m10 | action | spans | span | verb_predicate | doc | 8 | high |
| m11 | action | reflecting | reflect | verb_predicate | doc | 16 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 advmod -> bridge |
| e1 | has_attribute | m0 | m2 | medium | chunk0 amod -> bridge |
| e2 | has_attribute | m3 | m4 | medium | chunk1 amod -> architecture |
| e3 | has_attribute | m3 | m5 | medium | chunk1 amod -> architecture |
| e4 | has_context | scene | m7 | medium | scene_context token night |
| e5 | agent | m10 | m0 | medium | nsubj -> spans |
| e6 | patient | m10 | m6 | medium | dobj -> spans |
| e7 | agent | m11 | m8 | medium | nsubj -> reflecting |
| e8 | relation | m0 | m3 | high | with |
| e9 | relation | m0 | m7 | medium | at |
| e10 | relation | m8 | m9 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | bridge | bridge | object | m0 | raw_mention |  |  |  |
| ent_m3 | object | architecture | architecture | object | m3 | raw_mention |  |  |  |
| ent_m6 | object | river | river | object | m6 | raw_mention |  |  |  |
| ent_m7 | context | night | night | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | light | lights | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | water | water | object | m9 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | spans | span | span |  | agent:m0->ent_m0; patient:m6->ent_m6 |  |
| ce1 | m11 | reflecting | reflect | reflect |  | agent:m8->ent_m8 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | span | agent | m0 | ent_m0 | medium | e5 | nsubj -> spans |  |  |
| ce0 | span | patient | m6 | ent_m6 | medium | e6 | dobj -> spans |  |  |
| ce1 | reflect | agent | m8 | ent_m8 | medium | e7 | nsubj -> reflecting |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | with | high | e8 | False | False |  |  |
| cr1 | m0 | m7 | ent_m0 | ent_m7 | at | medium | e9 | False | False |  |  |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | on | high | e10 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 42

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `17189150ed62a17be1e9c143c5ee30f47cd5b5c6026c36739702e340533c4c14`
**parse_path:** `tag_list`

> red jerseys, soccer players, grass field, team huddle

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | jerseys | jersey | segment_head | t0 | 1 | high |
| m1 | attribute | red | red | attribute | t0 | 0 | high |
| m2 | object | soccer players | soccer_player | segment_head | t1 | 0 | high |
| m3 | object | field | field | segment_head | t2 | 1 | high |
| m4 | attribute | grass | grass | attribute | t2 | 0 | high |
| m5 | object | huddle | huddle | segment_head | t3 | 1 | high |
| m6 | attribute | team | team | attribute | t3 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> jerseys |
| e1 | has_attribute | m3 | m4 | high | t2 internal compound -> field |
| e2 | has_attribute | m5 | m6 | high | t3 internal compound -> huddle |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | jersey | jerseys | clothing | m0 | raw_mention |  |  |  |
| ent_m2 | object | soccer_player | soccer players | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | field | field | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | huddle | huddle | object | m5 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 43

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `173fffdc074a0d1191247922c97a20b543a27d12047ff7e244466a02f5da9814`
**parse_path:** `sentence`

> The open trunk of a black car contains a custom audio setup with a subwoofer and a framed display. A gray, monster-like figurine stands on the right side near the rear seats. The interior is lined with black leather, and another car is visible in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | trunk | trunk | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | open | open | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | car | car | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | black | black | color_attribute | chunk1 | 5 | high |
| m4 | object | setup | setup | noun_chunk_root | chunk2 | 11 | high |
| m5 | attribute | audio | audio | modifier_attribute | chunk2 | 10 | medium |
| m6 | object | subwoofer | subwoofer | noun_chunk_root | chunk3 | 14 | high |
| m7 | object | display | display | noun_chunk_root | chunk4 | 18 | high |
| m8 | attribute | framed | frame | state_attribute | chunk4 | 17 | medium |
| m9 | object | figurine | figurine | noun_chunk_root | chunk5 | 24 | high |
| m10 | attribute | gray | gray | color_attribute | chunk5 | 21 | high |
| m11 | attribute | monster-like | monster-like | modifier_attribute | chunk5 | 23 | medium |
| m12 | context | side | side | spatial_region | chunk6 | 29 | medium |
| m13 | object | seats | seat | noun_chunk_root | chunk7 | 33 | high |
| m14 | attribute | rear | rear | modifier_attribute | chunk7 | 32 | medium |
| m15 | object | interior | interior | noun_chunk_root | chunk8 | 36 | high |
| m16 | object | leather | leather | noun_chunk_root | chunk9 | 41 | high |
| m17 | attribute | black | black | color_attribute | chunk9 | 40 | high |
| m18 | object | car | car | noun_chunk_root | chunk10 | 45 | high |
| m19 | context | background | background | scene_context | chunk11 | 50 | high |
| m20 | action | contains | contain | verb_predicate | doc | 7 | high |
| m21 | action | stands | stand | verb_predicate | doc | 25 | high |
| m22 | action | lined | line | verb_predicate | doc | 38 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> trunk |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> car |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> setup |
| e3 | has_attribute | m7 | m8 | medium | chunk4 amod -> display |
| e4 | has_attribute | m9 | m10 | high | chunk5 amod -> figurine |
| e5 | has_attribute | m9 | m11 | medium | chunk5 amod -> figurine |
| e6 | has_attribute | m13 | m14 | medium | chunk7 amod -> seats |
| e7 | has_attribute | m16 | m17 | high | chunk9 amod -> leather |
| e8 | has_context | scene | m19 | high | scene_context token background |
| e9 | agent | m20 | m0 | medium | nsubj -> contains |
| e10 | patient | m20 | m4 | medium | dobj -> contains |
| e11 | agent | m21 | m9 | medium | nsubj -> stands |
| e12 | agent | m22 | m15 | medium | nsubjpass -> lined |
| e13 | relation | m0 | m2 | medium | of |
| e14 | relation | m4 | m6 | high | with |
| e15 | relation | m4 | m7 | high | with |
| e16 | relation | m9 | m12 | high | on |
| e17 | relation | m9 | m13 | high | near |
| e18 | relation | m15 | m16 | high | with |
| e19 | relation | m18 | m19 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | trunk | trunk | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | car | car | vehicle | m2 | raw_mention |  |  |  |
| ent_m4 | object | setup | setup | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | subwoofer | subwoofer | object | m6 | raw_mention |  |  |  |
| ent_m7 | object | display | display | object | m7 | raw_mention |  |  |  |
| ent_m9 | object | figurine | figurine | object | m9 | raw_mention |  |  |  |
| ent_m12 | context | side | side | object | m12 | raw_mention |  |  |  |
| ent_m13 | object | seat | seats | object | m13 | raw_mention |  |  |  |
| ent_m15 | object | interior | interior | object | m15 | raw_mention |  |  |  |
| ent_m16 | object | leather | leather | object | m16 | raw_mention |  |  |  |
| ent_m18 | object | car | car | vehicle | m18 | raw_mention |  |  |  |
| ent_m19 | context | background | background | object | m19 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m20 | contains | contain | contain |  | agent:m0->ent_m0; patient:m4->ent_m4 |  |
| ce1 | m21 | stands | stand | stand |  | agent:m9->ent_m9 |  |
| ce2 | m22 | lined | line | line |  | theme:m15->ent_m15 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | contain | agent | m0 | ent_m0 | medium | e9 | nsubj -> contains |  |  |
| ce0 | contain | patient | m4 | ent_m4 | medium | e10 | dobj -> contains |  |  |
| ce1 | stand | agent | m9 | ent_m9 | medium | e11 | nsubj -> stands |  |  |
| ce2 | line | theme | m15 | ent_m15 | medium | e12 | nsubjpass -> lined |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | of | medium | e13 | False | False |  |  |
| cr1 | m4 | m6 | ent_m4 | ent_m6 | with | high | e14 | False | False |  |  |
| cr2 | m4 | m7 | ent_m4 | ent_m7 | with | high | e15 | False | False |  |  |
| cr3 | m9 | m12 | ent_m9 | ent_m12 | on | high | e16 | False | False |  |  |
| cr4 | m9 | m13 | ent_m9 | ent_m13 | near | high | e17 | False | False |  |  |
| cr5 | m15 | m16 | ent_m15 | ent_m16 | with | high | e18 | False | False |  |  |
| cr6 | m18 | m19 | ent_m18 | ent_m19 | in | high | e19 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m22 | e12 | m15 |  |  | {"action_mention_id": "m22", "kind": "passive_subject_to_theme", "raw_edge_id": "e12", "target": "m15"} |

## 44

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `193c8da25cf4cf5a476da04622867cdbbd9870e204facf9d63d41427341d3c14`
**parse_path:** `sentence`

> A black-and-white aerial view shows a patchwork of farmland divided into rectangular fields.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | view | view | noun_chunk_root | chunk0 | 3 | high |
| m1 | attribute | black-and-white | black-and-white | modifier_attribute | chunk0 | 1 | medium |
| m2 | attribute | aerial | aerial | modifier_attribute | chunk0 | 2 | medium |
| m3 | object | patchwork | patchwork | noun_chunk_root | chunk1 | 6 | high |
| m4 | object | farmland | farmland | noun_chunk_root | chunk2 | 8 | high |
| m5 | object | fields | field | noun_chunk_root | chunk3 | 12 | high |
| m6 | attribute | rectangular | rectangular | modifier_attribute | chunk3 | 11 | medium |
| m7 | action | shows | show | verb_predicate | doc | 4 | high |
| m8 | action | divided | divide | verb_predicate | doc | 9 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> view |
| e1 | has_attribute | m0 | m2 | medium | chunk0 amod -> view |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> fields |
| e3 | agent | m7 | m0 | medium | nsubj -> shows |
| e4 | patient | m7 | m3 | medium | dobj -> shows |
| e5 | agent | m8 | m4 | medium | inherited agent acl -> farmland |
| e6 | relation | m3 | m4 | medium | of |
| e7 | relation | m4 | m5 | medium | into |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | view | view | object | m0 | raw_mention |  |  |  |
| ent_m3 | object | patchwork | patchwork | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | farmland | farmland | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | field | fields | object | m5 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | shows | show | show |  | agent:m0->ent_m0; patient:m3->ent_m3 |  |
| ce1 | m8 | divided | divide | divide |  | agent:m4->ent_m4 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | m0 | ent_m0 | medium | e3 | nsubj -> shows |  |  |
| ce0 | show | patient | m3 | ent_m3 | medium | e4 | dobj -> shows |  |  |
| ce1 | divide | agent | m4 | ent_m4 | medium | e5 | inherited agent acl -> farmland |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m3 | m4 | ent_m3 | ent_m4 | of | medium | e6 | False | False |  |  |
| cr1 | m4 | m5 | ent_m4 | ent_m5 | into | medium | e7 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 45

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `1a67a5e6fc7fc7f52fc413539887acd32937b29d38364ff00522ad1372764414`
**parse_path:** `tag_list`

> man speaking, suit, water bottle, nameplate

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | segment_head | t0 | 0 | high |
| m1 | object | suit | suit | segment_head | t1 | 0 | high |
| m2 | object | bottle | bottle | segment_head | t2 | 1 | high |
| m3 | attribute | water | water | attribute | t2 | 0 | high |
| m4 | object | nameplate | nameplate | segment_head | t3 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | t2 internal compound -> bottle |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | suit | suit | clothing | m1 | raw_mention |  |  |  |
| ent_m2 | object | bottle | bottle | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | nameplate | nameplate | object | m4 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 46

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `1cb6a222d3d9321d4c56d2de803c0e749d84c866122202d7ad305cca64c15014`
**parse_path:** `tag_list`

> ice rink, hockey player, goalie, blue jersey, protective gear

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | ice rink | ice_rink | segment_head | t0 | 0 | high |
| m1 | object | hockey player | hockey_player | segment_head | t1 | 0 | high |
| m2 | object | goalie | goalie | segment_head | t2 | 0 | high |
| m3 | object | jersey | jersey | segment_head | t3 | 1 | high |
| m4 | attribute | blue | blue | attribute | t3 | 0 | high |
| m5 | object | gear | gear | segment_head | t4 | 1 | high |
| m6 | attribute | protective | protective | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m3 | m4 | high | t3 internal compound -> jersey |
| e1 | has_attribute | m5 | m6 | high | t4 internal amod -> gear |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | ice_rink | ice rink | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | hockey_player | hockey player | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | goalie | goalie | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | jersey | jersey | clothing | m3 | raw_mention |  |  |  |
| ent_m5 | object | gear | gear | object | m5 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 47

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `1dda6c4dd9a5dc36750df82f622cd494428d712da6c3be28c32459395a813c14`
**parse_path:** `sentence`

> A person wearing a conical hat walks through tall green corn plants in a field.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | hat | hat | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | conical | conical | modifier_attribute | chunk1 | 4 | medium |
| m3 | object | plants | plant | noun_chunk_root | chunk2 | 11 | high |
| m4 | attribute | tall | tall | size_attribute | chunk2 | 8 | high |
| m5 | attribute | green | green | color_attribute | chunk2 | 9 | high |
| m6 | attribute | corn | corn | compound_modifier | chunk2 | 10 | medium |
| m7 | object | field | field | noun_chunk_root | chunk3 | 14 | high |
| m8 | action | wearing | wear | verb_predicate | doc | 2 | high |
| m9 | action | walks | walk | verb_predicate | doc | 6 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 amod -> hat |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> plants |
| e2 | has_attribute | m3 | m5 | high | chunk2 amod -> plants |
| e3 | has_attribute | m3 | m6 | medium | chunk2 compound -> plants |
| e4 | agent | m8 | m0 | medium | inherited agent acl -> person |
| e5 | patient | m8 | m1 | medium | dobj -> wearing |
| e6 | agent | m9 | m0 | medium | nsubj -> walks |
| e7 | relation | m0 | m3 | medium | through |
| e8 | relation | m0 | m7 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | hat | hat | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | plant | plants | object | m3 | raw_mention |  |  |  |
| ent_m7 | object | field | field | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | wearing | wear | wear |  | agent:m0->ent_m0; patient:m1->ent_m1 |  |
| ce1 | m9 | walks | walk | walk |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | wear | agent | m0 | ent_m0 | medium | e4 | inherited agent acl -> person |  |  |
| ce0 | wear | patient | m1 | ent_m1 | medium | e5 | dobj -> wearing |  |  |
| ce1 | walk | agent | m0 | ent_m0 | medium | e6 | nsubj -> walks |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | through | medium | e7 | False | False |  |  |
| cr1 | m0 | m7 | ent_m0 | ent_m7 | in | high | e8 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 48

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `206ea33b318039c8b699513c268fbdd208745194d679338b72093f3038337814`
**parse_path:** `tag_list`

> beach, palm trees, people, van, grass, ocean

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | beach | beach | segment_head | t0 | 0 | high |
| m1 | object | palm trees | palm_tree | segment_head | t1 | 0 | high |
| m2 | object | people | people | segment_head | t2 | 0 | high |
| m3 | object | van | van | segment_head | t3 | 0 | high |
| m4 | object | grass | grass | segment_head | t4 | 0 | high |
| m5 | object | ocean | ocean | segment_head | t5 | 0 | high |

### Raw Concept Edges
_none_

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | beach | beach | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | palm_tree | palm trees | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | people | people | person | m2 | raw_mention |  |  |  |
| ent_m3 | object | van | van | vehicle | m3 | raw_mention |  |  |  |
| ent_m4 | object | grass | grass | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | ocean | ocean | object | m5 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 49

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `20f9f6aa1b9882a46648386e9ee87f61be444356d78b198b99fb10f2cdb9dc14`
**parse_path:** `tag_list`

> snowy path, frosted trees, blue sky, winter landscape, bare branches

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | path | path | segment_head | t0 | 1 | high |
| m1 | attribute | snowy | snowy | attribute | t0 | 0 | high |
| m2 | object | trees | tree | segment_head | t1 | 1 | high |
| m3 | attribute | frosted | frosted | attribute | t1 | 0 | high |
| m4 | object | sky | sky | segment_head | t2 | 1 | high |
| m5 | attribute | blue | blue | attribute | t2 | 0 | high |
| m6 | object | landscape | landscape | segment_head | t3 | 1 | high |
| m7 | attribute | winter | winter | attribute | t3 | 0 | high |
| m8 | object | branches | branch | segment_head | t4 | 1 | high |
| m9 | attribute | bare | bare | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> path |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> trees |
| e2 | has_attribute | m4 | m5 | high | t2 internal amod -> sky |
| e3 | has_attribute | m6 | m7 | high | t3 internal compound -> landscape |
| e4 | has_attribute | m8 | m9 | high | t4 internal amod -> branches |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | path | path | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | tree | trees | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | sky | sky | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | landscape | landscape | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | branch | branches | object | m8 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 50

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `211c24a95c3516500269ebd16ea4c6fc0ad5745b24794fcc1df25d5d7327f014`
**parse_path:** `sentence`

> A Hard Rock Cafe sign is on a red building at Pier 39, with an American flag flying above.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | sign | sign | noun_chunk_root | chunk0 | 4 | high |
| m1 | attribute | Hard | hard | compound_modifier | chunk0 | 1 | medium |
| m2 | attribute | Rock | rock | compound_modifier | chunk0 | 2 | medium |
| m3 | attribute | Cafe | cafe | compound_modifier | chunk0 | 3 | medium |
| m4 | object | building | building | noun_chunk_root | chunk1 | 9 | high |
| m5 | attribute | red | red | color_attribute | chunk1 | 8 | high |
| m6 | object | Pier | pier | noun_chunk_root | chunk2 | 11 | high |
| m7 | object | American flag | american_flag | noun_chunk_root | chunk3 | 16 | high |
| m8 | action | flying | fly | verb_predicate | doc | 17 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 compound -> sign |
| e1 | has_attribute | m0 | m2 | medium | chunk0 compound -> sign |
| e2 | has_attribute | m0 | m3 | medium | chunk0 compound -> sign |
| e3 | has_attribute | m4 | m5 | high | chunk1 amod -> building |
| e4 | agent | m8 | m7 | medium | nsubj -> flying |
| e5 | relation | m0 | m4 | high | on |
| e6 | relation | m4 | m6 | medium | at |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sign | sign | document | m0 | raw_mention |  |  |  |
| ent_m4 | object | building | building | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | pier | Pier | object | m6 | raw_mention |  |  |  |
| ent_m7 | object | american_flag | American flag | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | flying | fly | fly |  | agent:m7->ent_m7 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | fly | agent | m7 | ent_m7 | medium | e4 | nsubj -> flying |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | on | high | e5 | False | False |  |  |
| cr1 | m4 | m6 | ent_m4 | ent_m6 | at | medium | e6 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 51

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `2212e683c5261f5a8d61ac3b532609ea0dfdcf733e158178ebfd2dac85ca6814`
**parse_path:** `sentence`

> A man stands on a rocky hillside with sparse bushes, wearing a yellow jacket and blue shirt. Distant mountains rise under a pale sky.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | hillside | hillside | noun_chunk_root | chunk1 | 6 | high |
| m2 | attribute | rocky | rocky | modifier_attribute | chunk1 | 5 | medium |
| m3 | object | bushes | bush | noun_chunk_root | chunk2 | 9 | high |
| m4 | attribute | sparse | sparse | modifier_attribute | chunk2 | 8 | medium |
| m5 | object | jacket | jacket | noun_chunk_root | chunk3 | 14 | high |
| m6 | attribute | yellow | yellow | color_attribute | chunk3 | 13 | high |
| m7 | object | shirt | shirt | noun_chunk_root | chunk4 | 17 | high |
| m8 | attribute | blue | blue | color_attribute | chunk4 | 16 | high |
| m9 | object | mountains | mountain | noun_chunk_root | chunk5 | 20 | high |
| m10 | attribute | Distant | distant | modifier_attribute | chunk5 | 19 | medium |
| m11 | object | sky | sky | noun_chunk_root | chunk6 | 25 | high |
| m12 | attribute | pale | pale | modifier_attribute | chunk6 | 24 | medium |
| m13 | action | stands | stand | verb_predicate | doc | 2 | high |
| m14 | action | wearing | wear | verb_predicate | doc | 11 | high |
| m15 | action | rise | rise | verb_predicate | doc | 21 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 amod -> hillside |
| e1 | has_attribute | m3 | m4 | medium | chunk2 amod -> bushes |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> jacket |
| e3 | has_attribute | m7 | m8 | high | chunk4 amod -> shirt |
| e4 | has_attribute | m9 | m10 | medium | chunk5 amod -> mountains |
| e5 | has_attribute | m11 | m12 | medium | chunk6 amod -> sky |
| e6 | agent | m13 | m0 | medium | nsubj -> stands |
| e7 | agent | m14 | m0 | medium | inherited agent advcl -> stands |
| e8 | patient | m14 | m5 | medium | dobj -> wearing |
| e9 | patient | m14 | m7 | medium | dobj -> wearing |
| e10 | agent | m15 | m9 | medium | nsubj -> rise |
| e11 | relation | m0 | m1 | high | on |
| e12 | relation | m1 | m3 | high | with |
| e13 | relation | m9 | m11 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | hillside | hillside | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | bush | bushes | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | jacket | jacket | clothing | m5 | raw_mention |  |  |  |
| ent_m7 | object | shirt | shirt | clothing | m7 | raw_mention |  |  |  |
| ent_m9 | object | mountain | mountains | object | m9 | raw_mention |  |  |  |
| ent_m11 | object | sky | sky | object | m11 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m13 | stands | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m14 | wearing | wear | wear |  | agent:m0->ent_m0; patient:m5->ent_m5; patient:m7->ent_m7 |  |
| ce2 | m15 | rise | rise | rise |  | agent:m9->ent_m9 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e6 | nsubj -> stands |  |  |
| ce1 | wear | agent | m0 | ent_m0 | medium | e7 | inherited agent advcl -> stands |  |  |
| ce1 | wear | patient | m5 | ent_m5 | medium | e8 | dobj -> wearing |  |  |
| ce1 | wear | patient | m7 | ent_m7 | medium | e9 | dobj -> wearing |  |  |
| ce2 | rise | agent | m9 | ent_m9 | medium | e10 | nsubj -> rise |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | on | high | e11 | False | False |  |  |
| cr1 | m1 | m3 | ent_m1 | ent_m3 | with | high | e12 | False | False |  |  |
| cr2 | m9 | m11 | ent_m9 | ent_m11 | under | high | e13 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 52

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `22934f61d98bca9733a9e09fee584a49438e4b06a954b581673247f3ef307014`
**parse_path:** `tag_list`

> football players, red uniforms, blue jerseys, stadium entrance, crowd, young boy

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | football players | football_player | segment_head | t0 | 0 | high |
| m1 | object | uniforms | uniform | segment_head | t1 | 1 | high |
| m2 | attribute | red | red | attribute | t1 | 0 | high |
| m3 | object | jerseys | jersey | segment_head | t2 | 1 | high |
| m4 | attribute | blue | blue | attribute | t2 | 0 | high |
| m5 | object | entrance | entrance | segment_head | t3 | 1 | high |
| m6 | attribute | stadium | stadium | attribute | t3 | 0 | high |
| m7 | object | crowd | crowd | segment_head | t4 | 0 | high |
| m8 | object | boy | boy | segment_head | t5 | 1 | high |
| m9 | attribute | young | young | attribute | t5 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | t1 internal amod -> uniforms |
| e1 | has_attribute | m3 | m4 | high | t2 internal amod -> jerseys |
| e2 | has_attribute | m5 | m6 | high | t3 internal compound -> entrance |
| e3 | has_attribute | m8 | m9 | high | t5 internal amod -> boy |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | football_player | football players | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | uniform | uniforms | clothing | m1 | raw_mention |  |  |  |
| ent_m3 | object | jersey | jerseys | clothing | m3 | raw_mention |  |  |  |
| ent_m5 | object | entrance | entrance | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | crowd | crowd | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | boy | boy | person | m8 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 53

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `2357777249fc3c53b6aba571795157f507c24b93ffb180994e7c09ce69012c14`
**parse_path:** `sentence`

> A man with gray hair speaks into a microphone while wearing a blue patterned shirt. He stands outdoors under a large white structure, with buildings and trees visible in the background. A person in a green vest is partially seen to his left.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | hair | hair | noun_chunk_root | chunk1 | 4 | high |
| m2 | attribute | gray | gray | color_attribute | chunk1 | 3 | high |
| m3 | object | microphone | microphone | noun_chunk_root | chunk2 | 8 | high |
| m4 | object | shirt | shirt | noun_chunk_root | chunk3 | 14 | high |
| m5 | attribute | blue | blue | color_attribute | chunk3 | 12 | high |
| m6 | attribute | patterned | patterned | modifier_attribute | chunk3 | 13 | medium |
| m7 | object | structure | structure | noun_chunk_root | chunk5 | 23 | high |
| m8 | attribute | large | large | size_attribute | chunk5 | 21 | high |
| m9 | attribute | white | white | color_attribute | chunk5 | 22 | high |
| m10 | object | buildings | building | noun_chunk_root | chunk6 | 26 | high |
| m11 | object | trees | tree | noun_chunk_root | chunk7 | 28 | high |
| m12 | context | background | background | scene_context | chunk8 | 32 | high |
| m13 | object | person | person | noun_chunk_root | chunk9 | 35 | high |
| m14 | object | vest | vest | noun_chunk_root | chunk10 | 39 | high |
| m15 | attribute | green | green | color_attribute | chunk10 | 38 | high |
| m16 | context | left | left | spatial_region | chunk11 | 45 | medium |
| m17 | context | outdoors | outdoors | scene_context | doc | 18 | high |
| m18 | action | speaks | speak | verb_predicate | doc | 5 | high |
| m19 | action | wearing | wear | verb_predicate | doc | 10 | high |
| m20 | action | stands | stand | verb_predicate | doc | 17 | high |
| m21 | action | seen | see | verb_predicate | doc | 42 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> hair |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> shirt |
| e2 | has_attribute | m4 | m6 | medium | chunk3 amod -> shirt |
| e3 | has_attribute | m7 | m8 | high | chunk5 amod -> structure |
| e4 | has_attribute | m7 | m9 | high | chunk5 amod -> structure |
| e5 | has_context | scene | m12 | high | scene_context token background |
| e6 | has_attribute | m14 | m15 | high | chunk10 amod -> vest |
| e7 | has_context | scene | m17 | high | scene_context token outdoors |
| e8 | agent | m18 | m0 | medium | nsubj -> speaks |
| e9 | agent | m19 | m0 | medium | inherited agent advcl -> speaks |
| e10 | patient | m19 | m4 | medium | dobj -> wearing |
| e11 | agent | m20 | m0 | medium | nsubj -> stands; resolved He -> man |
| e12 | agent | m21 | m13 | medium | nsubjpass -> seen |
| e13 | relation | m0 | m1 | high | with |
| e14 | relation | m0 | m3 | medium | into |
| e15 | relation | m0 | m7 | high | under |
| e16 | relation | m13 | m14 | high | in |
| e17 | relation | m13 | m16 | medium | to |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | hair | hair | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | microphone | microphone | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | shirt | shirt | clothing | m4 | raw_mention |  |  |  |
| ent_m7 | object | structure | structure | object | m7 | raw_mention |  |  |  |
| ent_m10 | object | building | buildings | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | tree | trees | object | m11 | raw_mention |  |  |  |
| ent_m12 | context | background | background | object | m12 | raw_mention |  |  |  |
| ent_m13 | object | person | person | person | m13 | raw_mention |  |  |  |
| ent_m14 | object | vest | vest | clothing | m14 | raw_mention |  |  |  |
| ent_m16 | context | left | left | object | m16 | raw_mention |  |  |  |
| ent_m17 | context | outdoors | outdoors | object | m17 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | speaks | speak | speak |  | agent:m0->ent_m0 |  |
| ce1 | m19 | wearing | wear | wear |  | agent:m0->ent_m0; patient:m4->ent_m4 |  |
| ce2 | m20 | stands | stand | stand |  | agent:m0->ent_m0 |  |
| ce3 | m21 | seen | see | see |  | theme:m13->ent_m13 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | speak | agent | m0 | ent_m0 | medium | e8 | nsubj -> speaks |  |  |
| ce1 | wear | agent | m0 | ent_m0 | medium | e9 | inherited agent advcl -> speaks |  |  |
| ce1 | wear | patient | m4 | ent_m4 | medium | e10 | dobj -> wearing |  |  |
| ce2 | stand | agent | m0 | ent_m0 | medium | e11 | nsubj -> stands; resolved He -> man |  |  |
| ce3 | see | theme | m13 | ent_m13 | medium | e12 | nsubjpass -> seen |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | high | e13 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | into | medium | e14 | False | False |  |  |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | under | high | e15 | False | False |  |  |
| cr3 | m13 | m14 | ent_m13 | ent_m14 | in | high | e16 | False | False |  |  |
| cr4 | m13 | m16 | ent_m13 | ent_m16 | to | medium | e17 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m21 | e12 | m13 |  |  | {"action_mention_id": "m21", "kind": "passive_subject_to_theme", "raw_edge_id": "e12", "target": "m13"} |

## 54

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `2382247db8d0f0d04bf57da902caf01fd96c226a7358f95da81fcb909adcf014`
**parse_path:** `sentence`

> A person rides a red motorcycle on a road beside a field. They wear a black helmet and jacket.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | motorcycle | motorcycle | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | red | red | color_attribute | chunk1 | 4 | high |
| m3 | object | road | road | noun_chunk_root | chunk2 | 8 | high |
| m4 | object | field | field | noun_chunk_root | chunk3 | 11 | high |
| m5 | object | helmet | helmet | noun_chunk_root | chunk5 | 17 | high |
| m6 | attribute | black | black | color_attribute | chunk5 | 16 | high |
| m7 | object | jacket | jacket | noun_chunk_root | chunk6 | 19 | high |
| m8 | action | rides | rid | verb_predicate | doc | 2 | high |
| m9 | action | wear | wear | verb_predicate | doc | 14 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> motorcycle |
| e1 | has_attribute | m5 | m6 | high | chunk5 amod -> helmet |
| e2 | agent | m8 | m0 | medium | nsubj -> rides |
| e3 | patient | m8 | m1 | medium | dobj -> rides |
| e4 | agent | m9 | m0 | medium | nsubj -> wear; resolved They -> person |
| e5 | patient | m9 | m5 | medium | dobj -> wear |
| e6 | patient | m9 | m7 | medium | dobj -> wear |
| e7 | relation | m0 | m3 | high | on |
| e8 | relation | m3 | m4 | high | beside |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | motorcycle | motorcycle | vehicle | m1 | raw_mention |  |  |  |
| ent_m3 | object | road | road | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | field | field | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | helmet | helmet | clothing | m5 | raw_mention |  |  |  |
| ent_m7 | object | jacket | jacket | clothing | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | rides | rid | rid |  | agent:m0->ent_m0; patient:m1->ent_m1 |  |
| ce1 | m9 | wear | wear | wear |  | agent:m0->ent_m0; patient:m5->ent_m5; patient:m7->ent_m7 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | rid | agent | m0 | ent_m0 | medium | e2 | nsubj -> rides |  |  |
| ce0 | rid | patient | m1 | ent_m1 | medium | e3 | dobj -> rides |  |  |
| ce1 | wear | agent | m0 | ent_m0 | medium | e4 | nsubj -> wear; resolved They -> person |  |  |
| ce1 | wear | patient | m5 | ent_m5 | medium | e5 | dobj -> wear |  |  |
| ce1 | wear | patient | m7 | ent_m7 | medium | e6 | dobj -> wear |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | on | high | e7 | False | False |  |  |
| cr1 | m3 | m4 | ent_m3 | ent_m4 | beside | high | e8 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 55

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `23ff5ece4644748c87739562585deccd29314becc568b42b37327d09bec93c14`
**parse_path:** `sentence`

> A young alpaca with long neck and fluffy white fur looks directly at the camera.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | alpaca | alpaca | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | young | young | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | neck | neck | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | long | long | size_attribute | chunk1 | 4 | high |
| m4 | object | fur | fur | noun_chunk_root | chunk2 | 9 | high |
| m5 | attribute | fluffy | fluffy | modifier_attribute | chunk2 | 7 | medium |
| m6 | attribute | white | white | color_attribute | chunk2 | 8 | high |
| m7 | object | camera | camera | noun_chunk_root | chunk3 | 14 | high |
| m8 | action | looks | look | verb_predicate | doc | 10 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> alpaca |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> neck |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> fur |
| e3 | has_attribute | m4 | m6 | high | chunk2 amod -> fur |
| e4 | agent | m8 | m0 | medium | nsubj -> looks |
| e5 | relation | m0 | m2 | high | with |
| e6 | relation | m0 | m4 | high | with |
| e7 | relation | m0 | m7 | medium | at |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | alpaca | alpaca | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | neck | neck | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | fur | fur | object | m4 | raw_mention |  |  |  |
| ent_m7 | object | camera | camera | device | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | looks | look | look |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | look | agent | m0 | ent_m0 | medium | e4 | nsubj -> looks |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e5 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | high | e6 | False | False |  |  |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | at | medium | e7 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 56

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `255de17e3c6b90c0e792442b32720e2cf575b2e3176e55fc0418e266884d7414`
**parse_path:** `sentence`

> A person hangs mid-air from ropes inside a large indoor facility with white walls and a high ceiling.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | mid-air | mid-air | noun_chunk_root | chunk1 | 3 | high |
| m2 | object | ropes | rope | noun_chunk_root | chunk2 | 5 | high |
| m3 | object | facility | facility | noun_chunk_root | chunk3 | 10 | high |
| m4 | attribute | large | large | size_attribute | chunk3 | 8 | high |
| m5 | attribute | indoor | indoor | modifier_attribute | chunk3 | 9 | medium |
| m6 | object | walls | wall | noun_chunk_root | chunk4 | 13 | high |
| m7 | attribute | white | white | color_attribute | chunk4 | 12 | high |
| m8 | object | ceiling | ceiling | noun_chunk_root | chunk5 | 17 | high |
| m9 | attribute | high | high | modifier_attribute | chunk5 | 16 | medium |
| m10 | action | hangs | hang | verb_predicate | doc | 2 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m3 | m4 | high | chunk3 amod -> facility |
| e1 | has_attribute | m3 | m5 | medium | chunk3 amod -> facility |
| e2 | has_attribute | m6 | m7 | high | chunk4 amod -> walls |
| e3 | has_attribute | m8 | m9 | medium | chunk5 amod -> ceiling |
| e4 | agent | m10 | m0 | medium | nsubj -> hangs |
| e5 | patient | m10 | m1 | medium | dobj -> hangs |
| e6 | relation | m0 | m2 | medium | from |
| e7 | relation | m0 | m3 | high | inside |
| e8 | relation | m3 | m6 | high | with |
| e9 | relation | m3 | m8 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | mid-air | mid-air | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | rope | ropes | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | facility | facility | object | m3 | raw_mention |  |  |  |
| ent_m6 | object | wall | walls | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | ceiling | ceiling | object | m8 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | hangs | hang | hang |  | agent:m0->ent_m0; patient:m1->ent_m1 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | hang | agent | m0 | ent_m0 | medium | e4 | nsubj -> hangs |  |  |
| ce0 | hang | patient | m1 | ent_m1 | medium | e5 | dobj -> hangs |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | from | medium | e6 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | inside | high | e7 | False | False |  |  |
| cr2 | m3 | m6 | ent_m3 | ent_m6 | with | high | e8 | False | False |  |  |
| cr3 | m3 | m8 | ent_m3 | ent_m8 | with | high | e9 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 57

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `26107b4d1da8a1acacc9ef8c65bf8585743ac92978974539ddaeaa9f873f8414`
**parse_path:** `sentence`

> A soccer player in a red jersey controls the ball while being challenged by opponents on a green field. Spectators fill the stands behind them.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | soccer player | soccer_player | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | jersey | jersey | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | red | red | color_attribute | chunk1 | 4 | high |
| m3 | object | ball | ball | noun_chunk_root | chunk2 | 8 | high |
| m4 | object | opponents | opponent | noun_chunk_root | chunk3 | 13 | high |
| m5 | object | field | field | noun_chunk_root | chunk4 | 17 | high |
| m6 | attribute | green | green | color_attribute | chunk4 | 16 | high |
| m7 | object | Spectators | spectator | noun_chunk_root | chunk5 | 19 | high |
| m8 | object | stands | stand | noun_chunk_root | chunk6 | 22 | high |
| m9 | action | controls | control | verb_predicate | doc | 6 | high |
| m10 | action | challenged | challenge | verb_predicate | doc | 11 | high |
| m11 | action | fill | fill | verb_predicate | doc | 20 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> jersey |
| e1 | has_attribute | m5 | m6 | high | chunk4 amod -> field |
| e2 | agent | m9 | m0 | medium | nsubj -> controls |
| e3 | patient | m9 | m3 | medium | dobj -> controls |
| e4 | agent | m10 | m0 | medium | inherited agent advcl -> controls |
| e5 | agent | m11 | m7 | medium | nsubj -> fill |
| e6 | patient | m11 | m8 | medium | dobj -> fill |
| e7 | relation | m0 | m1 | high | in |
| e8 | relation | m0 | m4 | medium | by |
| e9 | relation | m0 | m5 | high | on |
| e10 | relation | m8 | m0 | high | behind |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | soccer_player | soccer player | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | jersey | jersey | clothing | m1 | raw_mention |  |  |  |
| ent_m3 | object | ball | ball | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | opponent | opponents | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | field | field | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | spectator | Spectators | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | stand | stands | object | m8 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | controls | control | control |  | agent:m0->ent_m0; patient:m3->ent_m3 |  |
| ce1 | m10 | challenged | challenge | challenge |  | agent:m0->ent_m0 |  |
| ce2 | m11 | fill | fill | fill |  | agent:m7->ent_m7; patient:m8->ent_m8 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | control | agent | m0 | ent_m0 | medium | e2 | nsubj -> controls |  |  |
| ce0 | control | patient | m3 | ent_m3 | medium | e3 | dobj -> controls |  |  |
| ce1 | challenge | agent | m0 | ent_m0 | medium | e4 | inherited agent advcl -> controls |  |  |
| ce2 | fill | agent | m7 | ent_m7 | medium | e5 | nsubj -> fill |  |  |
| ce2 | fill | patient | m8 | ent_m8 | medium | e6 | dobj -> fill |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e7 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | by | medium | e8 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | on | high | e9 | False | False |  |  |
| cr3 | m8 | m0 | ent_m8 | ent_m0 | behind | high | e10 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 58

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `26b99eb0823d368a743bcbdbd61e2f41774123487d9d219593d62a9136239414`
**parse_path:** `sentence`

> A person in a white shirt and apron walks away from a group of people in a restaurant.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | shirt | shirt | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | white | white | color_attribute | chunk1 | 4 | high |
| m3 | object | apron | apron | noun_chunk_root | chunk2 | 7 | high |
| m4 | object | group | group | noun_chunk_root | chunk3 | 12 | high |
| m5 | object | people | people | noun_chunk_root | chunk4 | 14 | high |
| m6 | object | restaurant | restaurant | noun_chunk_root | chunk5 | 17 | high |
| m7 | action | walks | walk | verb_predicate | doc | 8 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> shirt |
| e1 | agent | m7 | m0 | medium | nsubj -> walks |
| e2 | relation | m0 | m1 | high | in |
| e3 | relation | m0 | m3 | high | in |
| e4 | relation | m0 | m4 | medium | away_from |
| e5 | relation | m4 | m5 | medium | of |
| e6 | relation | m4 | m6 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | shirt | shirt | clothing | m1 | raw_mention |  |  |  |
| ent_m3 | object | apron | apron | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | group | group | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | people | people | person | m5 | raw_mention |  |  |  |
| ent_m6 | object | restaurant | restaurant | object | m6 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | walks | walk | walk |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | walk | agent | m0 | ent_m0 | medium | e1 | nsubj -> walks |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e2 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | in | high | e3 | False | False |  |  |
| cr2 | m0 | m4 | ent_m0 | ent_m4 | away_from | medium | e4 | False | False |  |  |
| cr3 | m4 | m5 | ent_m4 | ent_m5 | of | medium | e5 | False | False |  |  |
| cr4 | m4 | m6 | ent_m4 | ent_m6 | in | high | e6 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 59

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `28159d2f1eb69798cdc14f4de25ac7aeea229acf6a1a253bef728896c3861014`
**parse_path:** `sentence`

> A row of historic buildings with green shutters lines a cobblestone street. Several cars are parked along the curb, including a white SUV on the left and a silver sedan next to it. The scene is set under an overcast sky with trees visible in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | row | row | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | buildings | building | noun_chunk_root | chunk1 | 4 | high |
| m2 | attribute | historic | historic | modifier_attribute | chunk1 | 3 | medium |
| m3 | object | shutters | shutter | noun_chunk_root | chunk2 | 7 | high |
| m4 | attribute | green | green | color_attribute | chunk2 | 6 | high |
| m5 | object | street | street | noun_chunk_root | chunk3 | 11 | high |
| m6 | attribute | cobblestone | cobblestone | modifier_attribute | chunk3 | 10 | medium |
| m7 | object | cars | car | noun_chunk_root | chunk4 | 14 | high |
| m8 | quantity | Several | several | approximate_quantity | chunk4 | 13 | medium |
| m9 | object | curb | curb | noun_chunk_root | chunk5 | 19 | high |
| m10 | object | SUV | suv | noun_chunk_root | chunk6 | 24 | high |
| m11 | attribute | white | white | color_attribute | chunk6 | 23 | high |
| m12 | context | left | left | spatial_region | chunk7 | 27 | medium |
| m13 | object | sedan | sedan | noun_chunk_root | chunk8 | 31 | high |
| m14 | attribute | silver | silver | color_attribute | chunk8 | 30 | high |
| m15 | object | scene | scene | noun_chunk_root | chunk10 | 37 | high |
| m16 | object | sky | sky | noun_chunk_root | chunk11 | 43 | high |
| m17 | attribute | overcast | overcast | modifier_attribute | chunk11 | 42 | medium |
| m18 | object | trees | tree | noun_chunk_root | chunk12 | 45 | high |
| m19 | context | background | background | scene_context | chunk13 | 49 | high |
| m20 | action | lines | line | verb_predicate | doc | 8 | high |
| m21 | action | parked | park | verb_predicate | doc | 16 | high |
| m22 | action | including | include | verb_predicate | doc | 21 | high |
| m23 | action | set | set | verb_predicate | doc | 39 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 amod -> buildings |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> shutters |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> street |
| e3 | has_quantity | m7 | m8 | medium | chunk4 quantity -> cars |
| e4 | has_attribute | m10 | m11 | high | chunk6 amod -> SUV |
| e5 | has_attribute | m13 | m14 | high | chunk8 amod -> sedan |
| e6 | has_attribute | m16 | m17 | medium | chunk11 amod -> sky |
| e7 | has_context | scene | m19 | high | scene_context token background |
| e8 | agent | m20 | m0 | medium | nsubj -> lines |
| e9 | patient | m20 | m5 | medium | dobj -> lines |
| e10 | agent | m21 | m7 | medium | nsubjpass -> parked |
| e11 | agent | m22 | m7 | medium | inherited agent prep -> cars |
| e12 | patient | m22 | m10 | medium | pobj -> including |
| e13 | patient | m22 | m13 | medium | pobj -> including |
| e14 | agent | m23 | m15 | medium | nsubjpass -> set |
| e15 | relation | m0 | m1 | medium | of |
| e16 | relation | m1 | m3 | high | with |
| e17 | relation | m7 | m9 | medium | along |
| e18 | relation | m7 | m10 | medium | include |
| e19 | relation | m7 | m13 | medium | include |
| e20 | relation | m10 | m12 | high | on |
| e21 | relation | m13 | m7 | high | next_to |
| e22 | relation | m15 | m16 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | row | row | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | building | buildings | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | shutter | shutters | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | street | street | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | car | cars | vehicle | m7 | raw_mention |  |  |  |
| ent_m9 | object | curb | curb | object | m9 | raw_mention |  |  |  |
| ent_m10 | object | suv | SUV | vehicle | m10 | raw_mention |  |  |  |
| ent_m12 | context | left | left | object | m12 | raw_mention |  |  |  |
| ent_m13 | object | sedan | sedan | object | m13 | raw_mention |  |  |  |
| ent_m15 | object | scene | scene | object | m15 | raw_mention |  |  |  |
| ent_m16 | object | sky | sky | object | m16 | raw_mention |  |  |  |
| ent_m18 | object | tree | trees | object | m18 | raw_mention |  |  |  |
| ent_m19 | context | background | background | object | m19 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m20 | lines | line | line |  | agent:m0->ent_m0; patient:m5->ent_m5 |  |
| ce1 | m21 | parked | park | park |  | theme:m7->ent_m7 |  |
| ce2 | m22 | including | include | include |  | agent:m7->ent_m7; patient:m10->ent_m10; patient:m13->ent_m13 |  |
| ce3 | m23 | set | set | set |  | theme:m15->ent_m15 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | line | agent | m0 | ent_m0 | medium | e8 | nsubj -> lines |  |  |
| ce0 | line | patient | m5 | ent_m5 | medium | e9 | dobj -> lines |  |  |
| ce1 | park | theme | m7 | ent_m7 | medium | e10 | nsubjpass -> parked |  |  |
| ce2 | include | agent | m7 | ent_m7 | medium | e11 | inherited agent prep -> cars |  |  |
| ce2 | include | patient | m10 | ent_m10 | medium | e12 | pobj -> including |  |  |
| ce2 | include | patient | m13 | ent_m13 | medium | e13 | pobj -> including |  |  |
| ce3 | set | theme | m15 | ent_m15 | medium | e14 | nsubjpass -> set |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | of | medium | e15 | False | False |  |  |
| cr1 | m1 | m3 | ent_m1 | ent_m3 | with | high | e16 | False | False |  |  |
| cr2 | m7 | m9 | ent_m7 | ent_m9 | along | medium | e17 | False | False |  |  |
| cr3 | m7 | m10 | ent_m7 | ent_m10 | include | medium | e18 | False | False |  |  |
| cr4 | m7 | m13 | ent_m7 | ent_m13 | include | medium | e19 | False | False |  |  |
| cr5 | m10 | m12 | ent_m10 | ent_m12 | on | high | e20 | False | False |  |  |
| cr6 | m13 | m7 | ent_m13 | ent_m7 | next_to | high | e21 | False | False |  |  |
| cr7 | m15 | m16 | ent_m15 | ent_m16 | under | high | e22 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m21 | e10 | m7 |  |  | {"action_mention_id": "m21", "kind": "passive_subject_to_theme", "raw_edge_id": "e10", "target": "m7"} |
| passive_subject_to_theme | m23 | e14 | m15 |  |  | {"action_mention_id": "m23", "kind": "passive_subject_to_theme", "raw_edge_id": "e14", "target": "m15"} |

## 60

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `2841a2913036cf5f9c2bdec35c13133be2151c77258abf6f61743512eb8ec814`
**parse_path:** `sentence`

> A dark, muddy buffalo grazes on green grass in a field. Another buffalo stands nearby in the background, also on the grassy slope.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | buffalo | buffalo | noun_chunk_root | chunk0 | 4 | high |
| m1 | attribute | dark | dark | visual_attribute | chunk0 | 1 | medium |
| m2 | attribute | muddy | muddy | modifier_attribute | chunk0 | 3 | medium |
| m3 | object | grass | grass | noun_chunk_root | chunk1 | 8 | high |
| m4 | attribute | green | green | color_attribute | chunk1 | 7 | high |
| m5 | object | field | field | noun_chunk_root | chunk2 | 11 | high |
| m6 | object | buffalo | buffalo | noun_chunk_root | chunk3 | 14 | high |
| m7 | context | background | background | scene_context | chunk4 | 19 | high |
| m8 | object | slope | slope | noun_chunk_root | chunk5 | 25 | high |
| m9 | attribute | grassy | grassy | modifier_attribute | chunk5 | 24 | medium |
| m10 | action | grazes | graze | verb_predicate | doc | 5 | high |
| m11 | action | stands | stand | verb_predicate | doc | 15 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> buffalo |
| e1 | has_attribute | m0 | m2 | medium | chunk0 amod -> buffalo |
| e2 | has_attribute | m3 | m4 | high | chunk1 amod -> grass |
| e3 | has_context | scene | m7 | high | scene_context token background |
| e4 | has_attribute | m8 | m9 | medium | chunk5 amod -> slope |
| e5 | agent | m10 | m0 | medium | nsubj -> grazes |
| e6 | agent | m11 | m6 | medium | nsubj -> stands |
| e7 | relation | m0 | m3 | high | on |
| e8 | relation | m0 | m5 | high | in |
| e9 | relation | m6 | m7 | high | in |
| e10 | relation | m6 | m8 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | buffalo | buffalo | object | m0 | raw_mention |  |  |  |
| ent_m3 | object | grass | grass | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | field | field | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | buffalo | buffalo | object | m6 | raw_mention |  |  |  |
| ent_m7 | context | background | background | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | slope | slope | object | m8 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | grazes | graze | graze |  | agent:m0->ent_m0 |  |
| ce1 | m11 | stands | stand | stand |  | agent:m6->ent_m6 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | graze | agent | m0 | ent_m0 | medium | e5 | nsubj -> grazes |  |  |
| ce1 | stand | agent | m6 | ent_m6 | medium | e6 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | on | high | e7 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | in | high | e8 | False | False |  |  |
| cr2 | m6 | m7 | ent_m6 | ent_m7 | in | high | e9 | False | False |  |  |
| cr3 | m6 | m8 | ent_m6 | ent_m8 | on | high | e10 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 61

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `2c1a3df2e080b489aabe477866e6631bf79ca8c0ba02181926c37675f98fec14`
**parse_path:** `sentence`

> A black hearing aid rests next to a white charging case on a light surface. The device has a curved shape and a small button, while the case has a round base with a white cable extending from it.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hearing aid | hearing_aid | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | black | black | color_attribute | chunk0 | 1 | high |
| m2 | object | case | case | noun_chunk_root | chunk1 | 9 | high |
| m3 | attribute | white | white | color_attribute | chunk1 | 7 | high |
| m4 | attribute | charging | charging | compound_modifier | chunk1 | 8 | medium |
| m5 | context | surface | surface | spatial_region | chunk2 | 13 | medium |
| m6 | object | device | device | noun_chunk_root | chunk3 | 16 | high |
| m7 | object | shape | shape | noun_chunk_root | chunk4 | 20 | high |
| m8 | attribute | curved | curved | modifier_attribute | chunk4 | 19 | medium |
| m9 | object | button | button | noun_chunk_root | chunk5 | 24 | high |
| m10 | attribute | small | small | size_attribute | chunk5 | 23 | high |
| m11 | object | case | case | noun_chunk_root | chunk6 | 28 | high |
| m12 | object | base | base | noun_chunk_root | chunk7 | 32 | high |
| m13 | attribute | round | round | modifier_attribute | chunk7 | 31 | medium |
| m14 | object | cable | cable | noun_chunk_root | chunk8 | 36 | high |
| m15 | attribute | white | white | color_attribute | chunk8 | 35 | high |
| m16 | action | rests | rest | verb_predicate | doc | 3 | high |
| m17 | action | has | have | verb_predicate | doc | 17 | high |
| m18 | action | has | have | verb_predicate | doc | 29 | high |
| m19 | action | extending | extend | verb_predicate | doc | 37 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> hearing aid |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> case |
| e2 | has_attribute | m2 | m4 | medium | chunk1 compound -> case |
| e3 | has_attribute | m7 | m8 | medium | chunk4 amod -> shape |
| e4 | has_attribute | m9 | m10 | high | chunk5 amod -> button |
| e5 | has_attribute | m12 | m13 | medium | chunk7 amod -> base |
| e6 | has_attribute | m14 | m15 | high | chunk8 amod -> cable |
| e7 | agent | m16 | m0 | medium | nsubj -> rests |
| e8 | agent | m17 | m6 | medium | nsubj -> has |
| e9 | patient | m17 | m7 | medium | dobj -> has |
| e10 | patient | m17 | m9 | medium | dobj -> has |
| e11 | agent | m18 | m11 | medium | nsubj -> has |
| e12 | patient | m18 | m12 | medium | dobj -> has |
| e13 | agent | m19 | m14 | medium | inherited agent acl -> cable |
| e14 | relation | m0 | m2 | high | next_to |
| e15 | relation | m0 | m5 | high | on |
| e16 | relation | m12 | m14 | high | with |
| e17 | relation | m14 | m11 | medium | from |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hearing_aid | hearing aid | device | m0 | raw_mention |  |  |  |
| ent_m2 | object | case | case | object | m2 | raw_mention |  |  |  |
| ent_m5 | context | surface | surface | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | device | device | device | m6 | raw_mention |  |  |  |
| ent_m7 | object | shape | shape | object | m7 | raw_mention |  |  |  |
| ent_m9 | object | button | button | object | m9 | raw_mention |  |  |  |
| ent_m11 | object | case | case | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | base | base | object | m12 | raw_mention |  |  |  |
| ent_m14 | object | cable | cable | object | m14 | raw_mention |  |  |  |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| generic_alias | m6 | ent_m6 |  | ent_m0 | medium |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | rests | rest | rest |  | agent:m0->ent_m0 |  |
| ce1 | m17 | has | have | have |  | agent:m6->ent_m0; patient:m7->ent_m7; patient:m9->ent_m9 |  |
| ce2 | m18 | has | have | have |  | agent:m11->ent_m11; patient:m12->ent_m12 |  |
| ce3 | m19 | extending | extend | extend |  | agent:m14->ent_m14 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | rest | agent | m0 | ent_m0 | medium | e7 | nsubj -> rests |  |  |
| ce1 | have | agent | m6 | ent_m0 | medium | e8 | nsubj -> has |  |  |
| ce1 | have | patient | m7 | ent_m7 | medium | e9 | dobj -> has |  |  |
| ce1 | have | patient | m9 | ent_m9 | medium | e10 | dobj -> has |  |  |
| ce2 | have | agent | m11 | ent_m11 | medium | e11 | nsubj -> has |  |  |
| ce2 | have | patient | m12 | ent_m12 | medium | e12 | dobj -> has |  |  |
| ce3 | extend | agent | m14 | ent_m14 | medium | e13 | inherited agent acl -> cable |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | next_to | high | e14 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | high | e15 | False | False |  |  |
| cr2 | m12 | m14 | ent_m12 | ent_m14 | with | high | e16 | False | False |  |  |
| cr3 | m14 | m11 | ent_m14 | ent_m11 | from | medium | e17 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 62

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `2c8d57f87a2faffdb49a205924b495b56874aeaf4b3b8a8a7f1d90d53f3e3414`
**parse_path:** `tag_list`

> mountain, trees, sky, car, clouds

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | mountain | mountain | segment_head | t0 | 0 | high |
| m1 | object | trees | tree | segment_head | t1 | 0 | high |
| m2 | object | sky | sky | segment_head | t2 | 0 | high |
| m3 | object | car | car | segment_head | t3 | 0 | high |
| m4 | object | clouds | cloud | segment_head | t4 | 0 | high |

### Raw Concept Edges
_none_

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | mountain | mountain | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | tree | trees | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | sky | sky | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | car | car | vehicle | m3 | raw_mention |  |  |  |
| ent_m4 | object | cloud | clouds | object | m4 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 63

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `2dc7c048d8f8187055314d252e2703a3d3f89662b051b5f1c840127f22f42414`
**parse_path:** `sentence`

> Three race cars speed along a curved track, with a red car in the foreground and two others behind it. Orange cones mark the edge of the track, surrounded by grass and trees in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | race cars | race_car | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | track | track | noun_chunk_root | chunk1 | 6 | high |
| m2 | attribute | curved | curved | modifier_attribute | chunk1 | 5 | medium |
| m3 | object | car | car | noun_chunk_root | chunk2 | 11 | high |
| m4 | attribute | red | red | color_attribute | chunk2 | 10 | high |
| m5 | context | foreground | foreground | scene_context | chunk3 | 14 | high |
| m6 | object | cones | cone | noun_chunk_root | chunk6 | 22 | high |
| m7 | attribute | Orange | orange | color_attribute | chunk6 | 21 | high |
| m8 | object | track | track | noun_chunk_root | chunk8 | 28 | high |
| m9 | object | grass | grass | noun_chunk_root | chunk9 | 32 | high |
| m10 | object | trees | tree | noun_chunk_root | chunk10 | 34 | high |
| m11 | context | background | background | scene_context | chunk11 | 37 | high |
| m12 | action | speed | speed | verb_predicate | doc | 2 | high |
| m13 | action | mark | mark | verb_predicate | doc | 23 | high |
| m14 | object | edge | edge | verb_object | doc | 25 | medium |
| m15 | action | surrounded | surround | verb_predicate | doc | 30 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 amod -> track |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> car |
| e2 | has_context | scene | m5 | high | scene_context token foreground |
| e3 | has_attribute | m6 | m7 | high | chunk6 compound -> cones |
| e4 | has_context | scene | m11 | high | scene_context token background |
| e5 | agent | m12 | m0 | medium | nsubj -> speed |
| e6 | agent | m13 | m6 | medium | nsubj -> mark |
| e7 | patient | m13 | m14 | medium | dobj -> mark |
| e8 | agent | m15 | m6 | medium | inherited agent advcl -> mark |
| e9 | relation | m0 | m1 | medium | along |
| e10 | relation | m0 | m3 | high | with |
| e11 | relation | m3 | m5 | high | in |
| e12 | relation | m6 | m8 | medium | edge_of |
| e13 | relation | m6 | m9 | medium | by |
| e14 | relation | m6 | m10 | medium | by |
| e15 | relation | m9 | m11 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | race_car | race cars | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | track | track | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | car | car | vehicle | m3 | raw_mention |  |  |  |
| ent_m5 | context | foreground | foreground | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | cone | cones | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | track | track | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | grass | grass | object | m9 | raw_mention |  |  |  |
| ent_m10 | object | tree | trees | object | m10 | raw_mention |  |  |  |
| ent_m11 | context | background | background | object | m11 | raw_mention |  |  |  |
| ent_m14 | object | edge | edge | object | m14 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | speed | speed | speed |  | agent:m0->ent_m0 |  |
| ce1 | m13 | mark | mark | mark |  | agent:m6->ent_m6; patient:m14->ent_m14 |  |
| ce2 | m15 | surrounded | surround | surround |  | agent:m6->ent_m6 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | speed | agent | m0 | ent_m0 | medium | e5 | nsubj -> speed |  |  |
| ce1 | mark | agent | m6 | ent_m6 | medium | e6 | nsubj -> mark |  |  |
| ce1 | mark | patient | m14 | ent_m14 | medium | e7 | dobj -> mark |  |  |
| ce2 | surround | agent | m6 | ent_m6 | medium | e8 | inherited agent advcl -> mark |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | along | medium | e9 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | with | high | e10 | False | False |  |  |
| cr2 | m3 | m5 | ent_m3 | ent_m5 | in | high | e11 | False | False |  |  |
| cr3 | m6 | m8 | ent_m6 | ent_m8 | edge_of | medium | e12 | False | False |  |  |
| cr4 | m6 | m9 | ent_m6 | ent_m9 | by | medium | e13 | False | False |  |  |
| cr5 | m6 | m10 | ent_m6 | ent_m10 | by | medium | e14 | False | False |  |  |
| cr6 | m9 | m11 | ent_m9 | ent_m11 | in | high | e15 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 64

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `2e770d74f49aba6dcaec3dd5d64fe6c050f061791bcc10f025024298b09b3414`
**parse_path:** `sentence`

> A gallery space displays various small objects on white shelves and pedestals. The walls are illuminated by overhead lights, and a large black woven vase sits on a central pedestal. Several figurines and decorative items are arranged across the shelves in an indoor setting.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | space | space | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | gallery | gallery | compound_modifier | chunk0 | 1 | medium |
| m2 | object | objects | object | noun_chunk_root | chunk1 | 6 | high |
| m3 | quantity | various | various | approximate_quantity | chunk1 | 4 | medium |
| m4 | attribute | small | small | size_attribute | chunk1 | 5 | high |
| m5 | object | shelves | shelf | noun_chunk_root | chunk2 | 9 | high |
| m6 | attribute | white | white | color_attribute | chunk2 | 8 | high |
| m7 | object | pedestals | pedestal | noun_chunk_root | chunk3 | 11 | high |
| m8 | object | walls | wall | noun_chunk_root | chunk4 | 14 | high |
| m9 | object | lights | light | noun_chunk_root | chunk5 | 19 | high |
| m10 | attribute | overhead | overhead | modifier_attribute | chunk5 | 18 | medium |
| m11 | object | vase | vase | noun_chunk_root | chunk6 | 26 | high |
| m12 | attribute | large | large | size_attribute | chunk6 | 23 | high |
| m13 | attribute | black | black | color_attribute | chunk6 | 24 | high |
| m14 | attribute | woven | weave | state_attribute | chunk6 | 25 | medium |
| m15 | object | pedestal | pedestal | noun_chunk_root | chunk7 | 31 | high |
| m16 | attribute | central | central | modifier_attribute | chunk7 | 30 | medium |
| m17 | object | figurines | figurine | noun_chunk_root | chunk8 | 34 | high |
| m18 | quantity | Several | several | approximate_quantity | chunk8 | 33 | medium |
| m19 | object | items | item | noun_chunk_root | chunk9 | 37 | high |
| m20 | attribute | decorative | decorative | modifier_attribute | chunk9 | 36 | medium |
| m21 | object | shelves | shelf | noun_chunk_root | chunk10 | 42 | high |
| m22 | context | setting | setting | scene_context | chunk11 | 46 | high |
| m23 | attribute | indoor | indoor | modifier_attribute | chunk11 | 45 | medium |
| m24 | action | displays | display | verb_predicate | doc | 3 | high |
| m25 | action | illuminated | illuminate | verb_predicate | doc | 16 | high |
| m26 | action | sits | sit | verb_predicate | doc | 27 | high |
| m27 | action | arranged | arrange | verb_predicate | doc | 39 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 compound -> space |
| e1 | has_quantity | m2 | m3 | medium | chunk1 quantity -> objects |
| e2 | has_attribute | m2 | m4 | high | chunk1 amod -> objects |
| e3 | has_attribute | m5 | m6 | high | chunk2 amod -> shelves |
| e4 | has_attribute | m9 | m10 | medium | chunk5 amod -> lights |
| e5 | has_attribute | m11 | m12 | high | chunk6 amod -> vase |
| e6 | has_attribute | m11 | m13 | high | chunk6 amod -> vase |
| e7 | has_attribute | m11 | m14 | medium | chunk6 amod -> vase |
| e8 | has_attribute | m15 | m16 | medium | chunk7 amod -> pedestal |
| e9 | has_quantity | m17 | m18 | medium | chunk8 quantity -> figurines |
| e10 | has_attribute | m19 | m20 | medium | chunk9 amod -> items |
| e11 | has_context | scene | m22 | high | scene_context token setting |
| e12 | has_attribute | m22 | m23 | medium | chunk11 amod -> setting |
| e13 | agent | m24 | m0 | medium | nsubj -> displays |
| e14 | patient | m24 | m2 | medium | dobj -> displays |
| e15 | agent | m25 | m8 | medium | nsubjpass -> illuminated |
| e16 | agent | m26 | m11 | medium | nsubj -> sits |
| e17 | agent | m27 | m17 | medium | nsubjpass -> arranged |
| e18 | agent | m27 | m19 | medium | nsubjpass -> arranged |
| e19 | relation | m0 | m5 | high | on |
| e20 | relation | m0 | m7 | high | on |
| e21 | relation | m8 | m9 | medium | by |
| e22 | relation | m11 | m15 | high | on |
| e23 | relation | m17 | m21 | high | across |
| e24 | relation | m17 | m22 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | space | space | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | object | objects | object | m2 | raw_mention |  |  |  |
| ent_m5 | object | shelf | shelves | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | pedestal | pedestals | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | wall | walls | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | light | lights | object | m9 | raw_mention |  |  |  |
| ent_m11 | object | vase | vase | object | m11 | raw_mention |  |  |  |
| ent_m15 | object | pedestal | pedestal | object | m15 | raw_mention |  |  |  |
| ent_m17 | object | figurine | figurines | object | m17 | raw_mention |  |  |  |
| ent_m19 | object | item | items | object | m19 | raw_mention |  |  |  |
| ent_m21 | object | shelf | shelves | object | m21 | raw_mention |  |  |  |
| ent_m22 | context | setting | setting | object | m22 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m24 | displays | display | display |  | agent:m0->ent_m0; patient:m2->ent_m2 |  |
| ce1 | m25 | illuminated | illuminate | illuminate |  | theme:m8->ent_m8; by_agent_or_causer:m9->ent_m9 |  |
| ce2 | m26 | sits | sit | sit |  | agent:m11->ent_m11 |  |
| ce3 | m27 | arranged | arrange | arrange |  | theme:m17->ent_m17; theme:m19->ent_m19 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | display | agent | m0 | ent_m0 | medium | e13 | nsubj -> displays |  |  |
| ce0 | display | patient | m2 | ent_m2 | medium | e14 | dobj -> displays |  |  |
| ce1 | illuminate | theme | m8 | ent_m8 | medium | e15 | nsubjpass -> illuminated |  |  |
| ce1 | illuminate | by_agent_or_causer | m9 | ent_m9 | medium | e21 | passive by-frame |  |  |
| ce2 | sit | agent | m11 | ent_m11 | medium | e16 | nsubj -> sits |  |  |
| ce3 | arrange | theme | m17 | ent_m17 | medium | e17 | nsubjpass -> arranged |  |  |
| ce3 | arrange | theme | m19 | ent_m19 | medium | e18 | nsubjpass -> arranged |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m5 | ent_m0 | ent_m5 | on | high | e19 | False | False |  |  |
| cr1 | m0 | m7 | ent_m0 | ent_m7 | on | high | e20 | False | False |  |  |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | by | medium | e21 | True | False |  |  |
| cr3 | m11 | m15 | ent_m11 | ent_m15 | on | high | e22 | False | False |  |  |
| cr4 | m17 | m21 | ent_m17 | ent_m21 | across | high | e23 | False | False |  |  |
| cr5 | m17 | m22 | ent_m17 | ent_m22 | in | high | e24 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m25 | e15 | m8 |  |  | {"action_mention_id": "m25", "kind": "passive_subject_to_theme", "raw_edge_id": "e15", "target": "m8"} |
| passive_by_frame_to_event_role | m25 | e21 |  |  |  | {"action_mention_id": "m25", "by_agent_or_causer": "m9", "kind": "passive_by_frame_to_event_role", "raw_edge_id": "e21", "theme": "m8"} |
| passive_subject_to_theme | m27 | e17 | m17 |  |  | {"action_mention_id": "m27", "kind": "passive_subject_to_theme", "raw_edge_id": "e17", "target": "m17"} |
| passive_subject_to_theme | m27 | e18 | m19 |  |  | {"action_mention_id": "m27", "kind": "passive_subject_to_theme", "raw_edge_id": "e18", "target": "m19"} |

## 65

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `2ea7e3419477bceca7256393dfb88f8d01c1ef0286b54daac7e1555e4901fc14`
**parse_path:** `sentence`

> A man in a white shirt and jeans holds up a framed plaque above his head. Several people around him, some wearing masks, clap and look on under a large tent with “SÃO PAULO” visible on the wall behind.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “SÃO PAULO” | são_paulo | quote_text | doc_quote | 35 | high |
| m1 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m2 | object | shirt | shirt | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | white | white | color_attribute | chunk1 | 4 | high |
| m4 | object | jeans | jean | noun_chunk_root | chunk2 | 7 | high |
| m5 | object | plaque | plaque | noun_chunk_root | chunk3 | 12 | high |
| m6 | attribute | framed | frame | state_attribute | chunk3 | 11 | medium |
| m7 | object | head | head | noun_chunk_root | chunk4 | 15 | high |
| m8 | object | people | people | noun_chunk_root | chunk5 | 18 | high |
| m9 | quantity | Several | several | approximate_quantity | chunk5 | 17 | medium |
| m10 | quantity | some | some | indefinite_quantity | chunk7 | 22 | medium |
| m11 | object | masks | mask | noun_chunk_root | chunk8 | 24 | high |
| m12 | object | tent | tent | noun_chunk_root | chunk9 | 33 | high |
| m13 | attribute | large | large | size_attribute | chunk9 | 32 | high |
| m14 | object | wall | wall | noun_chunk_root | chunk11 | 39 | high |
| m15 | action | holds | hold | verb_predicate | doc | 8 | high |
| m16 | particle | up | up | phrasal_particle | action_particle | 9 | medium |
| m17 | action | wearing | wear | verb_predicate | doc | 23 | high |
| m18 | action | clap | clap | verb_predicate | doc | 26 | high |
| m19 | action | look | look | verb_predicate | doc | 28 | high |
| m20 | particle | on | on | phrasal_particle | action_particle | 29 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | chunk1 amod -> shirt |
| e1 | has_attribute | m5 | m6 | medium | chunk3 amod -> plaque |
| e2 | has_quantity | m8 | m9 | medium | chunk5 quantity -> people |
| e3 | has_attribute | m12 | m13 | high | chunk9 amod -> tent |
| e4 | agent | m15 | m1 | medium | nsubj -> holds |
| e5 | has_particle | m15 | m16 | medium | prt -> holds |
| e6 | patient | m15 | m5 | medium | dobj -> holds |
| e7 | agent | m17 | m8 | medium | inherited agent relcl -> people |
| e8 | patient | m17 | m11 | medium | dobj -> wearing |
| e9 | agent | m18 | m8 | medium | nsubj -> clap |
| e10 | has_particle | m19 | m20 | medium | prt -> look |
| e11 | agent | m19 | m8 | medium | inherited agent conj -> clap |
| e12 | relation | m1 | m2 | high | in |
| e13 | relation | m1 | m4 | high | in |
| e14 | relation | m1 | m7 | high | above |
| e15 | relation | m8 | m1 | high | around |
| e16 | relation | m8 | m12 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | man | man | person | m1 | raw_mention |  |  |  |
| ent_m2 | object | shirt | shirt | clothing | m2 | raw_mention |  |  |  |
| ent_m4 | object | jean | jeans | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | plaque | plaque | document | m5 | raw_mention |  |  |  |
| ent_m7 | object | head | head | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | people | people | person | m8 | raw_mention |  |  |  |
| ent_m11 | object | mask | masks | clothing | m11 | raw_mention |  |  |  |
| ent_m12 | object | tent | tent | object | m12 | raw_mention |  |  |  |
| ent_m14 | object | wall | wall | object | m14 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | holds | hold | hold_up | up | agent:m1->ent_m1; patient:m5->ent_m5 | phrasal_action:hold up |
| ce1 | m17 | wearing | wear | wear |  | agent:m8->ent_m8; patient:m11->ent_m11 |  |
| ce2 | m18 | clap | clap | clap |  | agent:m8->ent_m8 |  |
| ce3 | m19 | look | look | look | on | agent:m8->ent_m8 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | hold_up | agent | m1 | ent_m1 | medium | e4 | nsubj -> holds |  |  |
| ce0 | hold_up | patient | m5 | ent_m5 | medium | e6 | dobj -> holds |  |  |
| ce1 | wear | agent | m8 | ent_m8 | medium | e7 | inherited agent relcl -> people |  |  |
| ce1 | wear | patient | m11 | ent_m11 | medium | e8 | dobj -> wearing |  |  |
| ce2 | clap | agent | m8 | ent_m8 | medium | e9 | nsubj -> clap |  |  |
| ce3 | look | agent | m8 | ent_m8 | medium | e11 | inherited agent conj -> clap |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | in | high | e12 | False | False |  |  |
| cr1 | m1 | m4 | ent_m1 | ent_m4 | in | high | e13 | False | False |  |  |
| cr2 | m1 | m7 | ent_m1 | ent_m7 | above | high | e14 | False | False |  |  |
| cr3 | m8 | m1 | ent_m8 | ent_m1 | around | high | e15 | False | False |  |  |
| cr4 | m8 | m12 | ent_m8 | ent_m12 | under | high | e16 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| phrasal_action_canonicalized | m15 |  |  |  |  | {"action_mention_id": "m15", "canonical": "hold_up", "kind": "phrasal_action_canonicalized", "source": "visual_genome_relation_predicates", "term": "hold up"} |

## 66

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `2edad03d414cd9df97abed25e0e65973c277bf42adbb760c0ec6ff029323a814`
**parse_path:** `sentence`

> A young child in a white dress stands on an ornate chair. Curtains are visible behind them in the studio setting.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | child | child | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | young | young | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | dress | dress | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | white | white | color_attribute | chunk1 | 5 | high |
| m4 | object | chair | chair | noun_chunk_root | chunk2 | 11 | high |
| m5 | attribute | ornate | ornate | modifier_attribute | chunk2 | 10 | medium |
| m6 | object | Curtains | curtain | noun_chunk_root | chunk3 | 13 | high |
| m7 | context | setting | setting | scene_context | chunk5 | 21 | high |
| m8 | attribute | studio | studio | compound_modifier | chunk5 | 20 | medium |
| m9 | action | stands | stand | verb_predicate | doc | 7 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> child |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> dress |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> chair |
| e3 | has_context | scene | m7 | high | scene_context token setting |
| e4 | has_attribute | m7 | m8 | medium | chunk5 compound -> setting |
| e5 | agent | m9 | m0 | medium | nsubj -> stands |
| e6 | relation | m0 | m2 | high | in |
| e7 | relation | m0 | m4 | high | on |
| e8 | relation | m6 | m0 | high | behind |
| e9 | relation | m6 | m7 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | child | child | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | dress | dress | clothing | m2 | raw_mention |  |  |  |
| ent_m4 | object | chair | chair | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | curtain | Curtains | object | m6 | raw_mention |  |  |  |
| ent_m7 | context | setting | setting | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | stands | stand | stand |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e5 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | high | e6 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | high | e7 | False | False |  |  |
| cr2 | m6 | m0 | ent_m6 | ent_m0 | behind | high | e8 | False | False |  |  |
| cr3 | m6 | m7 | ent_m6 | ent_m7 | in | high | e9 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 67

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `2f2ce66431e5451a01520b02af91689e6522fad31385be669f56dadb3aede414`
**parse_path:** `sentence`

> People walk on a paved path near the Royal Festival Hall building.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | People | people | noun_chunk_root | chunk0 | 0 | high |
| m1 | object | path | path | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | paved | paved | visual_attribute | chunk1 | 4 | medium |
| m3 | object | building | building | noun_chunk_root | chunk2 | 11 | high |
| m4 | attribute | Royal | royal | compound_modifier | chunk2 | 8 | medium |
| m5 | attribute | Festival | festival | compound_modifier | chunk2 | 9 | medium |
| m6 | attribute | Hall | hall | compound_modifier | chunk2 | 10 | medium |
| m7 | action | walk | walk | verb_predicate | doc | 1 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 amod -> path |
| e1 | has_attribute | m3 | m4 | medium | chunk2 compound -> building |
| e2 | has_attribute | m3 | m5 | medium | chunk2 compound -> building |
| e3 | has_attribute | m3 | m6 | medium | chunk2 compound -> building |
| e4 | agent | m7 | m0 | medium | nsubj -> walk |
| e5 | relation | m0 | m1 | high | on |
| e6 | relation | m0 | m3 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | People | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | path | path | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | building | building | object | m3 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | walk | walk | walk |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | walk | agent | m0 | ent_m0 | medium | e4 | nsubj -> walk |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | on | high | e5 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | near | high | e6 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 68

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `3156569e74ddc3825ce976fcaee3c3b3785db75d9d7d869ec496d5cb4daa5c14`
**parse_path:** `sentence`

> A rugged canyon with steep cliffs and sparse greenery. A small white house sits at the bottom of the valley.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | canyon | canyon | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | rugged | rugged | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | cliffs | cliff | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | steep | steep | modifier_attribute | chunk1 | 4 | medium |
| m4 | object | greenery | greenery | noun_chunk_root | chunk2 | 8 | high |
| m5 | attribute | sparse | sparse | modifier_attribute | chunk2 | 7 | medium |
| m6 | object | house | house | noun_chunk_root | chunk3 | 13 | high |
| m7 | attribute | small | small | size_attribute | chunk3 | 11 | high |
| m8 | attribute | white | white | color_attribute | chunk3 | 12 | high |
| m9 | object | valley | valley | noun_chunk_root | chunk5 | 20 | high |
| m10 | action | sits | sit | verb_predicate | doc | 14 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> canyon |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> cliffs |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> greenery |
| e3 | has_attribute | m6 | m7 | high | chunk3 amod -> house |
| e4 | has_attribute | m6 | m8 | high | chunk3 amod -> house |
| e5 | agent | m10 | m6 | medium | nsubj -> sits |
| e6 | relation | m0 | m2 | high | with |
| e7 | relation | m0 | m4 | high | with |
| e8 | relation | m6 | m9 | high | bottom_of |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | canyon | canyon | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | cliff | cliffs | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | greenery | greenery | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | house | house | object | m6 | raw_mention |  |  |  |
| ent_m9 | object | valley | valley | object | m9 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | sits | sit | sit |  | agent:m6->ent_m6 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m6 | ent_m6 | medium | e5 | nsubj -> sits |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e6 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | high | e7 | False | False |  |  |
| cr2 | m6 | m9 | ent_m6 | ent_m9 | bottom_of | high | e8 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 69

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `3302576e9b3fa334f206532a50a7c9f7dcd858f3ea8b2990723b089efcee1c14`
**parse_path:** `sentence`

> A phylogenetic tree shows evolutionary relationships among rodents, with icons of a leporid rabbit and an ocotoid rodent. Below, a graph tracks global temperature and vegetation changes over time, marked with key events like C3 grass origin and C4 expansion.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | tree | tree | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | phylogenetic | phylogenetic | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | relationships | relationship | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | evolutionary | evolutionary | modifier_attribute | chunk1 | 4 | medium |
| m4 | object | rodents | rodent | noun_chunk_root | chunk2 | 7 | high |
| m5 | object | icons | icon | noun_chunk_root | chunk3 | 10 | high |
| m6 | object | rabbit | rabbit | noun_chunk_root | chunk4 | 14 | high |
| m7 | attribute | leporid | leporid | modifier_attribute | chunk4 | 13 | medium |
| m8 | object | rodent | rodent | noun_chunk_root | chunk5 | 18 | high |
| m9 | attribute | ocotoid | ocotoid | compound_modifier | chunk5 | 17 | medium |
| m10 | object | graph | graph | noun_chunk_root | chunk6 | 23 | high |
| m11 | object | temperature | temperature | noun_chunk_root | chunk7 | 26 | high |
| m12 | attribute | global | global | modifier_attribute | chunk7 | 25 | medium |
| m13 | object | changes | change | noun_chunk_root | chunk8 | 29 | high |
| m14 | attribute | vegetation | vegetation | compound_modifier | chunk8 | 28 | medium |
| m15 | object | time | time | noun_chunk_root | chunk9 | 31 | high |
| m16 | object | events | event | noun_chunk_root | chunk10 | 36 | high |
| m17 | attribute | key | key | modifier_attribute | chunk10 | 35 | medium |
| m18 | object | origin | origin | noun_chunk_root | chunk11 | 40 | high |
| m19 | attribute | C3 | c3 | compound_modifier | chunk11 | 38 | medium |
| m20 | attribute | grass | grass | compound_modifier | chunk11 | 39 | medium |
| m21 | object | expansion | expansion | noun_chunk_root | chunk12 | 43 | high |
| m22 | attribute | C4 | c4 | compound_modifier | chunk12 | 42 | medium |
| m23 | action | shows | show | verb_predicate | doc | 3 | high |
| m24 | action | tracks | track | verb_predicate | doc | 24 | high |
| m25 | action | marked | mark | verb_predicate | doc | 33 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> tree |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> relationships |
| e2 | has_attribute | m6 | m7 | medium | chunk4 amod -> rabbit |
| e3 | has_attribute | m8 | m9 | medium | chunk5 compound -> rodent |
| e4 | has_attribute | m11 | m12 | medium | chunk7 amod -> temperature |
| e5 | has_attribute | m13 | m14 | medium | chunk8 compound -> changes |
| e6 | has_attribute | m16 | m17 | medium | chunk10 amod -> events |
| e7 | has_attribute | m18 | m19 | medium | chunk11 compound -> origin |
| e8 | has_attribute | m18 | m20 | medium | chunk11 compound -> origin |
| e9 | has_attribute | m21 | m22 | medium | chunk12 compound -> expansion |
| e10 | agent | m23 | m0 | medium | nsubj -> shows |
| e11 | patient | m23 | m2 | medium | dobj -> shows |
| e12 | agent | m24 | m10 | medium | nsubj -> tracks |
| e13 | patient | m24 | m11 | medium | dobj -> tracks |
| e14 | patient | m24 | m13 | medium | dobj -> tracks |
| e15 | agent | m25 | m10 | medium | inherited agent advcl -> tracks |
| e16 | relation | m2 | m4 | medium | among |
| e17 | relation | m0 | m5 | high | with |
| e18 | relation | m5 | m6 | medium | of |
| e19 | relation | m5 | m8 | medium | of |
| e20 | relation | m11 | m15 | high | over |
| e21 | relation | m10 | m16 | high | with |
| e22 | relation | m16 | m18 | medium | like |
| e23 | relation | m16 | m21 | medium | like |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | tree | tree | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | relationship | relationships | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | rodent | rodents | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | icon | icons | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | rabbit | rabbit | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | rodent | rodent | object | m8 | raw_mention |  |  |  |
| ent_m10 | object | graph | graph | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | temperature | temperature | object | m11 | raw_mention |  |  |  |
| ent_m13 | object | change | changes | object | m13 | raw_mention |  |  |  |
| ent_m15 | object | time | time | object | m15 | raw_mention |  |  |  |
| ent_m16 | object | event | events | object | m16 | raw_mention |  |  |  |
| ent_m18 | object | origin | origin | object | m18 | raw_mention |  |  |  |
| ent_m21 | object | expansion | expansion | object | m21 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m23 | shows | show | show |  | agent:m0->ent_m0; patient:m2->ent_m2 |  |
| ce1 | m24 | tracks | track | track |  | agent:m10->ent_m10; patient:m11->ent_m11; patient:m13->ent_m13 |  |
| ce2 | m25 | marked | mark | mark |  | agent:m10->ent_m10 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | m0 | ent_m0 | medium | e10 | nsubj -> shows |  |  |
| ce0 | show | patient | m2 | ent_m2 | medium | e11 | dobj -> shows |  |  |
| ce1 | track | agent | m10 | ent_m10 | medium | e12 | nsubj -> tracks |  |  |
| ce1 | track | patient | m11 | ent_m11 | medium | e13 | dobj -> tracks |  |  |
| ce1 | track | patient | m13 | ent_m13 | medium | e14 | dobj -> tracks |  |  |
| ce2 | mark | agent | m10 | ent_m10 | medium | e15 | inherited agent advcl -> tracks |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m2 | m4 | ent_m2 | ent_m4 | among | medium | e16 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | with | high | e17 | False | False |  |  |
| cr2 | m5 | m6 | ent_m5 | ent_m6 | of | medium | e18 | False | False |  |  |
| cr3 | m5 | m8 | ent_m5 | ent_m8 | of | medium | e19 | False | False |  |  |
| cr4 | m11 | m15 | ent_m11 | ent_m15 | over | high | e20 | False | False |  |  |
| cr5 | m10 | m16 | ent_m10 | ent_m16 | with | high | e21 | False | False |  |  |
| cr6 | m16 | m18 | ent_m16 | ent_m18 | like | medium | e22 | False | False |  |  |
| cr7 | m16 | m21 | ent_m16 | ent_m21 | like | medium | e23 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 70

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `33197bd517edd2b2a5fb1c6efdd1b00b2583e2a3ebe9acf2249c6cce3afa3414`
**parse_path:** `sentence`

> A man in a blue and gray vest stands next to a woman in a gray corset, both at a party.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | vest | vest | noun_chunk_root | chunk1 | 7 | high |
| m2 | attribute | blue | blue | color_attribute | chunk1 | 4 | high |
| m3 | attribute | gray | gray | color_attribute | chunk1 | 6 | high |
| m4 | object | woman | woman | noun_chunk_root | chunk2 | 12 | high |
| m5 | object | corset | corset | noun_chunk_root | chunk3 | 16 | high |
| m6 | attribute | gray | gray | color_attribute | chunk3 | 15 | high |
| m7 | object | party | party | noun_chunk_root | chunk4 | 21 | high |
| m8 | action | stands | stand | verb_predicate | doc | 8 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> vest |
| e1 | has_attribute | m1 | m3 | high | chunk1 conj -> vest |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> corset |
| e3 | agent | m8 | m0 | medium | nsubj -> stands |
| e4 | relation | m0 | m1 | high | in |
| e5 | relation | m0 | m4 | high | next_to |
| e6 | relation | m4 | m5 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | vest | vest | clothing | m1 | raw_mention |  |  |  |
| ent_m4 | object | woman | woman | person | m4 | raw_mention |  |  |  |
| ent_m5 | object | corset | corset | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | party | party | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | stands | stand | stand |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e3 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e4 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | next_to | high | e5 | False | False |  |  |
| cr2 | m4 | m5 | ent_m4 | ent_m5 | in | high | e6 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 71

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `331f38a142eb3d5bffb9d33eaec80a194a9f24567abee2b86a20b4258139c414`
**parse_path:** `sentence`

> A man in a blue suit and tie stands at a clear podium, waving with his right hand. Behind him is a large white backdrop with the “POLAND25.EU” logo repeated across it. He wears glasses and has a lanyard around his neck.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “POLAND25.EU” | poland25.eu | quote_text | doc_quote | 28 | high |
| m1 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m2 | object | suit | suit | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | blue | blue | color_attribute | chunk1 | 4 | high |
| m4 | object | tie | tie | noun_chunk_root | chunk2 | 7 | high |
| m5 | object | podium | podium | noun_chunk_root | chunk3 | 12 | high |
| m6 | attribute | clear | clear | visual_attribute | chunk3 | 11 | medium |
| m7 | object | right hand | right_hand | noun_chunk_root | chunk4 | 17 | high |
| m8 | object | backdrop | backdrop | noun_chunk_root | chunk6 | 25 | high |
| m9 | attribute | large | large | size_attribute | chunk6 | 23 | high |
| m10 | attribute | white | white | color_attribute | chunk6 | 24 | high |
| m11 | object | logo | logo | noun_chunk_root | chunk7 | 29 | high |
| m12 | object | glasses | glass | noun_chunk_root | chunk10 | 36 | high |
| m13 | object | lanyard | lanyard | noun_chunk_root | chunk11 | 40 | high |
| m14 | object | neck | neck | noun_chunk_root | chunk12 | 43 | high |
| m15 | action | stands | stand | verb_predicate | doc | 8 | high |
| m16 | action | waving | wave | verb_predicate | doc | 14 | high |
| m17 | action | repeated | repeat | verb_predicate | doc | 30 | high |
| m18 | action | wears | wear | verb_predicate | doc | 35 | high |
| m19 | action | has | have | verb_predicate | doc | 38 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | chunk1 amod -> suit |
| e1 | has_attribute | m5 | m6 | medium | chunk3 amod -> podium |
| e2 | has_attribute | m8 | m9 | high | chunk6 amod -> backdrop |
| e3 | has_attribute | m8 | m10 | high | chunk6 amod -> backdrop |
| e4 | agent | m15 | m1 | medium | nsubj -> stands |
| e5 | agent | m16 | m1 | medium | inherited agent advcl -> stands |
| e6 | agent | m17 | m11 | medium | inherited agent acl -> logo |
| e7 | agent | m18 | m1 | medium | nsubj -> wears; resolved He -> man |
| e8 | patient | m18 | m12 | medium | dobj -> wears |
| e9 | agent | m19 | m1 | medium | inherited agent conj -> wears |
| e10 | patient | m19 | m13 | medium | dobj -> has |
| e11 | relation | m1 | m2 | high | in |
| e12 | relation | m1 | m4 | high | in |
| e13 | relation | m1 | m5 | medium | at |
| e14 | relation | m1 | m7 | high | with |
| e15 | relation | m8 | m1 | high | behind |
| e16 | relation | m8 | m11 | high | with |
| e17 | relation | m11 | m8 | high | across |
| e18 | relation | m1 | m14 | high | around |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | man | man | person | m1 | raw_mention |  |  |  |
| ent_m2 | object | suit | suit | clothing | m2 | raw_mention |  |  |  |
| ent_m4 | object | tie | tie | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | podium | podium | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | right_hand | right hand | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | backdrop | backdrop | object | m8 | raw_mention |  |  |  |
| ent_m11 | object | logo | logo | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | glass | glasses | object | m12 | raw_mention |  |  |  |
| ent_m13 | object | lanyard | lanyard | object | m13 | raw_mention |  |  |  |
| ent_m14 | object | neck | neck | object | m14 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | stands | stand | stand |  | agent:m1->ent_m1 |  |
| ce1 | m16 | waving | wave | wave |  | agent:m1->ent_m1 |  |
| ce2 | m17 | repeated | repeat | repeat |  | agent:m11->ent_m11 |  |
| ce3 | m18 | wears | wear | wear |  | agent:m1->ent_m1; patient:m12->ent_m12 |  |
| ce4 | m19 | has | have | have |  | agent:m1->ent_m1; patient:m13->ent_m13 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m1 | ent_m1 | medium | e4 | nsubj -> stands |  |  |
| ce1 | wave | agent | m1 | ent_m1 | medium | e5 | inherited agent advcl -> stands |  |  |
| ce2 | repeat | agent | m11 | ent_m11 | medium | e6 | inherited agent acl -> logo |  |  |
| ce3 | wear | agent | m1 | ent_m1 | medium | e7 | nsubj -> wears; resolved He -> man |  |  |
| ce3 | wear | patient | m12 | ent_m12 | medium | e8 | dobj -> wears |  |  |
| ce4 | have | agent | m1 | ent_m1 | medium | e9 | inherited agent conj -> wears |  |  |
| ce4 | have | patient | m13 | ent_m13 | medium | e10 | dobj -> has |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | in | high | e11 | False | False |  |  |
| cr1 | m1 | m4 | ent_m1 | ent_m4 | in | high | e12 | False | False |  |  |
| cr2 | m1 | m5 | ent_m1 | ent_m5 | at | medium | e13 | False | False |  |  |
| cr3 | m1 | m7 | ent_m1 | ent_m7 | with | high | e14 | False | False |  |  |
| cr4 | m8 | m1 | ent_m8 | ent_m1 | behind | high | e15 | False | False |  |  |
| cr5 | m8 | m11 | ent_m8 | ent_m11 | with | high | e16 | False | False |  |  |
| cr6 | m11 | m8 | ent_m11 | ent_m8 | across | high | e17 | False | False |  |  |
| cr7 | m1 | m14 | ent_m1 | ent_m14 | around | high | e18 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 72

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `34cc48489fc531611fc9cdcecbf86ecd6a5ea1c440dce0396926c8f2fb6b5814`
**parse_path:** `sentence`

> A large, old machine stands in a dimly lit room with brick walls and pipes.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | machine | machine | noun_chunk_root | chunk0 | 4 | high |
| m1 | attribute | large | large | size_attribute | chunk0 | 1 | high |
| m2 | attribute | old | old | visual_attribute | chunk0 | 3 | medium |
| m3 | object | room | room | noun_chunk_root | chunk1 | 10 | high |
| m4 | attribute | dimly | dimly | modifier_attribute | chunk1 | 8 | medium |
| m5 | attribute | lit | light | visual_attribute | chunk1 | 9 | medium |
| m6 | object | walls | wall | noun_chunk_root | chunk2 | 13 | high |
| m7 | attribute | brick | brick | material_attribute | chunk2 | 12 | high |
| m8 | object | pipes | pipe | noun_chunk_root | chunk3 | 15 | high |
| m9 | action | stands | stand | verb_predicate | doc | 5 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> machine |
| e1 | has_attribute | m0 | m2 | medium | chunk0 amod -> machine |
| e2 | has_attribute | m3 | m4 | medium | chunk1 advmod -> room |
| e3 | has_attribute | m3 | m5 | medium | chunk1 amod -> room |
| e4 | has_attribute | m6 | m7 | high | chunk2 compound -> walls |
| e5 | agent | m9 | m0 | medium | nsubj -> stands |
| e6 | relation | m0 | m3 | high | in |
| e7 | relation | m3 | m6 | high | with |
| e8 | relation | m3 | m8 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | machine | machine | object | m0 | raw_mention |  |  |  |
| ent_m3 | object | room | room | object | m3 | raw_mention |  |  |  |
| ent_m6 | object | wall | walls | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | pipe | pipes | object | m8 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | stands | stand | stand |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e5 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | in | high | e6 | False | False |  |  |
| cr1 | m3 | m6 | ent_m3 | ent_m6 | with | high | e7 | False | False |  |  |
| cr2 | m3 | m8 | ent_m3 | ent_m8 | with | high | e8 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 73

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `34d700de50423ef5fba9bd0844a97c65242517a160b5fd1d1f1efde9bb74c414`
**parse_path:** `sentence`

> A red sports car with the number 27 is parked on a racetrack. Two people stand next to it—one in a blue jacket and another in a black jacket—on a paved surface with hills and trees in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | sports car | sports_car | noun_chunk_root | chunk0 | 2 | high |
| m1 | object | number | number | noun_chunk_root | chunk1 | 5 | high |
| m2 | object | racetrack | racetrack | noun_chunk_root | chunk2 | 11 | high |
| m3 | object | people | people | noun_chunk_root | chunk3 | 14 | high |
| m4 | quantity | Two | two | exact_quantity | chunk3 | 13 | high |
| m5 | object | jacket | jacket | noun_chunk_root | chunk5 | 24 | high |
| m6 | attribute | blue | blue | color_attribute | chunk5 | 23 | high |
| m7 | object | jacket | jacket | noun_chunk_root | chunk7 | 30 | high |
| m8 | attribute | black | black | color_attribute | chunk7 | 29 | high |
| m9 | object | paved surface | paved_surface | noun_chunk_root | chunk8 | 34 | high |
| m10 | object | hills | hill | noun_chunk_root | chunk9 | 36 | high |
| m11 | object | trees | tree | noun_chunk_root | chunk10 | 38 | high |
| m12 | context | background | background | scene_context | chunk11 | 41 | high |
| m13 | reference | one | one | singular_substitute | nominal_reference | 20 | high |
| m14 | reference | another | another | contrastive_reference | nominal_reference | 26 | high |
| m15 | action | parked | park | verb_predicate | doc | 8 | high |
| m16 | action | stand | stand | verb_predicate | doc | 15 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m3 | m4 | high | chunk3 quantity -> people |
| e1 | has_attribute | m5 | m6 | high | chunk5 amod -> jacket |
| e2 | has_attribute | m7 | m8 | high | chunk7 amod -> jacket |
| e3 | has_context | scene | m12 | high | scene_context token background |
| e4 | refers_to | m13 | m3 | high | singular_substitute one -> people; score=103 |
| e5 | refers_to | m14 | m3 | high | contrastive_reference another -> people; score=112 |
| e6 | agent | m15 | m0 | medium | nsubjpass -> parked |
| e7 | agent | m16 | m3 | medium | nsubj -> stand |
| e8 | relation | m0 | m1 | high | with |
| e9 | relation | m0 | m2 | high | on |
| e10 | relation | m3 | m0 | high | next_to |
| e11 | relation | m3 | m5 | high | in |
| e12 | relation | m3 | m7 | high | in |
| e13 | relation | m3 | m9 | high | on |
| e14 | relation | m9 | m10 | high | with |
| e15 | relation | m9 | m11 | high | with |
| e16 | relation | m10 | m12 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sports_car | sports car | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | number | number | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | racetrack | racetrack | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | people | people | person | m3 | raw_mention |  |  |  |
| ent_m5 | object | jacket | jacket | clothing | m5 | raw_mention |  |  |  |
| ent_m7 | object | jacket | jacket | clothing | m7 | raw_mention |  |  |  |
| ent_m9 | object | paved_surface | paved surface | object | m9 | raw_mention |  |  |  |
| ent_m10 | object | hill | hills | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | tree | trees | object | m11 | raw_mention |  |  |  |
| ent_m12 | context | background | background | object | m12 | raw_mention |  |  |  |
| eref_m13 | instance | people | one | person | m13 | stage9_reference | ent_m3 |  | 1 |
| eref_m14 | contrastive_instance | people | another | person | m14 | stage9_reference | ent_m3 |  | 1 |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m13 | eref_m13 | m3 | ent_m3 | high |  |
| refers_to | m14 | eref_m14 | m3 | ent_m3 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | parked | park | park |  | theme:m0->ent_m0 |  |
| ce1 | m16 | stand | stand | stand |  | agent:m3->ent_m3 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | park | theme | m0 | ent_m0 | medium | e6 | nsubjpass -> parked |  |  |
| ce1 | stand | agent | m3 | ent_m3 | medium | e7 | nsubj -> stand |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | high | e8 | False | False |  |  |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | on | high | e9 | False | False |  |  |
| cr2 | m3 | m0 | ent_m3 | ent_m0 | next_to | high | e10 | False | False |  |  |
| cr3 | m3 | m5 | eref_m13 | ent_m5 | in | high | e11 | False | False |  |  |
| cr4 | m3 | m7 | eref_m14 | ent_m7 | in | high | e12 | False | False |  |  |
| cr5 | m3 | m9 | ent_m3 | ent_m9 | on | high | e13 | False | False |  |  |
| cr6 | m9 | m10 | ent_m9 | ent_m10 | with | high | e14 | False | False |  |  |
| cr7 | m9 | m11 | ent_m9 | ent_m11 | with | high | e15 | False | False |  |  |
| cr8 | m10 | m12 | ent_m10 | ent_m12 | in | high | e16 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m15 | e6 | m0 |  |  | {"action_mention_id": "m15", "kind": "passive_subject_to_theme", "raw_edge_id": "e6", "target": "m0"} |

## 74

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `350de576a5a0ff340ea1b59f179de89068808c02979c1eb6ae6f29e29b104414`
**parse_path:** `sentence`

> A handwritten list on lined paper shows names and details in a table format. The document is labeled "Shipping Office, Canterbury Association" at the top with printed and typed text. Several entries are filled out by hand, including dates and signatures.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "Shipping Office, Canterbury Association" | shipping_office,_canterbury_association | quote_text | doc_quote | 19 | high |
| m1 | object | list | list | noun_chunk_root | chunk0 | 2 | high |
| m2 | attribute | handwritten | handwritten | modifier_attribute | chunk0 | 1 | medium |
| m3 | object | paper | paper | noun_chunk_root | chunk1 | 5 | high |
| m4 | attribute | lined | lined | modifier_attribute | chunk1 | 4 | medium |
| m5 | object | names | name | noun_chunk_root | chunk2 | 7 | high |
| m6 | object | details | detail | noun_chunk_root | chunk3 | 9 | high |
| m7 | object | format | format | noun_chunk_root | chunk4 | 13 | high |
| m8 | attribute | table | table | compound_modifier | chunk4 | 12 | medium |
| m9 | object | document | document | noun_chunk_root | chunk5 | 16 | high |
| m10 | context | top | top | spatial_region | chunk7 | 22 | medium |
| m11 | object | text | text | noun_chunk_root | chunk8 | 27 | high |
| m12 | attribute | printed | print | state_attribute | chunk8 | 24 | medium |
| m13 | object | entries | entry | noun_chunk_root | chunk9 | 30 | high |
| m14 | quantity | Several | several | approximate_quantity | chunk9 | 29 | medium |
| m15 | object | hand | hand | noun_chunk_root | chunk10 | 35 | high |
| m16 | object | dates | date | noun_chunk_root | chunk11 | 38 | high |
| m17 | object | signatures | signature | noun_chunk_root | chunk12 | 40 | high |
| m18 | action | shows | show | verb_predicate | doc | 6 | high |
| m19 | action | labeled | label | verb_predicate | doc | 18 | high |
| m20 | action | typed | type | verb_predicate | doc | 26 | high |
| m21 | action | filled | fill | verb_predicate | doc | 32 | high |
| m22 | particle | out | out | phrasal_particle | action_particle | 33 | medium |
| m23 | action | including | include | verb_predicate | doc | 37 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk0 amod -> list |
| e1 | has_attribute | m3 | m4 | medium | chunk1 amod -> paper |
| e2 | has_attribute | m7 | m8 | medium | chunk4 compound -> format |
| e3 | has_attribute | m11 | m12 | medium | chunk8 amod -> text |
| e4 | has_quantity | m13 | m14 | medium | chunk9 quantity -> entries |
| e5 | agent | m18 | m1 | medium | nsubj -> shows |
| e6 | patient | m18 | m5 | medium | dobj -> shows |
| e7 | patient | m18 | m6 | medium | dobj -> shows |
| e8 | agent | m19 | m9 | medium | nsubjpass -> labeled |
| e9 | patient | m19 | m0 | medium | oprd -> labeled |
| e10 | agent | m21 | m13 | medium | nsubjpass -> filled |
| e11 | has_particle | m21 | m22 | medium | prt -> filled |
| e12 | agent | m23 | m13 | medium | inherited agent prep -> entries |
| e13 | patient | m23 | m16 | medium | pobj -> including |
| e14 | patient | m23 | m17 | medium | pobj -> including |
| e15 | relation | m1 | m3 | high | on |
| e16 | relation | m1 | m7 | high | in |
| e17 | relation | m9 | m10 | medium | at |
| e18 | relation | m9 | m11 | high | with |
| e19 | relation | m13 | m15 | medium | by |
| e20 | relation | m13 | m16 | medium | include |
| e21 | relation | m13 | m17 | medium | include |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | list | list | document | m1 | raw_mention |  |  |  |
| ent_m3 | object | paper | paper | document | m3 | raw_mention |  |  |  |
| ent_m5 | object | name | names | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | detail | details | object | m6 | raw_mention |  |  |  |
| ent_m7 | object | format | format | object | m7 | raw_mention |  |  |  |
| ent_m9 | object | document | document | document | m9 | raw_mention |  |  |  |
| ent_m10 | context | top | top | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | text | text | document | m11 | raw_mention |  |  |  |
| ent_m13 | object | entry | entries | object | m13 | raw_mention |  |  |  |
| ent_m15 | object | hand | hand | object | m15 | raw_mention |  |  |  |
| ent_m16 | object | date | dates | object | m16 | raw_mention |  |  |  |
| ent_m17 | object | signature | signatures | object | m17 | raw_mention |  |  |  |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| generic_alias | m9 | ent_m9 |  | ent_m3 | medium |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | shows | show | show |  | agent:m1->ent_m1; patient:m5->ent_m5; patient:m6->ent_m6 |  |
| ce1 | m19 | labeled | label | label |  | theme:m9->ent_m3; patient:m0->None |  |
| ce2 | m20 | typed | type | type |  |  |  |
| ce3 | m21 | filled | fill | fill | out | theme:m13->ent_m13; by_agent_or_causer:m15->ent_m15 |  |
| ce4 | m23 | including | include | include |  | agent:m13->ent_m13; patient:m16->ent_m16; patient:m17->ent_m17 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | m1 | ent_m1 | medium | e5 | nsubj -> shows |  |  |
| ce0 | show | patient | m5 | ent_m5 | medium | e6 | dobj -> shows |  |  |
| ce0 | show | patient | m6 | ent_m6 | medium | e7 | dobj -> shows |  |  |
| ce1 | label | theme | m9 | ent_m3 | medium | e8 | nsubjpass -> labeled |  |  |
| ce1 | label | patient | m0 |  | medium | e9 | oprd -> labeled |  |  |
| ce3 | fill | theme | m13 | ent_m13 | medium | e10 | nsubjpass -> filled |  |  |
| ce3 | fill | by_agent_or_causer | m15 | ent_m15 | medium | e19 | passive by-frame |  |  |
| ce4 | include | agent | m13 | ent_m13 | medium | e12 | inherited agent prep -> entries |  |  |
| ce4 | include | patient | m16 | ent_m16 | medium | e13 | pobj -> including |  |  |
| ce4 | include | patient | m17 | ent_m17 | medium | e14 | pobj -> including |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m3 | ent_m1 | ent_m3 | on | high | e15 | False | False |  |  |
| cr1 | m1 | m7 | ent_m1 | ent_m7 | in | high | e16 | False | False |  |  |
| cr2 | m9 | m10 | ent_m3 | ent_m10 | at | medium | e17 | False | False |  |  |
| cr3 | m9 | m11 | ent_m3 | ent_m11 | with | high | e18 | False | False |  |  |
| cr4 | m13 | m15 | ent_m13 | ent_m15 | by | medium | e19 | True | False |  |  |
| cr5 | m13 | m16 | ent_m13 | ent_m16 | include | medium | e20 | False | False |  |  |
| cr6 | m13 | m17 | ent_m13 | ent_m17 | include | medium | e21 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m19 | e8 | m9 |  |  | {"action_mention_id": "m19", "kind": "passive_subject_to_theme", "raw_edge_id": "e8", "target": "m9"} |
| passive_subject_to_theme | m21 | e10 | m13 |  |  | {"action_mention_id": "m21", "kind": "passive_subject_to_theme", "raw_edge_id": "e10", "target": "m13"} |
| passive_by_frame_to_event_role | m21 | e19 |  |  |  | {"action_mention_id": "m21", "by_agent_or_causer": "m15", "kind": "passive_by_frame_to_event_role", "raw_edge_id": "e19", "theme": "m13"} |

## 75

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `35a8a2cb41d086897a80f0315db645719b1baf055872b152dfc5f95630924c14`
**parse_path:** `tag_list`

> person, path, trees, lake, fence

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | segment_head | t0 | 0 | high |
| m1 | object | path | path | segment_head | t1 | 0 | high |
| m2 | object | trees | tree | segment_head | t2 | 0 | high |
| m3 | object | lake | lake | segment_head | t3 | 0 | high |
| m4 | object | fence | fence | segment_head | t4 | 0 | high |

### Raw Concept Edges
_none_

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | path | path | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | tree | trees | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | lake | lake | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | fence | fence | object | m4 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 76

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `361f12f9479f0114f214410da64dfdec98173f5d972c21e3be8d788c62f2a414`
**parse_path:** `sentence`

> Three men in suits stand at a podium with a microphone. One man speaks while the others listen, positioned behind him near flags and a marble wall. A plaque on the podium reads “ASSEMBLEIA LEGISLATIVA.”

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “ASSEMBLEIA LEGISLATIVA.” | assembleia_legislativa. | quote_text | doc_quote | 36 | high |
| m1 | object | men | man | noun_chunk_root | chunk0 | 1 | high |
| m2 | quantity | Three | three | exact_quantity | chunk0 | 0 | high |
| m3 | object | suits | suit | noun_chunk_root | chunk1 | 3 | high |
| m4 | object | podium | podium | noun_chunk_root | chunk2 | 7 | high |
| m5 | object | microphone | microphone | noun_chunk_root | chunk3 | 10 | high |
| m6 | object | man | man | noun_chunk_root | chunk4 | 13 | high |
| m7 | quantity | One | one | exact_quantity | chunk4 | 12 | high |
| m8 | object | flags | flag | noun_chunk_root | chunk7 | 24 | high |
| m9 | object | wall | wall | noun_chunk_root | chunk8 | 28 | high |
| m10 | attribute | marble | marble | compound_modifier | chunk8 | 27 | medium |
| m11 | object | plaque | plaque | noun_chunk_root | chunk9 | 31 | high |
| m12 | object | podium | podium | noun_chunk_root | chunk10 | 34 | high |
| m13 | reference | others | other | contrastive_reference | nominal_reference | 17 | high |
| m14 | action | stand | stand | verb_predicate | doc | 4 | high |
| m15 | action | speaks | speak | verb_predicate | doc | 14 | high |
| m16 | action | listen | listen | verb_predicate | doc | 18 | high |
| m17 | action | positioned | position | verb_predicate | doc | 20 | high |
| m18 | action | reads | read | verb_predicate | doc | 35 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m1 | m2 | high | chunk0 quantity -> men |
| e1 | has_quantity | m6 | m7 | high | chunk4 quantity -> man |
| e2 | has_attribute | m9 | m10 | medium | chunk8 compound -> wall |
| e3 | refers_to | m13 | m1 | high | contrastive_reference others -> men; score=118; margin=30 |
| e4 | agent | m14 | m1 | medium | nsubj -> stand |
| e5 | agent | m15 | m6 | medium | nsubj -> speaks |
| e6 | agent | m16 | m1 | medium | nsubj -> listen; resolved others -> men |
| e7 | agent | m17 | m6 | medium | inherited agent advcl -> speaks |
| e8 | agent | m18 | m11 | medium | nsubj -> reads |
| e9 | patient | m18 | m0 | medium | dobj -> reads |
| e10 | relation | m1 | m3 | high | in |
| e11 | relation | m1 | m4 | medium | at |
| e12 | relation | m1 | m5 | high | with |
| e13 | relation | m6 | m8 | high | near |
| e14 | relation | m6 | m9 | high | near |
| e15 | relation | m11 | m12 | high | on |

### Skipped Raw Concept Edges
| type | source | target | confidence | reason | evidence |
| --- | --- | --- | --- | --- | --- |
| relation | m6 | m6 | high | self_edge_after_coref | behind |

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | man | men | person | m1 | raw_mention |  |  |  |
| ent_m3 | object | suit | suits | clothing | m3 | raw_mention |  |  |  |
| ent_m4 | object | podium | podium | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | microphone | microphone | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | man | man | person | m6 | raw_mention |  |  |  |
| ent_m8 | object | flag | flags | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | wall | wall | object | m9 | raw_mention |  |  |  |
| ent_m11 | object | plaque | plaque | document | m11 | raw_mention |  |  |  |
| ent_m12 | object | podium | podium | object | m12 | raw_mention |  |  |  |
| eref_m13 | complement_subset | man | others | person | m13 | stage9_reference | ent_m1 |  | many |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m13 | eref_m13 | m1 | ent_m1 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m14 | stand | stand | stand |  | agent:m1->ent_m1 |  |
| ce1 | m15 | speaks | speak | speak |  | agent:m6->ent_m6 |  |
| ce2 | m16 | listen | listen | listen |  | agent:m1->eref_m13 |  |
| ce3 | m17 | positioned | position | position |  | agent:m6->ent_m6 |  |
| ce4 | m18 | reads | read | read |  | agent:m11->ent_m11; patient:m0->None |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m1 | ent_m1 | medium | e4 | nsubj -> stand |  |  |
| ce1 | speak | agent | m6 | ent_m6 | medium | e5 | nsubj -> speaks |  |  |
| ce2 | listen | agent | m1 | eref_m13 | medium | e6 | nsubj -> listen; resolved others -> men |  |  |
| ce3 | position | agent | m6 | ent_m6 | medium | e7 | inherited agent advcl -> speaks |  |  |
| ce4 | read | agent | m11 | ent_m11 | medium | e8 | nsubj -> reads |  |  |
| ce4 | read | patient | m0 |  | medium | e9 | dobj -> reads |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m3 | ent_m1 | ent_m3 | in | high | e10 | False | False |  |  |
| cr1 | m1 | m4 | ent_m1 | ent_m4 | at | medium | e11 | False | False |  |  |
| cr2 | m1 | m5 | ent_m1 | ent_m5 | with | high | e12 | False | False |  |  |
| cr3 | m6 | m8 | ent_m6 | ent_m8 | near | high | e13 | False | False |  |  |
| cr4 | m6 | m9 | ent_m6 | ent_m9 | near | high | e14 | False | False |  |  |
| cr5 | m11 | m12 | ent_m11 | ent_m12 | on | high | e15 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 77

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `376ebd462683c1f3eb28ed9be54e2482e19ec9b94cfd32c1a5173b08d722d814`
**parse_path:** `sentence`

> Many white angel figurines are displayed closely together on a dark surface. One angel in the foreground has gold trim around its head and is lying down with wings spread. Some have small tags attached, suggesting they are for sale.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | figurines | figurine | noun_chunk_root | chunk0 | 3 | high |
| m1 | quantity | Many | many | approximate_quantity | chunk0 | 0 | medium |
| m2 | attribute | white | white | color_attribute | chunk0 | 1 | high |
| m3 | attribute | angel | angel | compound_modifier | chunk0 | 2 | medium |
| m4 | context | surface | surface | spatial_region | chunk1 | 11 | medium |
| m5 | object | angel | angel | noun_chunk_root | chunk2 | 14 | high |
| m6 | quantity | One | one | exact_quantity | chunk2 | 13 | high |
| m7 | context | foreground | foreground | scene_context | chunk3 | 17 | high |
| m8 | object | trim | trim | noun_chunk_root | chunk4 | 20 | high |
| m9 | attribute | gold | gold | color_attribute | chunk4 | 19 | high |
| m10 | object | head | head | noun_chunk_root | chunk5 | 23 | high |
| m11 | object | wings | wing | noun_chunk_root | chunk6 | 29 | high |
| m12 | quantity | Some | some | indefinite_quantity | chunk7 | 32 | medium |
| m13 | object | tags | tag | noun_chunk_root | chunk8 | 35 | high |
| m14 | attribute | small | small | size_attribute | chunk8 | 34 | high |
| m15 | object | sale | sale | noun_chunk_root | chunk10 | 42 | high |
| m16 | action | displayed | display | verb_predicate | doc | 5 | high |
| m17 | action | has | have | verb_predicate | doc | 18 | high |
| m18 | action | lying | lie | verb_predicate | doc | 26 | high |
| m19 | action | spread | spread | verb_predicate | doc | 30 | high |
| m20 | action | have | have | verb_predicate | doc | 33 | high |
| m21 | action | attached | attach | verb_predicate | doc | 36 | high |
| m22 | action | suggesting | suggest | verb_predicate | doc | 38 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | medium | chunk0 quantity -> figurines |
| e1 | has_attribute | m0 | m2 | high | chunk0 amod -> figurines |
| e2 | has_attribute | m0 | m3 | medium | chunk0 compound -> figurines |
| e3 | has_quantity | m5 | m6 | high | chunk2 quantity -> angel |
| e4 | has_context | scene | m7 | high | scene_context token foreground |
| e5 | has_attribute | m8 | m9 | high | chunk4 compound -> trim |
| e6 | has_attribute | m13 | m14 | high | chunk8 amod -> tags |
| e7 | agent | m16 | m0 | medium | nsubjpass -> displayed |
| e8 | agent | m17 | m5 | medium | nsubj -> has |
| e9 | patient | m17 | m8 | medium | dobj -> has |
| e10 | agent | m18 | m5 | medium | inherited agent conj -> has |
| e11 | agent | m19 | m11 | medium | nsubj -> spread |
| e12 | agent | m21 | m13 | medium | nsubj -> attached |
| e13 | relation | m0 | m4 | high | on |
| e14 | relation | m5 | m7 | high | in |
| e15 | relation | m5 | m10 | high | around |
| e16 | relation | m11 | m15 | medium | for |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | figurine | figurines | object | m0 | raw_mention |  |  |  |
| ent_m4 | context | surface | surface | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | angel | angel | object | m5 | raw_mention |  |  |  |
| ent_m7 | context | foreground | foreground | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | trim | trim | object | m8 | raw_mention |  |  |  |
| ent_m10 | object | head | head | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | wing | wings | object | m11 | raw_mention |  |  |  |
| ent_m13 | object | tag | tags | object | m13 | raw_mention |  |  |  |
| ent_m15 | object | sale | sale | object | m15 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | displayed | display | display |  | theme:m0->ent_m0 |  |
| ce1 | m17 | has | have | have |  | agent:m5->ent_m5; patient:m8->ent_m8 |  |
| ce2 | m18 | lying | lie | lie |  | agent:m5->ent_m5 |  |
| ce3 | m19 | spread | spread | spread |  | agent:m11->ent_m11 |  |
| ce4 | m20 | have | have | have |  |  |  |
| ce5 | m21 | attached | attach | attach |  | agent:m13->ent_m13 |  |
| ce6 | m22 | suggesting | suggest | suggest |  |  |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | display | theme | m0 | ent_m0 | medium | e7 | nsubjpass -> displayed |  |  |
| ce1 | have | agent | m5 | ent_m5 | medium | e8 | nsubj -> has |  |  |
| ce1 | have | patient | m8 | ent_m8 | medium | e9 | dobj -> has |  |  |
| ce2 | lie | agent | m5 | ent_m5 | medium | e10 | inherited agent conj -> has |  |  |
| ce3 | spread | agent | m11 | ent_m11 | medium | e11 | nsubj -> spread |  |  |
| ce5 | attach | agent | m13 | ent_m13 | medium | e12 | nsubj -> attached |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | on | high | e13 | False | False |  |  |
| cr1 | m5 | m7 | ent_m5 | ent_m7 | in | high | e14 | False | False |  |  |
| cr2 | m5 | m10 | ent_m5 | ent_m10 | around | high | e15 | False | False |  |  |
| cr3 | m11 | m15 | ent_m11 | ent_m15 | for | medium | e16 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m16 | e7 | m0 |  |  | {"action_mention_id": "m16", "kind": "passive_subject_to_theme", "raw_edge_id": "e7", "target": "m0"} |

## 78

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `38edf47d709d02a968cba65d1dfca5a24d612e5654f458d0287c380bc18a2014`
**parse_path:** `sentence`

> A narrow pathway leads through an arched entrance to a building at night. Several glowing spherical lights line the path, and two people are visible walking inside the archway. Snow covers the ground on either side of the walkway.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | pathway | pathway | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | narrow | narrow | size_attribute | chunk0 | 1 | high |
| m2 | object | entrance | entrance | noun_chunk_root | chunk1 | 7 | high |
| m3 | attribute | arched | arched | visual_attribute | chunk1 | 6 | medium |
| m4 | object | building | building | noun_chunk_root | chunk2 | 10 | high |
| m5 | context | night | night | scene_context | chunk3 | 12 | medium |
| m6 | object | lights | light | noun_chunk_root | chunk4 | 17 | high |
| m7 | quantity | Several | several | approximate_quantity | chunk4 | 14 | medium |
| m8 | attribute | glowing | glow | state_attribute | chunk4 | 15 | medium |
| m9 | attribute | spherical | spherical | modifier_attribute | chunk4 | 16 | medium |
| m10 | object | path | path | noun_chunk_root | chunk5 | 20 | high |
| m11 | object | people | people | noun_chunk_root | chunk6 | 24 | high |
| m12 | quantity | two | two | exact_quantity | chunk6 | 23 | high |
| m13 | object | archway | archway | noun_chunk_root | chunk7 | 30 | high |
| m14 | object | Snow | snow | noun_chunk_root | chunk8 | 32 | high |
| m15 | object | ground | ground | noun_chunk_root | chunk9 | 35 | high |
| m16 | context | side | side | spatial_region | chunk10 | 38 | medium |
| m17 | object | walkway | walkway | noun_chunk_root | chunk11 | 41 | high |
| m18 | action | leads | lead | verb_predicate | doc | 3 | high |
| m19 | action | line | line | verb_predicate | doc | 18 | high |
| m20 | action | walking | walk | verb_predicate | doc | 27 | high |
| m21 | action | covers | cover | verb_predicate | doc | 33 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> pathway |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> entrance |
| e2 | has_context | scene | m5 | medium | scene_context token night |
| e3 | has_quantity | m6 | m7 | medium | chunk4 quantity -> lights |
| e4 | has_attribute | m6 | m8 | medium | chunk4 amod -> lights |
| e5 | has_attribute | m6 | m9 | medium | chunk4 amod -> lights |
| e6 | has_quantity | m11 | m12 | high | chunk6 quantity -> people |
| e7 | agent | m18 | m0 | medium | nsubj -> leads |
| e8 | agent | m19 | m6 | medium | nsubj -> line |
| e9 | patient | m19 | m10 | medium | dobj -> line |
| e10 | agent | m21 | m14 | medium | nsubj -> covers |
| e11 | patient | m21 | m15 | medium | dobj -> covers |
| e12 | relation | m0 | m2 | medium | through |
| e13 | relation | m2 | m4 | medium | to |
| e14 | relation | m0 | m5 | medium | at |
| e15 | relation | m14 | m16 | high | on |
| e16 | relation | m16 | m17 | medium | of |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | pathway | pathway | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | entrance | entrance | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | building | building | object | m4 | raw_mention |  |  |  |
| ent_m5 | context | night | night | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | light | lights | object | m6 | raw_mention |  |  |  |
| ent_m10 | object | path | path | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | people | people | person | m11 | raw_mention |  |  |  |
| ent_m13 | object | archway | archway | object | m13 | raw_mention |  |  |  |
| ent_m14 | object | snow | Snow | object | m14 | raw_mention |  |  |  |
| ent_m15 | object | ground | ground | object | m15 | raw_mention |  |  |  |
| ent_m16 | context | side | side | object | m16 | raw_mention |  |  |  |
| ent_m17 | object | walkway | walkway | object | m17 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | leads | lead | lead |  | agent:m0->ent_m0 |  |
| ce1 | m19 | line | line | line |  | agent:m6->ent_m6; patient:m10->ent_m10 |  |
| ce2 | m20 | walking | walk | walk |  |  |  |
| ce3 | m21 | covers | cover | cover |  | agent:m14->ent_m14; patient:m15->ent_m15 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | lead | agent | m0 | ent_m0 | medium | e7 | nsubj -> leads |  |  |
| ce1 | line | agent | m6 | ent_m6 | medium | e8 | nsubj -> line |  |  |
| ce1 | line | patient | m10 | ent_m10 | medium | e9 | dobj -> line |  |  |
| ce3 | cover | agent | m14 | ent_m14 | medium | e10 | nsubj -> covers |  |  |
| ce3 | cover | patient | m15 | ent_m15 | medium | e11 | dobj -> covers |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | through | medium | e12 | False | False |  |  |
| cr1 | m2 | m4 | ent_m2 | ent_m4 | to | medium | e13 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | at | medium | e14 | False | False |  |  |
| cr3 | m14 | m16 | ent_m14 | ent_m16 | on | high | e15 | False | False |  |  |
| cr4 | m16 | m17 | ent_m16 | ent_m17 | of | medium | e16 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 79

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `3c5d43d61ed3ed53aa6b4588d4819a066946baf99be8b7d2bf7da9521a0c0414`
**parse_path:** `sentence`

> A person with white hair holds a tangled red rope in front of their face.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | hair | hair | noun_chunk_root | chunk1 | 4 | high |
| m2 | attribute | white | white | color_attribute | chunk1 | 3 | high |
| m3 | object | rope | rope | noun_chunk_root | chunk2 | 9 | high |
| m4 | attribute | tangled | tangle | state_attribute | chunk2 | 7 | medium |
| m5 | attribute | red | red | color_attribute | chunk2 | 8 | high |
| m6 | object | face | face | noun_chunk_root | chunk4 | 14 | high |
| m7 | action | holds | hold | verb_predicate | doc | 5 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> hair |
| e1 | has_attribute | m3 | m4 | medium | chunk2 amod -> rope |
| e2 | has_attribute | m3 | m5 | high | chunk2 amod -> rope |
| e3 | agent | m7 | m0 | medium | nsubj -> holds |
| e4 | patient | m7 | m3 | medium | dobj -> holds |
| e5 | relation | m0 | m1 | high | with |
| e6 | relation | m0 | m6 | high | in_front_of |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | hair | hair | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | rope | rope | object | m3 | raw_mention |  |  |  |
| ent_m6 | object | face | face | object | m6 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | holds | hold | hold |  | agent:m0->ent_m0; patient:m3->ent_m3 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | hold | agent | m0 | ent_m0 | medium | e3 | nsubj -> holds |  |  |
| ce0 | hold | patient | m3 | ent_m3 | medium | e4 | dobj -> holds |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | high | e5 | False | False |  |  |
| cr1 | m0 | m6 | ent_m3 | ent_m6 | in_front_of | high | e6 | False | False | pp_source_disambiguation | patient_body_part_anchor |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| pp_source_disambiguated | m7 | e6 |  | ent_m6 | patient_body_part_anchor | {"action_mention_id": "m7", "canonical_action": "hold", "canonical_source": "ent_m3", "canonical_target": "ent_m6", "confidence": "high", "kind": "pp_source_disambiguated", "previous_canonical_source": "ent_m0", "raw_edge_id": "e6", "raw_source": "m0", "raw_target": "m6", "reason": "patient_body_part_anchor", "relation": "in_front_of"} |

## 80

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `3c89dbf4ddc032df960c22d5b36ad91d9d785b52c535a524129808269fe56014`
**parse_path:** `sentence`

> Two hockey players skate on the ice, one in green and one in blue, while a referee watches nearby.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hockey players | hockey_player | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Two | two | exact_quantity | chunk0 | 0 | high |
| m2 | object | ice | ice | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | green | green | color_attribute | chunk2 | 9 | high |
| m4 | object | referee | referee | noun_chunk_root | chunk3 | 17 | high |
| m5 | reference | one | one | singular_substitute | nominal_reference | 7 | high |
| m6 | reference | one | one | singular_substitute | nominal_reference | 11 | high |
| m7 | action | skate | skate | verb_predicate | doc | 2 | high |
| m8 | action | watches | watch | verb_predicate | doc | 18 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> hockey players |
| e1 | refers_to | m5 | m0 | high | singular_substitute one -> hockey players; score=103 |
| e2 | refers_to | m6 | m0 | high | singular_substitute one -> hockey players; score=96 |
| e3 | agent | m7 | m0 | medium | nsubj -> skate |
| e4 | agent | m8 | m4 | medium | nsubj -> watches |
| e5 | relation | m0 | m2 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hockey_player | hockey players | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | ice | ice | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | referee | referee | person | m4 | raw_mention |  |  |  |
| eref_m5 | instance | hockey_player | one | object | m5 | stage9_reference | ent_m0 |  | 1 |
| eref_m6 | instance | hockey_player | one | object | m6 | stage9_reference | ent_m0 |  | 1 |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m5 | eref_m5 | m0 | ent_m0 | high |  |
| refers_to | m6 | eref_m6 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | skate | skate | skate |  | agent:m0->ent_m0 |  |
| ce1 | m8 | watches | watch | watch |  | agent:m4->ent_m4 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | skate | agent | m0 | ent_m0 | medium | e3 | nsubj -> skate |  |  |
| ce1 | watch | agent | m4 | ent_m4 | medium | e4 | nsubj -> watches |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | high | e5 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 81

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `3ce6ad26275a45c220438a773a16b0b3cafb709c25f367f6bc3f2bf74a0fa414`
**parse_path:** `sentence`

> A person with orange hair and tattoos wears a light green shirt, raising one arm against a dark background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | hair | hair | noun_chunk_root | chunk1 | 4 | high |
| m2 | attribute | orange | orange | color_attribute | chunk1 | 3 | high |
| m3 | object | tattoos | tattoo | noun_chunk_root | chunk2 | 6 | high |
| m4 | object | shirt | shirt | noun_chunk_root | chunk3 | 11 | high |
| m5 | attribute | light | light | visual_attribute | chunk3 | 9 | medium |
| m6 | attribute | green | green | color_attribute | chunk3 | 10 | high |
| m7 | object | arm | arm | noun_chunk_root | chunk4 | 15 | high |
| m8 | quantity | one | one | exact_quantity | chunk4 | 14 | high |
| m9 | context | background | background | scene_context | chunk5 | 19 | high |
| m10 | attribute | dark | dark | visual_attribute | chunk5 | 18 | medium |
| m11 | action | wears | wear | verb_predicate | doc | 7 | high |
| m12 | action | raising | raise | verb_predicate | doc | 13 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> hair |
| e1 | has_attribute | m4 | m5 | medium | chunk3 amod -> shirt |
| e2 | has_attribute | m4 | m6 | high | chunk3 amod -> shirt |
| e3 | has_quantity | m7 | m8 | high | chunk4 quantity -> arm |
| e4 | has_context | scene | m9 | high | scene_context token background |
| e5 | has_attribute | m9 | m10 | medium | chunk5 amod -> background |
| e6 | agent | m11 | m0 | medium | nsubj -> wears |
| e7 | patient | m11 | m4 | medium | dobj -> wears |
| e8 | agent | m12 | m0 | medium | inherited agent advcl -> wears |
| e9 | patient | m12 | m7 | medium | dobj -> raising |
| e10 | relation | m0 | m1 | high | with |
| e11 | relation | m0 | m3 | high | with |
| e12 | relation | m0 | m9 | high | against |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | hair | hair | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | tattoo | tattoos | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | shirt | shirt | clothing | m4 | raw_mention |  |  |  |
| ent_m7 | object | arm | arm | object | m7 | raw_mention |  |  |  |
| ent_m9 | context | background | background | object | m9 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m11 | wears | wear | wear |  | agent:m0->ent_m0; patient:m4->ent_m4 |  |
| ce1 | m12 | raising | raise | raise |  | agent:m0->ent_m0; patient:m7->ent_m7 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | wear | agent | m0 | ent_m0 | medium | e6 | nsubj -> wears |  |  |
| ce0 | wear | patient | m4 | ent_m4 | medium | e7 | dobj -> wears |  |  |
| ce1 | raise | agent | m0 | ent_m0 | medium | e8 | inherited agent advcl -> wears |  |  |
| ce1 | raise | patient | m7 | ent_m7 | medium | e9 | dobj -> raising |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | high | e10 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | with | high | e11 | False | False |  |  |
| cr2 | m0 | m9 | ent_m0 | ent_m9 | against | high | e12 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 82

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `3e2fb02a7420ac1fa49156d7cb913bd6b855d9bdbbb933336bd093e91e7f4414`
**parse_path:** `sentence`

> Soldiers wade through water in a landing craft, heading toward the Lincoln Memorial. The scene is set on a sunny day with trees lining the path and the monument visible in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | Soldiers | soldier | noun_chunk_root | chunk0 | 0 | high |
| m1 | object | water | water | noun_chunk_root | chunk1 | 3 | high |
| m2 | object | craft | craft | noun_chunk_root | chunk2 | 7 | high |
| m3 | attribute | landing | landing | compound_modifier | chunk2 | 6 | medium |
| m4 | object | Memorial | memorial | noun_chunk_root | chunk3 | 13 | high |
| m5 | attribute | Lincoln | lincoln | compound_modifier | chunk3 | 12 | medium |
| m6 | object | scene | scene | noun_chunk_root | chunk4 | 16 | high |
| m7 | context | day | day | scene_context | chunk5 | 22 | medium |
| m8 | attribute | sunny | sunny | modifier_attribute | chunk5 | 21 | medium |
| m9 | object | trees | tree | noun_chunk_root | chunk6 | 24 | high |
| m10 | object | path | path | noun_chunk_root | chunk7 | 27 | high |
| m11 | object | monument | monument | noun_chunk_root | chunk8 | 30 | high |
| m12 | context | background | background | scene_context | chunk9 | 34 | high |
| m13 | action | wade | wade | verb_predicate | doc | 1 | high |
| m14 | action | heading | head | verb_predicate | doc | 9 | high |
| m15 | action | set | set | verb_predicate | doc | 18 | high |
| m16 | action | lining | line | verb_predicate | doc | 25 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | medium | chunk2 compound -> craft |
| e1 | has_attribute | m4 | m5 | medium | chunk3 compound -> Memorial |
| e2 | has_context | scene | m7 | medium | scene_context token day |
| e3 | has_attribute | m7 | m8 | medium | chunk5 amod -> day |
| e4 | has_context | scene | m12 | high | scene_context token background |
| e5 | agent | m13 | m0 | medium | nsubj -> wade |
| e6 | agent | m14 | m0 | medium | inherited agent advcl -> wade |
| e7 | agent | m15 | m6 | medium | nsubjpass -> set |
| e8 | agent | m16 | m9 | medium | nsubj -> lining |
| e9 | patient | m16 | m10 | medium | dobj -> lining |
| e10 | relation | m0 | m1 | medium | through |
| e11 | relation | m0 | m2 | high | in |
| e12 | relation | m0 | m4 | medium | toward |
| e13 | relation | m6 | m7 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | soldier | Soldiers | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | water | water | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | craft | craft | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | memorial | Memorial | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | scene | scene | object | m6 | raw_mention |  |  |  |
| ent_m7 | context | day | day | object | m7 | raw_mention |  |  |  |
| ent_m9 | object | tree | trees | object | m9 | raw_mention |  |  |  |
| ent_m10 | object | path | path | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | monument | monument | object | m11 | raw_mention |  |  |  |
| ent_m12 | context | background | background | object | m12 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m13 | wade | wade | wade |  | agent:m0->ent_m0 |  |
| ce1 | m14 | heading | head | head |  | agent:m0->ent_m0 |  |
| ce2 | m15 | set | set | set |  | theme:m6->ent_m6 |  |
| ce3 | m16 | lining | line | line |  | agent:m9->ent_m9; patient:m10->ent_m10 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | wade | agent | m0 | ent_m0 | medium | e5 | nsubj -> wade |  |  |
| ce1 | head | agent | m0 | ent_m0 | medium | e6 | inherited agent advcl -> wade |  |  |
| ce2 | set | theme | m6 | ent_m6 | medium | e7 | nsubjpass -> set |  |  |
| ce3 | line | agent | m9 | ent_m9 | medium | e8 | nsubj -> lining |  |  |
| ce3 | line | patient | m10 | ent_m10 | medium | e9 | dobj -> lining |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | through | medium | e10 | False | False |  |  |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | in | high | e11 | False | False |  |  |
| cr2 | m0 | m4 | ent_m0 | ent_m4 | toward | medium | e12 | False | False |  |  |
| cr3 | m6 | m7 | ent_m6 | ent_m7 | on | high | e13 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m15 | e7 | m6 |  |  | {"action_mention_id": "m15", "kind": "passive_subject_to_theme", "raw_edge_id": "e7", "target": "m6"} |

## 83

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `3f2627a92b621bc5323f53361344ffe6603365aca0a7e45511dafc143b4e8414`
**parse_path:** `tag_list`

> buddha statue, mountain, green sky, bare tree, stone base

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | statue | statue | segment_head | t0 | 1 | high |
| m1 | attribute | buddha | buddha | attribute | t0 | 0 | high |
| m2 | object | mountain | mountain | segment_head | t1 | 0 | high |
| m3 | object | sky | sky | segment_head | t2 | 1 | high |
| m4 | attribute | green | green | attribute | t2 | 0 | high |
| m5 | object | tree | tree | segment_head | t3 | 1 | high |
| m6 | attribute | bare | bare | attribute | t3 | 0 | high |
| m7 | object | base | base | segment_head | t4 | 1 | high |
| m8 | attribute | stone | stone | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> statue |
| e1 | has_attribute | m3 | m4 | high | t2 internal amod -> sky |
| e2 | has_attribute | m5 | m6 | high | t3 internal compound -> tree |
| e3 | has_attribute | m7 | m8 | high | t4 internal compound -> base |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | statue | statue | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | mountain | mountain | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | sky | sky | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | tree | tree | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | base | base | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 84

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `3fcf2cc6b872a60103a0fa9cd041a37e58747dd4be0d298fb54cfac259f59c14`
**parse_path:** `tag_list`

> four women, beach, island, turquoise water

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | women | woman | segment_head | t0 | 1 | high |
| m1 | quantity | four | four | exact_quantity | t0 | 0 | high |
| m2 | object | beach | beach | segment_head | t1 | 0 | high |
| m3 | object | island | island | segment_head | t2 | 0 | high |
| m4 | object | water | water | segment_head | t3 | 1 | high |
| m5 | attribute | turquoise | turquoise | attribute | t3 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | t0 internal nummod -> women |
| e1 | has_attribute | m4 | m5 | high | t3 internal compound -> water |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | women | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | beach | beach | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | island | island | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | water | water | object | m4 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 85

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `4161c3fb3b79a5bec82d938c290ab6901f1716801e59b3578499ba911c4ea414`
**parse_path:** `tag_list`

> ancient pyramid, stone steps, green grass, tree shadows, jungle setting

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | pyramid | pyramid | segment_head | t0 | 1 | high |
| m1 | attribute | ancient | ancient | attribute | t0 | 0 | high |
| m2 | object | steps | step | segment_head | t1 | 1 | high |
| m3 | attribute | stone | stone | attribute | t1 | 0 | high |
| m4 | object | grass | grass | segment_head | t2 | 1 | high |
| m5 | attribute | green | green | attribute | t2 | 0 | high |
| m6 | object | shadows | shadow | segment_head | t3 | 1 | high |
| m7 | attribute | tree | tree | attribute | t3 | 0 | high |
| m8 | context | setting | setting | scene_context | t4 | 1 | high |
| m9 | attribute | jungle | jungle | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> pyramid |
| e1 | has_attribute | m2 | m3 | high | t1 internal compound -> steps |
| e2 | has_attribute | m4 | m5 | high | t2 internal amod -> grass |
| e3 | has_attribute | m6 | m7 | high | t3 internal compound -> shadows |
| e4 | has_context | scene | m8 | high | t4 context tag |
| e5 | has_attribute | m8 | m9 | high | t4 internal compound -> setting |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | pyramid | pyramid | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | step | steps | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | grass | grass | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | shadow | shadows | object | m6 | raw_mention |  |  |  |
| ent_m8 | context | setting | setting | object | m8 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 86

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `41cf3165de139e05001208a95820ee600a8211e254de5226434227a9370a2c14`
**parse_path:** `sentence`

> Two cricket players in white uniforms play on a grass field. One bats, the other runs toward the wicket.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | players | player | noun_chunk_root | chunk0 | 2 | high |
| m1 | quantity | Two | two | exact_quantity | chunk0 | 0 | high |
| m2 | attribute | cricket | cricket | compound_modifier | chunk0 | 1 | medium |
| m3 | object | uniforms | uniform | noun_chunk_root | chunk1 | 5 | high |
| m4 | attribute | white | white | color_attribute | chunk1 | 4 | high |
| m5 | object | field | field | noun_chunk_root | chunk2 | 10 | high |
| m6 | attribute | grass | grass | compound_modifier | chunk2 | 9 | medium |
| m7 | object | wicket | wicket | noun_chunk_root | chunk3 | 20 | high |
| m8 | reference | other | other | contrastive_reference | nominal_reference | 16 | high |
| m9 | action | play | play | verb_predicate | doc | 6 | high |
| m10 | action | bats | bat | verb_predicate | doc | 13 | high |
| m11 | action | runs | run | verb_predicate | doc | 17 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> players |
| e1 | has_attribute | m0 | m2 | medium | chunk0 compound -> players |
| e2 | has_attribute | m3 | m4 | high | chunk1 amod -> uniforms |
| e3 | has_attribute | m5 | m6 | medium | chunk2 compound -> field |
| e4 | refers_to | m8 | m0 | high | contrastive_reference other -> players; score=118; margin=30 |
| e5 | agent | m9 | m0 | medium | nsubj -> play |
| e6 | agent | m10 | m0 | medium | inherited agent ccomp -> runs |
| e7 | agent | m11 | m0 | medium | nsubj -> runs; resolved other -> players |
| e8 | relation | m0 | m3 | high | in |
| e9 | relation | m0 | m5 | high | on |
| e10 | relation | m0 | m7 | medium | toward |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | player | players | person | m0 | raw_mention |  |  |  |
| ent_m3 | object | uniform | uniforms | clothing | m3 | raw_mention |  |  |  |
| ent_m5 | object | field | field | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | wicket | wicket | object | m7 | raw_mention |  |  |  |
| eref_m8 | contrastive_instance | player | other | person | m8 | stage9_reference | ent_m0 |  | 1 |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m8 | eref_m8 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | play | play | play |  | agent:m0->ent_m0 |  |
| ce1 | m10 | bats | bat | bat |  | agent:m0->ent_m0 |  |
| ce2 | m11 | runs | run | run |  | agent:m0->eref_m8 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | play | agent | m0 | ent_m0 | medium | e5 | nsubj -> play |  |  |
| ce1 | bat | agent | m0 | ent_m0 | medium | e6 | inherited agent ccomp -> runs |  |  |
| ce2 | run | agent | m0 | eref_m8 | medium | e7 | nsubj -> runs; resolved other -> players |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | in | high | e8 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | high | e9 | False | False |  |  |
| cr2 | m0 | m7 | eref_m8 | ent_m7 | toward | medium | e10 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 87

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `43f23c61603ba21988593b02f24d0b27d1e8b7717ff3e41efe599cb785826c14`
**parse_path:** `sentence`

> A large brick building with a sloped roof stands at the corner of a paved street. Trees and a low wall are visible to the left, while a few distant structures appear in the background under an overcast sky.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | noun_chunk_root | chunk0 | 3 | high |
| m1 | attribute | large | large | size_attribute | chunk0 | 1 | high |
| m2 | attribute | brick | brick | material_attribute | chunk0 | 2 | high |
| m3 | object | roof | roof | noun_chunk_root | chunk1 | 7 | high |
| m4 | attribute | sloped | sloped | modifier_attribute | chunk1 | 6 | medium |
| m5 | object | street | street | noun_chunk_root | chunk3 | 15 | high |
| m6 | attribute | paved | paved | visual_attribute | chunk3 | 14 | medium |
| m7 | object | Trees | tree | noun_chunk_root | chunk4 | 17 | high |
| m8 | object | wall | wall | noun_chunk_root | chunk5 | 21 | high |
| m9 | attribute | low | low | modifier_attribute | chunk5 | 20 | medium |
| m10 | object | structures | structure | noun_chunk_root | chunk6 | 32 | high |
| m11 | quantity | few | few | approximate_quantity | chunk6 | 30 | medium |
| m12 | attribute | distant | distant | modifier_attribute | chunk6 | 31 | medium |
| m13 | context | background | background | scene_context | chunk7 | 36 | high |
| m14 | object | sky | sky | noun_chunk_root | chunk8 | 40 | high |
| m15 | attribute | overcast | overcast | modifier_attribute | chunk8 | 39 | medium |
| m16 | action | stands | stand | verb_predicate | doc | 8 | high |
| m17 | action | appear | appear | verb_predicate | doc | 33 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> building |
| e1 | has_attribute | m0 | m2 | high | chunk0 compound -> building |
| e2 | has_attribute | m3 | m4 | medium | chunk1 amod -> roof |
| e3 | has_attribute | m5 | m6 | medium | chunk3 amod -> street |
| e4 | has_attribute | m8 | m9 | medium | chunk5 amod -> wall |
| e5 | has_quantity | m10 | m11 | medium | chunk6 quantity -> structures |
| e6 | has_attribute | m10 | m12 | medium | chunk6 amod -> structures |
| e7 | has_context | scene | m13 | high | scene_context token background |
| e8 | has_attribute | m14 | m15 | medium | chunk8 amod -> sky |
| e9 | agent | m16 | m0 | medium | nsubj -> stands |
| e10 | agent | m17 | m10 | medium | nsubj -> appear |
| e11 | relation | m0 | m3 | high | with |
| e12 | relation | m0 | m5 | high | corner_of |
| e13 | relation | m10 | m13 | high | in |
| e14 | relation | m10 | m14 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | building | object | m0 | raw_mention |  |  |  |
| ent_m3 | object | roof | roof | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | street | street | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | tree | Trees | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | wall | wall | object | m8 | raw_mention |  |  |  |
| ent_m10 | object | structure | structures | object | m10 | raw_mention |  |  |  |
| ent_m13 | context | background | background | object | m13 | raw_mention |  |  |  |
| ent_m14 | object | sky | sky | object | m14 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | stands | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m17 | appear | appear | appear |  | agent:m10->ent_m10 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e9 | nsubj -> stands |  |  |
| ce1 | appear | agent | m10 | ent_m10 | medium | e10 | nsubj -> appear |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | with | high | e11 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | corner_of | high | e12 | False | False |  |  |
| cr2 | m10 | m13 | ent_m10 | ent_m13 | in | high | e13 | False | False |  |  |
| cr3 | m10 | m14 | ent_m10 | ent_m14 | under | high | e14 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 88

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `45428ee1d9a35ad63241938ce5e4ffc58c9443946d4676f4c388c189a14c7814`
**parse_path:** `tag_list`

> top hats, crowd, men, seated, formal attire

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | top hats | top_hat | segment_head | t0 | 0 | high |
| m1 | object | crowd | crowd | segment_head | t1 | 0 | high |
| m2 | object | men | men | segment_head | t2 | 0 | high |
| m3 | attribute | seated | seat | floating_attribute | t3 | 0 | medium |
| m4 | object | attire | attire | segment_head | t4 | 1 | high |
| m5 | attribute | formal | formal | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | candidate_has_attribute | m2 | m3 | low | t3 adjacent floating attribute |
| e1 | has_attribute | m4 | m5 | high | t4 internal amod -> attire |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | top_hat | top hats | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | crowd | crowd | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | men | men | person | m2 | raw_mention |  |  |  |
| ent_m4 | object | attire | attire | object | m4 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonicalization Notes
_none_

## 89

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `466babec43683bc6662ef5a0c610bc0e5f693f41da37b46f74f7aa0ca3b7d814`
**parse_path:** `sentence`

> Several sea lions rest on a wooden dock near the water. Some are lying down, while others sit or stand, with the calm blue water visible behind them. A few sea lions are on a platform further back, near a wooden post.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | sea lions | sea_lion | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | dock | dock | noun_chunk_root | chunk1 | 6 | high |
| m2 | attribute | wooden | wooden | material_attribute | chunk1 | 5 | high |
| m3 | object | water | water | noun_chunk_root | chunk2 | 9 | high |
| m4 | quantity | Some | some | indefinite_quantity | chunk3 | 11 | medium |
| m5 | object | water | water | noun_chunk_root | chunk5 | 26 | high |
| m6 | attribute | calm | calm | modifier_attribute | chunk5 | 24 | medium |
| m7 | attribute | blue | blue | color_attribute | chunk5 | 25 | high |
| m8 | object | sea lions | sea_lion | noun_chunk_root | chunk7 | 33 | high |
| m9 | object | platform | platform | noun_chunk_root | chunk8 | 37 | high |
| m10 | object | post | post | noun_chunk_root | chunk9 | 44 | high |
| m11 | attribute | wooden | wooden | material_attribute | chunk9 | 43 | high |
| m12 | action | rest | rest | verb_predicate | doc | 2 | high |
| m13 | action | lying | lie | verb_predicate | doc | 13 | high |
| m14 | particle | down | down | phrasal_particle | action_particle | 14 | medium |
| m15 | action | sit | sit | verb_predicate | doc | 18 | high |
| m16 | action | stand | stand | verb_predicate | doc | 20 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> dock |
| e1 | has_attribute | m5 | m6 | medium | chunk5 amod -> water |
| e2 | has_attribute | m5 | m7 | high | chunk5 amod -> water |
| e3 | has_attribute | m10 | m11 | high | chunk9 amod -> post |
| e4 | agent | m12 | m0 | medium | nsubj -> rest |
| e5 | has_particle | m13 | m14 | medium | prt -> lying |
| e6 | relation | m0 | m1 | high | on |
| e7 | relation | m0 | m3 | high | near |
| e8 | relation | m8 | m9 | high | on |
| e9 | relation | m9 | m10 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sea_lion | sea lions | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | dock | dock | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | water | water | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | water | water | object | m5 | raw_mention |  |  |  |
| ent_m8 | object | sea_lion | sea lions | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | platform | platform | object | m9 | raw_mention |  |  |  |
| ent_m10 | object | post | post | object | m10 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | rest | rest | rest |  | agent:m0->ent_m0 |  |
| ce1 | m13 | lying | lie | lie_down | down |  | phrasal_action:lie down |
| ce2 | m15 | sit | sit | sit |  |  |  |
| ce3 | m16 | stand | stand | stand |  |  |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | rest | agent | m0 | ent_m0 | medium | e4 | nsubj -> rest |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | on | high | e6 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | near | high | e7 | False | False |  |  |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | on | high | e8 | False | False |  |  |
| cr3 | m9 | m10 | ent_m9 | ent_m10 | near | high | e9 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| phrasal_action_canonicalized | m13 |  |  |  |  | {"action_mention_id": "m13", "canonical": "lie_down", "kind": "phrasal_action_canonicalized", "source": "visual_genome_relation_predicates", "term": "lie down"} |

## 90

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `47fc5c5143d58519323971343cf2e71769a9cfc2caf6516465d258a6d88bc014`
**parse_path:** `sentence`

> A man stands at a table, pointing to a screen showing video calls with several people. Others sit around the table in a modern room.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | table | table | noun_chunk_root | chunk1 | 5 | high |
| m2 | object | screen | screen | noun_chunk_root | chunk2 | 10 | high |
| m3 | object | calls | call | noun_chunk_root | chunk3 | 13 | high |
| m4 | attribute | video | video | compound_modifier | chunk3 | 12 | medium |
| m5 | object | people | people | noun_chunk_root | chunk4 | 16 | high |
| m6 | quantity | several | several | approximate_quantity | chunk4 | 15 | medium |
| m7 | object | table | table | noun_chunk_root | chunk6 | 22 | high |
| m8 | object | room | room | noun_chunk_root | chunk7 | 26 | high |
| m9 | attribute | modern | modern | modifier_attribute | chunk7 | 25 | medium |
| m10 | reference | Others | other | contrastive_reference | nominal_reference | 18 | high |
| m11 | action | stands | stand | verb_predicate | doc | 2 | high |
| m12 | action | pointing | point | verb_predicate | doc | 7 | high |
| m13 | action | showing | show | verb_predicate | doc | 11 | high |
| m14 | action | sit | sit | verb_predicate | doc | 19 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m3 | m4 | medium | chunk3 compound -> calls |
| e1 | has_quantity | m5 | m6 | medium | chunk4 quantity -> people |
| e2 | has_attribute | m8 | m9 | medium | chunk7 amod -> room |
| e3 | refers_to | m10 | m5 | high | contrastive_reference Others -> people; score=115 |
| e4 | agent | m11 | m0 | medium | nsubj -> stands |
| e5 | agent | m12 | m0 | medium | inherited agent advcl -> stands |
| e6 | agent | m13 | m2 | medium | inherited agent acl -> screen |
| e7 | patient | m13 | m3 | medium | dobj -> showing |
| e8 | agent | m14 | m5 | medium | nsubj -> sit; resolved Others -> people |
| e9 | relation | m0 | m1 | medium | at |
| e10 | relation | m0 | m2 | medium | to |
| e11 | relation | m3 | m5 | high | with |
| e12 | relation | m5 | m7 | high | around |
| e13 | relation | m5 | m8 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | table | table | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | screen | screen | device | m2 | raw_mention |  |  |  |
| ent_m3 | object | call | calls | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | people | people | person | m5 | raw_mention |  |  |  |
| ent_m7 | object | table | table | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | room | room | object | m8 | raw_mention |  |  |  |
| eref_m10 | complement_subset | people | Others | person | m10 | stage9_reference | ent_m5 |  | many |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m10 | eref_m10 | m5 | ent_m5 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m11 | stands | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m12 | pointing | point | point |  | agent:m0->ent_m0 |  |
| ce2 | m13 | showing | show | show |  | agent:m2->ent_m2; patient:m3->ent_m3 |  |
| ce3 | m14 | sit | sit | sit |  | agent:m5->eref_m10 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e4 | nsubj -> stands |  |  |
| ce1 | point | agent | m0 | ent_m0 | medium | e5 | inherited agent advcl -> stands |  |  |
| ce2 | show | agent | m2 | ent_m2 | medium | e6 | inherited agent acl -> screen |  |  |
| ce2 | show | patient | m3 | ent_m3 | medium | e7 | dobj -> showing |  |  |
| ce3 | sit | agent | m5 | eref_m10 | medium | e8 | nsubj -> sit; resolved Others -> people |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | at | medium | e9 | False | False |  |  |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | to | medium | e10 | False | False |  |  |
| cr2 | m3 | m5 | ent_m3 | ent_m5 | with | high | e11 | False | False |  |  |
| cr3 | m5 | m7 | ent_m5 | ent_m7 | around | high | e12 | False | False |  |  |
| cr4 | m5 | m8 | ent_m5 | ent_m8 | in | high | e13 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 91

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `482c9be0128cf7750aa70cd0831ac3ee03a6f39a18d1b8ab7347b2f724564c14`
**parse_path:** `sentence`

> An old airplane with a bicycle frame hangs from the ceiling in a large indoor space.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | airplane | airplane | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | old | old | visual_attribute | chunk0 | 1 | medium |
| m2 | object | frame | frame | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | bicycle | bicycle | compound_modifier | chunk1 | 5 | medium |
| m4 | object | ceiling | ceiling | noun_chunk_root | chunk2 | 10 | high |
| m5 | object | space | space | noun_chunk_root | chunk3 | 15 | high |
| m6 | attribute | large | large | size_attribute | chunk3 | 13 | high |
| m7 | attribute | indoor | indoor | modifier_attribute | chunk3 | 14 | medium |
| m8 | action | hangs | hang | verb_predicate | doc | 7 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> airplane |
| e1 | has_attribute | m2 | m3 | medium | chunk1 compound -> frame |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> space |
| e3 | has_attribute | m5 | m7 | medium | chunk3 amod -> space |
| e4 | agent | m8 | m0 | medium | nsubj -> hangs |
| e5 | relation | m0 | m2 | high | with |
| e6 | relation | m0 | m4 | medium | from |
| e7 | relation | m0 | m5 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | airplane | airplane | vehicle | m0 | raw_mention |  |  |  |
| ent_m2 | object | frame | frame | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | ceiling | ceiling | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | space | space | object | m5 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | hangs | hang | hang |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | hang | agent | m0 | ent_m0 | medium | e4 | nsubj -> hangs |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e5 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | from | medium | e6 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | in | high | e7 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 92

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `48c9d293a0e9e6816cfba07c73fa10b8733db96f953058d04db0edef64064414`
**parse_path:** `sentence`

> Several people sit at wooden tables outdoors, playing chess under trees. A young girl in a gray shirt is seated at a table with a chessboard in front of her, while others are focused on their games nearby. The setting is a sunny park-like area with buildings and greenery in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Several | several | approximate_quantity | chunk0 | 0 | medium |
| m2 | object | tables | table | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | wooden | wooden | material_attribute | chunk1 | 4 | high |
| m4 | object | chess | chess | noun_chunk_root | chunk2 | 9 | high |
| m5 | object | trees | tree | noun_chunk_root | chunk3 | 11 | high |
| m6 | object | girl | girl | noun_chunk_root | chunk4 | 15 | high |
| m7 | attribute | young | young | modifier_attribute | chunk4 | 14 | medium |
| m8 | object | shirt | shirt | noun_chunk_root | chunk5 | 19 | high |
| m9 | attribute | gray | gray | color_attribute | chunk5 | 18 | high |
| m10 | object | table | table | noun_chunk_root | chunk6 | 24 | high |
| m11 | object | chessboard | chessboard | noun_chunk_root | chunk7 | 27 | high |
| m12 | object | games | game | noun_chunk_root | chunk11 | 39 | high |
| m13 | context | setting | setting | scene_context | chunk12 | 43 | high |
| m14 | object | area | area | noun_chunk_root | chunk13 | 48 | high |
| m15 | attribute | sunny | sunny | modifier_attribute | chunk13 | 46 | medium |
| m16 | attribute | park-like | park-like | modifier_attribute | chunk13 | 47 | medium |
| m17 | object | buildings | building | noun_chunk_root | chunk14 | 50 | high |
| m18 | object | greenery | greenery | noun_chunk_root | chunk15 | 52 | high |
| m19 | context | background | background | scene_context | chunk16 | 55 | high |
| m20 | context | outdoors | outdoors | scene_context | doc | 6 | high |
| m21 | reference | others | other | contrastive_reference | nominal_reference | 34 | high |
| m22 | action | sit | sit | verb_predicate | doc | 2 | high |
| m23 | action | playing | play | verb_predicate | doc | 8 | high |
| m24 | action | seated | seat | verb_predicate | doc | 21 | high |
| m25 | action | focused | focus | verb_predicate | doc | 36 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | medium | chunk0 quantity -> people |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> tables |
| e2 | has_attribute | m6 | m7 | medium | chunk4 amod -> girl |
| e3 | has_attribute | m8 | m9 | high | chunk5 amod -> shirt |
| e4 | has_context | scene | m13 | high | scene_context token setting |
| e5 | has_attribute | m14 | m15 | medium | chunk13 amod -> area |
| e6 | has_attribute | m14 | m16 | medium | chunk13 amod -> area |
| e7 | has_context | scene | m19 | high | scene_context token background |
| e8 | has_context | scene | m20 | high | scene_context token outdoors |
| e9 | refers_to | m21 | m0 | high | contrastive_reference others -> people; score=100; margin=20 |
| e10 | agent | m22 | m0 | medium | nsubj -> sit |
| e11 | agent | m23 | m0 | medium | inherited agent advcl -> sit |
| e12 | patient | m23 | m4 | medium | dobj -> playing |
| e13 | agent | m24 | m6 | medium | nsubjpass -> seated |
| e14 | agent | m25 | m0 | medium | inherited agent acomp -> are |
| e15 | relation | m0 | m2 | medium | at |
| e16 | relation | m0 | m5 | high | under |
| e17 | relation | m6 | m8 | high | in |
| e18 | relation | m6 | m10 | medium | at |
| e19 | relation | m10 | m11 | high | with |
| e20 | relation | m11 | m6 | high | in_front_of |
| e21 | relation | m14 | m17 | high | with |
| e22 | relation | m14 | m18 | high | with |
| e23 | relation | m17 | m19 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | table | tables | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | chess | chess | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | tree | trees | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | girl | girl | person | m6 | raw_mention |  |  |  |
| ent_m8 | object | shirt | shirt | clothing | m8 | raw_mention |  |  |  |
| ent_m10 | object | table | table | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | chessboard | chessboard | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | game | games | object | m12 | raw_mention |  |  |  |
| ent_m13 | context | setting | setting | object | m13 | raw_mention |  |  |  |
| ent_m14 | object | area | area | object | m14 | raw_mention |  |  |  |
| ent_m17 | object | building | buildings | object | m17 | raw_mention |  |  |  |
| ent_m18 | object | greenery | greenery | object | m18 | raw_mention |  |  |  |
| ent_m19 | context | background | background | object | m19 | raw_mention |  |  |  |
| ent_m20 | context | outdoors | outdoors | object | m20 | raw_mention |  |  |  |
| eref_m21 | complement_subset | people | others | person | m21 | stage9_reference | ent_m0 |  | many |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m21 | eref_m21 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m22 | sit | sit | sit |  | agent:m0->ent_m0 |  |
| ce1 | m23 | playing | play | play |  | agent:m0->ent_m0; patient:m4->ent_m4 |  |
| ce2 | m24 | seated | seat | seat |  | theme:m6->ent_m6 |  |
| ce3 | m25 | focused | focus | focus |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m0 | ent_m0 | medium | e10 | nsubj -> sit |  |  |
| ce1 | play | agent | m0 | ent_m0 | medium | e11 | inherited agent advcl -> sit |  |  |
| ce1 | play | patient | m4 | ent_m4 | medium | e12 | dobj -> playing |  |  |
| ce2 | seat | theme | m6 | ent_m6 | medium | e13 | nsubjpass -> seated |  |  |
| ce3 | focus | agent | m0 | ent_m0 | medium | e14 | inherited agent acomp -> are |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | at | medium | e15 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | under | high | e16 | False | False |  |  |
| cr2 | m6 | m8 | ent_m6 | ent_m8 | in | high | e17 | False | False |  |  |
| cr3 | m6 | m10 | ent_m6 | ent_m10 | at | medium | e18 | False | False |  |  |
| cr4 | m10 | m11 | ent_m10 | ent_m11 | with | high | e19 | False | False |  |  |
| cr5 | m11 | m6 | ent_m11 | ent_m6 | in_front_of | high | e20 | False | False |  |  |
| cr6 | m14 | m17 | ent_m14 | ent_m17 | with | high | e21 | False | False |  |  |
| cr7 | m14 | m18 | ent_m14 | ent_m18 | with | high | e22 | False | False |  |  |
| cr8 | m17 | m19 | ent_m17 | ent_m19 | in | high | e23 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m24 | e13 | m6 |  |  | {"action_mention_id": "m24", "kind": "passive_subject_to_theme", "raw_edge_id": "e13", "target": "m6"} |

## 93

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `4bfd0342561c4cded12246ed215bdbe897f68be5c3f69a52dbfbc1b45cdc7414`
**parse_path:** `sentence`

> People sit at tables in a room, with one woman in bright yellow pants standing near a man in a plaid shirt.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | People | people | noun_chunk_root | chunk0 | 0 | high |
| m1 | object | tables | table | noun_chunk_root | chunk1 | 3 | high |
| m2 | object | room | room | noun_chunk_root | chunk2 | 6 | high |
| m3 | object | woman | woman | noun_chunk_root | chunk3 | 10 | high |
| m4 | quantity | one | one | exact_quantity | chunk3 | 9 | high |
| m5 | object | pants | pant | noun_chunk_root | chunk4 | 14 | high |
| m6 | attribute | bright | bright | visual_attribute | chunk4 | 12 | medium |
| m7 | attribute | yellow | yellow | color_attribute | chunk4 | 13 | high |
| m8 | object | man | man | noun_chunk_root | chunk5 | 18 | high |
| m9 | object | shirt | shirt | noun_chunk_root | chunk6 | 22 | high |
| m10 | attribute | plaid | plaid | modifier_attribute | chunk6 | 21 | medium |
| m11 | action | sit | sit | verb_predicate | doc | 1 | high |
| m12 | action | standing | stand | verb_predicate | doc | 15 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m3 | m4 | high | chunk3 quantity -> woman |
| e1 | has_attribute | m5 | m6 | medium | chunk4 amod -> pants |
| e2 | has_attribute | m5 | m7 | high | chunk4 amod -> pants |
| e3 | has_attribute | m9 | m10 | medium | chunk6 amod -> shirt |
| e4 | agent | m11 | m0 | medium | nsubj -> sit |
| e5 | agent | m12 | m3 | medium | nsubj -> standing |
| e6 | relation | m0 | m1 | medium | at |
| e7 | relation | m0 | m2 | high | in |
| e8 | relation | m3 | m5 | high | in |
| e9 | relation | m3 | m8 | high | near |
| e10 | relation | m8 | m9 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | People | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | table | tables | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | room | room | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | woman | woman | person | m3 | raw_mention |  |  |  |
| ent_m5 | object | pant | pants | object | m5 | raw_mention |  |  |  |
| ent_m8 | object | man | man | person | m8 | raw_mention |  |  |  |
| ent_m9 | object | shirt | shirt | clothing | m9 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m11 | sit | sit | sit |  | agent:m0->ent_m0 |  |
| ce1 | m12 | standing | stand | stand |  | agent:m3->ent_m3 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m0 | ent_m0 | medium | e4 | nsubj -> sit |  |  |
| ce1 | stand | agent | m3 | ent_m3 | medium | e5 | nsubj -> standing |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | at | medium | e6 | False | False |  |  |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | in | high | e7 | False | False |  |  |
| cr2 | m3 | m5 | ent_m3 | ent_m5 | in | high | e8 | False | False |  |  |
| cr3 | m3 | m8 | ent_m3 | ent_m8 | near | high | e9 | False | False |  |  |
| cr4 | m8 | m9 | ent_m8 | ent_m9 | in | high | e10 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 94

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `4c03ab0fe6b9ecbdf3f5eba512d6bab380a75a7b12f710780f3e67e2c1e38414`
**parse_path:** `sentence`

> Three runners compete on an indoor track, with one in an orange jersey and another in a gold and blue uniform.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | runners | runner | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Three | three | exact_quantity | chunk0 | 0 | high |
| m2 | object | track | track | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | indoor | indoor | modifier_attribute | chunk1 | 5 | medium |
| m4 | object | jersey | jersey | noun_chunk_root | chunk2 | 13 | high |
| m5 | attribute | orange | orange | color_attribute | chunk2 | 12 | high |
| m6 | object | uniform | uniform | noun_chunk_root | chunk4 | 21 | high |
| m7 | attribute | gold | gold | color_attribute | chunk4 | 18 | high |
| m8 | attribute | blue | blue | color_attribute | chunk4 | 20 | high |
| m9 | reference | one | one | singular_substitute | nominal_reference | 9 | high |
| m10 | reference | another | another | contrastive_reference | nominal_reference | 15 | high |
| m11 | action | compete | compete | verb_predicate | doc | 2 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> runners |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> track |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> jersey |
| e3 | has_attribute | m6 | m7 | high | chunk4 amod -> uniform |
| e4 | has_attribute | m6 | m8 | high | chunk4 conj -> uniform |
| e5 | refers_to | m9 | m0 | high | singular_substitute one -> runners; score=103 |
| e6 | refers_to | m10 | m0 | high | contrastive_reference another -> runners; score=102 |
| e7 | agent | m11 | m0 | medium | nsubj -> compete |
| e8 | relation | m0 | m2 | high | on |
| e9 | relation | m0 | m4 | high | in |
| e10 | relation | m0 | m6 | high | in |

### Skipped Raw Concept Edges
| type | source | target | confidence | reason | evidence |
| --- | --- | --- | --- | --- | --- |
| relation | m0 | m0 | high | self_edge_after_coref | with |
| relation | m0 | m0 | high | self_edge_after_coref | with |

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | runner | runners | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | track | track | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | jersey | jersey | clothing | m4 | raw_mention |  |  |  |
| ent_m6 | object | uniform | uniform | clothing | m6 | raw_mention |  |  |  |
| eref_m9 | instance | runner | one | person | m9 | stage9_reference | ent_m0 |  | 1 |
| eref_m10 | contrastive_instance | runner | another | person | m10 | stage9_reference | ent_m0 |  | 1 |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m9 | eref_m9 | m0 | ent_m0 | high |  |
| refers_to | m10 | eref_m10 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m11 | compete | compete | compete |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | compete | agent | m0 | ent_m0 | medium | e7 | nsubj -> compete |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | high | e8 | False | False |  |  |
| cr1 | m0 | m4 | eref_m9 | ent_m4 | in | high | e9 | False | False |  |  |
| cr2 | m0 | m6 | eref_m10 | ent_m6 | in | high | e10 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 95

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `4e942957441ee06442c3d3cfc0720fc33d15d3a18bb37504d895e759c98da014`
**parse_path:** `sentence`

> Two bronze military badges show a sunburst design with a crown and text. They are placed on a plain white surface.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | badges | badge | noun_chunk_root | chunk0 | 3 | high |
| m1 | quantity | Two | two | exact_quantity | chunk0 | 0 | high |
| m2 | attribute | military | military | modifier_attribute | chunk0 | 2 | medium |
| m3 | object | design | design | noun_chunk_root | chunk1 | 7 | high |
| m4 | attribute | sunburst | sunburst | compound_modifier | chunk1 | 6 | medium |
| m5 | object | crown | crown | noun_chunk_root | chunk2 | 10 | high |
| m6 | object | text | text | noun_chunk_root | chunk3 | 12 | high |
| m7 | context | surface | surface | spatial_region | chunk5 | 21 | medium |
| m8 | action | show | show | verb_predicate | doc | 4 | high |
| m9 | action | placed | place | verb_predicate | doc | 16 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> badges |
| e1 | has_attribute | m0 | m2 | medium | chunk0 amod -> badges |
| e2 | has_attribute | m3 | m4 | medium | chunk1 compound -> design |
| e3 | agent | m8 | m0 | medium | nsubj -> show |
| e4 | patient | m8 | m3 | medium | dobj -> show |
| e5 | agent | m9 | m0 | medium | nsubjpass -> placed; resolved They -> badges |
| e6 | relation | m3 | m5 | high | with |
| e7 | relation | m3 | m6 | high | with |
| e8 | relation | m0 | m7 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | badge | badges | object | m0 | raw_mention |  |  |  |
| ent_m3 | object | design | design | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | crown | crown | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | text | text | document | m6 | raw_mention |  |  |  |
| ent_m7 | context | surface | surface | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | show | show | show |  | agent:m0->ent_m0; patient:m3->ent_m3 |  |
| ce1 | m9 | placed | place | place |  | theme:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | m0 | ent_m0 | medium | e3 | nsubj -> show |  |  |
| ce0 | show | patient | m3 | ent_m3 | medium | e4 | dobj -> show |  |  |
| ce1 | place | theme | m0 | ent_m0 | medium | e5 | nsubjpass -> placed; resolved They -> badges |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m3 | m5 | ent_m3 | ent_m5 | with | high | e6 | False | False |  |  |
| cr1 | m3 | m6 | ent_m3 | ent_m6 | with | high | e7 | False | False |  |  |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | on | high | e8 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m9 | e5 | m0 |  |  | {"action_mention_id": "m9", "kind": "passive_subject_to_theme", "raw_edge_id": "e5", "target": "m0"} |

## 96

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `4ef94ef77dceaed5575f2fab38c07ce284810be3c71dde7af7e464bd0ccc8414`
**parse_path:** `sentence`

> A snow-covered sidewalk runs between parked cars and a house. A silver SUV is parked on the right, with a large bush and snow piled beside it. The street is lined with bare trees and houses under a dusky sky.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | sidewalk | sidewalk | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | snow-covered | snow-covered | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | cars | car | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | parked | park | state_attribute | chunk1 | 5 | medium |
| m4 | object | house | house | noun_chunk_root | chunk2 | 9 | high |
| m5 | object | SUV | suv | noun_chunk_root | chunk3 | 13 | high |
| m6 | attribute | silver | silver | color_attribute | chunk3 | 12 | high |
| m7 | context | right | right | spatial_region | chunk4 | 18 | medium |
| m8 | object | bush | bush | noun_chunk_root | chunk5 | 23 | high |
| m9 | attribute | large | large | size_attribute | chunk5 | 22 | high |
| m10 | object | snow | snow | noun_chunk_root | chunk6 | 25 | high |
| m11 | object | street | street | noun_chunk_root | chunk8 | 31 | high |
| m12 | object | trees | tree | noun_chunk_root | chunk9 | 36 | high |
| m13 | attribute | bare | bare | visual_attribute | chunk9 | 35 | medium |
| m14 | object | houses | house | noun_chunk_root | chunk10 | 38 | high |
| m15 | object | sky | sky | noun_chunk_root | chunk11 | 42 | high |
| m16 | attribute | dusky | dusky | modifier_attribute | chunk11 | 41 | medium |
| m17 | action | runs | run | verb_predicate | doc | 3 | high |
| m18 | action | parked | park | verb_predicate | doc | 15 | high |
| m19 | action | piled | pile | verb_predicate | doc | 26 | high |
| m20 | action | lined | line | verb_predicate | doc | 33 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> sidewalk |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> cars |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> SUV |
| e3 | has_attribute | m8 | m9 | high | chunk5 amod -> bush |
| e4 | has_attribute | m12 | m13 | medium | chunk9 amod -> trees |
| e5 | has_attribute | m15 | m16 | medium | chunk11 amod -> sky |
| e6 | agent | m17 | m0 | medium | nsubj -> runs |
| e7 | agent | m18 | m5 | medium | nsubjpass -> parked |
| e8 | agent | m19 | m8 | medium | inherited agent acl -> bush |
| e9 | agent | m20 | m11 | medium | nsubjpass -> lined |
| e10 | relation | m0 | m2 | high | between |
| e11 | relation | m0 | m4 | high | between |
| e12 | relation | m5 | m7 | high | on |
| e13 | relation | m5 | m8 | high | with |
| e14 | relation | m5 | m10 | high | with |
| e15 | relation | m8 | m5 | high | beside |
| e16 | relation | m11 | m12 | high | with |
| e17 | relation | m11 | m14 | high | with |
| e18 | relation | m14 | m15 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sidewalk | sidewalk | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | car | cars | vehicle | m2 | raw_mention |  |  |  |
| ent_m4 | object | house | house | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | suv | SUV | vehicle | m5 | raw_mention |  |  |  |
| ent_m7 | context | right | right | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | bush | bush | object | m8 | raw_mention |  |  |  |
| ent_m10 | object | snow | snow | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | street | street | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | tree | trees | object | m12 | raw_mention |  |  |  |
| ent_m14 | object | house | houses | object | m14 | raw_mention |  |  |  |
| ent_m15 | object | sky | sky | object | m15 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | runs | run | run |  | agent:m0->ent_m0 |  |
| ce1 | m18 | parked | park | park |  | theme:m5->ent_m5 |  |
| ce2 | m19 | piled | pile | pile |  | agent:m8->ent_m8 |  |
| ce3 | m20 | lined | line | line |  | theme:m11->ent_m11 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | run | agent | m0 | ent_m0 | medium | e6 | nsubj -> runs |  |  |
| ce1 | park | theme | m5 | ent_m5 | medium | e7 | nsubjpass -> parked |  |  |
| ce2 | pile | agent | m8 | ent_m8 | medium | e8 | inherited agent acl -> bush |  |  |
| ce3 | line | theme | m11 | ent_m11 | medium | e9 | nsubjpass -> lined |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | between | high | e10 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | between | high | e11 | False | False |  |  |
| cr2 | m5 | m7 | ent_m5 | ent_m7 | on | high | e12 | False | False |  |  |
| cr3 | m5 | m8 | ent_m5 | ent_m8 | with | high | e13 | False | False |  |  |
| cr4 | m5 | m10 | ent_m5 | ent_m10 | with | high | e14 | False | False |  |  |
| cr5 | m8 | m5 | ent_m8 | ent_m5 | beside | high | e15 | False | False |  |  |
| cr6 | m11 | m12 | ent_m11 | ent_m12 | with | high | e16 | False | False |  |  |
| cr7 | m11 | m14 | ent_m11 | ent_m14 | with | high | e17 | False | False |  |  |
| cr8 | m14 | m15 | ent_m14 | ent_m15 | under | high | e18 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m18 | e7 | m5 |  |  | {"action_mention_id": "m18", "kind": "passive_subject_to_theme", "raw_edge_id": "e7", "target": "m5"} |
| passive_subject_to_theme | m20 | e9 | m11 |  |  | {"action_mention_id": "m20", "kind": "passive_subject_to_theme", "raw_edge_id": "e9", "target": "m11"} |

## 97

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `51d7da189059dc55749d66b73dd715b598f2b475ef29bd301d4d1ae312bee414`
**parse_path:** `sentence`

> A skier in an orange helmet races down a snowy slope. Other skiers are visible in the background on the mountain.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | skier | skier | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | helmet | helmet | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | orange | orange | color_attribute | chunk1 | 4 | high |
| m3 | object | slope | slope | noun_chunk_root | chunk2 | 10 | high |
| m4 | attribute | snowy | snowy | modifier_attribute | chunk2 | 9 | medium |
| m5 | object | skiers | skier | noun_chunk_root | chunk3 | 13 | high |
| m6 | attribute | Other | other | modifier_attribute | chunk3 | 12 | medium |
| m7 | context | background | background | scene_context | chunk4 | 18 | high |
| m8 | object | mountain | mountain | noun_chunk_root | chunk5 | 21 | high |
| m9 | action | races | race | verb_predicate | doc | 6 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> helmet |
| e1 | has_attribute | m3 | m4 | medium | chunk2 amod -> slope |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> skiers |
| e3 | has_context | scene | m7 | high | scene_context token background |
| e4 | agent | m9 | m0 | medium | nsubj -> races |
| e5 | relation | m0 | m1 | high | in |
| e6 | relation | m0 | m3 | medium | down |
| e7 | relation | m5 | m7 | high | in |
| e8 | relation | m7 | m8 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | skier | skier | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | helmet | helmet | clothing | m1 | raw_mention |  |  |  |
| ent_m3 | object | slope | slope | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | skier | skiers | object | m5 | raw_mention |  |  |  |
| ent_m7 | context | background | background | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | mountain | mountain | object | m8 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | races | race | race |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | race | agent | m0 | ent_m0 | medium | e4 | nsubj -> races |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e5 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | down | medium | e6 | False | False |  |  |
| cr2 | m5 | m7 | ent_m5 | ent_m7 | in | high | e7 | False | False |  |  |
| cr3 | m7 | m8 | ent_m7 | ent_m8 | on | high | e8 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 98

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `521fef55b6e923e6376bef8ab4a4158436176b892a5537365ca12f4670742014`
**parse_path:** `sentence`

> A football team in white uniforms stands on the field with a referee nearby.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | team | team | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | football | football | compound_modifier | chunk0 | 1 | medium |
| m2 | object | uniforms | uniform | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | white | white | color_attribute | chunk1 | 4 | high |
| m4 | object | field | field | noun_chunk_root | chunk2 | 9 | high |
| m5 | action | stands | stand | verb_predicate | doc | 6 | high |
| m6 | object | referee | referee | with_absolute_recovered_object | with_absolute10 | 12 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 compound -> team |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> uniforms |
| e2 | agent | m5 | m0 | medium | nsubj -> stands |
| e3 | scene_contains | scene | m6 | medium | with_absolute10 recovered referee |
| e4 | relation | m0 | m2 | high | in |
| e5 | relation | m0 | m4 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | team | team | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | uniform | uniforms | clothing | m2 | raw_mention |  |  |  |
| ent_m4 | object | field | field | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | referee | referee | person | m6 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m5 | stands | stand | stand |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e2 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | high | e4 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | high | e5 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_

## 99

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `526c45c3e9f454f37c321a0e77be015a03b5384b98c2d52132db519bd9b88c14`
**parse_path:** `sentence`

> A woman in a red and black bikini jumps to hit a volleyball over the net on a sandy beach. Other people are visible in the background under white umbrellas, with the sun shining brightly overhead.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | bikini | bikini | noun_chunk_root | chunk1 | 7 | high |
| m2 | attribute | red | red | color_attribute | chunk1 | 4 | high |
| m3 | attribute | black | black | color_attribute | chunk1 | 6 | high |
| m4 | object | volleyball | volleyball | noun_chunk_root | chunk2 | 12 | high |
| m5 | object | net | net | noun_chunk_root | chunk3 | 15 | high |
| m6 | object | beach | beach | noun_chunk_root | chunk4 | 19 | high |
| m7 | attribute | sandy | sandy | modifier_attribute | chunk4 | 18 | medium |
| m8 | object | people | people | noun_chunk_root | chunk5 | 22 | high |
| m9 | attribute | Other | other | modifier_attribute | chunk5 | 21 | medium |
| m10 | context | background | background | scene_context | chunk6 | 27 | high |
| m11 | object | umbrellas | umbrella | noun_chunk_root | chunk7 | 30 | high |
| m12 | attribute | white | white | color_attribute | chunk7 | 29 | high |
| m13 | object | sun | sun | noun_chunk_root | chunk8 | 34 | high |
| m14 | action | jumps | jump | verb_predicate | doc | 8 | high |
| m15 | action | hit | hit | verb_predicate | doc | 10 | high |
| m16 | action | shining | shin | verb_predicate | doc | 35 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> bikini |
| e1 | has_attribute | m1 | m3 | high | chunk1 conj -> bikini |
| e2 | has_attribute | m6 | m7 | medium | chunk4 amod -> beach |
| e3 | has_attribute | m8 | m9 | medium | chunk5 amod -> people |
| e4 | has_context | scene | m10 | high | scene_context token background |
| e5 | has_attribute | m11 | m12 | high | chunk7 amod -> umbrellas |
| e6 | agent | m14 | m0 | medium | nsubj -> jumps |
| e7 | agent | m15 | m0 | medium | inherited agent advcl -> jumps |
| e8 | patient | m15 | m4 | medium | dobj -> hit |
| e9 | agent | m16 | m13 | medium | nsubj -> shining |
| e10 | relation | m0 | m1 | high | in |
| e11 | relation | m0 | m5 | high | over |
| e12 | relation | m0 | m6 | high | on |
| e13 | relation | m8 | m10 | high | in |
| e14 | relation | m8 | m11 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | bikini | bikini | object | m1 | raw_mention |  |  |  |
| ent_m4 | object | volleyball | volleyball | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | net | net | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | beach | beach | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | people | people | person | m8 | raw_mention |  |  |  |
| ent_m10 | context | background | background | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | umbrella | umbrellas | object | m11 | raw_mention |  |  |  |
| ent_m13 | object | sun | sun | object | m13 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m14 | jumps | jump | jump |  | agent:m0->ent_m0 |  |
| ce1 | m15 | hit | hit | hit |  | agent:m0->ent_m0; patient:m4->ent_m4 |  |
| ce2 | m16 | shining | shin | shin |  | agent:m13->ent_m13 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | jump | agent | m0 | ent_m0 | medium | e6 | nsubj -> jumps |  |  |
| ce1 | hit | agent | m0 | ent_m0 | medium | e7 | inherited agent advcl -> jumps |  |  |
| ce1 | hit | patient | m4 | ent_m4 | medium | e8 | dobj -> hit |  |  |
| ce2 | shin | agent | m13 | ent_m13 | medium | e9 | nsubj -> shining |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e10 | False | False |  |  |
| cr1 | m0 | m5 | ent_m4 | ent_m5 | over | high | e11 | False | False | pp_source_disambiguation | patient_trajectory |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | on | high | e12 | False | False |  |  |
| cr3 | m8 | m10 | ent_m8 | ent_m10 | in | high | e13 | False | False |  |  |
| cr4 | m8 | m11 | ent_m8 | ent_m11 | under | high | e14 | False | False |  |  |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| pp_source_disambiguated | m15 | e11 |  | ent_m5 | patient_trajectory | {"action_mention_id": "m15", "canonical_action": "hit", "canonical_source": "ent_m4", "canonical_target": "ent_m5", "confidence": "high", "kind": "pp_source_disambiguated", "previous_canonical_source": "ent_m0", "raw_edge_id": "e11", "raw_source": "m0", "raw_target": "m5", "reason": "patient_trajectory", "relation": "over"} |

## 100

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `528344da5e40f3da37b258a8808a079d436258cfb3f3f2fe991db7fb1672c014`
**parse_path:** `sentence`

> A lacrosse player in a white uniform runs through heavy snow on a snowy field. Another player in red is nearby.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | player | player | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | lacrosse | lacrosse | compound_modifier | chunk0 | 1 | medium |
| m2 | object | uniform | uniform | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | white | white | color_attribute | chunk1 | 5 | high |
| m4 | object | snow | snow | noun_chunk_root | chunk2 | 10 | high |
| m5 | attribute | heavy | heavy | modifier_attribute | chunk2 | 9 | medium |
| m6 | object | field | field | noun_chunk_root | chunk3 | 14 | high |
| m7 | attribute | snowy | snowy | modifier_attribute | chunk3 | 13 | medium |
| m8 | object | player | player | noun_chunk_root | chunk4 | 17 | high |
| m9 | attribute | red | red | color_attribute | chunk5 | 19 | high |
| m10 | action | runs | run | verb_predicate | doc | 7 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 compound -> player |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> uniform |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> snow |
| e3 | has_attribute | m6 | m7 | medium | chunk3 amod -> field |
| e4 | agent | m10 | m0 | medium | nsubj -> runs |
| e5 | relation | m0 | m2 | high | in |
| e6 | relation | m0 | m4 | medium | through |
| e7 | relation | m0 | m6 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | player | player | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | uniform | uniform | clothing | m2 | raw_mention |  |  |  |
| ent_m4 | object | snow | snow | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | field | field | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | player | player | person | m8 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | runs | run | run |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | run | agent | m0 | ent_m0 | medium | e4 | nsubj -> runs |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | high | e5 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | through | medium | e6 | False | False |  |  |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | on | high | e7 | False | False |  |  |

### Stage 9 Canonicalization Notes
_none_
