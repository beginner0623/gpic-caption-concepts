# Stage 9 Canonical v2 Case Detail - alt100 val00001

- input: `reports\canonical_concepts_alt100_val00001_trf_stage9_canonical_v2.jsonl`
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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | poster | posters | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:poster", "parents": []} |
| ent_m3 | object | wall | wall | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |
| ent_m5 | object | desk | desk | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m5 | raw_mention |  |  |  | True | {"canonical": "entity:desk", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m6 | object | computer_monitor | computer monitor | object | openimages_boxable\|visual_genome_object_synset\|wordnet_noun_mwe | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:computer_monitor", "parents": []} |
| ent_m7 | object | image | image | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:image", "parents": []} |
| ent_m8 | object | bottle | bottles | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:bottle", "parents": []} |
| ent_m10 | object | supply | supplies | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:supply", "parents": []} |
| ent_m12 | object | desk | desk | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m12 | raw_mention |  |  |  | True | {"canonical": "entity:desk", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m13 | mounted | mount | mount | raw_action | visual_action_fallback | visual_action |  | theme:m0->ent_m0 | {"canonical": "action:mount", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m14 | displays | display | display | raw_action | visual_action_fallback | visual_action |  | agent:m6->ent_m6; patient:m7->ent_m7 | {"canonical": "action:display", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m15 | sit | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m8->ent_m8; agent:m10->ent_m10 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | mount | theme | m0 | ent_m0 | medium | e5 | nsubjpass -> mounted |  |  |
| ce1 | display | agent | m6 | ent_m6 | medium | e6 | nsubj -> displays |  |  |
| ce1 | display | patient | m7 | ent_m7 | medium | e7 | dobj -> displays |  |  |
| ce2 | sit | agent | m8 | ent_m8 | medium | e8 | nsubj -> sit |  |  |
| ce2 | sit | agent | m10 | ent_m10 | medium | e9 | nsubj -> sit |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e10 | False | False |  |  |
| cr1 | m3 | m5 | ent_m3 | ent_m5 | above | above | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e11 | False | False |  |  |
| cr2 | m8 | m12 | ent_m8 | ent_m12 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e12 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | poster |  |  |  | entity_exists:poster | True | low |
| cf1 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf2 | entity_exists | desk |  |  | furniture, artifact | entity_exists:desk | True | high |
| cf3 | entity_exists | computer_monitor |  |  |  | entity_exists:computer_monitor | True | high |
| cf4 | entity_exists | image |  |  |  | entity_exists:image | True | low |
| cf5 | entity_exists | bottle |  |  |  | entity_exists:bottle | True | low |
| cf6 | entity_exists | supply |  |  |  | entity_exists:supply | True | low |
| cf7 | entity_exists | desk |  |  | furniture, artifact | entity_exists:desk | True | high |
| cf8 | has_quantity | poster | several |  | approximate_quantity, quantity | has_quantity:poster:several | True | medium |
| cf9 | has_attribute | poster | colorful |  | color_attribute, color_quantity, visual_attribute | has_attribute:poster:colorful | True | medium |
| cf10 | has_attribute | wall | white |  | color_attribute, color, visual_attribute | has_attribute:wall:white | True | high |
| cf11 | has_quantity | bottle | various |  | approximate_quantity, quantity | has_quantity:bottle:various | True | medium |
| cf12 | has_attribute | supply | art |  | compound_modifier, visual_attribute | has_attribute:supply:art | True | medium |
| cf13 | action_event | mount |  |  | visual_action | action_event:mount | True | low |
| cf14 | event_role | mount | theme | poster |  | event_role:mount:theme:poster | True | medium |
| cf15 | action_event | display |  |  | visual_action | action_event:display | True | low |
| cf16 | event_role | display | agent | computer_monitor |  | event_role:display:agent:computer_monitor | True | medium |
| cf17 | event_role | display | patient | image |  | event_role:display:patient:image | True | medium |
| cf18 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf19 | event_role | sit | agent | bottle |  | event_role:sit:agent:bottle | True | medium |
| cf20 | event_role | sit | agent | supply |  | event_role:sit:agent:supply | True | medium |
| cf21 | relation | poster | on | wall | spatial_support, visual_relation | relation:poster:on:wall | True | high |
| cf22 | relation | wall | above | desk | spatial_vertical, visual_relation | relation:wall:above:desk | True | high |
| cf23 | relation | bottle | on | desk | spatial_support, visual_relation | relation:bottle:on:desk | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | church | church | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:church", "parents": []} |
| ent_m2 | object | tower | towers | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:tower", "parents": []} |
| ent_m4 | object | walkway | walkway | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:walkway", "parents": []} |
| ent_m6 | object | garden | garden | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:garden", "parents": []} |
| ent_m8 | object | hedge | hedges | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:hedge", "parents": []} |
| ent_m10 | object | flower | flowers | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:flower", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e6 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e7 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e8 | False | False |  |  |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | beside | next_to | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e9 | False | False |  |  |
| cr3 | m6 | m8 | ent_m6 | ent_m8 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e10 | False | False |  |  |
| cr4 | m6 | m10 | ent_m6 | ent_m10 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e11 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | church |  |  |  | entity_exists:church | True | low |
| cf1 | entity_exists | tower |  |  |  | entity_exists:tower | True | low |
| cf2 | entity_exists | walkway |  |  |  | entity_exists:walkway | True | low |
| cf3 | entity_exists | garden |  |  |  | entity_exists:garden | True | low |
| cf4 | entity_exists | hedge |  |  |  | entity_exists:hedge | True | low |
| cf5 | entity_exists | flower |  |  |  | entity_exists:flower | True | low |
| cf6 | has_attribute | church | stone |  | material_attribute, material, visual_attribute | has_attribute:church:stone | True | high |
| cf7 | has_attribute | tower | pointed |  | modifier_attribute, visual_attribute | has_attribute:tower:pointed | True | medium |
| cf8 | has_attribute | walkway | arched |  | visual_attribute | has_attribute:walkway:arched | True | medium |
| cf9 | has_attribute | garden | grassy |  | modifier_attribute, visual_attribute | has_attribute:garden:grassy | True | medium |
| cf10 | has_attribute | hedge | trim |  | state_attribute, visual_attribute | has_attribute:hedge:trim | True | medium |
| cf11 | has_attribute | flower | pink |  | color_attribute, color, visual_attribute | has_attribute:flower:pink | True | high |
| cf12 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf13 | event_role | stand | agent | church |  | event_role:stand:agent:church | True | medium |
| cf14 | relation | church | with | tower | association_relation, visual_relation | relation:church:with:tower | True | high |
| cf15 | relation | church | with | walkway | association_relation, visual_relation | relation:church:with:walkway | True | high |
| cf16 | relation | church | next_to | garden | spatial_proximity, visual_relation | relation:church:next_to:garden | True | high |
| cf17 | relation | garden | with | hedge | association_relation, visual_relation | relation:garden:with:hedge | True | high |
| cf18 | relation | garden | with | flower | association_relation, visual_relation | relation:garden:with:flower | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e9 |  |  |  | {"canonical": "next_to", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e9", "raw_relation": "beside", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | tricycle | tricycle | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:tricycle", "parents": []} |
| ent_m2 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m2 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m4 | context | outdoor | outdoor | object | raw_lemma | stage9_seed:parent_seed | scene_context | m4 | raw_mention |  |  |  | True | {"canonical": "entity:outdoor", "parents": ["entity_parent:scene_context"]} |
| ent_m5 | object | tree | trees | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | tricycle |  |  |  | entity_exists:tricycle | True | low |
| cf1 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf2 | entity_exists | outdoor |  |  | scene_context | entity_exists:outdoor | True | high |
| cf3 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf4 | has_attribute | tricycle | orange |  | color_attribute, color, visual_attribute | has_attribute:tricycle:orange | True | high |
| cf5 | candidate_has_attribute | man | smile |  | floating_attribute, visual_attribute | candidate_has_attribute:man:smile | False | low |
| cf6 | has_attribute | tree | green |  | color_attribute, color, visual_attribute | has_attribute:tree:green | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m2 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m3 | object | street | street | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:street", "parents": []} |
| ent_m5 | object | hand | hands | object | raw_lemma | stage9_seed:parent_seed | body_part | m5 | raw_mention |  |  |  | True | {"canonical": "entity:hand", "parents": ["entity_parent:body_part"]} |
| ent_m6 | object | building | building | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | walk | walk | walk | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0; agent:m2->ent_m2 | {"canonical": "action:walk", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m9 | holding | hold | hold | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action |  | agent:m0->ent_m0; agent:m2->ent_m2; patient:m5->ent_m5 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | walk | agent | m0 | ent_m0 | medium | e3 | nsubj -> walk |  |  |
| ce0 | walk | agent | m2 | ent_m2 | medium | e4 | nsubj -> walk |  |  |
| ce1 | hold | agent | m0 | ent_m0 | medium | e5 | inherited agent advcl -> walk |  |  |
| ce1 | hold | agent | m2 | ent_m2 | medium | e6 | inherited agent advcl -> walk |  |  |
| ce1 | hold | patient | m5 | ent_m5 | medium | e7 | dobj -> holding |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e8 | False | False |  |  |
| cr1 | m0 | m6 | ent_m0 | ent_m6 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf2 | entity_exists | street |  |  |  | entity_exists:street | True | low |
| cf3 | entity_exists | hand |  |  | body_part | entity_exists:hand | True | high |
| cf4 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf5 | has_attribute | man | old |  | condition_attribute, clean_exact_overlap, maturity, newness, visual_attribute | has_attribute:man:old | True | medium |
| cf6 | has_attribute | street | city |  | compound_modifier, visual_attribute | has_attribute:street:city | True | medium |
| cf7 | has_attribute | building | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:building:large | True | high |
| cf8 | action_event | walk |  |  | locomotion_action, visual_action | action_event:walk | True | high |
| cf9 | event_role | walk | agent | man |  | event_role:walk:agent:man | True | medium |
| cf10 | event_role | walk | agent | woman |  | event_role:walk:agent:woman | True | medium |
| cf11 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf12 | event_role | hold | agent | man |  | event_role:hold:agent:man | True | medium |
| cf13 | event_role | hold | agent | woman |  | event_role:hold:agent:woman | True | medium |
| cf14 | event_role | hold | patient | hand |  | event_role:hold:patient:hand | True | medium |
| cf15 | relation | man | on | street | spatial_support, visual_relation | relation:man:on:street | True | high |
| cf16 | relation | man | near | building | spatial_proximity, visual_relation | relation:man:near:building | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | street | street | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:street", "parents": []} |
| ent_m2 | object | water | water | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": []} |
| ent_m3 | object | road | road | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:road", "parents": []} |
| ent_m4 | object | stop_sign | stop signs | object | coco_object\|lvis_object\|openimages_boxable\|visual_genome_object_synset | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:stop_sign", "parents": []} |
| ent_m5 | object | sign | sign | document | raw_lemma | stage9_seed:parent_seed | text_carrier, artifact | m5 | raw_mention |  |  |  | True | {"canonical": "entity:sign", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m8 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m8 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m9 | object | tree | trees | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m11 | object | hill | hill | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:hill", "parents": []} |
| ent_m13 | object | floodwater | floodwaters | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:floodwater", "parents": []} |
| ent_m14 | object | sky | sky | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | covering | cover | cover | raw_action | visual_action_fallback | visual_action |  | agent:m2->ent_m2; patient:m3->ent_m3 | {"canonical": "action:cover", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m16 | submerging | submerge | submerge | raw_action | visual_action_fallback | visual_action |  | agent:m2->ent_m2; patient:m4->ent_m4 | {"canonical": "action:submerge", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m17 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m5->ent_m5 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | cover | agent | m2 | ent_m2 | medium | e6 | nsubj -> covering |  |  |
| ce0 | cover | patient | m3 | ent_m3 | medium | e7 | dobj -> covering |  |  |
| ce1 | submerge | agent | m2 | ent_m2 | medium | e8 | inherited agent conj -> covering |  |  |
| ce1 | submerge | patient | m4 | ent_m4 | medium | e9 | dobj -> submerging |  |  |
| ce2 | stand | agent | m5 | ent_m5 | medium | e10 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m5 | m8 | ent_m5 | ent_m8 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e11 | False | False |  |  |
| cr1 | m5 | m9 | ent_m5 | ent_m9 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e12 | False | False |  |  |
| cr2 | m5 | m11 | ent_m5 | ent_m11 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e13 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | street |  |  |  | entity_exists:street | True | low |
| cf1 | entity_exists | water |  |  |  | entity_exists:water | True | low |
| cf2 | entity_exists | road |  |  |  | entity_exists:road | True | low |
| cf3 | entity_exists | stop_sign |  |  |  | entity_exists:stop_sign | True | high |
| cf4 | entity_exists | sign |  |  | text_carrier, artifact | entity_exists:sign | True | high |
| cf5 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf6 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf7 | entity_exists | hill |  |  |  | entity_exists:hill | True | low |
| cf8 | entity_exists | floodwater |  |  |  | entity_exists:floodwater | True | low |
| cf9 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf10 | has_attribute | street | flooded |  | modifier_attribute, visual_attribute | has_attribute:street:flooded | True | medium |
| cf11 | has_attribute | sign | green |  | color_attribute, color, visual_attribute | has_attribute:sign:green | True | high |
| cf12 | has_attribute | sign | digital |  | modifier_attribute, visual_attribute | has_attribute:sign:digital | True | medium |
| cf13 | has_attribute | tree | bare |  | visual_attribute | has_attribute:tree:bare | True | medium |
| cf14 | has_attribute | hill | grassy |  | modifier_attribute, visual_attribute | has_attribute:hill:grassy | True | medium |
| cf15 | action_event | cover |  |  | visual_action | action_event:cover | True | low |
| cf16 | event_role | cover | agent | water |  | event_role:cover:agent:water | True | medium |
| cf17 | event_role | cover | patient | road |  | event_role:cover:patient:road | True | medium |
| cf18 | action_event | submerge |  |  | visual_action | action_event:submerge | True | low |
| cf19 | event_role | submerge | agent | water |  | event_role:submerge:agent:water | True | medium |
| cf20 | event_role | submerge | patient | stop_sign |  | event_role:submerge:patient:stop_sign | True | medium |
| cf21 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf22 | event_role | stand | agent | sign |  | event_role:stand:agent:sign | True | medium |
| cf23 | relation | sign | in | background | spatial_containment, visual_relation | relation:sign:in:background | True | high |
| cf24 | relation | sign | with | tree | association_relation, visual_relation | relation:sign:with:tree | True | high |
| cf25 | relation | sign | with | hill | association_relation, visual_relation | relation:sign:with:hill | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | football_player | football players | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:football_player", "parents": []} |
| ent_m2 | object | uniform | uniforms | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m5 | object | field | field | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |
| ent_m7 | object | line | lines | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:line", "parents": []} |
| ent_m9 | object | helmet | helmets | clothing | raw_lemma | stage9_seed:parent_seed | protective_gear, clothing, wearable | m9 | raw_mention |  |  |  | True | {"canonical": "entity:helmet", "parents": ["entity_parent:protective_gear", "entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m10 | object | glove | gloves | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:glove", "parents": []} |
| ent_m11 | object | snow | snow | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:snow", "parents": []} |
| ent_m12 | object | sideline | sidelines | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:sideline", "parents": []} |
| ent_m13 | object | cone | cones | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:cone", "parents": []} |
| ent_m15 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m15 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m16 | object | tree | trees | object | raw_lemma | none |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m18 | object | fence | fence | object | raw_lemma | none |  | m18 | raw_mention |  |  |  | True | {"canonical": "entity:fence", "parents": []} |
| ent_m19 | object | lighting | lighting | object | raw_lemma | none |  | m19 | raw_mention |  |  |  | True | {"canonical": "entity:lighting", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m21 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m22 | wear | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m0->ent_m0; patient:m9->ent_m9; patient:m10->ent_m10 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce2 | m23 | shows | show | show | raw_action | visual_action_fallback | visual_action |  | agent:m15->ent_m15; patient:m16->ent_m16; patient:m18->ent_m18 | {"canonical": "action:show", "parents": ["action_parent:visual_action"]} |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e16 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e17 | False | False |  |  |
| cr2 | m5 | m7 | ent_m5 | ent_m7 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e18 | False | False |  |  |
| cr3 | m0 | m11 | ent_m0 | ent_m11 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e19 | False | False |  |  |
| cr4 | m0 | m13 | ent_m0 | ent_m13 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e20 | False | False |  |  |
| cr5 | m16 | m19 | ent_m16 | ent_m19 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e21 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | football_player |  |  |  | entity_exists:football_player | True | high |
| cf1 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf2 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf3 | entity_exists | line |  |  |  | entity_exists:line | True | low |
| cf4 | entity_exists | helmet |  |  | protective_gear, clothing, wearable | entity_exists:helmet | True | high |
| cf5 | entity_exists | glove |  |  |  | entity_exists:glove | True | low |
| cf6 | entity_exists | snow |  |  |  | entity_exists:snow | True | low |
| cf7 | entity_exists | sideline |  |  |  | entity_exists:sideline | True | low |
| cf8 | entity_exists | cone |  |  |  | entity_exists:cone | True | low |
| cf9 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf10 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf11 | entity_exists | fence |  |  |  | entity_exists:fence | True | low |
| cf12 | entity_exists | lighting |  |  |  | entity_exists:lighting | True | low |
| cf13 | has_quantity | football_player | three |  | exact_quantity, quantity | has_quantity:football_player:three | True | high |
| cf14 | has_attribute | uniform | blue |  | color_attribute, color, visual_attribute | has_attribute:uniform:blue | True | high |
| cf15 | has_attribute | uniform | black |  | color_attribute, color, visual_attribute | has_attribute:uniform:black | True | high |
| cf16 | has_attribute | field | grass |  | compound_modifier, visual_attribute | has_attribute:field:grass | True | medium |
| cf17 | has_attribute | line | white |  | color_attribute, color, visual_attribute | has_attribute:line:white | True | high |
| cf18 | has_attribute | cone | orange |  | color_attribute, color, visual_attribute | has_attribute:cone:orange | True | high |
| cf19 | has_attribute | tree | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:tree:dark | True | medium |
| cf20 | has_attribute | lighting | dim |  | modifier_attribute, visual_attribute | has_attribute:lighting:dim | True | medium |
| cf21 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf22 | event_role | stand | agent | football_player |  | event_role:stand:agent:football_player | True | medium |
| cf23 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf24 | event_role | wear | agent | football_player |  | event_role:wear:agent:football_player | True | medium |
| cf25 | event_role | wear | patient | helmet |  | event_role:wear:patient:helmet | True | medium |
| cf26 | event_role | wear | patient | glove |  | event_role:wear:patient:glove | True | medium |
| cf27 | action_event | show |  |  | visual_action | action_event:show | True | low |
| cf28 | event_role | show | agent | background |  | event_role:show:agent:background | True | medium |
| cf29 | event_role | show | patient | tree |  | event_role:show:patient:tree | True | medium |
| cf30 | event_role | show | patient | fence |  | event_role:show:patient:fence | True | medium |
| cf31 | relation | football_player | in | uniform | spatial_containment, visual_relation | relation:football_player:in:uniform | True | high |
| cf32 | relation | football_player | on | field | spatial_support, visual_relation | relation:football_player:on:field | True | high |
| cf33 | relation | field | with | line | association_relation, visual_relation | relation:field:with:line | True | high |
| cf34 | relation | football_player | with | snow | association_relation, visual_relation | relation:football_player:with:snow | True | high |
| cf35 | relation | football_player | with | cone | association_relation, visual_relation | relation:football_player:with:cone | True | high |
| cf36 | relation | tree | under | lighting | spatial_vertical, visual_relation | relation:tree:under:lighting | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | plaza | plaza | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:plaza", "parents": []} |
| ent_m4 | object | building | building | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m8 | object | sky | sky | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m11 | object | car | cars | vehicle | raw_lemma | stage9_seed:parent_seed | vehicle | m11 | raw_mention |  |  |  | True | {"canonical": "entity:car", "parents": ["entity_parent:vehicle"]} |
| ent_m14 | object | street | street | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:street", "parents": []} |
| ent_m15 | context | right | right | object | raw_lemma | semantic_type_fallback | scene_context | m15 | raw_mention |  |  |  | True | {"canonical": "entity:right", "parents": ["entity_parent:scene_context"]} |
| ent_m16 | object | sign | sign | document | raw_lemma | stage9_seed:parent_seed | text_carrier, artifact | m16 | raw_mention |  |  |  | True | {"canonical": "entity:sign", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m18 | object | lamppost | lamppost | object | raw_lemma | none |  | m18 | raw_mention |  |  |  | True | {"canonical": "entity:lamppost", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m20 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m21 | line | line | line | raw_action | visual_action_fallback | visual_action |  | agent:m11->ent_m11; patient:m14->ent_m14 | {"canonical": "action:line", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e11 | nsubj -> stand |  |  |
| ce1 | line | agent | m11 | ent_m11 | medium | e12 | nsubj -> line |  |  |
| ce1 | line | patient | m14 | ent_m14 | medium | e13 | dobj -> line |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e14 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e15 | False | False |  |  |
| cr2 | m0 | m8 | ent_m0 | ent_m8 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e16 | False | False |  |  |
| cr3 | m11 | m15 | ent_m11 | ent_m15 | to | to | raw_relation | raw_relation | visual_relation | medium | e17 | False | False |  |  |
| cr4 | m11 | m16 | ent_m11 | ent_m16 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e18 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | plaza |  |  |  | entity_exists:plaza | True | low |
| cf2 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf3 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf4 | entity_exists | car |  |  | vehicle | entity_exists:car | True | high |
| cf5 | entity_exists | street |  |  |  | entity_exists:street | True | low |
| cf6 | entity_exists | right |  |  | scene_context | entity_exists:right | True | medium |
| cf7 | entity_exists | sign |  |  | text_carrier, artifact | entity_exists:sign | True | high |
| cf8 | entity_exists | lamppost |  |  |  | entity_exists:lamppost | True | low |
| cf9 | has_quantity | people | two |  | exact_quantity, quantity | has_quantity:people:two | True | high |
| cf10 | has_attribute | plaza | paved |  | visual_attribute | has_attribute:plaza:paved | True | medium |
| cf11 | has_attribute | building | tall |  | size_attribute, height, visual_attribute | has_attribute:building:tall | True | high |
| cf12 | has_attribute | building | green |  | color_attribute, color, visual_attribute | has_attribute:building:green | True | high |
| cf13 | has_attribute | building | spire |  | compound_modifier, visual_attribute | has_attribute:building:spire | True | medium |
| cf14 | has_attribute | sky | clear |  | weather_attribute, opaqeness, weather, visual_attribute | has_attribute:sky:clear | True | medium |
| cf15 | has_attribute | sky | blue |  | color_attribute, color, visual_attribute | has_attribute:sky:blue | True | high |
| cf16 | has_quantity | car | several |  | approximate_quantity, quantity | has_quantity:car:several | True | medium |
| cf17 | has_attribute | car | parked |  | state_attribute, coco_subtype_rule, visual_attribute | has_attribute:car:parked | True | medium |
| cf18 | has_attribute | sign | parking |  | compound_modifier, visual_attribute | has_attribute:sign:parking | True | medium |
| cf19 | has_attribute | lamppost | gray |  | color_attribute, color, visual_attribute | has_attribute:lamppost:gray | True | high |
| cf20 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf21 | event_role | stand | agent | people |  | event_role:stand:agent:people | True | medium |
| cf22 | action_event | line |  |  | visual_action | action_event:line | True | low |
| cf23 | event_role | line | agent | car |  | event_role:line:agent:car | True | medium |
| cf24 | event_role | line | patient | street |  | event_role:line:patient:street | True | medium |
| cf25 | relation | people | on | plaza | spatial_support, visual_relation | relation:people:on:plaza | True | high |
| cf26 | relation | people | near | building | spatial_proximity, visual_relation | relation:people:near:building | True | high |
| cf27 | relation | people | under | sky | spatial_vertical, visual_relation | relation:people:under:sky | True | high |
| cf28 | relation | car | to | right | visual_relation | relation:car:to:right | True | medium |
| cf29 | relation | car | with | sign | association_relation, visual_relation | relation:car:with:sign | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woodpecker | woodpecker | animal | raw_lemma | stage9_seed:parent_seed | bird, animal, living_thing | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woodpecker", "parents": ["entity_parent:bird", "entity_parent:animal", "entity_parent:living_thing"]} |
| ent_m1 | object | feather | feathers | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:feather", "parents": []} |
| ent_m5 | object | log | log | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:log", "parents": []} |
| ent_m7 | object | grass | grass | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | perches | perch | perch | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:perch", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | perch | agent | m0 | ent_m0 | medium | e5 | nsubj -> perches |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e7 | False | False |  |  |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woodpecker |  |  | bird, animal, living_thing | entity_exists:woodpecker | True | high |
| cf1 | entity_exists | feather |  |  |  | entity_exists:feather | True | low |
| cf2 | entity_exists | log |  |  |  | entity_exists:log | True | low |
| cf3 | entity_exists | grass |  |  |  | entity_exists:grass | True | low |
| cf4 | has_attribute | feather | black |  | color_attribute, color, visual_attribute | has_attribute:feather:black | True | high |
| cf5 | has_attribute | feather | white |  | color_attribute, color, visual_attribute | has_attribute:feather:white | True | high |
| cf6 | has_attribute | feather | red |  | color_attribute, color, visual_attribute | has_attribute:feather:red | True | high |
| cf7 | has_attribute | log | broken |  | state_attribute, other, state, visual_attribute | has_attribute:log:broken | True | medium |
| cf8 | has_attribute | grass | tall |  | size_attribute, height, visual_attribute | has_attribute:grass:tall | True | high |
| cf9 | action_event | perch |  |  | visual_action | action_event:perch | True | low |
| cf10 | event_role | perch | agent | woodpecker |  | event_role:perch:agent:woodpecker | True | medium |
| cf11 | relation | woodpecker | with | feather | association_relation, visual_relation | relation:woodpecker:with:feather | True | high |
| cf12 | relation | woodpecker | on | log | spatial_support, visual_relation | relation:woodpecker:on:log | True | high |
| cf13 | relation | woodpecker | in | grass | spatial_containment, visual_relation | relation:woodpecker:in:grass | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | pant | pants | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:pant", "parents": []} |
| ent_m3 | object | step | steps | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:step", "parents": []} |
| ent_m5 | object | building | building | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m7 | object | tree | trees | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | pant |  |  |  | entity_exists:pant | True | low |
| cf2 | entity_exists | step |  |  |  | entity_exists:step | True | low |
| cf3 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf4 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf5 | has_attribute | pant | purple |  | color_attribute, color, visual_attribute | has_attribute:pant:purple | True | high |
| cf6 | has_attribute | step | stone |  | material_attribute, material, visual_attribute | has_attribute:step:stone | True | high |
| cf7 | has_attribute | building | classical |  | attribute, visual_attribute | has_attribute:building:classical | True | high |
| cf8 | has_attribute | tree | autumn |  | attribute, visual_attribute | has_attribute:tree:autumn | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sweater | sweater | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:sweater", "parents": []} |
| ent_m2 | object | child | child | person | raw_lemma | stage9_seed:parent_seed | person, human | m2 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m3 | object | drawing | drawing | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:drawing", "parents": []} |
| ent_m4 | object | locker | lockers | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:locker", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | sweater |  |  |  | entity_exists:sweater | True | low |
| cf1 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf2 | entity_exists | drawing |  |  |  | entity_exists:drawing | True | low |
| cf3 | entity_exists | locker |  |  |  | entity_exists:locker | True | low |
| cf4 | has_attribute | sweater | yellow |  | color_attribute, color, visual_attribute | has_attribute:sweater:yellow | True | high |
| cf5 | has_attribute | locker | green |  | color_attribute, color, visual_attribute | has_attribute:locker:green | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m2 | object | image | image | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:image", "parents": []} |
| ent_m3 | object | page | page | document | raw_lemma | stage9_seed:parent_seed | document, text_carrier, artifact | m3 | raw_mention |  |  |  | True | {"canonical": "entity:page", "parents": ["entity_parent:document", "entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m4 | object | book | book | document | raw_lemma | stage9_seed:parent_seed | document, text_carrier, artifact | m4 | raw_mention |  |  |  | True | {"canonical": "entity:book", "parents": ["entity_parent:document", "entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m5 | object | text | text | document | raw_lemma | stage9_seed:parent_seed | text_content | m5 | raw_mention |  |  |  | True | {"canonical": "entity:text", "parents": ["entity_parent:text_content"]} |
| ent_m7 | object | section | sections | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:section", "parents": []} |
| ent_m9 | object | title | titles | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:title", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | shows | show | show | raw_action | visual_action_fallback | visual_action |  | agent:m2->ent_m2; patient:m3->ent_m3 | {"canonical": "action:show", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m11 | listing | list | list | raw_action | visual_action_fallback | visual_action |  | agent:m2->ent_m2; patient:m7->ent_m7; patient:m9->ent_m9 | {"canonical": "action:list", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | m2 | ent_m2 | medium | e2 | nsubj -> shows |  |  |
| ce0 | show | patient | m3 | ent_m3 | medium | e3 | dobj -> shows |  |  |
| ce1 | list | agent | m2 | ent_m2 | medium | e4 | inherited agent advcl -> shows |  |  |
| ce1 | list | patient | m7 | ent_m7 | medium | e5 | dobj -> listing |  |  |
| ce1 | list | patient | m9 | ent_m9 | medium | e6 | dobj -> listing |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m3 | m4 | ent_m3 | ent_m4 | from | from | raw_relation | raw_relation | visual_relation | medium | e7 | False | False |  |  |
| cr1 | m4 | m5 | ent_m4 | ent_m5 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e8 | False | False |  |  |
| cr2 | m9 | m0 | ent_m9 |  | like | like | raw_relation | raw_relation | visual_relation | medium | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | image |  |  |  | entity_exists:image | True | low |
| cf1 | entity_exists | page |  |  | document, text_carrier, artifact | entity_exists:page | True | high |
| cf2 | entity_exists | book |  |  | document, text_carrier, artifact | entity_exists:book | True | high |
| cf3 | entity_exists | text |  |  | text_content | entity_exists:text | True | high |
| cf4 | entity_exists | section |  |  |  | entity_exists:section | True | low |
| cf5 | entity_exists | title |  |  |  | entity_exists:title | True | low |
| cf6 | has_attribute | text | russian |  | modifier_attribute, visual_attribute | has_attribute:text:russian | True | medium |
| cf7 | has_attribute | section | number |  | state_attribute, visual_attribute | has_attribute:section:number | True | medium |
| cf8 | action_event | show |  |  | visual_action | action_event:show | True | low |
| cf9 | event_role | show | agent | image |  | event_role:show:agent:image | True | medium |
| cf10 | event_role | show | patient | page |  | event_role:show:patient:page | True | medium |
| cf11 | action_event | list |  |  | visual_action | action_event:list | True | low |
| cf12 | event_role | list | agent | image |  | event_role:list:agent:image | True | medium |
| cf13 | event_role | list | patient | section |  | event_role:list:patient:section | True | medium |
| cf14 | event_role | list | patient | title |  | event_role:list:patient:title | True | medium |
| cf15 | relation | page | from | book | visual_relation | relation:page:from:book | True | medium |
| cf16 | relation | book | with | text | association_relation, visual_relation | relation:book:with:text | True | high |
| cf17 | relation | title | like |  | visual_relation | relation:title:like | False | medium |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | party | party | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:party", "parents": []} |
| ent_m4 | object | dress | dress | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:dress", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m6 | object | jacket | jacket | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m6 | raw_mention |  |  |  | True | {"canonical": "entity:jacket", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m8 | object | arm | arms | object | raw_lemma | stage9_seed:parent_seed | body_part | m8 | raw_mention |  |  |  | True | {"canonical": "entity:arm", "parents": ["entity_parent:body_part"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | party |  |  |  | entity_exists:party | True | low |
| cf2 | entity_exists | dress |  |  | clothing, wearable | entity_exists:dress | True | high |
| cf3 | entity_exists | jacket |  |  | clothing, wearable | entity_exists:jacket | True | high |
| cf4 | entity_exists | arm |  |  | body_part | entity_exists:arm | True | high |
| cf5 | has_attribute | people | dance |  | state_attribute, visual_attribute | has_attribute:people:dance | True | high |
| cf6 | has_attribute | party | indoor |  | attribute, visual_attribute | has_attribute:party:indoor | True | high |
| cf7 | has_attribute | dress | floral |  | pattern_attribute, pattern, pattern_marking, textile_pattern, visual_attribute | has_attribute:dress:floral | True | high |
| cf8 | has_attribute | jacket | denim |  | material_attribute, material, visual_attribute | has_attribute:jacket:denim | True | high |
| cf9 | has_attribute | arm | raise |  | state_attribute, visual_attribute | has_attribute:arm:raise | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | player | Players | person | raw_lemma | stage9_seed:parent_seed | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:player", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | jersey | jerseys | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:jersey", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m5 | object | ice_rink | ice rink | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:ice_rink", "parents": []} |
| ent_m6 | object | game | game | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:game", "parents": []} |
| ent_m8 | object | goalie | goalie | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:goalie", "parents": []} |
| ent_m9 | object | net | net | object | raw_lemma | stage9_seed:parent_seed | sports_equipment, artifact | m9 | raw_mention |  |  |  | True | {"canonical": "entity:net", "parents": ["entity_parent:sports_equipment", "entity_parent:artifact"]} |
| ent_m10 | object | stick | sticks | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:stick", "parents": []} |
| ent_m11 | object | ice | ice | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:ice", "parents": []} |
| eref_m12 | complement_subset | player | others | person | raw_lemma | stage9_seed:parent_seed | person, human | m12 | stage9_reference | ent_m1 |  | many | True | {"canonical": "entity:player", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m12 | eref_m12 | m1 | ent_m1 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m13 | skate | skate | skate | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:skate", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m14 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m8->ent_m8 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce2 | m15 | maneuver | maneuver | maneuver | raw_action | visual_action_fallback | visual_action |  | agent:m1->eref_m12 | {"canonical": "action:maneuver", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | skate | agent | m1 | ent_m1 | medium | e4 | nsubj -> skate |  |  |
| ce1 | stand | agent | m8 | ent_m8 | medium | e5 | nsubj -> stands |  |  |
| ce2 | maneuver | agent | m1 | eref_m12 | medium | e6 | nsubj -> maneuver; resolved others -> Players |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e7 | False | False |  |  |
| cr1 | m1 | m5 | ent_m1 | ent_m5 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e8 | False | False |  |  |
| cr2 | m1 | m6 | ent_m1 | ent_m6 | during | during | raw_relation | raw_relation | visual_relation | medium | e9 | False | False |  |  |
| cr3 | m8 | m9 | ent_m8 | ent_m9 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e10 | False | False |  |  |
| cr4 | m1 | m10 | ent_m1 | ent_m10 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e11 | False | False |  |  |
| cr5 | m1 | m11 | ent_m1 | ent_m11 | across | across | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | high | e12 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | player |  |  | person, human | entity_exists:player | True | high |
| cf1 | entity_exists | jersey |  |  | clothing, wearable | entity_exists:jersey | True | high |
| cf2 | entity_exists | ice_rink |  |  |  | entity_exists:ice_rink | True | high |
| cf3 | entity_exists | game |  |  |  | entity_exists:game | True | low |
| cf4 | entity_exists | goalie |  |  |  | entity_exists:goalie | True | low |
| cf5 | entity_exists | net |  |  | sports_equipment, artifact | entity_exists:net | True | medium |
| cf6 | entity_exists | stick |  |  |  | entity_exists:stick | True | low |
| cf7 | entity_exists | ice |  |  |  | entity_exists:ice | True | low |
| cf8 | entity_exists | player |  |  | person, human | entity_exists:player | True | high |
| cf9 | has_attribute | jersey | red |  | color_attribute, color, visual_attribute | has_attribute:jersey:red | True | high |
| cf10 | has_attribute | jersey | maroon |  | color_attribute, color, visual_attribute | has_attribute:jersey:maroon | True | high |
| cf11 | has_attribute | game | hockey |  | compound_modifier, visual_attribute | has_attribute:game:hockey | True | medium |
| cf12 | action_event | skate |  |  | locomotion_action, visual_action | action_event:skate | True | high |
| cf13 | event_role | skate | agent | player |  | event_role:skate:agent:player | True | medium |
| cf14 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf15 | event_role | stand | agent | goalie |  | event_role:stand:agent:goalie | True | medium |
| cf16 | action_event | maneuver |  |  | visual_action | action_event:maneuver | True | low |
| cf17 | event_role | maneuver | agent | player |  | event_role:maneuver:agent:player | True | medium |
| cf18 | relation | player | in | jersey | spatial_containment, visual_relation | relation:player:in:jersey | True | high |
| cf19 | relation | player | on | ice_rink | spatial_support, visual_relation | relation:player:on:ice_rink | True | high |
| cf20 | relation | player | during | game | visual_relation | relation:player:during:game | True | medium |
| cf21 | relation | goalie | near | net | spatial_proximity, visual_relation | relation:goalie:near:net | True | high |
| cf22 | relation | player | with | stick | association_relation, visual_relation | relation:player:with:stick | True | high |
| cf23 | relation | player | across | ice | spatial_path, visual_relation | relation:player:across:ice | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | river | river | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:river", "parents": []} |
| ent_m2 | object | rock | rocks | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:rock", "parents": []} |
| ent_m3 | object | area | area | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:area", "parents": []} |
| ent_m5 | object | leaf | leaves | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:leaf", "parents": []} |
| ent_m7 | object | shade | shades | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:shade", "parents": []} |
| ent_m10 | object | bank | banks | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:bank", "parents": []} |
| ent_m11 | object | tree | trees | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m12 | object | bush | bushes | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:bush", "parents": []} |
| ent_m13 | object | shoreline | shoreline | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:shoreline", "parents": []} |
| ent_m14 | object | water | water | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": []} |
| ent_m15 | object | rapid | rapids | object | raw_lemma | none |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:rapid", "parents": []} |
| ent_m17 | context | edge | edge | object | raw_lemma | semantic_type_fallback | scene_context | m17 | raw_mention |  |  |  | True | {"canonical": "entity:edge", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | rushes | rush | rush | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:rush", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m19 | line | line | line | raw_action | visual_action_fallback | visual_action |  | agent:m5->ent_m5; patient:m10->ent_m10 | {"canonical": "action:line", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m20 | moves | move | move | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m14->ent_m14 | {"canonical": "action:move", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce3 | m21 | creating | create | create | raw_action | visual_action_fallback | visual_action |  | agent:m14->ent_m14; patient:m15->ent_m15 | {"canonical": "action:create", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m22 | flows | flow | flow | raw_action | visual_action_fallback | visual_action |  | agent:m11->ent_m11 | {"canonical": "action:flow", "parents": ["action_parent:visual_action"]} |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | over | above | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e11 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | through | through | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | medium | e12 | False | False |  |  |
| cr2 | m5 | m7 | ent_m5 | ent_m7 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e13 | False | False |  |  |
| cr3 | m11 | m17 | ent_m11 | ent_m17 | past | past | raw_relation | raw_relation | visual_relation | medium | e14 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | river |  |  |  | entity_exists:river | True | low |
| cf1 | entity_exists | rock |  |  |  | entity_exists:rock | True | low |
| cf2 | entity_exists | area |  |  |  | entity_exists:area | True | low |
| cf3 | entity_exists | leaf |  |  |  | entity_exists:leaf | True | low |
| cf4 | entity_exists | shade |  |  |  | entity_exists:shade | True | low |
| cf5 | entity_exists | bank |  |  |  | entity_exists:bank | True | low |
| cf6 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf7 | entity_exists | bush |  |  |  | entity_exists:bush | True | low |
| cf8 | entity_exists | shoreline |  |  |  | entity_exists:shoreline | True | low |
| cf9 | entity_exists | water |  |  |  | entity_exists:water | True | low |
| cf10 | entity_exists | rapid |  |  |  | entity_exists:rapid | True | low |
| cf11 | entity_exists | edge |  |  | scene_context | entity_exists:edge | True | medium |
| cf12 | has_attribute | river | flow |  | state_attribute, visual_attribute | has_attribute:river:flow | True | medium |
| cf13 | has_attribute | area | forested |  | modifier_attribute, visual_attribute | has_attribute:area:forested | True | medium |
| cf14 | has_attribute | leaf | autumn |  | compound_modifier, visual_attribute | has_attribute:leaf:autumn | True | medium |
| cf15 | has_attribute | rapid | white |  | color_attribute, color, visual_attribute | has_attribute:rapid:white | True | high |
| cf16 | action_event | rush |  |  | visual_action | action_event:rush | True | low |
| cf17 | event_role | rush | agent | river |  | event_role:rush:agent:river | True | medium |
| cf18 | action_event | line |  |  | visual_action | action_event:line | True | low |
| cf19 | event_role | line | agent | leaf |  | event_role:line:agent:leaf | True | medium |
| cf20 | event_role | line | patient | bank |  | event_role:line:patient:bank | True | medium |
| cf21 | action_event | move |  |  | locomotion_action, visual_action | action_event:move | True | high |
| cf22 | event_role | move | agent | water |  | event_role:move:agent:water | True | medium |
| cf23 | action_event | create |  |  | visual_action | action_event:create | True | low |
| cf24 | event_role | create | agent | water |  | event_role:create:agent:water | True | medium |
| cf25 | event_role | create | patient | rapid |  | event_role:create:patient:rapid | True | medium |
| cf26 | action_event | flow |  |  | visual_action | action_event:flow | True | low |
| cf27 | event_role | flow | agent | tree |  | event_role:flow:agent:tree | True | medium |
| cf28 | relation | river | above | rock | spatial_vertical, visual_relation | relation:river:above:rock | True | high |
| cf29 | relation | river | through | area | spatial_path, visual_relation | relation:river:through:area | True | medium |
| cf30 | relation | leaf | in | shade | spatial_containment, visual_relation | relation:leaf:in:shade | True | high |
| cf31 | relation | tree | past | edge | visual_relation | relation:tree:past:edge | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e11 |  |  |  | {"canonical": "above", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e11", "raw_relation": "over", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | cactus | cacti | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:cactus", "parents": []} |
| ent_m2 | object | plant | plants | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:plant", "parents": []} |
| ent_m4 | object | greenhouse | greenhouse | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:greenhouse", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m6 | grow | grow | grow | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; agent:m2->ent_m2 | {"canonical": "action:grow", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | grow | agent | m0 | ent_m0 | medium | e3 | nsubj -> grow |  |  |
| ce0 | grow | agent | m2 | ent_m2 | medium | e4 | nsubj -> grow |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | inside | inside | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e5 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | cactus |  |  |  | entity_exists:cactus | True | low |
| cf1 | entity_exists | plant |  |  |  | entity_exists:plant | True | low |
| cf2 | entity_exists | greenhouse |  |  |  | entity_exists:greenhouse | True | low |
| cf3 | has_attribute | cactus | tall |  | size_attribute, height, visual_attribute | has_attribute:cactus:tall | True | high |
| cf4 | has_attribute | plant | spiky |  | shape_attribute, shape, visual_attribute | has_attribute:plant:spiky | True | medium |
| cf5 | has_attribute | greenhouse | glass |  | material_attribute, material, visual_attribute | has_attribute:greenhouse:glass | True | high |
| cf6 | action_event | grow |  |  | visual_action | action_event:grow | True | low |
| cf7 | event_role | grow | agent | cactus |  | event_role:grow:agent:cactus | True | medium |
| cf8 | event_role | grow | agent | plant |  | event_role:grow:agent:plant | True | medium |
| cf9 | relation | cactus | inside | greenhouse | spatial_containment, visual_relation | relation:cactus:inside:greenhouse | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | field | field | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |
| ent_m2 | object | wheat | wheat | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:wheat", "parents": []} |
| ent_m4 | object | line | line | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:line", "parents": []} |
| ent_m5 | object | tree | trees | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m7 | object | town | town | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:town", "parents": []} |
| ent_m9 | object | horizon | horizon | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:horizon", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | stretches | stretch | stretch | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stretch", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stretch | agent | m0 | ent_m0 | medium | e4 | nsubj -> stretches |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e5 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | toward | toward | raw_relation | raw_relation | visual_relation | medium | e6 | False | False |  |  |
| cr2 | m4 | m5 | ent_m4 | ent_m5 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf1 | entity_exists | wheat |  |  |  | entity_exists:wheat | True | low |
| cf2 | entity_exists | line |  |  |  | entity_exists:line | True | low |
| cf3 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf4 | entity_exists | town |  |  |  | entity_exists:town | True | low |
| cf5 | entity_exists | horizon |  |  |  | entity_exists:horizon | True | low |
| cf6 | has_attribute | field | harvest |  | state_attribute, visual_attribute | has_attribute:field:harvest | True | medium |
| cf7 | has_attribute | wheat | dry |  | state_attribute, clean_exact_overlap, state, visual_attribute | has_attribute:wheat:dry | True | medium |
| cf8 | has_attribute | tree | green |  | color_attribute, color, visual_attribute | has_attribute:tree:green | True | high |
| cf9 | has_attribute | town | distant |  | modifier_attribute, visual_attribute | has_attribute:town:distant | True | medium |
| cf10 | action_event | stretch |  |  | visual_action | action_event:stretch | True | low |
| cf11 | event_role | stretch | agent | field |  | event_role:stretch:agent:field | True | medium |
| cf12 | relation | field | of | wheat | part_relation, visual_relation | relation:field:of:wheat | True | medium |
| cf13 | relation | field | toward | line | visual_relation | relation:field:toward:line | True | medium |
| cf14 | relation | line | of | tree | part_relation, visual_relation | relation:line:of:tree | True | medium |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | glass | glass | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:glass", "parents": []} |
| ent_m2 | object | crucifix | crucifix | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:crucifix", "parents": []} |
| ent_m3 | object | altar | altar | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:altar", "parents": []} |
| ent_m4 | object | interior | interior | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:interior", "parents": []} |
| ent_m6 | object | pew | pews | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:pew", "parents": []} |
| ent_m8 | object | candle | candle | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:candle", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | glass |  |  |  | entity_exists:glass | True | low |
| cf1 | entity_exists | crucifix |  |  |  | entity_exists:crucifix | True | low |
| cf2 | entity_exists | altar |  |  |  | entity_exists:altar | True | low |
| cf3 | entity_exists | interior |  |  |  | entity_exists:interior | True | low |
| cf4 | entity_exists | pew |  |  |  | entity_exists:pew | True | low |
| cf5 | entity_exists | candle |  |  |  | entity_exists:candle | True | low |
| cf6 | has_attribute | glass | stained |  | texture_attribute, cleanliness, texture, visual_attribute | has_attribute:glass:stained | True | high |
| cf7 | has_attribute | interior | church |  | attribute, visual_attribute | has_attribute:interior:church | True | high |
| cf8 | has_attribute | pew | wooden |  | material_attribute, material, visual_attribute | has_attribute:pew:wooden | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | costume | costume | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:costume", "parents": []} |
| ent_m4 | object | ground | ground | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:ground", "parents": []} |
| ent_m5 | object | child | children | person | raw_lemma | stage9_seed:parent_seed | person, human | m5 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m7 | object | pikachu | Pikachu | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:pikachu", "parents": []} |
| ent_m8 | object | child | child | person | raw_lemma | stage9_seed:parent_seed | person, human | m8 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m10 | object | outfit | outfit | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:outfit", "parents": []} |
| ent_m13 | object | costume | costume | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:costume", "parents": []} |
| ent_m16 | object | stripe | stripes | object | raw_lemma | none |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:stripe", "parents": []} |
| ent_m18 | object | paved_surface | paved surface | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m18 | raw_mention |  |  |  | True | {"canonical": "entity:paved_surface", "parents": []} |
| ent_m19 | object | building | building | object | raw_lemma | none |  | m19 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m21 | context | outdoors | outdoors | object | raw_lemma | stage9_seed:parent_seed | scene_context | m21 | raw_mention |  |  |  | True | {"canonical": "entity:outdoors", "parents": ["entity_parent:scene_context"]} |
| ent_m26 | object | lamp | lamp | object | raw_lemma | none |  | m26 | raw_mention |  |  |  | True | {"canonical": "entity:lamp", "parents": []} |
| eref_m22 | contrastive_instance | child | another | person | raw_lemma | stage9_seed:parent_seed | person, human | m22 | stage9_reference | ent_m5 |  | 1 | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m22 | eref_m22 | m5 | ent_m5 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m23 | sits | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m24 | dressed | dress | wear | stage9_seed:synonym_seed | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m5->ent_m5 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce2 | m25 | wears | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m5->eref_m22; patient:m13->ent_m13 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m0 | ent_m0 | medium | e12 | nsubj -> sits |  |  |
| ce1 | wear | agent | m5 | ent_m5 | medium | e13 | inherited agent acl -> children |  |  |
| ce2 | wear | agent | m5 | eref_m22 | medium | e14 | nsubj -> wears; resolved another -> children |  |  |
| ce2 | wear | patient | m13 | ent_m13 | medium | e15 | dobj -> wears |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e18 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e19 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | next_to | next_to | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e20 | False | False |  |  |
| cr3 | m5 | m7 | ent_m5 | ent_m7 | as | as | raw_relation | raw_relation | visual_relation | medium | e21 | False | False |  |  |
| cr4 | m8 | m10 | ent_m8 | ent_m10 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e22 | False | False |  |  |
| cr5 | m13 | m16 | ent_m13 | ent_m16 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e23 | False | False |  |  |
| cr6 | m8 | m18 | ent_m8 | ent_m18 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e24 | False | False |  |  |
| cr7 | m18 | m19 | ent_m18 | ent_m19 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e25 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf1 | entity_exists | costume |  |  |  | entity_exists:costume | True | low |
| cf2 | entity_exists | ground |  |  |  | entity_exists:ground | True | low |
| cf3 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf4 | entity_exists | pikachu |  |  |  | entity_exists:pikachu | True | low |
| cf5 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf6 | entity_exists | outfit |  |  |  | entity_exists:outfit | True | low |
| cf7 | entity_exists | costume |  |  |  | entity_exists:costume | True | low |
| cf8 | entity_exists | stripe |  |  |  | entity_exists:stripe | True | low |
| cf9 | entity_exists | paved_surface |  |  |  | entity_exists:paved_surface | True | high |
| cf10 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf11 | entity_exists | outdoors |  |  | scene_context | entity_exists:outdoors | True | high |
| cf12 | entity_exists | lamp |  |  |  | entity_exists:lamp | True | low |
| cf13 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf14 | has_attribute | costume | white |  | color_attribute, color, visual_attribute | has_attribute:costume:white | True | high |
| cf15 | has_attribute | costume | stormtrooper |  | compound_modifier, visual_attribute | has_attribute:costume:stormtrooper | True | medium |
| cf16 | has_quantity | child | two |  | exact_quantity, quantity | has_quantity:child:two | True | high |
| cf17 | has_quantity | child | one |  | exact_quantity, quantity | has_quantity:child:one | True | high |
| cf18 | has_attribute | outfit | yellow |  | color_attribute, color, visual_attribute | has_attribute:outfit:yellow | True | high |
| cf19 | has_attribute | outfit | pikachu |  | compound_modifier, visual_attribute | has_attribute:outfit:pikachu | True | medium |
| cf20 | has_attribute | costume | yellow |  | color_attribute, color, visual_attribute | has_attribute:costume:yellow | True | high |
| cf21 | has_attribute | costume | hooded |  | modifier_attribute, visual_attribute | has_attribute:costume:hooded | True | medium |
| cf22 | has_attribute | stripe | red |  | color_attribute, color, visual_attribute | has_attribute:stripe:red | True | high |
| cf23 | has_attribute | building | glass |  | material_attribute, material, visual_attribute | has_attribute:building:glass | True | high |
| cf24 | has_attribute | lamp | yellow |  | color_attribute, color, visual_attribute | has_attribute:lamp:yellow | True | high |
| cf25 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf26 | event_role | sit | agent | person |  | event_role:sit:agent:person | True | medium |
| cf27 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf28 | event_role | wear | agent | child |  | event_role:wear:agent:child | True | medium |
| cf29 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf30 | event_role | wear | agent | child |  | event_role:wear:agent:child | True | medium |
| cf31 | event_role | wear | patient | costume |  | event_role:wear:patient:costume | True | medium |
| cf32 | relation | person | in | costume | spatial_containment, visual_relation | relation:person:in:costume | True | high |
| cf33 | relation | person | on | ground | spatial_support, visual_relation | relation:person:on:ground | True | high |
| cf34 | relation | person | next_to | child | spatial_proximity, visual_relation | relation:person:next_to:child | True | high |
| cf35 | relation | child | as | pikachu | visual_relation | relation:child:as:pikachu | True | medium |
| cf36 | relation | child | in | outfit | spatial_containment, visual_relation | relation:child:in:outfit | True | high |
| cf37 | relation | costume | with | stripe | association_relation, visual_relation | relation:costume:with:stripe | True | high |
| cf38 | relation | child | on | paved_surface | spatial_support, visual_relation | relation:child:on:paved_surface | True | high |
| cf39 | relation | paved_surface | near | building | spatial_proximity, visual_relation | relation:paved_surface:near:building | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| action_lexical_canonicalized | m24 |  |  |  |  | {"action_mention_id": "m24", "canonical": "wear", "kind": "action_lexical_canonicalized", "raw_canonical_action": "dress", "source": "stage9_seed:synonym_seed"} |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hockey_player | hockey players | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:hockey_player", "parents": []} |
| ent_m2 | object | ice | ice | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:ice", "parents": []} |
| ent_m3 | object | jersey | jersey | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m3 | raw_mention |  |  |  | True | {"canonical": "entity:jersey", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m5 | object | number | number | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:number", "parents": []} |
| ent_m6 | object | goal | goal | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:goal", "parents": []} |
| eref_m7 | instance | hockey_player | one | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m7 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:hockey_player", "parents": []} |
| eref_m8 | contrastive_instance | hockey_player | another | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m8 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:hockey_player", "parents": []} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m7 | eref_m7 | m0 | ent_m0 | high |  |
| refers_to | m8 | eref_m8 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | skate | skate | skate | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:skate", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | skate | agent | m0 | ent_m0 | medium | e4 | nsubj -> skate |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e5 | False | False |  |  |
| cr1 | m0 | m3 | eref_m7 | ent_m3 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e6 | False | False |  |  |
| cr2 | m3 | m5 | ent_m3 | ent_m5 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e7 | False | False |  |  |
| cr3 | m0 | m6 | eref_m8 | ent_m6 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | hockey_player |  |  |  | entity_exists:hockey_player | True | high |
| cf1 | entity_exists | ice |  |  |  | entity_exists:ice | True | low |
| cf2 | entity_exists | jersey |  |  | clothing, wearable | entity_exists:jersey | True | high |
| cf3 | entity_exists | number |  |  |  | entity_exists:number | True | low |
| cf4 | entity_exists | goal |  |  |  | entity_exists:goal | True | low |
| cf5 | entity_exists | hockey_player |  |  |  | entity_exists:hockey_player | True | high |
| cf6 | entity_exists | hockey_player |  |  |  | entity_exists:hockey_player | True | high |
| cf7 | has_quantity | hockey_player | two |  | exact_quantity, quantity | has_quantity:hockey_player:two | True | high |
| cf8 | has_attribute | jersey | white |  | color_attribute, color, visual_attribute | has_attribute:jersey:white | True | high |
| cf9 | action_event | skate |  |  | locomotion_action, visual_action | action_event:skate | True | high |
| cf10 | event_role | skate | agent | hockey_player |  | event_role:skate:agent:hockey_player | True | medium |
| cf11 | relation | hockey_player | on | ice | spatial_support, visual_relation | relation:hockey_player:on:ice | True | high |
| cf12 | relation | hockey_player | in | jersey | spatial_containment, visual_relation | relation:hockey_player:in:jersey | True | high |
| cf13 | relation | jersey | with | number | association_relation, visual_relation | relation:jersey:with:number | True | high |
| cf14 | relation | hockey_player | near | goal | spatial_proximity, visual_relation | relation:hockey_player:near:goal | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | skirt | skirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:skirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | blazer | blazer | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m3 | raw_mention |  |  |  | True | {"canonical": "entity:blazer", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m5 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m5 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m6 | object | suit | suit | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m6 | raw_mention |  |  |  | True | {"canonical": "entity:suit", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m9 | object | face_mask | face masks | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:face_mask", "parents": []} |
| ent_m10 | object | hall | hall | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:hall", "parents": []} |
| ent_m13 | object | attendee | attendees | person | raw_lemma | stage9_seed:parent_seed | person, human | m13 | raw_mention |  |  |  | True | {"canonical": "entity:attendee", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m16 | object | mask | masks | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m16 | raw_mention |  |  |  | True | {"canonical": "entity:mask", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m17 | object | paper | papers | document | raw_lemma | stage9_seed:parent_seed | document, text_carrier, artifact | m17 | raw_mention |  |  |  | True | {"canonical": "entity:paper", "parents": ["entity_parent:document", "entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m18 | group | skirt_and_blazer | a striped skirt and black blazer | group | raw_lemma | none |  | m18 | raw_mention |  |  |  | True | {"canonical": "entity:skirt_and_blazer", "parents": []} |
| eref_m19 | group | skirt_and_blazer | both | person | raw_lemma | semantic_type_fallback | person, human | m19 | stage9_reference_group_repair | ent_m18 |  | 2 | True | {"canonical": "entity:skirt_and_blazer", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m19 | eref_m19 | m18 | ent_m18 | medium |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m20 | walks | walk | walk | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:walk", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m21 | wearing | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m18->eref_m19; patient:m9->ent_m9 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce2 | m22 | wearing | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m0->ent_m0; patient:m16->ent_m16 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce3 | m23 | holding | hold | hold | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action |  | patient:m17->ent_m17 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce4 | m24 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e16 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e17 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | beside | next_to | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e18 | False | False |  |  |
| cr3 | m5 | m6 | ent_m5 | ent_m6 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e19 | False | False |  |  |
| cr4 | m0 | m10 | ent_m0 | ent_m10 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e20 | False | False |  |  |
| cr5 | m10 | m13 | ent_m10 | ent_m13 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e21 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | skirt |  |  | clothing, wearable | entity_exists:skirt | True | high |
| cf2 | entity_exists | blazer |  |  | clothing, wearable | entity_exists:blazer | True | high |
| cf3 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf4 | entity_exists | suit |  |  | clothing, wearable | entity_exists:suit | True | high |
| cf5 | entity_exists | face_mask |  |  |  | entity_exists:face_mask | True | high |
| cf6 | entity_exists | hall |  |  |  | entity_exists:hall | True | low |
| cf7 | entity_exists | attendee |  |  | person, human | entity_exists:attendee | True | high |
| cf8 | entity_exists | mask |  |  | clothing, wearable | entity_exists:mask | True | medium |
| cf9 | entity_exists | paper |  |  | document, text_carrier, artifact | entity_exists:paper | True | high |
| cf10 | entity_exists | skirt_and_blazer |  |  |  | entity_exists:skirt_and_blazer | True | low |
| cf11 | entity_exists | skirt_and_blazer |  |  | person, human | entity_exists:skirt_and_blazer | True | medium |
| cf12 | has_attribute | skirt | striped |  | pattern_attribute, clean_exact_overlap, pattern, pattern_marking, texture, visual_attribute | has_attribute:skirt:striped | True | medium |
| cf13 | has_attribute | blazer | black |  | color_attribute, color, visual_attribute | has_attribute:blazer:black | True | high |
| cf14 | has_attribute | suit | blue |  | color_attribute, color, visual_attribute | has_attribute:suit:blue | True | high |
| cf15 | has_attribute | hall | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:hall:large | True | high |
| cf16 | has_attribute | hall | indoor |  | modifier_attribute, visual_attribute | has_attribute:hall:indoor | True | medium |
| cf17 | has_attribute | attendee | seat |  | state_attribute, visual_attribute | has_attribute:attendee:seat | True | medium |
| cf18 | action_event | walk |  |  | locomotion_action, visual_action | action_event:walk | True | high |
| cf19 | event_role | walk | agent | woman |  | event_role:walk:agent:woman | True | medium |
| cf20 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf21 | event_role | wear | agent | skirt_and_blazer |  | event_role:wear:agent:skirt_and_blazer | True | medium |
| cf22 | event_role | wear | patient | face_mask |  | event_role:wear:patient:face_mask | True | medium |
| cf23 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf24 | event_role | wear | agent | woman |  | event_role:wear:agent:woman | True | medium |
| cf25 | event_role | wear | patient | mask |  | event_role:wear:patient:mask | True | medium |
| cf26 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf27 | event_role | hold | patient | paper |  | event_role:hold:patient:paper | True | medium |
| cf28 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf29 | event_role | stand | agent | woman |  | event_role:stand:agent:woman | True | medium |
| cf30 | relation | woman | in | skirt | spatial_containment, visual_relation | relation:woman:in:skirt | True | high |
| cf31 | relation | woman | in | blazer | spatial_containment, visual_relation | relation:woman:in:blazer | True | high |
| cf32 | relation | woman | next_to | man | spatial_proximity, visual_relation | relation:woman:next_to:man | True | high |
| cf33 | relation | man | in | suit | spatial_containment, visual_relation | relation:man:in:suit | True | high |
| cf34 | relation | woman | in | hall | spatial_containment, visual_relation | relation:woman:in:hall | True | high |
| cf35 | relation | hall | with | attendee | association_relation, visual_relation | relation:hall:with:attendee | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e18 |  |  |  | {"canonical": "next_to", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e18", "raw_relation": "beside", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | flower | flower | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:flower", "parents": []} |
| ent_m3 | object | ground | ground | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:ground", "parents": []} |
| ent_m4 | object | leaf | leaves | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:leaf", "parents": []} |
| ent_m6 | object | stem | stems | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:stem", "parents": []} |
| ent_m8 | object | petal | petals | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:petal", "parents": []} |
| ent_m9 | object | leaf | leaf | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:leaf", "parents": []} |
| ent_m10 | object | bloom | bloom | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:bloom", "parents": []} |
| ent_m11 | context | setting | setting | object | raw_lemma | stage9_seed:parent_seed | scene_context | m11 | raw_mention |  |  |  | True | {"canonical": "entity:setting", "parents": ["entity_parent:scene_context"]} |
| ent_m12 | object | soil | soil | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:soil", "parents": []} |
| ent_m13 | object | foliage | foliage | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:foliage", "parents": []} |
| ent_m15 | context | outdoors | outdoors | object | raw_lemma | stage9_seed:parent_seed | scene_context | m15 | raw_mention |  |  |  | True | {"canonical": "entity:outdoors", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | grows | grow | grow | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:grow", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m17 | appears | appear | appear | raw_action | visual_action_fallback | visual_action |  | agent:m11->ent_m11 | {"canonical": "action:appear", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m18 | covered | cover | cover | raw_action | visual_action_fallback | visual_action |  | agent:m12->ent_m12 | {"canonical": "action:cover", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | grow | agent | m0 | ent_m0 | medium | e7 | nsubj -> grows |  |  |
| ce1 | appear | agent | m11 | ent_m11 | medium | e8 | nsubj -> appears |  |  |
| ce2 | cover | agent | m12 | ent_m12 | medium | e9 | inherited agent acl -> soil |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e10 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | among | among | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_region, visual_relation | medium | e11 | False | False |  |  |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | among | among | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_region, visual_relation | medium | e12 | False | False |  |  |
| cr3 | m11 | m12 | ent_m11 | ent_m12 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e13 | False | False |  |  |
| cr4 | m12 | m13 | ent_m12 | ent_m13 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | flower |  |  |  | entity_exists:flower | True | low |
| cf1 | entity_exists | ground |  |  |  | entity_exists:ground | True | low |
| cf2 | entity_exists | leaf |  |  |  | entity_exists:leaf | True | low |
| cf3 | entity_exists | stem |  |  |  | entity_exists:stem | True | low |
| cf4 | entity_exists | petal |  |  |  | entity_exists:petal | True | low |
| cf5 | entity_exists | leaf |  |  |  | entity_exists:leaf | True | low |
| cf6 | entity_exists | bloom |  |  |  | entity_exists:bloom | True | low |
| cf7 | entity_exists | setting |  |  | scene_context | entity_exists:setting | True | high |
| cf8 | entity_exists | soil |  |  |  | entity_exists:soil | True | low |
| cf9 | entity_exists | foliage |  |  |  | entity_exists:foliage | True | low |
| cf10 | entity_exists | outdoors |  |  | scene_context | entity_exists:outdoors | True | high |
| cf11 | has_attribute | flower | purple |  | color_attribute, color, visual_attribute | has_attribute:flower:purple | True | high |
| cf12 | has_attribute | flower | white |  | color_attribute, color, visual_attribute | has_attribute:flower:white | True | high |
| cf13 | has_attribute | leaf | brown |  | color_attribute, color, visual_attribute | has_attribute:leaf:brown | True | high |
| cf14 | has_attribute | stem | green |  | color_attribute, color, visual_attribute | has_attribute:stem:green | True | high |
| cf15 | has_attribute | foliage | fallen |  | modifier_attribute, visual_attribute | has_attribute:foliage:fallen | True | medium |
| cf16 | action_event | grow |  |  | visual_action | action_event:grow | True | low |
| cf17 | event_role | grow | agent | flower |  | event_role:grow:agent:flower | True | medium |
| cf18 | action_event | appear |  |  | visual_action | action_event:appear | True | low |
| cf19 | event_role | appear | agent | setting |  | event_role:appear:agent:setting | True | medium |
| cf20 | action_event | cover |  |  | visual_action | action_event:cover | True | low |
| cf21 | event_role | cover | agent | soil |  | event_role:cover:agent:soil | True | medium |
| cf22 | relation | flower | in | ground | spatial_containment, visual_relation | relation:flower:in:ground | True | high |
| cf23 | relation | flower | among | leaf | spatial_region, visual_relation | relation:flower:among:leaf | True | medium |
| cf24 | relation | flower | among | stem | spatial_region, visual_relation | relation:flower:among:stem | True | medium |
| cf25 | relation | setting | on | soil | spatial_support, visual_relation | relation:setting:on:soil | True | high |
| cf26 | relation | soil | with | foliage | association_relation, visual_relation | relation:soil:with:foliage | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | spiderweb | spiderweb | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:spiderweb", "parents": []} |
| ent_m2 | object | tree_branch | tree branch | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:tree_branch", "parents": []} |
| ent_m3 | context | setting | setting | object | raw_lemma | stage9_seed:parent_seed | scene_context | m3 | raw_mention |  |  |  | True | {"canonical": "entity:setting", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | spiderweb |  |  |  | entity_exists:spiderweb | True | low |
| cf1 | entity_exists | tree_branch |  |  |  | entity_exists:tree_branch | True | high |
| cf2 | entity_exists | setting |  |  | scene_context | entity_exists:setting | True | high |
| cf3 | has_attribute | spiderweb | dewy |  | attribute, visual_attribute | has_attribute:spiderweb:dewy | True | high |
| cf4 | has_attribute | setting | natural |  | attribute, visual_attribute | has_attribute:setting:natural | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | street | street | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:street", "parents": []} |
| ent_m2 | object | building | building | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m4 | object | window | windows | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:window", "parents": []} |
| ent_m6 | object | traffic_light | traffic light | object | coco_object\|lvis_object\|openimages_boxable\|visual_genome_object_synset\|wordnet_noun_mwe | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:traffic_light", "parents": []} |
| ent_m7 | object | moon | moon | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:moon", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | street |  |  |  | entity_exists:street | True | low |
| cf1 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf2 | entity_exists | window |  |  |  | entity_exists:window | True | low |
| cf3 | entity_exists | traffic_light |  |  |  | entity_exists:traffic_light | True | high |
| cf4 | entity_exists | moon |  |  |  | entity_exists:moon | True | low |
| cf5 | has_attribute | street | night |  | attribute, visual_attribute | has_attribute:street:night | True | high |
| cf6 | has_attribute | building | brick |  | material_attribute, material, visual_attribute | has_attribute:building:brick | True | high |
| cf7 | has_attribute | window | light |  | state_attribute, visual_attribute | has_attribute:window:light | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | men | person | stage9_seed:synonym_seed | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | path | path | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:path", "parents": []} |
| ent_m4 | object | tree | trees | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m5 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m5 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m7 | context | foreground | foreground | object | raw_lemma | stage9_seed:parent_seed | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:foreground", "parents": ["entity_parent:scene_context"]} |
| ent_m8 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m8 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m10 | context | right | right | object | raw_lemma | semantic_type_fallback | scene_context | m10 | raw_mention |  |  |  | True | {"canonical": "entity:right", "parents": ["entity_parent:scene_context"]} |
| eref_m11 | contrastive_instance | man | another | person | raw_lemma | stage9_seed:parent_seed | person, human | m11 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m11 | eref_m11 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | run | run | run | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:run", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m13 | surrounded | surround | surround | raw_action | visual_action_fallback | visual_action |  | agent:m2->ent_m2 | {"canonical": "action:surround", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m14 | runs | run | run | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->eref_m11 | {"canonical": "action:run", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | run | agent | m0 | ent_m0 | medium | e6 | nsubj -> run |  |  |
| ce1 | surround | agent | m2 | ent_m2 | medium | e7 | inherited agent acl -> path |  |  |
| ce2 | run | agent | m0 | eref_m11 | medium | e8 | nsubj -> runs; resolved another -> men |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | along | along | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | medium | e9 | False | False |  |  |
| cr1 | m2 | m4 | ent_m2 | ent_m4 | by | by | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | medium | e10 | False | False |  |  |
| cr2 | m0 | m8 | eref_m11 | ent_m8 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e11 | False | False |  |  |
| cr3 | m8 | m0 | ent_m8 | ent_m0 | behind; repaired_self_edge_source from men | behind | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | medium | e12 | False | False |  |  |
| cr4 | m0 | m10 | ent_m0 | ent_m10 | to | to | raw_relation | raw_relation | visual_relation | medium | e13 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | path |  |  |  | entity_exists:path | True | low |
| cf2 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf3 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf4 | entity_exists | foreground |  |  | scene_context | entity_exists:foreground | True | high |
| cf5 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf6 | entity_exists | right |  |  | scene_context | entity_exists:right | True | medium |
| cf7 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf8 | has_quantity | man | several |  | approximate_quantity, quantity | has_quantity:man:several | True | medium |
| cf9 | has_attribute | path | dirt |  | material_attribute, cleanliness, material, visual_attribute | has_attribute:path:dirt | True | medium |
| cf10 | has_attribute | shirt | black |  | color_attribute, color, visual_attribute | has_attribute:shirt:black | True | high |
| cf11 | has_attribute | shirt | red |  | color_attribute, color, visual_attribute | has_attribute:shirt:red | True | high |
| cf12 | action_event | run |  |  | locomotion_action, visual_action | action_event:run | True | high |
| cf13 | event_role | run | agent | man |  | event_role:run:agent:man | True | medium |
| cf14 | action_event | surround |  |  | visual_action | action_event:surround | True | low |
| cf15 | event_role | surround | agent | path |  | event_role:surround:agent:path | True | medium |
| cf16 | action_event | run |  |  | locomotion_action, visual_action | action_event:run | True | high |
| cf17 | event_role | run | agent | man |  | event_role:run:agent:man | True | medium |
| cf18 | relation | man | along | path | spatial_path, visual_relation | relation:man:along:path | True | medium |
| cf19 | relation | path | by | tree | spatial_proximity, visual_relation | relation:path:by:tree | True | medium |
| cf20 | relation | man | in | shirt | spatial_containment, visual_relation | relation:man:in:shirt | True | high |
| cf21 | relation | shirt | behind | man | spatial_depth, visual_relation | relation:shirt:behind:man | True | medium |
| cf22 | relation | man | to | right | visual_relation | relation:man:to:right | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e12 |  |  |  | {"canonical": "behind", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e12", "raw_relation": "behind; repaired_self_edge_source from men", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sofa | couch | object | stage9_seed:synonym_seed | stage9_seed:parent_seed | furniture, artifact | m0 | raw_mention |  |  |  | True | {"canonical": "entity:sofa", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m2 | object | floor | floor | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:floor", "parents": []} |
| ent_m4 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m4 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m5 | object | child | child | person | raw_lemma | stage9_seed:parent_seed | person, human | m5 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m6 | object | living_room | living room | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:living_room", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | sofa |  |  | furniture, artifact | entity_exists:sofa | True | high |
| cf1 | entity_exists | floor |  |  |  | entity_exists:floor | True | low |
| cf2 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf3 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf4 | entity_exists | living_room |  |  |  | entity_exists:living_room | True | high |
| cf5 | has_attribute | sofa | brown |  | color_attribute, color, visual_attribute | has_attribute:sofa:brown | True | high |
| cf6 | has_attribute | floor | tiled |  | material_attribute, material, pattern, visual_attribute | has_attribute:floor:tiled | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | staircase | staircase | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:staircase", "parents": []} |
| ent_m2 | object | railing | railings | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:railing", "parents": []} |
| ent_m5 | object | pile | piles | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:pile", "parents": []} |
| ent_m7 | context | side | sides | object | raw_lemma | semantic_type_fallback | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:side", "parents": ["entity_parent:scene_context"]} |
| ent_m8 | object | tree | trees | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m10 | object | step | steps | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:step", "parents": []} |
| ent_m11 | object | sky | sky | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m13 | object | building | building | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m14 | object | shutter | shutters | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:shutter", "parents": []} |
| ent_m15 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m15 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | leads | lead | lead | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:lead", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m17 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m8->ent_m8 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | lead | agent | m0 | ent_m0 | medium | e7 | nsubj -> leads |  |  |
| ce1 | stand | agent | m8 | ent_m8 | medium | e8 | nsubj -> stand |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e9 | False | False |  |  |
| cr1 | m5 | m7 | ent_m5 | ent_m7 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e10 | False | False |  |  |
| cr2 | m8 | m10 | ent_m8 | ent_m10 | beside | next_to | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e11 | False | False |  |  |
| cr3 | m8 | m11 | ent_m8 | ent_m11 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e12 | False | False |  |  |
| cr4 | m13 | m14 | ent_m13 | ent_m14 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr5 | m13 | m15 | ent_m13 | ent_m15 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e14 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | staircase |  |  |  | entity_exists:staircase | True | low |
| cf1 | entity_exists | railing |  |  |  | entity_exists:railing | True | low |
| cf2 | entity_exists | pile |  |  |  | entity_exists:pile | True | low |
| cf3 | entity_exists | side |  |  | scene_context | entity_exists:side | True | medium |
| cf4 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf5 | entity_exists | step |  |  |  | entity_exists:step | True | low |
| cf6 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf7 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf8 | entity_exists | shutter |  |  |  | entity_exists:shutter | True | low |
| cf9 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf10 | has_attribute | staircase | snow-covered |  | modifier_attribute, visual_attribute | has_attribute:staircase:snow-covered | True | medium |
| cf11 | has_attribute | railing | rusted |  | modifier_attribute, visual_attribute | has_attribute:railing:rusted | True | medium |
| cf12 | has_attribute | railing | metal |  | material_attribute, material, non_textile_material_type, visual_attribute | has_attribute:railing:metal | True | high |
| cf13 | has_attribute | pile | snow |  | color_attribute, color, visual_attribute | has_attribute:pile:snow | True | medium |
| cf14 | has_attribute | tree | bare |  | visual_attribute | has_attribute:tree:bare | True | medium |
| cf15 | has_attribute | sky | cloudy |  | weather_attribute, weather, visual_attribute | has_attribute:sky:cloudy | True | medium |
| cf16 | action_event | lead |  |  | visual_action | action_event:lead | True | low |
| cf17 | event_role | lead | agent | staircase |  | event_role:lead:agent:staircase | True | medium |
| cf18 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf19 | event_role | stand | agent | tree |  | event_role:stand:agent:tree | True | medium |
| cf20 | relation | staircase | with | railing | association_relation, visual_relation | relation:staircase:with:railing | True | high |
| cf21 | relation | pile | on | side | spatial_support, visual_relation | relation:pile:on:side | True | high |
| cf22 | relation | tree | next_to | step | spatial_proximity, visual_relation | relation:tree:next_to:step | True | high |
| cf23 | relation | tree | under | sky | spatial_vertical, visual_relation | relation:tree:under:sky | True | high |
| cf24 | relation | building | with | shutter | association_relation, visual_relation | relation:building:with:shutter | True | high |
| cf25 | relation | building | in | background | spatial_containment, visual_relation | relation:building:in:background | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e11 |  |  |  | {"canonical": "next_to", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e11", "raw_relation": "beside", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | shepherd | Shepherd | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:shepherd", "parents": []} |
| ent_m2 | object | collar | collar | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:collar", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m4 | object | paved_surface | paved surface | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:paved_surface", "parents": []} |
| ent_m5 | object | dog | dogs | animal | raw_lemma | stage9_seed:parent_seed | animal, living_thing | m5 | raw_mention |  |  |  | True | {"canonical": "entity:dog", "parents": ["entity_parent:animal", "entity_parent:living_thing"]} |
| ent_m8 | object | person | person | person | raw_lemma | stage9_seed:parent_seed | person, human | m8 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m9 | object | jean | jeans | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:jean", "parents": []} |
| ent_m10 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m10 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m11 | object | tunnel | tunnel | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:tunnel", "parents": []} |
| eref_m14 | instance | dog | one | animal | raw_lemma | stage9_seed:parent_seed | animal, living_thing | m14 | stage9_reference | ent_m5 |  | 1 | True | {"canonical": "entity:dog", "parents": ["entity_parent:animal", "entity_parent:living_thing"]} |
| eref_m15 | complement_subset | dog | others | animal | raw_lemma | stage9_seed:parent_seed | animal, living_thing | m15 | stage9_reference | ent_m5 |  | many | True | {"canonical": "entity:dog", "parents": ["entity_parent:animal", "entity_parent:living_thing"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m14 | eref_m14 | m5 | ent_m5 | high |  |
| refers_to | m15 | eref_m15 | m5 | ent_m5 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | walks | walk | walk | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:walk", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m17 | including | include | include | raw_action | visual_action_fallback | visual_action |  | agent:m5->ent_m5; patient:m5->eref_m14; patient:m5->eref_m15 | {"canonical": "action:include", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m18 | lying | lie | lie | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m5->eref_m14 | {"canonical": "action:lie", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce3 | m19 | standing | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m5->eref_m15 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce4 | m20 | moving | move | move | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m5->eref_m15 | {"canonical": "action:move", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce5 | m21 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m8->ent_m8 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e15 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e16 | False | False |  |  |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e17 | False | False |  |  |
| cr3 | m8 | m10 | ent_m8 | ent_m10 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e18 | False | False |  |  |
| cr4 | m8 | m11 | ent_m8 | ent_m11 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e19 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | shepherd |  |  |  | entity_exists:shepherd | True | low |
| cf1 | entity_exists | collar |  |  | clothing, wearable | entity_exists:collar | True | medium |
| cf2 | entity_exists | paved_surface |  |  |  | entity_exists:paved_surface | True | high |
| cf3 | entity_exists | dog |  |  | animal, living_thing | entity_exists:dog | True | high |
| cf4 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf5 | entity_exists | jean |  |  |  | entity_exists:jean | True | low |
| cf6 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf7 | entity_exists | tunnel |  |  |  | entity_exists:tunnel | True | low |
| cf8 | entity_exists | dog |  |  | animal, living_thing | entity_exists:dog | True | high |
| cf9 | entity_exists | dog |  |  | animal, living_thing | entity_exists:dog | True | high |
| cf10 | has_attribute | shepherd | german |  | compound_modifier, visual_attribute | has_attribute:shepherd:german | True | medium |
| cf11 | has_attribute | collar | red |  | color_attribute, color, visual_attribute | has_attribute:collar:red | True | high |
| cf12 | has_quantity | dog | several |  | approximate_quantity, quantity | has_quantity:dog:several | True | medium |
| cf13 | has_attribute | dog | other |  | modifier_attribute, visual_attribute | has_attribute:dog:other | True | medium |
| cf14 | has_attribute | tunnel | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:tunnel:large | True | high |
| cf15 | has_attribute | tunnel | black |  | color_attribute, color, visual_attribute | has_attribute:tunnel:black | True | high |
| cf16 | action_event | walk |  |  | locomotion_action, visual_action | action_event:walk | True | high |
| cf17 | event_role | walk | agent | shepherd |  | event_role:walk:agent:shepherd | True | medium |
| cf18 | action_event | include |  |  | visual_action | action_event:include | True | low |
| cf19 | event_role | include | agent | dog |  | event_role:include:agent:dog | True | medium |
| cf20 | event_role | include | patient | dog |  | event_role:include:patient:dog | True | medium |
| cf21 | event_role | include | patient | dog |  | event_role:include:patient:dog | True | medium |
| cf22 | action_event | lie |  |  | body_pose_action, visual_action | action_event:lie | True | high |
| cf23 | event_role | lie | agent | dog |  | event_role:lie:agent:dog | True | medium |
| cf24 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf25 | event_role | stand | agent | dog |  | event_role:stand:agent:dog | True | medium |
| cf26 | action_event | move |  |  | locomotion_action, visual_action | action_event:move | True | high |
| cf27 | event_role | move | agent | dog |  | event_role:move:agent:dog | True | medium |
| cf28 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf29 | event_role | stand | agent | person |  | event_role:stand:agent:person | True | medium |
| cf30 | relation | shepherd | with | collar | association_relation, visual_relation | relation:shepherd:with:collar | True | high |
| cf31 | relation | shepherd | on | paved_surface | spatial_support, visual_relation | relation:shepherd:on:paved_surface | True | high |
| cf32 | relation | person | in | jean | spatial_containment, visual_relation | relation:person:in:jean | True | high |
| cf33 | relation | person | in | background | spatial_containment, visual_relation | relation:person:in:background | True | high |
| cf34 | relation | person | near | tunnel | spatial_proximity, visual_relation | relation:person:near:tunnel | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | player | players | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:player", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m4 | object | pool | pool | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:pool", "parents": []} |
| ent_m5 | object | cap | cap | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m5 | raw_mention |  |  |  | True | {"canonical": "entity:cap", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| eref_m7 | instance | player | one | person | raw_lemma | stage9_seed:parent_seed | person, human | m7 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:player", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m7 | eref_m7 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | swim | swim | swim | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:swim", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m9 | wearing | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m0->eref_m7; patient:m5->ent_m5 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce2 | m10 | marked | mark | mark | raw_action | visual_action_fallback | visual_action |  | agent:m5->ent_m5 | {"canonical": "action:mark", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | swim | agent | m0 | ent_m0 | medium | e5 | nsubj -> swim |  |  |
| ce1 | wear | agent | m0 | eref_m7 | medium | e6 | inherited agent acl -> one |  |  |
| ce1 | wear | patient | m5 | ent_m5 | medium | e7 | dobj -> wearing |  |  |
| ce2 | mark | agent | m5 | ent_m5 | medium | e8 | inherited agent acl -> cap |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | player |  |  | person, human | entity_exists:player | True | high |
| cf1 | entity_exists | pool |  |  |  | entity_exists:pool | True | low |
| cf2 | entity_exists | cap |  |  | clothing, wearable | entity_exists:cap | True | high |
| cf3 | entity_exists | player |  |  | person, human | entity_exists:player | True | high |
| cf4 | has_quantity | player | three |  | exact_quantity, quantity | has_quantity:player:three | True | high |
| cf5 | has_attribute | player | water |  | material_attribute, material, visual_attribute | has_attribute:player:water | True | medium |
| cf6 | has_attribute | player | polo |  | compound_modifier, visual_attribute | has_attribute:player:polo | True | medium |
| cf7 | has_attribute | cap | black |  | color_attribute, color, visual_attribute | has_attribute:cap:black | True | high |
| cf8 | action_event | swim |  |  | locomotion_action, visual_action | action_event:swim | True | high |
| cf9 | event_role | swim | agent | player |  | event_role:swim:agent:player | True | medium |
| cf10 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf11 | event_role | wear | agent | player |  | event_role:wear:agent:player | True | medium |
| cf12 | event_role | wear | patient | cap |  | event_role:wear:patient:cap | True | medium |
| cf13 | action_event | mark |  |  | visual_action | action_event:mark | True | low |
| cf14 | event_role | mark | agent | cap |  | event_role:mark:agent:cap | True | medium |
| cf15 | relation | player | in | pool | spatial_containment, visual_relation | relation:player:in:pool | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | diagram | diagram | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:diagram", "parents": []} |
| ent_m1 | object | view | views | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:view", "parents": []} |
| ent_m3 | object | aircraft | aircraft | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:aircraft", "parents": []} |
| ent_m5 | object | part | parts | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:part", "parents": []} |
| ent_m7 | object | arrow | arrows | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:arrow", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | shows | show | show | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m1->ent_m1 | {"canonical": "action:show", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | m0 | ent_m0 | medium | e4 | nsubj -> shows |  |  |
| ce0 | show | patient | m1 | ent_m1 | medium | e5 | dobj -> shows |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m3 | ent_m1 | ent_m3 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e6 | False | False |  |  |
| cr1 | m1 | m5 | ent_m1 | ent_m5 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e7 | False | False |  |  |
| cr2 | m1 | m7 | ent_m1 | ent_m7 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | diagram |  |  |  | entity_exists:diagram | True | low |
| cf1 | entity_exists | view |  |  |  | entity_exists:view | True | low |
| cf2 | entity_exists | aircraft |  |  |  | entity_exists:aircraft | True | low |
| cf3 | entity_exists | part |  |  |  | entity_exists:part | True | low |
| cf4 | entity_exists | arrow |  |  |  | entity_exists:arrow | True | low |
| cf5 | has_attribute | view | different |  | modifier_attribute, visual_attribute | has_attribute:view:different | True | medium |
| cf6 | has_attribute | aircraft | futuristic |  | modifier_attribute, visual_attribute | has_attribute:aircraft:futuristic | True | medium |
| cf7 | has_attribute | part | label |  | state_attribute, visual_attribute | has_attribute:part:label | True | medium |
| cf8 | has_attribute | arrow | directional |  | modifier_attribute, visual_attribute | has_attribute:arrow:directional | True | medium |
| cf9 | action_event | show |  |  | visual_action | action_event:show | True | low |
| cf10 | event_role | show | agent | diagram |  | event_role:show:agent:diagram | True | medium |
| cf11 | event_role | show | patient | view |  | event_role:show:patient:view | True | medium |
| cf12 | relation | view | of | aircraft | part_relation, visual_relation | relation:view:of:aircraft | True | medium |
| cf13 | relation | view | with | part | association_relation, visual_relation | relation:view:with:part | True | high |
| cf14 | relation | view | with | arrow | association_relation, visual_relation | relation:view:with:arrow | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | archway | archway | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:archway", "parents": []} |
| ent_m3 | object | carving | carvings | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:carving", "parents": []} |
| ent_m4 | object | wall | wall | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |
| ent_m7 | context | left | left | object | raw_lemma | semantic_type_fallback | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:left", "parents": ["entity_parent:scene_context"]} |
| ent_m8 | object | window | window | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:window", "parents": []} |
| ent_m10 | object | sign | sign | document | raw_lemma | stage9_seed:parent_seed | text_carrier, artifact | m10 | raw_mention |  |  |  | True | {"canonical": "entity:sign", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m13 | object | trash_can | trash can | object | lvis_object\|visual_genome_object_synset\|wordnet_noun_mwe | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:trash_can", "parents": []} |
| ent_m16 | object | plaque | plaque | document | raw_lemma | stage9_seed:parent_seed | text_carrier, artifact | m16 | raw_mention |  |  |  | True | {"canonical": "entity:plaque", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m18 | context | side | side | object | raw_lemma | semantic_type_fallback | scene_context | m18 | raw_mention |  |  |  | True | {"canonical": "entity:side", "parents": ["entity_parent:scene_context"]} |
| ent_m19 | object | arch | arch | object | raw_lemma | none |  | m19 | raw_mention |  |  |  | True | {"canonical": "entity:arch", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m20 | set | set | set | raw_action | visual_action_fallback | visual_action |  | theme:m0->ent_m0 | {"canonical": "action:set", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m21 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m8->ent_m8; agent:m10->ent_m10 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce2 | m22 | mounted | mount | mount | raw_action | visual_action_fallback | visual_action |  | theme:m16->ent_m16 | {"canonical": "action:mount", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | set | theme | m0 | ent_m0 | medium | e10 | nsubjpass -> set |  |  |
| ce1 | stand | agent | m8 | ent_m8 | medium | e11 | nsubj -> stand |  |  |
| ce1 | stand | agent | m10 | ent_m10 | medium | e12 | nsubj -> stand |  |  |
| ce2 | mount | theme | m16 | ent_m16 | medium | e13 | nsubjpass -> mounted |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | into | into | raw_relation | raw_relation | visual_relation | medium | e15 | False | False |  |  |
| cr2 | m8 | m7 | ent_m8 | ent_m7 | to | to | raw_relation | raw_relation | visual_relation | medium | e16 | False | False |  |  |
| cr3 | m8 | m13 | ent_m8 | ent_m13 | beside | next_to | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e17 | False | False |  |  |
| cr4 | m16 | m18 | ent_m16 | ent_m18 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e18 | False | False |  |  |
| cr5 | m18 | m19 | ent_m18 | ent_m19 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e19 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | archway |  |  |  | entity_exists:archway | True | low |
| cf1 | entity_exists | carving |  |  |  | entity_exists:carving | True | low |
| cf2 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf3 | entity_exists | left |  |  | scene_context | entity_exists:left | True | medium |
| cf4 | entity_exists | window |  |  |  | entity_exists:window | True | low |
| cf5 | entity_exists | sign |  |  | text_carrier, artifact | entity_exists:sign | True | high |
| cf6 | entity_exists | trash_can |  |  |  | entity_exists:trash_can | True | high |
| cf7 | entity_exists | plaque |  |  | text_carrier, artifact | entity_exists:plaque | True | high |
| cf8 | entity_exists | side |  |  | scene_context | entity_exists:side | True | medium |
| cf9 | entity_exists | arch |  |  |  | entity_exists:arch | True | low |
| cf10 | has_attribute | archway | ornate |  | modifier_attribute, visual_attribute | has_attribute:archway:ornate | True | medium |
| cf11 | has_attribute | archway | stone |  | material_attribute, material, visual_attribute | has_attribute:archway:stone | True | high |
| cf12 | has_attribute | wall | beige |  | color_attribute, color, visual_attribute | has_attribute:wall:beige | True | high |
| cf13 | has_attribute | wall | building |  | compound_modifier, visual_attribute | has_attribute:wall:building | True | medium |
| cf14 | has_attribute | window | red-framed |  | modifier_attribute, visual_attribute | has_attribute:window:red-framed | True | medium |
| cf15 | has_attribute | sign | black |  | color_attribute, color, visual_attribute | has_attribute:sign:black | True | high |
| cf16 | has_attribute | sign | chalkboard |  | compound_modifier, visual_attribute | has_attribute:sign:chalkboard | True | medium |
| cf17 | has_attribute | trash_can | small |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:trash_can:small | True | high |
| cf18 | has_attribute | trash_can | metal |  | material_attribute, material, non_textile_material_type, visual_attribute | has_attribute:trash_can:metal | True | high |
| cf19 | has_attribute | plaque | green |  | color_attribute, color, visual_attribute | has_attribute:plaque:green | True | high |
| cf20 | action_event | set |  |  | visual_action | action_event:set | True | low |
| cf21 | event_role | set | theme | archway |  | event_role:set:theme:archway | True | medium |
| cf22 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf23 | event_role | stand | agent | window |  | event_role:stand:agent:window | True | medium |
| cf24 | event_role | stand | agent | sign |  | event_role:stand:agent:sign | True | medium |
| cf25 | action_event | mount |  |  | visual_action | action_event:mount | True | low |
| cf26 | event_role | mount | theme | plaque |  | event_role:mount:theme:plaque | True | medium |
| cf27 | relation | archway | with | carving | association_relation, visual_relation | relation:archway:with:carving | True | high |
| cf28 | relation | archway | into | wall | visual_relation | relation:archway:into:wall | True | medium |
| cf29 | relation | window | to | left | visual_relation | relation:window:to:left | True | medium |
| cf30 | relation | window | next_to | trash_can | spatial_proximity, visual_relation | relation:window:next_to:trash_can | True | high |
| cf31 | relation | plaque | on | side | spatial_support, visual_relation | relation:plaque:on:side | True | high |
| cf32 | relation | side | of | arch | part_relation, visual_relation | relation:side:of:arch | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m20 | e10 | m0 |  |  | {"action_mention_id": "m20", "kind": "passive_subject_to_theme", "raw_edge_id": "e10", "target": "m0"} |
| passive_subject_to_theme | m22 | e13 | m16 |  |  | {"action_mention_id": "m22", "kind": "passive_subject_to_theme", "raw_edge_id": "e13", "target": "m16"} |
| relation_lexical_canonicalized |  | e17 |  |  |  | {"canonical": "next_to", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e17", "raw_relation": "beside", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | flower | flower | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:flower", "parents": []} |
| ent_m3 | object | petal | petals | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:petal", "parents": []} |
| ent_m5 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m5 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e6 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e7 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | against | against | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_contact, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | flower |  |  |  | entity_exists:flower | True | low |
| cf1 | entity_exists | petal |  |  |  | entity_exists:petal | True | low |
| cf2 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf3 | has_attribute | flower | vibrant |  | modifier_attribute, visual_attribute | has_attribute:flower:vibrant | True | medium |
| cf4 | has_attribute | flower | pink |  | color_attribute, color, visual_attribute | has_attribute:flower:pink | True | high |
| cf5 | has_attribute | petal | long |  | size_attribute, clean_exact_overlap, length, visual_attribute | has_attribute:petal:long | True | high |
| cf6 | has_attribute | background | blurred |  | modifier_attribute, visual_attribute | has_attribute:background:blurred | True | medium |
| cf7 | has_attribute | background | green |  | color_attribute, color, visual_attribute | has_attribute:background:green | True | high |
| cf8 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf9 | event_role | stand | agent | flower |  | event_role:stand:agent:flower | True | medium |
| cf10 | relation | flower | with | petal | association_relation, visual_relation | relation:flower:with:petal | True | high |
| cf11 | relation | flower | against | background | spatial_contact, visual_relation | relation:flower:against:background | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | women | person | stage9_seed:synonym_seed | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | protest | protest | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:protest", "parents": []} |
| ent_m2 | object | banner | banner | object | raw_lemma | stage9_seed:parent_seed | text_carrier, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:banner", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m3 | object | tree | trees | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m4 | object | dress | dress | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:dress", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | protest |  |  |  | entity_exists:protest | True | low |
| cf2 | entity_exists | banner |  |  | text_carrier, artifact | entity_exists:banner | True | high |
| cf3 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf4 | entity_exists | dress |  |  | clothing, wearable | entity_exists:dress | True | high |
| cf5 | has_attribute | dress | rainbow |  | attribute, visual_attribute | has_attribute:dress:rainbow | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | soap | soap | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:soap", "parents": []} |
| ent_m2 | object | bathtub | bathtub | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:bathtub", "parents": []} |
| ent_m3 | object | mirror | mirror | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:mirror", "parents": []} |
| ent_m4 | object | tile | tiles | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:tile", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | soap |  |  |  | entity_exists:soap | True | low |
| cf2 | entity_exists | bathtub |  |  |  | entity_exists:bathtub | True | low |
| cf3 | entity_exists | mirror |  |  |  | entity_exists:mirror | True | low |
| cf4 | entity_exists | tile |  |  |  | entity_exists:tile | True | low |
| cf5 | has_attribute | tile | white |  | color_attribute, color, visual_attribute | has_attribute:tile:white | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | view | view | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:view", "parents": []} |
| ent_m2 | object | forest | forest | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:forest", "parents": []} |
| ent_m3 | object | tree | trees | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m5 | object | underbrush | underbrush | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:underbrush", "parents": []} |
| ent_m7 | object | leaf | leaves | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:leaf", "parents": []} |
| ent_m10 | object | ground | ground | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:ground", "parents": []} |
| ent_m11 | object | tree_trunk | tree trunks | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:tree_trunk", "parents": []} |
| ent_m12 | object | out-of-focus | out-of-focus | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:out-of-focus", "parents": []} |
| ent_m14 | object | sky | sky | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m15 | object | blur | blur | object | raw_lemma | none |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:blur", "parents": []} |
| ent_m17 | object | movement | movement | object | raw_lemma | none |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:movement", "parents": []} |
| ent_m18 | object | wood | woods | object | raw_lemma | none |  | m18 | raw_mention |  |  |  | True | {"canonical": "entity:wood", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m19 | cover | cover | cover | raw_action | visual_action_fallback | visual_action |  | agent:m7->ent_m7; patient:m10->ent_m10 | {"canonical": "action:cover", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m20 | rising | rise | rise | raw_action | visual_action_fallback | visual_action |  | agent:m11->ent_m11 | {"canonical": "action:rise", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m21 | suggests | suggest | suggest | raw_action | visual_action_fallback | visual_action |  | agent:m15->ent_m15; patient:m17->ent_m17 | {"canonical": "action:suggest", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | cover | agent | m7 | ent_m7 | medium | e7 | nsubj -> cover |  |  |
| ce0 | cover | patient | m10 | ent_m10 | medium | e8 | dobj -> cover |  |  |
| ce1 | rise | agent | m11 | ent_m11 | medium | e9 | nsubj -> rising |  |  |
| ce2 | suggest | agent | m15 | ent_m15 | medium | e10 | nsubj -> suggests |  |  |
| ce2 | suggest | patient | m17 | ent_m17 | medium | e11 | dobj -> suggests |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e12 | False | False |  |  |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr2 | m2 | m5 | ent_m2 | ent_m5 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr3 | m11 | m12 | ent_m11 | ent_m12 | into | into | raw_relation | raw_relation | visual_relation | medium | e15 | False | False |  |  |
| cr4 | m17 | m18 | ent_m17 | ent_m18 | through | through | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | medium | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | view |  |  |  | entity_exists:view | True | low |
| cf1 | entity_exists | forest |  |  |  | entity_exists:forest | True | low |
| cf2 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf3 | entity_exists | underbrush |  |  |  | entity_exists:underbrush | True | low |
| cf4 | entity_exists | leaf |  |  |  | entity_exists:leaf | True | low |
| cf5 | entity_exists | ground |  |  |  | entity_exists:ground | True | low |
| cf6 | entity_exists | tree_trunk |  |  |  | entity_exists:tree_trunk | True | high |
| cf7 | entity_exists | out-of-focus |  |  |  | entity_exists:out-of-focus | True | low |
| cf8 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf9 | entity_exists | blur |  |  |  | entity_exists:blur | True | low |
| cf10 | entity_exists | movement |  |  |  | entity_exists:movement | True | low |
| cf11 | entity_exists | wood |  |  |  | entity_exists:wood | True | low |
| cf12 | has_attribute | view | blurry |  | visual_attribute | has_attribute:view:blurry | True | medium |
| cf13 | has_attribute | tree | tall |  | size_attribute, height, visual_attribute | has_attribute:tree:tall | True | high |
| cf14 | has_attribute | underbrush | dense |  | modifier_attribute, visual_attribute | has_attribute:underbrush:dense | True | medium |
| cf15 | has_attribute | leaf | green |  | color_attribute, color, visual_attribute | has_attribute:leaf:green | True | high |
| cf16 | has_attribute | leaf | brown |  | color_attribute, color, visual_attribute | has_attribute:leaf:brown | True | high |
| cf17 | has_attribute | out-of-focus | bright |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:out-of-focus:bright | True | medium |
| cf18 | has_attribute | blur | motion |  | compound_modifier, visual_attribute | has_attribute:blur:motion | True | medium |
| cf19 | action_event | cover |  |  | visual_action | action_event:cover | True | low |
| cf20 | event_role | cover | agent | leaf |  | event_role:cover:agent:leaf | True | medium |
| cf21 | event_role | cover | patient | ground |  | event_role:cover:patient:ground | True | medium |
| cf22 | action_event | rise |  |  | visual_action | action_event:rise | True | low |
| cf23 | event_role | rise | agent | tree_trunk |  | event_role:rise:agent:tree_trunk | True | medium |
| cf24 | action_event | suggest |  |  | visual_action | action_event:suggest | True | low |
| cf25 | event_role | suggest | agent | blur |  | event_role:suggest:agent:blur | True | medium |
| cf26 | event_role | suggest | patient | movement |  | event_role:suggest:patient:movement | True | medium |
| cf27 | relation | view | of | forest | part_relation, visual_relation | relation:view:of:forest | True | medium |
| cf28 | relation | forest | with | tree | association_relation, visual_relation | relation:forest:with:tree | True | high |
| cf29 | relation | forest | with | underbrush | association_relation, visual_relation | relation:forest:with:underbrush | True | high |
| cf30 | relation | tree_trunk | into | out-of-focus | visual_relation | relation:tree_trunk:into:out-of-focus | True | medium |
| cf31 | relation | movement | through | wood | spatial_path, visual_relation | relation:movement:through:wood | True | medium |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | mouse | mouse | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:mouse", "parents": []} |
| ent_m3 | object | seed | seeds | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:seed", "parents": []} |
| ent_m4 | object | lid | lid | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:lid", "parents": []} |
| ent_m7 | context | surface | surface | object | raw_lemma | semantic_type_fallback | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | eats | eat | eat | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m3->ent_m3 | {"canonical": "action:eat", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | eat | agent | m0 | ent_m0 | medium | e4 | nsubj -> eats |  |  |
| ce0 | eat | patient | m3 | ent_m3 | medium | e5 | dobj -> eats |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | from | from | raw_relation | raw_relation | visual_relation | medium | e6 | False | False |  |  |
| cr1 | m4 | m7 | ent_m4 | ent_m7 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | mouse |  |  |  | entity_exists:mouse | True | low |
| cf1 | entity_exists | seed |  |  |  | entity_exists:seed | True | low |
| cf2 | entity_exists | lid |  |  |  | entity_exists:lid | True | low |
| cf3 | entity_exists | surface |  |  | scene_context | entity_exists:surface | True | medium |
| cf4 | has_attribute | mouse | small |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:mouse:small | True | high |
| cf5 | has_attribute | mouse | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:mouse:dark | True | medium |
| cf6 | has_attribute | lid | green |  | color_attribute, color, visual_attribute | has_attribute:lid:green | True | high |
| cf7 | has_attribute | lid | plastic |  | material_attribute, clean_exact_overlap, material, non_textile_material_type, visual_attribute | has_attribute:lid:plastic | True | high |
| cf8 | action_event | eat |  |  | visual_action | action_event:eat | True | low |
| cf9 | event_role | eat | agent | mouse |  | event_role:eat:agent:mouse | True | medium |
| cf10 | event_role | eat | patient | seed |  | event_role:eat:patient:seed | True | medium |
| cf11 | relation | mouse | from | lid | visual_relation | relation:mouse:from:lid | True | medium |
| cf12 | relation | lid | on | surface | spatial_support, visual_relation | relation:lid:on:surface | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | podium | podium | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:podium", "parents": []} |
| ent_m3 | object | branding | branding | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:branding", "parents": []} |
| ent_m4 | object | audience | audience | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:audience", "parents": []} |
| ent_m5 | object | hall | hall | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:hall", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | speaks | speak | speak | raw_action | stage9_seed:parent_seed | communication_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:speak", "parents": ["action_parent:communication_action", "action_parent:visual_action"]} |  |
| ce1 | m8 | standing | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | speak | agent | m1 | ent_m1 | medium | e1 | nsubj -> speaks |  |  |
| ce1 | stand | agent | m1 | ent_m1 | medium | e2 | inherited agent advcl -> speaks |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e3 | False | False |  |  |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e4 | False | False |  |  |
| cr2 | m1 | m4 | ent_m1 | ent_m4 | before | before | raw_relation | raw_relation | visual_relation | medium | e5 | False | False |  |  |
| cr3 | m1 | m5 | ent_m1 | ent_m5 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e6 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | podium |  |  |  | entity_exists:podium | True | low |
| cf2 | entity_exists | branding |  |  |  | entity_exists:branding | True | low |
| cf3 | entity_exists | audience |  |  |  | entity_exists:audience | True | low |
| cf4 | entity_exists | hall |  |  |  | entity_exists:hall | True | low |
| cf5 | has_attribute | hall | lecture |  | compound_modifier, visual_attribute | has_attribute:hall:lecture | True | medium |
| cf6 | action_event | speak |  |  | communication_action, visual_action | action_event:speak | True | medium |
| cf7 | event_role | speak | agent | woman |  | event_role:speak:agent:woman | True | medium |
| cf8 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf9 | event_role | stand | agent | woman |  | event_role:stand:agent:woman | True | medium |
| cf10 | relation | woman | at | podium | spatial_location, visual_relation | relation:woman:at:podium | True | medium |
| cf11 | relation | podium | with | branding | association_relation, visual_relation | relation:podium:with:branding | True | high |
| cf12 | relation | woman | before | audience | visual_relation | relation:woman:before:audience | True | medium |
| cf13 | relation | woman | in | hall | spatial_containment, visual_relation | relation:woman:in:hall | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | jersey | jersey | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:jersey", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m7 | object | collar | collar | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m7 | raw_mention |  |  |  | True | {"canonical": "entity:collar", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | smiles | smile | smile | raw_action | stage9_seed:parent_seed | expression_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:smile", "parents": ["action_parent:expression_action", "action_parent:visual_action"]} |  |
| ce1 | m11 | wears | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m1->ent_m1; patient:m7->ent_m7 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce2 | m12 | printed | print | print | raw_action | visual_action_fallback | visual_action |  | agent:m0->None | {"canonical": "action:print", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | smile | agent | m1 | ent_m1 | medium | e6 | nsubj -> smiles |  |  |
| ce1 | wear | agent | m1 | ent_m1 | medium | e7 | nsubj -> wears; resolved She -> woman |  |  |
| ce1 | wear | patient | m7 | ent_m7 | medium | e8 | dobj -> wears |  |  |
| ce2 | print | agent | m0 |  | medium | e9 | nsubj -> printed |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e10 | False | False |  |  |
| cr1 | m0 | m1 |  | ent_m1 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e11 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | jersey |  |  | clothing, wearable | entity_exists:jersey | True | high |
| cf2 | entity_exists | collar |  |  | clothing, wearable | entity_exists:collar | True | medium |
| cf3 | has_attribute | jersey | white |  | color_attribute, color, visual_attribute | has_attribute:jersey:white | True | high |
| cf4 | has_attribute | jersey | orange |  | color_attribute, color, visual_attribute | has_attribute:jersey:orange | True | high |
| cf5 | has_attribute | jersey | blue |  | color_attribute, color, visual_attribute | has_attribute:jersey:blue | True | high |
| cf6 | has_attribute | jersey | cycling |  | compound_modifier, visual_attribute | has_attribute:jersey:cycling | True | medium |
| cf7 | has_attribute | collar | red |  | color_attribute, color, visual_attribute | has_attribute:collar:red | True | high |
| cf8 | has_attribute | collar | blue |  | color_attribute, color, visual_attribute | has_attribute:collar:blue | True | high |
| cf9 | action_event | smile |  |  | expression_action, visual_action | action_event:smile | True | high |
| cf10 | event_role | smile | agent | woman |  | event_role:smile:agent:woman | True | medium |
| cf11 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf12 | event_role | wear | agent | woman |  | event_role:wear:agent:woman | True | medium |
| cf13 | event_role | wear | patient | collar |  | event_role:wear:patient:collar | True | medium |
| cf14 | action_event | print |  |  | visual_action | action_event:print | True | low |
| cf15 | event_role | print | agent |  |  | event_role:print:agent | False | medium |
| cf16 | relation | woman | in | jersey | spatial_containment, visual_relation | relation:woman:in:jersey | True | high |
| cf17 | relation |  | on | woman | spatial_support, visual_relation | relation:on:woman | False | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m4 | object | eye | eyes | object | raw_lemma | stage9_seed:parent_seed | body_part | m4 | raw_mention |  |  |  | True | {"canonical": "entity:eye", "parents": ["entity_parent:body_part"]} |
| ent_m5 | object | chin | chin | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:chin", "parents": []} |
| ent_m6 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m6 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m7 | object | flag | flag | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:flag", "parents": []} |
| ent_m12 | object | hand | hand | object | raw_lemma | stage9_seed:parent_seed | body_part | m12 | raw_mention |  |  |  | True | {"canonical": "entity:hand", "parents": ["entity_parent:body_part"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | smiles | smile | smile | raw_action | stage9_seed:parent_seed | expression_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:smile", "parents": ["action_parent:expression_action", "action_parent:visual_action"]} |  |
| ce1 | m10 | closed | close | close | raw_action | visual_action_fallback | visual_action |  | agent:m4->ent_m4 | {"canonical": "action:close", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m11 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m6->ent_m6 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | smile | agent | m0 | ent_m0 | medium | e3 | nsubj -> smiles |  |  |
| ce1 | close | agent | m4 | ent_m4 | medium | e4 | nsubj -> closed |  |  |
| ce2 | stand | agent | m6 | ent_m6 | medium | e5 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e7 | False | False |  |  |
| cr1 | m12 | m5 | ent_m12 | ent_m5 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e8 | False | False |  |  |
| cr2 | m6 | m7 | ent_m6 | ent_m7 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf2 | entity_exists | eye |  |  | body_part | entity_exists:eye | True | high |
| cf3 | entity_exists | chin |  |  |  | entity_exists:chin | True | low |
| cf4 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf5 | entity_exists | flag |  |  |  | entity_exists:flag | True | low |
| cf6 | entity_exists | hand |  |  | body_part | entity_exists:hand | True | high |
| cf7 | has_attribute | man | old |  | condition_attribute, clean_exact_overlap, maturity, newness, visual_attribute | has_attribute:man:old | True | medium |
| cf8 | has_attribute | shirt | white |  | color_attribute, color, visual_attribute | has_attribute:shirt:white | True | high |
| cf9 | has_attribute | flag | red |  | color_attribute, color, visual_attribute | has_attribute:flag:red | True | high |
| cf10 | action_event | smile |  |  | expression_action, visual_action | action_event:smile | True | high |
| cf11 | event_role | smile | agent | man |  | event_role:smile:agent:man | True | medium |
| cf12 | action_event | close |  |  | visual_action | action_event:close | True | low |
| cf13 | event_role | close | agent | eye |  | event_role:close:agent:eye | True | medium |
| cf14 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf15 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf16 | relation | man | in | shirt | spatial_containment, visual_relation | relation:man:in:shirt | True | high |
| cf17 | relation | hand | near | chin | spatial_proximity, visual_relation | relation:hand:near:chin | True | high |
| cf18 | relation | man | near | flag | spatial_proximity, visual_relation | relation:man:near:flag | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | men | person | stage9_seed:synonym_seed | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | camera | camera | device | raw_lemma | stage9_seed:parent_seed | device, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:camera", "parents": ["entity_parent:device", "entity_parent:artifact"]} |
| ent_m3 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m3 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m5 | object | bandana | bandana | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:bandana", "parents": []} |
| ent_m6 | object | neck | neck | object | raw_lemma | stage9_seed:parent_seed | body_part | m6 | raw_mention |  |  |  | True | {"canonical": "entity:neck", "parents": ["entity_parent:body_part"]} |
| ent_m7 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m7 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m9 | object | face_mask | face mask | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:face_mask", "parents": []} |
| ent_m11 | object | collar | collar | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m11 | raw_mention |  |  |  | True | {"canonical": "entity:collar", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m12 | object | window | window | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:window", "parents": []} |
| ent_m13 | object | art | art | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:art", "parents": []} |
| ent_m16 | context | indoors | indoors | object | raw_lemma | stage9_seed:parent_seed | scene_context | m16 | raw_mention |  |  |  | True | {"canonical": "entity:indoors", "parents": ["entity_parent:scene_context"]} |
| eref_m17 | instance | man | One | person | raw_lemma | stage9_seed:parent_seed | person, human | m17 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| eref_m18 | contrastive_instance | man | other | person | raw_lemma | stage9_seed:parent_seed | person, human | m18 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m17 | eref_m17 | m0 | ent_m0 | high |  |
| refers_to | m18 | eref_m18 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m19 | smile | smile | smile | raw_action | stage9_seed:parent_seed | expression_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:smile", "parents": ["action_parent:expression_action", "action_parent:visual_action"]} |  |
| ce1 | m20 | standing | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce2 | m21 | wears | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m0->eref_m17; patient:m3->ent_m3 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce3 | m22 | has | have | have | raw_action | visual_action_fallback | visual_action |  | agent:m0->eref_m18; patient:m9->ent_m9 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m23 | hanging | hang | hang | raw_action | stage9_seed:parent_seed | attachment_action, visual_action |  | agent:m9->ent_m9 | {"canonical": "action:hang", "parents": ["action_parent:attachment_action", "action_parent:visual_action"]} |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e16 | False | False |  |  |
| cr1 | m3 | m5 | ent_m3 | ent_m5 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e17 | False | False |  |  |
| cr2 | m5 | m6 | ent_m5 | ent_m6 | around | around | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e18 | False | False |  |  |
| cr3 | m0 | m7 | eref_m18 | ent_m7 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e19 | False | False |  |  |
| cr4 | m9 | m11 | ent_m9 | ent_m11 | from | from | raw_relation | raw_relation | visual_relation | medium | e20 | False | False |  |  |
| cr5 | m12 | m0 | ent_m12 | ent_m0 | behind | behind | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e21 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | camera |  |  | device, artifact | entity_exists:camera | True | high |
| cf2 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf3 | entity_exists | bandana |  |  |  | entity_exists:bandana | True | low |
| cf4 | entity_exists | neck |  |  | body_part | entity_exists:neck | True | high |
| cf5 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf6 | entity_exists | face_mask |  |  |  | entity_exists:face_mask | True | high |
| cf7 | entity_exists | collar |  |  | clothing, wearable | entity_exists:collar | True | medium |
| cf8 | entity_exists | window |  |  |  | entity_exists:window | True | low |
| cf9 | entity_exists | art |  |  |  | entity_exists:art | True | low |
| cf10 | entity_exists | indoors |  |  | scene_context | entity_exists:indoors | True | high |
| cf11 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf12 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf13 | has_quantity | man | two |  | exact_quantity, quantity | has_quantity:man:two | True | high |
| cf14 | has_attribute | shirt | blue |  | color_attribute, color, visual_attribute | has_attribute:shirt:blue | True | high |
| cf15 | has_attribute | shirt | white |  | color_attribute, color, visual_attribute | has_attribute:shirt:white | True | high |
| cf16 | has_attribute | face_mask | black |  | color_attribute, color, visual_attribute | has_attribute:face_mask:black | True | high |
| cf17 | has_attribute | art | colorful |  | color_attribute, color_quantity, visual_attribute | has_attribute:art:colorful | True | medium |
| cf18 | has_attribute | art | wall |  | compound_modifier, visual_attribute | has_attribute:art:wall | True | medium |
| cf19 | action_event | smile |  |  | expression_action, visual_action | action_event:smile | True | high |
| cf20 | event_role | smile | agent | man |  | event_role:smile:agent:man | True | medium |
| cf21 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf22 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf23 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf24 | event_role | wear | agent | man |  | event_role:wear:agent:man | True | medium |
| cf25 | event_role | wear | patient | shirt |  | event_role:wear:patient:shirt | True | medium |
| cf26 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf27 | event_role | have | agent | man |  | event_role:have:agent:man | True | medium |
| cf28 | event_role | have | patient | face_mask |  | event_role:have:patient:face_mask | True | medium |
| cf29 | action_event | hang |  |  | attachment_action, visual_action | action_event:hang | True | high |
| cf30 | event_role | hang | agent | face_mask |  | event_role:hang:agent:face_mask | True | medium |
| cf31 | relation | man | at | camera | spatial_location, visual_relation | relation:man:at:camera | True | medium |
| cf32 | relation | shirt | with | bandana | association_relation, visual_relation | relation:shirt:with:bandana | True | high |
| cf33 | relation | bandana | around | neck | spatial_proximity, visual_relation | relation:bandana:around:neck | True | high |
| cf34 | relation | man | in | shirt | spatial_containment, visual_relation | relation:man:in:shirt | True | high |
| cf35 | relation | face_mask | from | collar | visual_relation | relation:face_mask:from:collar | True | medium |
| cf36 | relation | window | behind | man | spatial_depth, visual_relation | relation:window:behind:man | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | cathedral | cathedral | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:cathedral", "parents": []} |
| ent_m2 | object | tower | tower | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:tower", "parents": []} |
| ent_m4 | object | dome | dome | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:dome", "parents": []} |
| ent_m6 | object | sky | sky | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e5 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e7 | False | False |  |  |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | cathedral |  |  |  | entity_exists:cathedral | True | low |
| cf1 | entity_exists | tower |  |  |  | entity_exists:tower | True | low |
| cf2 | entity_exists | dome |  |  |  | entity_exists:dome | True | low |
| cf3 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf4 | has_attribute | cathedral | historic |  | modifier_attribute, visual_attribute | has_attribute:cathedral:historic | True | medium |
| cf5 | has_attribute | tower | tall |  | size_attribute, height, visual_attribute | has_attribute:tower:tall | True | high |
| cf6 | has_attribute | dome | red |  | color_attribute, color, visual_attribute | has_attribute:dome:red | True | high |
| cf7 | has_attribute | sky | bright |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:sky:bright | True | medium |
| cf8 | has_attribute | sky | blue |  | color_attribute, color, visual_attribute | has_attribute:sky:blue | True | high |
| cf9 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf10 | event_role | stand | agent | cathedral |  | event_role:stand:agent:cathedral | True | medium |
| cf11 | relation | cathedral | with | tower | association_relation, visual_relation | relation:cathedral:with:tower | True | high |
| cf12 | relation | cathedral | with | dome | association_relation, visual_relation | relation:cathedral:with:dome | True | high |
| cf13 | relation | cathedral | under | sky | spatial_vertical, visual_relation | relation:cathedral:under:sky | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | bridge | bridge | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:bridge", "parents": []} |
| ent_m3 | object | architecture | architecture | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:architecture", "parents": []} |
| ent_m6 | object | river | river | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:river", "parents": []} |
| ent_m7 | context | night | night | object | raw_lemma | stage9_seed:parent_seed | scene_context, time_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:night", "parents": ["entity_parent:scene_context", "entity_parent:time_context"]} |
| ent_m8 | object | light | lights | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:light", "parents": []} |
| ent_m9 | object | water | water | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | spans | span | span | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m6->ent_m6 | {"canonical": "action:span", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m11 | reflecting | reflect | reflect | raw_action | visual_action_fallback | visual_action |  | agent:m8->ent_m8 | {"canonical": "action:reflect", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | span | agent | m0 | ent_m0 | medium | e5 | nsubj -> spans |  |  |
| ce0 | span | patient | m6 | ent_m6 | medium | e6 | dobj -> spans |  |  |
| ce1 | reflect | agent | m8 | ent_m8 | medium | e7 | nsubj -> reflecting |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e8 | False | False |  |  |
| cr1 | m0 | m7 | ent_m0 | ent_m7 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e9 | False | False |  |  |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e10 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | bridge |  |  |  | entity_exists:bridge | True | low |
| cf1 | entity_exists | architecture |  |  |  | entity_exists:architecture | True | low |
| cf2 | entity_exists | river |  |  |  | entity_exists:river | True | low |
| cf3 | entity_exists | night |  |  | scene_context, time_context | entity_exists:night | True | high |
| cf4 | entity_exists | light |  |  |  | entity_exists:light | True | low |
| cf5 | entity_exists | water |  |  |  | entity_exists:water | True | low |
| cf6 | has_attribute | bridge | brightly |  | modifier_attribute, visual_attribute | has_attribute:bridge:brightly | True | medium |
| cf7 | has_attribute | bridge | light |  | visual_attribute | has_attribute:bridge:light | True | medium |
| cf8 | has_attribute | architecture | traditional |  | modifier_attribute, visual_attribute | has_attribute:architecture:traditional | True | medium |
| cf9 | has_attribute | architecture | chinese |  | modifier_attribute, visual_attribute | has_attribute:architecture:chinese | True | medium |
| cf10 | action_event | span |  |  | visual_action | action_event:span | True | low |
| cf11 | event_role | span | agent | bridge |  | event_role:span:agent:bridge | True | medium |
| cf12 | event_role | span | patient | river |  | event_role:span:patient:river | True | medium |
| cf13 | action_event | reflect |  |  | visual_action | action_event:reflect | True | low |
| cf14 | event_role | reflect | agent | light |  | event_role:reflect:agent:light | True | medium |
| cf15 | relation | bridge | with | architecture | association_relation, visual_relation | relation:bridge:with:architecture | True | high |
| cf16 | relation | bridge | at | night | spatial_location, visual_relation | relation:bridge:at:night | True | medium |
| cf17 | relation | light | on | water | spatial_support, visual_relation | relation:light:on:water | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | jersey | jerseys | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m0 | raw_mention |  |  |  | True | {"canonical": "entity:jersey", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m2 | object | soccer_player | soccer players | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:soccer_player", "parents": []} |
| ent_m3 | object | field | field | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |
| ent_m5 | object | huddle | huddle | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:huddle", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | jersey |  |  | clothing, wearable | entity_exists:jersey | True | high |
| cf1 | entity_exists | soccer_player |  |  |  | entity_exists:soccer_player | True | high |
| cf2 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf3 | entity_exists | huddle |  |  |  | entity_exists:huddle | True | low |
| cf4 | has_attribute | jersey | red |  | color_attribute, color, visual_attribute | has_attribute:jersey:red | True | high |
| cf5 | has_attribute | field | grass |  | attribute, visual_attribute | has_attribute:field:grass | True | high |
| cf6 | has_attribute | huddle | team |  | attribute, visual_attribute | has_attribute:huddle:team | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | trunk | trunk | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:trunk", "parents": []} |
| ent_m2 | object | car | car | vehicle | raw_lemma | stage9_seed:parent_seed | vehicle | m2 | raw_mention |  |  |  | True | {"canonical": "entity:car", "parents": ["entity_parent:vehicle"]} |
| ent_m4 | object | setup | setup | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:setup", "parents": []} |
| ent_m6 | object | subwoofer | subwoofer | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:subwoofer", "parents": []} |
| ent_m7 | object | display | display | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:display", "parents": []} |
| ent_m9 | object | figurine | figurine | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:figurine", "parents": []} |
| ent_m12 | context | side | side | object | raw_lemma | semantic_type_fallback | scene_context | m12 | raw_mention |  |  |  | True | {"canonical": "entity:side", "parents": ["entity_parent:scene_context"]} |
| ent_m13 | object | seat | seats | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:seat", "parents": []} |
| ent_m15 | object | interior | interior | object | raw_lemma | none |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:interior", "parents": []} |
| ent_m16 | object | leather | leather | object | raw_lemma | none |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:leather", "parents": []} |
| ent_m18 | object | car | car | vehicle | raw_lemma | stage9_seed:parent_seed | vehicle | m18 | raw_mention |  |  |  | True | {"canonical": "entity:car", "parents": ["entity_parent:vehicle"]} |
| ent_m19 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m19 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m20 | contains | contain | contain | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m4->ent_m4 | {"canonical": "action:contain", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m21 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m9->ent_m9 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce2 | m22 | lined | line | line | raw_action | visual_action_fallback | visual_action |  | theme:m15->ent_m15 | {"canonical": "action:line", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | contain | agent | m0 | ent_m0 | medium | e9 | nsubj -> contains |  |  |
| ce0 | contain | patient | m4 | ent_m4 | medium | e10 | dobj -> contains |  |  |
| ce1 | stand | agent | m9 | ent_m9 | medium | e11 | nsubj -> stands |  |  |
| ce2 | line | theme | m15 | ent_m15 | medium | e12 | nsubjpass -> lined |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e13 | False | False |  |  |
| cr1 | m4 | m6 | ent_m4 | ent_m6 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr2 | m4 | m7 | ent_m4 | ent_m7 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e15 | False | False |  |  |
| cr3 | m9 | m12 | ent_m9 | ent_m12 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e16 | False | False |  |  |
| cr4 | m9 | m13 | ent_m9 | ent_m13 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e17 | False | False |  |  |
| cr5 | m15 | m16 | ent_m15 | ent_m16 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e18 | False | False |  |  |
| cr6 | m18 | m19 | ent_m18 | ent_m19 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e19 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | trunk |  |  |  | entity_exists:trunk | True | low |
| cf1 | entity_exists | car |  |  | vehicle | entity_exists:car | True | high |
| cf2 | entity_exists | setup |  |  |  | entity_exists:setup | True | low |
| cf3 | entity_exists | subwoofer |  |  |  | entity_exists:subwoofer | True | low |
| cf4 | entity_exists | display |  |  |  | entity_exists:display | True | low |
| cf5 | entity_exists | figurine |  |  |  | entity_exists:figurine | True | low |
| cf6 | entity_exists | side |  |  | scene_context | entity_exists:side | True | medium |
| cf7 | entity_exists | seat |  |  |  | entity_exists:seat | True | low |
| cf8 | entity_exists | interior |  |  |  | entity_exists:interior | True | low |
| cf9 | entity_exists | leather |  |  |  | entity_exists:leather | True | low |
| cf10 | entity_exists | car |  |  | vehicle | entity_exists:car | True | high |
| cf11 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf12 | has_attribute | trunk | open |  | state_attribute, clean_exact_overlap, state, visual_attribute | has_attribute:trunk:open | True | medium |
| cf13 | has_attribute | car | black |  | color_attribute, color, visual_attribute | has_attribute:car:black | True | high |
| cf14 | has_attribute | setup | audio |  | modifier_attribute, visual_attribute | has_attribute:setup:audio | True | medium |
| cf15 | has_attribute | display | frame |  | state_attribute, visual_attribute | has_attribute:display:frame | True | medium |
| cf16 | has_attribute | figurine | gray |  | color_attribute, color, visual_attribute | has_attribute:figurine:gray | True | high |
| cf17 | has_attribute | figurine | monster-like |  | modifier_attribute, visual_attribute | has_attribute:figurine:monster-like | True | medium |
| cf18 | has_attribute | seat | rear |  | modifier_attribute, visual_attribute | has_attribute:seat:rear | True | medium |
| cf19 | has_attribute | leather | black |  | color_attribute, color, visual_attribute | has_attribute:leather:black | True | high |
| cf20 | action_event | contain |  |  | visual_action | action_event:contain | True | low |
| cf21 | event_role | contain | agent | trunk |  | event_role:contain:agent:trunk | True | medium |
| cf22 | event_role | contain | patient | setup |  | event_role:contain:patient:setup | True | medium |
| cf23 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf24 | event_role | stand | agent | figurine |  | event_role:stand:agent:figurine | True | medium |
| cf25 | action_event | line |  |  | visual_action | action_event:line | True | low |
| cf26 | event_role | line | theme | interior |  | event_role:line:theme:interior | True | medium |
| cf27 | relation | trunk | of | car | part_relation, visual_relation | relation:trunk:of:car | True | medium |
| cf28 | relation | setup | with | subwoofer | association_relation, visual_relation | relation:setup:with:subwoofer | True | high |
| cf29 | relation | setup | with | display | association_relation, visual_relation | relation:setup:with:display | True | high |
| cf30 | relation | figurine | on | side | spatial_support, visual_relation | relation:figurine:on:side | True | high |
| cf31 | relation | figurine | near | seat | spatial_proximity, visual_relation | relation:figurine:near:seat | True | high |
| cf32 | relation | interior | with | leather | association_relation, visual_relation | relation:interior:with:leather | True | high |
| cf33 | relation | car | in | background | spatial_containment, visual_relation | relation:car:in:background | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | view | view | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:view", "parents": []} |
| ent_m3 | object | patchwork | patchwork | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:patchwork", "parents": []} |
| ent_m4 | object | farmland | farmland | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:farmland", "parents": []} |
| ent_m5 | object | field | fields | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | shows | show | show | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m3->ent_m3 | {"canonical": "action:show", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m8 | divided | divide | divide | raw_action | visual_action_fallback | visual_action |  | agent:m4->ent_m4 | {"canonical": "action:divide", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | m0 | ent_m0 | medium | e3 | nsubj -> shows |  |  |
| ce0 | show | patient | m3 | ent_m3 | medium | e4 | dobj -> shows |  |  |
| ce1 | divide | agent | m4 | ent_m4 | medium | e5 | inherited agent acl -> farmland |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m3 | m4 | ent_m3 | ent_m4 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e6 | False | False |  |  |
| cr1 | m4 | m5 | ent_m4 | ent_m5 | into | into | raw_relation | raw_relation | visual_relation | medium | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | view |  |  |  | entity_exists:view | True | low |
| cf1 | entity_exists | patchwork |  |  |  | entity_exists:patchwork | True | low |
| cf2 | entity_exists | farmland |  |  |  | entity_exists:farmland | True | low |
| cf3 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf4 | has_attribute | view | black-and-white |  | modifier_attribute, visual_attribute | has_attribute:view:black-and-white | True | medium |
| cf5 | has_attribute | view | aerial |  | modifier_attribute, visual_attribute | has_attribute:view:aerial | True | medium |
| cf6 | has_attribute | field | rectangular |  | shape_attribute, shape, visual_attribute | has_attribute:field:rectangular | True | medium |
| cf7 | action_event | show |  |  | visual_action | action_event:show | True | low |
| cf8 | event_role | show | agent | view |  | event_role:show:agent:view | True | medium |
| cf9 | event_role | show | patient | patchwork |  | event_role:show:patient:patchwork | True | medium |
| cf10 | action_event | divide |  |  | visual_action | action_event:divide | True | low |
| cf11 | event_role | divide | agent | farmland |  | event_role:divide:agent:farmland | True | medium |
| cf12 | relation | patchwork | of | farmland | part_relation, visual_relation | relation:patchwork:of:farmland | True | medium |
| cf13 | relation | farmland | into | field | visual_relation | relation:farmland:into:field | True | medium |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | suit | suit | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:suit", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m2 | object | bottle | bottle | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:bottle", "parents": []} |
| ent_m4 | object | nameplate | nameplate | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:nameplate", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | suit |  |  | clothing, wearable | entity_exists:suit | True | high |
| cf2 | entity_exists | bottle |  |  |  | entity_exists:bottle | True | low |
| cf3 | entity_exists | nameplate |  |  |  | entity_exists:nameplate | True | low |
| cf4 | has_attribute | bottle | water |  | material_attribute, material, visual_attribute | has_attribute:bottle:water | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | ice_rink | ice rink | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:ice_rink", "parents": []} |
| ent_m1 | object | hockey_player | hockey player | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:hockey_player", "parents": []} |
| ent_m2 | object | goalie | goalie | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:goalie", "parents": []} |
| ent_m3 | object | jersey | jersey | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m3 | raw_mention |  |  |  | True | {"canonical": "entity:jersey", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m5 | object | gear | gear | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:gear", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | ice_rink |  |  |  | entity_exists:ice_rink | True | high |
| cf1 | entity_exists | hockey_player |  |  |  | entity_exists:hockey_player | True | high |
| cf2 | entity_exists | goalie |  |  |  | entity_exists:goalie | True | low |
| cf3 | entity_exists | jersey |  |  | clothing, wearable | entity_exists:jersey | True | high |
| cf4 | entity_exists | gear |  |  |  | entity_exists:gear | True | low |
| cf5 | has_attribute | jersey | blue |  | color_attribute, color, visual_attribute | has_attribute:jersey:blue | True | high |
| cf6 | has_attribute | gear | protective |  | attribute, visual_attribute | has_attribute:gear:protective | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | hat | hat | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:hat", "parents": []} |
| ent_m3 | object | plant | plants | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:plant", "parents": []} |
| ent_m7 | object | field | field | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | wearing | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m0->ent_m0; patient:m1->ent_m1 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce1 | m9 | walks | walk | walk | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:walk", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | wear | agent | m0 | ent_m0 | medium | e4 | inherited agent acl -> person |  |  |
| ce0 | wear | patient | m1 | ent_m1 | medium | e5 | dobj -> wearing |  |  |
| ce1 | walk | agent | m0 | ent_m0 | medium | e6 | nsubj -> walks |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | through | through | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | medium | e7 | False | False |  |  |
| cr1 | m0 | m7 | ent_m0 | ent_m7 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf1 | entity_exists | hat |  |  |  | entity_exists:hat | True | low |
| cf2 | entity_exists | plant |  |  |  | entity_exists:plant | True | low |
| cf3 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf4 | has_attribute | hat | conical |  | shape_attribute, shape, visual_attribute | has_attribute:hat:conical | True | medium |
| cf5 | has_attribute | plant | tall |  | size_attribute, height, visual_attribute | has_attribute:plant:tall | True | high |
| cf6 | has_attribute | plant | green |  | color_attribute, color, visual_attribute | has_attribute:plant:green | True | high |
| cf7 | has_attribute | plant | corn |  | compound_modifier, visual_attribute | has_attribute:plant:corn | True | medium |
| cf8 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf9 | event_role | wear | agent | person |  | event_role:wear:agent:person | True | medium |
| cf10 | event_role | wear | patient | hat |  | event_role:wear:patient:hat | True | medium |
| cf11 | action_event | walk |  |  | locomotion_action, visual_action | action_event:walk | True | high |
| cf12 | event_role | walk | agent | person |  | event_role:walk:agent:person | True | medium |
| cf13 | relation | person | through | plant | spatial_path, visual_relation | relation:person:through:plant | True | medium |
| cf14 | relation | person | in | field | spatial_containment, visual_relation | relation:person:in:field | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | beach | beach | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:beach", "parents": []} |
| ent_m1 | object | palm_tree | palm trees | object | openimages_boxable\|visual_genome_object_synset\|wordnet_noun_mwe | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:palm_tree", "parents": []} |
| ent_m2 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m2 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m3 | object | van | van | vehicle | raw_lemma | stage9_seed:parent_seed | vehicle | m3 | raw_mention |  |  |  | True | {"canonical": "entity:van", "parents": ["entity_parent:vehicle"]} |
| ent_m4 | object | grass | grass | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": []} |
| ent_m5 | object | ocean | ocean | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:ocean", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | beach |  |  |  | entity_exists:beach | True | low |
| cf1 | entity_exists | palm_tree |  |  |  | entity_exists:palm_tree | True | high |
| cf2 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf3 | entity_exists | van |  |  | vehicle | entity_exists:van | True | high |
| cf4 | entity_exists | grass |  |  |  | entity_exists:grass | True | low |
| cf5 | entity_exists | ocean |  |  |  | entity_exists:ocean | True | low |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | path | path | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:path", "parents": []} |
| ent_m2 | object | tree | trees | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m4 | object | sky | sky | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m6 | object | landscape | landscape | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:landscape", "parents": []} |
| ent_m8 | object | branch | branches | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:branch", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | path |  |  |  | entity_exists:path | True | low |
| cf1 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf2 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf3 | entity_exists | landscape |  |  |  | entity_exists:landscape | True | low |
| cf4 | entity_exists | branch |  |  |  | entity_exists:branch | True | low |
| cf5 | has_attribute | path | snowy |  | material_attribute, material, visual_attribute | has_attribute:path:snowy | True | high |
| cf6 | has_attribute | tree | frosted |  | attribute, visual_attribute | has_attribute:tree:frosted | True | high |
| cf7 | has_attribute | sky | blue |  | color_attribute, color, visual_attribute | has_attribute:sky:blue | True | high |
| cf8 | has_attribute | landscape | winter |  | attribute, visual_attribute | has_attribute:landscape:winter | True | high |
| cf9 | has_attribute | branch | bare |  | attribute, visual_attribute | has_attribute:branch:bare | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sign | sign | document | raw_lemma | stage9_seed:parent_seed | text_carrier, artifact | m0 | raw_mention |  |  |  | True | {"canonical": "entity:sign", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m4 | object | building | building | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m6 | object | pier | Pier | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:pier", "parents": []} |
| ent_m7 | object | american_flag | American flag | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:american_flag", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | flying | fly | fly | raw_action | visual_action_fallback | visual_action |  | agent:m7->ent_m7 | {"canonical": "action:fly", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | fly | agent | m7 | ent_m7 | medium | e4 | nsubj -> flying |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e5 | False | False |  |  |
| cr1 | m4 | m6 | ent_m4 | ent_m6 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e6 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | sign |  |  | text_carrier, artifact | entity_exists:sign | True | high |
| cf1 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf2 | entity_exists | pier |  |  |  | entity_exists:pier | True | low |
| cf3 | entity_exists | american_flag |  |  |  | entity_exists:american_flag | True | high |
| cf4 | has_attribute | sign | hard |  | texture_attribute, clean_exact_overlap, hardness, visual_attribute | has_attribute:sign:hard | True | medium |
| cf5 | has_attribute | sign | rock |  | compound_modifier, visual_attribute | has_attribute:sign:rock | True | medium |
| cf6 | has_attribute | sign | cafe |  | compound_modifier, visual_attribute | has_attribute:sign:cafe | True | medium |
| cf7 | has_attribute | building | red |  | color_attribute, color, visual_attribute | has_attribute:building:red | True | high |
| cf8 | action_event | fly |  |  | visual_action | action_event:fly | True | low |
| cf9 | event_role | fly | agent | american_flag |  | event_role:fly:agent:american_flag | True | medium |
| cf10 | relation | sign | on | building | spatial_support, visual_relation | relation:sign:on:building | True | high |
| cf11 | relation | building | at | pier | spatial_location, visual_relation | relation:building:at:pier | True | medium |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | hillside | hillside | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:hillside", "parents": []} |
| ent_m3 | object | bush | bushes | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:bush", "parents": []} |
| ent_m5 | object | jacket | jacket | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m5 | raw_mention |  |  |  | True | {"canonical": "entity:jacket", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m7 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m7 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m9 | object | mountain | mountains | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:mountain", "parents": []} |
| ent_m11 | object | sky | sky | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m13 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m14 | wearing | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m0->ent_m0; patient:m5->ent_m5; patient:m7->ent_m7 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce2 | m15 | rise | rise | rise | raw_action | visual_action_fallback | visual_action |  | agent:m9->ent_m9 | {"canonical": "action:rise", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e6 | nsubj -> stands |  |  |
| ce1 | wear | agent | m0 | ent_m0 | medium | e7 | inherited agent advcl -> stands |  |  |
| ce1 | wear | patient | m5 | ent_m5 | medium | e8 | dobj -> wearing |  |  |
| ce1 | wear | patient | m7 | ent_m7 | medium | e9 | dobj -> wearing |  |  |
| ce2 | rise | agent | m9 | ent_m9 | medium | e10 | nsubj -> rise |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e11 | False | False |  |  |
| cr1 | m1 | m3 | ent_m1 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e12 | False | False |  |  |
| cr2 | m9 | m11 | ent_m9 | ent_m11 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e13 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | hillside |  |  |  | entity_exists:hillside | True | low |
| cf2 | entity_exists | bush |  |  |  | entity_exists:bush | True | low |
| cf3 | entity_exists | jacket |  |  | clothing, wearable | entity_exists:jacket | True | high |
| cf4 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf5 | entity_exists | mountain |  |  |  | entity_exists:mountain | True | low |
| cf6 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf7 | has_attribute | hillside | rocky |  | material_attribute, material, visual_attribute | has_attribute:hillside:rocky | True | medium |
| cf8 | has_attribute | bush | sparse |  | modifier_attribute, visual_attribute | has_attribute:bush:sparse | True | medium |
| cf9 | has_attribute | jacket | yellow |  | color_attribute, color, visual_attribute | has_attribute:jacket:yellow | True | high |
| cf10 | has_attribute | shirt | blue |  | color_attribute, color, visual_attribute | has_attribute:shirt:blue | True | high |
| cf11 | has_attribute | mountain | distant |  | modifier_attribute, visual_attribute | has_attribute:mountain:distant | True | medium |
| cf12 | has_attribute | sky | pale |  | modifier_attribute, visual_attribute | has_attribute:sky:pale | True | medium |
| cf13 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf14 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf15 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf16 | event_role | wear | agent | man |  | event_role:wear:agent:man | True | medium |
| cf17 | event_role | wear | patient | jacket |  | event_role:wear:patient:jacket | True | medium |
| cf18 | event_role | wear | patient | shirt |  | event_role:wear:patient:shirt | True | medium |
| cf19 | action_event | rise |  |  | visual_action | action_event:rise | True | low |
| cf20 | event_role | rise | agent | mountain |  | event_role:rise:agent:mountain | True | medium |
| cf21 | relation | man | on | hillside | spatial_support, visual_relation | relation:man:on:hillside | True | high |
| cf22 | relation | hillside | with | bush | association_relation, visual_relation | relation:hillside:with:bush | True | high |
| cf23 | relation | mountain | under | sky | spatial_vertical, visual_relation | relation:mountain:under:sky | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | football_player | football players | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:football_player", "parents": []} |
| ent_m1 | object | uniform | uniforms | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | jersey | jerseys | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m3 | raw_mention |  |  |  | True | {"canonical": "entity:jersey", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m5 | object | entrance | entrance | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:entrance", "parents": []} |
| ent_m7 | object | crowd | crowd | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:crowd", "parents": []} |
| ent_m8 | object | boy | boy | person | raw_lemma | stage9_seed:parent_seed | person, human | m8 | raw_mention |  |  |  | True | {"canonical": "entity:boy", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | football_player |  |  |  | entity_exists:football_player | True | high |
| cf1 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf2 | entity_exists | jersey |  |  | clothing, wearable | entity_exists:jersey | True | high |
| cf3 | entity_exists | entrance |  |  |  | entity_exists:entrance | True | low |
| cf4 | entity_exists | crowd |  |  |  | entity_exists:crowd | True | low |
| cf5 | entity_exists | boy |  |  | person, human | entity_exists:boy | True | high |
| cf6 | has_attribute | uniform | red |  | color_attribute, color, visual_attribute | has_attribute:uniform:red | True | high |
| cf7 | has_attribute | jersey | blue |  | color_attribute, color, visual_attribute | has_attribute:jersey:blue | True | high |
| cf8 | has_attribute | entrance | stadium |  | attribute, visual_attribute | has_attribute:entrance:stadium | True | high |
| cf9 | has_attribute | boy | young |  | attribute, visual_attribute | has_attribute:boy:young | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | hair | hair | object | raw_lemma | stage9_seed:parent_seed | body_part | m1 | raw_mention |  |  |  | True | {"canonical": "entity:hair", "parents": ["entity_parent:body_part"]} |
| ent_m3 | object | microphone | microphone | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:microphone", "parents": []} |
| ent_m4 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m7 | object | structure | structure | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:structure", "parents": []} |
| ent_m10 | object | building | buildings | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m11 | object | tree | trees | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m12 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m12 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m13 | object | person | person | person | raw_lemma | stage9_seed:parent_seed | person, human | m13 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m14 | object | vest | vest | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m14 | raw_mention |  |  |  | True | {"canonical": "entity:vest", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m16 | context | left | left | object | raw_lemma | semantic_type_fallback | scene_context | m16 | raw_mention |  |  |  | True | {"canonical": "entity:left", "parents": ["entity_parent:scene_context"]} |
| ent_m17 | context | outdoors | outdoors | object | raw_lemma | stage9_seed:parent_seed | scene_context | m17 | raw_mention |  |  |  | True | {"canonical": "entity:outdoors", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | speaks | speak | speak | raw_action | stage9_seed:parent_seed | communication_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:speak", "parents": ["action_parent:communication_action", "action_parent:visual_action"]} |  |
| ce1 | m19 | wearing | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m0->ent_m0; patient:m4->ent_m4 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce2 | m20 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce3 | m21 | seen | see | see | raw_action | visual_action_fallback | visual_action |  | theme:m13->ent_m13 | {"canonical": "action:see", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | speak | agent | m0 | ent_m0 | medium | e8 | nsubj -> speaks |  |  |
| ce1 | wear | agent | m0 | ent_m0 | medium | e9 | inherited agent advcl -> speaks |  |  |
| ce1 | wear | patient | m4 | ent_m4 | medium | e10 | dobj -> wearing |  |  |
| ce2 | stand | agent | m0 | ent_m0 | medium | e11 | nsubj -> stands; resolved He -> man |  |  |
| ce3 | see | theme | m13 | ent_m13 | medium | e12 | nsubjpass -> seen |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | into | into | raw_relation | raw_relation | visual_relation | medium | e14 | False | False |  |  |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e15 | False | False |  |  |
| cr3 | m13 | m14 | ent_m13 | ent_m14 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e16 | False | False |  |  |
| cr4 | m13 | m16 | ent_m13 | ent_m16 | to | to | raw_relation | raw_relation | visual_relation | medium | e17 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | hair |  |  | body_part | entity_exists:hair | True | high |
| cf2 | entity_exists | microphone |  |  |  | entity_exists:microphone | True | low |
| cf3 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf4 | entity_exists | structure |  |  |  | entity_exists:structure | True | low |
| cf5 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf6 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf7 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf8 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf9 | entity_exists | vest |  |  | clothing, wearable | entity_exists:vest | True | high |
| cf10 | entity_exists | left |  |  | scene_context | entity_exists:left | True | medium |
| cf11 | entity_exists | outdoors |  |  | scene_context | entity_exists:outdoors | True | high |
| cf12 | has_attribute | hair | gray |  | color_attribute, color, visual_attribute | has_attribute:hair:gray | True | high |
| cf13 | has_attribute | shirt | blue |  | color_attribute, color, visual_attribute | has_attribute:shirt:blue | True | high |
| cf14 | has_attribute | shirt | patterned |  | pattern_attribute, pattern, visual_attribute | has_attribute:shirt:patterned | True | medium |
| cf15 | has_attribute | structure | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:structure:large | True | high |
| cf16 | has_attribute | structure | white |  | color_attribute, color, visual_attribute | has_attribute:structure:white | True | high |
| cf17 | has_attribute | vest | green |  | color_attribute, color, visual_attribute | has_attribute:vest:green | True | high |
| cf18 | action_event | speak |  |  | communication_action, visual_action | action_event:speak | True | medium |
| cf19 | event_role | speak | agent | man |  | event_role:speak:agent:man | True | medium |
| cf20 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf21 | event_role | wear | agent | man |  | event_role:wear:agent:man | True | medium |
| cf22 | event_role | wear | patient | shirt |  | event_role:wear:patient:shirt | True | medium |
| cf23 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf24 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf25 | action_event | see |  |  | visual_action | action_event:see | True | low |
| cf26 | event_role | see | theme | person |  | event_role:see:theme:person | True | medium |
| cf27 | relation | man | with | hair | association_relation, visual_relation | relation:man:with:hair | True | high |
| cf28 | relation | man | into | microphone | visual_relation | relation:man:into:microphone | True | medium |
| cf29 | relation | man | under | structure | spatial_vertical, visual_relation | relation:man:under:structure | True | high |
| cf30 | relation | person | in | vest | spatial_containment, visual_relation | relation:person:in:vest | True | high |
| cf31 | relation | person | to | left | visual_relation | relation:person:to:left | True | medium |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | motorcycle | motorcycle | vehicle | raw_lemma | stage9_seed:parent_seed | vehicle | m1 | raw_mention |  |  |  | True | {"canonical": "entity:motorcycle", "parents": ["entity_parent:vehicle"]} |
| ent_m3 | object | road | road | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:road", "parents": []} |
| ent_m4 | object | field | field | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |
| ent_m5 | object | helmet | helmet | clothing | raw_lemma | stage9_seed:parent_seed | protective_gear, clothing, wearable | m5 | raw_mention |  |  |  | True | {"canonical": "entity:helmet", "parents": ["entity_parent:protective_gear", "entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m7 | object | jacket | jacket | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m7 | raw_mention |  |  |  | True | {"canonical": "entity:jacket", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | rides | rid | rid | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m1->ent_m1 | {"canonical": "action:rid", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m9 | wear | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m0->ent_m0; patient:m5->ent_m5; patient:m7->ent_m7 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | rid | agent | m0 | ent_m0 | medium | e2 | nsubj -> rides |  |  |
| ce0 | rid | patient | m1 | ent_m1 | medium | e3 | dobj -> rides |  |  |
| ce1 | wear | agent | m0 | ent_m0 | medium | e4 | nsubj -> wear; resolved They -> person |  |  |
| ce1 | wear | patient | m5 | ent_m5 | medium | e5 | dobj -> wear |  |  |
| ce1 | wear | patient | m7 | ent_m7 | medium | e6 | dobj -> wear |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e7 | False | False |  |  |
| cr1 | m3 | m4 | ent_m3 | ent_m4 | beside | next_to | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf1 | entity_exists | motorcycle |  |  | vehicle | entity_exists:motorcycle | True | high |
| cf2 | entity_exists | road |  |  |  | entity_exists:road | True | low |
| cf3 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf4 | entity_exists | helmet |  |  | protective_gear, clothing, wearable | entity_exists:helmet | True | high |
| cf5 | entity_exists | jacket |  |  | clothing, wearable | entity_exists:jacket | True | high |
| cf6 | has_attribute | motorcycle | red |  | color_attribute, color, visual_attribute | has_attribute:motorcycle:red | True | high |
| cf7 | has_attribute | helmet | black |  | color_attribute, color, visual_attribute | has_attribute:helmet:black | True | high |
| cf8 | action_event | rid |  |  | visual_action | action_event:rid | True | low |
| cf9 | event_role | rid | agent | person |  | event_role:rid:agent:person | True | medium |
| cf10 | event_role | rid | patient | motorcycle |  | event_role:rid:patient:motorcycle | True | medium |
| cf11 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf12 | event_role | wear | agent | person |  | event_role:wear:agent:person | True | medium |
| cf13 | event_role | wear | patient | helmet |  | event_role:wear:patient:helmet | True | medium |
| cf14 | event_role | wear | patient | jacket |  | event_role:wear:patient:jacket | True | medium |
| cf15 | relation | person | on | road | spatial_support, visual_relation | relation:person:on:road | True | high |
| cf16 | relation | road | next_to | field | spatial_proximity, visual_relation | relation:road:next_to:field | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e8 |  |  |  | {"canonical": "next_to", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e8", "raw_relation": "beside", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | alpaca | alpaca | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:alpaca", "parents": []} |
| ent_m2 | object | neck | neck | object | raw_lemma | stage9_seed:parent_seed | body_part | m2 | raw_mention |  |  |  | True | {"canonical": "entity:neck", "parents": ["entity_parent:body_part"]} |
| ent_m4 | object | fur | fur | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:fur", "parents": []} |
| ent_m7 | object | camera | camera | device | raw_lemma | stage9_seed:parent_seed | device, artifact | m7 | raw_mention |  |  |  | True | {"canonical": "entity:camera", "parents": ["entity_parent:device", "entity_parent:artifact"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | looks | look | look | raw_action | stage9_seed:parent_seed | gaze_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:look", "parents": ["action_parent:gaze_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | look | agent | m0 | ent_m0 | medium | e4 | nsubj -> looks |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e5 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | alpaca |  |  |  | entity_exists:alpaca | True | low |
| cf1 | entity_exists | neck |  |  | body_part | entity_exists:neck | True | high |
| cf2 | entity_exists | fur |  |  |  | entity_exists:fur | True | low |
| cf3 | entity_exists | camera |  |  | device, artifact | entity_exists:camera | True | high |
| cf4 | has_attribute | alpaca | young |  | modifier_attribute, visual_attribute | has_attribute:alpaca:young | True | medium |
| cf5 | has_attribute | neck | long |  | size_attribute, clean_exact_overlap, length, visual_attribute | has_attribute:neck:long | True | high |
| cf6 | has_attribute | fur | fluffy |  | material_attribute, clean_exact_overlap, material, texture, visual_attribute | has_attribute:fur:fluffy | True | medium |
| cf7 | has_attribute | fur | white |  | color_attribute, color, visual_attribute | has_attribute:fur:white | True | high |
| cf8 | action_event | look |  |  | gaze_action, visual_action | action_event:look | True | high |
| cf9 | event_role | look | agent | alpaca |  | event_role:look:agent:alpaca | True | medium |
| cf10 | relation | alpaca | with | neck | association_relation, visual_relation | relation:alpaca:with:neck | True | high |
| cf11 | relation | alpaca | with | fur | association_relation, visual_relation | relation:alpaca:with:fur | True | high |
| cf12 | relation | alpaca | at | camera | spatial_location, visual_relation | relation:alpaca:at:camera | True | medium |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | mid-air | mid-air | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:mid-air", "parents": []} |
| ent_m2 | object | rope | ropes | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:rope", "parents": []} |
| ent_m3 | object | facility | facility | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:facility", "parents": []} |
| ent_m6 | object | wall | walls | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |
| ent_m8 | object | ceiling | ceiling | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:ceiling", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | hangs | hang | hang | raw_action | stage9_seed:parent_seed | attachment_action, visual_action |  | agent:m0->ent_m0; patient:m1->ent_m1 | {"canonical": "action:hang", "parents": ["action_parent:attachment_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | hang | agent | m0 | ent_m0 | medium | e4 | nsubj -> hangs |  |  |
| ce0 | hang | patient | m1 | ent_m1 | medium | e5 | dobj -> hangs |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | from | from | raw_relation | raw_relation | visual_relation | medium | e6 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | inside | inside | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e7 | False | False |  |  |
| cr2 | m3 | m6 | ent_m3 | ent_m6 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e8 | False | False |  |  |
| cr3 | m3 | m8 | ent_m3 | ent_m8 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf1 | entity_exists | mid-air |  |  |  | entity_exists:mid-air | True | low |
| cf2 | entity_exists | rope |  |  |  | entity_exists:rope | True | low |
| cf3 | entity_exists | facility |  |  |  | entity_exists:facility | True | low |
| cf4 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf5 | entity_exists | ceiling |  |  |  | entity_exists:ceiling | True | low |
| cf6 | has_attribute | facility | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:facility:large | True | high |
| cf7 | has_attribute | facility | indoor |  | modifier_attribute, visual_attribute | has_attribute:facility:indoor | True | medium |
| cf8 | has_attribute | wall | white |  | color_attribute, color, visual_attribute | has_attribute:wall:white | True | high |
| cf9 | has_attribute | ceiling | high |  | size_attribute, height, visual_attribute | has_attribute:ceiling:high | True | medium |
| cf10 | action_event | hang |  |  | attachment_action, visual_action | action_event:hang | True | high |
| cf11 | event_role | hang | agent | person |  | event_role:hang:agent:person | True | medium |
| cf12 | event_role | hang | patient | mid-air |  | event_role:hang:patient:mid-air | True | medium |
| cf13 | relation | person | from | rope | visual_relation | relation:person:from:rope | True | medium |
| cf14 | relation | person | inside | facility | spatial_containment, visual_relation | relation:person:inside:facility | True | high |
| cf15 | relation | facility | with | wall | association_relation, visual_relation | relation:facility:with:wall | True | high |
| cf16 | relation | facility | with | ceiling | association_relation, visual_relation | relation:facility:with:ceiling | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | soccer_player | soccer player | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:soccer_player", "parents": []} |
| ent_m1 | object | jersey | jersey | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:jersey", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | ball | ball | object | raw_lemma | stage9_seed:parent_seed | sports_equipment, artifact | m3 | raw_mention |  |  |  | True | {"canonical": "entity:ball", "parents": ["entity_parent:sports_equipment", "entity_parent:artifact"]} |
| ent_m4 | object | opponent | opponents | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:opponent", "parents": []} |
| ent_m5 | object | field | field | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |
| ent_m7 | object | spectator | Spectators | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:spectator", "parents": []} |
| ent_m8 | object | stand | stands | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:stand", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | controls | control | control | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action |  | agent:m0->ent_m0; patient:m3->ent_m3 | {"canonical": "action:control", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce1 | m10 | challenged | challenge | challenge | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:challenge", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m11 | fill | fill | fill | raw_action | visual_action_fallback | visual_action |  | agent:m7->ent_m7; patient:m8->ent_m8 | {"canonical": "action:fill", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | control | agent | m0 | ent_m0 | medium | e2 | nsubj -> controls |  |  |
| ce0 | control | patient | m3 | ent_m3 | medium | e3 | dobj -> controls |  |  |
| ce1 | challenge | agent | m0 | ent_m0 | medium | e4 | inherited agent advcl -> controls |  |  |
| ce2 | fill | agent | m7 | ent_m7 | medium | e5 | nsubj -> fill |  |  |
| ce2 | fill | patient | m8 | ent_m8 | medium | e6 | dobj -> fill |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e7 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | by | by | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | medium | e8 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e9 | False | False |  |  |
| cr3 | m8 | m0 | ent_m8 | ent_m0 | behind | behind | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e10 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | soccer_player |  |  |  | entity_exists:soccer_player | True | high |
| cf1 | entity_exists | jersey |  |  | clothing, wearable | entity_exists:jersey | True | high |
| cf2 | entity_exists | ball |  |  | sports_equipment, artifact | entity_exists:ball | True | high |
| cf3 | entity_exists | opponent |  |  |  | entity_exists:opponent | True | low |
| cf4 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf5 | entity_exists | spectator |  |  |  | entity_exists:spectator | True | low |
| cf6 | entity_exists | stand |  |  |  | entity_exists:stand | True | low |
| cf7 | has_attribute | jersey | red |  | color_attribute, color, visual_attribute | has_attribute:jersey:red | True | high |
| cf8 | has_attribute | field | green |  | color_attribute, color, visual_attribute | has_attribute:field:green | True | high |
| cf9 | action_event | control |  |  | manipulation_action, visual_action | action_event:control | True | medium |
| cf10 | event_role | control | agent | soccer_player |  | event_role:control:agent:soccer_player | True | medium |
| cf11 | event_role | control | patient | ball |  | event_role:control:patient:ball | True | medium |
| cf12 | action_event | challenge |  |  | visual_action | action_event:challenge | True | low |
| cf13 | event_role | challenge | agent | soccer_player |  | event_role:challenge:agent:soccer_player | True | medium |
| cf14 | action_event | fill |  |  | visual_action | action_event:fill | True | low |
| cf15 | event_role | fill | agent | spectator |  | event_role:fill:agent:spectator | True | medium |
| cf16 | event_role | fill | patient | stand |  | event_role:fill:patient:stand | True | medium |
| cf17 | relation | soccer_player | in | jersey | spatial_containment, visual_relation | relation:soccer_player:in:jersey | True | high |
| cf18 | relation | soccer_player | by | opponent | spatial_proximity, visual_relation | relation:soccer_player:by:opponent | True | medium |
| cf19 | relation | soccer_player | on | field | spatial_support, visual_relation | relation:soccer_player:on:field | True | high |
| cf20 | relation | stand | behind | soccer_player | spatial_depth, visual_relation | relation:stand:behind:soccer_player | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | apron | apron | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:apron", "parents": []} |
| ent_m4 | object | group | group | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:group", "parents": []} |
| ent_m5 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m5 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m6 | object | restaurant | restaurant | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:restaurant", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | walks | walk | walk | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:walk", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | walk | agent | m0 | ent_m0 | medium | e1 | nsubj -> walks |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e2 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e3 | False | False |  |  |
| cr2 | m0 | m4 | ent_m0 | ent_m4 | away_from | away_from | manual_clean_adposition | manual_clean_adposition | spatial_separation, visual_relation | medium | e4 | False | False |  |  |
| cr3 | m4 | m5 | ent_m4 | ent_m5 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e5 | False | False |  |  |
| cr4 | m4 | m6 | ent_m4 | ent_m6 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e6 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf1 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf2 | entity_exists | apron |  |  |  | entity_exists:apron | True | low |
| cf3 | entity_exists | group |  |  |  | entity_exists:group | True | low |
| cf4 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf5 | entity_exists | restaurant |  |  |  | entity_exists:restaurant | True | low |
| cf6 | has_attribute | shirt | white |  | color_attribute, color, visual_attribute | has_attribute:shirt:white | True | high |
| cf7 | action_event | walk |  |  | locomotion_action, visual_action | action_event:walk | True | high |
| cf8 | event_role | walk | agent | person |  | event_role:walk:agent:person | True | medium |
| cf9 | relation | person | in | shirt | spatial_containment, visual_relation | relation:person:in:shirt | True | high |
| cf10 | relation | person | in | apron | spatial_containment, visual_relation | relation:person:in:apron | True | high |
| cf11 | relation | person | away_from | group | spatial_separation, visual_relation | relation:person:away_from:group | True | medium |
| cf12 | relation | group | of | people | part_relation, visual_relation | relation:group:of:people | True | medium |
| cf13 | relation | group | in | restaurant | spatial_containment, visual_relation | relation:group:in:restaurant | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | row | row | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:row", "parents": []} |
| ent_m1 | object | building | buildings | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m3 | object | shutter | shutters | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:shutter", "parents": []} |
| ent_m5 | object | street | street | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:street", "parents": []} |
| ent_m7 | object | car | cars | vehicle | raw_lemma | stage9_seed:parent_seed | vehicle | m7 | raw_mention |  |  |  | True | {"canonical": "entity:car", "parents": ["entity_parent:vehicle"]} |
| ent_m9 | object | curb | curb | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:curb", "parents": []} |
| ent_m10 | object | suv | SUV | vehicle | raw_lemma | stage9_seed:parent_seed | vehicle | m10 | raw_mention |  |  |  | True | {"canonical": "entity:suv", "parents": ["entity_parent:vehicle"]} |
| ent_m12 | context | left | left | object | raw_lemma | semantic_type_fallback | scene_context | m12 | raw_mention |  |  |  | True | {"canonical": "entity:left", "parents": ["entity_parent:scene_context"]} |
| ent_m13 | object | sedan | sedan | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:sedan", "parents": []} |
| ent_m15 | object | scene | scene | object | raw_lemma | stage9_seed:parent_seed | scene_context | m15 | raw_mention |  |  |  | True | {"canonical": "entity:scene", "parents": ["entity_parent:scene_context"]} |
| ent_m16 | object | sky | sky | object | raw_lemma | none |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m18 | object | tree | trees | object | raw_lemma | none |  | m18 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m19 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m19 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m20 | lines | line | line | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m5->ent_m5 | {"canonical": "action:line", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m21 | parked | park | park | raw_action | visual_action_fallback | visual_action |  | theme:m7->ent_m7 | {"canonical": "action:park", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m22 | including | include | include | raw_action | visual_action_fallback | visual_action |  | agent:m7->ent_m7; patient:m10->ent_m10; patient:m13->ent_m13 | {"canonical": "action:include", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m23 | set | set | set | raw_action | visual_action_fallback | visual_action |  | theme:m15->ent_m15 | {"canonical": "action:set", "parents": ["action_parent:visual_action"]} |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e15 | False | False |  |  |
| cr1 | m1 | m3 | ent_m1 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e16 | False | False |  |  |
| cr2 | m7 | m9 | ent_m7 | ent_m9 | along | along | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | medium | e17 | False | False |  |  |
| cr3 | m7 | m10 | ent_m7 | ent_m10 | include | include | raw_relation | raw_relation | visual_relation | medium | e18 | False | False |  |  |
| cr4 | m7 | m13 | ent_m7 | ent_m13 | include | include | raw_relation | raw_relation | visual_relation | medium | e19 | False | False |  |  |
| cr5 | m10 | m12 | ent_m10 | ent_m12 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e20 | False | False |  |  |
| cr6 | m13 | m7 | ent_m13 | ent_m7 | next_to | next_to | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e21 | False | False |  |  |
| cr7 | m15 | m16 | ent_m15 | ent_m16 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e22 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | row |  |  |  | entity_exists:row | True | low |
| cf1 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf2 | entity_exists | shutter |  |  |  | entity_exists:shutter | True | low |
| cf3 | entity_exists | street |  |  |  | entity_exists:street | True | low |
| cf4 | entity_exists | car |  |  | vehicle | entity_exists:car | True | high |
| cf5 | entity_exists | curb |  |  |  | entity_exists:curb | True | low |
| cf6 | entity_exists | suv |  |  | vehicle | entity_exists:suv | True | high |
| cf7 | entity_exists | left |  |  | scene_context | entity_exists:left | True | medium |
| cf8 | entity_exists | sedan |  |  |  | entity_exists:sedan | True | low |
| cf9 | entity_exists | scene |  |  | scene_context | entity_exists:scene | True | high |
| cf10 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf11 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf12 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf13 | has_attribute | building | historic |  | modifier_attribute, visual_attribute | has_attribute:building:historic | True | medium |
| cf14 | has_attribute | shutter | green |  | color_attribute, color, visual_attribute | has_attribute:shutter:green | True | high |
| cf15 | has_attribute | street | cobblestone |  | material_attribute, material, visual_attribute | has_attribute:street:cobblestone | True | medium |
| cf16 | has_quantity | car | several |  | approximate_quantity, quantity | has_quantity:car:several | True | medium |
| cf17 | has_attribute | suv | white |  | color_attribute, color, visual_attribute | has_attribute:suv:white | True | high |
| cf18 | has_attribute | sedan | silver |  | color_attribute, color, material, visual_attribute | has_attribute:sedan:silver | True | high |
| cf19 | has_attribute | sky | overcast |  | weather_attribute, weather, visual_attribute | has_attribute:sky:overcast | True | medium |
| cf20 | action_event | line |  |  | visual_action | action_event:line | True | low |
| cf21 | event_role | line | agent | row |  | event_role:line:agent:row | True | medium |
| cf22 | event_role | line | patient | street |  | event_role:line:patient:street | True | medium |
| cf23 | action_event | park |  |  | visual_action | action_event:park | True | low |
| cf24 | event_role | park | theme | car |  | event_role:park:theme:car | True | medium |
| cf25 | action_event | include |  |  | visual_action | action_event:include | True | low |
| cf26 | event_role | include | agent | car |  | event_role:include:agent:car | True | medium |
| cf27 | event_role | include | patient | suv |  | event_role:include:patient:suv | True | medium |
| cf28 | event_role | include | patient | sedan |  | event_role:include:patient:sedan | True | medium |
| cf29 | action_event | set |  |  | visual_action | action_event:set | True | low |
| cf30 | event_role | set | theme | scene |  | event_role:set:theme:scene | True | medium |
| cf31 | relation | row | of | building | part_relation, visual_relation | relation:row:of:building | True | medium |
| cf32 | relation | building | with | shutter | association_relation, visual_relation | relation:building:with:shutter | True | high |
| cf33 | relation | car | along | curb | spatial_path, visual_relation | relation:car:along:curb | True | medium |
| cf34 | relation | car | include | suv | visual_relation | relation:car:include:suv | True | medium |
| cf35 | relation | car | include | sedan | visual_relation | relation:car:include:sedan | True | medium |
| cf36 | relation | suv | on | left | spatial_support, visual_relation | relation:suv:on:left | True | high |
| cf37 | relation | sedan | next_to | car | spatial_proximity, visual_relation | relation:sedan:next_to:car | True | high |
| cf38 | relation | scene | under | sky | spatial_vertical, visual_relation | relation:scene:under:sky | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | buffalo | buffalo | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:buffalo", "parents": []} |
| ent_m3 | object | grass | grass | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": []} |
| ent_m5 | object | field | field | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |
| ent_m6 | object | buffalo | buffalo | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:buffalo", "parents": []} |
| ent_m7 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m8 | object | slope | slope | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:slope", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | grazes | graze | graze | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:graze", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m11 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m6->ent_m6 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | graze | agent | m0 | ent_m0 | medium | e5 | nsubj -> grazes |  |  |
| ce1 | stand | agent | m6 | ent_m6 | medium | e6 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e7 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e8 | False | False |  |  |
| cr2 | m6 | m7 | ent_m6 | ent_m7 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e9 | False | False |  |  |
| cr3 | m6 | m8 | ent_m6 | ent_m8 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e10 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | buffalo |  |  |  | entity_exists:buffalo | True | low |
| cf1 | entity_exists | grass |  |  |  | entity_exists:grass | True | low |
| cf2 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf3 | entity_exists | buffalo |  |  |  | entity_exists:buffalo | True | low |
| cf4 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf5 | entity_exists | slope |  |  |  | entity_exists:slope | True | low |
| cf6 | has_attribute | buffalo | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:buffalo:dark | True | medium |
| cf7 | has_attribute | buffalo | muddy |  | material_attribute, cleanliness, material, visual_attribute | has_attribute:buffalo:muddy | True | medium |
| cf8 | has_attribute | grass | green |  | color_attribute, color, visual_attribute | has_attribute:grass:green | True | high |
| cf9 | has_attribute | slope | grassy |  | modifier_attribute, visual_attribute | has_attribute:slope:grassy | True | medium |
| cf10 | action_event | graze |  |  | visual_action | action_event:graze | True | low |
| cf11 | event_role | graze | agent | buffalo |  | event_role:graze:agent:buffalo | True | medium |
| cf12 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf13 | event_role | stand | agent | buffalo |  | event_role:stand:agent:buffalo | True | medium |
| cf14 | relation | buffalo | on | grass | spatial_support, visual_relation | relation:buffalo:on:grass | True | high |
| cf15 | relation | buffalo | in | field | spatial_containment, visual_relation | relation:buffalo:in:field | True | high |
| cf16 | relation | buffalo | in | background | spatial_containment, visual_relation | relation:buffalo:in:background | True | high |
| cf17 | relation | buffalo | on | slope | spatial_support, visual_relation | relation:buffalo:on:slope | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hearing_aid | hearing aid | device | visual_genome_object_synset\|wordnet_noun_mwe | stage9_seed:parent_seed | device, artifact | m0 | raw_mention |  |  |  | True | {"canonical": "entity:hearing_aid", "parents": ["entity_parent:device", "entity_parent:artifact"]} |
| ent_m2 | object | case | case | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:case", "parents": []} |
| ent_m5 | context | surface | surface | object | raw_lemma | semantic_type_fallback | scene_context | m5 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": ["entity_parent:scene_context"]} |
| ent_m6 | object | device | device | device | raw_lemma | stage9_seed:parent_seed | device, artifact | m6 | raw_mention |  |  |  | False | {"canonical": "entity:device", "parents": ["entity_parent:device", "entity_parent:artifact"]} |
| ent_m7 | object | shape | shape | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:shape", "parents": []} |
| ent_m9 | object | button | button | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:button", "parents": []} |
| ent_m11 | object | case | case | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:case", "parents": []} |
| ent_m12 | object | base | base | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:base", "parents": []} |
| ent_m14 | object | cable | cable | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:cable", "parents": []} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| generic_alias | m6 | ent_m6 |  | ent_m0 | medium |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | rests | rest | rest | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:rest", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m17 | has | have | have | raw_action | visual_action_fallback | visual_action |  | agent:m6->ent_m0; patient:m7->ent_m7; patient:m9->ent_m9 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m18 | has | have | have | raw_action | visual_action_fallback | visual_action |  | agent:m11->ent_m11; patient:m12->ent_m12 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m19 | extending | extend | extend | raw_action | visual_action_fallback | visual_action |  | agent:m14->ent_m14 | {"canonical": "action:extend", "parents": ["action_parent:visual_action"]} |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | next_to | next_to | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e14 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e15 | False | False |  |  |
| cr2 | m12 | m14 | ent_m12 | ent_m14 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e16 | False | False |  |  |
| cr3 | m14 | m11 | ent_m14 | ent_m11 | from | from | raw_relation | raw_relation | visual_relation | medium | e17 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | hearing_aid |  |  | device, artifact | entity_exists:hearing_aid | True | high |
| cf1 | entity_exists | case |  |  |  | entity_exists:case | True | low |
| cf2 | entity_exists | surface |  |  | scene_context | entity_exists:surface | True | medium |
| cf3 | entity_exists | shape |  |  |  | entity_exists:shape | True | low |
| cf4 | entity_exists | button |  |  |  | entity_exists:button | True | low |
| cf5 | entity_exists | case |  |  |  | entity_exists:case | True | low |
| cf6 | entity_exists | base |  |  |  | entity_exists:base | True | low |
| cf7 | entity_exists | cable |  |  |  | entity_exists:cable | True | low |
| cf8 | has_attribute | hearing_aid | black |  | color_attribute, color, visual_attribute | has_attribute:hearing_aid:black | True | high |
| cf9 | has_attribute | case | white |  | color_attribute, color, visual_attribute | has_attribute:case:white | True | high |
| cf10 | has_attribute | case | charging |  | compound_modifier, visual_attribute | has_attribute:case:charging | True | medium |
| cf11 | has_attribute | shape | curved |  | shape_attribute, clean_exact_overlap, shape, visual_attribute | has_attribute:shape:curved | True | medium |
| cf12 | has_attribute | button | small |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:button:small | True | high |
| cf13 | has_attribute | base | round |  | shape_attribute, clean_exact_overlap, shape, visual_attribute | has_attribute:base:round | True | medium |
| cf14 | has_attribute | cable | white |  | color_attribute, color, visual_attribute | has_attribute:cable:white | True | high |
| cf15 | action_event | rest |  |  | visual_action | action_event:rest | True | low |
| cf16 | event_role | rest | agent | hearing_aid |  | event_role:rest:agent:hearing_aid | True | medium |
| cf17 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf18 | event_role | have | agent | hearing_aid |  | event_role:have:agent:hearing_aid | True | medium |
| cf19 | event_role | have | patient | shape |  | event_role:have:patient:shape | True | medium |
| cf20 | event_role | have | patient | button |  | event_role:have:patient:button | True | medium |
| cf21 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf22 | event_role | have | agent | case |  | event_role:have:agent:case | True | medium |
| cf23 | event_role | have | patient | base |  | event_role:have:patient:base | True | medium |
| cf24 | action_event | extend |  |  | visual_action | action_event:extend | True | low |
| cf25 | event_role | extend | agent | cable |  | event_role:extend:agent:cable | True | medium |
| cf26 | relation | hearing_aid | next_to | case | spatial_proximity, visual_relation | relation:hearing_aid:next_to:case | True | high |
| cf27 | relation | hearing_aid | on | surface | spatial_support, visual_relation | relation:hearing_aid:on:surface | True | high |
| cf28 | relation | base | with | cable | association_relation, visual_relation | relation:base:with:cable | True | high |
| cf29 | relation | cable | from | case | visual_relation | relation:cable:from:case | True | medium |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | mountain | mountain | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:mountain", "parents": []} |
| ent_m1 | object | tree | trees | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m2 | object | sky | sky | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m3 | object | car | car | vehicle | raw_lemma | stage9_seed:parent_seed | vehicle | m3 | raw_mention |  |  |  | True | {"canonical": "entity:car", "parents": ["entity_parent:vehicle"]} |
| ent_m4 | object | cloud | clouds | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:cloud", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | mountain |  |  |  | entity_exists:mountain | True | low |
| cf1 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf2 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf3 | entity_exists | car |  |  | vehicle | entity_exists:car | True | high |
| cf4 | entity_exists | cloud |  |  |  | entity_exists:cloud | True | low |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | race_car | race cars | object | lvis_object\|wordnet_noun_mwe | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:race_car", "parents": []} |
| ent_m1 | object | track | track | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:track", "parents": []} |
| ent_m3 | object | car | car | vehicle | raw_lemma | stage9_seed:parent_seed | vehicle | m3 | raw_mention |  |  |  | True | {"canonical": "entity:car", "parents": ["entity_parent:vehicle"]} |
| ent_m5 | context | foreground | foreground | object | raw_lemma | stage9_seed:parent_seed | scene_context | m5 | raw_mention |  |  |  | True | {"canonical": "entity:foreground", "parents": ["entity_parent:scene_context"]} |
| ent_m6 | object | cone | cones | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:cone", "parents": []} |
| ent_m8 | object | track | track | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:track", "parents": []} |
| ent_m9 | object | grass | grass | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": []} |
| ent_m10 | object | tree | trees | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m11 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m11 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m14 | object | edge | edge | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:edge", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | speed | speed | speed | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:speed", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m13 | mark | mark | mark | raw_action | visual_action_fallback | visual_action |  | agent:m6->ent_m6; patient:m14->ent_m14 | {"canonical": "action:mark", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m15 | surrounded | surround | surround | raw_action | visual_action_fallback | visual_action |  | agent:m6->ent_m6 | {"canonical": "action:surround", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | speed | agent | m0 | ent_m0 | medium | e5 | nsubj -> speed |  |  |
| ce1 | mark | agent | m6 | ent_m6 | medium | e6 | nsubj -> mark |  |  |
| ce1 | mark | patient | m14 | ent_m14 | medium | e7 | dobj -> mark |  |  |
| ce2 | surround | agent | m6 | ent_m6 | medium | e8 | inherited agent advcl -> mark |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | along | along | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | medium | e9 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e10 | False | False |  |  |
| cr2 | m3 | m5 | ent_m3 | ent_m5 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e11 | False | False |  |  |
| cr3 | m6 | m8 | ent_m6 | ent_m8 | edge_of | edge_of | generated_region_pattern\|mixed_relation_collapse_rules | generated_region_pattern\|mixed_relation_collapse_rules | spatial_region, visual_relation | medium | e12 | False | False |  |  |
| cr4 | m6 | m9 | ent_m6 | ent_m9 | by | by | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | medium | e13 | False | False |  |  |
| cr5 | m6 | m10 | ent_m6 | ent_m10 | by | by | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | medium | e14 | False | False |  |  |
| cr6 | m9 | m11 | ent_m9 | ent_m11 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e15 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | race_car |  |  |  | entity_exists:race_car | True | high |
| cf1 | entity_exists | track |  |  |  | entity_exists:track | True | low |
| cf2 | entity_exists | car |  |  | vehicle | entity_exists:car | True | high |
| cf3 | entity_exists | foreground |  |  | scene_context | entity_exists:foreground | True | high |
| cf4 | entity_exists | cone |  |  |  | entity_exists:cone | True | low |
| cf5 | entity_exists | track |  |  |  | entity_exists:track | True | low |
| cf6 | entity_exists | grass |  |  |  | entity_exists:grass | True | low |
| cf7 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf8 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf9 | entity_exists | edge |  |  |  | entity_exists:edge | True | low |
| cf10 | has_attribute | track | curved |  | shape_attribute, clean_exact_overlap, shape, visual_attribute | has_attribute:track:curved | True | medium |
| cf11 | has_attribute | car | red |  | color_attribute, color, visual_attribute | has_attribute:car:red | True | high |
| cf12 | has_attribute | cone | orange |  | color_attribute, color, visual_attribute | has_attribute:cone:orange | True | high |
| cf13 | action_event | speed |  |  | visual_action | action_event:speed | True | low |
| cf14 | event_role | speed | agent | race_car |  | event_role:speed:agent:race_car | True | medium |
| cf15 | action_event | mark |  |  | visual_action | action_event:mark | True | low |
| cf16 | event_role | mark | agent | cone |  | event_role:mark:agent:cone | True | medium |
| cf17 | event_role | mark | patient | edge |  | event_role:mark:patient:edge | True | medium |
| cf18 | action_event | surround |  |  | visual_action | action_event:surround | True | low |
| cf19 | event_role | surround | agent | cone |  | event_role:surround:agent:cone | True | medium |
| cf20 | relation | race_car | along | track | spatial_path, visual_relation | relation:race_car:along:track | True | medium |
| cf21 | relation | race_car | with | car | association_relation, visual_relation | relation:race_car:with:car | True | high |
| cf22 | relation | car | in | foreground | spatial_containment, visual_relation | relation:car:in:foreground | True | high |
| cf23 | relation | cone | edge_of | track | spatial_region, visual_relation | relation:cone:edge_of:track | True | medium |
| cf24 | relation | cone | by | grass | spatial_proximity, visual_relation | relation:cone:by:grass | True | medium |
| cf25 | relation | cone | by | tree | spatial_proximity, visual_relation | relation:cone:by:tree | True | medium |
| cf26 | relation | grass | in | background | spatial_containment, visual_relation | relation:grass:in:background | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | space | space | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:space", "parents": []} |
| ent_m2 | object | object | objects | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:object", "parents": []} |
| ent_m5 | object | shelf | shelves | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:shelf", "parents": []} |
| ent_m7 | object | pedestal | pedestals | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:pedestal", "parents": []} |
| ent_m8 | object | wall | walls | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |
| ent_m9 | object | light | lights | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:light", "parents": []} |
| ent_m11 | object | vase | vase | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:vase", "parents": []} |
| ent_m15 | object | pedestal | pedestal | object | raw_lemma | none |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:pedestal", "parents": []} |
| ent_m17 | object | figurine | figurines | object | raw_lemma | none |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:figurine", "parents": []} |
| ent_m19 | object | item | items | object | raw_lemma | none |  | m19 | raw_mention |  |  |  | True | {"canonical": "entity:item", "parents": []} |
| ent_m21 | object | shelf | shelves | object | raw_lemma | none |  | m21 | raw_mention |  |  |  | True | {"canonical": "entity:shelf", "parents": []} |
| ent_m22 | context | setting | setting | object | raw_lemma | stage9_seed:parent_seed | scene_context | m22 | raw_mention |  |  |  | True | {"canonical": "entity:setting", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m24 | displays | display | display | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m2->ent_m2 | {"canonical": "action:display", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m25 | illuminated | illuminate | illuminate | raw_action | visual_action_fallback | visual_action |  | theme:m8->ent_m8; by_agent_or_causer:m9->ent_m9 | {"canonical": "action:illuminate", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m26 | sits | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m11->ent_m11 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce3 | m27 | arranged | arrange | arrange | raw_action | visual_action_fallback | visual_action |  | theme:m17->ent_m17; theme:m19->ent_m19 | {"canonical": "action:arrange", "parents": ["action_parent:visual_action"]} |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m5 | ent_m0 | ent_m5 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e19 | False | False |  |  |
| cr1 | m0 | m7 | ent_m0 | ent_m7 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e20 | False | False |  |  |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | by | by | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | medium | e21 | True | False |  |  |
| cr3 | m11 | m15 | ent_m11 | ent_m15 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e22 | False | False |  |  |
| cr4 | m17 | m21 | ent_m17 | ent_m21 | across | across | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | high | e23 | False | False |  |  |
| cr5 | m17 | m22 | ent_m17 | ent_m22 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e24 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | space |  |  |  | entity_exists:space | True | low |
| cf1 | entity_exists | object |  |  |  | entity_exists:object | True | low |
| cf2 | entity_exists | shelf |  |  |  | entity_exists:shelf | True | low |
| cf3 | entity_exists | pedestal |  |  |  | entity_exists:pedestal | True | low |
| cf4 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf5 | entity_exists | light |  |  |  | entity_exists:light | True | low |
| cf6 | entity_exists | vase |  |  |  | entity_exists:vase | True | low |
| cf7 | entity_exists | pedestal |  |  |  | entity_exists:pedestal | True | low |
| cf8 | entity_exists | figurine |  |  |  | entity_exists:figurine | True | low |
| cf9 | entity_exists | item |  |  |  | entity_exists:item | True | low |
| cf10 | entity_exists | shelf |  |  |  | entity_exists:shelf | True | low |
| cf11 | entity_exists | setting |  |  | scene_context | entity_exists:setting | True | high |
| cf12 | has_attribute | space | gallery |  | compound_modifier, visual_attribute | has_attribute:space:gallery | True | medium |
| cf13 | has_quantity | object | various |  | approximate_quantity, quantity | has_quantity:object:various | True | medium |
| cf14 | has_attribute | object | small |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:object:small | True | high |
| cf15 | has_attribute | shelf | white |  | color_attribute, color, visual_attribute | has_attribute:shelf:white | True | high |
| cf16 | has_attribute | light | overhead |  | modifier_attribute, visual_attribute | has_attribute:light:overhead | True | medium |
| cf17 | has_attribute | vase | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:vase:large | True | high |
| cf18 | has_attribute | vase | black |  | color_attribute, color, visual_attribute | has_attribute:vase:black | True | high |
| cf19 | has_attribute | vase | woven |  | pattern_attribute, other, pattern_marking, texture, visual_attribute | has_attribute:vase:woven | True | medium |
| cf20 | has_attribute | pedestal | central |  | modifier_attribute, visual_attribute | has_attribute:pedestal:central | True | medium |
| cf21 | has_quantity | figurine | several |  | approximate_quantity, quantity | has_quantity:figurine:several | True | medium |
| cf22 | has_attribute | item | decorative |  | modifier_attribute, visual_attribute | has_attribute:item:decorative | True | medium |
| cf23 | has_attribute | setting | indoor |  | modifier_attribute, visual_attribute | has_attribute:setting:indoor | True | medium |
| cf24 | action_event | display |  |  | visual_action | action_event:display | True | low |
| cf25 | event_role | display | agent | space |  | event_role:display:agent:space | True | medium |
| cf26 | event_role | display | patient | object |  | event_role:display:patient:object | True | medium |
| cf27 | action_event | illuminate |  |  | visual_action | action_event:illuminate | True | low |
| cf28 | event_role | illuminate | theme | wall |  | event_role:illuminate:theme:wall | True | medium |
| cf29 | event_role | illuminate | by_agent_or_causer | light |  | event_role:illuminate:by_agent_or_causer:light | True | medium |
| cf30 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf31 | event_role | sit | agent | vase |  | event_role:sit:agent:vase | True | medium |
| cf32 | action_event | arrange |  |  | visual_action | action_event:arrange | True | low |
| cf33 | event_role | arrange | theme | figurine |  | event_role:arrange:theme:figurine | True | medium |
| cf34 | event_role | arrange | theme | item |  | event_role:arrange:theme:item | True | medium |
| cf35 | relation | space | on | shelf | spatial_support, visual_relation | relation:space:on:shelf | True | high |
| cf36 | relation | space | on | pedestal | spatial_support, visual_relation | relation:space:on:pedestal | True | high |
| cf37 | relation | wall | by | light | spatial_proximity, visual_relation | relation:wall:by:light | False | medium |
| cf38 | relation | vase | on | pedestal | spatial_support, visual_relation | relation:vase:on:pedestal | True | high |
| cf39 | relation | figurine | across | shelf | spatial_path, visual_relation | relation:figurine:across:shelf | True | high |
| cf40 | relation | figurine | in | setting | spatial_containment, visual_relation | relation:figurine:in:setting | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m4 | object | jean | jeans | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:jean", "parents": []} |
| ent_m5 | object | plaque | plaque | document | raw_lemma | stage9_seed:parent_seed | text_carrier, artifact | m5 | raw_mention |  |  |  | True | {"canonical": "entity:plaque", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m7 | object | head | head | object | raw_lemma | stage9_seed:parent_seed | body_part | m7 | raw_mention |  |  |  | True | {"canonical": "entity:head", "parents": ["entity_parent:body_part"]} |
| ent_m8 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m8 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m11 | object | mask | masks | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m11 | raw_mention |  |  |  | True | {"canonical": "entity:mask", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m12 | object | tent | tent | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:tent", "parents": []} |
| ent_m14 | object | wall | wall | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | holds | hold | hold_up | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action | up | agent:m1->ent_m1; patient:m5->ent_m5 | {"canonical": "action:hold_up", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} | phrasal_action:hold up |
| ce1 | m17 | wearing | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m8->ent_m8; patient:m11->ent_m11 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce2 | m18 | clap | clap | clap | raw_action | stage9_seed:parent_seed | gesture_action, visual_action |  | agent:m8->ent_m8 | {"canonical": "action:clap", "parents": ["action_parent:gesture_action", "action_parent:visual_action"]} |  |
| ce3 | m19 | look | look | look | raw_action | stage9_seed:parent_seed | gaze_action, visual_action | on | agent:m8->ent_m8 | {"canonical": "action:look", "parents": ["action_parent:gaze_action", "action_parent:visual_action"]} |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e12 | False | False |  |  |
| cr1 | m1 | m4 | ent_m1 | ent_m4 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e13 | False | False |  |  |
| cr2 | m1 | m7 | ent_m1 | ent_m7 | above | above | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e14 | False | False |  |  |
| cr3 | m8 | m1 | ent_m8 | ent_m1 | around | around | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e15 | False | False |  |  |
| cr4 | m8 | m12 | ent_m8 | ent_m12 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf2 | entity_exists | jean |  |  |  | entity_exists:jean | True | low |
| cf3 | entity_exists | plaque |  |  | text_carrier, artifact | entity_exists:plaque | True | high |
| cf4 | entity_exists | head |  |  | body_part | entity_exists:head | True | high |
| cf5 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf6 | entity_exists | mask |  |  | clothing, wearable | entity_exists:mask | True | medium |
| cf7 | entity_exists | tent |  |  |  | entity_exists:tent | True | low |
| cf8 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf9 | has_attribute | shirt | white |  | color_attribute, color, visual_attribute | has_attribute:shirt:white | True | high |
| cf10 | has_attribute | plaque | frame |  | state_attribute, visual_attribute | has_attribute:plaque:frame | True | medium |
| cf11 | has_quantity | people | several |  | approximate_quantity, quantity | has_quantity:people:several | True | medium |
| cf12 | has_attribute | tent | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:tent:large | True | high |
| cf13 | action_event | hold_up |  |  | manipulation_action, visual_action | action_event:hold_up | True | high |
| cf14 | event_role | hold_up | agent | man |  | event_role:hold_up:agent:man | True | medium |
| cf15 | event_role | hold_up | patient | plaque |  | event_role:hold_up:patient:plaque | True | medium |
| cf16 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf17 | event_role | wear | agent | people |  | event_role:wear:agent:people | True | medium |
| cf18 | event_role | wear | patient | mask |  | event_role:wear:patient:mask | True | medium |
| cf19 | action_event | clap |  |  | gesture_action, visual_action | action_event:clap | True | high |
| cf20 | event_role | clap | agent | people |  | event_role:clap:agent:people | True | medium |
| cf21 | action_event | look |  |  | gaze_action, visual_action | action_event:look | True | high |
| cf22 | event_role | look | agent | people |  | event_role:look:agent:people | True | medium |
| cf23 | relation | man | in | shirt | spatial_containment, visual_relation | relation:man:in:shirt | True | high |
| cf24 | relation | man | in | jean | spatial_containment, visual_relation | relation:man:in:jean | True | high |
| cf25 | relation | man | above | head | spatial_vertical, visual_relation | relation:man:above:head | True | high |
| cf26 | relation | people | around | man | spatial_proximity, visual_relation | relation:people:around:man | True | high |
| cf27 | relation | people | under | tent | spatial_vertical, visual_relation | relation:people:under:tent | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | child | child | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | dress | dress | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:dress", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m4 | object | chair | chair | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m4 | raw_mention |  |  |  | True | {"canonical": "entity:chair", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m6 | object | curtain | Curtains | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:curtain", "parents": []} |
| ent_m7 | context | setting | setting | object | raw_lemma | stage9_seed:parent_seed | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:setting", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e5 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e6 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e7 | False | False |  |  |
| cr2 | m6 | m0 | ent_m6 | ent_m0 | behind | behind | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e8 | False | False |  |  |
| cr3 | m6 | m7 | ent_m6 | ent_m7 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf1 | entity_exists | dress |  |  | clothing, wearable | entity_exists:dress | True | high |
| cf2 | entity_exists | chair |  |  | furniture, artifact | entity_exists:chair | True | high |
| cf3 | entity_exists | curtain |  |  |  | entity_exists:curtain | True | low |
| cf4 | entity_exists | setting |  |  | scene_context | entity_exists:setting | True | high |
| cf5 | has_attribute | child | young |  | modifier_attribute, visual_attribute | has_attribute:child:young | True | medium |
| cf6 | has_attribute | dress | white |  | color_attribute, color, visual_attribute | has_attribute:dress:white | True | high |
| cf7 | has_attribute | chair | ornate |  | modifier_attribute, visual_attribute | has_attribute:chair:ornate | True | medium |
| cf8 | has_attribute | setting | studio |  | compound_modifier, visual_attribute | has_attribute:setting:studio | True | medium |
| cf9 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf10 | event_role | stand | agent | child |  | event_role:stand:agent:child | True | medium |
| cf11 | relation | child | in | dress | spatial_containment, visual_relation | relation:child:in:dress | True | high |
| cf12 | relation | child | on | chair | spatial_support, visual_relation | relation:child:on:chair | True | high |
| cf13 | relation | curtain | behind | child | spatial_depth, visual_relation | relation:curtain:behind:child | True | high |
| cf14 | relation | curtain | in | setting | spatial_containment, visual_relation | relation:curtain:in:setting | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | People | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | path | path | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:path", "parents": []} |
| ent_m3 | object | building | building | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | walk | walk | walk | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:walk", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | walk | agent | m0 | ent_m0 | medium | e4 | nsubj -> walk |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e5 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e6 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | path |  |  |  | entity_exists:path | True | low |
| cf2 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf3 | has_attribute | path | paved |  | visual_attribute | has_attribute:path:paved | True | medium |
| cf4 | has_attribute | building | royal |  | compound_modifier, visual_attribute | has_attribute:building:royal | True | medium |
| cf5 | has_attribute | building | festival |  | compound_modifier, visual_attribute | has_attribute:building:festival | True | medium |
| cf6 | has_attribute | building | hall |  | compound_modifier, visual_attribute | has_attribute:building:hall | True | medium |
| cf7 | action_event | walk |  |  | locomotion_action, visual_action | action_event:walk | True | high |
| cf8 | event_role | walk | agent | people |  | event_role:walk:agent:people | True | medium |
| cf9 | relation | people | on | path | spatial_support, visual_relation | relation:people:on:path | True | high |
| cf10 | relation | people | near | building | spatial_proximity, visual_relation | relation:people:near:building | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | canyon | canyon | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:canyon", "parents": []} |
| ent_m2 | object | cliff | cliffs | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:cliff", "parents": []} |
| ent_m4 | object | greenery | greenery | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:greenery", "parents": []} |
| ent_m6 | object | house | house | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:house", "parents": []} |
| ent_m9 | object | valley | valley | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:valley", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | sits | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m6->ent_m6 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m6 | ent_m6 | medium | e5 | nsubj -> sits |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e7 | False | False |  |  |
| cr2 | m6 | m9 | ent_m6 | ent_m9 | bottom_of | bottom_of | generated_region_pattern | generated_region_pattern | spatial_region, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | canyon |  |  |  | entity_exists:canyon | True | low |
| cf1 | entity_exists | cliff |  |  |  | entity_exists:cliff | True | low |
| cf2 | entity_exists | greenery |  |  |  | entity_exists:greenery | True | low |
| cf3 | entity_exists | house |  |  |  | entity_exists:house | True | low |
| cf4 | entity_exists | valley |  |  |  | entity_exists:valley | True | low |
| cf5 | has_attribute | canyon | rugged |  | modifier_attribute, visual_attribute | has_attribute:canyon:rugged | True | medium |
| cf6 | has_attribute | cliff | steep |  | modifier_attribute, visual_attribute | has_attribute:cliff:steep | True | medium |
| cf7 | has_attribute | greenery | sparse |  | modifier_attribute, visual_attribute | has_attribute:greenery:sparse | True | medium |
| cf8 | has_attribute | house | small |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:house:small | True | high |
| cf9 | has_attribute | house | white |  | color_attribute, color, visual_attribute | has_attribute:house:white | True | high |
| cf10 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf11 | event_role | sit | agent | house |  | event_role:sit:agent:house | True | medium |
| cf12 | relation | canyon | with | cliff | association_relation, visual_relation | relation:canyon:with:cliff | True | high |
| cf13 | relation | canyon | with | greenery | association_relation, visual_relation | relation:canyon:with:greenery | True | high |
| cf14 | relation | house | bottom_of | valley | spatial_region, visual_relation | relation:house:bottom_of:valley | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | tree | tree | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m2 | object | relationship | relationships | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:relationship", "parents": []} |
| ent_m4 | object | rodent | rodents | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:rodent", "parents": []} |
| ent_m5 | object | icon | icons | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:icon", "parents": []} |
| ent_m6 | object | rabbit | rabbit | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:rabbit", "parents": []} |
| ent_m8 | object | rodent | rodent | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:rodent", "parents": []} |
| ent_m10 | object | graph | graph | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:graph", "parents": []} |
| ent_m11 | object | temperature | temperature | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:temperature", "parents": []} |
| ent_m13 | object | change | changes | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:change", "parents": []} |
| ent_m15 | object | time | time | object | raw_lemma | none |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:time", "parents": []} |
| ent_m16 | object | event | events | object | raw_lemma | none |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:event", "parents": []} |
| ent_m18 | object | origin | origin | object | raw_lemma | none |  | m18 | raw_mention |  |  |  | True | {"canonical": "entity:origin", "parents": []} |
| ent_m21 | object | expansion | expansion | object | raw_lemma | none |  | m21 | raw_mention |  |  |  | True | {"canonical": "entity:expansion", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m23 | shows | show | show | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m2->ent_m2 | {"canonical": "action:show", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m24 | tracks | track | track | raw_action | visual_action_fallback | visual_action |  | agent:m10->ent_m10; patient:m11->ent_m11; patient:m13->ent_m13 | {"canonical": "action:track", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m25 | marked | mark | mark | raw_action | visual_action_fallback | visual_action |  | agent:m10->ent_m10 | {"canonical": "action:mark", "parents": ["action_parent:visual_action"]} |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m2 | m4 | ent_m2 | ent_m4 | among | among | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_region, visual_relation | medium | e16 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e17 | False | False |  |  |
| cr2 | m5 | m6 | ent_m5 | ent_m6 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e18 | False | False |  |  |
| cr3 | m5 | m8 | ent_m5 | ent_m8 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e19 | False | False |  |  |
| cr4 | m11 | m15 | ent_m11 | ent_m15 | over | above | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e20 | False | False |  |  |
| cr5 | m10 | m16 | ent_m10 | ent_m16 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e21 | False | False |  |  |
| cr6 | m16 | m18 | ent_m16 | ent_m18 | like | like | raw_relation | raw_relation | visual_relation | medium | e22 | False | False |  |  |
| cr7 | m16 | m21 | ent_m16 | ent_m21 | like | like | raw_relation | raw_relation | visual_relation | medium | e23 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf1 | entity_exists | relationship |  |  |  | entity_exists:relationship | True | low |
| cf2 | entity_exists | rodent |  |  |  | entity_exists:rodent | True | low |
| cf3 | entity_exists | icon |  |  |  | entity_exists:icon | True | low |
| cf4 | entity_exists | rabbit |  |  |  | entity_exists:rabbit | True | low |
| cf5 | entity_exists | rodent |  |  |  | entity_exists:rodent | True | low |
| cf6 | entity_exists | graph |  |  |  | entity_exists:graph | True | low |
| cf7 | entity_exists | temperature |  |  |  | entity_exists:temperature | True | low |
| cf8 | entity_exists | change |  |  |  | entity_exists:change | True | low |
| cf9 | entity_exists | time |  |  |  | entity_exists:time | True | low |
| cf10 | entity_exists | event |  |  |  | entity_exists:event | True | low |
| cf11 | entity_exists | origin |  |  |  | entity_exists:origin | True | low |
| cf12 | entity_exists | expansion |  |  |  | entity_exists:expansion | True | low |
| cf13 | has_attribute | tree | phylogenetic |  | modifier_attribute, visual_attribute | has_attribute:tree:phylogenetic | True | medium |
| cf14 | has_attribute | relationship | evolutionary |  | modifier_attribute, visual_attribute | has_attribute:relationship:evolutionary | True | medium |
| cf15 | has_attribute | rabbit | leporid |  | modifier_attribute, visual_attribute | has_attribute:rabbit:leporid | True | medium |
| cf16 | has_attribute | rodent | ocotoid |  | compound_modifier, visual_attribute | has_attribute:rodent:ocotoid | True | medium |
| cf17 | has_attribute | temperature | global |  | modifier_attribute, visual_attribute | has_attribute:temperature:global | True | medium |
| cf18 | has_attribute | change | vegetation |  | compound_modifier, visual_attribute | has_attribute:change:vegetation | True | medium |
| cf19 | has_attribute | event | key |  | modifier_attribute, visual_attribute | has_attribute:event:key | True | medium |
| cf20 | has_attribute | origin | c3 |  | compound_modifier, visual_attribute | has_attribute:origin:c3 | True | medium |
| cf21 | has_attribute | origin | grass |  | compound_modifier, visual_attribute | has_attribute:origin:grass | True | medium |
| cf22 | has_attribute | expansion | c4 |  | compound_modifier, visual_attribute | has_attribute:expansion:c4 | True | medium |
| cf23 | action_event | show |  |  | visual_action | action_event:show | True | low |
| cf24 | event_role | show | agent | tree |  | event_role:show:agent:tree | True | medium |
| cf25 | event_role | show | patient | relationship |  | event_role:show:patient:relationship | True | medium |
| cf26 | action_event | track |  |  | visual_action | action_event:track | True | low |
| cf27 | event_role | track | agent | graph |  | event_role:track:agent:graph | True | medium |
| cf28 | event_role | track | patient | temperature |  | event_role:track:patient:temperature | True | medium |
| cf29 | event_role | track | patient | change |  | event_role:track:patient:change | True | medium |
| cf30 | action_event | mark |  |  | visual_action | action_event:mark | True | low |
| cf31 | event_role | mark | agent | graph |  | event_role:mark:agent:graph | True | medium |
| cf32 | relation | relationship | among | rodent | spatial_region, visual_relation | relation:relationship:among:rodent | True | medium |
| cf33 | relation | tree | with | icon | association_relation, visual_relation | relation:tree:with:icon | True | high |
| cf34 | relation | icon | of | rabbit | part_relation, visual_relation | relation:icon:of:rabbit | True | medium |
| cf35 | relation | icon | of | rodent | part_relation, visual_relation | relation:icon:of:rodent | True | medium |
| cf36 | relation | temperature | above | time | spatial_vertical, visual_relation | relation:temperature:above:time | True | high |
| cf37 | relation | graph | with | event | association_relation, visual_relation | relation:graph:with:event | True | high |
| cf38 | relation | event | like | origin | visual_relation | relation:event:like:origin | True | medium |
| cf39 | relation | event | like | expansion | visual_relation | relation:event:like:expansion | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e20 |  |  |  | {"canonical": "above", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e20", "raw_relation": "over", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | vest | vest | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:vest", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m4 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m4 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m5 | object | corset | corset | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:corset", "parents": []} |
| ent_m7 | object | party | party | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:party", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e3 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e4 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | next_to | next_to | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e5 | False | False |  |  |
| cr2 | m4 | m5 | ent_m4 | ent_m5 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e6 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | vest |  |  | clothing, wearable | entity_exists:vest | True | high |
| cf2 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf3 | entity_exists | corset |  |  |  | entity_exists:corset | True | low |
| cf4 | entity_exists | party |  |  |  | entity_exists:party | True | low |
| cf5 | has_attribute | vest | blue |  | color_attribute, color, visual_attribute | has_attribute:vest:blue | True | high |
| cf6 | has_attribute | vest | gray |  | color_attribute, color, visual_attribute | has_attribute:vest:gray | True | high |
| cf7 | has_attribute | corset | gray |  | color_attribute, color, visual_attribute | has_attribute:corset:gray | True | high |
| cf8 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf9 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf10 | relation | man | in | vest | spatial_containment, visual_relation | relation:man:in:vest | True | high |
| cf11 | relation | man | next_to | woman | spatial_proximity, visual_relation | relation:man:next_to:woman | True | high |
| cf12 | relation | woman | in | corset | spatial_containment, visual_relation | relation:woman:in:corset | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | suit | suit | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:suit", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m4 | object | tie | tie | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:tie", "parents": []} |
| ent_m5 | object | podium | podium | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:podium", "parents": []} |
| ent_m7 | object | right_hand | right hand | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:right_hand", "parents": []} |
| ent_m8 | object | backdrop | backdrop | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:backdrop", "parents": []} |
| ent_m11 | object | logo | logo | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:logo", "parents": []} |
| ent_m12 | object | glass | glasses | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:glass", "parents": []} |
| ent_m13 | object | lanyard | lanyard | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:lanyard", "parents": []} |
| ent_m14 | object | neck | neck | object | raw_lemma | stage9_seed:parent_seed | body_part | m14 | raw_mention |  |  |  | True | {"canonical": "entity:neck", "parents": ["entity_parent:body_part"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m16 | waving | wave | wave | raw_action | visual_action_fallback | visual_action |  | agent:m1->ent_m1 | {"canonical": "action:wave", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m17 | repeated | repeat | repeat | raw_action | visual_action_fallback | visual_action |  | agent:m11->ent_m11 | {"canonical": "action:repeat", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m18 | wears | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m1->ent_m1; patient:m12->ent_m12 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce4 | m19 | has | have | have | raw_action | visual_action_fallback | visual_action |  | agent:m1->ent_m1; patient:m13->ent_m13 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e11 | False | False |  |  |
| cr1 | m1 | m4 | ent_m1 | ent_m4 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e12 | False | False |  |  |
| cr2 | m1 | m5 | ent_m1 | ent_m5 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e13 | False | False |  |  |
| cr3 | m1 | m7 | ent_m1 | ent_m7 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr4 | m8 | m1 | ent_m8 | ent_m1 | behind | behind | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e15 | False | False |  |  |
| cr5 | m8 | m11 | ent_m8 | ent_m11 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e16 | False | False |  |  |
| cr6 | m11 | m8 | ent_m11 | ent_m8 | across | across | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | high | e17 | False | False |  |  |
| cr7 | m1 | m14 | ent_m1 | ent_m14 | around | around | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e18 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | suit |  |  | clothing, wearable | entity_exists:suit | True | high |
| cf2 | entity_exists | tie |  |  |  | entity_exists:tie | True | low |
| cf3 | entity_exists | podium |  |  |  | entity_exists:podium | True | low |
| cf4 | entity_exists | right_hand |  |  |  | entity_exists:right_hand | True | high |
| cf5 | entity_exists | backdrop |  |  |  | entity_exists:backdrop | True | low |
| cf6 | entity_exists | logo |  |  |  | entity_exists:logo | True | low |
| cf7 | entity_exists | glass |  |  |  | entity_exists:glass | True | low |
| cf8 | entity_exists | lanyard |  |  |  | entity_exists:lanyard | True | low |
| cf9 | entity_exists | neck |  |  | body_part | entity_exists:neck | True | high |
| cf10 | has_attribute | suit | blue |  | color_attribute, color, visual_attribute | has_attribute:suit:blue | True | high |
| cf11 | has_attribute | podium | clear |  | weather_attribute, opaqeness, weather, visual_attribute | has_attribute:podium:clear | True | medium |
| cf12 | has_attribute | backdrop | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:backdrop:large | True | high |
| cf13 | has_attribute | backdrop | white |  | color_attribute, color, visual_attribute | has_attribute:backdrop:white | True | high |
| cf14 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf15 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf16 | action_event | wave |  |  | visual_action | action_event:wave | True | low |
| cf17 | event_role | wave | agent | man |  | event_role:wave:agent:man | True | medium |
| cf18 | action_event | repeat |  |  | visual_action | action_event:repeat | True | low |
| cf19 | event_role | repeat | agent | logo |  | event_role:repeat:agent:logo | True | medium |
| cf20 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf21 | event_role | wear | agent | man |  | event_role:wear:agent:man | True | medium |
| cf22 | event_role | wear | patient | glass |  | event_role:wear:patient:glass | True | medium |
| cf23 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf24 | event_role | have | agent | man |  | event_role:have:agent:man | True | medium |
| cf25 | event_role | have | patient | lanyard |  | event_role:have:patient:lanyard | True | medium |
| cf26 | relation | man | in | suit | spatial_containment, visual_relation | relation:man:in:suit | True | high |
| cf27 | relation | man | in | tie | spatial_containment, visual_relation | relation:man:in:tie | True | high |
| cf28 | relation | man | at | podium | spatial_location, visual_relation | relation:man:at:podium | True | medium |
| cf29 | relation | man | with | right_hand | association_relation, visual_relation | relation:man:with:right_hand | True | high |
| cf30 | relation | backdrop | behind | man | spatial_depth, visual_relation | relation:backdrop:behind:man | True | high |
| cf31 | relation | backdrop | with | logo | association_relation, visual_relation | relation:backdrop:with:logo | True | high |
| cf32 | relation | logo | across | backdrop | spatial_path, visual_relation | relation:logo:across:backdrop | True | high |
| cf33 | relation | man | around | neck | spatial_proximity, visual_relation | relation:man:around:neck | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | machine | machine | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:machine", "parents": []} |
| ent_m3 | object | room | room | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:room", "parents": []} |
| ent_m6 | object | wall | walls | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |
| ent_m8 | object | pipe | pipes | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:pipe", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e5 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e6 | False | False |  |  |
| cr1 | m3 | m6 | ent_m3 | ent_m6 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e7 | False | False |  |  |
| cr2 | m3 | m8 | ent_m3 | ent_m8 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | machine |  |  |  | entity_exists:machine | True | low |
| cf1 | entity_exists | room |  |  |  | entity_exists:room | True | low |
| cf2 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf3 | entity_exists | pipe |  |  |  | entity_exists:pipe | True | low |
| cf4 | has_attribute | machine | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:machine:large | True | high |
| cf5 | has_attribute | machine | old |  | condition_attribute, clean_exact_overlap, maturity, newness, visual_attribute | has_attribute:machine:old | True | medium |
| cf6 | has_attribute | room | dimly |  | modifier_attribute, visual_attribute | has_attribute:room:dimly | True | medium |
| cf7 | has_attribute | room | light |  | visual_attribute | has_attribute:room:light | True | medium |
| cf8 | has_attribute | wall | brick |  | material_attribute, material, visual_attribute | has_attribute:wall:brick | True | high |
| cf9 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf10 | event_role | stand | agent | machine |  | event_role:stand:agent:machine | True | medium |
| cf11 | relation | machine | in | room | spatial_containment, visual_relation | relation:machine:in:room | True | high |
| cf12 | relation | room | with | wall | association_relation, visual_relation | relation:room:with:wall | True | high |
| cf13 | relation | room | with | pipe | association_relation, visual_relation | relation:room:with:pipe | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sports_car | sports car | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:sports_car", "parents": []} |
| ent_m1 | object | number | number | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:number", "parents": []} |
| ent_m2 | object | racetrack | racetrack | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:racetrack", "parents": []} |
| ent_m3 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m3 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m5 | object | jacket | jacket | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m5 | raw_mention |  |  |  | True | {"canonical": "entity:jacket", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m7 | object | jacket | jacket | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m7 | raw_mention |  |  |  | True | {"canonical": "entity:jacket", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m9 | object | paved_surface | paved surface | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:paved_surface", "parents": []} |
| ent_m10 | object | hill | hills | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:hill", "parents": []} |
| ent_m11 | object | tree | trees | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m12 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m12 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| eref_m13 | instance | people | one | person | raw_lemma | stage9_seed:parent_seed | person, human | m13 | stage9_reference | ent_m3 |  | 1 | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| eref_m14 | contrastive_instance | people | another | person | raw_lemma | stage9_seed:parent_seed | person, human | m14 | stage9_reference | ent_m3 |  | 1 | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m13 | eref_m13 | m3 | ent_m3 | high |  |
| refers_to | m14 | eref_m14 | m3 | ent_m3 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | parked | park | park | raw_action | visual_action_fallback | visual_action |  | theme:m0->ent_m0 | {"canonical": "action:park", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m16 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m3->ent_m3 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | park | theme | m0 | ent_m0 | medium | e6 | nsubjpass -> parked |  |  |
| ce1 | stand | agent | m3 | ent_m3 | medium | e7 | nsubj -> stand |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e8 | False | False |  |  |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e9 | False | False |  |  |
| cr2 | m3 | m0 | ent_m3 | ent_m0 | next_to | next_to | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e10 | False | False |  |  |
| cr3 | m3 | m5 | eref_m13 | ent_m5 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e11 | False | False |  |  |
| cr4 | m3 | m7 | eref_m14 | ent_m7 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e12 | False | False |  |  |
| cr5 | m3 | m9 | ent_m3 | ent_m9 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e13 | False | False |  |  |
| cr6 | m9 | m10 | ent_m9 | ent_m10 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr7 | m9 | m11 | ent_m9 | ent_m11 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e15 | False | False |  |  |
| cr8 | m10 | m12 | ent_m10 | ent_m12 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | sports_car |  |  |  | entity_exists:sports_car | True | high |
| cf1 | entity_exists | number |  |  |  | entity_exists:number | True | low |
| cf2 | entity_exists | racetrack |  |  |  | entity_exists:racetrack | True | low |
| cf3 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf4 | entity_exists | jacket |  |  | clothing, wearable | entity_exists:jacket | True | high |
| cf5 | entity_exists | jacket |  |  | clothing, wearable | entity_exists:jacket | True | high |
| cf6 | entity_exists | paved_surface |  |  |  | entity_exists:paved_surface | True | high |
| cf7 | entity_exists | hill |  |  |  | entity_exists:hill | True | low |
| cf8 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf9 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf10 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf11 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf12 | has_quantity | people | two |  | exact_quantity, quantity | has_quantity:people:two | True | high |
| cf13 | has_attribute | jacket | blue |  | color_attribute, color, visual_attribute | has_attribute:jacket:blue | True | high |
| cf14 | has_attribute | jacket | black |  | color_attribute, color, visual_attribute | has_attribute:jacket:black | True | high |
| cf15 | action_event | park |  |  | visual_action | action_event:park | True | low |
| cf16 | event_role | park | theme | sports_car |  | event_role:park:theme:sports_car | True | medium |
| cf17 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf18 | event_role | stand | agent | people |  | event_role:stand:agent:people | True | medium |
| cf19 | relation | sports_car | with | number | association_relation, visual_relation | relation:sports_car:with:number | True | high |
| cf20 | relation | sports_car | on | racetrack | spatial_support, visual_relation | relation:sports_car:on:racetrack | True | high |
| cf21 | relation | people | next_to | sports_car | spatial_proximity, visual_relation | relation:people:next_to:sports_car | True | high |
| cf22 | relation | people | in | jacket | spatial_containment, visual_relation | relation:people:in:jacket | True | high |
| cf23 | relation | people | in | jacket | spatial_containment, visual_relation | relation:people:in:jacket | True | high |
| cf24 | relation | people | on | paved_surface | spatial_support, visual_relation | relation:people:on:paved_surface | True | high |
| cf25 | relation | paved_surface | with | hill | association_relation, visual_relation | relation:paved_surface:with:hill | True | high |
| cf26 | relation | paved_surface | with | tree | association_relation, visual_relation | relation:paved_surface:with:tree | True | high |
| cf27 | relation | hill | in | background | spatial_containment, visual_relation | relation:hill:in:background | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | list | list | document | raw_lemma | stage9_seed:parent_seed | document, text_carrier, artifact | m1 | raw_mention |  |  |  | True | {"canonical": "entity:list", "parents": ["entity_parent:document", "entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m3 | object | paper | paper | document | raw_lemma | stage9_seed:parent_seed | document, text_carrier, artifact | m3 | raw_mention |  |  |  | True | {"canonical": "entity:paper", "parents": ["entity_parent:document", "entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m5 | object | name | names | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:name", "parents": []} |
| ent_m6 | object | detail | details | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:detail", "parents": []} |
| ent_m7 | object | format | format | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:format", "parents": []} |
| ent_m9 | object | document | document | document | raw_lemma | stage9_seed:parent_seed | document, text_carrier, artifact | m9 | raw_mention |  |  |  | False | {"canonical": "entity:document", "parents": ["entity_parent:document", "entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m10 | context | top | top | object | raw_lemma | semantic_type_fallback | scene_context | m10 | raw_mention |  |  |  | True | {"canonical": "entity:top", "parents": ["entity_parent:scene_context"]} |
| ent_m11 | object | text | text | document | raw_lemma | stage9_seed:parent_seed | text_content | m11 | raw_mention |  |  |  | True | {"canonical": "entity:text", "parents": ["entity_parent:text_content"]} |
| ent_m13 | object | entry | entries | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:entry", "parents": []} |
| ent_m15 | object | hand | hand | object | raw_lemma | stage9_seed:parent_seed | body_part | m15 | raw_mention |  |  |  | True | {"canonical": "entity:hand", "parents": ["entity_parent:body_part"]} |
| ent_m16 | object | date | dates | object | raw_lemma | none |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:date", "parents": []} |
| ent_m17 | object | signature | signatures | object | raw_lemma | none |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:signature", "parents": []} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| generic_alias | m9 | ent_m9 |  | ent_m3 | medium |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | shows | show | show | raw_action | visual_action_fallback | visual_action |  | agent:m1->ent_m1; patient:m5->ent_m5; patient:m6->ent_m6 | {"canonical": "action:show", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m19 | labeled | label | label | raw_action | visual_action_fallback | visual_action |  | theme:m9->ent_m3; patient:m0->None | {"canonical": "action:label", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m20 | typed | type | type | raw_action | visual_action_fallback | visual_action |  |  | {"canonical": "action:type", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m21 | filled | fill | fill | raw_action | visual_action_fallback | visual_action | out | theme:m13->ent_m13; by_agent_or_causer:m15->ent_m15 | {"canonical": "action:fill", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m23 | including | include | include | raw_action | visual_action_fallback | visual_action |  | agent:m13->ent_m13; patient:m16->ent_m16; patient:m17->ent_m17 | {"canonical": "action:include", "parents": ["action_parent:visual_action"]} |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m3 | ent_m1 | ent_m3 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e15 | False | False |  |  |
| cr1 | m1 | m7 | ent_m1 | ent_m7 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e16 | False | False |  |  |
| cr2 | m9 | m10 | ent_m3 | ent_m10 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e17 | False | False |  |  |
| cr3 | m9 | m11 | ent_m3 | ent_m11 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e18 | False | False |  |  |
| cr4 | m13 | m15 | ent_m13 | ent_m15 | by | by | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | medium | e19 | True | False |  |  |
| cr5 | m13 | m16 | ent_m13 | ent_m16 | include | include | raw_relation | raw_relation | visual_relation | medium | e20 | False | False |  |  |
| cr6 | m13 | m17 | ent_m13 | ent_m17 | include | include | raw_relation | raw_relation | visual_relation | medium | e21 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | list |  |  | document, text_carrier, artifact | entity_exists:list | True | medium |
| cf1 | entity_exists | paper |  |  | document, text_carrier, artifact | entity_exists:paper | True | high |
| cf2 | entity_exists | name |  |  |  | entity_exists:name | True | low |
| cf3 | entity_exists | detail |  |  |  | entity_exists:detail | True | low |
| cf4 | entity_exists | format |  |  |  | entity_exists:format | True | low |
| cf5 | entity_exists | top |  |  | scene_context | entity_exists:top | True | medium |
| cf6 | entity_exists | text |  |  | text_content | entity_exists:text | True | high |
| cf7 | entity_exists | entry |  |  |  | entity_exists:entry | True | low |
| cf8 | entity_exists | hand |  |  | body_part | entity_exists:hand | True | high |
| cf9 | entity_exists | date |  |  |  | entity_exists:date | True | low |
| cf10 | entity_exists | signature |  |  |  | entity_exists:signature | True | low |
| cf11 | has_attribute | list | handwritten |  | modifier_attribute, visual_attribute | has_attribute:list:handwritten | True | medium |
| cf12 | has_attribute | paper | lined |  | pattern_attribute, pattern, texture, visual_attribute | has_attribute:paper:lined | True | medium |
| cf13 | has_attribute | format | table |  | compound_modifier, visual_attribute | has_attribute:format:table | True | medium |
| cf14 | has_attribute | text | print |  | state_attribute, visual_attribute | has_attribute:text:print | True | medium |
| cf15 | has_quantity | entry | several |  | approximate_quantity, quantity | has_quantity:entry:several | True | medium |
| cf16 | action_event | show |  |  | visual_action | action_event:show | True | low |
| cf17 | event_role | show | agent | list |  | event_role:show:agent:list | True | medium |
| cf18 | event_role | show | patient | name |  | event_role:show:patient:name | True | medium |
| cf19 | event_role | show | patient | detail |  | event_role:show:patient:detail | True | medium |
| cf20 | action_event | label |  |  | visual_action | action_event:label | True | low |
| cf21 | event_role | label | theme | paper |  | event_role:label:theme:paper | True | medium |
| cf22 | event_role | label | patient |  |  | event_role:label:patient | False | medium |
| cf23 | action_event | type |  |  | visual_action | action_event:type | True | low |
| cf24 | action_event | fill |  |  | visual_action | action_event:fill | True | low |
| cf25 | event_role | fill | theme | entry |  | event_role:fill:theme:entry | True | medium |
| cf26 | event_role | fill | by_agent_or_causer | hand |  | event_role:fill:by_agent_or_causer:hand | True | medium |
| cf27 | action_event | include |  |  | visual_action | action_event:include | True | low |
| cf28 | event_role | include | agent | entry |  | event_role:include:agent:entry | True | medium |
| cf29 | event_role | include | patient | date |  | event_role:include:patient:date | True | medium |
| cf30 | event_role | include | patient | signature |  | event_role:include:patient:signature | True | medium |
| cf31 | relation | list | on | paper | spatial_support, visual_relation | relation:list:on:paper | True | high |
| cf32 | relation | list | in | format | spatial_containment, visual_relation | relation:list:in:format | True | high |
| cf33 | relation | paper | at | top | spatial_location, visual_relation | relation:paper:at:top | True | medium |
| cf34 | relation | paper | with | text | association_relation, visual_relation | relation:paper:with:text | True | high |
| cf35 | relation | entry | by | hand | spatial_proximity, visual_relation | relation:entry:by:hand | False | medium |
| cf36 | relation | entry | include | date | visual_relation | relation:entry:include:date | True | medium |
| cf37 | relation | entry | include | signature | visual_relation | relation:entry:include:signature | True | medium |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | path | path | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:path", "parents": []} |
| ent_m2 | object | tree | trees | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m3 | object | lake | lake | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:lake", "parents": []} |
| ent_m4 | object | fence | fence | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:fence", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf1 | entity_exists | path |  |  |  | entity_exists:path | True | low |
| cf2 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf3 | entity_exists | lake |  |  |  | entity_exists:lake | True | low |
| cf4 | entity_exists | fence |  |  |  | entity_exists:fence | True | low |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | man | men | person | stage9_seed:synonym_seed | stage9_seed:parent_seed | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m3 | object | suit | suits | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m3 | raw_mention |  |  |  | True | {"canonical": "entity:suit", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m4 | object | podium | podium | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:podium", "parents": []} |
| ent_m5 | object | microphone | microphone | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:microphone", "parents": []} |
| ent_m6 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m6 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m8 | object | flag | flags | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:flag", "parents": []} |
| ent_m9 | object | wall | wall | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |
| ent_m11 | object | plaque | plaque | document | raw_lemma | stage9_seed:parent_seed | text_carrier, artifact | m11 | raw_mention |  |  |  | True | {"canonical": "entity:plaque", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m12 | object | podium | podium | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:podium", "parents": []} |
| eref_m13 | complement_subset | man | others | person | raw_lemma | stage9_seed:parent_seed | person, human | m13 | stage9_reference | ent_m1 |  | many | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m13 | eref_m13 | m1 | ent_m1 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m14 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m15 | speaks | speak | speak | raw_action | stage9_seed:parent_seed | communication_action, visual_action |  | agent:m6->ent_m6 | {"canonical": "action:speak", "parents": ["action_parent:communication_action", "action_parent:visual_action"]} |  |
| ce2 | m16 | listen | listen | listen | raw_action | visual_action_fallback | visual_action |  | agent:m1->eref_m13 | {"canonical": "action:listen", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m17 | positioned | position | position | raw_action | visual_action_fallback | visual_action |  | agent:m6->ent_m6 | {"canonical": "action:position", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m18 | reads | read | read | raw_action | stage9_seed:parent_seed | text_interaction_action, visual_action |  | agent:m11->ent_m11; patient:m0->None | {"canonical": "action:read", "parents": ["action_parent:text_interaction_action", "action_parent:visual_action"]} |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m3 | ent_m1 | ent_m3 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e10 | False | False |  |  |
| cr1 | m1 | m4 | ent_m1 | ent_m4 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e11 | False | False |  |  |
| cr2 | m1 | m5 | ent_m1 | ent_m5 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e12 | False | False |  |  |
| cr3 | m6 | m8 | ent_m6 | ent_m8 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e13 | False | False |  |  |
| cr4 | m6 | m9 | ent_m6 | ent_m9 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e14 | False | False |  |  |
| cr5 | m11 | m12 | ent_m11 | ent_m12 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e15 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | suit |  |  | clothing, wearable | entity_exists:suit | True | high |
| cf2 | entity_exists | podium |  |  |  | entity_exists:podium | True | low |
| cf3 | entity_exists | microphone |  |  |  | entity_exists:microphone | True | low |
| cf4 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf5 | entity_exists | flag |  |  |  | entity_exists:flag | True | low |
| cf6 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf7 | entity_exists | plaque |  |  | text_carrier, artifact | entity_exists:plaque | True | high |
| cf8 | entity_exists | podium |  |  |  | entity_exists:podium | True | low |
| cf9 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf10 | has_quantity | man | three |  | exact_quantity, quantity | has_quantity:man:three | True | high |
| cf11 | has_quantity | man | one |  | exact_quantity, quantity | has_quantity:man:one | True | high |
| cf12 | has_attribute | wall | marble |  | material_attribute, material, visual_attribute | has_attribute:wall:marble | True | medium |
| cf13 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf14 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf15 | action_event | speak |  |  | communication_action, visual_action | action_event:speak | True | medium |
| cf16 | event_role | speak | agent | man |  | event_role:speak:agent:man | True | medium |
| cf17 | action_event | listen |  |  | visual_action | action_event:listen | True | low |
| cf18 | event_role | listen | agent | man |  | event_role:listen:agent:man | True | medium |
| cf19 | action_event | position |  |  | visual_action | action_event:position | True | low |
| cf20 | event_role | position | agent | man |  | event_role:position:agent:man | True | medium |
| cf21 | action_event | read |  |  | text_interaction_action, visual_action | action_event:read | True | medium |
| cf22 | event_role | read | agent | plaque |  | event_role:read:agent:plaque | True | medium |
| cf23 | event_role | read | patient |  |  | event_role:read:patient | False | medium |
| cf24 | relation | man | in | suit | spatial_containment, visual_relation | relation:man:in:suit | True | high |
| cf25 | relation | man | at | podium | spatial_location, visual_relation | relation:man:at:podium | True | medium |
| cf26 | relation | man | with | microphone | association_relation, visual_relation | relation:man:with:microphone | True | high |
| cf27 | relation | man | near | flag | spatial_proximity, visual_relation | relation:man:near:flag | True | high |
| cf28 | relation | man | near | wall | spatial_proximity, visual_relation | relation:man:near:wall | True | high |
| cf29 | relation | plaque | on | podium | spatial_support, visual_relation | relation:plaque:on:podium | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | figurine | figurines | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:figurine", "parents": []} |
| ent_m4 | context | surface | surface | object | raw_lemma | semantic_type_fallback | scene_context | m4 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": ["entity_parent:scene_context"]} |
| ent_m5 | object | angel | angel | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:angel", "parents": []} |
| ent_m7 | context | foreground | foreground | object | raw_lemma | stage9_seed:parent_seed | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:foreground", "parents": ["entity_parent:scene_context"]} |
| ent_m8 | object | trim | trim | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:trim", "parents": []} |
| ent_m10 | object | head | head | object | raw_lemma | stage9_seed:parent_seed | body_part | m10 | raw_mention |  |  |  | True | {"canonical": "entity:head", "parents": ["entity_parent:body_part"]} |
| ent_m11 | object | wing | wings | object | raw_lemma | stage9_seed:parent_seed | body_part | m11 | raw_mention |  |  |  | True | {"canonical": "entity:wing", "parents": ["entity_parent:body_part"]} |
| ent_m13 | object | tag | tags | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:tag", "parents": []} |
| ent_m15 | object | sale | sale | object | raw_lemma | none |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:sale", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | displayed | display | display | raw_action | visual_action_fallback | visual_action |  | theme:m0->ent_m0 | {"canonical": "action:display", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m17 | has | have | have | raw_action | visual_action_fallback | visual_action |  | agent:m5->ent_m5; patient:m8->ent_m8 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m18 | lying | lie | lie | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m5->ent_m5 | {"canonical": "action:lie", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce3 | m19 | spread | spread | spread | raw_action | visual_action_fallback | visual_action |  | agent:m11->ent_m11 | {"canonical": "action:spread", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m20 | have | have | have | raw_action | visual_action_fallback | visual_action |  |  | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |
| ce5 | m21 | attached | attach | attach | raw_action | visual_action_fallback | visual_action |  | agent:m13->ent_m13 | {"canonical": "action:attach", "parents": ["action_parent:visual_action"]} |  |
| ce6 | m22 | suggesting | suggest | suggest | raw_action | visual_action_fallback | visual_action |  |  | {"canonical": "action:suggest", "parents": ["action_parent:visual_action"]} |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e13 | False | False |  |  |
| cr1 | m5 | m7 | ent_m5 | ent_m7 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e14 | False | False |  |  |
| cr2 | m5 | m10 | ent_m5 | ent_m10 | around | around | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e15 | False | False |  |  |
| cr3 | m11 | m15 | ent_m11 | ent_m15 | for | for | raw_relation | raw_relation | visual_relation | medium | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | figurine |  |  |  | entity_exists:figurine | True | low |
| cf1 | entity_exists | surface |  |  | scene_context | entity_exists:surface | True | medium |
| cf2 | entity_exists | angel |  |  |  | entity_exists:angel | True | low |
| cf3 | entity_exists | foreground |  |  | scene_context | entity_exists:foreground | True | high |
| cf4 | entity_exists | trim |  |  |  | entity_exists:trim | True | low |
| cf5 | entity_exists | head |  |  | body_part | entity_exists:head | True | high |
| cf6 | entity_exists | wing |  |  | body_part | entity_exists:wing | True | medium |
| cf7 | entity_exists | tag |  |  |  | entity_exists:tag | True | low |
| cf8 | entity_exists | sale |  |  |  | entity_exists:sale | True | low |
| cf9 | has_quantity | figurine | many |  | approximate_quantity, quantity | has_quantity:figurine:many | True | medium |
| cf10 | has_attribute | figurine | white |  | color_attribute, color, visual_attribute | has_attribute:figurine:white | True | high |
| cf11 | has_attribute | figurine | angel |  | compound_modifier, visual_attribute | has_attribute:figurine:angel | True | medium |
| cf12 | has_quantity | angel | one |  | exact_quantity, quantity | has_quantity:angel:one | True | high |
| cf13 | has_attribute | trim | gold |  | color_attribute, color, visual_attribute | has_attribute:trim:gold | True | high |
| cf14 | has_attribute | tag | small |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:tag:small | True | high |
| cf15 | action_event | display |  |  | visual_action | action_event:display | True | low |
| cf16 | event_role | display | theme | figurine |  | event_role:display:theme:figurine | True | medium |
| cf17 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf18 | event_role | have | agent | angel |  | event_role:have:agent:angel | True | medium |
| cf19 | event_role | have | patient | trim |  | event_role:have:patient:trim | True | medium |
| cf20 | action_event | lie |  |  | body_pose_action, visual_action | action_event:lie | True | high |
| cf21 | event_role | lie | agent | angel |  | event_role:lie:agent:angel | True | medium |
| cf22 | action_event | spread |  |  | visual_action | action_event:spread | True | low |
| cf23 | event_role | spread | agent | wing |  | event_role:spread:agent:wing | True | medium |
| cf24 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf25 | action_event | attach |  |  | visual_action | action_event:attach | True | low |
| cf26 | event_role | attach | agent | tag |  | event_role:attach:agent:tag | True | medium |
| cf27 | action_event | suggest |  |  | visual_action | action_event:suggest | True | low |
| cf28 | relation | figurine | on | surface | spatial_support, visual_relation | relation:figurine:on:surface | True | high |
| cf29 | relation | angel | in | foreground | spatial_containment, visual_relation | relation:angel:in:foreground | True | high |
| cf30 | relation | angel | around | head | spatial_proximity, visual_relation | relation:angel:around:head | True | high |
| cf31 | relation | wing | for | sale | visual_relation | relation:wing:for:sale | True | medium |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | pathway | pathway | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:pathway", "parents": []} |
| ent_m2 | object | entrance | entrance | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:entrance", "parents": []} |
| ent_m4 | object | building | building | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m5 | context | night | night | object | raw_lemma | stage9_seed:parent_seed | scene_context, time_context | m5 | raw_mention |  |  |  | True | {"canonical": "entity:night", "parents": ["entity_parent:scene_context", "entity_parent:time_context"]} |
| ent_m6 | object | light | lights | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:light", "parents": []} |
| ent_m10 | object | path | path | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:path", "parents": []} |
| ent_m11 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m11 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m13 | object | archway | archway | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:archway", "parents": []} |
| ent_m14 | object | snow | Snow | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:snow", "parents": []} |
| ent_m15 | object | ground | ground | object | raw_lemma | none |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:ground", "parents": []} |
| ent_m16 | context | side | side | object | raw_lemma | semantic_type_fallback | scene_context | m16 | raw_mention |  |  |  | True | {"canonical": "entity:side", "parents": ["entity_parent:scene_context"]} |
| ent_m17 | object | walkway | walkway | object | raw_lemma | none |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:walkway", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | leads | lead | lead | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:lead", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m19 | line | line | line | raw_action | visual_action_fallback | visual_action |  | agent:m6->ent_m6; patient:m10->ent_m10 | {"canonical": "action:line", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m20 | walking | walk | walk | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  |  | {"canonical": "action:walk", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce3 | m21 | covers | cover | cover | raw_action | visual_action_fallback | visual_action |  | agent:m14->ent_m14; patient:m15->ent_m15 | {"canonical": "action:cover", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | lead | agent | m0 | ent_m0 | medium | e7 | nsubj -> leads |  |  |
| ce1 | line | agent | m6 | ent_m6 | medium | e8 | nsubj -> line |  |  |
| ce1 | line | patient | m10 | ent_m10 | medium | e9 | dobj -> line |  |  |
| ce3 | cover | agent | m14 | ent_m14 | medium | e10 | nsubj -> covers |  |  |
| ce3 | cover | patient | m15 | ent_m15 | medium | e11 | dobj -> covers |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | through | through | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | medium | e12 | False | False |  |  |
| cr1 | m2 | m4 | ent_m2 | ent_m4 | to | to | raw_relation | raw_relation | visual_relation | medium | e13 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e14 | False | False |  |  |
| cr3 | m14 | m16 | ent_m14 | ent_m16 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e15 | False | False |  |  |
| cr4 | m16 | m17 | ent_m16 | ent_m17 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | pathway |  |  |  | entity_exists:pathway | True | low |
| cf1 | entity_exists | entrance |  |  |  | entity_exists:entrance | True | low |
| cf2 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf3 | entity_exists | night |  |  | scene_context, time_context | entity_exists:night | True | high |
| cf4 | entity_exists | light |  |  |  | entity_exists:light | True | low |
| cf5 | entity_exists | path |  |  |  | entity_exists:path | True | low |
| cf6 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf7 | entity_exists | archway |  |  |  | entity_exists:archway | True | low |
| cf8 | entity_exists | snow |  |  |  | entity_exists:snow | True | low |
| cf9 | entity_exists | ground |  |  |  | entity_exists:ground | True | low |
| cf10 | entity_exists | side |  |  | scene_context | entity_exists:side | True | medium |
| cf11 | entity_exists | walkway |  |  |  | entity_exists:walkway | True | low |
| cf12 | has_attribute | pathway | narrow |  | size_attribute, width, visual_attribute | has_attribute:pathway:narrow | True | high |
| cf13 | has_attribute | entrance | arched |  | visual_attribute | has_attribute:entrance:arched | True | medium |
| cf14 | has_quantity | light | several |  | approximate_quantity, quantity | has_quantity:light:several | True | medium |
| cf15 | has_attribute | light | glow |  | state_attribute, visual_attribute | has_attribute:light:glow | True | medium |
| cf16 | has_attribute | light | spherical |  | shape_attribute, shape, visual_attribute | has_attribute:light:spherical | True | medium |
| cf17 | has_quantity | people | two |  | exact_quantity, quantity | has_quantity:people:two | True | high |
| cf18 | action_event | lead |  |  | visual_action | action_event:lead | True | low |
| cf19 | event_role | lead | agent | pathway |  | event_role:lead:agent:pathway | True | medium |
| cf20 | action_event | line |  |  | visual_action | action_event:line | True | low |
| cf21 | event_role | line | agent | light |  | event_role:line:agent:light | True | medium |
| cf22 | event_role | line | patient | path |  | event_role:line:patient:path | True | medium |
| cf23 | action_event | walk |  |  | locomotion_action, visual_action | action_event:walk | True | high |
| cf24 | action_event | cover |  |  | visual_action | action_event:cover | True | low |
| cf25 | event_role | cover | agent | snow |  | event_role:cover:agent:snow | True | medium |
| cf26 | event_role | cover | patient | ground |  | event_role:cover:patient:ground | True | medium |
| cf27 | relation | pathway | through | entrance | spatial_path, visual_relation | relation:pathway:through:entrance | True | medium |
| cf28 | relation | entrance | to | building | visual_relation | relation:entrance:to:building | True | medium |
| cf29 | relation | pathway | at | night | spatial_location, visual_relation | relation:pathway:at:night | True | medium |
| cf30 | relation | snow | on | side | spatial_support, visual_relation | relation:snow:on:side | True | high |
| cf31 | relation | side | of | walkway | part_relation, visual_relation | relation:side:of:walkway | True | medium |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | hair | hair | object | raw_lemma | stage9_seed:parent_seed | body_part | m1 | raw_mention |  |  |  | True | {"canonical": "entity:hair", "parents": ["entity_parent:body_part"]} |
| ent_m3 | object | rope | rope | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:rope", "parents": []} |
| ent_m6 | object | face | face | object | raw_lemma | stage9_seed:parent_seed | body_part | m6 | raw_mention |  |  |  | True | {"canonical": "entity:face", "parents": ["entity_parent:body_part"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | holds | hold | hold | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action |  | agent:m0->ent_m0; patient:m3->ent_m3 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | hold | agent | m0 | ent_m0 | medium | e3 | nsubj -> holds |  |  |
| ce0 | hold | patient | m3 | ent_m3 | medium | e4 | dobj -> holds |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e5 | False | False |  |  |
| cr1 | m0 | m6 | ent_m3 | ent_m6 | in_front_of | in_front_of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e6 | False | False | pp_source_disambiguation | patient_body_part_anchor |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf1 | entity_exists | hair |  |  | body_part | entity_exists:hair | True | high |
| cf2 | entity_exists | rope |  |  |  | entity_exists:rope | True | low |
| cf3 | entity_exists | face |  |  | body_part | entity_exists:face | True | high |
| cf4 | has_attribute | hair | white |  | color_attribute, color, visual_attribute | has_attribute:hair:white | True | high |
| cf5 | has_attribute | rope | tangle |  | state_attribute, visual_attribute | has_attribute:rope:tangle | True | medium |
| cf6 | has_attribute | rope | red |  | color_attribute, color, visual_attribute | has_attribute:rope:red | True | high |
| cf7 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf8 | event_role | hold | agent | person |  | event_role:hold:agent:person | True | medium |
| cf9 | event_role | hold | patient | rope |  | event_role:hold:patient:rope | True | medium |
| cf10 | relation | person | with | hair | association_relation, visual_relation | relation:person:with:hair | True | high |
| cf11 | relation | rope | in_front_of | face | spatial_depth, visual_relation | relation:rope:in_front_of:face | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hockey_player | hockey players | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:hockey_player", "parents": []} |
| ent_m2 | object | ice | ice | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:ice", "parents": []} |
| ent_m4 | object | referee | referee | person | raw_lemma | stage9_seed:parent_seed | person, human | m4 | raw_mention |  |  |  | True | {"canonical": "entity:referee", "parents": ["entity_parent:person", "entity_parent:human"]} |
| eref_m5 | instance | hockey_player | one | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m5 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:hockey_player", "parents": []} |
| eref_m6 | instance | hockey_player | one | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m6 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:hockey_player", "parents": []} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m5 | eref_m5 | m0 | ent_m0 | high |  |
| refers_to | m6 | eref_m6 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | skate | skate | skate | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:skate", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m8 | watches | watch | watch | raw_action | stage9_seed:parent_seed | gaze_action, visual_action |  | agent:m4->ent_m4 | {"canonical": "action:watch", "parents": ["action_parent:gaze_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | skate | agent | m0 | ent_m0 | medium | e3 | nsubj -> skate |  |  |
| ce1 | watch | agent | m4 | ent_m4 | medium | e4 | nsubj -> watches |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e5 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | hockey_player |  |  |  | entity_exists:hockey_player | True | high |
| cf1 | entity_exists | ice |  |  |  | entity_exists:ice | True | low |
| cf2 | entity_exists | referee |  |  | person, human | entity_exists:referee | True | high |
| cf3 | entity_exists | hockey_player |  |  |  | entity_exists:hockey_player | True | high |
| cf4 | entity_exists | hockey_player |  |  |  | entity_exists:hockey_player | True | high |
| cf5 | has_quantity | hockey_player | two |  | exact_quantity, quantity | has_quantity:hockey_player:two | True | high |
| cf6 | action_event | skate |  |  | locomotion_action, visual_action | action_event:skate | True | high |
| cf7 | event_role | skate | agent | hockey_player |  | event_role:skate:agent:hockey_player | True | medium |
| cf8 | action_event | watch |  |  | gaze_action, visual_action | action_event:watch | True | medium |
| cf9 | event_role | watch | agent | referee |  | event_role:watch:agent:referee | True | medium |
| cf10 | relation | hockey_player | on | ice | spatial_support, visual_relation | relation:hockey_player:on:ice | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | hair | hair | object | raw_lemma | stage9_seed:parent_seed | body_part | m1 | raw_mention |  |  |  | True | {"canonical": "entity:hair", "parents": ["entity_parent:body_part"]} |
| ent_m3 | object | tattoo | tattoos | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:tattoo", "parents": []} |
| ent_m4 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m7 | object | arm | arm | object | raw_lemma | stage9_seed:parent_seed | body_part | m7 | raw_mention |  |  |  | True | {"canonical": "entity:arm", "parents": ["entity_parent:body_part"]} |
| ent_m9 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m9 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m11 | wears | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m0->ent_m0; patient:m4->ent_m4 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce1 | m12 | raising | raise | raise | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m7->ent_m7 | {"canonical": "action:raise", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | wear | agent | m0 | ent_m0 | medium | e6 | nsubj -> wears |  |  |
| ce0 | wear | patient | m4 | ent_m4 | medium | e7 | dobj -> wears |  |  |
| ce1 | raise | agent | m0 | ent_m0 | medium | e8 | inherited agent advcl -> wears |  |  |
| ce1 | raise | patient | m7 | ent_m7 | medium | e9 | dobj -> raising |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e10 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e11 | False | False |  |  |
| cr2 | m0 | m9 | ent_m0 | ent_m9 | against | against | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_contact, visual_relation | high | e12 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf1 | entity_exists | hair |  |  | body_part | entity_exists:hair | True | high |
| cf2 | entity_exists | tattoo |  |  |  | entity_exists:tattoo | True | low |
| cf3 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf4 | entity_exists | arm |  |  | body_part | entity_exists:arm | True | high |
| cf5 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf6 | has_attribute | hair | orange |  | color_attribute, color, visual_attribute | has_attribute:hair:orange | True | high |
| cf7 | has_attribute | shirt | light |  | visual_attribute | has_attribute:shirt:light | True | medium |
| cf8 | has_attribute | shirt | green |  | color_attribute, color, visual_attribute | has_attribute:shirt:green | True | high |
| cf9 | has_quantity | arm | one |  | exact_quantity, quantity | has_quantity:arm:one | True | high |
| cf10 | has_attribute | background | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:background:dark | True | medium |
| cf11 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf12 | event_role | wear | agent | person |  | event_role:wear:agent:person | True | medium |
| cf13 | event_role | wear | patient | shirt |  | event_role:wear:patient:shirt | True | medium |
| cf14 | action_event | raise |  |  | visual_action | action_event:raise | True | low |
| cf15 | event_role | raise | agent | person |  | event_role:raise:agent:person | True | medium |
| cf16 | event_role | raise | patient | arm |  | event_role:raise:patient:arm | True | medium |
| cf17 | relation | person | with | hair | association_relation, visual_relation | relation:person:with:hair | True | high |
| cf18 | relation | person | with | tattoo | association_relation, visual_relation | relation:person:with:tattoo | True | high |
| cf19 | relation | person | against | background | spatial_contact, visual_relation | relation:person:against:background | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | soldier | Soldiers | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:soldier", "parents": []} |
| ent_m1 | object | water | water | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": []} |
| ent_m2 | object | craft | craft | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:craft", "parents": []} |
| ent_m4 | object | memorial | Memorial | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:memorial", "parents": []} |
| ent_m6 | object | scene | scene | object | raw_lemma | stage9_seed:parent_seed | scene_context | m6 | raw_mention |  |  |  | True | {"canonical": "entity:scene", "parents": ["entity_parent:scene_context"]} |
| ent_m7 | context | day | day | object | raw_lemma | semantic_type_fallback | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:day", "parents": ["entity_parent:scene_context"]} |
| ent_m9 | object | tree | trees | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m10 | object | path | path | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:path", "parents": []} |
| ent_m11 | object | monument | monument | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:monument", "parents": []} |
| ent_m12 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m12 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m13 | wade | wade | wade | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:wade", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m14 | heading | head | head | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:head", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m15 | set | set | set | raw_action | visual_action_fallback | visual_action |  | theme:m6->ent_m6 | {"canonical": "action:set", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m16 | lining | line | line | raw_action | visual_action_fallback | visual_action |  | agent:m9->ent_m9; patient:m10->ent_m10 | {"canonical": "action:line", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | wade | agent | m0 | ent_m0 | medium | e5 | nsubj -> wade |  |  |
| ce1 | head | agent | m0 | ent_m0 | medium | e6 | inherited agent advcl -> wade |  |  |
| ce2 | set | theme | m6 | ent_m6 | medium | e7 | nsubjpass -> set |  |  |
| ce3 | line | agent | m9 | ent_m9 | medium | e8 | nsubj -> lining |  |  |
| ce3 | line | patient | m10 | ent_m10 | medium | e9 | dobj -> lining |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | through | through | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | medium | e10 | False | False |  |  |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e11 | False | False |  |  |
| cr2 | m0 | m4 | ent_m0 | ent_m4 | toward | toward | raw_relation | raw_relation | visual_relation | medium | e12 | False | False |  |  |
| cr3 | m6 | m7 | ent_m6 | ent_m7 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e13 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | soldier |  |  |  | entity_exists:soldier | True | low |
| cf1 | entity_exists | water |  |  |  | entity_exists:water | True | low |
| cf2 | entity_exists | craft |  |  |  | entity_exists:craft | True | low |
| cf3 | entity_exists | memorial |  |  |  | entity_exists:memorial | True | low |
| cf4 | entity_exists | scene |  |  | scene_context | entity_exists:scene | True | high |
| cf5 | entity_exists | day |  |  | scene_context | entity_exists:day | True | medium |
| cf6 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf7 | entity_exists | path |  |  |  | entity_exists:path | True | low |
| cf8 | entity_exists | monument |  |  |  | entity_exists:monument | True | low |
| cf9 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf10 | has_attribute | craft | landing |  | state_attribute, coco_subtype_rule, visual_attribute | has_attribute:craft:landing | True | medium |
| cf11 | has_attribute | memorial | lincoln |  | compound_modifier, visual_attribute | has_attribute:memorial:lincoln | True | medium |
| cf12 | has_attribute | day | sunny |  | weather_attribute, weather, visual_attribute | has_attribute:day:sunny | True | medium |
| cf13 | action_event | wade |  |  | visual_action | action_event:wade | True | low |
| cf14 | event_role | wade | agent | soldier |  | event_role:wade:agent:soldier | True | medium |
| cf15 | action_event | head |  |  | visual_action | action_event:head | True | low |
| cf16 | event_role | head | agent | soldier |  | event_role:head:agent:soldier | True | medium |
| cf17 | action_event | set |  |  | visual_action | action_event:set | True | low |
| cf18 | event_role | set | theme | scene |  | event_role:set:theme:scene | True | medium |
| cf19 | action_event | line |  |  | visual_action | action_event:line | True | low |
| cf20 | event_role | line | agent | tree |  | event_role:line:agent:tree | True | medium |
| cf21 | event_role | line | patient | path |  | event_role:line:patient:path | True | medium |
| cf22 | relation | soldier | through | water | spatial_path, visual_relation | relation:soldier:through:water | True | medium |
| cf23 | relation | soldier | in | craft | spatial_containment, visual_relation | relation:soldier:in:craft | True | high |
| cf24 | relation | soldier | toward | memorial | visual_relation | relation:soldier:toward:memorial | True | medium |
| cf25 | relation | scene | on | day | spatial_support, visual_relation | relation:scene:on:day | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | statue | statue | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:statue", "parents": []} |
| ent_m2 | object | mountain | mountain | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:mountain", "parents": []} |
| ent_m3 | object | sky | sky | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m5 | object | tree | tree | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m7 | object | base | base | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:base", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | statue |  |  |  | entity_exists:statue | True | low |
| cf1 | entity_exists | mountain |  |  |  | entity_exists:mountain | True | low |
| cf2 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf3 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf4 | entity_exists | base |  |  |  | entity_exists:base | True | low |
| cf5 | has_attribute | statue | buddha |  | attribute, visual_attribute | has_attribute:statue:buddha | True | high |
| cf6 | has_attribute | sky | green |  | color_attribute, color, visual_attribute | has_attribute:sky:green | True | high |
| cf7 | has_attribute | tree | bare |  | attribute, visual_attribute | has_attribute:tree:bare | True | high |
| cf8 | has_attribute | base | stone |  | material_attribute, material, visual_attribute | has_attribute:base:stone | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | women | person | stage9_seed:synonym_seed | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | beach | beach | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:beach", "parents": []} |
| ent_m3 | object | island | island | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:island", "parents": []} |
| ent_m4 | object | water | water | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | beach |  |  |  | entity_exists:beach | True | low |
| cf2 | entity_exists | island |  |  |  | entity_exists:island | True | low |
| cf3 | entity_exists | water |  |  |  | entity_exists:water | True | low |
| cf4 | has_quantity | woman | four |  | exact_quantity, quantity | has_quantity:woman:four | True | high |
| cf5 | has_attribute | water | turquoise |  | color_attribute, color, visual_attribute | has_attribute:water:turquoise | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | pyramid | pyramid | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:pyramid", "parents": []} |
| ent_m2 | object | step | steps | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:step", "parents": []} |
| ent_m4 | object | grass | grass | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": []} |
| ent_m6 | object | shadow | shadows | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:shadow", "parents": []} |
| ent_m8 | context | setting | setting | object | raw_lemma | stage9_seed:parent_seed | scene_context | m8 | raw_mention |  |  |  | True | {"canonical": "entity:setting", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | pyramid |  |  |  | entity_exists:pyramid | True | low |
| cf1 | entity_exists | step |  |  |  | entity_exists:step | True | low |
| cf2 | entity_exists | grass |  |  |  | entity_exists:grass | True | low |
| cf3 | entity_exists | shadow |  |  |  | entity_exists:shadow | True | low |
| cf4 | entity_exists | setting |  |  | scene_context | entity_exists:setting | True | high |
| cf5 | has_attribute | pyramid | ancient |  | attribute, visual_attribute | has_attribute:pyramid:ancient | True | high |
| cf6 | has_attribute | step | stone |  | material_attribute, material, visual_attribute | has_attribute:step:stone | True | high |
| cf7 | has_attribute | grass | green |  | color_attribute, color, visual_attribute | has_attribute:grass:green | True | high |
| cf8 | has_attribute | shadow | tree |  | attribute, visual_attribute | has_attribute:shadow:tree | True | high |
| cf9 | has_attribute | setting | jungle |  | attribute, visual_attribute | has_attribute:setting:jungle | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | player | players | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:player", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m3 | object | uniform | uniforms | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m3 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m5 | object | field | field | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |
| ent_m7 | object | wicket | wicket | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:wicket", "parents": []} |
| eref_m8 | contrastive_instance | player | other | person | raw_lemma | stage9_seed:parent_seed | person, human | m8 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:player", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m8 | eref_m8 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | play | play | play | raw_action | stage9_seed:parent_seed | activity_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:play", "parents": ["action_parent:activity_action", "action_parent:visual_action"]} |  |
| ce1 | m10 | bats | bat | bat | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:bat", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m11 | runs | run | run | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->eref_m8 | {"canonical": "action:run", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | play | agent | m0 | ent_m0 | medium | e5 | nsubj -> play |  |  |
| ce1 | bat | agent | m0 | ent_m0 | medium | e6 | inherited agent ccomp -> runs |  |  |
| ce2 | run | agent | m0 | eref_m8 | medium | e7 | nsubj -> runs; resolved other -> players |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e8 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e9 | False | False |  |  |
| cr2 | m0 | m7 | eref_m8 | ent_m7 | toward | toward | raw_relation | raw_relation | visual_relation | medium | e10 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | player |  |  | person, human | entity_exists:player | True | high |
| cf1 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf2 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf3 | entity_exists | wicket |  |  |  | entity_exists:wicket | True | low |
| cf4 | entity_exists | player |  |  | person, human | entity_exists:player | True | high |
| cf5 | has_quantity | player | two |  | exact_quantity, quantity | has_quantity:player:two | True | high |
| cf6 | has_attribute | player | cricket |  | compound_modifier, visual_attribute | has_attribute:player:cricket | True | medium |
| cf7 | has_attribute | uniform | white |  | color_attribute, color, visual_attribute | has_attribute:uniform:white | True | high |
| cf8 | has_attribute | field | grass |  | compound_modifier, visual_attribute | has_attribute:field:grass | True | medium |
| cf9 | action_event | play |  |  | activity_action, visual_action | action_event:play | True | high |
| cf10 | event_role | play | agent | player |  | event_role:play:agent:player | True | medium |
| cf11 | action_event | bat |  |  | visual_action | action_event:bat | True | low |
| cf12 | event_role | bat | agent | player |  | event_role:bat:agent:player | True | medium |
| cf13 | action_event | run |  |  | locomotion_action, visual_action | action_event:run | True | high |
| cf14 | event_role | run | agent | player |  | event_role:run:agent:player | True | medium |
| cf15 | relation | player | in | uniform | spatial_containment, visual_relation | relation:player:in:uniform | True | high |
| cf16 | relation | player | on | field | spatial_support, visual_relation | relation:player:on:field | True | high |
| cf17 | relation | player | toward | wicket | visual_relation | relation:player:toward:wicket | True | medium |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | building | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m3 | object | roof | roof | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:roof", "parents": []} |
| ent_m5 | object | street | street | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:street", "parents": []} |
| ent_m7 | object | tree | Trees | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m8 | object | wall | wall | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |
| ent_m10 | object | structure | structures | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:structure", "parents": []} |
| ent_m13 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m13 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m14 | object | sky | sky | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m17 | appear | appear | appear | raw_action | visual_action_fallback | visual_action |  | agent:m10->ent_m10 | {"canonical": "action:appear", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e9 | nsubj -> stands |  |  |
| ce1 | appear | agent | m10 | ent_m10 | medium | e10 | nsubj -> appear |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e11 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | corner_of | corner_of | generated_region_pattern | generated_region_pattern | spatial_region, visual_relation | high | e12 | False | False |  |  |
| cr2 | m10 | m13 | ent_m10 | ent_m13 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e13 | False | False |  |  |
| cr3 | m10 | m14 | ent_m10 | ent_m14 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e14 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf1 | entity_exists | roof |  |  |  | entity_exists:roof | True | low |
| cf2 | entity_exists | street |  |  |  | entity_exists:street | True | low |
| cf3 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf4 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf5 | entity_exists | structure |  |  |  | entity_exists:structure | True | low |
| cf6 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf7 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf8 | has_attribute | building | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:building:large | True | high |
| cf9 | has_attribute | building | brick |  | material_attribute, material, visual_attribute | has_attribute:building:brick | True | high |
| cf10 | has_attribute | roof | sloped |  | modifier_attribute, visual_attribute | has_attribute:roof:sloped | True | medium |
| cf11 | has_attribute | street | paved |  | visual_attribute | has_attribute:street:paved | True | medium |
| cf12 | has_attribute | wall | low |  | size_attribute, height, visual_attribute | has_attribute:wall:low | True | medium |
| cf13 | has_quantity | structure | few |  | approximate_quantity, quantity | has_quantity:structure:few | True | medium |
| cf14 | has_attribute | structure | distant |  | modifier_attribute, visual_attribute | has_attribute:structure:distant | True | medium |
| cf15 | has_attribute | sky | overcast |  | weather_attribute, weather, visual_attribute | has_attribute:sky:overcast | True | medium |
| cf16 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf17 | event_role | stand | agent | building |  | event_role:stand:agent:building | True | medium |
| cf18 | action_event | appear |  |  | visual_action | action_event:appear | True | low |
| cf19 | event_role | appear | agent | structure |  | event_role:appear:agent:structure | True | medium |
| cf20 | relation | building | with | roof | association_relation, visual_relation | relation:building:with:roof | True | high |
| cf21 | relation | building | corner_of | street | spatial_region, visual_relation | relation:building:corner_of:street | True | high |
| cf22 | relation | structure | in | background | spatial_containment, visual_relation | relation:structure:in:background | True | high |
| cf23 | relation | structure | under | sky | spatial_vertical, visual_relation | relation:structure:under:sky | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | top_hat | top hats | object | lvis_object\|visual_genome_object_synset\|wordnet_noun_mwe | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:top_hat", "parents": []} |
| ent_m1 | object | crowd | crowd | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:crowd", "parents": []} |
| ent_m2 | object | man | men | person | stage9_seed:synonym_seed | stage9_seed:parent_seed | person, human | m2 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m4 | object | attire | attire | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:attire", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
_none_

### Stage 9 Canonical Event Roles
_none_

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | top_hat |  |  |  | entity_exists:top_hat | True | high |
| cf1 | entity_exists | crowd |  |  |  | entity_exists:crowd | True | low |
| cf2 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf3 | entity_exists | attire |  |  |  | entity_exists:attire | True | low |
| cf4 | candidate_has_attribute | man | seat |  | floating_attribute, visual_attribute | candidate_has_attribute:man:seat | False | low |
| cf5 | has_attribute | attire | formal |  | attribute, visual_attribute | has_attribute:attire:formal | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sea_lion | sea lions | object | openimages_boxable\|wordnet_noun_mwe | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:sea_lion", "parents": []} |
| ent_m1 | object | dock | dock | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:dock", "parents": []} |
| ent_m3 | object | water | water | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": []} |
| ent_m5 | object | water | water | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": []} |
| ent_m8 | object | sea_lion | sea lions | object | openimages_boxable\|wordnet_noun_mwe | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:sea_lion", "parents": []} |
| ent_m9 | object | platform | platform | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:platform", "parents": []} |
| ent_m10 | object | post | post | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:post", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | rest | rest | rest | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:rest", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m13 | lying | lie | lie_down | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action | down |  | {"canonical": "action:lie_down", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} | phrasal_action:lie down |
| ce2 | m15 | sit | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  |  | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce3 | m16 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  |  | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | rest | agent | m0 | ent_m0 | medium | e4 | nsubj -> rest |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e6 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e7 | False | False |  |  |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e8 | False | False |  |  |
| cr3 | m9 | m10 | ent_m9 | ent_m10 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | sea_lion |  |  |  | entity_exists:sea_lion | True | high |
| cf1 | entity_exists | dock |  |  |  | entity_exists:dock | True | low |
| cf2 | entity_exists | water |  |  |  | entity_exists:water | True | low |
| cf3 | entity_exists | water |  |  |  | entity_exists:water | True | low |
| cf4 | entity_exists | sea_lion |  |  |  | entity_exists:sea_lion | True | high |
| cf5 | entity_exists | platform |  |  |  | entity_exists:platform | True | low |
| cf6 | entity_exists | post |  |  |  | entity_exists:post | True | low |
| cf7 | has_attribute | dock | wooden |  | material_attribute, material, visual_attribute | has_attribute:dock:wooden | True | high |
| cf8 | has_attribute | water | calm |  | modifier_attribute, visual_attribute | has_attribute:water:calm | True | medium |
| cf9 | has_attribute | water | blue |  | color_attribute, color, visual_attribute | has_attribute:water:blue | True | high |
| cf10 | has_attribute | post | wooden |  | material_attribute, material, visual_attribute | has_attribute:post:wooden | True | high |
| cf11 | action_event | rest |  |  | visual_action | action_event:rest | True | low |
| cf12 | event_role | rest | agent | sea_lion |  | event_role:rest:agent:sea_lion | True | medium |
| cf13 | action_event | lie_down |  |  | body_pose_action, visual_action | action_event:lie_down | True | high |
| cf14 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf15 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf16 | relation | sea_lion | on | dock | spatial_support, visual_relation | relation:sea_lion:on:dock | True | high |
| cf17 | relation | sea_lion | near | water | spatial_proximity, visual_relation | relation:sea_lion:near:water | True | high |
| cf18 | relation | sea_lion | on | platform | spatial_support, visual_relation | relation:sea_lion:on:platform | True | high |
| cf19 | relation | platform | near | post | spatial_proximity, visual_relation | relation:platform:near:post | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | table | table | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m1 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m2 | object | screen | screen | device | raw_lemma | stage9_seed:parent_seed | device, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:screen", "parents": ["entity_parent:device", "entity_parent:artifact"]} |
| ent_m3 | object | call | calls | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:call", "parents": []} |
| ent_m5 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m5 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m7 | object | table | table | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m7 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m8 | object | room | room | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:room", "parents": []} |
| eref_m10 | complement_subset | people | Others | person | raw_lemma | stage9_seed:parent_seed | person, human | m10 | stage9_reference | ent_m5 |  | many | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m10 | eref_m10 | m5 | ent_m5 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m11 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m12 | pointing | point | point | raw_action | stage9_seed:parent_seed | gesture_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:point", "parents": ["action_parent:gesture_action", "action_parent:visual_action"]} |  |
| ce2 | m13 | showing | show | show | raw_action | visual_action_fallback | visual_action |  | agent:m2->ent_m2; patient:m3->ent_m3 | {"canonical": "action:show", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m14 | sit | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m5->eref_m10 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e4 | nsubj -> stands |  |  |
| ce1 | point | agent | m0 | ent_m0 | medium | e5 | inherited agent advcl -> stands |  |  |
| ce2 | show | agent | m2 | ent_m2 | medium | e6 | inherited agent acl -> screen |  |  |
| ce2 | show | patient | m3 | ent_m3 | medium | e7 | dobj -> showing |  |  |
| ce3 | sit | agent | m5 | eref_m10 | medium | e8 | nsubj -> sit; resolved Others -> people |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e9 | False | False |  |  |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | to | to | raw_relation | raw_relation | visual_relation | medium | e10 | False | False |  |  |
| cr2 | m3 | m5 | ent_m3 | ent_m5 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e11 | False | False |  |  |
| cr3 | m5 | m7 | ent_m5 | ent_m7 | around | around | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e12 | False | False |  |  |
| cr4 | m5 | m8 | ent_m5 | ent_m8 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e13 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf2 | entity_exists | screen |  |  | device, artifact | entity_exists:screen | True | high |
| cf3 | entity_exists | call |  |  |  | entity_exists:call | True | low |
| cf4 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf5 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf6 | entity_exists | room |  |  |  | entity_exists:room | True | low |
| cf7 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf8 | has_attribute | call | video |  | compound_modifier, visual_attribute | has_attribute:call:video | True | medium |
| cf9 | has_quantity | people | several |  | approximate_quantity, quantity | has_quantity:people:several | True | medium |
| cf10 | has_attribute | room | modern |  | modifier_attribute, visual_attribute | has_attribute:room:modern | True | medium |
| cf11 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf12 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf13 | action_event | point |  |  | gesture_action, visual_action | action_event:point | True | high |
| cf14 | event_role | point | agent | man |  | event_role:point:agent:man | True | medium |
| cf15 | action_event | show |  |  | visual_action | action_event:show | True | low |
| cf16 | event_role | show | agent | screen |  | event_role:show:agent:screen | True | medium |
| cf17 | event_role | show | patient | call |  | event_role:show:patient:call | True | medium |
| cf18 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf19 | event_role | sit | agent | people |  | event_role:sit:agent:people | True | medium |
| cf20 | relation | man | at | table | spatial_location, visual_relation | relation:man:at:table | True | medium |
| cf21 | relation | man | to | screen | visual_relation | relation:man:to:screen | True | medium |
| cf22 | relation | call | with | people | association_relation, visual_relation | relation:call:with:people | True | high |
| cf23 | relation | people | around | table | spatial_proximity, visual_relation | relation:people:around:table | True | high |
| cf24 | relation | people | in | room | spatial_containment, visual_relation | relation:people:in:room | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | airplane | airplane | vehicle | raw_lemma | semantic_type_fallback | vehicle | m0 | raw_mention |  |  |  | True | {"canonical": "entity:airplane", "parents": ["entity_parent:vehicle"]} |
| ent_m2 | object | frame | frame | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:frame", "parents": []} |
| ent_m4 | object | ceiling | ceiling | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:ceiling", "parents": []} |
| ent_m5 | object | space | space | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:space", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | hangs | hang | hang | raw_action | stage9_seed:parent_seed | attachment_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:hang", "parents": ["action_parent:attachment_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | hang | agent | m0 | ent_m0 | medium | e4 | nsubj -> hangs |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e5 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | from | from | raw_relation | raw_relation | visual_relation | medium | e6 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | airplane |  |  | vehicle | entity_exists:airplane | True | medium |
| cf1 | entity_exists | frame |  |  |  | entity_exists:frame | True | low |
| cf2 | entity_exists | ceiling |  |  |  | entity_exists:ceiling | True | low |
| cf3 | entity_exists | space |  |  |  | entity_exists:space | True | low |
| cf4 | has_attribute | airplane | old |  | condition_attribute, clean_exact_overlap, maturity, newness, visual_attribute | has_attribute:airplane:old | True | medium |
| cf5 | has_attribute | frame | bicycle |  | compound_modifier, visual_attribute | has_attribute:frame:bicycle | True | medium |
| cf6 | has_attribute | space | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:space:large | True | high |
| cf7 | has_attribute | space | indoor |  | modifier_attribute, visual_attribute | has_attribute:space:indoor | True | medium |
| cf8 | action_event | hang |  |  | attachment_action, visual_action | action_event:hang | True | high |
| cf9 | event_role | hang | agent | airplane |  | event_role:hang:agent:airplane | True | medium |
| cf10 | relation | airplane | with | frame | association_relation, visual_relation | relation:airplane:with:frame | True | high |
| cf11 | relation | airplane | from | ceiling | visual_relation | relation:airplane:from:ceiling | True | medium |
| cf12 | relation | airplane | in | space | spatial_containment, visual_relation | relation:airplane:in:space | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | table | tables | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m4 | object | chess | chess | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:chess", "parents": []} |
| ent_m5 | object | tree | trees | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m6 | object | girl | girl | person | raw_lemma | stage9_seed:parent_seed | person, human | m6 | raw_mention |  |  |  | True | {"canonical": "entity:girl", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m8 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m8 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m10 | object | table | table | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m10 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m11 | object | chessboard | chessboard | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:chessboard", "parents": []} |
| ent_m12 | object | game | games | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:game", "parents": []} |
| ent_m13 | context | setting | setting | object | raw_lemma | stage9_seed:parent_seed | scene_context | m13 | raw_mention |  |  |  | True | {"canonical": "entity:setting", "parents": ["entity_parent:scene_context"]} |
| ent_m14 | object | area | area | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:area", "parents": []} |
| ent_m17 | object | building | buildings | object | raw_lemma | none |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m18 | object | greenery | greenery | object | raw_lemma | none |  | m18 | raw_mention |  |  |  | True | {"canonical": "entity:greenery", "parents": []} |
| ent_m19 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m19 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m20 | context | outdoors | outdoors | object | raw_lemma | stage9_seed:parent_seed | scene_context | m20 | raw_mention |  |  |  | True | {"canonical": "entity:outdoors", "parents": ["entity_parent:scene_context"]} |
| eref_m21 | complement_subset | people | others | person | raw_lemma | stage9_seed:parent_seed | person, human | m21 | stage9_reference | ent_m0 |  | many | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m21 | eref_m21 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m22 | sit | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m23 | playing | play | play | raw_action | stage9_seed:parent_seed | activity_action, visual_action |  | agent:m0->ent_m0; patient:m4->ent_m4 | {"canonical": "action:play", "parents": ["action_parent:activity_action", "action_parent:visual_action"]} |  |
| ce2 | m24 | seated | seat | sit | stage9_seed:synonym_seed | stage9_seed:parent_seed | body_pose_action, visual_action |  | theme:m6->ent_m6 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce3 | m25 | focused | focus | focus | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:focus", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m0 | ent_m0 | medium | e10 | nsubj -> sit |  |  |
| ce1 | play | agent | m0 | ent_m0 | medium | e11 | inherited agent advcl -> sit |  |  |
| ce1 | play | patient | m4 | ent_m4 | medium | e12 | dobj -> playing |  |  |
| ce2 | sit | theme | m6 | ent_m6 | medium | e13 | nsubjpass -> seated |  |  |
| ce3 | focus | agent | m0 | ent_m0 | medium | e14 | inherited agent acomp -> are |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e15 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e16 | False | False |  |  |
| cr2 | m6 | m8 | ent_m6 | ent_m8 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e17 | False | False |  |  |
| cr3 | m6 | m10 | ent_m6 | ent_m10 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e18 | False | False |  |  |
| cr4 | m10 | m11 | ent_m10 | ent_m11 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e19 | False | False |  |  |
| cr5 | m11 | m6 | ent_m11 | ent_m6 | in_front_of | in_front_of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e20 | False | False |  |  |
| cr6 | m14 | m17 | ent_m14 | ent_m17 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e21 | False | False |  |  |
| cr7 | m14 | m18 | ent_m14 | ent_m18 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e22 | False | False |  |  |
| cr8 | m17 | m19 | ent_m17 | ent_m19 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e23 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf2 | entity_exists | chess |  |  |  | entity_exists:chess | True | low |
| cf3 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf4 | entity_exists | girl |  |  | person, human | entity_exists:girl | True | high |
| cf5 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf6 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf7 | entity_exists | chessboard |  |  |  | entity_exists:chessboard | True | low |
| cf8 | entity_exists | game |  |  |  | entity_exists:game | True | low |
| cf9 | entity_exists | setting |  |  | scene_context | entity_exists:setting | True | high |
| cf10 | entity_exists | area |  |  |  | entity_exists:area | True | low |
| cf11 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf12 | entity_exists | greenery |  |  |  | entity_exists:greenery | True | low |
| cf13 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf14 | entity_exists | outdoors |  |  | scene_context | entity_exists:outdoors | True | high |
| cf15 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf16 | has_quantity | people | several |  | approximate_quantity, quantity | has_quantity:people:several | True | medium |
| cf17 | has_attribute | table | wooden |  | material_attribute, material, visual_attribute | has_attribute:table:wooden | True | high |
| cf18 | has_attribute | girl | young |  | modifier_attribute, visual_attribute | has_attribute:girl:young | True | medium |
| cf19 | has_attribute | shirt | gray |  | color_attribute, color, visual_attribute | has_attribute:shirt:gray | True | high |
| cf20 | has_attribute | area | sunny |  | weather_attribute, weather, visual_attribute | has_attribute:area:sunny | True | medium |
| cf21 | has_attribute | area | park-like |  | modifier_attribute, visual_attribute | has_attribute:area:park-like | True | medium |
| cf22 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf23 | event_role | sit | agent | people |  | event_role:sit:agent:people | True | medium |
| cf24 | action_event | play |  |  | activity_action, visual_action | action_event:play | True | high |
| cf25 | event_role | play | agent | people |  | event_role:play:agent:people | True | medium |
| cf26 | event_role | play | patient | chess |  | event_role:play:patient:chess | True | medium |
| cf27 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf28 | event_role | sit | theme | girl |  | event_role:sit:theme:girl | True | medium |
| cf29 | action_event | focus |  |  | visual_action | action_event:focus | True | low |
| cf30 | event_role | focus | agent | people |  | event_role:focus:agent:people | True | medium |
| cf31 | relation | people | at | table | spatial_location, visual_relation | relation:people:at:table | True | medium |
| cf32 | relation | people | under | tree | spatial_vertical, visual_relation | relation:people:under:tree | True | high |
| cf33 | relation | girl | in | shirt | spatial_containment, visual_relation | relation:girl:in:shirt | True | high |
| cf34 | relation | girl | at | table | spatial_location, visual_relation | relation:girl:at:table | True | medium |
| cf35 | relation | table | with | chessboard | association_relation, visual_relation | relation:table:with:chessboard | True | high |
| cf36 | relation | chessboard | in_front_of | girl | spatial_depth, visual_relation | relation:chessboard:in_front_of:girl | True | high |
| cf37 | relation | area | with | building | association_relation, visual_relation | relation:area:with:building | True | high |
| cf38 | relation | area | with | greenery | association_relation, visual_relation | relation:area:with:greenery | True | high |
| cf39 | relation | building | in | background | spatial_containment, visual_relation | relation:building:in:background | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| action_lexical_canonicalized | m24 |  |  |  |  | {"action_mention_id": "m24", "canonical": "sit", "kind": "action_lexical_canonicalized", "raw_canonical_action": "seat", "source": "stage9_seed:synonym_seed"} |
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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | People | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | table | tables | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m1 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m2 | object | room | room | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:room", "parents": []} |
| ent_m3 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m3 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m5 | object | pant | pants | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:pant", "parents": []} |
| ent_m8 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m8 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m9 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m9 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m11 | sit | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m12 | standing | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m3->ent_m3 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m0 | ent_m0 | medium | e4 | nsubj -> sit |  |  |
| ce1 | stand | agent | m3 | ent_m3 | medium | e5 | nsubj -> standing |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e6 | False | False |  |  |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e7 | False | False |  |  |
| cr2 | m3 | m5 | ent_m3 | ent_m5 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e8 | False | False |  |  |
| cr3 | m3 | m8 | ent_m3 | ent_m8 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e9 | False | False |  |  |
| cr4 | m8 | m9 | ent_m8 | ent_m9 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e10 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf2 | entity_exists | room |  |  |  | entity_exists:room | True | low |
| cf3 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf4 | entity_exists | pant |  |  |  | entity_exists:pant | True | low |
| cf5 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf6 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf7 | has_quantity | woman | one |  | exact_quantity, quantity | has_quantity:woman:one | True | high |
| cf8 | has_attribute | pant | bright |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:pant:bright | True | medium |
| cf9 | has_attribute | pant | yellow |  | color_attribute, color, visual_attribute | has_attribute:pant:yellow | True | high |
| cf10 | has_attribute | shirt | plaid |  | pattern_attribute, pattern, visual_attribute | has_attribute:shirt:plaid | True | medium |
| cf11 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf12 | event_role | sit | agent | people |  | event_role:sit:agent:people | True | medium |
| cf13 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf14 | event_role | stand | agent | woman |  | event_role:stand:agent:woman | True | medium |
| cf15 | relation | people | at | table | spatial_location, visual_relation | relation:people:at:table | True | medium |
| cf16 | relation | people | in | room | spatial_containment, visual_relation | relation:people:in:room | True | high |
| cf17 | relation | woman | in | pant | spatial_containment, visual_relation | relation:woman:in:pant | True | high |
| cf18 | relation | woman | near | man | spatial_proximity, visual_relation | relation:woman:near:man | True | high |
| cf19 | relation | man | in | shirt | spatial_containment, visual_relation | relation:man:in:shirt | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | runner | runners | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:runner", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | track | track | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:track", "parents": []} |
| ent_m4 | object | jersey | jersey | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:jersey", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m6 | object | uniform | uniform | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m6 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| eref_m9 | instance | runner | one | person | raw_lemma | stage9_seed:parent_seed | person, human | m9 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:runner", "parents": ["entity_parent:person", "entity_parent:human"]} |
| eref_m10 | contrastive_instance | runner | another | person | raw_lemma | stage9_seed:parent_seed | person, human | m10 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:runner", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m9 | eref_m9 | m0 | ent_m0 | high |  |
| refers_to | m10 | eref_m10 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m11 | compete | compete | compete | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:compete", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | compete | agent | m0 | ent_m0 | medium | e7 | nsubj -> compete |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e8 | False | False |  |  |
| cr1 | m0 | m4 | eref_m9 | ent_m4 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e9 | False | False |  |  |
| cr2 | m0 | m6 | eref_m10 | ent_m6 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e10 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | runner |  |  | person, human | entity_exists:runner | True | high |
| cf1 | entity_exists | track |  |  |  | entity_exists:track | True | low |
| cf2 | entity_exists | jersey |  |  | clothing, wearable | entity_exists:jersey | True | high |
| cf3 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf4 | entity_exists | runner |  |  | person, human | entity_exists:runner | True | high |
| cf5 | entity_exists | runner |  |  | person, human | entity_exists:runner | True | high |
| cf6 | has_quantity | runner | three |  | exact_quantity, quantity | has_quantity:runner:three | True | high |
| cf7 | has_attribute | track | indoor |  | modifier_attribute, visual_attribute | has_attribute:track:indoor | True | medium |
| cf8 | has_attribute | jersey | orange |  | color_attribute, color, visual_attribute | has_attribute:jersey:orange | True | high |
| cf9 | has_attribute | uniform | gold |  | color_attribute, color, visual_attribute | has_attribute:uniform:gold | True | high |
| cf10 | has_attribute | uniform | blue |  | color_attribute, color, visual_attribute | has_attribute:uniform:blue | True | high |
| cf11 | action_event | compete |  |  | visual_action | action_event:compete | True | low |
| cf12 | event_role | compete | agent | runner |  | event_role:compete:agent:runner | True | medium |
| cf13 | relation | runner | on | track | spatial_support, visual_relation | relation:runner:on:track | True | high |
| cf14 | relation | runner | in | jersey | spatial_containment, visual_relation | relation:runner:in:jersey | True | high |
| cf15 | relation | runner | in | uniform | spatial_containment, visual_relation | relation:runner:in:uniform | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | badge | badges | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:badge", "parents": []} |
| ent_m3 | object | design | design | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:design", "parents": []} |
| ent_m5 | object | crown | crown | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:crown", "parents": []} |
| ent_m6 | object | text | text | document | raw_lemma | stage9_seed:parent_seed | text_content | m6 | raw_mention |  |  |  | True | {"canonical": "entity:text", "parents": ["entity_parent:text_content"]} |
| ent_m7 | context | surface | surface | object | raw_lemma | semantic_type_fallback | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | show | show | show | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m3->ent_m3 | {"canonical": "action:show", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m9 | placed | place | place | raw_action | visual_action_fallback | visual_action |  | theme:m0->ent_m0 | {"canonical": "action:place", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | m0 | ent_m0 | medium | e3 | nsubj -> show |  |  |
| ce0 | show | patient | m3 | ent_m3 | medium | e4 | dobj -> show |  |  |
| ce1 | place | theme | m0 | ent_m0 | medium | e5 | nsubjpass -> placed; resolved They -> badges |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m3 | m5 | ent_m3 | ent_m5 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr1 | m3 | m6 | ent_m3 | ent_m6 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e7 | False | False |  |  |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | badge |  |  |  | entity_exists:badge | True | low |
| cf1 | entity_exists | design |  |  |  | entity_exists:design | True | low |
| cf2 | entity_exists | crown |  |  |  | entity_exists:crown | True | low |
| cf3 | entity_exists | text |  |  | text_content | entity_exists:text | True | high |
| cf4 | entity_exists | surface |  |  | scene_context | entity_exists:surface | True | medium |
| cf5 | has_quantity | badge | two |  | exact_quantity, quantity | has_quantity:badge:two | True | high |
| cf6 | has_attribute | badge | military |  | modifier_attribute, visual_attribute | has_attribute:badge:military | True | medium |
| cf7 | has_attribute | design | sunburst |  | compound_modifier, visual_attribute | has_attribute:design:sunburst | True | medium |
| cf8 | action_event | show |  |  | visual_action | action_event:show | True | low |
| cf9 | event_role | show | agent | badge |  | event_role:show:agent:badge | True | medium |
| cf10 | event_role | show | patient | design |  | event_role:show:patient:design | True | medium |
| cf11 | action_event | place |  |  | visual_action | action_event:place | True | low |
| cf12 | event_role | place | theme | badge |  | event_role:place:theme:badge | True | medium |
| cf13 | relation | design | with | crown | association_relation, visual_relation | relation:design:with:crown | True | high |
| cf14 | relation | design | with | text | association_relation, visual_relation | relation:design:with:text | True | high |
| cf15 | relation | badge | on | surface | spatial_support, visual_relation | relation:badge:on:surface | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sidewalk | sidewalk | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:sidewalk", "parents": []} |
| ent_m2 | object | car | cars | vehicle | raw_lemma | stage9_seed:parent_seed | vehicle | m2 | raw_mention |  |  |  | True | {"canonical": "entity:car", "parents": ["entity_parent:vehicle"]} |
| ent_m4 | object | house | house | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:house", "parents": []} |
| ent_m5 | object | suv | SUV | vehicle | raw_lemma | stage9_seed:parent_seed | vehicle | m5 | raw_mention |  |  |  | True | {"canonical": "entity:suv", "parents": ["entity_parent:vehicle"]} |
| ent_m7 | context | right | right | object | raw_lemma | semantic_type_fallback | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:right", "parents": ["entity_parent:scene_context"]} |
| ent_m8 | object | bush | bush | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:bush", "parents": []} |
| ent_m10 | object | snow | snow | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:snow", "parents": []} |
| ent_m11 | object | street | street | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:street", "parents": []} |
| ent_m12 | object | tree | trees | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m14 | object | house | houses | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:house", "parents": []} |
| ent_m15 | object | sky | sky | object | raw_lemma | none |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | runs | run | run | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:run", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m18 | parked | park | park | raw_action | visual_action_fallback | visual_action |  | theme:m5->ent_m5 | {"canonical": "action:park", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m19 | piled | pile | pile | raw_action | visual_action_fallback | visual_action |  | agent:m8->ent_m8 | {"canonical": "action:pile", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m20 | lined | line | line | raw_action | visual_action_fallback | visual_action |  | theme:m11->ent_m11 | {"canonical": "action:line", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | run | agent | m0 | ent_m0 | medium | e6 | nsubj -> runs |  |  |
| ce1 | park | theme | m5 | ent_m5 | medium | e7 | nsubjpass -> parked |  |  |
| ce2 | pile | agent | m8 | ent_m8 | medium | e8 | inherited agent acl -> bush |  |  |
| ce3 | line | theme | m11 | ent_m11 | medium | e9 | nsubjpass -> lined |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | between | between | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_region, visual_relation | high | e10 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | between | between | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_region, visual_relation | high | e11 | False | False |  |  |
| cr2 | m5 | m7 | ent_m5 | ent_m7 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e12 | False | False |  |  |
| cr3 | m5 | m8 | ent_m5 | ent_m8 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr4 | m5 | m10 | ent_m5 | ent_m10 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr5 | m8 | m5 | ent_m8 | ent_m5 | beside | next_to | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e15 | False | False |  |  |
| cr6 | m11 | m12 | ent_m11 | ent_m12 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e16 | False | False |  |  |
| cr7 | m11 | m14 | ent_m11 | ent_m14 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e17 | False | False |  |  |
| cr8 | m14 | m15 | ent_m14 | ent_m15 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e18 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | sidewalk |  |  |  | entity_exists:sidewalk | True | low |
| cf1 | entity_exists | car |  |  | vehicle | entity_exists:car | True | high |
| cf2 | entity_exists | house |  |  |  | entity_exists:house | True | low |
| cf3 | entity_exists | suv |  |  | vehicle | entity_exists:suv | True | high |
| cf4 | entity_exists | right |  |  | scene_context | entity_exists:right | True | medium |
| cf5 | entity_exists | bush |  |  |  | entity_exists:bush | True | low |
| cf6 | entity_exists | snow |  |  |  | entity_exists:snow | True | low |
| cf7 | entity_exists | street |  |  |  | entity_exists:street | True | low |
| cf8 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf9 | entity_exists | house |  |  |  | entity_exists:house | True | low |
| cf10 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf11 | has_attribute | sidewalk | snow-covered |  | modifier_attribute, visual_attribute | has_attribute:sidewalk:snow-covered | True | medium |
| cf12 | has_attribute | car | parked |  | state_attribute, coco_subtype_rule, visual_attribute | has_attribute:car:parked | True | medium |
| cf13 | has_attribute | suv | silver |  | color_attribute, color, material, visual_attribute | has_attribute:suv:silver | True | high |
| cf14 | has_attribute | bush | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:bush:large | True | high |
| cf15 | has_attribute | tree | bare |  | visual_attribute | has_attribute:tree:bare | True | medium |
| cf16 | has_attribute | sky | dusky |  | modifier_attribute, visual_attribute | has_attribute:sky:dusky | True | medium |
| cf17 | action_event | run |  |  | locomotion_action, visual_action | action_event:run | True | high |
| cf18 | event_role | run | agent | sidewalk |  | event_role:run:agent:sidewalk | True | medium |
| cf19 | action_event | park |  |  | visual_action | action_event:park | True | low |
| cf20 | event_role | park | theme | suv |  | event_role:park:theme:suv | True | medium |
| cf21 | action_event | pile |  |  | visual_action | action_event:pile | True | low |
| cf22 | event_role | pile | agent | bush |  | event_role:pile:agent:bush | True | medium |
| cf23 | action_event | line |  |  | visual_action | action_event:line | True | low |
| cf24 | event_role | line | theme | street |  | event_role:line:theme:street | True | medium |
| cf25 | relation | sidewalk | between | car | spatial_region, visual_relation | relation:sidewalk:between:car | True | high |
| cf26 | relation | sidewalk | between | house | spatial_region, visual_relation | relation:sidewalk:between:house | True | high |
| cf27 | relation | suv | on | right | spatial_support, visual_relation | relation:suv:on:right | True | high |
| cf28 | relation | suv | with | bush | association_relation, visual_relation | relation:suv:with:bush | True | high |
| cf29 | relation | suv | with | snow | association_relation, visual_relation | relation:suv:with:snow | True | high |
| cf30 | relation | bush | next_to | suv | spatial_proximity, visual_relation | relation:bush:next_to:suv | True | high |
| cf31 | relation | street | with | tree | association_relation, visual_relation | relation:street:with:tree | True | high |
| cf32 | relation | street | with | house | association_relation, visual_relation | relation:street:with:house | True | high |
| cf33 | relation | house | under | sky | spatial_vertical, visual_relation | relation:house:under:sky | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m18 | e7 | m5 |  |  | {"action_mention_id": "m18", "kind": "passive_subject_to_theme", "raw_edge_id": "e7", "target": "m5"} |
| passive_subject_to_theme | m20 | e9 | m11 |  |  | {"action_mention_id": "m20", "kind": "passive_subject_to_theme", "raw_edge_id": "e9", "target": "m11"} |
| relation_lexical_canonicalized |  | e15 |  |  |  | {"canonical": "next_to", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e15", "raw_relation": "beside", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | skier | skier | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:skier", "parents": []} |
| ent_m1 | object | helmet | helmet | clothing | raw_lemma | stage9_seed:parent_seed | protective_gear, clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:helmet", "parents": ["entity_parent:protective_gear", "entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | slope | slope | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:slope", "parents": []} |
| ent_m5 | object | skier | skiers | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:skier", "parents": []} |
| ent_m7 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m8 | object | mountain | mountain | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:mountain", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | races | race | race | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:race", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | race | agent | m0 | ent_m0 | medium | e4 | nsubj -> races |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e5 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | down | down | raw_relation | raw_relation | visual_relation | medium | e6 | False | False |  |  |
| cr2 | m5 | m7 | ent_m5 | ent_m7 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e7 | False | False |  |  |
| cr3 | m7 | m8 | ent_m7 | ent_m8 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | skier |  |  |  | entity_exists:skier | True | low |
| cf1 | entity_exists | helmet |  |  | protective_gear, clothing, wearable | entity_exists:helmet | True | high |
| cf2 | entity_exists | slope |  |  |  | entity_exists:slope | True | low |
| cf3 | entity_exists | skier |  |  |  | entity_exists:skier | True | low |
| cf4 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf5 | entity_exists | mountain |  |  |  | entity_exists:mountain | True | low |
| cf6 | has_attribute | helmet | orange |  | color_attribute, color, visual_attribute | has_attribute:helmet:orange | True | high |
| cf7 | has_attribute | slope | snowy |  | material_attribute, material, visual_attribute | has_attribute:slope:snowy | True | medium |
| cf8 | has_attribute | skier | other |  | modifier_attribute, visual_attribute | has_attribute:skier:other | True | medium |
| cf9 | action_event | race |  |  | visual_action | action_event:race | True | low |
| cf10 | event_role | race | agent | skier |  | event_role:race:agent:skier | True | medium |
| cf11 | relation | skier | in | helmet | spatial_containment, visual_relation | relation:skier:in:helmet | True | high |
| cf12 | relation | skier | down | slope | visual_relation | relation:skier:down:slope | True | medium |
| cf13 | relation | skier | in | background | spatial_containment, visual_relation | relation:skier:in:background | True | high |
| cf14 | relation | background | on | mountain | spatial_support, visual_relation | relation:background:on:mountain | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | team | team | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:team", "parents": []} |
| ent_m2 | object | uniform | uniforms | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m4 | object | field | field | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |
| ent_m6 | object | referee | referee | person | raw_lemma | stage9_seed:parent_seed | person, human | m6 | raw_mention |  |  |  | True | {"canonical": "entity:referee", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m5 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e2 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e4 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e5 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | team |  |  |  | entity_exists:team | True | low |
| cf1 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf2 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf3 | entity_exists | referee |  |  | person, human | entity_exists:referee | True | high |
| cf4 | has_attribute | team | football |  | compound_modifier, visual_attribute | has_attribute:team:football | True | medium |
| cf5 | has_attribute | uniform | white |  | color_attribute, color, visual_attribute | has_attribute:uniform:white | True | high |
| cf6 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf7 | event_role | stand | agent | team |  | event_role:stand:agent:team | True | medium |
| cf8 | relation | team | in | uniform | spatial_containment, visual_relation | relation:team:in:uniform | True | high |
| cf9 | relation | team | on | field | spatial_support, visual_relation | relation:team:on:field | True | high |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | bikini | bikini | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:bikini", "parents": []} |
| ent_m4 | object | volleyball | volleyball | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:volleyball", "parents": []} |
| ent_m5 | object | net | net | object | raw_lemma | stage9_seed:parent_seed | sports_equipment, artifact | m5 | raw_mention |  |  |  | True | {"canonical": "entity:net", "parents": ["entity_parent:sports_equipment", "entity_parent:artifact"]} |
| ent_m6 | object | beach | beach | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:beach", "parents": []} |
| ent_m8 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m8 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m10 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m10 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m11 | object | umbrella | umbrellas | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:umbrella", "parents": []} |
| ent_m13 | object | sun | sun | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:sun", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m14 | jumps | jump | jump | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:jump", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m15 | hit | hit | hit | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m4->ent_m4 | {"canonical": "action:hit", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m16 | shining | shin | shin | raw_action | visual_action_fallback | visual_action |  | agent:m13->ent_m13 | {"canonical": "action:shin", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | jump | agent | m0 | ent_m0 | medium | e6 | nsubj -> jumps |  |  |
| ce1 | hit | agent | m0 | ent_m0 | medium | e7 | inherited agent advcl -> jumps |  |  |
| ce1 | hit | patient | m4 | ent_m4 | medium | e8 | dobj -> hit |  |  |
| ce2 | shin | agent | m13 | ent_m13 | medium | e9 | nsubj -> shining |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e10 | False | False |  |  |
| cr1 | m0 | m5 | ent_m4 | ent_m5 | over | above | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e11 | False | False | pp_source_disambiguation | patient_trajectory |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e12 | False | False |  |  |
| cr3 | m8 | m10 | ent_m8 | ent_m10 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e13 | False | False |  |  |
| cr4 | m8 | m11 | ent_m8 | ent_m11 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e14 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | bikini |  |  |  | entity_exists:bikini | True | low |
| cf2 | entity_exists | volleyball |  |  |  | entity_exists:volleyball | True | low |
| cf3 | entity_exists | net |  |  | sports_equipment, artifact | entity_exists:net | True | medium |
| cf4 | entity_exists | beach |  |  |  | entity_exists:beach | True | low |
| cf5 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf6 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf7 | entity_exists | umbrella |  |  |  | entity_exists:umbrella | True | low |
| cf8 | entity_exists | sun |  |  |  | entity_exists:sun | True | low |
| cf9 | has_attribute | bikini | red |  | color_attribute, color, visual_attribute | has_attribute:bikini:red | True | high |
| cf10 | has_attribute | bikini | black |  | color_attribute, color, visual_attribute | has_attribute:bikini:black | True | high |
| cf11 | has_attribute | beach | sandy |  | material_attribute, material, visual_attribute | has_attribute:beach:sandy | True | medium |
| cf12 | has_attribute | people | other |  | modifier_attribute, visual_attribute | has_attribute:people:other | True | medium |
| cf13 | has_attribute | umbrella | white |  | color_attribute, color, visual_attribute | has_attribute:umbrella:white | True | high |
| cf14 | action_event | jump |  |  | locomotion_action, visual_action | action_event:jump | True | high |
| cf15 | event_role | jump | agent | woman |  | event_role:jump:agent:woman | True | medium |
| cf16 | action_event | hit |  |  | visual_action | action_event:hit | True | low |
| cf17 | event_role | hit | agent | woman |  | event_role:hit:agent:woman | True | medium |
| cf18 | event_role | hit | patient | volleyball |  | event_role:hit:patient:volleyball | True | medium |
| cf19 | action_event | shin |  |  | visual_action | action_event:shin | True | low |
| cf20 | event_role | shin | agent | sun |  | event_role:shin:agent:sun | True | medium |
| cf21 | relation | woman | in | bikini | spatial_containment, visual_relation | relation:woman:in:bikini | True | high |
| cf22 | relation | volleyball | above | net | spatial_vertical, visual_relation | relation:volleyball:above:net | True | high |
| cf23 | relation | woman | on | beach | spatial_support, visual_relation | relation:woman:on:beach | True | high |
| cf24 | relation | people | in | background | spatial_containment, visual_relation | relation:people:in:background | True | high |
| cf25 | relation | people | under | umbrella | spatial_vertical, visual_relation | relation:people:under:umbrella | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| pp_source_disambiguated | m15 | e11 |  | ent_m5 | patient_trajectory | {"action_mention_id": "m15", "canonical_action": "hit", "canonical_source": "ent_m4", "canonical_target": "ent_m5", "confidence": "high", "kind": "pp_source_disambiguated", "previous_canonical_source": "ent_m0", "raw_edge_id": "e11", "raw_source": "m0", "raw_target": "m5", "reason": "patient_trajectory", "relation": "over"} |
| relation_lexical_canonicalized |  | e11 |  |  |  | {"canonical": "above", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e11", "raw_relation": "over", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | player | player | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:player", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | uniform | uniform | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m4 | object | snow | snow | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:snow", "parents": []} |
| ent_m6 | object | field | field | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |
| ent_m8 | object | player | player | person | raw_lemma | stage9_seed:parent_seed | person, human | m8 | raw_mention |  |  |  | True | {"canonical": "entity:player", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | runs | run | run | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:run", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | run | agent | m0 | ent_m0 | medium | e4 | nsubj -> runs |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e5 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | through | through | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | medium | e6 | False | False |  |  |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | player |  |  | person, human | entity_exists:player | True | high |
| cf1 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf2 | entity_exists | snow |  |  |  | entity_exists:snow | True | low |
| cf3 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf4 | entity_exists | player |  |  | person, human | entity_exists:player | True | high |
| cf5 | has_attribute | player | lacrosse |  | compound_modifier, visual_attribute | has_attribute:player:lacrosse | True | medium |
| cf6 | has_attribute | uniform | white |  | color_attribute, color, visual_attribute | has_attribute:uniform:white | True | high |
| cf7 | has_attribute | snow | heavy |  | modifier_attribute, visual_attribute | has_attribute:snow:heavy | True | medium |
| cf8 | has_attribute | field | snowy |  | material_attribute, material, visual_attribute | has_attribute:field:snowy | True | medium |
| cf9 | action_event | run |  |  | locomotion_action, visual_action | action_event:run | True | high |
| cf10 | event_role | run | agent | player |  | event_role:run:agent:player | True | medium |
| cf11 | relation | player | in | uniform | spatial_containment, visual_relation | relation:player:in:uniform | True | high |
| cf12 | relation | player | through | snow | spatial_path, visual_relation | relation:player:through:snow | True | medium |
| cf13 | relation | player | on | field | spatial_support, visual_relation | relation:player:on:field | True | high |

### Stage 9 Canonicalization Notes
_none_
