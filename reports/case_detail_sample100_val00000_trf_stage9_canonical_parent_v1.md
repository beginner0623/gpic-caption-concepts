# Stage 9 Canonical Parent v1 Case Detail - sample100 val00000

- input: `reports\canonical_concepts_sample100_val00000_trf_stage9_canonical_parent_v1.jsonl`
- max_records: `100`
- contents: raw concept mentions/edges + Stage 9 canonical entities/events/relations

## 01

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `005a13525e45210df2a71777a9060032b3221dbee0e39d5344213385b23c8814`
**parse_path:** `sentence`

> A person with dreadlocks and a red bow sits at a table with art posters and stickers.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | dreadlocks | dreadlock | noun_chunk_root | chunk1 | 3 | high |
| m2 | object | bow | bow | noun_chunk_root | chunk2 | 7 | high |
| m3 | attribute | red | red | color_attribute | chunk2 | 6 | high |
| m4 | object | table | table | noun_chunk_root | chunk3 | 11 | high |
| m5 | object | posters | poster | noun_chunk_root | chunk4 | 14 | high |
| m6 | attribute | art | art | compound_modifier | chunk4 | 13 | medium |
| m7 | object | stickers | sticker | noun_chunk_root | chunk5 | 16 | high |
| m8 | action | sits | sit | verb_predicate | doc | 8 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | chunk2 amod -> bow |
| e1 | has_attribute | m5 | m6 | medium | chunk4 compound -> posters |
| e2 | agent | m8 | m0 | medium | nsubj -> sits |
| e3 | relation | m0 | m1 | high | with |
| e4 | relation | m0 | m2 | high | with |
| e5 | relation | m0 | m4 | medium | at |
| e6 | relation | m0 | m5 | high | with |
| e7 | relation | m0 | m7 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | dreadlock | dreadlocks | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:dreadlock", "parents": []} |
| ent_m2 | object | bow | bow | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:bow", "parents": []} |
| ent_m4 | object | table | table | object | furniture, artifact | m4 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m5 | object | poster | posters | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:poster", "parents": []} |
| ent_m7 | object | sticker | stickers | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:sticker", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | sits | sit | sit | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m0 | ent_m0 | medium | e2 | nsubj -> sits |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | with | association_relation, visual_relation | high | e3 | False | False |  |  |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e4 | False | False |  |  |
| cr2 | m0 | m4 | ent_m0 | ent_m4 | at | at | spatial_location, visual_relation | medium | e5 | False | False |  |  |
| cr3 | m0 | m5 | ent_m0 | ent_m5 | with | with | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr4 | m0 | m7 | ent_m0 | ent_m7 | with | with | association_relation, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf1 | entity_exists | dreadlock |  |  |  | entity_exists:dreadlock | True | low |
| cf2 | entity_exists | bow |  |  |  | entity_exists:bow | True | low |
| cf3 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf4 | entity_exists | poster |  |  |  | entity_exists:poster | True | low |
| cf5 | entity_exists | sticker |  |  |  | entity_exists:sticker | True | low |
| cf6 | has_attribute | bow | red |  | color_attribute, color, visual_attribute | has_attribute:bow:red | True | high |
| cf7 | has_attribute | poster | art |  | compound_modifier, visual_attribute | has_attribute:poster:art | True | medium |
| cf8 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf9 | event_role | sit | agent | person |  | event_role:sit:agent:person | True | medium |
| cf10 | relation | person | with | dreadlock | association_relation, visual_relation | relation:person:with:dreadlock | True | high |
| cf11 | relation | person | with | bow | association_relation, visual_relation | relation:person:with:bow | True | high |
| cf12 | relation | person | at | table | spatial_location, visual_relation | relation:person:at:table | True | medium |
| cf13 | relation | person | with | poster | association_relation, visual_relation | relation:person:with:poster | True | high |
| cf14 | relation | person | with | sticker | association_relation, visual_relation | relation:person:with:sticker | True | high |

### Stage 9 Canonicalization Notes
_none_

## 02

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `010bb91bf88524cee960135440eff96892d317358f1ef9e027accc6882429c14`
**parse_path:** `sentence`

> A brown insect with wings is crawling on a cracked, weathered wooden surface. The wood shows signs of age with visible splits and small bits of debris scattered around. The scene appears outdoors on a forest floor or fallen tree trunk.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | insect | insect | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | brown | brown | color_attribute | chunk0 | 1 | high |
| m2 | object | wings | wing | noun_chunk_root | chunk1 | 4 | high |
| m3 | context | surface | surface | spatial_region | chunk2 | 13 | medium |
| m4 | object | wood | wood | noun_chunk_root | chunk3 | 16 | high |
| m5 | object | signs | sign | noun_chunk_root | chunk4 | 18 | high |
| m6 | object | age | age | noun_chunk_root | chunk5 | 20 | high |
| m7 | object | splits | split | noun_chunk_root | chunk6 | 23 | high |
| m8 | attribute | visible | visible | modifier_attribute | chunk6 | 22 | medium |
| m9 | object | bits | bit | noun_chunk_root | chunk7 | 26 | high |
| m10 | attribute | small | small | size_attribute | chunk7 | 25 | high |
| m11 | object | debris | debris | noun_chunk_root | chunk8 | 28 | high |
| m12 | context | scene | scene | scene_context | chunk9 | 33 | high |
| m13 | object | floor | floor | noun_chunk_root | chunk10 | 39 | high |
| m14 | attribute | forest | forest | compound_modifier | chunk10 | 38 | medium |
| m15 | object | tree trunk | tree_trunk | noun_chunk_root | chunk11 | 42 | high |
| m16 | attribute | fallen | fallen | modifier_attribute | chunk11 | 41 | medium |
| m17 | context | outdoors | outdoors | scene_context | doc | 35 | high |
| m18 | action | crawling | crawl | verb_predicate | doc | 6 | high |
| m19 | action | shows | show | verb_predicate | doc | 17 | high |
| m20 | action | scattered | scatter | verb_predicate | doc | 29 | high |
| m21 | action | appears | appear | verb_predicate | doc | 34 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> insect |
| e1 | has_attribute | m7 | m8 | medium | chunk6 amod -> splits |
| e2 | has_attribute | m9 | m10 | high | chunk7 amod -> bits |
| e3 | has_context | scene | m12 | high | scene_context token scene |
| e4 | has_attribute | m13 | m14 | medium | chunk10 compound -> floor |
| e5 | has_attribute | m15 | m16 | medium | chunk11 amod -> tree trunk |
| e6 | has_context | scene | m17 | high | scene_context token outdoors |
| e7 | agent | m18 | m0 | medium | nsubj -> crawling |
| e8 | agent | m19 | m4 | medium | nsubj -> shows |
| e9 | patient | m19 | m5 | medium | dobj -> shows |
| e10 | agent | m20 | m7 | medium | inherited agent acl -> splits |
| e11 | agent | m21 | m12 | medium | nsubj -> appears |
| e12 | relation | m0 | m2 | high | with |
| e13 | relation | m0 | m3 | high | on |
| e14 | relation | m5 | m6 | medium | of |
| e15 | relation | m4 | m7 | high | with |
| e16 | relation | m4 | m9 | high | with |
| e17 | relation | m9 | m11 | medium | of |
| e18 | relation | m12 | m13 | high | on |
| e19 | relation | m12 | m15 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | insect | insect | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:insect", "parents": []} |
| ent_m2 | object | wing | wings | object | body_part | m2 | raw_mention |  |  |  | True | {"canonical": "entity:wing", "parents": ["entity_parent:body_part"]} |
| ent_m3 | context | surface | surface | object | scene_context | m3 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": ["entity_parent:scene_context"]} |
| ent_m4 | object | wood | wood | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:wood", "parents": []} |
| ent_m5 | object | sign | signs | document | text_carrier, artifact | m5 | raw_mention |  |  |  | True | {"canonical": "entity:sign", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m6 | object | age | age | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:age", "parents": []} |
| ent_m7 | object | split | splits | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:split", "parents": []} |
| ent_m9 | object | bit | bits | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:bit", "parents": []} |
| ent_m11 | object | debris | debris | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:debris", "parents": []} |
| ent_m12 | context | scene | scene | object | scene_context | m12 | raw_mention |  |  |  | True | {"canonical": "entity:scene", "parents": ["entity_parent:scene_context"]} |
| ent_m13 | object | floor | floor | object |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:floor", "parents": []} |
| ent_m15 | object | tree_trunk | tree trunk | object |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:tree_trunk", "parents": []} |
| ent_m17 | context | outdoors | outdoors | object | scene_context | m17 | raw_mention |  |  |  | True | {"canonical": "entity:outdoors", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | crawling | crawl | crawl | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:crawl", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m19 | shows | show | show | visual_action |  | agent:m4->ent_m4; patient:m5->ent_m5 | {"canonical": "action:show", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m20 | scattered | scatter | scatter | visual_action |  | agent:m7->ent_m7 | {"canonical": "action:scatter", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m21 | appears | appear | appear | visual_action |  | agent:m12->ent_m12 | {"canonical": "action:appear", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | crawl | agent | m0 | ent_m0 | medium | e7 | nsubj -> crawling |  |  |
| ce1 | show | agent | m4 | ent_m4 | medium | e8 | nsubj -> shows |  |  |
| ce1 | show | patient | m5 | ent_m5 | medium | e9 | dobj -> shows |  |  |
| ce2 | scatter | agent | m7 | ent_m7 | medium | e10 | inherited agent acl -> splits |  |  |
| ce3 | appear | agent | m12 | ent_m12 | medium | e11 | nsubj -> appears |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e12 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | on | on | spatial_support, visual_relation | high | e13 | False | False |  |  |
| cr2 | m5 | m6 | ent_m5 | ent_m6 | of | of | part_relation, visual_relation | medium | e14 | False | False |  |  |
| cr3 | m4 | m7 | ent_m4 | ent_m7 | with | with | association_relation, visual_relation | high | e15 | False | False |  |  |
| cr4 | m4 | m9 | ent_m4 | ent_m9 | with | with | association_relation, visual_relation | high | e16 | False | False |  |  |
| cr5 | m9 | m11 | ent_m9 | ent_m11 | of | of | part_relation, visual_relation | medium | e17 | False | False |  |  |
| cr6 | m12 | m13 | ent_m12 | ent_m13 | on | on | spatial_support, visual_relation | high | e18 | False | False |  |  |
| cr7 | m12 | m15 | ent_m12 | ent_m15 | on | on | spatial_support, visual_relation | high | e19 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | insect |  |  |  | entity_exists:insect | True | low |
| cf1 | entity_exists | wing |  |  | body_part | entity_exists:wing | True | medium |
| cf2 | entity_exists | surface |  |  | scene_context | entity_exists:surface | True | medium |
| cf3 | entity_exists | wood |  |  |  | entity_exists:wood | True | low |
| cf4 | entity_exists | sign |  |  | text_carrier, artifact | entity_exists:sign | True | high |
| cf5 | entity_exists | age |  |  |  | entity_exists:age | True | low |
| cf6 | entity_exists | split |  |  |  | entity_exists:split | True | low |
| cf7 | entity_exists | bit |  |  |  | entity_exists:bit | True | low |
| cf8 | entity_exists | debris |  |  |  | entity_exists:debris | True | low |
| cf9 | entity_exists | scene |  |  | scene_context | entity_exists:scene | True | high |
| cf10 | entity_exists | floor |  |  |  | entity_exists:floor | True | low |
| cf11 | entity_exists | tree_trunk |  |  |  | entity_exists:tree_trunk | True | low |
| cf12 | entity_exists | outdoors |  |  | scene_context | entity_exists:outdoors | True | high |
| cf13 | has_attribute | insect | brown |  | color_attribute, color, visual_attribute | has_attribute:insect:brown | True | high |
| cf14 | has_attribute | split | visible |  | modifier_attribute, visual_attribute | has_attribute:split:visible | True | medium |
| cf15 | has_attribute | bit | small |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:bit:small | True | high |
| cf16 | has_attribute | floor | forest |  | compound_modifier, visual_attribute | has_attribute:floor:forest | True | medium |
| cf17 | has_attribute | tree_trunk | fallen |  | modifier_attribute, visual_attribute | has_attribute:tree_trunk:fallen | True | medium |
| cf18 | action_event | crawl |  |  | visual_action | action_event:crawl | True | low |
| cf19 | event_role | crawl | agent | insect |  | event_role:crawl:agent:insect | True | medium |
| cf20 | action_event | show |  |  | visual_action | action_event:show | True | low |
| cf21 | event_role | show | agent | wood |  | event_role:show:agent:wood | True | medium |
| cf22 | event_role | show | patient | sign |  | event_role:show:patient:sign | True | medium |
| cf23 | action_event | scatter |  |  | visual_action | action_event:scatter | True | low |
| cf24 | event_role | scatter | agent | split |  | event_role:scatter:agent:split | True | medium |
| cf25 | action_event | appear |  |  | visual_action | action_event:appear | True | low |
| cf26 | event_role | appear | agent | scene |  | event_role:appear:agent:scene | True | medium |
| cf27 | relation | insect | with | wing | association_relation, visual_relation | relation:insect:with:wing | True | high |
| cf28 | relation | insect | on | surface | spatial_support, visual_relation | relation:insect:on:surface | True | high |
| cf29 | relation | sign | of | age | part_relation, visual_relation | relation:sign:of:age | True | medium |
| cf30 | relation | wood | with | split | association_relation, visual_relation | relation:wood:with:split | True | high |
| cf31 | relation | wood | with | bit | association_relation, visual_relation | relation:wood:with:bit | True | high |
| cf32 | relation | bit | of | debris | part_relation, visual_relation | relation:bit:of:debris | True | medium |
| cf33 | relation | scene | on | floor | spatial_support, visual_relation | relation:scene:on:floor | True | high |
| cf34 | relation | scene | on | tree_trunk | spatial_support, visual_relation | relation:scene:on:tree_trunk | True | high |

### Stage 9 Canonicalization Notes
_none_

## 03

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `0326facce37e93230108fb311cc653eecb8ee62a67a1f0d9f95525ddd9fe3014`
**parse_path:** `sentence`

> A woman stands at a podium speaking in front of an audience. An American flag is behind her, and a screen shows the text "Closing the Access Divide."

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "Closing the Access Divide." | closing_the_access_divide. | quote_text | doc_quote | 25 | high |
| m1 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m2 | object | podium | podium | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | audience | audience | noun_chunk_root | chunk3 | 11 | high |
| m4 | object | American flag | american_flag | noun_chunk_root | chunk4 | 14 | high |
| m5 | object | screen | screen | noun_chunk_root | chunk6 | 21 | high |
| m6 | object | text | text | noun_chunk_root | chunk7 | 24 | high |
| m7 | action | stands | stand | verb_predicate | doc | 2 | high |
| m8 | action | speaking | speak | verb_predicate | doc | 6 | high |
| m9 | action | shows | show | verb_predicate | doc | 22 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m6 | m0 | high | quote appos -> text |
| e1 | agent | m7 | m1 | medium | nsubj -> stands |
| e2 | agent | m8 | m1 | medium | inherited agent advcl -> stands |
| e3 | agent | m9 | m5 | medium | nsubj -> shows |
| e4 | patient | m9 | m6 | medium | dobj -> shows |
| e5 | relation | m1 | m2 | medium | at |
| e6 | relation | m1 | m3 | high | in_front_of |
| e7 | relation | m4 | m1 | high | behind |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | woman | woman | person | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | podium | podium | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:podium", "parents": []} |
| ent_m3 | object | audience | audience | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:audience", "parents": []} |
| ent_m4 | object | american_flag | American flag | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:american_flag", "parents": []} |
| ent_m5 | object | screen | screen | device | device, artifact | m5 | raw_mention |  |  |  | True | {"canonical": "entity:screen", "parents": ["entity_parent:device", "entity_parent:artifact"]} |
| ent_m6 | object | text | text | document | text_content | m6 | raw_mention |  |  |  | True | {"canonical": "entity:text", "parents": ["entity_parent:text_content"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | stands | stand | stand | body_pose_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m8 | speaking | speak | speak | communication_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:speak", "parents": ["action_parent:communication_action", "action_parent:visual_action"]} |  |
| ce2 | m9 | shows | show | show | visual_action |  | agent:m5->ent_m5; patient:m6->ent_m6 | {"canonical": "action:show", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m1 | ent_m1 | medium | e1 | nsubj -> stands |  |  |
| ce1 | speak | agent | m1 | ent_m1 | medium | e2 | inherited agent advcl -> stands |  |  |
| ce2 | show | agent | m5 | ent_m5 | medium | e3 | nsubj -> shows |  |  |
| ce2 | show | patient | m6 | ent_m6 | medium | e4 | dobj -> shows |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | at | at | spatial_location, visual_relation | medium | e5 | False | False |  |  |
| cr1 | m1 | m3 | ent_m1 | ent_m3 | in_front_of | in_front_of | spatial_depth, visual_relation | high | e6 | False | False |  |  |
| cr2 | m4 | m1 | ent_m4 | ent_m1 | behind | behind | spatial_depth, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | podium |  |  |  | entity_exists:podium | True | low |
| cf2 | entity_exists | audience |  |  |  | entity_exists:audience | True | low |
| cf3 | entity_exists | american_flag |  |  |  | entity_exists:american_flag | True | low |
| cf4 | entity_exists | screen |  |  | device, artifact | entity_exists:screen | True | high |
| cf5 | entity_exists | text |  |  | text_content | entity_exists:text | True | high |
| cf6 | has_attribute | text | closing_the_access_divide. |  | quote_text, visual_attribute | has_attribute:text:closing_the_access_divide. | True | high |
| cf7 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf8 | event_role | stand | agent | woman |  | event_role:stand:agent:woman | True | medium |
| cf9 | action_event | speak |  |  | communication_action, visual_action | action_event:speak | True | medium |
| cf10 | event_role | speak | agent | woman |  | event_role:speak:agent:woman | True | medium |
| cf11 | action_event | show |  |  | visual_action | action_event:show | True | low |
| cf12 | event_role | show | agent | screen |  | event_role:show:agent:screen | True | medium |
| cf13 | event_role | show | patient | text |  | event_role:show:patient:text | True | medium |
| cf14 | relation | woman | at | podium | spatial_location, visual_relation | relation:woman:at:podium | True | medium |
| cf15 | relation | woman | in_front_of | audience | spatial_depth, visual_relation | relation:woman:in_front_of:audience | True | high |
| cf16 | relation | american_flag | behind | woman | spatial_depth, visual_relation | relation:american_flag:behind:woman | True | high |

### Stage 9 Canonicalization Notes
_none_

## 04

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `03dfd14a3d7fc8b961a00424e43bfbdfcb9eded2464416b15cc6e9441a503814`
**parse_path:** `sentence`

> Three people stand with a shopping cart filled with groceries and bags. One person holds a red snack bag.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Three | three | exact_quantity | chunk0 | 0 | high |
| m2 | object | shopping cart | shopping_cart | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | groceries | grocery | noun_chunk_root | chunk2 | 8 | high |
| m4 | object | bags | bag | noun_chunk_root | chunk3 | 10 | high |
| m5 | object | person | person | noun_chunk_root | chunk4 | 13 | high |
| m6 | quantity | One | one | exact_quantity | chunk4 | 12 | high |
| m7 | object | bag | bag | noun_chunk_root | chunk5 | 18 | high |
| m8 | attribute | red | red | color_attribute | chunk5 | 16 | high |
| m9 | attribute | snack | snack | compound_modifier | chunk5 | 17 | medium |
| m10 | action | stand | stand | verb_predicate | doc | 2 | high |
| m11 | action | filled | fill | verb_predicate | doc | 6 | high |
| m12 | action | holds | hold | verb_predicate | doc | 14 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> people |
| e1 | has_quantity | m5 | m6 | high | chunk4 quantity -> person |
| e2 | has_attribute | m7 | m8 | high | chunk5 amod -> bag |
| e3 | has_attribute | m7 | m9 | medium | chunk5 compound -> bag |
| e4 | agent | m10 | m0 | medium | nsubj -> stand |
| e5 | agent | m11 | m2 | medium | inherited agent acl -> shopping cart |
| e6 | agent | m12 | m5 | medium | nsubj -> holds |
| e7 | patient | m12 | m7 | medium | dobj -> holds |
| e8 | relation | m0 | m2 | high | with |
| e9 | relation | m2 | m3 | high | with |
| e10 | relation | m2 | m4 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | shopping_cart | shopping cart | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:shopping_cart", "parents": []} |
| ent_m3 | object | grocery | groceries | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:grocery", "parents": []} |
| ent_m4 | object | bag | bags | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:bag", "parents": []} |
| ent_m5 | object | person | person | person | person, human | m5 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m7 | object | bag | bag | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:bag", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | stand | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m11 | filled | fill | fill | visual_action |  | agent:m2->ent_m2 | {"canonical": "action:fill", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m12 | holds | hold | hold | manipulation_action, visual_action |  | agent:m5->ent_m5; patient:m7->ent_m7 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e4 | nsubj -> stand |  |  |
| ce1 | fill | agent | m2 | ent_m2 | medium | e5 | inherited agent acl -> shopping cart |  |  |
| ce2 | hold | agent | m5 | ent_m5 | medium | e6 | nsubj -> holds |  |  |
| ce2 | hold | patient | m7 | ent_m7 | medium | e7 | dobj -> holds |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e8 | False | False |  |  |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | with | with | association_relation, visual_relation | high | e9 | False | False |  |  |
| cr2 | m2 | m4 | ent_m2 | ent_m4 | with | with | association_relation, visual_relation | high | e10 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | shopping_cart |  |  |  | entity_exists:shopping_cart | True | low |
| cf2 | entity_exists | grocery |  |  |  | entity_exists:grocery | True | low |
| cf3 | entity_exists | bag |  |  |  | entity_exists:bag | True | low |
| cf4 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf5 | entity_exists | bag |  |  |  | entity_exists:bag | True | low |
| cf6 | has_quantity | people | three |  | exact_quantity, quantity | has_quantity:people:three | True | high |
| cf7 | has_quantity | person | one |  | exact_quantity, quantity | has_quantity:person:one | True | high |
| cf8 | has_attribute | bag | red |  | color_attribute, color, visual_attribute | has_attribute:bag:red | True | high |
| cf9 | has_attribute | bag | snack |  | compound_modifier, visual_attribute | has_attribute:bag:snack | True | medium |
| cf10 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf11 | event_role | stand | agent | people |  | event_role:stand:agent:people | True | medium |
| cf12 | action_event | fill |  |  | visual_action | action_event:fill | True | low |
| cf13 | event_role | fill | agent | shopping_cart |  | event_role:fill:agent:shopping_cart | True | medium |
| cf14 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf15 | event_role | hold | agent | person |  | event_role:hold:agent:person | True | medium |
| cf16 | event_role | hold | patient | bag |  | event_role:hold:patient:bag | True | medium |
| cf17 | relation | people | with | shopping_cart | association_relation, visual_relation | relation:people:with:shopping_cart | True | high |
| cf18 | relation | shopping_cart | with | grocery | association_relation, visual_relation | relation:shopping_cart:with:grocery | True | high |
| cf19 | relation | shopping_cart | with | bag | association_relation, visual_relation | relation:shopping_cart:with:bag | True | high |

### Stage 9 Canonicalization Notes
_none_

## 05

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `049ccab2d0384df0e916b4cb21c0840387d630be1c36548aa7f05dad5f5d4014`
**parse_path:** `sentence`

> Bright orange glass flowers stand in a garden bed with green grass and purple blooms. In the background, people walk near a wooden fence under a large umbrella. Trees and a blue structure are visible beyond the garden area.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | flowers | flower | noun_chunk_root | chunk0 | 3 | high |
| m1 | attribute | Bright | bright | visual_attribute | chunk0 | 0 | medium |
| m2 | attribute | orange | orange | color_attribute | chunk0 | 1 | high |
| m3 | attribute | glass | glass | material_attribute | chunk0 | 2 | high |
| m4 | object | bed | bed | noun_chunk_root | chunk1 | 8 | high |
| m5 | attribute | garden | garden | compound_modifier | chunk1 | 7 | medium |
| m6 | object | grass | grass | noun_chunk_root | chunk2 | 11 | high |
| m7 | attribute | green | green | color_attribute | chunk2 | 10 | high |
| m8 | object | blooms | bloom | noun_chunk_root | chunk3 | 14 | high |
| m9 | attribute | purple | purple | color_attribute | chunk3 | 13 | high |
| m10 | context | background | background | scene_context | chunk4 | 18 | high |
| m11 | object | people | people | noun_chunk_root | chunk5 | 20 | high |
| m12 | object | fence | fence | noun_chunk_root | chunk6 | 25 | high |
| m13 | attribute | wooden | wooden | material_attribute | chunk6 | 24 | high |
| m14 | object | umbrella | umbrella | noun_chunk_root | chunk7 | 29 | high |
| m15 | attribute | large | large | size_attribute | chunk7 | 28 | high |
| m16 | object | Trees | tree | noun_chunk_root | chunk8 | 31 | high |
| m17 | object | structure | structure | noun_chunk_root | chunk9 | 35 | high |
| m18 | attribute | blue | blue | color_attribute | chunk9 | 34 | high |
| m19 | object | area | area | noun_chunk_root | chunk10 | 41 | high |
| m20 | attribute | garden | garden | compound_modifier | chunk10 | 40 | medium |
| m21 | action | stand | stand | verb_predicate | doc | 4 | high |
| m22 | action | walk | walk | verb_predicate | doc | 21 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> flowers |
| e1 | has_attribute | m0 | m2 | high | chunk0 compound -> flowers |
| e2 | has_attribute | m0 | m3 | high | chunk0 compound -> flowers |
| e3 | has_attribute | m4 | m5 | medium | chunk1 compound -> bed |
| e4 | has_attribute | m6 | m7 | high | chunk2 amod -> grass |
| e5 | has_attribute | m8 | m9 | high | chunk3 amod -> blooms |
| e6 | has_context | scene | m10 | high | scene_context token background |
| e7 | has_attribute | m12 | m13 | high | chunk6 amod -> fence |
| e8 | has_attribute | m14 | m15 | high | chunk7 amod -> umbrella |
| e9 | has_attribute | m17 | m18 | high | chunk9 amod -> structure |
| e10 | has_attribute | m19 | m20 | medium | chunk10 compound -> area |
| e11 | agent | m21 | m0 | medium | nsubj -> stand |
| e12 | agent | m22 | m11 | medium | nsubj -> walk |
| e13 | relation | m0 | m4 | high | in |
| e14 | relation | m4 | m6 | high | with |
| e15 | relation | m4 | m8 | high | with |
| e16 | relation | m11 | m10 | high | in |
| e17 | relation | m11 | m12 | high | near |
| e18 | relation | m11 | m14 | high | under |
| e19 | relation | m16 | m19 | high | beyond |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | flower | flowers | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:flower", "parents": []} |
| ent_m4 | object | bed | bed | object | furniture, artifact | m4 | raw_mention |  |  |  | True | {"canonical": "entity:bed", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m6 | object | grass | grass | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": []} |
| ent_m8 | object | bloom | blooms | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:bloom", "parents": []} |
| ent_m10 | context | background | background | object | scene_context | m10 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m11 | object | people | people | person | person, human | m11 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m12 | object | fence | fence | object |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:fence", "parents": []} |
| ent_m14 | object | umbrella | umbrella | object |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:umbrella", "parents": []} |
| ent_m16 | object | tree | Trees | object |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m17 | object | structure | structure | object |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:structure", "parents": []} |
| ent_m19 | object | area | area | object |  | m19 | raw_mention |  |  |  | True | {"canonical": "entity:area", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m21 | stand | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m22 | walk | walk | walk | locomotion_action, visual_action |  | agent:m11->ent_m11 | {"canonical": "action:walk", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e11 | nsubj -> stand |  |  |
| ce1 | walk | agent | m11 | ent_m11 | medium | e12 | nsubj -> walk |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | in | in | spatial_containment, visual_relation | high | e13 | False | False |  |  |
| cr1 | m4 | m6 | ent_m4 | ent_m6 | with | with | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr2 | m4 | m8 | ent_m4 | ent_m8 | with | with | association_relation, visual_relation | high | e15 | False | False |  |  |
| cr3 | m11 | m10 | ent_m11 | ent_m10 | in | in | spatial_containment, visual_relation | high | e16 | False | False |  |  |
| cr4 | m11 | m12 | ent_m11 | ent_m12 | near | near | spatial_proximity, visual_relation | high | e17 | False | False |  |  |
| cr5 | m11 | m14 | ent_m11 | ent_m14 | under | under | spatial_vertical, visual_relation | high | e18 | False | False |  |  |
| cr6 | m16 | m19 | ent_m16 | ent_m19 | beyond | beyond | visual_relation | high | e19 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | flower |  |  |  | entity_exists:flower | True | low |
| cf1 | entity_exists | bed |  |  | furniture, artifact | entity_exists:bed | True | high |
| cf2 | entity_exists | grass |  |  |  | entity_exists:grass | True | low |
| cf3 | entity_exists | bloom |  |  |  | entity_exists:bloom | True | low |
| cf4 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf5 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf6 | entity_exists | fence |  |  |  | entity_exists:fence | True | low |
| cf7 | entity_exists | umbrella |  |  |  | entity_exists:umbrella | True | low |
| cf8 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf9 | entity_exists | structure |  |  |  | entity_exists:structure | True | low |
| cf10 | entity_exists | area |  |  |  | entity_exists:area | True | low |
| cf11 | has_attribute | flower | bright |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:flower:bright | True | medium |
| cf12 | has_attribute | flower | orange |  | color_attribute, color, visual_attribute | has_attribute:flower:orange | True | high |
| cf13 | has_attribute | flower | glass |  | material_attribute, material, visual_attribute | has_attribute:flower:glass | True | high |
| cf14 | has_attribute | bed | garden |  | compound_modifier, visual_attribute | has_attribute:bed:garden | True | medium |
| cf15 | has_attribute | grass | green |  | color_attribute, color, visual_attribute | has_attribute:grass:green | True | high |
| cf16 | has_attribute | bloom | purple |  | color_attribute, color, visual_attribute | has_attribute:bloom:purple | True | high |
| cf17 | has_attribute | fence | wooden |  | material_attribute, material, visual_attribute | has_attribute:fence:wooden | True | high |
| cf18 | has_attribute | umbrella | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:umbrella:large | True | high |
| cf19 | has_attribute | structure | blue |  | color_attribute, color, visual_attribute | has_attribute:structure:blue | True | high |
| cf20 | has_attribute | area | garden |  | compound_modifier, visual_attribute | has_attribute:area:garden | True | medium |
| cf21 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf22 | event_role | stand | agent | flower |  | event_role:stand:agent:flower | True | medium |
| cf23 | action_event | walk |  |  | locomotion_action, visual_action | action_event:walk | True | high |
| cf24 | event_role | walk | agent | people |  | event_role:walk:agent:people | True | medium |
| cf25 | relation | flower | in | bed | spatial_containment, visual_relation | relation:flower:in:bed | True | high |
| cf26 | relation | bed | with | grass | association_relation, visual_relation | relation:bed:with:grass | True | high |
| cf27 | relation | bed | with | bloom | association_relation, visual_relation | relation:bed:with:bloom | True | high |
| cf28 | relation | people | in | background | spatial_containment, visual_relation | relation:people:in:background | True | high |
| cf29 | relation | people | near | fence | spatial_proximity, visual_relation | relation:people:near:fence | True | high |
| cf30 | relation | people | under | umbrella | spatial_vertical, visual_relation | relation:people:under:umbrella | True | high |
| cf31 | relation | tree | beyond | area | visual_relation | relation:tree:beyond:area | True | high |

### Stage 9 Canonicalization Notes
_none_

## 06

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `050521436694404336ade2d13e39d7635191e3ea8eccf2a0c80cf128880d7414`
**parse_path:** `tag_list`

> smiling couple, formal party, british flags, chandelier, wine glasses

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | couple | couple | segment_head | t0 | 1 | high |
| m1 | attribute | smiling | smile | state_attribute | t0 | 0 | high |
| m2 | object | party | party | segment_head | t1 | 1 | high |
| m3 | attribute | formal | formal | attribute | t1 | 0 | high |
| m4 | object | flags | flag | segment_head | t2 | 1 | high |
| m5 | attribute | british | british | attribute | t2 | 0 | high |
| m6 | object | chandelier | chandelier | segment_head | t3 | 0 | high |
| m7 | object | wine glasses | wine_glass | segment_head | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> couple |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> party |
| e2 | has_attribute | m4 | m5 | high | t2 internal amod -> flags |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | couple | couple | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:couple", "parents": []} |
| ent_m2 | object | party | party | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:party", "parents": []} |
| ent_m4 | object | flag | flags | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:flag", "parents": []} |
| ent_m6 | object | chandelier | chandelier | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:chandelier", "parents": []} |
| ent_m7 | object | wine_glass | wine glasses | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:wine_glass", "parents": []} |

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
| cf0 | entity_exists | couple |  |  |  | entity_exists:couple | True | low |
| cf1 | entity_exists | party |  |  |  | entity_exists:party | True | low |
| cf2 | entity_exists | flag |  |  |  | entity_exists:flag | True | low |
| cf3 | entity_exists | chandelier |  |  |  | entity_exists:chandelier | True | low |
| cf4 | entity_exists | wine_glass |  |  |  | entity_exists:wine_glass | True | low |
| cf5 | has_attribute | couple | smile |  | state_attribute, visual_attribute | has_attribute:couple:smile | True | high |
| cf6 | has_attribute | party | formal |  | attribute, visual_attribute | has_attribute:party:formal | True | high |
| cf7 | has_attribute | flag | british |  | attribute, visual_attribute | has_attribute:flag:british | True | high |

### Stage 9 Canonicalization Notes
_none_

## 07

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `054a504fff891dae0e43522f858a2e7df4e2a5c21d99937f70462b69a4386414`
**parse_path:** `sentence`

> A white church with a cross on top has stone steps leading to a wooden door.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | church | church | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | white | white | color_attribute | chunk0 | 1 | high |
| m2 | object | cross | cross | noun_chunk_root | chunk1 | 5 | high |
| m3 | context | top | top | spatial_region | chunk2 | 7 | medium |
| m4 | object | steps | step | noun_chunk_root | chunk3 | 10 | high |
| m5 | attribute | stone | stone | material_attribute | chunk3 | 9 | high |
| m6 | object | door | door | noun_chunk_root | chunk4 | 15 | high |
| m7 | attribute | wooden | wooden | material_attribute | chunk4 | 14 | high |
| m8 | action | has | have | verb_predicate | doc | 8 | high |
| m9 | action | leading | lead | verb_predicate | doc | 11 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> church |
| e1 | has_attribute | m4 | m5 | high | chunk3 compound -> steps |
| e2 | has_attribute | m6 | m7 | high | chunk4 amod -> door |
| e3 | agent | m8 | m0 | medium | nsubj -> has |
| e4 | patient | m8 | m4 | medium | dobj -> has |
| e5 | agent | m9 | m4 | medium | inherited agent acl -> steps |
| e6 | relation | m0 | m2 | high | with |
| e7 | relation | m2 | m3 | high | on |
| e8 | relation | m4 | m6 | medium | to |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | church | church | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:church", "parents": []} |
| ent_m2 | object | cross | cross | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:cross", "parents": []} |
| ent_m3 | context | top | top | object | scene_context | m3 | raw_mention |  |  |  | True | {"canonical": "entity:top", "parents": ["entity_parent:scene_context"]} |
| ent_m4 | object | step | steps | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:step", "parents": []} |
| ent_m6 | object | door | door | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:door", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | has | have | have | visual_action |  | agent:m0->ent_m0; patient:m4->ent_m4 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m9 | leading | lead | lead | visual_action |  | agent:m4->ent_m4 | {"canonical": "action:lead", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | have | agent | m0 | ent_m0 | medium | e3 | nsubj -> has |  |  |
| ce0 | have | patient | m4 | ent_m4 | medium | e4 | dobj -> has |  |  |
| ce1 | lead | agent | m4 | ent_m4 | medium | e5 | inherited agent acl -> steps |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | on | on | spatial_support, visual_relation | high | e7 | False | False |  |  |
| cr2 | m4 | m6 | ent_m4 | ent_m6 | to | to | visual_relation | medium | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | church |  |  |  | entity_exists:church | True | low |
| cf1 | entity_exists | cross |  |  |  | entity_exists:cross | True | low |
| cf2 | entity_exists | top |  |  | scene_context | entity_exists:top | True | medium |
| cf3 | entity_exists | step |  |  |  | entity_exists:step | True | low |
| cf4 | entity_exists | door |  |  |  | entity_exists:door | True | low |
| cf5 | has_attribute | church | white |  | color_attribute, color, visual_attribute | has_attribute:church:white | True | high |
| cf6 | has_attribute | step | stone |  | material_attribute, material, visual_attribute | has_attribute:step:stone | True | high |
| cf7 | has_attribute | door | wooden |  | material_attribute, material, visual_attribute | has_attribute:door:wooden | True | high |
| cf8 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf9 | event_role | have | agent | church |  | event_role:have:agent:church | True | medium |
| cf10 | event_role | have | patient | step |  | event_role:have:patient:step | True | medium |
| cf11 | action_event | lead |  |  | visual_action | action_event:lead | True | low |
| cf12 | event_role | lead | agent | step |  | event_role:lead:agent:step | True | medium |
| cf13 | relation | church | with | cross | association_relation, visual_relation | relation:church:with:cross | True | high |
| cf14 | relation | cross | on | top | spatial_support, visual_relation | relation:cross:on:top | True | high |
| cf15 | relation | step | to | door | visual_relation | relation:step:to:door | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 08

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `05784a8cb72a17349e2cd4389708153527b40af80a043636d0ff17fdcf16c014`
**parse_path:** `sentence`

> A poster on a black trash can reads "BANG GOES THE KNIGHTHOOD" with a silhouette of a man in a hat. The scene is on a city sidewalk.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "BANG GOES THE KNIGHTHOOD" | bang_goes_the_knighthood | quote_text | doc_quote | 7 | high |
| m1 | object | poster | poster | noun_chunk_root | chunk0 | 1 | high |
| m2 | object | trash can | trash_can | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | black | black | color_attribute | chunk1 | 4 | high |
| m4 | object | silhouette | silhouette | noun_chunk_root | chunk3 | 10 | high |
| m5 | object | man | man | noun_chunk_root | chunk4 | 13 | high |
| m6 | object | hat | hat | noun_chunk_root | chunk5 | 16 | high |
| m7 | context | scene | scene | scene_context | chunk6 | 19 | high |
| m8 | object | sidewalk | sidewalk | noun_chunk_root | chunk7 | 24 | high |
| m9 | attribute | city | city | compound_modifier | chunk7 | 23 | medium |
| m10 | action | reads | read | verb_predicate | doc | 6 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | chunk1 amod -> trash can |
| e1 | has_context | scene | m7 | high | scene_context token scene |
| e2 | has_attribute | m8 | m9 | medium | chunk7 compound -> sidewalk |
| e3 | agent | m10 | m1 | medium | nsubj -> reads |
| e4 | patient | m10 | m0 | medium | dobj -> reads |
| e5 | relation | m1 | m2 | high | on |
| e6 | relation | m1 | m4 | high | with |
| e7 | relation | m4 | m5 | medium | of |
| e8 | relation | m5 | m6 | high | in |
| e9 | relation | m7 | m8 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | poster | poster | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:poster", "parents": []} |
| ent_m2 | object | trash_can | trash can | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:trash_can", "parents": []} |
| ent_m4 | object | silhouette | silhouette | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:silhouette", "parents": []} |
| ent_m5 | object | man | man | person | person, human | m5 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m6 | object | hat | hat | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:hat", "parents": []} |
| ent_m7 | context | scene | scene | object | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:scene", "parents": ["entity_parent:scene_context"]} |
| ent_m8 | object | sidewalk | sidewalk | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:sidewalk", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | reads | read | read | text_interaction_action, visual_action |  | agent:m1->ent_m1; patient:m0->None | {"canonical": "action:read", "parents": ["action_parent:text_interaction_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | read | agent | m1 | ent_m1 | medium | e3 | nsubj -> reads |  |  |
| ce0 | read | patient | m0 |  | medium | e4 | dobj -> reads |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | on | on | spatial_support, visual_relation | high | e5 | False | False |  |  |
| cr1 | m1 | m4 | ent_m1 | ent_m4 | with | with | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr2 | m4 | m5 | ent_m4 | ent_m5 | of | of | part_relation, visual_relation | medium | e7 | False | False |  |  |
| cr3 | m5 | m6 | ent_m5 | ent_m6 | in | in | spatial_containment, visual_relation | high | e8 | False | False |  |  |
| cr4 | m7 | m8 | ent_m7 | ent_m8 | on | on | spatial_support, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | poster |  |  |  | entity_exists:poster | True | low |
| cf1 | entity_exists | trash_can |  |  |  | entity_exists:trash_can | True | low |
| cf2 | entity_exists | silhouette |  |  |  | entity_exists:silhouette | True | low |
| cf3 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf4 | entity_exists | hat |  |  |  | entity_exists:hat | True | low |
| cf5 | entity_exists | scene |  |  | scene_context | entity_exists:scene | True | high |
| cf6 | entity_exists | sidewalk |  |  |  | entity_exists:sidewalk | True | low |
| cf7 | has_attribute | trash_can | black |  | color_attribute, color, visual_attribute | has_attribute:trash_can:black | True | high |
| cf8 | has_attribute | sidewalk | city |  | compound_modifier, visual_attribute | has_attribute:sidewalk:city | True | medium |
| cf9 | action_event | read |  |  | text_interaction_action, visual_action | action_event:read | True | medium |
| cf10 | event_role | read | agent | poster |  | event_role:read:agent:poster | True | medium |
| cf11 | event_role | read | patient |  |  | event_role:read:patient | False | medium |
| cf12 | relation | poster | on | trash_can | spatial_support, visual_relation | relation:poster:on:trash_can | True | high |
| cf13 | relation | poster | with | silhouette | association_relation, visual_relation | relation:poster:with:silhouette | True | high |
| cf14 | relation | silhouette | of | man | part_relation, visual_relation | relation:silhouette:of:man | True | medium |
| cf15 | relation | man | in | hat | spatial_containment, visual_relation | relation:man:in:hat | True | high |
| cf16 | relation | scene | on | sidewalk | spatial_support, visual_relation | relation:scene:on:sidewalk | True | high |

### Stage 9 Canonicalization Notes
_none_

## 09

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `0670190ac8436d736a62a8bf08625ad242a7891121da4f518b00c9642570bc14`
**parse_path:** `sentence`

> A young child with blonde hair smiles widely while wearing a blue and white striped hat. The child is bare-shouldered and appears indoors, with a window visible in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | child | child | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | young | young | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | hair | hair | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | blonde | blonde | modifier_attribute | chunk1 | 4 | medium |
| m4 | object | hat | hat | noun_chunk_root | chunk2 | 15 | high |
| m5 | attribute | blue | blue | color_attribute | chunk2 | 11 | high |
| m6 | attribute | white | white | color_attribute | chunk2 | 13 | high |
| m7 | attribute | striped | strip | state_attribute | chunk2 | 14 | medium |
| m8 | object | child | child | noun_chunk_root | chunk3 | 18 | high |
| m9 | object | window | window | noun_chunk_root | chunk4 | 27 | high |
| m10 | context | background | background | scene_context | chunk5 | 31 | high |
| m11 | context | indoors | indoors | scene_context | doc | 23 | high |
| m12 | action | smiles | smile | verb_predicate | doc | 6 | high |
| m13 | action | wearing | wear | verb_predicate | doc | 9 | high |
| m14 | action | appears | appear | verb_predicate | doc | 22 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> child |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> hair |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> hat |
| e3 | has_attribute | m4 | m6 | high | chunk2 conj -> hat |
| e4 | has_attribute | m4 | m7 | medium | chunk2 amod -> hat |
| e5 | has_context | scene | m10 | high | scene_context token background |
| e6 | has_context | scene | m11 | high | scene_context token indoors |
| e7 | agent | m12 | m0 | medium | nsubj -> smiles |
| e8 | agent | m13 | m0 | medium | inherited agent advcl -> smiles |
| e9 | patient | m13 | m4 | medium | dobj -> wearing |
| e10 | agent | m14 | m8 | medium | inherited agent conj -> is |
| e11 | relation | m0 | m2 | high | with |
| e12 | relation | m8 | m9 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | child | child | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | hair | hair | object | body_part | m2 | raw_mention |  |  |  | True | {"canonical": "entity:hair", "parents": ["entity_parent:body_part"]} |
| ent_m4 | object | hat | hat | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:hat", "parents": []} |
| ent_m8 | object | child | child | person | person, human | m8 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m9 | object | window | window | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:window", "parents": []} |
| ent_m10 | context | background | background | object | scene_context | m10 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m11 | context | indoors | indoors | object | scene_context | m11 | raw_mention |  |  |  | True | {"canonical": "entity:indoors", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | smiles | smile | smile | expression_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:smile", "parents": ["action_parent:expression_action", "action_parent:visual_action"]} |  |
| ce1 | m13 | wearing | wear | wear | wearing_action, visual_action |  | agent:m0->ent_m0; patient:m4->ent_m4 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce2 | m14 | appears | appear | appear | visual_action |  | agent:m8->ent_m8 | {"canonical": "action:appear", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | smile | agent | m0 | ent_m0 | medium | e7 | nsubj -> smiles |  |  |
| ce1 | wear | agent | m0 | ent_m0 | medium | e8 | inherited agent advcl -> smiles |  |  |
| ce1 | wear | patient | m4 | ent_m4 | medium | e9 | dobj -> wearing |  |  |
| ce2 | appear | agent | m8 | ent_m8 | medium | e10 | inherited agent conj -> is |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e11 | False | False |  |  |
| cr1 | m8 | m9 | ent_m8 | ent_m9 | with | with | association_relation, visual_relation | high | e12 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf1 | entity_exists | hair |  |  | body_part | entity_exists:hair | True | high |
| cf2 | entity_exists | hat |  |  |  | entity_exists:hat | True | low |
| cf3 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf4 | entity_exists | window |  |  |  | entity_exists:window | True | low |
| cf5 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf6 | entity_exists | indoors |  |  | scene_context | entity_exists:indoors | True | high |
| cf7 | has_attribute | child | young |  | modifier_attribute, visual_attribute | has_attribute:child:young | True | medium |
| cf8 | has_attribute | hair | blonde |  | modifier_attribute, visual_attribute | has_attribute:hair:blonde | True | medium |
| cf9 | has_attribute | hat | blue |  | color_attribute, color, visual_attribute | has_attribute:hat:blue | True | high |
| cf10 | has_attribute | hat | white |  | color_attribute, color, visual_attribute | has_attribute:hat:white | True | high |
| cf11 | has_attribute | hat | striped |  | pattern_attribute, clean_exact_overlap, pattern, pattern_marking, texture, visual_attribute | has_attribute:hat:striped | True | medium |
| cf12 | action_event | smile |  |  | expression_action, visual_action | action_event:smile | True | high |
| cf13 | event_role | smile | agent | child |  | event_role:smile:agent:child | True | medium |
| cf14 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf15 | event_role | wear | agent | child |  | event_role:wear:agent:child | True | medium |
| cf16 | event_role | wear | patient | hat |  | event_role:wear:patient:hat | True | medium |
| cf17 | action_event | appear |  |  | visual_action | action_event:appear | True | low |
| cf18 | event_role | appear | agent | child |  | event_role:appear:agent:child | True | medium |
| cf19 | relation | child | with | hair | association_relation, visual_relation | relation:child:with:hair | True | high |
| cf20 | relation | child | with | window | association_relation, visual_relation | relation:child:with:window | True | high |

### Stage 9 Canonicalization Notes
_none_

## 10

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `068c9ac59345edb43cd2e03ceec8f57ee0c0fbf399ff97f5f348ac0e716b0014`
**parse_path:** `tag_list`

> roller skaters, helmet, referee, court, blue jersey

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | skaters | skater | segment_head | t0 | 1 | high |
| m1 | attribute | roller | roller | attribute | t0 | 0 | high |
| m2 | object | helmet | helmet | segment_head | t1 | 0 | high |
| m3 | object | referee | referee | segment_head | t2 | 0 | high |
| m4 | object | court | court | segment_head | t3 | 0 | high |
| m5 | object | jersey | jersey | segment_head | t4 | 1 | high |
| m6 | attribute | blue | blue | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> skaters |
| e1 | has_attribute | m5 | m6 | high | t4 internal compound -> jersey |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | skater | skaters | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:skater", "parents": []} |
| ent_m2 | object | helmet | helmet | clothing | protective_gear, clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:helmet", "parents": ["entity_parent:protective_gear", "entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | referee | referee | person | person, human | m3 | raw_mention |  |  |  | True | {"canonical": "entity:referee", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m4 | object | court | court | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:court", "parents": []} |
| ent_m5 | object | jersey | jersey | clothing | clothing, wearable | m5 | raw_mention |  |  |  | True | {"canonical": "entity:jersey", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |

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
| cf0 | entity_exists | skater |  |  |  | entity_exists:skater | True | low |
| cf1 | entity_exists | helmet |  |  | protective_gear, clothing, wearable | entity_exists:helmet | True | high |
| cf2 | entity_exists | referee |  |  | person, human | entity_exists:referee | True | high |
| cf3 | entity_exists | court |  |  |  | entity_exists:court | True | low |
| cf4 | entity_exists | jersey |  |  | clothing, wearable | entity_exists:jersey | True | high |
| cf5 | has_attribute | skater | roller |  | attribute, visual_attribute | has_attribute:skater:roller | True | high |
| cf6 | has_attribute | jersey | blue |  | color_attribute, color, visual_attribute | has_attribute:jersey:blue | True | high |

### Stage 9 Canonicalization Notes
_none_

## 11

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `08612f90283dcb7b3b1fa62f0512b84c577e5a2635a5e1e5346c33e0505ad414`
**parse_path:** `sentence`

> A large stone building with a gray roof and arched windows stands on a cobblestone street. A dark sedan is parked in front, and a bus is visible further down the road under a partly cloudy sky.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | noun_chunk_root | chunk0 | 3 | high |
| m1 | attribute | large | large | size_attribute | chunk0 | 1 | high |
| m2 | attribute | stone | stone | material_attribute | chunk0 | 2 | high |
| m3 | object | roof | roof | noun_chunk_root | chunk1 | 7 | high |
| m4 | attribute | gray | gray | color_attribute | chunk1 | 6 | high |
| m5 | object | windows | window | noun_chunk_root | chunk2 | 10 | high |
| m6 | attribute | arched | arched | visual_attribute | chunk2 | 9 | medium |
| m7 | object | street | street | noun_chunk_root | chunk3 | 15 | high |
| m8 | attribute | cobblestone | cobblestone | modifier_attribute | chunk3 | 14 | medium |
| m9 | object | sedan | sedan | noun_chunk_root | chunk4 | 19 | high |
| m10 | attribute | dark | dark | visual_attribute | chunk4 | 18 | medium |
| m11 | context | front | front | spatial_region | chunk5 | 23 | medium |
| m12 | object | bus | bus | noun_chunk_root | chunk6 | 27 | high |
| m13 | object | road | road | noun_chunk_root | chunk7 | 33 | high |
| m14 | object | sky | sky | noun_chunk_root | chunk8 | 38 | high |
| m15 | attribute | partly | partly | modifier_attribute | chunk8 | 36 | medium |
| m16 | attribute | cloudy | cloudy | modifier_attribute | chunk8 | 37 | medium |
| m17 | action | stands | stand | verb_predicate | doc | 11 | high |
| m18 | action | parked | park | verb_predicate | doc | 21 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> building |
| e1 | has_attribute | m0 | m2 | high | chunk0 compound -> building |
| e2 | has_attribute | m3 | m4 | high | chunk1 amod -> roof |
| e3 | has_attribute | m5 | m6 | medium | chunk2 amod -> windows |
| e4 | has_attribute | m7 | m8 | medium | chunk3 amod -> street |
| e5 | has_attribute | m9 | m10 | medium | chunk4 amod -> sedan |
| e6 | has_attribute | m14 | m15 | medium | chunk8 advmod -> sky |
| e7 | has_attribute | m14 | m16 | medium | chunk8 amod -> sky |
| e8 | agent | m17 | m0 | medium | nsubj -> stands |
| e9 | agent | m18 | m9 | medium | nsubjpass -> parked |
| e10 | relation | m0 | m3 | high | with |
| e11 | relation | m0 | m5 | high | with |
| e12 | relation | m0 | m7 | high | on |
| e13 | relation | m9 | m11 | high | in |
| e14 | relation | m12 | m13 | medium | down |
| e15 | relation | m12 | m14 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | building | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m3 | object | roof | roof | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:roof", "parents": []} |
| ent_m5 | object | window | windows | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:window", "parents": []} |
| ent_m7 | object | street | street | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:street", "parents": []} |
| ent_m9 | object | sedan | sedan | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:sedan", "parents": []} |
| ent_m11 | context | front | front | object | scene_context | m11 | raw_mention |  |  |  | True | {"canonical": "entity:front", "parents": ["entity_parent:scene_context"]} |
| ent_m12 | object | bus | bus | vehicle | vehicle | m12 | raw_mention |  |  |  | True | {"canonical": "entity:bus", "parents": ["entity_parent:vehicle"]} |
| ent_m13 | object | road | road | object |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:road", "parents": []} |
| ent_m14 | object | sky | sky | object |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | stands | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m18 | parked | park | park | visual_action |  | theme:m9->ent_m9 | {"canonical": "action:park", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e8 | nsubj -> stands |  |  |
| ce1 | park | theme | m9 | ent_m9 | medium | e9 | nsubjpass -> parked |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | with | with | association_relation, visual_relation | high | e10 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | with | with | association_relation, visual_relation | high | e11 | False | False |  |  |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | on | on | spatial_support, visual_relation | high | e12 | False | False |  |  |
| cr3 | m9 | m11 | ent_m9 | ent_m11 | in | in | spatial_containment, visual_relation | high | e13 | False | False |  |  |
| cr4 | m12 | m13 | ent_m12 | ent_m13 | down | down | visual_relation | medium | e14 | False | False |  |  |
| cr5 | m12 | m14 | ent_m12 | ent_m14 | under | under | spatial_vertical, visual_relation | high | e15 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf1 | entity_exists | roof |  |  |  | entity_exists:roof | True | low |
| cf2 | entity_exists | window |  |  |  | entity_exists:window | True | low |
| cf3 | entity_exists | street |  |  |  | entity_exists:street | True | low |
| cf4 | entity_exists | sedan |  |  |  | entity_exists:sedan | True | low |
| cf5 | entity_exists | front |  |  | scene_context | entity_exists:front | True | medium |
| cf6 | entity_exists | bus |  |  | vehicle | entity_exists:bus | True | high |
| cf7 | entity_exists | road |  |  |  | entity_exists:road | True | low |
| cf8 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf9 | has_attribute | building | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:building:large | True | high |
| cf10 | has_attribute | building | stone |  | material_attribute, material, visual_attribute | has_attribute:building:stone | True | high |
| cf11 | has_attribute | roof | gray |  | color_attribute, color, visual_attribute | has_attribute:roof:gray | True | high |
| cf12 | has_attribute | window | arched |  | visual_attribute | has_attribute:window:arched | True | medium |
| cf13 | has_attribute | street | cobblestone |  | material_attribute, material, visual_attribute | has_attribute:street:cobblestone | True | medium |
| cf14 | has_attribute | sedan | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:sedan:dark | True | medium |
| cf15 | has_attribute | sky | partly |  | modifier_attribute, visual_attribute | has_attribute:sky:partly | True | medium |
| cf16 | has_attribute | sky | cloudy |  | weather_attribute, weather, visual_attribute | has_attribute:sky:cloudy | True | medium |
| cf17 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf18 | event_role | stand | agent | building |  | event_role:stand:agent:building | True | medium |
| cf19 | action_event | park |  |  | visual_action | action_event:park | True | low |
| cf20 | event_role | park | theme | sedan |  | event_role:park:theme:sedan | True | medium |
| cf21 | relation | building | with | roof | association_relation, visual_relation | relation:building:with:roof | True | high |
| cf22 | relation | building | with | window | association_relation, visual_relation | relation:building:with:window | True | high |
| cf23 | relation | building | on | street | spatial_support, visual_relation | relation:building:on:street | True | high |
| cf24 | relation | sedan | in | front | spatial_containment, visual_relation | relation:sedan:in:front | True | high |
| cf25 | relation | bus | down | road | visual_relation | relation:bus:down:road | True | medium |
| cf26 | relation | bus | under | sky | spatial_vertical, visual_relation | relation:bus:under:sky | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m18 | e9 | m9 |  |  | {"action_mention_id": "m18", "kind": "passive_subject_to_theme", "raw_edge_id": "e9", "target": "m9"} |

## 12

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `0882bfa152ac30901673edf8d30aba5ce433439a9a71153fea1e970f9f0f4c14`
**parse_path:** `sentence`

> A man in a white shirt holds a basketball above his head on a gym court. Several people in pink and gray shirts play nearby.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | shirt | shirt | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | white | white | color_attribute | chunk1 | 4 | high |
| m3 | object | basketball | basketball | noun_chunk_root | chunk2 | 8 | high |
| m4 | object | head | head | noun_chunk_root | chunk3 | 11 | high |
| m5 | object | court | court | noun_chunk_root | chunk4 | 15 | high |
| m6 | attribute | gym | gym | compound_modifier | chunk4 | 14 | medium |
| m7 | object | people | people | noun_chunk_root | chunk5 | 18 | high |
| m8 | quantity | Several | several | approximate_quantity | chunk5 | 17 | medium |
| m9 | object | shirts | shirt | noun_chunk_root | chunk6 | 23 | high |
| m10 | attribute | pink | pink | color_attribute | chunk6 | 20 | high |
| m11 | attribute | gray | gray | color_attribute | chunk6 | 22 | high |
| m12 | action | holds | hold | verb_predicate | doc | 6 | high |
| m13 | action | play | play | verb_predicate | doc | 24 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> shirt |
| e1 | has_attribute | m5 | m6 | medium | chunk4 compound -> court |
| e2 | has_quantity | m7 | m8 | medium | chunk5 quantity -> people |
| e3 | has_attribute | m9 | m10 | high | chunk6 amod -> shirts |
| e4 | has_attribute | m9 | m11 | high | chunk6 conj -> shirts |
| e5 | agent | m12 | m0 | medium | nsubj -> holds |
| e6 | patient | m12 | m3 | medium | dobj -> holds |
| e7 | agent | m13 | m7 | medium | nsubj -> play |
| e8 | relation | m0 | m1 | high | in |
| e9 | relation | m0 | m4 | high | above |
| e10 | relation | m0 | m5 | high | on |
| e11 | relation | m7 | m9 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | shirt | shirt | clothing | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | basketball | basketball | object | ball, sports_equipment, artifact | m3 | raw_mention |  |  |  | True | {"canonical": "entity:basketball", "parents": ["entity_parent:ball", "entity_parent:sports_equipment", "entity_parent:artifact"]} |
| ent_m4 | object | head | head | object | body_part | m4 | raw_mention |  |  |  | True | {"canonical": "entity:head", "parents": ["entity_parent:body_part"]} |
| ent_m5 | object | court | court | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:court", "parents": []} |
| ent_m7 | object | people | people | person | person, human | m7 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m9 | object | shirt | shirts | clothing | clothing, wearable | m9 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | holds | hold | hold | manipulation_action, visual_action |  | agent:m0->ent_m0; patient:m3->ent_m3 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce1 | m13 | play | play | play | activity_action, visual_action |  | agent:m7->ent_m7 | {"canonical": "action:play", "parents": ["action_parent:activity_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | hold | agent | m0 | ent_m0 | medium | e5 | nsubj -> holds |  |  |
| ce0 | hold | patient | m3 | ent_m3 | medium | e6 | dobj -> holds |  |  |
| ce1 | play | agent | m7 | ent_m7 | medium | e7 | nsubj -> play |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | spatial_containment, visual_relation | high | e8 | False | False |  |  |
| cr1 | m0 | m4 | ent_m3 | ent_m4 | above | above | spatial_vertical, visual_relation | high | e9 | False | False | pp_source_disambiguation | patient_body_part_anchor |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | on | on | spatial_support, visual_relation | high | e10 | False | False |  |  |
| cr3 | m7 | m9 | ent_m7 | ent_m9 | in | in | spatial_containment, visual_relation | high | e11 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf2 | entity_exists | basketball |  |  | ball, sports_equipment, artifact | entity_exists:basketball | True | high |
| cf3 | entity_exists | head |  |  | body_part | entity_exists:head | True | high |
| cf4 | entity_exists | court |  |  |  | entity_exists:court | True | low |
| cf5 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf6 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf7 | has_attribute | shirt | white |  | color_attribute, color, visual_attribute | has_attribute:shirt:white | True | high |
| cf8 | has_attribute | court | gym |  | compound_modifier, visual_attribute | has_attribute:court:gym | True | medium |
| cf9 | has_quantity | people | several |  | approximate_quantity, quantity | has_quantity:people:several | True | medium |
| cf10 | has_attribute | shirt | pink |  | color_attribute, color, visual_attribute | has_attribute:shirt:pink | True | high |
| cf11 | has_attribute | shirt | gray |  | color_attribute, color, visual_attribute | has_attribute:shirt:gray | True | high |
| cf12 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf13 | event_role | hold | agent | man |  | event_role:hold:agent:man | True | medium |
| cf14 | event_role | hold | patient | basketball |  | event_role:hold:patient:basketball | True | medium |
| cf15 | action_event | play |  |  | activity_action, visual_action | action_event:play | True | high |
| cf16 | event_role | play | agent | people |  | event_role:play:agent:people | True | medium |
| cf17 | relation | man | in | shirt | spatial_containment, visual_relation | relation:man:in:shirt | True | high |
| cf18 | relation | basketball | above | head | spatial_vertical, visual_relation | relation:basketball:above:head | True | high |
| cf19 | relation | man | on | court | spatial_support, visual_relation | relation:man:on:court | True | high |
| cf20 | relation | people | in | shirt | spatial_containment, visual_relation | relation:people:in:shirt | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| pp_source_disambiguated | m12 | e9 |  | ent_m4 | patient_body_part_anchor | {"action_mention_id": "m12", "canonical_action": "hold", "canonical_source": "ent_m3", "canonical_target": "ent_m4", "confidence": "high", "kind": "pp_source_disambiguated", "previous_canonical_source": "ent_m0", "raw_edge_id": "e9", "raw_source": "m0", "raw_target": "m4", "reason": "patient_body_part_anchor", "relation": "above"} |

## 13

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `097c49356f8c365fc2a90e92a076d206bee7aa6abeea8fadad4ca092b9c5c414`
**parse_path:** `sentence`

> A desert landscape with mountains under a cloudy sky. A black object sits on the dry, rocky ground.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | landscape | landscape | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | desert | desert | compound_modifier | chunk0 | 1 | medium |
| m2 | object | mountains | mountain | noun_chunk_root | chunk1 | 4 | high |
| m3 | object | sky | sky | noun_chunk_root | chunk2 | 8 | high |
| m4 | attribute | cloudy | cloudy | modifier_attribute | chunk2 | 7 | medium |
| m5 | object | object | object | noun_chunk_root | chunk3 | 12 | high |
| m6 | attribute | black | black | color_attribute | chunk3 | 11 | high |
| m7 | object | ground | ground | noun_chunk_root | chunk4 | 19 | high |
| m8 | attribute | dry | dry | modifier_attribute | chunk4 | 16 | medium |
| m9 | attribute | rocky | rocky | modifier_attribute | chunk4 | 18 | medium |
| m10 | action | sits | sit | verb_predicate | doc | 13 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 compound -> landscape |
| e1 | has_attribute | m3 | m4 | medium | chunk2 amod -> sky |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> object |
| e3 | has_attribute | m7 | m8 | medium | chunk4 amod -> ground |
| e4 | has_attribute | m7 | m9 | medium | chunk4 amod -> ground |
| e5 | agent | m10 | m5 | medium | nsubj -> sits |
| e6 | relation | m0 | m2 | high | with |
| e7 | relation | m2 | m3 | high | under |
| e8 | relation | m5 | m7 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | landscape | landscape | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:landscape", "parents": []} |
| ent_m2 | object | mountain | mountains | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:mountain", "parents": []} |
| ent_m3 | object | sky | sky | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m5 | object | object | object | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:object", "parents": []} |
| ent_m7 | object | ground | ground | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:ground", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | sits | sit | sit | body_pose_action, visual_action |  | agent:m5->ent_m5 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m5 | ent_m5 | medium | e5 | nsubj -> sits |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | under | under | spatial_vertical, visual_relation | high | e7 | False | False |  |  |
| cr2 | m5 | m7 | ent_m5 | ent_m7 | on | on | spatial_support, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | landscape |  |  |  | entity_exists:landscape | True | low |
| cf1 | entity_exists | mountain |  |  |  | entity_exists:mountain | True | low |
| cf2 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf3 | entity_exists | object |  |  |  | entity_exists:object | True | low |
| cf4 | entity_exists | ground |  |  |  | entity_exists:ground | True | low |
| cf5 | has_attribute | landscape | desert |  | compound_modifier, visual_attribute | has_attribute:landscape:desert | True | medium |
| cf6 | has_attribute | sky | cloudy |  | weather_attribute, weather, visual_attribute | has_attribute:sky:cloudy | True | medium |
| cf7 | has_attribute | object | black |  | color_attribute, color, visual_attribute | has_attribute:object:black | True | high |
| cf8 | has_attribute | ground | dry |  | state_attribute, clean_exact_overlap, state, visual_attribute | has_attribute:ground:dry | True | medium |
| cf9 | has_attribute | ground | rocky |  | material_attribute, material, visual_attribute | has_attribute:ground:rocky | True | medium |
| cf10 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf11 | event_role | sit | agent | object |  | event_role:sit:agent:object | True | medium |
| cf12 | relation | landscape | with | mountain | association_relation, visual_relation | relation:landscape:with:mountain | True | high |
| cf13 | relation | mountain | under | sky | spatial_vertical, visual_relation | relation:mountain:under:sky | True | high |
| cf14 | relation | object | on | ground | spatial_support, visual_relation | relation:object:on:ground | True | high |

### Stage 9 Canonicalization Notes
_none_

## 14

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `0a404060dc0c39ea0ea98fdd78558ac2b78bfd5c7e8cce93647fda2de2964014`
**parse_path:** `tag_list`

> brown boot, indoor, brick wall, display, large

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | boot | boot | segment_head | t0 | 1 | high |
| m1 | attribute | brown | brown | attribute | t0 | 0 | high |
| m2 | context | indoor | indoor | scene_context | t1 | 0 | high |
| m3 | object | wall | wall | segment_head | t2 | 1 | high |
| m4 | attribute | brick | brick | attribute | t2 | 0 | high |
| m5 | object | display | display | segment_head | t3 | 0 | high |
| m6 | attribute | large | large | floating_attribute | t4 | 0 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> boot |
| e1 | has_context | scene | m2 | high | t1 context tag |
| e2 | has_attribute | m3 | m4 | high | t2 internal compound -> wall |
| e3 | candidate_has_attribute | m5 | m6 | low | t4 adjacent floating attribute |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | boot | boot | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:boot", "parents": []} |
| ent_m2 | context | indoor | indoor | object | scene_context | m2 | raw_mention |  |  |  | True | {"canonical": "entity:indoor", "parents": ["entity_parent:scene_context"]} |
| ent_m3 | object | wall | wall | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |
| ent_m5 | object | display | display | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:display", "parents": []} |

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
| cf0 | entity_exists | boot |  |  |  | entity_exists:boot | True | low |
| cf1 | entity_exists | indoor |  |  | scene_context | entity_exists:indoor | True | high |
| cf2 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf3 | entity_exists | display |  |  |  | entity_exists:display | True | low |
| cf4 | has_attribute | boot | brown |  | color_attribute, color, visual_attribute | has_attribute:boot:brown | True | high |
| cf5 | has_attribute | wall | brick |  | material_attribute, material, visual_attribute | has_attribute:wall:brick | True | high |
| cf6 | candidate_has_attribute | display | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | candidate_has_attribute:display:large | False | low |

### Stage 9 Canonicalization Notes
_none_

## 15

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `0a74bd648e7249dd4137548b30a087f07b1abb266189a2dd623d122f285af814`
**parse_path:** `sentence`

> Two men smile for the camera in a bathroom. One wears a vest and red scarf, the other a yellow shirt.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | men | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Two | two | exact_quantity | chunk0 | 0 | high |
| m2 | object | camera | camera | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | bathroom | bathroom | noun_chunk_root | chunk2 | 8 | high |
| m4 | object | vest | vest | noun_chunk_root | chunk3 | 13 | high |
| m5 | object | scarf | scarf | noun_chunk_root | chunk4 | 16 | high |
| m6 | attribute | red | red | color_attribute | chunk4 | 15 | high |
| m7 | reference | One | one | singular_substitute | nominal_reference | 10 | high |
| m8 | reference | other | other | contrastive_reference | nominal_reference | 19 | high |
| m9 | action | smile | smile | verb_predicate | doc | 2 | high |
| m10 | action | wears | wear | verb_predicate | doc | 11 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> men |
| e1 | has_attribute | m5 | m6 | high | chunk4 amod -> scarf |
| e2 | refers_to | m7 | m0 | high | singular_substitute One -> men; score=102 |
| e3 | refers_to | m8 | m0 | high | contrastive_reference other -> men; score=110; margin=21 |
| e4 | agent | m9 | m0 | medium | nsubj -> smile |
| e5 | agent | m10 | m0 | medium | nsubj -> wears; resolved One -> men |
| e6 | patient | m10 | m4 | medium | dobj -> wears |
| e7 | patient | m10 | m5 | medium | dobj -> wears |
| e8 | relation | m0 | m2 | medium | for |
| e9 | relation | m0 | m3 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | men | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | camera | camera | device | device, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:camera", "parents": ["entity_parent:device", "entity_parent:artifact"]} |
| ent_m3 | object | bathroom | bathroom | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:bathroom", "parents": []} |
| ent_m4 | object | vest | vest | clothing | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:vest", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m5 | object | scarf | scarf | clothing | clothing, wearable | m5 | raw_mention |  |  |  | True | {"canonical": "entity:scarf", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| eref_m7 | instance | man | One | person | person, human | m7 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| eref_m8 | contrastive_instance | man | other | person | person, human | m8 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m7 | eref_m7 | m0 | ent_m0 | high |  |
| refers_to | m8 | eref_m8 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | smile | smile | smile | expression_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:smile", "parents": ["action_parent:expression_action", "action_parent:visual_action"]} |  |
| ce1 | m10 | wears | wear | wear | wearing_action, visual_action |  | agent:m0->eref_m7; patient:m4->ent_m4; patient:m5->ent_m5 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | smile | agent | m0 | ent_m0 | medium | e4 | nsubj -> smile |  |  |
| ce1 | wear | agent | m0 | eref_m7 | medium | e5 | nsubj -> wears; resolved One -> men |  |  |
| ce1 | wear | patient | m4 | ent_m4 | medium | e6 | dobj -> wears |  |  |
| ce1 | wear | patient | m5 | ent_m5 | medium | e7 | dobj -> wears |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | for | for | visual_relation | medium | e8 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | in | in | spatial_containment, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | camera |  |  | device, artifact | entity_exists:camera | True | high |
| cf2 | entity_exists | bathroom |  |  |  | entity_exists:bathroom | True | low |
| cf3 | entity_exists | vest |  |  | clothing, wearable | entity_exists:vest | True | high |
| cf4 | entity_exists | scarf |  |  | clothing, wearable | entity_exists:scarf | True | high |
| cf5 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf6 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf7 | has_quantity | man | two |  | exact_quantity, quantity | has_quantity:man:two | True | high |
| cf8 | has_attribute | scarf | red |  | color_attribute, color, visual_attribute | has_attribute:scarf:red | True | high |
| cf9 | action_event | smile |  |  | expression_action, visual_action | action_event:smile | True | high |
| cf10 | event_role | smile | agent | man |  | event_role:smile:agent:man | True | medium |
| cf11 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf12 | event_role | wear | agent | man |  | event_role:wear:agent:man | True | medium |
| cf13 | event_role | wear | patient | vest |  | event_role:wear:patient:vest | True | medium |
| cf14 | event_role | wear | patient | scarf |  | event_role:wear:patient:scarf | True | medium |
| cf15 | relation | man | for | camera | visual_relation | relation:man:for:camera | True | medium |
| cf16 | relation | man | in | bathroom | spatial_containment, visual_relation | relation:man:in:bathroom | True | high |

### Stage 9 Canonicalization Notes
_none_

## 16

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `0b51847b650bf2311e48557b7b3619abd6c1246de89f64a33bb833c172fe4014`
**parse_path:** `sentence`

> Children in white dresses and shirts sit on chairs during a performance. One child holds a violin, while others are seated with music stands nearby. The setting is indoors, with red curtains and blue chairs visible in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | Children | child | noun_chunk_root | chunk0 | 0 | high |
| m1 | object | dresses | dress | noun_chunk_root | chunk1 | 3 | high |
| m2 | attribute | white | white | color_attribute | chunk1 | 2 | high |
| m3 | object | shirts | shirt | noun_chunk_root | chunk2 | 5 | high |
| m4 | object | chairs | chair | noun_chunk_root | chunk3 | 8 | high |
| m5 | object | performance | performance | noun_chunk_root | chunk4 | 11 | high |
| m6 | object | child | child | noun_chunk_root | chunk5 | 14 | high |
| m7 | quantity | One | one | exact_quantity | chunk5 | 13 | high |
| m8 | object | violin | violin | noun_chunk_root | chunk6 | 17 | high |
| m9 | object | music stands | music_stand | noun_chunk_root | chunk8 | 24 | high |
| m10 | context | setting | setting | scene_context | chunk9 | 28 | high |
| m11 | object | curtains | curtain | noun_chunk_root | chunk10 | 34 | high |
| m12 | attribute | red | red | color_attribute | chunk10 | 33 | high |
| m13 | object | chairs | chair | noun_chunk_root | chunk11 | 37 | high |
| m14 | attribute | blue | blue | color_attribute | chunk11 | 36 | high |
| m15 | context | background | background | scene_context | chunk12 | 41 | high |
| m16 | context | indoors | indoors | scene_context | doc | 30 | high |
| m17 | action | sit | sit | verb_predicate | doc | 6 | high |
| m18 | action | holds | hold | verb_predicate | doc | 15 | high |
| m19 | action | seated | seat | verb_predicate | doc | 22 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> dresses |
| e1 | has_quantity | m6 | m7 | high | chunk5 quantity -> child |
| e2 | has_context | scene | m10 | high | scene_context token setting |
| e3 | has_attribute | m11 | m12 | high | chunk10 amod -> curtains |
| e4 | has_attribute | m13 | m14 | high | chunk11 amod -> chairs |
| e5 | has_context | scene | m15 | high | scene_context token background |
| e6 | has_context | scene | m16 | high | scene_context token indoors |
| e7 | agent | m17 | m0 | medium | nsubj -> sit |
| e8 | agent | m18 | m6 | medium | nsubj -> holds |
| e9 | patient | m18 | m8 | medium | dobj -> holds |
| e10 | agent | m19 | m6 | medium | inherited agent advcl -> holds |
| e11 | relation | m0 | m1 | high | in |
| e12 | relation | m0 | m3 | high | in |
| e13 | relation | m0 | m4 | high | on |
| e14 | relation | m0 | m5 | medium | during |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | child | Children | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | dress | dresses | clothing | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:dress", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | shirt | shirts | clothing | clothing, wearable | m3 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m4 | object | chair | chairs | object | furniture, artifact | m4 | raw_mention |  |  |  | True | {"canonical": "entity:chair", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m5 | object | performance | performance | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:performance", "parents": []} |
| ent_m6 | object | child | child | person | person, human | m6 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m8 | object | violin | violin | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:violin", "parents": []} |
| ent_m9 | object | music_stand | music stands | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:music_stand", "parents": []} |
| ent_m10 | context | setting | setting | object | scene_context | m10 | raw_mention |  |  |  | True | {"canonical": "entity:setting", "parents": ["entity_parent:scene_context"]} |
| ent_m11 | object | curtain | curtains | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:curtain", "parents": []} |
| ent_m13 | object | chair | chairs | object | furniture, artifact | m13 | raw_mention |  |  |  | True | {"canonical": "entity:chair", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m15 | context | background | background | object | scene_context | m15 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m16 | context | indoors | indoors | object | scene_context | m16 | raw_mention |  |  |  | True | {"canonical": "entity:indoors", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | sit | sit | sit | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m18 | holds | hold | hold | manipulation_action, visual_action |  | agent:m6->ent_m6; patient:m8->ent_m8 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce2 | m19 | seated | seat | sit | body_pose_action, visual_action |  | agent:m6->ent_m6 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m0 | ent_m0 | medium | e7 | nsubj -> sit |  |  |
| ce1 | hold | agent | m6 | ent_m6 | medium | e8 | nsubj -> holds |  |  |
| ce1 | hold | patient | m8 | ent_m8 | medium | e9 | dobj -> holds |  |  |
| ce2 | sit | agent | m6 | ent_m6 | medium | e10 | inherited agent advcl -> holds |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | spatial_containment, visual_relation | high | e11 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | in | in | spatial_containment, visual_relation | high | e12 | False | False |  |  |
| cr2 | m0 | m4 | ent_m0 | ent_m4 | on | on | spatial_support, visual_relation | high | e13 | False | False |  |  |
| cr3 | m0 | m5 | ent_m0 | ent_m5 | during | during | visual_relation | medium | e14 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf1 | entity_exists | dress |  |  | clothing, wearable | entity_exists:dress | True | high |
| cf2 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf3 | entity_exists | chair |  |  | furniture, artifact | entity_exists:chair | True | high |
| cf4 | entity_exists | performance |  |  |  | entity_exists:performance | True | low |
| cf5 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf6 | entity_exists | violin |  |  |  | entity_exists:violin | True | low |
| cf7 | entity_exists | music_stand |  |  |  | entity_exists:music_stand | True | low |
| cf8 | entity_exists | setting |  |  | scene_context | entity_exists:setting | True | high |
| cf9 | entity_exists | curtain |  |  |  | entity_exists:curtain | True | low |
| cf10 | entity_exists | chair |  |  | furniture, artifact | entity_exists:chair | True | high |
| cf11 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf12 | entity_exists | indoors |  |  | scene_context | entity_exists:indoors | True | high |
| cf13 | has_attribute | dress | white |  | color_attribute, color, visual_attribute | has_attribute:dress:white | True | high |
| cf14 | has_quantity | child | one |  | exact_quantity, quantity | has_quantity:child:one | True | high |
| cf15 | has_attribute | curtain | red |  | color_attribute, color, visual_attribute | has_attribute:curtain:red | True | high |
| cf16 | has_attribute | chair | blue |  | color_attribute, color, visual_attribute | has_attribute:chair:blue | True | high |
| cf17 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf18 | event_role | sit | agent | child |  | event_role:sit:agent:child | True | medium |
| cf19 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf20 | event_role | hold | agent | child |  | event_role:hold:agent:child | True | medium |
| cf21 | event_role | hold | patient | violin |  | event_role:hold:patient:violin | True | medium |
| cf22 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf23 | event_role | sit | agent | child |  | event_role:sit:agent:child | True | medium |
| cf24 | relation | child | in | dress | spatial_containment, visual_relation | relation:child:in:dress | True | high |
| cf25 | relation | child | in | shirt | spatial_containment, visual_relation | relation:child:in:shirt | True | high |
| cf26 | relation | child | on | chair | spatial_support, visual_relation | relation:child:on:chair | True | high |
| cf27 | relation | child | during | performance | visual_relation | relation:child:during:performance | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| action_lexical_canonicalized | m19 |  |  |  |  | {"action_mention_id": "m19", "canonical": "sit", "kind": "action_lexical_canonicalized", "raw_canonical_action": "seat", "source": "stage9_seed"} |

## 17

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `0bb595b117e1184dd61d50f4c00209733e3beeb7d2cce3851c9878f87971fc14`
**parse_path:** `tag_list`

> glass wall, worker, sidewalk, building, reflection, grass

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | wall | wall | segment_head | t0 | 1 | high |
| m1 | attribute | glass | glass | attribute | t0 | 0 | high |
| m2 | object | worker | worker | segment_head | t1 | 0 | high |
| m3 | object | sidewalk | sidewalk | segment_head | t2 | 0 | high |
| m4 | object | building | building | segment_head | t3 | 0 | high |
| m5 | object | reflection | reflection | segment_head | t4 | 0 | high |
| m6 | object | grass | grass | segment_head | t5 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> wall |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | wall | wall | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |
| ent_m2 | object | worker | worker | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:worker", "parents": []} |
| ent_m3 | object | sidewalk | sidewalk | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:sidewalk", "parents": []} |
| ent_m4 | object | building | building | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m5 | object | reflection | reflection | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:reflection", "parents": []} |
| ent_m6 | object | grass | grass | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": []} |

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
| cf0 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf1 | entity_exists | worker |  |  |  | entity_exists:worker | True | low |
| cf2 | entity_exists | sidewalk |  |  |  | entity_exists:sidewalk | True | low |
| cf3 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf4 | entity_exists | reflection |  |  |  | entity_exists:reflection | True | low |
| cf5 | entity_exists | grass |  |  |  | entity_exists:grass | True | low |
| cf6 | has_attribute | wall | glass |  | material_attribute, material, visual_attribute | has_attribute:wall:glass | True | high |

### Stage 9 Canonicalization Notes
_none_

## 18

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `0c7588f2c805503462f15a197d85e1aa77344f20e2a1a6231d2f8726d4f1e414`
**parse_path:** `sentence`

> A cityscape viewed from between two tall buildings at dusk. Below, streets and vehicles stretch toward a waterfront with lit-up skyscrapers in the distance. The sky shows soft orange and gray hues near the horizon.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | cityscape | cityscape | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | buildings | building | noun_chunk_root | chunk1 | 7 | high |
| m2 | quantity | two | two | exact_quantity | chunk1 | 5 | high |
| m3 | attribute | tall | tall | size_attribute | chunk1 | 6 | high |
| m4 | context | dusk | dusk | scene_context | chunk2 | 9 | high |
| m5 | object | streets | street | noun_chunk_root | chunk3 | 13 | high |
| m6 | object | vehicles | vehicle | noun_chunk_root | chunk4 | 15 | high |
| m7 | object | waterfront | waterfront | noun_chunk_root | chunk5 | 19 | high |
| m8 | object | skyscrapers | skyscraper | noun_chunk_root | chunk6 | 22 | high |
| m9 | attribute | lit-up | lit-up | state_attribute | chunk6 | 21 | medium |
| m10 | context | distance | distance | scene_context | chunk7 | 25 | high |
| m11 | object | sky | sky | noun_chunk_root | chunk8 | 28 | high |
| m12 | object | hues | hue | noun_chunk_root | chunk9 | 34 | high |
| m13 | attribute | soft | soft | modifier_attribute | chunk9 | 30 | medium |
| m14 | attribute | orange | orange | color_attribute | chunk9 | 31 | high |
| m15 | attribute | gray | gray | color_attribute | chunk9 | 33 | high |
| m16 | object | horizon | horizon | noun_chunk_root | chunk10 | 37 | high |
| m17 | action | viewed | view | verb_predicate | doc | 2 | high |
| m18 | action | stretch | stretch | verb_predicate | doc | 16 | high |
| m19 | action | shows | show | verb_predicate | doc | 29 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m1 | m2 | high | chunk1 quantity -> buildings |
| e1 | has_attribute | m1 | m3 | high | chunk1 amod -> buildings |
| e2 | has_context | scene | m4 | high | scene_context token dusk |
| e3 | has_attribute | m8 | m9 | medium | chunk6 amod -> skyscrapers |
| e4 | has_context | scene | m10 | high | scene_context token distance |
| e5 | has_attribute | m12 | m13 | medium | chunk9 amod -> hues |
| e6 | has_attribute | m12 | m14 | high | chunk9 nmod -> hues |
| e7 | has_attribute | m12 | m15 | high | chunk9 conj -> hues |
| e8 | agent | m17 | m0 | medium | inherited agent acl -> cityscape |
| e9 | agent | m18 | m5 | medium | nsubj -> stretch |
| e10 | agent | m18 | m6 | medium | nsubj -> stretch |
| e11 | agent | m19 | m11 | medium | nsubj -> shows |
| e12 | patient | m19 | m12 | medium | dobj -> shows |
| e13 | relation | m0 | m4 | medium | at |
| e14 | relation | m5 | m7 | medium | toward |
| e15 | relation | m7 | m8 | high | with |
| e16 | relation | m8 | m10 | high | in |
| e17 | relation | m11 | m16 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | cityscape | cityscape | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:cityscape", "parents": []} |
| ent_m1 | object | building | buildings | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m4 | context | dusk | dusk | object | scene_context, time_context | m4 | raw_mention |  |  |  | True | {"canonical": "entity:dusk", "parents": ["entity_parent:scene_context", "entity_parent:time_context"]} |
| ent_m5 | object | street | streets | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:street", "parents": []} |
| ent_m6 | object | vehicle | vehicles | vehicle | vehicle | m6 | raw_mention |  |  |  | True | {"canonical": "entity:vehicle", "parents": ["entity_parent:vehicle"]} |
| ent_m7 | object | waterfront | waterfront | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:waterfront", "parents": []} |
| ent_m8 | object | skyscraper | skyscrapers | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:skyscraper", "parents": []} |
| ent_m10 | context | distance | distance | object | scene_context, spatial_context | m10 | raw_mention |  |  |  | True | {"canonical": "entity:distance", "parents": ["entity_parent:scene_context", "entity_parent:spatial_context"]} |
| ent_m11 | object | sky | sky | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m12 | object | hue | hues | object |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:hue", "parents": []} |
| ent_m16 | object | horizon | horizon | object |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:horizon", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | viewed | view | view | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:view", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m18 | stretch | stretch | stretch | visual_action |  | agent:m5->ent_m5; agent:m6->ent_m6 | {"canonical": "action:stretch", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m19 | shows | show | show | visual_action |  | agent:m11->ent_m11; patient:m12->ent_m12 | {"canonical": "action:show", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | view | agent | m0 | ent_m0 | medium | e8 | inherited agent acl -> cityscape |  |  |
| ce1 | stretch | agent | m5 | ent_m5 | medium | e9 | nsubj -> stretch |  |  |
| ce1 | stretch | agent | m6 | ent_m6 | medium | e10 | nsubj -> stretch |  |  |
| ce2 | show | agent | m11 | ent_m11 | medium | e11 | nsubj -> shows |  |  |
| ce2 | show | patient | m12 | ent_m12 | medium | e12 | dobj -> shows |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | at | at | spatial_location, visual_relation | medium | e13 | False | False |  |  |
| cr1 | m5 | m7 | ent_m5 | ent_m7 | toward | toward | visual_relation | medium | e14 | False | False |  |  |
| cr2 | m7 | m8 | ent_m7 | ent_m8 | with | with | association_relation, visual_relation | high | e15 | False | False |  |  |
| cr3 | m8 | m10 | ent_m8 | ent_m10 | in | in | spatial_containment, visual_relation | high | e16 | False | False |  |  |
| cr4 | m11 | m16 | ent_m11 | ent_m16 | near | near | spatial_proximity, visual_relation | high | e17 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | cityscape |  |  |  | entity_exists:cityscape | True | low |
| cf1 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf2 | entity_exists | dusk |  |  | scene_context, time_context | entity_exists:dusk | True | high |
| cf3 | entity_exists | street |  |  |  | entity_exists:street | True | low |
| cf4 | entity_exists | vehicle |  |  | vehicle | entity_exists:vehicle | True | high |
| cf5 | entity_exists | waterfront |  |  |  | entity_exists:waterfront | True | low |
| cf6 | entity_exists | skyscraper |  |  |  | entity_exists:skyscraper | True | low |
| cf7 | entity_exists | distance |  |  | scene_context, spatial_context | entity_exists:distance | True | high |
| cf8 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf9 | entity_exists | hue |  |  |  | entity_exists:hue | True | low |
| cf10 | entity_exists | horizon |  |  |  | entity_exists:horizon | True | low |
| cf11 | has_quantity | building | two |  | exact_quantity, quantity | has_quantity:building:two | True | high |
| cf12 | has_attribute | building | tall |  | size_attribute, height, visual_attribute | has_attribute:building:tall | True | high |
| cf13 | has_attribute | skyscraper | lit-up |  | state_attribute, visual_attribute | has_attribute:skyscraper:lit-up | True | medium |
| cf14 | has_attribute | hue | soft |  | texture_attribute, clean_exact_overlap, hardness, texture, visual_attribute | has_attribute:hue:soft | True | medium |
| cf15 | has_attribute | hue | orange |  | color_attribute, color, visual_attribute | has_attribute:hue:orange | True | high |
| cf16 | has_attribute | hue | gray |  | color_attribute, color, visual_attribute | has_attribute:hue:gray | True | high |
| cf17 | action_event | view |  |  | visual_action | action_event:view | True | low |
| cf18 | event_role | view | agent | cityscape |  | event_role:view:agent:cityscape | True | medium |
| cf19 | action_event | stretch |  |  | visual_action | action_event:stretch | True | low |
| cf20 | event_role | stretch | agent | street |  | event_role:stretch:agent:street | True | medium |
| cf21 | event_role | stretch | agent | vehicle |  | event_role:stretch:agent:vehicle | True | medium |
| cf22 | action_event | show |  |  | visual_action | action_event:show | True | low |
| cf23 | event_role | show | agent | sky |  | event_role:show:agent:sky | True | medium |
| cf24 | event_role | show | patient | hue |  | event_role:show:patient:hue | True | medium |
| cf25 | relation | cityscape | at | dusk | spatial_location, visual_relation | relation:cityscape:at:dusk | True | medium |
| cf26 | relation | street | toward | waterfront | visual_relation | relation:street:toward:waterfront | True | medium |
| cf27 | relation | waterfront | with | skyscraper | association_relation, visual_relation | relation:waterfront:with:skyscraper | True | high |
| cf28 | relation | skyscraper | in | distance | spatial_containment, visual_relation | relation:skyscraper:in:distance | True | high |
| cf29 | relation | sky | near | horizon | spatial_proximity, visual_relation | relation:sky:near:horizon | True | high |

### Stage 9 Canonicalization Notes
_none_

## 19

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `0e1b08528f25adc13662435f45a0bd1f5e90270018e6ae5fb0a30d822a589c14`
**parse_path:** `sentence`

> A paved road with a yellow line runs along the bottom of the frame. Beyond it, a vast green field stretches to the horizon under a clear blue sky. A few distant trees and power lines are visible in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | road | road | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | paved | paved | visual_attribute | chunk0 | 1 | medium |
| m2 | object | line | line | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | yellow | yellow | color_attribute | chunk1 | 5 | high |
| m4 | object | frame | frame | noun_chunk_root | chunk3 | 13 | high |
| m5 | object | field | field | noun_chunk_root | chunk5 | 21 | high |
| m6 | attribute | vast | vast | modifier_attribute | chunk5 | 19 | medium |
| m7 | attribute | green | green | color_attribute | chunk5 | 20 | high |
| m8 | object | horizon | horizon | noun_chunk_root | chunk6 | 25 | high |
| m9 | object | sky | sky | noun_chunk_root | chunk7 | 30 | high |
| m10 | attribute | clear | clear | visual_attribute | chunk7 | 28 | medium |
| m11 | attribute | blue | blue | color_attribute | chunk7 | 29 | high |
| m12 | object | trees | tree | noun_chunk_root | chunk8 | 35 | high |
| m13 | quantity | few | few | approximate_quantity | chunk8 | 33 | medium |
| m14 | attribute | distant | distant | modifier_attribute | chunk8 | 34 | medium |
| m15 | object | power lines | power_line | noun_chunk_root | chunk9 | 37 | high |
| m16 | context | background | background | scene_context | chunk10 | 42 | high |
| m17 | action | runs | run | verb_predicate | doc | 7 | high |
| m18 | action | stretches | stretch | verb_predicate | doc | 22 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> road |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> line |
| e2 | has_attribute | m5 | m6 | medium | chunk5 amod -> field |
| e3 | has_attribute | m5 | m7 | high | chunk5 amod -> field |
| e4 | has_attribute | m9 | m10 | medium | chunk7 amod -> sky |
| e5 | has_attribute | m9 | m11 | high | chunk7 amod -> sky |
| e6 | has_quantity | m12 | m13 | medium | chunk8 quantity -> trees |
| e7 | has_attribute | m12 | m14 | medium | chunk8 amod -> trees |
| e8 | has_context | scene | m16 | high | scene_context token background |
| e9 | agent | m17 | m0 | medium | nsubj -> runs |
| e10 | agent | m18 | m5 | medium | nsubj -> stretches |
| e11 | relation | m0 | m2 | high | with |
| e12 | relation | m0 | m4 | medium | bottom_of |
| e13 | relation | m5 | m0 | high | beyond |
| e14 | relation | m5 | m8 | medium | to |
| e15 | relation | m5 | m9 | high | under |
| e16 | relation | m12 | m16 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | road | road | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:road", "parents": []} |
| ent_m2 | object | line | line | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:line", "parents": []} |
| ent_m4 | object | frame | frame | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:frame", "parents": []} |
| ent_m5 | object | field | field | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |
| ent_m8 | object | horizon | horizon | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:horizon", "parents": []} |
| ent_m9 | object | sky | sky | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m12 | object | tree | trees | object |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m15 | object | power_line | power lines | object |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:power_line", "parents": []} |
| ent_m16 | context | background | background | object | scene_context | m16 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | runs | run | run | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:run", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m18 | stretches | stretch | stretch | visual_action |  | agent:m5->ent_m5 | {"canonical": "action:stretch", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | run | agent | m0 | ent_m0 | medium | e9 | nsubj -> runs |  |  |
| ce1 | stretch | agent | m5 | ent_m5 | medium | e10 | nsubj -> stretches |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e11 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | bottom_of | bottom_of | spatial_region, visual_relation | medium | e12 | False | False |  |  |
| cr2 | m5 | m0 | ent_m5 | ent_m0 | beyond | beyond | visual_relation | high | e13 | False | False |  |  |
| cr3 | m5 | m8 | ent_m5 | ent_m8 | to | to | visual_relation | medium | e14 | False | False |  |  |
| cr4 | m5 | m9 | ent_m5 | ent_m9 | under | under | spatial_vertical, visual_relation | high | e15 | False | False |  |  |
| cr5 | m12 | m16 | ent_m12 | ent_m16 | in | in | spatial_containment, visual_relation | high | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | road |  |  |  | entity_exists:road | True | low |
| cf1 | entity_exists | line |  |  |  | entity_exists:line | True | low |
| cf2 | entity_exists | frame |  |  |  | entity_exists:frame | True | low |
| cf3 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf4 | entity_exists | horizon |  |  |  | entity_exists:horizon | True | low |
| cf5 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf6 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf7 | entity_exists | power_line |  |  |  | entity_exists:power_line | True | low |
| cf8 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf9 | has_attribute | road | paved |  | visual_attribute | has_attribute:road:paved | True | medium |
| cf10 | has_attribute | line | yellow |  | color_attribute, color, visual_attribute | has_attribute:line:yellow | True | high |
| cf11 | has_attribute | field | vast |  | modifier_attribute, visual_attribute | has_attribute:field:vast | True | medium |
| cf12 | has_attribute | field | green |  | color_attribute, color, visual_attribute | has_attribute:field:green | True | high |
| cf13 | has_attribute | sky | clear |  | weather_attribute, opaqeness, weather, visual_attribute | has_attribute:sky:clear | True | medium |
| cf14 | has_attribute | sky | blue |  | color_attribute, color, visual_attribute | has_attribute:sky:blue | True | high |
| cf15 | has_quantity | tree | few |  | approximate_quantity, quantity | has_quantity:tree:few | True | medium |
| cf16 | has_attribute | tree | distant |  | modifier_attribute, visual_attribute | has_attribute:tree:distant | True | medium |
| cf17 | action_event | run |  |  | locomotion_action, visual_action | action_event:run | True | high |
| cf18 | event_role | run | agent | road |  | event_role:run:agent:road | True | medium |
| cf19 | action_event | stretch |  |  | visual_action | action_event:stretch | True | low |
| cf20 | event_role | stretch | agent | field |  | event_role:stretch:agent:field | True | medium |
| cf21 | relation | road | with | line | association_relation, visual_relation | relation:road:with:line | True | high |
| cf22 | relation | road | bottom_of | frame | spatial_region, visual_relation | relation:road:bottom_of:frame | True | medium |
| cf23 | relation | field | beyond | road | visual_relation | relation:field:beyond:road | True | high |
| cf24 | relation | field | to | horizon | visual_relation | relation:field:to:horizon | True | medium |
| cf25 | relation | field | under | sky | spatial_vertical, visual_relation | relation:field:under:sky | True | high |
| cf26 | relation | tree | in | background | spatial_containment, visual_relation | relation:tree:in:background | True | high |

### Stage 9 Canonicalization Notes
_none_

## 20

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `0e1b59c09008af99453425a727c0feab2c5e69433138763b5813eb069b64a814`
**parse_path:** `sentence`

> A teacher and six students in white shirts stand together on a colorful classroom rug.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | teacher | teacher | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | students | student | noun_chunk_root | chunk1 | 4 | high |
| m2 | quantity | six | six | exact_quantity | chunk1 | 3 | high |
| m3 | object | shirts | shirt | noun_chunk_root | chunk2 | 7 | high |
| m4 | attribute | white | white | color_attribute | chunk2 | 6 | high |
| m5 | object | rug | rug | noun_chunk_root | chunk3 | 14 | high |
| m6 | attribute | colorful | colorful | modifier_attribute | chunk3 | 12 | medium |
| m7 | attribute | classroom | classroom | compound_modifier | chunk3 | 13 | medium |
| m8 | action | stand | stand | verb_predicate | doc | 8 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m1 | m2 | high | chunk1 quantity -> students |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> shirts |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> rug |
| e3 | has_attribute | m5 | m7 | medium | chunk3 compound -> rug |
| e4 | agent | m8 | m0 | medium | nsubj -> stand |
| e5 | agent | m8 | m1 | medium | nsubj -> stand |
| e6 | relation | m1 | m3 | high | in |
| e7 | relation | m0 | m5 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | teacher | teacher | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:teacher", "parents": []} |
| ent_m1 | object | student | students | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:student", "parents": []} |
| ent_m3 | object | shirt | shirts | clothing | clothing, wearable | m3 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m5 | object | rug | rug | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:rug", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | stand | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0; agent:m1->ent_m1 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e4 | nsubj -> stand |  |  |
| ce0 | stand | agent | m1 | ent_m1 | medium | e5 | nsubj -> stand |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m3 | ent_m1 | ent_m3 | in | in | spatial_containment, visual_relation | high | e6 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | on | spatial_support, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | teacher |  |  |  | entity_exists:teacher | True | low |
| cf1 | entity_exists | student |  |  |  | entity_exists:student | True | low |
| cf2 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf3 | entity_exists | rug |  |  |  | entity_exists:rug | True | low |
| cf4 | has_quantity | student | six |  | exact_quantity, quantity | has_quantity:student:six | True | high |
| cf5 | has_attribute | shirt | white |  | color_attribute, color, visual_attribute | has_attribute:shirt:white | True | high |
| cf6 | has_attribute | rug | colorful |  | color_attribute, color_quantity, visual_attribute | has_attribute:rug:colorful | True | medium |
| cf7 | has_attribute | rug | classroom |  | compound_modifier, visual_attribute | has_attribute:rug:classroom | True | medium |
| cf8 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf9 | event_role | stand | agent | teacher |  | event_role:stand:agent:teacher | True | medium |
| cf10 | event_role | stand | agent | student |  | event_role:stand:agent:student | True | medium |
| cf11 | relation | student | in | shirt | spatial_containment, visual_relation | relation:student:in:shirt | True | high |
| cf12 | relation | teacher | on | rug | spatial_support, visual_relation | relation:teacher:on:rug | True | high |

### Stage 9 Canonicalization Notes
_none_

## 21

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `0e2296e144a650da6a374a53a16be972deaa045439c5c44eb5e0be47913ad414`
**parse_path:** `sentence`

> Three people are in close proximity indoors, with a man on the left, a woman in the center, and another woman on the right. The woman in the center has dark hair and is touching her lips with her finger, while the woman on the right smiles broadly. A green-lit sign is visible in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Three | three | exact_quantity | chunk0 | 0 | high |
| m2 | object | proximity | proximity | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | close | close | modifier_attribute | chunk1 | 4 | medium |
| m4 | object | man | man | noun_chunk_root | chunk2 | 10 | high |
| m5 | context | left | left | spatial_region | chunk3 | 13 | medium |
| m6 | object | woman | woman | noun_chunk_root | chunk4 | 16 | high |
| m7 | context | center | center | spatial_region | chunk5 | 19 | medium |
| m8 | object | woman | woman | noun_chunk_root | chunk6 | 23 | high |
| m9 | context | right | right | spatial_region | chunk7 | 26 | medium |
| m10 | object | woman | woman | noun_chunk_root | chunk8 | 29 | high |
| m11 | context | center | center | spatial_region | chunk9 | 32 | medium |
| m12 | object | hair | hair | noun_chunk_root | chunk10 | 35 | high |
| m13 | attribute | dark | dark | visual_attribute | chunk10 | 34 | medium |
| m14 | object | lips | lip | noun_chunk_root | chunk11 | 40 | high |
| m15 | object | finger | finger | noun_chunk_root | chunk12 | 43 | high |
| m16 | object | woman | woman | noun_chunk_root | chunk13 | 47 | high |
| m17 | context | right | right | spatial_region | chunk14 | 50 | medium |
| m18 | object | sign | sign | noun_chunk_root | chunk15 | 56 | high |
| m19 | attribute | green-lit | green-lit | modifier_attribute | chunk15 | 55 | medium |
| m20 | context | background | background | scene_context | chunk16 | 61 | high |
| m21 | context | indoors | indoors | scene_context | doc | 6 | high |
| m22 | action | has | have | verb_predicate | doc | 33 | high |
| m23 | action | touching | touch | verb_predicate | doc | 38 | high |
| m24 | action | smiles | smile | verb_predicate | doc | 51 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> people |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> proximity |
| e2 | has_attribute | m12 | m13 | medium | chunk10 amod -> hair |
| e3 | has_attribute | m18 | m19 | medium | chunk15 amod -> sign |
| e4 | has_context | scene | m20 | high | scene_context token background |
| e5 | has_context | scene | m21 | high | scene_context token indoors |
| e6 | agent | m22 | m10 | medium | nsubj -> has |
| e7 | patient | m22 | m12 | medium | dobj -> has |
| e8 | agent | m23 | m10 | medium | inherited agent conj -> has |
| e9 | patient | m23 | m14 | medium | dobj -> touching |
| e10 | agent | m24 | m16 | medium | nsubj -> smiles |
| e11 | relation | m0 | m2 | high | in |
| e12 | relation | m0 | m4 | high | with |
| e13 | relation | m0 | m6 | high | with |
| e14 | relation | m0 | m8 | high | with |
| e15 | relation | m4 | m5 | high | on |
| e16 | relation | m6 | m7 | high | in |
| e17 | relation | m8 | m9 | high | on |
| e18 | relation | m10 | m11 | high | in |
| e19 | relation | m10 | m15 | high | with |
| e20 | relation | m16 | m17 | high | on |
| e21 | relation | m18 | m20 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | proximity | proximity | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:proximity", "parents": []} |
| ent_m4 | object | man | man | person | person, human | m4 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m5 | context | left | left | object | scene_context | m5 | raw_mention |  |  |  | True | {"canonical": "entity:left", "parents": ["entity_parent:scene_context"]} |
| ent_m6 | object | woman | woman | person | person, human | m6 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m7 | context | center | center | object | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:center", "parents": ["entity_parent:scene_context"]} |
| ent_m8 | object | woman | woman | person | person, human | m8 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m9 | context | right | right | object | scene_context | m9 | raw_mention |  |  |  | True | {"canonical": "entity:right", "parents": ["entity_parent:scene_context"]} |
| ent_m10 | object | woman | woman | person | person, human | m10 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m11 | context | center | center | object | scene_context | m11 | raw_mention |  |  |  | True | {"canonical": "entity:center", "parents": ["entity_parent:scene_context"]} |
| ent_m12 | object | hair | hair | object | body_part | m12 | raw_mention |  |  |  | True | {"canonical": "entity:hair", "parents": ["entity_parent:body_part"]} |
| ent_m14 | object | lip | lips | object |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:lip", "parents": []} |
| ent_m15 | object | finger | finger | object | body_part | m15 | raw_mention |  |  |  | True | {"canonical": "entity:finger", "parents": ["entity_parent:body_part"]} |
| ent_m16 | object | woman | woman | person | person, human | m16 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m17 | context | right | right | object | scene_context | m17 | raw_mention |  |  |  | True | {"canonical": "entity:right", "parents": ["entity_parent:scene_context"]} |
| ent_m18 | object | sign | sign | document | text_carrier, artifact | m18 | raw_mention |  |  |  | True | {"canonical": "entity:sign", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m20 | context | background | background | object | scene_context | m20 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m21 | context | indoors | indoors | object | scene_context | m21 | raw_mention |  |  |  | True | {"canonical": "entity:indoors", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m22 | has | have | have | visual_action |  | agent:m10->ent_m10; patient:m12->ent_m12 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m23 | touching | touch | touch | visual_action |  | agent:m10->ent_m10; patient:m14->ent_m14 | {"canonical": "action:touch", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m24 | smiles | smile | smile | expression_action, visual_action |  | agent:m16->ent_m16 | {"canonical": "action:smile", "parents": ["action_parent:expression_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | have | agent | m10 | ent_m10 | medium | e6 | nsubj -> has |  |  |
| ce0 | have | patient | m12 | ent_m12 | medium | e7 | dobj -> has |  |  |
| ce1 | touch | agent | m10 | ent_m10 | medium | e8 | inherited agent conj -> has |  |  |
| ce1 | touch | patient | m14 | ent_m14 | medium | e9 | dobj -> touching |  |  |
| ce2 | smile | agent | m16 | ent_m16 | medium | e10 | nsubj -> smiles |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | spatial_containment, visual_relation | high | e11 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | with | association_relation, visual_relation | high | e12 | False | False |  |  |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | with | with | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr3 | m0 | m8 | ent_m0 | ent_m8 | with | with | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr4 | m4 | m5 | ent_m4 | ent_m5 | on | on | spatial_support, visual_relation | high | e15 | False | False |  |  |
| cr5 | m6 | m7 | ent_m6 | ent_m7 | in | in | spatial_containment, visual_relation | high | e16 | False | False |  |  |
| cr6 | m8 | m9 | ent_m8 | ent_m9 | on | on | spatial_support, visual_relation | high | e17 | False | False |  |  |
| cr7 | m10 | m11 | ent_m10 | ent_m11 | in | in | spatial_containment, visual_relation | high | e18 | False | False |  |  |
| cr8 | m10 | m15 | ent_m10 | ent_m15 | with | with | association_relation, visual_relation | high | e19 | False | False |  |  |
| cr9 | m16 | m17 | ent_m16 | ent_m17 | on | on | spatial_support, visual_relation | high | e20 | False | False |  |  |
| cr10 | m18 | m20 | ent_m18 | ent_m20 | in | in | spatial_containment, visual_relation | high | e21 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | proximity |  |  |  | entity_exists:proximity | True | low |
| cf2 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf3 | entity_exists | left |  |  | scene_context | entity_exists:left | True | medium |
| cf4 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf5 | entity_exists | center |  |  | scene_context | entity_exists:center | True | medium |
| cf6 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf7 | entity_exists | right |  |  | scene_context | entity_exists:right | True | medium |
| cf8 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf9 | entity_exists | center |  |  | scene_context | entity_exists:center | True | medium |
| cf10 | entity_exists | hair |  |  | body_part | entity_exists:hair | True | high |
| cf11 | entity_exists | lip |  |  |  | entity_exists:lip | True | low |
| cf12 | entity_exists | finger |  |  | body_part | entity_exists:finger | True | high |
| cf13 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf14 | entity_exists | right |  |  | scene_context | entity_exists:right | True | medium |
| cf15 | entity_exists | sign |  |  | text_carrier, artifact | entity_exists:sign | True | high |
| cf16 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf17 | entity_exists | indoors |  |  | scene_context | entity_exists:indoors | True | high |
| cf18 | has_quantity | people | three |  | exact_quantity, quantity | has_quantity:people:three | True | high |
| cf19 | has_attribute | proximity | close |  | modifier_attribute, visual_attribute | has_attribute:proximity:close | True | medium |
| cf20 | has_attribute | hair | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:hair:dark | True | medium |
| cf21 | has_attribute | sign | green-lit |  | modifier_attribute, visual_attribute | has_attribute:sign:green-lit | True | medium |
| cf22 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf23 | event_role | have | agent | woman |  | event_role:have:agent:woman | True | medium |
| cf24 | event_role | have | patient | hair |  | event_role:have:patient:hair | True | medium |
| cf25 | action_event | touch |  |  | visual_action | action_event:touch | True | low |
| cf26 | event_role | touch | agent | woman |  | event_role:touch:agent:woman | True | medium |
| cf27 | event_role | touch | patient | lip |  | event_role:touch:patient:lip | True | medium |
| cf28 | action_event | smile |  |  | expression_action, visual_action | action_event:smile | True | high |
| cf29 | event_role | smile | agent | woman |  | event_role:smile:agent:woman | True | medium |
| cf30 | relation | people | in | proximity | spatial_containment, visual_relation | relation:people:in:proximity | True | high |
| cf31 | relation | people | with | man | association_relation, visual_relation | relation:people:with:man | True | high |
| cf32 | relation | people | with | woman | association_relation, visual_relation | relation:people:with:woman | True | high |
| cf33 | relation | people | with | woman | association_relation, visual_relation | relation:people:with:woman | True | high |
| cf34 | relation | man | on | left | spatial_support, visual_relation | relation:man:on:left | True | high |
| cf35 | relation | woman | in | center | spatial_containment, visual_relation | relation:woman:in:center | True | high |
| cf36 | relation | woman | on | right | spatial_support, visual_relation | relation:woman:on:right | True | high |
| cf37 | relation | woman | in | center | spatial_containment, visual_relation | relation:woman:in:center | True | high |
| cf38 | relation | woman | with | finger | association_relation, visual_relation | relation:woman:with:finger | True | high |
| cf39 | relation | woman | on | right | spatial_support, visual_relation | relation:woman:on:right | True | high |
| cf40 | relation | sign | in | background | spatial_containment, visual_relation | relation:sign:in:background | True | high |

### Stage 9 Canonicalization Notes
_none_

## 22

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `0e7307588e1bd7a8877769b4ba2d54353f365910c3843e59fba4f25c14119014`
**parse_path:** `sentence`

> A brown duck swims in calm blue water, creating ripples around its body. Its head and neck are dark brown, with a lighter chest, and it glides smoothly near the surface. The water reflects light and faint tree branches above.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | duck | duck | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | brown | brown | color_attribute | chunk0 | 1 | high |
| m2 | object | water | water | noun_chunk_root | chunk1 | 7 | high |
| m3 | attribute | calm | calm | modifier_attribute | chunk1 | 5 | medium |
| m4 | attribute | blue | blue | color_attribute | chunk1 | 6 | high |
| m5 | object | ripples | ripple | noun_chunk_root | chunk2 | 10 | high |
| m6 | object | body | body | noun_chunk_root | chunk3 | 13 | high |
| m7 | object | head | head | noun_chunk_root | chunk4 | 16 | high |
| m8 | object | neck | neck | noun_chunk_root | chunk5 | 18 | high |
| m9 | object | chest | chest | noun_chunk_root | chunk6 | 26 | high |
| m10 | attribute | lighter | light | visual_attribute | chunk6 | 25 | medium |
| m11 | context | surface | surface | spatial_region | chunk8 | 34 | medium |
| m12 | object | water | water | noun_chunk_root | chunk9 | 37 | high |
| m13 | object | tree branches | tree_branch | noun_chunk_root | chunk10 | 42 | high |
| m14 | attribute | light | light | visual_attribute | chunk10 | 39 | medium |
| m15 | attribute | faint | faint | modifier_attribute | chunk10 | 41 | medium |
| m16 | action | swims | swim | verb_predicate | doc | 3 | high |
| m17 | action | creating | create | verb_predicate | doc | 9 | high |
| m18 | action | glides | glide | verb_predicate | doc | 30 | high |
| m19 | action | reflects | reflect | verb_predicate | doc | 38 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> duck |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> water |
| e2 | has_attribute | m2 | m4 | high | chunk1 amod -> water |
| e3 | has_attribute | m9 | m10 | medium | chunk6 amod -> chest |
| e4 | has_attribute | m13 | m14 | medium | chunk10 amod -> tree branches |
| e5 | has_attribute | m13 | m15 | medium | chunk10 conj -> tree branches |
| e6 | agent | m16 | m0 | medium | nsubj -> swims |
| e7 | agent | m17 | m0 | medium | inherited agent advcl -> swims |
| e8 | patient | m17 | m5 | medium | dobj -> creating |
| e9 | agent | m18 | m0 | medium | nsubj -> glides; resolved it -> duck |
| e10 | agent | m19 | m12 | medium | nsubj -> reflects |
| e11 | patient | m19 | m13 | medium | dobj -> reflects |
| e12 | relation | m0 | m2 | high | in |
| e13 | relation | m0 | m6 | high | around |
| e14 | relation | m0 | m11 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | duck | duck | animal | animal, living_thing | m0 | raw_mention |  |  |  | True | {"canonical": "entity:duck", "parents": ["entity_parent:animal", "entity_parent:living_thing"]} |
| ent_m2 | object | water | water | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": []} |
| ent_m5 | object | ripple | ripples | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:ripple", "parents": []} |
| ent_m6 | object | body | body | object | body_part | m6 | raw_mention |  |  |  | True | {"canonical": "entity:body", "parents": ["entity_parent:body_part"]} |
| ent_m7 | object | head | head | object | body_part | m7 | raw_mention |  |  |  | True | {"canonical": "entity:head", "parents": ["entity_parent:body_part"]} |
| ent_m8 | object | neck | neck | object | body_part | m8 | raw_mention |  |  |  | True | {"canonical": "entity:neck", "parents": ["entity_parent:body_part"]} |
| ent_m9 | object | chest | chest | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:chest", "parents": []} |
| ent_m11 | context | surface | surface | object | scene_context | m11 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": ["entity_parent:scene_context"]} |
| ent_m12 | object | water | water | object |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": []} |
| ent_m13 | object | tree_branch | tree branches | object |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:tree_branch", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | swims | swim | swim | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:swim", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m17 | creating | create | create | visual_action |  | agent:m0->ent_m0; patient:m5->ent_m5 | {"canonical": "action:create", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m18 | glides | glide | glide | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:glide", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce3 | m19 | reflects | reflect | reflect | visual_action |  | agent:m12->ent_m12; patient:m13->ent_m13 | {"canonical": "action:reflect", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | swim | agent | m0 | ent_m0 | medium | e6 | nsubj -> swims |  |  |
| ce1 | create | agent | m0 | ent_m0 | medium | e7 | inherited agent advcl -> swims |  |  |
| ce1 | create | patient | m5 | ent_m5 | medium | e8 | dobj -> creating |  |  |
| ce2 | glide | agent | m0 | ent_m0 | medium | e9 | nsubj -> glides; resolved it -> duck |  |  |
| ce3 | reflect | agent | m12 | ent_m12 | medium | e10 | nsubj -> reflects |  |  |
| ce3 | reflect | patient | m13 | ent_m13 | medium | e11 | dobj -> reflects |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | spatial_containment, visual_relation | high | e12 | False | False |  |  |
| cr1 | m0 | m6 | ent_m5 | ent_m6 | around | around | spatial_proximity, visual_relation | high | e13 | False | False | pp_source_disambiguation | created_object_location |
| cr2 | m0 | m11 | ent_m0 | ent_m11 | near | near | spatial_proximity, visual_relation | high | e14 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | duck |  |  | animal, living_thing | entity_exists:duck | True | high |
| cf1 | entity_exists | water |  |  |  | entity_exists:water | True | low |
| cf2 | entity_exists | ripple |  |  |  | entity_exists:ripple | True | low |
| cf3 | entity_exists | body |  |  | body_part | entity_exists:body | True | high |
| cf4 | entity_exists | head |  |  | body_part | entity_exists:head | True | high |
| cf5 | entity_exists | neck |  |  | body_part | entity_exists:neck | True | high |
| cf6 | entity_exists | chest |  |  |  | entity_exists:chest | True | low |
| cf7 | entity_exists | surface |  |  | scene_context | entity_exists:surface | True | medium |
| cf8 | entity_exists | water |  |  |  | entity_exists:water | True | low |
| cf9 | entity_exists | tree_branch |  |  |  | entity_exists:tree_branch | True | low |
| cf10 | has_attribute | duck | brown |  | color_attribute, color, visual_attribute | has_attribute:duck:brown | True | high |
| cf11 | has_attribute | water | calm |  | modifier_attribute, visual_attribute | has_attribute:water:calm | True | medium |
| cf12 | has_attribute | water | blue |  | color_attribute, color, visual_attribute | has_attribute:water:blue | True | high |
| cf13 | has_attribute | chest | light |  | visual_attribute | has_attribute:chest:light | True | medium |
| cf14 | has_attribute | tree_branch | light |  | visual_attribute | has_attribute:tree_branch:light | True | medium |
| cf15 | has_attribute | tree_branch | faint |  | modifier_attribute, visual_attribute | has_attribute:tree_branch:faint | True | medium |
| cf16 | action_event | swim |  |  | locomotion_action, visual_action | action_event:swim | True | high |
| cf17 | event_role | swim | agent | duck |  | event_role:swim:agent:duck | True | medium |
| cf18 | action_event | create |  |  | visual_action | action_event:create | True | low |
| cf19 | event_role | create | agent | duck |  | event_role:create:agent:duck | True | medium |
| cf20 | event_role | create | patient | ripple |  | event_role:create:patient:ripple | True | medium |
| cf21 | action_event | glide |  |  | locomotion_action, visual_action | action_event:glide | True | high |
| cf22 | event_role | glide | agent | duck |  | event_role:glide:agent:duck | True | medium |
| cf23 | action_event | reflect |  |  | visual_action | action_event:reflect | True | low |
| cf24 | event_role | reflect | agent | water |  | event_role:reflect:agent:water | True | medium |
| cf25 | event_role | reflect | patient | tree_branch |  | event_role:reflect:patient:tree_branch | True | medium |
| cf26 | relation | duck | in | water | spatial_containment, visual_relation | relation:duck:in:water | True | high |
| cf27 | relation | ripple | around | body | spatial_proximity, visual_relation | relation:ripple:around:body | True | high |
| cf28 | relation | duck | near | surface | spatial_proximity, visual_relation | relation:duck:near:surface | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| pp_source_disambiguated | m17 | e13 |  | ent_m6 | created_object_location | {"action_mention_id": "m17", "canonical_action": "create", "canonical_source": "ent_m5", "canonical_target": "ent_m6", "confidence": "medium", "kind": "pp_source_disambiguated", "previous_canonical_source": "ent_m0", "raw_edge_id": "e13", "raw_source": "m0", "raw_target": "m6", "reason": "created_object_location", "relation": "around"} |

## 23

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `0e976bfb7bcfe7c0ea36a64e605bba151e5a5a2b6e739540e24c3b07d68ce014`
**parse_path:** `tag_list`

> green scoreboard, hockey rink, banners, rough riders, ice surface

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | scoreboard | scoreboard | segment_head | t0 | 1 | high |
| m1 | attribute | green | green | attribute | t0 | 0 | high |
| m2 | object | rink | rink | segment_head | t1 | 1 | high |
| m3 | attribute | hockey | hockey | attribute | t1 | 0 | high |
| m4 | object | banners | banner | segment_head | t2 | 0 | high |
| m5 | object | riders | rider | segment_head | t3 | 1 | high |
| m6 | attribute | rough | rough | attribute | t3 | 0 | high |
| m7 | object | surface | surface | segment_head | t4 | 1 | high |
| m8 | attribute | ice | ice | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> scoreboard |
| e1 | has_attribute | m2 | m3 | high | t1 internal compound -> rink |
| e2 | has_attribute | m5 | m6 | high | t3 internal compound -> riders |
| e3 | has_attribute | m7 | m8 | high | t4 internal compound -> surface |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | scoreboard | scoreboard | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:scoreboard", "parents": []} |
| ent_m2 | object | rink | rink | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:rink", "parents": []} |
| ent_m4 | object | banner | banners | object | text_carrier, artifact | m4 | raw_mention |  |  |  | True | {"canonical": "entity:banner", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m5 | object | rider | riders | person | person, human | m5 | raw_mention |  |  |  | True | {"canonical": "entity:rider", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m7 | object | surface | surface | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": []} |

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
| cf0 | entity_exists | scoreboard |  |  |  | entity_exists:scoreboard | True | low |
| cf1 | entity_exists | rink |  |  |  | entity_exists:rink | True | low |
| cf2 | entity_exists | banner |  |  | text_carrier, artifact | entity_exists:banner | True | high |
| cf3 | entity_exists | rider |  |  | person, human | entity_exists:rider | True | high |
| cf4 | entity_exists | surface |  |  |  | entity_exists:surface | True | low |
| cf5 | has_attribute | scoreboard | green |  | color_attribute, color, visual_attribute | has_attribute:scoreboard:green | True | high |
| cf6 | has_attribute | rink | hockey |  | attribute, visual_attribute | has_attribute:rink:hockey | True | high |
| cf7 | has_attribute | rider | rough |  | texture_attribute, texture, visual_attribute | has_attribute:rider:rough | True | high |
| cf8 | has_attribute | surface | ice |  | attribute, visual_attribute | has_attribute:surface:ice | True | high |

### Stage 9 Canonicalization Notes
_none_

## 24

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `102c1e28a6c0c106f8ef32999591aa85fae258f045731fe97d3cde7bcf7cd014`
**parse_path:** `tag_list`

> text, page, russian, book, printed

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | text | text | segment_head | t0 | 0 | high |
| m1 | object | page | page | segment_head | t1 | 0 | high |
| m2 | attribute | russian | russian | floating_attribute | t2 | 0 | medium |
| m3 | object | book | book | segment_head | t3 | 0 | high |
| m4 | attribute | printed | print | floating_attribute | t4 | 0 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | candidate_has_attribute | m1 | m2 | low | t2 adjacent floating attribute |
| e1 | candidate_has_attribute | m3 | m4 | low | t4 adjacent floating attribute |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | text | text | document | text_content | m0 | raw_mention |  |  |  | True | {"canonical": "entity:text", "parents": ["entity_parent:text_content"]} |
| ent_m1 | object | page | page | document | document, text_carrier, artifact | m1 | raw_mention |  |  |  | True | {"canonical": "entity:page", "parents": ["entity_parent:document", "entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m3 | object | book | book | document | document, text_carrier, artifact | m3 | raw_mention |  |  |  | True | {"canonical": "entity:book", "parents": ["entity_parent:document", "entity_parent:text_carrier", "entity_parent:artifact"]} |

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
| cf0 | entity_exists | text |  |  | text_content | entity_exists:text | True | high |
| cf1 | entity_exists | page |  |  | document, text_carrier, artifact | entity_exists:page | True | high |
| cf2 | entity_exists | book |  |  | document, text_carrier, artifact | entity_exists:book | True | high |
| cf3 | candidate_has_attribute | page | russian |  | floating_attribute, visual_attribute | candidate_has_attribute:page:russian | False | low |
| cf4 | candidate_has_attribute | book | print |  | floating_attribute, visual_attribute | candidate_has_attribute:book:print | False | low |

### Stage 9 Canonicalization Notes
_none_

## 25

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `10360632429015a31bb702f2f1582216021cbd4735544d73052a16099d4d6014`
**parse_path:** `sentence`

> A brown dog leaps over a blue, white, and red basket on grass. A man in a black outfit with red and blue trim stands nearby, watching the dog. In the background, spectators stand behind a fence near a "ROYAL CANIN" banner.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "ROYAL CANIN" | royal_canin | quote_text | doc_quote | 45 | high |
| m1 | object | dog | dog | noun_chunk_root | chunk0 | 2 | high |
| m2 | attribute | brown | brown | color_attribute | chunk0 | 1 | high |
| m3 | object | basket | basket | noun_chunk_root | chunk1 | 12 | high |
| m4 | attribute | blue | blue | color_attribute | chunk1 | 6 | high |
| m5 | attribute | white | white | color_attribute | chunk1 | 8 | high |
| m6 | attribute | red | red | color_attribute | chunk1 | 11 | high |
| m7 | object | grass | grass | noun_chunk_root | chunk2 | 14 | high |
| m8 | object | man | man | noun_chunk_root | chunk3 | 17 | high |
| m9 | object | outfit | outfit | noun_chunk_root | chunk4 | 21 | high |
| m10 | attribute | black | black | color_attribute | chunk4 | 20 | high |
| m11 | object | trim | trim | noun_chunk_root | chunk5 | 26 | high |
| m12 | attribute | red | red | color_attribute | chunk5 | 23 | high |
| m13 | attribute | blue | blue | color_attribute | chunk5 | 25 | high |
| m14 | object | dog | dog | noun_chunk_root | chunk6 | 32 | high |
| m15 | context | background | background | scene_context | chunk7 | 36 | high |
| m16 | object | spectators | spectator | noun_chunk_root | chunk8 | 38 | high |
| m17 | object | fence | fence | noun_chunk_root | chunk9 | 42 | high |
| m18 | object | banner | banner | noun_chunk_root | chunk10 | 46 | high |
| m19 | action | leaps | leap | verb_predicate | doc | 3 | high |
| m20 | action | stands | stand | verb_predicate | doc | 27 | high |
| m21 | action | watching | watch | verb_predicate | doc | 30 | high |
| m22 | action | stand | stand | verb_predicate | doc | 39 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk0 amod -> dog |
| e1 | has_attribute | m3 | m4 | high | chunk1 amod -> basket |
| e2 | has_attribute | m3 | m5 | high | chunk1 conj -> basket |
| e3 | has_attribute | m3 | m6 | high | chunk1 conj -> basket |
| e4 | has_attribute | m9 | m10 | high | chunk4 amod -> outfit |
| e5 | has_attribute | m11 | m12 | high | chunk5 amod -> trim |
| e6 | has_attribute | m11 | m13 | high | chunk5 conj -> trim |
| e7 | has_context | scene | m15 | high | scene_context token background |
| e8 | has_attribute | m18 | m0 | high | chunk10 nmod -> banner |
| e9 | agent | m19 | m1 | medium | nsubj -> leaps |
| e10 | agent | m20 | m8 | medium | nsubj -> stands |
| e11 | agent | m21 | m8 | medium | inherited agent advcl -> stands |
| e12 | patient | m21 | m14 | medium | dobj -> watching |
| e13 | agent | m22 | m16 | medium | nsubj -> stand |
| e14 | relation | m1 | m3 | high | over |
| e15 | relation | m3 | m7 | high | on |
| e16 | relation | m8 | m9 | high | in |
| e17 | relation | m9 | m11 | high | with |
| e18 | relation | m16 | m15 | high | in |
| e19 | relation | m16 | m17 | high | behind |
| e20 | relation | m16 | m18 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | dog | dog | animal | animal, living_thing | m1 | raw_mention |  |  |  | True | {"canonical": "entity:dog", "parents": ["entity_parent:animal", "entity_parent:living_thing"]} |
| ent_m3 | object | basket | basket | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:basket", "parents": []} |
| ent_m7 | object | grass | grass | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": []} |
| ent_m8 | object | man | man | person | person, human | m8 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m9 | object | outfit | outfit | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:outfit", "parents": []} |
| ent_m11 | object | trim | trim | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:trim", "parents": []} |
| ent_m14 | object | dog | dog | animal | animal, living_thing | m14 | raw_mention |  |  |  | True | {"canonical": "entity:dog", "parents": ["entity_parent:animal", "entity_parent:living_thing"]} |
| ent_m15 | context | background | background | object | scene_context | m15 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m16 | object | spectator | spectators | object |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:spectator", "parents": []} |
| ent_m17 | object | fence | fence | object |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:fence", "parents": []} |
| ent_m18 | object | banner | banner | object | text_carrier, artifact | m18 | raw_mention |  |  |  | True | {"canonical": "entity:banner", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m19 | leaps | leap | leap | visual_action |  | agent:m1->ent_m1 | {"canonical": "action:leap", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m20 | stands | stand | stand | body_pose_action, visual_action |  | agent:m8->ent_m8 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce2 | m21 | watching | watch | watch | gaze_action, visual_action |  | agent:m8->ent_m8; patient:m14->ent_m14 | {"canonical": "action:watch", "parents": ["action_parent:gaze_action", "action_parent:visual_action"]} |  |
| ce3 | m22 | stand | stand | stand | body_pose_action, visual_action |  | agent:m16->ent_m16 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | leap | agent | m1 | ent_m1 | medium | e9 | nsubj -> leaps |  |  |
| ce1 | stand | agent | m8 | ent_m8 | medium | e10 | nsubj -> stands |  |  |
| ce2 | watch | agent | m8 | ent_m8 | medium | e11 | inherited agent advcl -> stands |  |  |
| ce2 | watch | patient | m14 | ent_m14 | medium | e12 | dobj -> watching |  |  |
| ce3 | stand | agent | m16 | ent_m16 | medium | e13 | nsubj -> stand |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m3 | ent_m1 | ent_m3 | over | above | spatial_vertical, visual_relation | high | e14 | False | False |  |  |
| cr1 | m3 | m7 | ent_m3 | ent_m7 | on | on | spatial_support, visual_relation | high | e15 | False | False |  |  |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | in | in | spatial_containment, visual_relation | high | e16 | False | False |  |  |
| cr3 | m9 | m11 | ent_m9 | ent_m11 | with | with | association_relation, visual_relation | high | e17 | False | False |  |  |
| cr4 | m16 | m15 | ent_m16 | ent_m15 | in | in | spatial_containment, visual_relation | high | e18 | False | False |  |  |
| cr5 | m16 | m17 | ent_m16 | ent_m17 | behind | behind | spatial_depth, visual_relation | high | e19 | False | False |  |  |
| cr6 | m16 | m18 | ent_m16 | ent_m18 | near | near | spatial_proximity, visual_relation | high | e20 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | dog |  |  | animal, living_thing | entity_exists:dog | True | high |
| cf1 | entity_exists | basket |  |  |  | entity_exists:basket | True | low |
| cf2 | entity_exists | grass |  |  |  | entity_exists:grass | True | low |
| cf3 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf4 | entity_exists | outfit |  |  |  | entity_exists:outfit | True | low |
| cf5 | entity_exists | trim |  |  |  | entity_exists:trim | True | low |
| cf6 | entity_exists | dog |  |  | animal, living_thing | entity_exists:dog | True | high |
| cf7 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf8 | entity_exists | spectator |  |  |  | entity_exists:spectator | True | low |
| cf9 | entity_exists | fence |  |  |  | entity_exists:fence | True | low |
| cf10 | entity_exists | banner |  |  | text_carrier, artifact | entity_exists:banner | True | high |
| cf11 | has_attribute | dog | brown |  | color_attribute, color, visual_attribute | has_attribute:dog:brown | True | high |
| cf12 | has_attribute | basket | blue |  | color_attribute, color, visual_attribute | has_attribute:basket:blue | True | high |
| cf13 | has_attribute | basket | white |  | color_attribute, color, visual_attribute | has_attribute:basket:white | True | high |
| cf14 | has_attribute | basket | red |  | color_attribute, color, visual_attribute | has_attribute:basket:red | True | high |
| cf15 | has_attribute | outfit | black |  | color_attribute, color, visual_attribute | has_attribute:outfit:black | True | high |
| cf16 | has_attribute | trim | red |  | color_attribute, color, visual_attribute | has_attribute:trim:red | True | high |
| cf17 | has_attribute | trim | blue |  | color_attribute, color, visual_attribute | has_attribute:trim:blue | True | high |
| cf18 | has_attribute | banner | royal_canin |  | quote_text, visual_attribute | has_attribute:banner:royal_canin | True | high |
| cf19 | action_event | leap |  |  | visual_action | action_event:leap | True | low |
| cf20 | event_role | leap | agent | dog |  | event_role:leap:agent:dog | True | medium |
| cf21 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf22 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf23 | action_event | watch |  |  | gaze_action, visual_action | action_event:watch | True | medium |
| cf24 | event_role | watch | agent | man |  | event_role:watch:agent:man | True | medium |
| cf25 | event_role | watch | patient | dog |  | event_role:watch:patient:dog | True | medium |
| cf26 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf27 | event_role | stand | agent | spectator |  | event_role:stand:agent:spectator | True | medium |
| cf28 | relation | dog | above | basket | spatial_vertical, visual_relation | relation:dog:above:basket | True | high |
| cf29 | relation | basket | on | grass | spatial_support, visual_relation | relation:basket:on:grass | True | high |
| cf30 | relation | man | in | outfit | spatial_containment, visual_relation | relation:man:in:outfit | True | high |
| cf31 | relation | outfit | with | trim | association_relation, visual_relation | relation:outfit:with:trim | True | high |
| cf32 | relation | spectator | in | background | spatial_containment, visual_relation | relation:spectator:in:background | True | high |
| cf33 | relation | spectator | behind | fence | spatial_depth, visual_relation | relation:spectator:behind:fence | True | high |
| cf34 | relation | spectator | near | banner | spatial_proximity, visual_relation | relation:spectator:near:banner | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e14 |  |  |  | {"canonical": "above", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e14", "raw_relation": "over", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 26

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `10b5d5feebae9613d0e6b4b6b39da6c83f0a783ab363bf8549cb72e231fdf814`
**parse_path:** `tag_list`

> axe, mask, costume, grass, fence, stump

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | axe | axe | segment_head | t0 | 0 | high |
| m1 | object | mask | mask | segment_head | t1 | 0 | high |
| m2 | object | costume | costume | segment_head | t2 | 0 | high |
| m3 | object | grass | grass | segment_head | t3 | 0 | high |
| m4 | object | fence | fence | segment_head | t4 | 0 | high |
| m5 | object | stump | stump | segment_head | t5 | 0 | high |

### Raw Concept Edges
_none_

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | axe | axe | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:axe", "parents": []} |
| ent_m1 | object | mask | mask | clothing | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:mask", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m2 | object | costume | costume | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:costume", "parents": []} |
| ent_m3 | object | grass | grass | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": []} |
| ent_m4 | object | fence | fence | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:fence", "parents": []} |
| ent_m5 | object | stump | stump | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:stump", "parents": []} |

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
| cf0 | entity_exists | axe |  |  |  | entity_exists:axe | True | low |
| cf1 | entity_exists | mask |  |  | clothing, wearable | entity_exists:mask | True | medium |
| cf2 | entity_exists | costume |  |  |  | entity_exists:costume | True | low |
| cf3 | entity_exists | grass |  |  |  | entity_exists:grass | True | low |
| cf4 | entity_exists | fence |  |  |  | entity_exists:fence | True | low |
| cf5 | entity_exists | stump |  |  |  | entity_exists:stump | True | low |

### Stage 9 Canonicalization Notes
_none_

## 27

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `10c4cd7231ff6d3987ddff17376eb7350864aaa2611b70c16fdee2a87f458014`
**parse_path:** `sentence`

> A man in a white shirt works on an electrical panel with wires and switches visible.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | shirt | shirt | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | white | white | color_attribute | chunk1 | 4 | high |
| m3 | object | panel | panel | noun_chunk_root | chunk2 | 10 | high |
| m4 | attribute | electrical | electrical | modifier_attribute | chunk2 | 9 | medium |
| m5 | object | wires | wire | noun_chunk_root | chunk3 | 12 | high |
| m6 | object | switches | switch | noun_chunk_root | chunk4 | 14 | high |
| m7 | action | works | work | verb_predicate | doc | 6 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> shirt |
| e1 | has_attribute | m3 | m4 | medium | chunk2 amod -> panel |
| e2 | agent | m7 | m0 | medium | nsubj -> works |
| e3 | relation | m0 | m1 | high | in |
| e4 | relation | m0 | m3 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | shirt | shirt | clothing | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | panel | panel | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:panel", "parents": []} |
| ent_m5 | object | wire | wires | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:wire", "parents": []} |
| ent_m6 | object | switch | switches | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:switch", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | works | work | work | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:work", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | work | agent | m0 | ent_m0 | medium | e2 | nsubj -> works |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | spatial_containment, visual_relation | high | e3 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | on | on | spatial_support, visual_relation | high | e4 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf2 | entity_exists | panel |  |  |  | entity_exists:panel | True | low |
| cf3 | entity_exists | wire |  |  |  | entity_exists:wire | True | low |
| cf4 | entity_exists | switch |  |  |  | entity_exists:switch | True | low |
| cf5 | has_attribute | shirt | white |  | color_attribute, color, visual_attribute | has_attribute:shirt:white | True | high |
| cf6 | has_attribute | panel | electrical |  | modifier_attribute, visual_attribute | has_attribute:panel:electrical | True | medium |
| cf7 | action_event | work |  |  | visual_action | action_event:work | True | low |
| cf8 | event_role | work | agent | man |  | event_role:work:agent:man | True | medium |
| cf9 | relation | man | in | shirt | spatial_containment, visual_relation | relation:man:in:shirt | True | high |
| cf10 | relation | man | on | panel | spatial_support, visual_relation | relation:man:on:panel | True | high |

### Stage 9 Canonicalization Notes
_none_

## 28

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `11adbf857279ff850b9bd6768acdaeb86ddecd51daf3f5980282a815b9e0c414`
**parse_path:** `sentence`

> A person in a blue and pink costume stands on a stage with glowing lights behind them.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | costume | costume | noun_chunk_root | chunk1 | 7 | high |
| m2 | attribute | blue | blue | color_attribute | chunk1 | 4 | high |
| m3 | attribute | pink | pink | color_attribute | chunk1 | 6 | high |
| m4 | object | stage | stage | noun_chunk_root | chunk2 | 11 | high |
| m5 | object | lights | light | noun_chunk_root | chunk3 | 14 | high |
| m6 | attribute | glowing | glow | state_attribute | chunk3 | 13 | medium |
| m7 | action | stands | stand | verb_predicate | doc | 8 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> costume |
| e1 | has_attribute | m1 | m3 | high | chunk1 conj -> costume |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> lights |
| e3 | agent | m7 | m0 | medium | nsubj -> stands |
| e4 | relation | m0 | m1 | high | in |
| e5 | relation | m0 | m4 | high | on |
| e6 | relation | m0 | m5 | high | with |
| e7 | relation | m5 | m0 | high | behind |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | costume | costume | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:costume", "parents": []} |
| ent_m4 | object | stage | stage | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:stage", "parents": []} |
| ent_m5 | object | light | lights | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:light", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | stands | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e3 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | spatial_containment, visual_relation | high | e4 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | on | spatial_support, visual_relation | high | e5 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | with | with | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr3 | m5 | m0 | ent_m5 | ent_m0 | behind | behind | spatial_depth, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf1 | entity_exists | costume |  |  |  | entity_exists:costume | True | low |
| cf2 | entity_exists | stage |  |  |  | entity_exists:stage | True | low |
| cf3 | entity_exists | light |  |  |  | entity_exists:light | True | low |
| cf4 | has_attribute | costume | blue |  | color_attribute, color, visual_attribute | has_attribute:costume:blue | True | high |
| cf5 | has_attribute | costume | pink |  | color_attribute, color, visual_attribute | has_attribute:costume:pink | True | high |
| cf6 | has_attribute | light | glow |  | state_attribute, visual_attribute | has_attribute:light:glow | True | medium |
| cf7 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf8 | event_role | stand | agent | person |  | event_role:stand:agent:person | True | medium |
| cf9 | relation | person | in | costume | spatial_containment, visual_relation | relation:person:in:costume | True | high |
| cf10 | relation | person | on | stage | spatial_support, visual_relation | relation:person:on:stage | True | high |
| cf11 | relation | person | with | light | association_relation, visual_relation | relation:person:with:light | True | high |
| cf12 | relation | light | behind | person | spatial_depth, visual_relation | relation:light:behind:person | True | high |

### Stage 9 Canonicalization Notes
_none_

## 29

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `120906119bf352f1e5f89c8f05a94ab5c8931e2066ff546366a6fbbd3540b414`
**parse_path:** `sentence`

> A yellow helicopter flies over a green hillside near a blue lake, with snow-capped mountains in the distance.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | helicopter | helicopter | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | yellow | yellow | color_attribute | chunk0 | 1 | high |
| m2 | object | hillside | hillside | noun_chunk_root | chunk1 | 7 | high |
| m3 | attribute | green | green | color_attribute | chunk1 | 6 | high |
| m4 | object | lake | lake | noun_chunk_root | chunk2 | 11 | high |
| m5 | attribute | blue | blue | color_attribute | chunk2 | 10 | high |
| m6 | context | distance | distance | scene_context | chunk3 | 18 | high |
| m7 | action | flies | fly | verb_predicate | doc | 3 | high |
| m8 | object | mountains | mountain | with_absolute_recovered_object | with_absolute13 | 15 | medium |
| m9 | attribute | snow-capped | snow-cappe | state_attribute | with_absolute13 | 14 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> helicopter |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> hillside |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> lake |
| e3 | has_context | scene | m6 | high | scene_context token distance |
| e4 | agent | m7 | m0 | medium | nsubj -> flies |
| e5 | scene_contains | scene | m8 | medium | with_absolute13 recovered mountains |
| e6 | has_attribute | m8 | m9 | medium | with_absolute13 amod -> mountains |
| e7 | relation | m0 | m2 | high | over |
| e8 | relation | m0 | m4 | high | near |
| e9 | relation | m8 | m6 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | helicopter | helicopter | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:helicopter", "parents": []} |
| ent_m2 | object | hillside | hillside | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:hillside", "parents": []} |
| ent_m4 | object | lake | lake | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:lake", "parents": []} |
| ent_m6 | context | distance | distance | object | scene_context, spatial_context | m6 | raw_mention |  |  |  | True | {"canonical": "entity:distance", "parents": ["entity_parent:scene_context", "entity_parent:spatial_context"]} |
| ent_m8 | object | mountain | mountains | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:mountain", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | flies | fly | fly | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:fly", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | fly | agent | m0 | ent_m0 | medium | e4 | nsubj -> flies |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | over | above | spatial_vertical, visual_relation | high | e7 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | near | near | spatial_proximity, visual_relation | high | e8 | False | False |  |  |
| cr2 | m8 | m6 | ent_m8 | ent_m6 | in | in | spatial_containment, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | helicopter |  |  |  | entity_exists:helicopter | True | low |
| cf1 | entity_exists | hillside |  |  |  | entity_exists:hillside | True | low |
| cf2 | entity_exists | lake |  |  |  | entity_exists:lake | True | low |
| cf3 | entity_exists | distance |  |  | scene_context, spatial_context | entity_exists:distance | True | high |
| cf4 | entity_exists | mountain |  |  |  | entity_exists:mountain | True | low |
| cf5 | has_attribute | helicopter | yellow |  | color_attribute, color, visual_attribute | has_attribute:helicopter:yellow | True | high |
| cf6 | has_attribute | hillside | green |  | color_attribute, color, visual_attribute | has_attribute:hillside:green | True | high |
| cf7 | has_attribute | lake | blue |  | color_attribute, color, visual_attribute | has_attribute:lake:blue | True | high |
| cf8 | has_attribute | mountain | snow-cappe |  | state_attribute, visual_attribute | has_attribute:mountain:snow-cappe | True | medium |
| cf9 | action_event | fly |  |  | visual_action | action_event:fly | True | low |
| cf10 | event_role | fly | agent | helicopter |  | event_role:fly:agent:helicopter | True | medium |
| cf11 | relation | helicopter | above | hillside | spatial_vertical, visual_relation | relation:helicopter:above:hillside | True | high |
| cf12 | relation | helicopter | near | lake | spatial_proximity, visual_relation | relation:helicopter:near:lake | True | high |
| cf13 | relation | mountain | in | distance | spatial_containment, visual_relation | relation:mountain:in:distance | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e7 |  |  |  | {"canonical": "above", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e7", "raw_relation": "over", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 30

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `128f7b170ef59050b227c1707de8baf01bdbd6538ddd1a66b840bd1586d83414`
**parse_path:** `sentence`

> A man and woman stand on a sandy beach, sharing a drink together.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | woman | woman | noun_chunk_root | chunk1 | 3 | high |
| m2 | object | beach | beach | noun_chunk_root | chunk2 | 8 | high |
| m3 | attribute | sandy | sandy | modifier_attribute | chunk2 | 7 | medium |
| m4 | object | drink | drink | noun_chunk_root | chunk3 | 12 | high |
| m5 | action | stand | stand | verb_predicate | doc | 4 | high |
| m6 | action | sharing | share | verb_predicate | doc | 10 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | medium | chunk2 amod -> beach |
| e1 | agent | m5 | m0 | medium | nsubj -> stand |
| e2 | agent | m5 | m1 | medium | nsubj -> stand |
| e3 | agent | m6 | m0 | medium | inherited agent advcl -> stand |
| e4 | agent | m6 | m1 | medium | inherited agent advcl -> stand |
| e5 | patient | m6 | m4 | medium | dobj -> sharing |
| e6 | relation | m0 | m2 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | woman | woman | person | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | beach | beach | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:beach", "parents": []} |
| ent_m4 | object | drink | drink | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:drink", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m5 | stand | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0; agent:m1->ent_m1 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m6 | sharing | share | share | visual_action |  | agent:m0->ent_m0; agent:m1->ent_m1; patient:m4->ent_m4 | {"canonical": "action:share", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e1 | nsubj -> stand |  |  |
| ce0 | stand | agent | m1 | ent_m1 | medium | e2 | nsubj -> stand |  |  |
| ce1 | share | agent | m0 | ent_m0 | medium | e3 | inherited agent advcl -> stand |  |  |
| ce1 | share | agent | m1 | ent_m1 | medium | e4 | inherited agent advcl -> stand |  |  |
| ce1 | share | patient | m4 | ent_m4 | medium | e5 | dobj -> sharing |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | on | spatial_support, visual_relation | high | e6 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf2 | entity_exists | beach |  |  |  | entity_exists:beach | True | low |
| cf3 | entity_exists | drink |  |  |  | entity_exists:drink | True | low |
| cf4 | has_attribute | beach | sandy |  | material_attribute, material, visual_attribute | has_attribute:beach:sandy | True | medium |
| cf5 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf6 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf7 | event_role | stand | agent | woman |  | event_role:stand:agent:woman | True | medium |
| cf8 | action_event | share |  |  | visual_action | action_event:share | True | low |
| cf9 | event_role | share | agent | man |  | event_role:share:agent:man | True | medium |
| cf10 | event_role | share | agent | woman |  | event_role:share:agent:woman | True | medium |
| cf11 | event_role | share | patient | drink |  | event_role:share:patient:drink | True | medium |
| cf12 | relation | man | on | beach | spatial_support, visual_relation | relation:man:on:beach | True | high |

### Stage 9 Canonicalization Notes
_none_

## 31

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `131382c8917ce69624883320df35ad846216456fba6b33e40b541b016aab9014`
**parse_path:** `sentence`

> Several giraffes stand in a dry, dusty savanna with scattered trees.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | giraffes | giraffe | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Several | several | approximate_quantity | chunk0 | 0 | medium |
| m2 | object | savanna | savanna | noun_chunk_root | chunk1 | 8 | high |
| m3 | attribute | dry | dry | modifier_attribute | chunk1 | 5 | medium |
| m4 | attribute | dusty | dusty | modifier_attribute | chunk1 | 7 | medium |
| m5 | object | trees | tree | noun_chunk_root | chunk2 | 11 | high |
| m6 | attribute | scattered | scatter | state_attribute | chunk2 | 10 | medium |
| m7 | action | stand | stand | verb_predicate | doc | 2 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | medium | chunk0 quantity -> giraffes |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> savanna |
| e2 | has_attribute | m2 | m4 | medium | chunk1 amod -> savanna |
| e3 | has_attribute | m5 | m6 | medium | chunk2 amod -> trees |
| e4 | agent | m7 | m0 | medium | nsubj -> stand |
| e5 | relation | m0 | m2 | high | in |
| e6 | relation | m2 | m5 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | giraffe | giraffes | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:giraffe", "parents": []} |
| ent_m2 | object | savanna | savanna | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:savanna", "parents": []} |
| ent_m5 | object | tree | trees | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | stand | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e4 | nsubj -> stand |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | spatial_containment, visual_relation | high | e5 | False | False |  |  |
| cr1 | m2 | m5 | ent_m2 | ent_m5 | with | with | association_relation, visual_relation | high | e6 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | giraffe |  |  |  | entity_exists:giraffe | True | low |
| cf1 | entity_exists | savanna |  |  |  | entity_exists:savanna | True | low |
| cf2 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf3 | has_quantity | giraffe | several |  | approximate_quantity, quantity | has_quantity:giraffe:several | True | medium |
| cf4 | has_attribute | savanna | dry |  | state_attribute, clean_exact_overlap, state, visual_attribute | has_attribute:savanna:dry | True | medium |
| cf5 | has_attribute | savanna | dusty |  | condition_attribute, cleanliness, visual_attribute | has_attribute:savanna:dusty | True | medium |
| cf6 | has_attribute | tree | scatter |  | state_attribute, visual_attribute | has_attribute:tree:scatter | True | medium |
| cf7 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf8 | event_role | stand | agent | giraffe |  | event_role:stand:agent:giraffe | True | medium |
| cf9 | relation | giraffe | in | savanna | spatial_containment, visual_relation | relation:giraffe:in:savanna | True | high |
| cf10 | relation | savanna | with | tree | association_relation, visual_relation | relation:savanna:with:tree | True | high |

### Stage 9 Canonicalization Notes
_none_

## 32

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `13f6ef667e3a8e279fbed679e2ff0eabef743354d2696c3b4164764c8b362414`
**parse_path:** `sentence`

> A close-up of a human eye with green irises and dark pupils. The eye is framed by blurred eyelashes and skin, with warm, glowing light surrounding it. Text at the bottom reads "BORDERLINE BIENNALE 2011 | Week-end 02 | Hacking, T.A.Z. & Utopies Pirates."

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "BORDERLINE BIENNALE 2011 \| Week-end 02 \| Hacking, T.A.Z. & Utopies Pirates." | borderline_biennale_2011_\|_week-end_02_\|_hacking,_t.a.z._&_utopies_pirates. | quote_text | doc_quote | 35 | high |
| m1 | object | close-up | close-up | noun_chunk_root | chunk0 | 1 | high |
| m2 | object | human eye | human_eye | noun_chunk_root | chunk1 | 4 | high |
| m3 | object | irises | iris | noun_chunk_root | chunk2 | 7 | high |
| m4 | attribute | green | green | color_attribute | chunk2 | 6 | high |
| m5 | object | pupils | pupil | noun_chunk_root | chunk3 | 10 | high |
| m6 | attribute | dark | dark | visual_attribute | chunk3 | 9 | medium |
| m7 | object | eye | eye | noun_chunk_root | chunk4 | 13 | high |
| m8 | object | eyelashes | eyelash | noun_chunk_root | chunk5 | 18 | high |
| m9 | attribute | blurred | blurred | modifier_attribute | chunk5 | 17 | medium |
| m10 | object | skin | skin | noun_chunk_root | chunk6 | 20 | high |
| m11 | object | light | light | noun_chunk_root | chunk7 | 26 | high |
| m12 | attribute | warm | warm | modifier_attribute | chunk7 | 23 | medium |
| m13 | attribute | glowing | glow | state_attribute | chunk7 | 25 | medium |
| m14 | object | Text | text | noun_chunk_root | chunk9 | 30 | high |
| m15 | context | bottom | bottom | spatial_region | chunk10 | 33 | medium |
| m16 | action | framed | frame | verb_predicate | doc | 15 | high |
| m17 | action | surrounding | surround | verb_predicate | doc | 27 | high |
| m18 | action | reads | read | verb_predicate | doc | 34 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m3 | m4 | high | chunk2 amod -> irises |
| e1 | has_attribute | m5 | m6 | medium | chunk3 amod -> pupils |
| e2 | has_attribute | m8 | m9 | medium | chunk5 amod -> eyelashes |
| e3 | has_attribute | m11 | m12 | medium | chunk7 amod -> light |
| e4 | has_attribute | m11 | m13 | medium | chunk7 amod -> light |
| e5 | agent | m16 | m7 | medium | nsubjpass -> framed |
| e6 | agent | m17 | m11 | medium | nsubj -> surrounding |
| e7 | patient | m17 | m7 | medium | dobj -> surrounding; resolved it -> eye |
| e8 | agent | m18 | m14 | medium | nsubj -> reads |
| e9 | patient | m18 | m0 | medium | dobj -> reads |
| e10 | relation | m1 | m2 | medium | of |
| e11 | relation | m2 | m3 | high | with |
| e12 | relation | m2 | m5 | high | with |
| e13 | relation | m7 | m8 | medium | by |
| e14 | relation | m7 | m10 | medium | by |
| e15 | relation | m14 | m15 | medium | at |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | close-up | close-up | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:close-up", "parents": []} |
| ent_m2 | object | human_eye | human eye | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:human_eye", "parents": []} |
| ent_m3 | object | iris | irises | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:iris", "parents": []} |
| ent_m5 | object | pupil | pupils | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:pupil", "parents": []} |
| ent_m7 | object | eye | eye | object | body_part | m7 | raw_mention |  |  |  | True | {"canonical": "entity:eye", "parents": ["entity_parent:body_part"]} |
| ent_m8 | object | eyelash | eyelashes | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:eyelash", "parents": []} |
| ent_m10 | object | skin | skin | object |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:skin", "parents": []} |
| ent_m11 | object | light | light | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:light", "parents": []} |
| ent_m14 | object | text | Text | document | text_content | m14 | raw_mention |  |  |  | True | {"canonical": "entity:text", "parents": ["entity_parent:text_content"]} |
| ent_m15 | context | bottom | bottom | object | scene_context | m15 | raw_mention |  |  |  | True | {"canonical": "entity:bottom", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | framed | frame | frame | visual_action |  | theme:m7->ent_m7; by_agent_or_causer:m8->ent_m8; by_agent_or_causer:m10->ent_m10 | {"canonical": "action:frame", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m17 | surrounding | surround | surround | visual_action |  | agent:m11->ent_m11; patient:m7->ent_m7 | {"canonical": "action:surround", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m18 | reads | read | read | text_interaction_action, visual_action |  | agent:m14->ent_m14; patient:m0->None | {"canonical": "action:read", "parents": ["action_parent:text_interaction_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | frame | theme | m7 | ent_m7 | medium | e5 | nsubjpass -> framed |  |  |
| ce0 | frame | by_agent_or_causer | m8 | ent_m8 | medium | e13 | passive by-frame |  |  |
| ce0 | frame | by_agent_or_causer | m10 | ent_m10 | medium | e14 | passive by-frame |  |  |
| ce1 | surround | agent | m11 | ent_m11 | medium | e6 | nsubj -> surrounding |  |  |
| ce1 | surround | patient | m7 | ent_m7 | medium | e7 | dobj -> surrounding; resolved it -> eye |  |  |
| ce2 | read | agent | m14 | ent_m14 | medium | e8 | nsubj -> reads |  |  |
| ce2 | read | patient | m0 |  | medium | e9 | dobj -> reads |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | of | of | part_relation, visual_relation | medium | e10 | False | False |  |  |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | with | with | association_relation, visual_relation | high | e11 | False | False |  |  |
| cr2 | m2 | m5 | ent_m2 | ent_m5 | with | with | association_relation, visual_relation | high | e12 | False | False |  |  |
| cr3 | m7 | m8 | ent_m7 | ent_m8 | by | by | spatial_proximity, visual_relation | medium | e13 | True | False |  |  |
| cr4 | m7 | m10 | ent_m7 | ent_m10 | by | by | spatial_proximity, visual_relation | medium | e14 | True | False |  |  |
| cr5 | m14 | m15 | ent_m14 | ent_m15 | at | at | spatial_location, visual_relation | medium | e15 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | close-up |  |  |  | entity_exists:close-up | True | low |
| cf1 | entity_exists | human_eye |  |  |  | entity_exists:human_eye | True | low |
| cf2 | entity_exists | iris |  |  |  | entity_exists:iris | True | low |
| cf3 | entity_exists | pupil |  |  |  | entity_exists:pupil | True | low |
| cf4 | entity_exists | eye |  |  | body_part | entity_exists:eye | True | high |
| cf5 | entity_exists | eyelash |  |  |  | entity_exists:eyelash | True | low |
| cf6 | entity_exists | skin |  |  |  | entity_exists:skin | True | low |
| cf7 | entity_exists | light |  |  |  | entity_exists:light | True | low |
| cf8 | entity_exists | text |  |  | text_content | entity_exists:text | True | high |
| cf9 | entity_exists | bottom |  |  | scene_context | entity_exists:bottom | True | medium |
| cf10 | has_attribute | iris | green |  | color_attribute, color, visual_attribute | has_attribute:iris:green | True | high |
| cf11 | has_attribute | pupil | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:pupil:dark | True | medium |
| cf12 | has_attribute | eyelash | blurred |  | modifier_attribute, visual_attribute | has_attribute:eyelash:blurred | True | medium |
| cf13 | has_attribute | light | warm |  | modifier_attribute, visual_attribute | has_attribute:light:warm | True | medium |
| cf14 | has_attribute | light | glow |  | state_attribute, visual_attribute | has_attribute:light:glow | True | medium |
| cf15 | action_event | frame |  |  | visual_action | action_event:frame | True | low |
| cf16 | event_role | frame | theme | eye |  | event_role:frame:theme:eye | True | medium |
| cf17 | event_role | frame | by_agent_or_causer | eyelash |  | event_role:frame:by_agent_or_causer:eyelash | True | medium |
| cf18 | event_role | frame | by_agent_or_causer | skin |  | event_role:frame:by_agent_or_causer:skin | True | medium |
| cf19 | action_event | surround |  |  | visual_action | action_event:surround | True | low |
| cf20 | event_role | surround | agent | light |  | event_role:surround:agent:light | True | medium |
| cf21 | event_role | surround | patient | eye |  | event_role:surround:patient:eye | True | medium |
| cf22 | action_event | read |  |  | text_interaction_action, visual_action | action_event:read | True | medium |
| cf23 | event_role | read | agent | text |  | event_role:read:agent:text | True | medium |
| cf24 | event_role | read | patient |  |  | event_role:read:patient | False | medium |
| cf25 | relation | close-up | of | human_eye | part_relation, visual_relation | relation:close-up:of:human_eye | True | medium |
| cf26 | relation | human_eye | with | iris | association_relation, visual_relation | relation:human_eye:with:iris | True | high |
| cf27 | relation | human_eye | with | pupil | association_relation, visual_relation | relation:human_eye:with:pupil | True | high |
| cf28 | relation | eye | by | eyelash | spatial_proximity, visual_relation | relation:eye:by:eyelash | False | medium |
| cf29 | relation | eye | by | skin | spatial_proximity, visual_relation | relation:eye:by:skin | False | medium |
| cf30 | relation | text | at | bottom | spatial_location, visual_relation | relation:text:at:bottom | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m16 | e5 | m7 |  |  | {"action_mention_id": "m16", "kind": "passive_subject_to_theme", "raw_edge_id": "e5", "target": "m7"} |
| passive_by_frame_to_event_role | m16 | e13 |  |  |  | {"action_mention_id": "m16", "by_agent_or_causer": "m8", "kind": "passive_by_frame_to_event_role", "raw_edge_id": "e13", "theme": "m7"} |
| passive_by_frame_to_event_role | m16 | e14 |  |  |  | {"action_mention_id": "m16", "by_agent_or_causer": "m10", "kind": "passive_by_frame_to_event_role", "raw_edge_id": "e14", "theme": "m7"} |

## 33

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `1524f40396e3ee37f6ab4234e0783cbbdab0250d92b25f92a011fc39bd2a4014`
**parse_path:** `sentence`

> A woman walks down a city sidewalk while talking on her phone, carrying a black bag.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | sidewalk | sidewalk | noun_chunk_root | chunk1 | 6 | high |
| m2 | attribute | city | city | compound_modifier | chunk1 | 5 | medium |
| m3 | object | phone | phone | noun_chunk_root | chunk2 | 11 | high |
| m4 | object | bag | bag | noun_chunk_root | chunk3 | 16 | high |
| m5 | attribute | black | black | color_attribute | chunk3 | 15 | high |
| m6 | action | walks | walk | verb_predicate | doc | 2 | high |
| m7 | action | talking | talk | verb_predicate | doc | 8 | high |
| m8 | action | carrying | carry | verb_predicate | doc | 13 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 compound -> sidewalk |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> bag |
| e2 | agent | m6 | m0 | medium | nsubj -> walks |
| e3 | agent | m7 | m0 | medium | inherited agent advcl -> walks |
| e4 | agent | m8 | m0 | medium | inherited agent advcl -> walks |
| e5 | patient | m8 | m4 | medium | dobj -> carrying |
| e6 | relation | m0 | m1 | medium | down |
| e7 | relation | m0 | m3 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | sidewalk | sidewalk | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:sidewalk", "parents": []} |
| ent_m3 | object | phone | phone | device | device, artifact | m3 | raw_mention |  |  |  | True | {"canonical": "entity:phone", "parents": ["entity_parent:device", "entity_parent:artifact"]} |
| ent_m4 | object | bag | bag | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:bag", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m6 | walks | walk | walk | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:walk", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m7 | talking | talk | talk | communication_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:talk", "parents": ["action_parent:communication_action", "action_parent:visual_action"]} |  |
| ce2 | m8 | carrying | carry | carry | manipulation_action, visual_action |  | agent:m0->ent_m0; patient:m4->ent_m4 | {"canonical": "action:carry", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | walk | agent | m0 | ent_m0 | medium | e2 | nsubj -> walks |  |  |
| ce1 | talk | agent | m0 | ent_m0 | medium | e3 | inherited agent advcl -> walks |  |  |
| ce2 | carry | agent | m0 | ent_m0 | medium | e4 | inherited agent advcl -> walks |  |  |
| ce2 | carry | patient | m4 | ent_m4 | medium | e5 | dobj -> carrying |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | down | down | visual_relation | medium | e6 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | on | on | spatial_support, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | sidewalk |  |  |  | entity_exists:sidewalk | True | low |
| cf2 | entity_exists | phone |  |  | device, artifact | entity_exists:phone | True | high |
| cf3 | entity_exists | bag |  |  |  | entity_exists:bag | True | low |
| cf4 | has_attribute | sidewalk | city |  | compound_modifier, visual_attribute | has_attribute:sidewalk:city | True | medium |
| cf5 | has_attribute | bag | black |  | color_attribute, color, visual_attribute | has_attribute:bag:black | True | high |
| cf6 | action_event | walk |  |  | locomotion_action, visual_action | action_event:walk | True | high |
| cf7 | event_role | walk | agent | woman |  | event_role:walk:agent:woman | True | medium |
| cf8 | action_event | talk |  |  | communication_action, visual_action | action_event:talk | True | medium |
| cf9 | event_role | talk | agent | woman |  | event_role:talk:agent:woman | True | medium |
| cf10 | action_event | carry |  |  | manipulation_action, visual_action | action_event:carry | True | high |
| cf11 | event_role | carry | agent | woman |  | event_role:carry:agent:woman | True | medium |
| cf12 | event_role | carry | patient | bag |  | event_role:carry:patient:bag | True | medium |
| cf13 | relation | woman | down | sidewalk | visual_relation | relation:woman:down:sidewalk | True | medium |
| cf14 | relation | woman | on | phone | spatial_support, visual_relation | relation:woman:on:phone | True | high |

### Stage 9 Canonicalization Notes
_none_

## 34

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `1703f280c90701c4aef227f67111f898a019781df197ca00271778204d4e0014`
**parse_path:** `sentence`

> A black-and-white graffiti stencil on a concrete pillar reads “THE ONLY MAN TO ENTER PARLIAMENT WITH HONEST INTENTIONS.” The artwork depicts a man in a hat and ruff collar, surrounded by a circle. The pillar stands beside a narrow alley with a stone wall and a wooden beam above.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “THE ONLY MAN TO ENTER PARLIAMENT WITH HONEST INTENTIONS.” | the_only_man_to_enter_parliament_with_honest_intentions. | quote_text | doc_quote | 9 | high |
| m1 | object | stencil | stencil | noun_chunk_root | chunk0 | 3 | high |
| m2 | attribute | black-and-white | black-and-white | modifier_attribute | chunk0 | 1 | medium |
| m3 | attribute | graffiti | graffiti | compound_modifier | chunk0 | 2 | medium |
| m4 | object | pillar | pillar | noun_chunk_root | chunk1 | 7 | high |
| m5 | attribute | concrete | concrete | material_attribute | chunk1 | 6 | high |
| m6 | object | artwork | artwork | noun_chunk_root | chunk2 | 11 | high |
| m7 | object | man | man | noun_chunk_root | chunk3 | 14 | high |
| m8 | object | hat | hat | noun_chunk_root | chunk4 | 17 | high |
| m9 | object | collar | collar | noun_chunk_root | chunk5 | 20 | high |
| m10 | attribute | ruff | ruff | compound_modifier | chunk5 | 19 | medium |
| m11 | object | circle | circle | noun_chunk_root | chunk6 | 25 | high |
| m12 | object | pillar | pillar | noun_chunk_root | chunk7 | 28 | high |
| m13 | object | alley | alley | noun_chunk_root | chunk8 | 33 | high |
| m14 | attribute | narrow | narrow | size_attribute | chunk8 | 32 | high |
| m15 | object | wall | wall | noun_chunk_root | chunk9 | 37 | high |
| m16 | attribute | stone | stone | material_attribute | chunk9 | 36 | high |
| m17 | object | beam | beam | noun_chunk_root | chunk10 | 41 | high |
| m18 | attribute | wooden | wooden | material_attribute | chunk10 | 40 | high |
| m19 | action | reads | read | verb_predicate | doc | 8 | high |
| m20 | action | depicts | depict | verb_predicate | doc | 12 | high |
| m21 | action | surrounded | surround | verb_predicate | doc | 22 | high |
| m22 | action | stands | stand | verb_predicate | doc | 29 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk0 amod -> stencil |
| e1 | has_attribute | m1 | m3 | medium | chunk0 compound -> stencil |
| e2 | has_attribute | m4 | m5 | high | chunk1 amod -> pillar |
| e3 | has_attribute | m9 | m10 | medium | chunk5 compound -> collar |
| e4 | has_attribute | m13 | m14 | high | chunk8 amod -> alley |
| e5 | has_attribute | m15 | m16 | high | chunk9 compound -> wall |
| e6 | has_attribute | m17 | m18 | high | chunk10 amod -> beam |
| e7 | agent | m19 | m1 | medium | nsubj -> reads |
| e8 | agent | m20 | m6 | medium | nsubj -> depicts |
| e9 | patient | m20 | m7 | medium | dobj -> depicts |
| e10 | agent | m21 | m7 | medium | inherited agent acl -> man |
| e11 | agent | m22 | m12 | medium | nsubj -> stands |
| e12 | relation | m1 | m4 | high | on |
| e13 | relation | m7 | m8 | high | in |
| e14 | relation | m7 | m9 | high | in |
| e15 | relation | m7 | m11 | medium | by |
| e16 | relation | m12 | m13 | high | beside |
| e17 | relation | m13 | m15 | high | with |
| e18 | relation | m13 | m17 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | stencil | stencil | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:stencil", "parents": []} |
| ent_m4 | object | pillar | pillar | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:pillar", "parents": []} |
| ent_m6 | object | artwork | artwork | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:artwork", "parents": []} |
| ent_m7 | object | man | man | person | person, human | m7 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m8 | object | hat | hat | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:hat", "parents": []} |
| ent_m9 | object | collar | collar | clothing | clothing, wearable | m9 | raw_mention |  |  |  | True | {"canonical": "entity:collar", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m11 | object | circle | circle | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:circle", "parents": []} |
| ent_m12 | object | pillar | pillar | object |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:pillar", "parents": []} |
| ent_m13 | object | alley | alley | object |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:alley", "parents": []} |
| ent_m15 | object | wall | wall | object |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |
| ent_m17 | object | beam | beam | object |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:beam", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m19 | reads | read | read | text_interaction_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:read", "parents": ["action_parent:text_interaction_action", "action_parent:visual_action"]} |  |
| ce1 | m20 | depicts | depict | depict | visual_action |  | agent:m6->ent_m6; patient:m7->ent_m7 | {"canonical": "action:depict", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m21 | surrounded | surround | surround | visual_action |  | agent:m7->ent_m7 | {"canonical": "action:surround", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m22 | stands | stand | stand | body_pose_action, visual_action |  | agent:m12->ent_m12 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | read | agent | m1 | ent_m1 | medium | e7 | nsubj -> reads |  |  |
| ce1 | depict | agent | m6 | ent_m6 | medium | e8 | nsubj -> depicts |  |  |
| ce1 | depict | patient | m7 | ent_m7 | medium | e9 | dobj -> depicts |  |  |
| ce2 | surround | agent | m7 | ent_m7 | medium | e10 | inherited agent acl -> man |  |  |
| ce3 | stand | agent | m12 | ent_m12 | medium | e11 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m4 | ent_m1 | ent_m4 | on | on | spatial_support, visual_relation | high | e12 | False | False |  |  |
| cr1 | m7 | m8 | ent_m7 | ent_m8 | in | in | spatial_containment, visual_relation | high | e13 | False | False |  |  |
| cr2 | m7 | m9 | ent_m7 | ent_m9 | in | in | spatial_containment, visual_relation | high | e14 | False | False |  |  |
| cr3 | m7 | m11 | ent_m7 | ent_m11 | by | by | spatial_proximity, visual_relation | medium | e15 | False | False |  |  |
| cr4 | m12 | m13 | ent_m12 | ent_m13 | beside | next_to | spatial_proximity, visual_relation | high | e16 | False | False |  |  |
| cr5 | m13 | m15 | ent_m13 | ent_m15 | with | with | association_relation, visual_relation | high | e17 | False | False |  |  |
| cr6 | m13 | m17 | ent_m13 | ent_m17 | with | with | association_relation, visual_relation | high | e18 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | stencil |  |  |  | entity_exists:stencil | True | low |
| cf1 | entity_exists | pillar |  |  |  | entity_exists:pillar | True | low |
| cf2 | entity_exists | artwork |  |  |  | entity_exists:artwork | True | low |
| cf3 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf4 | entity_exists | hat |  |  |  | entity_exists:hat | True | low |
| cf5 | entity_exists | collar |  |  | clothing, wearable | entity_exists:collar | True | medium |
| cf6 | entity_exists | circle |  |  |  | entity_exists:circle | True | low |
| cf7 | entity_exists | pillar |  |  |  | entity_exists:pillar | True | low |
| cf8 | entity_exists | alley |  |  |  | entity_exists:alley | True | low |
| cf9 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf10 | entity_exists | beam |  |  |  | entity_exists:beam | True | low |
| cf11 | has_attribute | stencil | black-and-white |  | modifier_attribute, visual_attribute | has_attribute:stencil:black-and-white | True | medium |
| cf12 | has_attribute | stencil | graffiti |  | compound_modifier, visual_attribute | has_attribute:stencil:graffiti | True | medium |
| cf13 | has_attribute | pillar | concrete |  | material_attribute, material, visual_attribute | has_attribute:pillar:concrete | True | high |
| cf14 | has_attribute | collar | ruff |  | compound_modifier, visual_attribute | has_attribute:collar:ruff | True | medium |
| cf15 | has_attribute | alley | narrow |  | size_attribute, width, visual_attribute | has_attribute:alley:narrow | True | high |
| cf16 | has_attribute | wall | stone |  | material_attribute, material, visual_attribute | has_attribute:wall:stone | True | high |
| cf17 | has_attribute | beam | wooden |  | material_attribute, material, visual_attribute | has_attribute:beam:wooden | True | high |
| cf18 | action_event | read |  |  | text_interaction_action, visual_action | action_event:read | True | medium |
| cf19 | event_role | read | agent | stencil |  | event_role:read:agent:stencil | True | medium |
| cf20 | action_event | depict |  |  | visual_action | action_event:depict | True | low |
| cf21 | event_role | depict | agent | artwork |  | event_role:depict:agent:artwork | True | medium |
| cf22 | event_role | depict | patient | man |  | event_role:depict:patient:man | True | medium |
| cf23 | action_event | surround |  |  | visual_action | action_event:surround | True | low |
| cf24 | event_role | surround | agent | man |  | event_role:surround:agent:man | True | medium |
| cf25 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf26 | event_role | stand | agent | pillar |  | event_role:stand:agent:pillar | True | medium |
| cf27 | relation | stencil | on | pillar | spatial_support, visual_relation | relation:stencil:on:pillar | True | high |
| cf28 | relation | man | in | hat | spatial_containment, visual_relation | relation:man:in:hat | True | high |
| cf29 | relation | man | in | collar | spatial_containment, visual_relation | relation:man:in:collar | True | high |
| cf30 | relation | man | by | circle | spatial_proximity, visual_relation | relation:man:by:circle | True | medium |
| cf31 | relation | pillar | next_to | alley | spatial_proximity, visual_relation | relation:pillar:next_to:alley | True | high |
| cf32 | relation | alley | with | wall | association_relation, visual_relation | relation:alley:with:wall | True | high |
| cf33 | relation | alley | with | beam | association_relation, visual_relation | relation:alley:with:beam | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e16 |  |  |  | {"canonical": "next_to", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e16", "raw_relation": "beside", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 35

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `17bb3cbac28bf54f3adf0a0392bde680a28bcd74014af96019175bcafd55a414`
**parse_path:** `sentence`

> A man with dark hair and a goatee wears a black shirt and makes a hand gesture with both hands. He has red nail polish, a silver chain necklace, and an earring, standing indoors near a wooden door and a colorful banner.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | hair | hair | noun_chunk_root | chunk1 | 4 | high |
| m2 | attribute | dark | dark | visual_attribute | chunk1 | 3 | medium |
| m3 | object | goatee | goatee | noun_chunk_root | chunk2 | 7 | high |
| m4 | object | shirt | shirt | noun_chunk_root | chunk3 | 11 | high |
| m5 | attribute | black | black | color_attribute | chunk3 | 10 | high |
| m6 | object | gesture | gesture | noun_chunk_root | chunk4 | 16 | high |
| m7 | attribute | hand | hand | compound_modifier | chunk4 | 15 | medium |
| m8 | object | hands | hand | noun_chunk_root | chunk5 | 19 | high |
| m9 | quantity | both | both | group_quantity | chunk5 | 18 | high |
| m10 | object | nail polish | nail_polish | noun_chunk_root | chunk7 | 24 | high |
| m11 | attribute | red | red | color_attribute | chunk7 | 23 | high |
| m12 | object | necklace | necklace | noun_chunk_root | chunk8 | 29 | high |
| m13 | attribute | silver | silver | color_attribute | chunk8 | 27 | high |
| m14 | attribute | chain | chain | compound_modifier | chunk8 | 28 | medium |
| m15 | object | earring | earring | noun_chunk_root | chunk9 | 33 | high |
| m16 | object | door | door | noun_chunk_root | chunk10 | 40 | high |
| m17 | attribute | wooden | wooden | material_attribute | chunk10 | 39 | high |
| m18 | object | banner | banner | noun_chunk_root | chunk11 | 44 | high |
| m19 | attribute | colorful | colorful | modifier_attribute | chunk11 | 43 | medium |
| m20 | context | indoors | indoors | scene_context | doc | 36 | high |
| m21 | action | wears | wear | verb_predicate | doc | 8 | high |
| m22 | action | makes | make | verb_predicate | doc | 13 | high |
| m23 | action | has | have | verb_predicate | doc | 22 | high |
| m24 | action | standing | stand | verb_predicate | doc | 35 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 amod -> hair |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> shirt |
| e2 | has_attribute | m6 | m7 | medium | chunk4 compound -> gesture |
| e3 | has_quantity | m8 | m9 | high | chunk5 quantity -> hands |
| e4 | has_attribute | m10 | m11 | high | chunk7 amod -> nail polish |
| e5 | has_attribute | m12 | m13 | high | chunk8 amod -> necklace |
| e6 | has_attribute | m12 | m14 | medium | chunk8 compound -> necklace |
| e7 | has_attribute | m16 | m17 | high | chunk10 amod -> door |
| e8 | has_attribute | m18 | m19 | medium | chunk11 amod -> banner |
| e9 | has_context | scene | m20 | high | scene_context token indoors |
| e10 | agent | m21 | m0 | medium | nsubj -> wears |
| e11 | patient | m21 | m4 | medium | dobj -> wears |
| e12 | agent | m22 | m0 | medium | inherited agent conj -> wears |
| e13 | patient | m22 | m6 | medium | dobj -> makes |
| e14 | agent | m23 | m0 | medium | nsubj -> has; resolved He -> man |
| e15 | patient | m23 | m10 | medium | dobj -> has |
| e16 | patient | m23 | m12 | medium | dobj -> has |
| e17 | patient | m23 | m15 | medium | dobj -> has |
| e18 | agent | m24 | m0 | medium | inherited agent advcl -> has |
| e19 | relation | m0 | m1 | high | with |
| e20 | relation | m0 | m3 | high | with |
| e21 | relation | m0 | m8 | high | with |
| e22 | relation | m0 | m16 | high | near |
| e23 | relation | m0 | m18 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | hair | hair | object | body_part | m1 | raw_mention |  |  |  | True | {"canonical": "entity:hair", "parents": ["entity_parent:body_part"]} |
| ent_m3 | object | goatee | goatee | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:goatee", "parents": []} |
| ent_m4 | object | shirt | shirt | clothing | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m6 | object | gesture | gesture | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:gesture", "parents": []} |
| ent_m8 | object | hand | hands | object | body_part | m8 | raw_mention |  |  |  | True | {"canonical": "entity:hand", "parents": ["entity_parent:body_part"]} |
| ent_m10 | object | nail_polish | nail polish | object |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:nail_polish", "parents": []} |
| ent_m12 | object | necklace | necklace | object |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:necklace", "parents": []} |
| ent_m15 | object | earring | earring | object |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:earring", "parents": []} |
| ent_m16 | object | door | door | object |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:door", "parents": []} |
| ent_m18 | object | banner | banner | object | text_carrier, artifact | m18 | raw_mention |  |  |  | True | {"canonical": "entity:banner", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m20 | context | indoors | indoors | object | scene_context | m20 | raw_mention |  |  |  | True | {"canonical": "entity:indoors", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m21 | wears | wear | wear | wearing_action, visual_action |  | agent:m0->ent_m0; patient:m4->ent_m4 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce1 | m22 | makes | make | make | visual_action |  | agent:m0->ent_m0; patient:m6->ent_m6 | {"canonical": "action:make", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m23 | has | have | have | visual_action |  | agent:m0->ent_m0; patient:m10->ent_m10; patient:m12->ent_m12; patient:m15->ent_m15 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m24 | standing | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | wear | agent | m0 | ent_m0 | medium | e10 | nsubj -> wears |  |  |
| ce0 | wear | patient | m4 | ent_m4 | medium | e11 | dobj -> wears |  |  |
| ce1 | make | agent | m0 | ent_m0 | medium | e12 | inherited agent conj -> wears |  |  |
| ce1 | make | patient | m6 | ent_m6 | medium | e13 | dobj -> makes |  |  |
| ce2 | have | agent | m0 | ent_m0 | medium | e14 | nsubj -> has; resolved He -> man |  |  |
| ce2 | have | patient | m10 | ent_m10 | medium | e15 | dobj -> has |  |  |
| ce2 | have | patient | m12 | ent_m12 | medium | e16 | dobj -> has |  |  |
| ce2 | have | patient | m15 | ent_m15 | medium | e17 | dobj -> has |  |  |
| ce3 | stand | agent | m0 | ent_m0 | medium | e18 | inherited agent advcl -> has |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | with | association_relation, visual_relation | high | e19 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | with | with | association_relation, visual_relation | high | e20 | False | False |  |  |
| cr2 | m0 | m8 | ent_m0 | ent_m8 | with | with | association_relation, visual_relation | high | e21 | False | False |  |  |
| cr3 | m0 | m16 | ent_m0 | ent_m16 | near | near | spatial_proximity, visual_relation | high | e22 | False | False |  |  |
| cr4 | m0 | m18 | ent_m0 | ent_m18 | near | near | spatial_proximity, visual_relation | high | e23 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | hair |  |  | body_part | entity_exists:hair | True | high |
| cf2 | entity_exists | goatee |  |  |  | entity_exists:goatee | True | low |
| cf3 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf4 | entity_exists | gesture |  |  |  | entity_exists:gesture | True | low |
| cf5 | entity_exists | hand |  |  | body_part | entity_exists:hand | True | high |
| cf6 | entity_exists | nail_polish |  |  |  | entity_exists:nail_polish | True | low |
| cf7 | entity_exists | necklace |  |  |  | entity_exists:necklace | True | low |
| cf8 | entity_exists | earring |  |  |  | entity_exists:earring | True | low |
| cf9 | entity_exists | door |  |  |  | entity_exists:door | True | low |
| cf10 | entity_exists | banner |  |  | text_carrier, artifact | entity_exists:banner | True | high |
| cf11 | entity_exists | indoors |  |  | scene_context | entity_exists:indoors | True | high |
| cf12 | has_attribute | hair | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:hair:dark | True | medium |
| cf13 | has_attribute | shirt | black |  | color_attribute, color, visual_attribute | has_attribute:shirt:black | True | high |
| cf14 | has_attribute | gesture | hand |  | compound_modifier, visual_attribute | has_attribute:gesture:hand | True | medium |
| cf15 | has_quantity | hand | both |  | group_quantity, quantity | has_quantity:hand:both | True | high |
| cf16 | has_attribute | nail_polish | red |  | color_attribute, color, visual_attribute | has_attribute:nail_polish:red | True | high |
| cf17 | has_attribute | necklace | silver |  | color_attribute, color, material, visual_attribute | has_attribute:necklace:silver | True | high |
| cf18 | has_attribute | necklace | chain |  | compound_modifier, visual_attribute | has_attribute:necklace:chain | True | medium |
| cf19 | has_attribute | door | wooden |  | material_attribute, material, visual_attribute | has_attribute:door:wooden | True | high |
| cf20 | has_attribute | banner | colorful |  | color_attribute, color_quantity, visual_attribute | has_attribute:banner:colorful | True | medium |
| cf21 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf22 | event_role | wear | agent | man |  | event_role:wear:agent:man | True | medium |
| cf23 | event_role | wear | patient | shirt |  | event_role:wear:patient:shirt | True | medium |
| cf24 | action_event | make |  |  | visual_action | action_event:make | True | low |
| cf25 | event_role | make | agent | man |  | event_role:make:agent:man | True | medium |
| cf26 | event_role | make | patient | gesture |  | event_role:make:patient:gesture | True | medium |
| cf27 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf28 | event_role | have | agent | man |  | event_role:have:agent:man | True | medium |
| cf29 | event_role | have | patient | nail_polish |  | event_role:have:patient:nail_polish | True | medium |
| cf30 | event_role | have | patient | necklace |  | event_role:have:patient:necklace | True | medium |
| cf31 | event_role | have | patient | earring |  | event_role:have:patient:earring | True | medium |
| cf32 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf33 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf34 | relation | man | with | hair | association_relation, visual_relation | relation:man:with:hair | True | high |
| cf35 | relation | man | with | goatee | association_relation, visual_relation | relation:man:with:goatee | True | high |
| cf36 | relation | man | with | hand | association_relation, visual_relation | relation:man:with:hand | True | high |
| cf37 | relation | man | near | door | spatial_proximity, visual_relation | relation:man:near:door | True | high |
| cf38 | relation | man | near | banner | spatial_proximity, visual_relation | relation:man:near:banner | True | high |

### Stage 9 Canonicalization Notes
_none_

## 36

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `1bd607b3ebbc9d4a0a56e7195d5cb8de4411b1fa93b2690f1555eb336d366814`
**parse_path:** `sentence`

> A large building with "P.J. HURPHY MOVING & STORAGE" sign stands beside a road, near tall smokestacks and power lines.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "P.J. HURPHY MOVING & STORAGE" | p.j._hurphy_moving_&_storage | quote_text | doc_quote | 4 | high |
| m1 | object | building | building | noun_chunk_root | chunk0 | 2 | high |
| m2 | attribute | large | large | size_attribute | chunk0 | 1 | high |
| m3 | object | sign | sign | noun_chunk_root | chunk1 | 5 | high |
| m4 | object | road | road | noun_chunk_root | chunk2 | 9 | high |
| m5 | object | smokestacks | smokestack | noun_chunk_root | chunk3 | 13 | high |
| m6 | attribute | tall | tall | size_attribute | chunk3 | 12 | high |
| m7 | object | power lines | power_line | noun_chunk_root | chunk4 | 15 | high |
| m8 | action | stands | stand | verb_predicate | doc | 6 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk0 amod -> building |
| e1 | has_attribute | m3 | m0 | high | chunk1 nmod -> sign |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> smokestacks |
| e3 | agent | m8 | m1 | medium | nsubj -> stands |
| e4 | relation | m1 | m3 | high | with |
| e5 | relation | m1 | m4 | high | beside |
| e6 | relation | m1 | m5 | high | near |
| e7 | relation | m1 | m7 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | building | building | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m3 | object | sign | sign | document | text_carrier, artifact | m3 | raw_mention |  |  |  | True | {"canonical": "entity:sign", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m4 | object | road | road | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:road", "parents": []} |
| ent_m5 | object | smokestack | smokestacks | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:smokestack", "parents": []} |
| ent_m7 | object | power_line | power lines | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:power_line", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | stands | stand | stand | body_pose_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m1 | ent_m1 | medium | e3 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m3 | ent_m1 | ent_m3 | with | with | association_relation, visual_relation | high | e4 | False | False |  |  |
| cr1 | m1 | m4 | ent_m1 | ent_m4 | beside | next_to | spatial_proximity, visual_relation | high | e5 | False | False |  |  |
| cr2 | m1 | m5 | ent_m1 | ent_m5 | near | near | spatial_proximity, visual_relation | high | e6 | False | False |  |  |
| cr3 | m1 | m7 | ent_m1 | ent_m7 | near | near | spatial_proximity, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf1 | entity_exists | sign |  |  | text_carrier, artifact | entity_exists:sign | True | high |
| cf2 | entity_exists | road |  |  |  | entity_exists:road | True | low |
| cf3 | entity_exists | smokestack |  |  |  | entity_exists:smokestack | True | low |
| cf4 | entity_exists | power_line |  |  |  | entity_exists:power_line | True | low |
| cf5 | has_attribute | building | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:building:large | True | high |
| cf6 | has_attribute | sign | p.j._hurphy_moving_&_storage |  | quote_text, visual_attribute | has_attribute:sign:p.j._hurphy_moving_&_storage | True | high |
| cf7 | has_attribute | smokestack | tall |  | size_attribute, height, visual_attribute | has_attribute:smokestack:tall | True | high |
| cf8 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf9 | event_role | stand | agent | building |  | event_role:stand:agent:building | True | medium |
| cf10 | relation | building | with | sign | association_relation, visual_relation | relation:building:with:sign | True | high |
| cf11 | relation | building | next_to | road | spatial_proximity, visual_relation | relation:building:next_to:road | True | high |
| cf12 | relation | building | near | smokestack | spatial_proximity, visual_relation | relation:building:near:smokestack | True | high |
| cf13 | relation | building | near | power_line | spatial_proximity, visual_relation | relation:building:near:power_line | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e5 |  |  |  | {"canonical": "next_to", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e5", "raw_relation": "beside", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 37

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `1c4fa5d0c6c46c6b268a9729dce637adb5c2e3c0167d2364feb3a039ba805414`
**parse_path:** `sentence`

> A narrow alleyway paved with bricks stretches between two tall brick walls. On the right, a bare tree stands near the end of the path, with houses visible beyond. Shadows stretch across the ground from the left wall.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | alleyway | alleyway | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | narrow | narrow | size_attribute | chunk0 | 1 | high |
| m2 | object | bricks | brick | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | walls | wall | noun_chunk_root | chunk2 | 11 | high |
| m4 | quantity | two | two | exact_quantity | chunk2 | 8 | high |
| m5 | attribute | tall | tall | size_attribute | chunk2 | 9 | high |
| m6 | attribute | brick | brick | material_attribute | chunk2 | 10 | high |
| m7 | context | right | right | spatial_region | chunk3 | 15 | medium |
| m8 | object | tree | tree | noun_chunk_root | chunk4 | 19 | high |
| m9 | attribute | bare | bare | visual_attribute | chunk4 | 18 | medium |
| m10 | object | path | path | noun_chunk_root | chunk6 | 26 | high |
| m11 | object | houses | house | noun_chunk_root | chunk7 | 29 | high |
| m12 | object | Shadows | shadow | noun_chunk_root | chunk8 | 33 | high |
| m13 | object | ground | ground | noun_chunk_root | chunk9 | 37 | high |
| m14 | object | wall | wall | noun_chunk_root | chunk10 | 41 | high |
| m15 | attribute | left | left | modifier_attribute | chunk10 | 40 | medium |
| m16 | action | paved | pave | verb_predicate | doc | 3 | high |
| m17 | action | stretches | stretch | verb_predicate | doc | 6 | high |
| m18 | action | stands | stand | verb_predicate | doc | 20 | high |
| m19 | action | stretch | stretch | verb_predicate | doc | 34 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> alleyway |
| e1 | has_quantity | m3 | m4 | high | chunk2 quantity -> walls |
| e2 | has_attribute | m3 | m5 | high | chunk2 amod -> walls |
| e3 | has_attribute | m3 | m6 | high | chunk2 compound -> walls |
| e4 | has_attribute | m8 | m9 | medium | chunk4 amod -> tree |
| e5 | has_attribute | m14 | m15 | medium | chunk10 amod -> wall |
| e6 | agent | m16 | m0 | medium | inherited agent acl -> alleyway |
| e7 | agent | m17 | m0 | medium | nsubj -> stretches |
| e8 | agent | m18 | m8 | medium | nsubj -> stands |
| e9 | agent | m19 | m12 | medium | nsubj -> stretch |
| e10 | relation | m0 | m2 | high | with |
| e11 | relation | m0 | m3 | high | between |
| e12 | relation | m8 | m7 | high | on |
| e13 | relation | m8 | m10 | medium | near_end_of |
| e14 | relation | m12 | m13 | high | across |
| e15 | relation | m12 | m14 | medium | from |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | alleyway | alleyway | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:alleyway", "parents": []} |
| ent_m2 | object | brick | bricks | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:brick", "parents": []} |
| ent_m3 | object | wall | walls | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |
| ent_m7 | context | right | right | object | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:right", "parents": ["entity_parent:scene_context"]} |
| ent_m8 | object | tree | tree | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m10 | object | path | path | object |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:path", "parents": []} |
| ent_m11 | object | house | houses | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:house", "parents": []} |
| ent_m12 | object | shadow | Shadows | object |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:shadow", "parents": []} |
| ent_m13 | object | ground | ground | object |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:ground", "parents": []} |
| ent_m14 | object | wall | wall | object |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | paved | pave | pave | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:pave", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m17 | stretches | stretch | stretch | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stretch", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m18 | stands | stand | stand | body_pose_action, visual_action |  | agent:m8->ent_m8 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce3 | m19 | stretch | stretch | stretch | visual_action |  | agent:m12->ent_m12 | {"canonical": "action:stretch", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | pave | agent | m0 | ent_m0 | medium | e6 | inherited agent acl -> alleyway |  |  |
| ce1 | stretch | agent | m0 | ent_m0 | medium | e7 | nsubj -> stretches |  |  |
| ce2 | stand | agent | m8 | ent_m8 | medium | e8 | nsubj -> stands |  |  |
| ce3 | stretch | agent | m12 | ent_m12 | medium | e9 | nsubj -> stretch |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e10 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | between | between | spatial_region, visual_relation | high | e11 | False | False |  |  |
| cr2 | m8 | m7 | ent_m8 | ent_m7 | on | on | spatial_support, visual_relation | high | e12 | False | False |  |  |
| cr3 | m8 | m10 | ent_m8 | ent_m10 | near_end_of | near_end_of | spatial_region, visual_relation | medium | e13 | False | False |  |  |
| cr4 | m12 | m13 | ent_m12 | ent_m13 | across | across | spatial_path, visual_relation | high | e14 | False | False |  |  |
| cr5 | m12 | m14 | ent_m12 | ent_m14 | from | from | visual_relation | medium | e15 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | alleyway |  |  |  | entity_exists:alleyway | True | low |
| cf1 | entity_exists | brick |  |  |  | entity_exists:brick | True | low |
| cf2 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf3 | entity_exists | right |  |  | scene_context | entity_exists:right | True | medium |
| cf4 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf5 | entity_exists | path |  |  |  | entity_exists:path | True | low |
| cf6 | entity_exists | house |  |  |  | entity_exists:house | True | low |
| cf7 | entity_exists | shadow |  |  |  | entity_exists:shadow | True | low |
| cf8 | entity_exists | ground |  |  |  | entity_exists:ground | True | low |
| cf9 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf10 | has_attribute | alleyway | narrow |  | size_attribute, width, visual_attribute | has_attribute:alleyway:narrow | True | high |
| cf11 | has_quantity | wall | two |  | exact_quantity, quantity | has_quantity:wall:two | True | high |
| cf12 | has_attribute | wall | tall |  | size_attribute, height, visual_attribute | has_attribute:wall:tall | True | high |
| cf13 | has_attribute | wall | brick |  | material_attribute, material, visual_attribute | has_attribute:wall:brick | True | high |
| cf14 | has_attribute | tree | bare |  | visual_attribute | has_attribute:tree:bare | True | medium |
| cf15 | has_attribute | wall | left |  | modifier_attribute, visual_attribute | has_attribute:wall:left | True | medium |
| cf16 | action_event | pave |  |  | visual_action | action_event:pave | True | low |
| cf17 | event_role | pave | agent | alleyway |  | event_role:pave:agent:alleyway | True | medium |
| cf18 | action_event | stretch |  |  | visual_action | action_event:stretch | True | low |
| cf19 | event_role | stretch | agent | alleyway |  | event_role:stretch:agent:alleyway | True | medium |
| cf20 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf21 | event_role | stand | agent | tree |  | event_role:stand:agent:tree | True | medium |
| cf22 | action_event | stretch |  |  | visual_action | action_event:stretch | True | low |
| cf23 | event_role | stretch | agent | shadow |  | event_role:stretch:agent:shadow | True | medium |
| cf24 | relation | alleyway | with | brick | association_relation, visual_relation | relation:alleyway:with:brick | True | high |
| cf25 | relation | alleyway | between | wall | spatial_region, visual_relation | relation:alleyway:between:wall | True | high |
| cf26 | relation | tree | on | right | spatial_support, visual_relation | relation:tree:on:right | True | high |
| cf27 | relation | tree | near_end_of | path | spatial_region, visual_relation | relation:tree:near_end_of:path | True | medium |
| cf28 | relation | shadow | across | ground | spatial_path, visual_relation | relation:shadow:across:ground | True | high |
| cf29 | relation | shadow | from | wall | visual_relation | relation:shadow:from:wall | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 38

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `219a6de5da69d0a3b9cee9914590eb7a70c6495c2e2aa659e88a3d3a4c4f0014`
**parse_path:** `sentence`

> A beige building with columns and a golden entrance is surrounded by tall palm trees. The structure sits on a green lawn under a clear blue sky, with shadows cast across the grass from the trees.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | beige | beige | color_attribute | chunk0 | 1 | high |
| m2 | object | columns | column | noun_chunk_root | chunk1 | 4 | high |
| m3 | object | entrance | entrance | noun_chunk_root | chunk2 | 8 | high |
| m4 | attribute | golden | golden | color_attribute | chunk2 | 7 | high |
| m5 | object | palm trees | palm_tree | noun_chunk_root | chunk3 | 13 | high |
| m6 | attribute | tall | tall | size_attribute | chunk3 | 12 | high |
| m8 | object | lawn | lawn | noun_chunk_root | chunk5 | 21 | high |
| m9 | attribute | green | green | color_attribute | chunk5 | 20 | high |
| m10 | object | sky | sky | noun_chunk_root | chunk6 | 26 | high |
| m11 | attribute | clear | clear | visual_attribute | chunk6 | 24 | medium |
| m12 | attribute | blue | blue | color_attribute | chunk6 | 25 | high |
| m13 | object | shadows | shadow | noun_chunk_root | chunk7 | 29 | high |
| m14 | object | grass | grass | noun_chunk_root | chunk8 | 33 | high |
| m15 | object | trees | tree | noun_chunk_root | chunk9 | 36 | high |
| m16 | reference | The structure | structure | generic_structure_reference | generic_anaphoric | 16 | high |
| m17 | action | surrounded | surround | verb_predicate | doc | 10 | high |
| m18 | action | sits | sit | verb_predicate | doc | 17 | high |
| m19 | action | cast | cast | verb_predicate | doc | 30 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> building |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> entrance |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> palm trees |
| e3 | has_attribute | m8 | m9 | high | chunk5 amod -> lawn |
| e4 | has_attribute | m10 | m11 | medium | chunk6 amod -> sky |
| e5 | has_attribute | m10 | m12 | high | chunk6 amod -> sky |
| e6 | refers_to | m16 | m0 | high | generic definite NP score=172 margin=93 |
| e7 | agent | m17 | m0 | medium | nsubjpass -> surrounded |
| e8 | agent | m18 | m0 | medium | nsubj -> sits; resolved structure -> building |
| e9 | agent | m19 | m13 | medium | inherited agent acl -> shadows |
| e10 | relation | m0 | m2 | high | with |
| e11 | relation | m0 | m3 | high | with |
| e12 | relation | m0 | m5 | medium | by |
| e13 | relation | m0 | m8 | high | on |
| e14 | relation | m0 | m10 | high | under |
| e15 | relation | m0 | m13 | high | with |
| e16 | relation | m13 | m14 | high | across |
| e17 | relation | m13 | m15 | medium | from |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | building | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m2 | object | column | columns | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:column", "parents": []} |
| ent_m3 | object | entrance | entrance | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:entrance", "parents": []} |
| ent_m5 | object | palm_tree | palm trees | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:palm_tree", "parents": []} |
| ent_m8 | object | lawn | lawn | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:lawn", "parents": []} |
| ent_m10 | object | sky | sky | object |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m13 | object | shadow | shadows | object |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:shadow", "parents": []} |
| ent_m14 | object | grass | grass | object |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": []} |
| ent_m15 | object | tree | trees | object |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| eref_m16 | reference | building | The structure | object |  | m16 | stage9_reference | ent_m0 |  |  | True | {"canonical": "entity:building", "parents": []} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m16 | eref_m16 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | surrounded | surround | surround | visual_action |  | theme:m0->ent_m0; by_agent_or_causer:m5->ent_m5 | {"canonical": "action:surround", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m18 | sits | sit | sit | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce2 | m19 | cast | cast | cast | visual_action |  | agent:m13->ent_m13 | {"canonical": "action:cast", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | surround | theme | m0 | ent_m0 | medium | e7 | nsubjpass -> surrounded |  |  |
| ce0 | surround | by_agent_or_causer | m5 | ent_m5 | medium | e12 | passive by-frame |  |  |
| ce1 | sit | agent | m0 | ent_m0 | medium | e8 | nsubj -> sits; resolved structure -> building |  |  |
| ce2 | cast | agent | m13 | ent_m13 | medium | e9 | inherited agent acl -> shadows |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e10 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | with | with | association_relation, visual_relation | high | e11 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | by | by | spatial_proximity, visual_relation | medium | e12 | True | False |  |  |
| cr3 | m0 | m8 | ent_m0 | ent_m8 | on | on | spatial_support, visual_relation | high | e13 | False | False |  |  |
| cr4 | m0 | m10 | ent_m0 | ent_m10 | under | under | spatial_vertical, visual_relation | high | e14 | False | False |  |  |
| cr5 | m0 | m13 | ent_m0 | ent_m13 | with | with | association_relation, visual_relation | high | e15 | False | False |  |  |
| cr6 | m13 | m14 | ent_m13 | ent_m14 | across | across | spatial_path, visual_relation | high | e16 | False | False |  |  |
| cr7 | m13 | m15 | ent_m13 | ent_m15 | from | from | visual_relation | medium | e17 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf1 | entity_exists | column |  |  |  | entity_exists:column | True | low |
| cf2 | entity_exists | entrance |  |  |  | entity_exists:entrance | True | low |
| cf3 | entity_exists | palm_tree |  |  |  | entity_exists:palm_tree | True | low |
| cf4 | entity_exists | lawn |  |  |  | entity_exists:lawn | True | low |
| cf5 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf6 | entity_exists | shadow |  |  |  | entity_exists:shadow | True | low |
| cf7 | entity_exists | grass |  |  |  | entity_exists:grass | True | low |
| cf8 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf9 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf10 | has_attribute | building | beige |  | color_attribute, color, visual_attribute | has_attribute:building:beige | True | high |
| cf11 | has_attribute | entrance | golden |  | color_attribute, color, visual_attribute | has_attribute:entrance:golden | True | high |
| cf12 | has_attribute | palm_tree | tall |  | size_attribute, height, visual_attribute | has_attribute:palm_tree:tall | True | high |
| cf13 | has_attribute | lawn | green |  | color_attribute, color, visual_attribute | has_attribute:lawn:green | True | high |
| cf14 | has_attribute | sky | clear |  | weather_attribute, opaqeness, weather, visual_attribute | has_attribute:sky:clear | True | medium |
| cf15 | has_attribute | sky | blue |  | color_attribute, color, visual_attribute | has_attribute:sky:blue | True | high |
| cf16 | action_event | surround |  |  | visual_action | action_event:surround | True | low |
| cf17 | event_role | surround | theme | building |  | event_role:surround:theme:building | True | medium |
| cf18 | event_role | surround | by_agent_or_causer | palm_tree |  | event_role:surround:by_agent_or_causer:palm_tree | True | medium |
| cf19 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf20 | event_role | sit | agent | building |  | event_role:sit:agent:building | True | medium |
| cf21 | action_event | cast |  |  | visual_action | action_event:cast | True | low |
| cf22 | event_role | cast | agent | shadow |  | event_role:cast:agent:shadow | True | medium |
| cf23 | relation | building | with | column | association_relation, visual_relation | relation:building:with:column | True | high |
| cf24 | relation | building | with | entrance | association_relation, visual_relation | relation:building:with:entrance | True | high |
| cf25 | relation | building | by | palm_tree | spatial_proximity, visual_relation | relation:building:by:palm_tree | False | medium |
| cf26 | relation | building | on | lawn | spatial_support, visual_relation | relation:building:on:lawn | True | high |
| cf27 | relation | building | under | sky | spatial_vertical, visual_relation | relation:building:under:sky | True | high |
| cf28 | relation | building | with | shadow | association_relation, visual_relation | relation:building:with:shadow | True | high |
| cf29 | relation | shadow | across | grass | spatial_path, visual_relation | relation:shadow:across:grass | True | high |
| cf30 | relation | shadow | from | tree | visual_relation | relation:shadow:from:tree | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m17 | e7 | m0 |  |  | {"action_mention_id": "m17", "kind": "passive_subject_to_theme", "raw_edge_id": "e7", "target": "m0"} |
| passive_by_frame_to_event_role | m17 | e12 |  |  |  | {"action_mention_id": "m17", "by_agent_or_causer": "m5", "kind": "passive_by_frame_to_event_role", "raw_edge_id": "e12", "theme": "m0"} |

## 39

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `21f64d6e3be344388d8ed0dc49bd94c22a5ba9c555a96cdfc624524854997c14`
**parse_path:** `sentence`

> A tall glass of latte macchiato sits on a wooden table, topped with foam and resting on a black tray with a doily. A spoon and sugar packet are beside it, with a blurred outdoor background showing rocks and greenery.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | glass | glass | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | tall | tall | size_attribute | chunk0 | 1 | high |
| m2 | object | macchiato | macchiato | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | latte | latte | compound_modifier | chunk1 | 4 | medium |
| m4 | object | table | table | noun_chunk_root | chunk2 | 10 | high |
| m5 | attribute | wooden | wooden | material_attribute | chunk2 | 9 | high |
| m6 | object | foam | foam | noun_chunk_root | chunk3 | 14 | high |
| m7 | object | tray | tray | noun_chunk_root | chunk4 | 20 | high |
| m8 | attribute | black | black | color_attribute | chunk4 | 19 | high |
| m9 | object | doily | doily | noun_chunk_root | chunk5 | 23 | high |
| m10 | object | spoon | spoon | noun_chunk_root | chunk6 | 26 | high |
| m11 | object | packet | packet | noun_chunk_root | chunk7 | 29 | high |
| m12 | attribute | sugar | sugar | compound_modifier | chunk7 | 28 | medium |
| m13 | context | background | background | scene_context | chunk9 | 38 | high |
| m14 | attribute | blurred | blurred | modifier_attribute | chunk9 | 36 | medium |
| m15 | attribute | outdoor | outdoor | modifier_attribute | chunk9 | 37 | medium |
| m16 | object | rocks | rock | noun_chunk_root | chunk10 | 40 | high |
| m17 | object | greenery | greenery | noun_chunk_root | chunk11 | 42 | high |
| m18 | action | sits | sit | verb_predicate | doc | 6 | high |
| m19 | action | topped | top | verb_predicate | doc | 12 | high |
| m20 | action | resting | rest | verb_predicate | doc | 16 | high |
| m21 | action | showing | show | verb_predicate | doc | 39 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> glass |
| e1 | has_attribute | m2 | m3 | medium | chunk1 compound -> macchiato |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> table |
| e3 | has_attribute | m7 | m8 | high | chunk4 amod -> tray |
| e4 | has_attribute | m11 | m12 | medium | chunk7 compound -> packet |
| e5 | has_context | scene | m13 | high | scene_context token background |
| e6 | has_attribute | m13 | m14 | medium | chunk9 amod -> background |
| e7 | has_attribute | m13 | m15 | medium | chunk9 amod -> background |
| e8 | agent | m18 | m0 | medium | nsubj -> sits |
| e9 | agent | m19 | m0 | medium | inherited agent advcl -> sits |
| e10 | agent | m20 | m0 | medium | inherited agent conj -> topped |
| e11 | agent | m21 | m13 | medium | nsubj -> showing |
| e12 | patient | m21 | m16 | medium | dobj -> showing |
| e13 | patient | m21 | m17 | medium | dobj -> showing |
| e14 | relation | m0 | m2 | medium | of |
| e15 | relation | m0 | m4 | high | on |
| e16 | relation | m0 | m6 | high | with |
| e17 | relation | m7 | m9 | high | with |

### Skipped Raw Concept Edges
| type | source | target | confidence | reason | evidence |
| --- | --- | --- | --- | --- | --- |
| relation | m10 | m10 | high | self_edge_after_coref | beside |

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | glass | glass | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:glass", "parents": []} |
| ent_m2 | object | macchiato | macchiato | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:macchiato", "parents": []} |
| ent_m4 | object | table | table | object | furniture, artifact | m4 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m6 | object | foam | foam | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:foam", "parents": []} |
| ent_m7 | object | tray | tray | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:tray", "parents": []} |
| ent_m9 | object | doily | doily | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:doily", "parents": []} |
| ent_m10 | object | spoon | spoon | object |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:spoon", "parents": []} |
| ent_m11 | object | packet | packet | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:packet", "parents": []} |
| ent_m13 | context | background | background | object | scene_context | m13 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m16 | object | rock | rocks | object |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:rock", "parents": []} |
| ent_m17 | object | greenery | greenery | object |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:greenery", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | sits | sit | sit | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m19 | topped | top | top | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:top", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m20 | resting | rest | rest | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:rest", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m21 | showing | show | show | visual_action |  | agent:m13->ent_m13; patient:m16->ent_m16; patient:m17->ent_m17 | {"canonical": "action:show", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m0 | ent_m0 | medium | e8 | nsubj -> sits |  |  |
| ce1 | top | agent | m0 | ent_m0 | medium | e9 | inherited agent advcl -> sits |  |  |
| ce2 | rest | agent | m0 | ent_m0 | medium | e10 | inherited agent conj -> topped |  |  |
| ce3 | show | agent | m13 | ent_m13 | medium | e11 | nsubj -> showing |  |  |
| ce3 | show | patient | m16 | ent_m16 | medium | e12 | dobj -> showing |  |  |
| ce3 | show | patient | m17 | ent_m17 | medium | e13 | dobj -> showing |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | of | of | part_relation, visual_relation | medium | e14 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | on | spatial_support, visual_relation | high | e15 | False | False |  |  |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | with | with | association_relation, visual_relation | high | e16 | False | False |  |  |
| cr3 | m7 | m9 | ent_m7 | ent_m9 | with | with | association_relation, visual_relation | high | e17 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | glass |  |  |  | entity_exists:glass | True | low |
| cf1 | entity_exists | macchiato |  |  |  | entity_exists:macchiato | True | low |
| cf2 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf3 | entity_exists | foam |  |  |  | entity_exists:foam | True | low |
| cf4 | entity_exists | tray |  |  |  | entity_exists:tray | True | low |
| cf5 | entity_exists | doily |  |  |  | entity_exists:doily | True | low |
| cf6 | entity_exists | spoon |  |  |  | entity_exists:spoon | True | low |
| cf7 | entity_exists | packet |  |  |  | entity_exists:packet | True | low |
| cf8 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf9 | entity_exists | rock |  |  |  | entity_exists:rock | True | low |
| cf10 | entity_exists | greenery |  |  |  | entity_exists:greenery | True | low |
| cf11 | has_attribute | glass | tall |  | size_attribute, height, visual_attribute | has_attribute:glass:tall | True | high |
| cf12 | has_attribute | macchiato | latte |  | compound_modifier, visual_attribute | has_attribute:macchiato:latte | True | medium |
| cf13 | has_attribute | table | wooden |  | material_attribute, material, visual_attribute | has_attribute:table:wooden | True | high |
| cf14 | has_attribute | tray | black |  | color_attribute, color, visual_attribute | has_attribute:tray:black | True | high |
| cf15 | has_attribute | packet | sugar |  | compound_modifier, visual_attribute | has_attribute:packet:sugar | True | medium |
| cf16 | has_attribute | background | blurred |  | modifier_attribute, visual_attribute | has_attribute:background:blurred | True | medium |
| cf17 | has_attribute | background | outdoor |  | modifier_attribute, visual_attribute | has_attribute:background:outdoor | True | medium |
| cf18 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf19 | event_role | sit | agent | glass |  | event_role:sit:agent:glass | True | medium |
| cf20 | action_event | top |  |  | visual_action | action_event:top | True | low |
| cf21 | event_role | top | agent | glass |  | event_role:top:agent:glass | True | medium |
| cf22 | action_event | rest |  |  | visual_action | action_event:rest | True | low |
| cf23 | event_role | rest | agent | glass |  | event_role:rest:agent:glass | True | medium |
| cf24 | action_event | show |  |  | visual_action | action_event:show | True | low |
| cf25 | event_role | show | agent | background |  | event_role:show:agent:background | True | medium |
| cf26 | event_role | show | patient | rock |  | event_role:show:patient:rock | True | medium |
| cf27 | event_role | show | patient | greenery |  | event_role:show:patient:greenery | True | medium |
| cf28 | relation | glass | of | macchiato | part_relation, visual_relation | relation:glass:of:macchiato | True | medium |
| cf29 | relation | glass | on | table | spatial_support, visual_relation | relation:glass:on:table | True | high |
| cf30 | relation | glass | with | foam | association_relation, visual_relation | relation:glass:with:foam | True | high |
| cf31 | relation | tray | with | doily | association_relation, visual_relation | relation:tray:with:doily | True | high |

### Stage 9 Canonicalization Notes
_none_

## 40

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `2287af524065dd30ea7e24c23568f4ad086da9db7aa0bc9e9be343f573a60c14`
**parse_path:** `sentence`

> A curved brick building with large windows stands on a paved lot. Several cars, including a red one, are parked nearby under a bright sky, with trees and other buildings visible in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | noun_chunk_root | chunk0 | 3 | high |
| m1 | attribute | curved | curved | modifier_attribute | chunk0 | 1 | medium |
| m2 | attribute | brick | brick | material_attribute | chunk0 | 2 | high |
| m3 | object | windows | window | noun_chunk_root | chunk1 | 6 | high |
| m4 | attribute | large | large | size_attribute | chunk1 | 5 | high |
| m5 | object | lot | lot | noun_chunk_root | chunk2 | 11 | high |
| m6 | attribute | paved | paved | visual_attribute | chunk2 | 10 | medium |
| m7 | object | cars | car | noun_chunk_root | chunk3 | 14 | high |
| m8 | quantity | Several | several | approximate_quantity | chunk3 | 13 | medium |
| m9 | object | sky | sky | noun_chunk_root | chunk4 | 27 | high |
| m10 | attribute | bright | bright | visual_attribute | chunk4 | 26 | medium |
| m11 | object | trees | tree | noun_chunk_root | chunk5 | 30 | high |
| m12 | object | buildings | building | noun_chunk_root | chunk6 | 33 | high |
| m13 | attribute | other | other | modifier_attribute | chunk6 | 32 | medium |
| m14 | context | background | background | scene_context | chunk7 | 37 | high |
| m15 | reference | one | one | singular_substitute | nominal_reference | 19 | high |
| m16 | object | red car | car | nominal_reference_instance | nominal_reference | 19 | high |
| m17 | attribute | red | red | color_attribute | nominal_reference | 18 | high |
| m18 | action | stands | stand | verb_predicate | doc | 7 | high |
| m19 | action | including | include | verb_predicate | doc | 16 | high |
| m20 | action | parked | park | verb_predicate | doc | 22 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> building |
| e1 | has_attribute | m0 | m2 | high | chunk0 compound -> building |
| e2 | has_attribute | m3 | m4 | high | chunk1 amod -> windows |
| e3 | has_attribute | m5 | m6 | medium | chunk2 amod -> lot |
| e4 | has_quantity | m7 | m8 | medium | chunk3 quantity -> cars |
| e5 | has_attribute | m9 | m10 | medium | chunk4 amod -> sky |
| e6 | has_attribute | m12 | m13 | medium | chunk6 amod -> buildings |
| e7 | has_context | scene | m14 | high | scene_context token background |
| e8 | refers_to | m15 | m7 | high | singular_substitute one -> cars; score=111; margin=21 |
| e9 | derived_from | m16 | m7 | high | singular_substitute one -> cars; score=111; margin=21 |
| e10 | has_attribute | m16 | m17 | high | nominal_reference amod -> one; singular_substitute one -> cars; score=111; margin=21 |
| e11 | agent | m18 | m0 | medium | nsubj -> stands |
| e12 | agent | m19 | m7 | medium | inherited agent prep -> cars |
| e13 | patient | m19 | m16 | medium | pobj -> including; resolved one -> red car |
| e14 | agent | m20 | m7 | medium | nsubjpass -> parked |
| e15 | relation | m0 | m3 | high | with |
| e16 | relation | m0 | m5 | high | on |
| e17 | relation | m7 | m16 | medium | include |
| e18 | relation | m7 | m9 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | building | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m3 | object | window | windows | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:window", "parents": []} |
| ent_m5 | object | lot | lot | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:lot", "parents": []} |
| ent_m7 | object | car | cars | vehicle | vehicle | m7 | raw_mention |  |  |  | True | {"canonical": "entity:car", "parents": ["entity_parent:vehicle"]} |
| ent_m9 | object | sky | sky | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m11 | object | tree | trees | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m12 | object | building | buildings | object |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m14 | context | background | background | object | scene_context | m14 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m16 | object | car | red car | vehicle | vehicle | m16 | raw_mention |  |  |  | True | {"canonical": "entity:car", "parents": ["entity_parent:vehicle"]} |
| eref_m15 | instance | car | one | vehicle | vehicle | m15 | stage9_reference | ent_m7 |  | 1 | True | {"canonical": "entity:car", "parents": ["entity_parent:vehicle"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m15 | eref_m15 | m7 | ent_m7 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | stands | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m19 | including | include | include | visual_action |  | agent:m7->ent_m7; patient:m16->ent_m16 | {"canonical": "action:include", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m20 | parked | park | park | visual_action |  | theme:m7->ent_m7 | {"canonical": "action:park", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e11 | nsubj -> stands |  |  |
| ce1 | include | agent | m7 | ent_m7 | medium | e12 | inherited agent prep -> cars |  |  |
| ce1 | include | patient | m16 | ent_m16 | medium | e13 | pobj -> including; resolved one -> red car |  |  |
| ce2 | park | theme | m7 | ent_m7 | medium | e14 | nsubjpass -> parked |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | with | with | association_relation, visual_relation | high | e15 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | on | spatial_support, visual_relation | high | e16 | False | False |  |  |
| cr2 | m7 | m16 | ent_m7 | ent_m16 | include | include | visual_relation | medium | e17 | False | False |  |  |
| cr3 | m7 | m9 | ent_m7 | ent_m9 | under | under | spatial_vertical, visual_relation | high | e18 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf1 | entity_exists | window |  |  |  | entity_exists:window | True | low |
| cf2 | entity_exists | lot |  |  |  | entity_exists:lot | True | low |
| cf3 | entity_exists | car |  |  | vehicle | entity_exists:car | True | high |
| cf4 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf5 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf6 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf7 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf8 | entity_exists | car |  |  | vehicle | entity_exists:car | True | high |
| cf9 | entity_exists | car |  |  | vehicle | entity_exists:car | True | high |
| cf10 | has_attribute | building | curved |  | shape_attribute, clean_exact_overlap, shape, visual_attribute | has_attribute:building:curved | True | medium |
| cf11 | has_attribute | building | brick |  | material_attribute, material, visual_attribute | has_attribute:building:brick | True | high |
| cf12 | has_attribute | window | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:window:large | True | high |
| cf13 | has_attribute | lot | paved |  | visual_attribute | has_attribute:lot:paved | True | medium |
| cf14 | has_quantity | car | several |  | approximate_quantity, quantity | has_quantity:car:several | True | medium |
| cf15 | has_attribute | sky | bright |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:sky:bright | True | medium |
| cf16 | has_attribute | building | other |  | modifier_attribute, visual_attribute | has_attribute:building:other | True | medium |
| cf17 | has_attribute | car | red |  | color_attribute, color, visual_attribute | has_attribute:car:red | True | high |
| cf18 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf19 | event_role | stand | agent | building |  | event_role:stand:agent:building | True | medium |
| cf20 | action_event | include |  |  | visual_action | action_event:include | True | low |
| cf21 | event_role | include | agent | car |  | event_role:include:agent:car | True | medium |
| cf22 | event_role | include | patient | car |  | event_role:include:patient:car | True | medium |
| cf23 | action_event | park |  |  | visual_action | action_event:park | True | low |
| cf24 | event_role | park | theme | car |  | event_role:park:theme:car | True | medium |
| cf25 | relation | building | with | window | association_relation, visual_relation | relation:building:with:window | True | high |
| cf26 | relation | building | on | lot | spatial_support, visual_relation | relation:building:on:lot | True | high |
| cf27 | relation | car | include | car | visual_relation | relation:car:include:car | True | medium |
| cf28 | relation | car | under | sky | spatial_vertical, visual_relation | relation:car:under:sky | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m20 | e14 | m7 |  |  | {"action_mention_id": "m20", "kind": "passive_subject_to_theme", "raw_edge_id": "e14", "target": "m7"} |

## 41

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `22d73ce6e1983f13f62e0e06d5dac7795e38f3c9f1ff1a64409ea01ab45f4814`
**parse_path:** `sentence`

> A man in a blue shirt plays an acoustic guitar while singing into a microphone. He stands on a stage with black curtains behind him and a keyboard visible to his right.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | shirt | shirt | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | blue | blue | color_attribute | chunk1 | 4 | high |
| m3 | object | acoustic guitar | acoustic_guitar | noun_chunk_root | chunk2 | 8 | high |
| m4 | object | microphone | microphone | noun_chunk_root | chunk3 | 13 | high |
| m5 | object | stage | stage | noun_chunk_root | chunk5 | 19 | high |
| m6 | object | curtains | curtain | noun_chunk_root | chunk6 | 22 | high |
| m7 | attribute | black | black | color_attribute | chunk6 | 21 | high |
| m8 | object | keyboard | keyboard | noun_chunk_root | chunk8 | 27 | high |
| m9 | context | right | right | spatial_region | chunk9 | 31 | medium |
| m10 | action | plays | play | verb_predicate | doc | 6 | high |
| m11 | action | singing | sing | verb_predicate | doc | 10 | high |
| m12 | action | stands | stand | verb_predicate | doc | 16 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> shirt |
| e1 | has_attribute | m6 | m7 | high | chunk6 amod -> curtains |
| e2 | agent | m10 | m0 | medium | nsubj -> plays |
| e3 | patient | m10 | m3 | medium | dobj -> plays |
| e4 | agent | m11 | m0 | medium | inherited agent advcl -> plays |
| e5 | agent | m12 | m0 | medium | nsubj -> stands; resolved He -> man |
| e6 | relation | m0 | m1 | high | in |
| e7 | relation | m0 | m4 | medium | into |
| e8 | relation | m0 | m5 | high | on |
| e9 | relation | m0 | m6 | high | with |
| e10 | relation | m0 | m8 | high | with |
| e11 | relation | m6 | m0 | high | behind |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | shirt | shirt | clothing | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | acoustic_guitar | acoustic guitar | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:acoustic_guitar", "parents": []} |
| ent_m4 | object | microphone | microphone | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:microphone", "parents": []} |
| ent_m5 | object | stage | stage | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:stage", "parents": []} |
| ent_m6 | object | curtain | curtains | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:curtain", "parents": []} |
| ent_m8 | object | keyboard | keyboard | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:keyboard", "parents": []} |
| ent_m9 | context | right | right | object | scene_context | m9 | raw_mention |  |  |  | True | {"canonical": "entity:right", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | plays | play | play | activity_action, visual_action |  | agent:m0->ent_m0; patient:m3->ent_m3 | {"canonical": "action:play", "parents": ["action_parent:activity_action", "action_parent:visual_action"]} |  |
| ce1 | m11 | singing | sing | sing | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sing", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m12 | stands | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | play | agent | m0 | ent_m0 | medium | e2 | nsubj -> plays |  |  |
| ce0 | play | patient | m3 | ent_m3 | medium | e3 | dobj -> plays |  |  |
| ce1 | sing | agent | m0 | ent_m0 | medium | e4 | inherited agent advcl -> plays |  |  |
| ce2 | stand | agent | m0 | ent_m0 | medium | e5 | nsubj -> stands; resolved He -> man |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | spatial_containment, visual_relation | high | e6 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | into | into | visual_relation | medium | e7 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | on | on | spatial_support, visual_relation | high | e8 | False | False |  |  |
| cr3 | m0 | m6 | ent_m0 | ent_m6 | with | with | association_relation, visual_relation | high | e9 | False | False |  |  |
| cr4 | m0 | m8 | ent_m0 | ent_m8 | with | with | association_relation, visual_relation | high | e10 | False | False |  |  |
| cr5 | m6 | m0 | ent_m6 | ent_m0 | behind | behind | spatial_depth, visual_relation | high | e11 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf2 | entity_exists | acoustic_guitar |  |  |  | entity_exists:acoustic_guitar | True | low |
| cf3 | entity_exists | microphone |  |  |  | entity_exists:microphone | True | low |
| cf4 | entity_exists | stage |  |  |  | entity_exists:stage | True | low |
| cf5 | entity_exists | curtain |  |  |  | entity_exists:curtain | True | low |
| cf6 | entity_exists | keyboard |  |  |  | entity_exists:keyboard | True | low |
| cf7 | entity_exists | right |  |  | scene_context | entity_exists:right | True | medium |
| cf8 | has_attribute | shirt | blue |  | color_attribute, color, visual_attribute | has_attribute:shirt:blue | True | high |
| cf9 | has_attribute | curtain | black |  | color_attribute, color, visual_attribute | has_attribute:curtain:black | True | high |
| cf10 | action_event | play |  |  | activity_action, visual_action | action_event:play | True | high |
| cf11 | event_role | play | agent | man |  | event_role:play:agent:man | True | medium |
| cf12 | event_role | play | patient | acoustic_guitar |  | event_role:play:patient:acoustic_guitar | True | medium |
| cf13 | action_event | sing |  |  | visual_action | action_event:sing | True | low |
| cf14 | event_role | sing | agent | man |  | event_role:sing:agent:man | True | medium |
| cf15 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf16 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf17 | relation | man | in | shirt | spatial_containment, visual_relation | relation:man:in:shirt | True | high |
| cf18 | relation | man | into | microphone | visual_relation | relation:man:into:microphone | True | medium |
| cf19 | relation | man | on | stage | spatial_support, visual_relation | relation:man:on:stage | True | high |
| cf20 | relation | man | with | curtain | association_relation, visual_relation | relation:man:with:curtain | True | high |
| cf21 | relation | man | with | keyboard | association_relation, visual_relation | relation:man:with:keyboard | True | high |
| cf22 | relation | curtain | behind | man | spatial_depth, visual_relation | relation:curtain:behind:man | True | high |

### Stage 9 Canonicalization Notes
_none_

## 42

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `24f96a09612e1e5fdd421dc7fc39eeb0c8aaf431c50ed9152c49237f7f98bc14`
**parse_path:** `sentence`

> Large rusted metal pipes run diagonally across the frame under a blue sky. Below, green construction fencing and steel rebar are visible, with workers and equipment in the distance. The scene is an outdoor construction site with exposed concrete walls and structural beams.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | pipes | pipe | noun_chunk_root | chunk0 | 3 | high |
| m1 | attribute | Large | large | size_attribute | chunk0 | 0 | high |
| m2 | attribute | rusted | rusted | modifier_attribute | chunk0 | 1 | medium |
| m3 | attribute | metal | metal | material_attribute | chunk0 | 2 | high |
| m4 | object | frame | frame | noun_chunk_root | chunk1 | 8 | high |
| m5 | object | sky | sky | noun_chunk_root | chunk2 | 12 | high |
| m6 | attribute | blue | blue | color_attribute | chunk2 | 11 | high |
| m7 | object | fencing | fencing | noun_chunk_root | chunk3 | 18 | high |
| m8 | attribute | green | green | color_attribute | chunk3 | 16 | high |
| m9 | attribute | construction | construction | compound_modifier | chunk3 | 17 | medium |
| m10 | object | rebar | rebar | noun_chunk_root | chunk4 | 21 | high |
| m11 | attribute | steel | steel | material_attribute | chunk4 | 20 | high |
| m12 | context | distance | distance | scene_context | chunk5 | 31 | high |
| m13 | context | scene | scene | scene_context | chunk6 | 34 | high |
| m14 | object | site | site | noun_chunk_root | chunk7 | 39 | high |
| m15 | attribute | outdoor | outdoor | modifier_attribute | chunk7 | 37 | medium |
| m16 | attribute | construction | construction | compound_modifier | chunk7 | 38 | medium |
| m17 | object | walls | wall | noun_chunk_root | chunk8 | 43 | high |
| m18 | attribute | exposed | expose | state_attribute | chunk8 | 41 | medium |
| m19 | attribute | concrete | concrete | material_attribute | chunk8 | 42 | high |
| m20 | object | beams | beam | noun_chunk_root | chunk9 | 46 | high |
| m21 | attribute | structural | structural | modifier_attribute | chunk9 | 45 | medium |
| m22 | action | run | run | verb_predicate | doc | 4 | high |
| m23 | object | workers | worker | with_absolute_recovered_object | with_absolute25 | 26 | medium |
| m24 | object | equipment | equipment | with_absolute_recovered_object | with_absolute25 | 28 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> pipes |
| e1 | has_attribute | m0 | m2 | medium | chunk0 amod -> pipes |
| e2 | has_attribute | m0 | m3 | high | chunk0 compound -> pipes |
| e3 | has_attribute | m5 | m6 | high | chunk2 amod -> sky |
| e4 | has_attribute | m7 | m8 | high | chunk3 amod -> fencing |
| e5 | has_attribute | m7 | m9 | medium | chunk3 compound -> fencing |
| e6 | has_attribute | m10 | m11 | high | chunk4 compound -> rebar |
| e7 | has_context | scene | m12 | high | scene_context token distance |
| e8 | has_context | scene | m13 | high | scene_context token scene |
| e9 | has_attribute | m14 | m15 | medium | chunk7 amod -> site |
| e10 | has_attribute | m14 | m16 | medium | chunk7 compound -> site |
| e11 | has_attribute | m17 | m18 | medium | chunk8 amod -> walls |
| e12 | has_attribute | m17 | m19 | high | chunk8 amod -> walls |
| e13 | has_attribute | m20 | m21 | medium | chunk9 amod -> beams |
| e14 | agent | m22 | m0 | medium | nsubj -> run |
| e15 | scene_contains | scene | m23 | medium | with_absolute25 recovered workers |
| e16 | scene_contains | scene | m24 | medium | with_absolute25 recovered equipment |
| e17 | relation | m0 | m4 | high | across |
| e18 | relation | m0 | m5 | high | under |
| e19 | relation | m23 | m12 | high | in |
| e20 | relation | m14 | m17 | high | with |
| e21 | relation | m14 | m20 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | pipe | pipes | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:pipe", "parents": []} |
| ent_m4 | object | frame | frame | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:frame", "parents": []} |
| ent_m5 | object | sky | sky | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m7 | object | fencing | fencing | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:fencing", "parents": []} |
| ent_m10 | object | rebar | rebar | object |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:rebar", "parents": []} |
| ent_m12 | context | distance | distance | object | scene_context, spatial_context | m12 | raw_mention |  |  |  | True | {"canonical": "entity:distance", "parents": ["entity_parent:scene_context", "entity_parent:spatial_context"]} |
| ent_m13 | context | scene | scene | object | scene_context | m13 | raw_mention |  |  |  | True | {"canonical": "entity:scene", "parents": ["entity_parent:scene_context"]} |
| ent_m14 | object | site | site | object |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:site", "parents": []} |
| ent_m17 | object | wall | walls | object |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |
| ent_m20 | object | beam | beams | object |  | m20 | raw_mention |  |  |  | True | {"canonical": "entity:beam", "parents": []} |
| ent_m23 | object | worker | workers | object |  | m23 | raw_mention |  |  |  | True | {"canonical": "entity:worker", "parents": []} |
| ent_m24 | object | equipment | equipment | object |  | m24 | raw_mention |  |  |  | True | {"canonical": "entity:equipment", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m22 | run | run | run | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:run", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | run | agent | m0 | ent_m0 | medium | e14 | nsubj -> run |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | across | across | spatial_path, visual_relation | high | e17 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | under | under | spatial_vertical, visual_relation | high | e18 | False | False |  |  |
| cr2 | m23 | m12 | ent_m23 | ent_m12 | in | in | spatial_containment, visual_relation | high | e19 | False | False |  |  |
| cr3 | m14 | m17 | ent_m14 | ent_m17 | with | with | association_relation, visual_relation | high | e20 | False | False |  |  |
| cr4 | m14 | m20 | ent_m14 | ent_m20 | with | with | association_relation, visual_relation | high | e21 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | pipe |  |  |  | entity_exists:pipe | True | low |
| cf1 | entity_exists | frame |  |  |  | entity_exists:frame | True | low |
| cf2 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf3 | entity_exists | fencing |  |  |  | entity_exists:fencing | True | low |
| cf4 | entity_exists | rebar |  |  |  | entity_exists:rebar | True | low |
| cf5 | entity_exists | distance |  |  | scene_context, spatial_context | entity_exists:distance | True | high |
| cf6 | entity_exists | scene |  |  | scene_context | entity_exists:scene | True | high |
| cf7 | entity_exists | site |  |  |  | entity_exists:site | True | low |
| cf8 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf9 | entity_exists | beam |  |  |  | entity_exists:beam | True | low |
| cf10 | entity_exists | worker |  |  |  | entity_exists:worker | True | low |
| cf11 | entity_exists | equipment |  |  |  | entity_exists:equipment | True | low |
| cf12 | has_attribute | pipe | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:pipe:large | True | high |
| cf13 | has_attribute | pipe | rusted |  | modifier_attribute, visual_attribute | has_attribute:pipe:rusted | True | medium |
| cf14 | has_attribute | pipe | metal |  | material_attribute, material, non_textile_material_type, visual_attribute | has_attribute:pipe:metal | True | high |
| cf15 | has_attribute | sky | blue |  | color_attribute, color, visual_attribute | has_attribute:sky:blue | True | high |
| cf16 | has_attribute | fencing | green |  | color_attribute, color, visual_attribute | has_attribute:fencing:green | True | high |
| cf17 | has_attribute | fencing | construction |  | compound_modifier, visual_attribute | has_attribute:fencing:construction | True | medium |
| cf18 | has_attribute | rebar | steel |  | material_attribute, material, visual_attribute | has_attribute:rebar:steel | True | high |
| cf19 | has_attribute | site | outdoor |  | modifier_attribute, visual_attribute | has_attribute:site:outdoor | True | medium |
| cf20 | has_attribute | site | construction |  | compound_modifier, visual_attribute | has_attribute:site:construction | True | medium |
| cf21 | has_attribute | wall | expose |  | state_attribute, visual_attribute | has_attribute:wall:expose | True | medium |
| cf22 | has_attribute | wall | concrete |  | material_attribute, material, visual_attribute | has_attribute:wall:concrete | True | high |
| cf23 | has_attribute | beam | structural |  | modifier_attribute, visual_attribute | has_attribute:beam:structural | True | medium |
| cf24 | action_event | run |  |  | locomotion_action, visual_action | action_event:run | True | high |
| cf25 | event_role | run | agent | pipe |  | event_role:run:agent:pipe | True | medium |
| cf26 | relation | pipe | across | frame | spatial_path, visual_relation | relation:pipe:across:frame | True | high |
| cf27 | relation | pipe | under | sky | spatial_vertical, visual_relation | relation:pipe:under:sky | True | high |
| cf28 | relation | worker | in | distance | spatial_containment, visual_relation | relation:worker:in:distance | True | high |
| cf29 | relation | site | with | wall | association_relation, visual_relation | relation:site:with:wall | True | high |
| cf30 | relation | site | with | beam | association_relation, visual_relation | relation:site:with:beam | True | high |

### Stage 9 Canonicalization Notes
_none_

## 43

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `257035d6745c0795663db829fc580f78c93e5c49f954babc40906661a92b7414`
**parse_path:** `sentence`

> A female soccer player in a black uniform stands on a grass field, preparing to kick a white and black soccer ball. Spectators are visible behind a fence in the background, with trees and an overcast sky above.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | soccer player | soccer_player | noun_chunk_root | chunk0 | 2 | high |
| m1 | object | uniform | uniform | noun_chunk_root | chunk1 | 6 | high |
| m2 | attribute | black | black | color_attribute | chunk1 | 5 | high |
| m3 | object | field | field | noun_chunk_root | chunk2 | 11 | high |
| m4 | attribute | grass | grass | compound_modifier | chunk2 | 10 | medium |
| m5 | object | soccer ball | soccer_ball | noun_chunk_root | chunk3 | 20 | high |
| m6 | attribute | white | white | color_attribute | chunk3 | 17 | high |
| m7 | attribute | black | black | color_attribute | chunk3 | 19 | high |
| m8 | object | Spectators | spectator | noun_chunk_root | chunk4 | 22 | high |
| m9 | object | fence | fence | noun_chunk_root | chunk5 | 27 | high |
| m10 | context | background | background | scene_context | chunk6 | 30 | high |
| m11 | action | stands | stand | verb_predicate | doc | 7 | high |
| m12 | action | preparing | prepare | verb_predicate | doc | 13 | high |
| m13 | action | kick | kick | verb_predicate | doc | 15 | high |
| m14 | object | trees | tree | with_absolute_recovered_object | with_absolute32 | 33 | medium |
| m15 | object | sky | sky | with_absolute_recovered_object | with_absolute32 | 37 | medium |
| m16 | attribute | overcast | overcast | modifier_attribute | with_absolute32 | 36 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> uniform |
| e1 | has_attribute | m3 | m4 | medium | chunk2 compound -> field |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> soccer ball |
| e3 | has_attribute | m5 | m7 | high | chunk3 conj -> soccer ball |
| e4 | has_context | scene | m10 | high | scene_context token background |
| e5 | agent | m11 | m0 | medium | nsubj -> stands |
| e6 | agent | m12 | m0 | medium | inherited agent advcl -> stands |
| e7 | agent | m13 | m0 | medium | inherited agent xcomp -> preparing |
| e8 | patient | m13 | m5 | medium | dobj -> kick |
| e9 | scene_contains | scene | m14 | medium | with_absolute32 recovered trees |
| e10 | scene_contains | scene | m15 | medium | with_absolute32 recovered sky |
| e11 | has_attribute | m15 | m16 | medium | with_absolute32 amod -> sky |
| e12 | relation | m0 | m1 | high | in |
| e13 | relation | m0 | m3 | high | on |
| e14 | relation | m8 | m9 | high | behind |
| e15 | relation | m9 | m10 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | soccer_player | soccer player | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:soccer_player", "parents": []} |
| ent_m1 | object | uniform | uniform | clothing | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | field | field | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |
| ent_m5 | object | soccer_ball | soccer ball | object | ball, sports_equipment, artifact | m5 | raw_mention |  |  |  | True | {"canonical": "entity:soccer_ball", "parents": ["entity_parent:ball", "entity_parent:sports_equipment", "entity_parent:artifact"]} |
| ent_m8 | object | spectator | Spectators | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:spectator", "parents": []} |
| ent_m9 | object | fence | fence | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:fence", "parents": []} |
| ent_m10 | context | background | background | object | scene_context | m10 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m14 | object | tree | trees | object |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m15 | object | sky | sky | object |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m11 | stands | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m12 | preparing | prepare | prepare | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:prepare", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m13 | kick | kick | kick | visual_action |  | agent:m0->ent_m0; patient:m5->ent_m5 | {"canonical": "action:kick", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e5 | nsubj -> stands |  |  |
| ce1 | prepare | agent | m0 | ent_m0 | medium | e6 | inherited agent advcl -> stands |  |  |
| ce2 | kick | agent | m0 | ent_m0 | medium | e7 | inherited agent xcomp -> preparing |  |  |
| ce2 | kick | patient | m5 | ent_m5 | medium | e8 | dobj -> kick |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | spatial_containment, visual_relation | high | e12 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | on | on | spatial_support, visual_relation | high | e13 | False | False |  |  |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | behind | behind | spatial_depth, visual_relation | high | e14 | False | False |  |  |
| cr3 | m9 | m10 | ent_m9 | ent_m10 | in | in | spatial_containment, visual_relation | high | e15 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | soccer_player |  |  |  | entity_exists:soccer_player | True | low |
| cf1 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf2 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf3 | entity_exists | soccer_ball |  |  | ball, sports_equipment, artifact | entity_exists:soccer_ball | True | high |
| cf4 | entity_exists | spectator |  |  |  | entity_exists:spectator | True | low |
| cf5 | entity_exists | fence |  |  |  | entity_exists:fence | True | low |
| cf6 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf7 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf8 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf9 | has_attribute | uniform | black |  | color_attribute, color, visual_attribute | has_attribute:uniform:black | True | high |
| cf10 | has_attribute | field | grass |  | compound_modifier, visual_attribute | has_attribute:field:grass | True | medium |
| cf11 | has_attribute | soccer_ball | white |  | color_attribute, color, visual_attribute | has_attribute:soccer_ball:white | True | high |
| cf12 | has_attribute | soccer_ball | black |  | color_attribute, color, visual_attribute | has_attribute:soccer_ball:black | True | high |
| cf13 | has_attribute | sky | overcast |  | weather_attribute, weather, visual_attribute | has_attribute:sky:overcast | True | medium |
| cf14 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf15 | event_role | stand | agent | soccer_player |  | event_role:stand:agent:soccer_player | True | medium |
| cf16 | action_event | prepare |  |  | visual_action | action_event:prepare | True | low |
| cf17 | event_role | prepare | agent | soccer_player |  | event_role:prepare:agent:soccer_player | True | medium |
| cf18 | action_event | kick |  |  | visual_action | action_event:kick | True | low |
| cf19 | event_role | kick | agent | soccer_player |  | event_role:kick:agent:soccer_player | True | medium |
| cf20 | event_role | kick | patient | soccer_ball |  | event_role:kick:patient:soccer_ball | True | medium |
| cf21 | relation | soccer_player | in | uniform | spatial_containment, visual_relation | relation:soccer_player:in:uniform | True | high |
| cf22 | relation | soccer_player | on | field | spatial_support, visual_relation | relation:soccer_player:on:field | True | high |
| cf23 | relation | spectator | behind | fence | spatial_depth, visual_relation | relation:spectator:behind:fence | True | high |
| cf24 | relation | fence | in | background | spatial_containment, visual_relation | relation:fence:in:background | True | high |

### Stage 9 Canonicalization Notes
_none_

## 44

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `26bf5861cff19fa38f02fc4a87aad03013cd7b1ec644d44ddef69bc384efbc14`
**parse_path:** `sentence`

> A young hockey player stands on an ice rink wearing a maroon and white jersey, black shorts, and protective gear. They hold a hockey stick with both hands, positioned in front of them, while looking forward. The yellow wall of the rink is visible in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hockey player | hockey_player | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | young | young | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | ice rink | ice_rink | noun_chunk_root | chunk1 | 6 | high |
| m3 | object | jersey | jersey | noun_chunk_root | chunk2 | 12 | high |
| m4 | attribute | maroon | maroon | color_attribute | chunk2 | 9 | high |
| m5 | attribute | white | white | color_attribute | chunk2 | 11 | high |
| m6 | object | shorts | short | noun_chunk_root | chunk3 | 15 | high |
| m7 | attribute | black | black | color_attribute | chunk3 | 14 | high |
| m8 | object | gear | gear | noun_chunk_root | chunk4 | 19 | high |
| m9 | attribute | protective | protective | modifier_attribute | chunk4 | 18 | medium |
| m10 | object | hockey stick | hockey_stick | noun_chunk_root | chunk6 | 24 | high |
| m11 | object | hands | hand | noun_chunk_root | chunk7 | 27 | high |
| m12 | quantity | both | both | group_quantity | chunk7 | 26 | high |
| m13 | object | wall | wall | noun_chunk_root | chunk10 | 41 | high |
| m14 | attribute | yellow | yellow | color_attribute | chunk10 | 40 | high |
| m15 | object | rink | rink | noun_chunk_root | chunk11 | 44 | high |
| m16 | context | background | background | scene_context | chunk12 | 49 | high |
| m17 | action | stands | stand | verb_predicate | doc | 3 | high |
| m18 | action | wearing | wear | verb_predicate | doc | 7 | high |
| m19 | action | hold | hold | verb_predicate | doc | 22 | high |
| m20 | action | positioned | position | verb_predicate | doc | 29 | high |
| m21 | action | looking | look | verb_predicate | doc | 36 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> hockey player |
| e1 | has_attribute | m3 | m4 | high | chunk2 nmod -> jersey |
| e2 | has_attribute | m3 | m5 | high | chunk2 conj -> jersey |
| e3 | has_attribute | m6 | m7 | high | chunk3 amod -> shorts |
| e4 | has_attribute | m8 | m9 | medium | chunk4 amod -> gear |
| e5 | has_quantity | m11 | m12 | high | chunk7 quantity -> hands |
| e6 | has_attribute | m13 | m14 | high | chunk10 amod -> wall |
| e7 | has_context | scene | m16 | high | scene_context token background |
| e8 | agent | m17 | m0 | medium | nsubj -> stands |
| e9 | agent | m18 | m0 | medium | inherited agent advcl -> stands |
| e10 | patient | m18 | m3 | medium | dobj -> wearing |
| e11 | patient | m18 | m6 | medium | dobj -> wearing |
| e12 | patient | m18 | m8 | medium | dobj -> wearing |
| e13 | agent | m19 | m0 | medium | nsubj -> hold; resolved They -> hockey player |
| e14 | patient | m19 | m10 | medium | dobj -> hold |
| e15 | agent | m20 | m0 | medium | inherited agent advcl -> hold |
| e16 | agent | m21 | m0 | medium | inherited agent advcl -> positioned |
| e17 | relation | m0 | m2 | high | on |
| e18 | relation | m0 | m11 | high | with |
| e19 | relation | m10 | m0 | medium | in_front_of; repaired_self_edge_source from hockey player |
| e20 | relation | m13 | m15 | medium | of |
| e21 | relation | m13 | m16 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hockey_player | hockey player | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:hockey_player", "parents": []} |
| ent_m2 | object | ice_rink | ice rink | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:ice_rink", "parents": []} |
| ent_m3 | object | jersey | jersey | clothing | clothing, wearable | m3 | raw_mention |  |  |  | True | {"canonical": "entity:jersey", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m6 | object | short | shorts | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:short", "parents": []} |
| ent_m8 | object | gear | gear | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:gear", "parents": []} |
| ent_m10 | object | hockey_stick | hockey stick | object |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:hockey_stick", "parents": []} |
| ent_m11 | object | hand | hands | object | body_part | m11 | raw_mention |  |  |  | True | {"canonical": "entity:hand", "parents": ["entity_parent:body_part"]} |
| ent_m13 | object | wall | wall | object |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |
| ent_m15 | object | rink | rink | object |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:rink", "parents": []} |
| ent_m16 | context | background | background | object | scene_context | m16 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | stands | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m18 | wearing | wear | wear | wearing_action, visual_action |  | agent:m0->ent_m0; patient:m3->ent_m3; patient:m6->ent_m6; patient:m8->ent_m8 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce2 | m19 | hold | hold | hold | manipulation_action, visual_action |  | agent:m0->ent_m0; patient:m10->ent_m10 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce3 | m20 | positioned | position | position | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:position", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m21 | looking | look | look | gaze_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:look", "parents": ["action_parent:gaze_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e8 | nsubj -> stands |  |  |
| ce1 | wear | agent | m0 | ent_m0 | medium | e9 | inherited agent advcl -> stands |  |  |
| ce1 | wear | patient | m3 | ent_m3 | medium | e10 | dobj -> wearing |  |  |
| ce1 | wear | patient | m6 | ent_m6 | medium | e11 | dobj -> wearing |  |  |
| ce1 | wear | patient | m8 | ent_m8 | medium | e12 | dobj -> wearing |  |  |
| ce2 | hold | agent | m0 | ent_m0 | medium | e13 | nsubj -> hold; resolved They -> hockey player |  |  |
| ce2 | hold | patient | m10 | ent_m10 | medium | e14 | dobj -> hold |  |  |
| ce3 | position | agent | m0 | ent_m0 | medium | e15 | inherited agent advcl -> hold |  |  |
| ce4 | look | agent | m0 | ent_m0 | medium | e16 | inherited agent advcl -> positioned |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | on | spatial_support, visual_relation | high | e17 | False | False |  |  |
| cr1 | m0 | m11 | ent_m0 | ent_m11 | with | with | association_relation, visual_relation | high | e18 | False | False |  |  |
| cr2 | m10 | m0 | ent_m10 | ent_m0 | in_front_of; repaired_self_edge_source from hockey player | in_front_of | spatial_depth, visual_relation | medium | e19 | False | False |  |  |
| cr3 | m13 | m15 | ent_m13 | ent_m15 | of | of | part_relation, visual_relation | medium | e20 | False | False |  |  |
| cr4 | m13 | m16 | ent_m13 | ent_m16 | in | in | spatial_containment, visual_relation | high | e21 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | hockey_player |  |  |  | entity_exists:hockey_player | True | low |
| cf1 | entity_exists | ice_rink |  |  |  | entity_exists:ice_rink | True | low |
| cf2 | entity_exists | jersey |  |  | clothing, wearable | entity_exists:jersey | True | high |
| cf3 | entity_exists | short |  |  |  | entity_exists:short | True | low |
| cf4 | entity_exists | gear |  |  |  | entity_exists:gear | True | low |
| cf5 | entity_exists | hockey_stick |  |  |  | entity_exists:hockey_stick | True | low |
| cf6 | entity_exists | hand |  |  | body_part | entity_exists:hand | True | high |
| cf7 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf8 | entity_exists | rink |  |  |  | entity_exists:rink | True | low |
| cf9 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf10 | has_attribute | hockey_player | young |  | modifier_attribute, visual_attribute | has_attribute:hockey_player:young | True | medium |
| cf11 | has_attribute | jersey | maroon |  | color_attribute, color, visual_attribute | has_attribute:jersey:maroon | True | high |
| cf12 | has_attribute | jersey | white |  | color_attribute, color, visual_attribute | has_attribute:jersey:white | True | high |
| cf13 | has_attribute | short | black |  | color_attribute, color, visual_attribute | has_attribute:short:black | True | high |
| cf14 | has_attribute | gear | protective |  | modifier_attribute, visual_attribute | has_attribute:gear:protective | True | medium |
| cf15 | has_quantity | hand | both |  | group_quantity, quantity | has_quantity:hand:both | True | high |
| cf16 | has_attribute | wall | yellow |  | color_attribute, color, visual_attribute | has_attribute:wall:yellow | True | high |
| cf17 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf18 | event_role | stand | agent | hockey_player |  | event_role:stand:agent:hockey_player | True | medium |
| cf19 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf20 | event_role | wear | agent | hockey_player |  | event_role:wear:agent:hockey_player | True | medium |
| cf21 | event_role | wear | patient | jersey |  | event_role:wear:patient:jersey | True | medium |
| cf22 | event_role | wear | patient | short |  | event_role:wear:patient:short | True | medium |
| cf23 | event_role | wear | patient | gear |  | event_role:wear:patient:gear | True | medium |
| cf24 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf25 | event_role | hold | agent | hockey_player |  | event_role:hold:agent:hockey_player | True | medium |
| cf26 | event_role | hold | patient | hockey_stick |  | event_role:hold:patient:hockey_stick | True | medium |
| cf27 | action_event | position |  |  | visual_action | action_event:position | True | low |
| cf28 | event_role | position | agent | hockey_player |  | event_role:position:agent:hockey_player | True | medium |
| cf29 | action_event | look |  |  | gaze_action, visual_action | action_event:look | True | high |
| cf30 | event_role | look | agent | hockey_player |  | event_role:look:agent:hockey_player | True | medium |
| cf31 | relation | hockey_player | on | ice_rink | spatial_support, visual_relation | relation:hockey_player:on:ice_rink | True | high |
| cf32 | relation | hockey_player | with | hand | association_relation, visual_relation | relation:hockey_player:with:hand | True | high |
| cf33 | relation | hockey_stick | in_front_of | hockey_player | spatial_depth, visual_relation | relation:hockey_stick:in_front_of:hockey_player | True | medium |
| cf34 | relation | wall | of | rink | part_relation, visual_relation | relation:wall:of:rink | True | medium |
| cf35 | relation | wall | in | background | spatial_containment, visual_relation | relation:wall:in:background | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e19 |  |  |  | {"canonical": "in_front_of", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e19", "raw_relation": "in_front_of; repaired_self_edge_source from hockey player", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 45

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `26c7740ca0bb561574835f609a8a1cc602f57ba46a5a2e8be20264cbdd9ef814`
**parse_path:** `sentence`

> A stone building with arched windows and a decorative spire stands under a clear blue sky. A black streetlamp hangs from the right side of the frame, next to the building’s facade. Flower boxes line the windows on the upper floor.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | stone | stone | material_attribute | chunk0 | 1 | high |
| m2 | object | windows | window | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | arched | arched | visual_attribute | chunk1 | 4 | medium |
| m4 | object | spire | spire | noun_chunk_root | chunk2 | 9 | high |
| m5 | attribute | decorative | decorative | modifier_attribute | chunk2 | 8 | medium |
| m6 | object | sky | sky | noun_chunk_root | chunk3 | 15 | high |
| m7 | attribute | clear | clear | visual_attribute | chunk3 | 13 | medium |
| m8 | attribute | blue | blue | color_attribute | chunk3 | 14 | high |
| m9 | object | streetlamp | streetlamp | noun_chunk_root | chunk4 | 19 | high |
| m10 | attribute | black | black | color_attribute | chunk4 | 18 | high |
| m11 | object | frame | frame | noun_chunk_root | chunk6 | 27 | high |
| m12 | object | facade | facade | noun_chunk_root | chunk7 | 34 | high |
| m13 | attribute | building | building | modifier_attribute | chunk7 | 32 | medium |
| m14 | object | boxes | box | noun_chunk_root | chunk8 | 37 | high |
| m15 | attribute | Flower | flower | compound_modifier | chunk8 | 36 | medium |
| m16 | object | windows | window | noun_chunk_root | chunk9 | 40 | high |
| m17 | object | floor | floor | noun_chunk_root | chunk10 | 44 | high |
| m18 | attribute | upper | upper | modifier_attribute | chunk10 | 43 | medium |
| m19 | action | stands | stand | verb_predicate | doc | 10 | high |
| m20 | action | hangs | hang | verb_predicate | doc | 20 | high |
| m21 | action | line | line | verb_predicate | doc | 38 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 compound -> building |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> windows |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> spire |
| e3 | has_attribute | m6 | m7 | medium | chunk3 amod -> sky |
| e4 | has_attribute | m6 | m8 | high | chunk3 amod -> sky |
| e5 | has_attribute | m9 | m10 | high | chunk4 amod -> streetlamp |
| e6 | has_attribute | m12 | m13 | medium | chunk7 poss -> facade |
| e7 | has_attribute | m14 | m15 | medium | chunk8 compound -> boxes |
| e8 | has_attribute | m17 | m18 | medium | chunk10 amod -> floor |
| e9 | agent | m19 | m0 | medium | nsubj -> stands |
| e10 | agent | m20 | m9 | medium | nsubj -> hangs |
| e11 | agent | m21 | m14 | medium | nsubj -> line |
| e12 | patient | m21 | m16 | medium | dobj -> line |
| e13 | relation | m0 | m2 | high | with |
| e14 | relation | m0 | m4 | high | with |
| e15 | relation | m0 | m6 | high | under |
| e16 | relation | m9 | m11 | medium | from_side_of |
| e17 | relation | m9 | m12 | high | next_to |
| e18 | relation | m16 | m17 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | building | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m2 | object | window | windows | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:window", "parents": []} |
| ent_m4 | object | spire | spire | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:spire", "parents": []} |
| ent_m6 | object | sky | sky | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m9 | object | streetlamp | streetlamp | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:streetlamp", "parents": []} |
| ent_m11 | object | frame | frame | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:frame", "parents": []} |
| ent_m12 | object | facade | facade | object |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:facade", "parents": []} |
| ent_m14 | object | box | boxes | object |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:box", "parents": []} |
| ent_m16 | object | window | windows | object |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:window", "parents": []} |
| ent_m17 | object | floor | floor | object |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:floor", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m19 | stands | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m20 | hangs | hang | hang | attachment_action, visual_action |  | agent:m9->ent_m9 | {"canonical": "action:hang", "parents": ["action_parent:attachment_action", "action_parent:visual_action"]} |  |
| ce2 | m21 | line | line | line | visual_action |  | agent:m14->ent_m14; patient:m16->ent_m16 | {"canonical": "action:line", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e9 | nsubj -> stands |  |  |
| ce1 | hang | agent | m9 | ent_m9 | medium | e10 | nsubj -> hangs |  |  |
| ce2 | line | agent | m14 | ent_m14 | medium | e11 | nsubj -> line |  |  |
| ce2 | line | patient | m16 | ent_m16 | medium | e12 | dobj -> line |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | with | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | under | under | spatial_vertical, visual_relation | high | e15 | False | False |  |  |
| cr3 | m9 | m11 | ent_m9 | ent_m11 | from_side_of | from_side_of | spatial_source, visual_relation | medium | e16 | False | False |  |  |
| cr4 | m9 | m12 | ent_m9 | ent_m12 | next_to | next_to | spatial_proximity, visual_relation | high | e17 | False | False |  |  |
| cr5 | m16 | m17 | ent_m16 | ent_m17 | on | on | spatial_support, visual_relation | high | e18 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf1 | entity_exists | window |  |  |  | entity_exists:window | True | low |
| cf2 | entity_exists | spire |  |  |  | entity_exists:spire | True | low |
| cf3 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf4 | entity_exists | streetlamp |  |  |  | entity_exists:streetlamp | True | low |
| cf5 | entity_exists | frame |  |  |  | entity_exists:frame | True | low |
| cf6 | entity_exists | facade |  |  |  | entity_exists:facade | True | low |
| cf7 | entity_exists | box |  |  |  | entity_exists:box | True | low |
| cf8 | entity_exists | window |  |  |  | entity_exists:window | True | low |
| cf9 | entity_exists | floor |  |  |  | entity_exists:floor | True | low |
| cf10 | has_attribute | building | stone |  | material_attribute, material, visual_attribute | has_attribute:building:stone | True | high |
| cf11 | has_attribute | window | arched |  | visual_attribute | has_attribute:window:arched | True | medium |
| cf12 | has_attribute | spire | decorative |  | modifier_attribute, visual_attribute | has_attribute:spire:decorative | True | medium |
| cf13 | has_attribute | sky | clear |  | weather_attribute, opaqeness, weather, visual_attribute | has_attribute:sky:clear | True | medium |
| cf14 | has_attribute | sky | blue |  | color_attribute, color, visual_attribute | has_attribute:sky:blue | True | high |
| cf15 | has_attribute | streetlamp | black |  | color_attribute, color, visual_attribute | has_attribute:streetlamp:black | True | high |
| cf16 | has_attribute | facade | building |  | modifier_attribute, visual_attribute | has_attribute:facade:building | True | medium |
| cf17 | has_attribute | box | flower |  | compound_modifier, visual_attribute | has_attribute:box:flower | True | medium |
| cf18 | has_attribute | floor | upper |  | modifier_attribute, visual_attribute | has_attribute:floor:upper | True | medium |
| cf19 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf20 | event_role | stand | agent | building |  | event_role:stand:agent:building | True | medium |
| cf21 | action_event | hang |  |  | attachment_action, visual_action | action_event:hang | True | high |
| cf22 | event_role | hang | agent | streetlamp |  | event_role:hang:agent:streetlamp | True | medium |
| cf23 | action_event | line |  |  | visual_action | action_event:line | True | low |
| cf24 | event_role | line | agent | box |  | event_role:line:agent:box | True | medium |
| cf25 | event_role | line | patient | window |  | event_role:line:patient:window | True | medium |
| cf26 | relation | building | with | window | association_relation, visual_relation | relation:building:with:window | True | high |
| cf27 | relation | building | with | spire | association_relation, visual_relation | relation:building:with:spire | True | high |
| cf28 | relation | building | under | sky | spatial_vertical, visual_relation | relation:building:under:sky | True | high |
| cf29 | relation | streetlamp | from_side_of | frame | spatial_source, visual_relation | relation:streetlamp:from_side_of:frame | True | medium |
| cf30 | relation | streetlamp | next_to | facade | spatial_proximity, visual_relation | relation:streetlamp:next_to:facade | True | high |
| cf31 | relation | window | on | floor | spatial_support, visual_relation | relation:window:on:floor | True | high |

### Stage 9 Canonicalization Notes
_none_

## 46

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `2787924a005a3274c2f1298b97e68af52c84f0abb4317613b3d60836705b4c14`
**parse_path:** `tag_list`

> rusty metal, scrap pile, cornfield, broken pipes, red beam

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | metal | metal | segment_head | t0 | 1 | high |
| m1 | attribute | rusty | rusty | attribute | t0 | 0 | high |
| m2 | object | pile | pile | segment_head | t1 | 1 | high |
| m3 | attribute | scrap | scrap | attribute | t1 | 0 | high |
| m4 | object | cornfield | cornfield | segment_head | t2 | 0 | high |
| m5 | object | pipes | pipe | segment_head | t3 | 1 | high |
| m6 | attribute | broken | broken | attribute | t3 | 0 | high |
| m7 | object | beam | beam | segment_head | t4 | 1 | high |
| m8 | attribute | red | red | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> metal |
| e1 | has_attribute | m2 | m3 | high | t1 internal compound -> pile |
| e2 | has_attribute | m5 | m6 | high | t3 internal amod -> pipes |
| e3 | has_attribute | m7 | m8 | high | t4 internal amod -> beam |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | metal | metal | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:metal", "parents": []} |
| ent_m2 | object | pile | pile | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:pile", "parents": []} |
| ent_m4 | object | cornfield | cornfield | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:cornfield", "parents": []} |
| ent_m5 | object | pipe | pipes | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:pipe", "parents": []} |
| ent_m7 | object | beam | beam | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:beam", "parents": []} |

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
| cf0 | entity_exists | metal |  |  |  | entity_exists:metal | True | low |
| cf1 | entity_exists | pile |  |  |  | entity_exists:pile | True | low |
| cf2 | entity_exists | cornfield |  |  |  | entity_exists:cornfield | True | low |
| cf3 | entity_exists | pipe |  |  |  | entity_exists:pipe | True | low |
| cf4 | entity_exists | beam |  |  |  | entity_exists:beam | True | low |
| cf5 | has_attribute | metal | rusty |  | attribute, visual_attribute | has_attribute:metal:rusty | True | high |
| cf6 | has_attribute | pile | scrap |  | attribute, visual_attribute | has_attribute:pile:scrap | True | high |
| cf7 | has_attribute | pipe | broken |  | state_attribute, other, state, visual_attribute | has_attribute:pipe:broken | True | high |
| cf8 | has_attribute | beam | red |  | color_attribute, color, visual_attribute | has_attribute:beam:red | True | high |

### Stage 9 Canonicalization Notes
_none_

## 47

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `27b9261b58a992423ef196b870b3213354abab3bfcabd4ea4016363cf8e8b814`
**parse_path:** `sentence`

> Four people sit at a table during a panel discussion. Behind them, a large screen displays the text “edición, diversidad cultural y desarrollo.” Each person has a microphone and nameplate in front of them.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “edición, diversidad cultural y desarrollo.” | edición,_diversidad_cultural_y_desarrollo. | quote_text | doc_quote | 20 | high |
| m1 | object | people | people | noun_chunk_root | chunk0 | 1 | high |
| m2 | quantity | Four | four | exact_quantity | chunk0 | 0 | high |
| m3 | object | table | table | noun_chunk_root | chunk1 | 5 | high |
| m4 | object | discussion | discussion | noun_chunk_root | chunk2 | 9 | high |
| m5 | attribute | panel | panel | compound_modifier | chunk2 | 8 | medium |
| m6 | object | screen | screen | noun_chunk_root | chunk4 | 16 | high |
| m7 | attribute | large | large | size_attribute | chunk4 | 15 | high |
| m8 | object | text | text | noun_chunk_root | chunk5 | 19 | high |
| m9 | object | person | person | noun_chunk_root | chunk7 | 22 | high |
| m10 | quantity | Each | each | distributive_quantity | chunk7 | 21 | high |
| m11 | object | microphone | microphone | noun_chunk_root | chunk8 | 25 | high |
| m12 | object | nameplate | nameplate | noun_chunk_root | chunk9 | 27 | high |
| m13 | action | sit | sit | verb_predicate | doc | 2 | high |
| m14 | action | displays | display | verb_predicate | doc | 17 | high |
| m15 | action | has | have | verb_predicate | doc | 23 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m1 | m2 | high | chunk0 quantity -> people |
| e1 | has_attribute | m4 | m5 | medium | chunk2 compound -> discussion |
| e2 | has_attribute | m6 | m7 | high | chunk4 amod -> screen |
| e3 | has_quantity | m9 | m10 | high | chunk7 quantity -> person |
| e4 | has_attribute | m8 | m0 | high | quote appos -> text |
| e5 | agent | m13 | m1 | medium | nsubj -> sit |
| e6 | agent | m14 | m6 | medium | nsubj -> displays |
| e7 | patient | m14 | m8 | medium | dobj -> displays |
| e8 | agent | m15 | m9 | medium | nsubj -> has |
| e9 | patient | m15 | m11 | medium | dobj -> has |
| e10 | patient | m15 | m12 | medium | dobj -> has |
| e11 | relation | m1 | m3 | medium | at |
| e12 | relation | m1 | m4 | medium | during |
| e13 | relation | m6 | m1 | high | behind |
| e14 | relation | m11 | m9 | medium | in_front_of; repaired_self_edge_source from person |
| e15 | relation | m12 | m9 | medium | in_front_of; repaired_self_edge_source from person |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | people | people | person | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m3 | object | table | table | object | furniture, artifact | m3 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m4 | object | discussion | discussion | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:discussion", "parents": []} |
| ent_m6 | object | screen | screen | device | device, artifact | m6 | raw_mention |  |  |  | True | {"canonical": "entity:screen", "parents": ["entity_parent:device", "entity_parent:artifact"]} |
| ent_m8 | object | text | text | document | text_content | m8 | raw_mention |  |  |  | True | {"canonical": "entity:text", "parents": ["entity_parent:text_content"]} |
| ent_m9 | object | person | person | person | person, human | m9 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m11 | object | microphone | microphone | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:microphone", "parents": []} |
| ent_m12 | object | nameplate | nameplate | object |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:nameplate", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m13 | sit | sit | sit | body_pose_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m14 | displays | display | display | visual_action |  | agent:m6->ent_m6; patient:m8->ent_m8 | {"canonical": "action:display", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m15 | has | have | have | visual_action |  | agent:m9->ent_m9; patient:m11->ent_m11; patient:m12->ent_m12 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m1 | ent_m1 | medium | e5 | nsubj -> sit |  |  |
| ce1 | display | agent | m6 | ent_m6 | medium | e6 | nsubj -> displays |  |  |
| ce1 | display | patient | m8 | ent_m8 | medium | e7 | dobj -> displays |  |  |
| ce2 | have | agent | m9 | ent_m9 | medium | e8 | nsubj -> has |  |  |
| ce2 | have | patient | m11 | ent_m11 | medium | e9 | dobj -> has |  |  |
| ce2 | have | patient | m12 | ent_m12 | medium | e10 | dobj -> has |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m3 | ent_m1 | ent_m3 | at | at | spatial_location, visual_relation | medium | e11 | False | False |  |  |
| cr1 | m1 | m4 | ent_m1 | ent_m4 | during | during | visual_relation | medium | e12 | False | False |  |  |
| cr2 | m6 | m1 | ent_m6 | ent_m1 | behind | behind | spatial_depth, visual_relation | high | e13 | False | False |  |  |
| cr3 | m11 | m9 | ent_m11 | ent_m9 | in_front_of; repaired_self_edge_source from person | in_front_of | spatial_depth, visual_relation | medium | e14 | False | False |  |  |
| cr4 | m12 | m9 | ent_m12 | ent_m9 | in_front_of; repaired_self_edge_source from person | in_front_of | spatial_depth, visual_relation | medium | e15 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf2 | entity_exists | discussion |  |  |  | entity_exists:discussion | True | low |
| cf3 | entity_exists | screen |  |  | device, artifact | entity_exists:screen | True | high |
| cf4 | entity_exists | text |  |  | text_content | entity_exists:text | True | high |
| cf5 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf6 | entity_exists | microphone |  |  |  | entity_exists:microphone | True | low |
| cf7 | entity_exists | nameplate |  |  |  | entity_exists:nameplate | True | low |
| cf8 | has_quantity | people | four |  | exact_quantity, quantity | has_quantity:people:four | True | high |
| cf9 | has_attribute | discussion | panel |  | compound_modifier, visual_attribute | has_attribute:discussion:panel | True | medium |
| cf10 | has_attribute | screen | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:screen:large | True | high |
| cf11 | has_quantity | person | each |  | distributive_quantity, quantity | has_quantity:person:each | True | high |
| cf12 | has_attribute | text | edición,_diversidad_cultural_y_desarrollo. |  | quote_text, visual_attribute | has_attribute:text:edición,_diversidad_cultural_y_desarrollo. | True | high |
| cf13 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf14 | event_role | sit | agent | people |  | event_role:sit:agent:people | True | medium |
| cf15 | action_event | display |  |  | visual_action | action_event:display | True | low |
| cf16 | event_role | display | agent | screen |  | event_role:display:agent:screen | True | medium |
| cf17 | event_role | display | patient | text |  | event_role:display:patient:text | True | medium |
| cf18 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf19 | event_role | have | agent | person |  | event_role:have:agent:person | True | medium |
| cf20 | event_role | have | patient | microphone |  | event_role:have:patient:microphone | True | medium |
| cf21 | event_role | have | patient | nameplate |  | event_role:have:patient:nameplate | True | medium |
| cf22 | relation | people | at | table | spatial_location, visual_relation | relation:people:at:table | True | medium |
| cf23 | relation | people | during | discussion | visual_relation | relation:people:during:discussion | True | medium |
| cf24 | relation | screen | behind | people | spatial_depth, visual_relation | relation:screen:behind:people | True | high |
| cf25 | relation | microphone | in_front_of | person | spatial_depth, visual_relation | relation:microphone:in_front_of:person | True | medium |
| cf26 | relation | nameplate | in_front_of | person | spatial_depth, visual_relation | relation:nameplate:in_front_of:person | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e14 |  |  |  | {"canonical": "in_front_of", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e14", "raw_relation": "in_front_of; repaired_self_edge_source from person", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |
| relation_lexical_canonicalized |  | e15 |  |  |  | {"canonical": "in_front_of", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e15", "raw_relation": "in_front_of; repaired_self_edge_source from person", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 48

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `2852b9dad94ae23a32a05bfce5ec5c5eea0eef8648c433e1e5464e376cbc9814`
**parse_path:** `sentence`

> A man in a tuxedo gives a thumbs-up while holding a trophy on stage. A woman stands beside him, smiling.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | tuxedo | tuxedo | noun_chunk_root | chunk1 | 4 | high |
| m2 | object | thumbs-up | thumbs-up | noun_chunk_root | chunk2 | 7 | high |
| m3 | object | trophy | trophy | noun_chunk_root | chunk3 | 11 | high |
| m4 | object | stage | stage | noun_chunk_root | chunk4 | 13 | high |
| m5 | object | woman | woman | noun_chunk_root | chunk5 | 16 | high |
| m6 | action | gives | give | verb_predicate | doc | 5 | high |
| m7 | action | holding | hold | verb_predicate | doc | 9 | high |
| m8 | action | stands | stand | verb_predicate | doc | 17 | high |
| m9 | action | smiling | smile | verb_predicate | doc | 21 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | agent | m6 | m0 | medium | nsubj -> gives |
| e1 | patient | m6 | m2 | medium | dobj -> gives |
| e2 | agent | m7 | m0 | medium | inherited agent advcl -> gives |
| e3 | patient | m7 | m3 | medium | dobj -> holding |
| e4 | agent | m8 | m5 | medium | nsubj -> stands |
| e5 | agent | m9 | m5 | medium | inherited agent advcl -> stands |
| e6 | relation | m0 | m1 | high | in |
| e7 | relation | m0 | m4 | high | on |
| e8 | relation | m5 | m0 | high | beside |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | tuxedo | tuxedo | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:tuxedo", "parents": []} |
| ent_m2 | object | thumbs-up | thumbs-up | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:thumbs-up", "parents": []} |
| ent_m3 | object | trophy | trophy | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:trophy", "parents": []} |
| ent_m4 | object | stage | stage | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:stage", "parents": []} |
| ent_m5 | object | woman | woman | person | person, human | m5 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m6 | gives | give | give | visual_action |  | agent:m0->ent_m0; patient:m2->ent_m2 | {"canonical": "action:give", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m7 | holding | hold | hold | manipulation_action, visual_action |  | agent:m0->ent_m0; patient:m3->ent_m3 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce2 | m8 | stands | stand | stand | body_pose_action, visual_action |  | agent:m5->ent_m5 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce3 | m9 | smiling | smile | smile | expression_action, visual_action |  | agent:m5->ent_m5 | {"canonical": "action:smile", "parents": ["action_parent:expression_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | give | agent | m0 | ent_m0 | medium | e0 | nsubj -> gives |  |  |
| ce0 | give | patient | m2 | ent_m2 | medium | e1 | dobj -> gives |  |  |
| ce1 | hold | agent | m0 | ent_m0 | medium | e2 | inherited agent advcl -> gives |  |  |
| ce1 | hold | patient | m3 | ent_m3 | medium | e3 | dobj -> holding |  |  |
| ce2 | stand | agent | m5 | ent_m5 | medium | e4 | nsubj -> stands |  |  |
| ce3 | smile | agent | m5 | ent_m5 | medium | e5 | inherited agent advcl -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | spatial_containment, visual_relation | high | e6 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | on | spatial_support, visual_relation | high | e7 | False | False |  |  |
| cr2 | m5 | m0 | ent_m5 | ent_m0 | beside | next_to | spatial_proximity, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | tuxedo |  |  |  | entity_exists:tuxedo | True | low |
| cf2 | entity_exists | thumbs-up |  |  |  | entity_exists:thumbs-up | True | low |
| cf3 | entity_exists | trophy |  |  |  | entity_exists:trophy | True | low |
| cf4 | entity_exists | stage |  |  |  | entity_exists:stage | True | low |
| cf5 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf6 | action_event | give |  |  | visual_action | action_event:give | True | low |
| cf7 | event_role | give | agent | man |  | event_role:give:agent:man | True | medium |
| cf8 | event_role | give | patient | thumbs-up |  | event_role:give:patient:thumbs-up | True | medium |
| cf9 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf10 | event_role | hold | agent | man |  | event_role:hold:agent:man | True | medium |
| cf11 | event_role | hold | patient | trophy |  | event_role:hold:patient:trophy | True | medium |
| cf12 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf13 | event_role | stand | agent | woman |  | event_role:stand:agent:woman | True | medium |
| cf14 | action_event | smile |  |  | expression_action, visual_action | action_event:smile | True | high |
| cf15 | event_role | smile | agent | woman |  | event_role:smile:agent:woman | True | medium |
| cf16 | relation | man | in | tuxedo | spatial_containment, visual_relation | relation:man:in:tuxedo | True | high |
| cf17 | relation | man | on | stage | spatial_support, visual_relation | relation:man:on:stage | True | high |
| cf18 | relation | woman | next_to | man | spatial_proximity, visual_relation | relation:woman:next_to:man | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e8 |  |  |  | {"canonical": "next_to", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e8", "raw_relation": "beside", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 49

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `297167f329b8ff2480dda2037bd067eb4f305c39aff064b27927358c36f74814`
**parse_path:** `sentence`

> A person wears a black and yellow bicycle helmet with blue sunglasses. The individual is outdoors, with grass and sunlight visible in the background. A date stamp reads “2007/06/09 01:14” in the corner.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “2007/06/09 01:14” | 2007/06/09_01:14 | quote_text | doc_quote | 30 | high |
| m1 | object | person | person | noun_chunk_root | chunk0 | 1 | high |
| m2 | object | bicycle helmet | bicycle_helmet | noun_chunk_root | chunk1 | 7 | high |
| m3 | attribute | black | black | color_attribute | chunk1 | 4 | high |
| m4 | attribute | yellow | yellow | color_attribute | chunk1 | 6 | high |
| m5 | object | sunglasses | sunglass | noun_chunk_root | chunk2 | 10 | high |
| m6 | attribute | blue | blue | color_attribute | chunk2 | 9 | high |
| m8 | object | grass | grass | noun_chunk_root | chunk4 | 18 | high |
| m9 | object | sunlight | sunlight | noun_chunk_root | chunk5 | 20 | high |
| m10 | context | background | background | scene_context | chunk6 | 24 | high |
| m11 | object | stamp | stamp | noun_chunk_root | chunk7 | 28 | high |
| m12 | attribute | date | date | compound_modifier | chunk7 | 27 | medium |
| m13 | context | corner | corner | spatial_region | chunk8 | 33 | medium |
| m14 | context | outdoors | outdoors | scene_context | doc | 15 | high |
| m15 | reference | The individual | individual | generic_human_reference | generic_anaphoric | 13 | high |
| m16 | action | wears | wear | verb_predicate | doc | 2 | high |
| m17 | action | reads | read | verb_predicate | doc | 29 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | chunk1 amod -> bicycle helmet |
| e1 | has_attribute | m2 | m4 | high | chunk1 conj -> bicycle helmet |
| e2 | has_attribute | m5 | m6 | high | chunk2 amod -> sunglasses |
| e3 | has_context | scene | m10 | high | scene_context token background |
| e4 | has_attribute | m11 | m12 | medium | chunk7 compound -> stamp |
| e5 | has_context | scene | m14 | high | scene_context token outdoors |
| e6 | refers_to | m15 | m1 | high | generic definite NP score=177 margin=177 |
| e7 | agent | m16 | m1 | medium | nsubj -> wears |
| e8 | patient | m16 | m2 | medium | dobj -> wears |
| e9 | agent | m17 | m11 | medium | nsubj -> reads |
| e10 | patient | m17 | m0 | medium | dobj -> reads |
| e11 | relation | m2 | m5 | high | with |
| e12 | relation | m11 | m13 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | person | person | person | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | bicycle_helmet | bicycle helmet | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:bicycle_helmet", "parents": []} |
| ent_m5 | object | sunglass | sunglasses | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:sunglass", "parents": []} |
| ent_m8 | object | grass | grass | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": []} |
| ent_m9 | object | sunlight | sunlight | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:sunlight", "parents": []} |
| ent_m10 | context | background | background | object | scene_context | m10 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m11 | object | stamp | stamp | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:stamp", "parents": []} |
| ent_m13 | context | corner | corner | object | scene_context | m13 | raw_mention |  |  |  | True | {"canonical": "entity:corner", "parents": ["entity_parent:scene_context"]} |
| ent_m14 | context | outdoors | outdoors | object | scene_context | m14 | raw_mention |  |  |  | True | {"canonical": "entity:outdoors", "parents": ["entity_parent:scene_context"]} |
| eref_m15 | reference | person | The individual | person | person, human | m15 | stage9_reference | ent_m1 |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m15 | eref_m15 | m1 | ent_m1 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | wears | wear | wear | wearing_action, visual_action |  | agent:m1->ent_m1; patient:m2->ent_m2 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce1 | m17 | reads | read | read | text_interaction_action, visual_action |  | agent:m11->ent_m11; patient:m0->None | {"canonical": "action:read", "parents": ["action_parent:text_interaction_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | wear | agent | m1 | ent_m1 | medium | e7 | nsubj -> wears |  |  |
| ce0 | wear | patient | m2 | ent_m2 | medium | e8 | dobj -> wears |  |  |
| ce1 | read | agent | m11 | ent_m11 | medium | e9 | nsubj -> reads |  |  |
| ce1 | read | patient | m0 |  | medium | e10 | dobj -> reads |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m2 | m5 | ent_m2 | ent_m5 | with | with | association_relation, visual_relation | high | e11 | False | False |  |  |
| cr1 | m11 | m13 | ent_m11 | ent_m13 | in | in | spatial_containment, visual_relation | high | e12 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf1 | entity_exists | bicycle_helmet |  |  |  | entity_exists:bicycle_helmet | True | low |
| cf2 | entity_exists | sunglass |  |  |  | entity_exists:sunglass | True | low |
| cf3 | entity_exists | grass |  |  |  | entity_exists:grass | True | low |
| cf4 | entity_exists | sunlight |  |  |  | entity_exists:sunlight | True | low |
| cf5 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf6 | entity_exists | stamp |  |  |  | entity_exists:stamp | True | low |
| cf7 | entity_exists | corner |  |  | scene_context | entity_exists:corner | True | medium |
| cf8 | entity_exists | outdoors |  |  | scene_context | entity_exists:outdoors | True | high |
| cf9 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf10 | has_attribute | bicycle_helmet | black |  | color_attribute, color, visual_attribute | has_attribute:bicycle_helmet:black | True | high |
| cf11 | has_attribute | bicycle_helmet | yellow |  | color_attribute, color, visual_attribute | has_attribute:bicycle_helmet:yellow | True | high |
| cf12 | has_attribute | sunglass | blue |  | color_attribute, color, visual_attribute | has_attribute:sunglass:blue | True | high |
| cf13 | has_attribute | stamp | date |  | compound_modifier, visual_attribute | has_attribute:stamp:date | True | medium |
| cf14 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf15 | event_role | wear | agent | person |  | event_role:wear:agent:person | True | medium |
| cf16 | event_role | wear | patient | bicycle_helmet |  | event_role:wear:patient:bicycle_helmet | True | medium |
| cf17 | action_event | read |  |  | text_interaction_action, visual_action | action_event:read | True | medium |
| cf18 | event_role | read | agent | stamp |  | event_role:read:agent:stamp | True | medium |
| cf19 | event_role | read | patient |  |  | event_role:read:patient | False | medium |
| cf20 | relation | bicycle_helmet | with | sunglass | association_relation, visual_relation | relation:bicycle_helmet:with:sunglass | True | high |
| cf21 | relation | stamp | in | corner | spatial_containment, visual_relation | relation:stamp:in:corner | True | high |

### Stage 9 Canonicalization Notes
_none_

## 50

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `2a74cb3297dae2956b9597135736563591d14b31bbc8d75474c9d828d0a15414`
**parse_path:** `tag_list`

> orange flower, green leaves, blurred background

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | flower | flower | segment_head | t0 | 1 | high |
| m1 | attribute | orange | orange | attribute | t0 | 0 | high |
| m2 | object | leaves | leaf | segment_head | t1 | 1 | high |
| m3 | attribute | green | green | attribute | t1 | 0 | high |
| m4 | context | background | background | scene_context | t2 | 1 | high |
| m5 | attribute | blurred | blurred | attribute | t2 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> flower |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> leaves |
| e2 | has_context | scene | m4 | high | t2 context tag |
| e3 | has_attribute | m4 | m5 | high | t2 internal amod -> background |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | flower | flower | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:flower", "parents": []} |
| ent_m2 | object | leaf | leaves | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:leaf", "parents": []} |
| ent_m4 | context | background | background | object | scene_context | m4 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

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
| cf0 | entity_exists | flower |  |  |  | entity_exists:flower | True | low |
| cf1 | entity_exists | leaf |  |  |  | entity_exists:leaf | True | low |
| cf2 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf3 | has_attribute | flower | orange |  | color_attribute, color, visual_attribute | has_attribute:flower:orange | True | high |
| cf4 | has_attribute | leaf | green |  | color_attribute, color, visual_attribute | has_attribute:leaf:green | True | high |
| cf5 | has_attribute | background | blurred |  | attribute, visual_attribute | has_attribute:background:blurred | True | high |

### Stage 9 Canonicalization Notes
_none_

## 51

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `2a852a207447331ae329e1f42115b77bd23852e22e630f967738b27a9a8ca014`
**parse_path:** `sentence`

> A man holds a black umbrella and stands beside a stone sign that reads "MILE 0 VICTORIA BC" in a grassy park.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "MILE 0 VICTORIA BC" | mile_0_victoria_bc | quote_text | doc_quote | 14 | high |
| m1 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m2 | object | umbrella | umbrella | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | black | black | color_attribute | chunk1 | 4 | high |
| m4 | object | sign | sign | noun_chunk_root | chunk2 | 11 | high |
| m5 | attribute | stone | stone | material_attribute | chunk2 | 10 | high |
| m6 | object | park | park | noun_chunk_root | chunk5 | 18 | high |
| m7 | attribute | grassy | grassy | modifier_attribute | chunk5 | 17 | medium |
| m8 | action | holds | hold | verb_predicate | doc | 2 | high |
| m9 | action | stands | stand | verb_predicate | doc | 7 | high |
| m10 | action | reads | read | verb_predicate | doc | 13 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | chunk1 amod -> umbrella |
| e1 | has_attribute | m4 | m5 | high | chunk2 compound -> sign |
| e2 | has_attribute | m6 | m7 | medium | chunk5 amod -> park |
| e3 | agent | m8 | m1 | medium | nsubj -> holds |
| e4 | patient | m8 | m2 | medium | dobj -> holds |
| e5 | agent | m9 | m1 | medium | inherited agent conj -> holds |
| e6 | agent | m10 | m4 | medium | nsubj -> reads; resolved that -> sign |
| e7 | patient | m10 | m0 | medium | dobj -> reads |
| e8 | relation | m1 | m4 | high | beside |
| e9 | relation | m1 | m6 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | man | man | person | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | umbrella | umbrella | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:umbrella", "parents": []} |
| ent_m4 | object | sign | sign | document | text_carrier, artifact | m4 | raw_mention |  |  |  | True | {"canonical": "entity:sign", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m6 | object | park | park | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:park", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | holds | hold | hold | manipulation_action, visual_action |  | agent:m1->ent_m1; patient:m2->ent_m2 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce1 | m9 | stands | stand | stand | body_pose_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce2 | m10 | reads | read | read | text_interaction_action, visual_action |  | agent:m4->ent_m4; patient:m0->None | {"canonical": "action:read", "parents": ["action_parent:text_interaction_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | hold | agent | m1 | ent_m1 | medium | e3 | nsubj -> holds |  |  |
| ce0 | hold | patient | m2 | ent_m2 | medium | e4 | dobj -> holds |  |  |
| ce1 | stand | agent | m1 | ent_m1 | medium | e5 | inherited agent conj -> holds |  |  |
| ce2 | read | agent | m4 | ent_m4 | medium | e6 | nsubj -> reads; resolved that -> sign |  |  |
| ce2 | read | patient | m0 |  | medium | e7 | dobj -> reads |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m4 | ent_m1 | ent_m4 | beside | next_to | spatial_proximity, visual_relation | high | e8 | False | False |  |  |
| cr1 | m1 | m6 | ent_m1 | ent_m6 | in | in | spatial_containment, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | umbrella |  |  |  | entity_exists:umbrella | True | low |
| cf2 | entity_exists | sign |  |  | text_carrier, artifact | entity_exists:sign | True | high |
| cf3 | entity_exists | park |  |  |  | entity_exists:park | True | low |
| cf4 | has_attribute | umbrella | black |  | color_attribute, color, visual_attribute | has_attribute:umbrella:black | True | high |
| cf5 | has_attribute | sign | stone |  | material_attribute, material, visual_attribute | has_attribute:sign:stone | True | high |
| cf6 | has_attribute | park | grassy |  | modifier_attribute, visual_attribute | has_attribute:park:grassy | True | medium |
| cf7 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf8 | event_role | hold | agent | man |  | event_role:hold:agent:man | True | medium |
| cf9 | event_role | hold | patient | umbrella |  | event_role:hold:patient:umbrella | True | medium |
| cf10 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf11 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf12 | action_event | read |  |  | text_interaction_action, visual_action | action_event:read | True | medium |
| cf13 | event_role | read | agent | sign |  | event_role:read:agent:sign | True | medium |
| cf14 | event_role | read | patient |  |  | event_role:read:patient | False | medium |
| cf15 | relation | man | next_to | sign | spatial_proximity, visual_relation | relation:man:next_to:sign | True | high |
| cf16 | relation | man | in | park | spatial_containment, visual_relation | relation:man:in:park | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e8 |  |  |  | {"canonical": "next_to", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e8", "raw_relation": "beside", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 52

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `2abf634f1e2fadbc15793d84fb42b2c069992fa23cafc566cc5be2e943246814`
**parse_path:** `sentence`

> A boy in a yellow jersey kicks a soccer ball on a green field. Another player in a white jersey with the number 10 runs nearby, while other children and adults are visible in the background near a fence and building.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | boy | boy | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | jersey | jersey | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | yellow | yellow | color_attribute | chunk1 | 4 | high |
| m3 | object | soccer ball | soccer_ball | noun_chunk_root | chunk2 | 8 | high |
| m4 | object | field | field | noun_chunk_root | chunk3 | 12 | high |
| m5 | attribute | green | green | color_attribute | chunk3 | 11 | high |
| m6 | object | player | player | noun_chunk_root | chunk4 | 15 | high |
| m7 | object | jersey | jersey | noun_chunk_root | chunk5 | 19 | high |
| m8 | attribute | white | white | color_attribute | chunk5 | 18 | high |
| m9 | object | number | number | noun_chunk_root | chunk6 | 22 | high |
| m10 | object | children | child | noun_chunk_root | chunk7 | 29 | high |
| m11 | attribute | other | other | modifier_attribute | chunk7 | 28 | medium |
| m12 | object | adults | adult | noun_chunk_root | chunk8 | 31 | high |
| m13 | context | background | background | scene_context | chunk9 | 36 | high |
| m14 | object | fence | fence | noun_chunk_root | chunk10 | 39 | high |
| m15 | object | building | building | noun_chunk_root | chunk11 | 41 | high |
| m16 | action | kicks | kick | verb_predicate | doc | 6 | high |
| m17 | action | runs | run | verb_predicate | doc | 24 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> jersey |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> field |
| e2 | has_attribute | m7 | m8 | high | chunk5 amod -> jersey |
| e3 | has_attribute | m10 | m11 | medium | chunk7 amod -> children |
| e4 | has_context | scene | m13 | high | scene_context token background |
| e5 | agent | m16 | m0 | medium | nsubj -> kicks |
| e6 | patient | m16 | m3 | medium | dobj -> kicks |
| e7 | agent | m17 | m6 | medium | nsubj -> runs |
| e8 | relation | m0 | m1 | high | in |
| e9 | relation | m0 | m4 | high | on |
| e10 | relation | m6 | m7 | high | in |
| e11 | relation | m7 | m9 | high | with |
| e12 | relation | m10 | m13 | high | in |
| e13 | relation | m10 | m14 | high | near |
| e14 | relation | m10 | m15 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | boy | boy | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:boy", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | jersey | jersey | clothing | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:jersey", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | soccer_ball | soccer ball | object | ball, sports_equipment, artifact | m3 | raw_mention |  |  |  | True | {"canonical": "entity:soccer_ball", "parents": ["entity_parent:ball", "entity_parent:sports_equipment", "entity_parent:artifact"]} |
| ent_m4 | object | field | field | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |
| ent_m6 | object | player | player | person | person, human | m6 | raw_mention |  |  |  | True | {"canonical": "entity:player", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m7 | object | jersey | jersey | clothing | clothing, wearable | m7 | raw_mention |  |  |  | True | {"canonical": "entity:jersey", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m9 | object | number | number | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:number", "parents": []} |
| ent_m10 | object | child | children | person | person, human | m10 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m12 | object | adult | adults | person | person, human | m12 | raw_mention |  |  |  | True | {"canonical": "entity:adult", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m13 | context | background | background | object | scene_context | m13 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m14 | object | fence | fence | object |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:fence", "parents": []} |
| ent_m15 | object | building | building | object |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | kicks | kick | kick | visual_action |  | agent:m0->ent_m0; patient:m3->ent_m3 | {"canonical": "action:kick", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m17 | runs | run | run | locomotion_action, visual_action |  | agent:m6->ent_m6 | {"canonical": "action:run", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | kick | agent | m0 | ent_m0 | medium | e5 | nsubj -> kicks |  |  |
| ce0 | kick | patient | m3 | ent_m3 | medium | e6 | dobj -> kicks |  |  |
| ce1 | run | agent | m6 | ent_m6 | medium | e7 | nsubj -> runs |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | spatial_containment, visual_relation | high | e8 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | on | spatial_support, visual_relation | high | e9 | False | False |  |  |
| cr2 | m6 | m7 | ent_m6 | ent_m7 | in | in | spatial_containment, visual_relation | high | e10 | False | False |  |  |
| cr3 | m7 | m9 | ent_m7 | ent_m9 | with | with | association_relation, visual_relation | high | e11 | False | False |  |  |
| cr4 | m10 | m13 | ent_m10 | ent_m13 | in | in | spatial_containment, visual_relation | high | e12 | False | False |  |  |
| cr5 | m10 | m14 | ent_m10 | ent_m14 | near | near | spatial_proximity, visual_relation | high | e13 | False | False |  |  |
| cr6 | m10 | m15 | ent_m10 | ent_m15 | near | near | spatial_proximity, visual_relation | high | e14 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | boy |  |  | person, human | entity_exists:boy | True | high |
| cf1 | entity_exists | jersey |  |  | clothing, wearable | entity_exists:jersey | True | high |
| cf2 | entity_exists | soccer_ball |  |  | ball, sports_equipment, artifact | entity_exists:soccer_ball | True | high |
| cf3 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf4 | entity_exists | player |  |  | person, human | entity_exists:player | True | high |
| cf5 | entity_exists | jersey |  |  | clothing, wearable | entity_exists:jersey | True | high |
| cf6 | entity_exists | number |  |  |  | entity_exists:number | True | low |
| cf7 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf8 | entity_exists | adult |  |  | person, human | entity_exists:adult | True | high |
| cf9 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf10 | entity_exists | fence |  |  |  | entity_exists:fence | True | low |
| cf11 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf12 | has_attribute | jersey | yellow |  | color_attribute, color, visual_attribute | has_attribute:jersey:yellow | True | high |
| cf13 | has_attribute | field | green |  | color_attribute, color, visual_attribute | has_attribute:field:green | True | high |
| cf14 | has_attribute | jersey | white |  | color_attribute, color, visual_attribute | has_attribute:jersey:white | True | high |
| cf15 | has_attribute | child | other |  | modifier_attribute, visual_attribute | has_attribute:child:other | True | medium |
| cf16 | action_event | kick |  |  | visual_action | action_event:kick | True | low |
| cf17 | event_role | kick | agent | boy |  | event_role:kick:agent:boy | True | medium |
| cf18 | event_role | kick | patient | soccer_ball |  | event_role:kick:patient:soccer_ball | True | medium |
| cf19 | action_event | run |  |  | locomotion_action, visual_action | action_event:run | True | high |
| cf20 | event_role | run | agent | player |  | event_role:run:agent:player | True | medium |
| cf21 | relation | boy | in | jersey | spatial_containment, visual_relation | relation:boy:in:jersey | True | high |
| cf22 | relation | boy | on | field | spatial_support, visual_relation | relation:boy:on:field | True | high |
| cf23 | relation | player | in | jersey | spatial_containment, visual_relation | relation:player:in:jersey | True | high |
| cf24 | relation | jersey | with | number | association_relation, visual_relation | relation:jersey:with:number | True | high |
| cf25 | relation | child | in | background | spatial_containment, visual_relation | relation:child:in:background | True | high |
| cf26 | relation | child | near | fence | spatial_proximity, visual_relation | relation:child:near:fence | True | high |
| cf27 | relation | child | near | building | spatial_proximity, visual_relation | relation:child:near:building | True | high |

### Stage 9 Canonicalization Notes
_none_

## 53

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `2cd35fda2e263d175868d6361038cddb75310861b6ff222d7924305a5e347c14`
**parse_path:** `tag_list`

> green balloons, yellow balloons, party decor

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | balloons | balloon | segment_head | t0 | 1 | high |
| m1 | attribute | green | green | attribute | t0 | 0 | high |
| m2 | object | balloons | balloon | segment_head | t1 | 1 | high |
| m3 | attribute | yellow | yellow | attribute | t1 | 0 | high |
| m4 | object | decor | decor | segment_head | t2 | 1 | high |
| m5 | attribute | party | party | attribute | t2 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> balloons |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> balloons |
| e2 | has_attribute | m4 | m5 | high | t2 internal compound -> decor |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | balloon | balloons | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:balloon", "parents": []} |
| ent_m2 | object | balloon | balloons | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:balloon", "parents": []} |
| ent_m4 | object | decor | decor | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:decor", "parents": []} |

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
| cf0 | entity_exists | balloon |  |  |  | entity_exists:balloon | True | low |
| cf1 | entity_exists | balloon |  |  |  | entity_exists:balloon | True | low |
| cf2 | entity_exists | decor |  |  |  | entity_exists:decor | True | low |
| cf3 | has_attribute | balloon | green |  | color_attribute, color, visual_attribute | has_attribute:balloon:green | True | high |
| cf4 | has_attribute | balloon | yellow |  | color_attribute, color, visual_attribute | has_attribute:balloon:yellow | True | high |
| cf5 | has_attribute | decor | party |  | attribute, visual_attribute | has_attribute:decor:party | True | high |

### Stage 9 Canonicalization Notes
_none_

## 54

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `2dfa309f889152f451bddf6323a66c94e8d9d743da86609cddd26af1ccd00c14`
**parse_path:** `tag_list`

> glass lamp, black and white, reflective surface, cracked glass, bulb

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | lamp | lamp | segment_head | t0 | 1 | high |
| m1 | attribute | glass | glass | attribute | t0 | 0 | high |
| m2 | attribute | black | black | color_attribute | t1 | 0 | high |
| m3 | attribute | white | white | color_attribute | t1 | 2 | high |
| m4 | object | surface | surface | segment_head | t2 | 1 | high |
| m5 | attribute | reflective | reflective | attribute | t2 | 0 | high |
| m6 | object | glass | glass | segment_head | t3 | 1 | high |
| m7 | attribute | cracked | crack | state_attribute | t3 | 0 | high |
| m8 | object | bulb | bulb | segment_head | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> lamp |
| e1 | candidate_has_attribute | m0 | m2 | low | t1 adjacent floating attribute |
| e2 | candidate_has_attribute | m0 | m3 | low | t1 adjacent floating attribute |
| e3 | has_attribute | m4 | m5 | high | t2 internal amod -> surface |
| e4 | has_attribute | m6 | m7 | high | t3 internal amod -> glass |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | lamp | lamp | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:lamp", "parents": []} |
| ent_m4 | object | surface | surface | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": []} |
| ent_m6 | object | glass | glass | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:glass", "parents": []} |
| ent_m8 | object | bulb | bulb | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:bulb", "parents": []} |

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
| cf0 | entity_exists | lamp |  |  |  | entity_exists:lamp | True | low |
| cf1 | entity_exists | surface |  |  |  | entity_exists:surface | True | low |
| cf2 | entity_exists | glass |  |  |  | entity_exists:glass | True | low |
| cf3 | entity_exists | bulb |  |  |  | entity_exists:bulb | True | low |
| cf4 | has_attribute | lamp | glass |  | material_attribute, material, visual_attribute | has_attribute:lamp:glass | True | high |
| cf5 | candidate_has_attribute | lamp | black |  | color_attribute, color, visual_attribute | candidate_has_attribute:lamp:black | False | low |
| cf6 | candidate_has_attribute | lamp | white |  | color_attribute, color, visual_attribute | candidate_has_attribute:lamp:white | False | low |
| cf7 | has_attribute | surface | reflective |  | attribute, visual_attribute | has_attribute:surface:reflective | True | high |
| cf8 | has_attribute | glass | cracked |  | texture_attribute, state, texture, visual_attribute | has_attribute:glass:cracked | True | high |

### Stage 9 Canonicalization Notes
_none_

## 55

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `2e4e7755258469126a5cba139a7f39e0d9ea63233ac4a7cae2d43cde2adb7c14`
**parse_path:** `sentence`

> A Mercedes-Benz building with several cars parked in front. Blue pillars and glass windows are visible.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | Mercedes-Benz | mercedes-benz | compound_modifier | chunk0 | 1 | medium |
| m2 | object | cars | car | noun_chunk_root | chunk1 | 5 | high |
| m3 | quantity | several | several | approximate_quantity | chunk1 | 4 | medium |
| m4 | context | front | front | spatial_region | chunk2 | 8 | medium |
| m5 | object | pillars | pillar | noun_chunk_root | chunk3 | 11 | high |
| m6 | attribute | Blue | blue | color_attribute | chunk3 | 10 | high |
| m7 | object | windows | window | noun_chunk_root | chunk4 | 14 | high |
| m8 | attribute | glass | glass | material_attribute | chunk4 | 13 | high |
| m9 | action | parked | park | verb_predicate | doc | 6 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 compound -> building |
| e1 | has_quantity | m2 | m3 | medium | chunk1 quantity -> cars |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> pillars |
| e3 | has_attribute | m7 | m8 | high | chunk4 compound -> windows |
| e4 | agent | m9 | m2 | medium | inherited agent acl -> cars |
| e5 | relation | m0 | m2 | high | with |
| e6 | relation | m2 | m4 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | building | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m2 | object | car | cars | vehicle | vehicle | m2 | raw_mention |  |  |  | True | {"canonical": "entity:car", "parents": ["entity_parent:vehicle"]} |
| ent_m4 | context | front | front | object | scene_context | m4 | raw_mention |  |  |  | True | {"canonical": "entity:front", "parents": ["entity_parent:scene_context"]} |
| ent_m5 | object | pillar | pillars | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:pillar", "parents": []} |
| ent_m7 | object | window | windows | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:window", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | parked | park | park | visual_action |  | agent:m2->ent_m2 | {"canonical": "action:park", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | park | agent | m2 | ent_m2 | medium | e4 | inherited agent acl -> cars |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e5 | False | False |  |  |
| cr1 | m2 | m4 | ent_m2 | ent_m4 | in | in | spatial_containment, visual_relation | high | e6 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf1 | entity_exists | car |  |  | vehicle | entity_exists:car | True | high |
| cf2 | entity_exists | front |  |  | scene_context | entity_exists:front | True | medium |
| cf3 | entity_exists | pillar |  |  |  | entity_exists:pillar | True | low |
| cf4 | entity_exists | window |  |  |  | entity_exists:window | True | low |
| cf5 | has_attribute | building | mercedes-benz |  | compound_modifier, visual_attribute | has_attribute:building:mercedes-benz | True | medium |
| cf6 | has_quantity | car | several |  | approximate_quantity, quantity | has_quantity:car:several | True | medium |
| cf7 | has_attribute | pillar | blue |  | color_attribute, color, visual_attribute | has_attribute:pillar:blue | True | high |
| cf8 | has_attribute | window | glass |  | material_attribute, material, visual_attribute | has_attribute:window:glass | True | high |
| cf9 | action_event | park |  |  | visual_action | action_event:park | True | low |
| cf10 | event_role | park | agent | car |  | event_role:park:agent:car | True | medium |
| cf11 | relation | building | with | car | association_relation, visual_relation | relation:building:with:car | True | high |
| cf12 | relation | car | in | front | spatial_containment, visual_relation | relation:car:in:front | True | high |

### Stage 9 Canonicalization Notes
_none_

## 56

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `2e7e96b37fb008c7a81a490d20b0e27c614469755665c93183a59dff62163014`
**parse_path:** `sentence`

> Green fields and trees stretch across a valley under a cloudy sky. Pine trees frame the foreground.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | fields | field | noun_chunk_root | chunk0 | 1 | high |
| m1 | attribute | Green | green | color_attribute | chunk0 | 0 | high |
| m2 | object | trees | tree | noun_chunk_root | chunk1 | 3 | high |
| m3 | object | valley | valley | noun_chunk_root | chunk2 | 7 | high |
| m4 | object | sky | sky | noun_chunk_root | chunk3 | 11 | high |
| m5 | attribute | cloudy | cloudy | modifier_attribute | chunk3 | 10 | medium |
| m6 | object | Pine trees | pine_tree | noun_chunk_root | chunk4 | 13 | high |
| m7 | context | foreground | foreground | scene_context | chunk5 | 16 | high |
| m8 | action | stretch | stretch | verb_predicate | doc | 4 | high |
| m9 | action | frame | frame | verb_predicate | doc | 14 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> fields |
| e1 | has_attribute | m4 | m5 | medium | chunk3 amod -> sky |
| e2 | has_context | scene | m7 | high | scene_context token foreground |
| e3 | agent | m8 | m0 | medium | nsubj -> stretch |
| e4 | agent | m8 | m2 | medium | nsubj -> stretch |
| e5 | agent | m9 | m6 | medium | nsubj -> frame |
| e6 | patient | m9 | m7 | medium | dobj -> frame |
| e7 | relation | m0 | m3 | high | across |
| e8 | relation | m0 | m4 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | field | fields | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |
| ent_m2 | object | tree | trees | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m3 | object | valley | valley | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:valley", "parents": []} |
| ent_m4 | object | sky | sky | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m6 | object | pine_tree | Pine trees | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:pine_tree", "parents": []} |
| ent_m7 | context | foreground | foreground | object | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:foreground", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | stretch | stretch | stretch | visual_action |  | agent:m0->ent_m0; agent:m2->ent_m2 | {"canonical": "action:stretch", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m9 | frame | frame | frame | visual_action |  | agent:m6->ent_m6; patient:m7->ent_m7 | {"canonical": "action:frame", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stretch | agent | m0 | ent_m0 | medium | e3 | nsubj -> stretch |  |  |
| ce0 | stretch | agent | m2 | ent_m2 | medium | e4 | nsubj -> stretch |  |  |
| ce1 | frame | agent | m6 | ent_m6 | medium | e5 | nsubj -> frame |  |  |
| ce1 | frame | patient | m7 | ent_m7 | medium | e6 | dobj -> frame |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | across | across | spatial_path, visual_relation | high | e7 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | under | under | spatial_vertical, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf1 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf2 | entity_exists | valley |  |  |  | entity_exists:valley | True | low |
| cf3 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf4 | entity_exists | pine_tree |  |  |  | entity_exists:pine_tree | True | low |
| cf5 | entity_exists | foreground |  |  | scene_context | entity_exists:foreground | True | high |
| cf6 | has_attribute | field | green |  | color_attribute, color, visual_attribute | has_attribute:field:green | True | high |
| cf7 | has_attribute | sky | cloudy |  | weather_attribute, weather, visual_attribute | has_attribute:sky:cloudy | True | medium |
| cf8 | action_event | stretch |  |  | visual_action | action_event:stretch | True | low |
| cf9 | event_role | stretch | agent | field |  | event_role:stretch:agent:field | True | medium |
| cf10 | event_role | stretch | agent | tree |  | event_role:stretch:agent:tree | True | medium |
| cf11 | action_event | frame |  |  | visual_action | action_event:frame | True | low |
| cf12 | event_role | frame | agent | pine_tree |  | event_role:frame:agent:pine_tree | True | medium |
| cf13 | event_role | frame | patient | foreground |  | event_role:frame:patient:foreground | True | medium |
| cf14 | relation | field | across | valley | spatial_path, visual_relation | relation:field:across:valley | True | high |
| cf15 | relation | field | under | sky | spatial_vertical, visual_relation | relation:field:under:sky | True | high |

### Stage 9 Canonicalization Notes
_none_

## 57

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `2f1810981f1e7a25986b6d3d1b18205489e3d0812d69ac51e9f4121a83be3814`
**parse_path:** `sentence`

> A small, weathered orange-brown artifact with a rounded top and flat base rests on a white surface. Below it, a scale marker reads "50 mm," indicating its size. The object appears to be an ancient or archaeological fragment.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "50 mm," | 50_mm, | quote_text | doc_quote | 26 | high |
| m1 | object | artifact | artifact | noun_chunk_root | chunk0 | 5 | high |
| m2 | attribute | small | small | size_attribute | chunk0 | 1 | high |
| m3 | attribute | weathered | weathered | modifier_attribute | chunk0 | 3 | medium |
| m4 | attribute | orange-brown | orange-brown | modifier_attribute | chunk0 | 4 | medium |
| m5 | context | top | top | spatial_region | chunk1 | 9 | medium |
| m6 | object | base | base | noun_chunk_root | chunk2 | 12 | high |
| m7 | attribute | flat | flat | modifier_attribute | chunk2 | 11 | medium |
| m8 | context | surface | surface | spatial_region | chunk3 | 17 | medium |
| m9 | object | marker | marker | noun_chunk_root | chunk5 | 24 | high |
| m10 | attribute | scale | scale | compound_modifier | chunk5 | 23 | medium |
| m11 | object | size | size | noun_chunk_root | chunk6 | 29 | high |
| m13 | object | fragment | fragment | noun_chunk_root | chunk8 | 40 | high |
| m14 | attribute | ancient | ancient | modifier_attribute | chunk8 | 37 | medium |
| m15 | attribute | archaeological | archaeological | modifier_attribute | chunk8 | 39 | medium |
| m16 | reference | The object | object | generic_object_reference | generic_anaphoric | 32 | high |
| m17 | action | rests | rest | verb_predicate | doc | 13 | high |
| m18 | action | reads | read | verb_predicate | doc | 25 | high |
| m19 | action | indicating | indicate | verb_predicate | doc | 27 | high |
| m20 | action | appears | appear | verb_predicate | doc | 33 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk0 amod -> artifact |
| e1 | has_attribute | m1 | m3 | medium | chunk0 amod -> artifact |
| e2 | has_attribute | m1 | m4 | medium | chunk0 amod -> artifact |
| e3 | has_attribute | m6 | m7 | medium | chunk2 amod -> base |
| e4 | has_attribute | m9 | m10 | medium | chunk5 compound -> marker |
| e5 | has_attribute | m13 | m14 | medium | chunk8 amod -> fragment |
| e6 | has_attribute | m13 | m15 | medium | chunk8 conj -> fragment |
| e7 | refers_to | m16 | m1 | high | generic definite NP score=132 margin=30 |
| e8 | agent | m17 | m1 | medium | nsubj -> rests |
| e9 | agent | m18 | m9 | medium | nsubj -> reads |
| e10 | agent | m19 | m9 | medium | inherited agent advcl -> reads |
| e11 | patient | m19 | m11 | medium | dobj -> indicating |
| e12 | agent | m20 | m1 | medium | nsubj -> appears; resolved object -> artifact |
| e13 | relation | m1 | m5 | high | with |
| e14 | relation | m1 | m6 | high | with |
| e15 | relation | m1 | m8 | high | on |
| e16 | relation | m9 | m1 | high | below |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | artifact | artifact | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:artifact", "parents": []} |
| ent_m5 | context | top | top | object | scene_context | m5 | raw_mention |  |  |  | True | {"canonical": "entity:top", "parents": ["entity_parent:scene_context"]} |
| ent_m6 | object | base | base | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:base", "parents": []} |
| ent_m8 | context | surface | surface | object | scene_context | m8 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": ["entity_parent:scene_context"]} |
| ent_m9 | object | marker | marker | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:marker", "parents": []} |
| ent_m11 | object | size | size | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:size", "parents": []} |
| ent_m13 | object | fragment | fragment | object |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:fragment", "parents": []} |
| eref_m16 | reference | artifact | The object | object |  | m16 | stage9_reference | ent_m1 |  |  | True | {"canonical": "entity:artifact", "parents": []} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m16 | eref_m16 | m1 | ent_m1 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | rests | rest | rest | visual_action |  | agent:m1->ent_m1 | {"canonical": "action:rest", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m18 | reads | read | read | text_interaction_action, visual_action |  | agent:m9->ent_m9 | {"canonical": "action:read", "parents": ["action_parent:text_interaction_action", "action_parent:visual_action"]} |  |
| ce2 | m19 | indicating | indicate | indicate | visual_action |  | agent:m9->ent_m9; patient:m11->ent_m11 | {"canonical": "action:indicate", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m20 | appears | appear | appear | visual_action |  | agent:m1->ent_m1 | {"canonical": "action:appear", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | rest | agent | m1 | ent_m1 | medium | e8 | nsubj -> rests |  |  |
| ce1 | read | agent | m9 | ent_m9 | medium | e9 | nsubj -> reads |  |  |
| ce2 | indicate | agent | m9 | ent_m9 | medium | e10 | inherited agent advcl -> reads |  |  |
| ce2 | indicate | patient | m11 | ent_m11 | medium | e11 | dobj -> indicating |  |  |
| ce3 | appear | agent | m1 | ent_m1 | medium | e12 | nsubj -> appears; resolved object -> artifact |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m5 | ent_m1 | ent_m5 | with | with | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr1 | m1 | m6 | ent_m1 | ent_m6 | with | with | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr2 | m1 | m8 | ent_m1 | ent_m8 | on | on | spatial_support, visual_relation | high | e15 | False | False |  |  |
| cr3 | m9 | m1 | ent_m9 | ent_m1 | below | below | spatial_vertical, visual_relation | high | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | artifact |  |  |  | entity_exists:artifact | True | low |
| cf1 | entity_exists | top |  |  | scene_context | entity_exists:top | True | medium |
| cf2 | entity_exists | base |  |  |  | entity_exists:base | True | low |
| cf3 | entity_exists | surface |  |  | scene_context | entity_exists:surface | True | medium |
| cf4 | entity_exists | marker |  |  |  | entity_exists:marker | True | low |
| cf5 | entity_exists | size |  |  |  | entity_exists:size | True | low |
| cf6 | entity_exists | fragment |  |  |  | entity_exists:fragment | True | low |
| cf7 | entity_exists | artifact |  |  |  | entity_exists:artifact | True | low |
| cf8 | has_attribute | artifact | small |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:artifact:small | True | high |
| cf9 | has_attribute | artifact | weathered |  | state_attribute, state, visual_attribute | has_attribute:artifact:weathered | True | medium |
| cf10 | has_attribute | artifact | orange-brown |  | modifier_attribute, visual_attribute | has_attribute:artifact:orange-brown | True | medium |
| cf11 | has_attribute | base | flat |  | shape_attribute, coco_subtype_rule, visual_attribute | has_attribute:base:flat | True | medium |
| cf12 | has_attribute | marker | scale |  | compound_modifier, visual_attribute | has_attribute:marker:scale | True | medium |
| cf13 | has_attribute | fragment | ancient |  | modifier_attribute, visual_attribute | has_attribute:fragment:ancient | True | medium |
| cf14 | has_attribute | fragment | archaeological |  | modifier_attribute, visual_attribute | has_attribute:fragment:archaeological | True | medium |
| cf15 | action_event | rest |  |  | visual_action | action_event:rest | True | low |
| cf16 | event_role | rest | agent | artifact |  | event_role:rest:agent:artifact | True | medium |
| cf17 | action_event | read |  |  | text_interaction_action, visual_action | action_event:read | True | medium |
| cf18 | event_role | read | agent | marker |  | event_role:read:agent:marker | True | medium |
| cf19 | action_event | indicate |  |  | visual_action | action_event:indicate | True | low |
| cf20 | event_role | indicate | agent | marker |  | event_role:indicate:agent:marker | True | medium |
| cf21 | event_role | indicate | patient | size |  | event_role:indicate:patient:size | True | medium |
| cf22 | action_event | appear |  |  | visual_action | action_event:appear | True | low |
| cf23 | event_role | appear | agent | artifact |  | event_role:appear:agent:artifact | True | medium |
| cf24 | relation | artifact | with | top | association_relation, visual_relation | relation:artifact:with:top | True | high |
| cf25 | relation | artifact | with | base | association_relation, visual_relation | relation:artifact:with:base | True | high |
| cf26 | relation | artifact | on | surface | spatial_support, visual_relation | relation:artifact:on:surface | True | high |
| cf27 | relation | marker | below | artifact | spatial_vertical, visual_relation | relation:marker:below:artifact | True | high |

### Stage 9 Canonicalization Notes
_none_

## 58

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `2f295fa7a4dda24b537ab1663d4e055c2255d51e5b9d545e3e0b84827872d414`
**parse_path:** `sentence`

> Tall trees with rough bark stand in a forest clearing, their branches filtering sunlight onto the ground. Green bushes and dry leaves cover the forest floor, with dappled light creating bright spots among the shadows. The scene is quiet and natural, surrounded by dense woodland.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | trees | tree | noun_chunk_root | chunk0 | 1 | high |
| m1 | attribute | Tall | tall | size_attribute | chunk0 | 0 | high |
| m2 | object | bark | bark | noun_chunk_root | chunk1 | 4 | high |
| m3 | attribute | rough | rough | modifier_attribute | chunk1 | 3 | medium |
| m4 | object | clearing | clearing | noun_chunk_root | chunk2 | 9 | high |
| m5 | attribute | forest | forest | compound_modifier | chunk2 | 8 | medium |
| m6 | object | branches | branch | noun_chunk_root | chunk3 | 12 | high |
| m7 | object | sunlight | sunlight | noun_chunk_root | chunk4 | 14 | high |
| m8 | object | ground | ground | noun_chunk_root | chunk5 | 17 | high |
| m9 | object | bushes | bush | noun_chunk_root | chunk6 | 20 | high |
| m10 | attribute | Green | green | color_attribute | chunk6 | 19 | high |
| m11 | object | leaves | leaf | noun_chunk_root | chunk7 | 23 | high |
| m12 | attribute | dry | dry | modifier_attribute | chunk7 | 22 | medium |
| m13 | object | floor | floor | noun_chunk_root | chunk8 | 27 | high |
| m14 | attribute | forest | forest | compound_modifier | chunk8 | 26 | medium |
| m15 | object | light | light | noun_chunk_root | chunk9 | 31 | high |
| m16 | attribute | dappled | dappled | modifier_attribute | chunk9 | 30 | medium |
| m17 | object | spots | spot | noun_chunk_root | chunk10 | 34 | high |
| m18 | attribute | bright | bright | visual_attribute | chunk10 | 33 | medium |
| m19 | object | shadows | shadow | noun_chunk_root | chunk11 | 37 | high |
| m20 | context | scene | scene | scene_context | chunk12 | 40 | high |
| m21 | object | woodland | woodland | noun_chunk_root | chunk13 | 49 | high |
| m22 | attribute | dense | dense | modifier_attribute | chunk13 | 48 | medium |
| m23 | action | stand | stand | verb_predicate | doc | 5 | high |
| m24 | action | filtering | filter | verb_predicate | doc | 13 | high |
| m25 | action | cover | cover | verb_predicate | doc | 24 | high |
| m26 | action | creating | create | verb_predicate | doc | 32 | high |
| m27 | action | surrounded | surround | verb_predicate | doc | 46 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> trees |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> bark |
| e2 | has_attribute | m4 | m5 | medium | chunk2 compound -> clearing |
| e3 | has_attribute | m9 | m10 | high | chunk6 amod -> bushes |
| e4 | has_attribute | m11 | m12 | medium | chunk7 amod -> leaves |
| e5 | has_attribute | m13 | m14 | medium | chunk8 compound -> floor |
| e6 | has_attribute | m15 | m16 | medium | chunk9 amod -> light |
| e7 | has_attribute | m17 | m18 | medium | chunk10 amod -> spots |
| e8 | has_context | scene | m20 | high | scene_context token scene |
| e9 | has_attribute | m21 | m22 | medium | chunk13 amod -> woodland |
| e10 | agent | m23 | m0 | medium | nsubj -> stand |
| e11 | agent | m24 | m6 | medium | nsubj -> filtering |
| e12 | patient | m24 | m7 | medium | dobj -> filtering |
| e13 | agent | m25 | m9 | medium | nsubj -> cover |
| e14 | agent | m25 | m11 | medium | nsubj -> cover |
| e15 | patient | m25 | m13 | medium | dobj -> cover |
| e16 | agent | m26 | m15 | medium | nsubj -> creating |
| e17 | patient | m26 | m17 | medium | dobj -> creating |
| e18 | agent | m27 | m20 | medium | inherited agent advcl -> is |
| e19 | relation | m0 | m2 | high | with |
| e20 | relation | m0 | m4 | high | in |
| e21 | relation | m6 | m8 | medium | onto |
| e22 | relation | m15 | m19 | medium | among |
| e23 | relation | m20 | m21 | medium | by |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | tree | trees | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m2 | object | bark | bark | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:bark", "parents": []} |
| ent_m4 | object | clearing | clearing | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:clearing", "parents": []} |
| ent_m6 | object | branch | branches | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:branch", "parents": []} |
| ent_m7 | object | sunlight | sunlight | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:sunlight", "parents": []} |
| ent_m8 | object | ground | ground | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:ground", "parents": []} |
| ent_m9 | object | bush | bushes | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:bush", "parents": []} |
| ent_m11 | object | leaf | leaves | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:leaf", "parents": []} |
| ent_m13 | object | floor | floor | object |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:floor", "parents": []} |
| ent_m15 | object | light | light | object |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:light", "parents": []} |
| ent_m17 | object | spot | spots | object |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:spot", "parents": []} |
| ent_m19 | object | shadow | shadows | object |  | m19 | raw_mention |  |  |  | True | {"canonical": "entity:shadow", "parents": []} |
| ent_m20 | context | scene | scene | object | scene_context | m20 | raw_mention |  |  |  | True | {"canonical": "entity:scene", "parents": ["entity_parent:scene_context"]} |
| ent_m21 | object | woodland | woodland | object |  | m21 | raw_mention |  |  |  | True | {"canonical": "entity:woodland", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m23 | stand | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m24 | filtering | filter | filter | visual_action |  | agent:m6->ent_m6; patient:m7->ent_m7 | {"canonical": "action:filter", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m25 | cover | cover | cover | visual_action |  | agent:m9->ent_m9; agent:m11->ent_m11; patient:m13->ent_m13 | {"canonical": "action:cover", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m26 | creating | create | create | visual_action |  | agent:m15->ent_m15; patient:m17->ent_m17 | {"canonical": "action:create", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m27 | surrounded | surround | surround | visual_action |  | agent:m20->ent_m20 | {"canonical": "action:surround", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e10 | nsubj -> stand |  |  |
| ce1 | filter | agent | m6 | ent_m6 | medium | e11 | nsubj -> filtering |  |  |
| ce1 | filter | patient | m7 | ent_m7 | medium | e12 | dobj -> filtering |  |  |
| ce2 | cover | agent | m9 | ent_m9 | medium | e13 | nsubj -> cover |  |  |
| ce2 | cover | agent | m11 | ent_m11 | medium | e14 | nsubj -> cover |  |  |
| ce2 | cover | patient | m13 | ent_m13 | medium | e15 | dobj -> cover |  |  |
| ce3 | create | agent | m15 | ent_m15 | medium | e16 | nsubj -> creating |  |  |
| ce3 | create | patient | m17 | ent_m17 | medium | e17 | dobj -> creating |  |  |
| ce4 | surround | agent | m20 | ent_m20 | medium | e18 | inherited agent advcl -> is |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e19 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | in | in | spatial_containment, visual_relation | high | e20 | False | False |  |  |
| cr2 | m6 | m8 | ent_m6 | ent_m8 | onto | on | spatial_support, visual_relation | medium | e21 | False | False |  |  |
| cr3 | m15 | m19 | ent_m15 | ent_m19 | among | among | spatial_region, visual_relation | medium | e22 | False | False |  |  |
| cr4 | m20 | m21 | ent_m20 | ent_m21 | by | by | spatial_proximity, visual_relation | medium | e23 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf1 | entity_exists | bark |  |  |  | entity_exists:bark | True | low |
| cf2 | entity_exists | clearing |  |  |  | entity_exists:clearing | True | low |
| cf3 | entity_exists | branch |  |  |  | entity_exists:branch | True | low |
| cf4 | entity_exists | sunlight |  |  |  | entity_exists:sunlight | True | low |
| cf5 | entity_exists | ground |  |  |  | entity_exists:ground | True | low |
| cf6 | entity_exists | bush |  |  |  | entity_exists:bush | True | low |
| cf7 | entity_exists | leaf |  |  |  | entity_exists:leaf | True | low |
| cf8 | entity_exists | floor |  |  |  | entity_exists:floor | True | low |
| cf9 | entity_exists | light |  |  |  | entity_exists:light | True | low |
| cf10 | entity_exists | spot |  |  |  | entity_exists:spot | True | low |
| cf11 | entity_exists | shadow |  |  |  | entity_exists:shadow | True | low |
| cf12 | entity_exists | scene |  |  | scene_context | entity_exists:scene | True | high |
| cf13 | entity_exists | woodland |  |  |  | entity_exists:woodland | True | low |
| cf14 | has_attribute | tree | tall |  | size_attribute, height, visual_attribute | has_attribute:tree:tall | True | high |
| cf15 | has_attribute | bark | rough |  | texture_attribute, texture, visual_attribute | has_attribute:bark:rough | True | medium |
| cf16 | has_attribute | clearing | forest |  | compound_modifier, visual_attribute | has_attribute:clearing:forest | True | medium |
| cf17 | has_attribute | bush | green |  | color_attribute, color, visual_attribute | has_attribute:bush:green | True | high |
| cf18 | has_attribute | leaf | dry |  | state_attribute, clean_exact_overlap, state, visual_attribute | has_attribute:leaf:dry | True | medium |
| cf19 | has_attribute | floor | forest |  | compound_modifier, visual_attribute | has_attribute:floor:forest | True | medium |
| cf20 | has_attribute | light | dappled |  | modifier_attribute, visual_attribute | has_attribute:light:dappled | True | medium |
| cf21 | has_attribute | spot | bright |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:spot:bright | True | medium |
| cf22 | has_attribute | woodland | dense |  | modifier_attribute, visual_attribute | has_attribute:woodland:dense | True | medium |
| cf23 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf24 | event_role | stand | agent | tree |  | event_role:stand:agent:tree | True | medium |
| cf25 | action_event | filter |  |  | visual_action | action_event:filter | True | low |
| cf26 | event_role | filter | agent | branch |  | event_role:filter:agent:branch | True | medium |
| cf27 | event_role | filter | patient | sunlight |  | event_role:filter:patient:sunlight | True | medium |
| cf28 | action_event | cover |  |  | visual_action | action_event:cover | True | low |
| cf29 | event_role | cover | agent | bush |  | event_role:cover:agent:bush | True | medium |
| cf30 | event_role | cover | agent | leaf |  | event_role:cover:agent:leaf | True | medium |
| cf31 | event_role | cover | patient | floor |  | event_role:cover:patient:floor | True | medium |
| cf32 | action_event | create |  |  | visual_action | action_event:create | True | low |
| cf33 | event_role | create | agent | light |  | event_role:create:agent:light | True | medium |
| cf34 | event_role | create | patient | spot |  | event_role:create:patient:spot | True | medium |
| cf35 | action_event | surround |  |  | visual_action | action_event:surround | True | low |
| cf36 | event_role | surround | agent | scene |  | event_role:surround:agent:scene | True | medium |
| cf37 | relation | tree | with | bark | association_relation, visual_relation | relation:tree:with:bark | True | high |
| cf38 | relation | tree | in | clearing | spatial_containment, visual_relation | relation:tree:in:clearing | True | high |
| cf39 | relation | branch | on | ground | spatial_support, visual_relation | relation:branch:on:ground | True | medium |
| cf40 | relation | light | among | shadow | spatial_region, visual_relation | relation:light:among:shadow | True | medium |
| cf41 | relation | scene | by | woodland | spatial_proximity, visual_relation | relation:scene:by:woodland | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e21 |  |  |  | {"canonical": "on", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e21", "raw_relation": "onto", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 59

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `3067f6b54759f2cb448fa4e611600ffbe88bd51c44e60b4c44d135baea3b2c14`
**parse_path:** `sentence`

> A softball player in a maroon uniform stands on a base as an umpire walks nearby. Spectators sit in chairs behind a fence in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | player | player | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | softball | softball | compound_modifier | chunk0 | 1 | medium |
| m2 | object | uniform | uniform | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | maroon | maroon | color_attribute | chunk1 | 5 | high |
| m4 | context | base | base | spatial_region | chunk2 | 10 | medium |
| m5 | object | umpire | umpire | noun_chunk_root | chunk3 | 13 | high |
| m6 | object | Spectators | spectator | noun_chunk_root | chunk4 | 17 | high |
| m7 | object | chairs | chair | noun_chunk_root | chunk5 | 20 | high |
| m8 | object | fence | fence | noun_chunk_root | chunk6 | 23 | high |
| m9 | context | background | background | scene_context | chunk7 | 26 | high |
| m10 | action | stands | stand | verb_predicate | doc | 7 | high |
| m11 | action | walks | walk | verb_predicate | doc | 14 | high |
| m12 | action | sit | sit | verb_predicate | doc | 18 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 compound -> player |
| e1 | has_attribute | m2 | m3 | high | chunk1 compound -> uniform |
| e2 | has_context | scene | m9 | high | scene_context token background |
| e3 | agent | m10 | m0 | medium | nsubj -> stands |
| e4 | agent | m11 | m5 | medium | nsubj -> walks |
| e5 | agent | m12 | m6 | medium | nsubj -> sit |
| e6 | relation | m0 | m2 | high | in |
| e7 | relation | m0 | m4 | high | on |
| e8 | relation | m6 | m7 | high | in |
| e9 | relation | m6 | m8 | high | behind |
| e10 | relation | m6 | m9 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | player | player | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:player", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | uniform | uniform | clothing | clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m4 | context | base | base | object | scene_context | m4 | raw_mention |  |  |  | True | {"canonical": "entity:base", "parents": ["entity_parent:scene_context"]} |
| ent_m5 | object | umpire | umpire | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:umpire", "parents": []} |
| ent_m6 | object | spectator | Spectators | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:spectator", "parents": []} |
| ent_m7 | object | chair | chairs | object | furniture, artifact | m7 | raw_mention |  |  |  | True | {"canonical": "entity:chair", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m8 | object | fence | fence | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:fence", "parents": []} |
| ent_m9 | context | background | background | object | scene_context | m9 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | stands | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m11 | walks | walk | walk | locomotion_action, visual_action |  | agent:m5->ent_m5 | {"canonical": "action:walk", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce2 | m12 | sit | sit | sit | body_pose_action, visual_action |  | agent:m6->ent_m6 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e3 | nsubj -> stands |  |  |
| ce1 | walk | agent | m5 | ent_m5 | medium | e4 | nsubj -> walks |  |  |
| ce2 | sit | agent | m6 | ent_m6 | medium | e5 | nsubj -> sit |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | spatial_containment, visual_relation | high | e6 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | on | spatial_support, visual_relation | high | e7 | False | False |  |  |
| cr2 | m6 | m7 | ent_m6 | ent_m7 | in | in | spatial_containment, visual_relation | high | e8 | False | False |  |  |
| cr3 | m6 | m8 | ent_m6 | ent_m8 | behind | behind | spatial_depth, visual_relation | high | e9 | False | False |  |  |
| cr4 | m6 | m9 | ent_m6 | ent_m9 | in | in | spatial_containment, visual_relation | high | e10 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | player |  |  | person, human | entity_exists:player | True | high |
| cf1 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf2 | entity_exists | base |  |  | scene_context | entity_exists:base | True | medium |
| cf3 | entity_exists | umpire |  |  |  | entity_exists:umpire | True | low |
| cf4 | entity_exists | spectator |  |  |  | entity_exists:spectator | True | low |
| cf5 | entity_exists | chair |  |  | furniture, artifact | entity_exists:chair | True | high |
| cf6 | entity_exists | fence |  |  |  | entity_exists:fence | True | low |
| cf7 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf8 | has_attribute | player | softball |  | compound_modifier, visual_attribute | has_attribute:player:softball | True | medium |
| cf9 | has_attribute | uniform | maroon |  | color_attribute, color, visual_attribute | has_attribute:uniform:maroon | True | high |
| cf10 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf11 | event_role | stand | agent | player |  | event_role:stand:agent:player | True | medium |
| cf12 | action_event | walk |  |  | locomotion_action, visual_action | action_event:walk | True | high |
| cf13 | event_role | walk | agent | umpire |  | event_role:walk:agent:umpire | True | medium |
| cf14 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf15 | event_role | sit | agent | spectator |  | event_role:sit:agent:spectator | True | medium |
| cf16 | relation | player | in | uniform | spatial_containment, visual_relation | relation:player:in:uniform | True | high |
| cf17 | relation | player | on | base | spatial_support, visual_relation | relation:player:on:base | True | high |
| cf18 | relation | spectator | in | chair | spatial_containment, visual_relation | relation:spectator:in:chair | True | high |
| cf19 | relation | spectator | behind | fence | spatial_depth, visual_relation | relation:spectator:behind:fence | True | high |
| cf20 | relation | spectator | in | background | spatial_containment, visual_relation | relation:spectator:in:background | True | high |

### Stage 9 Canonicalization Notes
_none_

## 60

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `3071b315a1e687d13684eb7dfce218b5cc007d8b21f2fd2ea5126c6308acf014`
**parse_path:** `sentence`

> A stone church with a cross on its tower stands under a blue sky. An arched entrance leads into the building.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | church | church | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | stone | stone | material_attribute | chunk0 | 1 | high |
| m2 | object | cross | cross | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | tower | tower | noun_chunk_root | chunk2 | 8 | high |
| m4 | object | sky | sky | noun_chunk_root | chunk3 | 13 | high |
| m5 | attribute | blue | blue | color_attribute | chunk3 | 12 | high |
| m6 | object | entrance | entrance | noun_chunk_root | chunk4 | 17 | high |
| m7 | attribute | arched | arched | visual_attribute | chunk4 | 16 | medium |
| m8 | object | building | building | noun_chunk_root | chunk5 | 21 | high |
| m9 | action | stands | stand | verb_predicate | doc | 9 | high |
| m10 | action | leads | lead | verb_predicate | doc | 18 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 compound -> church |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> sky |
| e2 | has_attribute | m6 | m7 | medium | chunk4 amod -> entrance |
| e3 | agent | m9 | m0 | medium | nsubj -> stands |
| e4 | agent | m10 | m6 | medium | nsubj -> leads |
| e5 | relation | m0 | m2 | high | with |
| e6 | relation | m2 | m3 | high | on |
| e7 | relation | m0 | m4 | high | under |
| e8 | relation | m6 | m8 | medium | into |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | church | church | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:church", "parents": []} |
| ent_m2 | object | cross | cross | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:cross", "parents": []} |
| ent_m3 | object | tower | tower | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:tower", "parents": []} |
| ent_m4 | object | sky | sky | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m6 | object | entrance | entrance | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:entrance", "parents": []} |
| ent_m8 | object | building | building | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | stands | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m10 | leads | lead | lead | visual_action |  | agent:m6->ent_m6 | {"canonical": "action:lead", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e3 | nsubj -> stands |  |  |
| ce1 | lead | agent | m6 | ent_m6 | medium | e4 | nsubj -> leads |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e5 | False | False |  |  |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | on | on | spatial_support, visual_relation | high | e6 | False | False |  |  |
| cr2 | m0 | m4 | ent_m0 | ent_m4 | under | under | spatial_vertical, visual_relation | high | e7 | False | False |  |  |
| cr3 | m6 | m8 | ent_m6 | ent_m8 | into | into | visual_relation | medium | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | church |  |  |  | entity_exists:church | True | low |
| cf1 | entity_exists | cross |  |  |  | entity_exists:cross | True | low |
| cf2 | entity_exists | tower |  |  |  | entity_exists:tower | True | low |
| cf3 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf4 | entity_exists | entrance |  |  |  | entity_exists:entrance | True | low |
| cf5 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf6 | has_attribute | church | stone |  | material_attribute, material, visual_attribute | has_attribute:church:stone | True | high |
| cf7 | has_attribute | sky | blue |  | color_attribute, color, visual_attribute | has_attribute:sky:blue | True | high |
| cf8 | has_attribute | entrance | arched |  | visual_attribute | has_attribute:entrance:arched | True | medium |
| cf9 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf10 | event_role | stand | agent | church |  | event_role:stand:agent:church | True | medium |
| cf11 | action_event | lead |  |  | visual_action | action_event:lead | True | low |
| cf12 | event_role | lead | agent | entrance |  | event_role:lead:agent:entrance | True | medium |
| cf13 | relation | church | with | cross | association_relation, visual_relation | relation:church:with:cross | True | high |
| cf14 | relation | cross | on | tower | spatial_support, visual_relation | relation:cross:on:tower | True | high |
| cf15 | relation | church | under | sky | spatial_vertical, visual_relation | relation:church:under:sky | True | high |
| cf16 | relation | entrance | into | building | visual_relation | relation:entrance:into:building | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 61

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `310880df54b4043e639fa4c97eb815ee953daef624af9115d22bd9ca06542c14`
**parse_path:** `sentence`

> A gradient sky shows blue fading into orange near the horizon.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | sky | sky | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | gradient | gradient | compound_modifier | chunk0 | 1 | medium |
| m2 | attribute | blue | blue | color_attribute | chunk1 | 4 | high |
| m3 | attribute | orange | orange | color_attribute | chunk2 | 7 | high |
| m4 | object | horizon | horizon | noun_chunk_root | chunk3 | 10 | high |
| m5 | action | shows | show | verb_predicate | doc | 3 | high |
| m6 | action | fading | fade | verb_predicate | doc | 5 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 compound -> sky |
| e1 | agent | m5 | m0 | medium | nsubj -> shows |
| e2 | agent | m6 | m0 | medium | inherited agent ccomp -> shows |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sky | sky | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m4 | object | horizon | horizon | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:horizon", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m5 | shows | show | show | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:show", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m6 | fading | fade | fade | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:fade", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | m0 | ent_m0 | medium | e1 | nsubj -> shows |  |  |
| ce1 | fade | agent | m0 | ent_m0 | medium | e2 | inherited agent ccomp -> shows |  |  |

### Stage 9 Canonical Relations
_none_

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf1 | entity_exists | horizon |  |  |  | entity_exists:horizon | True | low |
| cf2 | has_attribute | sky | gradient |  | compound_modifier, visual_attribute | has_attribute:sky:gradient | True | medium |
| cf3 | action_event | show |  |  | visual_action | action_event:show | True | low |
| cf4 | event_role | show | agent | sky |  | event_role:show:agent:sky | True | medium |
| cf5 | action_event | fade |  |  | visual_action | action_event:fade | True | low |
| cf6 | event_role | fade | agent | sky |  | event_role:fade:agent:sky | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 62

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `31175b7ae109233857b3b712027236ce9b67be47e5a0660848273ad48d080c14`
**parse_path:** `sentence`

> A man and a woman sit close together in a dimly lit room. The woman holds a single red rose with a ribbon, wearing a dark purple top and dangling earrings. Both look toward the camera with gentle smiles.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | woman | woman | noun_chunk_root | chunk1 | 4 | high |
| m2 | object | room | room | noun_chunk_root | chunk2 | 12 | high |
| m3 | attribute | dimly | dimly | modifier_attribute | chunk2 | 10 | medium |
| m4 | attribute | lit | light | visual_attribute | chunk2 | 11 | medium |
| m5 | object | woman | woman | noun_chunk_root | chunk3 | 15 | high |
| m6 | object | rose | rose | noun_chunk_root | chunk4 | 20 | high |
| m7 | attribute | single | single | modifier_attribute | chunk4 | 18 | medium |
| m8 | attribute | red | red | color_attribute | chunk4 | 19 | high |
| m9 | object | ribbon | ribbon | noun_chunk_root | chunk5 | 23 | high |
| m10 | object | top | top | noun_chunk_root | chunk6 | 29 | high |
| m11 | attribute | dark | dark | visual_attribute | chunk6 | 27 | medium |
| m12 | attribute | purple | purple | color_attribute | chunk6 | 28 | high |
| m13 | object | earrings | earring | noun_chunk_root | chunk7 | 32 | high |
| m14 | attribute | dangling | dangle | state_attribute | chunk7 | 31 | medium |
| m15 | quantity | Both | both | group_quantity | chunk8 | 34 | high |
| m16 | object | camera | camera | noun_chunk_root | chunk9 | 38 | high |
| m17 | object | smiles | smile | noun_chunk_root | chunk10 | 41 | high |
| m18 | attribute | gentle | gentle | modifier_attribute | chunk10 | 40 | medium |
| m19 | group | A man and a woman | man_and_woman | coordination_group | nominal_reference | 1 | high |
| m20 | reference | Both | both | group_reference | nominal_reference | 34 | high |
| m21 | action | sit | sit | verb_predicate | doc | 5 | high |
| m22 | action | holds | hold | verb_predicate | doc | 16 | high |
| m23 | action | wearing | wear | verb_predicate | doc | 25 | high |
| m24 | action | look | look | verb_predicate | doc | 35 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | medium | chunk2 advmod -> room |
| e1 | has_attribute | m2 | m4 | medium | chunk2 amod -> room |
| e2 | has_attribute | m6 | m7 | medium | chunk4 amod -> rose |
| e3 | has_attribute | m6 | m8 | high | chunk4 amod -> rose |
| e4 | has_attribute | m10 | m11 | medium | chunk6 amod -> top |
| e5 | has_attribute | m10 | m12 | high | chunk6 amod -> top |
| e6 | has_attribute | m13 | m14 | medium | chunk7 amod -> earrings |
| e7 | has_attribute | m17 | m18 | medium | chunk10 amod -> smiles |
| e8 | has_member | m19 | m0 | high | coordination_group |
| e9 | has_member | m19 | m1 | high | coordination_group |
| e10 | refers_to | m20 | m19 | high | group_reference Both -> A man and a woman; score=120; margin=30 |
| e11 | agent | m21 | m0 | medium | nsubj -> sit |
| e12 | agent | m21 | m1 | medium | nsubj -> sit |
| e13 | agent | m22 | m5 | medium | nsubj -> holds |
| e14 | patient | m22 | m6 | medium | dobj -> holds |
| e15 | agent | m23 | m5 | medium | inherited agent advcl -> holds |
| e16 | patient | m23 | m10 | medium | dobj -> wearing |
| e17 | patient | m23 | m13 | medium | dobj -> wearing |
| e18 | agent | m24 | m19 | medium | nsubj -> look; resolved Both -> A man and a woman |
| e19 | relation | m0 | m2 | high | in |
| e20 | relation | m6 | m9 | high | with |
| e21 | relation | m19 | m16 | medium | toward |
| e22 | relation | m19 | m17 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | woman | woman | person | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | room | room | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:room", "parents": []} |
| ent_m5 | object | woman | woman | person | person, human | m5 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m6 | object | rose | rose | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:rose", "parents": []} |
| ent_m9 | object | ribbon | ribbon | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:ribbon", "parents": []} |
| ent_m10 | object | top | top | object |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:top", "parents": []} |
| ent_m13 | object | earring | earrings | object |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:earring", "parents": []} |
| ent_m16 | object | camera | camera | device | device, artifact | m16 | raw_mention |  |  |  | True | {"canonical": "entity:camera", "parents": ["entity_parent:device", "entity_parent:artifact"]} |
| ent_m17 | object | smile | smiles | object |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:smile", "parents": []} |
| ent_m19 | group | man_and_woman | A man and a woman | group |  | m19 | raw_mention |  |  |  | True | {"canonical": "entity:man_and_woman", "parents": []} |
| eref_m20 | group | man_and_woman | Both | person | person, human | m20 | stage9_reference_group_repair | ent_m19 |  | 2 | True | {"canonical": "entity:man_and_woman", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m20 | eref_m20 | m19 | ent_m19 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m21 | sit | sit | sit | body_pose_action, visual_action |  | agent:m0->ent_m0; agent:m1->ent_m1 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m22 | holds | hold | hold | manipulation_action, visual_action |  | agent:m5->ent_m5; patient:m6->ent_m6 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce2 | m23 | wearing | wear | wear | wearing_action, visual_action |  | agent:m5->ent_m5; patient:m10->ent_m10; patient:m13->ent_m13 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce3 | m24 | look | look | look | gaze_action, visual_action |  | agent:m19->eref_m20 | {"canonical": "action:look", "parents": ["action_parent:gaze_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m0 | ent_m0 | medium | e11 | nsubj -> sit |  |  |
| ce0 | sit | agent | m1 | ent_m1 | medium | e12 | nsubj -> sit |  |  |
| ce1 | hold | agent | m5 | ent_m5 | medium | e13 | nsubj -> holds |  |  |
| ce1 | hold | patient | m6 | ent_m6 | medium | e14 | dobj -> holds |  |  |
| ce2 | wear | agent | m5 | ent_m5 | medium | e15 | inherited agent advcl -> holds |  |  |
| ce2 | wear | patient | m10 | ent_m10 | medium | e16 | dobj -> wearing |  |  |
| ce2 | wear | patient | m13 | ent_m13 | medium | e17 | dobj -> wearing |  |  |
| ce3 | look | agent | m19 | eref_m20 | medium | e18 | nsubj -> look; resolved Both -> A man and a woman |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | spatial_containment, visual_relation | high | e19 | False | False |  |  |
| cr1 | m6 | m9 | ent_m6 | ent_m9 | with | with | association_relation, visual_relation | high | e20 | False | False |  |  |
| cr2 | m19 | m16 | eref_m20 | ent_m16 | toward | toward | visual_relation | medium | e21 | False | False |  |  |
| cr3 | m19 | m17 | ent_m19 | ent_m17 | with | with | association_relation, visual_relation | high | e22 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf2 | entity_exists | room |  |  |  | entity_exists:room | True | low |
| cf3 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf4 | entity_exists | rose |  |  |  | entity_exists:rose | True | low |
| cf5 | entity_exists | ribbon |  |  |  | entity_exists:ribbon | True | low |
| cf6 | entity_exists | top |  |  |  | entity_exists:top | True | low |
| cf7 | entity_exists | earring |  |  |  | entity_exists:earring | True | low |
| cf8 | entity_exists | camera |  |  | device, artifact | entity_exists:camera | True | high |
| cf9 | entity_exists | smile |  |  |  | entity_exists:smile | True | low |
| cf10 | entity_exists | man_and_woman |  |  |  | entity_exists:man_and_woman | True | low |
| cf11 | entity_exists | man_and_woman |  |  | person, human | entity_exists:man_and_woman | True | medium |
| cf12 | has_attribute | room | dimly |  | modifier_attribute, visual_attribute | has_attribute:room:dimly | True | medium |
| cf13 | has_attribute | room | light |  | visual_attribute | has_attribute:room:light | True | medium |
| cf14 | has_attribute | rose | single |  | modifier_attribute, visual_attribute | has_attribute:rose:single | True | medium |
| cf15 | has_attribute | rose | red |  | color_attribute, color, visual_attribute | has_attribute:rose:red | True | high |
| cf16 | has_attribute | top | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:top:dark | True | medium |
| cf17 | has_attribute | top | purple |  | color_attribute, color, visual_attribute | has_attribute:top:purple | True | high |
| cf18 | has_attribute | earring | dangle |  | state_attribute, visual_attribute | has_attribute:earring:dangle | True | medium |
| cf19 | has_attribute | smile | gentle |  | modifier_attribute, visual_attribute | has_attribute:smile:gentle | True | medium |
| cf20 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf21 | event_role | sit | agent | man |  | event_role:sit:agent:man | True | medium |
| cf22 | event_role | sit | agent | woman |  | event_role:sit:agent:woman | True | medium |
| cf23 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf24 | event_role | hold | agent | woman |  | event_role:hold:agent:woman | True | medium |
| cf25 | event_role | hold | patient | rose |  | event_role:hold:patient:rose | True | medium |
| cf26 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf27 | event_role | wear | agent | woman |  | event_role:wear:agent:woman | True | medium |
| cf28 | event_role | wear | patient | top |  | event_role:wear:patient:top | True | medium |
| cf29 | event_role | wear | patient | earring |  | event_role:wear:patient:earring | True | medium |
| cf30 | action_event | look |  |  | gaze_action, visual_action | action_event:look | True | high |
| cf31 | event_role | look | agent | man_and_woman |  | event_role:look:agent:man_and_woman | True | medium |
| cf32 | relation | man | in | room | spatial_containment, visual_relation | relation:man:in:room | True | high |
| cf33 | relation | rose | with | ribbon | association_relation, visual_relation | relation:rose:with:ribbon | True | high |
| cf34 | relation | man_and_woman | toward | camera | visual_relation | relation:man_and_woman:toward:camera | True | medium |
| cf35 | relation | man_and_woman | with | smile | association_relation, visual_relation | relation:man_and_woman:with:smile | True | high |

### Stage 9 Canonicalization Notes
_none_

## 63

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `3177bcfa49aa3f7319ad241b1f6f7217718fb646fe189a246c1ab7685830b414`
**parse_path:** `sentence`

> Two men in camouflage uniforms are grappling on a blue and red mat inside a gym. One is on top, controlling the other who is lying on their back, with a chain-link fence visible behind them. A third person in similar gear is bent over nearby.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | men | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Two | two | exact_quantity | chunk0 | 0 | high |
| m2 | object | uniforms | uniform | noun_chunk_root | chunk1 | 4 | high |
| m3 | attribute | camouflage | camouflage | compound_modifier | chunk1 | 3 | medium |
| m4 | object | mat | mat | noun_chunk_root | chunk2 | 12 | high |
| m5 | attribute | blue | blue | color_attribute | chunk2 | 9 | high |
| m6 | attribute | red | red | color_attribute | chunk2 | 11 | high |
| m7 | object | gym | gym | noun_chunk_root | chunk3 | 15 | high |
| m8 | context | top | top | spatial_region | chunk4 | 20 | medium |
| m9 | context | back | back | spatial_region | chunk6 | 30 | medium |
| m10 | object | fence | fence | noun_chunk_root | chunk7 | 35 | high |
| m11 | attribute | chain-link | chain-link | compound_modifier | chunk7 | 34 | medium |
| m12 | object | person | person | noun_chunk_root | chunk9 | 42 | high |
| m13 | attribute | third | third | modifier_attribute | chunk9 | 41 | medium |
| m14 | object | gear | gear | noun_chunk_root | chunk10 | 45 | high |
| m15 | attribute | similar | similar | modifier_attribute | chunk10 | 44 | medium |
| m16 | reference | One | one | singular_substitute | nominal_reference | 17 | high |
| m17 | reference | other | other | contrastive_reference | nominal_reference | 24 | high |
| m18 | action | grappling | grapple | verb_predicate | doc | 6 | high |
| m19 | action | controlling | control | verb_predicate | doc | 22 | high |
| m20 | action | lying | lie | verb_predicate | doc | 27 | high |
| m21 | action | bent | bend | verb_predicate | doc | 47 | high |
| m22 | particle | over | over | phrasal_particle | action_particle | 48 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> men |
| e1 | has_attribute | m2 | m3 | medium | chunk1 compound -> uniforms |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> mat |
| e3 | has_attribute | m4 | m6 | high | chunk2 conj -> mat |
| e4 | has_attribute | m10 | m11 | medium | chunk7 compound -> fence |
| e5 | has_attribute | m12 | m13 | medium | chunk9 amod -> person |
| e6 | has_attribute | m14 | m15 | medium | chunk10 amod -> gear |
| e7 | refers_to | m16 | m0 | high | singular_substitute One -> men; score=102; margin=20 |
| e8 | refers_to | m17 | m0 | high | contrastive_reference other -> men; score=110; margin=30 |
| e9 | agent | m18 | m0 | medium | nsubj -> grappling |
| e10 | agent | m19 | m0 | medium | inherited agent advcl -> is |
| e11 | agent | m20 | m0 | medium | inherited agent relcl -> other |
| e12 | has_particle | m21 | m22 | medium | prt -> bent |
| e13 | agent | m21 | m12 | medium | inherited agent acomp -> is |
| e14 | relation | m0 | m2 | high | in |
| e15 | relation | m0 | m4 | high | on |
| e16 | relation | m0 | m7 | high | inside |
| e17 | relation | m0 | m8 | high | on |
| e18 | relation | m12 | m14 | high | in |

### Skipped Raw Concept Edges
| type | source | target | confidence | reason | evidence |
| --- | --- | --- | --- | --- | --- |
| patient | m19 | m0 | medium | pronoun_resolved_to_action_agent | dobj -> controlling; resolved other -> men |

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | men | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | uniform | uniforms | clothing | clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m4 | object | mat | mat | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:mat", "parents": []} |
| ent_m7 | object | gym | gym | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:gym", "parents": []} |
| ent_m8 | context | top | top | object | scene_context | m8 | raw_mention |  |  |  | True | {"canonical": "entity:top", "parents": ["entity_parent:scene_context"]} |
| ent_m9 | context | back | back | object | body_part | m9 | raw_mention |  |  |  | True | {"canonical": "entity:back", "parents": ["entity_parent:body_part"]} |
| ent_m10 | object | fence | fence | object |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:fence", "parents": []} |
| ent_m12 | object | person | person | person | person, human | m12 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m14 | object | gear | gear | object |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:gear", "parents": []} |
| eref_m16 | instance | man | One | person | person, human | m16 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| eref_m17 | contrastive_instance | man | other | person | person, human | m17 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m16 | eref_m16 | m0 | ent_m0 | high |  |
| refers_to | m17 | eref_m17 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | grappling | grapple | grapple | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:grapple", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m19 | controlling | control | control | manipulation_action, visual_action |  | agent:m0->ent_m0; patient:m0->eref_m17 | {"canonical": "action:control", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce2 | m20 | lying | lie | lie | body_pose_action, visual_action |  | agent:m0->eref_m17 | {"canonical": "action:lie", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce3 | m21 | bent | bend | bend_over | body_pose_action, visual_action | over | agent:m12->ent_m12 | {"canonical": "action:bend_over", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} | phrasal_action:bend over |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | grapple | agent | m0 | ent_m0 | medium | e9 | nsubj -> grappling |  |  |
| ce1 | control | agent | m0 | ent_m0 | medium | e10 | inherited agent advcl -> is |  |  |
| ce1 | control | patient | m0 | eref_m17 | medium |  | dobj -> controlling; resolved other -> men | pronoun_resolved_to_action_agent |  |
| ce2 | lie | agent | m0 | eref_m17 | medium | e11 | inherited agent relcl -> other |  |  |
| ce3 | bend_over | agent | m12 | ent_m12 | medium | e13 | inherited agent acomp -> is |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | spatial_containment, visual_relation | high | e14 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | on | spatial_support, visual_relation | high | e15 | False | False |  |  |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | inside | inside | spatial_containment, visual_relation | high | e16 | False | False |  |  |
| cr3 | m0 | m8 | ent_m0 | ent_m8 | on | on | spatial_support, visual_relation | high | e17 | False | False |  |  |
| cr4 | m12 | m14 | ent_m12 | ent_m14 | in | in | spatial_containment, visual_relation | high | e18 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf2 | entity_exists | mat |  |  |  | entity_exists:mat | True | low |
| cf3 | entity_exists | gym |  |  |  | entity_exists:gym | True | low |
| cf4 | entity_exists | top |  |  | scene_context | entity_exists:top | True | medium |
| cf5 | entity_exists | back |  |  | body_part | entity_exists:back | True | medium |
| cf6 | entity_exists | fence |  |  |  | entity_exists:fence | True | low |
| cf7 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf8 | entity_exists | gear |  |  |  | entity_exists:gear | True | low |
| cf9 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf10 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf11 | has_quantity | man | two |  | exact_quantity, quantity | has_quantity:man:two | True | high |
| cf12 | has_attribute | uniform | camouflage |  | pattern_attribute, other, textile_pattern, visual_attribute | has_attribute:uniform:camouflage | True | medium |
| cf13 | has_attribute | mat | blue |  | color_attribute, color, visual_attribute | has_attribute:mat:blue | True | high |
| cf14 | has_attribute | mat | red |  | color_attribute, color, visual_attribute | has_attribute:mat:red | True | high |
| cf15 | has_attribute | fence | chain-link |  | compound_modifier, visual_attribute | has_attribute:fence:chain-link | True | medium |
| cf16 | has_attribute | person | third |  | modifier_attribute, visual_attribute | has_attribute:person:third | True | medium |
| cf17 | has_attribute | gear | similar |  | modifier_attribute, visual_attribute | has_attribute:gear:similar | True | medium |
| cf18 | action_event | grapple |  |  | visual_action | action_event:grapple | True | low |
| cf19 | event_role | grapple | agent | man |  | event_role:grapple:agent:man | True | medium |
| cf20 | action_event | control |  |  | manipulation_action, visual_action | action_event:control | True | medium |
| cf21 | event_role | control | agent | man |  | event_role:control:agent:man | True | medium |
| cf22 | event_role | control | patient | man |  | event_role:control:patient:man | True | medium |
| cf23 | action_event | lie |  |  | body_pose_action, visual_action | action_event:lie | True | high |
| cf24 | event_role | lie | agent | man |  | event_role:lie:agent:man | True | medium |
| cf25 | action_event | bend_over |  |  | body_pose_action, visual_action | action_event:bend_over | True | high |
| cf26 | event_role | bend_over | agent | person |  | event_role:bend_over:agent:person | True | medium |
| cf27 | relation | man | in | uniform | spatial_containment, visual_relation | relation:man:in:uniform | True | high |
| cf28 | relation | man | on | mat | spatial_support, visual_relation | relation:man:on:mat | True | high |
| cf29 | relation | man | inside | gym | spatial_containment, visual_relation | relation:man:inside:gym | True | high |
| cf30 | relation | man | on | top | spatial_support, visual_relation | relation:man:on:top | True | high |
| cf31 | relation | person | in | gear | spatial_containment, visual_relation | relation:person:in:gear | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| skipped_reference_role_recovered | m19 |  |  | eref_m17 | pronoun_resolved_to_action_agent | {"action_mention_id": "m19", "canonical_target": "eref_m17", "kind": "skipped_reference_role_recovered", "reason": "pronoun_resolved_to_action_agent", "role": "patient"} |
| phrasal_action_canonicalized | m21 |  |  |  |  | {"action_mention_id": "m21", "canonical": "bend_over", "kind": "phrasal_action_canonicalized", "source": "visual_genome_relation_predicates", "term": "bend over"} |

## 64

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `319fb2034f0f1e660f1018f787b0ee1fb3ddff1a65e6543f4556fae5c3b85814`
**parse_path:** `sentence`

> A woman walks past a wall covered with colorful real estate signs in Chinese.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | wall | wall | noun_chunk_root | chunk1 | 5 | high |
| m2 | object | signs | sign | noun_chunk_root | chunk2 | 11 | high |
| m3 | attribute | colorful | colorful | modifier_attribute | chunk2 | 8 | medium |
| m4 | attribute | real | real | modifier_attribute | chunk2 | 9 | medium |
| m5 | attribute | estate | estate | compound_modifier | chunk2 | 10 | medium |
| m6 | object | Chinese | chinese | noun_chunk_root | chunk3 | 13 | high |
| m7 | action | walks | walk | verb_predicate | doc | 2 | high |
| m8 | action | covered | cover | verb_predicate | doc | 6 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | medium | chunk2 amod -> signs |
| e1 | has_attribute | m2 | m4 | medium | chunk2 amod -> signs |
| e2 | has_attribute | m2 | m5 | medium | chunk2 compound -> signs |
| e3 | agent | m7 | m0 | medium | nsubj -> walks |
| e4 | agent | m8 | m1 | medium | inherited agent acl -> wall |
| e5 | relation | m0 | m1 | medium | past |
| e6 | relation | m1 | m2 | high | with |
| e7 | relation | m2 | m6 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | wall | wall | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |
| ent_m2 | object | sign | signs | document | text_carrier, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:sign", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m6 | object | chinese | Chinese | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:chinese", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | walks | walk | walk | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:walk", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m8 | covered | cover | cover | visual_action |  | agent:m1->ent_m1 | {"canonical": "action:cover", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | walk | agent | m0 | ent_m0 | medium | e3 | nsubj -> walks |  |  |
| ce1 | cover | agent | m1 | ent_m1 | medium | e4 | inherited agent acl -> wall |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | past | past | visual_relation | medium | e5 | False | False |  |  |
| cr1 | m1 | m2 | ent_m1 | ent_m2 | with | with | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr2 | m2 | m6 | ent_m2 | ent_m6 | in | in | spatial_containment, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf2 | entity_exists | sign |  |  | text_carrier, artifact | entity_exists:sign | True | high |
| cf3 | entity_exists | chinese |  |  |  | entity_exists:chinese | True | low |
| cf4 | has_attribute | sign | colorful |  | color_attribute, color_quantity, visual_attribute | has_attribute:sign:colorful | True | medium |
| cf5 | has_attribute | sign | real |  | modifier_attribute, visual_attribute | has_attribute:sign:real | True | medium |
| cf6 | has_attribute | sign | estate |  | compound_modifier, visual_attribute | has_attribute:sign:estate | True | medium |
| cf7 | action_event | walk |  |  | locomotion_action, visual_action | action_event:walk | True | high |
| cf8 | event_role | walk | agent | woman |  | event_role:walk:agent:woman | True | medium |
| cf9 | action_event | cover |  |  | visual_action | action_event:cover | True | low |
| cf10 | event_role | cover | agent | wall |  | event_role:cover:agent:wall | True | medium |
| cf11 | relation | woman | past | wall | visual_relation | relation:woman:past:wall | True | medium |
| cf12 | relation | wall | with | sign | association_relation, visual_relation | relation:wall:with:sign | True | high |
| cf13 | relation | sign | in | chinese | spatial_containment, visual_relation | relation:sign:in:chinese | True | high |

### Stage 9 Canonicalization Notes
_none_

## 65

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `32bdeb0aa470fea2161e734b82fa841661fcaaed423d1b7274f831210a489c14`
**parse_path:** `tag_list`

> man, drink, pool, night, chair

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | tag_list_person_object_override | t0 | 0 | high |
| m1 | object | drink | drink | segment_head | t1 | 0 | high |
| m2 | object | pool | pool | segment_head | t2 | 0 | high |
| m3 | context | night | night | scene_context | t3 | 0 | high |
| m4 | object | chair | chair | segment_head | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_context | scene | m3 | high | t3 context tag |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | drink | drink | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:drink", "parents": []} |
| ent_m2 | object | pool | pool | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:pool", "parents": []} |
| ent_m3 | context | night | night | object | scene_context, time_context | m3 | raw_mention |  |  |  | True | {"canonical": "entity:night", "parents": ["entity_parent:scene_context", "entity_parent:time_context"]} |
| ent_m4 | object | chair | chair | object | furniture, artifact | m4 | raw_mention |  |  |  | True | {"canonical": "entity:chair", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |

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
| cf1 | entity_exists | drink |  |  |  | entity_exists:drink | True | low |
| cf2 | entity_exists | pool |  |  |  | entity_exists:pool | True | low |
| cf3 | entity_exists | night |  |  | scene_context, time_context | entity_exists:night | True | high |
| cf4 | entity_exists | chair |  |  | furniture, artifact | entity_exists:chair | True | high |

### Stage 9 Canonicalization Notes
_none_

## 66

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `3324412e9131638c6f5171d825b2f4408edaeeaf42702e4a7d12dc415afbe414`
**parse_path:** `tag_list`

> grandparent, child, toy car, striped shirt, red shirt

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | grandparent | grandparent | segment_head | t0 | 0 | high |
| m1 | object | child | child | segment_head | t1 | 0 | high |
| m2 | object | car | car | segment_head | t2 | 1 | high |
| m3 | attribute | toy | toy | attribute | t2 | 0 | high |
| m4 | object | shirt | shirt | segment_head | t3 | 1 | high |
| m5 | attribute | striped | striped | attribute | t3 | 0 | high |
| m6 | object | shirt | shirt | segment_head | t4 | 1 | high |
| m7 | attribute | red | red | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | t2 internal compound -> car |
| e1 | has_attribute | m4 | m5 | high | t3 internal amod -> shirt |
| e2 | has_attribute | m6 | m7 | high | t4 internal compound -> shirt |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | grandparent | grandparent | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:grandparent", "parents": []} |
| ent_m1 | object | child | child | person | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | car | car | vehicle | vehicle | m2 | raw_mention |  |  |  | True | {"canonical": "entity:car", "parents": ["entity_parent:vehicle"]} |
| ent_m4 | object | shirt | shirt | clothing | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m6 | object | shirt | shirt | clothing | clothing, wearable | m6 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |

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
| cf0 | entity_exists | grandparent |  |  |  | entity_exists:grandparent | True | low |
| cf1 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf2 | entity_exists | car |  |  | vehicle | entity_exists:car | True | high |
| cf3 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf4 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf5 | has_attribute | car | toy |  | attribute, visual_attribute | has_attribute:car:toy | True | high |
| cf6 | has_attribute | shirt | striped |  | pattern_attribute, clean_exact_overlap, pattern, pattern_marking, texture, visual_attribute | has_attribute:shirt:striped | True | high |
| cf7 | has_attribute | shirt | red |  | color_attribute, color, visual_attribute | has_attribute:shirt:red | True | high |

### Stage 9 Canonicalization Notes
_none_

## 67

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `338c0b314d1beee6ba81fa613f7f9bca53a4ad5bad1cefb3cf625a6cbc0f1014`
**parse_path:** `sentence`

> A soccer player in a black uniform controls the ball on a grassy field. Another player in a light blue uniform stands nearby, with spectators and tents visible in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | soccer player | soccer_player | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | uniform | uniform | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | black | black | color_attribute | chunk1 | 4 | high |
| m3 | object | ball | ball | noun_chunk_root | chunk2 | 8 | high |
| m4 | object | field | field | noun_chunk_root | chunk3 | 12 | high |
| m5 | attribute | grassy | grassy | modifier_attribute | chunk3 | 11 | medium |
| m6 | object | player | player | noun_chunk_root | chunk4 | 15 | high |
| m7 | object | uniform | uniform | noun_chunk_root | chunk5 | 20 | high |
| m8 | attribute | light | light | visual_attribute | chunk5 | 18 | medium |
| m9 | attribute | blue | blue | color_attribute | chunk5 | 19 | high |
| m10 | object | spectators | spectator | noun_chunk_root | chunk6 | 25 | high |
| m11 | object | tents | tent | noun_chunk_root | chunk7 | 27 | high |
| m12 | context | background | background | scene_context | chunk8 | 31 | high |
| m13 | action | controls | control | verb_predicate | doc | 6 | high |
| m14 | action | stands | stand | verb_predicate | doc | 21 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> uniform |
| e1 | has_attribute | m4 | m5 | medium | chunk3 amod -> field |
| e2 | has_attribute | m7 | m8 | medium | chunk5 amod -> uniform |
| e3 | has_attribute | m7 | m9 | high | chunk5 amod -> uniform |
| e4 | has_context | scene | m12 | high | scene_context token background |
| e5 | agent | m13 | m0 | medium | nsubj -> controls |
| e6 | patient | m13 | m3 | medium | dobj -> controls |
| e7 | agent | m14 | m6 | medium | nsubj -> stands |
| e8 | relation | m0 | m1 | high | in |
| e9 | relation | m0 | m4 | high | on |
| e10 | relation | m6 | m7 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | soccer_player | soccer player | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:soccer_player", "parents": []} |
| ent_m1 | object | uniform | uniform | clothing | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | ball | ball | object | sports_equipment, artifact | m3 | raw_mention |  |  |  | True | {"canonical": "entity:ball", "parents": ["entity_parent:sports_equipment", "entity_parent:artifact"]} |
| ent_m4 | object | field | field | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |
| ent_m6 | object | player | player | person | person, human | m6 | raw_mention |  |  |  | True | {"canonical": "entity:player", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m7 | object | uniform | uniform | clothing | clothing, wearable | m7 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m10 | object | spectator | spectators | object |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:spectator", "parents": []} |
| ent_m11 | object | tent | tents | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:tent", "parents": []} |
| ent_m12 | context | background | background | object | scene_context | m12 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m13 | controls | control | control | manipulation_action, visual_action |  | agent:m0->ent_m0; patient:m3->ent_m3 | {"canonical": "action:control", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce1 | m14 | stands | stand | stand | body_pose_action, visual_action |  | agent:m6->ent_m6 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | control | agent | m0 | ent_m0 | medium | e5 | nsubj -> controls |  |  |
| ce0 | control | patient | m3 | ent_m3 | medium | e6 | dobj -> controls |  |  |
| ce1 | stand | agent | m6 | ent_m6 | medium | e7 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | spatial_containment, visual_relation | high | e8 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | on | spatial_support, visual_relation | high | e9 | False | False |  |  |
| cr2 | m6 | m7 | ent_m6 | ent_m7 | in | in | spatial_containment, visual_relation | high | e10 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | soccer_player |  |  |  | entity_exists:soccer_player | True | low |
| cf1 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf2 | entity_exists | ball |  |  | sports_equipment, artifact | entity_exists:ball | True | high |
| cf3 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf4 | entity_exists | player |  |  | person, human | entity_exists:player | True | high |
| cf5 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf6 | entity_exists | spectator |  |  |  | entity_exists:spectator | True | low |
| cf7 | entity_exists | tent |  |  |  | entity_exists:tent | True | low |
| cf8 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf9 | has_attribute | uniform | black |  | color_attribute, color, visual_attribute | has_attribute:uniform:black | True | high |
| cf10 | has_attribute | field | grassy |  | modifier_attribute, visual_attribute | has_attribute:field:grassy | True | medium |
| cf11 | has_attribute | uniform | light |  | visual_attribute | has_attribute:uniform:light | True | medium |
| cf12 | has_attribute | uniform | blue |  | color_attribute, color, visual_attribute | has_attribute:uniform:blue | True | high |
| cf13 | action_event | control |  |  | manipulation_action, visual_action | action_event:control | True | medium |
| cf14 | event_role | control | agent | soccer_player |  | event_role:control:agent:soccer_player | True | medium |
| cf15 | event_role | control | patient | ball |  | event_role:control:patient:ball | True | medium |
| cf16 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf17 | event_role | stand | agent | player |  | event_role:stand:agent:player | True | medium |
| cf18 | relation | soccer_player | in | uniform | spatial_containment, visual_relation | relation:soccer_player:in:uniform | True | high |
| cf19 | relation | soccer_player | on | field | spatial_support, visual_relation | relation:soccer_player:on:field | True | high |
| cf20 | relation | player | in | uniform | spatial_containment, visual_relation | relation:player:in:uniform | True | high |

### Stage 9 Canonicalization Notes
_none_

## 68

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `35393afd2046cb36424127001a7c11fd60ac76df2218391c52e6f0a687b6c014`
**parse_path:** `sentence`

> A long, rusty metal pipe runs diagonally across a lush green hillside. It is supported by concrete blocks and surrounded by dense foliage and trees under bright sunlight.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | pipe | pipe | noun_chunk_root | chunk0 | 5 | high |
| m1 | attribute | long | long | size_attribute | chunk0 | 1 | high |
| m2 | attribute | rusty | rusty | modifier_attribute | chunk0 | 3 | medium |
| m3 | attribute | metal | metal | material_attribute | chunk0 | 4 | high |
| m4 | object | hillside | hillside | noun_chunk_root | chunk1 | 12 | high |
| m5 | attribute | lush | lush | modifier_attribute | chunk1 | 10 | medium |
| m6 | attribute | green | green | color_attribute | chunk1 | 11 | high |
| m7 | object | blocks | block | noun_chunk_root | chunk3 | 19 | high |
| m8 | attribute | concrete | concrete | material_attribute | chunk3 | 18 | high |
| m9 | object | foliage | foliage | noun_chunk_root | chunk4 | 24 | high |
| m10 | attribute | dense | dense | modifier_attribute | chunk4 | 23 | medium |
| m11 | object | trees | tree | noun_chunk_root | chunk5 | 26 | high |
| m12 | object | sunlight | sunlight | noun_chunk_root | chunk6 | 29 | high |
| m13 | attribute | bright | bright | visual_attribute | chunk6 | 28 | medium |
| m14 | action | runs | run | verb_predicate | doc | 6 | high |
| m15 | action | supported | support | verb_predicate | doc | 16 | high |
| m16 | action | surrounded | surround | verb_predicate | doc | 21 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> pipe |
| e1 | has_attribute | m0 | m2 | medium | chunk0 amod -> pipe |
| e2 | has_attribute | m0 | m3 | high | chunk0 compound -> pipe |
| e3 | has_attribute | m4 | m5 | medium | chunk1 amod -> hillside |
| e4 | has_attribute | m4 | m6 | high | chunk1 amod -> hillside |
| e5 | has_attribute | m7 | m8 | high | chunk3 compound -> blocks |
| e6 | has_attribute | m9 | m10 | medium | chunk4 amod -> foliage |
| e7 | has_attribute | m12 | m13 | medium | chunk6 amod -> sunlight |
| e8 | agent | m14 | m0 | medium | nsubj -> runs |
| e9 | agent | m15 | m0 | medium | nsubjpass -> supported; resolved It -> pipe |
| e10 | agent | m16 | m0 | medium | inherited agent conj -> supported |
| e11 | relation | m0 | m4 | high | across |
| e12 | relation | m0 | m7 | medium | by |
| e13 | relation | m0 | m9 | medium | by |
| e14 | relation | m0 | m11 | medium | by |
| e15 | relation | m0 | m12 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | pipe | pipe | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:pipe", "parents": []} |
| ent_m4 | object | hillside | hillside | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:hillside", "parents": []} |
| ent_m7 | object | block | blocks | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:block", "parents": []} |
| ent_m9 | object | foliage | foliage | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:foliage", "parents": []} |
| ent_m11 | object | tree | trees | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m12 | object | sunlight | sunlight | object |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:sunlight", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m14 | runs | run | run | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:run", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m15 | supported | support | support | visual_action |  | theme:m0->ent_m0; by_agent_or_causer:m7->ent_m7; by_agent_or_causer:m9->ent_m9; by_agent_or_causer:m11->ent_m11 | {"canonical": "action:support", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m16 | surrounded | surround | surround | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:surround", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | run | agent | m0 | ent_m0 | medium | e8 | nsubj -> runs |  |  |
| ce1 | support | theme | m0 | ent_m0 | medium | e9 | nsubjpass -> supported; resolved It -> pipe |  |  |
| ce1 | support | by_agent_or_causer | m7 | ent_m7 | medium | e12 | passive by-frame |  |  |
| ce1 | support | by_agent_or_causer | m9 | ent_m9 | medium | e13 | passive by-frame |  |  |
| ce1 | support | by_agent_or_causer | m11 | ent_m11 | medium | e14 | passive by-frame |  |  |
| ce2 | surround | agent | m0 | ent_m0 | medium | e10 | inherited agent conj -> supported |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | across | across | spatial_path, visual_relation | high | e11 | False | False |  |  |
| cr1 | m0 | m7 | ent_m0 | ent_m7 | by | by | spatial_proximity, visual_relation | medium | e12 | True | False |  |  |
| cr2 | m0 | m9 | ent_m0 | ent_m9 | by | by | spatial_proximity, visual_relation | medium | e13 | True | False |  |  |
| cr3 | m0 | m11 | ent_m0 | ent_m11 | by | by | spatial_proximity, visual_relation | medium | e14 | True | False |  |  |
| cr4 | m0 | m12 | ent_m0 | ent_m12 | under | under | spatial_vertical, visual_relation | high | e15 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | pipe |  |  |  | entity_exists:pipe | True | low |
| cf1 | entity_exists | hillside |  |  |  | entity_exists:hillside | True | low |
| cf2 | entity_exists | block |  |  |  | entity_exists:block | True | low |
| cf3 | entity_exists | foliage |  |  |  | entity_exists:foliage | True | low |
| cf4 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf5 | entity_exists | sunlight |  |  |  | entity_exists:sunlight | True | low |
| cf6 | has_attribute | pipe | long |  | size_attribute, clean_exact_overlap, length, visual_attribute | has_attribute:pipe:long | True | high |
| cf7 | has_attribute | pipe | rusty |  | modifier_attribute, visual_attribute | has_attribute:pipe:rusty | True | medium |
| cf8 | has_attribute | pipe | metal |  | material_attribute, material, non_textile_material_type, visual_attribute | has_attribute:pipe:metal | True | high |
| cf9 | has_attribute | hillside | lush |  | modifier_attribute, visual_attribute | has_attribute:hillside:lush | True | medium |
| cf10 | has_attribute | hillside | green |  | color_attribute, color, visual_attribute | has_attribute:hillside:green | True | high |
| cf11 | has_attribute | block | concrete |  | material_attribute, material, visual_attribute | has_attribute:block:concrete | True | high |
| cf12 | has_attribute | foliage | dense |  | modifier_attribute, visual_attribute | has_attribute:foliage:dense | True | medium |
| cf13 | has_attribute | sunlight | bright |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:sunlight:bright | True | medium |
| cf14 | action_event | run |  |  | locomotion_action, visual_action | action_event:run | True | high |
| cf15 | event_role | run | agent | pipe |  | event_role:run:agent:pipe | True | medium |
| cf16 | action_event | support |  |  | visual_action | action_event:support | True | low |
| cf17 | event_role | support | theme | pipe |  | event_role:support:theme:pipe | True | medium |
| cf18 | event_role | support | by_agent_or_causer | block |  | event_role:support:by_agent_or_causer:block | True | medium |
| cf19 | event_role | support | by_agent_or_causer | foliage |  | event_role:support:by_agent_or_causer:foliage | True | medium |
| cf20 | event_role | support | by_agent_or_causer | tree |  | event_role:support:by_agent_or_causer:tree | True | medium |
| cf21 | action_event | surround |  |  | visual_action | action_event:surround | True | low |
| cf22 | event_role | surround | agent | pipe |  | event_role:surround:agent:pipe | True | medium |
| cf23 | relation | pipe | across | hillside | spatial_path, visual_relation | relation:pipe:across:hillside | True | high |
| cf24 | relation | pipe | by | block | spatial_proximity, visual_relation | relation:pipe:by:block | False | medium |
| cf25 | relation | pipe | by | foliage | spatial_proximity, visual_relation | relation:pipe:by:foliage | False | medium |
| cf26 | relation | pipe | by | tree | spatial_proximity, visual_relation | relation:pipe:by:tree | False | medium |
| cf27 | relation | pipe | under | sunlight | spatial_vertical, visual_relation | relation:pipe:under:sunlight | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m15 | e9 | m0 |  |  | {"action_mention_id": "m15", "kind": "passive_subject_to_theme", "raw_edge_id": "e9", "target": "m0"} |
| passive_by_frame_to_event_role | m15 | e12 |  |  |  | {"action_mention_id": "m15", "by_agent_or_causer": "m7", "kind": "passive_by_frame_to_event_role", "raw_edge_id": "e12", "theme": "m0"} |
| passive_by_frame_to_event_role | m15 | e13 |  |  |  | {"action_mention_id": "m15", "by_agent_or_causer": "m9", "kind": "passive_by_frame_to_event_role", "raw_edge_id": "e13", "theme": "m0"} |
| passive_by_frame_to_event_role | m15 | e14 |  |  |  | {"action_mention_id": "m15", "by_agent_or_causer": "m11", "kind": "passive_by_frame_to_event_role", "raw_edge_id": "e14", "theme": "m0"} |

## 69

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `364c26cb7e32d9e444ebc8af7227977754b9c5bfd04f524c894693089c490414`
**parse_path:** `sentence`

> A woman with long hair speaks while gesturing with both hands against a dark background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | hair | hair | noun_chunk_root | chunk1 | 4 | high |
| m2 | attribute | long | long | size_attribute | chunk1 | 3 | high |
| m3 | object | hands | hand | noun_chunk_root | chunk2 | 10 | high |
| m4 | quantity | both | both | group_quantity | chunk2 | 9 | high |
| m5 | context | background | background | scene_context | chunk3 | 14 | high |
| m6 | attribute | dark | dark | visual_attribute | chunk3 | 13 | medium |
| m7 | action | speaks | speak | verb_predicate | doc | 5 | high |
| m8 | action | gesturing | gesture | verb_predicate | doc | 7 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> hair |
| e1 | has_quantity | m3 | m4 | high | chunk2 quantity -> hands |
| e2 | has_context | scene | m5 | high | scene_context token background |
| e3 | has_attribute | m5 | m6 | medium | chunk3 amod -> background |
| e4 | agent | m7 | m0 | medium | nsubj -> speaks |
| e5 | agent | m8 | m0 | medium | inherited agent advcl -> speaks |
| e6 | relation | m0 | m1 | high | with |
| e7 | relation | m0 | m3 | high | with |
| e8 | relation | m0 | m5 | high | against |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | hair | hair | object | body_part | m1 | raw_mention |  |  |  | True | {"canonical": "entity:hair", "parents": ["entity_parent:body_part"]} |
| ent_m3 | object | hand | hands | object | body_part | m3 | raw_mention |  |  |  | True | {"canonical": "entity:hand", "parents": ["entity_parent:body_part"]} |
| ent_m5 | context | background | background | object | scene_context | m5 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | speaks | speak | speak | communication_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:speak", "parents": ["action_parent:communication_action", "action_parent:visual_action"]} |  |
| ce1 | m8 | gesturing | gesture | gesture | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:gesture", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | speak | agent | m0 | ent_m0 | medium | e4 | nsubj -> speaks |  |  |
| ce1 | gesture | agent | m0 | ent_m0 | medium | e5 | inherited agent advcl -> speaks |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | with | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | with | with | association_relation, visual_relation | high | e7 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | against | against | spatial_contact, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | hair |  |  | body_part | entity_exists:hair | True | high |
| cf2 | entity_exists | hand |  |  | body_part | entity_exists:hand | True | high |
| cf3 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf4 | has_attribute | hair | long |  | size_attribute, clean_exact_overlap, length, visual_attribute | has_attribute:hair:long | True | high |
| cf5 | has_quantity | hand | both |  | group_quantity, quantity | has_quantity:hand:both | True | high |
| cf6 | has_attribute | background | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:background:dark | True | medium |
| cf7 | action_event | speak |  |  | communication_action, visual_action | action_event:speak | True | medium |
| cf8 | event_role | speak | agent | woman |  | event_role:speak:agent:woman | True | medium |
| cf9 | action_event | gesture |  |  | visual_action | action_event:gesture | True | low |
| cf10 | event_role | gesture | agent | woman |  | event_role:gesture:agent:woman | True | medium |
| cf11 | relation | woman | with | hair | association_relation, visual_relation | relation:woman:with:hair | True | high |
| cf12 | relation | woman | with | hand | association_relation, visual_relation | relation:woman:with:hand | True | high |
| cf13 | relation | woman | against | background | spatial_contact, visual_relation | relation:woman:against:background | True | high |

### Stage 9 Canonicalization Notes
_none_

## 70

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `37399b25943350293d011927c3fbd226e1c5e79dea38f98134b620ef8ccfbc14`
**parse_path:** `sentence`

> A rocky, steamy crater with mist rising from its edge. The ground is covered in dark, rough stones and patches of white material.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | crater | crater | noun_chunk_root | chunk0 | 4 | high |
| m1 | attribute | rocky | rocky | modifier_attribute | chunk0 | 1 | medium |
| m2 | attribute | steamy | steamy | modifier_attribute | chunk0 | 3 | medium |
| m3 | object | mist | mist | noun_chunk_root | chunk1 | 6 | high |
| m4 | context | edge | edge | spatial_region | chunk2 | 10 | medium |
| m5 | object | ground | ground | noun_chunk_root | chunk3 | 13 | high |
| m6 | object | stones | stone | noun_chunk_root | chunk4 | 20 | high |
| m7 | attribute | dark | dark | visual_attribute | chunk4 | 17 | medium |
| m8 | attribute | rough | rough | modifier_attribute | chunk4 | 19 | medium |
| m9 | object | patches | patch | noun_chunk_root | chunk5 | 22 | high |
| m10 | object | material | material | noun_chunk_root | chunk6 | 25 | high |
| m11 | attribute | white | white | color_attribute | chunk6 | 24 | high |
| m12 | action | rising | rise | verb_predicate | doc | 7 | high |
| m13 | action | covered | cover | verb_predicate | doc | 15 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> crater |
| e1 | has_attribute | m0 | m2 | medium | chunk0 amod -> crater |
| e2 | has_attribute | m6 | m7 | medium | chunk4 amod -> stones |
| e3 | has_attribute | m6 | m8 | medium | chunk4 amod -> stones |
| e4 | has_attribute | m10 | m11 | high | chunk6 amod -> material |
| e5 | agent | m12 | m3 | medium | inherited agent acl -> mist |
| e6 | agent | m13 | m5 | medium | nsubjpass -> covered |
| e7 | relation | m0 | m3 | high | with |
| e8 | relation | m3 | m4 | medium | from |
| e9 | relation | m5 | m6 | high | in |
| e10 | relation | m5 | m9 | high | in |
| e11 | relation | m9 | m10 | medium | of |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | crater | crater | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:crater", "parents": []} |
| ent_m3 | object | mist | mist | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:mist", "parents": []} |
| ent_m4 | context | edge | edge | object | scene_context | m4 | raw_mention |  |  |  | True | {"canonical": "entity:edge", "parents": ["entity_parent:scene_context"]} |
| ent_m5 | object | ground | ground | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:ground", "parents": []} |
| ent_m6 | object | stone | stones | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:stone", "parents": []} |
| ent_m9 | object | patch | patches | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:patch", "parents": []} |
| ent_m10 | object | material | material | object |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:material", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | rising | rise | rise | visual_action |  | agent:m3->ent_m3 | {"canonical": "action:rise", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m13 | covered | cover | cover | visual_action |  | theme:m5->ent_m5 | {"canonical": "action:cover", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | rise | agent | m3 | ent_m3 | medium | e5 | inherited agent acl -> mist |  |  |
| ce1 | cover | theme | m5 | ent_m5 | medium | e6 | nsubjpass -> covered |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | with | with | association_relation, visual_relation | high | e7 | False | False |  |  |
| cr1 | m3 | m4 | ent_m3 | ent_m4 | from | from | visual_relation | medium | e8 | False | False |  |  |
| cr2 | m5 | m6 | ent_m5 | ent_m6 | in | in | spatial_containment, visual_relation | high | e9 | False | False |  |  |
| cr3 | m5 | m9 | ent_m5 | ent_m9 | in | in | spatial_containment, visual_relation | high | e10 | False | False |  |  |
| cr4 | m9 | m10 | ent_m9 | ent_m10 | of | of | part_relation, visual_relation | medium | e11 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | crater |  |  |  | entity_exists:crater | True | low |
| cf1 | entity_exists | mist |  |  |  | entity_exists:mist | True | low |
| cf2 | entity_exists | edge |  |  | scene_context | entity_exists:edge | True | medium |
| cf3 | entity_exists | ground |  |  |  | entity_exists:ground | True | low |
| cf4 | entity_exists | stone |  |  |  | entity_exists:stone | True | low |
| cf5 | entity_exists | patch |  |  |  | entity_exists:patch | True | low |
| cf6 | entity_exists | material |  |  |  | entity_exists:material | True | low |
| cf7 | has_attribute | crater | rocky |  | material_attribute, material, visual_attribute | has_attribute:crater:rocky | True | medium |
| cf8 | has_attribute | crater | steamy |  | modifier_attribute, visual_attribute | has_attribute:crater:steamy | True | medium |
| cf9 | has_attribute | stone | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:stone:dark | True | medium |
| cf10 | has_attribute | stone | rough |  | texture_attribute, texture, visual_attribute | has_attribute:stone:rough | True | medium |
| cf11 | has_attribute | material | white |  | color_attribute, color, visual_attribute | has_attribute:material:white | True | high |
| cf12 | action_event | rise |  |  | visual_action | action_event:rise | True | low |
| cf13 | event_role | rise | agent | mist |  | event_role:rise:agent:mist | True | medium |
| cf14 | action_event | cover |  |  | visual_action | action_event:cover | True | low |
| cf15 | event_role | cover | theme | ground |  | event_role:cover:theme:ground | True | medium |
| cf16 | relation | crater | with | mist | association_relation, visual_relation | relation:crater:with:mist | True | high |
| cf17 | relation | mist | from | edge | visual_relation | relation:mist:from:edge | True | medium |
| cf18 | relation | ground | in | stone | spatial_containment, visual_relation | relation:ground:in:stone | True | high |
| cf19 | relation | ground | in | patch | spatial_containment, visual_relation | relation:ground:in:patch | True | high |
| cf20 | relation | patch | of | material | part_relation, visual_relation | relation:patch:of:material | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m13 | e6 | m5 |  |  | {"action_mention_id": "m13", "kind": "passive_subject_to_theme", "raw_edge_id": "e6", "target": "m5"} |

## 71

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `37d073e88ed18fd0db9727b4d89445dfd62a421b6926982817521f733def6c14`
**parse_path:** `sentence`

> A table shows statistics for various regions of the Russian Empire, including numbers and percentages.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | table | table | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | statistics | statistic | noun_chunk_root | chunk1 | 3 | high |
| m2 | object | regions | region | noun_chunk_root | chunk2 | 6 | high |
| m3 | quantity | various | various | approximate_quantity | chunk2 | 5 | medium |
| m4 | object | Empire | empire | noun_chunk_root | chunk3 | 10 | high |
| m5 | attribute | Russian | russian | compound_modifier | chunk3 | 9 | medium |
| m6 | object | numbers | number | noun_chunk_root | chunk4 | 13 | high |
| m7 | object | percentages | percentage | noun_chunk_root | chunk5 | 15 | high |
| m8 | action | shows | show | verb_predicate | doc | 2 | high |
| m9 | action | including | include | verb_predicate | doc | 12 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m2 | m3 | medium | chunk2 quantity -> regions |
| e1 | has_attribute | m4 | m5 | medium | chunk3 compound -> Empire |
| e2 | agent | m8 | m0 | medium | nsubj -> shows |
| e3 | patient | m8 | m1 | medium | dobj -> shows |
| e4 | agent | m9 | m1 | medium | inherited agent prep -> statistics |
| e5 | patient | m9 | m6 | medium | pobj -> including |
| e6 | patient | m9 | m7 | medium | pobj -> including |
| e7 | relation | m1 | m2 | medium | for |
| e8 | relation | m2 | m4 | medium | of |
| e9 | relation | m1 | m6 | medium | include |
| e10 | relation | m1 | m7 | medium | include |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | table | table | object | furniture, artifact | m0 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m1 | object | statistic | statistics | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:statistic", "parents": []} |
| ent_m2 | object | region | regions | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:region", "parents": []} |
| ent_m4 | object | empire | Empire | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:empire", "parents": []} |
| ent_m6 | object | number | numbers | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:number", "parents": []} |
| ent_m7 | object | percentage | percentages | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:percentage", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | shows | show | show | visual_action |  | agent:m0->ent_m0; patient:m1->ent_m1 | {"canonical": "action:show", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m9 | including | include | include | visual_action |  | agent:m1->ent_m1; patient:m6->ent_m6; patient:m7->ent_m7 | {"canonical": "action:include", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | m0 | ent_m0 | medium | e2 | nsubj -> shows |  |  |
| ce0 | show | patient | m1 | ent_m1 | medium | e3 | dobj -> shows |  |  |
| ce1 | include | agent | m1 | ent_m1 | medium | e4 | inherited agent prep -> statistics |  |  |
| ce1 | include | patient | m6 | ent_m6 | medium | e5 | pobj -> including |  |  |
| ce1 | include | patient | m7 | ent_m7 | medium | e6 | pobj -> including |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | for | for | visual_relation | medium | e7 | False | False |  |  |
| cr1 | m2 | m4 | ent_m2 | ent_m4 | of | of | part_relation, visual_relation | medium | e8 | False | False |  |  |
| cr2 | m1 | m6 | ent_m1 | ent_m6 | include | include | visual_relation | medium | e9 | False | False |  |  |
| cr3 | m1 | m7 | ent_m1 | ent_m7 | include | include | visual_relation | medium | e10 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf1 | entity_exists | statistic |  |  |  | entity_exists:statistic | True | low |
| cf2 | entity_exists | region |  |  |  | entity_exists:region | True | low |
| cf3 | entity_exists | empire |  |  |  | entity_exists:empire | True | low |
| cf4 | entity_exists | number |  |  |  | entity_exists:number | True | low |
| cf5 | entity_exists | percentage |  |  |  | entity_exists:percentage | True | low |
| cf6 | has_quantity | region | various |  | approximate_quantity, quantity | has_quantity:region:various | True | medium |
| cf7 | has_attribute | empire | russian |  | compound_modifier, visual_attribute | has_attribute:empire:russian | True | medium |
| cf8 | action_event | show |  |  | visual_action | action_event:show | True | low |
| cf9 | event_role | show | agent | table |  | event_role:show:agent:table | True | medium |
| cf10 | event_role | show | patient | statistic |  | event_role:show:patient:statistic | True | medium |
| cf11 | action_event | include |  |  | visual_action | action_event:include | True | low |
| cf12 | event_role | include | agent | statistic |  | event_role:include:agent:statistic | True | medium |
| cf13 | event_role | include | patient | number |  | event_role:include:patient:number | True | medium |
| cf14 | event_role | include | patient | percentage |  | event_role:include:patient:percentage | True | medium |
| cf15 | relation | statistic | for | region | visual_relation | relation:statistic:for:region | True | medium |
| cf16 | relation | region | of | empire | part_relation, visual_relation | relation:region:of:empire | True | medium |
| cf17 | relation | statistic | include | number | visual_relation | relation:statistic:include:number | True | medium |
| cf18 | relation | statistic | include | percentage | visual_relation | relation:statistic:include:percentage | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 72

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `3a18b4bdc7ca12c3129ed90ba2b225be2e83234f2f1de35bd8cf9e137192e414`
**parse_path:** `sentence`

> A yellow dog with wide eyes and an open mouth stands in a dark room. A bright red balloon is visible to the right, contrasting with the black-and-white background. The dog appears to be looking directly at the camera.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | dog | dog | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | yellow | yellow | color_attribute | chunk0 | 1 | high |
| m2 | object | eyes | eye | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | wide | wide | size_attribute | chunk1 | 4 | high |
| m4 | object | mouth | mouth | noun_chunk_root | chunk2 | 9 | high |
| m5 | attribute | open | open | modifier_attribute | chunk2 | 8 | medium |
| m6 | object | room | room | noun_chunk_root | chunk3 | 14 | high |
| m7 | attribute | dark | dark | visual_attribute | chunk3 | 13 | medium |
| m8 | object | balloon | balloon | noun_chunk_root | chunk4 | 19 | high |
| m9 | attribute | bright | bright | visual_attribute | chunk4 | 17 | medium |
| m10 | attribute | red | red | color_attribute | chunk4 | 18 | high |
| m11 | context | right | right | spatial_region | chunk5 | 24 | medium |
| m12 | context | background | background | scene_context | chunk6 | 30 | high |
| m13 | attribute | black-and-white | black-and-white | modifier_attribute | chunk6 | 29 | medium |
| m14 | object | dog | dog | noun_chunk_root | chunk7 | 33 | high |
| m15 | object | camera | camera | noun_chunk_root | chunk8 | 41 | high |
| m16 | action | stands | stand | verb_predicate | doc | 10 | high |
| m17 | action | contrasting | contrast | verb_predicate | doc | 26 | high |
| m18 | action | appears | appear | verb_predicate | doc | 34 | high |
| m19 | action | looking | look | verb_predicate | doc | 37 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> dog |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> eyes |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> mouth |
| e3 | has_attribute | m6 | m7 | medium | chunk3 amod -> room |
| e4 | has_attribute | m8 | m9 | medium | chunk4 amod -> balloon |
| e5 | has_attribute | m8 | m10 | high | chunk4 amod -> balloon |
| e6 | has_context | scene | m12 | high | scene_context token background |
| e7 | has_attribute | m12 | m13 | medium | chunk6 amod -> background |
| e8 | agent | m16 | m0 | medium | nsubj -> stands |
| e9 | agent | m17 | m8 | medium | inherited agent advcl -> is |
| e10 | agent | m18 | m14 | medium | nsubj -> appears |
| e11 | agent | m19 | m14 | medium | inherited agent xcomp -> appears |
| e12 | relation | m0 | m2 | high | with |
| e13 | relation | m0 | m4 | high | with |
| e14 | relation | m0 | m6 | high | in |
| e15 | relation | m8 | m12 | high | with |
| e16 | relation | m14 | m15 | medium | at |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | dog | dog | animal | animal, living_thing | m0 | raw_mention |  |  |  | True | {"canonical": "entity:dog", "parents": ["entity_parent:animal", "entity_parent:living_thing"]} |
| ent_m2 | object | eye | eyes | object | body_part | m2 | raw_mention |  |  |  | True | {"canonical": "entity:eye", "parents": ["entity_parent:body_part"]} |
| ent_m4 | object | mouth | mouth | object | body_part | m4 | raw_mention |  |  |  | True | {"canonical": "entity:mouth", "parents": ["entity_parent:body_part"]} |
| ent_m6 | object | room | room | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:room", "parents": []} |
| ent_m8 | object | balloon | balloon | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:balloon", "parents": []} |
| ent_m11 | context | right | right | object | scene_context | m11 | raw_mention |  |  |  | True | {"canonical": "entity:right", "parents": ["entity_parent:scene_context"]} |
| ent_m12 | context | background | background | object | scene_context | m12 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m14 | object | dog | dog | animal | animal, living_thing | m14 | raw_mention |  |  |  | True | {"canonical": "entity:dog", "parents": ["entity_parent:animal", "entity_parent:living_thing"]} |
| ent_m15 | object | camera | camera | device | device, artifact | m15 | raw_mention |  |  |  | True | {"canonical": "entity:camera", "parents": ["entity_parent:device", "entity_parent:artifact"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | stands | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m17 | contrasting | contrast | contrast | visual_action |  | agent:m8->ent_m8 | {"canonical": "action:contrast", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m18 | appears | appear | appear | visual_action |  | agent:m14->ent_m14 | {"canonical": "action:appear", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m19 | looking | look | look | gaze_action, visual_action |  | agent:m14->ent_m14 | {"canonical": "action:look", "parents": ["action_parent:gaze_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e8 | nsubj -> stands |  |  |
| ce1 | contrast | agent | m8 | ent_m8 | medium | e9 | inherited agent advcl -> is |  |  |
| ce2 | appear | agent | m14 | ent_m14 | medium | e10 | nsubj -> appears |  |  |
| ce3 | look | agent | m14 | ent_m14 | medium | e11 | inherited agent xcomp -> appears |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e12 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | with | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | in | in | spatial_containment, visual_relation | high | e14 | False | False |  |  |
| cr3 | m8 | m12 | ent_m8 | ent_m12 | with | with | association_relation, visual_relation | high | e15 | False | False |  |  |
| cr4 | m14 | m15 | ent_m14 | ent_m15 | at | at | spatial_location, visual_relation | medium | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | dog |  |  | animal, living_thing | entity_exists:dog | True | high |
| cf1 | entity_exists | eye |  |  | body_part | entity_exists:eye | True | high |
| cf2 | entity_exists | mouth |  |  | body_part | entity_exists:mouth | True | high |
| cf3 | entity_exists | room |  |  |  | entity_exists:room | True | low |
| cf4 | entity_exists | balloon |  |  |  | entity_exists:balloon | True | low |
| cf5 | entity_exists | right |  |  | scene_context | entity_exists:right | True | medium |
| cf6 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf7 | entity_exists | dog |  |  | animal, living_thing | entity_exists:dog | True | high |
| cf8 | entity_exists | camera |  |  | device, artifact | entity_exists:camera | True | high |
| cf9 | has_attribute | dog | yellow |  | color_attribute, color, visual_attribute | has_attribute:dog:yellow | True | high |
| cf10 | has_attribute | eye | wide |  | size_attribute, width, visual_attribute | has_attribute:eye:wide | True | high |
| cf11 | has_attribute | mouth | open |  | state_attribute, clean_exact_overlap, state, visual_attribute | has_attribute:mouth:open | True | medium |
| cf12 | has_attribute | room | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:room:dark | True | medium |
| cf13 | has_attribute | balloon | bright |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:balloon:bright | True | medium |
| cf14 | has_attribute | balloon | red |  | color_attribute, color, visual_attribute | has_attribute:balloon:red | True | high |
| cf15 | has_attribute | background | black-and-white |  | modifier_attribute, visual_attribute | has_attribute:background:black-and-white | True | medium |
| cf16 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf17 | event_role | stand | agent | dog |  | event_role:stand:agent:dog | True | medium |
| cf18 | action_event | contrast |  |  | visual_action | action_event:contrast | True | low |
| cf19 | event_role | contrast | agent | balloon |  | event_role:contrast:agent:balloon | True | medium |
| cf20 | action_event | appear |  |  | visual_action | action_event:appear | True | low |
| cf21 | event_role | appear | agent | dog |  | event_role:appear:agent:dog | True | medium |
| cf22 | action_event | look |  |  | gaze_action, visual_action | action_event:look | True | high |
| cf23 | event_role | look | agent | dog |  | event_role:look:agent:dog | True | medium |
| cf24 | relation | dog | with | eye | association_relation, visual_relation | relation:dog:with:eye | True | high |
| cf25 | relation | dog | with | mouth | association_relation, visual_relation | relation:dog:with:mouth | True | high |
| cf26 | relation | dog | in | room | spatial_containment, visual_relation | relation:dog:in:room | True | high |
| cf27 | relation | balloon | with | background | association_relation, visual_relation | relation:balloon:with:background | True | high |
| cf28 | relation | dog | at | camera | spatial_location, visual_relation | relation:dog:at:camera | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 73

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `3a3e745a8aea22b051a37ba29b47fd4059bb427e9b44d0d3f43bba15c3703c14`
**parse_path:** `sentence`

> A gray building with a blue lower section and red trim stands behind a green fence. A concrete area with puddles is in the foreground, and stairs lead up to the building’s entrance. The sky is overcast, and grass grows around the base of the structure.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | gray | gray | color_attribute | chunk0 | 1 | high |
| m2 | object | section | section | noun_chunk_root | chunk1 | 7 | high |
| m3 | attribute | blue | blue | color_attribute | chunk1 | 5 | high |
| m4 | attribute | lower | low | modifier_attribute | chunk1 | 6 | medium |
| m5 | object | trim | trim | noun_chunk_root | chunk2 | 10 | high |
| m6 | attribute | red | red | color_attribute | chunk2 | 9 | high |
| m7 | object | fence | fence | noun_chunk_root | chunk3 | 15 | high |
| m8 | attribute | green | green | color_attribute | chunk3 | 14 | high |
| m9 | object | area | area | noun_chunk_root | chunk4 | 19 | high |
| m10 | attribute | concrete | concrete | material_attribute | chunk4 | 18 | high |
| m11 | object | puddles | puddle | noun_chunk_root | chunk5 | 21 | high |
| m12 | context | foreground | foreground | scene_context | chunk6 | 25 | high |
| m13 | object | stairs | stair | noun_chunk_root | chunk7 | 28 | high |
| m14 | object | entrance | entrance | noun_chunk_root | chunk8 | 35 | high |
| m15 | attribute | building | building | modifier_attribute | chunk8 | 33 | medium |
| m16 | object | sky | sky | noun_chunk_root | chunk9 | 38 | high |
| m17 | object | grass | grass | noun_chunk_root | chunk10 | 43 | high |
| m19 | reference | the structure | structure | generic_structure_reference | generic_anaphoric | 50 | high |
| m20 | action | stands | stand | verb_predicate | doc | 11 | high |
| m21 | action | lead | lead | verb_predicate | doc | 29 | high |
| m22 | particle | up | up | phrasal_particle | action_particle | 30 | medium |
| m23 | action | grows | grow | verb_predicate | doc | 44 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> building |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> section |
| e2 | has_attribute | m2 | m4 | medium | chunk1 amod -> section |
| e3 | has_attribute | m5 | m6 | high | chunk2 amod -> trim |
| e4 | has_attribute | m7 | m8 | high | chunk3 amod -> fence |
| e5 | has_attribute | m9 | m10 | high | chunk4 amod -> area |
| e6 | has_context | scene | m12 | high | scene_context token foreground |
| e7 | has_attribute | m14 | m15 | medium | chunk8 poss -> entrance |
| e8 | refers_to | m19 | m0 | high | generic definite NP score=154 margin=60 |
| e9 | agent | m20 | m0 | medium | nsubj -> stands |
| e10 | agent | m21 | m13 | medium | nsubj -> lead |
| e11 | has_particle | m21 | m22 | medium | prt -> lead |
| e12 | agent | m23 | m17 | medium | nsubj -> grows |
| e13 | relation | m0 | m2 | high | with |
| e14 | relation | m0 | m5 | high | with |
| e15 | relation | m0 | m7 | high | behind |
| e16 | relation | m9 | m11 | high | with |
| e17 | relation | m9 | m12 | high | in |
| e18 | relation | m13 | m14 | medium | to |
| e19 | relation | m17 | m0 | medium | base_of |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | building | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m2 | object | section | section | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:section", "parents": []} |
| ent_m5 | object | trim | trim | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:trim", "parents": []} |
| ent_m7 | object | fence | fence | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:fence", "parents": []} |
| ent_m9 | object | area | area | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:area", "parents": []} |
| ent_m11 | object | puddle | puddles | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:puddle", "parents": []} |
| ent_m12 | context | foreground | foreground | object | scene_context | m12 | raw_mention |  |  |  | True | {"canonical": "entity:foreground", "parents": ["entity_parent:scene_context"]} |
| ent_m13 | object | stair | stairs | object |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:stair", "parents": []} |
| ent_m14 | object | entrance | entrance | object |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:entrance", "parents": []} |
| ent_m16 | object | sky | sky | object |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m17 | object | grass | grass | object |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": []} |
| eref_m19 | reference | building | the structure | object |  | m19 | stage9_reference | ent_m0 |  |  | True | {"canonical": "entity:building", "parents": []} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m19 | eref_m19 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m20 | stands | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m21 | lead | lead | lead | visual_action | up | agent:m13->ent_m13 | {"canonical": "action:lead", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m23 | grows | grow | grow | visual_action |  | agent:m17->ent_m17 | {"canonical": "action:grow", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e9 | nsubj -> stands |  |  |
| ce1 | lead | agent | m13 | ent_m13 | medium | e10 | nsubj -> lead |  |  |
| ce2 | grow | agent | m17 | ent_m17 | medium | e12 | nsubj -> grows |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | with | with | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | behind | behind | spatial_depth, visual_relation | high | e15 | False | False |  |  |
| cr3 | m9 | m11 | ent_m9 | ent_m11 | with | with | association_relation, visual_relation | high | e16 | False | False |  |  |
| cr4 | m9 | m12 | ent_m9 | ent_m12 | in | in | spatial_containment, visual_relation | high | e17 | False | False |  |  |
| cr5 | m13 | m14 | ent_m13 | ent_m14 | to | to | visual_relation | medium | e18 | False | False |  |  |
| cr6 | m17 | m0 | ent_m17 | ent_m0 | base_of | base_of | spatial_region, visual_relation | medium | e19 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf1 | entity_exists | section |  |  |  | entity_exists:section | True | low |
| cf2 | entity_exists | trim |  |  |  | entity_exists:trim | True | low |
| cf3 | entity_exists | fence |  |  |  | entity_exists:fence | True | low |
| cf4 | entity_exists | area |  |  |  | entity_exists:area | True | low |
| cf5 | entity_exists | puddle |  |  |  | entity_exists:puddle | True | low |
| cf6 | entity_exists | foreground |  |  | scene_context | entity_exists:foreground | True | high |
| cf7 | entity_exists | stair |  |  |  | entity_exists:stair | True | low |
| cf8 | entity_exists | entrance |  |  |  | entity_exists:entrance | True | low |
| cf9 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf10 | entity_exists | grass |  |  |  | entity_exists:grass | True | low |
| cf11 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf12 | has_attribute | building | gray |  | color_attribute, color, visual_attribute | has_attribute:building:gray | True | high |
| cf13 | has_attribute | section | blue |  | color_attribute, color, visual_attribute | has_attribute:section:blue | True | high |
| cf14 | has_attribute | section | low |  | size_attribute, height, visual_attribute | has_attribute:section:low | True | medium |
| cf15 | has_attribute | trim | red |  | color_attribute, color, visual_attribute | has_attribute:trim:red | True | high |
| cf16 | has_attribute | fence | green |  | color_attribute, color, visual_attribute | has_attribute:fence:green | True | high |
| cf17 | has_attribute | area | concrete |  | material_attribute, material, visual_attribute | has_attribute:area:concrete | True | high |
| cf18 | has_attribute | entrance | building |  | modifier_attribute, visual_attribute | has_attribute:entrance:building | True | medium |
| cf19 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf20 | event_role | stand | agent | building |  | event_role:stand:agent:building | True | medium |
| cf21 | action_event | lead |  |  | visual_action | action_event:lead | True | low |
| cf22 | event_role | lead | agent | stair |  | event_role:lead:agent:stair | True | medium |
| cf23 | action_event | grow |  |  | visual_action | action_event:grow | True | low |
| cf24 | event_role | grow | agent | grass |  | event_role:grow:agent:grass | True | medium |
| cf25 | relation | building | with | section | association_relation, visual_relation | relation:building:with:section | True | high |
| cf26 | relation | building | with | trim | association_relation, visual_relation | relation:building:with:trim | True | high |
| cf27 | relation | building | behind | fence | spatial_depth, visual_relation | relation:building:behind:fence | True | high |
| cf28 | relation | area | with | puddle | association_relation, visual_relation | relation:area:with:puddle | True | high |
| cf29 | relation | area | in | foreground | spatial_containment, visual_relation | relation:area:in:foreground | True | high |
| cf30 | relation | stair | to | entrance | visual_relation | relation:stair:to:entrance | True | medium |
| cf31 | relation | grass | base_of | building | spatial_region, visual_relation | relation:grass:base_of:building | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 74

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `3a94bef6569e8de11d6f22d1351ebabb5559cbd80977398b0ed11b3f5a3be414`
**parse_path:** `sentence`

> A man in a blue suit stands at a wooden podium speaking into microphones. To his left, a man in a gray suit sits with a mask on, and to his right, a woman in a yellow jacket sits with a mask on. They are in front of a backdrop with "Philadelphia Flyers" logos and text.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "Philadelphia Flyers" | philadelphia_flyers | quote_text | doc_quote | 56 | high |
| m1 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m2 | object | suit | suit | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | blue | blue | color_attribute | chunk1 | 4 | high |
| m4 | object | podium | podium | noun_chunk_root | chunk2 | 10 | high |
| m5 | attribute | wooden | wooden | material_attribute | chunk2 | 9 | high |
| m6 | object | microphones | microphone | noun_chunk_root | chunk3 | 13 | high |
| m7 | context | left | left | spatial_region | chunk4 | 17 | medium |
| m8 | object | man | man | noun_chunk_root | chunk5 | 20 | high |
| m9 | object | suit | suit | noun_chunk_root | chunk6 | 24 | high |
| m10 | attribute | gray | gray | color_attribute | chunk6 | 23 | high |
| m11 | object | mask | mask | noun_chunk_root | chunk7 | 28 | high |
| m12 | context | right | right | spatial_region | chunk8 | 34 | medium |
| m13 | object | woman | woman | noun_chunk_root | chunk9 | 37 | high |
| m14 | object | jacket | jacket | noun_chunk_root | chunk10 | 41 | high |
| m15 | attribute | yellow | yellow | color_attribute | chunk10 | 40 | high |
| m16 | object | mask | mask | noun_chunk_root | chunk11 | 45 | high |
| m17 | object | backdrop | backdrop | noun_chunk_root | chunk14 | 54 | high |
| m18 | object | logos | logo | noun_chunk_root | chunk15 | 57 | high |
| m19 | object | text | text | noun_chunk_root | chunk16 | 59 | high |
| m20 | action | stands | stand | verb_predicate | doc | 6 | high |
| m21 | action | speaking | speak | verb_predicate | doc | 11 | high |
| m22 | action | sits | sit | verb_predicate | doc | 25 | high |
| m23 | action | sits | sit | verb_predicate | doc | 42 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | chunk1 amod -> suit |
| e1 | has_attribute | m4 | m5 | high | chunk2 amod -> podium |
| e2 | has_attribute | m9 | m10 | high | chunk6 amod -> suit |
| e3 | has_attribute | m14 | m15 | high | chunk10 amod -> jacket |
| e4 | agent | m20 | m1 | medium | nsubj -> stands |
| e5 | agent | m21 | m1 | medium | inherited agent advcl -> stands |
| e6 | agent | m22 | m8 | medium | nsubj -> sits |
| e7 | agent | m23 | m13 | medium | nsubj -> sits |
| e8 | relation | m1 | m2 | high | in |
| e9 | relation | m1 | m4 | medium | at |
| e10 | relation | m1 | m6 | medium | into |
| e11 | relation | m8 | m7 | medium | to |
| e12 | relation | m8 | m9 | high | in |
| e13 | relation | m13 | m12 | medium | to |
| e14 | relation | m13 | m14 | high | in |
| e15 | relation | m13 | m17 | high | in_front_of |
| e16 | relation | m17 | m18 | high | with |
| e17 | relation | m17 | m19 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | man | man | person | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | suit | suit | clothing | clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:suit", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m4 | object | podium | podium | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:podium", "parents": []} |
| ent_m6 | object | microphone | microphones | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:microphone", "parents": []} |
| ent_m7 | context | left | left | object | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:left", "parents": ["entity_parent:scene_context"]} |
| ent_m8 | object | man | man | person | person, human | m8 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m9 | object | suit | suit | clothing | clothing, wearable | m9 | raw_mention |  |  |  | True | {"canonical": "entity:suit", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m11 | object | mask | mask | clothing | clothing, wearable | m11 | raw_mention |  |  |  | True | {"canonical": "entity:mask", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m12 | context | right | right | object | scene_context | m12 | raw_mention |  |  |  | True | {"canonical": "entity:right", "parents": ["entity_parent:scene_context"]} |
| ent_m13 | object | woman | woman | person | person, human | m13 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m14 | object | jacket | jacket | clothing | clothing, wearable | m14 | raw_mention |  |  |  | True | {"canonical": "entity:jacket", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m16 | object | mask | mask | clothing | clothing, wearable | m16 | raw_mention |  |  |  | True | {"canonical": "entity:mask", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m17 | object | backdrop | backdrop | object |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:backdrop", "parents": []} |
| ent_m18 | object | logo | logos | object |  | m18 | raw_mention |  |  |  | True | {"canonical": "entity:logo", "parents": []} |
| ent_m19 | object | text | text | document | text_content | m19 | raw_mention |  |  |  | True | {"canonical": "entity:text", "parents": ["entity_parent:text_content"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m20 | stands | stand | stand | body_pose_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m21 | speaking | speak | speak | communication_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:speak", "parents": ["action_parent:communication_action", "action_parent:visual_action"]} |  |
| ce2 | m22 | sits | sit | sit | body_pose_action, visual_action |  | agent:m8->ent_m8 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce3 | m23 | sits | sit | sit | body_pose_action, visual_action |  | agent:m13->ent_m13 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m1 | ent_m1 | medium | e4 | nsubj -> stands |  |  |
| ce1 | speak | agent | m1 | ent_m1 | medium | e5 | inherited agent advcl -> stands |  |  |
| ce2 | sit | agent | m8 | ent_m8 | medium | e6 | nsubj -> sits |  |  |
| ce3 | sit | agent | m13 | ent_m13 | medium | e7 | nsubj -> sits |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | in | in | spatial_containment, visual_relation | high | e8 | False | False |  |  |
| cr1 | m1 | m4 | ent_m1 | ent_m4 | at | at | spatial_location, visual_relation | medium | e9 | False | False |  |  |
| cr2 | m1 | m6 | ent_m1 | ent_m6 | into | into | visual_relation | medium | e10 | False | False |  |  |
| cr3 | m8 | m7 | ent_m8 | ent_m7 | to | to | visual_relation | medium | e11 | False | False |  |  |
| cr4 | m8 | m9 | ent_m8 | ent_m9 | in | in | spatial_containment, visual_relation | high | e12 | False | False |  |  |
| cr5 | m13 | m12 | ent_m13 | ent_m12 | to | to | visual_relation | medium | e13 | False | False |  |  |
| cr6 | m13 | m14 | ent_m13 | ent_m14 | in | in | spatial_containment, visual_relation | high | e14 | False | False |  |  |
| cr7 | m13 | m17 | ent_m13 | ent_m17 | in_front_of | in_front_of | spatial_depth, visual_relation | high | e15 | False | False |  |  |
| cr8 | m17 | m18 | ent_m17 | ent_m18 | with | with | association_relation, visual_relation | high | e16 | False | False |  |  |
| cr9 | m17 | m19 | ent_m17 | ent_m19 | with | with | association_relation, visual_relation | high | e17 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | suit |  |  | clothing, wearable | entity_exists:suit | True | high |
| cf2 | entity_exists | podium |  |  |  | entity_exists:podium | True | low |
| cf3 | entity_exists | microphone |  |  |  | entity_exists:microphone | True | low |
| cf4 | entity_exists | left |  |  | scene_context | entity_exists:left | True | medium |
| cf5 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf6 | entity_exists | suit |  |  | clothing, wearable | entity_exists:suit | True | high |
| cf7 | entity_exists | mask |  |  | clothing, wearable | entity_exists:mask | True | medium |
| cf8 | entity_exists | right |  |  | scene_context | entity_exists:right | True | medium |
| cf9 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf10 | entity_exists | jacket |  |  | clothing, wearable | entity_exists:jacket | True | high |
| cf11 | entity_exists | mask |  |  | clothing, wearable | entity_exists:mask | True | medium |
| cf12 | entity_exists | backdrop |  |  |  | entity_exists:backdrop | True | low |
| cf13 | entity_exists | logo |  |  |  | entity_exists:logo | True | low |
| cf14 | entity_exists | text |  |  | text_content | entity_exists:text | True | high |
| cf15 | has_attribute | suit | blue |  | color_attribute, color, visual_attribute | has_attribute:suit:blue | True | high |
| cf16 | has_attribute | podium | wooden |  | material_attribute, material, visual_attribute | has_attribute:podium:wooden | True | high |
| cf17 | has_attribute | suit | gray |  | color_attribute, color, visual_attribute | has_attribute:suit:gray | True | high |
| cf18 | has_attribute | jacket | yellow |  | color_attribute, color, visual_attribute | has_attribute:jacket:yellow | True | high |
| cf19 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf20 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf21 | action_event | speak |  |  | communication_action, visual_action | action_event:speak | True | medium |
| cf22 | event_role | speak | agent | man |  | event_role:speak:agent:man | True | medium |
| cf23 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf24 | event_role | sit | agent | man |  | event_role:sit:agent:man | True | medium |
| cf25 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf26 | event_role | sit | agent | woman |  | event_role:sit:agent:woman | True | medium |
| cf27 | relation | man | in | suit | spatial_containment, visual_relation | relation:man:in:suit | True | high |
| cf28 | relation | man | at | podium | spatial_location, visual_relation | relation:man:at:podium | True | medium |
| cf29 | relation | man | into | microphone | visual_relation | relation:man:into:microphone | True | medium |
| cf30 | relation | man | to | left | visual_relation | relation:man:to:left | True | medium |
| cf31 | relation | man | in | suit | spatial_containment, visual_relation | relation:man:in:suit | True | high |
| cf32 | relation | woman | to | right | visual_relation | relation:woman:to:right | True | medium |
| cf33 | relation | woman | in | jacket | spatial_containment, visual_relation | relation:woman:in:jacket | True | high |
| cf34 | relation | woman | in_front_of | backdrop | spatial_depth, visual_relation | relation:woman:in_front_of:backdrop | True | high |
| cf35 | relation | backdrop | with | logo | association_relation, visual_relation | relation:backdrop:with:logo | True | high |
| cf36 | relation | backdrop | with | text | association_relation, visual_relation | relation:backdrop:with:text | True | high |

### Stage 9 Canonicalization Notes
_none_

## 75

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `3af8f056cfe76e2dac26e55da0973df75cb449f6d54b6c2a0428c9bd66a2d814`
**parse_path:** `tag_list`

> man, pipe, concrete, dirt, gloves

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | tag_list_person_object_override | t0 | 0 | high |
| m1 | object | pipe | pipe | segment_head | t1 | 0 | high |
| m2 | object | concrete | concrete | segment_head | t2 | 0 | high |
| m3 | object | dirt | dirt | segment_head | t3 | 0 | high |
| m4 | object | gloves | glove | segment_head | t4 | 0 | high |

### Raw Concept Edges
_none_

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | pipe | pipe | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:pipe", "parents": []} |
| ent_m2 | object | concrete | concrete | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:concrete", "parents": []} |
| ent_m3 | object | dirt | dirt | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:dirt", "parents": []} |
| ent_m4 | object | glove | gloves | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:glove", "parents": []} |

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
| cf1 | entity_exists | pipe |  |  |  | entity_exists:pipe | True | low |
| cf2 | entity_exists | concrete |  |  |  | entity_exists:concrete | True | low |
| cf3 | entity_exists | dirt |  |  |  | entity_exists:dirt | True | low |
| cf4 | entity_exists | glove |  |  |  | entity_exists:glove | True | low |

### Stage 9 Canonicalization Notes
_none_

## 76

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `3b29dd4a058b71aa53a74f8fb31acb6906beda323ec3a8f8aa9410c838afa014`
**parse_path:** `sentence`

> A person’s hand holds a phone on a stone ledge overlooking a sprawling town. The town features many white buildings with some colorful roofs, nestled among green trees under a bright sky. Distant hills and scattered clouds complete the horizon.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hand | hand | noun_chunk_root | chunk0 | 3 | high |
| m1 | attribute | person | person | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | phone | phone | noun_chunk_root | chunk1 | 6 | high |
| m3 | object | ledge | ledge | noun_chunk_root | chunk2 | 10 | high |
| m4 | attribute | stone | stone | material_attribute | chunk2 | 9 | high |
| m5 | object | town | town | noun_chunk_root | chunk3 | 14 | high |
| m6 | attribute | sprawling | sprawl | state_attribute | chunk3 | 13 | medium |
| m7 | object | town | town | noun_chunk_root | chunk4 | 17 | high |
| m8 | object | buildings | building | noun_chunk_root | chunk5 | 21 | high |
| m9 | quantity | many | many | approximate_quantity | chunk5 | 19 | medium |
| m10 | attribute | white | white | color_attribute | chunk5 | 20 | high |
| m11 | object | roofs | roof | noun_chunk_root | chunk6 | 25 | high |
| m12 | quantity | some | some | indefinite_quantity | chunk6 | 23 | medium |
| m13 | attribute | colorful | colorful | modifier_attribute | chunk6 | 24 | medium |
| m14 | object | trees | tree | noun_chunk_root | chunk7 | 30 | high |
| m15 | attribute | green | green | color_attribute | chunk7 | 29 | high |
| m16 | object | sky | sky | noun_chunk_root | chunk8 | 34 | high |
| m17 | attribute | bright | bright | visual_attribute | chunk8 | 33 | medium |
| m18 | object | hills | hill | noun_chunk_root | chunk9 | 37 | high |
| m19 | attribute | Distant | distant | modifier_attribute | chunk9 | 36 | medium |
| m20 | object | clouds | cloud | noun_chunk_root | chunk10 | 40 | high |
| m21 | attribute | scattered | scatter | state_attribute | chunk10 | 39 | medium |
| m22 | object | horizon | horizon | noun_chunk_root | chunk11 | 43 | high |
| m23 | action | holds | hold | verb_predicate | doc | 4 | high |
| m24 | action | overlooking | overlook | verb_predicate | doc | 11 | high |
| m25 | action | features | feature | verb_predicate | doc | 18 | high |
| m26 | action | nestled | nestle | verb_predicate | doc | 27 | high |
| m27 | action | complete | complete | verb_predicate | doc | 41 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 poss -> hand |
| e1 | has_attribute | m3 | m4 | high | chunk2 compound -> ledge |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> town |
| e3 | has_quantity | m8 | m9 | medium | chunk5 quantity -> buildings |
| e4 | has_attribute | m8 | m10 | high | chunk5 amod -> buildings |
| e5 | has_quantity | m11 | m12 | medium | chunk6 quantity -> roofs |
| e6 | has_attribute | m11 | m13 | medium | chunk6 amod -> roofs |
| e7 | has_attribute | m14 | m15 | high | chunk7 amod -> trees |
| e8 | has_attribute | m16 | m17 | medium | chunk8 amod -> sky |
| e9 | has_attribute | m18 | m19 | medium | chunk9 amod -> hills |
| e10 | has_attribute | m20 | m21 | medium | chunk10 amod -> clouds |
| e11 | agent | m23 | m0 | medium | nsubj -> holds |
| e12 | patient | m23 | m2 | medium | dobj -> holds |
| e13 | agent | m24 | m3 | medium | inherited agent acl -> ledge |
| e14 | patient | m24 | m5 | medium | dobj -> overlooking |
| e15 | agent | m25 | m7 | medium | nsubj -> features |
| e16 | patient | m25 | m8 | medium | dobj -> features |
| e17 | agent | m26 | m8 | medium | inherited agent acl -> buildings |
| e18 | agent | m27 | m18 | medium | nsubj -> complete |
| e19 | agent | m27 | m20 | medium | nsubj -> complete |
| e20 | patient | m27 | m22 | medium | dobj -> complete |
| e21 | relation | m0 | m3 | high | on |
| e22 | relation | m8 | m11 | high | with |
| e23 | relation | m8 | m14 | medium | among |
| e24 | relation | m14 | m16 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hand | hand | object | body_part | m0 | raw_mention |  |  |  | True | {"canonical": "entity:hand", "parents": ["entity_parent:body_part"]} |
| ent_m2 | object | phone | phone | device | device, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:phone", "parents": ["entity_parent:device", "entity_parent:artifact"]} |
| ent_m3 | object | ledge | ledge | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:ledge", "parents": []} |
| ent_m5 | object | town | town | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:town", "parents": []} |
| ent_m7 | object | town | town | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:town", "parents": []} |
| ent_m8 | object | building | buildings | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m11 | object | roof | roofs | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:roof", "parents": []} |
| ent_m14 | object | tree | trees | object |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m16 | object | sky | sky | object |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m18 | object | hill | hills | object |  | m18 | raw_mention |  |  |  | True | {"canonical": "entity:hill", "parents": []} |
| ent_m20 | object | cloud | clouds | object |  | m20 | raw_mention |  |  |  | True | {"canonical": "entity:cloud", "parents": []} |
| ent_m22 | object | horizon | horizon | object |  | m22 | raw_mention |  |  |  | True | {"canonical": "entity:horizon", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m23 | holds | hold | hold | manipulation_action, visual_action |  | agent:m0->ent_m0; patient:m2->ent_m2 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce1 | m24 | overlooking | overlook | overlook | visual_action |  | agent:m3->ent_m3; patient:m5->ent_m5 | {"canonical": "action:overlook", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m25 | features | feature | feature | visual_action |  | agent:m7->ent_m7; patient:m8->ent_m8 | {"canonical": "action:feature", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m26 | nestled | nestle | nestle | visual_action |  | agent:m8->ent_m8 | {"canonical": "action:nestle", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m27 | complete | complete | complete | visual_action |  | agent:m18->ent_m18; agent:m20->ent_m20; patient:m22->ent_m22 | {"canonical": "action:complete", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | hold | agent | m0 | ent_m0 | medium | e11 | nsubj -> holds |  |  |
| ce0 | hold | patient | m2 | ent_m2 | medium | e12 | dobj -> holds |  |  |
| ce1 | overlook | agent | m3 | ent_m3 | medium | e13 | inherited agent acl -> ledge |  |  |
| ce1 | overlook | patient | m5 | ent_m5 | medium | e14 | dobj -> overlooking |  |  |
| ce2 | feature | agent | m7 | ent_m7 | medium | e15 | nsubj -> features |  |  |
| ce2 | feature | patient | m8 | ent_m8 | medium | e16 | dobj -> features |  |  |
| ce3 | nestle | agent | m8 | ent_m8 | medium | e17 | inherited agent acl -> buildings |  |  |
| ce4 | complete | agent | m18 | ent_m18 | medium | e18 | nsubj -> complete |  |  |
| ce4 | complete | agent | m20 | ent_m20 | medium | e19 | nsubj -> complete |  |  |
| ce4 | complete | patient | m22 | ent_m22 | medium | e20 | dobj -> complete |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | on | on | spatial_support, visual_relation | high | e21 | False | False |  |  |
| cr1 | m8 | m11 | ent_m8 | ent_m11 | with | with | association_relation, visual_relation | high | e22 | False | False |  |  |
| cr2 | m8 | m14 | ent_m8 | ent_m14 | among | among | spatial_region, visual_relation | medium | e23 | False | False |  |  |
| cr3 | m14 | m16 | ent_m14 | ent_m16 | under | under | spatial_vertical, visual_relation | high | e24 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | hand |  |  | body_part | entity_exists:hand | True | high |
| cf1 | entity_exists | phone |  |  | device, artifact | entity_exists:phone | True | high |
| cf2 | entity_exists | ledge |  |  |  | entity_exists:ledge | True | low |
| cf3 | entity_exists | town |  |  |  | entity_exists:town | True | low |
| cf4 | entity_exists | town |  |  |  | entity_exists:town | True | low |
| cf5 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf6 | entity_exists | roof |  |  |  | entity_exists:roof | True | low |
| cf7 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf8 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf9 | entity_exists | hill |  |  |  | entity_exists:hill | True | low |
| cf10 | entity_exists | cloud |  |  |  | entity_exists:cloud | True | low |
| cf11 | entity_exists | horizon |  |  |  | entity_exists:horizon | True | low |
| cf12 | has_attribute | hand | person |  | modifier_attribute, visual_attribute | has_attribute:hand:person | True | medium |
| cf13 | has_attribute | ledge | stone |  | material_attribute, material, visual_attribute | has_attribute:ledge:stone | True | high |
| cf14 | has_attribute | town | sprawl |  | state_attribute, visual_attribute | has_attribute:town:sprawl | True | medium |
| cf15 | has_quantity | building | many |  | approximate_quantity, quantity | has_quantity:building:many | True | medium |
| cf16 | has_attribute | building | white |  | color_attribute, color, visual_attribute | has_attribute:building:white | True | high |
| cf17 | has_quantity | roof | some |  | indefinite_quantity, quantity | has_quantity:roof:some | True | medium |
| cf18 | has_attribute | roof | colorful |  | color_attribute, color_quantity, visual_attribute | has_attribute:roof:colorful | True | medium |
| cf19 | has_attribute | tree | green |  | color_attribute, color, visual_attribute | has_attribute:tree:green | True | high |
| cf20 | has_attribute | sky | bright |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:sky:bright | True | medium |
| cf21 | has_attribute | hill | distant |  | modifier_attribute, visual_attribute | has_attribute:hill:distant | True | medium |
| cf22 | has_attribute | cloud | scatter |  | state_attribute, visual_attribute | has_attribute:cloud:scatter | True | medium |
| cf23 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf24 | event_role | hold | agent | hand |  | event_role:hold:agent:hand | True | medium |
| cf25 | event_role | hold | patient | phone |  | event_role:hold:patient:phone | True | medium |
| cf26 | action_event | overlook |  |  | visual_action | action_event:overlook | True | low |
| cf27 | event_role | overlook | agent | ledge |  | event_role:overlook:agent:ledge | True | medium |
| cf28 | event_role | overlook | patient | town |  | event_role:overlook:patient:town | True | medium |
| cf29 | action_event | feature |  |  | visual_action | action_event:feature | True | low |
| cf30 | event_role | feature | agent | town |  | event_role:feature:agent:town | True | medium |
| cf31 | event_role | feature | patient | building |  | event_role:feature:patient:building | True | medium |
| cf32 | action_event | nestle |  |  | visual_action | action_event:nestle | True | low |
| cf33 | event_role | nestle | agent | building |  | event_role:nestle:agent:building | True | medium |
| cf34 | action_event | complete |  |  | visual_action | action_event:complete | True | low |
| cf35 | event_role | complete | agent | hill |  | event_role:complete:agent:hill | True | medium |
| cf36 | event_role | complete | agent | cloud |  | event_role:complete:agent:cloud | True | medium |
| cf37 | event_role | complete | patient | horizon |  | event_role:complete:patient:horizon | True | medium |
| cf38 | relation | hand | on | ledge | spatial_support, visual_relation | relation:hand:on:ledge | True | high |
| cf39 | relation | building | with | roof | association_relation, visual_relation | relation:building:with:roof | True | high |
| cf40 | relation | building | among | tree | spatial_region, visual_relation | relation:building:among:tree | True | medium |
| cf41 | relation | tree | under | sky | spatial_vertical, visual_relation | relation:tree:under:sky | True | high |

### Stage 9 Canonicalization Notes
_none_

## 77

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `3b5770a7546308c5e0951bca64a4e13b3c91834d525b06b373afbe6b6eaf2814`
**parse_path:** `sentence`

> A woman in a black, American flag-themed outfit holds up a shiny championship belt. She stands indoors under chandeliers with a ceiling and ventilation ducts visible behind her.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | outfit | outfit | noun_chunk_root | chunk1 | 9 | high |
| m2 | attribute | black | black | color_attribute | chunk1 | 4 | high |
| m3 | attribute | themed | theme | state_attribute | chunk1 | 8 | medium |
| m4 | object | belt | belt | noun_chunk_root | chunk2 | 15 | high |
| m5 | attribute | shiny | shiny | visual_attribute | chunk2 | 13 | medium |
| m6 | attribute | championship | championship | compound_modifier | chunk2 | 14 | medium |
| m7 | object | chandeliers | chandelier | noun_chunk_root | chunk4 | 21 | high |
| m8 | object | ceiling | ceiling | noun_chunk_root | chunk5 | 24 | high |
| m9 | object | ducts | duct | noun_chunk_root | chunk6 | 27 | high |
| m10 | attribute | ventilation | ventilation | compound_modifier | chunk6 | 26 | medium |
| m11 | context | indoors | indoors | scene_context | doc | 19 | high |
| m12 | action | holds | hold | verb_predicate | doc | 10 | high |
| m13 | particle | up | up | phrasal_particle | action_particle | 11 | medium |
| m14 | action | stands | stand | verb_predicate | doc | 18 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> outfit |
| e1 | has_attribute | m1 | m3 | medium | chunk1 amod -> outfit |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> belt |
| e3 | has_attribute | m4 | m6 | medium | chunk2 compound -> belt |
| e4 | has_attribute | m9 | m10 | medium | chunk6 compound -> ducts |
| e5 | has_context | scene | m11 | high | scene_context token indoors |
| e6 | agent | m12 | m0 | medium | nsubj -> holds |
| e7 | has_particle | m12 | m13 | medium | prt -> holds |
| e8 | patient | m12 | m4 | medium | dobj -> holds |
| e9 | agent | m14 | m0 | medium | nsubj -> stands; resolved She -> woman |
| e10 | relation | m0 | m1 | high | in |
| e11 | relation | m0 | m7 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | outfit | outfit | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:outfit", "parents": []} |
| ent_m4 | object | belt | belt | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:belt", "parents": []} |
| ent_m7 | object | chandelier | chandeliers | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:chandelier", "parents": []} |
| ent_m8 | object | ceiling | ceiling | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:ceiling", "parents": []} |
| ent_m9 | object | duct | ducts | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:duct", "parents": []} |
| ent_m11 | context | indoors | indoors | object | scene_context | m11 | raw_mention |  |  |  | True | {"canonical": "entity:indoors", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | holds | hold | hold_up | manipulation_action, visual_action | up | agent:m0->ent_m0; patient:m4->ent_m4 | {"canonical": "action:hold_up", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} | phrasal_action:hold up |
| ce1 | m14 | stands | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | hold_up | agent | m0 | ent_m0 | medium | e6 | nsubj -> holds |  |  |
| ce0 | hold_up | patient | m4 | ent_m4 | medium | e8 | dobj -> holds |  |  |
| ce1 | stand | agent | m0 | ent_m0 | medium | e9 | nsubj -> stands; resolved She -> woman |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | spatial_containment, visual_relation | high | e10 | False | False |  |  |
| cr1 | m0 | m7 | ent_m0 | ent_m7 | under | under | spatial_vertical, visual_relation | high | e11 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | outfit |  |  |  | entity_exists:outfit | True | low |
| cf2 | entity_exists | belt |  |  |  | entity_exists:belt | True | low |
| cf3 | entity_exists | chandelier |  |  |  | entity_exists:chandelier | True | low |
| cf4 | entity_exists | ceiling |  |  |  | entity_exists:ceiling | True | low |
| cf5 | entity_exists | duct |  |  |  | entity_exists:duct | True | low |
| cf6 | entity_exists | indoors |  |  | scene_context | entity_exists:indoors | True | high |
| cf7 | has_attribute | outfit | black |  | color_attribute, color, visual_attribute | has_attribute:outfit:black | True | high |
| cf8 | has_attribute | outfit | theme |  | state_attribute, visual_attribute | has_attribute:outfit:theme | True | medium |
| cf9 | has_attribute | belt | shiny |  | visual_attribute | has_attribute:belt:shiny | True | medium |
| cf10 | has_attribute | belt | championship |  | compound_modifier, visual_attribute | has_attribute:belt:championship | True | medium |
| cf11 | has_attribute | duct | ventilation |  | compound_modifier, visual_attribute | has_attribute:duct:ventilation | True | medium |
| cf12 | action_event | hold_up |  |  | manipulation_action, visual_action | action_event:hold_up | True | high |
| cf13 | event_role | hold_up | agent | woman |  | event_role:hold_up:agent:woman | True | medium |
| cf14 | event_role | hold_up | patient | belt |  | event_role:hold_up:patient:belt | True | medium |
| cf15 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf16 | event_role | stand | agent | woman |  | event_role:stand:agent:woman | True | medium |
| cf17 | relation | woman | in | outfit | spatial_containment, visual_relation | relation:woman:in:outfit | True | high |
| cf18 | relation | woman | under | chandelier | spatial_vertical, visual_relation | relation:woman:under:chandelier | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| phrasal_action_canonicalized | m12 |  |  |  |  | {"action_mention_id": "m12", "canonical": "hold_up", "kind": "phrasal_action_canonicalized", "source": "visual_genome_relation_predicates", "term": "hold up"} |

## 78

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `3d615bf81b2edbc0ddf312c8e46aeff2ced9ab2d0015e50b4be5dc566214c414`
**parse_path:** `sentence`

> People in suits sit at wooden desks in a large legislative chamber. A large screen above displays text in Portuguese, including “Assembleia Legislativa do Estado do Espírito Santo” and meeting details. Several individuals are seated or standing near the front, facing the screen.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “Assembleia Legislativa do Estado do Espírito Santo” | assembleia_legislativa_do_estado_do_espírito_santo | quote_text | doc_quote | 23 | high |
| m1 | object | People | people | noun_chunk_root | chunk0 | 0 | high |
| m2 | object | suits | suit | noun_chunk_root | chunk1 | 2 | high |
| m3 | object | desks | desk | noun_chunk_root | chunk2 | 6 | high |
| m4 | attribute | wooden | wooden | material_attribute | chunk2 | 5 | high |
| m5 | object | chamber | chamber | noun_chunk_root | chunk3 | 11 | high |
| m6 | attribute | large | large | size_attribute | chunk3 | 9 | high |
| m7 | attribute | legislative | legislative | modifier_attribute | chunk3 | 10 | medium |
| m8 | object | screen | screen | noun_chunk_root | chunk4 | 15 | high |
| m9 | attribute | large | large | size_attribute | chunk4 | 14 | high |
| m10 | object | text | text | noun_chunk_root | chunk5 | 18 | high |
| m11 | object | Portuguese | portuguese | noun_chunk_root | chunk6 | 20 | high |
| m12 | object | individuals | individual | noun_chunk_root | chunk8 | 29 | high |
| m13 | quantity | Several | several | approximate_quantity | chunk8 | 28 | medium |
| m14 | context | front | front | spatial_region | chunk9 | 36 | medium |
| m15 | object | screen | screen | noun_chunk_root | chunk10 | 40 | high |
| m16 | action | sit | sit | verb_predicate | doc | 3 | high |
| m17 | action | displays | display | verb_predicate | doc | 17 | high |
| m18 | action | including | include | verb_predicate | doc | 22 | high |
| m19 | action | seated | seat | verb_predicate | doc | 31 | high |
| m20 | action | standing | stand | verb_predicate | doc | 33 | high |
| m21 | action | facing | face | verb_predicate | doc | 38 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m3 | m4 | high | chunk2 amod -> desks |
| e1 | has_attribute | m5 | m6 | high | chunk3 amod -> chamber |
| e2 | has_attribute | m5 | m7 | medium | chunk3 amod -> chamber |
| e3 | has_attribute | m8 | m9 | high | chunk4 amod -> screen |
| e4 | has_quantity | m12 | m13 | medium | chunk8 quantity -> individuals |
| e5 | agent | m16 | m1 | medium | nsubj -> sit |
| e6 | agent | m17 | m8 | medium | nsubj -> displays |
| e7 | patient | m17 | m10 | medium | dobj -> displays |
| e8 | agent | m18 | m10 | medium | inherited agent prep -> text |
| e9 | patient | m18 | m0 | medium | pobj -> including |
| e10 | agent | m19 | m12 | medium | nsubjpass -> seated |
| e11 | agent | m20 | m12 | medium | inherited agent conj -> seated |
| e12 | agent | m21 | m12 | medium | inherited agent conj -> standing |
| e13 | patient | m21 | m15 | medium | dobj -> facing |
| e14 | relation | m1 | m2 | high | in |
| e15 | relation | m1 | m3 | medium | at |
| e16 | relation | m1 | m5 | high | in |
| e17 | relation | m10 | m11 | high | in |
| e18 | relation | m10 | m0 | medium | include |
| e19 | relation | m12 | m14 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | people | People | person | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | suit | suits | clothing | clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:suit", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | desk | desks | object | furniture, artifact | m3 | raw_mention |  |  |  | True | {"canonical": "entity:desk", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m5 | object | chamber | chamber | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:chamber", "parents": []} |
| ent_m8 | object | screen | screen | device | device, artifact | m8 | raw_mention |  |  |  | True | {"canonical": "entity:screen", "parents": ["entity_parent:device", "entity_parent:artifact"]} |
| ent_m10 | object | text | text | document | text_content | m10 | raw_mention |  |  |  | True | {"canonical": "entity:text", "parents": ["entity_parent:text_content"]} |
| ent_m11 | object | portuguese | Portuguese | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:portuguese", "parents": []} |
| ent_m12 | object | individual | individuals | object |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:individual", "parents": []} |
| ent_m14 | context | front | front | object | scene_context | m14 | raw_mention |  |  |  | True | {"canonical": "entity:front", "parents": ["entity_parent:scene_context"]} |
| ent_m15 | object | screen | screen | device | device, artifact | m15 | raw_mention |  |  |  | True | {"canonical": "entity:screen", "parents": ["entity_parent:device", "entity_parent:artifact"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | sit | sit | sit | body_pose_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m17 | displays | display | display | visual_action |  | agent:m8->ent_m8; patient:m10->ent_m10 | {"canonical": "action:display", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m18 | including | include | include | visual_action |  | agent:m10->ent_m10; patient:m0->None | {"canonical": "action:include", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m19 | seated | seat | sit | body_pose_action, visual_action |  | theme:m12->ent_m12 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce4 | m20 | standing | stand | stand | body_pose_action, visual_action |  | agent:m12->ent_m12 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce5 | m21 | facing | face | face | orientation_action, visual_action |  | agent:m12->ent_m12; patient:m15->ent_m15 | {"canonical": "action:face", "parents": ["action_parent:orientation_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m1 | ent_m1 | medium | e5 | nsubj -> sit |  |  |
| ce1 | display | agent | m8 | ent_m8 | medium | e6 | nsubj -> displays |  |  |
| ce1 | display | patient | m10 | ent_m10 | medium | e7 | dobj -> displays |  |  |
| ce2 | include | agent | m10 | ent_m10 | medium | e8 | inherited agent prep -> text |  |  |
| ce2 | include | patient | m0 |  | medium | e9 | pobj -> including |  |  |
| ce3 | sit | theme | m12 | ent_m12 | medium | e10 | nsubjpass -> seated |  |  |
| ce4 | stand | agent | m12 | ent_m12 | medium | e11 | inherited agent conj -> seated |  |  |
| ce5 | face | agent | m12 | ent_m12 | medium | e12 | inherited agent conj -> standing |  |  |
| ce5 | face | patient | m15 | ent_m15 | medium | e13 | dobj -> facing |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | in | in | spatial_containment, visual_relation | high | e14 | False | False |  |  |
| cr1 | m1 | m3 | ent_m1 | ent_m3 | at | at | spatial_location, visual_relation | medium | e15 | False | False |  |  |
| cr2 | m1 | m5 | ent_m1 | ent_m5 | in | in | spatial_containment, visual_relation | high | e16 | False | False |  |  |
| cr3 | m10 | m11 | ent_m10 | ent_m11 | in | in | spatial_containment, visual_relation | high | e17 | False | False |  |  |
| cr4 | m10 | m0 | ent_m10 |  | include | include | visual_relation | medium | e18 | False | False |  |  |
| cr5 | m12 | m14 | ent_m12 | ent_m14 | near | near | spatial_proximity, visual_relation | high | e19 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | suit |  |  | clothing, wearable | entity_exists:suit | True | high |
| cf2 | entity_exists | desk |  |  | furniture, artifact | entity_exists:desk | True | high |
| cf3 | entity_exists | chamber |  |  |  | entity_exists:chamber | True | low |
| cf4 | entity_exists | screen |  |  | device, artifact | entity_exists:screen | True | high |
| cf5 | entity_exists | text |  |  | text_content | entity_exists:text | True | high |
| cf6 | entity_exists | portuguese |  |  |  | entity_exists:portuguese | True | low |
| cf7 | entity_exists | individual |  |  |  | entity_exists:individual | True | low |
| cf8 | entity_exists | front |  |  | scene_context | entity_exists:front | True | medium |
| cf9 | entity_exists | screen |  |  | device, artifact | entity_exists:screen | True | high |
| cf10 | has_attribute | desk | wooden |  | material_attribute, material, visual_attribute | has_attribute:desk:wooden | True | high |
| cf11 | has_attribute | chamber | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:chamber:large | True | high |
| cf12 | has_attribute | chamber | legislative |  | modifier_attribute, visual_attribute | has_attribute:chamber:legislative | True | medium |
| cf13 | has_attribute | screen | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:screen:large | True | high |
| cf14 | has_quantity | individual | several |  | approximate_quantity, quantity | has_quantity:individual:several | True | medium |
| cf15 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf16 | event_role | sit | agent | people |  | event_role:sit:agent:people | True | medium |
| cf17 | action_event | display |  |  | visual_action | action_event:display | True | low |
| cf18 | event_role | display | agent | screen |  | event_role:display:agent:screen | True | medium |
| cf19 | event_role | display | patient | text |  | event_role:display:patient:text | True | medium |
| cf20 | action_event | include |  |  | visual_action | action_event:include | True | low |
| cf21 | event_role | include | agent | text |  | event_role:include:agent:text | True | medium |
| cf22 | event_role | include | patient |  |  | event_role:include:patient | False | medium |
| cf23 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf24 | event_role | sit | theme | individual |  | event_role:sit:theme:individual | True | medium |
| cf25 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf26 | event_role | stand | agent | individual |  | event_role:stand:agent:individual | True | medium |
| cf27 | action_event | face |  |  | orientation_action, visual_action | action_event:face | True | high |
| cf28 | event_role | face | agent | individual |  | event_role:face:agent:individual | True | medium |
| cf29 | event_role | face | patient | screen |  | event_role:face:patient:screen | True | medium |
| cf30 | relation | people | in | suit | spatial_containment, visual_relation | relation:people:in:suit | True | high |
| cf31 | relation | people | at | desk | spatial_location, visual_relation | relation:people:at:desk | True | medium |
| cf32 | relation | people | in | chamber | spatial_containment, visual_relation | relation:people:in:chamber | True | high |
| cf33 | relation | text | in | portuguese | spatial_containment, visual_relation | relation:text:in:portuguese | True | high |
| cf34 | relation | text | include |  | visual_relation | relation:text:include | False | medium |
| cf35 | relation | individual | near | front | spatial_proximity, visual_relation | relation:individual:near:front | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| action_lexical_canonicalized | m19 |  |  |  |  | {"action_mention_id": "m19", "canonical": "sit", "kind": "action_lexical_canonicalized", "raw_canonical_action": "seat", "source": "stage9_seed"} |
| passive_subject_to_theme | m19 | e10 | m12 |  |  | {"action_mention_id": "m19", "kind": "passive_subject_to_theme", "raw_edge_id": "e10", "target": "m12"} |

## 79

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `3fd213aa27d03cea945474fbd22867b9a96db60cb511f2579c214920945ccc14`
**parse_path:** `tag_list`

> gold medal, ribbon, pin, cross

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | medal | medal | segment_head | t0 | 1 | high |
| m1 | attribute | gold | gold | attribute | t0 | 0 | high |
| m2 | object | ribbon | ribbon | segment_head | t1 | 0 | high |
| m3 | object | pin | pin | segment_head | t2 | 0 | high |
| m4 | object | cross | cross | segment_head | t3 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> medal |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | medal | medal | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:medal", "parents": []} |
| ent_m2 | object | ribbon | ribbon | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:ribbon", "parents": []} |
| ent_m3 | object | pin | pin | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:pin", "parents": []} |
| ent_m4 | object | cross | cross | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:cross", "parents": []} |

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
| cf0 | entity_exists | medal |  |  |  | entity_exists:medal | True | low |
| cf1 | entity_exists | ribbon |  |  |  | entity_exists:ribbon | True | low |
| cf2 | entity_exists | pin |  |  |  | entity_exists:pin | True | low |
| cf3 | entity_exists | cross |  |  |  | entity_exists:cross | True | low |
| cf4 | has_attribute | medal | gold |  | color_attribute, color, visual_attribute | has_attribute:medal:gold | True | high |

### Stage 9 Canonicalization Notes
_none_

## 80

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `40ccbff955e113a1f352c3648a1521830574e2870d90a14c32cf857d1d185814`
**parse_path:** `sentence`

> A square, dark gray slab with a rough, uneven surface rests on a light-colored flat background. The object has visible texture and minor imperfections, suggesting it may be made of stone or metal. Its edges are slightly irregular, and it appears stationary.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | slab | slab | noun_chunk_root | chunk0 | 5 | high |
| m1 | attribute | square | square | modifier_attribute | chunk0 | 1 | medium |
| m2 | attribute | dark | dark | visual_attribute | chunk0 | 3 | medium |
| m3 | attribute | gray | gray | color_attribute | chunk0 | 4 | high |
| m4 | context | surface | surface | spatial_region | chunk1 | 11 | medium |
| m5 | context | background | background | scene_context | chunk2 | 17 | high |
| m6 | attribute | light-colored | light-colored | modifier_attribute | chunk2 | 15 | medium |
| m7 | attribute | flat | flat | modifier_attribute | chunk2 | 16 | medium |
| m9 | object | texture | texture | noun_chunk_root | chunk4 | 23 | high |
| m10 | attribute | visible | visible | modifier_attribute | chunk4 | 22 | medium |
| m11 | object | imperfections | imperfection | noun_chunk_root | chunk5 | 26 | high |
| m12 | attribute | minor | minor | modifier_attribute | chunk5 | 25 | medium |
| m13 | object | stone | stone | noun_chunk_root | chunk7 | 34 | high |
| m14 | object | metal | metal | noun_chunk_root | chunk8 | 36 | high |
| m15 | object | edges | edge | noun_chunk_root | chunk9 | 39 | high |
| m16 | reference | The object | object | generic_object_reference | generic_anaphoric | 20 | high |
| m17 | action | rests | rest | verb_predicate | doc | 12 | high |
| m18 | action | has | have | verb_predicate | doc | 21 | high |
| m19 | action | suggesting | suggest | verb_predicate | doc | 28 | high |
| m20 | action | made | make | verb_predicate | doc | 32 | high |
| m21 | action | appears | appear | verb_predicate | doc | 46 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> slab |
| e1 | has_attribute | m0 | m2 | medium | chunk0 amod -> slab |
| e2 | has_attribute | m0 | m3 | high | chunk0 amod -> slab |
| e3 | has_context | scene | m5 | high | scene_context token background |
| e4 | has_attribute | m5 | m6 | medium | chunk2 amod -> background |
| e5 | has_attribute | m5 | m7 | medium | chunk2 amod -> background |
| e6 | has_attribute | m9 | m10 | medium | chunk4 amod -> texture |
| e7 | has_attribute | m11 | m12 | medium | chunk5 amod -> imperfections |
| e8 | refers_to | m16 | m0 | high | generic definite NP score=150 margin=150 |
| e9 | agent | m17 | m0 | medium | nsubj -> rests |
| e10 | agent | m18 | m0 | medium | nsubj -> has; resolved object -> slab |
| e11 | patient | m18 | m9 | medium | dobj -> has |
| e12 | patient | m18 | m11 | medium | dobj -> has |
| e13 | agent | m19 | m0 | medium | inherited agent advcl -> has |
| e14 | agent | m20 | m0 | medium | nsubjpass -> made; resolved it -> slab |
| e15 | agent | m21 | m15 | medium | nsubj -> appears; resolved it -> edges |
| e16 | relation | m0 | m4 | high | with |
| e17 | relation | m0 | m5 | high | on |
| e18 | relation | m0 | m13 | medium | of |
| e19 | relation | m0 | m14 | medium | of |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | slab | slab | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:slab", "parents": []} |
| ent_m4 | context | surface | surface | object | scene_context | m4 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": ["entity_parent:scene_context"]} |
| ent_m5 | context | background | background | object | scene_context | m5 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m9 | object | texture | texture | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:texture", "parents": []} |
| ent_m11 | object | imperfection | imperfections | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:imperfection", "parents": []} |
| ent_m13 | object | stone | stone | object |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:stone", "parents": []} |
| ent_m14 | object | metal | metal | object |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:metal", "parents": []} |
| ent_m15 | object | edge | edges | object |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:edge", "parents": []} |
| eref_m16 | reference | slab | The object | object |  | m16 | stage9_reference | ent_m0 |  |  | True | {"canonical": "entity:slab", "parents": []} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m16 | eref_m16 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | rests | rest | rest | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:rest", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m18 | has | have | have | visual_action |  | agent:m0->ent_m0; patient:m9->ent_m9; patient:m11->ent_m11 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m19 | suggesting | suggest | suggest | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:suggest", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m20 | made | make | make | visual_action |  | theme:m0->ent_m0 | {"canonical": "action:make", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m21 | appears | appear | appear | visual_action |  | agent:m15->ent_m15 | {"canonical": "action:appear", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | rest | agent | m0 | ent_m0 | medium | e9 | nsubj -> rests |  |  |
| ce1 | have | agent | m0 | ent_m0 | medium | e10 | nsubj -> has; resolved object -> slab |  |  |
| ce1 | have | patient | m9 | ent_m9 | medium | e11 | dobj -> has |  |  |
| ce1 | have | patient | m11 | ent_m11 | medium | e12 | dobj -> has |  |  |
| ce2 | suggest | agent | m0 | ent_m0 | medium | e13 | inherited agent advcl -> has |  |  |
| ce3 | make | theme | m0 | ent_m0 | medium | e14 | nsubjpass -> made; resolved it -> slab |  |  |
| ce4 | appear | agent | m15 | ent_m15 | medium | e15 | nsubj -> appears; resolved it -> edges |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | with | with | association_relation, visual_relation | high | e16 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | on | spatial_support, visual_relation | high | e17 | False | False |  |  |
| cr2 | m0 | m13 | ent_m0 | ent_m13 | of | of | part_relation, visual_relation | medium | e18 | False | False |  |  |
| cr3 | m0 | m14 | ent_m0 | ent_m14 | of | of | part_relation, visual_relation | medium | e19 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | slab |  |  |  | entity_exists:slab | True | low |
| cf1 | entity_exists | surface |  |  | scene_context | entity_exists:surface | True | medium |
| cf2 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf3 | entity_exists | texture |  |  |  | entity_exists:texture | True | low |
| cf4 | entity_exists | imperfection |  |  |  | entity_exists:imperfection | True | low |
| cf5 | entity_exists | stone |  |  |  | entity_exists:stone | True | low |
| cf6 | entity_exists | metal |  |  |  | entity_exists:metal | True | low |
| cf7 | entity_exists | edge |  |  |  | entity_exists:edge | True | low |
| cf8 | entity_exists | slab |  |  |  | entity_exists:slab | True | low |
| cf9 | has_attribute | slab | square |  | shape_attribute, shape, visual_attribute | has_attribute:slab:square | True | medium |
| cf10 | has_attribute | slab | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:slab:dark | True | medium |
| cf11 | has_attribute | slab | gray |  | color_attribute, color, visual_attribute | has_attribute:slab:gray | True | high |
| cf12 | has_attribute | background | light-colored |  | modifier_attribute, visual_attribute | has_attribute:background:light-colored | True | medium |
| cf13 | has_attribute | background | flat |  | shape_attribute, coco_subtype_rule, visual_attribute | has_attribute:background:flat | True | medium |
| cf14 | has_attribute | texture | visible |  | modifier_attribute, visual_attribute | has_attribute:texture:visible | True | medium |
| cf15 | has_attribute | imperfection | minor |  | modifier_attribute, visual_attribute | has_attribute:imperfection:minor | True | medium |
| cf16 | action_event | rest |  |  | visual_action | action_event:rest | True | low |
| cf17 | event_role | rest | agent | slab |  | event_role:rest:agent:slab | True | medium |
| cf18 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf19 | event_role | have | agent | slab |  | event_role:have:agent:slab | True | medium |
| cf20 | event_role | have | patient | texture |  | event_role:have:patient:texture | True | medium |
| cf21 | event_role | have | patient | imperfection |  | event_role:have:patient:imperfection | True | medium |
| cf22 | action_event | suggest |  |  | visual_action | action_event:suggest | True | low |
| cf23 | event_role | suggest | agent | slab |  | event_role:suggest:agent:slab | True | medium |
| cf24 | action_event | make |  |  | visual_action | action_event:make | True | low |
| cf25 | event_role | make | theme | slab |  | event_role:make:theme:slab | True | medium |
| cf26 | action_event | appear |  |  | visual_action | action_event:appear | True | low |
| cf27 | event_role | appear | agent | edge |  | event_role:appear:agent:edge | True | medium |
| cf28 | relation | slab | with | surface | association_relation, visual_relation | relation:slab:with:surface | True | high |
| cf29 | relation | slab | on | background | spatial_support, visual_relation | relation:slab:on:background | True | high |
| cf30 | relation | slab | of | stone | part_relation, visual_relation | relation:slab:of:stone | True | medium |
| cf31 | relation | slab | of | metal | part_relation, visual_relation | relation:slab:of:metal | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m20 | e14 | m0 |  |  | {"action_mention_id": "m20", "kind": "passive_subject_to_theme", "raw_edge_id": "e14", "target": "m0"} |

## 81

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `4137bc66f4d1f6035892ec5f727cc91dc7d31ade7927509d1882e3b883915014`
**parse_path:** `sentence`

> Snow-covered trees stand on a snowy hill under a clear blue sky.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | trees | tree | noun_chunk_root | chunk0 | 1 | high |
| m1 | attribute | Snow-covered | snow-covered | modifier_attribute | chunk0 | 0 | medium |
| m2 | object | hill | hill | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | snowy | snowy | modifier_attribute | chunk1 | 5 | medium |
| m4 | object | sky | sky | noun_chunk_root | chunk2 | 11 | high |
| m5 | attribute | clear | clear | visual_attribute | chunk2 | 9 | medium |
| m6 | attribute | blue | blue | color_attribute | chunk2 | 10 | high |
| m7 | action | stand | stand | verb_predicate | doc | 2 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> trees |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> hill |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> sky |
| e3 | has_attribute | m4 | m6 | high | chunk2 amod -> sky |
| e4 | agent | m7 | m0 | medium | nsubj -> stand |
| e5 | relation | m0 | m2 | high | on |
| e6 | relation | m0 | m4 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | tree | trees | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m2 | object | hill | hill | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:hill", "parents": []} |
| ent_m4 | object | sky | sky | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | stand | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e4 | nsubj -> stand |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | on | spatial_support, visual_relation | high | e5 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | under | under | spatial_vertical, visual_relation | high | e6 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf1 | entity_exists | hill |  |  |  | entity_exists:hill | True | low |
| cf2 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf3 | has_attribute | tree | snow-covered |  | modifier_attribute, visual_attribute | has_attribute:tree:snow-covered | True | medium |
| cf4 | has_attribute | hill | snowy |  | material_attribute, material, visual_attribute | has_attribute:hill:snowy | True | medium |
| cf5 | has_attribute | sky | clear |  | weather_attribute, opaqeness, weather, visual_attribute | has_attribute:sky:clear | True | medium |
| cf6 | has_attribute | sky | blue |  | color_attribute, color, visual_attribute | has_attribute:sky:blue | True | high |
| cf7 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf8 | event_role | stand | agent | tree |  | event_role:stand:agent:tree | True | medium |
| cf9 | relation | tree | on | hill | spatial_support, visual_relation | relation:tree:on:hill | True | high |
| cf10 | relation | tree | under | sky | spatial_vertical, visual_relation | relation:tree:under:sky | True | high |

### Stage 9 Canonicalization Notes
_none_

## 82

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `4220764c409a789c7cf2ce02bf17e8ed251f5213b62c1e2adbe9ec0687c82014`
**parse_path:** `sentence`

> A young woman with long brown hair smiles, wearing a red and black striped shirt and large hoop earrings.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | young | young | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | hair | hair | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | long | long | size_attribute | chunk1 | 4 | high |
| m4 | attribute | brown | brown | color_attribute | chunk1 | 5 | high |
| m5 | object | shirt | shirt | noun_chunk_root | chunk2 | 15 | high |
| m6 | attribute | red | red | color_attribute | chunk2 | 11 | high |
| m7 | attribute | black | black | color_attribute | chunk2 | 13 | high |
| m8 | attribute | striped | striped | modifier_attribute | chunk2 | 14 | medium |
| m9 | object | earrings | earring | noun_chunk_root | chunk3 | 19 | high |
| m10 | attribute | large | large | size_attribute | chunk3 | 17 | high |
| m11 | attribute | hoop | hoop | compound_modifier | chunk3 | 18 | medium |
| m12 | action | smiles | smile | verb_predicate | doc | 7 | high |
| m13 | action | wearing | wear | verb_predicate | doc | 9 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> woman |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> hair |
| e2 | has_attribute | m2 | m4 | high | chunk1 amod -> hair |
| e3 | has_attribute | m5 | m6 | high | chunk2 amod -> shirt |
| e4 | has_attribute | m5 | m7 | high | chunk2 conj -> shirt |
| e5 | has_attribute | m5 | m8 | medium | chunk2 amod -> shirt |
| e6 | has_attribute | m9 | m10 | high | chunk3 amod -> earrings |
| e7 | has_attribute | m9 | m11 | medium | chunk3 compound -> earrings |
| e8 | agent | m12 | m0 | medium | nsubj -> smiles |
| e9 | agent | m13 | m0 | medium | inherited agent advcl -> smiles |
| e10 | patient | m13 | m5 | medium | dobj -> wearing |
| e11 | patient | m13 | m9 | medium | dobj -> wearing |
| e12 | relation | m0 | m2 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | hair | hair | object | body_part | m2 | raw_mention |  |  |  | True | {"canonical": "entity:hair", "parents": ["entity_parent:body_part"]} |
| ent_m5 | object | shirt | shirt | clothing | clothing, wearable | m5 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m9 | object | earring | earrings | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:earring", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | smiles | smile | smile | expression_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:smile", "parents": ["action_parent:expression_action", "action_parent:visual_action"]} |  |
| ce1 | m13 | wearing | wear | wear | wearing_action, visual_action |  | agent:m0->ent_m0; patient:m5->ent_m5; patient:m9->ent_m9 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | smile | agent | m0 | ent_m0 | medium | e8 | nsubj -> smiles |  |  |
| ce1 | wear | agent | m0 | ent_m0 | medium | e9 | inherited agent advcl -> smiles |  |  |
| ce1 | wear | patient | m5 | ent_m5 | medium | e10 | dobj -> wearing |  |  |
| ce1 | wear | patient | m9 | ent_m9 | medium | e11 | dobj -> wearing |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e12 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | hair |  |  | body_part | entity_exists:hair | True | high |
| cf2 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf3 | entity_exists | earring |  |  |  | entity_exists:earring | True | low |
| cf4 | has_attribute | woman | young |  | modifier_attribute, visual_attribute | has_attribute:woman:young | True | medium |
| cf5 | has_attribute | hair | long |  | size_attribute, clean_exact_overlap, length, visual_attribute | has_attribute:hair:long | True | high |
| cf6 | has_attribute | hair | brown |  | color_attribute, color, visual_attribute | has_attribute:hair:brown | True | high |
| cf7 | has_attribute | shirt | red |  | color_attribute, color, visual_attribute | has_attribute:shirt:red | True | high |
| cf8 | has_attribute | shirt | black |  | color_attribute, color, visual_attribute | has_attribute:shirt:black | True | high |
| cf9 | has_attribute | shirt | striped |  | pattern_attribute, clean_exact_overlap, pattern, pattern_marking, texture, visual_attribute | has_attribute:shirt:striped | True | medium |
| cf10 | has_attribute | earring | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:earring:large | True | high |
| cf11 | has_attribute | earring | hoop |  | compound_modifier, visual_attribute | has_attribute:earring:hoop | True | medium |
| cf12 | action_event | smile |  |  | expression_action, visual_action | action_event:smile | True | high |
| cf13 | event_role | smile | agent | woman |  | event_role:smile:agent:woman | True | medium |
| cf14 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf15 | event_role | wear | agent | woman |  | event_role:wear:agent:woman | True | medium |
| cf16 | event_role | wear | patient | shirt |  | event_role:wear:patient:shirt | True | medium |
| cf17 | event_role | wear | patient | earring |  | event_role:wear:patient:earring | True | medium |
| cf18 | relation | woman | with | hair | association_relation, visual_relation | relation:woman:with:hair | True | high |

### Stage 9 Canonicalization Notes
_none_

## 83

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `44f8a614329a02e0c0056eaab4a12c0a514594fe2368415f7e48097ac9189014`
**parse_path:** `sentence`

> Football players in green and white uniforms run on a field during a game. A referee in black and white stands nearby.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | Football players | football_player | noun_chunk_root | chunk0 | 0 | high |
| m1 | object | uniforms | uniform | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | green | green | color_attribute | chunk1 | 2 | high |
| m3 | attribute | white | white | color_attribute | chunk1 | 4 | high |
| m4 | object | field | field | noun_chunk_root | chunk2 | 9 | high |
| m5 | object | game | game | noun_chunk_root | chunk3 | 12 | high |
| m6 | object | referee | referee | noun_chunk_root | chunk4 | 15 | high |
| m7 | attribute | black | black | color_attribute | chunk5 | 17 | high |
| m8 | attribute | white | white | color_attribute | chunk6 | 19 | high |
| m9 | action | run | run | verb_predicate | doc | 6 | high |
| m10 | action | stands | stand | verb_predicate | doc | 20 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> uniforms |
| e1 | has_attribute | m1 | m3 | high | chunk1 conj -> uniforms |
| e2 | agent | m9 | m0 | medium | nsubj -> run |
| e3 | agent | m10 | m6 | medium | nsubj -> stands |
| e4 | relation | m0 | m1 | high | in |
| e5 | relation | m0 | m4 | high | on |
| e6 | relation | m0 | m5 | medium | during |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | football_player | Football players | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:football_player", "parents": []} |
| ent_m1 | object | uniform | uniforms | clothing | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m4 | object | field | field | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |
| ent_m5 | object | game | game | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:game", "parents": []} |
| ent_m6 | object | referee | referee | person | person, human | m6 | raw_mention |  |  |  | True | {"canonical": "entity:referee", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | run | run | run | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:run", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m10 | stands | stand | stand | body_pose_action, visual_action |  | agent:m6->ent_m6 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | run | agent | m0 | ent_m0 | medium | e2 | nsubj -> run |  |  |
| ce1 | stand | agent | m6 | ent_m6 | medium | e3 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | spatial_containment, visual_relation | high | e4 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | on | spatial_support, visual_relation | high | e5 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | during | during | visual_relation | medium | e6 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | football_player |  |  |  | entity_exists:football_player | True | low |
| cf1 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf2 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf3 | entity_exists | game |  |  |  | entity_exists:game | True | low |
| cf4 | entity_exists | referee |  |  | person, human | entity_exists:referee | True | high |
| cf5 | has_attribute | uniform | green |  | color_attribute, color, visual_attribute | has_attribute:uniform:green | True | high |
| cf6 | has_attribute | uniform | white |  | color_attribute, color, visual_attribute | has_attribute:uniform:white | True | high |
| cf7 | action_event | run |  |  | locomotion_action, visual_action | action_event:run | True | high |
| cf8 | event_role | run | agent | football_player |  | event_role:run:agent:football_player | True | medium |
| cf9 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf10 | event_role | stand | agent | referee |  | event_role:stand:agent:referee | True | medium |
| cf11 | relation | football_player | in | uniform | spatial_containment, visual_relation | relation:football_player:in:uniform | True | high |
| cf12 | relation | football_player | on | field | spatial_support, visual_relation | relation:football_player:on:field | True | high |
| cf13 | relation | football_player | during | game | visual_relation | relation:football_player:during:game | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 84

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `4520335aa9590d3ac5578d1b581822595dc7c25487d871a33c943f90890c4414`
**parse_path:** `tag_list`

> text, page, book, russian, printed

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | text | text | segment_head | t0 | 0 | high |
| m1 | object | page | page | segment_head | t1 | 0 | high |
| m2 | object | book | book | segment_head | t2 | 0 | high |
| m3 | attribute | russian | russian | floating_attribute | t3 | 0 | medium |
| m4 | attribute | printed | print | floating_attribute | t4 | 0 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | candidate_has_attribute | m2 | m3 | low | t3 adjacent floating attribute |
| e1 | candidate_has_attribute | m2 | m4 | low | t4 adjacent floating attribute |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | text | text | document | text_content | m0 | raw_mention |  |  |  | True | {"canonical": "entity:text", "parents": ["entity_parent:text_content"]} |
| ent_m1 | object | page | page | document | document, text_carrier, artifact | m1 | raw_mention |  |  |  | True | {"canonical": "entity:page", "parents": ["entity_parent:document", "entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m2 | object | book | book | document | document, text_carrier, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:book", "parents": ["entity_parent:document", "entity_parent:text_carrier", "entity_parent:artifact"]} |

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
| cf0 | entity_exists | text |  |  | text_content | entity_exists:text | True | high |
| cf1 | entity_exists | page |  |  | document, text_carrier, artifact | entity_exists:page | True | high |
| cf2 | entity_exists | book |  |  | document, text_carrier, artifact | entity_exists:book | True | high |
| cf3 | candidate_has_attribute | book | russian |  | floating_attribute, visual_attribute | candidate_has_attribute:book:russian | False | low |
| cf4 | candidate_has_attribute | book | print |  | floating_attribute, visual_attribute | candidate_has_attribute:book:print | False | low |

### Stage 9 Canonicalization Notes
_none_

## 85

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `4534c60ad9d43cb8de486c52e3839889e81b20688b0308d02dff250997cf5014`
**parse_path:** `tag_list`

> ocean, trees, cloudy sky, coastline, waves

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | ocean | ocean | segment_head | t0 | 0 | high |
| m1 | object | trees | tree | segment_head | t1 | 0 | high |
| m2 | object | sky | sky | segment_head | t2 | 1 | high |
| m3 | attribute | cloudy | cloudy | attribute | t2 | 0 | high |
| m4 | object | coastline | coastline | segment_head | t3 | 0 | high |
| m5 | object | waves | wave | segment_head | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | t2 internal amod -> sky |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | ocean | ocean | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:ocean", "parents": []} |
| ent_m1 | object | tree | trees | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m2 | object | sky | sky | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m4 | object | coastline | coastline | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:coastline", "parents": []} |
| ent_m5 | object | wave | waves | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:wave", "parents": []} |

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
| cf0 | entity_exists | ocean |  |  |  | entity_exists:ocean | True | low |
| cf1 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf2 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf3 | entity_exists | coastline |  |  |  | entity_exists:coastline | True | low |
| cf4 | entity_exists | wave |  |  |  | entity_exists:wave | True | low |
| cf5 | has_attribute | sky | cloudy |  | weather_attribute, weather, visual_attribute | has_attribute:sky:cloudy | True | high |

### Stage 9 Canonicalization Notes
_none_

## 86

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `4629060f393ba0054f5f960b0b8f890a0bd363cac2b8baf241e4d37186c28414`
**parse_path:** `sentence`

> Three boys stand around a green roulette table, placing bets with chips.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | boys | boy | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Three | three | exact_quantity | chunk0 | 0 | high |
| m2 | object | table | table | noun_chunk_root | chunk1 | 7 | high |
| m3 | attribute | green | green | color_attribute | chunk1 | 5 | high |
| m4 | attribute | roulette | roulette | compound_modifier | chunk1 | 6 | medium |
| m5 | object | bets | bet | noun_chunk_root | chunk2 | 10 | high |
| m6 | object | chips | chip | noun_chunk_root | chunk3 | 12 | high |
| m7 | action | stand | stand | verb_predicate | doc | 2 | high |
| m8 | action | placing | place | verb_predicate | doc | 9 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> boys |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> table |
| e2 | has_attribute | m2 | m4 | medium | chunk1 compound -> table |
| e3 | agent | m7 | m0 | medium | nsubj -> stand |
| e4 | agent | m8 | m0 | medium | inherited agent advcl -> stand |
| e5 | patient | m8 | m5 | medium | dobj -> placing |
| e6 | relation | m0 | m2 | high | around |
| e7 | relation | m0 | m6 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | boy | boys | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:boy", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | table | table | object | furniture, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m5 | object | bet | bets | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:bet", "parents": []} |
| ent_m6 | object | chip | chips | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:chip", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | stand | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m8 | placing | place | place | visual_action |  | agent:m0->ent_m0; patient:m5->ent_m5 | {"canonical": "action:place", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e3 | nsubj -> stand |  |  |
| ce1 | place | agent | m0 | ent_m0 | medium | e4 | inherited agent advcl -> stand |  |  |
| ce1 | place | patient | m5 | ent_m5 | medium | e5 | dobj -> placing |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | around | around | spatial_proximity, visual_relation | high | e6 | False | False |  |  |
| cr1 | m0 | m6 | ent_m0 | ent_m6 | with | with | association_relation, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | boy |  |  | person, human | entity_exists:boy | True | high |
| cf1 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf2 | entity_exists | bet |  |  |  | entity_exists:bet | True | low |
| cf3 | entity_exists | chip |  |  |  | entity_exists:chip | True | low |
| cf4 | has_quantity | boy | three |  | exact_quantity, quantity | has_quantity:boy:three | True | high |
| cf5 | has_attribute | table | green |  | color_attribute, color, visual_attribute | has_attribute:table:green | True | high |
| cf6 | has_attribute | table | roulette |  | compound_modifier, visual_attribute | has_attribute:table:roulette | True | medium |
| cf7 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf8 | event_role | stand | agent | boy |  | event_role:stand:agent:boy | True | medium |
| cf9 | action_event | place |  |  | visual_action | action_event:place | True | low |
| cf10 | event_role | place | agent | boy |  | event_role:place:agent:boy | True | medium |
| cf11 | event_role | place | patient | bet |  | event_role:place:patient:bet | True | medium |
| cf12 | relation | boy | around | table | spatial_proximity, visual_relation | relation:boy:around:table | True | high |
| cf13 | relation | boy | with | chip | association_relation, visual_relation | relation:boy:with:chip | True | high |

### Stage 9 Canonicalization Notes
_none_

## 87

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `46ded0945fa518dcf266d085b23d00b0f7e091b16de462d808e44473fc1d4414`
**parse_path:** `tag_list`

> dump truck, orange bed, nighttime, street light, wet ground

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | dump truck | dump_truck | segment_head | t0 | 0 | high |
| m1 | object | bed | bed | segment_head | t1 | 1 | high |
| m2 | attribute | orange | orange | attribute | t1 | 0 | high |
| m3 | context | nighttime | nighttime | scene_context | t2 | 0 | high |
| m4 | object | street light | street_light | segment_head | t3 | 0 | high |
| m5 | object | ground | ground | segment_head | t4 | 1 | high |
| m6 | attribute | wet | wet | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | t1 internal amod -> bed |
| e1 | has_context | scene | m3 | high | t2 context tag |
| e2 | has_attribute | m5 | m6 | high | t4 internal amod -> ground |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | dump_truck | dump truck | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:dump_truck", "parents": []} |
| ent_m1 | object | bed | bed | object | furniture, artifact | m1 | raw_mention |  |  |  | True | {"canonical": "entity:bed", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m3 | context | nighttime | nighttime | object | scene_context | m3 | raw_mention |  |  |  | True | {"canonical": "entity:nighttime", "parents": ["entity_parent:scene_context"]} |
| ent_m4 | object | street_light | street light | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:street_light", "parents": []} |
| ent_m5 | object | ground | ground | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:ground", "parents": []} |

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
| cf0 | entity_exists | dump_truck |  |  |  | entity_exists:dump_truck | True | low |
| cf1 | entity_exists | bed |  |  | furniture, artifact | entity_exists:bed | True | high |
| cf2 | entity_exists | nighttime |  |  | scene_context | entity_exists:nighttime | True | medium |
| cf3 | entity_exists | street_light |  |  |  | entity_exists:street_light | True | low |
| cf4 | entity_exists | ground |  |  |  | entity_exists:ground | True | low |
| cf5 | has_attribute | bed | orange |  | color_attribute, color, visual_attribute | has_attribute:bed:orange | True | high |
| cf6 | has_attribute | ground | wet |  | state_attribute, clean_exact_overlap, state, visual_attribute | has_attribute:ground:wet | True | high |

### Stage 9 Canonicalization Notes
_none_

## 88

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `4796dfef4cc06424f06ef22a84b9650c73e479905f025701ec03baab64fd0414`
**parse_path:** `sentence`

> A woman kneels in grass, planting a small green plant. Another person stands nearby wearing black shoes.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | grass | grass | noun_chunk_root | chunk1 | 4 | high |
| m2 | object | plant | plant | noun_chunk_root | chunk2 | 10 | high |
| m3 | attribute | small | small | size_attribute | chunk2 | 8 | high |
| m4 | attribute | green | green | color_attribute | chunk2 | 9 | high |
| m5 | object | person | person | noun_chunk_root | chunk3 | 13 | high |
| m6 | object | shoes | shoe | noun_chunk_root | chunk4 | 18 | high |
| m7 | attribute | black | black | color_attribute | chunk4 | 17 | high |
| m8 | action | kneels | kneel | verb_predicate | doc | 2 | high |
| m9 | action | planting | plant | verb_predicate | doc | 6 | high |
| m10 | action | stands | stand | verb_predicate | doc | 14 | high |
| m11 | action | wearing | wear | verb_predicate | doc | 16 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | chunk2 amod -> plant |
| e1 | has_attribute | m2 | m4 | high | chunk2 amod -> plant |
| e2 | has_attribute | m6 | m7 | high | chunk4 amod -> shoes |
| e3 | agent | m8 | m0 | medium | nsubj -> kneels |
| e4 | agent | m9 | m0 | medium | inherited agent advcl -> kneels |
| e5 | patient | m9 | m2 | medium | dobj -> planting |
| e6 | agent | m10 | m5 | medium | nsubj -> stands |
| e7 | agent | m11 | m5 | medium | inherited agent advcl -> stands |
| e8 | patient | m11 | m6 | medium | dobj -> wearing |
| e9 | relation | m0 | m1 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | grass | grass | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": []} |
| ent_m2 | object | plant | plant | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:plant", "parents": []} |
| ent_m5 | object | person | person | person | person, human | m5 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m6 | object | shoe | shoes | clothing | clothing, wearable | m6 | raw_mention |  |  |  | True | {"canonical": "entity:shoe", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | kneels | kneel | kneel | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:kneel", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m9 | planting | plant | plant | visual_action |  | agent:m0->ent_m0; patient:m2->ent_m2 | {"canonical": "action:plant", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m10 | stands | stand | stand | body_pose_action, visual_action |  | agent:m5->ent_m5 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce3 | m11 | wearing | wear | wear | wearing_action, visual_action |  | agent:m5->ent_m5; patient:m6->ent_m6 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | kneel | agent | m0 | ent_m0 | medium | e3 | nsubj -> kneels |  |  |
| ce1 | plant | agent | m0 | ent_m0 | medium | e4 | inherited agent advcl -> kneels |  |  |
| ce1 | plant | patient | m2 | ent_m2 | medium | e5 | dobj -> planting |  |  |
| ce2 | stand | agent | m5 | ent_m5 | medium | e6 | nsubj -> stands |  |  |
| ce3 | wear | agent | m5 | ent_m5 | medium | e7 | inherited agent advcl -> stands |  |  |
| ce3 | wear | patient | m6 | ent_m6 | medium | e8 | dobj -> wearing |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | spatial_containment, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | grass |  |  |  | entity_exists:grass | True | low |
| cf2 | entity_exists | plant |  |  |  | entity_exists:plant | True | low |
| cf3 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf4 | entity_exists | shoe |  |  | clothing, wearable | entity_exists:shoe | True | high |
| cf5 | has_attribute | plant | small |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:plant:small | True | high |
| cf6 | has_attribute | plant | green |  | color_attribute, color, visual_attribute | has_attribute:plant:green | True | high |
| cf7 | has_attribute | shoe | black |  | color_attribute, color, visual_attribute | has_attribute:shoe:black | True | high |
| cf8 | action_event | kneel |  |  | visual_action | action_event:kneel | True | low |
| cf9 | event_role | kneel | agent | woman |  | event_role:kneel:agent:woman | True | medium |
| cf10 | action_event | plant |  |  | visual_action | action_event:plant | True | low |
| cf11 | event_role | plant | agent | woman |  | event_role:plant:agent:woman | True | medium |
| cf12 | event_role | plant | patient | plant |  | event_role:plant:patient:plant | True | medium |
| cf13 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf14 | event_role | stand | agent | person |  | event_role:stand:agent:person | True | medium |
| cf15 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf16 | event_role | wear | agent | person |  | event_role:wear:agent:person | True | medium |
| cf17 | event_role | wear | patient | shoe |  | event_role:wear:patient:shoe | True | medium |
| cf18 | relation | woman | in | grass | spatial_containment, visual_relation | relation:woman:in:grass | True | high |

### Stage 9 Canonicalization Notes
_none_

## 89

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `4b92bad03af761f9f17b04d31ec5e98b2a3d7f91093f3ed8a263fbf2b5043c14`
**parse_path:** `sentence`

> Two men stand near a large fire outdoors, one stirring food in a pan over the flames. Another fire burns nearby on the ground.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | men | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Two | two | exact_quantity | chunk0 | 0 | high |
| m2 | object | fire | fire | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | large | large | size_attribute | chunk1 | 5 | high |
| m4 | object | food | food | noun_chunk_root | chunk2 | 11 | high |
| m5 | object | pan | pan | noun_chunk_root | chunk3 | 14 | high |
| m6 | object | flames | flame | noun_chunk_root | chunk4 | 17 | high |
| m7 | object | fire | fire | noun_chunk_root | chunk5 | 20 | high |
| m8 | object | ground | ground | noun_chunk_root | chunk6 | 25 | high |
| m9 | context | outdoors | outdoors | scene_context | doc | 7 | high |
| m10 | reference | one | one | singular_substitute | nominal_reference | 9 | high |
| m11 | action | stand | stand | verb_predicate | doc | 2 | high |
| m12 | action | stirring | stir | verb_predicate | doc | 10 | high |
| m13 | action | burns | burn | verb_predicate | doc | 21 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> men |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> fire |
| e2 | has_context | scene | m9 | high | scene_context token outdoors |
| e3 | refers_to | m10 | m0 | high | singular_substitute one -> men; score=103 |
| e4 | agent | m11 | m0 | medium | nsubj -> stand |
| e5 | agent | m12 | m0 | medium | nsubj -> stirring; resolved one -> men |
| e6 | patient | m12 | m4 | medium | dobj -> stirring |
| e7 | agent | m13 | m7 | medium | nsubj -> burns |
| e8 | relation | m0 | m2 | high | near |
| e9 | relation | m0 | m5 | high | in |
| e10 | relation | m0 | m6 | high | over |
| e11 | relation | m7 | m8 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | men | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | fire | fire | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:fire", "parents": []} |
| ent_m4 | object | food | food | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:food", "parents": []} |
| ent_m5 | object | pan | pan | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:pan", "parents": []} |
| ent_m6 | object | flame | flames | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:flame", "parents": []} |
| ent_m7 | object | fire | fire | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:fire", "parents": []} |
| ent_m8 | object | ground | ground | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:ground", "parents": []} |
| ent_m9 | context | outdoors | outdoors | object | scene_context | m9 | raw_mention |  |  |  | True | {"canonical": "entity:outdoors", "parents": ["entity_parent:scene_context"]} |
| eref_m10 | instance | man | one | person | person, human | m10 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m10 | eref_m10 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m11 | stand | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m12 | stirring | stir | stir | visual_action |  | agent:m0->eref_m10; patient:m4->ent_m4 | {"canonical": "action:stir", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m13 | burns | burn | burn | visual_action |  | agent:m7->ent_m7 | {"canonical": "action:burn", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e4 | nsubj -> stand |  |  |
| ce1 | stir | agent | m0 | eref_m10 | medium | e5 | nsubj -> stirring; resolved one -> men |  |  |
| ce1 | stir | patient | m4 | ent_m4 | medium | e6 | dobj -> stirring |  |  |
| ce2 | burn | agent | m7 | ent_m7 | medium | e7 | nsubj -> burns |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | near | near | spatial_proximity, visual_relation | high | e8 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | in | in | spatial_containment, visual_relation | high | e9 | False | False |  |  |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | over | above | spatial_vertical, visual_relation | high | e10 | False | False |  |  |
| cr3 | m7 | m8 | ent_m7 | ent_m8 | on | on | spatial_support, visual_relation | high | e11 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | fire |  |  |  | entity_exists:fire | True | low |
| cf2 | entity_exists | food |  |  |  | entity_exists:food | True | low |
| cf3 | entity_exists | pan |  |  |  | entity_exists:pan | True | low |
| cf4 | entity_exists | flame |  |  |  | entity_exists:flame | True | low |
| cf5 | entity_exists | fire |  |  |  | entity_exists:fire | True | low |
| cf6 | entity_exists | ground |  |  |  | entity_exists:ground | True | low |
| cf7 | entity_exists | outdoors |  |  | scene_context | entity_exists:outdoors | True | high |
| cf8 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf9 | has_quantity | man | two |  | exact_quantity, quantity | has_quantity:man:two | True | high |
| cf10 | has_attribute | fire | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:fire:large | True | high |
| cf11 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf12 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf13 | action_event | stir |  |  | visual_action | action_event:stir | True | low |
| cf14 | event_role | stir | agent | man |  | event_role:stir:agent:man | True | medium |
| cf15 | event_role | stir | patient | food |  | event_role:stir:patient:food | True | medium |
| cf16 | action_event | burn |  |  | visual_action | action_event:burn | True | low |
| cf17 | event_role | burn | agent | fire |  | event_role:burn:agent:fire | True | medium |
| cf18 | relation | man | near | fire | spatial_proximity, visual_relation | relation:man:near:fire | True | high |
| cf19 | relation | man | in | pan | spatial_containment, visual_relation | relation:man:in:pan | True | high |
| cf20 | relation | man | above | flame | spatial_vertical, visual_relation | relation:man:above:flame | True | high |
| cf21 | relation | fire | on | ground | spatial_support, visual_relation | relation:fire:on:ground | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e10 |  |  |  | {"canonical": "above", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e10", "raw_relation": "over", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 90

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `4bdbef927b2be02d84676c5d4761e2273071526b2c5224f2a1e2195169fc6814`
**parse_path:** `sentence`

> A white fabric tag with the number "1709-1" is stitched onto a bright yellow garment. The tag is slightly frayed at the edges and sits against the textured, wrinkled fabric of the clothing.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "1709-1" | 1709-1 | quote_text | doc_quote | 7 | high |
| m1 | object | tag | tag | noun_chunk_root | chunk0 | 3 | high |
| m2 | attribute | white | white | color_attribute | chunk0 | 1 | high |
| m3 | attribute | fabric | fabric | material_attribute | chunk0 | 2 | high |
| m4 | object | number | number | noun_chunk_root | chunk1 | 6 | high |
| m5 | object | garment | garment | noun_chunk_root | chunk2 | 14 | high |
| m6 | attribute | bright | bright | visual_attribute | chunk2 | 12 | medium |
| m7 | attribute | yellow | yellow | color_attribute | chunk2 | 13 | high |
| m8 | object | tag | tag | noun_chunk_root | chunk3 | 17 | high |
| m9 | context | edges | edge | spatial_region | chunk4 | 23 | medium |
| m10 | object | fabric | fabric | noun_chunk_root | chunk5 | 31 | high |
| m11 | attribute | textured | textured | modifier_attribute | chunk5 | 28 | medium |
| m12 | attribute | wrinkled | wrinkled | modifier_attribute | chunk5 | 30 | medium |
| m13 | object | clothing | clothing | noun_chunk_root | chunk6 | 34 | high |
| m14 | action | stitched | stitch | verb_predicate | doc | 9 | high |
| m15 | action | frayed | fray | verb_predicate | doc | 20 | high |
| m16 | action | sits | sit | verb_predicate | doc | 25 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk0 amod -> tag |
| e1 | has_attribute | m1 | m3 | high | chunk0 compound -> tag |
| e2 | has_attribute | m5 | m6 | medium | chunk2 amod -> garment |
| e3 | has_attribute | m5 | m7 | high | chunk2 amod -> garment |
| e4 | has_attribute | m10 | m11 | medium | chunk5 amod -> fabric |
| e5 | has_attribute | m10 | m12 | medium | chunk5 amod -> fabric |
| e6 | has_attribute | m4 | m0 | high | quote appos -> number |
| e7 | agent | m14 | m1 | medium | nsubjpass -> stitched |
| e8 | agent | m15 | m8 | medium | nsubjpass -> frayed |
| e9 | agent | m16 | m8 | medium | inherited agent conj -> frayed |
| e10 | relation | m1 | m4 | high | with |
| e11 | relation | m1 | m5 | medium | onto |
| e12 | relation | m8 | m9 | medium | at |
| e13 | relation | m8 | m10 | high | against |
| e14 | relation | m10 | m13 | medium | of |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | tag | tag | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:tag", "parents": []} |
| ent_m4 | object | number | number | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:number", "parents": []} |
| ent_m5 | object | garment | garment | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:garment", "parents": []} |
| ent_m8 | object | tag | tag | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:tag", "parents": []} |
| ent_m9 | context | edge | edges | object | scene_context | m9 | raw_mention |  |  |  | True | {"canonical": "entity:edge", "parents": ["entity_parent:scene_context"]} |
| ent_m10 | object | fabric | fabric | object |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:fabric", "parents": []} |
| ent_m13 | object | clothing | clothing | object |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:clothing", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m14 | stitched | stitch | stitch | visual_action |  | theme:m1->ent_m1 | {"canonical": "action:stitch", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m15 | frayed | fray | fray | visual_action |  | theme:m8->ent_m8 | {"canonical": "action:fray", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m16 | sits | sit | sit | body_pose_action, visual_action |  | agent:m8->ent_m8 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stitch | theme | m1 | ent_m1 | medium | e7 | nsubjpass -> stitched |  |  |
| ce1 | fray | theme | m8 | ent_m8 | medium | e8 | nsubjpass -> frayed |  |  |
| ce2 | sit | agent | m8 | ent_m8 | medium | e9 | inherited agent conj -> frayed |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m4 | ent_m1 | ent_m4 | with | with | association_relation, visual_relation | high | e10 | False | False |  |  |
| cr1 | m1 | m5 | ent_m1 | ent_m5 | onto | on | spatial_support, visual_relation | medium | e11 | False | False |  |  |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | at | at | spatial_location, visual_relation | medium | e12 | False | False |  |  |
| cr3 | m8 | m10 | ent_m8 | ent_m10 | against | against | spatial_contact, visual_relation | high | e13 | False | False |  |  |
| cr4 | m10 | m13 | ent_m10 | ent_m13 | of | of | part_relation, visual_relation | medium | e14 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | tag |  |  |  | entity_exists:tag | True | low |
| cf1 | entity_exists | number |  |  |  | entity_exists:number | True | low |
| cf2 | entity_exists | garment |  |  |  | entity_exists:garment | True | low |
| cf3 | entity_exists | tag |  |  |  | entity_exists:tag | True | low |
| cf4 | entity_exists | edge |  |  | scene_context | entity_exists:edge | True | medium |
| cf5 | entity_exists | fabric |  |  |  | entity_exists:fabric | True | low |
| cf6 | entity_exists | clothing |  |  |  | entity_exists:clothing | True | low |
| cf7 | has_attribute | tag | white |  | color_attribute, color, visual_attribute | has_attribute:tag:white | True | high |
| cf8 | has_attribute | tag | fabric |  | material_attribute, material, visual_attribute | has_attribute:tag:fabric | True | high |
| cf9 | has_attribute | garment | bright |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:garment:bright | True | medium |
| cf10 | has_attribute | garment | yellow |  | color_attribute, color, visual_attribute | has_attribute:garment:yellow | True | high |
| cf11 | has_attribute | fabric | textured |  | texture_attribute, texture, visual_attribute | has_attribute:fabric:textured | True | medium |
| cf12 | has_attribute | fabric | wrinkled |  | texture_attribute, texture, visual_attribute | has_attribute:fabric:wrinkled | True | medium |
| cf13 | has_attribute | number | 1709-1 |  | quote_text, visual_attribute | has_attribute:number:1709-1 | True | high |
| cf14 | action_event | stitch |  |  | visual_action | action_event:stitch | True | low |
| cf15 | event_role | stitch | theme | tag |  | event_role:stitch:theme:tag | True | medium |
| cf16 | action_event | fray |  |  | visual_action | action_event:fray | True | low |
| cf17 | event_role | fray | theme | tag |  | event_role:fray:theme:tag | True | medium |
| cf18 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf19 | event_role | sit | agent | tag |  | event_role:sit:agent:tag | True | medium |
| cf20 | relation | tag | with | number | association_relation, visual_relation | relation:tag:with:number | True | high |
| cf21 | relation | tag | on | garment | spatial_support, visual_relation | relation:tag:on:garment | True | medium |
| cf22 | relation | tag | at | edge | spatial_location, visual_relation | relation:tag:at:edge | True | medium |
| cf23 | relation | tag | against | fabric | spatial_contact, visual_relation | relation:tag:against:fabric | True | high |
| cf24 | relation | fabric | of | clothing | part_relation, visual_relation | relation:fabric:of:clothing | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m14 | e7 | m1 |  |  | {"action_mention_id": "m14", "kind": "passive_subject_to_theme", "raw_edge_id": "e7", "target": "m1"} |
| passive_subject_to_theme | m15 | e8 | m8 |  |  | {"action_mention_id": "m15", "kind": "passive_subject_to_theme", "raw_edge_id": "e8", "target": "m8"} |
| relation_lexical_canonicalized |  | e11 |  |  |  | {"canonical": "on", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e11", "raw_relation": "onto", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 91

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `4c3c734e1a2f098c9b6b84ea0d285fc45132f0b736138635798ee19b16700c14`
**parse_path:** `tag_list`

> green hill, forest, trees, foliage, slope

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hill | hill | segment_head | t0 | 1 | high |
| m1 | attribute | green | green | attribute | t0 | 0 | high |
| m2 | object | forest | forest | segment_head | t1 | 0 | high |
| m3 | object | trees | tree | segment_head | t2 | 0 | high |
| m4 | object | foliage | foliage | segment_head | t3 | 0 | high |
| m5 | object | slope | slope | segment_head | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> hill |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hill | hill | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:hill", "parents": []} |
| ent_m2 | object | forest | forest | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:forest", "parents": []} |
| ent_m3 | object | tree | trees | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m4 | object | foliage | foliage | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:foliage", "parents": []} |
| ent_m5 | object | slope | slope | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:slope", "parents": []} |

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
| cf0 | entity_exists | hill |  |  |  | entity_exists:hill | True | low |
| cf1 | entity_exists | forest |  |  |  | entity_exists:forest | True | low |
| cf2 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf3 | entity_exists | foliage |  |  |  | entity_exists:foliage | True | low |
| cf4 | entity_exists | slope |  |  |  | entity_exists:slope | True | low |
| cf5 | has_attribute | hill | green |  | color_attribute, color, visual_attribute | has_attribute:hill:green | True | high |

### Stage 9 Canonicalization Notes
_none_

## 92

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `4c4766ae1c27a85a6d4897a868761e118b7ea64c82d65d1438a894aaedeed814`
**parse_path:** `tag_list`

> conference hall, speaker, red chairs, presentation screen, banner

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hall | hall | segment_head | t0 | 1 | high |
| m1 | attribute | conference | conference | attribute | t0 | 0 | high |
| m2 | object | speaker | speaker | segment_head | t1 | 0 | high |
| m3 | object | chairs | chair | segment_head | t2 | 1 | high |
| m4 | attribute | red | red | attribute | t2 | 0 | high |
| m5 | object | screen | screen | segment_head | t3 | 1 | high |
| m6 | attribute | presentation | presentation | attribute | t3 | 0 | high |
| m7 | object | banner | banner | segment_head | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> hall |
| e1 | has_attribute | m3 | m4 | high | t2 internal amod -> chairs |
| e2 | has_attribute | m5 | m6 | high | t3 internal compound -> screen |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hall | hall | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:hall", "parents": []} |
| ent_m2 | object | speaker | speaker | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:speaker", "parents": []} |
| ent_m3 | object | chair | chairs | object | furniture, artifact | m3 | raw_mention |  |  |  | True | {"canonical": "entity:chair", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m5 | object | screen | screen | device | device, artifact | m5 | raw_mention |  |  |  | True | {"canonical": "entity:screen", "parents": ["entity_parent:device", "entity_parent:artifact"]} |
| ent_m7 | object | banner | banner | object | text_carrier, artifact | m7 | raw_mention |  |  |  | True | {"canonical": "entity:banner", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |

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
| cf0 | entity_exists | hall |  |  |  | entity_exists:hall | True | low |
| cf1 | entity_exists | speaker |  |  |  | entity_exists:speaker | True | low |
| cf2 | entity_exists | chair |  |  | furniture, artifact | entity_exists:chair | True | high |
| cf3 | entity_exists | screen |  |  | device, artifact | entity_exists:screen | True | high |
| cf4 | entity_exists | banner |  |  | text_carrier, artifact | entity_exists:banner | True | high |
| cf5 | has_attribute | hall | conference |  | attribute, visual_attribute | has_attribute:hall:conference | True | high |
| cf6 | has_attribute | chair | red |  | color_attribute, color, visual_attribute | has_attribute:chair:red | True | high |
| cf7 | has_attribute | screen | presentation |  | attribute, visual_attribute | has_attribute:screen:presentation | True | high |

### Stage 9 Canonicalization Notes
_none_

## 93

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `4c56e1b58491d0d3a411f339954e03386183a18bfa198776807c15df358bc014`
**parse_path:** `sentence`

> A man in a suit stands with two officers in brown uniforms and hats outdoors near a brick building.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | suit | suit | noun_chunk_root | chunk1 | 4 | high |
| m2 | object | officers | officer | noun_chunk_root | chunk2 | 8 | high |
| m3 | quantity | two | two | exact_quantity | chunk2 | 7 | high |
| m4 | object | uniforms | uniform | noun_chunk_root | chunk3 | 11 | high |
| m5 | attribute | brown | brown | color_attribute | chunk3 | 10 | high |
| m6 | object | hats | hat | noun_chunk_root | chunk4 | 13 | high |
| m7 | object | building | building | noun_chunk_root | chunk5 | 18 | high |
| m8 | attribute | brick | brick | material_attribute | chunk5 | 17 | high |
| m9 | context | outdoors | outdoors | scene_context | doc | 14 | high |
| m10 | action | stands | stand | verb_predicate | doc | 5 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m2 | m3 | high | chunk2 quantity -> officers |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> uniforms |
| e2 | has_attribute | m7 | m8 | high | chunk5 compound -> building |
| e3 | has_context | scene | m9 | high | scene_context token outdoors |
| e4 | agent | m10 | m0 | medium | nsubj -> stands |
| e5 | relation | m0 | m1 | high | in |
| e6 | relation | m0 | m2 | high | with |
| e7 | relation | m2 | m4 | high | in |
| e8 | relation | m2 | m6 | high | in |
| e9 | relation | m0 | m7 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | suit | suit | clothing | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:suit", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m2 | object | officer | officers | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:officer", "parents": []} |
| ent_m4 | object | uniform | uniforms | clothing | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m6 | object | hat | hats | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:hat", "parents": []} |
| ent_m7 | object | building | building | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |
| ent_m9 | context | outdoors | outdoors | object | scene_context | m9 | raw_mention |  |  |  | True | {"canonical": "entity:outdoors", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | stands | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e4 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | spatial_containment, visual_relation | high | e5 | False | False |  |  |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr2 | m2 | m4 | ent_m2 | ent_m4 | in | in | spatial_containment, visual_relation | high | e7 | False | False |  |  |
| cr3 | m2 | m6 | ent_m2 | ent_m6 | in | in | spatial_containment, visual_relation | high | e8 | False | False |  |  |
| cr4 | m0 | m7 | ent_m0 | ent_m7 | near | near | spatial_proximity, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | suit |  |  | clothing, wearable | entity_exists:suit | True | high |
| cf2 | entity_exists | officer |  |  |  | entity_exists:officer | True | low |
| cf3 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf4 | entity_exists | hat |  |  |  | entity_exists:hat | True | low |
| cf5 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf6 | entity_exists | outdoors |  |  | scene_context | entity_exists:outdoors | True | high |
| cf7 | has_quantity | officer | two |  | exact_quantity, quantity | has_quantity:officer:two | True | high |
| cf8 | has_attribute | uniform | brown |  | color_attribute, color, visual_attribute | has_attribute:uniform:brown | True | high |
| cf9 | has_attribute | building | brick |  | material_attribute, material, visual_attribute | has_attribute:building:brick | True | high |
| cf10 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf11 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf12 | relation | man | in | suit | spatial_containment, visual_relation | relation:man:in:suit | True | high |
| cf13 | relation | man | with | officer | association_relation, visual_relation | relation:man:with:officer | True | high |
| cf14 | relation | officer | in | uniform | spatial_containment, visual_relation | relation:officer:in:uniform | True | high |
| cf15 | relation | officer | in | hat | spatial_containment, visual_relation | relation:officer:in:hat | True | high |
| cf16 | relation | man | near | building | spatial_proximity, visual_relation | relation:man:near:building | True | high |

### Stage 9 Canonicalization Notes
_none_

## 94

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `4d32641dbcf279e49f454f162fee1519d21d7d06d7bb7a3670cf3b687045b414`
**parse_path:** `sentence`

> A forested hillside overlooks a wide, winding river and a turquoise lake, with mountains in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hillside | hillside | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | forested | forested | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | river | river | noun_chunk_root | chunk1 | 8 | high |
| m3 | attribute | wide | wide | size_attribute | chunk1 | 5 | high |
| m4 | attribute | winding | wind | state_attribute | chunk1 | 7 | medium |
| m5 | object | lake | lake | noun_chunk_root | chunk2 | 12 | high |
| m6 | attribute | turquoise | turquoise | color_attribute | chunk2 | 11 | high |
| m7 | object | mountains | mountain | noun_chunk_root | chunk3 | 15 | high |
| m8 | context | background | background | scene_context | chunk4 | 18 | high |
| m9 | action | overlooks | overlook | verb_predicate | doc | 3 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> hillside |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> river |
| e2 | has_attribute | m2 | m4 | medium | chunk1 amod -> river |
| e3 | has_attribute | m5 | m6 | high | chunk2 amod -> lake |
| e4 | has_context | scene | m8 | high | scene_context token background |
| e5 | agent | m9 | m0 | medium | nsubj -> overlooks |
| e6 | patient | m9 | m2 | medium | dobj -> overlooks |
| e7 | patient | m9 | m5 | medium | dobj -> overlooks |
| e8 | relation | m0 | m7 | high | with |
| e9 | relation | m7 | m8 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hillside | hillside | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:hillside", "parents": []} |
| ent_m2 | object | river | river | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:river", "parents": []} |
| ent_m5 | object | lake | lake | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:lake", "parents": []} |
| ent_m7 | object | mountain | mountains | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:mountain", "parents": []} |
| ent_m8 | context | background | background | object | scene_context | m8 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | overlooks | overlook | overlook | visual_action |  | agent:m0->ent_m0; patient:m2->ent_m2; patient:m5->ent_m5 | {"canonical": "action:overlook", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | overlook | agent | m0 | ent_m0 | medium | e5 | nsubj -> overlooks |  |  |
| ce0 | overlook | patient | m2 | ent_m2 | medium | e6 | dobj -> overlooks |  |  |
| ce0 | overlook | patient | m5 | ent_m5 | medium | e7 | dobj -> overlooks |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m7 | ent_m0 | ent_m7 | with | with | association_relation, visual_relation | high | e8 | False | False |  |  |
| cr1 | m7 | m8 | ent_m7 | ent_m8 | in | in | spatial_containment, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | hillside |  |  |  | entity_exists:hillside | True | low |
| cf1 | entity_exists | river |  |  |  | entity_exists:river | True | low |
| cf2 | entity_exists | lake |  |  |  | entity_exists:lake | True | low |
| cf3 | entity_exists | mountain |  |  |  | entity_exists:mountain | True | low |
| cf4 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf5 | has_attribute | hillside | forested |  | modifier_attribute, visual_attribute | has_attribute:hillside:forested | True | medium |
| cf6 | has_attribute | river | wide |  | size_attribute, width, visual_attribute | has_attribute:river:wide | True | high |
| cf7 | has_attribute | river | wind |  | state_attribute, visual_attribute | has_attribute:river:wind | True | medium |
| cf8 | has_attribute | lake | turquoise |  | color_attribute, color, visual_attribute | has_attribute:lake:turquoise | True | high |
| cf9 | action_event | overlook |  |  | visual_action | action_event:overlook | True | low |
| cf10 | event_role | overlook | agent | hillside |  | event_role:overlook:agent:hillside | True | medium |
| cf11 | event_role | overlook | patient | river |  | event_role:overlook:patient:river | True | medium |
| cf12 | event_role | overlook | patient | lake |  | event_role:overlook:patient:lake | True | medium |
| cf13 | relation | hillside | with | mountain | association_relation, visual_relation | relation:hillside:with:mountain | True | high |
| cf14 | relation | mountain | in | background | spatial_containment, visual_relation | relation:mountain:in:background | True | high |

### Stage 9 Canonicalization Notes
_none_

## 95

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `4dc463b2d8ef33464459810bb14ebafc29c1274af7b8e1f4ed9219b4b951d814`
**parse_path:** `tag_list`

> green backpack, blue sign, exhibition booth, person, indoor

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | backpack | backpack | segment_head | t0 | 1 | high |
| m1 | attribute | green | green | attribute | t0 | 0 | high |
| m2 | object | sign | sign | segment_head | t1 | 1 | high |
| m3 | attribute | blue | blue | attribute | t1 | 0 | high |
| m4 | object | booth | booth | segment_head | t2 | 1 | high |
| m5 | attribute | exhibition | exhibition | attribute | t2 | 0 | high |
| m6 | object | person | person | segment_head | t3 | 0 | high |
| m7 | context | indoor | indoor | scene_context | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> backpack |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> sign |
| e2 | has_attribute | m4 | m5 | high | t2 internal compound -> booth |
| e3 | has_context | scene | m7 | high | t4 context tag |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | backpack | backpack | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:backpack", "parents": []} |
| ent_m2 | object | sign | sign | document | text_carrier, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:sign", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m4 | object | booth | booth | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:booth", "parents": []} |
| ent_m6 | object | person | person | person | person, human | m6 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m7 | context | indoor | indoor | object | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:indoor", "parents": ["entity_parent:scene_context"]} |

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
| cf0 | entity_exists | backpack |  |  |  | entity_exists:backpack | True | low |
| cf1 | entity_exists | sign |  |  | text_carrier, artifact | entity_exists:sign | True | high |
| cf2 | entity_exists | booth |  |  |  | entity_exists:booth | True | low |
| cf3 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf4 | entity_exists | indoor |  |  | scene_context | entity_exists:indoor | True | high |
| cf5 | has_attribute | backpack | green |  | color_attribute, color, visual_attribute | has_attribute:backpack:green | True | high |
| cf6 | has_attribute | sign | blue |  | color_attribute, color, visual_attribute | has_attribute:sign:blue | True | high |
| cf7 | has_attribute | booth | exhibition |  | attribute, visual_attribute | has_attribute:booth:exhibition | True | high |

### Stage 9 Canonicalization Notes
_none_

## 96

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `4ee72aa601ec49378a9d19b957a90696b5de2c99d1d4efdde87fad946346d814`
**parse_path:** `sentence`

> A close-up of a dark bee with fuzzy body and transparent wings stands on a dark surface.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | close-up | close-up | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | bee | bee | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | dark | dark | visual_attribute | chunk1 | 4 | medium |
| m3 | object | body | body | noun_chunk_root | chunk2 | 8 | high |
| m4 | attribute | fuzzy | fuzzy | modifier_attribute | chunk2 | 7 | medium |
| m5 | object | wings | wing | noun_chunk_root | chunk3 | 11 | high |
| m6 | attribute | transparent | transparent | modifier_attribute | chunk3 | 10 | medium |
| m7 | context | surface | surface | spatial_region | chunk4 | 16 | medium |
| m8 | action | stands | stand | verb_predicate | doc | 12 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 amod -> bee |
| e1 | has_attribute | m3 | m4 | medium | chunk2 amod -> body |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> wings |
| e3 | agent | m8 | m0 | medium | nsubj -> stands |
| e4 | relation | m0 | m1 | medium | of |
| e5 | relation | m1 | m3 | high | with |
| e6 | relation | m1 | m5 | high | with |
| e7 | relation | m0 | m7 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | close-up | close-up | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:close-up", "parents": []} |
| ent_m1 | object | bee | bee | object |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:bee", "parents": []} |
| ent_m3 | object | body | body | object | body_part | m3 | raw_mention |  |  |  | True | {"canonical": "entity:body", "parents": ["entity_parent:body_part"]} |
| ent_m5 | object | wing | wings | object | body_part | m5 | raw_mention |  |  |  | True | {"canonical": "entity:wing", "parents": ["entity_parent:body_part"]} |
| ent_m7 | context | surface | surface | object | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | stands | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e3 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | of | of | part_relation, visual_relation | medium | e4 | False | False |  |  |
| cr1 | m1 | m3 | ent_m1 | ent_m3 | with | with | association_relation, visual_relation | high | e5 | False | False |  |  |
| cr2 | m1 | m5 | ent_m1 | ent_m5 | with | with | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr3 | m0 | m7 | ent_m0 | ent_m7 | on | on | spatial_support, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | close-up |  |  |  | entity_exists:close-up | True | low |
| cf1 | entity_exists | bee |  |  |  | entity_exists:bee | True | low |
| cf2 | entity_exists | body |  |  | body_part | entity_exists:body | True | high |
| cf3 | entity_exists | wing |  |  | body_part | entity_exists:wing | True | medium |
| cf4 | entity_exists | surface |  |  | scene_context | entity_exists:surface | True | medium |
| cf5 | has_attribute | bee | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:bee:dark | True | medium |
| cf6 | has_attribute | body | fuzzy |  | texture_attribute, coco_subtype_rule, visual_attribute | has_attribute:body:fuzzy | True | medium |
| cf7 | has_attribute | wing | transparent |  | modifier_attribute, visual_attribute | has_attribute:wing:transparent | True | medium |
| cf8 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf9 | event_role | stand | agent | close-up |  | event_role:stand:agent:close-up | True | medium |
| cf10 | relation | close-up | of | bee | part_relation, visual_relation | relation:close-up:of:bee | True | medium |
| cf11 | relation | bee | with | body | association_relation, visual_relation | relation:bee:with:body | True | high |
| cf12 | relation | bee | with | wing | association_relation, visual_relation | relation:bee:with:wing | True | high |
| cf13 | relation | close-up | on | surface | spatial_support, visual_relation | relation:close-up:on:surface | True | high |

### Stage 9 Canonicalization Notes
_none_

## 97

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `4f56ca8847a4a005e4c454c9e252f4b7320e5d66beb78072b93832ab5627e414`
**parse_path:** `sentence`

> A stone church tower with a pointed roof stands against a clear blue sky. Evergreen trees and a stone wall are in the foreground, with a hillside visible behind the building.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | church tower | church_tower | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | stone | stone | material_attribute | chunk0 | 1 | high |
| m2 | object | roof | roof | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | pointed | pointed | modifier_attribute | chunk1 | 5 | medium |
| m4 | object | sky | sky | noun_chunk_root | chunk2 | 12 | high |
| m5 | attribute | clear | clear | visual_attribute | chunk2 | 10 | medium |
| m6 | attribute | blue | blue | color_attribute | chunk2 | 11 | high |
| m7 | object | trees | tree | noun_chunk_root | chunk3 | 15 | high |
| m8 | attribute | Evergreen | evergreen | modifier_attribute | chunk3 | 14 | medium |
| m9 | object | wall | wall | noun_chunk_root | chunk4 | 19 | high |
| m10 | attribute | stone | stone | material_attribute | chunk4 | 18 | high |
| m11 | context | foreground | foreground | scene_context | chunk5 | 23 | high |
| m12 | object | hillside | hillside | noun_chunk_root | chunk6 | 27 | high |
| m13 | object | building | building | noun_chunk_root | chunk7 | 31 | high |
| m14 | action | stands | stand | verb_predicate | doc | 7 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 compound -> church tower |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> roof |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> sky |
| e3 | has_attribute | m4 | m6 | high | chunk2 amod -> sky |
| e4 | has_attribute | m7 | m8 | medium | chunk3 amod -> trees |
| e5 | has_attribute | m9 | m10 | high | chunk4 compound -> wall |
| e6 | has_context | scene | m11 | high | scene_context token foreground |
| e7 | agent | m14 | m0 | medium | nsubj -> stands |
| e8 | relation | m0 | m2 | high | with |
| e9 | relation | m0 | m4 | high | against |
| e10 | relation | m7 | m11 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | church_tower | church tower | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:church_tower", "parents": []} |
| ent_m2 | object | roof | roof | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:roof", "parents": []} |
| ent_m4 | object | sky | sky | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": []} |
| ent_m7 | object | tree | trees | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": []} |
| ent_m9 | object | wall | wall | object |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": []} |
| ent_m11 | context | foreground | foreground | object | scene_context | m11 | raw_mention |  |  |  | True | {"canonical": "entity:foreground", "parents": ["entity_parent:scene_context"]} |
| ent_m12 | object | hillside | hillside | object |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:hillside", "parents": []} |
| ent_m13 | object | building | building | object |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m14 | stands | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e7 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e8 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | against | against | spatial_contact, visual_relation | high | e9 | False | False |  |  |
| cr2 | m7 | m11 | ent_m7 | ent_m11 | in | in | spatial_containment, visual_relation | high | e10 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | church_tower |  |  |  | entity_exists:church_tower | True | low |
| cf1 | entity_exists | roof |  |  |  | entity_exists:roof | True | low |
| cf2 | entity_exists | sky |  |  |  | entity_exists:sky | True | low |
| cf3 | entity_exists | tree |  |  |  | entity_exists:tree | True | low |
| cf4 | entity_exists | wall |  |  |  | entity_exists:wall | True | low |
| cf5 | entity_exists | foreground |  |  | scene_context | entity_exists:foreground | True | high |
| cf6 | entity_exists | hillside |  |  |  | entity_exists:hillside | True | low |
| cf7 | entity_exists | building |  |  |  | entity_exists:building | True | low |
| cf8 | has_attribute | church_tower | stone |  | material_attribute, material, visual_attribute | has_attribute:church_tower:stone | True | high |
| cf9 | has_attribute | roof | pointed |  | modifier_attribute, visual_attribute | has_attribute:roof:pointed | True | medium |
| cf10 | has_attribute | sky | clear |  | weather_attribute, opaqeness, weather, visual_attribute | has_attribute:sky:clear | True | medium |
| cf11 | has_attribute | sky | blue |  | color_attribute, color, visual_attribute | has_attribute:sky:blue | True | high |
| cf12 | has_attribute | tree | evergreen |  | modifier_attribute, visual_attribute | has_attribute:tree:evergreen | True | medium |
| cf13 | has_attribute | wall | stone |  | material_attribute, material, visual_attribute | has_attribute:wall:stone | True | high |
| cf14 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf15 | event_role | stand | agent | church_tower |  | event_role:stand:agent:church_tower | True | medium |
| cf16 | relation | church_tower | with | roof | association_relation, visual_relation | relation:church_tower:with:roof | True | high |
| cf17 | relation | church_tower | against | sky | spatial_contact, visual_relation | relation:church_tower:against:sky | True | high |
| cf18 | relation | tree | in | foreground | spatial_containment, visual_relation | relation:tree:in:foreground | True | high |

### Stage 9 Canonicalization Notes
_none_

## 98

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `503da8cbdc4c15313e8d7891c32a5893a947513d5b58aaf7d26f4b76e852a014`
**parse_path:** `sentence`

> Four people in white lab coats stand at a table, each holding a glass flask. Three men wear goggles and pour liquids into flasks, while a woman in a patterned hijab stands beside them. A logo and text are visible at the top and bottom of the image.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Four | four | exact_quantity | chunk0 | 0 | high |
| m2 | object | lab coats | lab_coat | noun_chunk_root | chunk1 | 4 | high |
| m3 | attribute | white | white | color_attribute | chunk1 | 3 | high |
| m4 | object | table | table | noun_chunk_root | chunk2 | 8 | high |
| m5 | quantity | each | each | distributive_quantity | chunk3 | 10 | high |
| m6 | object | flask | flask | noun_chunk_root | chunk4 | 14 | high |
| m7 | attribute | glass | glass | material_attribute | chunk4 | 13 | high |
| m8 | object | men | man | noun_chunk_root | chunk5 | 17 | high |
| m9 | quantity | Three | three | exact_quantity | chunk5 | 16 | high |
| m10 | object | goggles | goggle | noun_chunk_root | chunk6 | 19 | high |
| m11 | object | liquids | liquid | noun_chunk_root | chunk7 | 22 | high |
| m12 | object | flasks | flask | noun_chunk_root | chunk8 | 24 | high |
| m13 | object | woman | woman | noun_chunk_root | chunk9 | 28 | high |
| m14 | object | hijab | hijab | noun_chunk_root | chunk10 | 32 | high |
| m15 | attribute | patterned | patterned | modifier_attribute | chunk10 | 31 | medium |
| m16 | object | logo | logo | noun_chunk_root | chunk12 | 38 | high |
| m17 | object | text | text | noun_chunk_root | chunk13 | 40 | high |
| m18 | object | bottom | bottom | noun_chunk_root | chunk15 | 47 | high |
| m19 | object | image | image | noun_chunk_root | chunk16 | 50 | high |
| m20 | reference | each | each | distributive_reference | nominal_reference | 10 | high |
| m21 | action | stand | stand | verb_predicate | doc | 5 | high |
| m22 | action | holding | hold | verb_predicate | doc | 11 | high |
| m23 | action | wear | wear | verb_predicate | doc | 18 | high |
| m24 | action | pour | pour | verb_predicate | doc | 21 | high |
| m25 | action | stands | stand | verb_predicate | doc | 33 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> people |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> lab coats |
| e2 | has_attribute | m6 | m7 | high | chunk4 compound -> flask |
| e3 | has_quantity | m8 | m9 | high | chunk5 quantity -> men |
| e4 | has_attribute | m14 | m15 | medium | chunk10 amod -> hijab |
| e5 | refers_to | m20 | m0 | high | distributive_reference each -> people; score=112 |
| e6 | agent | m21 | m0 | medium | nsubj -> stand |
| e7 | agent | m22 | m0 | medium | nsubj -> holding; resolved each -> people |
| e8 | patient | m22 | m6 | medium | dobj -> holding |
| e9 | agent | m23 | m8 | medium | nsubj -> wear |
| e10 | patient | m23 | m10 | medium | dobj -> wear |
| e11 | agent | m24 | m8 | medium | inherited agent conj -> wear |
| e12 | patient | m24 | m11 | medium | dobj -> pour |
| e13 | agent | m25 | m13 | medium | nsubj -> stands |
| e14 | relation | m0 | m2 | high | in |
| e15 | relation | m0 | m4 | medium | at |
| e16 | relation | m8 | m12 | medium | into |
| e17 | relation | m13 | m14 | high | in |
| e18 | relation | m13 | m8 | medium | beside; repaired_self_edge_target from them->woman |
| e19 | relation | m16 | m19 | high | at_top_of |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | lab_coat | lab coats | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:lab_coat", "parents": []} |
| ent_m4 | object | table | table | object | furniture, artifact | m4 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m6 | object | flask | flask | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:flask", "parents": []} |
| ent_m8 | object | man | men | person | person, human | m8 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m10 | object | goggle | goggles | object |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:goggle", "parents": []} |
| ent_m11 | object | liquid | liquids | object |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:liquid", "parents": []} |
| ent_m12 | object | flask | flasks | object |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:flask", "parents": []} |
| ent_m13 | object | woman | woman | person | person, human | m13 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m14 | object | hijab | hijab | object |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:hijab", "parents": []} |
| ent_m16 | object | logo | logo | object |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:logo", "parents": []} |
| ent_m17 | object | text | text | document | text_content | m17 | raw_mention |  |  |  | True | {"canonical": "entity:text", "parents": ["entity_parent:text_content"]} |
| ent_m18 | object | bottom | bottom | object |  | m18 | raw_mention |  |  |  | True | {"canonical": "entity:bottom", "parents": []} |
| ent_m19 | object | image | image | object |  | m19 | raw_mention |  |  |  | True | {"canonical": "entity:image", "parents": []} |
| eref_m20 | reference | people | each | person | person, human | m20 | stage9_reference | ent_m0 |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m20 | eref_m20 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m21 | stand | stand | stand | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m22 | holding | hold | hold | manipulation_action, visual_action |  | agent:m0->eref_m20; patient:m6->ent_m6 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce2 | m23 | wear | wear | wear | wearing_action, visual_action |  | agent:m8->ent_m8; patient:m10->ent_m10 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce3 | m24 | pour | pour | pour | visual_action |  | agent:m8->ent_m8; patient:m11->ent_m11 | {"canonical": "action:pour", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m25 | stands | stand | stand | body_pose_action, visual_action |  | agent:m13->ent_m13 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e6 | nsubj -> stand |  |  |
| ce1 | hold | agent | m0 | eref_m20 | medium | e7 | nsubj -> holding; resolved each -> people |  |  |
| ce1 | hold | patient | m6 | ent_m6 | medium | e8 | dobj -> holding |  |  |
| ce2 | wear | agent | m8 | ent_m8 | medium | e9 | nsubj -> wear |  |  |
| ce2 | wear | patient | m10 | ent_m10 | medium | e10 | dobj -> wear |  |  |
| ce3 | pour | agent | m8 | ent_m8 | medium | e11 | inherited agent conj -> wear |  |  |
| ce3 | pour | patient | m11 | ent_m11 | medium | e12 | dobj -> pour |  |  |
| ce4 | stand | agent | m13 | ent_m13 | medium | e13 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | spatial_containment, visual_relation | high | e14 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | at | at | spatial_location, visual_relation | medium | e15 | False | False |  |  |
| cr2 | m8 | m12 | ent_m8 | ent_m12 | into | into | visual_relation | medium | e16 | False | False |  |  |
| cr3 | m13 | m14 | ent_m13 | ent_m14 | in | in | spatial_containment, visual_relation | high | e17 | False | False |  |  |
| cr4 | m13 | m8 | ent_m13 | ent_m8 | beside; repaired_self_edge_target from them->woman | next_to | spatial_proximity, visual_relation | medium | e18 | False | False |  |  |
| cr5 | m16 | m19 | ent_m16 | ent_m19 | at_top_of | at_top_of | spatial_region, visual_relation | high | e19 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | lab_coat |  |  |  | entity_exists:lab_coat | True | low |
| cf2 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf3 | entity_exists | flask |  |  |  | entity_exists:flask | True | low |
| cf4 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf5 | entity_exists | goggle |  |  |  | entity_exists:goggle | True | low |
| cf6 | entity_exists | liquid |  |  |  | entity_exists:liquid | True | low |
| cf7 | entity_exists | flask |  |  |  | entity_exists:flask | True | low |
| cf8 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf9 | entity_exists | hijab |  |  |  | entity_exists:hijab | True | low |
| cf10 | entity_exists | logo |  |  |  | entity_exists:logo | True | low |
| cf11 | entity_exists | text |  |  | text_content | entity_exists:text | True | high |
| cf12 | entity_exists | bottom |  |  |  | entity_exists:bottom | True | low |
| cf13 | entity_exists | image |  |  |  | entity_exists:image | True | low |
| cf14 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf15 | has_quantity | people | four |  | exact_quantity, quantity | has_quantity:people:four | True | high |
| cf16 | has_attribute | lab_coat | white |  | color_attribute, color, visual_attribute | has_attribute:lab_coat:white | True | high |
| cf17 | has_attribute | flask | glass |  | material_attribute, material, visual_attribute | has_attribute:flask:glass | True | high |
| cf18 | has_quantity | man | three |  | exact_quantity, quantity | has_quantity:man:three | True | high |
| cf19 | has_attribute | hijab | patterned |  | pattern_attribute, pattern, visual_attribute | has_attribute:hijab:patterned | True | medium |
| cf20 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf21 | event_role | stand | agent | people |  | event_role:stand:agent:people | True | medium |
| cf22 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf23 | event_role | hold | agent | people |  | event_role:hold:agent:people | True | medium |
| cf24 | event_role | hold | patient | flask |  | event_role:hold:patient:flask | True | medium |
| cf25 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf26 | event_role | wear | agent | man |  | event_role:wear:agent:man | True | medium |
| cf27 | event_role | wear | patient | goggle |  | event_role:wear:patient:goggle | True | medium |
| cf28 | action_event | pour |  |  | visual_action | action_event:pour | True | low |
| cf29 | event_role | pour | agent | man |  | event_role:pour:agent:man | True | medium |
| cf30 | event_role | pour | patient | liquid |  | event_role:pour:patient:liquid | True | medium |
| cf31 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf32 | event_role | stand | agent | woman |  | event_role:stand:agent:woman | True | medium |
| cf33 | relation | people | in | lab_coat | spatial_containment, visual_relation | relation:people:in:lab_coat | True | high |
| cf34 | relation | people | at | table | spatial_location, visual_relation | relation:people:at:table | True | medium |
| cf35 | relation | man | into | flask | visual_relation | relation:man:into:flask | True | medium |
| cf36 | relation | woman | in | hijab | spatial_containment, visual_relation | relation:woman:in:hijab | True | high |
| cf37 | relation | woman | next_to | man | spatial_proximity, visual_relation | relation:woman:next_to:man | True | medium |
| cf38 | relation | logo | at_top_of | image | spatial_region, visual_relation | relation:logo:at_top_of:image | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e18 |  |  |  | {"canonical": "next_to", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e18", "raw_relation": "beside; repaired_self_edge_target from them->woman", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 99

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `5207ae2f4f54cd83ab86dd91b37fd66a2f511a9c2d803f88e8709886baf89c14`
**parse_path:** `sentence`

> A domed ceiling with repeating octagonal patterns and a central skylight lets in bright light.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | ceiling | ceiling | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | domed | domed | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | patterns | pattern | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | repeating | repeat | state_attribute | chunk1 | 4 | medium |
| m4 | attribute | octagonal | octagonal | modifier_attribute | chunk1 | 5 | medium |
| m5 | object | skylight | skylight | noun_chunk_root | chunk2 | 10 | high |
| m6 | attribute | central | central | modifier_attribute | chunk2 | 9 | medium |
| m7 | object | light | light | noun_chunk_root | chunk3 | 14 | high |
| m8 | attribute | bright | bright | visual_attribute | chunk3 | 13 | medium |
| m9 | action | lets | let | verb_predicate | doc | 11 | high |
| m10 | particle | in | in | phrasal_particle | action_particle | 12 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> ceiling |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> patterns |
| e2 | has_attribute | m2 | m4 | medium | chunk1 amod -> patterns |
| e3 | has_attribute | m5 | m6 | medium | chunk2 amod -> skylight |
| e4 | has_attribute | m7 | m8 | medium | chunk3 amod -> light |
| e5 | agent | m9 | m0 | medium | nsubj -> lets |
| e6 | agent | m9 | m5 | medium | nsubj -> lets |
| e7 | has_particle | m9 | m10 | medium | prt -> lets |
| e8 | patient | m9 | m7 | medium | dobj -> lets |
| e9 | relation | m0 | m2 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | ceiling | ceiling | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:ceiling", "parents": []} |
| ent_m2 | object | pattern | patterns | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:pattern", "parents": []} |
| ent_m5 | object | skylight | skylight | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:skylight", "parents": []} |
| ent_m7 | object | light | light | object |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:light", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | lets | let | let | visual_action | in | agent:m0->ent_m0; agent:m5->ent_m5; patient:m7->ent_m7 | {"canonical": "action:let", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | let | agent | m0 | ent_m0 | medium | e5 | nsubj -> lets |  |  |
| ce0 | let | agent | m5 | ent_m5 | medium | e6 | nsubj -> lets |  |  |
| ce0 | let | patient | m7 | ent_m7 | medium | e8 | dobj -> lets |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | association_relation, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | ceiling |  |  |  | entity_exists:ceiling | True | low |
| cf1 | entity_exists | pattern |  |  |  | entity_exists:pattern | True | low |
| cf2 | entity_exists | skylight |  |  |  | entity_exists:skylight | True | low |
| cf3 | entity_exists | light |  |  |  | entity_exists:light | True | low |
| cf4 | has_attribute | ceiling | domed |  | shape_attribute, shape, visual_attribute | has_attribute:ceiling:domed | True | medium |
| cf5 | has_attribute | pattern | repeat |  | state_attribute, visual_attribute | has_attribute:pattern:repeat | True | medium |
| cf6 | has_attribute | pattern | octagonal |  | shape_attribute, shape, visual_attribute | has_attribute:pattern:octagonal | True | medium |
| cf7 | has_attribute | skylight | central |  | modifier_attribute, visual_attribute | has_attribute:skylight:central | True | medium |
| cf8 | has_attribute | light | bright |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:light:bright | True | medium |
| cf9 | action_event | let |  |  | visual_action | action_event:let | True | low |
| cf10 | event_role | let | agent | ceiling |  | event_role:let:agent:ceiling | True | medium |
| cf11 | event_role | let | agent | skylight |  | event_role:let:agent:skylight | True | medium |
| cf12 | event_role | let | patient | light |  | event_role:let:patient:light | True | medium |
| cf13 | relation | ceiling | with | pattern | association_relation, visual_relation | relation:ceiling:with:pattern | True | high |

### Stage 9 Canonicalization Notes
_none_

## 100

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `52c6598a381abe73c3610f5d91093f1c455d382883d1a9f5a94877f489cdc814`
**parse_path:** `sentence`

> An aerial view shows a town with houses, a river, and roads winding through green fields and hills.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | view | view | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | aerial | aerial | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | town | town | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | houses | house | noun_chunk_root | chunk2 | 7 | high |
| m4 | object | river | river | noun_chunk_root | chunk3 | 10 | high |
| m5 | object | roads | road | noun_chunk_root | chunk4 | 13 | high |
| m6 | object | fields | field | noun_chunk_root | chunk5 | 17 | high |
| m7 | attribute | green | green | color_attribute | chunk5 | 16 | high |
| m8 | object | hills | hill | noun_chunk_root | chunk6 | 19 | high |
| m9 | action | shows | show | verb_predicate | doc | 3 | high |
| m10 | action | winding | wind | verb_predicate | doc | 14 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> view |
| e1 | has_attribute | m6 | m7 | high | chunk5 amod -> fields |
| e2 | agent | m9 | m0 | medium | nsubj -> shows |
| e3 | patient | m9 | m2 | medium | dobj -> shows |
| e4 | agent | m10 | m5 | medium | inherited agent acl -> roads |
| e5 | relation | m2 | m3 | high | with |
| e6 | relation | m2 | m4 | high | with |
| e7 | relation | m2 | m5 | high | with |
| e8 | relation | m5 | m6 | medium | through |
| e9 | relation | m5 | m8 | medium | through |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | view | view | object |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:view", "parents": []} |
| ent_m2 | object | town | town | object |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:town", "parents": []} |
| ent_m3 | object | house | houses | object |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:house", "parents": []} |
| ent_m4 | object | river | river | object |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:river", "parents": []} |
| ent_m5 | object | road | roads | object |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:road", "parents": []} |
| ent_m6 | object | field | fields | object |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": []} |
| ent_m8 | object | hill | hills | object |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:hill", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | shows | show | show | visual_action |  | agent:m0->ent_m0; patient:m2->ent_m2 | {"canonical": "action:show", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m10 | winding | wind | wind | visual_action |  | agent:m5->ent_m5 | {"canonical": "action:wind", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | m0 | ent_m0 | medium | e2 | nsubj -> shows |  |  |
| ce0 | show | patient | m2 | ent_m2 | medium | e3 | dobj -> shows |  |  |
| ce1 | wind | agent | m5 | ent_m5 | medium | e4 | inherited agent acl -> roads |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m2 | m3 | ent_m2 | ent_m3 | with | with | association_relation, visual_relation | high | e5 | False | False |  |  |
| cr1 | m2 | m4 | ent_m2 | ent_m4 | with | with | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr2 | m2 | m5 | ent_m2 | ent_m5 | with | with | association_relation, visual_relation | high | e7 | False | False |  |  |
| cr3 | m5 | m6 | ent_m5 | ent_m6 | through | through | spatial_path, visual_relation | medium | e8 | False | False |  |  |
| cr4 | m5 | m8 | ent_m5 | ent_m8 | through | through | spatial_path, visual_relation | medium | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | view |  |  |  | entity_exists:view | True | low |
| cf1 | entity_exists | town |  |  |  | entity_exists:town | True | low |
| cf2 | entity_exists | house |  |  |  | entity_exists:house | True | low |
| cf3 | entity_exists | river |  |  |  | entity_exists:river | True | low |
| cf4 | entity_exists | road |  |  |  | entity_exists:road | True | low |
| cf5 | entity_exists | field |  |  |  | entity_exists:field | True | low |
| cf6 | entity_exists | hill |  |  |  | entity_exists:hill | True | low |
| cf7 | has_attribute | view | aerial |  | modifier_attribute, visual_attribute | has_attribute:view:aerial | True | medium |
| cf8 | has_attribute | field | green |  | color_attribute, color, visual_attribute | has_attribute:field:green | True | high |
| cf9 | action_event | show |  |  | visual_action | action_event:show | True | low |
| cf10 | event_role | show | agent | view |  | event_role:show:agent:view | True | medium |
| cf11 | event_role | show | patient | town |  | event_role:show:patient:town | True | medium |
| cf12 | action_event | wind |  |  | visual_action | action_event:wind | True | low |
| cf13 | event_role | wind | agent | road |  | event_role:wind:agent:road | True | medium |
| cf14 | relation | town | with | house | association_relation, visual_relation | relation:town:with:house | True | high |
| cf15 | relation | town | with | river | association_relation, visual_relation | relation:town:with:river | True | high |
| cf16 | relation | town | with | road | association_relation, visual_relation | relation:town:with:road | True | high |
| cf17 | relation | road | through | field | spatial_path, visual_relation | relation:road:through:field | True | medium |
| cf18 | relation | road | through | hill | spatial_path, visual_relation | relation:road:through:hill | True | medium |

### Stage 9 Canonicalization Notes
_none_
