# Stage 9 Canonical v2 Detail: 1k val00002-00011 first 100

- input: `reports\canonical_concepts_1k_val00002_00011_trf_stage9_canonical_v2.jsonl`
- max_records: `100`
- contents: raw concept mentions/edges + Stage 9 canonical entities/events/relations

## 01

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `00980cb5d333d1441fcd805bed8c588b3e7e0eb0210cfcefb6d80835498e6414`
**parse_path:** `sentence`

> A blue heron stands in tall green grass. Its long neck is raised, and it has a pointed black beak. The background is blurred with soft green and brown tones.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | heron | heron | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | blue | blue | color_attribute | chunk0 | 1 | high |
| m2 | object | grass | grass | noun_chunk_root | chunk1 | 7 | high |
| m3 | attribute | tall | tall | size_attribute | chunk1 | 5 | high |
| m4 | attribute | green | green | color_attribute | chunk1 | 6 | high |
| m5 | object | neck | neck | noun_chunk_root | chunk2 | 11 | high |
| m6 | attribute | long | long | size_attribute | chunk2 | 10 | high |
| m7 | object | beak | beak | noun_chunk_root | chunk4 | 21 | high |
| m8 | attribute | pointed | pointed | modifier_attribute | chunk4 | 19 | medium |
| m9 | attribute | black | black | color_attribute | chunk4 | 20 | high |
| m10 | object | background | background | noun_chunk_root | chunk5 | 24 | high |
| m11 | object | tones | tone | noun_chunk_root | chunk6 | 32 | high |
| m12 | attribute | soft | soft | modifier_attribute | chunk6 | 28 | medium |
| m13 | attribute | green | green | color_attribute | chunk6 | 29 | high |
| m14 | attribute | brown | brown | color_attribute | chunk6 | 31 | high |
| m15 | context | background | background | context_word | doc | 24 | medium |
| m16 | action | stands | stand | verb_predicate | doc | 3 | high |
| m17 | action | raised | raise | verb_predicate | doc | 13 | high |
| m18 | action | has | have | verb_predicate | doc | 17 | high |
| m19 | action | blurred | blur | verb_predicate | doc | 26 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> heron |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> grass |
| e2 | has_attribute | m2 | m4 | high | chunk1 amod -> grass |
| e3 | has_attribute | m5 | m6 | high | chunk2 amod -> neck |
| e4 | has_attribute | m7 | m8 | medium | chunk4 amod -> beak |
| e5 | has_attribute | m7 | m9 | high | chunk4 amod -> beak |
| e6 | has_attribute | m11 | m12 | medium | chunk6 amod -> tones |
| e7 | has_attribute | m11 | m13 | high | chunk6 amod -> tones |
| e8 | has_attribute | m11 | m14 | high | chunk6 conj -> tones |
| e9 | has_context | scene | m15 | medium | context_word token background |
| e10 | agent | m16 | m0 | medium | nsubj -> stands |
| e11 | agent | m17 | m5 | medium | nsubjpass -> raised |
| e12 | agent | m18 | m0 | medium | nsubj -> has; resolved it -> heron |
| e13 | patient | m18 | m7 | medium | dobj -> has |
| e14 | agent | m19 | m15 | medium | nsubjpass -> blurred |
| e15 | relation | m0 | m2 | high | in |
| e16 | relation | m15 | m11 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | heron | heron | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:heron", "parents": []} |
| ent_m2 | object | grass | grass | object | raw_lemma | wordnet_synset:grass.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m2 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m5 | object | neck | neck | object | raw_lemma | stage9_seed:parent_seed | body_part | m5 | raw_mention |  |  |  | True | {"canonical": "entity:neck", "parents": ["entity_parent:body_part"]} |
| ent_m7 | object | beak | beak | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:beak", "parents": []} |
| ent_m10 | object | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m10 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m11 | object | tone | tones | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:tone", "parents": []} |
| ent_m15 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m15 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m17 | raised | raise | raise | raw_action | visual_action_fallback | visual_action |  | patient<-theme[passive_to_active]:m5->ent_m5 | {"canonical": "action:raise", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m18 | has | have | have | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m7->ent_m7 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m19 | blurred | blur | blur | raw_action | visual_action_fallback | visual_action |  | patient<-theme[passive_to_active]:m15->ent_m15 | {"canonical": "action:blur", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e10 | nsubj -> stands |  |  |
| ce1 | raise | patient | theme | passive_to_active | m5 | ent_m5 | medium | e11 | nsubjpass -> raised |  |  |
| ce2 | have | agent | agent | none | m0 | ent_m0 | medium | e12 | nsubj -> has; resolved it -> heron |  |  |
| ce2 | have | patient | patient | none | m7 | ent_m7 | medium | e13 | dobj -> has |  |  |
| ce3 | blur | patient | theme | passive_to_active | m15 | ent_m15 | medium | e14 | nsubjpass -> blurred |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e15 | False | False |  |  |
| cr1 | m15 | m11 | ent_m15 | ent_m11 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | heron |  |  |  | entity_exists:heron | True | low |
| cf1 | entity_exists | grass |  |  | plant, living_thing | entity_exists:grass | True | high |
| cf2 | entity_exists | neck |  |  | body_part | entity_exists:neck | True | high |
| cf3 | entity_exists | beak |  |  |  | entity_exists:beak | True | low |
| cf4 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf5 | entity_exists | tone |  |  |  | entity_exists:tone | True | low |
| cf6 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf7 | has_attribute | heron | blue |  | color_attribute, color, visual_attribute | has_attribute:heron:blue | True | high |
| cf8 | has_attribute | grass | tall |  | size_attribute, height, visual_attribute | has_attribute:grass:tall | True | high |
| cf9 | has_attribute | grass | green |  | color_attribute, color, visual_attribute | has_attribute:grass:green | True | high |
| cf10 | has_attribute | neck | long |  | size_attribute, clean_exact_overlap, length, visual_attribute | has_attribute:neck:long | True | high |
| cf11 | has_attribute | beak | pointed |  | modifier_attribute, visual_attribute | has_attribute:beak:pointed | True | medium |
| cf12 | has_attribute | beak | black |  | color_attribute, color, visual_attribute | has_attribute:beak:black | True | high |
| cf13 | has_attribute | tone | soft |  | texture_attribute, clean_exact_overlap, hardness, texture, visual_attribute | has_attribute:tone:soft | True | medium |
| cf14 | has_attribute | tone | green |  | color_attribute, color, visual_attribute | has_attribute:tone:green | True | high |
| cf15 | has_attribute | tone | brown |  | color_attribute, color, visual_attribute | has_attribute:tone:brown | True | high |
| cf16 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf17 | event_role | stand | agent | heron |  | event_role:stand:agent:heron | True | medium |
| cf18 | action_event | raise |  |  | visual_action | action_event:raise | True | low |
| cf19 | event_role | raise | patient | neck |  | event_role:raise:patient:neck | True | medium |
| cf20 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf21 | event_role | have | agent | heron |  | event_role:have:agent:heron | True | medium |
| cf22 | event_role | have | patient | beak |  | event_role:have:patient:beak | True | medium |
| cf23 | action_event | blur |  |  | visual_action | action_event:blur | True | low |
| cf24 | event_role | blur | patient | background |  | event_role:blur:patient:background | True | medium |
| cf25 | relation | heron | in | grass | spatial_containment, visual_relation | relation:heron:in:grass | True | high |
| cf26 | relation | background | with | tone | association_relation, visual_relation | relation:background:with:tone | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m17 | e11 | m5 |  |  | {"action_mention_id": "m17", "kind": "passive_subject_to_patient", "raw_edge_id": "e11", "raw_role": "theme", "role": "patient", "target": "m5", "voice_normalization": "passive_to_active"} |
| passive_subject_to_patient | m19 | e14 | m15 |  |  | {"action_mention_id": "m19", "kind": "passive_subject_to_patient", "raw_edge_id": "e14", "raw_role": "theme", "role": "patient", "target": "m15", "voice_normalization": "passive_to_active"} |

## 02

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `0119e2be990c3beeff249e51586bed4d924cc4eac39be649f74871e5b655dc14`
**parse_path:** `tag_list`

> hockey players, goalie, ice rink, crowd, red jersey

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hockey players | hockey_player | segment_head | t0 | 0 | high |
| m1 | object | goalie | goalie | segment_head | t1 | 0 | high |
| m2 | object | ice rink | ice_rink | segment_head | t2 | 0 | high |
| m3 | object | crowd | crowd | segment_head | t3 | 0 | high |
| m4 | object | jersey | jersey | segment_head | t4 | 1 | high |
| m5 | attribute | red | red | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m4 | m5 | high | t4 internal compound -> jersey |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hockey_player | hockey players | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:hockey_player", "parents": []} |
| ent_m1 | object | goalie | goalie | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:goalie", "parents": []} |
| ent_m2 | object | ice_rink | ice rink | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:ice_rink", "parents": []} |
| ent_m3 | object | crowd | crowd | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:crowd", "parents": []} |
| ent_m4 | object | jersey | jersey | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:jersey", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |

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
| cf0 | entity_exists | hockey_player |  |  |  | entity_exists:hockey_player | True | high |
| cf1 | entity_exists | goalie |  |  |  | entity_exists:goalie | True | low |
| cf2 | entity_exists | ice_rink |  |  |  | entity_exists:ice_rink | True | high |
| cf3 | entity_exists | crowd |  |  |  | entity_exists:crowd | True | low |
| cf4 | entity_exists | jersey |  |  | clothing, wearable | entity_exists:jersey | True | high |
| cf5 | has_attribute | jersey | red |  | color_attribute, color, visual_attribute | has_attribute:jersey:red | True | high |

### Stage 9 Canonicalization Notes
_none_

## 03

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `01f14c038b3924de7503bb34718fecd8b0f02669fb9bdc31e34f4ef861777814`
**parse_path:** `sentence`

> A tall stone monument stands on a gravel path near a body of water. Japanese characters are carved vertically on its surface, with grass and reeds growing nearby. The sky shows soft sunset hues over the calm water in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | monument | monument | noun_chunk_root | chunk0 | 3 | high |
| m1 | attribute | tall | tall | size_attribute | chunk0 | 1 | high |
| m2 | attribute | stone | stone | material_attribute | chunk0 | 2 | high |
| m3 | object | path | path | noun_chunk_root | chunk1 | 8 | high |
| m4 | attribute | gravel | gravel | compound_modifier | chunk1 | 7 | medium |
| m5 | object | body | body | noun_chunk_root | chunk2 | 11 | high |
| m6 | object | water | water | noun_chunk_root | chunk3 | 13 | high |
| m7 | object | characters | character | noun_chunk_root | chunk4 | 16 | high |
| m8 | attribute | Japanese | japanese | modifier_attribute | chunk4 | 15 | medium |
| m9 | context | surface | surface | spatial_region | chunk5 | 22 | medium |
| m10 | object | grass | grass | noun_chunk_root | chunk6 | 25 | high |
| m11 | object | reeds | reed | noun_chunk_root | chunk7 | 27 | high |
| m12 | object | sky | sky | noun_chunk_root | chunk8 | 32 | high |
| m13 | object | hues | hue | noun_chunk_root | chunk9 | 36 | high |
| m14 | attribute | soft | soft | modifier_attribute | chunk9 | 34 | medium |
| m15 | attribute | sunset | sunset | compound_modifier | chunk9 | 35 | medium |
| m16 | object | water | water | noun_chunk_root | chunk10 | 40 | high |
| m17 | attribute | calm | calm | modifier_attribute | chunk10 | 39 | medium |
| m18 | context | background | background | scene_context | chunk11 | 43 | high |
| m19 | action | stands | stand | verb_predicate | doc | 4 | high |
| m20 | action | carved | carve | verb_predicate | doc | 18 | high |
| m21 | action | growing | grow | verb_predicate | doc | 28 | high |
| m22 | action | shows | show | verb_predicate | doc | 33 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> monument |
| e1 | has_attribute | m0 | m2 | high | chunk0 compound -> monument |
| e2 | has_attribute | m3 | m4 | medium | chunk1 compound -> path |
| e3 | has_attribute | m7 | m8 | medium | chunk4 amod -> characters |
| e4 | has_attribute | m13 | m14 | medium | chunk9 amod -> hues |
| e5 | has_attribute | m13 | m15 | medium | chunk9 compound -> hues |
| e6 | has_attribute | m16 | m17 | medium | chunk10 amod -> water |
| e7 | has_context | scene | m18 | high | scene_context token background |
| e8 | agent | m19 | m0 | medium | nsubj -> stands |
| e9 | agent | m20 | m7 | medium | nsubjpass -> carved |
| e10 | agent | m21 | m10 | medium | nsubj -> growing |
| e11 | agent | m21 | m11 | medium | nsubj -> growing |
| e12 | agent | m22 | m12 | medium | nsubj -> shows |
| e13 | patient | m22 | m13 | medium | dobj -> shows |
| e14 | relation | m0 | m3 | high | on |
| e15 | relation | m0 | m5 | high | near |
| e16 | relation | m5 | m6 | medium | of |
| e17 | relation | m7 | m9 | high | on |
| e18 | relation | m13 | m16 | high | over |
| e19 | relation | m16 | m18 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | monument | monument | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:monument", "parents": []} |
| ent_m3 | object | path | path | object | raw_lemma | wordnet_synset:path.n.04 + stage9_audit | path, place | m3 | raw_mention |  |  |  | True | {"canonical": "entity:path", "parents": ["entity_parent:path", "entity_parent:place"]} |
| ent_m5 | object | body | body | object | raw_lemma | stage9_seed:parent_seed | body_part | m5 | raw_mention |  |  |  | True | {"canonical": "entity:body", "parents": ["entity_parent:body_part"]} |
| ent_m6 | object | water | water | object | raw_lemma | wordnet_synset:water.n.01 + stage9_audit | natural_element | m6 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": ["entity_parent:natural_element"]} |
| ent_m7 | object | character | characters | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:character", "parents": []} |
| ent_m9 | context | surface | surface | object | raw_lemma | semantic_type_fallback | scene_context | m9 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": ["entity_parent:scene_context"]} |
| ent_m10 | object | grass | grass | object | raw_lemma | wordnet_synset:grass.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m10 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m11 | object | reed | reeds | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:reed", "parents": []} |
| ent_m12 | object | sky | sky | object | raw_lemma | wordnet_synset:sky.n.01 + stage9_audit | natural_scene | m12 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": ["entity_parent:natural_scene"]} |
| ent_m13 | object | hue | hues | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:hue", "parents": []} |
| ent_m16 | object | water | water | object | raw_lemma | wordnet_synset:water.n.01 + stage9_audit | natural_element | m16 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": ["entity_parent:natural_element"]} |
| ent_m18 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m18 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m19 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m20 | carved | carve | carve | raw_action | visual_action_fallback | visual_action |  | patient<-theme[passive_to_active]:m7->ent_m7 | {"canonical": "action:carve", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m21 | growing | grow | grow | raw_action | visual_action_fallback | visual_action |  | agent:m10->ent_m10; agent:m11->ent_m11 | {"canonical": "action:grow", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m22 | shows | show | show | raw_action | wordnet_synset:show.v.01 + stage9_audit | visual_presentation_action, visual_action |  | agent:m12->ent_m12; patient:m13->ent_m13 | {"canonical": "action:show", "parents": ["action_parent:visual_presentation_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e8 | nsubj -> stands |  |  |
| ce1 | carve | patient | theme | passive_to_active | m7 | ent_m7 | medium | e9 | nsubjpass -> carved |  |  |
| ce2 | grow | agent | agent | none | m10 | ent_m10 | medium | e10 | nsubj -> growing |  |  |
| ce2 | grow | agent | agent | none | m11 | ent_m11 | medium | e11 | nsubj -> growing |  |  |
| ce3 | show | agent | agent | none | m12 | ent_m12 | medium | e12 | nsubj -> shows |  |  |
| ce3 | show | patient | patient | none | m13 | ent_m13 | medium | e13 | dobj -> shows |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e14 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e15 | False | False |  |  |
| cr2 | m5 | m6 | ent_m5 | ent_m6 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e16 | False | False |  |  |
| cr3 | m7 | m9 | ent_m7 | ent_m9 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e17 | False | False |  |  |
| cr4 | m13 | m16 | ent_m13 | ent_m16 | over | above | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e18 | False | False |  |  |
| cr5 | m16 | m18 | ent_m16 | ent_m18 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e19 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | monument |  |  |  | entity_exists:monument | True | low |
| cf1 | entity_exists | path |  |  | path, place | entity_exists:path | True | high |
| cf2 | entity_exists | body |  |  | body_part | entity_exists:body | True | high |
| cf3 | entity_exists | water |  |  | natural_element | entity_exists:water | True | high |
| cf4 | entity_exists | character |  |  |  | entity_exists:character | True | low |
| cf5 | entity_exists | surface |  |  | scene_context | entity_exists:surface | True | medium |
| cf6 | entity_exists | grass |  |  | plant, living_thing | entity_exists:grass | True | high |
| cf7 | entity_exists | reed |  |  |  | entity_exists:reed | True | low |
| cf8 | entity_exists | sky |  |  | natural_scene | entity_exists:sky | True | high |
| cf9 | entity_exists | hue |  |  |  | entity_exists:hue | True | low |
| cf10 | entity_exists | water |  |  | natural_element | entity_exists:water | True | high |
| cf11 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf12 | has_attribute | monument | tall |  | size_attribute, height, visual_attribute | has_attribute:monument:tall | True | high |
| cf13 | has_attribute | monument | stone |  | material_attribute, material, visual_attribute | has_attribute:monument:stone | True | high |
| cf14 | has_attribute | path | gravel |  | material_attribute, material, visual_attribute | has_attribute:path:gravel | True | medium |
| cf15 | has_attribute | character | japanese |  | modifier_attribute, visual_attribute | has_attribute:character:japanese | True | medium |
| cf16 | has_attribute | hue | soft |  | texture_attribute, clean_exact_overlap, hardness, texture, visual_attribute | has_attribute:hue:soft | True | medium |
| cf17 | has_attribute | hue | sunset |  | compound_modifier, visual_attribute | has_attribute:hue:sunset | True | medium |
| cf18 | has_attribute | water | calm |  | modifier_attribute, visual_attribute | has_attribute:water:calm | True | medium |
| cf19 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf20 | event_role | stand | agent | monument |  | event_role:stand:agent:monument | True | medium |
| cf21 | action_event | carve |  |  | visual_action | action_event:carve | True | low |
| cf22 | event_role | carve | patient | character |  | event_role:carve:patient:character | True | medium |
| cf23 | action_event | grow |  |  | visual_action | action_event:grow | True | low |
| cf24 | event_role | grow | agent | grass |  | event_role:grow:agent:grass | True | medium |
| cf25 | event_role | grow | agent | reed |  | event_role:grow:agent:reed | True | medium |
| cf26 | action_event | show |  |  | visual_presentation_action, visual_action | action_event:show | True | high |
| cf27 | event_role | show | agent | sky |  | event_role:show:agent:sky | True | medium |
| cf28 | event_role | show | patient | hue |  | event_role:show:patient:hue | True | medium |
| cf29 | relation | monument | on | path | spatial_support, visual_relation | relation:monument:on:path | True | high |
| cf30 | relation | monument | near | body | spatial_proximity, visual_relation | relation:monument:near:body | True | high |
| cf31 | relation | body | of | water | part_relation, visual_relation | relation:body:of:water | True | medium |
| cf32 | relation | character | on | surface | spatial_support, visual_relation | relation:character:on:surface | True | high |
| cf33 | relation | hue | above | water | spatial_vertical, visual_relation | relation:hue:above:water | True | high |
| cf34 | relation | water | in | background | spatial_containment, visual_relation | relation:water:in:background | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m20 | e9 | m7 |  |  | {"action_mention_id": "m20", "kind": "passive_subject_to_patient", "raw_edge_id": "e9", "raw_role": "theme", "role": "patient", "target": "m7", "voice_normalization": "passive_to_active"} |
| relation_lexical_canonicalized |  | e18 |  |  |  | {"canonical": "above", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e18", "raw_relation": "over", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 04

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `02a7b2e837c3cac93cf60e7cc81add7ca643e3424cd072f1e96e59727cd54c14`
**parse_path:** `sentence`

> People sit on wide stone steps in front of a large, historic church with a clock tower. A cyclist rides past on the sidewalk to the right, while others stand or walk nearby under a partly cloudy sky.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | People | people | noun_chunk_root | chunk0 | 0 | high |
| m1 | object | steps | step | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | wide | wide | size_attribute | chunk1 | 3 | high |
| m3 | attribute | stone | stone | material_attribute | chunk1 | 4 | high |
| m4 | object | church | church | noun_chunk_root | chunk3 | 13 | high |
| m5 | attribute | large | large | size_attribute | chunk3 | 10 | high |
| m6 | attribute | historic | historic | modifier_attribute | chunk3 | 12 | medium |
| m7 | object | clock tower | clock_tower | noun_chunk_root | chunk4 | 16 | high |
| m8 | object | cyclist | cyclist | noun_chunk_root | chunk5 | 19 | high |
| m9 | object | sidewalk | sidewalk | noun_chunk_root | chunk6 | 24 | high |
| m10 | context | right | right | spatial_region | chunk7 | 27 | medium |
| m11 | object | sky | sky | noun_chunk_root | chunk9 | 39 | high |
| m12 | attribute | partly | partly | modifier_attribute | chunk9 | 37 | medium |
| m13 | attribute | cloudy | cloudy | modifier_attribute | chunk9 | 38 | medium |
| m14 | reference | others | other | contrastive_reference | nominal_reference | 30 | high |
| m15 | action | sit | sit | verb_predicate | doc | 1 | high |
| m16 | action | rides | rid | verb_predicate | doc | 20 | high |
| m17 | action | stand | stand | verb_predicate | doc | 31 | high |
| m18 | action | walk | walk | verb_predicate | doc | 33 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> steps |
| e1 | has_attribute | m1 | m3 | high | chunk1 compound -> steps |
| e2 | has_attribute | m4 | m5 | high | chunk3 amod -> church |
| e3 | has_attribute | m4 | m6 | medium | chunk3 amod -> church |
| e4 | has_attribute | m11 | m12 | medium | chunk9 advmod -> sky |
| e5 | has_attribute | m11 | m13 | medium | chunk9 amod -> sky |
| e6 | refers_to | m14 | m0 | high | contrastive_reference others -> People; score=100 |
| e7 | agent | m15 | m0 | medium | nsubj -> sit |
| e8 | agent | m16 | m8 | medium | nsubj -> rides |
| e9 | agent | m17 | m0 | medium | nsubj -> stand; resolved others -> People |
| e10 | agent | m18 | m0 | medium | inherited agent conj -> stand |
| e11 | relation | m0 | m1 | high | on |
| e12 | relation | m0 | m4 | high | in_front_of |
| e13 | relation | m4 | m7 | high | with |
| e14 | relation | m8 | m9 | high | on |
| e15 | relation | m8 | m10 | medium | to |
| e16 | relation | m0 | m11 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | People | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | step | steps | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:step", "parents": []} |
| ent_m4 | object | church | church | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:church", "parents": []} |
| ent_m7 | object | clock_tower | clock tower | object | lvis_object\|visual_genome_object_synset\|wordnet_noun_mwe | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:clock_tower", "parents": []} |
| ent_m8 | object | cyclist | cyclist | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:cyclist", "parents": []} |
| ent_m9 | object | sidewalk | sidewalk | object | raw_lemma | wordnet_synset:sidewalk.n.01 + stage9_audit | path, place | m9 | raw_mention |  |  |  | True | {"canonical": "entity:sidewalk", "parents": ["entity_parent:path", "entity_parent:place"]} |
| ent_m10 | context | right | right | object | raw_lemma | semantic_type_fallback | scene_context | m10 | raw_mention |  |  |  | True | {"canonical": "entity:right", "parents": ["entity_parent:scene_context"]} |
| ent_m11 | object | sky | sky | object | raw_lemma | wordnet_synset:sky.n.01 + stage9_audit | natural_scene | m11 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": ["entity_parent:natural_scene"]} |
| eref_m14 | complement_subset | people | others | person | raw_lemma | stage9_seed:parent_seed | person, human | m14 | stage9_reference | ent_m0 |  | many | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m14 | eref_m14 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | sit | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m16 | rides | rid | rid | raw_action | visual_action_fallback | visual_action |  | agent:m8->ent_m8 | {"canonical": "action:rid", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m17 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->eref_m14 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce3 | m18 | walk | walk | walk | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->eref_m14 | {"canonical": "action:walk", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | agent | none | m0 | ent_m0 | medium | e7 | nsubj -> sit |  |  |
| ce1 | rid | agent | agent | none | m8 | ent_m8 | medium | e8 | nsubj -> rides |  |  |
| ce2 | stand | agent | agent | none | m0 | eref_m14 | medium | e9 | nsubj -> stand; resolved others -> People |  |  |
| ce3 | walk | agent | agent | none | m0 | eref_m14 | medium | e10 | inherited agent conj -> stand |  | conj_agent_inherited_from_reference_canonical_target |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e11 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | in_front_of | in_front_of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e12 | False | False |  |  |
| cr2 | m4 | m7 | ent_m4 | ent_m7 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr3 | m8 | m9 | ent_m8 | ent_m9 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e14 | False | False |  |  |
| cr4 | m8 | m10 | ent_m8 | ent_m10 | to | to | raw_relation | raw_relation | visual_relation | medium | e15 | False | False |  |  |
| cr5 | m0 | m11 | ent_m0 | ent_m11 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | step |  |  |  | entity_exists:step | True | low |
| cf2 | entity_exists | church |  |  |  | entity_exists:church | True | low |
| cf3 | entity_exists | clock_tower |  |  |  | entity_exists:clock_tower | True | high |
| cf4 | entity_exists | cyclist |  |  |  | entity_exists:cyclist | True | low |
| cf5 | entity_exists | sidewalk |  |  | path, place | entity_exists:sidewalk | True | high |
| cf6 | entity_exists | right |  |  | scene_context | entity_exists:right | True | medium |
| cf7 | entity_exists | sky |  |  | natural_scene | entity_exists:sky | True | high |
| cf8 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf9 | has_attribute | step | wide |  | size_attribute, width, visual_attribute | has_attribute:step:wide | True | high |
| cf10 | has_attribute | step | stone |  | material_attribute, material, visual_attribute | has_attribute:step:stone | True | high |
| cf11 | has_attribute | church | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:church:large | True | high |
| cf12 | has_attribute | church | historic |  | modifier_attribute, visual_attribute | has_attribute:church:historic | True | medium |
| cf13 | has_attribute | sky | partly |  | modifier_attribute, visual_attribute | has_attribute:sky:partly | True | medium |
| cf14 | has_attribute | sky | cloudy |  | weather_attribute, weather, visual_attribute | has_attribute:sky:cloudy | True | medium |
| cf15 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf16 | event_role | sit | agent | people |  | event_role:sit:agent:people | True | medium |
| cf17 | action_event | rid |  |  | visual_action | action_event:rid | True | low |
| cf18 | event_role | rid | agent | cyclist |  | event_role:rid:agent:cyclist | True | medium |
| cf19 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf20 | event_role | stand | agent | people |  | event_role:stand:agent:people | True | medium |
| cf21 | action_event | walk |  |  | locomotion_action, visual_action | action_event:walk | True | high |
| cf22 | event_role | walk | agent | people |  | event_role:walk:agent:people | True | medium |
| cf23 | relation | people | on | step | spatial_support, visual_relation | relation:people:on:step | True | high |
| cf24 | relation | people | in_front_of | church | spatial_depth, visual_relation | relation:people:in_front_of:church | True | high |
| cf25 | relation | church | with | clock_tower | association_relation, visual_relation | relation:church:with:clock_tower | True | high |
| cf26 | relation | cyclist | on | sidewalk | spatial_support, visual_relation | relation:cyclist:on:sidewalk | True | high |
| cf27 | relation | cyclist | to | right | visual_relation | relation:cyclist:to:right | True | medium |
| cf28 | relation | people | under | sky | spatial_vertical, visual_relation | relation:people:under:sky | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| conj_agent_reference_target_inherited | m18 |  |  | eref_m14 |  | {"action_mention_id": "m18", "canonical_target": "eref_m14", "kind": "conj_agent_reference_target_inherited", "source_action_mention_id": "m17"} |

## 05

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `04f16e480e0b0f5944612561a52042cb74d80b7ea1df060e12bdf6da98052c14`
**parse_path:** `tag_list`

> wooden box, concrete floor, tripod, shadow

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | box | box | segment_head | t0 | 1 | high |
| m1 | attribute | wooden | wooden | attribute | t0 | 0 | high |
| m2 | object | floor | floor | segment_head | t1 | 1 | high |
| m3 | attribute | concrete | concrete | attribute | t1 | 0 | high |
| m4 | object | tripod | tripod | segment_head | t2 | 0 | high |
| m5 | object | shadow | shadow | segment_head | t3 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> box |
| e1 | has_attribute | m2 | m3 | high | t1 internal compound -> floor |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | box | box | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:box", "parents": []} |
| ent_m2 | object | floor | floor | object | raw_lemma | wordnet_synset:floor.n.01 + stage9_audit | architectural_part, surface, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:floor", "parents": ["entity_parent:architectural_part", "entity_parent:surface", "entity_parent:artifact"]} |
| ent_m4 | object | tripod | tripod | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:tripod", "parents": []} |
| ent_m5 | object | shadow | shadow | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:shadow", "parents": []} |

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
| cf0 | entity_exists | box |  |  |  | entity_exists:box | True | low |
| cf1 | entity_exists | floor |  |  | architectural_part, surface, artifact | entity_exists:floor | True | high |
| cf2 | entity_exists | tripod |  |  |  | entity_exists:tripod | True | low |
| cf3 | entity_exists | shadow |  |  |  | entity_exists:shadow | True | low |
| cf4 | has_attribute | box | wood |  | material_attribute, material, visual_attribute | has_attribute:box:wood | True | high |
| cf5 | has_attribute | floor | concrete |  | material_attribute, material, visual_attribute | has_attribute:floor:concrete | True | high |

### Stage 9 Canonicalization Notes
_none_

## 06

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `0505a3df96a9837be782abf822c765dd5956aaefa9e26796be1ca97ff81c2014`
**parse_path:** `sentence`

> Two judokas compete on a yellow mat, one in blue and the other in white, during a match.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | judokas | judoka | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Two | two | exact_quantity | chunk0 | 0 | high |
| m2 | object | mat | mat | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | yellow | yellow | color_attribute | chunk1 | 5 | high |
| m4 | attribute | white | white | color_attribute | chunk2 | 15 | high |
| m5 | object | match | match | noun_chunk_root | chunk3 | 19 | high |
| m6 | reference | other | other | contrastive_reference | nominal_reference | 13 | high |
| m7 | action | compete | compete | verb_predicate | doc | 2 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> judokas |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> mat |
| e2 | refers_to | m6 | m0 | high | contrastive_reference other -> judokas; score=102 |
| e3 | agent | m7 | m0 | medium | nsubj -> compete |
| e4 | relation | m0 | m2 | high | on |
| e5 | relation | m0 | m5 | medium | during |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | judoka | judokas | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:judoka", "parents": []} |
| ent_m2 | object | mat | mat | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:mat", "parents": []} |
| ent_m5 | object | match | match | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:match", "parents": []} |
| eref_m6 | contrastive_instance | judoka | other | object | raw_lemma | none |  | m6 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:judoka", "parents": []} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m6 | eref_m6 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | compete | compete | compete | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:compete", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | compete | agent | agent | none | m0 | ent_m0 | medium | e3 | nsubj -> compete |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e4 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | during | during | raw_relation | raw_relation | visual_relation | medium | e5 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | judoka |  |  |  | entity_exists:judoka | True | low |
| cf1 | entity_exists | mat |  |  |  | entity_exists:mat | True | low |
| cf2 | entity_exists | match |  |  |  | entity_exists:match | True | low |
| cf3 | entity_exists | judoka |  |  |  | entity_exists:judoka | True | low |
| cf4 | has_quantity | judoka | two |  | exact_quantity, quantity | has_quantity:judoka:two | True | high |
| cf5 | has_attribute | mat | yellow |  | color_attribute, color, visual_attribute | has_attribute:mat:yellow | True | high |
| cf6 | action_event | compete |  |  | visual_action | action_event:compete | True | low |
| cf7 | event_role | compete | agent | judoka |  | event_role:compete:agent:judoka | True | medium |
| cf8 | relation | judoka | on | mat | spatial_support, visual_relation | relation:judoka:on:mat | True | high |
| cf9 | relation | judoka | during | match | visual_relation | relation:judoka:during:match | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 07

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `07f982a0b585cc271afa3cc955ece485e81aa426cac0b13431d1964753043c14`
**parse_path:** `sentence`

> Several people clap and smile around a table with food and drinks. One person in a red sweater stands and claps while others sit nearby.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Several | several | approximate_quantity | chunk0 | 0 | medium |
| m2 | object | table | table | noun_chunk_root | chunk1 | 7 | high |
| m3 | object | food | food | noun_chunk_root | chunk2 | 9 | high |
| m4 | object | drinks | drink | noun_chunk_root | chunk3 | 11 | high |
| m5 | object | person | person | noun_chunk_root | chunk4 | 14 | high |
| m6 | quantity | One | one | exact_quantity | chunk4 | 13 | high |
| m7 | object | sweater | sweater | noun_chunk_root | chunk5 | 18 | high |
| m8 | attribute | red | red | color_attribute | chunk5 | 17 | high |
| m9 | reference | others | other | contrastive_reference | nominal_reference | 23 | high |
| m10 | action | clap | clap | verb_predicate | doc | 2 | high |
| m11 | action | smile | smile | verb_predicate | doc | 4 | high |
| m12 | action | stands | stand | verb_predicate | doc | 19 | high |
| m13 | action | claps | clap | verb_predicate | doc | 21 | high |
| m14 | action | sit | sit | verb_predicate | doc | 24 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | medium | chunk0 quantity -> people |
| e1 | has_quantity | m5 | m6 | high | chunk4 quantity -> person |
| e2 | has_attribute | m7 | m8 | high | chunk5 amod -> sweater |
| e3 | refers_to | m9 | m0 | high | contrastive_reference others -> people; score=110 |
| e4 | agent | m10 | m0 | medium | nsubj -> clap |
| e5 | agent | m11 | m0 | medium | inherited agent conj -> clap |
| e6 | agent | m12 | m5 | medium | nsubj -> stands |
| e7 | agent | m13 | m5 | medium | inherited agent conj -> stands |
| e8 | agent | m14 | m0 | medium | nsubj -> sit; resolved others -> people |
| e9 | relation | m0 | m2 | high | around |
| e10 | relation | m2 | m3 | high | with |
| e11 | relation | m2 | m4 | high | with |
| e12 | relation | m5 | m7 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | table | table | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m3 | object | food | food | object | raw_lemma | wordnet_synset:food.n.01 + stage9_audit | food | m3 | raw_mention |  |  |  | True | {"canonical": "entity:food", "parents": ["entity_parent:food"]} |
| ent_m4 | object | drink | drinks | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:drink", "parents": []} |
| ent_m5 | object | person | person | person | raw_lemma | stage9_seed:parent_seed | person, human | m5 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m7 | object | sweater | sweater | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:sweater", "parents": []} |
| eref_m9 | complement_subset | people | others | person | raw_lemma | stage9_seed:parent_seed | person, human | m9 | stage9_reference | ent_m0 |  | many | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m9 | eref_m9 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | clap | clap | clap | raw_action | stage9_seed:parent_seed | gesture_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:clap", "parents": ["action_parent:gesture_action", "action_parent:visual_action"]} |  |
| ce1 | m11 | smile | smile | smile | raw_action | stage9_seed:parent_seed | expression_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:smile", "parents": ["action_parent:expression_action", "action_parent:visual_action"]} |  |
| ce2 | m12 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m5->ent_m5 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce3 | m13 | claps | clap | clap | raw_action | stage9_seed:parent_seed | gesture_action, visual_action |  | agent:m5->ent_m5 | {"canonical": "action:clap", "parents": ["action_parent:gesture_action", "action_parent:visual_action"]} |  |
| ce4 | m14 | sit | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->eref_m9 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | clap | agent | agent | none | m0 | ent_m0 | medium | e4 | nsubj -> clap |  |  |
| ce1 | smile | agent | agent | none | m0 | ent_m0 | medium | e5 | inherited agent conj -> clap |  |  |
| ce2 | stand | agent | agent | none | m5 | ent_m5 | medium | e6 | nsubj -> stands |  |  |
| ce3 | clap | agent | agent | none | m5 | ent_m5 | medium | e7 | inherited agent conj -> stands |  |  |
| ce4 | sit | agent | agent | none | m0 | eref_m9 | medium | e8 | nsubj -> sit; resolved others -> people |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | around | around | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e9 | False | False |  |  |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e10 | False | False |  |  |
| cr2 | m2 | m4 | ent_m2 | ent_m4 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e11 | False | False |  |  |
| cr3 | m5 | m7 | ent_m5 | ent_m7 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e12 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf2 | entity_exists | food |  |  | food | entity_exists:food | True | high |
| cf3 | entity_exists | drink |  |  |  | entity_exists:drink | True | low |
| cf4 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf5 | entity_exists | sweater |  |  |  | entity_exists:sweater | True | low |
| cf6 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf7 | has_quantity | people | several |  | approximate_quantity, quantity | has_quantity:people:several | True | medium |
| cf8 | has_quantity | person | one |  | exact_quantity, quantity | has_quantity:person:one | True | high |
| cf9 | has_attribute | sweater | red |  | color_attribute, color, visual_attribute | has_attribute:sweater:red | True | high |
| cf10 | action_event | clap |  |  | gesture_action, visual_action | action_event:clap | True | high |
| cf11 | event_role | clap | agent | people |  | event_role:clap:agent:people | True | medium |
| cf12 | action_event | smile |  |  | expression_action, visual_action | action_event:smile | True | high |
| cf13 | event_role | smile | agent | people |  | event_role:smile:agent:people | True | medium |
| cf14 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf15 | event_role | stand | agent | person |  | event_role:stand:agent:person | True | medium |
| cf16 | action_event | clap |  |  | gesture_action, visual_action | action_event:clap | True | high |
| cf17 | event_role | clap | agent | person |  | event_role:clap:agent:person | True | medium |
| cf18 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf19 | event_role | sit | agent | people |  | event_role:sit:agent:people | True | medium |
| cf20 | relation | people | around | table | spatial_proximity, visual_relation | relation:people:around:table | True | high |
| cf21 | relation | table | with | food | association_relation, visual_relation | relation:table:with:food | True | high |
| cf22 | relation | table | with | drink | association_relation, visual_relation | relation:table:with:drink | True | high |
| cf23 | relation | person | in | sweater | spatial_containment, visual_relation | relation:person:in:sweater | True | high |

### Stage 9 Canonicalization Notes
_none_

## 08

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `08812870e84a91c2cad938b10facdccaae11d39d95c2ea3604c032c412d53014`
**parse_path:** `sentence`

> A large airplane with a blue tail sits on the tarmac near airport buildings. Ground vehicles are parked nearby.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | airplane | airplane | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | large | large | size_attribute | chunk0 | 1 | high |
| m2 | object | tail | tail | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | blue | blue | color_attribute | chunk1 | 5 | high |
| m4 | object | tarmac | tarmac | noun_chunk_root | chunk2 | 10 | high |
| m5 | object | buildings | building | noun_chunk_root | chunk3 | 13 | high |
| m6 | attribute | airport | airport | compound_modifier | chunk3 | 12 | medium |
| m7 | object | vehicles | vehicle | noun_chunk_root | chunk4 | 16 | high |
| m8 | attribute | Ground | ground | compound_modifier | chunk4 | 15 | medium |
| m9 | action | sits | sit | verb_predicate | doc | 7 | high |
| m10 | action | parked | park | verb_predicate | doc | 18 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> airplane |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> tail |
| e2 | has_attribute | m5 | m6 | medium | chunk3 compound -> buildings |
| e3 | has_attribute | m7 | m8 | medium | chunk4 compound -> vehicles |
| e4 | agent | m9 | m0 | medium | nsubj -> sits |
| e5 | agent | m10 | m7 | medium | nsubjpass -> parked |
| e6 | relation | m0 | m2 | high | with |
| e7 | relation | m0 | m4 | high | on |
| e8 | relation | m0 | m5 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | airplane | airplane | vehicle | raw_lemma | COCO object label + wordnet_hypernym:vehicle.n.01 + stage9_audit | vehicle | m0 | raw_mention |  |  |  | True | {"canonical": "entity:airplane", "parents": ["entity_parent:vehicle"]} |
| ent_m2 | object | tail | tail | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:tail", "parents": []} |
| ent_m4 | object | tarmac | tarmac | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:tarmac", "parents": []} |
| ent_m5 | object | building | buildings | object | raw_lemma | wordnet_synset:building.n.01 + stage9_audit | structure, artifact | m5 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m7 | object | vehicle | vehicles | vehicle | raw_lemma | stage9_seed:parent_seed | vehicle | m7 | raw_mention |  |  |  | False | {"canonical": "entity:vehicle", "parents": ["entity_parent:vehicle"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| generic_alias | m7 | ent_m7 |  | ent_m0 | medium |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | sits | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m10 | parked | park | park | raw_action | visual_action_fallback | visual_action |  | patient<-theme[passive_to_active]:m7->ent_m0 | {"canonical": "action:park", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | agent | none | m0 | ent_m0 | medium | e4 | nsubj -> sits |  |  |
| ce1 | park | patient | theme | passive_to_active | m7 | ent_m0 | medium | e5 | nsubjpass -> parked |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e7 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | airplane |  |  | vehicle | entity_exists:airplane | True | high |
| cf1 | entity_exists | tail |  |  |  | entity_exists:tail | True | low |
| cf2 | entity_exists | tarmac |  |  |  | entity_exists:tarmac | True | low |
| cf3 | entity_exists | building |  |  | structure, artifact | entity_exists:building | True | high |
| cf4 | has_attribute | airplane | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:airplane:large | True | high |
| cf5 | has_attribute | tail | blue |  | color_attribute, color, visual_attribute | has_attribute:tail:blue | True | high |
| cf6 | has_attribute | building | airport |  | compound_modifier, visual_attribute | has_attribute:building:airport | True | medium |
| cf7 | has_attribute | airplane | ground |  | compound_modifier, visual_attribute | has_attribute:airplane:ground | True | medium |
| cf8 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf9 | event_role | sit | agent | airplane |  | event_role:sit:agent:airplane | True | medium |
| cf10 | action_event | park |  |  | visual_action | action_event:park | True | low |
| cf11 | event_role | park | patient | airplane |  | event_role:park:patient:airplane | True | medium |
| cf12 | relation | airplane | with | tail | association_relation, visual_relation | relation:airplane:with:tail | True | high |
| cf13 | relation | airplane | on | tarmac | spatial_support, visual_relation | relation:airplane:on:tarmac | True | high |
| cf14 | relation | airplane | near | building | spatial_proximity, visual_relation | relation:airplane:near:building | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m10 | e5 | m7 |  |  | {"action_mention_id": "m10", "kind": "passive_subject_to_patient", "raw_edge_id": "e5", "raw_role": "theme", "role": "patient", "target": "m7", "voice_normalization": "passive_to_active"} |

## 09

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `08a998bcf60a92935fe636467dbe0e16049f6fb26141d2784a9f642f5b0c0414`
**parse_path:** `sentence`

> A person in a pink shirt stands next to an orange bicycle on a paved road. Green signs for “Gilltown Stud” and “Gilltown Stud Offices” are mounted on a stone wall beside them, with trees lining the road behind.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “Gilltown Stud” | gilltown_stud | quote_text | doc_quote | 20 | high |
| m1 | attribute | “Gilltown Stud Offices” | gilltown_stud_offices | quote_text | doc_quote | 22 | high |
| m2 | object | person | person | noun_chunk_root | chunk0 | 1 | high |
| m3 | object | shirt | shirt | noun_chunk_root | chunk1 | 5 | high |
| m4 | attribute | pink | pink | color_attribute | chunk1 | 4 | high |
| m5 | object | bicycle | bicycle | noun_chunk_root | chunk2 | 11 | high |
| m6 | attribute | orange | orange | color_attribute | chunk2 | 10 | high |
| m7 | object | road | road | noun_chunk_root | chunk3 | 15 | high |
| m8 | attribute | paved | paved | visual_attribute | chunk3 | 14 | medium |
| m9 | object | signs | sign | noun_chunk_root | chunk4 | 18 | high |
| m10 | attribute | Green | green | color_attribute | chunk4 | 17 | high |
| m11 | object | wall | wall | noun_chunk_root | chunk7 | 28 | high |
| m12 | attribute | stone | stone | material_attribute | chunk7 | 27 | high |
| m13 | object | trees | tree | noun_chunk_root | chunk9 | 33 | high |
| m14 | object | road | road | noun_chunk_root | chunk10 | 36 | high |
| m15 | action | stands | stand | verb_predicate | doc | 6 | high |
| m16 | action | mounted | mount | verb_predicate | doc | 24 | high |
| m17 | action | lining | line | verb_predicate | doc | 34 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m3 | m4 | high | chunk1 amod -> shirt |
| e1 | has_attribute | m5 | m6 | high | chunk2 amod -> bicycle |
| e2 | has_attribute | m7 | m8 | medium | chunk3 amod -> road |
| e3 | has_attribute | m9 | m10 | high | chunk4 amod -> signs |
| e4 | has_attribute | m11 | m12 | high | chunk7 compound -> wall |
| e5 | agent | m15 | m2 | medium | nsubj -> stands |
| e6 | agent | m16 | m9 | medium | nsubjpass -> mounted |
| e7 | agent | m17 | m13 | medium | nsubj -> lining |
| e8 | patient | m17 | m14 | medium | dobj -> lining |
| e9 | relation | m2 | m3 | high | in |
| e10 | relation | m2 | m5 | high | next_to |
| e11 | relation | m2 | m7 | high | on |
| e12 | relation | m9 | m0 | medium | for |
| e13 | relation | m9 | m1 | medium | for |
| e14 | relation | m9 | m11 | high | on |
| e15 | relation | m11 | m2 | high | beside |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m2 | object | person | person | person | raw_lemma | stage9_seed:parent_seed | person, human | m2 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m3 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m3 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m5 | object | bicycle | bicycle | object | raw_lemma | stage9_seed:parent_seed | vehicle | m5 | raw_mention |  |  |  | True | {"canonical": "entity:bicycle", "parents": ["entity_parent:vehicle"]} |
| ent_m7 | object | road | road | object | raw_lemma | wordnet_synset:road.n.01 + stage9_audit | path, place | m7 | raw_mention |  |  |  | True | {"canonical": "entity:road", "parents": ["entity_parent:path", "entity_parent:place"]} |
| ent_m9 | object | sign | signs | document | raw_lemma | stage9_seed:parent_seed | text_carrier, artifact | m9 | raw_mention |  |  |  | True | {"canonical": "entity:sign", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m11 | object | wall | wall | object | raw_lemma | wordnet_synset:wall.n.01 + stage9_audit | architectural_part, structure, artifact | m11 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": ["entity_parent:architectural_part", "entity_parent:structure", "entity_parent:artifact"]} |
| ent_m13 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m13 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m14 | object | road | road | object | raw_lemma | wordnet_synset:road.n.01 + stage9_audit | path, place | m14 | raw_mention |  |  |  | True | {"canonical": "entity:road", "parents": ["entity_parent:path", "entity_parent:place"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m2->ent_m2 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m16 | mounted | mount | mount | raw_action | visual_action_fallback | visual_action |  | patient<-theme[passive_to_active]:m9->ent_m9 | {"canonical": "action:mount", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m17 | lining | line | line | raw_action | visual_action_fallback | visual_action |  | agent:m13->ent_m13; patient:m14->ent_m14 | {"canonical": "action:line", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m2 | ent_m2 | medium | e5 | nsubj -> stands |  |  |
| ce1 | mount | patient | theme | passive_to_active | m9 | ent_m9 | medium | e6 | nsubjpass -> mounted |  |  |
| ce2 | line | agent | agent | none | m13 | ent_m13 | medium | e7 | nsubj -> lining |  |  |
| ce2 | line | patient | patient | none | m14 | ent_m14 | medium | e8 | dobj -> lining |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m2 | m3 | ent_m2 | ent_m3 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e9 | False | False |  |  |
| cr1 | m2 | m5 | ent_m2 | ent_m5 | next_to | next_to | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e10 | False | False |  |  |
| cr2 | m2 | m7 | ent_m2 | ent_m7 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e11 | False | False |  |  |
| cr3 | m9 | m0 | ent_m9 |  | for | for | raw_relation | raw_relation | visual_relation | medium | e12 | False | False |  |  |
| cr4 | m9 | m1 | ent_m9 |  | for | for | raw_relation | raw_relation | visual_relation | medium | e13 | False | False |  |  |
| cr5 | m9 | m11 | ent_m9 | ent_m11 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e14 | False | False |  |  |
| cr6 | m11 | m2 | ent_m11 | ent_m2 | beside | next_to | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e15 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf1 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf2 | entity_exists | bicycle |  |  | vehicle | entity_exists:bicycle | True | high |
| cf3 | entity_exists | road |  |  | path, place | entity_exists:road | True | high |
| cf4 | entity_exists | sign |  |  | text_carrier, artifact | entity_exists:sign | True | high |
| cf5 | entity_exists | wall |  |  | architectural_part, structure, artifact | entity_exists:wall | True | high |
| cf6 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf7 | entity_exists | road |  |  | path, place | entity_exists:road | True | high |
| cf8 | has_attribute | shirt | pink |  | color_attribute, color, visual_attribute | has_attribute:shirt:pink | True | high |
| cf9 | has_attribute | bicycle | orange |  | color_attribute, color, visual_attribute | has_attribute:bicycle:orange | True | high |
| cf10 | has_attribute | road | paved |  | visual_attribute | has_attribute:road:paved | True | medium |
| cf11 | has_attribute | sign | green |  | color_attribute, color, visual_attribute | has_attribute:sign:green | True | high |
| cf12 | has_attribute | wall | stone |  | material_attribute, material, visual_attribute | has_attribute:wall:stone | True | high |
| cf13 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf14 | event_role | stand | agent | person |  | event_role:stand:agent:person | True | medium |
| cf15 | action_event | mount |  |  | visual_action | action_event:mount | True | low |
| cf16 | event_role | mount | patient | sign |  | event_role:mount:patient:sign | True | medium |
| cf17 | action_event | line |  |  | visual_action | action_event:line | True | low |
| cf18 | event_role | line | agent | tree |  | event_role:line:agent:tree | True | medium |
| cf19 | event_role | line | patient | road |  | event_role:line:patient:road | True | medium |
| cf20 | relation | person | in | shirt | spatial_containment, visual_relation | relation:person:in:shirt | True | high |
| cf21 | relation | person | next_to | bicycle | spatial_proximity, visual_relation | relation:person:next_to:bicycle | True | high |
| cf22 | relation | person | on | road | spatial_support, visual_relation | relation:person:on:road | True | high |
| cf23 | relation | sign | for |  | visual_relation | relation:sign:for | False | medium |
| cf24 | relation | sign | for |  | visual_relation | relation:sign:for | False | medium |
| cf25 | relation | sign | on | wall | spatial_support, visual_relation | relation:sign:on:wall | True | high |
| cf26 | relation | wall | next_to | person | spatial_proximity, visual_relation | relation:wall:next_to:person | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m16 | e6 | m9 |  |  | {"action_mention_id": "m16", "kind": "passive_subject_to_patient", "raw_edge_id": "e6", "raw_role": "theme", "role": "patient", "target": "m9", "voice_normalization": "passive_to_active"} |
| relation_lexical_canonicalized |  | e15 |  |  |  | {"canonical": "next_to", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e15", "raw_relation": "beside", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 10

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `08acaf299afd7f0c9dd8eb728beed521a16769598c08740a370b313de4bb7414`
**parse_path:** `sentence`

> A car's side mirror reflects a highway at sunset, showing orange and yellow skies above trees. Orange and white traffic cones line the road, with a distant vehicle’s headlights glowing ahead. The mirror also captures part of the car’s window and interior.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | mirror | mirror | noun_chunk_root | chunk0 | 4 | high |
| m1 | attribute | car | car | modifier_attribute | chunk0 | 1 | medium |
| m2 | attribute | side | side | compound_modifier | chunk0 | 3 | medium |
| m3 | object | highway | highway | noun_chunk_root | chunk1 | 7 | high |
| m4 | context | sunset | sunset | scene_context | chunk2 | 9 | medium |
| m5 | object | skies | sky | noun_chunk_root | chunk3 | 15 | high |
| m6 | attribute | orange | orange | color_attribute | chunk3 | 12 | high |
| m7 | attribute | yellow | yellow | color_attribute | chunk3 | 14 | high |
| m8 | object | trees | tree | noun_chunk_root | chunk4 | 17 | high |
| m9 | object | traffic cones | traffic_cone | noun_chunk_root | chunk5 | 22 | high |
| m10 | object | road | road | noun_chunk_root | chunk6 | 25 | high |
| m11 | object | headlights | headlight | noun_chunk_root | chunk7 | 32 | high |
| m12 | attribute | distant | distant | modifier_attribute | chunk7 | 29 | medium |
| m13 | attribute | vehicle | vehicle | modifier_attribute | chunk7 | 30 | medium |
| m14 | object | mirror | mirror | noun_chunk_root | chunk8 | 37 | high |
| m15 | object | part | part | noun_chunk_root | chunk9 | 40 | high |
| m16 | object | window | window | noun_chunk_root | chunk10 | 45 | high |
| m17 | attribute | car | car | modifier_attribute | chunk10 | 43 | medium |
| m18 | object | interior | interior | noun_chunk_root | chunk11 | 47 | high |
| m19 | action | reflects | reflect | verb_predicate | doc | 5 | high |
| m20 | action | showing | show | verb_predicate | doc | 11 | high |
| m21 | action | line | line | verb_predicate | doc | 23 | high |
| m22 | action | glowing | glow | verb_predicate | doc | 33 | high |
| m23 | action | captures | capture | verb_predicate | doc | 39 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 poss -> mirror |
| e1 | has_attribute | m0 | m2 | medium | chunk0 compound -> mirror |
| e2 | has_context | scene | m4 | medium | scene_context token sunset |
| e3 | has_attribute | m5 | m6 | high | chunk3 amod -> skies |
| e4 | has_attribute | m5 | m7 | high | chunk3 conj -> skies |
| e5 | has_attribute | m11 | m12 | medium | chunk7 amod -> headlights |
| e6 | has_attribute | m11 | m13 | medium | chunk7 poss -> headlights |
| e7 | has_attribute | m16 | m17 | medium | chunk10 poss -> window |
| e8 | agent | m19 | m0 | medium | nsubj -> reflects |
| e9 | patient | m19 | m3 | medium | dobj -> reflects |
| e10 | agent | m20 | m0 | medium | inherited agent advcl -> reflects |
| e11 | patient | m20 | m5 | medium | dobj -> showing |
| e12 | agent | m21 | m9 | medium | nsubj -> line |
| e13 | patient | m21 | m10 | medium | dobj -> line |
| e14 | agent | m22 | m11 | medium | nsubj -> glowing |
| e15 | agent | m23 | m14 | medium | nsubj -> captures |
| e16 | patient | m23 | m15 | medium | dobj -> captures |
| e17 | relation | m0 | m4 | medium | at |
| e18 | relation | m5 | m8 | high | above |
| e19 | relation | m15 | m16 | medium | of |
| e20 | relation | m15 | m18 | medium | of |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | mirror | mirror | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:mirror", "parents": []} |
| ent_m3 | object | highway | highway | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:highway", "parents": []} |
| ent_m4 | context | sunset | sunset | object | raw_lemma | semantic_type_fallback | scene_context | m4 | raw_mention |  |  |  | True | {"canonical": "entity:sunset", "parents": ["entity_parent:scene_context"]} |
| ent_m5 | object | sky | skies | object | raw_lemma | wordnet_synset:sky.n.01 + stage9_audit | natural_scene | m5 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": ["entity_parent:natural_scene"]} |
| ent_m8 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m8 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m9 | object | traffic_cone | traffic cones | object | lvis_object | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:traffic_cone", "parents": []} |
| ent_m10 | object | road | road | object | raw_lemma | wordnet_synset:road.n.01 + stage9_audit | path, place | m10 | raw_mention |  |  |  | True | {"canonical": "entity:road", "parents": ["entity_parent:path", "entity_parent:place"]} |
| ent_m11 | object | headlight | headlights | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:headlight", "parents": []} |
| ent_m14 | object | mirror | mirror | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:mirror", "parents": []} |
| ent_m15 | object | part | part | object | raw_lemma | none |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:part", "parents": []} |
| ent_m16 | object | window | window | object | raw_lemma | wordnet_synset:window.n.01 + stage9_audit | architectural_part, artifact | m16 | raw_mention |  |  |  | True | {"canonical": "entity:window", "parents": ["entity_parent:architectural_part", "entity_parent:artifact"]} |
| ent_m18 | object | interior | interior | object | raw_lemma | none |  | m18 | raw_mention |  |  |  | True | {"canonical": "entity:interior", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m19 | reflects | reflect | reflect | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m3->ent_m3 | {"canonical": "action:reflect", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m20 | showing | show | show | raw_action | wordnet_synset:show.v.01 + stage9_audit | visual_presentation_action, visual_action |  | agent:m0->ent_m0; patient:m5->ent_m5 | {"canonical": "action:show", "parents": ["action_parent:visual_presentation_action", "action_parent:visual_action"]} |  |
| ce2 | m21 | line | line | line | raw_action | visual_action_fallback | visual_action |  | agent:m9->ent_m9; patient:m10->ent_m10 | {"canonical": "action:line", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m22 | glowing | glow | glow | raw_action | visual_action_fallback | visual_action |  | agent:m11->ent_m11 | {"canonical": "action:glow", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m23 | captures | capture | capture | raw_action | visual_action_fallback | visual_action |  | agent:m14->ent_m14; patient:m15->ent_m15 | {"canonical": "action:capture", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | reflect | agent | agent | none | m0 | ent_m0 | medium | e8 | nsubj -> reflects |  |  |
| ce0 | reflect | patient | patient | none | m3 | ent_m3 | medium | e9 | dobj -> reflects |  |  |
| ce1 | show | agent | agent | none | m0 | ent_m0 | medium | e10 | inherited agent advcl -> reflects |  |  |
| ce1 | show | patient | patient | none | m5 | ent_m5 | medium | e11 | dobj -> showing |  |  |
| ce2 | line | agent | agent | none | m9 | ent_m9 | medium | e12 | nsubj -> line |  |  |
| ce2 | line | patient | patient | none | m10 | ent_m10 | medium | e13 | dobj -> line |  |  |
| ce3 | glow | agent | agent | none | m11 | ent_m11 | medium | e14 | nsubj -> glowing |  |  |
| ce4 | capture | agent | agent | none | m14 | ent_m14 | medium | e15 | nsubj -> captures |  |  |
| ce4 | capture | patient | patient | none | m15 | ent_m15 | medium | e16 | dobj -> captures |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e17 | False | False |  |  |
| cr1 | m5 | m8 | ent_m5 | ent_m8 | above | above | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e18 | False | False |  |  |
| cr2 | m15 | m16 | ent_m15 | ent_m16 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e19 | False | False |  |  |
| cr3 | m15 | m18 | ent_m15 | ent_m18 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e20 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | mirror |  |  |  | entity_exists:mirror | True | low |
| cf1 | entity_exists | highway |  |  |  | entity_exists:highway | True | low |
| cf2 | entity_exists | sunset |  |  | scene_context | entity_exists:sunset | True | medium |
| cf3 | entity_exists | sky |  |  | natural_scene | entity_exists:sky | True | high |
| cf4 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf5 | entity_exists | traffic_cone |  |  |  | entity_exists:traffic_cone | True | high |
| cf6 | entity_exists | road |  |  | path, place | entity_exists:road | True | high |
| cf7 | entity_exists | headlight |  |  |  | entity_exists:headlight | True | low |
| cf8 | entity_exists | mirror |  |  |  | entity_exists:mirror | True | low |
| cf9 | entity_exists | part |  |  |  | entity_exists:part | True | low |
| cf10 | entity_exists | window |  |  | architectural_part, artifact | entity_exists:window | True | high |
| cf11 | entity_exists | interior |  |  |  | entity_exists:interior | True | low |
| cf12 | has_attribute | mirror | car |  | modifier_attribute, visual_attribute | has_attribute:mirror:car | True | medium |
| cf13 | has_attribute | mirror | side |  | compound_modifier, visual_attribute | has_attribute:mirror:side | True | medium |
| cf14 | has_attribute | sky | orange |  | color_attribute, color, visual_attribute | has_attribute:sky:orange | True | high |
| cf15 | has_attribute | sky | yellow |  | color_attribute, color, visual_attribute | has_attribute:sky:yellow | True | high |
| cf16 | has_attribute | headlight | distant |  | modifier_attribute, visual_attribute | has_attribute:headlight:distant | True | medium |
| cf17 | has_attribute | headlight | vehicle |  | modifier_attribute, visual_attribute | has_attribute:headlight:vehicle | True | medium |
| cf18 | has_attribute | window | car |  | modifier_attribute, visual_attribute | has_attribute:window:car | True | medium |
| cf19 | action_event | reflect |  |  | visual_action | action_event:reflect | True | low |
| cf20 | event_role | reflect | agent | mirror |  | event_role:reflect:agent:mirror | True | medium |
| cf21 | event_role | reflect | patient | highway |  | event_role:reflect:patient:highway | True | medium |
| cf22 | action_event | show |  |  | visual_presentation_action, visual_action | action_event:show | True | high |
| cf23 | event_role | show | agent | mirror |  | event_role:show:agent:mirror | True | medium |
| cf24 | event_role | show | patient | sky |  | event_role:show:patient:sky | True | medium |
| cf25 | action_event | line |  |  | visual_action | action_event:line | True | low |
| cf26 | event_role | line | agent | traffic_cone |  | event_role:line:agent:traffic_cone | True | medium |
| cf27 | event_role | line | patient | road |  | event_role:line:patient:road | True | medium |
| cf28 | action_event | glow |  |  | visual_action | action_event:glow | True | low |
| cf29 | event_role | glow | agent | headlight |  | event_role:glow:agent:headlight | True | medium |
| cf30 | action_event | capture |  |  | visual_action | action_event:capture | True | low |
| cf31 | event_role | capture | agent | mirror |  | event_role:capture:agent:mirror | True | medium |
| cf32 | event_role | capture | patient | part |  | event_role:capture:patient:part | True | medium |
| cf33 | relation | mirror | at | sunset | spatial_location, visual_relation | relation:mirror:at:sunset | True | medium |
| cf34 | relation | sky | above | tree | spatial_vertical, visual_relation | relation:sky:above:tree | True | high |
| cf35 | relation | part | of | window | part_relation, visual_relation | relation:part:of:window | True | medium |
| cf36 | relation | part | of | interior | part_relation, visual_relation | relation:part:of:interior | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 11

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `09ddd68098c5f17ab93c33bb96e16c0aac7932a1727aef28059668dff60aa414`
**parse_path:** `sentence`

> A yellow building with a clock and pointed roof stands beside a tall striped pole. Several people walk along the sidewalk in front of it.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | yellow | yellow | color_attribute | chunk0 | 1 | high |
| m2 | object | clock | clock | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | roof | roof | noun_chunk_root | chunk2 | 8 | high |
| m4 | attribute | pointed | pointed | modifier_attribute | chunk2 | 7 | medium |
| m5 | object | pole | pole | noun_chunk_root | chunk3 | 14 | high |
| m6 | attribute | tall | tall | size_attribute | chunk3 | 12 | high |
| m7 | attribute | striped | striped | modifier_attribute | chunk3 | 13 | medium |
| m8 | object | people | people | noun_chunk_root | chunk4 | 17 | high |
| m9 | quantity | Several | several | approximate_quantity | chunk4 | 16 | medium |
| m10 | object | sidewalk | sidewalk | noun_chunk_root | chunk5 | 21 | high |
| m11 | action | stands | stand | verb_predicate | doc | 9 | high |
| m12 | action | walk | walk | verb_predicate | doc | 18 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> building |
| e1 | has_attribute | m3 | m4 | medium | chunk2 amod -> roof |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> pole |
| e3 | has_attribute | m5 | m7 | medium | chunk3 amod -> pole |
| e4 | has_quantity | m8 | m9 | medium | chunk4 quantity -> people |
| e5 | agent | m11 | m0 | medium | nsubj -> stands |
| e6 | agent | m12 | m8 | medium | nsubj -> walk |
| e7 | relation | m0 | m2 | high | with |
| e8 | relation | m0 | m3 | high | with |
| e9 | relation | m0 | m5 | high | beside |
| e10 | relation | m8 | m10 | medium | along |

### Skipped Raw Concept Edges
| type | source | target | confidence | reason | evidence |
| --- | --- | --- | --- | --- | --- |
| relation | m8 | m8 | high | self_edge_after_coref | in_front_of |

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | building | object | raw_lemma | wordnet_synset:building.n.01 + stage9_audit | structure, artifact | m0 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m2 | object | clock | clock | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:clock", "parents": []} |
| ent_m3 | object | roof | roof | object | raw_lemma | wordnet_synset:roof.n.01 + stage9_audit | architectural_part, structure, artifact | m3 | raw_mention |  |  |  | True | {"canonical": "entity:roof", "parents": ["entity_parent:architectural_part", "entity_parent:structure", "entity_parent:artifact"]} |
| ent_m5 | object | pole | pole | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:pole", "parents": []} |
| ent_m8 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m8 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m10 | object | sidewalk | sidewalk | object | raw_lemma | wordnet_synset:sidewalk.n.01 + stage9_audit | path, place | m10 | raw_mention |  |  |  | True | {"canonical": "entity:sidewalk", "parents": ["entity_parent:path", "entity_parent:place"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m11 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m12 | walk | walk | walk | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m8->ent_m8 | {"canonical": "action:walk", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e5 | nsubj -> stands |  |  |
| ce1 | walk | agent | agent | none | m8 | ent_m8 | medium | e6 | nsubj -> walk |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e7 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e8 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | beside | next_to | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e9 | False | False |  |  |
| cr3 | m8 | m10 | ent_m8 | ent_m10 | along | along | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | medium | e10 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | building |  |  | structure, artifact | entity_exists:building | True | high |
| cf1 | entity_exists | clock |  |  |  | entity_exists:clock | True | low |
| cf2 | entity_exists | roof |  |  | architectural_part, structure, artifact | entity_exists:roof | True | high |
| cf3 | entity_exists | pole |  |  |  | entity_exists:pole | True | low |
| cf4 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf5 | entity_exists | sidewalk |  |  | path, place | entity_exists:sidewalk | True | high |
| cf6 | has_attribute | building | yellow |  | color_attribute, color, visual_attribute | has_attribute:building:yellow | True | high |
| cf7 | has_attribute | roof | pointed |  | modifier_attribute, visual_attribute | has_attribute:roof:pointed | True | medium |
| cf8 | has_attribute | pole | tall |  | size_attribute, height, visual_attribute | has_attribute:pole:tall | True | high |
| cf9 | has_attribute | pole | striped |  | pattern_attribute, clean_exact_overlap, pattern, pattern_marking, texture, visual_attribute | has_attribute:pole:striped | True | medium |
| cf10 | has_quantity | people | several |  | approximate_quantity, quantity | has_quantity:people:several | True | medium |
| cf11 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf12 | event_role | stand | agent | building |  | event_role:stand:agent:building | True | medium |
| cf13 | action_event | walk |  |  | locomotion_action, visual_action | action_event:walk | True | high |
| cf14 | event_role | walk | agent | people |  | event_role:walk:agent:people | True | medium |
| cf15 | relation | building | with | clock | association_relation, visual_relation | relation:building:with:clock | True | high |
| cf16 | relation | building | with | roof | association_relation, visual_relation | relation:building:with:roof | True | high |
| cf17 | relation | building | next_to | pole | spatial_proximity, visual_relation | relation:building:next_to:pole | True | high |
| cf18 | relation | people | along | sidewalk | spatial_path, visual_relation | relation:people:along:sidewalk | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e9 |  |  |  | {"canonical": "next_to", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e9", "raw_relation": "beside", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 12

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `0b17046c71a518f3de7f1db6c455d6f5b8396a4a19bf5dbc76eea5acbcc81014`
**parse_path:** `tag_list`

> bicyclists, race, street, cone, helmets

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | bicyclists | bicyclist | segment_head | t0 | 0 | high |
| m1 | object | race | race | segment_head | t1 | 0 | high |
| m2 | object | street | street | segment_head | t2 | 0 | high |
| m3 | object | cone | cone | segment_head | t3 | 0 | high |
| m4 | object | helmets | helmet | segment_head | t4 | 0 | high |

### Raw Concept Edges
_none_

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | bicyclist | bicyclists | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:bicyclist", "parents": []} |
| ent_m1 | object | race | race | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:race", "parents": []} |
| ent_m2 | object | street | street | object | raw_lemma | wordnet_synset:street.n.01 + stage9_audit | path, place | m2 | raw_mention |  |  |  | True | {"canonical": "entity:street", "parents": ["entity_parent:path", "entity_parent:place"]} |
| ent_m3 | object | cone | cone | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:cone", "parents": []} |
| ent_m4 | object | helmet | helmets | clothing | raw_lemma | stage9_seed:parent_seed | protective_gear, clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:helmet", "parents": ["entity_parent:protective_gear", "entity_parent:clothing", "entity_parent:wearable"]} |

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
| cf0 | entity_exists | bicyclist |  |  |  | entity_exists:bicyclist | True | low |
| cf1 | entity_exists | race |  |  |  | entity_exists:race | True | low |
| cf2 | entity_exists | street |  |  | path, place | entity_exists:street | True | high |
| cf3 | entity_exists | cone |  |  |  | entity_exists:cone | True | low |
| cf4 | entity_exists | helmet |  |  | protective_gear, clothing, wearable | entity_exists:helmet | True | high |

### Stage 9 Canonicalization Notes
_none_

## 13

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `0bd89cdf3c4942d95b06e8fc118c3e6b4c38bc11434780a82dcb6b26a0b70c14`
**parse_path:** `tag_list`

> half-timbered buildings, street, statue, people, awnings

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | buildings | building | segment_head | t0 | 1 | high |
| m1 | attribute | half-timbered | half-timbered | attribute | t0 | 0 | high |
| m2 | object | street | street | segment_head | t1 | 0 | high |
| m3 | object | statue | statue | segment_head | t2 | 0 | high |
| m4 | object | people | people | segment_head | t3 | 0 | high |
| m5 | object | awnings | awnings | segment_head | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> buildings |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | buildings | object | raw_lemma | wordnet_synset:building.n.01 + stage9_audit | structure, artifact | m0 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m2 | object | street | street | object | raw_lemma | wordnet_synset:street.n.01 + stage9_audit | path, place | m2 | raw_mention |  |  |  | True | {"canonical": "entity:street", "parents": ["entity_parent:path", "entity_parent:place"]} |
| ent_m3 | object | statue | statue | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:statue", "parents": []} |
| ent_m4 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m4 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m5 | object | awnings | awnings | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:awnings", "parents": []} |

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
| cf0 | entity_exists | building |  |  | structure, artifact | entity_exists:building | True | high |
| cf1 | entity_exists | street |  |  | path, place | entity_exists:street | True | high |
| cf2 | entity_exists | statue |  |  |  | entity_exists:statue | True | low |
| cf3 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf4 | entity_exists | awnings |  |  |  | entity_exists:awnings | True | low |
| cf5 | has_attribute | building | half-timbered |  | attribute, visual_attribute | has_attribute:building:half-timbered | True | high |

### Stage 9 Canonicalization Notes
_none_

## 14

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `0ce67c195f5c9dcbb8f9aaa2130fd97a4cc6d553e18406baf64f5000e1e72014`
**parse_path:** `sentence`

> A white building with a blue roof and matching blue doors stands under a clear blue sky. It has multiple windows and is surrounded by a green lawn with shadows cast across it. A paved path leads to the entrance on the right side.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | white | white | color_attribute | chunk0 | 1 | high |
| m2 | object | roof | roof | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | blue | blue | color_attribute | chunk1 | 5 | high |
| m4 | object | doors | door | noun_chunk_root | chunk2 | 10 | high |
| m5 | attribute | matching | matching | modifier_attribute | chunk2 | 8 | medium |
| m6 | attribute | blue | blue | color_attribute | chunk2 | 9 | high |
| m7 | object | sky | sky | noun_chunk_root | chunk3 | 16 | high |
| m8 | attribute | clear | clear | visual_attribute | chunk3 | 14 | medium |
| m9 | attribute | blue | blue | color_attribute | chunk3 | 15 | high |
| m10 | object | windows | window | noun_chunk_root | chunk5 | 21 | high |
| m11 | quantity | multiple | multiple | approximate_quantity | chunk5 | 20 | medium |
| m12 | object | lawn | lawn | noun_chunk_root | chunk6 | 28 | high |
| m13 | attribute | green | green | color_attribute | chunk6 | 27 | high |
| m14 | object | shadows | shadow | noun_chunk_root | chunk7 | 30 | high |
| m15 | object | path | path | noun_chunk_root | chunk9 | 37 | high |
| m16 | attribute | paved | paved | visual_attribute | chunk9 | 36 | medium |
| m17 | object | entrance | entrance | noun_chunk_root | chunk10 | 41 | high |
| m18 | context | side | side | spatial_region | chunk11 | 45 | medium |
| m19 | action | stands | stand | verb_predicate | doc | 11 | high |
| m20 | action | has | have | verb_predicate | doc | 19 | high |
| m21 | action | surrounded | surround | verb_predicate | doc | 24 | high |
| m22 | action | cast | cast | verb_predicate | doc | 31 | high |
| m23 | action | leads | lead | verb_predicate | doc | 38 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> building |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> roof |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> doors |
| e3 | has_attribute | m4 | m6 | high | chunk2 amod -> doors |
| e4 | has_attribute | m7 | m8 | medium | chunk3 amod -> sky |
| e5 | has_attribute | m7 | m9 | high | chunk3 amod -> sky |
| e6 | has_quantity | m10 | m11 | medium | chunk5 quantity -> windows |
| e7 | has_attribute | m12 | m13 | high | chunk6 amod -> lawn |
| e8 | has_attribute | m15 | m16 | medium | chunk9 amod -> path |
| e9 | agent | m19 | m0 | medium | nsubj -> stands |
| e10 | agent | m20 | m0 | medium | nsubj -> has; resolved It -> building |
| e11 | patient | m20 | m10 | medium | dobj -> has |
| e12 | agent | m21 | m0 | medium | inherited agent conj -> has |
| e13 | agent | m22 | m14 | medium | inherited agent acl -> shadows |
| e14 | agent | m23 | m15 | medium | nsubj -> leads |
| e15 | relation | m0 | m2 | high | with |
| e16 | relation | m0 | m4 | high | with |
| e17 | relation | m0 | m7 | high | under |
| e18 | relation | m0 | m12 | medium | by |
| e19 | relation | m12 | m14 | high | with |
| e20 | relation | m14 | m0 | high | across |
| e21 | relation | m15 | m17 | medium | to |
| e22 | relation | m17 | m18 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | building | object | raw_lemma | wordnet_synset:building.n.01 + stage9_audit | structure, artifact | m0 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m2 | object | roof | roof | object | raw_lemma | wordnet_synset:roof.n.01 + stage9_audit | architectural_part, structure, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:roof", "parents": ["entity_parent:architectural_part", "entity_parent:structure", "entity_parent:artifact"]} |
| ent_m4 | object | door | doors | object | raw_lemma | wordnet_synset:door.n.01 + stage9_audit | architectural_part, artifact | m4 | raw_mention |  |  |  | True | {"canonical": "entity:door", "parents": ["entity_parent:architectural_part", "entity_parent:artifact"]} |
| ent_m7 | object | sky | sky | object | raw_lemma | wordnet_synset:sky.n.01 + stage9_audit | natural_scene | m7 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": ["entity_parent:natural_scene"]} |
| ent_m10 | object | window | windows | object | raw_lemma | wordnet_synset:window.n.01 + stage9_audit | architectural_part, artifact | m10 | raw_mention |  |  |  | True | {"canonical": "entity:window", "parents": ["entity_parent:architectural_part", "entity_parent:artifact"]} |
| ent_m12 | object | lawn | lawn | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:lawn", "parents": []} |
| ent_m14 | object | shadow | shadows | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:shadow", "parents": []} |
| ent_m15 | object | path | path | object | raw_lemma | wordnet_synset:path.n.04 + stage9_audit | path, place | m15 | raw_mention |  |  |  | True | {"canonical": "entity:path", "parents": ["entity_parent:path", "entity_parent:place"]} |
| ent_m17 | object | entrance | entrance | object | raw_lemma | none |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:entrance", "parents": []} |
| ent_m18 | context | side | side | object | raw_lemma | semantic_type_fallback | scene_context | m18 | raw_mention |  |  |  | True | {"canonical": "entity:side", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m19 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m20 | has | have | have | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m10->ent_m10 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m21 | surrounded | surround | surround | raw_action | wordnet_synset:surround.v.01 + stage9_audit | spatial_configuration_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:surround", "parents": ["action_parent:spatial_configuration_action", "action_parent:visual_action"]} |  |
| ce3 | m22 | cast | cast | cast | raw_action | visual_action_fallback | visual_action |  | agent:m14->ent_m14 | {"canonical": "action:cast", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m23 | leads | lead | lead | raw_action | visual_action_fallback | visual_action |  | agent:m15->ent_m15 | {"canonical": "action:lead", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e9 | nsubj -> stands |  |  |
| ce1 | have | agent | agent | none | m0 | ent_m0 | medium | e10 | nsubj -> has; resolved It -> building |  |  |
| ce1 | have | patient | patient | none | m10 | ent_m10 | medium | e11 | dobj -> has |  |  |
| ce2 | surround | agent | agent | none | m0 | ent_m0 | medium | e12 | inherited agent conj -> has |  |  |
| ce3 | cast | agent | agent | none | m14 | ent_m14 | medium | e13 | inherited agent acl -> shadows |  |  |
| ce4 | lead | agent | agent | none | m15 | ent_m15 | medium | e14 | nsubj -> leads |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e15 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e16 | False | False |  |  |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e17 | False | False |  |  |
| cr3 | m0 | m12 | ent_m0 | ent_m12 | by | by | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | medium | e18 | False | False |  |  |
| cr4 | m12 | m14 | ent_m12 | ent_m14 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e19 | False | False |  |  |
| cr5 | m14 | m0 | ent_m14 | ent_m0 | across | across | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | high | e20 | False | False |  |  |
| cr6 | m15 | m17 | ent_m15 | ent_m17 | to | to | raw_relation | raw_relation | visual_relation | medium | e21 | False | False |  |  |
| cr7 | m17 | m18 | ent_m17 | ent_m18 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e22 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | building |  |  | structure, artifact | entity_exists:building | True | high |
| cf1 | entity_exists | roof |  |  | architectural_part, structure, artifact | entity_exists:roof | True | high |
| cf2 | entity_exists | door |  |  | architectural_part, artifact | entity_exists:door | True | high |
| cf3 | entity_exists | sky |  |  | natural_scene | entity_exists:sky | True | high |
| cf4 | entity_exists | window |  |  | architectural_part, artifact | entity_exists:window | True | high |
| cf5 | entity_exists | lawn |  |  |  | entity_exists:lawn | True | low |
| cf6 | entity_exists | shadow |  |  |  | entity_exists:shadow | True | low |
| cf7 | entity_exists | path |  |  | path, place | entity_exists:path | True | high |
| cf8 | entity_exists | entrance |  |  |  | entity_exists:entrance | True | low |
| cf9 | entity_exists | side |  |  | scene_context | entity_exists:side | True | medium |
| cf10 | has_attribute | building | white |  | color_attribute, color, visual_attribute | has_attribute:building:white | True | high |
| cf11 | has_attribute | roof | blue |  | color_attribute, color, visual_attribute | has_attribute:roof:blue | True | high |
| cf12 | has_attribute | door | matching |  | modifier_attribute, visual_attribute | has_attribute:door:matching | True | medium |
| cf13 | has_attribute | door | blue |  | color_attribute, color, visual_attribute | has_attribute:door:blue | True | high |
| cf14 | has_attribute | sky | clear |  | weather_attribute, opaqeness, weather, visual_attribute | has_attribute:sky:clear | True | medium |
| cf15 | has_attribute | sky | blue |  | color_attribute, color, visual_attribute | has_attribute:sky:blue | True | high |
| cf16 | has_quantity | window | multiple |  | approximate_quantity, quantity | has_quantity:window:multiple | True | medium |
| cf17 | has_attribute | lawn | green |  | color_attribute, color, visual_attribute | has_attribute:lawn:green | True | high |
| cf18 | has_attribute | path | paved |  | visual_attribute | has_attribute:path:paved | True | medium |
| cf19 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf20 | event_role | stand | agent | building |  | event_role:stand:agent:building | True | medium |
| cf21 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf22 | event_role | have | agent | building |  | event_role:have:agent:building | True | medium |
| cf23 | event_role | have | patient | window |  | event_role:have:patient:window | True | medium |
| cf24 | action_event | surround |  |  | spatial_configuration_action, visual_action | action_event:surround | True | high |
| cf25 | event_role | surround | agent | building |  | event_role:surround:agent:building | True | medium |
| cf26 | action_event | cast |  |  | visual_action | action_event:cast | True | low |
| cf27 | event_role | cast | agent | shadow |  | event_role:cast:agent:shadow | True | medium |
| cf28 | action_event | lead |  |  | visual_action | action_event:lead | True | low |
| cf29 | event_role | lead | agent | path |  | event_role:lead:agent:path | True | medium |
| cf30 | relation | building | with | roof | association_relation, visual_relation | relation:building:with:roof | True | high |
| cf31 | relation | building | with | door | association_relation, visual_relation | relation:building:with:door | True | high |
| cf32 | relation | building | under | sky | spatial_vertical, visual_relation | relation:building:under:sky | True | high |
| cf33 | relation | building | by | lawn | spatial_proximity, visual_relation | relation:building:by:lawn | True | medium |
| cf34 | relation | lawn | with | shadow | association_relation, visual_relation | relation:lawn:with:shadow | True | high |
| cf35 | relation | shadow | across | building | spatial_path, visual_relation | relation:shadow:across:building | True | high |
| cf36 | relation | path | to | entrance | visual_relation | relation:path:to:entrance | True | medium |
| cf37 | relation | entrance | on | side | spatial_support, visual_relation | relation:entrance:on:side | True | high |

### Stage 9 Canonicalization Notes
_none_

## 15

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `0fe378832389290aa28d8f9003f9b89de710b2db48f02eb51cc802f648982814`
**parse_path:** `sentence`

> A woman stands at a podium speaking into a microphone. Behind her, a large screen displays the logo and name "atooma" with the tagline "a touch of magic." The setting is a conference room with branded backdrops and lighting.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "atooma" | atooma | quote_text | doc_quote | 22 | high |
| m1 | attribute | "a touch of magic." | a_touch_of_magic. | quote_text | doc_quote | 26 | high |
| m2 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m3 | object | podium | podium | noun_chunk_root | chunk1 | 5 | high |
| m4 | object | microphone | microphone | noun_chunk_root | chunk2 | 9 | high |
| m5 | object | screen | screen | noun_chunk_root | chunk4 | 16 | high |
| m6 | attribute | large | large | size_attribute | chunk4 | 15 | high |
| m7 | object | logo | logo | noun_chunk_root | chunk5 | 19 | high |
| m8 | object | name | name | noun_chunk_root | chunk6 | 21 | high |
| m9 | object | tagline | tagline | noun_chunk_root | chunk8 | 25 | high |
| m10 | context | setting | setting | scene_context | chunk10 | 28 | high |
| m11 | object | conference room | conference_room | noun_chunk_root | chunk11 | 31 | high |
| m12 | object | backdrops | backdrop | noun_chunk_root | chunk12 | 34 | high |
| m13 | attribute | branded | brand | state_attribute | chunk12 | 33 | medium |
| m14 | object | lighting | lighting | noun_chunk_root | chunk13 | 36 | high |
| m15 | action | stands | stand | verb_predicate | doc | 2 | high |
| m16 | action | speaking | speak | verb_predicate | doc | 6 | high |
| m17 | action | displays | display | verb_predicate | doc | 17 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m5 | m6 | high | chunk4 amod -> screen |
| e1 | has_context | scene | m10 | high | scene_context token setting |
| e2 | has_attribute | m12 | m13 | medium | chunk12 amod -> backdrops |
| e3 | has_attribute | m7 | m0 | high | quote appos -> logo |
| e4 | has_attribute | m9 | m1 | high | quote appos -> tagline |
| e5 | agent | m15 | m2 | medium | nsubj -> stands |
| e6 | agent | m16 | m2 | medium | inherited agent advcl -> stands |
| e7 | agent | m17 | m5 | medium | nsubj -> displays |
| e8 | patient | m17 | m7 | medium | dobj -> displays |
| e9 | patient | m17 | m8 | medium | dobj -> displays |
| e10 | relation | m2 | m3 | medium | at |
| e11 | relation | m2 | m4 | medium | into |
| e12 | relation | m5 | m2 | high | behind |
| e13 | relation | m7 | m9 | high | with |
| e14 | relation | m11 | m12 | high | with |
| e15 | relation | m11 | m14 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m2 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m2 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m3 | object | podium | podium | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:podium", "parents": []} |
| ent_m4 | object | microphone | microphone | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:microphone", "parents": []} |
| ent_m5 | object | screen | screen | device | raw_lemma | stage9_seed:parent_seed | device, artifact | m5 | raw_mention |  |  |  | True | {"canonical": "entity:screen", "parents": ["entity_parent:device", "entity_parent:artifact"]} |
| ent_m7 | object | logo | logo | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:logo", "parents": []} |
| ent_m8 | object | name | name | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:name", "parents": []} |
| ent_m9 | object | tagline | tagline | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:tagline", "parents": []} |
| ent_m10 | context | setting | setting | object | raw_lemma | stage9_seed:parent_seed | scene_context | m10 | raw_mention |  |  |  | True | {"canonical": "entity:setting", "parents": ["entity_parent:scene_context"]} |
| ent_m11 | object | conference_room | conference room | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:conference_room", "parents": []} |
| ent_m12 | object | backdrop | backdrops | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:backdrop", "parents": []} |
| ent_m14 | object | lighting | lighting | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:lighting", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m2->ent_m2 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m16 | speaking | speak | speak | raw_action | stage9_seed:parent_seed | communication_action, visual_action |  | agent:m2->ent_m2 | {"canonical": "action:speak", "parents": ["action_parent:communication_action", "action_parent:visual_action"]} |  |
| ce2 | m17 | displays | display | display | raw_action | wordnet_synset:display.v.01 + stage9_audit | visual_presentation_action, visual_action |  | agent:m5->ent_m5; patient:m7->ent_m7; patient:m8->ent_m8 | {"canonical": "action:display", "parents": ["action_parent:visual_presentation_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m2 | ent_m2 | medium | e5 | nsubj -> stands |  |  |
| ce1 | speak | agent | agent | none | m2 | ent_m2 | medium | e6 | inherited agent advcl -> stands |  |  |
| ce2 | display | agent | agent | none | m5 | ent_m5 | medium | e7 | nsubj -> displays |  |  |
| ce2 | display | patient | patient | none | m7 | ent_m7 | medium | e8 | dobj -> displays |  |  |
| ce2 | display | patient | patient | none | m8 | ent_m8 | medium | e9 | dobj -> displays |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m2 | m3 | ent_m2 | ent_m3 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e10 | False | False |  |  |
| cr1 | m2 | m4 | ent_m2 | ent_m4 | into | into | raw_relation | raw_relation | visual_relation | medium | e11 | False | False |  |  |
| cr2 | m5 | m2 | ent_m5 | ent_m2 | behind | behind | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e12 | False | False |  |  |
| cr3 | m7 | m9 | ent_m7 | ent_m9 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr4 | m11 | m12 | ent_m11 | ent_m12 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr5 | m11 | m14 | ent_m11 | ent_m14 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e15 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | podium |  |  |  | entity_exists:podium | True | low |
| cf2 | entity_exists | microphone |  |  |  | entity_exists:microphone | True | low |
| cf3 | entity_exists | screen |  |  | device, artifact | entity_exists:screen | True | high |
| cf4 | entity_exists | logo |  |  |  | entity_exists:logo | True | low |
| cf5 | entity_exists | name |  |  |  | entity_exists:name | True | low |
| cf6 | entity_exists | tagline |  |  |  | entity_exists:tagline | True | low |
| cf7 | entity_exists | setting |  |  | scene_context | entity_exists:setting | True | high |
| cf8 | entity_exists | conference_room |  |  |  | entity_exists:conference_room | True | high |
| cf9 | entity_exists | backdrop |  |  |  | entity_exists:backdrop | True | low |
| cf10 | entity_exists | lighting |  |  |  | entity_exists:lighting | True | low |
| cf11 | has_attribute | screen | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:screen:large | True | high |
| cf12 | has_attribute | backdrop | brand |  | state_attribute, visual_attribute | has_attribute:backdrop:brand | True | medium |
| cf13 | has_attribute | logo | atooma |  | quote_text, visual_attribute | has_attribute:logo:atooma | True | high |
| cf14 | has_attribute | tagline | a_touch_of_magic. |  | quote_text, visual_attribute | has_attribute:tagline:a_touch_of_magic. | True | high |
| cf15 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf16 | event_role | stand | agent | woman |  | event_role:stand:agent:woman | True | medium |
| cf17 | action_event | speak |  |  | communication_action, visual_action | action_event:speak | True | medium |
| cf18 | event_role | speak | agent | woman |  | event_role:speak:agent:woman | True | medium |
| cf19 | action_event | display |  |  | visual_presentation_action, visual_action | action_event:display | True | high |
| cf20 | event_role | display | agent | screen |  | event_role:display:agent:screen | True | medium |
| cf21 | event_role | display | patient | logo |  | event_role:display:patient:logo | True | medium |
| cf22 | event_role | display | patient | name |  | event_role:display:patient:name | True | medium |
| cf23 | relation | woman | at | podium | spatial_location, visual_relation | relation:woman:at:podium | True | medium |
| cf24 | relation | woman | into | microphone | visual_relation | relation:woman:into:microphone | True | medium |
| cf25 | relation | screen | behind | woman | spatial_depth, visual_relation | relation:screen:behind:woman | True | high |
| cf26 | relation | logo | with | tagline | association_relation, visual_relation | relation:logo:with:tagline | True | high |
| cf27 | relation | conference_room | with | backdrop | association_relation, visual_relation | relation:conference_room:with:backdrop | True | high |
| cf28 | relation | conference_room | with | lighting | association_relation, visual_relation | relation:conference_room:with:lighting | True | high |

### Stage 9 Canonicalization Notes
_none_

## 16

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `100e688aa0945869b4f39eaeab2d64ecd6ecd0a7984780489c7d39f95f9f0c14`
**parse_path:** `sentence`

> A brown goose stands on snow-covered ground, its orange feet visible. It has a dark head and is surrounded by scattered leaves.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | goose | goose | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | brown | brown | color_attribute | chunk0 | 1 | high |
| m2 | object | ground | ground | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | snow-covered | snow-covered | modifier_attribute | chunk1 | 5 | medium |
| m4 | object | feet | foot | noun_chunk_root | chunk2 | 10 | high |
| m5 | attribute | orange | orange | color_attribute | chunk2 | 9 | high |
| m6 | object | head | head | noun_chunk_root | chunk4 | 17 | high |
| m7 | attribute | dark | dark | visual_attribute | chunk4 | 16 | medium |
| m8 | object | leaves | leaf | noun_chunk_root | chunk5 | 23 | high |
| m9 | attribute | scattered | scatter | state_attribute | chunk5 | 22 | medium |
| m10 | action | stands | stand | verb_predicate | doc | 3 | high |
| m11 | action | has | have | verb_predicate | doc | 14 | high |
| m12 | action | surrounded | surround | verb_predicate | doc | 20 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> goose |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> ground |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> feet |
| e3 | has_attribute | m6 | m7 | medium | chunk4 amod -> head |
| e4 | has_attribute | m8 | m9 | medium | chunk5 amod -> leaves |
| e5 | agent | m10 | m0 | medium | nsubj -> stands |
| e6 | agent | m11 | m4 | medium | nsubj -> has; resolved It -> feet |
| e7 | patient | m11 | m6 | medium | dobj -> has |
| e8 | agent | m12 | m4 | medium | inherited agent conj -> has |
| e9 | relation | m0 | m2 | high | on |
| e10 | relation | m4 | m8 | medium | by |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | goose | goose | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:goose", "parents": []} |
| ent_m2 | object | ground | ground | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:ground", "parents": []} |
| ent_m4 | object | foot | feet | object | raw_lemma | stage9_seed:parent_seed | body_part | m4 | raw_mention |  |  |  | True | {"canonical": "entity:foot", "parents": ["entity_parent:body_part"]} |
| ent_m6 | object | head | head | object | raw_lemma | stage9_seed:parent_seed | body_part | m6 | raw_mention |  |  |  | True | {"canonical": "entity:head", "parents": ["entity_parent:body_part"]} |
| ent_m8 | object | leaf | leaves | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:leaf", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m11 | has | have | have | raw_action | visual_action_fallback | visual_action |  | agent:m4->ent_m4; patient:m6->ent_m6 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m12 | surrounded | surround | surround | raw_action | wordnet_synset:surround.v.01 + stage9_audit | spatial_configuration_action, visual_action |  | agent:m4->ent_m4 | {"canonical": "action:surround", "parents": ["action_parent:spatial_configuration_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e5 | nsubj -> stands |  |  |
| ce1 | have | agent | agent | none | m4 | ent_m4 | medium | e6 | nsubj -> has; resolved It -> feet |  |  |
| ce1 | have | patient | patient | none | m6 | ent_m6 | medium | e7 | dobj -> has |  |  |
| ce2 | surround | agent | agent | none | m4 | ent_m4 | medium | e8 | inherited agent conj -> has |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e9 | False | False |  |  |
| cr1 | m4 | m8 | ent_m4 | ent_m8 | by | by | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | medium | e10 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | goose |  |  |  | entity_exists:goose | True | low |
| cf1 | entity_exists | ground |  |  |  | entity_exists:ground | True | low |
| cf2 | entity_exists | foot |  |  | body_part | entity_exists:foot | True | high |
| cf3 | entity_exists | head |  |  | body_part | entity_exists:head | True | high |
| cf4 | entity_exists | leaf |  |  |  | entity_exists:leaf | True | low |
| cf5 | has_attribute | goose | brown |  | color_attribute, color, visual_attribute | has_attribute:goose:brown | True | high |
| cf6 | has_attribute | ground | snow-covered |  | modifier_attribute, visual_attribute | has_attribute:ground:snow-covered | True | medium |
| cf7 | has_attribute | foot | orange |  | color_attribute, color, visual_attribute | has_attribute:foot:orange | True | high |
| cf8 | has_attribute | head | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:head:dark | True | medium |
| cf9 | has_attribute | leaf | scatter |  | state_attribute, visual_attribute | has_attribute:leaf:scatter | True | medium |
| cf10 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf11 | event_role | stand | agent | goose |  | event_role:stand:agent:goose | True | medium |
| cf12 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf13 | event_role | have | agent | foot |  | event_role:have:agent:foot | True | medium |
| cf14 | event_role | have | patient | head |  | event_role:have:patient:head | True | medium |
| cf15 | action_event | surround |  |  | spatial_configuration_action, visual_action | action_event:surround | True | high |
| cf16 | event_role | surround | agent | foot |  | event_role:surround:agent:foot | True | medium |
| cf17 | relation | goose | on | ground | spatial_support, visual_relation | relation:goose:on:ground | True | high |
| cf18 | relation | foot | by | leaf | spatial_proximity, visual_relation | relation:foot:by:leaf | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 17

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `11ff950eed40cf38696dcfc36245c105bb31059099f4df7cdab35e11e6881c14`
**parse_path:** `sentence`

> A woman in a white suit and a man in a black suit shake hands. Behind them are two flags: a blue one with yellow stars and a red, white, and blue flag with a coat of arms. They stand indoors against a marble wall with a crest above the flags.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | suit | suit | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | white | white | color_attribute | chunk1 | 4 | high |
| m3 | object | man | man | noun_chunk_root | chunk2 | 8 | high |
| m4 | object | suit | suit | noun_chunk_root | chunk3 | 12 | high |
| m5 | attribute | black | black | color_attribute | chunk3 | 11 | high |
| m6 | object | hands | hand | noun_chunk_root | chunk4 | 14 | high |
| m7 | object | flags | flag | noun_chunk_root | chunk6 | 20 | high |
| m8 | quantity | two | two | exact_quantity | chunk6 | 19 | high |
| m9 | object | stars | star | noun_chunk_root | chunk7 | 27 | high |
| m10 | attribute | yellow | yellow | color_attribute | chunk7 | 26 | high |
| m11 | object | flag | flag | noun_chunk_root | chunk8 | 36 | high |
| m12 | attribute | red | red | color_attribute | chunk8 | 30 | high |
| m13 | attribute | white | white | color_attribute | chunk8 | 32 | high |
| m14 | attribute | blue | blue | color_attribute | chunk8 | 35 | high |
| m15 | object | coat | coat | noun_chunk_root | chunk9 | 39 | high |
| m16 | object | arms | arm | noun_chunk_root | chunk10 | 41 | high |
| m17 | object | wall | wall | noun_chunk_root | chunk12 | 49 | high |
| m18 | attribute | marble | marble | compound_modifier | chunk12 | 48 | medium |
| m19 | object | crest | crest | noun_chunk_root | chunk13 | 52 | high |
| m20 | object | flags | flag | noun_chunk_root | chunk14 | 55 | high |
| m21 | context | indoors | indoors | scene_context | doc | 45 | high |
| m22 | reference | one | one | singular_substitute | nominal_reference | 24 | high |
| m23 | object | blue flag | flag | nominal_reference_instance | nominal_reference | 24 | high |
| m24 | attribute | blue | blue | color_attribute | nominal_reference | 23 | high |
| m25 | action | shake | shake | verb_predicate | doc | 13 | high |
| m26 | action | stand | stand | verb_predicate | doc | 44 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> suit |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> suit |
| e2 | has_quantity | m7 | m8 | high | chunk6 quantity -> flags |
| e3 | has_attribute | m9 | m10 | high | chunk7 amod -> stars |
| e4 | has_attribute | m11 | m12 | high | chunk8 amod -> flag |
| e5 | has_attribute | m11 | m13 | high | chunk8 conj -> flag |
| e6 | has_attribute | m11 | m14 | high | chunk8 conj -> flag |
| e7 | has_attribute | m17 | m18 | medium | chunk12 compound -> wall |
| e8 | has_context | scene | m21 | high | scene_context token indoors |
| e9 | refers_to | m22 | m7 | high | singular_substitute one -> flags; score=111; margin=19 |
| e10 | derived_from | m23 | m7 | high | singular_substitute one -> flags; score=111; margin=19 |
| e11 | has_attribute | m23 | m24 | high | nominal_reference amod -> one; singular_substitute one -> flags; score=111; margin=19 |
| e12 | agent | m25 | m0 | medium | nsubj -> shake |
| e13 | agent | m25 | m3 | medium | nsubj -> shake |
| e14 | patient | m25 | m6 | medium | dobj -> shake |
| e15 | agent | m26 | m0 | medium | nsubj -> stand; resolved They -> woman |
| e16 | relation | m0 | m1 | high | in |
| e17 | relation | m3 | m4 | high | in |
| e18 | relation | m7 | m0 | high | behind |
| e19 | relation | m23 | m9 | high | with |
| e20 | relation | m11 | m15 | high | with |
| e21 | relation | m15 | m16 | medium | of |
| e22 | relation | m0 | m17 | high | against |
| e23 | relation | m17 | m19 | high | with |
| e24 | relation | m19 | m20 | high | above |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | suit | suit | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:suit", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m3 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m4 | object | suit | suit | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:suit", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m6 | object | hand | hands | object | raw_lemma | stage9_seed:parent_seed | body_part | m6 | raw_mention |  |  |  | True | {"canonical": "entity:hand", "parents": ["entity_parent:body_part"]} |
| ent_m7 | object | flag | flags | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:flag", "parents": []} |
| ent_m9 | object | star | stars | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:star", "parents": []} |
| ent_m11 | object | flag | flag | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:flag", "parents": []} |
| ent_m15 | object | coat | coat | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m15 | raw_mention |  |  |  | True | {"canonical": "entity:coat", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m16 | object | arm | arms | object | raw_lemma | stage9_seed:parent_seed | body_part | m16 | raw_mention |  |  |  | True | {"canonical": "entity:arm", "parents": ["entity_parent:body_part"]} |
| ent_m17 | object | wall | wall | object | raw_lemma | wordnet_synset:wall.n.01 + stage9_audit | architectural_part, structure, artifact | m17 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": ["entity_parent:architectural_part", "entity_parent:structure", "entity_parent:artifact"]} |
| ent_m19 | object | crest | crest | object | raw_lemma | none |  | m19 | raw_mention |  |  |  | True | {"canonical": "entity:crest", "parents": []} |
| ent_m20 | object | flag | flags | object | raw_lemma | none |  | m20 | raw_mention |  |  |  | True | {"canonical": "entity:flag", "parents": []} |
| ent_m21 | context | indoors | indoors | object | raw_lemma | stage9_seed:parent_seed | scene_context | m21 | raw_mention |  |  |  | True | {"canonical": "entity:indoors", "parents": ["entity_parent:scene_context"]} |
| ent_m23 | object | flag | blue flag | object | raw_lemma | none |  | m23 | raw_mention |  |  |  | True | {"canonical": "entity:flag", "parents": []} |
| eref_m22 | instance | flag | one | object | raw_lemma | none |  | m22 | stage9_reference | ent_m7 |  | 1 | True | {"canonical": "entity:flag", "parents": []} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m22 | eref_m22 | m7 | ent_m7 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m25 | shake | shake | shake | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; agent:m3->ent_m3; patient:m6->ent_m6 | {"canonical": "action:shake", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m26 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | shake | agent | agent | none | m0 | ent_m0 | medium | e12 | nsubj -> shake |  |  |
| ce0 | shake | agent | agent | none | m3 | ent_m3 | medium | e13 | nsubj -> shake |  |  |
| ce0 | shake | patient | patient | none | m6 | ent_m6 | medium | e14 | dobj -> shake |  |  |
| ce1 | stand | agent | agent | none | m0 | ent_m0 | medium | e15 | nsubj -> stand; resolved They -> woman |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e16 | False | False |  |  |
| cr1 | m3 | m4 | ent_m3 | ent_m4 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e17 | False | False |  |  |
| cr2 | m7 | m0 | ent_m7 | ent_m0 | behind | behind | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e18 | False | False |  |  |
| cr3 | m23 | m9 | ent_m23 | ent_m9 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e19 | False | False |  |  |
| cr4 | m11 | m15 | ent_m11 | ent_m15 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e20 | False | False |  |  |
| cr5 | m15 | m16 | ent_m15 | ent_m16 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e21 | False | False |  |  |
| cr6 | m0 | m17 | ent_m0 | ent_m17 | against | against | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_contact, visual_relation | high | e22 | False | False |  |  |
| cr7 | m17 | m19 | ent_m17 | ent_m19 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e23 | False | False |  |  |
| cr8 | m19 | m20 | ent_m19 | ent_m20 | above | above | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e24 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | suit |  |  | clothing, wearable | entity_exists:suit | True | high |
| cf2 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf3 | entity_exists | suit |  |  | clothing, wearable | entity_exists:suit | True | high |
| cf4 | entity_exists | hand |  |  | body_part | entity_exists:hand | True | high |
| cf5 | entity_exists | flag |  |  |  | entity_exists:flag | True | low |
| cf6 | entity_exists | star |  |  |  | entity_exists:star | True | low |
| cf7 | entity_exists | flag |  |  |  | entity_exists:flag | True | low |
| cf8 | entity_exists | coat |  |  | clothing, wearable | entity_exists:coat | True | high |
| cf9 | entity_exists | arm |  |  | body_part | entity_exists:arm | True | high |
| cf10 | entity_exists | wall |  |  | architectural_part, structure, artifact | entity_exists:wall | True | high |
| cf11 | entity_exists | crest |  |  |  | entity_exists:crest | True | low |
| cf12 | entity_exists | flag |  |  |  | entity_exists:flag | True | low |
| cf13 | entity_exists | indoors |  |  | scene_context | entity_exists:indoors | True | high |
| cf14 | entity_exists | flag |  |  |  | entity_exists:flag | True | low |
| cf15 | entity_exists | flag |  |  |  | entity_exists:flag | True | low |
| cf16 | has_attribute | suit | white |  | color_attribute, color, visual_attribute | has_attribute:suit:white | True | high |
| cf17 | has_attribute | suit | black |  | color_attribute, color, visual_attribute | has_attribute:suit:black | True | high |
| cf18 | has_quantity | flag | two |  | exact_quantity, quantity | has_quantity:flag:two | True | high |
| cf19 | has_attribute | star | yellow |  | color_attribute, color, visual_attribute | has_attribute:star:yellow | True | high |
| cf20 | has_attribute | flag | red |  | color_attribute, color, visual_attribute | has_attribute:flag:red | True | high |
| cf21 | has_attribute | flag | white |  | color_attribute, color, visual_attribute | has_attribute:flag:white | True | high |
| cf22 | has_attribute | flag | blue |  | color_attribute, color, visual_attribute | has_attribute:flag:blue | True | high |
| cf23 | has_attribute | wall | marble |  | material_attribute, material, visual_attribute | has_attribute:wall:marble | True | medium |
| cf24 | has_attribute | flag | blue |  | color_attribute, color, visual_attribute | has_attribute:flag:blue | True | high |
| cf25 | action_event | shake |  |  | visual_action | action_event:shake | True | low |
| cf26 | event_role | shake | agent | woman |  | event_role:shake:agent:woman | True | medium |
| cf27 | event_role | shake | agent | man |  | event_role:shake:agent:man | True | medium |
| cf28 | event_role | shake | patient | hand |  | event_role:shake:patient:hand | True | medium |
| cf29 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf30 | event_role | stand | agent | woman |  | event_role:stand:agent:woman | True | medium |
| cf31 | relation | woman | in | suit | spatial_containment, visual_relation | relation:woman:in:suit | True | high |
| cf32 | relation | man | in | suit | spatial_containment, visual_relation | relation:man:in:suit | True | high |
| cf33 | relation | flag | behind | woman | spatial_depth, visual_relation | relation:flag:behind:woman | True | high |
| cf34 | relation | flag | with | star | association_relation, visual_relation | relation:flag:with:star | True | high |
| cf35 | relation | flag | with | coat | association_relation, visual_relation | relation:flag:with:coat | True | high |
| cf36 | relation | coat | of | arm | part_relation, visual_relation | relation:coat:of:arm | True | medium |
| cf37 | relation | woman | against | wall | spatial_contact, visual_relation | relation:woman:against:wall | True | high |
| cf38 | relation | wall | with | crest | association_relation, visual_relation | relation:wall:with:crest | True | high |
| cf39 | relation | crest | above | flag | spatial_vertical, visual_relation | relation:crest:above:flag | True | high |

### Stage 9 Canonicalization Notes
_none_

## 18

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `1213ce4d1b75b64c9baec0406d020eb811e1220d5ff30ab47b5051cd44d0e814`
**parse_path:** `tag_list`

> cyclists, track, helmets, bikes, green surface

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | cyclists | cyclist | segment_head | t0 | 0 | high |
| m1 | object | track | track | segment_head | t1 | 0 | high |
| m2 | object | helmets | helmet | segment_head | t2 | 0 | high |
| m3 | object | bikes | bike | segment_head | t3 | 0 | high |
| m4 | object | surface | surface | segment_head | t4 | 1 | high |
| m5 | attribute | green | green | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m4 | m5 | high | t4 internal amod -> surface |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | cyclist | cyclists | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:cyclist", "parents": []} |
| ent_m1 | object | track | track | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:track", "parents": []} |
| ent_m2 | object | helmet | helmets | clothing | raw_lemma | stage9_seed:parent_seed | protective_gear, clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:helmet", "parents": ["entity_parent:protective_gear", "entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | bicycle | bikes | vehicle | stage9_seed:synonym_seed | stage9_seed:parent_seed | vehicle | m3 | raw_mention |  |  |  | True | {"canonical": "entity:bicycle", "parents": ["entity_parent:vehicle"]} |
| ent_m4 | object | surface | surface | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": []} |

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
| cf0 | entity_exists | cyclist |  |  |  | entity_exists:cyclist | True | low |
| cf1 | entity_exists | track |  |  |  | entity_exists:track | True | low |
| cf2 | entity_exists | helmet |  |  | protective_gear, clothing, wearable | entity_exists:helmet | True | high |
| cf3 | entity_exists | bicycle |  |  | vehicle | entity_exists:bicycle | True | high |
| cf4 | entity_exists | surface |  |  |  | entity_exists:surface | True | low |
| cf5 | has_attribute | surface | green |  | color_attribute, color, visual_attribute | has_attribute:surface:green | True | high |

### Stage 9 Canonicalization Notes
_none_

## 19

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `128d683c4174168321af868bcb9bf9e881116f6e303ed8f7d58da1616c8a4014`
**parse_path:** `sentence`

> A blue jet flies through a cloudy sky, leaving a white trail behind it.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | jet | jet | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | blue | blue | color_attribute | chunk0 | 1 | high |
| m2 | object | sky | sky | noun_chunk_root | chunk1 | 7 | high |
| m3 | attribute | cloudy | cloudy | modifier_attribute | chunk1 | 6 | medium |
| m4 | object | trail | trail | noun_chunk_root | chunk2 | 12 | high |
| m5 | attribute | white | white | color_attribute | chunk2 | 11 | high |
| m6 | action | flies | fly | verb_predicate | doc | 3 | high |
| m7 | action | leaving | leave | verb_predicate | doc | 9 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> jet |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> sky |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> trail |
| e3 | agent | m6 | m0 | medium | nsubj -> flies |
| e4 | agent | m7 | m0 | medium | inherited agent advcl -> flies |
| e5 | patient | m7 | m4 | medium | dobj -> leaving |
| e6 | relation | m0 | m2 | medium | through |
| e7 | relation | m4 | m0 | medium | behind; repaired_self_edge_source from jet |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | jet | jet | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:jet", "parents": []} |
| ent_m2 | object | sky | sky | object | raw_lemma | wordnet_synset:sky.n.01 + stage9_audit | natural_scene | m2 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": ["entity_parent:natural_scene"]} |
| ent_m4 | object | trail | trail | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:trail", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m6 | flies | fly | fly | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:fly", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m7 | leaving | leave | leave | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m4->ent_m4 | {"canonical": "action:leave", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | fly | agent | agent | none | m0 | ent_m0 | medium | e3 | nsubj -> flies |  |  |
| ce1 | leave | agent | agent | none | m0 | ent_m0 | medium | e4 | inherited agent advcl -> flies |  |  |
| ce1 | leave | patient | patient | none | m4 | ent_m4 | medium | e5 | dobj -> leaving |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | through | through | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | medium | e6 | False | False |  |  |
| cr1 | m4 | m0 | ent_m4 | ent_m0 | behind; repaired_self_edge_source from jet | behind | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | medium | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | jet |  |  |  | entity_exists:jet | True | low |
| cf1 | entity_exists | sky |  |  | natural_scene | entity_exists:sky | True | high |
| cf2 | entity_exists | trail |  |  |  | entity_exists:trail | True | low |
| cf3 | has_attribute | jet | blue |  | color_attribute, color, visual_attribute | has_attribute:jet:blue | True | high |
| cf4 | has_attribute | sky | cloudy |  | weather_attribute, weather, visual_attribute | has_attribute:sky:cloudy | True | medium |
| cf5 | has_attribute | trail | white |  | color_attribute, color, visual_attribute | has_attribute:trail:white | True | high |
| cf6 | action_event | fly |  |  | visual_action | action_event:fly | True | low |
| cf7 | event_role | fly | agent | jet |  | event_role:fly:agent:jet | True | medium |
| cf8 | action_event | leave |  |  | visual_action | action_event:leave | True | low |
| cf9 | event_role | leave | agent | jet |  | event_role:leave:agent:jet | True | medium |
| cf10 | event_role | leave | patient | trail |  | event_role:leave:patient:trail | True | medium |
| cf11 | relation | jet | through | sky | spatial_path, visual_relation | relation:jet:through:sky | True | medium |
| cf12 | relation | trail | behind | jet | spatial_depth, visual_relation | relation:trail:behind:jet | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e7 |  |  |  | {"canonical": "behind", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e7", "raw_relation": "behind; repaired_self_edge_source from jet", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 20

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `137626f9019827af55c18a7b2c8617c201b47d6e195ec0142918817fd6a32c14`
**parse_path:** `sentence`

> Four people pose in front of a backdrop with logos and text. A man in a black suit holds a blue award, while three women beside him hold trophies and wave. They are at the Stevie 2019 awards event.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Four | four | exact_quantity | chunk0 | 0 | high |
| m2 | object | backdrop | backdrop | noun_chunk_root | chunk2 | 7 | high |
| m3 | object | logos | logo | noun_chunk_root | chunk3 | 9 | high |
| m4 | object | text | text | noun_chunk_root | chunk4 | 11 | high |
| m5 | object | man | man | noun_chunk_root | chunk5 | 14 | high |
| m6 | object | suit | suit | noun_chunk_root | chunk6 | 18 | high |
| m7 | attribute | black | black | color_attribute | chunk6 | 17 | high |
| m8 | object | award | award | noun_chunk_root | chunk7 | 22 | high |
| m9 | attribute | blue | blue | color_attribute | chunk7 | 21 | high |
| m10 | object | women | woman | noun_chunk_root | chunk8 | 26 | high |
| m11 | quantity | three | three | exact_quantity | chunk8 | 25 | high |
| m12 | object | trophies | trophy | noun_chunk_root | chunk10 | 30 | high |
| m13 | object | event | event | noun_chunk_root | chunk12 | 41 | high |
| m14 | quantity | 2019 | 2019 | exact_quantity | chunk12 | 39 | high |
| m15 | attribute | awards | award | compound_modifier | chunk12 | 40 | medium |
| m16 | action | pose | pose | verb_predicate | doc | 2 | high |
| m17 | action | holds | hold | verb_predicate | doc | 19 | high |
| m18 | action | hold | hold | verb_predicate | doc | 29 | high |
| m19 | action | wave | wave | verb_predicate | doc | 32 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> people |
| e1 | has_attribute | m6 | m7 | high | chunk6 amod -> suit |
| e2 | has_attribute | m8 | m9 | high | chunk7 amod -> award |
| e3 | has_quantity | m10 | m11 | high | chunk8 quantity -> women |
| e4 | has_quantity | m13 | m14 | high | chunk12 quantity -> event |
| e5 | has_attribute | m13 | m15 | medium | chunk12 compound -> event |
| e6 | agent | m16 | m0 | medium | nsubj -> pose |
| e7 | agent | m17 | m5 | medium | nsubj -> holds |
| e8 | patient | m17 | m8 | medium | dobj -> holds |
| e9 | agent | m18 | m10 | medium | nsubj -> hold |
| e10 | patient | m18 | m12 | medium | dobj -> hold |
| e11 | agent | m19 | m10 | medium | inherited agent conj -> hold |
| e12 | relation | m0 | m2 | high | in_front_of |
| e13 | relation | m2 | m3 | high | with |
| e14 | relation | m2 | m4 | high | with |
| e15 | relation | m5 | m6 | high | in |
| e16 | relation | m10 | m5 | high | beside |
| e17 | relation | m10 | m13 | medium | at |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | backdrop | backdrop | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:backdrop", "parents": []} |
| ent_m3 | object | logo | logos | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:logo", "parents": []} |
| ent_m4 | object | text | text | document | raw_lemma | stage9_seed:parent_seed | text_content | m4 | raw_mention |  |  |  | True | {"canonical": "entity:text", "parents": ["entity_parent:text_content"]} |
| ent_m5 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m5 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m6 | object | suit | suit | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m6 | raw_mention |  |  |  | True | {"canonical": "entity:suit", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m8 | object | award | award | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:award", "parents": []} |
| ent_m10 | object | woman | women | person | stage9_seed:synonym_seed | stage9_seed:parent_seed | person, human | m10 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m12 | object | trophy | trophies | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:trophy", "parents": []} |
| ent_m13 | object | event | event | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:event", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | pose | pose | pose | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:pose", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m17 | holds | hold | hold | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action |  | agent:m5->ent_m5; patient:m8->ent_m8 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce2 | m18 | hold | hold | hold | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action |  | agent:m10->ent_m10; patient:m12->ent_m12 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce3 | m19 | wave | wave | wave | raw_action | visual_action_fallback | visual_action |  | agent:m10->ent_m10 | {"canonical": "action:wave", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | pose | agent | agent | none | m0 | ent_m0 | medium | e6 | nsubj -> pose |  |  |
| ce1 | hold | agent | agent | none | m5 | ent_m5 | medium | e7 | nsubj -> holds |  |  |
| ce1 | hold | patient | patient | none | m8 | ent_m8 | medium | e8 | dobj -> holds |  |  |
| ce2 | hold | agent | agent | none | m10 | ent_m10 | medium | e9 | nsubj -> hold |  |  |
| ce2 | hold | patient | patient | none | m12 | ent_m12 | medium | e10 | dobj -> hold |  |  |
| ce3 | wave | agent | agent | none | m10 | ent_m10 | medium | e11 | inherited agent conj -> hold |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in_front_of | in_front_of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e12 | False | False |  |  |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr2 | m2 | m4 | ent_m2 | ent_m4 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr3 | m5 | m6 | ent_m5 | ent_m6 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e15 | False | False |  |  |
| cr4 | m10 | m5 | ent_m10 | ent_m5 | beside | next_to | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e16 | False | False |  |  |
| cr5 | m10 | m13 | ent_m10 | ent_m13 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e17 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | backdrop |  |  |  | entity_exists:backdrop | True | low |
| cf2 | entity_exists | logo |  |  |  | entity_exists:logo | True | low |
| cf3 | entity_exists | text |  |  | text_content | entity_exists:text | True | high |
| cf4 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf5 | entity_exists | suit |  |  | clothing, wearable | entity_exists:suit | True | high |
| cf6 | entity_exists | award |  |  |  | entity_exists:award | True | low |
| cf7 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf8 | entity_exists | trophy |  |  |  | entity_exists:trophy | True | low |
| cf9 | entity_exists | event |  |  |  | entity_exists:event | True | low |
| cf10 | has_quantity | people | four |  | exact_quantity, quantity | has_quantity:people:four | True | high |
| cf11 | has_attribute | suit | black |  | color_attribute, color, visual_attribute | has_attribute:suit:black | True | high |
| cf12 | has_attribute | award | blue |  | color_attribute, color, visual_attribute | has_attribute:award:blue | True | high |
| cf13 | has_quantity | woman | three |  | exact_quantity, quantity | has_quantity:woman:three | True | high |
| cf14 | has_quantity | event | 2019 |  | exact_quantity, quantity | has_quantity:event:2019 | True | high |
| cf15 | has_attribute | event | award |  | compound_modifier, visual_attribute | has_attribute:event:award | True | medium |
| cf16 | action_event | pose |  |  | body_pose_action, visual_action | action_event:pose | True | high |
| cf17 | event_role | pose | agent | people |  | event_role:pose:agent:people | True | medium |
| cf18 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf19 | event_role | hold | agent | man |  | event_role:hold:agent:man | True | medium |
| cf20 | event_role | hold | patient | award |  | event_role:hold:patient:award | True | medium |
| cf21 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf22 | event_role | hold | agent | woman |  | event_role:hold:agent:woman | True | medium |
| cf23 | event_role | hold | patient | trophy |  | event_role:hold:patient:trophy | True | medium |
| cf24 | action_event | wave |  |  | visual_action | action_event:wave | True | low |
| cf25 | event_role | wave | agent | woman |  | event_role:wave:agent:woman | True | medium |
| cf26 | relation | people | in_front_of | backdrop | spatial_depth, visual_relation | relation:people:in_front_of:backdrop | True | high |
| cf27 | relation | backdrop | with | logo | association_relation, visual_relation | relation:backdrop:with:logo | True | high |
| cf28 | relation | backdrop | with | text | association_relation, visual_relation | relation:backdrop:with:text | True | high |
| cf29 | relation | man | in | suit | spatial_containment, visual_relation | relation:man:in:suit | True | high |
| cf30 | relation | woman | next_to | man | spatial_proximity, visual_relation | relation:woman:next_to:man | True | high |
| cf31 | relation | woman | at | event | spatial_location, visual_relation | relation:woman:at:event | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e16 |  |  |  | {"canonical": "next_to", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e16", "raw_relation": "beside", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 21

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `14dedc4d381cb5086246f6cd530e47a679d897a375a1514606789907e31b4814`
**parse_path:** `sentence`

> Several people stand on a stage in a gymnasium with red and white walls. One woman in a black hoodie and boots smiles as she speaks, while others nearby hold microphones or listen. A camera operator is visible on the left, capturing the event.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Several | several | approximate_quantity | chunk0 | 0 | medium |
| m2 | object | stage | stage | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | gymnasium | gymnasium | noun_chunk_root | chunk2 | 8 | high |
| m4 | object | walls | wall | noun_chunk_root | chunk3 | 13 | high |
| m5 | attribute | red | red | color_attribute | chunk3 | 10 | high |
| m6 | attribute | white | white | color_attribute | chunk3 | 12 | high |
| m7 | object | woman | woman | noun_chunk_root | chunk4 | 16 | high |
| m8 | quantity | One | one | exact_quantity | chunk4 | 15 | high |
| m9 | object | hoodie | hoodie | noun_chunk_root | chunk5 | 20 | high |
| m10 | attribute | black | black | color_attribute | chunk5 | 19 | high |
| m11 | object | boots | boot | noun_chunk_root | chunk6 | 22 | high |
| m12 | object | microphones | microphone | noun_chunk_root | chunk9 | 32 | high |
| m13 | object | operator | operator | noun_chunk_root | chunk10 | 38 | high |
| m14 | attribute | camera | camera | compound_modifier | chunk10 | 37 | medium |
| m15 | context | left | left | spatial_region | chunk11 | 43 | medium |
| m16 | object | event | event | noun_chunk_root | chunk12 | 47 | high |
| m17 | reference | others | other | contrastive_reference | nominal_reference | 29 | high |
| m18 | action | stand | stand | verb_predicate | doc | 2 | high |
| m19 | action | smiles | smile | verb_predicate | doc | 23 | high |
| m20 | action | speaks | speak | verb_predicate | doc | 26 | high |
| m21 | action | hold | hold | verb_predicate | doc | 31 | high |
| m22 | action | listen | listen | verb_predicate | doc | 34 | high |
| m23 | action | capturing | capture | verb_predicate | doc | 45 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | medium | chunk0 quantity -> people |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> walls |
| e2 | has_attribute | m4 | m6 | high | chunk3 conj -> walls |
| e3 | has_quantity | m7 | m8 | high | chunk4 quantity -> woman |
| e4 | has_attribute | m9 | m10 | high | chunk5 amod -> hoodie |
| e5 | has_attribute | m13 | m14 | medium | chunk10 compound -> operator |
| e6 | refers_to | m17 | m0 | high | contrastive_reference others -> people; score=110 |
| e7 | agent | m18 | m0 | medium | nsubj -> stand |
| e8 | agent | m19 | m7 | medium | nsubj -> smiles |
| e9 | agent | m20 | m7 | medium | nsubj -> speaks; resolved she -> woman |
| e10 | agent | m21 | m0 | medium | nsubj -> hold; resolved others -> people |
| e11 | patient | m21 | m12 | medium | dobj -> hold |
| e12 | agent | m22 | m0 | medium | inherited agent conj -> hold |
| e13 | agent | m23 | m13 | medium | inherited agent advcl -> is |
| e14 | patient | m23 | m16 | medium | dobj -> capturing |
| e15 | relation | m0 | m2 | high | on |
| e16 | relation | m0 | m3 | high | in |
| e17 | relation | m3 | m4 | high | with |
| e18 | relation | m7 | m9 | high | in |
| e19 | relation | m7 | m11 | high | in |
| e20 | relation | m13 | m15 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | stage | stage | object | raw_lemma | wordnet_synset:stage.n.03 + stage9_audit | platform, place, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:stage", "parents": ["entity_parent:platform", "entity_parent:place", "entity_parent:artifact"]} |
| ent_m3 | object | gymnasium | gymnasium | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:gymnasium", "parents": []} |
| ent_m4 | object | wall | walls | object | raw_lemma | wordnet_synset:wall.n.01 + stage9_audit | architectural_part, structure, artifact | m4 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": ["entity_parent:architectural_part", "entity_parent:structure", "entity_parent:artifact"]} |
| ent_m7 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m7 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m9 | object | hoodie | hoodie | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:hoodie", "parents": []} |
| ent_m11 | object | boot | boots | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:boot", "parents": []} |
| ent_m12 | object | microphone | microphones | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:microphone", "parents": []} |
| ent_m13 | object | operator | operator | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:operator", "parents": []} |
| ent_m15 | context | left | left | object | raw_lemma | semantic_type_fallback | scene_context | m15 | raw_mention |  |  |  | True | {"canonical": "entity:left", "parents": ["entity_parent:scene_context"]} |
| ent_m16 | object | event | event | object | raw_lemma | none |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:event", "parents": []} |
| eref_m17 | complement_subset | people | others | person | raw_lemma | stage9_seed:parent_seed | person, human | m17 | stage9_reference | ent_m0 |  | many | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m17 | eref_m17 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m19 | smiles | smile | smile | raw_action | stage9_seed:parent_seed | expression_action, visual_action |  | agent:m7->ent_m7 | {"canonical": "action:smile", "parents": ["action_parent:expression_action", "action_parent:visual_action"]} |  |
| ce2 | m20 | speaks | speak | speak | raw_action | stage9_seed:parent_seed | communication_action, visual_action |  | agent:m7->ent_m7 | {"canonical": "action:speak", "parents": ["action_parent:communication_action", "action_parent:visual_action"]} |  |
| ce3 | m21 | hold | hold | hold | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action |  | agent:m0->eref_m17; patient:m12->ent_m12 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce4 | m22 | listen | listen | listen | raw_action | visual_action_fallback | visual_action |  | agent:m0->eref_m17 | {"canonical": "action:listen", "parents": ["action_parent:visual_action"]} |  |
| ce5 | m23 | capturing | capture | capture | raw_action | visual_action_fallback | visual_action |  | agent:m13->ent_m13; patient:m16->ent_m16 | {"canonical": "action:capture", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e7 | nsubj -> stand |  |  |
| ce1 | smile | agent | agent | none | m7 | ent_m7 | medium | e8 | nsubj -> smiles |  |  |
| ce2 | speak | agent | agent | none | m7 | ent_m7 | medium | e9 | nsubj -> speaks; resolved she -> woman |  |  |
| ce3 | hold | agent | agent | none | m0 | eref_m17 | medium | e10 | nsubj -> hold; resolved others -> people |  |  |
| ce3 | hold | patient | patient | none | m12 | ent_m12 | medium | e11 | dobj -> hold |  |  |
| ce4 | listen | agent | agent | none | m0 | eref_m17 | medium | e12 | inherited agent conj -> hold |  | conj_agent_inherited_from_reference_canonical_target |
| ce5 | capture | agent | agent | none | m13 | ent_m13 | medium | e13 | inherited agent advcl -> is |  |  |
| ce5 | capture | patient | patient | none | m16 | ent_m16 | medium | e14 | dobj -> capturing |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e15 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e16 | False | False |  |  |
| cr2 | m3 | m4 | ent_m3 | ent_m4 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e17 | False | False |  |  |
| cr3 | m7 | m9 | ent_m7 | ent_m9 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e18 | False | False |  |  |
| cr4 | m7 | m11 | ent_m7 | ent_m11 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e19 | False | False |  |  |
| cr5 | m13 | m15 | ent_m13 | ent_m15 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e20 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | stage |  |  | platform, place, artifact | entity_exists:stage | True | medium |
| cf2 | entity_exists | gymnasium |  |  |  | entity_exists:gymnasium | True | low |
| cf3 | entity_exists | wall |  |  | architectural_part, structure, artifact | entity_exists:wall | True | high |
| cf4 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf5 | entity_exists | hoodie |  |  |  | entity_exists:hoodie | True | low |
| cf6 | entity_exists | boot |  |  |  | entity_exists:boot | True | low |
| cf7 | entity_exists | microphone |  |  |  | entity_exists:microphone | True | low |
| cf8 | entity_exists | operator |  |  |  | entity_exists:operator | True | low |
| cf9 | entity_exists | left |  |  | scene_context | entity_exists:left | True | medium |
| cf10 | entity_exists | event |  |  |  | entity_exists:event | True | low |
| cf11 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf12 | has_quantity | people | several |  | approximate_quantity, quantity | has_quantity:people:several | True | medium |
| cf13 | has_attribute | wall | red |  | color_attribute, color, visual_attribute | has_attribute:wall:red | True | high |
| cf14 | has_attribute | wall | white |  | color_attribute, color, visual_attribute | has_attribute:wall:white | True | high |
| cf15 | has_quantity | woman | one |  | exact_quantity, quantity | has_quantity:woman:one | True | high |
| cf16 | has_attribute | hoodie | black |  | color_attribute, color, visual_attribute | has_attribute:hoodie:black | True | high |
| cf17 | has_attribute | operator | camera |  | compound_modifier, visual_attribute | has_attribute:operator:camera | True | medium |
| cf18 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf19 | event_role | stand | agent | people |  | event_role:stand:agent:people | True | medium |
| cf20 | action_event | smile |  |  | expression_action, visual_action | action_event:smile | True | high |
| cf21 | event_role | smile | agent | woman |  | event_role:smile:agent:woman | True | medium |
| cf22 | action_event | speak |  |  | communication_action, visual_action | action_event:speak | True | medium |
| cf23 | event_role | speak | agent | woman |  | event_role:speak:agent:woman | True | medium |
| cf24 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf25 | event_role | hold | agent | people |  | event_role:hold:agent:people | True | medium |
| cf26 | event_role | hold | patient | microphone |  | event_role:hold:patient:microphone | True | medium |
| cf27 | action_event | listen |  |  | visual_action | action_event:listen | True | low |
| cf28 | event_role | listen | agent | people |  | event_role:listen:agent:people | True | medium |
| cf29 | action_event | capture |  |  | visual_action | action_event:capture | True | low |
| cf30 | event_role | capture | agent | operator |  | event_role:capture:agent:operator | True | medium |
| cf31 | event_role | capture | patient | event |  | event_role:capture:patient:event | True | medium |
| cf32 | relation | people | on | stage | spatial_support, visual_relation | relation:people:on:stage | True | high |
| cf33 | relation | people | in | gymnasium | spatial_containment, visual_relation | relation:people:in:gymnasium | True | high |
| cf34 | relation | gymnasium | with | wall | association_relation, visual_relation | relation:gymnasium:with:wall | True | high |
| cf35 | relation | woman | in | hoodie | spatial_containment, visual_relation | relation:woman:in:hoodie | True | high |
| cf36 | relation | woman | in | boot | spatial_containment, visual_relation | relation:woman:in:boot | True | high |
| cf37 | relation | operator | on | left | spatial_support, visual_relation | relation:operator:on:left | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| conj_agent_reference_target_inherited | m22 |  |  | eref_m17 |  | {"action_mention_id": "m22", "canonical_target": "eref_m17", "kind": "conj_agent_reference_target_inherited", "source_action_mention_id": "m21"} |

## 22

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `159bd94dc5d6e11d8345643f4271808cfc207e7c586955c03e684e1508e04814`
**parse_path:** `sentence`

> A group of students and adults stand together indoors, posing in front of a blue banner with an emblem.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | group | group | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | students | student | noun_chunk_root | chunk1 | 3 | high |
| m2 | object | adults | adult | noun_chunk_root | chunk2 | 5 | high |
| m3 | object | banner | banner | noun_chunk_root | chunk4 | 16 | high |
| m4 | attribute | blue | blue | color_attribute | chunk4 | 15 | high |
| m5 | object | emblem | emblem | noun_chunk_root | chunk5 | 19 | high |
| m6 | context | indoors | indoors | scene_context | doc | 8 | high |
| m7 | action | stand | stand | verb_predicate | doc | 6 | high |
| m8 | action | posing | pose | verb_predicate | doc | 10 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m3 | m4 | high | chunk4 amod -> banner |
| e1 | has_context | scene | m6 | high | scene_context token indoors |
| e2 | agent | m7 | m0 | medium | nsubj -> stand |
| e3 | agent | m8 | m0 | medium | inherited agent advcl -> stand |
| e4 | relation | m0 | m1 | medium | of |
| e5 | relation | m0 | m2 | medium | of |
| e6 | relation | m0 | m3 | high | in_front_of |
| e7 | relation | m3 | m5 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | group | group | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:group", "parents": []} |
| ent_m1 | object | student | students | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:student", "parents": []} |
| ent_m2 | object | adult | adults | person | raw_lemma | stage9_seed:parent_seed | person, human | m2 | raw_mention |  |  |  | True | {"canonical": "entity:adult", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m3 | object | banner | banner | object | raw_lemma | stage9_seed:parent_seed | text_carrier, artifact | m3 | raw_mention |  |  |  | True | {"canonical": "entity:banner", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m5 | object | emblem | emblem | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:emblem", "parents": []} |
| ent_m6 | context | indoors | indoors | object | raw_lemma | stage9_seed:parent_seed | scene_context | m6 | raw_mention |  |  |  | True | {"canonical": "entity:indoors", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m8 | posing | pose | pose | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:pose", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e2 | nsubj -> stand |  |  |
| ce1 | pose | agent | agent | none | m0 | ent_m0 | medium | e3 | inherited agent advcl -> stand |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e4 | False | False |  |  |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e5 | False | False |  |  |
| cr2 | m0 | m3 | ent_m0 | ent_m3 | in_front_of | in_front_of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e6 | False | False |  |  |
| cr3 | m3 | m5 | ent_m3 | ent_m5 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | group |  |  |  | entity_exists:group | True | low |
| cf1 | entity_exists | student |  |  |  | entity_exists:student | True | low |
| cf2 | entity_exists | adult |  |  | person, human | entity_exists:adult | True | high |
| cf3 | entity_exists | banner |  |  | text_carrier, artifact | entity_exists:banner | True | high |
| cf4 | entity_exists | emblem |  |  |  | entity_exists:emblem | True | low |
| cf5 | entity_exists | indoors |  |  | scene_context | entity_exists:indoors | True | high |
| cf6 | has_attribute | banner | blue |  | color_attribute, color, visual_attribute | has_attribute:banner:blue | True | high |
| cf7 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf8 | event_role | stand | agent | group |  | event_role:stand:agent:group | True | medium |
| cf9 | action_event | pose |  |  | body_pose_action, visual_action | action_event:pose | True | high |
| cf10 | event_role | pose | agent | group |  | event_role:pose:agent:group | True | medium |
| cf11 | relation | group | of | student | part_relation, visual_relation | relation:group:of:student | True | medium |
| cf12 | relation | group | of | adult | part_relation, visual_relation | relation:group:of:adult | True | medium |
| cf13 | relation | group | in_front_of | banner | spatial_depth, visual_relation | relation:group:in_front_of:banner | True | high |
| cf14 | relation | banner | with | emblem | association_relation, visual_relation | relation:banner:with:emblem | True | high |

### Stage 9 Canonicalization Notes
_none_

## 23

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `15a42c4ee7b0a52728f5e40b8e8ad1083926a7a4ed8dd1b7adb2241fb4a65814`
**parse_path:** `sentence`

> Three men stand together, looking at a magazine or brochure. One man holds it open while the others examine it.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | men | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Three | three | exact_quantity | chunk0 | 0 | high |
| m2 | object | magazine | magazine | noun_chunk_root | chunk1 | 8 | high |
| m3 | object | brochure | brochure | noun_chunk_root | chunk2 | 10 | high |
| m4 | object | man | man | noun_chunk_root | chunk3 | 13 | high |
| m5 | quantity | One | one | exact_quantity | chunk3 | 12 | high |
| m6 | reference | others | other | contrastive_reference | nominal_reference | 19 | high |
| m7 | action | stand | stand | verb_predicate | doc | 2 | high |
| m8 | action | looking | look | verb_predicate | doc | 5 | high |
| m9 | action | holds | hold | verb_predicate | doc | 14 | high |
| m10 | action | examine | examine | verb_predicate | doc | 20 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> men |
| e1 | has_quantity | m4 | m5 | high | chunk3 quantity -> man |
| e2 | refers_to | m6 | m0 | high | contrastive_reference others -> men; score=110; margin=22 |
| e3 | agent | m7 | m0 | medium | nsubj -> stand |
| e4 | agent | m8 | m0 | medium | inherited agent advcl -> stand |
| e5 | agent | m9 | m4 | medium | nsubj -> holds |
| e6 | patient | m9 | m0 | medium | dobj -> holds; resolved it -> men |
| e7 | agent | m10 | m0 | medium | nsubj -> examine; resolved others -> men |
| e8 | patient | m10 | m4 | medium | dobj -> examine; resolved it -> man |
| e9 | relation | m0 | m2 | medium | at |
| e10 | relation | m0 | m3 | medium | at |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | men | person | stage9_seed:synonym_seed | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | magazine | magazine | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:magazine", "parents": []} |
| ent_m3 | object | brochure | brochure | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:brochure", "parents": []} |
| ent_m4 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m4 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| eref_m6 | complement_subset | man | others | person | raw_lemma | stage9_seed:parent_seed | person, human | m6 | stage9_reference | ent_m0 |  | many | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m6 | eref_m6 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m8 | looking | look | look | raw_action | stage9_seed:parent_seed | gaze_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:look", "parents": ["action_parent:gaze_action", "action_parent:visual_action"]} |  |
| ce2 | m9 | holds | hold | hold | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action |  | agent:m4->ent_m4; patient:m0->ent_m0 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce3 | m10 | examine | examine | examine | raw_action | visual_action_fallback | visual_action |  | agent:m0->eref_m6; patient:m4->ent_m4 | {"canonical": "action:examine", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e3 | nsubj -> stand |  |  |
| ce1 | look | agent | agent | none | m0 | ent_m0 | medium | e4 | inherited agent advcl -> stand |  |  |
| ce2 | hold | agent | agent | none | m4 | ent_m4 | medium | e5 | nsubj -> holds |  |  |
| ce2 | hold | patient | patient | none | m0 | ent_m0 | medium | e6 | dobj -> holds; resolved it -> men |  |  |
| ce3 | examine | agent | agent | none | m0 | eref_m6 | medium | e7 | nsubj -> examine; resolved others -> men |  |  |
| ce3 | examine | patient | patient | none | m4 | ent_m4 | medium | e8 | dobj -> examine; resolved it -> man |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e9 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e10 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | magazine |  |  |  | entity_exists:magazine | True | low |
| cf2 | entity_exists | brochure |  |  |  | entity_exists:brochure | True | low |
| cf3 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf4 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf5 | has_quantity | man | three |  | exact_quantity, quantity | has_quantity:man:three | True | high |
| cf6 | has_quantity | man | one |  | exact_quantity, quantity | has_quantity:man:one | True | high |
| cf7 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf8 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf9 | action_event | look |  |  | gaze_action, visual_action | action_event:look | True | high |
| cf10 | event_role | look | agent | man |  | event_role:look:agent:man | True | medium |
| cf11 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf12 | event_role | hold | agent | man |  | event_role:hold:agent:man | True | medium |
| cf13 | event_role | hold | patient | man |  | event_role:hold:patient:man | True | medium |
| cf14 | action_event | examine |  |  | visual_action | action_event:examine | True | low |
| cf15 | event_role | examine | agent | man |  | event_role:examine:agent:man | True | medium |
| cf16 | event_role | examine | patient | man |  | event_role:examine:patient:man | True | medium |
| cf17 | relation | man | at | magazine | spatial_location, visual_relation | relation:man:at:magazine | True | medium |
| cf18 | relation | man | at | brochure | spatial_location, visual_relation | relation:man:at:brochure | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 24

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `15ca060b0e27d9711e27e5524da5e7bafe861a413e963822c6ef8acd0a319014`
**parse_path:** `sentence`

> A person in a cap and orange shirt draws back a bow, aiming at a colorful target on a grassy field.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | cap | cap | noun_chunk_root | chunk1 | 4 | high |
| m2 | object | shirt | shirt | noun_chunk_root | chunk2 | 7 | high |
| m3 | attribute | orange | orange | color_attribute | chunk2 | 6 | high |
| m4 | object | bow | bow | noun_chunk_root | chunk3 | 11 | high |
| m5 | object | target | target | noun_chunk_root | chunk4 | 17 | high |
| m6 | attribute | colorful | colorful | modifier_attribute | chunk4 | 16 | medium |
| m7 | object | field | field | noun_chunk_root | chunk5 | 21 | high |
| m8 | attribute | grassy | grassy | modifier_attribute | chunk5 | 20 | medium |
| m9 | action | draws | draw | verb_predicate | doc | 8 | high |
| m10 | action | aiming | aim | verb_predicate | doc | 13 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | chunk2 amod -> shirt |
| e1 | has_attribute | m5 | m6 | medium | chunk4 amod -> target |
| e2 | has_attribute | m7 | m8 | medium | chunk5 amod -> field |
| e3 | agent | m9 | m0 | medium | nsubj -> draws |
| e4 | patient | m9 | m4 | medium | dobj -> draws |
| e5 | agent | m10 | m0 | medium | inherited agent advcl -> draws |
| e6 | relation | m0 | m1 | high | in |
| e7 | relation | m0 | m2 | high | in |
| e8 | relation | m0 | m5 | medium | at |
| e9 | relation | m0 | m7 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | cap | cap | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:cap", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m2 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m4 | object | bow | bow | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:bow", "parents": []} |
| ent_m5 | object | target | target | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:target", "parents": []} |
| ent_m7 | object | field | field | object | raw_lemma | wordnet_synset:field.n.01 + stage9_audit | outdoor_scene, place | m7 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": ["entity_parent:outdoor_scene", "entity_parent:place"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | draws | draw | draw | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m4->ent_m4 | {"canonical": "action:draw", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m10 | aiming | aim | aim | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:aim", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | draw | agent | agent | none | m0 | ent_m0 | medium | e3 | nsubj -> draws |  |  |
| ce0 | draw | patient | patient | none | m4 | ent_m4 | medium | e4 | dobj -> draws |  |  |
| ce1 | aim | agent | agent | none | m0 | ent_m0 | medium | e5 | inherited agent advcl -> draws |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e6 | False | False |  |  |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e7 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e8 | False | False |  |  |
| cr3 | m0 | m7 | ent_m0 | ent_m7 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf1 | entity_exists | cap |  |  | clothing, wearable | entity_exists:cap | True | high |
| cf2 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf3 | entity_exists | bow |  |  |  | entity_exists:bow | True | low |
| cf4 | entity_exists | target |  |  |  | entity_exists:target | True | low |
| cf5 | entity_exists | field |  |  | outdoor_scene, place | entity_exists:field | True | medium |
| cf6 | has_attribute | shirt | orange |  | color_attribute, color, visual_attribute | has_attribute:shirt:orange | True | high |
| cf7 | has_attribute | target | colorful |  | color_attribute, color_quantity, visual_attribute | has_attribute:target:colorful | True | medium |
| cf8 | has_attribute | field | grassy |  | modifier_attribute, visual_attribute | has_attribute:field:grassy | True | medium |
| cf9 | action_event | draw |  |  | visual_action | action_event:draw | True | low |
| cf10 | event_role | draw | agent | person |  | event_role:draw:agent:person | True | medium |
| cf11 | event_role | draw | patient | bow |  | event_role:draw:patient:bow | True | medium |
| cf12 | action_event | aim |  |  | visual_action | action_event:aim | True | low |
| cf13 | event_role | aim | agent | person |  | event_role:aim:agent:person | True | medium |
| cf14 | relation | person | in | cap | spatial_containment, visual_relation | relation:person:in:cap | True | high |
| cf15 | relation | person | in | shirt | spatial_containment, visual_relation | relation:person:in:shirt | True | high |
| cf16 | relation | person | at | target | spatial_location, visual_relation | relation:person:at:target | True | medium |
| cf17 | relation | person | on | field | spatial_support, visual_relation | relation:person:on:field | True | high |

### Stage 9 Canonicalization Notes
_none_

## 25

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `1791e009c374d7e8a74739cb5b128938d5d60960c3fb6083b5cf41fd806fc814`
**parse_path:** `sentence`

> Tall palm trees stand in front of a modern building with a reflective glass facade. The building mirrors the trees and sky, while a dark car is parked nearby on a paved area. A signpost is visible to the left, and bushes surround the base of the trees.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | palm trees | palm_tree | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | building | building | noun_chunk_root | chunk2 | 8 | high |
| m2 | attribute | modern | modern | modifier_attribute | chunk2 | 7 | medium |
| m3 | object | facade | facade | noun_chunk_root | chunk3 | 13 | high |
| m4 | attribute | reflective | reflective | modifier_attribute | chunk3 | 11 | medium |
| m5 | attribute | glass | glass | material_attribute | chunk3 | 12 | high |
| m6 | object | building | building | noun_chunk_root | chunk4 | 16 | high |
| m7 | object | trees | tree | noun_chunk_root | chunk5 | 19 | high |
| m8 | object | sky | sky | noun_chunk_root | chunk6 | 21 | high |
| m9 | object | car | car | noun_chunk_root | chunk7 | 26 | high |
| m10 | attribute | dark | dark | visual_attribute | chunk7 | 25 | medium |
| m11 | object | area | area | noun_chunk_root | chunk8 | 33 | high |
| m12 | attribute | paved | paved | visual_attribute | chunk8 | 32 | medium |
| m13 | object | signpost | signpost | noun_chunk_root | chunk9 | 36 | high |
| m14 | context | left | left | spatial_region | chunk10 | 41 | medium |
| m15 | object | bushes | bush | noun_chunk_root | chunk11 | 44 | high |
| m16 | object | trees | tree | noun_chunk_root | chunk13 | 50 | high |
| m17 | action | stand | stand | verb_predicate | doc | 2 | high |
| m18 | action | mirrors | mirror | verb_predicate | doc | 17 | high |
| m19 | action | parked | park | verb_predicate | doc | 28 | high |
| m20 | action | surround | surround | verb_predicate | doc | 45 | high |
| m21 | object | base | base | verb_object | doc | 47 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk2 amod -> building |
| e1 | has_attribute | m3 | m4 | medium | chunk3 amod -> facade |
| e2 | has_attribute | m3 | m5 | high | chunk3 compound -> facade |
| e3 | has_attribute | m9 | m10 | medium | chunk7 amod -> car |
| e4 | has_attribute | m11 | m12 | medium | chunk8 amod -> area |
| e5 | agent | m17 | m0 | medium | nsubj -> stand |
| e6 | agent | m18 | m6 | medium | nsubj -> mirrors |
| e7 | patient | m18 | m7 | medium | dobj -> mirrors |
| e8 | patient | m18 | m8 | medium | dobj -> mirrors |
| e9 | agent | m19 | m9 | medium | nsubjpass -> parked |
| e10 | agent | m20 | m15 | medium | nsubj -> surround |
| e11 | patient | m20 | m21 | medium | dobj -> surround |
| e12 | relation | m0 | m1 | high | in_front_of |
| e13 | relation | m1 | m3 | high | with |
| e14 | relation | m9 | m11 | high | on |
| e15 | relation | m15 | m16 | medium | base_of |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | palm_tree | palm trees | object | openimages_boxable\|visual_genome_object_synset\|wordnet_noun_mwe | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:palm_tree", "parents": []} |
| ent_m1 | object | building | building | object | raw_lemma | wordnet_synset:building.n.01 + stage9_audit | structure, artifact | m1 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m3 | object | facade | facade | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:facade", "parents": []} |
| ent_m6 | object | building | building | object | raw_lemma | wordnet_synset:building.n.01 + stage9_audit | structure, artifact | m6 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m7 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m7 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m8 | object | sky | sky | object | raw_lemma | wordnet_synset:sky.n.01 + stage9_audit | natural_scene | m8 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": ["entity_parent:natural_scene"]} |
| ent_m9 | object | car | car | vehicle | raw_lemma | stage9_seed:parent_seed | vehicle | m9 | raw_mention |  |  |  | True | {"canonical": "entity:car", "parents": ["entity_parent:vehicle"]} |
| ent_m11 | object | area | area | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:area", "parents": []} |
| ent_m13 | object | signpost | signpost | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:signpost", "parents": []} |
| ent_m14 | context | left | left | object | raw_lemma | semantic_type_fallback | scene_context | m14 | raw_mention |  |  |  | True | {"canonical": "entity:left", "parents": ["entity_parent:scene_context"]} |
| ent_m15 | object | bush | bushes | object | raw_lemma | wordnet_synset:shrub.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m15 | raw_mention |  |  |  | True | {"canonical": "entity:bush", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m16 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m16 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m21 | object | base | base | object | raw_lemma | none |  | m21 | raw_mention |  |  |  | True | {"canonical": "entity:base", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m18 | mirrors | mirror | mirror | raw_action | visual_action_fallback | visual_action |  | agent:m6->ent_m6; patient:m7->ent_m7; patient:m8->ent_m8 | {"canonical": "action:mirror", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m19 | parked | park | park | raw_action | visual_action_fallback | visual_action |  | patient<-theme[passive_to_active]:m9->ent_m9 | {"canonical": "action:park", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m20 | surround | surround | surround | raw_action | wordnet_synset:surround.v.01 + stage9_audit | spatial_configuration_action, visual_action |  | agent:m15->ent_m15; patient:m21->ent_m21 | {"canonical": "action:surround", "parents": ["action_parent:spatial_configuration_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e5 | nsubj -> stand |  |  |
| ce1 | mirror | agent | agent | none | m6 | ent_m6 | medium | e6 | nsubj -> mirrors |  |  |
| ce1 | mirror | patient | patient | none | m7 | ent_m7 | medium | e7 | dobj -> mirrors |  |  |
| ce1 | mirror | patient | patient | none | m8 | ent_m8 | medium | e8 | dobj -> mirrors |  |  |
| ce2 | park | patient | theme | passive_to_active | m9 | ent_m9 | medium | e9 | nsubjpass -> parked |  |  |
| ce3 | surround | agent | agent | none | m15 | ent_m15 | medium | e10 | nsubj -> surround |  |  |
| ce3 | surround | patient | patient | none | m21 | ent_m21 | medium | e11 | dobj -> surround |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in_front_of | in_front_of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e12 | False | False |  |  |
| cr1 | m1 | m3 | ent_m1 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr2 | m9 | m11 | ent_m9 | ent_m11 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e14 | False | False |  |  |
| cr3 | m15 | m16 | ent_m15 | ent_m16 | base_of | base_of | generated_region_pattern | generated_region_pattern | spatial_region, visual_relation | medium | e15 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | palm_tree |  |  |  | entity_exists:palm_tree | True | high |
| cf1 | entity_exists | building |  |  | structure, artifact | entity_exists:building | True | high |
| cf2 | entity_exists | facade |  |  |  | entity_exists:facade | True | low |
| cf3 | entity_exists | building |  |  | structure, artifact | entity_exists:building | True | high |
| cf4 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf5 | entity_exists | sky |  |  | natural_scene | entity_exists:sky | True | high |
| cf6 | entity_exists | car |  |  | vehicle | entity_exists:car | True | high |
| cf7 | entity_exists | area |  |  |  | entity_exists:area | True | low |
| cf8 | entity_exists | signpost |  |  |  | entity_exists:signpost | True | low |
| cf9 | entity_exists | left |  |  | scene_context | entity_exists:left | True | medium |
| cf10 | entity_exists | bush |  |  | plant, living_thing | entity_exists:bush | True | high |
| cf11 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf12 | entity_exists | base |  |  |  | entity_exists:base | True | low |
| cf13 | has_attribute | building | modern |  | modifier_attribute, visual_attribute | has_attribute:building:modern | True | medium |
| cf14 | has_attribute | facade | reflective |  | modifier_attribute, visual_attribute | has_attribute:facade:reflective | True | medium |
| cf15 | has_attribute | facade | glass |  | material_attribute, material, visual_attribute | has_attribute:facade:glass | True | high |
| cf16 | has_attribute | car | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:car:dark | True | medium |
| cf17 | has_attribute | area | paved |  | visual_attribute | has_attribute:area:paved | True | medium |
| cf18 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf19 | event_role | stand | agent | palm_tree |  | event_role:stand:agent:palm_tree | True | medium |
| cf20 | action_event | mirror |  |  | visual_action | action_event:mirror | True | low |
| cf21 | event_role | mirror | agent | building |  | event_role:mirror:agent:building | True | medium |
| cf22 | event_role | mirror | patient | tree |  | event_role:mirror:patient:tree | True | medium |
| cf23 | event_role | mirror | patient | sky |  | event_role:mirror:patient:sky | True | medium |
| cf24 | action_event | park |  |  | visual_action | action_event:park | True | low |
| cf25 | event_role | park | patient | car |  | event_role:park:patient:car | True | medium |
| cf26 | action_event | surround |  |  | spatial_configuration_action, visual_action | action_event:surround | True | high |
| cf27 | event_role | surround | agent | bush |  | event_role:surround:agent:bush | True | medium |
| cf28 | event_role | surround | patient | base |  | event_role:surround:patient:base | True | medium |
| cf29 | relation | palm_tree | in_front_of | building | spatial_depth, visual_relation | relation:palm_tree:in_front_of:building | True | high |
| cf30 | relation | building | with | facade | association_relation, visual_relation | relation:building:with:facade | True | high |
| cf31 | relation | car | on | area | spatial_support, visual_relation | relation:car:on:area | True | high |
| cf32 | relation | bush | base_of | tree | spatial_region, visual_relation | relation:bush:base_of:tree | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m19 | e9 | m9 |  |  | {"action_mention_id": "m19", "kind": "passive_subject_to_patient", "raw_edge_id": "e9", "raw_role": "theme", "role": "patient", "target": "m9", "voice_normalization": "passive_to_active"} |

## 26

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `17e88176c77a1d42188f780c829666c61786c47359b5abb00e0ac0591fe68c14`
**parse_path:** `tag_list`

> moon, bridge, water, lights, night

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | moon | moon | segment_head | t0 | 0 | high |
| m1 | object | bridge | bridge | segment_head | t1 | 0 | high |
| m2 | object | water | water | segment_head | t2 | 0 | high |
| m3 | object | lights | light | segment_head | t3 | 0 | high |
| m4 | context | night | night | scene_context | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_context | scene | m4 | high | t4 context tag |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | moon | moon | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:moon", "parents": []} |
| ent_m1 | object | bridge | bridge | object | raw_lemma | wordnet_synset:bridge.n.01 + stage9_audit | structure, artifact | m1 | raw_mention |  |  |  | True | {"canonical": "entity:bridge", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m2 | object | water | water | object | raw_lemma | wordnet_synset:water.n.01 + stage9_audit | natural_element | m2 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": ["entity_parent:natural_element"]} |
| ent_m3 | object | light | lights | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:light", "parents": []} |
| ent_m4 | context | night | night | object | raw_lemma | stage9_seed:parent_seed | scene_context, time_context | m4 | raw_mention |  |  |  | True | {"canonical": "entity:night", "parents": ["entity_parent:scene_context", "entity_parent:time_context"]} |

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
| cf0 | entity_exists | moon |  |  |  | entity_exists:moon | True | low |
| cf1 | entity_exists | bridge |  |  | structure, artifact | entity_exists:bridge | True | high |
| cf2 | entity_exists | water |  |  | natural_element | entity_exists:water | True | high |
| cf3 | entity_exists | light |  |  |  | entity_exists:light | True | low |
| cf4 | entity_exists | night |  |  | scene_context, time_context | entity_exists:night | True | high |

### Stage 9 Canonicalization Notes
_none_

## 27

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `18f4deca4ee00a8458b66afa0497996842995180e1e11385ae172c0c0c411c14`
**parse_path:** `sentence`

> A large artillery piece sits in a war-torn field with sandbags nearby. Bare trees and damaged buildings are visible in the background, with several figures standing far off in the distance. The scene is set outdoors in a ruined landscape.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | piece | piece | noun_chunk_root | chunk0 | 3 | high |
| m1 | attribute | large | large | size_attribute | chunk0 | 1 | high |
| m2 | attribute | artillery | artillery | compound_modifier | chunk0 | 2 | medium |
| m3 | object | field | field | noun_chunk_root | chunk1 | 8 | high |
| m4 | attribute | war-torn | war-torn | modifier_attribute | chunk1 | 7 | medium |
| m5 | object | sandbags | sandbag | noun_chunk_root | chunk2 | 10 | high |
| m6 | object | trees | tree | noun_chunk_root | chunk3 | 14 | high |
| m7 | attribute | Bare | bare | visual_attribute | chunk3 | 13 | medium |
| m8 | object | buildings | building | noun_chunk_root | chunk4 | 17 | high |
| m9 | attribute | damaged | damage | state_attribute | chunk4 | 16 | medium |
| m10 | context | background | background | scene_context | chunk5 | 22 | high |
| m11 | object | figures | figure | noun_chunk_root | chunk6 | 26 | high |
| m12 | quantity | several | several | approximate_quantity | chunk6 | 25 | medium |
| m13 | context | distance | distance | scene_context | chunk7 | 32 | high |
| m14 | object | scene | scene | noun_chunk_root | chunk8 | 35 | high |
| m15 | object | landscape | landscape | noun_chunk_root | chunk9 | 42 | high |
| m16 | attribute | ruined | ruined | modifier_attribute | chunk9 | 41 | medium |
| m17 | context | outdoors | outdoors | scene_context | doc | 38 | high |
| m18 | action | sits | sit | verb_predicate | doc | 4 | high |
| m19 | action | standing | stand | verb_predicate | doc | 27 | high |
| m20 | action | set | set | verb_predicate | doc | 37 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> piece |
| e1 | has_attribute | m0 | m2 | medium | chunk0 compound -> piece |
| e2 | has_attribute | m3 | m4 | medium | chunk1 amod -> field |
| e3 | has_attribute | m6 | m7 | medium | chunk3 amod -> trees |
| e4 | has_attribute | m8 | m9 | medium | chunk4 amod -> buildings |
| e5 | has_context | scene | m10 | high | scene_context token background |
| e6 | has_quantity | m11 | m12 | medium | chunk6 quantity -> figures |
| e7 | has_context | scene | m13 | high | scene_context token distance |
| e8 | has_attribute | m15 | m16 | medium | chunk9 amod -> landscape |
| e9 | has_context | scene | m17 | high | scene_context token outdoors |
| e10 | agent | m18 | m0 | medium | nsubj -> sits |
| e11 | agent | m19 | m11 | medium | nsubj -> standing |
| e12 | agent | m20 | m14 | medium | nsubjpass -> set |
| e13 | relation | m0 | m3 | high | in |
| e14 | relation | m0 | m5 | high | with |
| e15 | relation | m6 | m10 | high | in |
| e16 | relation | m14 | m15 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | piece | piece | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:piece", "parents": []} |
| ent_m3 | object | field | field | object | raw_lemma | wordnet_synset:field.n.01 + stage9_audit | outdoor_scene, place | m3 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": ["entity_parent:outdoor_scene", "entity_parent:place"]} |
| ent_m5 | object | sandbag | sandbags | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:sandbag", "parents": []} |
| ent_m6 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m6 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m8 | object | building | buildings | object | raw_lemma | wordnet_synset:building.n.01 + stage9_audit | structure, artifact | m8 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m10 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m10 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m11 | object | figure | figures | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:figure", "parents": []} |
| ent_m13 | context | distance | distance | object | raw_lemma | stage9_seed:parent_seed | scene_context, spatial_context | m13 | raw_mention |  |  |  | True | {"canonical": "entity:distance", "parents": ["entity_parent:scene_context", "entity_parent:spatial_context"]} |
| ent_m14 | object | scene | scene | object | raw_lemma | stage9_seed:parent_seed | scene_context | m14 | raw_mention |  |  |  | True | {"canonical": "entity:scene", "parents": ["entity_parent:scene_context"]} |
| ent_m15 | object | landscape | landscape | object | raw_lemma | none |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:landscape", "parents": []} |
| ent_m17 | context | outdoors | outdoors | object | raw_lemma | stage9_seed:parent_seed | scene_context | m17 | raw_mention |  |  |  | True | {"canonical": "entity:outdoors", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | sits | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m19 | standing | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m11->ent_m11 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce2 | m20 | set | set | set | raw_action | visual_action_fallback | visual_action |  | patient<-theme[passive_to_active]:m14->ent_m14 | {"canonical": "action:set", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | agent | none | m0 | ent_m0 | medium | e10 | nsubj -> sits |  |  |
| ce1 | stand | agent | agent | none | m11 | ent_m11 | medium | e11 | nsubj -> standing |  |  |
| ce2 | set | patient | theme | passive_to_active | m14 | ent_m14 | medium | e12 | nsubjpass -> set |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e13 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr2 | m6 | m10 | ent_m6 | ent_m10 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e15 | False | False |  |  |
| cr3 | m14 | m15 | ent_m14 | ent_m15 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | piece |  |  |  | entity_exists:piece | True | low |
| cf1 | entity_exists | field |  |  | outdoor_scene, place | entity_exists:field | True | medium |
| cf2 | entity_exists | sandbag |  |  |  | entity_exists:sandbag | True | low |
| cf3 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf4 | entity_exists | building |  |  | structure, artifact | entity_exists:building | True | high |
| cf5 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf6 | entity_exists | figure |  |  |  | entity_exists:figure | True | low |
| cf7 | entity_exists | distance |  |  | scene_context, spatial_context | entity_exists:distance | True | high |
| cf8 | entity_exists | scene |  |  | scene_context | entity_exists:scene | True | high |
| cf9 | entity_exists | landscape |  |  |  | entity_exists:landscape | True | low |
| cf10 | entity_exists | outdoors |  |  | scene_context | entity_exists:outdoors | True | high |
| cf11 | has_attribute | piece | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:piece:large | True | high |
| cf12 | has_attribute | piece | artillery |  | compound_modifier, visual_attribute | has_attribute:piece:artillery | True | medium |
| cf13 | has_attribute | field | war-torn |  | modifier_attribute, visual_attribute | has_attribute:field:war-torn | True | medium |
| cf14 | has_attribute | tree | bare |  | visual_attribute | has_attribute:tree:bare | True | medium |
| cf15 | has_attribute | building | damage |  | state_attribute, visual_attribute | has_attribute:building:damage | True | medium |
| cf16 | has_quantity | figure | several |  | approximate_quantity, quantity | has_quantity:figure:several | True | medium |
| cf17 | has_attribute | landscape | ruined |  | state_attribute, state, visual_attribute | has_attribute:landscape:ruined | True | medium |
| cf18 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf19 | event_role | sit | agent | piece |  | event_role:sit:agent:piece | True | medium |
| cf20 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf21 | event_role | stand | agent | figure |  | event_role:stand:agent:figure | True | medium |
| cf22 | action_event | set |  |  | visual_action | action_event:set | True | low |
| cf23 | event_role | set | patient | scene |  | event_role:set:patient:scene | True | medium |
| cf24 | relation | piece | in | field | spatial_containment, visual_relation | relation:piece:in:field | True | high |
| cf25 | relation | piece | with | sandbag | association_relation, visual_relation | relation:piece:with:sandbag | True | high |
| cf26 | relation | tree | in | background | spatial_containment, visual_relation | relation:tree:in:background | True | high |
| cf27 | relation | scene | in | landscape | spatial_containment, visual_relation | relation:scene:in:landscape | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m20 | e12 | m14 |  |  | {"action_mention_id": "m20", "kind": "passive_subject_to_patient", "raw_edge_id": "e12", "raw_role": "theme", "role": "patient", "target": "m14", "voice_normalization": "passive_to_active"} |

## 28

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `1b035d43d40c47a816338cf94ea819e4acee96b6d097a664acac2dd203583c14`
**parse_path:** `sentence`

> Tall buildings line a city street, with the Chrysler Building towering in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | buildings | building | noun_chunk_root | chunk0 | 1 | high |
| m1 | attribute | Tall | tall | size_attribute | chunk0 | 0 | high |
| m2 | object | street | street | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | city | city | compound_modifier | chunk1 | 4 | medium |
| m4 | object | Building | building | noun_chunk_root | chunk2 | 10 | high |
| m5 | attribute | Chrysler | chrysler | compound_modifier | chunk2 | 9 | medium |
| m6 | context | background | background | scene_context | chunk3 | 14 | high |
| m7 | action | line | line | verb_predicate | doc | 2 | high |
| m8 | action | towering | tower | verb_predicate | doc | 11 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> buildings |
| e1 | has_attribute | m2 | m3 | medium | chunk1 compound -> street |
| e2 | has_attribute | m4 | m5 | medium | chunk2 compound -> Building |
| e3 | has_context | scene | m6 | high | scene_context token background |
| e4 | agent | m7 | m0 | medium | nsubj -> line |
| e5 | patient | m7 | m2 | medium | dobj -> line |
| e6 | agent | m8 | m4 | medium | nsubj -> towering |
| e7 | relation | m4 | m6 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | buildings | object | raw_lemma | wordnet_synset:building.n.01 + stage9_audit | structure, artifact | m0 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m2 | object | street | street | object | raw_lemma | wordnet_synset:street.n.01 + stage9_audit | path, place | m2 | raw_mention |  |  |  | True | {"canonical": "entity:street", "parents": ["entity_parent:path", "entity_parent:place"]} |
| ent_m4 | object | building | Building | object | raw_lemma | wordnet_synset:building.n.01 + stage9_audit | structure, artifact | m4 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m6 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m6 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | line | line | line | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m2->ent_m2 | {"canonical": "action:line", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m8 | towering | tower | tower | raw_action | visual_action_fallback | visual_action |  | agent:m4->ent_m4 | {"canonical": "action:tower", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | line | agent | agent | none | m0 | ent_m0 | medium | e4 | nsubj -> line |  |  |
| ce0 | line | patient | patient | none | m2 | ent_m2 | medium | e5 | dobj -> line |  |  |
| ce1 | tower | agent | agent | none | m4 | ent_m4 | medium | e6 | nsubj -> towering |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m4 | m6 | ent_m4 | ent_m6 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | building |  |  | structure, artifact | entity_exists:building | True | high |
| cf1 | entity_exists | street |  |  | path, place | entity_exists:street | True | high |
| cf2 | entity_exists | building |  |  | structure, artifact | entity_exists:building | True | high |
| cf3 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf4 | has_attribute | building | tall |  | size_attribute, height, visual_attribute | has_attribute:building:tall | True | high |
| cf5 | has_attribute | street | city |  | compound_modifier, visual_attribute | has_attribute:street:city | True | medium |
| cf6 | has_attribute | building | chrysler |  | compound_modifier, visual_attribute | has_attribute:building:chrysler | True | medium |
| cf7 | action_event | line |  |  | visual_action | action_event:line | True | low |
| cf8 | event_role | line | agent | building |  | event_role:line:agent:building | True | medium |
| cf9 | event_role | line | patient | street |  | event_role:line:patient:street | True | medium |
| cf10 | action_event | tower |  |  | visual_action | action_event:tower | True | low |
| cf11 | event_role | tower | agent | building |  | event_role:tower:agent:building | True | medium |
| cf12 | relation | building | in | background | spatial_containment, visual_relation | relation:building:in:background | True | high |

### Stage 9 Canonicalization Notes
_none_

## 29

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `1b0acd33c3d9b0d42ae8e6ceba63add1710ed4f650c85e1928a6ebae029e2014`
**parse_path:** `sentence`

> Two people sit at a white table wearing 3D glasses. Shadows and light patterns are projected onto the table surface, with one person adjusting their glasses while the other looks through theirs.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Two | two | exact_quantity | chunk0 | 0 | high |
| m2 | object | table | table | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | white | white | color_attribute | chunk1 | 5 | high |
| m4 | object | glasses | glass | noun_chunk_root | chunk2 | 9 | high |
| m5 | attribute | 3D | 3d | modifier_attribute | chunk2 | 8 | medium |
| m6 | object | Shadows | shadow | noun_chunk_root | chunk3 | 11 | high |
| m7 | object | patterns | pattern | noun_chunk_root | chunk4 | 14 | high |
| m8 | attribute | light | light | visual_attribute | chunk4 | 13 | medium |
| m9 | context | surface | surface | spatial_region | chunk5 | 20 | medium |
| m10 | object | person | person | noun_chunk_root | chunk6 | 24 | high |
| m11 | quantity | one | one | exact_quantity | chunk6 | 23 | high |
| m12 | object | glasses | glass | noun_chunk_root | chunk7 | 27 | high |
| m13 | reference | other | other | contrastive_reference | nominal_reference | 30 | high |
| m14 | action | sit | sit | verb_predicate | doc | 2 | high |
| m15 | action | wearing | wear | verb_predicate | doc | 7 | high |
| m16 | action | projected | project | verb_predicate | doc | 16 | high |
| m17 | action | adjusting | adjust | verb_predicate | doc | 25 | high |
| m18 | action | looks | look | verb_predicate | doc | 31 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> people |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> table |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> glasses |
| e3 | has_attribute | m7 | m8 | medium | chunk4 compound -> patterns |
| e4 | has_quantity | m10 | m11 | high | chunk6 quantity -> person |
| e5 | refers_to | m13 | m0 | high | contrastive_reference other -> people; score=110 |
| e6 | agent | m14 | m0 | medium | nsubj -> sit |
| e7 | agent | m15 | m0 | medium | inherited agent advcl -> sit |
| e8 | patient | m15 | m4 | medium | dobj -> wearing |
| e9 | agent | m16 | m6 | medium | nsubjpass -> projected |
| e10 | agent | m16 | m7 | medium | nsubjpass -> projected |
| e11 | agent | m17 | m10 | medium | nsubj -> adjusting |
| e12 | patient | m17 | m12 | medium | dobj -> adjusting |
| e13 | agent | m18 | m0 | medium | nsubj -> looks; resolved other -> people |
| e14 | relation | m0 | m2 | medium | at |
| e15 | relation | m6 | m9 | medium | onto |
| e16 | relation | m0 | m10 | medium | through |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | table | table | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m4 | object | glass | glasses | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:glass", "parents": []} |
| ent_m6 | object | shadow | Shadows | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:shadow", "parents": []} |
| ent_m7 | object | pattern | patterns | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:pattern", "parents": []} |
| ent_m9 | context | surface | surface | object | raw_lemma | semantic_type_fallback | scene_context | m9 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": ["entity_parent:scene_context"]} |
| ent_m10 | object | person | person | person | raw_lemma | stage9_seed:parent_seed | person, human | m10 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m12 | object | glass | glasses | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:glass", "parents": []} |
| eref_m13 | contrastive_instance | people | other | person | raw_lemma | stage9_seed:parent_seed | person, human | m13 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m13 | eref_m13 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m14 | sit | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m15 | wearing | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m0->ent_m0; patient:m4->ent_m4 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce2 | m16 | projected | project | project | raw_action | visual_action_fallback | visual_action |  | patient<-theme[passive_to_active]:m6->ent_m6; patient<-theme[passive_to_active]:m7->ent_m7 | {"canonical": "action:project", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m17 | adjusting | adjust | adjust | raw_action | visual_action_fallback | visual_action |  | agent:m10->ent_m10; patient:m12->ent_m12 | {"canonical": "action:adjust", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m18 | looks | look | look | raw_action | stage9_seed:parent_seed | gaze_action, visual_action |  | agent:m0->eref_m13 | {"canonical": "action:look", "parents": ["action_parent:gaze_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | agent | none | m0 | ent_m0 | medium | e6 | nsubj -> sit |  |  |
| ce1 | wear | agent | agent | none | m0 | ent_m0 | medium | e7 | inherited agent advcl -> sit |  |  |
| ce1 | wear | patient | patient | none | m4 | ent_m4 | medium | e8 | dobj -> wearing |  |  |
| ce2 | project | patient | theme | passive_to_active | m6 | ent_m6 | medium | e9 | nsubjpass -> projected |  |  |
| ce2 | project | patient | theme | passive_to_active | m7 | ent_m7 | medium | e10 | nsubjpass -> projected |  |  |
| ce3 | adjust | agent | agent | none | m10 | ent_m10 | medium | e11 | nsubj -> adjusting |  |  |
| ce3 | adjust | patient | patient | none | m12 | ent_m12 | medium | e12 | dobj -> adjusting |  |  |
| ce4 | look | agent | agent | none | m0 | eref_m13 | medium | e13 | nsubj -> looks; resolved other -> people |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e14 | False | False |  |  |
| cr1 | m6 | m9 | ent_m6 | ent_m9 | onto | on | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | medium | e15 | False | False |  |  |
| cr2 | m0 | m10 | ent_m0 | ent_m10 | through | through | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | medium | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf2 | entity_exists | glass |  |  |  | entity_exists:glass | True | low |
| cf3 | entity_exists | shadow |  |  |  | entity_exists:shadow | True | low |
| cf4 | entity_exists | pattern |  |  |  | entity_exists:pattern | True | low |
| cf5 | entity_exists | surface |  |  | scene_context | entity_exists:surface | True | medium |
| cf6 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf7 | entity_exists | glass |  |  |  | entity_exists:glass | True | low |
| cf8 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf9 | has_quantity | people | two |  | exact_quantity, quantity | has_quantity:people:two | True | high |
| cf10 | has_attribute | table | white |  | color_attribute, color, visual_attribute | has_attribute:table:white | True | high |
| cf11 | has_attribute | glass | 3d |  | modifier_attribute, visual_attribute | has_attribute:glass:3d | True | medium |
| cf12 | has_attribute | pattern | light |  | visual_attribute | has_attribute:pattern:light | True | medium |
| cf13 | has_quantity | person | one |  | exact_quantity, quantity | has_quantity:person:one | True | high |
| cf14 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf15 | event_role | sit | agent | people |  | event_role:sit:agent:people | True | medium |
| cf16 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf17 | event_role | wear | agent | people |  | event_role:wear:agent:people | True | medium |
| cf18 | event_role | wear | patient | glass |  | event_role:wear:patient:glass | True | medium |
| cf19 | action_event | project |  |  | visual_action | action_event:project | True | low |
| cf20 | event_role | project | patient | shadow |  | event_role:project:patient:shadow | True | medium |
| cf21 | event_role | project | patient | pattern |  | event_role:project:patient:pattern | True | medium |
| cf22 | action_event | adjust |  |  | visual_action | action_event:adjust | True | low |
| cf23 | event_role | adjust | agent | person |  | event_role:adjust:agent:person | True | medium |
| cf24 | event_role | adjust | patient | glass |  | event_role:adjust:patient:glass | True | medium |
| cf25 | action_event | look |  |  | gaze_action, visual_action | action_event:look | True | high |
| cf26 | event_role | look | agent | people |  | event_role:look:agent:people | True | medium |
| cf27 | relation | people | at | table | spatial_location, visual_relation | relation:people:at:table | True | medium |
| cf28 | relation | shadow | on | surface | spatial_support, visual_relation | relation:shadow:on:surface | True | medium |
| cf29 | relation | people | through | person | spatial_path, visual_relation | relation:people:through:person | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m16 | e9 | m6 |  |  | {"action_mention_id": "m16", "kind": "passive_subject_to_patient", "raw_edge_id": "e9", "raw_role": "theme", "role": "patient", "target": "m6", "voice_normalization": "passive_to_active"} |
| passive_subject_to_patient | m16 | e10 | m7 |  |  | {"action_mention_id": "m16", "kind": "passive_subject_to_patient", "raw_edge_id": "e10", "raw_role": "theme", "role": "patient", "target": "m7", "voice_normalization": "passive_to_active"} |
| relation_lexical_canonicalized |  | e15 |  |  |  | {"canonical": "on", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e15", "raw_relation": "onto", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 30

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `1cef04e49522744d3c3608efc602acab3ad915f75efba3c32b29c2be88123c14`
**parse_path:** `sentence`

> A large, colorful world map hangs on a wall, showing continents in various hues with oceans in blue. At the top, Chinese characters read “世界地图,” and a row of small flags lines the bottom edge. A dark cord or wire rests against the lower left corner.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “世界地图,” | 世界地图, | quote_text | doc_quote | 28 | high |
| m1 | object | map | map | noun_chunk_root | chunk0 | 5 | high |
| m2 | attribute | large | large | size_attribute | chunk0 | 1 | high |
| m3 | attribute | colorful | colorful | modifier_attribute | chunk0 | 3 | medium |
| m4 | attribute | world | world | compound_modifier | chunk0 | 4 | medium |
| m5 | object | wall | wall | noun_chunk_root | chunk1 | 9 | high |
| m6 | object | continents | continent | noun_chunk_root | chunk2 | 12 | high |
| m7 | object | hues | hue | noun_chunk_root | chunk3 | 15 | high |
| m8 | quantity | various | various | approximate_quantity | chunk3 | 14 | medium |
| m9 | object | oceans | ocean | noun_chunk_root | chunk4 | 17 | high |
| m10 | attribute | blue | blue | color_attribute | chunk5 | 19 | high |
| m11 | context | top | top | spatial_region | chunk6 | 23 | medium |
| m12 | object | characters | character | noun_chunk_root | chunk7 | 26 | high |
| m13 | attribute | Chinese | chinese | modifier_attribute | chunk7 | 25 | medium |
| m14 | object | row | row | noun_chunk_root | chunk8 | 31 | high |
| m15 | object | flags | flag | noun_chunk_root | chunk9 | 34 | high |
| m16 | attribute | small | small | size_attribute | chunk9 | 33 | high |
| m17 | object | edge | edge | noun_chunk_root | chunk10 | 38 | high |
| m18 | attribute | bottom | bottom | modifier_attribute | chunk10 | 37 | medium |
| m19 | object | cord | cord | noun_chunk_root | chunk11 | 42 | high |
| m20 | attribute | dark | dark | visual_attribute | chunk11 | 41 | medium |
| m21 | object | wire | wire | noun_chunk_root | chunk12 | 44 | high |
| m22 | context | corner | corner | spatial_region | chunk13 | 50 | medium |
| m23 | action | hangs | hang | verb_predicate | doc | 6 | high |
| m24 | action | showing | show | verb_predicate | doc | 11 | high |
| m25 | action | read | read | verb_predicate | doc | 27 | high |
| m26 | action | lines | line | verb_predicate | doc | 35 | high |
| m27 | action | rests | rest | verb_predicate | doc | 45 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk0 amod -> map |
| e1 | has_attribute | m1 | m3 | medium | chunk0 amod -> map |
| e2 | has_attribute | m1 | m4 | medium | chunk0 compound -> map |
| e3 | has_quantity | m7 | m8 | medium | chunk3 quantity -> hues |
| e4 | has_attribute | m12 | m13 | medium | chunk7 amod -> characters |
| e5 | has_attribute | m15 | m16 | high | chunk9 amod -> flags |
| e6 | has_attribute | m17 | m18 | medium | chunk10 amod -> edge |
| e7 | has_attribute | m19 | m20 | medium | chunk11 amod -> cord |
| e8 | agent | m23 | m1 | medium | nsubj -> hangs |
| e9 | agent | m24 | m1 | medium | inherited agent advcl -> hangs |
| e10 | patient | m24 | m6 | medium | dobj -> showing |
| e11 | agent | m25 | m12 | medium | nsubj -> read |
| e12 | agent | m26 | m14 | medium | nsubj -> lines |
| e13 | patient | m26 | m17 | medium | dobj -> lines |
| e14 | agent | m27 | m19 | medium | nsubj -> rests |
| e15 | agent | m27 | m21 | medium | nsubj -> rests |
| e16 | relation | m1 | m5 | high | on |
| e17 | relation | m6 | m7 | high | in |
| e18 | relation | m6 | m9 | high | with |
| e19 | relation | m12 | m11 | medium | at |
| e20 | relation | m14 | m15 | medium | of |
| e21 | relation | m19 | m22 | high | against |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | map | map | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:map", "parents": []} |
| ent_m5 | object | wall | wall | object | raw_lemma | wordnet_synset:wall.n.01 + stage9_audit | architectural_part, structure, artifact | m5 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": ["entity_parent:architectural_part", "entity_parent:structure", "entity_parent:artifact"]} |
| ent_m6 | object | continent | continents | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:continent", "parents": []} |
| ent_m7 | object | hue | hues | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:hue", "parents": []} |
| ent_m9 | object | ocean | oceans | object | raw_lemma | wordnet_synset:ocean.n.01 + stage9_audit | body_of_water, place | m9 | raw_mention |  |  |  | True | {"canonical": "entity:ocean", "parents": ["entity_parent:body_of_water", "entity_parent:place"]} |
| ent_m11 | context | top | top | object | raw_lemma | semantic_type_fallback | scene_context | m11 | raw_mention |  |  |  | True | {"canonical": "entity:top", "parents": ["entity_parent:scene_context"]} |
| ent_m12 | object | character | characters | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:character", "parents": []} |
| ent_m14 | object | row | row | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:row", "parents": []} |
| ent_m15 | object | flag | flags | object | raw_lemma | none |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:flag", "parents": []} |
| ent_m17 | object | edge | edge | object | raw_lemma | none |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:edge", "parents": []} |
| ent_m19 | object | cord | cord | object | raw_lemma | none |  | m19 | raw_mention |  |  |  | True | {"canonical": "entity:cord", "parents": []} |
| ent_m21 | object | wire | wire | object | raw_lemma | none |  | m21 | raw_mention |  |  |  | True | {"canonical": "entity:wire", "parents": []} |
| ent_m22 | context | corner | corner | object | raw_lemma | semantic_type_fallback | scene_context | m22 | raw_mention |  |  |  | True | {"canonical": "entity:corner", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m23 | hangs | hang | hang | raw_action | stage9_seed:parent_seed | attachment_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:hang", "parents": ["action_parent:attachment_action", "action_parent:visual_action"]} |  |
| ce1 | m24 | showing | show | show | raw_action | wordnet_synset:show.v.01 + stage9_audit | visual_presentation_action, visual_action |  | agent:m1->ent_m1; patient:m6->ent_m6 | {"canonical": "action:show", "parents": ["action_parent:visual_presentation_action", "action_parent:visual_action"]} |  |
| ce2 | m25 | read | read | read | raw_action | stage9_seed:parent_seed | text_interaction_action, visual_action |  | agent:m12->ent_m12 | {"canonical": "action:read", "parents": ["action_parent:text_interaction_action", "action_parent:visual_action"]} |  |
| ce3 | m26 | lines | line | line | raw_action | visual_action_fallback | visual_action |  | agent:m14->ent_m14; patient:m17->ent_m17 | {"canonical": "action:line", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m27 | rests | rest | rest | raw_action | wordnet_synset:rest.v.01 + stage9_audit | support_state_action, visual_action |  | agent:m19->ent_m19; agent:m21->ent_m21 | {"canonical": "action:rest", "parents": ["action_parent:support_state_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | hang | agent | agent | none | m1 | ent_m1 | medium | e8 | nsubj -> hangs |  |  |
| ce1 | show | agent | agent | none | m1 | ent_m1 | medium | e9 | inherited agent advcl -> hangs |  |  |
| ce1 | show | patient | patient | none | m6 | ent_m6 | medium | e10 | dobj -> showing |  |  |
| ce2 | read | agent | agent | none | m12 | ent_m12 | medium | e11 | nsubj -> read |  |  |
| ce3 | line | agent | agent | none | m14 | ent_m14 | medium | e12 | nsubj -> lines |  |  |
| ce3 | line | patient | patient | none | m17 | ent_m17 | medium | e13 | dobj -> lines |  |  |
| ce4 | rest | agent | agent | none | m19 | ent_m19 | medium | e14 | nsubj -> rests |  |  |
| ce4 | rest | agent | agent | none | m21 | ent_m21 | medium | e15 | nsubj -> rests |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m5 | ent_m1 | ent_m5 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e16 | False | False |  |  |
| cr1 | m6 | m7 | ent_m6 | ent_m7 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e17 | False | False |  |  |
| cr2 | m6 | m9 | ent_m6 | ent_m9 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e18 | False | False |  |  |
| cr3 | m12 | m11 | ent_m12 | ent_m11 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e19 | False | False |  |  |
| cr4 | m14 | m15 | ent_m14 | ent_m15 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e20 | False | False |  |  |
| cr5 | m19 | m22 | ent_m19 | ent_m22 | against | against | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_contact, visual_relation | high | e21 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | map |  |  |  | entity_exists:map | True | low |
| cf1 | entity_exists | wall |  |  | architectural_part, structure, artifact | entity_exists:wall | True | high |
| cf2 | entity_exists | continent |  |  |  | entity_exists:continent | True | low |
| cf3 | entity_exists | hue |  |  |  | entity_exists:hue | True | low |
| cf4 | entity_exists | ocean |  |  | body_of_water, place | entity_exists:ocean | True | high |
| cf5 | entity_exists | top |  |  | scene_context | entity_exists:top | True | medium |
| cf6 | entity_exists | character |  |  |  | entity_exists:character | True | low |
| cf7 | entity_exists | row |  |  |  | entity_exists:row | True | low |
| cf8 | entity_exists | flag |  |  |  | entity_exists:flag | True | low |
| cf9 | entity_exists | edge |  |  |  | entity_exists:edge | True | low |
| cf10 | entity_exists | cord |  |  |  | entity_exists:cord | True | low |
| cf11 | entity_exists | wire |  |  |  | entity_exists:wire | True | low |
| cf12 | entity_exists | corner |  |  | scene_context | entity_exists:corner | True | medium |
| cf13 | has_attribute | map | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:map:large | True | high |
| cf14 | has_attribute | map | colorful |  | color_attribute, color_quantity, visual_attribute | has_attribute:map:colorful | True | medium |
| cf15 | has_attribute | map | world |  | compound_modifier, visual_attribute | has_attribute:map:world | True | medium |
| cf16 | has_quantity | hue | various |  | approximate_quantity, quantity | has_quantity:hue:various | True | medium |
| cf17 | has_attribute | character | chinese |  | modifier_attribute, visual_attribute | has_attribute:character:chinese | True | medium |
| cf18 | has_attribute | flag | small |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:flag:small | True | high |
| cf19 | has_attribute | edge | bottom |  | modifier_attribute, visual_attribute | has_attribute:edge:bottom | True | medium |
| cf20 | has_attribute | cord | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:cord:dark | True | medium |
| cf21 | action_event | hang |  |  | attachment_action, visual_action | action_event:hang | True | high |
| cf22 | event_role | hang | agent | map |  | event_role:hang:agent:map | True | medium |
| cf23 | action_event | show |  |  | visual_presentation_action, visual_action | action_event:show | True | high |
| cf24 | event_role | show | agent | map |  | event_role:show:agent:map | True | medium |
| cf25 | event_role | show | patient | continent |  | event_role:show:patient:continent | True | medium |
| cf26 | action_event | read |  |  | text_interaction_action, visual_action | action_event:read | True | medium |
| cf27 | event_role | read | agent | character |  | event_role:read:agent:character | True | medium |
| cf28 | action_event | line |  |  | visual_action | action_event:line | True | low |
| cf29 | event_role | line | agent | row |  | event_role:line:agent:row | True | medium |
| cf30 | event_role | line | patient | edge |  | event_role:line:patient:edge | True | medium |
| cf31 | action_event | rest |  |  | support_state_action, visual_action | action_event:rest | True | medium |
| cf32 | event_role | rest | agent | cord |  | event_role:rest:agent:cord | True | medium |
| cf33 | event_role | rest | agent | wire |  | event_role:rest:agent:wire | True | medium |
| cf34 | relation | map | on | wall | spatial_support, visual_relation | relation:map:on:wall | True | high |
| cf35 | relation | continent | in | hue | spatial_containment, visual_relation | relation:continent:in:hue | True | high |
| cf36 | relation | continent | with | ocean | association_relation, visual_relation | relation:continent:with:ocean | True | high |
| cf37 | relation | character | at | top | spatial_location, visual_relation | relation:character:at:top | True | medium |
| cf38 | relation | row | of | flag | part_relation, visual_relation | relation:row:of:flag | True | medium |
| cf39 | relation | cord | against | corner | spatial_contact, visual_relation | relation:cord:against:corner | True | high |

### Stage 9 Canonicalization Notes
_none_

## 31

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `1d0b068f5bb95c75a1ed5ca25ca479e332acda5f1a92ffa19e434d09cb5d9014`
**parse_path:** `sentence`

> A blue and white race car with "INKSYS" written on its side drives on a paved road. It is parked near a brick building with trees and a person standing in the background. A red and white striped barrier runs along the edge of the road.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "INKSYS" | inksys | quote_text | doc_quote | 6 | high |
| m1 | object | race car | race_car | noun_chunk_root | chunk0 | 4 | high |
| m2 | attribute | blue | blue | color_attribute | chunk0 | 1 | high |
| m3 | attribute | white | white | color_attribute | chunk0 | 3 | high |
| m4 | context | side | side | spatial_region | chunk2 | 10 | medium |
| m5 | object | road | road | noun_chunk_root | chunk3 | 15 | high |
| m6 | attribute | paved | paved | visual_attribute | chunk3 | 14 | medium |
| m7 | object | building | building | noun_chunk_root | chunk5 | 23 | high |
| m8 | attribute | brick | brick | material_attribute | chunk5 | 22 | high |
| m9 | object | trees | tree | noun_chunk_root | chunk6 | 25 | high |
| m10 | object | person | person | noun_chunk_root | chunk7 | 28 | high |
| m11 | context | background | background | scene_context | chunk8 | 32 | high |
| m12 | object | barrier | barrier | noun_chunk_root | chunk9 | 39 | high |
| m13 | attribute | red | red | color_attribute | chunk9 | 35 | high |
| m14 | attribute | white | white | color_attribute | chunk9 | 37 | high |
| m15 | attribute | striped | strip | state_attribute | chunk9 | 38 | medium |
| m16 | object | road | road | noun_chunk_root | chunk11 | 46 | high |
| m17 | action | written | write | verb_predicate | doc | 7 | high |
| m18 | action | drives | drive | verb_predicate | doc | 11 | high |
| m19 | action | parked | park | verb_predicate | doc | 19 | high |
| m20 | action | standing | stand | verb_predicate | doc | 29 | high |
| m21 | action | runs | run | verb_predicate | doc | 40 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk0 amod -> race car |
| e1 | has_attribute | m1 | m3 | high | chunk0 conj -> race car |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> road |
| e3 | has_attribute | m7 | m8 | high | chunk5 compound -> building |
| e4 | has_context | scene | m11 | high | scene_context token background |
| e5 | has_attribute | m12 | m13 | high | chunk9 amod -> barrier |
| e6 | has_attribute | m12 | m14 | high | chunk9 conj -> barrier |
| e7 | has_attribute | m12 | m15 | medium | chunk9 amod -> barrier |
| e8 | agent | m17 | m0 | medium | inherited agent acl -> "INKSYS" |
| e9 | agent | m18 | m1 | medium | nsubj -> drives |
| e10 | agent | m19 | m1 | medium | nsubjpass -> parked; resolved It -> race car |
| e11 | agent | m20 | m10 | medium | inherited agent acl -> person |
| e12 | agent | m21 | m12 | medium | nsubj -> runs |
| e13 | relation | m1 | m0 | high | with |
| e14 | relation | m1 | m5 | high | on |
| e15 | relation | m1 | m7 | high | near |
| e16 | relation | m7 | m9 | high | with |
| e17 | relation | m7 | m10 | high | with |
| e18 | relation | m10 | m11 | high | in |
| e19 | relation | m12 | m16 | medium | along_edge_of |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | race_car | race car | object | lvis_object\|wordnet_noun_mwe | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:race_car", "parents": []} |
| ent_m4 | context | side | side | object | raw_lemma | semantic_type_fallback | scene_context | m4 | raw_mention |  |  |  | True | {"canonical": "entity:side", "parents": ["entity_parent:scene_context"]} |
| ent_m5 | object | road | road | object | raw_lemma | wordnet_synset:road.n.01 + stage9_audit | path, place | m5 | raw_mention |  |  |  | True | {"canonical": "entity:road", "parents": ["entity_parent:path", "entity_parent:place"]} |
| ent_m7 | object | building | building | object | raw_lemma | wordnet_synset:building.n.01 + stage9_audit | structure, artifact | m7 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m9 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m9 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m10 | object | person | person | person | raw_lemma | stage9_seed:parent_seed | person, human | m10 | raw_mention |  |  |  | True | {"canonical": "entity:person", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m11 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m11 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m12 | object | barrier | barrier | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:barrier", "parents": []} |
| ent_m16 | object | road | road | object | raw_lemma | wordnet_synset:road.n.01 + stage9_audit | path, place | m16 | raw_mention |  |  |  | True | {"canonical": "entity:road", "parents": ["entity_parent:path", "entity_parent:place"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | written | write | write | raw_action | visual_action_fallback | visual_action |  | agent:m0->None | {"canonical": "action:write", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m18 | drives | drive | drive | raw_action | visual_action_fallback | visual_action |  | agent:m1->ent_m1 | {"canonical": "action:drive", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m19 | parked | park | park | raw_action | visual_action_fallback | visual_action |  | patient<-theme[passive_to_active]:m1->ent_m1 | {"canonical": "action:park", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m20 | standing | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m10->ent_m10 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce4 | m21 | runs | run | run | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m12->ent_m12 | {"canonical": "action:run", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | write | agent | agent | none | m0 |  | medium | e8 | inherited agent acl -> "INKSYS" |  |  |
| ce1 | drive | agent | agent | none | m1 | ent_m1 | medium | e9 | nsubj -> drives |  |  |
| ce2 | park | patient | theme | passive_to_active | m1 | ent_m1 | medium | e10 | nsubjpass -> parked; resolved It -> race car |  |  |
| ce3 | stand | agent | agent | none | m10 | ent_m10 | medium | e11 | inherited agent acl -> person |  |  |
| ce4 | run | agent | agent | none | m12 | ent_m12 | medium | e12 | nsubj -> runs |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m0 | ent_m1 |  | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr1 | m1 | m5 | ent_m1 | ent_m5 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e14 | False | False |  |  |
| cr2 | m1 | m7 | ent_m1 | ent_m7 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e15 | False | False |  |  |
| cr3 | m7 | m9 | ent_m7 | ent_m9 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e16 | False | False |  |  |
| cr4 | m7 | m10 | ent_m7 | ent_m10 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e17 | False | False |  |  |
| cr5 | m10 | m11 | ent_m10 | ent_m11 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e18 | False | False |  |  |
| cr6 | m12 | m16 | ent_m12 | ent_m16 | along_edge_of | along_edge_of | generated_region_pattern | generated_region_pattern | spatial_path, visual_relation | medium | e19 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | race_car |  |  |  | entity_exists:race_car | True | high |
| cf1 | entity_exists | side |  |  | scene_context | entity_exists:side | True | medium |
| cf2 | entity_exists | road |  |  | path, place | entity_exists:road | True | high |
| cf3 | entity_exists | building |  |  | structure, artifact | entity_exists:building | True | high |
| cf4 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf5 | entity_exists | person |  |  | person, human | entity_exists:person | True | high |
| cf6 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf7 | entity_exists | barrier |  |  |  | entity_exists:barrier | True | low |
| cf8 | entity_exists | road |  |  | path, place | entity_exists:road | True | high |
| cf9 | has_attribute | race_car | blue |  | color_attribute, color, visual_attribute | has_attribute:race_car:blue | True | high |
| cf10 | has_attribute | race_car | white |  | color_attribute, color, visual_attribute | has_attribute:race_car:white | True | high |
| cf11 | has_attribute | road | paved |  | visual_attribute | has_attribute:road:paved | True | medium |
| cf12 | has_attribute | building | brick |  | material_attribute, material, visual_attribute | has_attribute:building:brick | True | high |
| cf13 | has_attribute | barrier | red |  | color_attribute, color, visual_attribute | has_attribute:barrier:red | True | high |
| cf14 | has_attribute | barrier | white |  | color_attribute, color, visual_attribute | has_attribute:barrier:white | True | high |
| cf15 | has_attribute | barrier | striped |  | pattern_attribute, clean_exact_overlap, pattern, pattern_marking, texture, visual_attribute | has_attribute:barrier:striped | True | medium |
| cf16 | action_event | write |  |  | visual_action | action_event:write | True | low |
| cf17 | event_role | write | agent |  |  | event_role:write:agent | False | medium |
| cf18 | action_event | drive |  |  | visual_action | action_event:drive | True | low |
| cf19 | event_role | drive | agent | race_car |  | event_role:drive:agent:race_car | True | medium |
| cf20 | action_event | park |  |  | visual_action | action_event:park | True | low |
| cf21 | event_role | park | patient | race_car |  | event_role:park:patient:race_car | True | medium |
| cf22 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf23 | event_role | stand | agent | person |  | event_role:stand:agent:person | True | medium |
| cf24 | action_event | run |  |  | locomotion_action, visual_action | action_event:run | True | high |
| cf25 | event_role | run | agent | barrier |  | event_role:run:agent:barrier | True | medium |
| cf26 | relation | race_car | with |  | association_relation, visual_relation | relation:race_car:with | False | high |
| cf27 | relation | race_car | on | road | spatial_support, visual_relation | relation:race_car:on:road | True | high |
| cf28 | relation | race_car | near | building | spatial_proximity, visual_relation | relation:race_car:near:building | True | high |
| cf29 | relation | building | with | tree | association_relation, visual_relation | relation:building:with:tree | True | high |
| cf30 | relation | building | with | person | association_relation, visual_relation | relation:building:with:person | True | high |
| cf31 | relation | person | in | background | spatial_containment, visual_relation | relation:person:in:background | True | high |
| cf32 | relation | barrier | along_edge_of | road | spatial_path, visual_relation | relation:barrier:along_edge_of:road | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m19 | e10 | m1 |  |  | {"action_mention_id": "m19", "kind": "passive_subject_to_patient", "raw_edge_id": "e10", "raw_role": "theme", "role": "patient", "target": "m1", "voice_normalization": "passive_to_active"} |

## 32

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `1dbd1444a7eb9ea0c0c81c353fe98aae031078d88f1d4de2dcb40a55d460d414`
**parse_path:** `sentence`

> A man in a blue suit speaks at a microphone while others sit in a formal room with masks on.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | suit | suit | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | blue | blue | color_attribute | chunk1 | 4 | high |
| m3 | object | microphone | microphone | noun_chunk_root | chunk2 | 9 | high |
| m4 | object | room | room | noun_chunk_root | chunk4 | 16 | high |
| m5 | attribute | formal | formal | modifier_attribute | chunk4 | 15 | medium |
| m6 | object | masks | mask | noun_chunk_root | chunk5 | 18 | high |
| m7 | action | speaks | speak | verb_predicate | doc | 6 | high |
| m8 | action | sit | sit | verb_predicate | doc | 12 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> suit |
| e1 | has_attribute | m4 | m5 | medium | chunk4 amod -> room |
| e2 | agent | m7 | m0 | medium | nsubj -> speaks |
| e3 | agent | m8 | m0 | medium | inherited agent advcl -> speaks |
| e4 | relation | m0 | m1 | high | in |
| e5 | relation | m0 | m3 | medium | at |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | suit | suit | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:suit", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | microphone | microphone | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:microphone", "parents": []} |
| ent_m4 | object | room | room | object | raw_lemma | wordnet_synset:room.n.01 + stage9_audit | interior_place, place | m4 | raw_mention |  |  |  | True | {"canonical": "entity:room", "parents": ["entity_parent:interior_place", "entity_parent:place"]} |
| ent_m6 | object | mask | masks | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m6 | raw_mention |  |  |  | True | {"canonical": "entity:mask", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | speaks | speak | speak | raw_action | stage9_seed:parent_seed | communication_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:speak", "parents": ["action_parent:communication_action", "action_parent:visual_action"]} |  |
| ce1 | m8 | sit | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | speak | agent | agent | none | m0 | ent_m0 | medium | e2 | nsubj -> speaks |  |  |
| ce1 | sit | agent | agent | none | m0 | ent_m0 | medium | e3 | inherited agent advcl -> speaks |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e4 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e5 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | suit |  |  | clothing, wearable | entity_exists:suit | True | high |
| cf2 | entity_exists | microphone |  |  |  | entity_exists:microphone | True | low |
| cf3 | entity_exists | room |  |  | interior_place, place | entity_exists:room | True | high |
| cf4 | entity_exists | mask |  |  | clothing, wearable | entity_exists:mask | True | medium |
| cf5 | has_attribute | suit | blue |  | color_attribute, color, visual_attribute | has_attribute:suit:blue | True | high |
| cf6 | has_attribute | room | formal |  | modifier_attribute, visual_attribute | has_attribute:room:formal | True | medium |
| cf7 | action_event | speak |  |  | communication_action, visual_action | action_event:speak | True | medium |
| cf8 | event_role | speak | agent | man |  | event_role:speak:agent:man | True | medium |
| cf9 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf10 | event_role | sit | agent | man |  | event_role:sit:agent:man | True | medium |
| cf11 | relation | man | in | suit | spatial_containment, visual_relation | relation:man:in:suit | True | high |
| cf12 | relation | man | at | microphone | spatial_location, visual_relation | relation:man:at:microphone | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 33

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `1ed19f9ae5248d3c26f9410857f74a394f02fee4b0e2bc173e9a4934cde12c14`
**parse_path:** `sentence`

> A naval officer stands before a group of service members in uniform on a concrete yard.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | officer | officer | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | naval | naval | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | group | group | noun_chunk_root | chunk1 | 6 | high |
| m3 | object | members | member | noun_chunk_root | chunk2 | 9 | high |
| m4 | attribute | service | service | compound_modifier | chunk2 | 8 | medium |
| m5 | object | uniform | uniform | noun_chunk_root | chunk3 | 11 | high |
| m6 | object | yard | yard | noun_chunk_root | chunk4 | 15 | high |
| m7 | attribute | concrete | concrete | material_attribute | chunk4 | 14 | high |
| m8 | action | stands | stand | verb_predicate | doc | 3 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> officer |
| e1 | has_attribute | m3 | m4 | medium | chunk2 compound -> members |
| e2 | has_attribute | m6 | m7 | high | chunk4 amod -> yard |
| e3 | agent | m8 | m0 | medium | nsubj -> stands |
| e4 | relation | m0 | m2 | medium | before |
| e5 | relation | m2 | m3 | medium | of |
| e6 | relation | m3 | m5 | high | in |
| e7 | relation | m0 | m6 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | officer | officer | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:officer", "parents": []} |
| ent_m2 | object | group | group | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:group", "parents": []} |
| ent_m3 | object | member | members | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:member", "parents": []} |
| ent_m5 | object | uniform | uniform | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m5 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m6 | object | yard | yard | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:yard", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e3 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | before | before | raw_relation | raw_relation | visual_relation | medium | e4 | False | False |  |  |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e5 | False | False |  |  |
| cr2 | m3 | m5 | ent_m3 | ent_m5 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e6 | False | False |  |  |
| cr3 | m0 | m6 | ent_m0 | ent_m6 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | officer |  |  |  | entity_exists:officer | True | low |
| cf1 | entity_exists | group |  |  |  | entity_exists:group | True | low |
| cf2 | entity_exists | member |  |  |  | entity_exists:member | True | low |
| cf3 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf4 | entity_exists | yard |  |  |  | entity_exists:yard | True | low |
| cf5 | has_attribute | officer | naval |  | modifier_attribute, visual_attribute | has_attribute:officer:naval | True | medium |
| cf6 | has_attribute | member | service |  | compound_modifier, visual_attribute | has_attribute:member:service | True | medium |
| cf7 | has_attribute | yard | concrete |  | material_attribute, material, visual_attribute | has_attribute:yard:concrete | True | high |
| cf8 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf9 | event_role | stand | agent | officer |  | event_role:stand:agent:officer | True | medium |
| cf10 | relation | officer | before | group | visual_relation | relation:officer:before:group | True | medium |
| cf11 | relation | group | of | member | part_relation, visual_relation | relation:group:of:member | True | medium |
| cf12 | relation | member | in | uniform | spatial_containment, visual_relation | relation:member:in:uniform | True | high |
| cf13 | relation | officer | on | yard | spatial_support, visual_relation | relation:officer:on:yard | True | high |

### Stage 9 Canonicalization Notes
_none_

## 34

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `1edae671c34341d39438fcb17df49652a04e1d077cd8555bc1d38f8fd4e61814`
**parse_path:** `sentence`

> A speaker stands at a podium on stage, addressing a large audience seated in rows of chairs.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | speaker | speaker | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | podium | podium | noun_chunk_root | chunk1 | 5 | high |
| m2 | object | stage | stage | noun_chunk_root | chunk2 | 7 | high |
| m3 | object | audience | audience | noun_chunk_root | chunk3 | 12 | high |
| m4 | attribute | large | large | size_attribute | chunk3 | 11 | high |
| m5 | object | rows | row | noun_chunk_root | chunk4 | 15 | high |
| m6 | object | chairs | chair | noun_chunk_root | chunk5 | 17 | high |
| m7 | action | stands | stand | verb_predicate | doc | 2 | high |
| m8 | action | addressing | address | verb_predicate | doc | 9 | high |
| m9 | action | seated | seat | verb_predicate | doc | 13 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m3 | m4 | high | chunk3 amod -> audience |
| e1 | agent | m7 | m0 | medium | nsubj -> stands |
| e2 | agent | m8 | m0 | medium | inherited agent advcl -> stands |
| e3 | patient | m8 | m3 | medium | dobj -> addressing |
| e4 | agent | m9 | m3 | medium | inherited agent acl -> audience |
| e5 | relation | m0 | m1 | medium | at |
| e6 | relation | m1 | m2 | high | on |
| e7 | relation | m3 | m5 | high | in |
| e8 | relation | m5 | m6 | medium | of |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | speaker | speaker | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:speaker", "parents": []} |
| ent_m1 | object | podium | podium | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:podium", "parents": []} |
| ent_m2 | object | stage | stage | object | raw_lemma | wordnet_synset:stage.n.03 + stage9_audit | platform, place, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:stage", "parents": ["entity_parent:platform", "entity_parent:place", "entity_parent:artifact"]} |
| ent_m3 | object | audience | audience | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:audience", "parents": []} |
| ent_m5 | object | row | rows | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:row", "parents": []} |
| ent_m6 | object | chair | chairs | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m6 | raw_mention |  |  |  | True | {"canonical": "entity:chair", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m8 | addressing | address | address | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m3->ent_m3 | {"canonical": "action:address", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m9 | seated | seat | sit | stage9_seed:synonym_seed | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m3->ent_m3 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e1 | nsubj -> stands |  |  |
| ce1 | address | agent | agent | none | m0 | ent_m0 | medium | e2 | inherited agent advcl -> stands |  |  |
| ce1 | address | patient | patient | none | m3 | ent_m3 | medium | e3 | dobj -> addressing |  |  |
| ce2 | sit | agent | agent | none | m3 | ent_m3 | medium | e4 | inherited agent acl -> audience |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e5 | False | False |  |  |
| cr1 | m1 | m2 | ent_m1 | ent_m2 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e6 | False | False |  |  |
| cr2 | m3 | m5 | ent_m3 | ent_m5 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e7 | False | False |  |  |
| cr3 | m5 | m6 | ent_m5 | ent_m6 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | speaker |  |  |  | entity_exists:speaker | True | low |
| cf1 | entity_exists | podium |  |  |  | entity_exists:podium | True | low |
| cf2 | entity_exists | stage |  |  | platform, place, artifact | entity_exists:stage | True | medium |
| cf3 | entity_exists | audience |  |  |  | entity_exists:audience | True | low |
| cf4 | entity_exists | row |  |  |  | entity_exists:row | True | low |
| cf5 | entity_exists | chair |  |  | furniture, artifact | entity_exists:chair | True | high |
| cf6 | has_attribute | audience | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:audience:large | True | high |
| cf7 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf8 | event_role | stand | agent | speaker |  | event_role:stand:agent:speaker | True | medium |
| cf9 | action_event | address |  |  | visual_action | action_event:address | True | low |
| cf10 | event_role | address | agent | speaker |  | event_role:address:agent:speaker | True | medium |
| cf11 | event_role | address | patient | audience |  | event_role:address:patient:audience | True | medium |
| cf12 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf13 | event_role | sit | agent | audience |  | event_role:sit:agent:audience | True | medium |
| cf14 | relation | speaker | at | podium | spatial_location, visual_relation | relation:speaker:at:podium | True | medium |
| cf15 | relation | podium | on | stage | spatial_support, visual_relation | relation:podium:on:stage | True | high |
| cf16 | relation | audience | in | row | spatial_containment, visual_relation | relation:audience:in:row | True | high |
| cf17 | relation | row | of | chair | part_relation, visual_relation | relation:row:of:chair | True | medium |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| action_lexical_canonicalized | m9 |  |  |  |  | {"action_mention_id": "m9", "canonical": "sit", "kind": "action_lexical_canonicalized", "raw_canonical_action": "seat", "source": "stage9_seed:synonym_seed"} |

## 35

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `1f11bb39ba7eb254d725852643e806b15bc8ba5534e19faff30dec48adfd2c14`
**parse_path:** `sentence`

> Snow-covered trees stand in a forest with bare branches reaching upward. Mist shrouds the mountains in the background under a cloudy sky. The ground is blanketed in white, and evergreen trees are visible among the snow-laden pines.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | trees | tree | noun_chunk_root | chunk0 | 1 | high |
| m1 | attribute | Snow-covered | snow-covered | modifier_attribute | chunk0 | 0 | medium |
| m2 | object | forest | forest | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | branches | branch | noun_chunk_root | chunk2 | 8 | high |
| m4 | attribute | bare | bare | visual_attribute | chunk2 | 7 | medium |
| m5 | object | Mist | mist | noun_chunk_root | chunk3 | 12 | high |
| m6 | object | mountains | mountain | noun_chunk_root | chunk4 | 15 | high |
| m7 | context | background | background | scene_context | chunk5 | 18 | high |
| m8 | object | sky | sky | noun_chunk_root | chunk6 | 22 | high |
| m9 | attribute | cloudy | cloudy | modifier_attribute | chunk6 | 21 | medium |
| m10 | object | ground | ground | noun_chunk_root | chunk7 | 25 | high |
| m11 | attribute | white | white | color_attribute | chunk8 | 29 | high |
| m12 | object | trees | tree | noun_chunk_root | chunk9 | 33 | high |
| m13 | attribute | evergreen | evergreen | modifier_attribute | chunk9 | 32 | medium |
| m14 | object | pines | pine | noun_chunk_root | chunk10 | 39 | high |
| m15 | attribute | snow-laden | snow-laden | modifier_attribute | chunk10 | 38 | medium |
| m16 | action | stand | stand | verb_predicate | doc | 2 | high |
| m17 | action | reaching | reach | verb_predicate | doc | 9 | high |
| m18 | action | shrouds | shroud | verb_predicate | doc | 13 | high |
| m19 | action | blanketed | blanket | verb_predicate | doc | 27 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> trees |
| e1 | has_attribute | m3 | m4 | medium | chunk2 amod -> branches |
| e2 | has_context | scene | m7 | high | scene_context token background |
| e3 | has_attribute | m8 | m9 | medium | chunk6 amod -> sky |
| e4 | has_attribute | m12 | m13 | medium | chunk9 amod -> trees |
| e5 | has_attribute | m14 | m15 | medium | chunk10 amod -> pines |
| e6 | agent | m16 | m0 | medium | nsubj -> stand |
| e7 | agent | m17 | m3 | medium | nsubj -> reaching |
| e8 | agent | m18 | m5 | medium | nsubj -> shrouds |
| e9 | patient | m18 | m6 | medium | dobj -> shrouds |
| e10 | agent | m19 | m10 | medium | nsubjpass -> blanketed |
| e11 | relation | m0 | m2 | high | in |
| e12 | relation | m5 | m7 | high | in |
| e13 | relation | m5 | m8 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m0 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m2 | object | forest | forest | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:forest", "parents": []} |
| ent_m3 | object | branch | branches | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:branch", "parents": []} |
| ent_m5 | object | mist | Mist | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:mist", "parents": []} |
| ent_m6 | object | mountain | mountains | object | raw_lemma | wordnet_synset:mountain.n.01 + stage9_audit | landform, place | m6 | raw_mention |  |  |  | True | {"canonical": "entity:mountain", "parents": ["entity_parent:landform", "entity_parent:place"]} |
| ent_m7 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m8 | object | sky | sky | object | raw_lemma | wordnet_synset:sky.n.01 + stage9_audit | natural_scene | m8 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": ["entity_parent:natural_scene"]} |
| ent_m10 | object | ground | ground | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:ground", "parents": []} |
| ent_m12 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m12 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m14 | object | pine | pines | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:pine", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m17 | reaching | reach | reach | raw_action | visual_action_fallback | visual_action |  | agent:m3->ent_m3 | {"canonical": "action:reach", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m18 | shrouds | shroud | shroud | raw_action | visual_action_fallback | visual_action |  | agent:m5->ent_m5; patient:m6->ent_m6 | {"canonical": "action:shroud", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m19 | blanketed | blanket | blanket | raw_action | visual_action_fallback | visual_action |  | patient<-theme[passive_to_active]:m10->ent_m10 | {"canonical": "action:blanket", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e6 | nsubj -> stand |  |  |
| ce1 | reach | agent | agent | none | m3 | ent_m3 | medium | e7 | nsubj -> reaching |  |  |
| ce2 | shroud | agent | agent | none | m5 | ent_m5 | medium | e8 | nsubj -> shrouds |  |  |
| ce2 | shroud | patient | patient | none | m6 | ent_m6 | medium | e9 | dobj -> shrouds |  |  |
| ce3 | blanket | patient | theme | passive_to_active | m10 | ent_m10 | medium | e10 | nsubjpass -> blanketed |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e11 | False | False |  |  |
| cr1 | m5 | m7 | ent_m5 | ent_m7 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e12 | False | False |  |  |
| cr2 | m5 | m8 | ent_m5 | ent_m8 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e13 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf1 | entity_exists | forest |  |  |  | entity_exists:forest | True | low |
| cf2 | entity_exists | branch |  |  |  | entity_exists:branch | True | low |
| cf3 | entity_exists | mist |  |  |  | entity_exists:mist | True | low |
| cf4 | entity_exists | mountain |  |  | landform, place | entity_exists:mountain | True | high |
| cf5 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf6 | entity_exists | sky |  |  | natural_scene | entity_exists:sky | True | high |
| cf7 | entity_exists | ground |  |  |  | entity_exists:ground | True | low |
| cf8 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf9 | entity_exists | pine |  |  |  | entity_exists:pine | True | low |
| cf10 | has_attribute | tree | snow-covered |  | modifier_attribute, visual_attribute | has_attribute:tree:snow-covered | True | medium |
| cf11 | has_attribute | branch | bare |  | visual_attribute | has_attribute:branch:bare | True | medium |
| cf12 | has_attribute | sky | cloudy |  | weather_attribute, weather, visual_attribute | has_attribute:sky:cloudy | True | medium |
| cf13 | has_attribute | tree | evergreen |  | modifier_attribute, visual_attribute | has_attribute:tree:evergreen | True | medium |
| cf14 | has_attribute | pine | snow-laden |  | modifier_attribute, visual_attribute | has_attribute:pine:snow-laden | True | medium |
| cf15 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf16 | event_role | stand | agent | tree |  | event_role:stand:agent:tree | True | medium |
| cf17 | action_event | reach |  |  | visual_action | action_event:reach | True | low |
| cf18 | event_role | reach | agent | branch |  | event_role:reach:agent:branch | True | medium |
| cf19 | action_event | shroud |  |  | visual_action | action_event:shroud | True | low |
| cf20 | event_role | shroud | agent | mist |  | event_role:shroud:agent:mist | True | medium |
| cf21 | event_role | shroud | patient | mountain |  | event_role:shroud:patient:mountain | True | medium |
| cf22 | action_event | blanket |  |  | visual_action | action_event:blanket | True | low |
| cf23 | event_role | blanket | patient | ground |  | event_role:blanket:patient:ground | True | medium |
| cf24 | relation | tree | in | forest | spatial_containment, visual_relation | relation:tree:in:forest | True | high |
| cf25 | relation | mist | in | background | spatial_containment, visual_relation | relation:mist:in:background | True | high |
| cf26 | relation | mist | under | sky | spatial_vertical, visual_relation | relation:mist:under:sky | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m19 | e10 | m10 |  |  | {"action_mention_id": "m19", "kind": "passive_subject_to_patient", "raw_edge_id": "e10", "raw_role": "theme", "role": "patient", "target": "m10", "voice_normalization": "passive_to_active"} |

## 36

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `20032fade56eef98738bedcc363c9c2ecc58e22b0e995f3fec445fd942ae4c14`
**parse_path:** `sentence`

> A group of people sit at tables in a conference room with a large projection screen displaying a presentation. A whiteboard stands near the wall, and colorful abstract paintings hang behind it. The room has wooden paneling and a shiny tiled floor.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | group | group | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | people | people | noun_chunk_root | chunk1 | 3 | high |
| m2 | object | tables | table | noun_chunk_root | chunk2 | 6 | high |
| m3 | object | conference room | conference_room | noun_chunk_root | chunk3 | 9 | high |
| m4 | object | projection screen | projection_screen | noun_chunk_root | chunk4 | 13 | high |
| m5 | attribute | large | large | size_attribute | chunk4 | 12 | high |
| m6 | object | presentation | presentation | noun_chunk_root | chunk5 | 16 | high |
| m7 | object | whiteboard | whiteboard | noun_chunk_root | chunk6 | 19 | high |
| m8 | object | wall | wall | noun_chunk_root | chunk7 | 23 | high |
| m9 | object | paintings | painting | noun_chunk_root | chunk8 | 28 | high |
| m10 | attribute | colorful | colorful | modifier_attribute | chunk8 | 26 | medium |
| m11 | attribute | abstract | abstract | modifier_attribute | chunk8 | 27 | medium |
| m12 | object | room | room | noun_chunk_root | chunk10 | 34 | high |
| m13 | object | paneling | paneling | noun_chunk_root | chunk11 | 37 | high |
| m14 | attribute | wooden | wooden | material_attribute | chunk11 | 36 | high |
| m15 | object | floor | floor | noun_chunk_root | chunk12 | 42 | high |
| m16 | attribute | shiny | shiny | visual_attribute | chunk12 | 40 | medium |
| m17 | attribute | tiled | tile | state_attribute | chunk12 | 41 | medium |
| m18 | action | sit | sit | verb_predicate | doc | 4 | high |
| m19 | action | displaying | display | verb_predicate | doc | 14 | high |
| m20 | action | stands | stand | verb_predicate | doc | 20 | high |
| m21 | action | hang | hang | verb_predicate | doc | 29 | high |
| m22 | action | has | have | verb_predicate | doc | 35 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m4 | m5 | high | chunk4 amod -> projection screen |
| e1 | has_attribute | m9 | m10 | medium | chunk8 amod -> paintings |
| e2 | has_attribute | m9 | m11 | medium | chunk8 amod -> paintings |
| e3 | has_attribute | m13 | m14 | high | chunk11 amod -> paneling |
| e4 | has_attribute | m15 | m16 | medium | chunk12 amod -> floor |
| e5 | has_attribute | m15 | m17 | medium | chunk12 amod -> floor |
| e6 | agent | m18 | m0 | medium | nsubj -> sit |
| e7 | agent | m19 | m4 | medium | inherited agent acl -> projection screen |
| e8 | patient | m19 | m6 | medium | dobj -> displaying |
| e9 | agent | m20 | m7 | medium | nsubj -> stands |
| e10 | agent | m21 | m9 | medium | nsubj -> hang |
| e11 | agent | m22 | m12 | medium | nsubj -> has |
| e12 | patient | m22 | m13 | medium | dobj -> has |
| e13 | patient | m22 | m15 | medium | dobj -> has |
| e14 | relation | m0 | m1 | medium | of |
| e15 | relation | m0 | m2 | medium | at |
| e16 | relation | m0 | m3 | high | in |
| e17 | relation | m0 | m4 | high | with |
| e18 | relation | m7 | m8 | high | near |

### Skipped Raw Concept Edges
| type | source | target | confidence | reason | evidence |
| --- | --- | --- | --- | --- | --- |
| relation | m9 | m9 | high | self_edge_after_coref | behind |

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | group | group | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:group", "parents": []} |
| ent_m1 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | table | tables | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m3 | object | conference_room | conference room | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:conference_room", "parents": []} |
| ent_m4 | object | projection_screen | projection screen | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:projection_screen", "parents": []} |
| ent_m6 | object | presentation | presentation | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:presentation", "parents": []} |
| ent_m7 | object | whiteboard | whiteboard | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:whiteboard", "parents": []} |
| ent_m8 | object | wall | wall | object | raw_lemma | wordnet_synset:wall.n.01 + stage9_audit | architectural_part, structure, artifact | m8 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": ["entity_parent:architectural_part", "entity_parent:structure", "entity_parent:artifact"]} |
| ent_m9 | object | painting | paintings | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:painting", "parents": []} |
| ent_m12 | object | room | room | object | raw_lemma | wordnet_synset:room.n.01 + stage9_audit | interior_place, place | m12 | raw_mention |  |  |  | True | {"canonical": "entity:room", "parents": ["entity_parent:interior_place", "entity_parent:place"]} |
| ent_m13 | object | paneling | paneling | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:paneling", "parents": []} |
| ent_m15 | object | floor | floor | object | raw_lemma | wordnet_synset:floor.n.01 + stage9_audit | architectural_part, surface, artifact | m15 | raw_mention |  |  |  | True | {"canonical": "entity:floor", "parents": ["entity_parent:architectural_part", "entity_parent:surface", "entity_parent:artifact"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | sit | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m19 | displaying | display | display | raw_action | wordnet_synset:display.v.01 + stage9_audit | visual_presentation_action, visual_action |  | agent:m4->ent_m4; patient:m6->ent_m6 | {"canonical": "action:display", "parents": ["action_parent:visual_presentation_action", "action_parent:visual_action"]} |  |
| ce2 | m20 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m7->ent_m7 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce3 | m21 | hang | hang | hang | raw_action | stage9_seed:parent_seed | attachment_action, visual_action |  | agent:m9->ent_m9 | {"canonical": "action:hang", "parents": ["action_parent:attachment_action", "action_parent:visual_action"]} |  |
| ce4 | m22 | has | have | have | raw_action | visual_action_fallback | visual_action |  | agent:m12->ent_m12; patient:m13->ent_m13; patient:m15->ent_m15 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | agent | none | m0 | ent_m0 | medium | e6 | nsubj -> sit |  |  |
| ce1 | display | agent | agent | none | m4 | ent_m4 | medium | e7 | inherited agent acl -> projection screen |  |  |
| ce1 | display | patient | patient | none | m6 | ent_m6 | medium | e8 | dobj -> displaying |  |  |
| ce2 | stand | agent | agent | none | m7 | ent_m7 | medium | e9 | nsubj -> stands |  |  |
| ce3 | hang | agent | agent | none | m9 | ent_m9 | medium | e10 | nsubj -> hang |  |  |
| ce4 | have | agent | agent | none | m12 | ent_m12 | medium | e11 | nsubj -> has |  |  |
| ce4 | have | patient | patient | none | m13 | ent_m13 | medium | e12 | dobj -> has |  |  |
| ce4 | have | patient | patient | none | m15 | ent_m15 | medium | e13 | dobj -> has |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e14 | False | False |  |  |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e15 | False | False |  |  |
| cr2 | m0 | m3 | ent_m0 | ent_m3 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e16 | False | False |  |  |
| cr3 | m0 | m4 | ent_m0 | ent_m4 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e17 | False | False |  |  |
| cr4 | m7 | m8 | ent_m7 | ent_m8 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e18 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | group |  |  |  | entity_exists:group | True | low |
| cf1 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf2 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf3 | entity_exists | conference_room |  |  |  | entity_exists:conference_room | True | high |
| cf4 | entity_exists | projection_screen |  |  |  | entity_exists:projection_screen | True | high |
| cf5 | entity_exists | presentation |  |  |  | entity_exists:presentation | True | low |
| cf6 | entity_exists | whiteboard |  |  |  | entity_exists:whiteboard | True | low |
| cf7 | entity_exists | wall |  |  | architectural_part, structure, artifact | entity_exists:wall | True | high |
| cf8 | entity_exists | painting |  |  |  | entity_exists:painting | True | low |
| cf9 | entity_exists | room |  |  | interior_place, place | entity_exists:room | True | high |
| cf10 | entity_exists | paneling |  |  |  | entity_exists:paneling | True | low |
| cf11 | entity_exists | floor |  |  | architectural_part, surface, artifact | entity_exists:floor | True | high |
| cf12 | has_attribute | projection_screen | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:projection_screen:large | True | high |
| cf13 | has_attribute | painting | colorful |  | color_attribute, color_quantity, visual_attribute | has_attribute:painting:colorful | True | medium |
| cf14 | has_attribute | painting | abstract |  | pattern_attribute, textile_pattern, visual_attribute | has_attribute:painting:abstract | True | medium |
| cf15 | has_attribute | paneling | wood |  | material_attribute, material, visual_attribute | has_attribute:paneling:wood | True | high |
| cf16 | has_attribute | floor | shiny |  | visual_attribute | has_attribute:floor:shiny | True | medium |
| cf17 | has_attribute | floor | tiled |  | material_attribute, material, pattern, visual_attribute | has_attribute:floor:tiled | True | medium |
| cf18 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf19 | event_role | sit | agent | group |  | event_role:sit:agent:group | True | medium |
| cf20 | action_event | display |  |  | visual_presentation_action, visual_action | action_event:display | True | high |
| cf21 | event_role | display | agent | projection_screen |  | event_role:display:agent:projection_screen | True | medium |
| cf22 | event_role | display | patient | presentation |  | event_role:display:patient:presentation | True | medium |
| cf23 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf24 | event_role | stand | agent | whiteboard |  | event_role:stand:agent:whiteboard | True | medium |
| cf25 | action_event | hang |  |  | attachment_action, visual_action | action_event:hang | True | high |
| cf26 | event_role | hang | agent | painting |  | event_role:hang:agent:painting | True | medium |
| cf27 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf28 | event_role | have | agent | room |  | event_role:have:agent:room | True | medium |
| cf29 | event_role | have | patient | paneling |  | event_role:have:patient:paneling | True | medium |
| cf30 | event_role | have | patient | floor |  | event_role:have:patient:floor | True | medium |
| cf31 | relation | group | of | people | part_relation, visual_relation | relation:group:of:people | True | medium |
| cf32 | relation | group | at | table | spatial_location, visual_relation | relation:group:at:table | True | medium |
| cf33 | relation | group | in | conference_room | spatial_containment, visual_relation | relation:group:in:conference_room | True | high |
| cf34 | relation | group | with | projection_screen | association_relation, visual_relation | relation:group:with:projection_screen | True | high |
| cf35 | relation | whiteboard | near | wall | spatial_proximity, visual_relation | relation:whiteboard:near:wall | True | high |

### Stage 9 Canonicalization Notes
_none_

## 37

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `20fbac96b2d56737b22b58a8d76d4b8398599b85009400755d05de149ea24014`
**parse_path:** `sentence`

> A gray sports car with a large rear spoiler drifts on a wet racetrack, kicking up water spray. The car is near a concrete barrier, with blurred spectators and signage visible in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | sports car | sports_car | noun_chunk_root | chunk0 | 2 | high |
| m1 | object | spoiler | spoiler | noun_chunk_root | chunk1 | 7 | high |
| m2 | attribute | large | large | size_attribute | chunk1 | 5 | high |
| m3 | attribute | rear | rear | modifier_attribute | chunk1 | 6 | medium |
| m4 | object | racetrack | racetrack | noun_chunk_root | chunk2 | 12 | high |
| m5 | attribute | wet | wet | modifier_attribute | chunk2 | 11 | medium |
| m6 | object | spray | spray | noun_chunk_root | chunk3 | 17 | high |
| m7 | attribute | water | water | compound_modifier | chunk3 | 16 | medium |
| m8 | object | car | car | noun_chunk_root | chunk4 | 20 | high |
| m9 | object | barrier | barrier | noun_chunk_root | chunk5 | 25 | high |
| m10 | attribute | concrete | concrete | material_attribute | chunk5 | 24 | high |
| m11 | object | spectators | spectator | noun_chunk_root | chunk6 | 29 | high |
| m12 | attribute | blurred | blurred | modifier_attribute | chunk6 | 28 | medium |
| m13 | object | signage | signage | noun_chunk_root | chunk7 | 31 | high |
| m14 | context | background | background | scene_context | chunk8 | 35 | high |
| m15 | action | drifts | drift | verb_predicate | doc | 8 | high |
| m16 | action | kicking | kick | verb_predicate | doc | 14 | high |
| m17 | particle | up | up | phrasal_particle | action_particle | 15 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> spoiler |
| e1 | has_attribute | m1 | m3 | medium | chunk1 amod -> spoiler |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> racetrack |
| e3 | has_attribute | m6 | m7 | medium | chunk3 compound -> spray |
| e4 | has_attribute | m9 | m10 | high | chunk5 amod -> barrier |
| e5 | has_attribute | m11 | m12 | medium | chunk6 amod -> spectators |
| e6 | has_context | scene | m14 | high | scene_context token background |
| e7 | agent | m15 | m0 | medium | nsubj -> drifts |
| e8 | has_particle | m16 | m17 | medium | prt -> kicking |
| e9 | agent | m16 | m0 | medium | inherited agent advcl -> drifts |
| e10 | patient | m16 | m6 | medium | dobj -> kicking |
| e11 | relation | m0 | m1 | high | with |
| e12 | relation | m0 | m4 | high | on |
| e13 | relation | m8 | m9 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sports_car | sports car | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:sports_car", "parents": []} |
| ent_m1 | object | spoiler | spoiler | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:spoiler", "parents": []} |
| ent_m4 | object | racetrack | racetrack | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:racetrack", "parents": []} |
| ent_m6 | object | spray | spray | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:spray", "parents": []} |
| ent_m8 | object | car | car | vehicle | raw_lemma | stage9_seed:parent_seed | vehicle | m8 | raw_mention |  |  |  | True | {"canonical": "entity:car", "parents": ["entity_parent:vehicle"]} |
| ent_m9 | object | barrier | barrier | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:barrier", "parents": []} |
| ent_m11 | object | spectator | spectators | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:spectator", "parents": []} |
| ent_m13 | object | signage | signage | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:signage", "parents": []} |
| ent_m14 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m14 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | drifts | drift | drift | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:drift", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m16 | kicking | kick | kick | raw_action | wordnet_synset:kick.v.01 + stage9_audit | body_motion_action, sports_action, visual_action | up | agent:m0->ent_m0; patient:m6->ent_m6 | {"canonical": "action:kick", "parents": ["action_parent:body_motion_action", "action_parent:sports_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | drift | agent | agent | none | m0 | ent_m0 | medium | e7 | nsubj -> drifts |  |  |
| ce1 | kick | agent | agent | none | m0 | ent_m0 | medium | e9 | inherited agent advcl -> drifts |  |  |
| ce1 | kick | patient | patient | none | m6 | ent_m6 | medium | e10 | dobj -> kicking |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e11 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e12 | False | False |  |  |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e13 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | sports_car |  |  |  | entity_exists:sports_car | True | high |
| cf1 | entity_exists | spoiler |  |  |  | entity_exists:spoiler | True | low |
| cf2 | entity_exists | racetrack |  |  |  | entity_exists:racetrack | True | low |
| cf3 | entity_exists | spray |  |  |  | entity_exists:spray | True | low |
| cf4 | entity_exists | car |  |  | vehicle | entity_exists:car | True | high |
| cf5 | entity_exists | barrier |  |  |  | entity_exists:barrier | True | low |
| cf6 | entity_exists | spectator |  |  |  | entity_exists:spectator | True | low |
| cf7 | entity_exists | signage |  |  |  | entity_exists:signage | True | low |
| cf8 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf9 | has_attribute | spoiler | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:spoiler:large | True | high |
| cf10 | has_attribute | spoiler | rear |  | modifier_attribute, visual_attribute | has_attribute:spoiler:rear | True | medium |
| cf11 | has_attribute | racetrack | wet |  | state_attribute, clean_exact_overlap, state, visual_attribute | has_attribute:racetrack:wet | True | medium |
| cf12 | has_attribute | spray | water |  | material_attribute, material, visual_attribute | has_attribute:spray:water | True | medium |
| cf13 | has_attribute | barrier | concrete |  | material_attribute, material, visual_attribute | has_attribute:barrier:concrete | True | high |
| cf14 | has_attribute | spectator | blurred |  | modifier_attribute, visual_attribute | has_attribute:spectator:blurred | True | medium |
| cf15 | action_event | drift |  |  | visual_action | action_event:drift | True | low |
| cf16 | event_role | drift | agent | sports_car |  | event_role:drift:agent:sports_car | True | medium |
| cf17 | action_event | kick |  |  | body_motion_action, sports_action, visual_action | action_event:kick | True | high |
| cf18 | event_role | kick | agent | sports_car |  | event_role:kick:agent:sports_car | True | medium |
| cf19 | event_role | kick | patient | spray |  | event_role:kick:patient:spray | True | medium |
| cf20 | relation | sports_car | with | spoiler | association_relation, visual_relation | relation:sports_car:with:spoiler | True | high |
| cf21 | relation | sports_car | on | racetrack | spatial_support, visual_relation | relation:sports_car:on:racetrack | True | high |
| cf22 | relation | car | near | barrier | spatial_proximity, visual_relation | relation:car:near:barrier | True | high |

### Stage 9 Canonicalization Notes
_none_

## 38

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `21b77b6261e50dd4d7e003f906820e9804510119fdfbdec41cbd5c670cf17814`
**parse_path:** `sentence`

> Three people in chef hats gather around a table with a red-and-white checkered cloth. One holds a microphone while another wears purple gloves.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Three | three | exact_quantity | chunk0 | 0 | high |
| m2 | object | hats | hat | noun_chunk_root | chunk1 | 4 | high |
| m3 | attribute | chef | chef | compound_modifier | chunk1 | 3 | medium |
| m4 | object | table | table | noun_chunk_root | chunk2 | 8 | high |
| m5 | object | cloth | cloth | noun_chunk_root | chunk3 | 13 | high |
| m6 | attribute | red-and-white | red-and-white | modifier_attribute | chunk3 | 11 | medium |
| m7 | attribute | checkered | checkered | modifier_attribute | chunk3 | 12 | medium |
| m8 | object | microphone | microphone | noun_chunk_root | chunk4 | 18 | high |
| m9 | object | gloves | glove | noun_chunk_root | chunk6 | 23 | high |
| m10 | attribute | purple | purple | color_attribute | chunk6 | 22 | high |
| m11 | reference | One | one | singular_substitute | nominal_reference | 15 | high |
| m12 | reference | another | another | contrastive_reference | nominal_reference | 20 | high |
| m13 | action | gather | gather | verb_predicate | doc | 5 | high |
| m14 | action | holds | hold | verb_predicate | doc | 16 | high |
| m15 | action | wears | wear | verb_predicate | doc | 21 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> people |
| e1 | has_attribute | m2 | m3 | medium | chunk1 compound -> hats |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> cloth |
| e3 | has_attribute | m5 | m7 | medium | chunk3 amod -> cloth |
| e4 | has_attribute | m9 | m10 | high | chunk6 amod -> gloves |
| e5 | refers_to | m11 | m0 | high | singular_substitute One -> people; score=102 |
| e6 | refers_to | m12 | m0 | high | contrastive_reference another -> people; score=110 |
| e7 | agent | m13 | m0 | medium | nsubj -> gather |
| e8 | agent | m14 | m0 | medium | nsubj -> holds; resolved One -> people |
| e9 | patient | m14 | m8 | medium | dobj -> holds |
| e10 | agent | m15 | m0 | medium | nsubj -> wears; resolved another -> people |
| e11 | patient | m15 | m9 | medium | dobj -> wears |
| e12 | relation | m0 | m2 | high | in |
| e13 | relation | m0 | m4 | high | around |
| e14 | relation | m0 | m5 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | hat | hats | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:hat", "parents": []} |
| ent_m4 | object | table | table | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m4 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m5 | object | cloth | cloth | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:cloth", "parents": []} |
| ent_m8 | object | microphone | microphone | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:microphone", "parents": []} |
| ent_m9 | object | glove | gloves | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:glove", "parents": []} |
| eref_m11 | instance | people | One | person | raw_lemma | stage9_seed:parent_seed | person, human | m11 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| eref_m12 | contrastive_instance | people | another | person | raw_lemma | stage9_seed:parent_seed | person, human | m12 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m11 | eref_m11 | m0 | ent_m0 | high |  |
| refers_to | m12 | eref_m12 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m13 | gather | gather | gather | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:gather", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m14 | holds | hold | hold | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action |  | agent:m0->eref_m11; patient:m8->ent_m8 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce2 | m15 | wears | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m0->eref_m12; patient:m9->ent_m9 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | gather | agent | agent | none | m0 | ent_m0 | medium | e7 | nsubj -> gather |  |  |
| ce1 | hold | agent | agent | none | m0 | eref_m11 | medium | e8 | nsubj -> holds; resolved One -> people |  |  |
| ce1 | hold | patient | patient | none | m8 | ent_m8 | medium | e9 | dobj -> holds |  |  |
| ce2 | wear | agent | agent | none | m0 | eref_m12 | medium | e10 | nsubj -> wears; resolved another -> people |  |  |
| ce2 | wear | patient | patient | none | m9 | ent_m9 | medium | e11 | dobj -> wears |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e12 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | around | around | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e13 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | hat |  |  |  | entity_exists:hat | True | low |
| cf2 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf3 | entity_exists | cloth |  |  |  | entity_exists:cloth | True | low |
| cf4 | entity_exists | microphone |  |  |  | entity_exists:microphone | True | low |
| cf5 | entity_exists | glove |  |  |  | entity_exists:glove | True | low |
| cf6 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf7 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf8 | has_quantity | people | three |  | exact_quantity, quantity | has_quantity:people:three | True | high |
| cf9 | has_attribute | hat | chef |  | compound_modifier, visual_attribute | has_attribute:hat:chef | True | medium |
| cf10 | has_attribute | cloth | red-and-white |  | modifier_attribute, visual_attribute | has_attribute:cloth:red-and-white | True | medium |
| cf11 | has_attribute | cloth | checkered |  | pattern_attribute, pattern, pattern_marking, visual_attribute | has_attribute:cloth:checkered | True | medium |
| cf12 | has_attribute | glove | purple |  | color_attribute, color, visual_attribute | has_attribute:glove:purple | True | high |
| cf13 | action_event | gather |  |  | visual_action | action_event:gather | True | low |
| cf14 | event_role | gather | agent | people |  | event_role:gather:agent:people | True | medium |
| cf15 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf16 | event_role | hold | agent | people |  | event_role:hold:agent:people | True | medium |
| cf17 | event_role | hold | patient | microphone |  | event_role:hold:patient:microphone | True | medium |
| cf18 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf19 | event_role | wear | agent | people |  | event_role:wear:agent:people | True | medium |
| cf20 | event_role | wear | patient | glove |  | event_role:wear:patient:glove | True | medium |
| cf21 | relation | people | in | hat | spatial_containment, visual_relation | relation:people:in:hat | True | high |
| cf22 | relation | people | around | table | spatial_proximity, visual_relation | relation:people:around:table | True | high |
| cf23 | relation | people | with | cloth | association_relation, visual_relation | relation:people:with:cloth | True | high |

### Stage 9 Canonicalization Notes
_none_

## 39

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `23bf4db1d338eeb026dae8712121662f0c1266d75881e3ec3f904306ec635414`
**parse_path:** `tag_list`

> pink dress, smiling woman, nightclub, red carpet, bright lights

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | dress | dress | segment_head | t0 | 1 | high |
| m1 | attribute | pink | pink | attribute | t0 | 0 | high |
| m2 | object | woman | woman | segment_head | t1 | 1 | high |
| m3 | attribute | smiling | smile | state_attribute | t1 | 0 | high |
| m4 | object | nightclub | nightclub | segment_head | t2 | 0 | high |
| m5 | object | carpet | carpet | segment_head | t3 | 1 | high |
| m6 | attribute | red | red | attribute | t3 | 0 | high |
| m7 | object | lights | light | segment_head | t4 | 1 | high |
| m8 | attribute | bright | bright | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> dress |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> woman |
| e2 | has_attribute | m5 | m6 | high | t3 internal amod -> carpet |
| e3 | has_attribute | m7 | m8 | high | t4 internal amod -> lights |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | dress | dress | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m0 | raw_mention |  |  |  | True | {"canonical": "entity:dress", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m2 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m2 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m4 | object | nightclub | nightclub | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:nightclub", "parents": []} |
| ent_m5 | object | carpet | carpet | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:carpet", "parents": []} |
| ent_m7 | object | light | lights | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:light", "parents": []} |

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
| cf0 | entity_exists | dress |  |  | clothing, wearable | entity_exists:dress | True | high |
| cf1 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf2 | entity_exists | nightclub |  |  |  | entity_exists:nightclub | True | low |
| cf3 | entity_exists | carpet |  |  |  | entity_exists:carpet | True | low |
| cf4 | entity_exists | light |  |  |  | entity_exists:light | True | low |
| cf5 | has_attribute | dress | pink |  | color_attribute, color, visual_attribute | has_attribute:dress:pink | True | high |
| cf6 | has_attribute | woman | smile |  | state_attribute, visual_attribute | has_attribute:woman:smile | True | high |
| cf7 | has_attribute | carpet | red |  | color_attribute, color, visual_attribute | has_attribute:carpet:red | True | high |
| cf8 | has_attribute | light | bright |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:light:bright | True | high |

### Stage 9 Canonicalization Notes
_none_

## 40

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `23c4f99414a3c5572cc0f6a2e6fc8db0298987272ab0d4d316fea181c2abd414`
**parse_path:** `tag_list`

> white ibis, green grass, pink legs, wooden post

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | ibis | ibis | segment_head | t0 | 1 | high |
| m1 | attribute | white | white | attribute | t0 | 0 | high |
| m2 | object | grass | grass | segment_head | t1 | 1 | high |
| m3 | attribute | green | green | attribute | t1 | 0 | high |
| m4 | object | legs | leg | segment_head | t2 | 1 | high |
| m5 | attribute | pink | pink | attribute | t2 | 0 | high |
| m6 | object | post | post | segment_head | t3 | 1 | high |
| m7 | attribute | wooden | wooden | attribute | t3 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> ibis |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> grass |
| e2 | has_attribute | m4 | m5 | high | t2 internal compound -> legs |
| e3 | has_attribute | m6 | m7 | high | t3 internal compound -> post |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | ibis | ibis | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:ibis", "parents": []} |
| ent_m2 | object | grass | grass | object | raw_lemma | wordnet_synset:grass.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m2 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m4 | object | leg | legs | object | raw_lemma | stage9_seed:parent_seed | body_part | m4 | raw_mention |  |  |  | True | {"canonical": "entity:leg", "parents": ["entity_parent:body_part"]} |
| ent_m6 | object | post | post | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:post", "parents": []} |

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
| cf0 | entity_exists | ibis |  |  |  | entity_exists:ibis | True | low |
| cf1 | entity_exists | grass |  |  | plant, living_thing | entity_exists:grass | True | high |
| cf2 | entity_exists | leg |  |  | body_part | entity_exists:leg | True | high |
| cf3 | entity_exists | post |  |  |  | entity_exists:post | True | low |
| cf4 | has_attribute | ibis | white |  | color_attribute, color, visual_attribute | has_attribute:ibis:white | True | high |
| cf5 | has_attribute | grass | green |  | color_attribute, color, visual_attribute | has_attribute:grass:green | True | high |
| cf6 | has_attribute | leg | pink |  | color_attribute, color, visual_attribute | has_attribute:leg:pink | True | high |
| cf7 | has_attribute | post | wood |  | material_attribute, material, visual_attribute | has_attribute:post:wood | True | high |

### Stage 9 Canonicalization Notes
_none_

## 41

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `254553a6d15b56f433a2a33cbd7e89a5fd3f14719debd03c6ad04b19ca1c4814`
**parse_path:** `tag_list`

> graduation gown, peace sign, blue shirt, pink flip-flops

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | gown | gown | segment_head | t0 | 1 | high |
| m1 | attribute | graduation | graduation | attribute | t0 | 0 | high |
| m2 | object | sign | sign | segment_head | t1 | 1 | high |
| m3 | attribute | peace | peace | attribute | t1 | 0 | high |
| m4 | object | shirt | shirt | segment_head | t2 | 1 | high |
| m5 | attribute | blue | blue | attribute | t2 | 0 | high |
| m6 | object | flip-flops | flip-flop | segment_head | t3 | 1 | high |
| m7 | attribute | pink | pink | attribute | t3 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> gown |
| e1 | has_attribute | m2 | m3 | high | t1 internal compound -> sign |
| e2 | has_attribute | m4 | m5 | high | t2 internal amod -> shirt |
| e3 | has_attribute | m6 | m7 | high | t3 internal compound -> flip-flops |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | gown | gown | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:gown", "parents": []} |
| ent_m2 | object | sign | sign | document | raw_lemma | stage9_seed:parent_seed | text_carrier, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:sign", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m4 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m6 | object | flip-flop | flip-flops | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:flip-flop", "parents": []} |

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
| cf0 | entity_exists | gown |  |  |  | entity_exists:gown | True | low |
| cf1 | entity_exists | sign |  |  | text_carrier, artifact | entity_exists:sign | True | high |
| cf2 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf3 | entity_exists | flip-flop |  |  |  | entity_exists:flip-flop | True | low |
| cf4 | has_attribute | gown | graduation |  | attribute, visual_attribute | has_attribute:gown:graduation | True | high |
| cf5 | has_attribute | sign | peace |  | attribute, visual_attribute | has_attribute:sign:peace | True | high |
| cf6 | has_attribute | shirt | blue |  | color_attribute, color, visual_attribute | has_attribute:shirt:blue | True | high |
| cf7 | has_attribute | flip-flop | pink |  | color_attribute, color, visual_attribute | has_attribute:flip-flop:pink | True | high |

### Stage 9 Canonicalization Notes
_none_

## 42

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `262066ad0df4d8bd993f70f292e8635b3c2ea4919a2c29a06f0450ea51c45c14`
**parse_path:** `tag_list`

> wooden sign, forest, grass, trees

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | sign | sign | segment_head | t0 | 1 | high |
| m1 | attribute | wooden | wooden | attribute | t0 | 0 | high |
| m2 | object | forest | forest | segment_head | t1 | 0 | high |
| m3 | object | grass | grass | segment_head | t2 | 0 | high |
| m4 | object | trees | tree | segment_head | t3 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> sign |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sign | sign | document | raw_lemma | stage9_seed:parent_seed | text_carrier, artifact | m0 | raw_mention |  |  |  | True | {"canonical": "entity:sign", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m2 | object | forest | forest | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:forest", "parents": []} |
| ent_m3 | object | grass | grass | object | raw_lemma | wordnet_synset:grass.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m3 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m4 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m4 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |

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
| cf0 | entity_exists | sign |  |  | text_carrier, artifact | entity_exists:sign | True | high |
| cf1 | entity_exists | forest |  |  |  | entity_exists:forest | True | low |
| cf2 | entity_exists | grass |  |  | plant, living_thing | entity_exists:grass | True | high |
| cf3 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf4 | has_attribute | sign | wood |  | material_attribute, material, visual_attribute | has_attribute:sign:wood | True | high |

### Stage 9 Canonicalization Notes
_none_

## 43

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `28d1f982d6b2e250197d4b39be5e3b3bc35ea71b6c880d4180b4cd8e91f80814`
**parse_path:** `sentence`

> A group of low buildings with sloped roofs sits on a grassy hillside, surrounded by dense green bushes. Several cars are parked in a lot near the structures, with trees visible in the background under an overcast sky.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | group | group | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | buildings | building | noun_chunk_root | chunk1 | 4 | high |
| m2 | attribute | low | low | modifier_attribute | chunk1 | 3 | medium |
| m3 | object | roofs | roof | noun_chunk_root | chunk2 | 7 | high |
| m4 | attribute | sloped | sloped | modifier_attribute | chunk2 | 6 | medium |
| m5 | object | hillside | hillside | noun_chunk_root | chunk3 | 12 | high |
| m6 | attribute | grassy | grassy | modifier_attribute | chunk3 | 11 | medium |
| m7 | object | bushes | bush | noun_chunk_root | chunk4 | 18 | high |
| m8 | attribute | dense | dense | modifier_attribute | chunk4 | 16 | medium |
| m9 | attribute | green | green | color_attribute | chunk4 | 17 | high |
| m10 | object | cars | car | noun_chunk_root | chunk5 | 21 | high |
| m11 | quantity | Several | several | approximate_quantity | chunk5 | 20 | medium |
| m12 | object | lot | lot | noun_chunk_root | chunk6 | 26 | high |
| m13 | object | structures | structure | noun_chunk_root | chunk7 | 29 | high |
| m14 | object | trees | tree | noun_chunk_root | chunk8 | 32 | high |
| m15 | context | background | background | scene_context | chunk9 | 36 | high |
| m16 | object | sky | sky | noun_chunk_root | chunk10 | 40 | high |
| m17 | attribute | overcast | overcast | modifier_attribute | chunk10 | 39 | medium |
| m18 | action | sits | sit | verb_predicate | doc | 8 | high |
| m19 | action | surrounded | surround | verb_predicate | doc | 14 | high |
| m20 | action | parked | park | verb_predicate | doc | 23 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 amod -> buildings |
| e1 | has_attribute | m3 | m4 | medium | chunk2 amod -> roofs |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> hillside |
| e3 | has_attribute | m7 | m8 | medium | chunk4 amod -> bushes |
| e4 | has_attribute | m7 | m9 | high | chunk4 amod -> bushes |
| e5 | has_quantity | m10 | m11 | medium | chunk5 quantity -> cars |
| e6 | has_context | scene | m15 | high | scene_context token background |
| e7 | has_attribute | m16 | m17 | medium | chunk10 amod -> sky |
| e8 | agent | m18 | m0 | medium | nsubj -> sits |
| e9 | agent | m19 | m0 | medium | inherited agent advcl -> sits |
| e10 | agent | m20 | m10 | medium | nsubjpass -> parked |
| e11 | relation | m0 | m1 | medium | of |
| e12 | relation | m1 | m3 | high | with |
| e13 | relation | m0 | m5 | high | on |
| e14 | relation | m0 | m7 | medium | by |
| e15 | relation | m10 | m12 | high | in |
| e16 | relation | m12 | m13 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | group | group | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:group", "parents": []} |
| ent_m1 | object | building | buildings | object | raw_lemma | wordnet_synset:building.n.01 + stage9_audit | structure, artifact | m1 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m3 | object | roof | roofs | object | raw_lemma | wordnet_synset:roof.n.01 + stage9_audit | architectural_part, structure, artifact | m3 | raw_mention |  |  |  | True | {"canonical": "entity:roof", "parents": ["entity_parent:architectural_part", "entity_parent:structure", "entity_parent:artifact"]} |
| ent_m5 | object | hillside | hillside | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:hillside", "parents": []} |
| ent_m7 | object | bush | bushes | object | raw_lemma | wordnet_synset:shrub.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m7 | raw_mention |  |  |  | True | {"canonical": "entity:bush", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m10 | object | car | cars | vehicle | raw_lemma | stage9_seed:parent_seed | vehicle | m10 | raw_mention |  |  |  | True | {"canonical": "entity:car", "parents": ["entity_parent:vehicle"]} |
| ent_m12 | object | lot | lot | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:lot", "parents": []} |
| ent_m13 | object | structure | structures | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:structure", "parents": []} |
| ent_m14 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m14 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m15 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m15 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m16 | object | sky | sky | object | raw_lemma | wordnet_synset:sky.n.01 + stage9_audit | natural_scene | m16 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": ["entity_parent:natural_scene"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | sits | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m19 | surrounded | surround | surround | raw_action | wordnet_synset:surround.v.01 + stage9_audit | spatial_configuration_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:surround", "parents": ["action_parent:spatial_configuration_action", "action_parent:visual_action"]} |  |
| ce2 | m20 | parked | park | park | raw_action | visual_action_fallback | visual_action |  | patient<-theme[passive_to_active]:m10->ent_m10 | {"canonical": "action:park", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | agent | none | m0 | ent_m0 | medium | e8 | nsubj -> sits |  |  |
| ce1 | surround | agent | agent | none | m0 | ent_m0 | medium | e9 | inherited agent advcl -> sits |  |  |
| ce2 | park | patient | theme | passive_to_active | m10 | ent_m10 | medium | e10 | nsubjpass -> parked |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e11 | False | False |  |  |
| cr1 | m1 | m3 | ent_m1 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e12 | False | False |  |  |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e13 | False | False |  |  |
| cr3 | m0 | m7 | ent_m0 | ent_m7 | by | by | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | medium | e14 | False | False |  |  |
| cr4 | m10 | m12 | ent_m10 | ent_m12 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e15 | False | False |  |  |
| cr5 | m12 | m13 | ent_m12 | ent_m13 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | group |  |  |  | entity_exists:group | True | low |
| cf1 | entity_exists | building |  |  | structure, artifact | entity_exists:building | True | high |
| cf2 | entity_exists | roof |  |  | architectural_part, structure, artifact | entity_exists:roof | True | high |
| cf3 | entity_exists | hillside |  |  |  | entity_exists:hillside | True | low |
| cf4 | entity_exists | bush |  |  | plant, living_thing | entity_exists:bush | True | high |
| cf5 | entity_exists | car |  |  | vehicle | entity_exists:car | True | high |
| cf6 | entity_exists | lot |  |  |  | entity_exists:lot | True | low |
| cf7 | entity_exists | structure |  |  |  | entity_exists:structure | True | low |
| cf8 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf9 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf10 | entity_exists | sky |  |  | natural_scene | entity_exists:sky | True | high |
| cf11 | has_attribute | building | low |  | size_attribute, height, visual_attribute | has_attribute:building:low | True | medium |
| cf12 | has_attribute | roof | sloped |  | modifier_attribute, visual_attribute | has_attribute:roof:sloped | True | medium |
| cf13 | has_attribute | hillside | grassy |  | modifier_attribute, visual_attribute | has_attribute:hillside:grassy | True | medium |
| cf14 | has_attribute | bush | dense |  | modifier_attribute, visual_attribute | has_attribute:bush:dense | True | medium |
| cf15 | has_attribute | bush | green |  | color_attribute, color, visual_attribute | has_attribute:bush:green | True | high |
| cf16 | has_quantity | car | several |  | approximate_quantity, quantity | has_quantity:car:several | True | medium |
| cf17 | has_attribute | sky | overcast |  | weather_attribute, weather, visual_attribute | has_attribute:sky:overcast | True | medium |
| cf18 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf19 | event_role | sit | agent | group |  | event_role:sit:agent:group | True | medium |
| cf20 | action_event | surround |  |  | spatial_configuration_action, visual_action | action_event:surround | True | high |
| cf21 | event_role | surround | agent | group |  | event_role:surround:agent:group | True | medium |
| cf22 | action_event | park |  |  | visual_action | action_event:park | True | low |
| cf23 | event_role | park | patient | car |  | event_role:park:patient:car | True | medium |
| cf24 | relation | group | of | building | part_relation, visual_relation | relation:group:of:building | True | medium |
| cf25 | relation | building | with | roof | association_relation, visual_relation | relation:building:with:roof | True | high |
| cf26 | relation | group | on | hillside | spatial_support, visual_relation | relation:group:on:hillside | True | high |
| cf27 | relation | group | by | bush | spatial_proximity, visual_relation | relation:group:by:bush | True | medium |
| cf28 | relation | car | in | lot | spatial_containment, visual_relation | relation:car:in:lot | True | high |
| cf29 | relation | lot | near | structure | spatial_proximity, visual_relation | relation:lot:near:structure | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m20 | e10 | m10 |  |  | {"action_mention_id": "m20", "kind": "passive_subject_to_patient", "raw_edge_id": "e10", "raw_role": "theme", "role": "patient", "target": "m10", "voice_normalization": "passive_to_active"} |

## 44

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `298e72b9114fdb8b403da1bcfc25f1e88a340029bc672fc863e9884ec53b7414`
**parse_path:** `tag_list`

> water, buildings, skyline, dock, calm

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | water | water | segment_head | t0 | 0 | high |
| m1 | object | buildings | building | segment_head | t1 | 0 | high |
| m2 | object | skyline | skyline | segment_head | t2 | 0 | high |
| m3 | object | dock | dock | segment_head | t3 | 0 | high |
| m4 | object | calm | calm | segment_head | t4 | 0 | high |

### Raw Concept Edges
_none_

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | water | water | object | raw_lemma | wordnet_synset:water.n.01 + stage9_audit | natural_element | m0 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": ["entity_parent:natural_element"]} |
| ent_m1 | object | building | buildings | object | raw_lemma | wordnet_synset:building.n.01 + stage9_audit | structure, artifact | m1 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m2 | object | skyline | skyline | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:skyline", "parents": []} |
| ent_m3 | object | dock | dock | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:dock", "parents": []} |
| ent_m4 | object | calm | calm | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:calm", "parents": []} |

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
| cf0 | entity_exists | water |  |  | natural_element | entity_exists:water | True | high |
| cf1 | entity_exists | building |  |  | structure, artifact | entity_exists:building | True | high |
| cf2 | entity_exists | skyline |  |  |  | entity_exists:skyline | True | low |
| cf3 | entity_exists | dock |  |  |  | entity_exists:dock | True | low |
| cf4 | entity_exists | calm |  |  |  | entity_exists:calm | True | low |

### Stage 9 Canonicalization Notes
_none_

## 45

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `29bc2961cae2b204fdf2fa9648b6df7ebbfeedfd6a0887d5ad283a4b4593a814`
**parse_path:** `sentence`

> Several children sit on the floor around a large cardboard game mat with a space-themed design. One boy in an orange shirt holds a controller, while others watch or sit nearby with their own controllers and small yellow robots.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | children | child | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Several | several | approximate_quantity | chunk0 | 0 | medium |
| m2 | object | floor | floor | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | mat | mat | noun_chunk_root | chunk2 | 11 | high |
| m4 | attribute | large | large | size_attribute | chunk2 | 8 | high |
| m5 | attribute | cardboard | cardboard | compound_modifier | chunk2 | 9 | medium |
| m6 | attribute | game | game | compound_modifier | chunk2 | 10 | medium |
| m7 | object | design | design | noun_chunk_root | chunk3 | 15 | high |
| m8 | attribute | space-themed | space-themed | modifier_attribute | chunk3 | 14 | medium |
| m9 | object | boy | boy | noun_chunk_root | chunk4 | 18 | high |
| m10 | quantity | One | one | exact_quantity | chunk4 | 17 | high |
| m11 | object | shirt | shirt | noun_chunk_root | chunk5 | 22 | high |
| m12 | attribute | orange | orange | color_attribute | chunk5 | 21 | high |
| m13 | object | controller | controller | noun_chunk_root | chunk6 | 25 | high |
| m14 | object | controllers | controller | noun_chunk_root | chunk8 | 36 | high |
| m15 | attribute | own | own | modifier_attribute | chunk8 | 35 | medium |
| m16 | object | robots | robot | noun_chunk_root | chunk9 | 40 | high |
| m17 | attribute | small | small | size_attribute | chunk9 | 38 | high |
| m18 | attribute | yellow | yellow | color_attribute | chunk9 | 39 | high |
| m19 | reference | others | other | contrastive_reference | nominal_reference | 28 | high |
| m20 | action | sit | sit | verb_predicate | doc | 2 | high |
| m21 | action | holds | hold | verb_predicate | doc | 23 | high |
| m22 | action | watch | watch | verb_predicate | doc | 29 | high |
| m23 | action | sit | sit | verb_predicate | doc | 31 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | medium | chunk0 quantity -> children |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> mat |
| e2 | has_attribute | m3 | m5 | medium | chunk2 compound -> mat |
| e3 | has_attribute | m3 | m6 | medium | chunk2 compound -> mat |
| e4 | has_attribute | m7 | m8 | medium | chunk3 amod -> design |
| e5 | has_quantity | m9 | m10 | high | chunk4 quantity -> boy |
| e6 | has_attribute | m11 | m12 | high | chunk5 amod -> shirt |
| e7 | has_attribute | m14 | m15 | medium | chunk8 amod -> controllers |
| e8 | has_attribute | m16 | m17 | high | chunk9 amod -> robots |
| e9 | has_attribute | m16 | m18 | high | chunk9 amod -> robots |
| e10 | refers_to | m19 | m0 | high | contrastive_reference others -> children; score=110 |
| e11 | agent | m20 | m0 | medium | nsubj -> sit |
| e12 | agent | m21 | m9 | medium | nsubj -> holds |
| e13 | patient | m21 | m13 | medium | dobj -> holds |
| e14 | agent | m22 | m0 | medium | nsubj -> watch; resolved others -> children |
| e15 | agent | m23 | m0 | medium | inherited agent conj -> watch |
| e16 | relation | m0 | m2 | high | on |
| e17 | relation | m0 | m3 | high | around |
| e18 | relation | m3 | m7 | high | with |
| e19 | relation | m9 | m11 | high | in |
| e20 | relation | m0 | m14 | high | with |
| e21 | relation | m0 | m16 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | child | children | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | floor | floor | object | raw_lemma | wordnet_synset:floor.n.01 + stage9_audit | architectural_part, surface, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:floor", "parents": ["entity_parent:architectural_part", "entity_parent:surface", "entity_parent:artifact"]} |
| ent_m3 | object | mat | mat | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:mat", "parents": []} |
| ent_m7 | object | design | design | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:design", "parents": []} |
| ent_m9 | object | boy | boy | person | raw_lemma | stage9_seed:parent_seed | person, human | m9 | raw_mention |  |  |  | True | {"canonical": "entity:boy", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m11 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m11 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m13 | object | controller | controller | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:controller", "parents": []} |
| ent_m14 | object | controller | controllers | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:controller", "parents": []} |
| ent_m16 | object | robot | robots | object | raw_lemma | none |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:robot", "parents": []} |
| eref_m19 | complement_subset | child | others | person | raw_lemma | stage9_seed:parent_seed | person, human | m19 | stage9_reference | ent_m0 |  | many | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m19 | eref_m19 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m20 | sit | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m21 | holds | hold | hold | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action |  | agent:m9->ent_m9; patient:m13->ent_m13 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce2 | m22 | watch | watch | watch | raw_action | stage9_seed:parent_seed | gaze_action, visual_action |  | agent:m0->eref_m19 | {"canonical": "action:watch", "parents": ["action_parent:gaze_action", "action_parent:visual_action"]} |  |
| ce3 | m23 | sit | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->eref_m19 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | agent | none | m0 | ent_m0 | medium | e11 | nsubj -> sit |  |  |
| ce1 | hold | agent | agent | none | m9 | ent_m9 | medium | e12 | nsubj -> holds |  |  |
| ce1 | hold | patient | patient | none | m13 | ent_m13 | medium | e13 | dobj -> holds |  |  |
| ce2 | watch | agent | agent | none | m0 | eref_m19 | medium | e14 | nsubj -> watch; resolved others -> children |  |  |
| ce3 | sit | agent | agent | none | m0 | eref_m19 | medium | e15 | inherited agent conj -> watch |  | conj_agent_inherited_from_reference_canonical_target |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e16 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | around | around | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e17 | False | False |  |  |
| cr2 | m3 | m7 | ent_m3 | ent_m7 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e18 | False | False |  |  |
| cr3 | m9 | m11 | ent_m9 | ent_m11 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e19 | False | False |  |  |
| cr4 | m0 | m14 | ent_m0 | ent_m14 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e20 | False | False |  |  |
| cr5 | m0 | m16 | ent_m0 | ent_m16 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e21 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf1 | entity_exists | floor |  |  | architectural_part, surface, artifact | entity_exists:floor | True | high |
| cf2 | entity_exists | mat |  |  |  | entity_exists:mat | True | low |
| cf3 | entity_exists | design |  |  |  | entity_exists:design | True | low |
| cf4 | entity_exists | boy |  |  | person, human | entity_exists:boy | True | high |
| cf5 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf6 | entity_exists | controller |  |  |  | entity_exists:controller | True | low |
| cf7 | entity_exists | controller |  |  |  | entity_exists:controller | True | low |
| cf8 | entity_exists | robot |  |  |  | entity_exists:robot | True | low |
| cf9 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf10 | has_quantity | child | several |  | approximate_quantity, quantity | has_quantity:child:several | True | medium |
| cf11 | has_attribute | mat | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:mat:large | True | high |
| cf12 | has_attribute | mat | cardboard |  | material_attribute, material, visual_attribute | has_attribute:mat:cardboard | True | medium |
| cf13 | has_attribute | mat | game |  | compound_modifier, visual_attribute | has_attribute:mat:game | True | medium |
| cf14 | has_attribute | design | space-themed |  | modifier_attribute, visual_attribute | has_attribute:design:space-themed | True | medium |
| cf15 | has_quantity | boy | one |  | exact_quantity, quantity | has_quantity:boy:one | True | high |
| cf16 | has_attribute | shirt | orange |  | color_attribute, color, visual_attribute | has_attribute:shirt:orange | True | high |
| cf17 | has_attribute | controller | own |  | modifier_attribute, visual_attribute | has_attribute:controller:own | True | medium |
| cf18 | has_attribute | robot | small |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:robot:small | True | high |
| cf19 | has_attribute | robot | yellow |  | color_attribute, color, visual_attribute | has_attribute:robot:yellow | True | high |
| cf20 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf21 | event_role | sit | agent | child |  | event_role:sit:agent:child | True | medium |
| cf22 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf23 | event_role | hold | agent | boy |  | event_role:hold:agent:boy | True | medium |
| cf24 | event_role | hold | patient | controller |  | event_role:hold:patient:controller | True | medium |
| cf25 | action_event | watch |  |  | gaze_action, visual_action | action_event:watch | True | medium |
| cf26 | event_role | watch | agent | child |  | event_role:watch:agent:child | True | medium |
| cf27 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf28 | event_role | sit | agent | child |  | event_role:sit:agent:child | True | medium |
| cf29 | relation | child | on | floor | spatial_support, visual_relation | relation:child:on:floor | True | high |
| cf30 | relation | child | around | mat | spatial_proximity, visual_relation | relation:child:around:mat | True | high |
| cf31 | relation | mat | with | design | association_relation, visual_relation | relation:mat:with:design | True | high |
| cf32 | relation | boy | in | shirt | spatial_containment, visual_relation | relation:boy:in:shirt | True | high |
| cf33 | relation | child | with | controller | association_relation, visual_relation | relation:child:with:controller | True | high |
| cf34 | relation | child | with | robot | association_relation, visual_relation | relation:child:with:robot | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| conj_agent_reference_target_inherited | m23 |  |  | eref_m19 |  | {"action_mention_id": "m23", "canonical_target": "eref_m19", "kind": "conj_agent_reference_target_inherited", "source_action_mention_id": "m22"} |

## 46

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `2b0e504a3dfe9f3d5c46371be0785cb6fa6ec9f2bb9b6fffe1ccd3633fb63c14`
**parse_path:** `sentence`

> A football player in a white uniform runs on a field. A truck is parked in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | football player | football_player | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | uniform | uniform | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | white | white | color_attribute | chunk1 | 4 | high |
| m3 | object | field | field | noun_chunk_root | chunk2 | 9 | high |
| m4 | object | truck | truck | noun_chunk_root | chunk3 | 12 | high |
| m5 | context | background | background | scene_context | chunk4 | 17 | high |
| m6 | action | runs | run | verb_predicate | doc | 6 | high |
| m7 | action | parked | park | verb_predicate | doc | 14 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> uniform |
| e1 | has_context | scene | m5 | high | scene_context token background |
| e2 | agent | m6 | m0 | medium | nsubj -> runs |
| e3 | agent | m7 | m4 | medium | nsubjpass -> parked |
| e4 | relation | m0 | m1 | high | in |
| e5 | relation | m0 | m3 | high | on |
| e6 | relation | m4 | m5 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | football_player | football player | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:football_player", "parents": []} |
| ent_m1 | object | uniform | uniform | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | field | field | object | raw_lemma | wordnet_synset:field.n.01 + stage9_audit | outdoor_scene, place | m3 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": ["entity_parent:outdoor_scene", "entity_parent:place"]} |
| ent_m4 | object | truck | truck | vehicle | raw_lemma | stage9_seed:parent_seed | vehicle | m4 | raw_mention |  |  |  | True | {"canonical": "entity:truck", "parents": ["entity_parent:vehicle"]} |
| ent_m5 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m5 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m6 | runs | run | run | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:run", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m7 | parked | park | park | raw_action | visual_action_fallback | visual_action |  | patient<-theme[passive_to_active]:m4->ent_m4 | {"canonical": "action:park", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | run | agent | agent | none | m0 | ent_m0 | medium | e2 | nsubj -> runs |  |  |
| ce1 | park | patient | theme | passive_to_active | m4 | ent_m4 | medium | e3 | nsubjpass -> parked |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e4 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e5 | False | False |  |  |
| cr2 | m4 | m5 | ent_m4 | ent_m5 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e6 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | football_player |  |  |  | entity_exists:football_player | True | high |
| cf1 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf2 | entity_exists | field |  |  | outdoor_scene, place | entity_exists:field | True | medium |
| cf3 | entity_exists | truck |  |  | vehicle | entity_exists:truck | True | high |
| cf4 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf5 | has_attribute | uniform | white |  | color_attribute, color, visual_attribute | has_attribute:uniform:white | True | high |
| cf6 | action_event | run |  |  | locomotion_action, visual_action | action_event:run | True | high |
| cf7 | event_role | run | agent | football_player |  | event_role:run:agent:football_player | True | medium |
| cf8 | action_event | park |  |  | visual_action | action_event:park | True | low |
| cf9 | event_role | park | patient | truck |  | event_role:park:patient:truck | True | medium |
| cf10 | relation | football_player | in | uniform | spatial_containment, visual_relation | relation:football_player:in:uniform | True | high |
| cf11 | relation | football_player | on | field | spatial_support, visual_relation | relation:football_player:on:field | True | high |
| cf12 | relation | truck | in | background | spatial_containment, visual_relation | relation:truck:in:background | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m7 | e3 | m4 |  |  | {"action_mention_id": "m7", "kind": "passive_subject_to_patient", "raw_edge_id": "e3", "raw_role": "theme", "role": "patient", "target": "m4", "voice_normalization": "passive_to_active"} |

## 47

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `2b5e6f052ecfd896d720ab9365f0f9b273e34cdbe78df4ae64f5a3a913a75814`
**parse_path:** `tag_list`

> paper lanterns, red frame, sunlight, sky

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | lanterns | lantern | segment_head | t0 | 1 | high |
| m1 | attribute | paper | paper | attribute | t0 | 0 | high |
| m2 | object | frame | frame | segment_head | t1 | 1 | high |
| m3 | attribute | red | red | attribute | t1 | 0 | high |
| m4 | object | sunlight | sunlight | segment_head | t2 | 0 | high |
| m5 | object | sky | sky | segment_head | t3 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> lanterns |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> frame |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | lantern | lanterns | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:lantern", "parents": []} |
| ent_m2 | object | frame | frame | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:frame", "parents": []} |
| ent_m4 | object | sunlight | sunlight | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:sunlight", "parents": []} |
| ent_m5 | object | sky | sky | object | raw_lemma | wordnet_synset:sky.n.01 + stage9_audit | natural_scene | m5 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": ["entity_parent:natural_scene"]} |

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
| cf0 | entity_exists | lantern |  |  |  | entity_exists:lantern | True | low |
| cf1 | entity_exists | frame |  |  |  | entity_exists:frame | True | low |
| cf2 | entity_exists | sunlight |  |  |  | entity_exists:sunlight | True | low |
| cf3 | entity_exists | sky |  |  | natural_scene | entity_exists:sky | True | high |
| cf4 | has_attribute | lantern | paper |  | material_attribute, material, visual_attribute | has_attribute:lantern:paper | True | high |
| cf5 | has_attribute | frame | red |  | color_attribute, color, visual_attribute | has_attribute:frame:red | True | high |

### Stage 9 Canonicalization Notes
_none_

## 48

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `2c3ac13ef1426602d87224ebf0ca08623c9a8a06b92346eef8261c1e22d06014`
**parse_path:** `tag_list`

> earth conference, panel, speakers, audience, table, bottles

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | conference | conference | segment_head | t0 | 1 | high |
| m1 | attribute | earth | earth | attribute | t0 | 0 | high |
| m2 | object | panel | panel | segment_head | t1 | 0 | high |
| m3 | object | speakers | speaker | segment_head | t2 | 0 | high |
| m4 | object | audience | audience | segment_head | t3 | 0 | high |
| m5 | object | table | table | segment_head | t4 | 0 | high |
| m6 | object | bottles | bottle | segment_head | t5 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> conference |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | conference | conference | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:conference", "parents": []} |
| ent_m2 | object | panel | panel | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:panel", "parents": []} |
| ent_m3 | object | speaker | speakers | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:speaker", "parents": []} |
| ent_m4 | object | audience | audience | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:audience", "parents": []} |
| ent_m5 | object | table | table | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m5 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m6 | object | bottle | bottles | object | raw_lemma | COCO object label + wordnet_hypernym:container.n.01 + stage9_audit | container, artifact | m6 | raw_mention |  |  |  | True | {"canonical": "entity:bottle", "parents": ["entity_parent:container", "entity_parent:artifact"]} |

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
| cf0 | entity_exists | conference |  |  |  | entity_exists:conference | True | low |
| cf1 | entity_exists | panel |  |  |  | entity_exists:panel | True | low |
| cf2 | entity_exists | speaker |  |  |  | entity_exists:speaker | True | low |
| cf3 | entity_exists | audience |  |  |  | entity_exists:audience | True | low |
| cf4 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf5 | entity_exists | bottle |  |  | container, artifact | entity_exists:bottle | True | high |
| cf6 | has_attribute | conference | earth |  | attribute, visual_attribute | has_attribute:conference:earth | True | high |

### Stage 9 Canonicalization Notes
_none_

## 49

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `2c4da3fcc17b0b481765e63a09cfdbf0db871933a6e428c35499eec13e49d414`
**parse_path:** `sentence`

> A small, fluffy puppy with dark brown and white fur lies on a red patterned surface. Its tongue is slightly out, and it rests near green leaves and a metal grate in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | puppy | puppy | noun_chunk_root | chunk0 | 4 | high |
| m1 | attribute | small | small | size_attribute | chunk0 | 1 | high |
| m2 | attribute | fluffy | fluffy | modifier_attribute | chunk0 | 3 | medium |
| m3 | object | fur | fur | noun_chunk_root | chunk1 | 10 | high |
| m4 | attribute | dark | dark | visual_attribute | chunk1 | 6 | medium |
| m5 | attribute | brown | brown | color_attribute | chunk1 | 7 | high |
| m6 | attribute | white | white | color_attribute | chunk1 | 9 | high |
| m7 | context | surface | surface | spatial_region | chunk2 | 16 | medium |
| m8 | object | tongue | tongue | noun_chunk_root | chunk3 | 19 | high |
| m9 | object | leaves | leaf | noun_chunk_root | chunk5 | 29 | high |
| m10 | attribute | green | green | color_attribute | chunk5 | 28 | high |
| m11 | object | grate | grate | noun_chunk_root | chunk6 | 33 | high |
| m12 | attribute | metal | metal | material_attribute | chunk6 | 32 | high |
| m13 | context | background | background | scene_context | chunk7 | 36 | high |
| m14 | action | lies | lie | verb_predicate | doc | 11 | high |
| m15 | action | rests | rest | verb_predicate | doc | 26 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> puppy |
| e1 | has_attribute | m0 | m2 | medium | chunk0 amod -> puppy |
| e2 | has_attribute | m3 | m4 | medium | chunk1 amod -> fur |
| e3 | has_attribute | m3 | m5 | high | chunk1 amod -> fur |
| e4 | has_attribute | m3 | m6 | high | chunk1 conj -> fur |
| e5 | has_attribute | m9 | m10 | high | chunk5 amod -> leaves |
| e6 | has_attribute | m11 | m12 | high | chunk6 compound -> grate |
| e7 | has_context | scene | m13 | high | scene_context token background |
| e8 | agent | m14 | m0 | medium | nsubj -> lies |
| e9 | agent | m15 | m8 | medium | nsubj -> rests; resolved it -> tongue |
| e10 | relation | m0 | m3 | high | with |
| e11 | relation | m0 | m7 | high | on |
| e12 | relation | m8 | m9 | high | near |
| e13 | relation | m8 | m11 | high | near |
| e14 | relation | m8 | m13 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | dog | puppy | object | wordnet_synset:puppy.n.01 + stage9_audit | stage9_seed:parent_seed | animal, living_thing | m0 | raw_mention |  |  |  | True | {"canonical": "entity:dog", "parents": ["entity_parent:animal", "entity_parent:living_thing"]} |
| ent_m3 | object | fur | fur | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:fur", "parents": []} |
| ent_m7 | context | surface | surface | object | raw_lemma | semantic_type_fallback | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": ["entity_parent:scene_context"]} |
| ent_m8 | object | tongue | tongue | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:tongue", "parents": []} |
| ent_m9 | object | leaf | leaves | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:leaf", "parents": []} |
| ent_m11 | object | grate | grate | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:grate", "parents": []} |
| ent_m13 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m13 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m14 | lies | lie | lie | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:lie", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m15 | rests | rest | rest | raw_action | wordnet_synset:rest.v.01 + stage9_audit | support_state_action, visual_action |  | agent:m8->ent_m8 | {"canonical": "action:rest", "parents": ["action_parent:support_state_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | lie | agent | agent | none | m0 | ent_m0 | medium | e8 | nsubj -> lies |  |  |
| ce1 | rest | agent | agent | none | m8 | ent_m8 | medium | e9 | nsubj -> rests; resolved it -> tongue |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e10 | False | False |  |  |
| cr1 | m0 | m7 | ent_m0 | ent_m7 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e11 | False | False |  |  |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e12 | False | False |  |  |
| cr3 | m8 | m11 | ent_m8 | ent_m11 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e13 | False | False |  |  |
| cr4 | m8 | m13 | ent_m8 | ent_m13 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e14 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | dog |  |  | animal, living_thing | entity_exists:dog | True | high |
| cf1 | entity_exists | fur |  |  |  | entity_exists:fur | True | low |
| cf2 | entity_exists | surface |  |  | scene_context | entity_exists:surface | True | medium |
| cf3 | entity_exists | tongue |  |  |  | entity_exists:tongue | True | low |
| cf4 | entity_exists | leaf |  |  |  | entity_exists:leaf | True | low |
| cf5 | entity_exists | grate |  |  |  | entity_exists:grate | True | low |
| cf6 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf7 | has_attribute | dog | small |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:dog:small | True | high |
| cf8 | has_attribute | dog | fluffy |  | material_attribute, clean_exact_overlap, material, texture, visual_attribute | has_attribute:dog:fluffy | True | medium |
| cf9 | has_attribute | fur | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:fur:dark | True | medium |
| cf10 | has_attribute | fur | brown |  | color_attribute, color, visual_attribute | has_attribute:fur:brown | True | high |
| cf11 | has_attribute | fur | white |  | color_attribute, color, visual_attribute | has_attribute:fur:white | True | high |
| cf12 | has_attribute | leaf | green |  | color_attribute, color, visual_attribute | has_attribute:leaf:green | True | high |
| cf13 | has_attribute | grate | metal |  | material_attribute, material, non_textile_material_type, visual_attribute | has_attribute:grate:metal | True | high |
| cf14 | action_event | lie |  |  | body_pose_action, visual_action | action_event:lie | True | high |
| cf15 | event_role | lie | agent | dog |  | event_role:lie:agent:dog | True | medium |
| cf16 | action_event | rest |  |  | support_state_action, visual_action | action_event:rest | True | medium |
| cf17 | event_role | rest | agent | tongue |  | event_role:rest:agent:tongue | True | medium |
| cf18 | relation | dog | with | fur | association_relation, visual_relation | relation:dog:with:fur | True | high |
| cf19 | relation | dog | on | surface | spatial_support, visual_relation | relation:dog:on:surface | True | high |
| cf20 | relation | tongue | near | leaf | spatial_proximity, visual_relation | relation:tongue:near:leaf | True | high |
| cf21 | relation | tongue | near | grate | spatial_proximity, visual_relation | relation:tongue:near:grate | True | high |
| cf22 | relation | tongue | in | background | spatial_containment, visual_relation | relation:tongue:in:background | True | high |

### Stage 9 Canonicalization Notes
_none_

## 50

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `2d0230ba6335e97bbe7364ebe789b70f12ee54c828a585897b561771da019014`
**parse_path:** `tag_list`

> octopus, greens, plate, garnish, sauce

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | octopus | octopus | segment_head | t0 | 0 | high |
| m1 | attribute | greens | green | color_attribute | t1 | 0 | high |
| m2 | object | plate | plate | segment_head | t2 | 0 | high |
| m3 | object | garnish | garnish | segment_head | t3 | 0 | high |
| m4 | object | sauce | sauce | segment_head | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | candidate_has_attribute | m0 | m1 | low | t1 adjacent floating attribute |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | octopus | octopus | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:octopus", "parents": []} |
| ent_m2 | object | plate | plate | object | raw_lemma | wordnet_synset:plate.n.04 + stage9_audit | dishware, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:plate", "parents": ["entity_parent:dishware", "entity_parent:artifact"]} |
| ent_m3 | object | garnish | garnish | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:garnish", "parents": []} |
| ent_m4 | object | sauce | sauce | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:sauce", "parents": []} |

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
| cf0 | entity_exists | octopus |  |  |  | entity_exists:octopus | True | low |
| cf1 | entity_exists | plate |  |  | dishware, artifact | entity_exists:plate | True | high |
| cf2 | entity_exists | garnish |  |  |  | entity_exists:garnish | True | low |
| cf3 | entity_exists | sauce |  |  |  | entity_exists:sauce | True | low |
| cf4 | candidate_has_attribute | octopus | green |  | color_attribute, color, visual_attribute | candidate_has_attribute:octopus:green | False | low |

### Stage 9 Canonicalization Notes
_none_

## 51

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `2d2ec1363c601d308f6db4facfe8c20b92bbb05e3abd446e2b59502bef3b0014`
**parse_path:** `sentence`

> A kitchen with wooden cabinets and a countertop sink is shown. A dining table with chairs sits to the left, near a window with patterned curtains. A ceiling fan hangs above, and a red popcorn machine stands in the corner.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | kitchen | kitchen | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | cabinets | cabinet | noun_chunk_root | chunk1 | 4 | high |
| m2 | attribute | wooden | wooden | material_attribute | chunk1 | 3 | high |
| m3 | object | sink | sink | noun_chunk_root | chunk2 | 8 | high |
| m4 | attribute | countertop | countertop | compound_modifier | chunk2 | 7 | medium |
| m5 | object | dining table | dining_table | noun_chunk_root | chunk3 | 13 | high |
| m6 | object | chairs | chair | noun_chunk_root | chunk4 | 15 | high |
| m7 | context | left | left | spatial_region | chunk5 | 19 | medium |
| m8 | object | window | window | noun_chunk_root | chunk6 | 23 | high |
| m9 | object | curtains | curtain | noun_chunk_root | chunk7 | 26 | high |
| m10 | attribute | patterned | patterned | modifier_attribute | chunk7 | 25 | medium |
| m11 | object | ceiling fan | ceiling_fan | noun_chunk_root | chunk8 | 29 | high |
| m12 | object | machine | machine | noun_chunk_root | chunk9 | 37 | high |
| m13 | attribute | red | red | color_attribute | chunk9 | 35 | high |
| m14 | attribute | popcorn | popcorn | compound_modifier | chunk9 | 36 | medium |
| m15 | context | corner | corner | spatial_region | chunk10 | 41 | medium |
| m16 | action | shown | show | verb_predicate | doc | 10 | high |
| m17 | action | sits | sit | verb_predicate | doc | 16 | high |
| m18 | action | hangs | hang | verb_predicate | doc | 30 | high |
| m19 | action | stands | stand | verb_predicate | doc | 38 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> cabinets |
| e1 | has_attribute | m3 | m4 | medium | chunk2 compound -> sink |
| e2 | has_attribute | m9 | m10 | medium | chunk7 amod -> curtains |
| e3 | has_attribute | m12 | m13 | high | chunk9 amod -> machine |
| e4 | has_attribute | m12 | m14 | medium | chunk9 compound -> machine |
| e5 | agent | m16 | m0 | medium | nsubjpass -> shown |
| e6 | agent | m17 | m5 | medium | nsubj -> sits |
| e7 | agent | m18 | m11 | medium | nsubj -> hangs |
| e8 | agent | m19 | m12 | medium | nsubj -> stands |
| e9 | relation | m0 | m1 | high | with |
| e10 | relation | m0 | m3 | high | with |
| e11 | relation | m5 | m6 | high | with |
| e12 | relation | m5 | m7 | medium | to |
| e13 | relation | m5 | m8 | high | near |
| e14 | relation | m8 | m9 | high | with |
| e15 | relation | m12 | m15 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | kitchen | kitchen | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:kitchen", "parents": []} |
| ent_m1 | object | cabinet | cabinets | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:cabinet", "parents": []} |
| ent_m3 | object | sink | sink | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:sink", "parents": []} |
| ent_m5 | object | dining_table | dining table | object | coco_object\|lvis_object\|visual_genome_object_synset\|wordnet_noun_mwe | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:dining_table", "parents": []} |
| ent_m6 | object | chair | chairs | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m6 | raw_mention |  |  |  | True | {"canonical": "entity:chair", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m7 | context | left | left | object | raw_lemma | semantic_type_fallback | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:left", "parents": ["entity_parent:scene_context"]} |
| ent_m8 | object | window | window | object | raw_lemma | wordnet_synset:window.n.01 + stage9_audit | architectural_part, artifact | m8 | raw_mention |  |  |  | True | {"canonical": "entity:window", "parents": ["entity_parent:architectural_part", "entity_parent:artifact"]} |
| ent_m9 | object | curtain | curtains | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:curtain", "parents": []} |
| ent_m11 | object | ceiling_fan | ceiling fan | object | openimages_boxable | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:ceiling_fan", "parents": []} |
| ent_m12 | object | machine | machine | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:machine", "parents": []} |
| ent_m15 | context | corner | corner | object | raw_lemma | semantic_type_fallback | scene_context | m15 | raw_mention |  |  |  | True | {"canonical": "entity:corner", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | shown | show | show | raw_action | wordnet_synset:show.v.01 + stage9_audit | visual_presentation_action, visual_action |  | patient<-theme[passive_to_active]:m0->ent_m0 | {"canonical": "action:show", "parents": ["action_parent:visual_presentation_action", "action_parent:visual_action"]} |  |
| ce1 | m17 | sits | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m5->ent_m5 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce2 | m18 | hangs | hang | hang | raw_action | stage9_seed:parent_seed | attachment_action, visual_action |  | agent:m11->ent_m11 | {"canonical": "action:hang", "parents": ["action_parent:attachment_action", "action_parent:visual_action"]} |  |
| ce3 | m19 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m12->ent_m12 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | patient | theme | passive_to_active | m0 | ent_m0 | medium | e5 | nsubjpass -> shown |  |  |
| ce1 | sit | agent | agent | none | m5 | ent_m5 | medium | e6 | nsubj -> sits |  |  |
| ce2 | hang | agent | agent | none | m11 | ent_m11 | medium | e7 | nsubj -> hangs |  |  |
| ce3 | stand | agent | agent | none | m12 | ent_m12 | medium | e8 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e9 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e10 | False | False |  |  |
| cr2 | m5 | m6 | ent_m5 | ent_m6 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e11 | False | False |  |  |
| cr3 | m5 | m7 | ent_m5 | ent_m7 | to | to | raw_relation | raw_relation | visual_relation | medium | e12 | False | False |  |  |
| cr4 | m5 | m8 | ent_m5 | ent_m8 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e13 | False | False |  |  |
| cr5 | m8 | m9 | ent_m8 | ent_m9 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr6 | m12 | m15 | ent_m12 | ent_m15 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e15 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | kitchen |  |  |  | entity_exists:kitchen | True | low |
| cf1 | entity_exists | cabinet |  |  |  | entity_exists:cabinet | True | low |
| cf2 | entity_exists | sink |  |  |  | entity_exists:sink | True | low |
| cf3 | entity_exists | dining_table |  |  |  | entity_exists:dining_table | True | high |
| cf4 | entity_exists | chair |  |  | furniture, artifact | entity_exists:chair | True | high |
| cf5 | entity_exists | left |  |  | scene_context | entity_exists:left | True | medium |
| cf6 | entity_exists | window |  |  | architectural_part, artifact | entity_exists:window | True | high |
| cf7 | entity_exists | curtain |  |  |  | entity_exists:curtain | True | low |
| cf8 | entity_exists | ceiling_fan |  |  |  | entity_exists:ceiling_fan | True | high |
| cf9 | entity_exists | machine |  |  |  | entity_exists:machine | True | low |
| cf10 | entity_exists | corner |  |  | scene_context | entity_exists:corner | True | medium |
| cf11 | has_attribute | cabinet | wood |  | material_attribute, material, visual_attribute | has_attribute:cabinet:wood | True | high |
| cf12 | has_attribute | sink | countertop |  | compound_modifier, visual_attribute | has_attribute:sink:countertop | True | medium |
| cf13 | has_attribute | curtain | patterned |  | pattern_attribute, pattern, visual_attribute | has_attribute:curtain:patterned | True | medium |
| cf14 | has_attribute | machine | red |  | color_attribute, color, visual_attribute | has_attribute:machine:red | True | high |
| cf15 | has_attribute | machine | popcorn |  | compound_modifier, visual_attribute | has_attribute:machine:popcorn | True | medium |
| cf16 | action_event | show |  |  | visual_presentation_action, visual_action | action_event:show | True | high |
| cf17 | event_role | show | patient | kitchen |  | event_role:show:patient:kitchen | True | medium |
| cf18 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf19 | event_role | sit | agent | dining_table |  | event_role:sit:agent:dining_table | True | medium |
| cf20 | action_event | hang |  |  | attachment_action, visual_action | action_event:hang | True | high |
| cf21 | event_role | hang | agent | ceiling_fan |  | event_role:hang:agent:ceiling_fan | True | medium |
| cf22 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf23 | event_role | stand | agent | machine |  | event_role:stand:agent:machine | True | medium |
| cf24 | relation | kitchen | with | cabinet | association_relation, visual_relation | relation:kitchen:with:cabinet | True | high |
| cf25 | relation | kitchen | with | sink | association_relation, visual_relation | relation:kitchen:with:sink | True | high |
| cf26 | relation | dining_table | with | chair | association_relation, visual_relation | relation:dining_table:with:chair | True | high |
| cf27 | relation | dining_table | to | left | visual_relation | relation:dining_table:to:left | True | medium |
| cf28 | relation | dining_table | near | window | spatial_proximity, visual_relation | relation:dining_table:near:window | True | high |
| cf29 | relation | window | with | curtain | association_relation, visual_relation | relation:window:with:curtain | True | high |
| cf30 | relation | machine | in | corner | spatial_containment, visual_relation | relation:machine:in:corner | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m16 | e5 | m0 |  |  | {"action_mention_id": "m16", "kind": "passive_subject_to_patient", "raw_edge_id": "e5", "raw_role": "theme", "role": "patient", "target": "m0", "voice_normalization": "passive_to_active"} |

## 52

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `2eb8f61acb7123f8d9ba0dd4b47e1de6b9376896360ce8f68d3023f75aebf414`
**parse_path:** `sentence`

> Several power lines stretch across a cloudy sky, with a tall pole in the center. Buildings frame the left and right sides of the scene, their dark silhouettes contrasting against the bright, overcast background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | power lines | power_line | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Several | several | approximate_quantity | chunk0 | 0 | medium |
| m2 | object | sky | sky | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | cloudy | cloudy | modifier_attribute | chunk1 | 5 | medium |
| m4 | object | pole | pole | noun_chunk_root | chunk2 | 11 | high |
| m5 | attribute | tall | tall | size_attribute | chunk2 | 10 | high |
| m6 | context | center | center | spatial_region | chunk3 | 14 | medium |
| m7 | object | Buildings | building | noun_chunk_root | chunk4 | 16 | high |
| m8 | context | scene | scene | scene_context | chunk6 | 25 | high |
| m9 | object | silhouettes | silhouette | noun_chunk_root | chunk7 | 29 | high |
| m10 | attribute | dark | dark | visual_attribute | chunk7 | 28 | medium |
| m11 | context | background | background | scene_context | chunk8 | 36 | high |
| m12 | attribute | bright | bright | visual_attribute | chunk8 | 33 | medium |
| m13 | attribute | overcast | overcast | modifier_attribute | chunk8 | 35 | medium |
| m14 | action | stretch | stretch | verb_predicate | doc | 2 | high |
| m15 | action | frame | frame | verb_predicate | doc | 17 | high |
| m16 | object | sides | side | verb_object | doc | 22 | medium |
| m17 | action | contrasting | contrast | verb_predicate | doc | 30 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | medium | chunk0 quantity -> power lines |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> sky |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> pole |
| e3 | has_context | scene | m8 | high | scene_context token scene |
| e4 | has_attribute | m9 | m10 | medium | chunk7 amod -> silhouettes |
| e5 | has_context | scene | m11 | high | scene_context token background |
| e6 | has_attribute | m11 | m12 | medium | chunk8 amod -> background |
| e7 | has_attribute | m11 | m13 | medium | chunk8 amod -> background |
| e8 | agent | m14 | m0 | medium | nsubj -> stretch |
| e9 | agent | m15 | m7 | medium | nsubj -> frame |
| e10 | patient | m15 | m16 | medium | dobj -> frame |
| e11 | agent | m17 | m9 | medium | nsubj -> contrasting |
| e12 | relation | m0 | m2 | high | across |
| e13 | relation | m0 | m4 | high | with |
| e14 | relation | m4 | m6 | high | in |
| e15 | relation | m7 | m8 | medium | side_region_of |
| e16 | relation | m9 | m11 | high | against |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | power_line | power lines | object | visual_genome_object_synset\|wordnet_noun_mwe | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:power_line", "parents": []} |
| ent_m2 | object | sky | sky | object | raw_lemma | wordnet_synset:sky.n.01 + stage9_audit | natural_scene | m2 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": ["entity_parent:natural_scene"]} |
| ent_m4 | object | pole | pole | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:pole", "parents": []} |
| ent_m6 | context | center | center | object | raw_lemma | semantic_type_fallback | scene_context | m6 | raw_mention |  |  |  | True | {"canonical": "entity:center", "parents": ["entity_parent:scene_context"]} |
| ent_m7 | object | building | Buildings | object | raw_lemma | wordnet_synset:building.n.01 + stage9_audit | structure, artifact | m7 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m8 | context | scene | scene | object | raw_lemma | stage9_seed:parent_seed | scene_context | m8 | raw_mention |  |  |  | True | {"canonical": "entity:scene", "parents": ["entity_parent:scene_context"]} |
| ent_m9 | object | silhouette | silhouettes | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:silhouette", "parents": []} |
| ent_m11 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m11 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m16 | object | side | sides | object | raw_lemma | none |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:side", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m14 | stretch | stretch | stretch | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stretch", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m15 | frame | frame | frame | raw_action | visual_action_fallback | visual_action |  | agent:m7->ent_m7; patient:m16->ent_m16 | {"canonical": "action:frame", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m17 | contrasting | contrast | contrast | raw_action | visual_action_fallback | visual_action |  | agent:m9->ent_m9 | {"canonical": "action:contrast", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stretch | agent | agent | none | m0 | ent_m0 | medium | e8 | nsubj -> stretch |  |  |
| ce1 | frame | agent | agent | none | m7 | ent_m7 | medium | e9 | nsubj -> frame |  |  |
| ce1 | frame | patient | patient | none | m16 | ent_m16 | medium | e10 | dobj -> frame |  |  |
| ce2 | contrast | agent | agent | none | m9 | ent_m9 | medium | e11 | nsubj -> contrasting |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | across | across | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | high | e12 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr2 | m4 | m6 | ent_m4 | ent_m6 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e14 | False | False |  |  |
| cr3 | m7 | m8 | ent_m7 | ent_m8 | side_region_of | side_region_of | generated_region_pattern\|mixed_relation_collapse_rules | generated_region_pattern\|mixed_relation_collapse_rules | spatial_region, visual_relation | medium | e15 | False | False |  |  |
| cr4 | m9 | m11 | ent_m9 | ent_m11 | against | against | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_contact, visual_relation | high | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | power_line |  |  |  | entity_exists:power_line | True | high |
| cf1 | entity_exists | sky |  |  | natural_scene | entity_exists:sky | True | high |
| cf2 | entity_exists | pole |  |  |  | entity_exists:pole | True | low |
| cf3 | entity_exists | center |  |  | scene_context | entity_exists:center | True | medium |
| cf4 | entity_exists | building |  |  | structure, artifact | entity_exists:building | True | high |
| cf5 | entity_exists | scene |  |  | scene_context | entity_exists:scene | True | high |
| cf6 | entity_exists | silhouette |  |  |  | entity_exists:silhouette | True | low |
| cf7 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf8 | entity_exists | side |  |  |  | entity_exists:side | True | low |
| cf9 | has_quantity | power_line | several |  | approximate_quantity, quantity | has_quantity:power_line:several | True | medium |
| cf10 | has_attribute | sky | cloudy |  | weather_attribute, weather, visual_attribute | has_attribute:sky:cloudy | True | medium |
| cf11 | has_attribute | pole | tall |  | size_attribute, height, visual_attribute | has_attribute:pole:tall | True | high |
| cf12 | has_attribute | silhouette | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:silhouette:dark | True | medium |
| cf13 | has_attribute | background | bright |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:background:bright | True | medium |
| cf14 | has_attribute | background | overcast |  | weather_attribute, weather, visual_attribute | has_attribute:background:overcast | True | medium |
| cf15 | action_event | stretch |  |  | visual_action | action_event:stretch | True | low |
| cf16 | event_role | stretch | agent | power_line |  | event_role:stretch:agent:power_line | True | medium |
| cf17 | action_event | frame |  |  | visual_action | action_event:frame | True | low |
| cf18 | event_role | frame | agent | building |  | event_role:frame:agent:building | True | medium |
| cf19 | event_role | frame | patient | side |  | event_role:frame:patient:side | True | medium |
| cf20 | action_event | contrast |  |  | visual_action | action_event:contrast | True | low |
| cf21 | event_role | contrast | agent | silhouette |  | event_role:contrast:agent:silhouette | True | medium |
| cf22 | relation | power_line | across | sky | spatial_path, visual_relation | relation:power_line:across:sky | True | high |
| cf23 | relation | power_line | with | pole | association_relation, visual_relation | relation:power_line:with:pole | True | high |
| cf24 | relation | pole | in | center | spatial_containment, visual_relation | relation:pole:in:center | True | high |
| cf25 | relation | building | side_region_of | scene | spatial_region, visual_relation | relation:building:side_region_of:scene | True | medium |
| cf26 | relation | silhouette | against | background | spatial_contact, visual_relation | relation:silhouette:against:background | True | high |

### Stage 9 Canonicalization Notes
_none_

## 53

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `2ee4861bdbc52993940aadee3693fc63b9668cb21e714921a12b9bce17386c14`
**parse_path:** `sentence`

> A stone doorway leads to a sunlit courtyard with green trees and ancient carvings.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | doorway | doorway | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | stone | stone | material_attribute | chunk0 | 1 | high |
| m2 | object | courtyard | courtyard | noun_chunk_root | chunk1 | 7 | high |
| m3 | attribute | sunlit | sunlit | modifier_attribute | chunk1 | 6 | medium |
| m4 | object | trees | tree | noun_chunk_root | chunk2 | 10 | high |
| m5 | attribute | green | green | color_attribute | chunk2 | 9 | high |
| m6 | object | carvings | carving | noun_chunk_root | chunk3 | 13 | high |
| m7 | attribute | ancient | ancient | modifier_attribute | chunk3 | 12 | medium |
| m8 | action | leads | lead | verb_predicate | doc | 3 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 compound -> doorway |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> courtyard |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> trees |
| e3 | has_attribute | m6 | m7 | medium | chunk3 amod -> carvings |
| e4 | agent | m8 | m0 | medium | nsubj -> leads |
| e5 | relation | m0 | m2 | medium | to |
| e6 | relation | m2 | m4 | high | with |
| e7 | relation | m2 | m6 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | doorway | doorway | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:doorway", "parents": []} |
| ent_m2 | object | courtyard | courtyard | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:courtyard", "parents": []} |
| ent_m4 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m4 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m6 | object | carving | carvings | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:carving", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | leads | lead | lead | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:lead", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | lead | agent | agent | none | m0 | ent_m0 | medium | e4 | nsubj -> leads |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | to | to | raw_relation | raw_relation | visual_relation | medium | e5 | False | False |  |  |
| cr1 | m2 | m4 | ent_m2 | ent_m4 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e6 | False | False |  |  |
| cr2 | m2 | m6 | ent_m2 | ent_m6 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | doorway |  |  |  | entity_exists:doorway | True | low |
| cf1 | entity_exists | courtyard |  |  |  | entity_exists:courtyard | True | low |
| cf2 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf3 | entity_exists | carving |  |  |  | entity_exists:carving | True | low |
| cf4 | has_attribute | doorway | stone |  | material_attribute, material, visual_attribute | has_attribute:doorway:stone | True | high |
| cf5 | has_attribute | courtyard | sunlit |  | modifier_attribute, visual_attribute | has_attribute:courtyard:sunlit | True | medium |
| cf6 | has_attribute | tree | green |  | color_attribute, color, visual_attribute | has_attribute:tree:green | True | high |
| cf7 | has_attribute | carving | ancient |  | modifier_attribute, visual_attribute | has_attribute:carving:ancient | True | medium |
| cf8 | action_event | lead |  |  | visual_action | action_event:lead | True | low |
| cf9 | event_role | lead | agent | doorway |  | event_role:lead:agent:doorway | True | medium |
| cf10 | relation | doorway | to | courtyard | visual_relation | relation:doorway:to:courtyard | True | medium |
| cf11 | relation | courtyard | with | tree | association_relation, visual_relation | relation:courtyard:with:tree | True | high |
| cf12 | relation | courtyard | with | carving | association_relation, visual_relation | relation:courtyard:with:carving | True | high |

### Stage 9 Canonicalization Notes
_none_

## 54

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `2f81dfe56d932210512d803864aa779437fc0a9502fc27ce5dbb503f59182414`
**parse_path:** `sentence`

> A group of green memory modules is installed inside a silver computer chassis. A red arrow points to the modules, with a label in Chinese that reads “加裝記憶體” below them. The setup appears to be inside a server or workstation unit.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “加裝記憶體” | 加裝記憶體 | quote_text | doc_quote | 29 | high |
| m1 | object | group | group | noun_chunk_root | chunk0 | 1 | high |
| m2 | object | modules | module | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | green | green | color_attribute | chunk1 | 3 | high |
| m4 | attribute | memory | memory | compound_modifier | chunk1 | 4 | medium |
| m5 | object | chassis | chassis | noun_chunk_root | chunk2 | 12 | high |
| m6 | attribute | silver | silver | color_attribute | chunk2 | 10 | high |
| m7 | attribute | computer | computer | compound_modifier | chunk2 | 11 | medium |
| m8 | object | arrow | arrow | noun_chunk_root | chunk3 | 16 | high |
| m9 | attribute | red | red | color_attribute | chunk3 | 15 | high |
| m10 | object | modules | module | noun_chunk_root | chunk4 | 20 | high |
| m11 | object | label | label | noun_chunk_root | chunk5 | 24 | high |
| m12 | object | Chinese | chinese | noun_chunk_root | chunk6 | 26 | high |
| m13 | object | setup | setup | noun_chunk_root | chunk10 | 34 | high |
| m14 | object | unit | unit | noun_chunk_root | chunk11 | 43 | high |
| m15 | action | installed | instal | verb_predicate | doc | 7 | high |
| m16 | action | points | point | verb_predicate | doc | 17 | high |
| m17 | action | reads | read | verb_predicate | doc | 28 | high |
| m18 | action | appears | appear | verb_predicate | doc | 35 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | chunk1 amod -> modules |
| e1 | has_attribute | m2 | m4 | medium | chunk1 compound -> modules |
| e2 | has_attribute | m5 | m6 | high | chunk2 amod -> chassis |
| e3 | has_attribute | m5 | m7 | medium | chunk2 compound -> chassis |
| e4 | has_attribute | m8 | m9 | high | chunk3 amod -> arrow |
| e5 | agent | m15 | m1 | medium | nsubjpass -> installed |
| e6 | agent | m16 | m8 | medium | nsubj -> points |
| e7 | agent | m17 | m11 | medium | nsubj -> reads; resolved that -> label |
| e8 | patient | m17 | m0 | medium | dobj -> reads |
| e9 | agent | m18 | m13 | medium | nsubj -> appears |
| e10 | relation | m1 | m2 | medium | of |
| e11 | relation | m1 | m5 | high | inside |
| e12 | relation | m8 | m10 | medium | to |
| e13 | relation | m8 | m11 | high | with |
| e14 | relation | m11 | m12 | high | in |
| e15 | relation | m11 | m8 | high | below |
| e16 | relation | m13 | m14 | high | inside |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | group | group | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:group", "parents": []} |
| ent_m2 | object | module | modules | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:module", "parents": []} |
| ent_m5 | object | chassis | chassis | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:chassis", "parents": []} |
| ent_m8 | object | arrow | arrow | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:arrow", "parents": []} |
| ent_m10 | object | module | modules | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:module", "parents": []} |
| ent_m11 | object | label | label | document | raw_lemma | stage9_seed:parent_seed | text_carrier, artifact | m11 | raw_mention |  |  |  | True | {"canonical": "entity:label", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m12 | object | chinese | Chinese | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:chinese", "parents": []} |
| ent_m13 | object | setup | setup | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:setup", "parents": []} |
| ent_m14 | object | unit | unit | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:unit", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | installed | instal | instal | raw_action | visual_action_fallback | visual_action |  | patient<-theme[passive_to_active]:m1->ent_m1 | {"canonical": "action:instal", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m16 | points | point | point | raw_action | stage9_seed:parent_seed | gesture_action, visual_action |  | agent:m8->ent_m8 | {"canonical": "action:point", "parents": ["action_parent:gesture_action", "action_parent:visual_action"]} |  |
| ce2 | m17 | reads | read | read | raw_action | stage9_seed:parent_seed | text_interaction_action, visual_action |  | agent:m11->ent_m11; patient:m0->None | {"canonical": "action:read", "parents": ["action_parent:text_interaction_action", "action_parent:visual_action"]} |  |
| ce3 | m18 | appears | appear | appear | raw_action | visual_action_fallback | visual_action |  | agent:m13->ent_m13 | {"canonical": "action:appear", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | instal | patient | theme | passive_to_active | m1 | ent_m1 | medium | e5 | nsubjpass -> installed |  |  |
| ce1 | point | agent | agent | none | m8 | ent_m8 | medium | e6 | nsubj -> points |  |  |
| ce2 | read | agent | agent | none | m11 | ent_m11 | medium | e7 | nsubj -> reads; resolved that -> label |  |  |
| ce2 | read | patient | patient | none | m0 |  | medium | e8 | dobj -> reads |  |  |
| ce3 | appear | agent | agent | none | m13 | ent_m13 | medium | e9 | nsubj -> appears |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e10 | False | False |  |  |
| cr1 | m1 | m5 | ent_m1 | ent_m5 | inside | inside | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e11 | False | False |  |  |
| cr2 | m8 | m10 | ent_m8 | ent_m10 | to | to | raw_relation | raw_relation | visual_relation | medium | e12 | False | False |  |  |
| cr3 | m8 | m11 | ent_m8 | ent_m11 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr4 | m11 | m12 | ent_m11 | ent_m12 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e14 | False | False |  |  |
| cr5 | m11 | m8 | ent_m11 | ent_m8 | below | below | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e15 | False | False |  |  |
| cr6 | m13 | m14 | ent_m13 | ent_m14 | inside | inside | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | group |  |  |  | entity_exists:group | True | low |
| cf1 | entity_exists | module |  |  |  | entity_exists:module | True | low |
| cf2 | entity_exists | chassis |  |  |  | entity_exists:chassis | True | low |
| cf3 | entity_exists | arrow |  |  |  | entity_exists:arrow | True | low |
| cf4 | entity_exists | module |  |  |  | entity_exists:module | True | low |
| cf5 | entity_exists | label |  |  | text_carrier, artifact | entity_exists:label | True | high |
| cf6 | entity_exists | chinese |  |  |  | entity_exists:chinese | True | low |
| cf7 | entity_exists | setup |  |  |  | entity_exists:setup | True | low |
| cf8 | entity_exists | unit |  |  |  | entity_exists:unit | True | low |
| cf9 | has_attribute | module | green |  | color_attribute, color, visual_attribute | has_attribute:module:green | True | high |
| cf10 | has_attribute | module | memory |  | compound_modifier, visual_attribute | has_attribute:module:memory | True | medium |
| cf11 | has_attribute | chassis | silver |  | color_attribute, color, material, visual_attribute | has_attribute:chassis:silver | True | high |
| cf12 | has_attribute | chassis | computer |  | compound_modifier, visual_attribute | has_attribute:chassis:computer | True | medium |
| cf13 | has_attribute | arrow | red |  | color_attribute, color, visual_attribute | has_attribute:arrow:red | True | high |
| cf14 | action_event | instal |  |  | visual_action | action_event:instal | True | low |
| cf15 | event_role | instal | patient | group |  | event_role:instal:patient:group | True | medium |
| cf16 | action_event | point |  |  | gesture_action, visual_action | action_event:point | True | high |
| cf17 | event_role | point | agent | arrow |  | event_role:point:agent:arrow | True | medium |
| cf18 | action_event | read |  |  | text_interaction_action, visual_action | action_event:read | True | medium |
| cf19 | event_role | read | agent | label |  | event_role:read:agent:label | True | medium |
| cf20 | event_role | read | patient |  |  | event_role:read:patient | False | medium |
| cf21 | action_event | appear |  |  | visual_action | action_event:appear | True | low |
| cf22 | event_role | appear | agent | setup |  | event_role:appear:agent:setup | True | medium |
| cf23 | relation | group | of | module | part_relation, visual_relation | relation:group:of:module | True | medium |
| cf24 | relation | group | inside | chassis | spatial_containment, visual_relation | relation:group:inside:chassis | True | high |
| cf25 | relation | arrow | to | module | visual_relation | relation:arrow:to:module | True | medium |
| cf26 | relation | arrow | with | label | association_relation, visual_relation | relation:arrow:with:label | True | high |
| cf27 | relation | label | in | chinese | spatial_containment, visual_relation | relation:label:in:chinese | True | high |
| cf28 | relation | label | below | arrow | spatial_vertical, visual_relation | relation:label:below:arrow | True | high |
| cf29 | relation | setup | inside | unit | spatial_containment, visual_relation | relation:setup:inside:unit | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m15 | e5 | m1 |  |  | {"action_mention_id": "m15", "kind": "passive_subject_to_patient", "raw_edge_id": "e5", "raw_role": "theme", "role": "patient", "target": "m1", "voice_normalization": "passive_to_active"} |

## 55

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `30c926e8e6cca68a73e53f04074da5cc4f57ea9ab29888a5e3ba0440b6d42014`
**parse_path:** `tag_list`

> dish, plate, sauce, greens

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | dish | dish | segment_head | t0 | 0 | high |
| m1 | object | plate | plate | segment_head | t1 | 0 | high |
| m2 | object | sauce | sauce | segment_head | t2 | 0 | high |
| m3 | attribute | greens | green | color_attribute | t3 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | candidate_has_attribute | m2 | m3 | low | t3 adjacent floating attribute |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | dish | dish | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:dish", "parents": []} |
| ent_m1 | object | plate | plate | object | raw_lemma | wordnet_synset:plate.n.04 + stage9_audit | dishware, artifact | m1 | raw_mention |  |  |  | True | {"canonical": "entity:plate", "parents": ["entity_parent:dishware", "entity_parent:artifact"]} |
| ent_m2 | object | sauce | sauce | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:sauce", "parents": []} |

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
| cf0 | entity_exists | dish |  |  |  | entity_exists:dish | True | low |
| cf1 | entity_exists | plate |  |  | dishware, artifact | entity_exists:plate | True | high |
| cf2 | entity_exists | sauce |  |  |  | entity_exists:sauce | True | low |
| cf3 | candidate_has_attribute | sauce | green |  | color_attribute, color, visual_attribute | candidate_has_attribute:sauce:green | False | low |

### Stage 9 Canonicalization Notes
_none_

## 56

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `321881c56e881fa878d606737db46ddfff718a32c464a52727ad396993cb8814`
**parse_path:** `sentence`

> A child with green, blue, and white paint on their face and clothing stands in a group. Several other children are nearby, some looking at them, in what appears to be an outdoor setting.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | child | child | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | paint | paint | noun_chunk_root | chunk1 | 9 | high |
| m2 | attribute | green | green | color_attribute | chunk1 | 3 | high |
| m3 | attribute | blue | blue | color_attribute | chunk1 | 5 | high |
| m4 | attribute | white | white | color_attribute | chunk1 | 8 | high |
| m5 | object | face | face | noun_chunk_root | chunk2 | 12 | high |
| m6 | object | clothing | clothing | noun_chunk_root | chunk3 | 14 | high |
| m7 | object | group | group | noun_chunk_root | chunk4 | 18 | high |
| m8 | object | children | child | noun_chunk_root | chunk5 | 22 | high |
| m9 | quantity | Several | several | approximate_quantity | chunk5 | 20 | medium |
| m10 | attribute | other | other | modifier_attribute | chunk5 | 21 | medium |
| m11 | quantity | some | some | indefinite_quantity | chunk6 | 26 | medium |
| m12 | context | setting | setting | scene_context | chunk9 | 38 | high |
| m13 | attribute | outdoor | outdoor | modifier_attribute | chunk9 | 37 | medium |
| m14 | action | stands | stand | verb_predicate | doc | 15 | high |
| m15 | action | looking | look | verb_predicate | doc | 27 | high |
| m16 | action | appears | appear | verb_predicate | doc | 33 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> paint |
| e1 | has_attribute | m1 | m3 | high | chunk1 conj -> paint |
| e2 | has_attribute | m1 | m4 | high | chunk1 conj -> paint |
| e3 | has_quantity | m8 | m9 | medium | chunk5 quantity -> children |
| e4 | has_attribute | m8 | m10 | medium | chunk5 amod -> children |
| e5 | has_context | scene | m12 | high | scene_context token setting |
| e6 | has_attribute | m12 | m13 | medium | chunk9 amod -> setting |
| e7 | agent | m14 | m0 | medium | nsubj -> stands |
| e8 | agent | m15 | m8 | medium | inherited agent advcl -> are |
| e9 | relation | m0 | m1 | high | with |
| e10 | relation | m1 | m5 | high | on |
| e11 | relation | m1 | m6 | high | on |
| e12 | relation | m0 | m7 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | child | child | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | paint | paint | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:paint", "parents": []} |
| ent_m5 | object | face | face | object | raw_lemma | stage9_seed:parent_seed | body_part | m5 | raw_mention |  |  |  | True | {"canonical": "entity:face", "parents": ["entity_parent:body_part"]} |
| ent_m6 | object | clothing | clothing | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:clothing", "parents": []} |
| ent_m7 | object | group | group | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:group", "parents": []} |
| ent_m8 | object | child | children | person | raw_lemma | stage9_seed:parent_seed | person, human | m8 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m12 | context | setting | setting | object | raw_lemma | stage9_seed:parent_seed | scene_context | m12 | raw_mention |  |  |  | True | {"canonical": "entity:setting", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m14 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m15 | looking | look | look | raw_action | stage9_seed:parent_seed | gaze_action, visual_action |  | agent:m8->ent_m8 | {"canonical": "action:look", "parents": ["action_parent:gaze_action", "action_parent:visual_action"]} |  |
| ce2 | m16 | appears | appear | appear | raw_action | visual_action_fallback | visual_action |  |  | {"canonical": "action:appear", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e7 | nsubj -> stands |  |  |
| ce1 | look | agent | agent | none | m8 | ent_m8 | medium | e8 | inherited agent advcl -> are |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e9 | False | False |  |  |
| cr1 | m1 | m5 | ent_m1 | ent_m5 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e10 | False | False |  |  |
| cr2 | m1 | m6 | ent_m1 | ent_m6 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e11 | False | False |  |  |
| cr3 | m0 | m7 | ent_m0 | ent_m7 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e12 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf1 | entity_exists | paint |  |  |  | entity_exists:paint | True | low |
| cf2 | entity_exists | face |  |  | body_part | entity_exists:face | True | high |
| cf3 | entity_exists | clothing |  |  |  | entity_exists:clothing | True | low |
| cf4 | entity_exists | group |  |  |  | entity_exists:group | True | low |
| cf5 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf6 | entity_exists | setting |  |  | scene_context | entity_exists:setting | True | high |
| cf7 | has_attribute | paint | green |  | color_attribute, color, visual_attribute | has_attribute:paint:green | True | high |
| cf8 | has_attribute | paint | blue |  | color_attribute, color, visual_attribute | has_attribute:paint:blue | True | high |
| cf9 | has_attribute | paint | white |  | color_attribute, color, visual_attribute | has_attribute:paint:white | True | high |
| cf10 | has_quantity | child | several |  | approximate_quantity, quantity | has_quantity:child:several | True | medium |
| cf11 | has_attribute | child | other |  | modifier_attribute, visual_attribute | has_attribute:child:other | True | medium |
| cf12 | has_attribute | setting | outdoor |  | modifier_attribute, visual_attribute | has_attribute:setting:outdoor | True | medium |
| cf13 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf14 | event_role | stand | agent | child |  | event_role:stand:agent:child | True | medium |
| cf15 | action_event | look |  |  | gaze_action, visual_action | action_event:look | True | high |
| cf16 | event_role | look | agent | child |  | event_role:look:agent:child | True | medium |
| cf17 | action_event | appear |  |  | visual_action | action_event:appear | True | low |
| cf18 | relation | child | with | paint | association_relation, visual_relation | relation:child:with:paint | True | high |
| cf19 | relation | paint | on | face | spatial_support, visual_relation | relation:paint:on:face | True | high |
| cf20 | relation | paint | on | clothing | spatial_support, visual_relation | relation:paint:on:clothing | True | high |
| cf21 | relation | child | in | group | spatial_containment, visual_relation | relation:child:in:group | True | high |

### Stage 9 Canonicalization Notes
_none_

## 57

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `32837795de5a42abc14574cb80663c2c96bd873a311a50f8b42559a9fd213814`
**parse_path:** `sentence`

> People walk along a path near a traditional Japanese building with red autumn trees and a blue sky.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | People | people | noun_chunk_root | chunk0 | 0 | high |
| m1 | object | path | path | noun_chunk_root | chunk1 | 4 | high |
| m2 | object | building | building | noun_chunk_root | chunk2 | 9 | high |
| m3 | attribute | traditional | traditional | modifier_attribute | chunk2 | 7 | medium |
| m4 | attribute | Japanese | japanese | modifier_attribute | chunk2 | 8 | medium |
| m5 | object | trees | tree | noun_chunk_root | chunk3 | 13 | high |
| m6 | attribute | red | red | color_attribute | chunk3 | 11 | high |
| m7 | attribute | autumn | autumn | compound_modifier | chunk3 | 12 | medium |
| m8 | object | sky | sky | noun_chunk_root | chunk4 | 17 | high |
| m9 | attribute | blue | blue | color_attribute | chunk4 | 16 | high |
| m10 | action | walk | walk | verb_predicate | doc | 1 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | medium | chunk2 amod -> building |
| e1 | has_attribute | m2 | m4 | medium | chunk2 amod -> building |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> trees |
| e3 | has_attribute | m5 | m7 | medium | chunk3 compound -> trees |
| e4 | has_attribute | m8 | m9 | high | chunk4 amod -> sky |
| e5 | agent | m10 | m0 | medium | nsubj -> walk |
| e6 | relation | m0 | m1 | medium | along |
| e7 | relation | m0 | m2 | high | near |
| e8 | relation | m2 | m5 | high | with |
| e9 | relation | m2 | m8 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | People | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | path | path | object | raw_lemma | wordnet_synset:path.n.04 + stage9_audit | path, place | m1 | raw_mention |  |  |  | True | {"canonical": "entity:path", "parents": ["entity_parent:path", "entity_parent:place"]} |
| ent_m2 | object | building | building | object | raw_lemma | wordnet_synset:building.n.01 + stage9_audit | structure, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m5 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m5 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m8 | object | sky | sky | object | raw_lemma | wordnet_synset:sky.n.01 + stage9_audit | natural_scene | m8 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": ["entity_parent:natural_scene"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | walk | walk | walk | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:walk", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | walk | agent | agent | none | m0 | ent_m0 | medium | e5 | nsubj -> walk |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | along | along | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | medium | e6 | False | False |  |  |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e7 | False | False |  |  |
| cr2 | m2 | m5 | ent_m2 | ent_m5 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e8 | False | False |  |  |
| cr3 | m2 | m8 | ent_m2 | ent_m8 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | path |  |  | path, place | entity_exists:path | True | high |
| cf2 | entity_exists | building |  |  | structure, artifact | entity_exists:building | True | high |
| cf3 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf4 | entity_exists | sky |  |  | natural_scene | entity_exists:sky | True | high |
| cf5 | has_attribute | building | traditional |  | modifier_attribute, visual_attribute | has_attribute:building:traditional | True | medium |
| cf6 | has_attribute | building | japanese |  | modifier_attribute, visual_attribute | has_attribute:building:japanese | True | medium |
| cf7 | has_attribute | tree | red |  | color_attribute, color, visual_attribute | has_attribute:tree:red | True | high |
| cf8 | has_attribute | tree | autumn |  | compound_modifier, visual_attribute | has_attribute:tree:autumn | True | medium |
| cf9 | has_attribute | sky | blue |  | color_attribute, color, visual_attribute | has_attribute:sky:blue | True | high |
| cf10 | action_event | walk |  |  | locomotion_action, visual_action | action_event:walk | True | high |
| cf11 | event_role | walk | agent | people |  | event_role:walk:agent:people | True | medium |
| cf12 | relation | people | along | path | spatial_path, visual_relation | relation:people:along:path | True | medium |
| cf13 | relation | people | near | building | spatial_proximity, visual_relation | relation:people:near:building | True | high |
| cf14 | relation | building | with | tree | association_relation, visual_relation | relation:building:with:tree | True | high |
| cf15 | relation | building | with | sky | association_relation, visual_relation | relation:building:with:sky | True | high |

### Stage 9 Canonicalization Notes
_none_

## 58

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `35764b32bba35000fc76f03ab1a6a9b84798280e31615a7fbaab8a57a68cd414`
**parse_path:** `sentence`

> A woman in a floral dress speaks into a red microphone while others stand nearby at an outdoor event.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | dress | dress | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | floral | floral | modifier_attribute | chunk1 | 4 | medium |
| m3 | object | microphone | microphone | noun_chunk_root | chunk2 | 10 | high |
| m4 | attribute | red | red | color_attribute | chunk2 | 9 | high |
| m5 | object | event | event | noun_chunk_root | chunk4 | 18 | high |
| m6 | attribute | outdoor | outdoor | modifier_attribute | chunk4 | 17 | medium |
| m7 | action | speaks | speak | verb_predicate | doc | 6 | high |
| m8 | action | stand | stand | verb_predicate | doc | 13 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 amod -> dress |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> microphone |
| e2 | has_attribute | m5 | m6 | medium | chunk4 amod -> event |
| e3 | agent | m7 | m0 | medium | nsubj -> speaks |
| e4 | agent | m8 | m0 | medium | inherited agent advcl -> speaks |
| e5 | relation | m0 | m1 | high | in |
| e6 | relation | m0 | m3 | medium | into |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | dress | dress | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:dress", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | microphone | microphone | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:microphone", "parents": []} |
| ent_m5 | object | event | event | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:event", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | speaks | speak | speak | raw_action | stage9_seed:parent_seed | communication_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:speak", "parents": ["action_parent:communication_action", "action_parent:visual_action"]} |  |
| ce1 | m8 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | speak | agent | agent | none | m0 | ent_m0 | medium | e3 | nsubj -> speaks |  |  |
| ce1 | stand | agent | agent | none | m0 | ent_m0 | medium | e4 | inherited agent advcl -> speaks |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e5 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | into | into | raw_relation | raw_relation | visual_relation | medium | e6 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | dress |  |  | clothing, wearable | entity_exists:dress | True | high |
| cf2 | entity_exists | microphone |  |  |  | entity_exists:microphone | True | low |
| cf3 | entity_exists | event |  |  |  | entity_exists:event | True | low |
| cf4 | has_attribute | dress | floral |  | pattern_attribute, pattern, pattern_marking, textile_pattern, visual_attribute | has_attribute:dress:floral | True | medium |
| cf5 | has_attribute | microphone | red |  | color_attribute, color, visual_attribute | has_attribute:microphone:red | True | high |
| cf6 | has_attribute | event | outdoor |  | modifier_attribute, visual_attribute | has_attribute:event:outdoor | True | medium |
| cf7 | action_event | speak |  |  | communication_action, visual_action | action_event:speak | True | medium |
| cf8 | event_role | speak | agent | woman |  | event_role:speak:agent:woman | True | medium |
| cf9 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf10 | event_role | stand | agent | woman |  | event_role:stand:agent:woman | True | medium |
| cf11 | relation | woman | in | dress | spatial_containment, visual_relation | relation:woman:in:dress | True | high |
| cf12 | relation | woman | into | microphone | visual_relation | relation:woman:into:microphone | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 59

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `35c090288298c1cb46fac5c35c67f866253d3435fa4267e8c7f537a9d413d014`
**parse_path:** `sentence`

> A light brown moth with speckled wings rests on a patterned surface. Its body is fuzzy, and it has thin antennae extending from its head. The background shows muted tones and geometric shapes.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | moth | moth | noun_chunk_root | chunk0 | 3 | high |
| m1 | attribute | light | light | visual_attribute | chunk0 | 1 | medium |
| m2 | attribute | brown | brown | color_attribute | chunk0 | 2 | high |
| m3 | object | wings | wing | noun_chunk_root | chunk1 | 6 | high |
| m4 | attribute | speckled | speckled | modifier_attribute | chunk1 | 5 | medium |
| m5 | context | surface | surface | spatial_region | chunk2 | 11 | medium |
| m6 | object | body | body | noun_chunk_root | chunk3 | 14 | high |
| m7 | object | antennae | antenna | noun_chunk_root | chunk5 | 22 | high |
| m8 | attribute | thin | thin | modifier_attribute | chunk5 | 21 | medium |
| m9 | object | head | head | noun_chunk_root | chunk6 | 26 | high |
| m10 | context | background | background | scene_context | chunk7 | 29 | high |
| m11 | object | tones | tone | noun_chunk_root | chunk8 | 32 | high |
| m12 | attribute | muted | muted | modifier_attribute | chunk8 | 31 | medium |
| m13 | object | shapes | shape | noun_chunk_root | chunk9 | 35 | high |
| m14 | attribute | geometric | geometric | modifier_attribute | chunk9 | 34 | medium |
| m15 | action | rests | rest | verb_predicate | doc | 7 | high |
| m16 | action | has | have | verb_predicate | doc | 20 | high |
| m17 | action | extending | extend | verb_predicate | doc | 23 | high |
| m18 | action | shows | show | verb_predicate | doc | 30 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> moth |
| e1 | has_attribute | m0 | m2 | high | chunk0 amod -> moth |
| e2 | has_attribute | m3 | m4 | medium | chunk1 amod -> wings |
| e3 | has_attribute | m7 | m8 | medium | chunk5 amod -> antennae |
| e4 | has_context | scene | m10 | high | scene_context token background |
| e5 | has_attribute | m11 | m12 | medium | chunk8 amod -> tones |
| e6 | has_attribute | m13 | m14 | medium | chunk9 amod -> shapes |
| e7 | agent | m15 | m0 | medium | nsubj -> rests |
| e8 | agent | m16 | m6 | medium | nsubj -> has; resolved it -> body |
| e9 | patient | m16 | m7 | medium | dobj -> has |
| e10 | agent | m17 | m7 | medium | inherited agent acl -> antennae |
| e11 | agent | m18 | m10 | medium | nsubj -> shows |
| e12 | patient | m18 | m11 | medium | dobj -> shows |
| e13 | patient | m18 | m13 | medium | dobj -> shows |
| e14 | relation | m0 | m3 | high | with |
| e15 | relation | m0 | m5 | high | on |
| e16 | relation | m7 | m9 | medium | from |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | moth | moth | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:moth", "parents": []} |
| ent_m3 | object | wing | wings | object | raw_lemma | stage9_seed:parent_seed | body_part | m3 | raw_mention |  |  |  | True | {"canonical": "entity:wing", "parents": ["entity_parent:body_part"]} |
| ent_m5 | context | surface | surface | object | raw_lemma | semantic_type_fallback | scene_context | m5 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": ["entity_parent:scene_context"]} |
| ent_m6 | object | body | body | object | raw_lemma | stage9_seed:parent_seed | body_part | m6 | raw_mention |  |  |  | True | {"canonical": "entity:body", "parents": ["entity_parent:body_part"]} |
| ent_m7 | object | antenna | antennae | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:antenna", "parents": []} |
| ent_m9 | object | head | head | object | raw_lemma | stage9_seed:parent_seed | body_part | m9 | raw_mention |  |  |  | True | {"canonical": "entity:head", "parents": ["entity_parent:body_part"]} |
| ent_m10 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m10 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m11 | object | tone | tones | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:tone", "parents": []} |
| ent_m13 | object | shape | shapes | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:shape", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | rests | rest | rest | raw_action | wordnet_synset:rest.v.01 + stage9_audit | support_state_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:rest", "parents": ["action_parent:support_state_action", "action_parent:visual_action"]} |  |
| ce1 | m16 | has | have | have | raw_action | visual_action_fallback | visual_action |  | agent:m6->ent_m6; patient:m7->ent_m7 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m17 | extending | extend | extend | raw_action | visual_action_fallback | visual_action |  | agent:m7->ent_m7 | {"canonical": "action:extend", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m18 | shows | show | show | raw_action | wordnet_synset:show.v.01 + stage9_audit | visual_presentation_action, visual_action |  | agent:m10->ent_m10; patient:m11->ent_m11; patient:m13->ent_m13 | {"canonical": "action:show", "parents": ["action_parent:visual_presentation_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | rest | agent | agent | none | m0 | ent_m0 | medium | e7 | nsubj -> rests |  |  |
| ce1 | have | agent | agent | none | m6 | ent_m6 | medium | e8 | nsubj -> has; resolved it -> body |  |  |
| ce1 | have | patient | patient | none | m7 | ent_m7 | medium | e9 | dobj -> has |  |  |
| ce2 | extend | agent | agent | none | m7 | ent_m7 | medium | e10 | inherited agent acl -> antennae |  |  |
| ce3 | show | agent | agent | none | m10 | ent_m10 | medium | e11 | nsubj -> shows |  |  |
| ce3 | show | patient | patient | none | m11 | ent_m11 | medium | e12 | dobj -> shows |  |  |
| ce3 | show | patient | patient | none | m13 | ent_m13 | medium | e13 | dobj -> shows |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e15 | False | False |  |  |
| cr2 | m7 | m9 | ent_m7 | ent_m9 | from | from | raw_relation | raw_relation | visual_relation | medium | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | moth |  |  |  | entity_exists:moth | True | low |
| cf1 | entity_exists | wing |  |  | body_part | entity_exists:wing | True | medium |
| cf2 | entity_exists | surface |  |  | scene_context | entity_exists:surface | True | medium |
| cf3 | entity_exists | body |  |  | body_part | entity_exists:body | True | high |
| cf4 | entity_exists | antenna |  |  |  | entity_exists:antenna | True | low |
| cf5 | entity_exists | head |  |  | body_part | entity_exists:head | True | high |
| cf6 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf7 | entity_exists | tone |  |  |  | entity_exists:tone | True | low |
| cf8 | entity_exists | shape |  |  |  | entity_exists:shape | True | low |
| cf9 | has_attribute | moth | light |  | visual_attribute | has_attribute:moth:light | True | medium |
| cf10 | has_attribute | moth | brown |  | color_attribute, color, visual_attribute | has_attribute:moth:brown | True | high |
| cf11 | has_attribute | wing | speckled |  | pattern_attribute, pattern, visual_attribute | has_attribute:wing:speckled | True | medium |
| cf12 | has_attribute | antenna | thin |  | size_attribute, clean_exact_overlap, fatness, size, thickness, width, visual_attribute | has_attribute:antenna:thin | True | medium |
| cf13 | has_attribute | tone | muted |  | modifier_attribute, visual_attribute | has_attribute:tone:muted | True | medium |
| cf14 | has_attribute | shape | geometric |  | pattern_attribute, textile_pattern, visual_attribute | has_attribute:shape:geometric | True | medium |
| cf15 | action_event | rest |  |  | support_state_action, visual_action | action_event:rest | True | medium |
| cf16 | event_role | rest | agent | moth |  | event_role:rest:agent:moth | True | medium |
| cf17 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf18 | event_role | have | agent | body |  | event_role:have:agent:body | True | medium |
| cf19 | event_role | have | patient | antenna |  | event_role:have:patient:antenna | True | medium |
| cf20 | action_event | extend |  |  | visual_action | action_event:extend | True | low |
| cf21 | event_role | extend | agent | antenna |  | event_role:extend:agent:antenna | True | medium |
| cf22 | action_event | show |  |  | visual_presentation_action, visual_action | action_event:show | True | high |
| cf23 | event_role | show | agent | background |  | event_role:show:agent:background | True | medium |
| cf24 | event_role | show | patient | tone |  | event_role:show:patient:tone | True | medium |
| cf25 | event_role | show | patient | shape |  | event_role:show:patient:shape | True | medium |
| cf26 | relation | moth | with | wing | association_relation, visual_relation | relation:moth:with:wing | True | high |
| cf27 | relation | moth | on | surface | spatial_support, visual_relation | relation:moth:on:surface | True | high |
| cf28 | relation | antenna | from | head | visual_relation | relation:antenna:from:head | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 60

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `35e5d4c882b23f5c0085a15fe8bd447c952c1e7e07cc7cd56cb49533e5023014`
**parse_path:** `tag_list`

> black dog, brown patches, gravel ground, chain link fence, utility pole

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | dog | dog | segment_head | t0 | 1 | high |
| m1 | attribute | black | black | attribute | t0 | 0 | high |
| m2 | object | patches | patch | segment_head | t1 | 1 | high |
| m3 | attribute | brown | brown | attribute | t1 | 0 | high |
| m4 | object | ground | ground | segment_head | t2 | 1 | high |
| m5 | attribute | gravel | gravel | attribute | t2 | 0 | high |
| m6 | object | fence | fence | segment_head | t3 | 2 | high |
| m7 | attribute | chain | chain | attribute | t3 | 0 | high |
| m8 | attribute | link | link | attribute | t3 | 1 | high |
| m9 | object | pole | pole | segment_head | t4 | 1 | high |
| m10 | attribute | utility | utility | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> dog |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> patches |
| e2 | has_attribute | m4 | m5 | high | t2 internal compound -> ground |
| e3 | has_attribute | m6 | m7 | high | t3 internal compound -> fence |
| e4 | has_attribute | m6 | m8 | high | t3 internal compound -> fence |
| e5 | has_attribute | m9 | m10 | high | t4 internal compound -> pole |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | dog | dog | animal | raw_lemma | stage9_seed:parent_seed | animal, living_thing | m0 | raw_mention |  |  |  | True | {"canonical": "entity:dog", "parents": ["entity_parent:animal", "entity_parent:living_thing"]} |
| ent_m2 | object | patch | patches | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:patch", "parents": []} |
| ent_m4 | object | ground | ground | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:ground", "parents": []} |
| ent_m6 | object | fence | fence | object | raw_lemma | wordnet_synset:fence.n.01 + stage9_audit | structure, artifact | m6 | raw_mention |  |  |  | True | {"canonical": "entity:fence", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m9 | object | pole | pole | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:pole", "parents": []} |

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
| cf0 | entity_exists | dog |  |  | animal, living_thing | entity_exists:dog | True | high |
| cf1 | entity_exists | patch |  |  |  | entity_exists:patch | True | low |
| cf2 | entity_exists | ground |  |  |  | entity_exists:ground | True | low |
| cf3 | entity_exists | fence |  |  | structure, artifact | entity_exists:fence | True | high |
| cf4 | entity_exists | pole |  |  |  | entity_exists:pole | True | low |
| cf5 | has_attribute | dog | black |  | color_attribute, color, visual_attribute | has_attribute:dog:black | True | high |
| cf6 | has_attribute | patch | brown |  | color_attribute, color, visual_attribute | has_attribute:patch:brown | True | high |
| cf7 | has_attribute | ground | gravel |  | material_attribute, material, visual_attribute | has_attribute:ground:gravel | True | high |
| cf8 | has_attribute | fence | chain |  | attribute, visual_attribute | has_attribute:fence:chain | True | high |
| cf9 | has_attribute | fence | link |  | attribute, visual_attribute | has_attribute:fence:link | True | high |
| cf10 | has_attribute | pole | utility |  | attribute, visual_attribute | has_attribute:pole:utility | True | high |

### Stage 9 Canonicalization Notes
_none_

## 61

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `361cc9e233503b7f9612753b35ef23ba21389d1234656c5ce3fab90a6a542414`
**parse_path:** `sentence`

> A young man smiles while standing at a wooden table with food trays. Several people are in the background near a doorway.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | young | young | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | table | table | noun_chunk_root | chunk1 | 9 | high |
| m3 | attribute | wooden | wooden | material_attribute | chunk1 | 8 | high |
| m4 | object | trays | tray | noun_chunk_root | chunk2 | 12 | high |
| m5 | attribute | food | food | compound_modifier | chunk2 | 11 | medium |
| m6 | object | people | people | noun_chunk_root | chunk3 | 15 | high |
| m7 | quantity | Several | several | approximate_quantity | chunk3 | 14 | medium |
| m8 | context | background | background | scene_context | chunk4 | 19 | high |
| m9 | object | doorway | doorway | noun_chunk_root | chunk5 | 22 | high |
| m10 | action | smiles | smile | verb_predicate | doc | 3 | high |
| m11 | action | standing | stand | verb_predicate | doc | 5 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> man |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> table |
| e2 | has_attribute | m4 | m5 | medium | chunk2 compound -> trays |
| e3 | has_quantity | m6 | m7 | medium | chunk3 quantity -> people |
| e4 | has_context | scene | m8 | high | scene_context token background |
| e5 | agent | m10 | m0 | medium | nsubj -> smiles |
| e6 | agent | m11 | m0 | medium | inherited agent advcl -> smiles |
| e7 | relation | m0 | m2 | medium | at |
| e8 | relation | m0 | m4 | high | with |
| e9 | relation | m6 | m8 | high | in |
| e10 | relation | m6 | m9 | high | near |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | table | table | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m4 | object | tray | trays | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:tray", "parents": []} |
| ent_m6 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m6 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m8 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m8 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m9 | object | doorway | doorway | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:doorway", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | smiles | smile | smile | raw_action | stage9_seed:parent_seed | expression_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:smile", "parents": ["action_parent:expression_action", "action_parent:visual_action"]} |  |
| ce1 | m11 | standing | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | smile | agent | agent | none | m0 | ent_m0 | medium | e5 | nsubj -> smiles |  |  |
| ce1 | stand | agent | agent | none | m0 | ent_m0 | medium | e6 | inherited agent advcl -> smiles |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e7 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e8 | False | False |  |  |
| cr2 | m6 | m8 | ent_m6 | ent_m8 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e9 | False | False |  |  |
| cr3 | m6 | m9 | ent_m6 | ent_m9 | near | near | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|streusle_mwe\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | high | e10 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf2 | entity_exists | tray |  |  |  | entity_exists:tray | True | low |
| cf3 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf4 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf5 | entity_exists | doorway |  |  |  | entity_exists:doorway | True | low |
| cf6 | has_attribute | man | young |  | modifier_attribute, visual_attribute | has_attribute:man:young | True | medium |
| cf7 | has_attribute | table | wood |  | material_attribute, material, visual_attribute | has_attribute:table:wood | True | high |
| cf8 | has_attribute | tray | food |  | compound_modifier, visual_attribute | has_attribute:tray:food | True | medium |
| cf9 | has_quantity | people | several |  | approximate_quantity, quantity | has_quantity:people:several | True | medium |
| cf10 | action_event | smile |  |  | expression_action, visual_action | action_event:smile | True | high |
| cf11 | event_role | smile | agent | man |  | event_role:smile:agent:man | True | medium |
| cf12 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf13 | event_role | stand | agent | man |  | event_role:stand:agent:man | True | medium |
| cf14 | relation | man | at | table | spatial_location, visual_relation | relation:man:at:table | True | medium |
| cf15 | relation | man | with | tray | association_relation, visual_relation | relation:man:with:tray | True | high |
| cf16 | relation | people | in | background | spatial_containment, visual_relation | relation:people:in:background | True | high |
| cf17 | relation | people | near | doorway | spatial_proximity, visual_relation | relation:people:near:doorway | True | high |

### Stage 9 Canonicalization Notes
_none_

## 62

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `36a9b06d7fc05417e45424ee67372c40ea8e1dab8321d5ee2886f7fffd49a814`
**parse_path:** `tag_list`

> snowy mountains, rocky path, blue sky, clouds, trail

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | mountains | mountain | segment_head | t0 | 1 | high |
| m1 | attribute | snowy | snowy | attribute | t0 | 0 | high |
| m2 | object | path | path | segment_head | t1 | 1 | high |
| m3 | attribute | rocky | rocky | attribute | t1 | 0 | high |
| m4 | object | sky | sky | segment_head | t2 | 1 | high |
| m5 | attribute | blue | blue | attribute | t2 | 0 | high |
| m6 | object | clouds | cloud | segment_head | t3 | 0 | high |
| m7 | object | trail | trail | segment_head | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> mountains |
| e1 | has_attribute | m2 | m3 | high | t1 internal compound -> path |
| e2 | has_attribute | m4 | m5 | high | t2 internal amod -> sky |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | mountain | mountains | object | raw_lemma | wordnet_synset:mountain.n.01 + stage9_audit | landform, place | m0 | raw_mention |  |  |  | True | {"canonical": "entity:mountain", "parents": ["entity_parent:landform", "entity_parent:place"]} |
| ent_m2 | object | path | path | object | raw_lemma | wordnet_synset:path.n.04 + stage9_audit | path, place | m2 | raw_mention |  |  |  | True | {"canonical": "entity:path", "parents": ["entity_parent:path", "entity_parent:place"]} |
| ent_m4 | object | sky | sky | object | raw_lemma | wordnet_synset:sky.n.01 + stage9_audit | natural_scene | m4 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": ["entity_parent:natural_scene"]} |
| ent_m6 | object | cloud | clouds | object | raw_lemma | wordnet_synset:cloud.n.01 + stage9_audit | natural_element | m6 | raw_mention |  |  |  | True | {"canonical": "entity:cloud", "parents": ["entity_parent:natural_element"]} |
| ent_m7 | object | trail | trail | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:trail", "parents": []} |

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
| cf0 | entity_exists | mountain |  |  | landform, place | entity_exists:mountain | True | high |
| cf1 | entity_exists | path |  |  | path, place | entity_exists:path | True | high |
| cf2 | entity_exists | sky |  |  | natural_scene | entity_exists:sky | True | high |
| cf3 | entity_exists | cloud |  |  | natural_element | entity_exists:cloud | True | high |
| cf4 | entity_exists | trail |  |  |  | entity_exists:trail | True | low |
| cf5 | has_attribute | mountain | snowy |  | material_attribute, material, visual_attribute | has_attribute:mountain:snowy | True | high |
| cf6 | has_attribute | path | rocky |  | material_attribute, material, visual_attribute | has_attribute:path:rocky | True | high |
| cf7 | has_attribute | sky | blue |  | color_attribute, color, visual_attribute | has_attribute:sky:blue | True | high |

### Stage 9 Canonicalization Notes
_none_

## 63

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `37ad4a9f27e6170f690be91cc569967a05f9349e8327ae1a65b9dbf27fe30814`
**parse_path:** `sentence`

> A small bird with a spiky crest perches on a thorny bush.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | bird | bird | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | small | small | size_attribute | chunk0 | 1 | high |
| m2 | object | crest | crest | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | spiky | spiky | modifier_attribute | chunk1 | 5 | medium |
| m4 | object | bush | bush | noun_chunk_root | chunk2 | 11 | high |
| m5 | attribute | thorny | thorny | modifier_attribute | chunk2 | 10 | medium |
| m6 | action | perches | perch | verb_predicate | doc | 7 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> bird |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> crest |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> bush |
| e3 | agent | m6 | m0 | medium | nsubj -> perches |
| e4 | relation | m0 | m2 | high | with |
| e5 | relation | m0 | m4 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | bird | bird | animal | raw_lemma | stage9_seed:parent_seed | animal, living_thing | m0 | raw_mention |  |  |  | True | {"canonical": "entity:bird", "parents": ["entity_parent:animal", "entity_parent:living_thing"]} |
| ent_m2 | object | crest | crest | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:crest", "parents": []} |
| ent_m4 | object | bush | bush | object | raw_lemma | wordnet_synset:shrub.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m4 | raw_mention |  |  |  | True | {"canonical": "entity:bush", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m6 | perches | perch | perch | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:perch", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | perch | agent | agent | none | m0 | ent_m0 | medium | e3 | nsubj -> perches |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e4 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e5 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | bird |  |  | animal, living_thing | entity_exists:bird | True | high |
| cf1 | entity_exists | crest |  |  |  | entity_exists:crest | True | low |
| cf2 | entity_exists | bush |  |  | plant, living_thing | entity_exists:bush | True | high |
| cf3 | has_attribute | bird | small |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:bird:small | True | high |
| cf4 | has_attribute | crest | spiky |  | shape_attribute, shape, visual_attribute | has_attribute:crest:spiky | True | medium |
| cf5 | has_attribute | bush | thorny |  | modifier_attribute, visual_attribute | has_attribute:bush:thorny | True | medium |
| cf6 | action_event | perch |  |  | visual_action | action_event:perch | True | low |
| cf7 | event_role | perch | agent | bird |  | event_role:perch:agent:bird | True | medium |
| cf8 | relation | bird | with | crest | association_relation, visual_relation | relation:bird:with:crest | True | high |
| cf9 | relation | bird | on | bush | spatial_support, visual_relation | relation:bird:on:bush | True | high |

### Stage 9 Canonicalization Notes
_none_

## 64

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `38253930f1c6f2089d2f21a95cd4b1500e0963b889e3bb5a42489534984cb014`
**parse_path:** `sentence`

> Several children run on a dirt track with white lane lines. One boy in a yellow shirt is in the foreground, while others in different colored shirts follow behind him. A green field and a sign reading “Nosotros jugamos con coraje” are visible in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “Nosotros jugamos con coraje” | nosotros_jugamos_con_coraje | quote_text | doc_quote | 40 | high |
| m1 | object | children | child | noun_chunk_root | chunk0 | 1 | high |
| m2 | quantity | Several | several | approximate_quantity | chunk0 | 0 | medium |
| m3 | object | track | track | noun_chunk_root | chunk1 | 6 | high |
| m4 | attribute | dirt | dirt | compound_modifier | chunk1 | 5 | medium |
| m5 | object | lines | line | noun_chunk_root | chunk2 | 10 | high |
| m6 | attribute | white | white | color_attribute | chunk2 | 8 | high |
| m7 | attribute | lane | lane | compound_modifier | chunk2 | 9 | medium |
| m8 | object | boy | boy | noun_chunk_root | chunk3 | 13 | high |
| m9 | quantity | One | one | exact_quantity | chunk3 | 12 | high |
| m10 | object | shirt | shirt | noun_chunk_root | chunk4 | 17 | high |
| m11 | attribute | yellow | yellow | color_attribute | chunk4 | 16 | high |
| m12 | context | foreground | foreground | scene_context | chunk5 | 21 | high |
| m13 | object | shirts | shirt | noun_chunk_root | chunk7 | 28 | high |
| m14 | attribute | different | different | modifier_attribute | chunk7 | 26 | medium |
| m15 | attribute | colored | colored | modifier_attribute | chunk7 | 27 | medium |
| m16 | object | field | field | noun_chunk_root | chunk9 | 35 | high |
| m17 | attribute | green | green | color_attribute | chunk9 | 34 | high |
| m18 | object | sign | sign | noun_chunk_root | chunk10 | 38 | high |
| m19 | context | background | background | scene_context | chunk11 | 45 | high |
| m20 | reference | others | other | contrastive_reference | nominal_reference | 24 | high |
| m21 | action | run | run | verb_predicate | doc | 2 | high |
| m22 | action | follow | follow | verb_predicate | doc | 29 | high |
| m23 | action | reading | read | verb_predicate | doc | 39 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m1 | m2 | medium | chunk0 quantity -> children |
| e1 | has_attribute | m3 | m4 | medium | chunk1 compound -> track |
| e2 | has_attribute | m5 | m6 | high | chunk2 amod -> lines |
| e3 | has_attribute | m5 | m7 | medium | chunk2 compound -> lines |
| e4 | has_quantity | m8 | m9 | high | chunk3 quantity -> boy |
| e5 | has_attribute | m10 | m11 | high | chunk4 amod -> shirt |
| e6 | has_context | scene | m12 | high | scene_context token foreground |
| e7 | has_attribute | m13 | m14 | medium | chunk7 amod -> shirts |
| e8 | has_attribute | m13 | m15 | medium | chunk7 amod -> shirts |
| e9 | has_attribute | m16 | m17 | high | chunk9 amod -> field |
| e10 | has_context | scene | m19 | high | scene_context token background |
| e11 | refers_to | m20 | m1 | high | contrastive_reference others -> children; score=110; margin=22 |
| e12 | agent | m21 | m1 | medium | nsubj -> run |
| e13 | agent | m22 | m1 | medium | nsubj -> follow; resolved others -> children |
| e14 | agent | m23 | m18 | medium | inherited agent acl -> sign |
| e15 | patient | m23 | m0 | medium | dobj -> reading |
| e16 | relation | m1 | m3 | high | on |
| e17 | relation | m3 | m5 | high | with |
| e18 | relation | m8 | m10 | high | in |
| e19 | relation | m8 | m12 | high | in |
| e20 | relation | m1 | m13 | high | in |
| e21 | relation | m1 | m8 | high | behind |
| e22 | relation | m16 | m19 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | child | children | person | raw_lemma | stage9_seed:parent_seed | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m3 | object | track | track | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:track", "parents": []} |
| ent_m5 | object | line | lines | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:line", "parents": []} |
| ent_m8 | object | boy | boy | person | raw_lemma | stage9_seed:parent_seed | person, human | m8 | raw_mention |  |  |  | True | {"canonical": "entity:boy", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m10 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m10 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m12 | context | foreground | foreground | object | raw_lemma | stage9_seed:parent_seed | scene_context | m12 | raw_mention |  |  |  | True | {"canonical": "entity:foreground", "parents": ["entity_parent:scene_context"]} |
| ent_m13 | object | shirt | shirts | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m13 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m16 | object | field | field | object | raw_lemma | wordnet_synset:field.n.01 + stage9_audit | outdoor_scene, place | m16 | raw_mention |  |  |  | True | {"canonical": "entity:field", "parents": ["entity_parent:outdoor_scene", "entity_parent:place"]} |
| ent_m18 | object | sign | sign | document | raw_lemma | stage9_seed:parent_seed | text_carrier, artifact | m18 | raw_mention |  |  |  | True | {"canonical": "entity:sign", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m19 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m19 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| eref_m20 | complement_subset | child | others | person | raw_lemma | stage9_seed:parent_seed | person, human | m20 | stage9_reference | ent_m1 |  | many | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m20 | eref_m20 | m1 | ent_m1 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m21 | run | run | run | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:run", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m22 | follow | follow | follow | raw_action | visual_action_fallback | visual_action |  | agent:m1->eref_m20 | {"canonical": "action:follow", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m23 | reading | read | read | raw_action | stage9_seed:parent_seed | text_interaction_action, visual_action |  | agent:m18->ent_m18; patient:m0->None | {"canonical": "action:read", "parents": ["action_parent:text_interaction_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | run | agent | agent | none | m1 | ent_m1 | medium | e12 | nsubj -> run |  |  |
| ce1 | follow | agent | agent | none | m1 | eref_m20 | medium | e13 | nsubj -> follow; resolved others -> children |  |  |
| ce2 | read | agent | agent | none | m18 | ent_m18 | medium | e14 | inherited agent acl -> sign |  |  |
| ce2 | read | patient | patient | none | m0 |  | medium | e15 | dobj -> reading |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m3 | ent_m1 | ent_m3 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e16 | False | False |  |  |
| cr1 | m3 | m5 | ent_m3 | ent_m5 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e17 | False | False |  |  |
| cr2 | m8 | m10 | ent_m8 | ent_m10 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e18 | False | False |  |  |
| cr3 | m8 | m12 | ent_m8 | ent_m12 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e19 | False | False |  |  |
| cr4 | m1 | m13 | eref_m20 | ent_m13 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e20 | False | False |  |  |
| cr5 | m1 | m8 | ent_m1 | ent_m8 | behind | behind | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e21 | False | False |  |  |
| cr6 | m16 | m19 | ent_m16 | ent_m19 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e22 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf1 | entity_exists | track |  |  |  | entity_exists:track | True | low |
| cf2 | entity_exists | line |  |  |  | entity_exists:line | True | low |
| cf3 | entity_exists | boy |  |  | person, human | entity_exists:boy | True | high |
| cf4 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf5 | entity_exists | foreground |  |  | scene_context | entity_exists:foreground | True | high |
| cf6 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf7 | entity_exists | field |  |  | outdoor_scene, place | entity_exists:field | True | medium |
| cf8 | entity_exists | sign |  |  | text_carrier, artifact | entity_exists:sign | True | high |
| cf9 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf10 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf11 | has_quantity | child | several |  | approximate_quantity, quantity | has_quantity:child:several | True | medium |
| cf12 | has_attribute | track | dirt |  | material_attribute, cleanliness, material, visual_attribute | has_attribute:track:dirt | True | medium |
| cf13 | has_attribute | line | white |  | color_attribute, color, visual_attribute | has_attribute:line:white | True | high |
| cf14 | has_attribute | line | lane |  | compound_modifier, visual_attribute | has_attribute:line:lane | True | medium |
| cf15 | has_quantity | boy | one |  | exact_quantity, quantity | has_quantity:boy:one | True | high |
| cf16 | has_attribute | shirt | yellow |  | color_attribute, color, visual_attribute | has_attribute:shirt:yellow | True | high |
| cf17 | has_attribute | shirt | different |  | modifier_attribute, visual_attribute | has_attribute:shirt:different | True | medium |
| cf18 | has_attribute | shirt | colored |  | modifier_attribute, visual_attribute | has_attribute:shirt:colored | True | medium |
| cf19 | has_attribute | field | green |  | color_attribute, color, visual_attribute | has_attribute:field:green | True | high |
| cf20 | action_event | run |  |  | locomotion_action, visual_action | action_event:run | True | high |
| cf21 | event_role | run | agent | child |  | event_role:run:agent:child | True | medium |
| cf22 | action_event | follow |  |  | visual_action | action_event:follow | True | low |
| cf23 | event_role | follow | agent | child |  | event_role:follow:agent:child | True | medium |
| cf24 | action_event | read |  |  | text_interaction_action, visual_action | action_event:read | True | medium |
| cf25 | event_role | read | agent | sign |  | event_role:read:agent:sign | True | medium |
| cf26 | event_role | read | patient |  |  | event_role:read:patient | False | medium |
| cf27 | relation | child | on | track | spatial_support, visual_relation | relation:child:on:track | True | high |
| cf28 | relation | track | with | line | association_relation, visual_relation | relation:track:with:line | True | high |
| cf29 | relation | boy | in | shirt | spatial_containment, visual_relation | relation:boy:in:shirt | True | high |
| cf30 | relation | boy | in | foreground | spatial_containment, visual_relation | relation:boy:in:foreground | True | high |
| cf31 | relation | child | in | shirt | spatial_containment, visual_relation | relation:child:in:shirt | True | high |
| cf32 | relation | child | behind | boy | spatial_depth, visual_relation | relation:child:behind:boy | True | high |
| cf33 | relation | field | in | background | spatial_containment, visual_relation | relation:field:in:background | True | high |

### Stage 9 Canonicalization Notes
_none_

## 65

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `38fd4b9a989ffd766541728e517093432635fd3e9f1127ec4d08656384924414`
**parse_path:** `sentence`

> A woman in a pink bikini stands in shallow, clear water at the beach. Water sprays upward from beneath her, sending her dark hair flying into the air. Distant hills and calm sea stretch out behind her under a soft sky.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | bikini | bikini | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | pink | pink | color_attribute | chunk1 | 4 | high |
| m3 | object | water | water | noun_chunk_root | chunk2 | 11 | high |
| m4 | attribute | shallow | shallow | modifier_attribute | chunk2 | 8 | medium |
| m5 | attribute | clear | clear | visual_attribute | chunk2 | 10 | medium |
| m6 | object | beach | beach | noun_chunk_root | chunk3 | 14 | high |
| m7 | object | Water | water | noun_chunk_root | chunk4 | 16 | high |
| m8 | object | hair | hair | noun_chunk_root | chunk6 | 26 | high |
| m9 | attribute | dark | dark | visual_attribute | chunk6 | 25 | medium |
| m10 | object | air | air | noun_chunk_root | chunk7 | 30 | high |
| m11 | object | hills | hill | noun_chunk_root | chunk8 | 33 | high |
| m12 | attribute | Distant | distant | modifier_attribute | chunk8 | 32 | medium |
| m13 | object | sea | sea | noun_chunk_root | chunk9 | 36 | high |
| m14 | attribute | calm | calm | modifier_attribute | chunk9 | 35 | medium |
| m15 | object | sky | sky | noun_chunk_root | chunk11 | 44 | high |
| m16 | attribute | soft | soft | modifier_attribute | chunk11 | 43 | medium |
| m17 | action | stands | stand | verb_predicate | doc | 6 | high |
| m18 | action | sprays | spray | verb_predicate | doc | 17 | high |
| m19 | action | sending | send | verb_predicate | doc | 23 | high |
| m20 | action | flying | fly | verb_predicate | doc | 27 | high |
| m21 | action | stretch | stretch | verb_predicate | doc | 37 | high |
| m22 | particle | out | out | phrasal_particle | action_particle | 38 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> bikini |
| e1 | has_attribute | m3 | m4 | medium | chunk2 amod -> water |
| e2 | has_attribute | m3 | m5 | medium | chunk2 amod -> water |
| e3 | has_attribute | m8 | m9 | medium | chunk6 amod -> hair |
| e4 | has_attribute | m11 | m12 | medium | chunk8 amod -> hills |
| e5 | has_attribute | m13 | m14 | medium | chunk9 amod -> sea |
| e6 | has_attribute | m15 | m16 | medium | chunk11 amod -> sky |
| e7 | agent | m17 | m0 | medium | nsubj -> stands |
| e8 | agent | m18 | m7 | medium | nsubj -> sprays |
| e9 | agent | m19 | m7 | medium | inherited agent advcl -> sprays |
| e10 | agent | m20 | m8 | medium | nsubj -> flying |
| e11 | agent | m21 | m11 | medium | nsubj -> stretch |
| e12 | agent | m21 | m13 | medium | nsubj -> stretch |
| e13 | has_particle | m21 | m22 | medium | prt -> stretch |
| e14 | relation | m0 | m1 | high | in |
| e15 | relation | m0 | m3 | high | in |
| e16 | relation | m0 | m6 | medium | at |
| e17 | relation | m8 | m10 | medium | into |
| e18 | relation | m11 | m0 | high | behind |
| e19 | relation | m11 | m15 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | bikini | bikini | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:bikini", "parents": []} |
| ent_m3 | object | water | water | object | raw_lemma | wordnet_synset:water.n.01 + stage9_audit | natural_element | m3 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": ["entity_parent:natural_element"]} |
| ent_m6 | object | beach | beach | object | raw_lemma | wordnet_synset:beach.n.01 + stage9_audit | outdoor_scene, place | m6 | raw_mention |  |  |  | True | {"canonical": "entity:beach", "parents": ["entity_parent:outdoor_scene", "entity_parent:place"]} |
| ent_m7 | object | water | Water | object | raw_lemma | wordnet_synset:water.n.01 + stage9_audit | natural_element | m7 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": ["entity_parent:natural_element"]} |
| ent_m8 | object | hair | hair | object | raw_lemma | stage9_seed:parent_seed | body_part | m8 | raw_mention |  |  |  | True | {"canonical": "entity:hair", "parents": ["entity_parent:body_part"]} |
| ent_m10 | object | air | air | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:air", "parents": []} |
| ent_m11 | object | hill | hills | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:hill", "parents": []} |
| ent_m13 | object | sea | sea | object | raw_lemma | wordnet_synset:sea.n.01 + stage9_audit | body_of_water, place | m13 | raw_mention |  |  |  | True | {"canonical": "entity:sea", "parents": ["entity_parent:body_of_water", "entity_parent:place"]} |
| ent_m15 | object | sky | sky | object | raw_lemma | wordnet_synset:sky.n.01 + stage9_audit | natural_scene | m15 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": ["entity_parent:natural_scene"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m18 | sprays | spray | spray | raw_action | visual_action_fallback | visual_action |  | agent:m7->ent_m7 | {"canonical": "action:spray", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m19 | sending | send | send | raw_action | visual_action_fallback | visual_action |  | agent:m7->ent_m7 | {"canonical": "action:send", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m20 | flying | fly | fly | raw_action | visual_action_fallback | visual_action |  | agent:m8->ent_m8 | {"canonical": "action:fly", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m21 | stretch | stretch | stretch | raw_action | visual_action_fallback | visual_action | out | agent:m11->ent_m11; agent:m13->ent_m13 | {"canonical": "action:stretch", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e7 | nsubj -> stands |  |  |
| ce1 | spray | agent | agent | none | m7 | ent_m7 | medium | e8 | nsubj -> sprays |  |  |
| ce2 | send | agent | agent | none | m7 | ent_m7 | medium | e9 | inherited agent advcl -> sprays |  |  |
| ce3 | fly | agent | agent | none | m8 | ent_m8 | medium | e10 | nsubj -> flying |  |  |
| ce4 | stretch | agent | agent | none | m11 | ent_m11 | medium | e11 | nsubj -> stretch |  |  |
| ce4 | stretch | agent | agent | none | m13 | ent_m13 | medium | e12 | nsubj -> stretch |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e14 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e15 | False | False |  |  |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e16 | False | False |  |  |
| cr3 | m8 | m10 | ent_m8 | ent_m10 | into | into | raw_relation | raw_relation | visual_relation | medium | e17 | False | False |  |  |
| cr4 | m11 | m0 | ent_m11 | ent_m0 | behind | behind | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e18 | False | False |  |  |
| cr5 | m11 | m15 | ent_m11 | ent_m15 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e19 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | bikini |  |  |  | entity_exists:bikini | True | low |
| cf2 | entity_exists | water |  |  | natural_element | entity_exists:water | True | high |
| cf3 | entity_exists | beach |  |  | outdoor_scene, place | entity_exists:beach | True | high |
| cf4 | entity_exists | water |  |  | natural_element | entity_exists:water | True | high |
| cf5 | entity_exists | hair |  |  | body_part | entity_exists:hair | True | high |
| cf6 | entity_exists | air |  |  |  | entity_exists:air | True | low |
| cf7 | entity_exists | hill |  |  |  | entity_exists:hill | True | low |
| cf8 | entity_exists | sea |  |  | body_of_water, place | entity_exists:sea | True | high |
| cf9 | entity_exists | sky |  |  | natural_scene | entity_exists:sky | True | high |
| cf10 | has_attribute | bikini | pink |  | color_attribute, color, visual_attribute | has_attribute:bikini:pink | True | high |
| cf11 | has_attribute | water | shallow |  | size_attribute, depth, visual_attribute | has_attribute:water:shallow | True | medium |
| cf12 | has_attribute | water | clear |  | weather_attribute, opaqeness, weather, visual_attribute | has_attribute:water:clear | True | medium |
| cf13 | has_attribute | hair | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:hair:dark | True | medium |
| cf14 | has_attribute | hill | distant |  | modifier_attribute, visual_attribute | has_attribute:hill:distant | True | medium |
| cf15 | has_attribute | sea | calm |  | modifier_attribute, visual_attribute | has_attribute:sea:calm | True | medium |
| cf16 | has_attribute | sky | soft |  | texture_attribute, clean_exact_overlap, hardness, texture, visual_attribute | has_attribute:sky:soft | True | medium |
| cf17 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf18 | event_role | stand | agent | woman |  | event_role:stand:agent:woman | True | medium |
| cf19 | action_event | spray |  |  | visual_action | action_event:spray | True | low |
| cf20 | event_role | spray | agent | water |  | event_role:spray:agent:water | True | medium |
| cf21 | action_event | send |  |  | visual_action | action_event:send | True | low |
| cf22 | event_role | send | agent | water |  | event_role:send:agent:water | True | medium |
| cf23 | action_event | fly |  |  | visual_action | action_event:fly | True | low |
| cf24 | event_role | fly | agent | hair |  | event_role:fly:agent:hair | True | medium |
| cf25 | action_event | stretch |  |  | visual_action | action_event:stretch | True | low |
| cf26 | event_role | stretch | agent | hill |  | event_role:stretch:agent:hill | True | medium |
| cf27 | event_role | stretch | agent | sea |  | event_role:stretch:agent:sea | True | medium |
| cf28 | relation | woman | in | bikini | spatial_containment, visual_relation | relation:woman:in:bikini | True | high |
| cf29 | relation | woman | in | water | spatial_containment, visual_relation | relation:woman:in:water | True | high |
| cf30 | relation | woman | at | beach | spatial_location, visual_relation | relation:woman:at:beach | True | medium |
| cf31 | relation | hair | into | air | visual_relation | relation:hair:into:air | True | medium |
| cf32 | relation | hill | behind | woman | spatial_depth, visual_relation | relation:hill:behind:woman | True | high |
| cf33 | relation | hill | under | sky | spatial_vertical, visual_relation | relation:hill:under:sky | True | high |

### Stage 9 Canonicalization Notes
_none_

## 66

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `3b6f749877c95a70b9e7bdfcb602ef3b1a48f94b7b350a6aa552db91126f4014`
**parse_path:** `sentence`

> Several small dishes of Japanese food are arranged on a dark wooden tray. The items include a bowl with pickled vegetables, a black plate with sliced fish and garnish, and a white bowl with colorful salad-like ingredients.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | dishes | dish | noun_chunk_root | chunk0 | 2 | high |
| m1 | quantity | Several | several | approximate_quantity | chunk0 | 0 | medium |
| m2 | attribute | small | small | size_attribute | chunk0 | 1 | high |
| m3 | object | food | food | noun_chunk_root | chunk1 | 5 | high |
| m4 | attribute | Japanese | japanese | modifier_attribute | chunk1 | 4 | medium |
| m5 | object | tray | tray | noun_chunk_root | chunk2 | 12 | high |
| m6 | attribute | dark | dark | visual_attribute | chunk2 | 10 | medium |
| m7 | attribute | wooden | wooden | material_attribute | chunk2 | 11 | high |
| m8 | object | items | item | noun_chunk_root | chunk3 | 15 | high |
| m9 | object | bowl | bowl | noun_chunk_root | chunk4 | 18 | high |
| m10 | object | vegetables | vegetable | noun_chunk_root | chunk5 | 21 | high |
| m11 | attribute | pickled | pickle | state_attribute | chunk5 | 20 | medium |
| m12 | object | plate | plate | noun_chunk_root | chunk6 | 25 | high |
| m13 | attribute | black | black | color_attribute | chunk6 | 24 | high |
| m14 | object | fish | fish | noun_chunk_root | chunk7 | 28 | high |
| m15 | attribute | sliced | slice | state_attribute | chunk7 | 27 | medium |
| m16 | object | garnish | garnish | noun_chunk_root | chunk8 | 30 | high |
| m17 | object | bowl | bowl | noun_chunk_root | chunk9 | 35 | high |
| m18 | attribute | white | white | color_attribute | chunk9 | 34 | high |
| m19 | object | ingredients | ingredient | noun_chunk_root | chunk10 | 39 | high |
| m20 | attribute | colorful | colorful | modifier_attribute | chunk10 | 37 | medium |
| m21 | attribute | salad-like | salad-like | modifier_attribute | chunk10 | 38 | medium |
| m22 | action | arranged | arrange | verb_predicate | doc | 7 | high |
| m23 | action | include | include | verb_predicate | doc | 16 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | medium | chunk0 quantity -> dishes |
| e1 | has_attribute | m0 | m2 | high | chunk0 amod -> dishes |
| e2 | has_attribute | m3 | m4 | medium | chunk1 amod -> food |
| e3 | has_attribute | m5 | m6 | medium | chunk2 amod -> tray |
| e4 | has_attribute | m5 | m7 | high | chunk2 amod -> tray |
| e5 | has_attribute | m10 | m11 | medium | chunk5 amod -> vegetables |
| e6 | has_attribute | m12 | m13 | high | chunk6 amod -> plate |
| e7 | has_attribute | m14 | m15 | medium | chunk7 amod -> fish |
| e8 | has_attribute | m17 | m18 | high | chunk9 amod -> bowl |
| e9 | has_attribute | m19 | m20 | medium | chunk10 amod -> ingredients |
| e10 | has_attribute | m19 | m21 | medium | chunk10 amod -> ingredients |
| e11 | agent | m22 | m0 | medium | nsubjpass -> arranged |
| e12 | agent | m23 | m8 | medium | nsubj -> include |
| e13 | patient | m23 | m9 | medium | dobj -> include |
| e14 | patient | m23 | m12 | medium | dobj -> include |
| e15 | patient | m23 | m17 | medium | dobj -> include |
| e16 | relation | m0 | m3 | medium | of |
| e17 | relation | m0 | m5 | high | on |
| e18 | relation | m9 | m10 | high | with |
| e19 | relation | m12 | m14 | high | with |
| e20 | relation | m12 | m16 | high | with |
| e21 | relation | m17 | m19 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | dish | dishes | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:dish", "parents": []} |
| ent_m3 | object | food | food | object | raw_lemma | wordnet_synset:food.n.01 + stage9_audit | food | m3 | raw_mention |  |  |  | True | {"canonical": "entity:food", "parents": ["entity_parent:food"]} |
| ent_m5 | object | tray | tray | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:tray", "parents": []} |
| ent_m8 | object | item | items | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:item", "parents": []} |
| ent_m9 | object | bowl | bowl | object | raw_lemma | COCO object label + wordnet_hypernym:container.n.01 + stage9_audit | container, artifact | m9 | raw_mention |  |  |  | True | {"canonical": "entity:bowl", "parents": ["entity_parent:container", "entity_parent:artifact"]} |
| ent_m10 | object | vegetable | vegetables | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:vegetable", "parents": []} |
| ent_m12 | object | plate | plate | object | raw_lemma | wordnet_synset:plate.n.04 + stage9_audit | dishware, artifact | m12 | raw_mention |  |  |  | True | {"canonical": "entity:plate", "parents": ["entity_parent:dishware", "entity_parent:artifact"]} |
| ent_m14 | object | fish | fish | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:fish", "parents": []} |
| ent_m16 | object | garnish | garnish | object | raw_lemma | none |  | m16 | raw_mention |  |  |  | True | {"canonical": "entity:garnish", "parents": []} |
| ent_m17 | object | bowl | bowl | object | raw_lemma | COCO object label + wordnet_hypernym:container.n.01 + stage9_audit | container, artifact | m17 | raw_mention |  |  |  | True | {"canonical": "entity:bowl", "parents": ["entity_parent:container", "entity_parent:artifact"]} |
| ent_m19 | object | ingredient | ingredients | object | raw_lemma | none |  | m19 | raw_mention |  |  |  | True | {"canonical": "entity:ingredient", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m22 | arranged | arrange | arrange | raw_action | visual_action_fallback | visual_action |  | patient<-theme[passive_to_active]:m0->ent_m0 | {"canonical": "action:arrange", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m23 | include | include | include | raw_action | visual_action_fallback | visual_action |  | agent:m8->ent_m8; patient:m9->ent_m9; patient:m12->ent_m12; patient:m17->ent_m17 | {"canonical": "action:include", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | arrange | patient | theme | passive_to_active | m0 | ent_m0 | medium | e11 | nsubjpass -> arranged |  |  |
| ce1 | include | agent | agent | none | m8 | ent_m8 | medium | e12 | nsubj -> include |  |  |
| ce1 | include | patient | patient | none | m9 | ent_m9 | medium | e13 | dobj -> include |  |  |
| ce1 | include | patient | patient | none | m12 | ent_m12 | medium | e14 | dobj -> include |  |  |
| ce1 | include | patient | patient | none | m17 | ent_m17 | medium | e15 | dobj -> include |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e16 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e17 | False | False |  |  |
| cr2 | m9 | m10 | ent_m9 | ent_m10 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e18 | False | False |  |  |
| cr3 | m12 | m14 | ent_m12 | ent_m14 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e19 | False | False |  |  |
| cr4 | m12 | m16 | ent_m12 | ent_m16 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e20 | False | False |  |  |
| cr5 | m17 | m19 | ent_m17 | ent_m19 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e21 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | dish |  |  |  | entity_exists:dish | True | low |
| cf1 | entity_exists | food |  |  | food | entity_exists:food | True | high |
| cf2 | entity_exists | tray |  |  |  | entity_exists:tray | True | low |
| cf3 | entity_exists | item |  |  |  | entity_exists:item | True | low |
| cf4 | entity_exists | bowl |  |  | container, artifact | entity_exists:bowl | True | high |
| cf5 | entity_exists | vegetable |  |  |  | entity_exists:vegetable | True | low |
| cf6 | entity_exists | plate |  |  | dishware, artifact | entity_exists:plate | True | high |
| cf7 | entity_exists | fish |  |  |  | entity_exists:fish | True | low |
| cf8 | entity_exists | garnish |  |  |  | entity_exists:garnish | True | low |
| cf9 | entity_exists | bowl |  |  | container, artifact | entity_exists:bowl | True | high |
| cf10 | entity_exists | ingredient |  |  |  | entity_exists:ingredient | True | low |
| cf11 | has_quantity | dish | several |  | approximate_quantity, quantity | has_quantity:dish:several | True | medium |
| cf12 | has_attribute | dish | small |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:dish:small | True | high |
| cf13 | has_attribute | food | japanese |  | modifier_attribute, visual_attribute | has_attribute:food:japanese | True | medium |
| cf14 | has_attribute | tray | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:tray:dark | True | medium |
| cf15 | has_attribute | tray | wood |  | material_attribute, material, visual_attribute | has_attribute:tray:wood | True | high |
| cf16 | has_attribute | vegetable | pickle |  | state_attribute, visual_attribute | has_attribute:vegetable:pickle | True | medium |
| cf17 | has_attribute | plate | black |  | color_attribute, color, visual_attribute | has_attribute:plate:black | True | high |
| cf18 | has_attribute | fish | slice |  | state_attribute, visual_attribute | has_attribute:fish:slice | True | medium |
| cf19 | has_attribute | bowl | white |  | color_attribute, color, visual_attribute | has_attribute:bowl:white | True | high |
| cf20 | has_attribute | ingredient | colorful |  | color_attribute, color_quantity, visual_attribute | has_attribute:ingredient:colorful | True | medium |
| cf21 | has_attribute | ingredient | salad-like |  | modifier_attribute, visual_attribute | has_attribute:ingredient:salad-like | True | medium |
| cf22 | action_event | arrange |  |  | visual_action | action_event:arrange | True | low |
| cf23 | event_role | arrange | patient | dish |  | event_role:arrange:patient:dish | True | medium |
| cf24 | action_event | include |  |  | visual_action | action_event:include | True | low |
| cf25 | event_role | include | agent | item |  | event_role:include:agent:item | True | medium |
| cf26 | event_role | include | patient | bowl |  | event_role:include:patient:bowl | True | medium |
| cf27 | event_role | include | patient | plate |  | event_role:include:patient:plate | True | medium |
| cf28 | event_role | include | patient | bowl |  | event_role:include:patient:bowl | True | medium |
| cf29 | relation | dish | of | food | part_relation, visual_relation | relation:dish:of:food | True | medium |
| cf30 | relation | dish | on | tray | spatial_support, visual_relation | relation:dish:on:tray | True | high |
| cf31 | relation | bowl | with | vegetable | association_relation, visual_relation | relation:bowl:with:vegetable | True | high |
| cf32 | relation | plate | with | fish | association_relation, visual_relation | relation:plate:with:fish | True | high |
| cf33 | relation | plate | with | garnish | association_relation, visual_relation | relation:plate:with:garnish | True | high |
| cf34 | relation | bowl | with | ingredient | association_relation, visual_relation | relation:bowl:with:ingredient | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m22 | e11 | m0 |  |  | {"action_mention_id": "m22", "kind": "passive_subject_to_patient", "raw_edge_id": "e11", "raw_role": "theme", "role": "patient", "target": "m0", "voice_normalization": "passive_to_active"} |

## 67

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `3c2fd0027fd5a16e9c3726f1501d0b2cd2bc11b530900eb648a20b48dd8db414`
**parse_path:** `tag_list`

> green outfit, children, park, microphone, grass, trees

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | outfit | outfit | segment_head | t0 | 1 | high |
| m1 | attribute | green | green | attribute | t0 | 0 | high |
| m2 | object | children | child | segment_head | t1 | 0 | high |
| m3 | object | park | park | segment_head | t2 | 0 | high |
| m4 | object | microphone | microphone | segment_head | t3 | 0 | high |
| m5 | object | grass | grass | segment_head | t4 | 0 | high |
| m6 | object | trees | tree | segment_head | t5 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> outfit |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | outfit | outfit | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:outfit", "parents": []} |
| ent_m2 | object | child | children | person | raw_lemma | stage9_seed:parent_seed | person, human | m2 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m3 | object | park | park | object | raw_lemma | wordnet_synset:park.n.02 + stage9_audit | outdoor_scene, place | m3 | raw_mention |  |  |  | True | {"canonical": "entity:park", "parents": ["entity_parent:outdoor_scene", "entity_parent:place"]} |
| ent_m4 | object | microphone | microphone | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:microphone", "parents": []} |
| ent_m5 | object | grass | grass | object | raw_lemma | wordnet_synset:grass.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m5 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m6 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m6 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |

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
| cf0 | entity_exists | outfit |  |  |  | entity_exists:outfit | True | low |
| cf1 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf2 | entity_exists | park |  |  | outdoor_scene, place | entity_exists:park | True | medium |
| cf3 | entity_exists | microphone |  |  |  | entity_exists:microphone | True | low |
| cf4 | entity_exists | grass |  |  | plant, living_thing | entity_exists:grass | True | high |
| cf5 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf6 | has_attribute | outfit | green |  | color_attribute, color, visual_attribute | has_attribute:outfit:green | True | high |

### Stage 9 Canonicalization Notes
_none_

## 68

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `3c3317a4efb150fb1fb7d271bc97bf5c951faa5973014b6bb7cae5c48beb3014`
**parse_path:** `sentence`

> Two men shake hands under a white tent. One wears a suit, the other a uniform with medals and a sash.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | men | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Two | two | exact_quantity | chunk0 | 0 | high |
| m2 | object | hands | hand | noun_chunk_root | chunk1 | 3 | high |
| m3 | object | tent | tent | noun_chunk_root | chunk2 | 7 | high |
| m4 | attribute | white | white | color_attribute | chunk2 | 6 | high |
| m5 | object | suit | suit | noun_chunk_root | chunk3 | 12 | high |
| m6 | object | medals | medal | noun_chunk_root | chunk4 | 19 | high |
| m7 | object | sash | sash | noun_chunk_root | chunk5 | 22 | high |
| m8 | reference | One | one | singular_substitute | nominal_reference | 9 | high |
| m9 | reference | other | other | contrastive_reference | nominal_reference | 15 | high |
| m10 | action | shake | shake | verb_predicate | doc | 2 | high |
| m11 | action | wears | wear | verb_predicate | doc | 10 | high |
| m12 | object | uniform | uniform | relation_head | doc | 17 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> men |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> tent |
| e2 | refers_to | m8 | m0 | high | singular_substitute One -> men; score=109 |
| e3 | refers_to | m9 | m0 | high | contrastive_reference other -> men; score=118; margin=30 |
| e4 | agent | m10 | m0 | medium | nsubj -> shake |
| e5 | patient | m10 | m2 | medium | dobj -> shake |
| e6 | agent | m11 | m0 | medium | nsubj -> wears; resolved One -> men |
| e7 | patient | m11 | m5 | medium | dobj -> wears |
| e8 | relation | m0 | m3 | high | under |
| e9 | relation | m12 | m6 | high | with |
| e10 | relation | m12 | m7 | high | with |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | men | person | stage9_seed:synonym_seed | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | hand | hands | object | raw_lemma | stage9_seed:parent_seed | body_part | m2 | raw_mention |  |  |  | True | {"canonical": "entity:hand", "parents": ["entity_parent:body_part"]} |
| ent_m3 | object | tent | tent | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:tent", "parents": []} |
| ent_m5 | object | suit | suit | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m5 | raw_mention |  |  |  | True | {"canonical": "entity:suit", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m6 | object | medal | medals | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:medal", "parents": []} |
| ent_m7 | object | sash | sash | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:sash", "parents": []} |
| ent_m12 | object | uniform | uniform | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m12 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| eref_m8 | instance | man | One | person | raw_lemma | stage9_seed:parent_seed | person, human | m8 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| eref_m9 | contrastive_instance | man | other | person | raw_lemma | stage9_seed:parent_seed | person, human | m9 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m8 | eref_m8 | m0 | ent_m0 | high |  |
| refers_to | m9 | eref_m9 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | shake | shake | shake | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m2->ent_m2 | {"canonical": "action:shake", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m11 | wears | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m0->eref_m8; patient:m5->ent_m5 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | shake | agent | agent | none | m0 | ent_m0 | medium | e4 | nsubj -> shake |  |  |
| ce0 | shake | patient | patient | none | m2 | ent_m2 | medium | e5 | dobj -> shake |  |  |
| ce1 | wear | agent | agent | none | m0 | eref_m8 | medium | e6 | nsubj -> wears; resolved One -> men |  |  |
| ce1 | wear | patient | patient | none | m5 | ent_m5 | medium | e7 | dobj -> wears |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e8 | False | False |  |  |
| cr1 | m12 | m6 | ent_m12 | ent_m6 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e9 | False | False |  |  |
| cr2 | m12 | m7 | ent_m12 | ent_m7 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e10 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | hand |  |  | body_part | entity_exists:hand | True | high |
| cf2 | entity_exists | tent |  |  |  | entity_exists:tent | True | low |
| cf3 | entity_exists | suit |  |  | clothing, wearable | entity_exists:suit | True | high |
| cf4 | entity_exists | medal |  |  |  | entity_exists:medal | True | low |
| cf5 | entity_exists | sash |  |  |  | entity_exists:sash | True | low |
| cf6 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf7 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf8 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf9 | has_quantity | man | two |  | exact_quantity, quantity | has_quantity:man:two | True | high |
| cf10 | has_attribute | tent | white |  | color_attribute, color, visual_attribute | has_attribute:tent:white | True | high |
| cf11 | action_event | shake |  |  | visual_action | action_event:shake | True | low |
| cf12 | event_role | shake | agent | man |  | event_role:shake:agent:man | True | medium |
| cf13 | event_role | shake | patient | hand |  | event_role:shake:patient:hand | True | medium |
| cf14 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf15 | event_role | wear | agent | man |  | event_role:wear:agent:man | True | medium |
| cf16 | event_role | wear | patient | suit |  | event_role:wear:patient:suit | True | medium |
| cf17 | relation | man | under | tent | spatial_vertical, visual_relation | relation:man:under:tent | True | high |
| cf18 | relation | uniform | with | medal | association_relation, visual_relation | relation:uniform:with:medal | True | high |
| cf19 | relation | uniform | with | sash | association_relation, visual_relation | relation:uniform:with:sash | True | high |

### Stage 9 Canonicalization Notes
_none_

## 69

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `3dc33e25c1232f8c43b0edf4d45d654ce7722d590e05267925b163d65ea0a814`
**parse_path:** `sentence`

> Two men sit at a table playing chess, each with a nameplate in front of them. One wears a light blue shirt and rests his chin on his hand, while the other in a denim jacket leans forward with hands clasped. A metal barrier stands behind them, and people are visible in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | men | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Two | two | exact_quantity | chunk0 | 0 | high |
| m2 | object | table | table | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | chess | ches | noun_chunk_root | chunk2 | 7 | high |
| m4 | quantity | each | each | distributive_quantity | chunk3 | 9 | high |
| m5 | object | nameplate | nameplate | noun_chunk_root | chunk4 | 12 | high |
| m6 | object | shirt | shirt | noun_chunk_root | chunk7 | 23 | high |
| m7 | attribute | light | light | visual_attribute | chunk7 | 21 | medium |
| m8 | attribute | blue | blue | color_attribute | chunk7 | 22 | high |
| m9 | object | chin | chin | noun_chunk_root | chunk8 | 27 | high |
| m10 | object | hand | hand | noun_chunk_root | chunk9 | 30 | high |
| m11 | object | jacket | jacket | noun_chunk_root | chunk10 | 38 | high |
| m12 | attribute | denim | denim | material_attribute | chunk10 | 37 | high |
| m13 | object | hands | hand | noun_chunk_root | chunk11 | 42 | high |
| m14 | object | barrier | barrier | noun_chunk_root | chunk12 | 47 | high |
| m15 | attribute | metal | metal | material_attribute | chunk12 | 46 | high |
| m16 | object | people | people | noun_chunk_root | chunk14 | 53 | high |
| m17 | context | background | background | scene_context | chunk15 | 58 | high |
| m18 | reference | each | each | distributive_reference | nominal_reference | 9 | high |
| m19 | reference | One | one | singular_substitute | nominal_reference | 18 | high |
| m20 | reference | other | other | contrastive_reference | nominal_reference | 34 | high |
| m21 | action | sit | sit | verb_predicate | doc | 2 | high |
| m22 | action | playing | play | verb_predicate | doc | 6 | high |
| m23 | action | wears | wear | verb_predicate | doc | 19 | high |
| m24 | action | rests | rest | verb_predicate | doc | 25 | high |
| m25 | action | leans | lean | verb_predicate | doc | 39 | high |
| m26 | action | clasped | clasp | verb_predicate | doc | 43 | high |
| m27 | action | stands | stand | verb_predicate | doc | 48 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> men |
| e1 | has_attribute | m6 | m7 | medium | chunk7 amod -> shirt |
| e2 | has_attribute | m6 | m8 | high | chunk7 amod -> shirt |
| e3 | has_attribute | m11 | m12 | high | chunk10 compound -> jacket |
| e4 | has_attribute | m14 | m15 | high | chunk12 compound -> barrier |
| e5 | has_context | scene | m17 | high | scene_context token background |
| e6 | refers_to | m18 | m0 | high | distributive_reference each -> men; score=119; margin=30 |
| e7 | refers_to | m19 | m0 | high | singular_substitute One -> men; score=94 |
| e8 | refers_to | m20 | m0 | high | contrastive_reference other -> men; score=100; margin=20 |
| e9 | agent | m21 | m0 | medium | nsubj -> sit |
| e10 | agent | m22 | m0 | medium | inherited agent advcl -> sit |
| e11 | patient | m22 | m3 | medium | dobj -> playing |
| e12 | agent | m23 | m0 | medium | nsubj -> wears; resolved One -> men |
| e13 | patient | m23 | m6 | medium | dobj -> wears |
| e14 | agent | m24 | m0 | medium | inherited agent conj -> wears |
| e15 | patient | m24 | m9 | medium | dobj -> rests |
| e16 | agent | m25 | m0 | medium | nsubj -> leans; resolved other -> men |
| e17 | agent | m26 | m13 | medium | nsubj -> clasped |
| e18 | agent | m27 | m14 | medium | nsubj -> stands |
| e19 | relation | m0 | m2 | medium | at |
| e20 | relation | m0 | m5 | high | with |
| e21 | relation | m5 | m0 | high | in_front_of |
| e22 | relation | m0 | m10 | high | on |
| e23 | relation | m0 | m11 | high | in |
| e24 | relation | m14 | m0 | high | behind |
| e25 | relation | m16 | m17 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | men | person | stage9_seed:synonym_seed | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | table | table | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m3 | object | ches | chess | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:ches", "parents": []} |
| ent_m5 | object | nameplate | nameplate | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:nameplate", "parents": []} |
| ent_m6 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m6 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m9 | object | chin | chin | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:chin", "parents": []} |
| ent_m10 | object | hand | hand | object | raw_lemma | stage9_seed:parent_seed | body_part | m10 | raw_mention |  |  |  | True | {"canonical": "entity:hand", "parents": ["entity_parent:body_part"]} |
| ent_m11 | object | jacket | jacket | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m11 | raw_mention |  |  |  | True | {"canonical": "entity:jacket", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m13 | object | hand | hands | object | raw_lemma | stage9_seed:parent_seed | body_part | m13 | raw_mention |  |  |  | True | {"canonical": "entity:hand", "parents": ["entity_parent:body_part"]} |
| ent_m14 | object | barrier | barrier | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:barrier", "parents": []} |
| ent_m16 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m16 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m17 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m17 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| eref_m18 | reference | man | each | person | raw_lemma | stage9_seed:parent_seed | person, human | m18 | stage9_reference | ent_m0 |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| eref_m19 | instance | man | One | person | raw_lemma | stage9_seed:parent_seed | person, human | m19 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| eref_m20 | contrastive_instance | man | other | person | raw_lemma | stage9_seed:parent_seed | person, human | m20 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m18 | eref_m18 | m0 | ent_m0 | high |  |
| refers_to | m19 | eref_m19 | m0 | ent_m0 | high |  |
| refers_to | m20 | eref_m20 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m21 | sit | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m22 | playing | play | play | raw_action | stage9_seed:parent_seed | activity_action, visual_action |  | agent:m0->ent_m0; patient:m3->ent_m3 | {"canonical": "action:play", "parents": ["action_parent:activity_action", "action_parent:visual_action"]} |  |
| ce2 | m23 | wears | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m0->eref_m19; patient:m6->ent_m6 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce3 | m24 | rests | rest | rest | raw_action | wordnet_synset:rest.v.01 + stage9_audit | support_state_action, visual_action |  | agent:m0->eref_m19; patient:m9->ent_m9 | {"canonical": "action:rest", "parents": ["action_parent:support_state_action", "action_parent:visual_action"]} |  |
| ce4 | m25 | leans | lean | lean | raw_action | wordnet_synset:lean.v.01 + stage9_audit | body_pose_action, support_state_action, visual_action |  | agent:m0->eref_m20 | {"canonical": "action:lean", "parents": ["action_parent:body_pose_action", "action_parent:support_state_action", "action_parent:visual_action"]} |  |
| ce5 | m26 | clasped | clasp | clasp | raw_action | visual_action_fallback | visual_action |  | agent:m13->ent_m13 | {"canonical": "action:clasp", "parents": ["action_parent:visual_action"]} |  |
| ce6 | m27 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m14->ent_m14 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | agent | none | m0 | ent_m0 | medium | e9 | nsubj -> sit |  |  |
| ce1 | play | agent | agent | none | m0 | ent_m0 | medium | e10 | inherited agent advcl -> sit |  |  |
| ce1 | play | patient | patient | none | m3 | ent_m3 | medium | e11 | dobj -> playing |  |  |
| ce2 | wear | agent | agent | none | m0 | eref_m19 | medium | e12 | nsubj -> wears; resolved One -> men |  |  |
| ce2 | wear | patient | patient | none | m6 | ent_m6 | medium | e13 | dobj -> wears |  |  |
| ce3 | rest | agent | agent | none | m0 | eref_m19 | medium | e14 | inherited agent conj -> wears |  | conj_agent_inherited_from_reference_canonical_target |
| ce3 | rest | patient | patient | none | m9 | ent_m9 | medium | e15 | dobj -> rests |  |  |
| ce4 | lean | agent | agent | none | m0 | eref_m20 | medium | e16 | nsubj -> leans; resolved other -> men |  |  |
| ce5 | clasp | agent | agent | none | m13 | ent_m13 | medium | e17 | nsubj -> clasped |  |  |
| ce6 | stand | agent | agent | none | m14 | ent_m14 | medium | e18 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e19 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e20 | False | False |  |  |
| cr2 | m5 | m0 | ent_m5 | ent_m0 | in_front_of | in_front_of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e21 | False | False |  |  |
| cr3 | m0 | m10 | ent_m9 | ent_m10 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e22 | False | False | pp_source_disambiguation | patient_body_part_anchor |
| cr4 | m0 | m11 | eref_m20 | ent_m11 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e23 | False | False |  |  |
| cr5 | m14 | m0 | ent_m14 | ent_m0 | behind | behind | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e24 | False | False |  |  |
| cr6 | m16 | m17 | ent_m16 | ent_m17 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e25 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf2 | entity_exists | ches |  |  |  | entity_exists:ches | True | low |
| cf3 | entity_exists | nameplate |  |  |  | entity_exists:nameplate | True | low |
| cf4 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf5 | entity_exists | chin |  |  |  | entity_exists:chin | True | low |
| cf6 | entity_exists | hand |  |  | body_part | entity_exists:hand | True | high |
| cf7 | entity_exists | jacket |  |  | clothing, wearable | entity_exists:jacket | True | high |
| cf8 | entity_exists | hand |  |  | body_part | entity_exists:hand | True | high |
| cf9 | entity_exists | barrier |  |  |  | entity_exists:barrier | True | low |
| cf10 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf11 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf12 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf13 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf14 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf15 | has_quantity | man | two |  | exact_quantity, quantity | has_quantity:man:two | True | high |
| cf16 | has_attribute | shirt | light |  | visual_attribute | has_attribute:shirt:light | True | medium |
| cf17 | has_attribute | shirt | blue |  | color_attribute, color, visual_attribute | has_attribute:shirt:blue | True | high |
| cf18 | has_attribute | jacket | denim |  | material_attribute, material, visual_attribute | has_attribute:jacket:denim | True | high |
| cf19 | has_attribute | barrier | metal |  | material_attribute, material, non_textile_material_type, visual_attribute | has_attribute:barrier:metal | True | high |
| cf20 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf21 | event_role | sit | agent | man |  | event_role:sit:agent:man | True | medium |
| cf22 | action_event | play |  |  | activity_action, visual_action | action_event:play | True | high |
| cf23 | event_role | play | agent | man |  | event_role:play:agent:man | True | medium |
| cf24 | event_role | play | patient | ches |  | event_role:play:patient:ches | True | medium |
| cf25 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf26 | event_role | wear | agent | man |  | event_role:wear:agent:man | True | medium |
| cf27 | event_role | wear | patient | shirt |  | event_role:wear:patient:shirt | True | medium |
| cf28 | action_event | rest |  |  | support_state_action, visual_action | action_event:rest | True | medium |
| cf29 | event_role | rest | agent | man |  | event_role:rest:agent:man | True | medium |
| cf30 | event_role | rest | patient | chin |  | event_role:rest:patient:chin | True | medium |
| cf31 | action_event | lean |  |  | body_pose_action, support_state_action, visual_action | action_event:lean | True | high |
| cf32 | event_role | lean | agent | man |  | event_role:lean:agent:man | True | medium |
| cf33 | action_event | clasp |  |  | visual_action | action_event:clasp | True | low |
| cf34 | event_role | clasp | agent | hand |  | event_role:clasp:agent:hand | True | medium |
| cf35 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf36 | event_role | stand | agent | barrier |  | event_role:stand:agent:barrier | True | medium |
| cf37 | relation | man | at | table | spatial_location, visual_relation | relation:man:at:table | True | medium |
| cf38 | relation | man | with | nameplate | association_relation, visual_relation | relation:man:with:nameplate | True | high |
| cf39 | relation | nameplate | in_front_of | man | spatial_depth, visual_relation | relation:nameplate:in_front_of:man | True | high |
| cf40 | relation | chin | on | hand | spatial_support, visual_relation | relation:chin:on:hand | True | high |
| cf41 | relation | man | in | jacket | spatial_containment, visual_relation | relation:man:in:jacket | True | high |
| cf42 | relation | barrier | behind | man | spatial_depth, visual_relation | relation:barrier:behind:man | True | high |
| cf43 | relation | people | in | background | spatial_containment, visual_relation | relation:people:in:background | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| conj_agent_reference_target_inherited | m24 |  |  | eref_m19 |  | {"action_mention_id": "m24", "canonical_target": "eref_m19", "kind": "conj_agent_reference_target_inherited", "source_action_mention_id": "m23"} |
| pp_source_disambiguated | m24 | e22 |  | ent_m10 | patient_body_part_anchor | {"action_mention_id": "m24", "canonical_action": "rest", "canonical_source": "ent_m9", "canonical_target": "ent_m10", "confidence": "high", "kind": "pp_source_disambiguated", "previous_canonical_source": "ent_m0", "raw_edge_id": "e22", "raw_source": "m0", "raw_target": "m10", "reason": "patient_body_part_anchor", "relation": "on"} |

## 70

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `3dfe1525b1e6171c354eabe145616a23c9cc23b39ea60a700455daa4227a1c14`
**parse_path:** `tag_list`

> strawberry cake, whipped cream, dark plate, wooden panel, bright light

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | cake | cake | segment_head | t0 | 1 | high |
| m1 | attribute | strawberry | strawberry | attribute | t0 | 0 | high |
| m2 | object | whipped cream | whipped_cream | segment_head | t1 | 0 | high |
| m3 | object | plate | plate | segment_head | t2 | 1 | high |
| m4 | attribute | dark | dark | attribute | t2 | 0 | high |
| m5 | object | panel | panel | segment_head | t3 | 1 | high |
| m6 | attribute | wooden | wooden | attribute | t3 | 0 | high |
| m7 | object | light | light | segment_head | t4 | 1 | high |
| m8 | attribute | bright | bright | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> cake |
| e1 | has_attribute | m3 | m4 | high | t2 internal amod -> plate |
| e2 | has_attribute | m5 | m6 | high | t3 internal compound -> panel |
| e3 | has_attribute | m7 | m8 | high | t4 internal amod -> light |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | cake | cake | object | raw_lemma | COCO object label + wordnet_hypernym:food.n.01 + stage9_audit | prepared_food, food | m0 | raw_mention |  |  |  | True | {"canonical": "entity:cake", "parents": ["entity_parent:prepared_food", "entity_parent:food"]} |
| ent_m2 | object | whipped_cream | whipped cream | object | lvis_object\|visual_genome_object_synset\|wordnet_noun_mwe | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:whipped_cream", "parents": []} |
| ent_m3 | object | plate | plate | object | raw_lemma | wordnet_synset:plate.n.04 + stage9_audit | dishware, artifact | m3 | raw_mention |  |  |  | True | {"canonical": "entity:plate", "parents": ["entity_parent:dishware", "entity_parent:artifact"]} |
| ent_m5 | object | panel | panel | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:panel", "parents": []} |
| ent_m7 | object | light | light | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:light", "parents": []} |

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
| cf0 | entity_exists | cake |  |  | prepared_food, food | entity_exists:cake | True | high |
| cf1 | entity_exists | whipped_cream |  |  |  | entity_exists:whipped_cream | True | high |
| cf2 | entity_exists | plate |  |  | dishware, artifact | entity_exists:plate | True | high |
| cf3 | entity_exists | panel |  |  |  | entity_exists:panel | True | low |
| cf4 | entity_exists | light |  |  |  | entity_exists:light | True | low |
| cf5 | has_attribute | cake | strawberry |  | attribute, visual_attribute | has_attribute:cake:strawberry | True | high |
| cf6 | has_attribute | plate | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:plate:dark | True | high |
| cf7 | has_attribute | panel | wood |  | material_attribute, material, visual_attribute | has_attribute:panel:wood | True | high |
| cf8 | has_attribute | light | bright |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:light:bright | True | high |

### Stage 9 Canonicalization Notes
_none_

## 71

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `3ee5e72a9d60584099af9a3e0a468861e9f1a910d2876b8557e55d4bb98be414`
**parse_path:** `sentence`

> Three women sit at a table outdoors, one speaking into a microphone while the others listen.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | women | woman | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Three | three | exact_quantity | chunk0 | 0 | high |
| m2 | object | table | table | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | microphone | microphone | noun_chunk_root | chunk2 | 12 | high |
| m4 | context | outdoors | outdoors | scene_context | doc | 6 | high |
| m5 | reference | one | one | singular_substitute | nominal_reference | 8 | high |
| m6 | reference | others | other | contrastive_reference | nominal_reference | 15 | high |
| m7 | action | sit | sit | verb_predicate | doc | 2 | high |
| m8 | action | speaking | speak | verb_predicate | doc | 9 | high |
| m9 | action | listen | listen | verb_predicate | doc | 16 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> women |
| e1 | has_context | scene | m4 | high | scene_context token outdoors |
| e2 | refers_to | m5 | m0 | high | singular_substitute one -> women; score=103 |
| e3 | refers_to | m6 | m0 | high | contrastive_reference others -> women; score=112 |
| e4 | agent | m7 | m0 | medium | nsubj -> sit |
| e5 | agent | m8 | m0 | medium | nsubj -> speaking; resolved one -> women |
| e6 | agent | m9 | m0 | medium | nsubj -> listen; resolved others -> women |
| e7 | relation | m0 | m2 | medium | at |
| e8 | relation | m0 | m3 | medium | into |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | women | person | stage9_seed:synonym_seed | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | table | table | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m2 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m3 | object | microphone | microphone | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:microphone", "parents": []} |
| ent_m4 | context | outdoors | outdoors | object | raw_lemma | stage9_seed:parent_seed | scene_context | m4 | raw_mention |  |  |  | True | {"canonical": "entity:outdoors", "parents": ["entity_parent:scene_context"]} |
| eref_m5 | instance | woman | one | person | raw_lemma | stage9_seed:parent_seed | person, human | m5 | stage9_reference | ent_m0 |  | 1 | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| eref_m6 | complement_subset | woman | others | person | raw_lemma | stage9_seed:parent_seed | person, human | m6 | stage9_reference | ent_m0 |  | many | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m5 | eref_m5 | m0 | ent_m0 | high |  |
| refers_to | m6 | eref_m6 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | sit | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m8 | speaking | speak | speak | raw_action | stage9_seed:parent_seed | communication_action, visual_action |  | agent:m0->eref_m5 | {"canonical": "action:speak", "parents": ["action_parent:communication_action", "action_parent:visual_action"]} |  |
| ce2 | m9 | listen | listen | listen | raw_action | visual_action_fallback | visual_action |  | agent:m0->eref_m6 | {"canonical": "action:listen", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | agent | none | m0 | ent_m0 | medium | e4 | nsubj -> sit |  |  |
| ce1 | speak | agent | agent | none | m0 | eref_m5 | medium | e5 | nsubj -> speaking; resolved one -> women |  |  |
| ce2 | listen | agent | agent | none | m0 | eref_m6 | medium | e6 | nsubj -> listen; resolved others -> women |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e7 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | into | into | raw_relation | raw_relation | visual_relation | medium | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf2 | entity_exists | microphone |  |  |  | entity_exists:microphone | True | low |
| cf3 | entity_exists | outdoors |  |  | scene_context | entity_exists:outdoors | True | high |
| cf4 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf5 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf6 | has_quantity | woman | three |  | exact_quantity, quantity | has_quantity:woman:three | True | high |
| cf7 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf8 | event_role | sit | agent | woman |  | event_role:sit:agent:woman | True | medium |
| cf9 | action_event | speak |  |  | communication_action, visual_action | action_event:speak | True | medium |
| cf10 | event_role | speak | agent | woman |  | event_role:speak:agent:woman | True | medium |
| cf11 | action_event | listen |  |  | visual_action | action_event:listen | True | low |
| cf12 | event_role | listen | agent | woman |  | event_role:listen:agent:woman | True | medium |
| cf13 | relation | woman | at | table | spatial_location, visual_relation | relation:woman:at:table | True | medium |
| cf14 | relation | woman | into | microphone | visual_relation | relation:woman:into:microphone | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 72

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `3ef32f9a38a29c7f765a681ca5b1b849ab42593f8e2da27565d2b8f5f15fc414`
**parse_path:** `sentence`

> A tall waterfall cascades down a rocky cliff into a pool below. Lush green foliage frames the scene in the foreground, with trees and vegetation covering the surrounding cliffs. The water creates a misty spray as it hits the surface.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | waterfall | waterfall | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | tall | tall | size_attribute | chunk0 | 1 | high |
| m2 | object | cliff | cliff | noun_chunk_root | chunk1 | 7 | high |
| m3 | attribute | rocky | rocky | modifier_attribute | chunk1 | 6 | medium |
| m4 | object | pool | pool | noun_chunk_root | chunk2 | 10 | high |
| m5 | object | foliage | foliage | noun_chunk_root | chunk3 | 15 | high |
| m6 | attribute | Lush | lush | modifier_attribute | chunk3 | 13 | medium |
| m7 | attribute | green | green | color_attribute | chunk3 | 14 | high |
| m8 | context | scene | scene | scene_context | chunk4 | 18 | high |
| m9 | context | foreground | foreground | scene_context | chunk5 | 21 | high |
| m10 | object | trees | tree | noun_chunk_root | chunk6 | 24 | high |
| m11 | object | vegetation | vegetation | noun_chunk_root | chunk7 | 26 | high |
| m12 | object | cliffs | cliff | noun_chunk_root | chunk8 | 30 | high |
| m13 | attribute | surrounding | surround | state_attribute | chunk8 | 29 | medium |
| m14 | object | water | water | noun_chunk_root | chunk9 | 33 | high |
| m15 | object | spray | spray | noun_chunk_root | chunk10 | 37 | high |
| m16 | attribute | misty | misty | modifier_attribute | chunk10 | 36 | medium |
| m17 | object | surface | surface | noun_chunk_root | chunk12 | 42 | high |
| m18 | action | cascades | cascade | verb_predicate | doc | 3 | high |
| m19 | action | frames | frame | verb_predicate | doc | 16 | high |
| m20 | action | covering | cover | verb_predicate | doc | 27 | high |
| m21 | action | creates | create | verb_predicate | doc | 34 | high |
| m22 | action | hits | hit | verb_predicate | doc | 40 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> waterfall |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> cliff |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> foliage |
| e3 | has_attribute | m5 | m7 | high | chunk3 amod -> foliage |
| e4 | has_context | scene | m8 | high | scene_context token scene |
| e5 | has_context | scene | m9 | high | scene_context token foreground |
| e6 | has_attribute | m12 | m13 | medium | chunk8 amod -> cliffs |
| e7 | has_attribute | m15 | m16 | medium | chunk10 amod -> spray |
| e8 | agent | m18 | m0 | medium | nsubj -> cascades |
| e9 | agent | m19 | m5 | medium | nsubj -> frames |
| e10 | patient | m19 | m8 | medium | dobj -> frames |
| e11 | agent | m20 | m10 | medium | nsubj -> covering |
| e12 | agent | m20 | m11 | medium | nsubj -> covering |
| e13 | patient | m20 | m12 | medium | dobj -> covering |
| e14 | agent | m21 | m14 | medium | nsubj -> creates |
| e15 | patient | m21 | m15 | medium | dobj -> creates |
| e16 | agent | m22 | m10 | medium | nsubj -> hits; resolved it -> trees |
| e17 | patient | m22 | m17 | medium | dobj -> hits |
| e18 | relation | m0 | m2 | medium | down |
| e19 | relation | m0 | m4 | medium | into |
| e20 | relation | m8 | m9 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | waterfall | waterfall | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:waterfall", "parents": []} |
| ent_m2 | object | cliff | cliff | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:cliff", "parents": []} |
| ent_m4 | object | pool | pool | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:pool", "parents": []} |
| ent_m5 | object | foliage | foliage | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:foliage", "parents": []} |
| ent_m8 | context | scene | scene | object | raw_lemma | stage9_seed:parent_seed | scene_context | m8 | raw_mention |  |  |  | True | {"canonical": "entity:scene", "parents": ["entity_parent:scene_context"]} |
| ent_m9 | context | foreground | foreground | object | raw_lemma | stage9_seed:parent_seed | scene_context | m9 | raw_mention |  |  |  | True | {"canonical": "entity:foreground", "parents": ["entity_parent:scene_context"]} |
| ent_m10 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m10 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m11 | object | vegetation | vegetation | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:vegetation", "parents": []} |
| ent_m12 | object | cliff | cliffs | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:cliff", "parents": []} |
| ent_m14 | object | water | water | object | raw_lemma | wordnet_synset:water.n.01 + stage9_audit | natural_element | m14 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": ["entity_parent:natural_element"]} |
| ent_m15 | object | spray | spray | object | raw_lemma | none |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:spray", "parents": []} |
| ent_m17 | object | surface | surface | object | raw_lemma | none |  | m17 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | cascades | cascade | cascade | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:cascade", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m19 | frames | frame | frame | raw_action | visual_action_fallback | visual_action |  | agent:m5->ent_m5; patient:m8->ent_m8 | {"canonical": "action:frame", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m20 | covering | cover | cover | raw_action | wordnet_synset:cover.v.01 + stage9_audit | occlusion_or_covering_action, visual_action |  | agent:m10->ent_m10; agent:m11->ent_m11; patient:m12->ent_m12 | {"canonical": "action:cover", "parents": ["action_parent:occlusion_or_covering_action", "action_parent:visual_action"]} |  |
| ce3 | m21 | creates | create | create | raw_action | visual_action_fallback | visual_action |  | agent:m14->ent_m14; patient:m15->ent_m15 | {"canonical": "action:create", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m22 | hits | hit | hit | raw_action | wordnet_synset:hit.v.01 + stage9_audit | contact_action, visual_action |  | agent:m10->ent_m10; patient:m17->ent_m17 | {"canonical": "action:hit", "parents": ["action_parent:contact_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | cascade | agent | agent | none | m0 | ent_m0 | medium | e8 | nsubj -> cascades |  |  |
| ce1 | frame | agent | agent | none | m5 | ent_m5 | medium | e9 | nsubj -> frames |  |  |
| ce1 | frame | patient | patient | none | m8 | ent_m8 | medium | e10 | dobj -> frames |  |  |
| ce2 | cover | agent | agent | none | m10 | ent_m10 | medium | e11 | nsubj -> covering |  |  |
| ce2 | cover | agent | agent | none | m11 | ent_m11 | medium | e12 | nsubj -> covering |  |  |
| ce2 | cover | patient | patient | none | m12 | ent_m12 | medium | e13 | dobj -> covering |  |  |
| ce3 | create | agent | agent | none | m14 | ent_m14 | medium | e14 | nsubj -> creates |  |  |
| ce3 | create | patient | patient | none | m15 | ent_m15 | medium | e15 | dobj -> creates |  |  |
| ce4 | hit | agent | agent | none | m10 | ent_m10 | medium | e16 | nsubj -> hits; resolved it -> trees |  |  |
| ce4 | hit | patient | patient | none | m17 | ent_m17 | medium | e17 | dobj -> hits |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | down | down | raw_relation | raw_relation | visual_relation | medium | e18 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | into | into | raw_relation | raw_relation | visual_relation | medium | e19 | False | False |  |  |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e20 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | waterfall |  |  |  | entity_exists:waterfall | True | low |
| cf1 | entity_exists | cliff |  |  |  | entity_exists:cliff | True | low |
| cf2 | entity_exists | pool |  |  |  | entity_exists:pool | True | low |
| cf3 | entity_exists | foliage |  |  |  | entity_exists:foliage | True | low |
| cf4 | entity_exists | scene |  |  | scene_context | entity_exists:scene | True | high |
| cf5 | entity_exists | foreground |  |  | scene_context | entity_exists:foreground | True | high |
| cf6 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf7 | entity_exists | vegetation |  |  |  | entity_exists:vegetation | True | low |
| cf8 | entity_exists | cliff |  |  |  | entity_exists:cliff | True | low |
| cf9 | entity_exists | water |  |  | natural_element | entity_exists:water | True | high |
| cf10 | entity_exists | spray |  |  |  | entity_exists:spray | True | low |
| cf11 | entity_exists | surface |  |  |  | entity_exists:surface | True | low |
| cf12 | has_attribute | waterfall | tall |  | size_attribute, height, visual_attribute | has_attribute:waterfall:tall | True | high |
| cf13 | has_attribute | cliff | rocky |  | material_attribute, material, visual_attribute | has_attribute:cliff:rocky | True | medium |
| cf14 | has_attribute | foliage | lush |  | modifier_attribute, visual_attribute | has_attribute:foliage:lush | True | medium |
| cf15 | has_attribute | foliage | green |  | color_attribute, color, visual_attribute | has_attribute:foliage:green | True | high |
| cf16 | has_attribute | cliff | surround |  | state_attribute, visual_attribute | has_attribute:cliff:surround | True | medium |
| cf17 | has_attribute | spray | misty |  | modifier_attribute, visual_attribute | has_attribute:spray:misty | True | medium |
| cf18 | action_event | cascade |  |  | visual_action | action_event:cascade | True | low |
| cf19 | event_role | cascade | agent | waterfall |  | event_role:cascade:agent:waterfall | True | medium |
| cf20 | action_event | frame |  |  | visual_action | action_event:frame | True | low |
| cf21 | event_role | frame | agent | foliage |  | event_role:frame:agent:foliage | True | medium |
| cf22 | event_role | frame | patient | scene |  | event_role:frame:patient:scene | True | medium |
| cf23 | action_event | cover |  |  | occlusion_or_covering_action, visual_action | action_event:cover | True | high |
| cf24 | event_role | cover | agent | tree |  | event_role:cover:agent:tree | True | medium |
| cf25 | event_role | cover | agent | vegetation |  | event_role:cover:agent:vegetation | True | medium |
| cf26 | event_role | cover | patient | cliff |  | event_role:cover:patient:cliff | True | medium |
| cf27 | action_event | create |  |  | visual_action | action_event:create | True | low |
| cf28 | event_role | create | agent | water |  | event_role:create:agent:water | True | medium |
| cf29 | event_role | create | patient | spray |  | event_role:create:patient:spray | True | medium |
| cf30 | action_event | hit |  |  | contact_action, visual_action | action_event:hit | True | high |
| cf31 | event_role | hit | agent | tree |  | event_role:hit:agent:tree | True | medium |
| cf32 | event_role | hit | patient | surface |  | event_role:hit:patient:surface | True | medium |
| cf33 | relation | waterfall | down | cliff | visual_relation | relation:waterfall:down:cliff | True | medium |
| cf34 | relation | waterfall | into | pool | visual_relation | relation:waterfall:into:pool | True | medium |
| cf35 | relation | scene | in | foreground | spatial_containment, visual_relation | relation:scene:in:foreground | True | high |

### Stage 9 Canonicalization Notes
_none_

## 73

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `3fc554fbcb69acbbdfe10e7f1a0d4c9338e8d80d620dbe29bc0fe748f6e86814`
**parse_path:** `sentence`

> Three swords are displayed on a stand in a museum setting. Each has a unique handle and blade design.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | swords | sword | noun_chunk_root | chunk0 | 1 | high |
| m1 | quantity | Three | three | exact_quantity | chunk0 | 0 | high |
| m2 | object | stand | stand | noun_chunk_root | chunk1 | 6 | high |
| m3 | context | setting | setting | scene_context | chunk2 | 10 | high |
| m4 | attribute | museum | museum | compound_modifier | chunk2 | 9 | medium |
| m5 | quantity | Each | each | distributive_quantity | chunk3 | 12 | high |
| m6 | object | design | design | noun_chunk_root | chunk4 | 19 | high |
| m7 | attribute | unique | unique | modifier_attribute | chunk4 | 15 | medium |
| m8 | reference | Each | each | distributive_reference | nominal_reference | 12 | high |
| m9 | action | displayed | display | verb_predicate | doc | 3 | high |
| m10 | action | has | have | verb_predicate | doc | 13 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> swords |
| e1 | has_context | scene | m3 | high | scene_context token setting |
| e2 | has_attribute | m3 | m4 | medium | chunk2 compound -> setting |
| e3 | has_attribute | m6 | m7 | medium | chunk4 amod -> design |
| e4 | refers_to | m8 | m0 | high | distributive_reference Each -> swords; score=108 |
| e5 | agent | m9 | m0 | medium | nsubjpass -> displayed |
| e6 | agent | m10 | m0 | medium | nsubj -> has; resolved Each -> swords |
| e7 | patient | m10 | m6 | medium | dobj -> has |
| e8 | relation | m0 | m2 | high | on |
| e9 | relation | m0 | m3 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sword | swords | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:sword", "parents": []} |
| ent_m2 | object | stand | stand | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:stand", "parents": []} |
| ent_m3 | context | setting | setting | object | raw_lemma | stage9_seed:parent_seed | scene_context | m3 | raw_mention |  |  |  | True | {"canonical": "entity:setting", "parents": ["entity_parent:scene_context"]} |
| ent_m6 | object | design | design | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:design", "parents": []} |
| eref_m8 | reference | sword | Each | object | raw_lemma | none |  | m8 | stage9_reference | ent_m0 |  |  | True | {"canonical": "entity:sword", "parents": []} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m8 | eref_m8 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | displayed | display | display | raw_action | wordnet_synset:display.v.01 + stage9_audit | visual_presentation_action, visual_action |  | patient<-theme[passive_to_active]:m0->ent_m0 | {"canonical": "action:display", "parents": ["action_parent:visual_presentation_action", "action_parent:visual_action"]} |  |
| ce1 | m10 | has | have | have | raw_action | visual_action_fallback | visual_action |  | agent:m0->eref_m8; patient:m6->ent_m6 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | display | patient | theme | passive_to_active | m0 | ent_m0 | medium | e5 | nsubjpass -> displayed |  |  |
| ce1 | have | agent | agent | none | m0 | eref_m8 | medium | e6 | nsubj -> has; resolved Each -> swords |  |  |
| ce1 | have | patient | patient | none | m6 | ent_m6 | medium | e7 | dobj -> has |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e8 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | sword |  |  |  | entity_exists:sword | True | low |
| cf1 | entity_exists | stand |  |  |  | entity_exists:stand | True | low |
| cf2 | entity_exists | setting |  |  | scene_context | entity_exists:setting | True | high |
| cf3 | entity_exists | design |  |  |  | entity_exists:design | True | low |
| cf4 | entity_exists | sword |  |  |  | entity_exists:sword | True | low |
| cf5 | has_quantity | sword | three |  | exact_quantity, quantity | has_quantity:sword:three | True | high |
| cf6 | has_attribute | setting | museum |  | compound_modifier, visual_attribute | has_attribute:setting:museum | True | medium |
| cf7 | has_attribute | design | unique |  | modifier_attribute, visual_attribute | has_attribute:design:unique | True | medium |
| cf8 | action_event | display |  |  | visual_presentation_action, visual_action | action_event:display | True | high |
| cf9 | event_role | display | patient | sword |  | event_role:display:patient:sword | True | medium |
| cf10 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf11 | event_role | have | agent | sword |  | event_role:have:agent:sword | True | medium |
| cf12 | event_role | have | patient | design |  | event_role:have:patient:design | True | medium |
| cf13 | relation | sword | on | stand | spatial_support, visual_relation | relation:sword:on:stand | True | high |
| cf14 | relation | sword | in | setting | spatial_containment, visual_relation | relation:sword:in:setting | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m9 | e5 | m0 |  |  | {"action_mention_id": "m9", "kind": "passive_subject_to_patient", "raw_edge_id": "e5", "raw_role": "theme", "role": "patient", "target": "m0", "voice_normalization": "passive_to_active"} |

## 74

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `41eadfcb8656112ba20fe03fce3a770277c1593469fc4ae86da7784a9ffef814`
**parse_path:** `sentence`

> A young girl in a pink floral jacket and owl hat stands in deep snow.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | girl | girl | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | young | young | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | jacket | jacket | noun_chunk_root | chunk1 | 7 | high |
| m3 | attribute | pink | pink | color_attribute | chunk1 | 5 | high |
| m4 | attribute | floral | floral | modifier_attribute | chunk1 | 6 | medium |
| m5 | object | hat | hat | noun_chunk_root | chunk2 | 10 | high |
| m6 | attribute | owl | owl | compound_modifier | chunk2 | 9 | medium |
| m7 | object | snow | snow | noun_chunk_root | chunk3 | 14 | high |
| m8 | attribute | deep | deep | modifier_attribute | chunk3 | 13 | medium |
| m9 | action | stands | stand | verb_predicate | doc | 11 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> girl |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> jacket |
| e2 | has_attribute | m2 | m4 | medium | chunk1 amod -> jacket |
| e3 | has_attribute | m5 | m6 | medium | chunk2 compound -> hat |
| e4 | has_attribute | m7 | m8 | medium | chunk3 amod -> snow |
| e5 | agent | m9 | m0 | medium | nsubj -> stands |
| e6 | relation | m0 | m2 | high | in |
| e7 | relation | m0 | m5 | high | in |
| e8 | relation | m0 | m7 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | girl | girl | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:girl", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | jacket | jacket | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m2 | raw_mention |  |  |  | True | {"canonical": "entity:jacket", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m5 | object | hat | hat | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:hat", "parents": []} |
| ent_m7 | object | snow | snow | object | raw_lemma | wordnet_synset:snow.n.01 + stage9_audit | natural_element | m7 | raw_mention |  |  |  | True | {"canonical": "entity:snow", "parents": ["entity_parent:natural_element"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e5 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e6 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e7 | False | False |  |  |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | girl |  |  | person, human | entity_exists:girl | True | high |
| cf1 | entity_exists | jacket |  |  | clothing, wearable | entity_exists:jacket | True | high |
| cf2 | entity_exists | hat |  |  |  | entity_exists:hat | True | low |
| cf3 | entity_exists | snow |  |  | natural_element | entity_exists:snow | True | high |
| cf4 | has_attribute | girl | young |  | modifier_attribute, visual_attribute | has_attribute:girl:young | True | medium |
| cf5 | has_attribute | jacket | pink |  | color_attribute, color, visual_attribute | has_attribute:jacket:pink | True | high |
| cf6 | has_attribute | jacket | floral |  | pattern_attribute, pattern, pattern_marking, textile_pattern, visual_attribute | has_attribute:jacket:floral | True | medium |
| cf7 | has_attribute | hat | owl |  | compound_modifier, visual_attribute | has_attribute:hat:owl | True | medium |
| cf8 | has_attribute | snow | deep |  | size_attribute, depth, visual_attribute | has_attribute:snow:deep | True | medium |
| cf9 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf10 | event_role | stand | agent | girl |  | event_role:stand:agent:girl | True | medium |
| cf11 | relation | girl | in | jacket | spatial_containment, visual_relation | relation:girl:in:jacket | True | high |
| cf12 | relation | girl | in | hat | spatial_containment, visual_relation | relation:girl:in:hat | True | high |
| cf13 | relation | girl | in | snow | spatial_containment, visual_relation | relation:girl:in:snow | True | high |

### Stage 9 Canonicalization Notes
_none_

## 75

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `43bc81e7a594453a5ae3934e8308b7edc25eb629c4f2db7115b8124686036c14`
**parse_path:** `sentence`

> Several basketball players in blue and white uniforms are on a court behind a chain-link fence. One player with the number 5 raises his hand, while others stand nearby, including one wearing number 6. A sign reading “NO MARKING SHOES ON THE COURTS” is visible on the fence.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “NO MARKING SHOES ON THE COURTS” | no_marking_shoes_on_the_courts | quote_text | doc_quote | 41 | high |
| m1 | object | players | player | noun_chunk_root | chunk0 | 2 | high |
| m2 | quantity | Several | several | approximate_quantity | chunk0 | 0 | medium |
| m3 | attribute | basketball | basketball | compound_modifier | chunk0 | 1 | medium |
| m4 | object | uniforms | uniform | noun_chunk_root | chunk1 | 7 | high |
| m5 | attribute | blue | blue | color_attribute | chunk1 | 4 | high |
| m6 | attribute | white | white | color_attribute | chunk1 | 6 | high |
| m7 | object | court | court | noun_chunk_root | chunk2 | 11 | high |
| m8 | object | fence | fence | noun_chunk_root | chunk3 | 15 | high |
| m9 | attribute | chain-link | chain-link | compound_modifier | chunk3 | 14 | medium |
| m10 | object | player | player | noun_chunk_root | chunk4 | 18 | high |
| m11 | quantity | One | one | exact_quantity | chunk4 | 17 | high |
| m12 | object | number | number | noun_chunk_root | chunk5 | 21 | high |
| m13 | object | hand | hand | noun_chunk_root | chunk6 | 25 | high |
| m14 | object | number | number | noun_chunk_root | chunk8 | 35 | high |
| m15 | object | sign | sign | noun_chunk_root | chunk9 | 39 | high |
| m16 | object | fence | fence | noun_chunk_root | chunk11 | 46 | high |
| m17 | reference | others | other | contrastive_reference | nominal_reference | 28 | high |
| m18 | reference | one | one | singular_substitute | nominal_reference | 33 | high |
| m19 | action | raises | raise | verb_predicate | doc | 23 | high |
| m20 | action | stand | stand | verb_predicate | doc | 29 | high |
| m21 | action | including | include | verb_predicate | doc | 32 | high |
| m22 | action | wearing | wear | verb_predicate | doc | 34 | high |
| m23 | action | reading | read | verb_predicate | doc | 40 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m1 | m2 | medium | chunk0 quantity -> players |
| e1 | has_attribute | m1 | m3 | medium | chunk0 compound -> players |
| e2 | has_attribute | m4 | m5 | high | chunk1 amod -> uniforms |
| e3 | has_attribute | m4 | m6 | high | chunk1 conj -> uniforms |
| e4 | has_attribute | m8 | m9 | medium | chunk3 compound -> fence |
| e5 | has_quantity | m10 | m11 | high | chunk4 quantity -> player |
| e6 | refers_to | m17 | m1 | high | contrastive_reference others -> players; score=110 |
| e7 | refers_to | m18 | m1 | high | singular_substitute one -> players; score=94; margin=20 |
| e8 | agent | m19 | m10 | medium | nsubj -> raises |
| e9 | patient | m19 | m13 | medium | dobj -> raises |
| e10 | agent | m20 | m1 | medium | nsubj -> stand; resolved others -> players |
| e11 | patient | m21 | m1 | medium | pobj -> including; resolved one -> players |
| e12 | agent | m22 | m1 | medium | inherited agent acl -> one |
| e13 | patient | m22 | m14 | medium | dobj -> wearing |
| e14 | agent | m23 | m15 | medium | inherited agent acl -> sign |
| e15 | patient | m23 | m0 | medium | dobj -> reading |
| e16 | relation | m1 | m4 | high | in |
| e17 | relation | m1 | m7 | high | on |
| e18 | relation | m1 | m8 | high | behind |
| e19 | relation | m10 | m12 | high | with |
| e20 | relation | m15 | m16 | high | on |

### Skipped Raw Concept Edges
| type | source | target | confidence | reason | evidence |
| --- | --- | --- | --- | --- | --- |
| relation | m1 | m1 | medium | self_edge_after_coref | include |

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | player | players | person | raw_lemma | stage9_seed:parent_seed | person, human | m1 | raw_mention |  |  |  | True | {"canonical": "entity:player", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m4 | object | uniform | uniforms | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m7 | object | court | court | object | raw_lemma | wordnet_synset:court.n.01 + stage9_audit | sports_place, place | m7 | raw_mention |  |  |  | True | {"canonical": "entity:court", "parents": ["entity_parent:sports_place", "entity_parent:place"]} |
| ent_m8 | object | fence | fence | object | raw_lemma | wordnet_synset:fence.n.01 + stage9_audit | structure, artifact | m8 | raw_mention |  |  |  | True | {"canonical": "entity:fence", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m10 | object | player | player | person | raw_lemma | stage9_seed:parent_seed | person, human | m10 | raw_mention |  |  |  | True | {"canonical": "entity:player", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m12 | object | number | number | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:number", "parents": []} |
| ent_m13 | object | hand | hand | object | raw_lemma | stage9_seed:parent_seed | body_part | m13 | raw_mention |  |  |  | True | {"canonical": "entity:hand", "parents": ["entity_parent:body_part"]} |
| ent_m14 | object | number | number | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:number", "parents": []} |
| ent_m15 | object | sign | sign | document | raw_lemma | stage9_seed:parent_seed | text_carrier, artifact | m15 | raw_mention |  |  |  | True | {"canonical": "entity:sign", "parents": ["entity_parent:text_carrier", "entity_parent:artifact"]} |
| ent_m16 | object | fence | fence | object | raw_lemma | wordnet_synset:fence.n.01 + stage9_audit | structure, artifact | m16 | raw_mention |  |  |  | True | {"canonical": "entity:fence", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| eref_m17 | complement_subset | player | others | person | raw_lemma | stage9_seed:parent_seed | person, human | m17 | stage9_reference | ent_m1 |  | many | True | {"canonical": "entity:player", "parents": ["entity_parent:person", "entity_parent:human"]} |
| eref_m18 | instance | player | one | person | raw_lemma | stage9_seed:parent_seed | person, human | m18 | stage9_reference | ent_m1 |  | 1 | True | {"canonical": "entity:player", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m17 | eref_m17 | m1 | ent_m1 | high |  |
| refers_to | m18 | eref_m18 | m1 | ent_m1 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m19 | raises | raise | raise | raw_action | visual_action_fallback | visual_action |  | agent:m10->ent_m10; patient:m13->ent_m13 | {"canonical": "action:raise", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m20 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m1->eref_m17 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce2 | m21 | including | include | include | raw_action | visual_action_fallback | visual_action |  | patient:m1->eref_m18 | {"canonical": "action:include", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m22 | wearing | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m1->eref_m18; patient:m14->ent_m14 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce4 | m23 | reading | read | read | raw_action | stage9_seed:parent_seed | text_interaction_action, visual_action |  | agent:m15->ent_m15; patient:m0->None | {"canonical": "action:read", "parents": ["action_parent:text_interaction_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | raise | agent | agent | none | m10 | ent_m10 | medium | e8 | nsubj -> raises |  |  |
| ce0 | raise | patient | patient | none | m13 | ent_m13 | medium | e9 | dobj -> raises |  |  |
| ce1 | stand | agent | agent | none | m1 | eref_m17 | medium | e10 | nsubj -> stand; resolved others -> players |  |  |
| ce2 | include | patient | patient | none | m1 | eref_m18 | medium | e11 | pobj -> including; resolved one -> players |  |  |
| ce3 | wear | agent | agent | none | m1 | eref_m18 | medium | e12 | inherited agent acl -> one |  |  |
| ce3 | wear | patient | patient | none | m14 | ent_m14 | medium | e13 | dobj -> wearing |  |  |
| ce4 | read | agent | agent | none | m15 | ent_m15 | medium | e14 | inherited agent acl -> sign |  |  |
| ce4 | read | patient | patient | none | m0 |  | medium | e15 | dobj -> reading |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m4 | ent_m1 | ent_m4 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e16 | False | False |  |  |
| cr1 | m1 | m7 | ent_m1 | ent_m7 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e17 | False | False |  |  |
| cr2 | m1 | m8 | ent_m1 | ent_m8 | behind | behind | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e18 | False | False |  |  |
| cr3 | m10 | m12 | ent_m10 | ent_m12 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e19 | False | False |  |  |
| cr4 | m15 | m16 | ent_m15 | ent_m16 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e20 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | player |  |  | person, human | entity_exists:player | True | high |
| cf1 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf2 | entity_exists | court |  |  | sports_place, place | entity_exists:court | True | medium |
| cf3 | entity_exists | fence |  |  | structure, artifact | entity_exists:fence | True | high |
| cf4 | entity_exists | player |  |  | person, human | entity_exists:player | True | high |
| cf5 | entity_exists | number |  |  |  | entity_exists:number | True | low |
| cf6 | entity_exists | hand |  |  | body_part | entity_exists:hand | True | high |
| cf7 | entity_exists | number |  |  |  | entity_exists:number | True | low |
| cf8 | entity_exists | sign |  |  | text_carrier, artifact | entity_exists:sign | True | high |
| cf9 | entity_exists | fence |  |  | structure, artifact | entity_exists:fence | True | high |
| cf10 | entity_exists | player |  |  | person, human | entity_exists:player | True | high |
| cf11 | entity_exists | player |  |  | person, human | entity_exists:player | True | high |
| cf12 | has_quantity | player | several |  | approximate_quantity, quantity | has_quantity:player:several | True | medium |
| cf13 | has_attribute | player | basketball |  | compound_modifier, visual_attribute | has_attribute:player:basketball | True | medium |
| cf14 | has_attribute | uniform | blue |  | color_attribute, color, visual_attribute | has_attribute:uniform:blue | True | high |
| cf15 | has_attribute | uniform | white |  | color_attribute, color, visual_attribute | has_attribute:uniform:white | True | high |
| cf16 | has_attribute | fence | chain-link |  | compound_modifier, visual_attribute | has_attribute:fence:chain-link | True | medium |
| cf17 | has_quantity | player | one |  | exact_quantity, quantity | has_quantity:player:one | True | high |
| cf18 | action_event | raise |  |  | visual_action | action_event:raise | True | low |
| cf19 | event_role | raise | agent | player |  | event_role:raise:agent:player | True | medium |
| cf20 | event_role | raise | patient | hand |  | event_role:raise:patient:hand | True | medium |
| cf21 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf22 | event_role | stand | agent | player |  | event_role:stand:agent:player | True | medium |
| cf23 | action_event | include |  |  | visual_action | action_event:include | True | low |
| cf24 | event_role | include | patient | player |  | event_role:include:patient:player | True | medium |
| cf25 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf26 | event_role | wear | agent | player |  | event_role:wear:agent:player | True | medium |
| cf27 | event_role | wear | patient | number |  | event_role:wear:patient:number | True | medium |
| cf28 | action_event | read |  |  | text_interaction_action, visual_action | action_event:read | True | medium |
| cf29 | event_role | read | agent | sign |  | event_role:read:agent:sign | True | medium |
| cf30 | event_role | read | patient |  |  | event_role:read:patient | False | medium |
| cf31 | relation | player | in | uniform | spatial_containment, visual_relation | relation:player:in:uniform | True | high |
| cf32 | relation | player | on | court | spatial_support, visual_relation | relation:player:on:court | True | high |
| cf33 | relation | player | behind | fence | spatial_depth, visual_relation | relation:player:behind:fence | True | high |
| cf34 | relation | player | with | number | association_relation, visual_relation | relation:player:with:number | True | high |
| cf35 | relation | sign | on | fence | spatial_support, visual_relation | relation:sign:on:fence | True | high |

### Stage 9 Canonicalization Notes
_none_

## 76

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `440a406878704dac38b48f810adab983379090cfc88ba57e174f27e254f10814`
**parse_path:** `tag_list`

> construction, safety, banquet, machinery, roadwork, orange, black

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | construction | construction | segment_head | t0 | 0 | high |
| m1 | object | safety | safety | segment_head | t1 | 0 | high |
| m2 | object | banquet | banquet | segment_head | t2 | 0 | high |
| m3 | object | machinery | machinery | segment_head | t3 | 0 | high |
| m4 | object | roadwork | roadwork | segment_head | t4 | 0 | high |
| m5 | attribute | orange | orange | color_attribute | t5 | 0 | high |
| m6 | attribute | black | black | color_attribute | t6 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | candidate_has_attribute | m4 | m5 | low | t5 adjacent floating attribute |
| e1 | candidate_has_attribute | m4 | m6 | low | t6 adjacent floating attribute |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | construction | construction | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:construction", "parents": []} |
| ent_m1 | object | safety | safety | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:safety", "parents": []} |
| ent_m2 | object | banquet | banquet | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:banquet", "parents": []} |
| ent_m3 | object | machinery | machinery | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:machinery", "parents": []} |
| ent_m4 | object | roadwork | roadwork | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:roadwork", "parents": []} |

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
| cf0 | entity_exists | construction |  |  |  | entity_exists:construction | True | low |
| cf1 | entity_exists | safety |  |  |  | entity_exists:safety | True | low |
| cf2 | entity_exists | banquet |  |  |  | entity_exists:banquet | True | low |
| cf3 | entity_exists | machinery |  |  |  | entity_exists:machinery | True | low |
| cf4 | entity_exists | roadwork |  |  |  | entity_exists:roadwork | True | low |
| cf5 | candidate_has_attribute | roadwork | orange |  | color_attribute, color, visual_attribute | candidate_has_attribute:roadwork:orange | False | low |
| cf6 | candidate_has_attribute | roadwork | black |  | color_attribute, color, visual_attribute | candidate_has_attribute:roadwork:black | False | low |

### Stage 9 Canonicalization Notes
_none_

## 77

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `44c2de876d814e7a8e13a555e11fba2c812dd33e1e1f319d9b8b2ced74d84c14`
**parse_path:** `sentence`

> A rock surface covered in patches of yellow and gray lichen.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | surface | surface | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | rock | rock | compound_modifier | chunk0 | 1 | medium |
| m2 | object | patches | patch | noun_chunk_root | chunk1 | 5 | high |
| m3 | object | lichen | lichen | noun_chunk_root | chunk2 | 10 | high |
| m4 | attribute | yellow | yellow | color_attribute | chunk2 | 7 | high |
| m5 | attribute | gray | gray | color_attribute | chunk2 | 9 | high |
| m6 | action | covered | cover | verb_predicate | doc | 3 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 compound -> surface |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> lichen |
| e2 | has_attribute | m3 | m5 | high | chunk2 conj -> lichen |
| e3 | agent | m6 | m0 | medium | inherited agent acl -> surface |
| e4 | relation | m0 | m2 | high | in |
| e5 | relation | m2 | m3 | medium | of |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | surface | surface | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": []} |
| ent_m2 | object | patch | patches | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:patch", "parents": []} |
| ent_m3 | object | lichen | lichen | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:lichen", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m6 | covered | cover | cover | raw_action | wordnet_synset:cover.v.01 + stage9_audit | occlusion_or_covering_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:cover", "parents": ["action_parent:occlusion_or_covering_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | cover | agent | agent | none | m0 | ent_m0 | medium | e3 | inherited agent acl -> surface |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e4 | False | False |  |  |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e5 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | surface |  |  |  | entity_exists:surface | True | low |
| cf1 | entity_exists | patch |  |  |  | entity_exists:patch | True | low |
| cf2 | entity_exists | lichen |  |  |  | entity_exists:lichen | True | low |
| cf3 | has_attribute | surface | rock |  | compound_modifier, visual_attribute | has_attribute:surface:rock | True | medium |
| cf4 | has_attribute | lichen | yellow |  | color_attribute, color, visual_attribute | has_attribute:lichen:yellow | True | high |
| cf5 | has_attribute | lichen | gray |  | color_attribute, color, visual_attribute | has_attribute:lichen:gray | True | high |
| cf6 | action_event | cover |  |  | occlusion_or_covering_action, visual_action | action_event:cover | True | high |
| cf7 | event_role | cover | agent | surface |  | event_role:cover:agent:surface | True | medium |
| cf8 | relation | surface | in | patch | spatial_containment, visual_relation | relation:surface:in:patch | True | high |
| cf9 | relation | patch | of | lichen | part_relation, visual_relation | relation:patch:of:lichen | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 78

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `44e11ff4392a6e1193b109115149794c1373cba45a9a2cea236203142e4c3414`
**parse_path:** `sentence`

> A long, rolled rug with a geometric pattern in purple and cream colors lies on a floor. The design features repeating octagons and circles, and text on the rug reads "3/16/08 rug shopping at ABC Carpet."

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "3/16/08 rug shopping at ABC Carpet." | 3/16/08_rug_shopping_at_abc_carpet. | quote_text | doc_quote | 33 | high |
| m1 | object | rug | rug | noun_chunk_root | chunk0 | 4 | high |
| m2 | attribute | long | long | size_attribute | chunk0 | 1 | high |
| m3 | attribute | rolled | roll | state_attribute | chunk0 | 3 | medium |
| m4 | object | pattern | pattern | noun_chunk_root | chunk1 | 8 | high |
| m5 | attribute | geometric | geometric | modifier_attribute | chunk1 | 7 | medium |
| m6 | object | colors | color | noun_chunk_root | chunk2 | 13 | high |
| m7 | attribute | purple | purple | color_attribute | chunk2 | 10 | high |
| m8 | object | floor | floor | noun_chunk_root | chunk3 | 17 | high |
| m9 | object | design | design | noun_chunk_root | chunk4 | 20 | high |
| m10 | object | octagons | octagon | noun_chunk_root | chunk5 | 23 | high |
| m11 | attribute | repeating | repeat | state_attribute | chunk5 | 22 | medium |
| m12 | object | circles | circle | noun_chunk_root | chunk6 | 25 | high |
| m13 | object | text | text | noun_chunk_root | chunk7 | 28 | high |
| m14 | object | rug | rug | noun_chunk_root | chunk8 | 31 | high |
| m15 | action | lies | lie | verb_predicate | doc | 14 | high |
| m16 | action | features | feature | verb_predicate | doc | 21 | high |
| m17 | action | reads | read | verb_predicate | doc | 32 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk0 amod -> rug |
| e1 | has_attribute | m1 | m3 | medium | chunk0 amod -> rug |
| e2 | has_attribute | m4 | m5 | medium | chunk1 amod -> pattern |
| e3 | has_attribute | m6 | m7 | high | chunk2 nmod -> colors |
| e4 | has_attribute | m10 | m11 | medium | chunk5 amod -> octagons |
| e5 | agent | m15 | m1 | medium | nsubj -> lies |
| e6 | agent | m16 | m9 | medium | nsubj -> features |
| e7 | patient | m16 | m10 | medium | dobj -> features |
| e8 | patient | m16 | m12 | medium | dobj -> features |
| e9 | agent | m17 | m13 | medium | nsubj -> reads |
| e10 | patient | m17 | m0 | medium | dobj -> reads |
| e11 | relation | m1 | m4 | high | with |
| e12 | relation | m4 | m6 | high | in |
| e13 | relation | m1 | m8 | high | on |
| e14 | relation | m13 | m14 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | rug | rug | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:rug", "parents": []} |
| ent_m4 | object | pattern | pattern | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:pattern", "parents": []} |
| ent_m6 | object | color | colors | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:color", "parents": []} |
| ent_m8 | object | floor | floor | object | raw_lemma | wordnet_synset:floor.n.01 + stage9_audit | architectural_part, surface, artifact | m8 | raw_mention |  |  |  | True | {"canonical": "entity:floor", "parents": ["entity_parent:architectural_part", "entity_parent:surface", "entity_parent:artifact"]} |
| ent_m9 | object | design | design | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:design", "parents": []} |
| ent_m10 | object | octagon | octagons | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:octagon", "parents": []} |
| ent_m12 | object | circle | circles | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:circle", "parents": []} |
| ent_m13 | object | text | text | document | raw_lemma | stage9_seed:parent_seed | text_content | m13 | raw_mention |  |  |  | True | {"canonical": "entity:text", "parents": ["entity_parent:text_content"]} |
| ent_m14 | object | rug | rug | object | raw_lemma | none |  | m14 | raw_mention |  |  |  | True | {"canonical": "entity:rug", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | lies | lie | lie | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:lie", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m16 | features | feature | feature | raw_action | visual_action_fallback | visual_action |  | agent:m9->ent_m9; patient:m10->ent_m10; patient:m12->ent_m12 | {"canonical": "action:feature", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m17 | reads | read | read | raw_action | stage9_seed:parent_seed | text_interaction_action, visual_action |  | agent:m13->ent_m13; patient:m0->None | {"canonical": "action:read", "parents": ["action_parent:text_interaction_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | lie | agent | agent | none | m1 | ent_m1 | medium | e5 | nsubj -> lies |  |  |
| ce1 | feature | agent | agent | none | m9 | ent_m9 | medium | e6 | nsubj -> features |  |  |
| ce1 | feature | patient | patient | none | m10 | ent_m10 | medium | e7 | dobj -> features |  |  |
| ce1 | feature | patient | patient | none | m12 | ent_m12 | medium | e8 | dobj -> features |  |  |
| ce2 | read | agent | agent | none | m13 | ent_m13 | medium | e9 | nsubj -> reads |  |  |
| ce2 | read | patient | patient | none | m0 |  | medium | e10 | dobj -> reads |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m4 | ent_m1 | ent_m4 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e11 | False | False |  |  |
| cr1 | m4 | m6 | ent_m4 | ent_m6 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e12 | False | False |  |  |
| cr2 | m1 | m8 | ent_m1 | ent_m8 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e13 | False | False |  |  |
| cr3 | m13 | m14 | ent_m13 | ent_m14 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e14 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | rug |  |  |  | entity_exists:rug | True | low |
| cf1 | entity_exists | pattern |  |  |  | entity_exists:pattern | True | low |
| cf2 | entity_exists | color |  |  |  | entity_exists:color | True | low |
| cf3 | entity_exists | floor |  |  | architectural_part, surface, artifact | entity_exists:floor | True | high |
| cf4 | entity_exists | design |  |  |  | entity_exists:design | True | low |
| cf5 | entity_exists | octagon |  |  |  | entity_exists:octagon | True | low |
| cf6 | entity_exists | circle |  |  |  | entity_exists:circle | True | low |
| cf7 | entity_exists | text |  |  | text_content | entity_exists:text | True | high |
| cf8 | entity_exists | rug |  |  |  | entity_exists:rug | True | low |
| cf9 | has_attribute | rug | long |  | size_attribute, clean_exact_overlap, length, visual_attribute | has_attribute:rug:long | True | high |
| cf10 | has_attribute | rug | roll |  | state_attribute, visual_attribute | has_attribute:rug:roll | True | medium |
| cf11 | has_attribute | pattern | geometric |  | pattern_attribute, textile_pattern, visual_attribute | has_attribute:pattern:geometric | True | medium |
| cf12 | has_attribute | color | purple |  | color_attribute, color, visual_attribute | has_attribute:color:purple | True | high |
| cf13 | has_attribute | octagon | repeat |  | state_attribute, visual_attribute | has_attribute:octagon:repeat | True | medium |
| cf14 | action_event | lie |  |  | body_pose_action, visual_action | action_event:lie | True | high |
| cf15 | event_role | lie | agent | rug |  | event_role:lie:agent:rug | True | medium |
| cf16 | action_event | feature |  |  | visual_action | action_event:feature | True | low |
| cf17 | event_role | feature | agent | design |  | event_role:feature:agent:design | True | medium |
| cf18 | event_role | feature | patient | octagon |  | event_role:feature:patient:octagon | True | medium |
| cf19 | event_role | feature | patient | circle |  | event_role:feature:patient:circle | True | medium |
| cf20 | action_event | read |  |  | text_interaction_action, visual_action | action_event:read | True | medium |
| cf21 | event_role | read | agent | text |  | event_role:read:agent:text | True | medium |
| cf22 | event_role | read | patient |  |  | event_role:read:patient | False | medium |
| cf23 | relation | rug | with | pattern | association_relation, visual_relation | relation:rug:with:pattern | True | high |
| cf24 | relation | pattern | in | color | spatial_containment, visual_relation | relation:pattern:in:color | True | high |
| cf25 | relation | rug | on | floor | spatial_support, visual_relation | relation:rug:on:floor | True | high |
| cf26 | relation | text | on | rug | spatial_support, visual_relation | relation:text:on:rug | True | high |

### Stage 9 Canonicalization Notes
_none_

## 79

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `47124c2ed61bbf30199cd59e9537e4d66e3fac1226d87e7e1bdeb0b8b89c2814`
**parse_path:** `sentence`

> A man in a dark uniform and cap holds a wooden rifle, pointing it forward.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | uniform | uniform | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | dark | dark | visual_attribute | chunk1 | 4 | medium |
| m3 | object | cap | cap | noun_chunk_root | chunk2 | 7 | high |
| m4 | object | rifle | rifle | noun_chunk_root | chunk3 | 11 | high |
| m5 | attribute | wooden | wooden | material_attribute | chunk3 | 10 | high |
| m6 | action | holds | hold | verb_predicate | doc | 8 | high |
| m7 | action | pointing | point | verb_predicate | doc | 13 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 amod -> uniform |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> rifle |
| e2 | agent | m6 | m0 | medium | nsubj -> holds |
| e3 | patient | m6 | m4 | medium | dobj -> holds |
| e4 | agent | m7 | m0 | medium | inherited agent advcl -> holds |
| e5 | relation | m0 | m1 | high | in |
| e6 | relation | m0 | m3 | high | in |

### Skipped Raw Concept Edges
| type | source | target | confidence | reason | evidence |
| --- | --- | --- | --- | --- | --- |
| patient | m7 | m0 | medium | pronoun_resolved_to_action_agent | dobj -> pointing; resolved it -> man |

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | uniform | uniform | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | cap | cap | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m3 | raw_mention |  |  |  | True | {"canonical": "entity:cap", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m4 | object | rifle | rifle | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:rifle", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m6 | holds | hold | hold | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action |  | agent:m0->ent_m0; patient:m4->ent_m4 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce1 | m7 | pointing | point | point | raw_action | stage9_seed:parent_seed | gesture_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:point", "parents": ["action_parent:gesture_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | hold | agent | agent | none | m0 | ent_m0 | medium | e2 | nsubj -> holds |  |  |
| ce0 | hold | patient | patient | none | m4 | ent_m4 | medium | e3 | dobj -> holds |  |  |
| ce1 | point | agent | agent | none | m0 | ent_m0 | medium | e4 | inherited agent advcl -> holds |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e5 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e6 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf1 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf2 | entity_exists | cap |  |  | clothing, wearable | entity_exists:cap | True | high |
| cf3 | entity_exists | rifle |  |  |  | entity_exists:rifle | True | low |
| cf4 | has_attribute | uniform | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:uniform:dark | True | medium |
| cf5 | has_attribute | rifle | wood |  | material_attribute, material, visual_attribute | has_attribute:rifle:wood | True | high |
| cf6 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf7 | event_role | hold | agent | man |  | event_role:hold:agent:man | True | medium |
| cf8 | event_role | hold | patient | rifle |  | event_role:hold:patient:rifle | True | medium |
| cf9 | action_event | point |  |  | gesture_action, visual_action | action_event:point | True | high |
| cf10 | event_role | point | agent | man |  | event_role:point:agent:man | True | medium |
| cf11 | relation | man | in | uniform | spatial_containment, visual_relation | relation:man:in:uniform | True | high |
| cf12 | relation | man | in | cap | spatial_containment, visual_relation | relation:man:in:cap | True | high |

### Stage 9 Canonicalization Notes
_none_

## 80

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `47f45ea5be5abc8d58086072d52f797dafdb8bf5e7d3667e080d087caa18a414`
**parse_path:** `sentence`

> A bride in a white dress and a groom in a black suit walk through a banquet hall, waving to guests. Tables with food and drinks are set around them, and people sit at tables in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | bride | bride | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | dress | dress | noun_chunk_root | chunk1 | 5 | high |
| m2 | attribute | white | white | color_attribute | chunk1 | 4 | high |
| m3 | object | groom | groom | noun_chunk_root | chunk2 | 8 | high |
| m4 | object | suit | suit | noun_chunk_root | chunk3 | 12 | high |
| m5 | attribute | black | black | color_attribute | chunk3 | 11 | high |
| m6 | object | hall | hall | noun_chunk_root | chunk4 | 17 | high |
| m7 | attribute | banquet | banquet | compound_modifier | chunk4 | 16 | medium |
| m8 | object | guests | guest | noun_chunk_root | chunk5 | 21 | high |
| m9 | object | Tables | table | noun_chunk_root | chunk6 | 23 | high |
| m10 | object | food | food | noun_chunk_root | chunk7 | 25 | high |
| m11 | object | drinks | drink | noun_chunk_root | chunk8 | 27 | high |
| m12 | object | people | people | noun_chunk_root | chunk10 | 34 | high |
| m13 | object | tables | table | noun_chunk_root | chunk11 | 37 | high |
| m14 | context | background | background | scene_context | chunk12 | 40 | high |
| m15 | action | walk | walk | verb_predicate | doc | 13 | high |
| m16 | action | waving | wave | verb_predicate | doc | 19 | high |
| m17 | action | set | set | verb_predicate | doc | 29 | high |
| m18 | action | sit | sit | verb_predicate | doc | 35 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> dress |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> suit |
| e2 | has_attribute | m6 | m7 | medium | chunk4 compound -> hall |
| e3 | has_context | scene | m14 | high | scene_context token background |
| e4 | agent | m15 | m0 | medium | nsubj -> walk |
| e5 | agent | m15 | m3 | medium | nsubj -> walk |
| e6 | agent | m16 | m0 | medium | inherited agent advcl -> walk |
| e7 | agent | m16 | m3 | medium | inherited agent advcl -> walk |
| e8 | agent | m17 | m9 | medium | nsubjpass -> set |
| e9 | agent | m18 | m12 | medium | nsubj -> sit |
| e10 | relation | m0 | m1 | high | in |
| e11 | relation | m3 | m4 | high | in |
| e12 | relation | m0 | m6 | medium | through |
| e13 | relation | m0 | m8 | medium | to |
| e14 | relation | m9 | m10 | high | with |
| e15 | relation | m9 | m11 | high | with |
| e16 | relation | m9 | m8 | medium | around; repaired_self_edge_target from them->Tables |
| e17 | relation | m12 | m13 | medium | at |
| e18 | relation | m12 | m14 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | bride | bride | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:bride", "parents": []} |
| ent_m1 | object | dress | dress | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m1 | raw_mention |  |  |  | True | {"canonical": "entity:dress", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m3 | object | groom | groom | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:groom", "parents": []} |
| ent_m4 | object | suit | suit | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:suit", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m6 | object | hall | hall | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:hall", "parents": []} |
| ent_m8 | object | guest | guests | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:guest", "parents": []} |
| ent_m9 | object | table | Tables | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m9 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m10 | object | food | food | object | raw_lemma | wordnet_synset:food.n.01 + stage9_audit | food | m10 | raw_mention |  |  |  | True | {"canonical": "entity:food", "parents": ["entity_parent:food"]} |
| ent_m11 | object | drink | drinks | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:drink", "parents": []} |
| ent_m12 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m12 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m13 | object | table | tables | object | raw_lemma | stage9_seed:parent_seed | furniture, artifact | m13 | raw_mention |  |  |  | True | {"canonical": "entity:table", "parents": ["entity_parent:furniture", "entity_parent:artifact"]} |
| ent_m14 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m14 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | walk | walk | walk | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0; agent:m3->ent_m3 | {"canonical": "action:walk", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m16 | waving | wave | wave | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; agent:m3->ent_m3 | {"canonical": "action:wave", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m17 | set | set | set | raw_action | visual_action_fallback | visual_action |  | patient<-theme[passive_to_active]:m9->ent_m9 | {"canonical": "action:set", "parents": ["action_parent:visual_action"]} |  |
| ce3 | m18 | sit | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m12->ent_m12 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | walk | agent | agent | none | m0 | ent_m0 | medium | e4 | nsubj -> walk |  |  |
| ce0 | walk | agent | agent | none | m3 | ent_m3 | medium | e5 | nsubj -> walk |  |  |
| ce1 | wave | agent | agent | none | m0 | ent_m0 | medium | e6 | inherited agent advcl -> walk |  |  |
| ce1 | wave | agent | agent | none | m3 | ent_m3 | medium | e7 | inherited agent advcl -> walk |  |  |
| ce2 | set | patient | theme | passive_to_active | m9 | ent_m9 | medium | e8 | nsubjpass -> set |  |  |
| ce3 | sit | agent | agent | none | m12 | ent_m12 | medium | e9 | nsubj -> sit |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e10 | False | False |  |  |
| cr1 | m3 | m4 | ent_m3 | ent_m4 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e11 | False | False |  |  |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | through | through | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | medium | e12 | False | False |  |  |
| cr3 | m0 | m8 | ent_m0 | ent_m8 | to | to | raw_relation | raw_relation | visual_relation | medium | e13 | False | False |  |  |
| cr4 | m9 | m10 | ent_m9 | ent_m10 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr5 | m9 | m11 | ent_m9 | ent_m11 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e15 | False | False |  |  |
| cr6 | m9 | m8 | ent_m9 | ent_m8 | around; repaired_self_edge_target from them->Tables | around | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | medium | e16 | False | False |  |  |
| cr7 | m12 | m13 | ent_m12 | ent_m13 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e17 | False | False |  |  |
| cr8 | m12 | m14 | ent_m12 | ent_m14 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e18 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | bride |  |  |  | entity_exists:bride | True | low |
| cf1 | entity_exists | dress |  |  | clothing, wearable | entity_exists:dress | True | high |
| cf2 | entity_exists | groom |  |  |  | entity_exists:groom | True | low |
| cf3 | entity_exists | suit |  |  | clothing, wearable | entity_exists:suit | True | high |
| cf4 | entity_exists | hall |  |  |  | entity_exists:hall | True | low |
| cf5 | entity_exists | guest |  |  |  | entity_exists:guest | True | low |
| cf6 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf7 | entity_exists | food |  |  | food | entity_exists:food | True | high |
| cf8 | entity_exists | drink |  |  |  | entity_exists:drink | True | low |
| cf9 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf10 | entity_exists | table |  |  | furniture, artifact | entity_exists:table | True | high |
| cf11 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf12 | has_attribute | dress | white |  | color_attribute, color, visual_attribute | has_attribute:dress:white | True | high |
| cf13 | has_attribute | suit | black |  | color_attribute, color, visual_attribute | has_attribute:suit:black | True | high |
| cf14 | has_attribute | hall | banquet |  | compound_modifier, visual_attribute | has_attribute:hall:banquet | True | medium |
| cf15 | action_event | walk |  |  | locomotion_action, visual_action | action_event:walk | True | high |
| cf16 | event_role | walk | agent | bride |  | event_role:walk:agent:bride | True | medium |
| cf17 | event_role | walk | agent | groom |  | event_role:walk:agent:groom | True | medium |
| cf18 | action_event | wave |  |  | visual_action | action_event:wave | True | low |
| cf19 | event_role | wave | agent | bride |  | event_role:wave:agent:bride | True | medium |
| cf20 | event_role | wave | agent | groom |  | event_role:wave:agent:groom | True | medium |
| cf21 | action_event | set |  |  | visual_action | action_event:set | True | low |
| cf22 | event_role | set | patient | table |  | event_role:set:patient:table | True | medium |
| cf23 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf24 | event_role | sit | agent | people |  | event_role:sit:agent:people | True | medium |
| cf25 | relation | bride | in | dress | spatial_containment, visual_relation | relation:bride:in:dress | True | high |
| cf26 | relation | groom | in | suit | spatial_containment, visual_relation | relation:groom:in:suit | True | high |
| cf27 | relation | bride | through | hall | spatial_path, visual_relation | relation:bride:through:hall | True | medium |
| cf28 | relation | bride | to | guest | visual_relation | relation:bride:to:guest | True | medium |
| cf29 | relation | table | with | food | association_relation, visual_relation | relation:table:with:food | True | high |
| cf30 | relation | table | with | drink | association_relation, visual_relation | relation:table:with:drink | True | high |
| cf31 | relation | table | around | guest | spatial_proximity, visual_relation | relation:table:around:guest | True | medium |
| cf32 | relation | people | at | table | spatial_location, visual_relation | relation:people:at:table | True | medium |
| cf33 | relation | people | in | background | spatial_containment, visual_relation | relation:people:in:background | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m17 | e8 | m9 |  |  | {"action_mention_id": "m17", "kind": "passive_subject_to_patient", "raw_edge_id": "e8", "raw_role": "theme", "role": "patient", "target": "m9", "voice_normalization": "passive_to_active"} |
| relation_lexical_canonicalized |  | e16 |  |  |  | {"canonical": "around", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e16", "raw_relation": "around; repaired_self_edge_target from them->Tables", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 81

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `48143566a9414c9db9a9a2fee5fa6e7780ef4b76099ce1cf605377f059c70414`
**parse_path:** `sentence`

> A woman smiles while holding a large fox costume with blue fur on its head. They are outdoors under trees.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | costume | costume | noun_chunk_root | chunk1 | 8 | high |
| m2 | attribute | large | large | size_attribute | chunk1 | 6 | high |
| m3 | attribute | fox | fox | compound_modifier | chunk1 | 7 | medium |
| m4 | object | fur | fur | noun_chunk_root | chunk2 | 11 | high |
| m5 | attribute | blue | blue | color_attribute | chunk2 | 10 | high |
| m6 | object | head | head | noun_chunk_root | chunk3 | 14 | high |
| m7 | object | trees | tree | noun_chunk_root | chunk5 | 20 | high |
| m8 | context | outdoors | outdoors | scene_context | doc | 18 | high |
| m9 | action | smiles | smile | verb_predicate | doc | 2 | high |
| m10 | action | holding | hold | verb_predicate | doc | 4 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> costume |
| e1 | has_attribute | m1 | m3 | medium | chunk1 compound -> costume |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> fur |
| e3 | has_context | scene | m8 | high | scene_context token outdoors |
| e4 | agent | m9 | m0 | medium | nsubj -> smiles |
| e5 | agent | m10 | m0 | medium | inherited agent advcl -> smiles |
| e6 | patient | m10 | m1 | medium | dobj -> holding |
| e7 | relation | m1 | m4 | high | with |
| e8 | relation | m4 | m6 | high | on |
| e9 | relation | m0 | m7 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | costume | costume | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:costume", "parents": []} |
| ent_m4 | object | fur | fur | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:fur", "parents": []} |
| ent_m6 | object | head | head | object | raw_lemma | stage9_seed:parent_seed | body_part | m6 | raw_mention |  |  |  | True | {"canonical": "entity:head", "parents": ["entity_parent:body_part"]} |
| ent_m7 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m7 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m8 | context | outdoors | outdoors | object | raw_lemma | stage9_seed:parent_seed | scene_context | m8 | raw_mention |  |  |  | True | {"canonical": "entity:outdoors", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | smiles | smile | smile | raw_action | stage9_seed:parent_seed | expression_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:smile", "parents": ["action_parent:expression_action", "action_parent:visual_action"]} |  |
| ce1 | m10 | holding | hold | hold | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action |  | agent:m0->ent_m0; patient:m1->ent_m1 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | smile | agent | agent | none | m0 | ent_m0 | medium | e4 | nsubj -> smiles |  |  |
| ce1 | hold | agent | agent | none | m0 | ent_m0 | medium | e5 | inherited agent advcl -> smiles |  |  |
| ce1 | hold | patient | patient | none | m1 | ent_m1 | medium | e6 | dobj -> holding |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m4 | ent_m1 | ent_m4 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e7 | False | False |  |  |
| cr1 | m4 | m6 | ent_m4 | ent_m6 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e8 | False | False |  |  |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e9 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | costume |  |  |  | entity_exists:costume | True | low |
| cf2 | entity_exists | fur |  |  |  | entity_exists:fur | True | low |
| cf3 | entity_exists | head |  |  | body_part | entity_exists:head | True | high |
| cf4 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf5 | entity_exists | outdoors |  |  | scene_context | entity_exists:outdoors | True | high |
| cf6 | has_attribute | costume | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:costume:large | True | high |
| cf7 | has_attribute | costume | fox |  | compound_modifier, visual_attribute | has_attribute:costume:fox | True | medium |
| cf8 | has_attribute | fur | blue |  | color_attribute, color, visual_attribute | has_attribute:fur:blue | True | high |
| cf9 | action_event | smile |  |  | expression_action, visual_action | action_event:smile | True | high |
| cf10 | event_role | smile | agent | woman |  | event_role:smile:agent:woman | True | medium |
| cf11 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf12 | event_role | hold | agent | woman |  | event_role:hold:agent:woman | True | medium |
| cf13 | event_role | hold | patient | costume |  | event_role:hold:patient:costume | True | medium |
| cf14 | relation | costume | with | fur | association_relation, visual_relation | relation:costume:with:fur | True | high |
| cf15 | relation | fur | on | head | spatial_support, visual_relation | relation:fur:on:head | True | high |
| cf16 | relation | woman | under | tree | spatial_vertical, visual_relation | relation:woman:under:tree | True | high |

### Stage 9 Canonicalization Notes
_none_

## 82

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `49d3a7cc30bd10310985cc24c7423cc240986723dbca4927dea5c09c70e8d814`
**parse_path:** `sentence`

> A small brown clay figurine stands on a light-colored surface. It has a detailed headdress and holds a circular object, possibly a shield or disk, in its hands. The background is a plain, textured wall, suggesting it is displayed in a museum or gallery setting.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | figurine | figurine | noun_chunk_root | chunk0 | 4 | high |
| m1 | attribute | small | small | size_attribute | chunk0 | 1 | high |
| m2 | attribute | brown | brown | color_attribute | chunk0 | 2 | high |
| m3 | attribute | clay | clay | compound_modifier | chunk0 | 3 | medium |
| m4 | context | surface | surface | spatial_region | chunk1 | 9 | medium |
| m5 | object | headdress | headdress | noun_chunk_root | chunk3 | 15 | high |
| m6 | attribute | detailed | detailed | modifier_attribute | chunk3 | 14 | medium |
| m7 | object | object | object | noun_chunk_root | chunk4 | 20 | high |
| m8 | attribute | circular | circular | modifier_attribute | chunk4 | 19 | medium |
| m9 | object | shield | shield | noun_chunk_root | chunk5 | 24 | high |
| m10 | attribute | possibly | possibly | modifier_attribute | chunk5 | 22 | medium |
| m11 | object | disk | disk | noun_chunk_root | chunk6 | 26 | high |
| m12 | object | hands | hand | noun_chunk_root | chunk7 | 30 | high |
| m13 | context | background | background | scene_context | chunk8 | 33 | high |
| m14 | object | wall | wall | noun_chunk_root | chunk9 | 39 | high |
| m15 | attribute | plain | plain | modifier_attribute | chunk9 | 36 | medium |
| m16 | attribute | textured | textured | modifier_attribute | chunk9 | 38 | medium |
| m17 | context | setting | setting | scene_context | chunk11 | 50 | high |
| m18 | action | stands | stand | verb_predicate | doc | 5 | high |
| m19 | action | has | have | verb_predicate | doc | 12 | high |
| m20 | action | holds | hold | verb_predicate | doc | 17 | high |
| m21 | action | suggesting | suggest | verb_predicate | doc | 41 | high |
| m22 | action | displayed | display | verb_predicate | doc | 44 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> figurine |
| e1 | has_attribute | m0 | m2 | high | chunk0 amod -> figurine |
| e2 | has_attribute | m0 | m3 | medium | chunk0 compound -> figurine |
| e3 | has_attribute | m5 | m6 | medium | chunk3 amod -> headdress |
| e4 | has_attribute | m7 | m8 | medium | chunk4 amod -> object |
| e5 | has_attribute | m9 | m10 | medium | chunk5 advmod -> shield |
| e6 | has_context | scene | m13 | high | scene_context token background |
| e7 | has_attribute | m14 | m15 | medium | chunk9 amod -> wall |
| e8 | has_attribute | m14 | m16 | medium | chunk9 amod -> wall |
| e9 | has_context | scene | m17 | high | scene_context token setting |
| e10 | agent | m18 | m0 | medium | nsubj -> stands |
| e11 | agent | m19 | m0 | medium | nsubj -> has; resolved It -> figurine |
| e12 | patient | m19 | m5 | medium | dobj -> has |
| e13 | agent | m20 | m0 | medium | inherited agent conj -> has |
| e14 | patient | m20 | m7 | medium | dobj -> holds |
| e15 | agent | m21 | m13 | medium | inherited agent advcl -> is |
| e16 | agent | m22 | m12 | medium | nsubjpass -> displayed; resolved it -> hands |
| e17 | relation | m0 | m4 | high | on |
| e18 | relation | m0 | m12 | high | in |
| e19 | relation | m12 | m17 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | figurine | figurine | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:figurine", "parents": []} |
| ent_m4 | context | surface | surface | object | raw_lemma | semantic_type_fallback | scene_context | m4 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": ["entity_parent:scene_context"]} |
| ent_m5 | object | headdress | headdress | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:headdress", "parents": []} |
| ent_m7 | object | object | object | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:object", "parents": []} |
| ent_m9 | object | shield | shield | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:shield", "parents": []} |
| ent_m11 | object | disk | disk | object | raw_lemma | none |  | m11 | raw_mention |  |  |  | True | {"canonical": "entity:disk", "parents": []} |
| ent_m12 | object | hand | hands | object | raw_lemma | stage9_seed:parent_seed | body_part | m12 | raw_mention |  |  |  | True | {"canonical": "entity:hand", "parents": ["entity_parent:body_part"]} |
| ent_m13 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m13 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m14 | object | wall | wall | object | raw_lemma | wordnet_synset:wall.n.01 + stage9_audit | architectural_part, structure, artifact | m14 | raw_mention |  |  |  | True | {"canonical": "entity:wall", "parents": ["entity_parent:architectural_part", "entity_parent:structure", "entity_parent:artifact"]} |
| ent_m17 | context | setting | setting | object | raw_lemma | stage9_seed:parent_seed | scene_context | m17 | raw_mention |  |  |  | True | {"canonical": "entity:setting", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m19 | has | have | have | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0; patient:m5->ent_m5 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m20 | holds | hold | hold | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action |  | agent:m0->ent_m0; patient:m7->ent_m7 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce3 | m21 | suggesting | suggest | suggest | raw_action | visual_action_fallback | visual_action |  | agent:m13->ent_m13 | {"canonical": "action:suggest", "parents": ["action_parent:visual_action"]} |  |
| ce4 | m22 | displayed | display | display | raw_action | wordnet_synset:display.v.01 + stage9_audit | visual_presentation_action, visual_action |  | patient<-theme[passive_to_active]:m12->ent_m12 | {"canonical": "action:display", "parents": ["action_parent:visual_presentation_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e10 | nsubj -> stands |  |  |
| ce1 | have | agent | agent | none | m0 | ent_m0 | medium | e11 | nsubj -> has; resolved It -> figurine |  |  |
| ce1 | have | patient | patient | none | m5 | ent_m5 | medium | e12 | dobj -> has |  |  |
| ce2 | hold | agent | agent | none | m0 | ent_m0 | medium | e13 | inherited agent conj -> has |  |  |
| ce2 | hold | patient | patient | none | m7 | ent_m7 | medium | e14 | dobj -> holds |  |  |
| ce3 | suggest | agent | agent | none | m13 | ent_m13 | medium | e15 | inherited agent advcl -> is |  |  |
| ce4 | display | patient | theme | passive_to_active | m12 | ent_m12 | medium | e16 | nsubjpass -> displayed; resolved it -> hands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e17 | False | False |  |  |
| cr1 | m0 | m12 | ent_m0 | ent_m12 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e18 | False | False |  |  |
| cr2 | m12 | m17 | ent_m12 | ent_m17 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e19 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | figurine |  |  |  | entity_exists:figurine | True | low |
| cf1 | entity_exists | surface |  |  | scene_context | entity_exists:surface | True | medium |
| cf2 | entity_exists | headdress |  |  |  | entity_exists:headdress | True | low |
| cf3 | entity_exists | object |  |  |  | entity_exists:object | True | low |
| cf4 | entity_exists | shield |  |  |  | entity_exists:shield | True | low |
| cf5 | entity_exists | disk |  |  |  | entity_exists:disk | True | low |
| cf6 | entity_exists | hand |  |  | body_part | entity_exists:hand | True | high |
| cf7 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf8 | entity_exists | wall |  |  | architectural_part, structure, artifact | entity_exists:wall | True | high |
| cf9 | entity_exists | setting |  |  | scene_context | entity_exists:setting | True | high |
| cf10 | has_attribute | figurine | small |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:figurine:small | True | high |
| cf11 | has_attribute | figurine | brown |  | color_attribute, color, visual_attribute | has_attribute:figurine:brown | True | high |
| cf12 | has_attribute | figurine | clay |  | material_attribute, material, visual_attribute | has_attribute:figurine:clay | True | medium |
| cf13 | has_attribute | headdress | detailed |  | modifier_attribute, visual_attribute | has_attribute:headdress:detailed | True | medium |
| cf14 | has_attribute | object | circular |  | shape_attribute, shape, visual_attribute | has_attribute:object:circular | True | medium |
| cf15 | has_attribute | shield | possibly |  | modifier_attribute, visual_attribute | has_attribute:shield:possibly | True | medium |
| cf16 | has_attribute | wall | plain |  | pattern_attribute, clean_exact_overlap, other, pattern, pattern_marking, visual_attribute | has_attribute:wall:plain | True | medium |
| cf17 | has_attribute | wall | textured |  | texture_attribute, texture, visual_attribute | has_attribute:wall:textured | True | medium |
| cf18 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf19 | event_role | stand | agent | figurine |  | event_role:stand:agent:figurine | True | medium |
| cf20 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf21 | event_role | have | agent | figurine |  | event_role:have:agent:figurine | True | medium |
| cf22 | event_role | have | patient | headdress |  | event_role:have:patient:headdress | True | medium |
| cf23 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf24 | event_role | hold | agent | figurine |  | event_role:hold:agent:figurine | True | medium |
| cf25 | event_role | hold | patient | object |  | event_role:hold:patient:object | True | medium |
| cf26 | action_event | suggest |  |  | visual_action | action_event:suggest | True | low |
| cf27 | event_role | suggest | agent | background |  | event_role:suggest:agent:background | True | medium |
| cf28 | action_event | display |  |  | visual_presentation_action, visual_action | action_event:display | True | high |
| cf29 | event_role | display | patient | hand |  | event_role:display:patient:hand | True | medium |
| cf30 | relation | figurine | on | surface | spatial_support, visual_relation | relation:figurine:on:surface | True | high |
| cf31 | relation | figurine | in | hand | spatial_containment, visual_relation | relation:figurine:in:hand | True | high |
| cf32 | relation | hand | in | setting | spatial_containment, visual_relation | relation:hand:in:setting | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m22 | e16 | m12 |  |  | {"action_mention_id": "m22", "kind": "passive_subject_to_patient", "raw_edge_id": "e16", "raw_role": "theme", "role": "patient", "target": "m12", "voice_normalization": "passive_to_active"} |

## 83

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `4bd2f22f7bed38afb788ec46117f223feb2c82fa438dc992a877f064d1182814`
**parse_path:** `sentence`

> A sunset glows over a calm lake, casting golden light across the water and sky.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | sunset | sunset | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | lake | lake | noun_chunk_root | chunk1 | 6 | high |
| m2 | attribute | calm | calm | modifier_attribute | chunk1 | 5 | medium |
| m3 | object | light | light | noun_chunk_root | chunk2 | 10 | high |
| m4 | attribute | golden | golden | color_attribute | chunk2 | 9 | high |
| m5 | object | water | water | noun_chunk_root | chunk3 | 13 | high |
| m6 | object | sky | sky | noun_chunk_root | chunk4 | 15 | high |
| m7 | context | sunset | sunset | context_word | doc | 1 | medium |
| m8 | action | glows | glow | verb_predicate | doc | 2 | high |
| m9 | action | casting | cast | verb_predicate | doc | 8 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 amod -> lake |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> light |
| e2 | has_context | scene | m7 | medium | context_word token sunset |
| e3 | agent | m8 | m7 | medium | nsubj -> glows |
| e4 | agent | m9 | m7 | medium | inherited agent advcl -> glows |
| e5 | patient | m9 | m3 | medium | dobj -> casting |
| e6 | relation | m7 | m1 | high | over |
| e7 | relation | m7 | m5 | high | across |
| e8 | relation | m7 | m6 | high | across |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sunset | sunset | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:sunset", "parents": []} |
| ent_m1 | object | lake | lake | object | raw_lemma | wordnet_synset:lake.n.01 + stage9_audit | body_of_water, place | m1 | raw_mention |  |  |  | True | {"canonical": "entity:lake", "parents": ["entity_parent:body_of_water", "entity_parent:place"]} |
| ent_m3 | object | light | light | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:light", "parents": []} |
| ent_m5 | object | water | water | object | raw_lemma | wordnet_synset:water.n.01 + stage9_audit | natural_element | m5 | raw_mention |  |  |  | True | {"canonical": "entity:water", "parents": ["entity_parent:natural_element"]} |
| ent_m6 | object | sky | sky | object | raw_lemma | wordnet_synset:sky.n.01 + stage9_audit | natural_scene | m6 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": ["entity_parent:natural_scene"]} |
| ent_m7 | context | sunset | sunset | object | raw_lemma | semantic_type_fallback | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:sunset", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | glows | glow | glow | raw_action | visual_action_fallback | visual_action |  | agent:m7->ent_m7 | {"canonical": "action:glow", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m9 | casting | cast | cast | raw_action | visual_action_fallback | visual_action |  | agent:m7->ent_m7; patient:m3->ent_m3 | {"canonical": "action:cast", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | glow | agent | agent | none | m7 | ent_m7 | medium | e3 | nsubj -> glows |  |  |
| ce1 | cast | agent | agent | none | m7 | ent_m7 | medium | e4 | inherited agent advcl -> glows |  |  |
| ce1 | cast | patient | patient | none | m3 | ent_m3 | medium | e5 | dobj -> casting |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m7 | m1 | ent_m7 | ent_m1 | over | above | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e6 | False | False |  |  |
| cr1 | m7 | m5 | ent_m7 | ent_m5 | across | across | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | high | e7 | False | False |  |  |
| cr2 | m7 | m6 | ent_m7 | ent_m6 | across | across | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | sunset |  |  |  | entity_exists:sunset | True | low |
| cf1 | entity_exists | lake |  |  | body_of_water, place | entity_exists:lake | True | high |
| cf2 | entity_exists | light |  |  |  | entity_exists:light | True | low |
| cf3 | entity_exists | water |  |  | natural_element | entity_exists:water | True | high |
| cf4 | entity_exists | sky |  |  | natural_scene | entity_exists:sky | True | high |
| cf5 | entity_exists | sunset |  |  | scene_context | entity_exists:sunset | True | medium |
| cf6 | has_attribute | lake | calm |  | modifier_attribute, visual_attribute | has_attribute:lake:calm | True | medium |
| cf7 | has_attribute | light | golden |  | color_attribute, color, visual_attribute | has_attribute:light:golden | True | high |
| cf8 | action_event | glow |  |  | visual_action | action_event:glow | True | low |
| cf9 | event_role | glow | agent | sunset |  | event_role:glow:agent:sunset | True | medium |
| cf10 | action_event | cast |  |  | visual_action | action_event:cast | True | low |
| cf11 | event_role | cast | agent | sunset |  | event_role:cast:agent:sunset | True | medium |
| cf12 | event_role | cast | patient | light |  | event_role:cast:patient:light | True | medium |
| cf13 | relation | sunset | above | lake | spatial_vertical, visual_relation | relation:sunset:above:lake | True | high |
| cf14 | relation | sunset | across | water | spatial_path, visual_relation | relation:sunset:across:water | True | high |
| cf15 | relation | sunset | across | sky | spatial_path, visual_relation | relation:sunset:across:sky | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e6 |  |  |  | {"canonical": "above", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e6", "raw_relation": "over", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 84

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `4d0013cce3e5d2f542f4783322d9a481f0788ffec8f4cfe4a78b884345d1b814`
**parse_path:** `sentence`

> A woman in a blue belly dance outfit performs on a stage. People watch from the sides in a gymnasium.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | outfit | outfit | noun_chunk_root | chunk1 | 7 | high |
| m2 | attribute | blue | blue | color_attribute | chunk1 | 4 | high |
| m3 | attribute | belly | belly | compound_modifier | chunk1 | 5 | medium |
| m4 | attribute | dance | dance | compound_modifier | chunk1 | 6 | medium |
| m5 | object | stage | stage | noun_chunk_root | chunk2 | 11 | high |
| m6 | object | People | people | noun_chunk_root | chunk3 | 13 | high |
| m7 | context | sides | side | spatial_region | chunk4 | 17 | medium |
| m8 | object | gymnasium | gymnasium | noun_chunk_root | chunk5 | 20 | high |
| m9 | action | performs | perform | verb_predicate | doc | 8 | high |
| m10 | action | watch | watch | verb_predicate | doc | 14 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> outfit |
| e1 | has_attribute | m1 | m3 | medium | chunk1 compound -> outfit |
| e2 | has_attribute | m1 | m4 | medium | chunk1 compound -> outfit |
| e3 | agent | m9 | m0 | medium | nsubj -> performs |
| e4 | agent | m10 | m6 | medium | nsubj -> watch |
| e5 | relation | m0 | m1 | high | in |
| e6 | relation | m0 | m5 | high | on |
| e7 | relation | m6 | m7 | medium | from |
| e8 | relation | m6 | m8 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | outfit | outfit | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:outfit", "parents": []} |
| ent_m5 | object | stage | stage | object | raw_lemma | wordnet_synset:stage.n.03 + stage9_audit | platform, place, artifact | m5 | raw_mention |  |  |  | True | {"canonical": "entity:stage", "parents": ["entity_parent:platform", "entity_parent:place", "entity_parent:artifact"]} |
| ent_m6 | object | people | People | person | raw_lemma | stage9_seed:parent_seed | person, human | m6 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m7 | context | side | sides | object | raw_lemma | semantic_type_fallback | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:side", "parents": ["entity_parent:scene_context"]} |
| ent_m8 | object | gymnasium | gymnasium | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:gymnasium", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | performs | perform | perform | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:perform", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m10 | watch | watch | watch | raw_action | stage9_seed:parent_seed | gaze_action, visual_action |  | agent:m6->ent_m6 | {"canonical": "action:watch", "parents": ["action_parent:gaze_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | perform | agent | agent | none | m0 | ent_m0 | medium | e3 | nsubj -> performs |  |  |
| ce1 | watch | agent | agent | none | m6 | ent_m6 | medium | e4 | nsubj -> watch |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e5 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e6 | False | False |  |  |
| cr2 | m6 | m7 | ent_m6 | ent_m7 | from | from | raw_relation | raw_relation | visual_relation | medium | e7 | False | False |  |  |
| cr3 | m6 | m8 | ent_m6 | ent_m8 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e8 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | outfit |  |  |  | entity_exists:outfit | True | low |
| cf2 | entity_exists | stage |  |  | platform, place, artifact | entity_exists:stage | True | medium |
| cf3 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf4 | entity_exists | side |  |  | scene_context | entity_exists:side | True | medium |
| cf5 | entity_exists | gymnasium |  |  |  | entity_exists:gymnasium | True | low |
| cf6 | has_attribute | outfit | blue |  | color_attribute, color, visual_attribute | has_attribute:outfit:blue | True | high |
| cf7 | has_attribute | outfit | belly |  | compound_modifier, visual_attribute | has_attribute:outfit:belly | True | medium |
| cf8 | has_attribute | outfit | dance |  | compound_modifier, visual_attribute | has_attribute:outfit:dance | True | medium |
| cf9 | action_event | perform |  |  | visual_action | action_event:perform | True | low |
| cf10 | event_role | perform | agent | woman |  | event_role:perform:agent:woman | True | medium |
| cf11 | action_event | watch |  |  | gaze_action, visual_action | action_event:watch | True | medium |
| cf12 | event_role | watch | agent | people |  | event_role:watch:agent:people | True | medium |
| cf13 | relation | woman | in | outfit | spatial_containment, visual_relation | relation:woman:in:outfit | True | high |
| cf14 | relation | woman | on | stage | spatial_support, visual_relation | relation:woman:on:stage | True | high |
| cf15 | relation | people | from | side | visual_relation | relation:people:from:side | True | medium |
| cf16 | relation | people | in | gymnasium | spatial_containment, visual_relation | relation:people:in:gymnasium | True | high |

### Stage 9 Canonicalization Notes
_none_

## 85

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `4d430422ce516f4d9a04a92c26bf4527ededfa74890e0271e0e31c59b1f83814`
**parse_path:** `sentence`

> A decorated float with red drums and colorful patterns moves down a street. People in casual clothes stand on the sidewalk watching, with buildings and a blue tarp visible in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | float | float | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | decorated | decorate | state_attribute | chunk0 | 1 | medium |
| m2 | object | drums | drum | noun_chunk_root | chunk1 | 5 | high |
| m3 | attribute | red | red | color_attribute | chunk1 | 4 | high |
| m4 | object | patterns | pattern | noun_chunk_root | chunk2 | 8 | high |
| m5 | attribute | colorful | colorful | modifier_attribute | chunk2 | 7 | medium |
| m6 | object | street | street | noun_chunk_root | chunk3 | 12 | high |
| m7 | object | People | people | noun_chunk_root | chunk4 | 14 | high |
| m8 | object | clothes | clothe | noun_chunk_root | chunk5 | 17 | high |
| m9 | attribute | casual | casual | modifier_attribute | chunk5 | 16 | medium |
| m10 | object | sidewalk | sidewalk | noun_chunk_root | chunk6 | 21 | high |
| m11 | object | buildings | building | noun_chunk_root | chunk7 | 25 | high |
| m12 | object | tarp | tarp | noun_chunk_root | chunk8 | 29 | high |
| m13 | attribute | blue | blue | color_attribute | chunk8 | 28 | high |
| m14 | context | background | background | scene_context | chunk9 | 33 | high |
| m15 | action | moves | move | verb_predicate | doc | 9 | high |
| m16 | action | stand | stand | verb_predicate | doc | 18 | high |
| m17 | action | watching | watch | verb_predicate | doc | 22 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> float |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> drums |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> patterns |
| e3 | has_attribute | m8 | m9 | medium | chunk5 amod -> clothes |
| e4 | has_attribute | m12 | m13 | high | chunk8 amod -> tarp |
| e5 | has_context | scene | m14 | high | scene_context token background |
| e6 | agent | m15 | m0 | medium | nsubj -> moves |
| e7 | agent | m16 | m7 | medium | nsubj -> stand |
| e8 | agent | m17 | m7 | medium | inherited agent advcl -> stand |
| e9 | relation | m0 | m2 | high | with |
| e10 | relation | m0 | m4 | high | with |
| e11 | relation | m0 | m6 | medium | down |
| e12 | relation | m7 | m8 | high | in |
| e13 | relation | m7 | m10 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | float | float | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:float", "parents": []} |
| ent_m2 | object | drum | drums | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:drum", "parents": []} |
| ent_m4 | object | pattern | patterns | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:pattern", "parents": []} |
| ent_m6 | object | street | street | object | raw_lemma | wordnet_synset:street.n.01 + stage9_audit | path, place | m6 | raw_mention |  |  |  | True | {"canonical": "entity:street", "parents": ["entity_parent:path", "entity_parent:place"]} |
| ent_m7 | object | people | People | person | raw_lemma | stage9_seed:parent_seed | person, human | m7 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m8 | object | clothe | clothes | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:clothe", "parents": []} |
| ent_m10 | object | sidewalk | sidewalk | object | raw_lemma | wordnet_synset:sidewalk.n.01 + stage9_audit | path, place | m10 | raw_mention |  |  |  | True | {"canonical": "entity:sidewalk", "parents": ["entity_parent:path", "entity_parent:place"]} |
| ent_m11 | object | building | buildings | object | raw_lemma | wordnet_synset:building.n.01 + stage9_audit | structure, artifact | m11 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m12 | object | tarp | tarp | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:tarp", "parents": []} |
| ent_m14 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m14 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | moves | move | move | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:move", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |
| ce1 | m16 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m7->ent_m7 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce2 | m17 | watching | watch | watch | raw_action | stage9_seed:parent_seed | gaze_action, visual_action |  | agent:m7->ent_m7 | {"canonical": "action:watch", "parents": ["action_parent:gaze_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | move | agent | agent | none | m0 | ent_m0 | medium | e6 | nsubj -> moves |  |  |
| ce1 | stand | agent | agent | none | m7 | ent_m7 | medium | e7 | nsubj -> stand |  |  |
| ce2 | watch | agent | agent | none | m7 | ent_m7 | medium | e8 | inherited agent advcl -> stand |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e9 | False | False |  |  |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e10 | False | False |  |  |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | down | down | raw_relation | raw_relation | visual_relation | medium | e11 | False | False |  |  |
| cr3 | m7 | m8 | ent_m7 | ent_m8 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e12 | False | False |  |  |
| cr4 | m7 | m10 | ent_m7 | ent_m10 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e13 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | float |  |  |  | entity_exists:float | True | low |
| cf1 | entity_exists | drum |  |  |  | entity_exists:drum | True | low |
| cf2 | entity_exists | pattern |  |  |  | entity_exists:pattern | True | low |
| cf3 | entity_exists | street |  |  | path, place | entity_exists:street | True | high |
| cf4 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf5 | entity_exists | clothe |  |  |  | entity_exists:clothe | True | low |
| cf6 | entity_exists | sidewalk |  |  | path, place | entity_exists:sidewalk | True | high |
| cf7 | entity_exists | building |  |  | structure, artifact | entity_exists:building | True | high |
| cf8 | entity_exists | tarp |  |  |  | entity_exists:tarp | True | low |
| cf9 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf10 | has_attribute | float | decorate |  | state_attribute, visual_attribute | has_attribute:float:decorate | True | medium |
| cf11 | has_attribute | drum | red |  | color_attribute, color, visual_attribute | has_attribute:drum:red | True | high |
| cf12 | has_attribute | pattern | colorful |  | color_attribute, color_quantity, visual_attribute | has_attribute:pattern:colorful | True | medium |
| cf13 | has_attribute | clothe | casual |  | modifier_attribute, visual_attribute | has_attribute:clothe:casual | True | medium |
| cf14 | has_attribute | tarp | blue |  | color_attribute, color, visual_attribute | has_attribute:tarp:blue | True | high |
| cf15 | action_event | move |  |  | locomotion_action, visual_action | action_event:move | True | high |
| cf16 | event_role | move | agent | float |  | event_role:move:agent:float | True | medium |
| cf17 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf18 | event_role | stand | agent | people |  | event_role:stand:agent:people | True | medium |
| cf19 | action_event | watch |  |  | gaze_action, visual_action | action_event:watch | True | medium |
| cf20 | event_role | watch | agent | people |  | event_role:watch:agent:people | True | medium |
| cf21 | relation | float | with | drum | association_relation, visual_relation | relation:float:with:drum | True | high |
| cf22 | relation | float | with | pattern | association_relation, visual_relation | relation:float:with:pattern | True | high |
| cf23 | relation | float | down | street | visual_relation | relation:float:down:street | True | medium |
| cf24 | relation | people | in | clothe | spatial_containment, visual_relation | relation:people:in:clothe | True | high |
| cf25 | relation | people | on | sidewalk | spatial_support, visual_relation | relation:people:on:sidewalk | True | high |

### Stage 9 Canonicalization Notes
_none_

## 86

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `4d551319236a1b6a5a39d1d82c65e42bfd911148e77ec3e904c0d4345cbbc814`
**parse_path:** `sentence`

> People sit on a red and black miniature train under green trees. A wooden bridge is visible nearby.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | People | people | noun_chunk_root | chunk0 | 0 | high |
| m1 | object | train | train | noun_chunk_root | chunk1 | 8 | high |
| m2 | attribute | red | red | color_attribute | chunk1 | 4 | high |
| m3 | attribute | black | black | color_attribute | chunk1 | 6 | high |
| m4 | attribute | miniature | miniature | size_attribute | chunk1 | 7 | high |
| m5 | object | trees | tree | noun_chunk_root | chunk2 | 11 | high |
| m6 | attribute | green | green | color_attribute | chunk2 | 10 | high |
| m7 | object | bridge | bridge | noun_chunk_root | chunk3 | 15 | high |
| m8 | attribute | wooden | wooden | material_attribute | chunk3 | 14 | high |
| m9 | action | sit | sit | verb_predicate | doc | 1 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> train |
| e1 | has_attribute | m1 | m3 | high | chunk1 conj -> train |
| e2 | has_attribute | m1 | m4 | high | chunk1 amod -> train |
| e3 | has_attribute | m5 | m6 | high | chunk2 amod -> trees |
| e4 | has_attribute | m7 | m8 | high | chunk3 amod -> bridge |
| e5 | agent | m9 | m0 | medium | nsubj -> sit |
| e6 | relation | m0 | m1 | high | on |
| e7 | relation | m0 | m5 | high | under |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | People | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | train | train | object | raw_lemma | COCO object label + wordnet_hypernym:vehicle.n.01 + stage9_audit | vehicle | m1 | raw_mention |  |  |  | True | {"canonical": "entity:train", "parents": ["entity_parent:vehicle"]} |
| ent_m5 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m5 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m7 | object | bridge | bridge | object | raw_lemma | wordnet_synset:bridge.n.01 + stage9_audit | structure, artifact | m7 | raw_mention |  |  |  | True | {"canonical": "entity:bridge", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | sit | sit | sit | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:sit", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | agent | none | m0 | ent_m0 | medium | e5 | nsubj -> sit |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e6 | False | False |  |  |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | under | under | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | train |  |  | vehicle | entity_exists:train | True | high |
| cf2 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf3 | entity_exists | bridge |  |  | structure, artifact | entity_exists:bridge | True | high |
| cf4 | has_attribute | train | red |  | color_attribute, color, visual_attribute | has_attribute:train:red | True | high |
| cf5 | has_attribute | train | black |  | color_attribute, color, visual_attribute | has_attribute:train:black | True | high |
| cf6 | has_attribute | train | miniature |  | size_attribute, visual_attribute | has_attribute:train:miniature | True | high |
| cf7 | has_attribute | tree | green |  | color_attribute, color, visual_attribute | has_attribute:tree:green | True | high |
| cf8 | has_attribute | bridge | wood |  | material_attribute, material, visual_attribute | has_attribute:bridge:wood | True | high |
| cf9 | action_event | sit |  |  | body_pose_action, visual_action | action_event:sit | True | high |
| cf10 | event_role | sit | agent | people |  | event_role:sit:agent:people | True | medium |
| cf11 | relation | people | on | train | spatial_support, visual_relation | relation:people:on:train | True | high |
| cf12 | relation | people | under | tree | spatial_vertical, visual_relation | relation:people:under:tree | True | high |

### Stage 9 Canonicalization Notes
_none_

## 87

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `4e8092e13eaab55a7241a0814c16722893bae832a811e00ba887eaaa914b5014`
**parse_path:** `sentence`

> An oval photograph in a gold-framed case shows two young girls standing side by side. The left side of the case contains a red velvet lining, and the photo is set against a dark background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | photograph | photograph | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | oval | oval | modifier_attribute | chunk0 | 1 | medium |
| m2 | object | case | case | noun_chunk_root | chunk1 | 6 | high |
| m3 | attribute | gold-framed | gold-framed | modifier_attribute | chunk1 | 5 | medium |
| m4 | object | girls | girl | noun_chunk_root | chunk2 | 10 | high |
| m5 | quantity | two | two | exact_quantity | chunk2 | 8 | high |
| m6 | attribute | young | young | modifier_attribute | chunk2 | 9 | medium |
| m7 | context | side | side | spatial_region | chunk3 | 14 | medium |
| m8 | object | case | case | noun_chunk_root | chunk5 | 21 | high |
| m9 | object | lining | lining | noun_chunk_root | chunk6 | 26 | high |
| m10 | attribute | red | red | color_attribute | chunk6 | 24 | high |
| m11 | attribute | velvet | velvet | compound_modifier | chunk6 | 25 | medium |
| m12 | object | photo | photo | noun_chunk_root | chunk7 | 30 | high |
| m13 | context | background | background | scene_context | chunk8 | 36 | high |
| m14 | attribute | dark | dark | visual_attribute | chunk8 | 35 | medium |
| m15 | action | shows | show | verb_predicate | doc | 7 | high |
| m16 | action | standing | stand | verb_predicate | doc | 11 | high |
| m17 | action | contains | contain | verb_predicate | doc | 22 | high |
| m18 | object | side | side | verb_subject | doc | 18 | medium |
| m19 | action | set | set | verb_predicate | doc | 32 | high |
| m20 | object | side | side | relation_head | doc | 12 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> photograph |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> case |
| e2 | has_quantity | m4 | m5 | high | chunk2 quantity -> girls |
| e3 | has_attribute | m4 | m6 | medium | chunk2 amod -> girls |
| e4 | has_attribute | m9 | m10 | high | chunk6 amod -> lining |
| e5 | has_attribute | m9 | m11 | medium | chunk6 compound -> lining |
| e6 | has_context | scene | m13 | high | scene_context token background |
| e7 | has_attribute | m13 | m14 | medium | chunk8 amod -> background |
| e8 | agent | m15 | m0 | medium | nsubj -> shows |
| e9 | agent | m16 | m4 | medium | nsubj -> standing |
| e10 | agent | m17 | m18 | medium | nsubj -> contains |
| e11 | patient | m17 | m9 | medium | dobj -> contains |
| e12 | agent | m19 | m12 | medium | nsubjpass -> set |
| e13 | relation | m0 | m2 | high | in |
| e14 | relation | m20 | m7 | medium | by |
| e15 | relation | m18 | m8 | medium | side_region_of |
| e16 | relation | m12 | m13 | high | against |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | photograph | photograph | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:photograph", "parents": []} |
| ent_m2 | object | case | case | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:case", "parents": []} |
| ent_m4 | object | girl | girls | person | raw_lemma | stage9_seed:parent_seed | person, human | m4 | raw_mention |  |  |  | True | {"canonical": "entity:girl", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m7 | context | side | side | object | raw_lemma | semantic_type_fallback | scene_context | m7 | raw_mention |  |  |  | True | {"canonical": "entity:side", "parents": ["entity_parent:scene_context"]} |
| ent_m8 | object | case | case | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:case", "parents": []} |
| ent_m9 | object | lining | lining | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:lining", "parents": []} |
| ent_m12 | object | photo | photo | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:photo", "parents": []} |
| ent_m13 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m13 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m18 | object | side | side | object | raw_lemma | none |  | m18 | raw_mention |  |  |  | True | {"canonical": "entity:side", "parents": []} |
| ent_m20 | object | side | side | object | raw_lemma | none |  | m20 | raw_mention |  |  |  | True | {"canonical": "entity:side", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | shows | show | show | raw_action | wordnet_synset:show.v.01 + stage9_audit | visual_presentation_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:show", "parents": ["action_parent:visual_presentation_action", "action_parent:visual_action"]} |  |
| ce1 | m16 | standing | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m4->ent_m4 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce2 | m17 | contains | contain | contain | raw_action | wordnet_synset:contain.v.01 + stage9_audit | containment_state_action, visual_action |  | agent:m18->ent_m18; patient:m9->ent_m9 | {"canonical": "action:contain", "parents": ["action_parent:containment_state_action", "action_parent:visual_action"]} |  |
| ce3 | m19 | set | set | set | raw_action | visual_action_fallback | visual_action |  | patient<-theme[passive_to_active]:m12->ent_m12 | {"canonical": "action:set", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | agent | none | m0 | ent_m0 | medium | e8 | nsubj -> shows |  |  |
| ce1 | stand | agent | agent | none | m4 | ent_m4 | medium | e9 | nsubj -> standing |  |  |
| ce2 | contain | agent | agent | none | m18 | ent_m18 | medium | e10 | nsubj -> contains |  |  |
| ce2 | contain | patient | patient | none | m9 | ent_m9 | medium | e11 | dobj -> contains |  |  |
| ce3 | set | patient | theme | passive_to_active | m12 | ent_m12 | medium | e12 | nsubjpass -> set |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e13 | False | False |  |  |
| cr1 | m20 | m7 | ent_m20 | ent_m7 | by | by | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | medium | e14 | False | False |  |  |
| cr2 | m18 | m8 | ent_m18 | ent_m8 | side_region_of | side_region_of | generated_region_pattern\|mixed_relation_collapse_rules | generated_region_pattern\|mixed_relation_collapse_rules | spatial_region, visual_relation | medium | e15 | False | False |  |  |
| cr3 | m12 | m13 | ent_m12 | ent_m13 | against | against | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_contact, visual_relation | high | e16 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | photograph |  |  |  | entity_exists:photograph | True | low |
| cf1 | entity_exists | case |  |  |  | entity_exists:case | True | low |
| cf2 | entity_exists | girl |  |  | person, human | entity_exists:girl | True | high |
| cf3 | entity_exists | side |  |  | scene_context | entity_exists:side | True | medium |
| cf4 | entity_exists | case |  |  |  | entity_exists:case | True | low |
| cf5 | entity_exists | lining |  |  |  | entity_exists:lining | True | low |
| cf6 | entity_exists | photo |  |  |  | entity_exists:photo | True | low |
| cf7 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf8 | entity_exists | side |  |  |  | entity_exists:side | True | low |
| cf9 | entity_exists | side |  |  |  | entity_exists:side | True | low |
| cf10 | has_attribute | photograph | oval |  | modifier_attribute, visual_attribute | has_attribute:photograph:oval | True | medium |
| cf11 | has_attribute | case | gold-framed |  | modifier_attribute, visual_attribute | has_attribute:case:gold-framed | True | medium |
| cf12 | has_quantity | girl | two |  | exact_quantity, quantity | has_quantity:girl:two | True | high |
| cf13 | has_attribute | girl | young |  | modifier_attribute, visual_attribute | has_attribute:girl:young | True | medium |
| cf14 | has_attribute | lining | red |  | color_attribute, color, visual_attribute | has_attribute:lining:red | True | high |
| cf15 | has_attribute | lining | velvet |  | material_attribute, material, visual_attribute | has_attribute:lining:velvet | True | medium |
| cf16 | has_attribute | background | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:background:dark | True | medium |
| cf17 | action_event | show |  |  | visual_presentation_action, visual_action | action_event:show | True | high |
| cf18 | event_role | show | agent | photograph |  | event_role:show:agent:photograph | True | medium |
| cf19 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf20 | event_role | stand | agent | girl |  | event_role:stand:agent:girl | True | medium |
| cf21 | action_event | contain |  |  | containment_state_action, visual_action | action_event:contain | True | medium |
| cf22 | event_role | contain | agent | side |  | event_role:contain:agent:side | True | medium |
| cf23 | event_role | contain | patient | lining |  | event_role:contain:patient:lining | True | medium |
| cf24 | action_event | set |  |  | visual_action | action_event:set | True | low |
| cf25 | event_role | set | patient | photo |  | event_role:set:patient:photo | True | medium |
| cf26 | relation | photograph | in | case | spatial_containment, visual_relation | relation:photograph:in:case | True | high |
| cf27 | relation | side | by | side | spatial_proximity, visual_relation | relation:side:by:side | True | medium |
| cf28 | relation | side | side_region_of | case | spatial_region, visual_relation | relation:side:side_region_of:case | True | medium |
| cf29 | relation | photo | against | background | spatial_contact, visual_relation | relation:photo:against:background | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_patient | m19 | e12 | m12 |  |  | {"action_mention_id": "m19", "kind": "passive_subject_to_patient", "raw_edge_id": "e12", "raw_role": "theme", "role": "patient", "target": "m12", "voice_normalization": "passive_to_active"} |

## 88

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `4ecc5d80e02b3fd8d39cfc00680ada9d3be1bd6da0c6b0726081e963008a1c14`
**parse_path:** `tag_list`

> golf player, green grass, golf bag, golf club, trees

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | player | player | segment_head | t0 | 1 | high |
| m1 | attribute | golf | golf | attribute | t0 | 0 | high |
| m2 | object | grass | grass | segment_head | t1 | 1 | high |
| m3 | attribute | green | green | attribute | t1 | 0 | high |
| m4 | object | bag | bag | segment_head | t2 | 1 | high |
| m5 | attribute | golf | golf | attribute | t2 | 0 | high |
| m6 | object | golf club | golf_club | segment_head | t3 | 0 | high |
| m7 | object | trees | tree | segment_head | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> player |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> grass |
| e2 | has_attribute | m4 | m5 | high | t2 internal compound -> bag |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | player | player | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:player", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | grass | grass | object | raw_lemma | wordnet_synset:grass.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m2 | raw_mention |  |  |  | True | {"canonical": "entity:grass", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m4 | object | bag | bag | object | raw_lemma | wordnet_synset:bag.n.01 + stage9_audit | container, accessory, artifact | m4 | raw_mention |  |  |  | True | {"canonical": "entity:bag", "parents": ["entity_parent:container", "entity_parent:accessory", "entity_parent:artifact"]} |
| ent_m6 | object | golf_club | golf club | object | lvis_object\|visual_genome_object_synset\|wordnet_noun_mwe | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:golf_club", "parents": []} |
| ent_m7 | object | tree | trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m7 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |

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
| cf0 | entity_exists | player |  |  | person, human | entity_exists:player | True | high |
| cf1 | entity_exists | grass |  |  | plant, living_thing | entity_exists:grass | True | high |
| cf2 | entity_exists | bag |  |  | container, accessory, artifact | entity_exists:bag | True | medium |
| cf3 | entity_exists | golf_club |  |  |  | entity_exists:golf_club | True | high |
| cf4 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf5 | has_attribute | player | golf |  | attribute, visual_attribute | has_attribute:player:golf | True | high |
| cf6 | has_attribute | grass | green |  | color_attribute, color, visual_attribute | has_attribute:grass:green | True | high |
| cf7 | has_attribute | bag | golf |  | attribute, visual_attribute | has_attribute:bag:golf | True | high |

### Stage 9 Canonicalization Notes
_none_

## 89

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `4ef4fa26000ddbb432bf80a1d34fd2b2635c2d8aac6478de72ed4d4e93040c14`
**parse_path:** `sentence`

> People in historical costumes march through a courtyard with brick arches and windows. Some carry flags with red and white designs, while others hold instruments or walk beside them. A large umbrella is visible in the foreground on the right.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | People | people | noun_chunk_root | chunk0 | 0 | high |
| m1 | object | costumes | costume | noun_chunk_root | chunk1 | 3 | high |
| m2 | attribute | historical | historical | modifier_attribute | chunk1 | 2 | medium |
| m3 | object | courtyard | courtyard | noun_chunk_root | chunk2 | 7 | high |
| m4 | object | arches | arch | noun_chunk_root | chunk3 | 10 | high |
| m5 | attribute | brick | brick | material_attribute | chunk3 | 9 | high |
| m6 | object | windows | window | noun_chunk_root | chunk4 | 12 | high |
| m7 | quantity | Some | some | indefinite_quantity | chunk5 | 14 | medium |
| m8 | object | flags | flag | noun_chunk_root | chunk6 | 16 | high |
| m9 | object | designs | design | noun_chunk_root | chunk7 | 21 | high |
| m10 | attribute | red | red | color_attribute | chunk7 | 18 | high |
| m11 | attribute | white | white | color_attribute | chunk7 | 20 | high |
| m12 | object | instruments | instrument | noun_chunk_root | chunk9 | 26 | high |
| m13 | object | umbrella | umbrella | noun_chunk_root | chunk11 | 34 | high |
| m14 | attribute | large | large | size_attribute | chunk11 | 33 | high |
| m15 | context | foreground | foreground | scene_context | chunk12 | 39 | high |
| m16 | context | right | right | spatial_region | chunk13 | 42 | medium |
| m17 | reference | others | other | contrastive_reference | nominal_reference | 24 | high |
| m18 | action | march | march | verb_predicate | doc | 4 | high |
| m19 | action | carry | carry | verb_predicate | doc | 15 | high |
| m20 | action | hold | hold | verb_predicate | doc | 25 | high |
| m21 | action | walk | walk | verb_predicate | doc | 28 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 amod -> costumes |
| e1 | has_attribute | m4 | m5 | high | chunk3 compound -> arches |
| e2 | has_attribute | m9 | m10 | high | chunk7 amod -> designs |
| e3 | has_attribute | m9 | m11 | high | chunk7 conj -> designs |
| e4 | has_attribute | m13 | m14 | high | chunk11 amod -> umbrella |
| e5 | has_context | scene | m15 | high | scene_context token foreground |
| e6 | refers_to | m17 | m0 | high | contrastive_reference others -> People; score=100 |
| e7 | agent | m18 | m0 | medium | nsubj -> march |
| e8 | patient | m19 | m8 | medium | dobj -> carry |
| e9 | agent | m20 | m0 | medium | nsubj -> hold; resolved others -> People |
| e10 | patient | m20 | m12 | medium | dobj -> hold |
| e11 | agent | m21 | m0 | medium | inherited agent conj -> hold |
| e12 | relation | m0 | m1 | high | in |
| e13 | relation | m0 | m3 | medium | through |
| e14 | relation | m3 | m4 | high | with |
| e15 | relation | m3 | m6 | high | with |
| e16 | relation | m8 | m9 | high | with |
| e17 | relation | m12 | m0 | medium | beside; repaired_self_edge_source from People |
| e18 | relation | m13 | m16 | high | on |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | People | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | costume | costumes | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:costume", "parents": []} |
| ent_m3 | object | courtyard | courtyard | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:courtyard", "parents": []} |
| ent_m4 | object | arch | arches | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:arch", "parents": []} |
| ent_m6 | object | window | windows | object | raw_lemma | wordnet_synset:window.n.01 + stage9_audit | architectural_part, artifact | m6 | raw_mention |  |  |  | True | {"canonical": "entity:window", "parents": ["entity_parent:architectural_part", "entity_parent:artifact"]} |
| ent_m8 | object | flag | flags | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:flag", "parents": []} |
| ent_m9 | object | design | designs | object | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:design", "parents": []} |
| ent_m12 | object | instrument | instruments | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:instrument", "parents": []} |
| ent_m13 | object | umbrella | umbrella | object | raw_lemma | COCO object label + wordnet_synset:umbrella.n.01 + stage9_audit | accessory, artifact | m13 | raw_mention |  |  |  | True | {"canonical": "entity:umbrella", "parents": ["entity_parent:accessory", "entity_parent:artifact"]} |
| ent_m15 | context | foreground | foreground | object | raw_lemma | stage9_seed:parent_seed | scene_context | m15 | raw_mention |  |  |  | True | {"canonical": "entity:foreground", "parents": ["entity_parent:scene_context"]} |
| ent_m16 | context | right | right | object | raw_lemma | semantic_type_fallback | scene_context | m16 | raw_mention |  |  |  | True | {"canonical": "entity:right", "parents": ["entity_parent:scene_context"]} |
| eref_m17 | complement_subset | people | others | person | raw_lemma | stage9_seed:parent_seed | person, human | m17 | stage9_reference | ent_m0 |  | many | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m17 | eref_m17 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | march | march | march | raw_action | visual_action_fallback | visual_action |  | agent:m0->ent_m0 | {"canonical": "action:march", "parents": ["action_parent:visual_action"]} |  |
| ce1 | m19 | carry | carry | carry | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action |  | patient:m8->ent_m8 | {"canonical": "action:carry", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce2 | m20 | hold | hold | hold | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action |  | agent:m0->eref_m17; patient:m12->ent_m12 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce3 | m21 | walk | walk | walk | raw_action | stage9_seed:parent_seed | locomotion_action, visual_action |  | agent:m0->eref_m17 | {"canonical": "action:walk", "parents": ["action_parent:locomotion_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | march | agent | agent | none | m0 | ent_m0 | medium | e7 | nsubj -> march |  |  |
| ce1 | carry | patient | patient | none | m8 | ent_m8 | medium | e8 | dobj -> carry |  |  |
| ce2 | hold | agent | agent | none | m0 | eref_m17 | medium | e9 | nsubj -> hold; resolved others -> People |  |  |
| ce2 | hold | patient | patient | none | m12 | ent_m12 | medium | e10 | dobj -> hold |  |  |
| ce3 | walk | agent | agent | none | m0 | eref_m17 | medium | e11 | inherited agent conj -> hold |  | conj_agent_inherited_from_reference_canonical_target |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e12 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | through | through | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_path, visual_relation | medium | e13 | False | False |  |  |
| cr2 | m3 | m4 | ent_m3 | ent_m4 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr3 | m3 | m6 | ent_m3 | ent_m6 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e15 | False | False |  |  |
| cr4 | m8 | m9 | ent_m8 | ent_m9 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e16 | False | False |  |  |
| cr5 | m12 | m0 | ent_m12 | ent_m0 | beside; repaired_self_edge_source from People | next_to | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_proximity, visual_relation | medium | e17 | False | False |  |  |
| cr6 | m13 | m16 | ent_m13 | ent_m16 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e18 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf1 | entity_exists | costume |  |  |  | entity_exists:costume | True | low |
| cf2 | entity_exists | courtyard |  |  |  | entity_exists:courtyard | True | low |
| cf3 | entity_exists | arch |  |  |  | entity_exists:arch | True | low |
| cf4 | entity_exists | window |  |  | architectural_part, artifact | entity_exists:window | True | high |
| cf5 | entity_exists | flag |  |  |  | entity_exists:flag | True | low |
| cf6 | entity_exists | design |  |  |  | entity_exists:design | True | low |
| cf7 | entity_exists | instrument |  |  |  | entity_exists:instrument | True | low |
| cf8 | entity_exists | umbrella |  |  | accessory, artifact | entity_exists:umbrella | True | high |
| cf9 | entity_exists | foreground |  |  | scene_context | entity_exists:foreground | True | high |
| cf10 | entity_exists | right |  |  | scene_context | entity_exists:right | True | medium |
| cf11 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf12 | has_attribute | costume | historical |  | modifier_attribute, visual_attribute | has_attribute:costume:historical | True | medium |
| cf13 | has_attribute | arch | brick |  | material_attribute, material, visual_attribute | has_attribute:arch:brick | True | high |
| cf14 | has_attribute | design | red |  | color_attribute, color, visual_attribute | has_attribute:design:red | True | high |
| cf15 | has_attribute | design | white |  | color_attribute, color, visual_attribute | has_attribute:design:white | True | high |
| cf16 | has_attribute | umbrella | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:umbrella:large | True | high |
| cf17 | action_event | march |  |  | visual_action | action_event:march | True | low |
| cf18 | event_role | march | agent | people |  | event_role:march:agent:people | True | medium |
| cf19 | action_event | carry |  |  | manipulation_action, visual_action | action_event:carry | True | high |
| cf20 | event_role | carry | patient | flag |  | event_role:carry:patient:flag | True | medium |
| cf21 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf22 | event_role | hold | agent | people |  | event_role:hold:agent:people | True | medium |
| cf23 | event_role | hold | patient | instrument |  | event_role:hold:patient:instrument | True | medium |
| cf24 | action_event | walk |  |  | locomotion_action, visual_action | action_event:walk | True | high |
| cf25 | event_role | walk | agent | people |  | event_role:walk:agent:people | True | medium |
| cf26 | relation | people | in | costume | spatial_containment, visual_relation | relation:people:in:costume | True | high |
| cf27 | relation | people | through | courtyard | spatial_path, visual_relation | relation:people:through:courtyard | True | medium |
| cf28 | relation | courtyard | with | arch | association_relation, visual_relation | relation:courtyard:with:arch | True | high |
| cf29 | relation | courtyard | with | window | association_relation, visual_relation | relation:courtyard:with:window | True | high |
| cf30 | relation | flag | with | design | association_relation, visual_relation | relation:flag:with:design | True | high |
| cf31 | relation | instrument | next_to | people | spatial_proximity, visual_relation | relation:instrument:next_to:people | True | medium |
| cf32 | relation | umbrella | on | right | spatial_support, visual_relation | relation:umbrella:on:right | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| conj_agent_reference_target_inherited | m21 |  |  | eref_m17 |  | {"action_mention_id": "m21", "canonical_target": "eref_m17", "kind": "conj_agent_reference_target_inherited", "source_action_mention_id": "m20"} |
| relation_lexical_canonicalized |  | e17 |  |  |  | {"canonical": "next_to", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e17", "raw_relation": "beside; repaired_self_edge_source from People", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 90

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `5039b9d28bf1196b57964ae33759c79770ece5a2b906aee3e9733df49e5cd414`
**parse_path:** `tag_list`

> child, painting, hat, green uniform, classroom

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | child | child | segment_head | t0 | 0 | high |
| m1 | object | painting | painting | segment_head | t1 | 0 | high |
| m2 | object | hat | hat | segment_head | t2 | 0 | high |
| m3 | object | uniform | uniform | segment_head | t3 | 1 | high |
| m4 | attribute | green | green | attribute | t3 | 0 | high |
| m5 | object | classroom | classroom | segment_head | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m3 | m4 | high | t3 internal compound -> uniform |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | child | child | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | painting | painting | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:painting", "parents": []} |
| ent_m2 | object | hat | hat | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:hat", "parents": []} |
| ent_m3 | object | uniform | uniform | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m3 | raw_mention |  |  |  | True | {"canonical": "entity:uniform", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m5 | object | classroom | classroom | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:classroom", "parents": []} |

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
| cf0 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf1 | entity_exists | painting |  |  |  | entity_exists:painting | True | low |
| cf2 | entity_exists | hat |  |  |  | entity_exists:hat | True | low |
| cf3 | entity_exists | uniform |  |  | clothing, wearable | entity_exists:uniform | True | high |
| cf4 | entity_exists | classroom |  |  |  | entity_exists:classroom | True | low |
| cf5 | has_attribute | uniform | green |  | color_attribute, color, visual_attribute | has_attribute:uniform:green | True | high |

### Stage 9 Canonicalization Notes
_none_

## 91

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `507048cdb9a5cdef5b15cda6353c416040d976a84c4a5bdd4aefb83f77532c14`
**parse_path:** `tag_list`

> control levers, dirty metal, red background, stickers, mechanical controls

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | levers | lever | segment_head | t0 | 1 | high |
| m1 | attribute | control | control | attribute | t0 | 0 | high |
| m2 | object | metal | metal | segment_head | t1 | 1 | high |
| m3 | attribute | dirty | dirty | attribute | t1 | 0 | high |
| m4 | context | background | background | scene_context | t2 | 1 | high |
| m5 | attribute | red | red | attribute | t2 | 0 | high |
| m6 | object | stickers | sticker | segment_head | t3 | 0 | high |
| m7 | object | controls | control | segment_head | t4 | 1 | high |
| m8 | attribute | mechanical | mechanical | attribute | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> levers |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> metal |
| e2 | has_context | scene | m4 | high | t2 context tag |
| e3 | has_attribute | m4 | m5 | high | t2 internal amod -> background |
| e4 | has_attribute | m7 | m8 | high | t4 internal amod -> controls |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | lever | levers | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:lever", "parents": []} |
| ent_m2 | object | metal | metal | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:metal", "parents": []} |
| ent_m4 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m4 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m6 | object | sticker | stickers | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:sticker", "parents": []} |
| ent_m7 | object | control | controls | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:control", "parents": []} |

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
| cf0 | entity_exists | lever |  |  |  | entity_exists:lever | True | low |
| cf1 | entity_exists | metal |  |  |  | entity_exists:metal | True | low |
| cf2 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf3 | entity_exists | sticker |  |  |  | entity_exists:sticker | True | low |
| cf4 | entity_exists | control |  |  |  | entity_exists:control | True | low |
| cf5 | has_attribute | lever | control |  | attribute, visual_attribute | has_attribute:lever:control | True | high |
| cf6 | has_attribute | metal | dirty |  | condition_attribute, clean_exact_overlap, cleanliness, visual_attribute | has_attribute:metal:dirty | True | high |
| cf7 | has_attribute | background | red |  | color_attribute, color, visual_attribute | has_attribute:background:red | True | high |
| cf8 | has_attribute | control | mechanical |  | attribute, visual_attribute | has_attribute:control:mechanical | True | high |

### Stage 9 Canonicalization Notes
_none_

## 92

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `517403938d146fa547a32e32a745dbb0d465ef936a474a1589a49aef6e272c14`
**parse_path:** `tag_list`

> volcano, island, ocean, mountains, landscape

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | volcano | volcano | segment_head | t0 | 0 | high |
| m1 | object | island | island | segment_head | t1 | 0 | high |
| m2 | object | ocean | ocean | segment_head | t2 | 0 | high |
| m3 | object | mountains | mountain | segment_head | t3 | 0 | high |
| m4 | object | landscape | landscape | segment_head | t4 | 0 | high |

### Raw Concept Edges
_none_

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | volcano | volcano | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:volcano", "parents": []} |
| ent_m1 | object | island | island | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:island", "parents": []} |
| ent_m2 | object | ocean | ocean | object | raw_lemma | wordnet_synset:ocean.n.01 + stage9_audit | body_of_water, place | m2 | raw_mention |  |  |  | True | {"canonical": "entity:ocean", "parents": ["entity_parent:body_of_water", "entity_parent:place"]} |
| ent_m3 | object | mountain | mountains | object | raw_lemma | wordnet_synset:mountain.n.01 + stage9_audit | landform, place | m3 | raw_mention |  |  |  | True | {"canonical": "entity:mountain", "parents": ["entity_parent:landform", "entity_parent:place"]} |
| ent_m4 | object | landscape | landscape | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:landscape", "parents": []} |

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
| cf0 | entity_exists | volcano |  |  |  | entity_exists:volcano | True | low |
| cf1 | entity_exists | island |  |  |  | entity_exists:island | True | low |
| cf2 | entity_exists | ocean |  |  | body_of_water, place | entity_exists:ocean | True | high |
| cf3 | entity_exists | mountain |  |  | landform, place | entity_exists:mountain | True | high |
| cf4 | entity_exists | landscape |  |  |  | entity_exists:landscape | True | low |

### Stage 9 Canonicalization Notes
_none_

## 93

**caption_shape:** `multi-sentence`
**caption_type:** `short`
**caption_id:** `53df658cabfb9bc2b0afb0a7c6336c4cf2f52cbe8dd02fb950e71dc95b153c14`
**parse_path:** `sentence`

> A statue stands on a pedestal against a cloudy, golden sky. Trees are visible to the left.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | statue | statue | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | pedestal | pedestal | noun_chunk_root | chunk1 | 5 | high |
| m2 | object | sky | sky | noun_chunk_root | chunk2 | 11 | high |
| m3 | attribute | cloudy | cloudy | modifier_attribute | chunk2 | 8 | medium |
| m4 | attribute | golden | golden | color_attribute | chunk2 | 10 | high |
| m5 | object | Trees | tree | noun_chunk_root | chunk3 | 13 | high |
| m6 | context | left | left | spatial_region | chunk4 | 18 | medium |
| m7 | action | stands | stand | verb_predicate | doc | 2 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | medium | chunk2 amod -> sky |
| e1 | has_attribute | m2 | m4 | high | chunk2 amod -> sky |
| e2 | agent | m7 | m0 | medium | nsubj -> stands |
| e3 | relation | m0 | m1 | high | on |
| e4 | relation | m0 | m2 | high | against |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | statue | statue | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:statue", "parents": []} |
| ent_m1 | object | pedestal | pedestal | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:pedestal", "parents": []} |
| ent_m2 | object | sky | sky | object | raw_lemma | wordnet_synset:sky.n.01 + stage9_audit | natural_scene | m2 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": ["entity_parent:natural_scene"]} |
| ent_m5 | object | tree | Trees | object | raw_lemma | wordnet_synset:tree.n.01 + wordnet_hypernym:plant.n.02 + stage9_audit | plant, living_thing | m5 | raw_mention |  |  |  | True | {"canonical": "entity:tree", "parents": ["entity_parent:plant", "entity_parent:living_thing"]} |
| ent_m6 | context | left | left | object | raw_lemma | semantic_type_fallback | scene_context | m6 | raw_mention |  |  |  | True | {"canonical": "entity:left", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e2 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e3 | False | False |  |  |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | against | against | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_contact, visual_relation | high | e4 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | statue |  |  |  | entity_exists:statue | True | low |
| cf1 | entity_exists | pedestal |  |  |  | entity_exists:pedestal | True | low |
| cf2 | entity_exists | sky |  |  | natural_scene | entity_exists:sky | True | high |
| cf3 | entity_exists | tree |  |  | plant, living_thing | entity_exists:tree | True | high |
| cf4 | entity_exists | left |  |  | scene_context | entity_exists:left | True | medium |
| cf5 | has_attribute | sky | cloudy |  | weather_attribute, weather, visual_attribute | has_attribute:sky:cloudy | True | medium |
| cf6 | has_attribute | sky | golden |  | color_attribute, color, visual_attribute | has_attribute:sky:golden | True | high |
| cf7 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf8 | event_role | stand | agent | statue |  | event_role:stand:agent:statue | True | medium |
| cf9 | relation | statue | on | pedestal | spatial_support, visual_relation | relation:statue:on:pedestal | True | high |
| cf10 | relation | statue | against | sky | spatial_contact, visual_relation | relation:statue:against:sky | True | high |

### Stage 9 Canonicalization Notes
_none_

## 94

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `5449af841d678115201d7d7bf1455dd8929b0c1c50430e9e9c3b6fb636f85814`
**parse_path:** `sentence`

> A woman in a tiara and cape stands with a man in a red coat holding a child, all smiling at a party.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | noun_chunk_root | chunk0 | 1 | high |
| m1 | object | tiara | tiara | noun_chunk_root | chunk1 | 4 | high |
| m2 | object | cape | cape | noun_chunk_root | chunk2 | 6 | high |
| m3 | object | man | man | noun_chunk_root | chunk3 | 10 | high |
| m4 | object | coat | coat | noun_chunk_root | chunk4 | 14 | high |
| m5 | attribute | red | red | color_attribute | chunk4 | 13 | high |
| m6 | object | child | child | noun_chunk_root | chunk5 | 17 | high |
| m7 | quantity | all | all | group_quantity | chunk6 | 19 | high |
| m8 | object | party | party | noun_chunk_root | chunk7 | 23 | high |
| m9 | group | a tiara and cape | tiara_and_cape | coordination_group | nominal_reference | 4 | medium |
| m10 | reference | all | all | group_reference | nominal_reference | 19 | medium |
| m11 | action | stands | stand | verb_predicate | doc | 7 | high |
| m12 | action | holding | hold | verb_predicate | doc | 15 | high |
| m13 | action | smiling | smile | verb_predicate | doc | 20 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m4 | m5 | high | chunk4 amod -> coat |
| e1 | has_member | m9 | m1 | medium | coordination_group |
| e2 | has_member | m9 | m2 | medium | coordination_group |
| e3 | refers_to | m10 | m9 | medium | group_reference all -> a tiara and cape; score=77 |
| e4 | agent | m11 | m0 | medium | nsubj -> stands |
| e5 | agent | m12 | m3 | medium | inherited agent acl -> man |
| e6 | patient | m12 | m6 | medium | dobj -> holding |
| e7 | agent | m13 | m9 | medium | nsubj -> smiling; resolved all -> a tiara and cape |
| e8 | relation | m0 | m1 | high | in |
| e9 | relation | m0 | m2 | high | in |
| e10 | relation | m0 | m3 | high | with |
| e11 | relation | m3 | m4 | high | in |
| e12 | relation | m9 | m8 | medium | at |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m1 | object | tiara | tiara | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:tiara", "parents": []} |
| ent_m2 | object | cape | cape | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:cape", "parents": []} |
| ent_m3 | object | man | man | person | raw_lemma | stage9_seed:parent_seed | person, human | m3 | raw_mention |  |  |  | True | {"canonical": "entity:man", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m4 | object | coat | coat | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:coat", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m6 | object | child | child | person | raw_lemma | stage9_seed:parent_seed | person, human | m6 | raw_mention |  |  |  | True | {"canonical": "entity:child", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m8 | object | party | party | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:party", "parents": []} |
| ent_m9 | group | tiara_and_cape | a tiara and cape | group | raw_lemma | none |  | m9 | raw_mention |  |  |  | True | {"canonical": "entity:tiara_and_cape", "parents": []} |
| eref_m10 | group | tiara_and_cape | all | group | raw_lemma | none |  | m10 | stage9_reference | ent_m9 |  | 2 | True | {"canonical": "entity:tiara_and_cape", "parents": []} |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m10 | eref_m10 | m9 | ent_m9 | medium |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m11 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m12 | holding | hold | hold | raw_action | stage9_seed:parent_seed | manipulation_action, visual_action |  | agent:m3->ent_m3; patient:m6->ent_m6 | {"canonical": "action:hold", "parents": ["action_parent:manipulation_action", "action_parent:visual_action"]} |  |
| ce2 | m13 | smiling | smile | smile | raw_action | stage9_seed:parent_seed | expression_action, visual_action |  | agent:m9->eref_m10 | {"canonical": "action:smile", "parents": ["action_parent:expression_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e4 | nsubj -> stands |  |  |
| ce1 | hold | agent | agent | none | m3 | ent_m3 | medium | e5 | inherited agent acl -> man |  |  |
| ce1 | hold | patient | patient | none | m6 | ent_m6 | medium | e6 | dobj -> holding |  |  |
| ce2 | smile | agent | agent | none | m9 | eref_m10 | medium | e7 | nsubj -> smiling; resolved all -> a tiara and cape |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e8 | False | False |  |  |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e9 | False | False |  |  |
| cr2 | m0 | m3 | ent_m0 | ent_m3 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e10 | False | False |  |  |
| cr3 | m3 | m4 | ent_m3 | ent_m4 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e11 | False | False |  |  |
| cr4 | m9 | m8 | ent_m9 | ent_m8 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e12 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | tiara |  |  |  | entity_exists:tiara | True | low |
| cf2 | entity_exists | cape |  |  |  | entity_exists:cape | True | low |
| cf3 | entity_exists | man |  |  | person, human | entity_exists:man | True | high |
| cf4 | entity_exists | coat |  |  | clothing, wearable | entity_exists:coat | True | high |
| cf5 | entity_exists | child |  |  | person, human | entity_exists:child | True | high |
| cf6 | entity_exists | party |  |  |  | entity_exists:party | True | low |
| cf7 | entity_exists | tiara_and_cape |  |  |  | entity_exists:tiara_and_cape | True | low |
| cf8 | entity_exists | tiara_and_cape |  |  |  | entity_exists:tiara_and_cape | True | low |
| cf9 | has_attribute | coat | red |  | color_attribute, color, visual_attribute | has_attribute:coat:red | True | high |
| cf10 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf11 | event_role | stand | agent | woman |  | event_role:stand:agent:woman | True | medium |
| cf12 | action_event | hold |  |  | manipulation_action, visual_action | action_event:hold | True | high |
| cf13 | event_role | hold | agent | man |  | event_role:hold:agent:man | True | medium |
| cf14 | event_role | hold | patient | child |  | event_role:hold:patient:child | True | medium |
| cf15 | action_event | smile |  |  | expression_action, visual_action | action_event:smile | True | high |
| cf16 | event_role | smile | agent | tiara_and_cape |  | event_role:smile:agent:tiara_and_cape | True | medium |
| cf17 | relation | woman | in | tiara | spatial_containment, visual_relation | relation:woman:in:tiara | True | high |
| cf18 | relation | woman | in | cape | spatial_containment, visual_relation | relation:woman:in:cape | True | high |
| cf19 | relation | woman | with | man | association_relation, visual_relation | relation:woman:with:man | True | high |
| cf20 | relation | man | in | coat | spatial_containment, visual_relation | relation:man:in:coat | True | high |
| cf21 | relation | tiara_and_cape | at | party | spatial_location, visual_relation | relation:tiara_and_cape:at:party | True | medium |

### Stage 9 Canonicalization Notes
_none_

## 95

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `54b81836f2d965daa4a6236ab25b5a40db1393fba74684c849dcf868a0dfbc14`
**parse_path:** `tag_list`

> yellow orchid, green stem, dark sky, large leaves

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | orchid | orchid | segment_head | t0 | 1 | high |
| m1 | attribute | yellow | yellow | attribute | t0 | 0 | high |
| m2 | object | stem | stem | segment_head | t1 | 1 | high |
| m3 | attribute | green | green | attribute | t1 | 0 | high |
| m4 | object | sky | sky | segment_head | t2 | 1 | high |
| m5 | attribute | dark | dark | attribute | t2 | 0 | high |
| m6 | object | leaves | leaf | segment_head | t3 | 1 | high |
| m7 | attribute | large | large | attribute | t3 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> orchid |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> stem |
| e2 | has_attribute | m4 | m5 | high | t2 internal amod -> sky |
| e3 | has_attribute | m6 | m7 | high | t3 internal amod -> leaves |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | orchid | orchid | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:orchid", "parents": []} |
| ent_m2 | object | stem | stem | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:stem", "parents": []} |
| ent_m4 | object | sky | sky | object | raw_lemma | wordnet_synset:sky.n.01 + stage9_audit | natural_scene | m4 | raw_mention |  |  |  | True | {"canonical": "entity:sky", "parents": ["entity_parent:natural_scene"]} |
| ent_m6 | object | leaf | leaves | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:leaf", "parents": []} |

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
| cf0 | entity_exists | orchid |  |  |  | entity_exists:orchid | True | low |
| cf1 | entity_exists | stem |  |  |  | entity_exists:stem | True | low |
| cf2 | entity_exists | sky |  |  | natural_scene | entity_exists:sky | True | high |
| cf3 | entity_exists | leaf |  |  |  | entity_exists:leaf | True | low |
| cf4 | has_attribute | orchid | yellow |  | color_attribute, color, visual_attribute | has_attribute:orchid:yellow | True | high |
| cf5 | has_attribute | stem | green |  | color_attribute, color, visual_attribute | has_attribute:stem:green | True | high |
| cf6 | has_attribute | sky | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:sky:dark | True | high |
| cf7 | has_attribute | leaf | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:leaf:large | True | high |

### Stage 9 Canonicalization Notes
_none_

## 96

**caption_shape:** `tag-list-like`
**caption_type:** `tag`
**caption_id:** `55375c4707e2fdf8ac11dde961eff116c10a6ab8bba07095a67251011efc1c14`
**parse_path:** `tag_list`

> long hair, robot, hands, suit, indoor

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hair | hair | segment_head | t0 | 1 | high |
| m1 | attribute | long | long | attribute | t0 | 0 | high |
| m2 | object | robot | robot | segment_head | t1 | 0 | high |
| m3 | object | hands | hand | segment_head | t2 | 0 | high |
| m4 | object | suit | suit | segment_head | t3 | 0 | high |
| m5 | context | indoor | indoor | scene_context | t4 | 0 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> hair |
| e1 | has_context | scene | m5 | high | t4 context tag |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hair | hair | object | raw_lemma | stage9_seed:parent_seed | body_part | m0 | raw_mention |  |  |  | True | {"canonical": "entity:hair", "parents": ["entity_parent:body_part"]} |
| ent_m2 | object | robot | robot | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:robot", "parents": []} |
| ent_m3 | object | hand | hands | object | raw_lemma | stage9_seed:parent_seed | body_part | m3 | raw_mention |  |  |  | True | {"canonical": "entity:hand", "parents": ["entity_parent:body_part"]} |
| ent_m4 | object | suit | suit | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:suit", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m5 | context | indoor | indoor | object | raw_lemma | stage9_seed:parent_seed | scene_context | m5 | raw_mention |  |  |  | True | {"canonical": "entity:indoor", "parents": ["entity_parent:scene_context"]} |

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
| cf0 | entity_exists | hair |  |  | body_part | entity_exists:hair | True | high |
| cf1 | entity_exists | robot |  |  |  | entity_exists:robot | True | low |
| cf2 | entity_exists | hand |  |  | body_part | entity_exists:hand | True | high |
| cf3 | entity_exists | suit |  |  | clothing, wearable | entity_exists:suit | True | high |
| cf4 | entity_exists | indoor |  |  | scene_context | entity_exists:indoor | True | high |
| cf5 | has_attribute | hair | long |  | size_attribute, clean_exact_overlap, length, visual_attribute | has_attribute:hair:long | True | high |

### Stage 9 Canonicalization Notes
_none_

## 97

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `5588c4cd10d0cf2280ac14580e8b1a7ec7da7d9bd960ff4ebdffd3407ca92014`
**parse_path:** `sentence`

> A large red soccer ball sculpture stands in a city square. A cyclist rides past it, while two people stand nearby on the paved ground. A building with “KUMHO TYRES” signage is visible in the background.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “KUMHO TYRES” | kumho_tyres | quote_text | doc_quote | 30 | high |
| m1 | object | sculpture | sculpture | noun_chunk_root | chunk0 | 4 | high |
| m2 | attribute | large | large | size_attribute | chunk0 | 1 | high |
| m3 | attribute | red | red | color_attribute | chunk0 | 2 | high |
| m4 | attribute | soccer ball | soccer_ball | compound_modifier | chunk0 | 3 | medium |
| m5 | object | square | square | noun_chunk_root | chunk1 | 9 | high |
| m6 | attribute | city | city | compound_modifier | chunk1 | 8 | medium |
| m7 | object | cyclist | cyclist | noun_chunk_root | chunk2 | 12 | high |
| m8 | object | people | people | noun_chunk_root | chunk4 | 19 | high |
| m9 | quantity | two | two | exact_quantity | chunk4 | 18 | high |
| m10 | object | ground | ground | noun_chunk_root | chunk5 | 25 | high |
| m11 | attribute | paved | paved | visual_attribute | chunk5 | 24 | medium |
| m12 | object | building | building | noun_chunk_root | chunk6 | 28 | high |
| m13 | object | signage | signage | noun_chunk_root | chunk7 | 31 | high |
| m14 | context | background | background | scene_context | chunk8 | 36 | high |
| m15 | action | stands | stand | verb_predicate | doc | 5 | high |
| m16 | action | rides | rid | verb_predicate | doc | 13 | high |
| m17 | action | stand | stand | verb_predicate | doc | 20 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk0 amod -> sculpture |
| e1 | has_attribute | m1 | m3 | high | chunk0 amod -> sculpture |
| e2 | has_attribute | m1 | m4 | medium | chunk0 compound -> sculpture |
| e3 | has_attribute | m5 | m6 | medium | chunk1 compound -> square |
| e4 | has_quantity | m8 | m9 | high | chunk4 quantity -> people |
| e5 | has_attribute | m10 | m11 | medium | chunk5 amod -> ground |
| e6 | has_attribute | m13 | m0 | high | chunk7 nmod -> signage |
| e7 | has_context | scene | m14 | high | scene_context token background |
| e8 | agent | m15 | m1 | medium | nsubj -> stands |
| e9 | agent | m16 | m7 | medium | nsubj -> rides |
| e10 | agent | m17 | m8 | medium | nsubj -> stand |
| e11 | relation | m1 | m5 | high | in |
| e12 | relation | m7 | m1 | medium | past |
| e13 | relation | m8 | m10 | high | on |
| e14 | relation | m12 | m13 | high | with |
| e15 | relation | m12 | m14 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | sculpture | sculpture | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:sculpture", "parents": []} |
| ent_m5 | object | square | square | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:square", "parents": []} |
| ent_m7 | object | cyclist | cyclist | object | raw_lemma | none |  | m7 | raw_mention |  |  |  | True | {"canonical": "entity:cyclist", "parents": []} |
| ent_m8 | object | people | people | person | raw_lemma | stage9_seed:parent_seed | person, human | m8 | raw_mention |  |  |  | True | {"canonical": "entity:people", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m10 | object | ground | ground | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:ground", "parents": []} |
| ent_m12 | object | building | building | object | raw_lemma | wordnet_synset:building.n.01 + stage9_audit | structure, artifact | m12 | raw_mention |  |  |  | True | {"canonical": "entity:building", "parents": ["entity_parent:structure", "entity_parent:artifact"]} |
| ent_m13 | object | signage | signage | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:signage", "parents": []} |
| ent_m14 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m14 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m15 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m16 | rides | rid | rid | raw_action | visual_action_fallback | visual_action |  | agent:m7->ent_m7 | {"canonical": "action:rid", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m17 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m8->ent_m8 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m1 | ent_m1 | medium | e8 | nsubj -> stands |  |  |
| ce1 | rid | agent | agent | none | m7 | ent_m7 | medium | e9 | nsubj -> rides |  |  |
| ce2 | stand | agent | agent | none | m8 | ent_m8 | medium | e10 | nsubj -> stand |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m5 | ent_m1 | ent_m5 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e11 | False | False |  |  |
| cr1 | m7 | m1 | ent_m7 | ent_m1 | past | past | raw_relation | raw_relation | visual_relation | medium | e12 | False | False |  |  |
| cr2 | m8 | m10 | ent_m8 | ent_m10 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e13 | False | False |  |  |
| cr3 | m12 | m13 | ent_m12 | ent_m13 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr4 | m12 | m14 | ent_m12 | ent_m14 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e15 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | sculpture |  |  |  | entity_exists:sculpture | True | low |
| cf1 | entity_exists | square |  |  |  | entity_exists:square | True | low |
| cf2 | entity_exists | cyclist |  |  |  | entity_exists:cyclist | True | low |
| cf3 | entity_exists | people |  |  | person, human | entity_exists:people | True | high |
| cf4 | entity_exists | ground |  |  |  | entity_exists:ground | True | low |
| cf5 | entity_exists | building |  |  | structure, artifact | entity_exists:building | True | high |
| cf6 | entity_exists | signage |  |  |  | entity_exists:signage | True | low |
| cf7 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf8 | has_attribute | sculpture | large |  | size_attribute, clean_exact_overlap, size, visual_attribute | has_attribute:sculpture:large | True | high |
| cf9 | has_attribute | sculpture | red |  | color_attribute, color, visual_attribute | has_attribute:sculpture:red | True | high |
| cf10 | has_attribute | sculpture | soccer_ball |  | compound_modifier, visual_attribute | has_attribute:sculpture:soccer_ball | True | medium |
| cf11 | has_attribute | square | city |  | compound_modifier, visual_attribute | has_attribute:square:city | True | medium |
| cf12 | has_quantity | people | two |  | exact_quantity, quantity | has_quantity:people:two | True | high |
| cf13 | has_attribute | ground | paved |  | visual_attribute | has_attribute:ground:paved | True | medium |
| cf14 | has_attribute | signage | kumho_tyres |  | quote_text, visual_attribute | has_attribute:signage:kumho_tyres | True | high |
| cf15 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf16 | event_role | stand | agent | sculpture |  | event_role:stand:agent:sculpture | True | medium |
| cf17 | action_event | rid |  |  | visual_action | action_event:rid | True | low |
| cf18 | event_role | rid | agent | cyclist |  | event_role:rid:agent:cyclist | True | medium |
| cf19 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf20 | event_role | stand | agent | people |  | event_role:stand:agent:people | True | medium |
| cf21 | relation | sculpture | in | square | spatial_containment, visual_relation | relation:sculpture:in:square | True | high |
| cf22 | relation | cyclist | past | sculpture | visual_relation | relation:cyclist:past:sculpture | True | medium |
| cf23 | relation | people | on | ground | spatial_support, visual_relation | relation:people:on:ground | True | high |
| cf24 | relation | building | with | signage | association_relation, visual_relation | relation:building:with:signage | True | high |
| cf25 | relation | building | in | background | spatial_containment, visual_relation | relation:building:in:background | True | high |

### Stage 9 Canonicalization Notes
_none_

## 98

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `55dddc3d49fd44a5859b513b8085c5af68c0ee8b9ee9f1b11d23915105d6c014`
**parse_path:** `sentence`

> An older woman with glasses stands at a microphone, wearing a red embroidered vest over a dark shirt. She is in a room with ornate gold decorations and patterned screens behind her, facing an audience whose heads are visible in the foreground.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | noun_chunk_root | chunk0 | 2 | high |
| m1 | attribute | older | old | visual_attribute | chunk0 | 1 | medium |
| m2 | object | glasses | glass | noun_chunk_root | chunk1 | 4 | high |
| m3 | object | microphone | microphone | noun_chunk_root | chunk2 | 8 | high |
| m4 | object | vest | vest | noun_chunk_root | chunk3 | 14 | high |
| m5 | attribute | red | red | color_attribute | chunk3 | 12 | high |
| m6 | attribute | embroidered | embroidered | modifier_attribute | chunk3 | 13 | medium |
| m7 | object | shirt | shirt | noun_chunk_root | chunk4 | 18 | high |
| m8 | attribute | dark | dark | visual_attribute | chunk4 | 17 | medium |
| m9 | object | room | room | noun_chunk_root | chunk6 | 24 | high |
| m10 | object | decorations | decoration | noun_chunk_root | chunk7 | 28 | high |
| m11 | attribute | ornate | ornate | modifier_attribute | chunk7 | 26 | medium |
| m12 | attribute | gold | gold | color_attribute | chunk7 | 27 | high |
| m13 | object | screens | screen | noun_chunk_root | chunk8 | 31 | high |
| m14 | attribute | patterned | patterned | modifier_attribute | chunk8 | 30 | medium |
| m15 | object | audience | audience | noun_chunk_root | chunk10 | 37 | high |
| m16 | object | heads | head | noun_chunk_root | chunk11 | 39 | high |
| m17 | context | foreground | foreground | scene_context | chunk12 | 44 | high |
| m18 | action | stands | stand | verb_predicate | doc | 5 | high |
| m19 | action | wearing | wear | verb_predicate | doc | 10 | high |
| m20 | action | facing | face | verb_predicate | doc | 35 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> woman |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> vest |
| e2 | has_attribute | m4 | m6 | medium | chunk3 amod -> vest |
| e3 | has_attribute | m7 | m8 | medium | chunk4 amod -> shirt |
| e4 | has_attribute | m10 | m11 | medium | chunk7 amod -> decorations |
| e5 | has_attribute | m10 | m12 | high | chunk7 amod -> decorations |
| e6 | has_attribute | m13 | m14 | medium | chunk8 amod -> screens |
| e7 | has_context | scene | m17 | high | scene_context token foreground |
| e8 | agent | m18 | m0 | medium | nsubj -> stands |
| e9 | agent | m19 | m0 | medium | inherited agent advcl -> stands |
| e10 | patient | m19 | m4 | medium | dobj -> wearing |
| e11 | agent | m20 | m0 | medium | inherited agent advcl -> is |
| e12 | patient | m20 | m15 | medium | dobj -> facing |
| e13 | relation | m0 | m2 | high | with |
| e14 | relation | m0 | m3 | medium | at |
| e15 | relation | m0 | m7 | high | over |
| e16 | relation | m0 | m9 | high | in |
| e17 | relation | m9 | m10 | high | with |
| e18 | relation | m9 | m13 | high | with |
| e19 | relation | m10 | m0 | high | behind |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | raw_lemma | stage9_seed:parent_seed | person, human | m0 | raw_mention |  |  |  | True | {"canonical": "entity:woman", "parents": ["entity_parent:person", "entity_parent:human"]} |
| ent_m2 | object | glass | glasses | object | raw_lemma | none |  | m2 | raw_mention |  |  |  | True | {"canonical": "entity:glass", "parents": []} |
| ent_m3 | object | microphone | microphone | object | raw_lemma | none |  | m3 | raw_mention |  |  |  | True | {"canonical": "entity:microphone", "parents": []} |
| ent_m4 | object | vest | vest | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m4 | raw_mention |  |  |  | True | {"canonical": "entity:vest", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m7 | object | shirt | shirt | clothing | raw_lemma | stage9_seed:parent_seed | clothing, wearable | m7 | raw_mention |  |  |  | True | {"canonical": "entity:shirt", "parents": ["entity_parent:clothing", "entity_parent:wearable"]} |
| ent_m9 | object | room | room | object | raw_lemma | wordnet_synset:room.n.01 + stage9_audit | interior_place, place | m9 | raw_mention |  |  |  | True | {"canonical": "entity:room", "parents": ["entity_parent:interior_place", "entity_parent:place"]} |
| ent_m10 | object | decoration | decorations | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:decoration", "parents": []} |
| ent_m13 | object | screen | screens | device | raw_lemma | stage9_seed:parent_seed | device, artifact | m13 | raw_mention |  |  |  | True | {"canonical": "entity:screen", "parents": ["entity_parent:device", "entity_parent:artifact"]} |
| ent_m15 | object | audience | audience | object | raw_lemma | none |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:audience", "parents": []} |
| ent_m16 | object | head | heads | object | raw_lemma | stage9_seed:parent_seed | body_part | m16 | raw_mention |  |  |  | True | {"canonical": "entity:head", "parents": ["entity_parent:body_part"]} |
| ent_m17 | context | foreground | foreground | object | raw_lemma | stage9_seed:parent_seed | scene_context | m17 | raw_mention |  |  |  | True | {"canonical": "entity:foreground", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | stands | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m19 | wearing | wear | wear | raw_action | stage9_seed:parent_seed | wearing_action, visual_action |  | agent:m0->ent_m0; patient:m4->ent_m4 | {"canonical": "action:wear", "parents": ["action_parent:wearing_action", "action_parent:visual_action"]} |  |
| ce2 | m20 | facing | face | face | raw_action | stage9_seed:parent_seed | orientation_action, visual_action |  | agent:m0->ent_m0; patient:m15->ent_m15 | {"canonical": "action:face", "parents": ["action_parent:orientation_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e8 | nsubj -> stands |  |  |
| ce1 | wear | agent | agent | none | m0 | ent_m0 | medium | e9 | inherited agent advcl -> stands |  |  |
| ce1 | wear | patient | patient | none | m4 | ent_m4 | medium | e10 | dobj -> wearing |  |  |
| ce2 | face | agent | agent | none | m0 | ent_m0 | medium | e11 | inherited agent advcl -> is |  |  |
| ce2 | face | patient | patient | none | m15 | ent_m15 | medium | e12 | dobj -> facing |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e13 | False | False |  |  |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | at | at | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_location, visual_relation | medium | e14 | False | False |  |  |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | over | above | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_vertical, visual_relation | high | e15 | False | False |  |  |
| cr3 | m0 | m9 | ent_m0 | ent_m9 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e16 | False | False |  |  |
| cr4 | m9 | m10 | ent_m9 | ent_m10 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e17 | False | False |  |  |
| cr5 | m9 | m13 | ent_m9 | ent_m13 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e18 | False | False |  |  |
| cr6 | m10 | m0 | ent_m10 | ent_m0 | behind | behind | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_depth, visual_relation | high | e19 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | woman |  |  | person, human | entity_exists:woman | True | high |
| cf1 | entity_exists | glass |  |  |  | entity_exists:glass | True | low |
| cf2 | entity_exists | microphone |  |  |  | entity_exists:microphone | True | low |
| cf3 | entity_exists | vest |  |  | clothing, wearable | entity_exists:vest | True | high |
| cf4 | entity_exists | shirt |  |  | clothing, wearable | entity_exists:shirt | True | high |
| cf5 | entity_exists | room |  |  | interior_place, place | entity_exists:room | True | high |
| cf6 | entity_exists | decoration |  |  |  | entity_exists:decoration | True | low |
| cf7 | entity_exists | screen |  |  | device, artifact | entity_exists:screen | True | high |
| cf8 | entity_exists | audience |  |  |  | entity_exists:audience | True | low |
| cf9 | entity_exists | head |  |  | body_part | entity_exists:head | True | high |
| cf10 | entity_exists | foreground |  |  | scene_context | entity_exists:foreground | True | high |
| cf11 | has_attribute | woman | old |  | condition_attribute, clean_exact_overlap, maturity, newness, visual_attribute | has_attribute:woman:old | True | medium |
| cf12 | has_attribute | vest | red |  | color_attribute, color, visual_attribute | has_attribute:vest:red | True | high |
| cf13 | has_attribute | vest | embroidered |  | modifier_attribute, visual_attribute | has_attribute:vest:embroidered | True | medium |
| cf14 | has_attribute | shirt | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:shirt:dark | True | medium |
| cf15 | has_attribute | decoration | ornate |  | modifier_attribute, visual_attribute | has_attribute:decoration:ornate | True | medium |
| cf16 | has_attribute | decoration | gold |  | color_attribute, color, visual_attribute | has_attribute:decoration:gold | True | high |
| cf17 | has_attribute | screen | patterned |  | pattern_attribute, pattern, visual_attribute | has_attribute:screen:patterned | True | medium |
| cf18 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf19 | event_role | stand | agent | woman |  | event_role:stand:agent:woman | True | medium |
| cf20 | action_event | wear |  |  | wearing_action, visual_action | action_event:wear | True | high |
| cf21 | event_role | wear | agent | woman |  | event_role:wear:agent:woman | True | medium |
| cf22 | event_role | wear | patient | vest |  | event_role:wear:patient:vest | True | medium |
| cf23 | action_event | face |  |  | orientation_action, visual_action | action_event:face | True | high |
| cf24 | event_role | face | agent | woman |  | event_role:face:agent:woman | True | medium |
| cf25 | event_role | face | patient | audience |  | event_role:face:patient:audience | True | medium |
| cf26 | relation | woman | with | glass | association_relation, visual_relation | relation:woman:with:glass | True | high |
| cf27 | relation | woman | at | microphone | spatial_location, visual_relation | relation:woman:at:microphone | True | medium |
| cf28 | relation | woman | above | shirt | spatial_vertical, visual_relation | relation:woman:above:shirt | True | high |
| cf29 | relation | woman | in | room | spatial_containment, visual_relation | relation:woman:in:room | True | high |
| cf30 | relation | room | with | decoration | association_relation, visual_relation | relation:room:with:decoration | True | high |
| cf31 | relation | room | with | screen | association_relation, visual_relation | relation:room:with:screen | True | high |
| cf32 | relation | decoration | behind | woman | spatial_depth, visual_relation | relation:decoration:behind:woman | True | high |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| relation_lexical_canonicalized |  | e15 |  |  |  | {"canonical": "above", "kind": "relation_lexical_canonicalized", "raw_edge_id": "e15", "raw_relation": "over", "source": "manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count"} |

## 99

**caption_shape:** `multi-sentence`
**caption_type:** `medium`
**caption_id:** `56394a3bf104dce8ae42e18ea11b584da54999152e7a0a6fec3be5ffda619814`
**parse_path:** `sentence`

> A silver watch case rests on a gray, round surface. The case has a textured bezel and engraved markings, placed on a green workbench with tools and objects in the background. A date stamp “25 11 2015” is visible in the corner.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “25 11 2015” | 25_11_2015 | quote_text | doc_quote | 38 | high |
| m1 | object | case | case | noun_chunk_root | chunk0 | 3 | high |
| m2 | attribute | silver | silver | color_attribute | chunk0 | 1 | high |
| m3 | attribute | watch | watch | compound_modifier | chunk0 | 2 | medium |
| m4 | context | surface | surface | spatial_region | chunk1 | 10 | medium |
| m5 | object | case | case | noun_chunk_root | chunk2 | 13 | high |
| m6 | object | bezel | bezel | noun_chunk_root | chunk3 | 17 | high |
| m7 | attribute | textured | textured | modifier_attribute | chunk3 | 16 | medium |
| m8 | object | markings | marking | noun_chunk_root | chunk4 | 20 | high |
| m9 | attribute | engraved | engrave | state_attribute | chunk4 | 19 | medium |
| m10 | object | workbench | workbench | noun_chunk_root | chunk5 | 26 | high |
| m11 | attribute | green | green | color_attribute | chunk5 | 25 | high |
| m12 | object | tools | tool | noun_chunk_root | chunk6 | 28 | high |
| m13 | object | objects | object | noun_chunk_root | chunk7 | 30 | high |
| m14 | context | background | background | scene_context | chunk8 | 33 | high |
| m15 | object | stamp | stamp | noun_chunk_root | chunk9 | 37 | high |
| m16 | attribute | date | date | compound_modifier | chunk9 | 36 | medium |
| m17 | context | corner | corner | spatial_region | chunk10 | 43 | medium |
| m18 | action | rests | rest | verb_predicate | doc | 4 | high |
| m19 | action | has | have | verb_predicate | doc | 14 | high |
| m20 | action | placed | place | verb_predicate | doc | 22 | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk0 compound -> case |
| e1 | has_attribute | m1 | m3 | medium | chunk0 compound -> case |
| e2 | has_attribute | m6 | m7 | medium | chunk3 amod -> bezel |
| e3 | has_attribute | m8 | m9 | medium | chunk4 amod -> markings |
| e4 | has_attribute | m10 | m11 | high | chunk5 amod -> workbench |
| e5 | has_context | scene | m14 | high | scene_context token background |
| e6 | has_attribute | m15 | m16 | medium | chunk9 compound -> stamp |
| e7 | agent | m18 | m1 | medium | nsubj -> rests |
| e8 | agent | m19 | m5 | medium | nsubj -> has |
| e9 | patient | m19 | m6 | medium | dobj -> has |
| e10 | patient | m19 | m8 | medium | dobj -> has |
| e11 | agent | m20 | m6 | medium | inherited agent acl -> bezel |
| e12 | relation | m1 | m4 | high | on |
| e13 | relation | m6 | m10 | high | on |
| e14 | relation | m10 | m12 | high | with |
| e15 | relation | m10 | m13 | high | with |
| e16 | relation | m12 | m14 | high | in |
| e17 | relation | m15 | m17 | high | in |

### Skipped Raw Concept Edges
_none_

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | case | case | object | raw_lemma | none |  | m1 | raw_mention |  |  |  | True | {"canonical": "entity:case", "parents": []} |
| ent_m4 | context | surface | surface | object | raw_lemma | semantic_type_fallback | scene_context | m4 | raw_mention |  |  |  | True | {"canonical": "entity:surface", "parents": ["entity_parent:scene_context"]} |
| ent_m5 | object | case | case | object | raw_lemma | none |  | m5 | raw_mention |  |  |  | True | {"canonical": "entity:case", "parents": []} |
| ent_m6 | object | bezel | bezel | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:bezel", "parents": []} |
| ent_m8 | object | marking | markings | object | raw_lemma | none |  | m8 | raw_mention |  |  |  | True | {"canonical": "entity:marking", "parents": []} |
| ent_m10 | object | workbench | workbench | object | raw_lemma | none |  | m10 | raw_mention |  |  |  | True | {"canonical": "entity:workbench", "parents": []} |
| ent_m12 | object | tool | tools | object | raw_lemma | none |  | m12 | raw_mention |  |  |  | True | {"canonical": "entity:tool", "parents": []} |
| ent_m13 | object | object | objects | object | raw_lemma | none |  | m13 | raw_mention |  |  |  | True | {"canonical": "entity:object", "parents": []} |
| ent_m14 | context | background | background | object | raw_lemma | stage9_seed:parent_seed | scene_context | m14 | raw_mention |  |  |  | True | {"canonical": "entity:background", "parents": ["entity_parent:scene_context"]} |
| ent_m15 | object | stamp | stamp | object | raw_lemma | none |  | m15 | raw_mention |  |  |  | True | {"canonical": "entity:stamp", "parents": []} |
| ent_m17 | context | corner | corner | object | raw_lemma | semantic_type_fallback | scene_context | m17 | raw_mention |  |  |  | True | {"canonical": "entity:corner", "parents": ["entity_parent:scene_context"]} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | rests | rest | rest | raw_action | wordnet_synset:rest.v.01 + stage9_audit | support_state_action, visual_action |  | agent:m1->ent_m1 | {"canonical": "action:rest", "parents": ["action_parent:support_state_action", "action_parent:visual_action"]} |  |
| ce1 | m19 | has | have | have | raw_action | visual_action_fallback | visual_action |  | agent:m5->ent_m5; patient:m6->ent_m6; patient:m8->ent_m8 | {"canonical": "action:have", "parents": ["action_parent:visual_action"]} |  |
| ce2 | m20 | placed | place | place | raw_action | wordnet_synset:put.v.01 + stage9_audit | placement_action, visual_action |  | agent:m6->ent_m6 | {"canonical": "action:place", "parents": ["action_parent:placement_action", "action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | rest | agent | agent | none | m1 | ent_m1 | medium | e7 | nsubj -> rests |  |  |
| ce1 | have | agent | agent | none | m5 | ent_m5 | medium | e8 | nsubj -> has |  |  |
| ce1 | have | patient | patient | none | m6 | ent_m6 | medium | e9 | dobj -> has |  |  |
| ce1 | have | patient | patient | none | m8 | ent_m8 | medium | e10 | dobj -> has |  |  |
| ce2 | place | agent | agent | none | m6 | ent_m6 | medium | e11 | inherited agent acl -> bezel |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m4 | ent_m1 | ent_m4 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e12 | False | False |  |  |
| cr1 | m6 | m10 | ent_m6 | ent_m10 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e13 | False | False |  |  |
| cr2 | m10 | m12 | ent_m10 | ent_m12 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e14 | False | False |  |  |
| cr3 | m10 | m13 | ent_m10 | ent_m13 | with | with | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | association_relation, visual_relation | high | e15 | False | False |  |  |
| cr4 | m12 | m14 | ent_m12 | ent_m14 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e16 | False | False |  |  |
| cr5 | m15 | m17 | ent_m15 | ent_m17 | in | in | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_containment, visual_relation | high | e17 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | case |  |  |  | entity_exists:case | True | low |
| cf1 | entity_exists | surface |  |  | scene_context | entity_exists:surface | True | medium |
| cf2 | entity_exists | case |  |  |  | entity_exists:case | True | low |
| cf3 | entity_exists | bezel |  |  |  | entity_exists:bezel | True | low |
| cf4 | entity_exists | marking |  |  |  | entity_exists:marking | True | low |
| cf5 | entity_exists | workbench |  |  |  | entity_exists:workbench | True | low |
| cf6 | entity_exists | tool |  |  |  | entity_exists:tool | True | low |
| cf7 | entity_exists | object |  |  |  | entity_exists:object | True | low |
| cf8 | entity_exists | background |  |  | scene_context | entity_exists:background | True | high |
| cf9 | entity_exists | stamp |  |  |  | entity_exists:stamp | True | low |
| cf10 | entity_exists | corner |  |  | scene_context | entity_exists:corner | True | medium |
| cf11 | has_attribute | case | silver |  | color_attribute, color, material, visual_attribute | has_attribute:case:silver | True | high |
| cf12 | has_attribute | case | watch |  | compound_modifier, visual_attribute | has_attribute:case:watch | True | medium |
| cf13 | has_attribute | bezel | textured |  | texture_attribute, texture, visual_attribute | has_attribute:bezel:textured | True | medium |
| cf14 | has_attribute | marking | engrave |  | state_attribute, visual_attribute | has_attribute:marking:engrave | True | medium |
| cf15 | has_attribute | workbench | green |  | color_attribute, color, visual_attribute | has_attribute:workbench:green | True | high |
| cf16 | has_attribute | stamp | date |  | compound_modifier, visual_attribute | has_attribute:stamp:date | True | medium |
| cf17 | action_event | rest |  |  | support_state_action, visual_action | action_event:rest | True | medium |
| cf18 | event_role | rest | agent | case |  | event_role:rest:agent:case | True | medium |
| cf19 | action_event | have |  |  | visual_action | action_event:have | True | low |
| cf20 | event_role | have | agent | case |  | event_role:have:agent:case | True | medium |
| cf21 | event_role | have | patient | bezel |  | event_role:have:patient:bezel | True | medium |
| cf22 | event_role | have | patient | marking |  | event_role:have:patient:marking | True | medium |
| cf23 | action_event | place |  |  | placement_action, visual_action | action_event:place | True | high |
| cf24 | event_role | place | agent | bezel |  | event_role:place:agent:bezel | True | medium |
| cf25 | relation | case | on | surface | spatial_support, visual_relation | relation:case:on:surface | True | high |
| cf26 | relation | bezel | on | workbench | spatial_support, visual_relation | relation:bezel:on:workbench | True | high |
| cf27 | relation | workbench | with | tool | association_relation, visual_relation | relation:workbench:with:tool | True | high |
| cf28 | relation | workbench | with | object | association_relation, visual_relation | relation:workbench:with:object | True | high |
| cf29 | relation | tool | in | background | spatial_containment, visual_relation | relation:tool:in:background | True | high |
| cf30 | relation | stamp | in | corner | spatial_containment, visual_relation | relation:stamp:in:corner | True | high |

### Stage 9 Canonicalization Notes
_none_

## 100

**caption_shape:** `sentence-like`
**caption_type:** `short`
**caption_id:** `5737eff6d3296cc3dd74029d983f367c3b201cd8f176641e0d0738427cf55814`
**parse_path:** `sentence`

> Two stone statues stand on either side of a dark doorway with steps leading up to it.

### Raw Concept Mentions
| id | type | text | lemma | role | source_tag | source_token | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | statues | statue | noun_chunk_root | chunk0 | 2 | high |
| m1 | quantity | Two | two | exact_quantity | chunk0 | 0 | high |
| m2 | attribute | stone | stone | material_attribute | chunk0 | 1 | high |
| m3 | context | side | side | spatial_region | chunk1 | 6 | medium |
| m4 | object | doorway | doorway | noun_chunk_root | chunk2 | 10 | high |
| m5 | attribute | dark | dark | visual_attribute | chunk2 | 9 | medium |
| m6 | object | steps | step | noun_chunk_root | chunk3 | 12 | high |
| m7 | action | stand | stand | verb_predicate | doc | 3 | high |
| m8 | action | leading | lead | verb_predicate | doc | 13 | high |
| m9 | particle | up | up | phrasal_particle | action_particle | 14 | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 quantity -> statues |
| e1 | has_attribute | m0 | m2 | high | chunk0 compound -> statues |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> doorway |
| e3 | agent | m7 | m0 | medium | nsubj -> stand |
| e4 | agent | m8 | m6 | medium | nsubj -> leading |
| e5 | has_particle | m8 | m9 | medium | prt -> leading |
| e6 | relation | m0 | m3 | high | on |
| e7 | relation | m3 | m4 | medium | of |

### Skipped Raw Concept Edges
| type | source | target | confidence | reason | evidence |
| --- | --- | --- | --- | --- | --- |
| relation | m6 | m6 | medium | self_edge_after_coref | to |

### Stage 9 Canonical Entities
| entity_id | entity_type | canonical_lemma | text | semantic_type | canonical_source | parent_source | parent_chain | raw_mentions | source | parent_entity | member_entities | cardinality | count_eligible | count_keys |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | statue | statues | object | raw_lemma | none |  | m0 | raw_mention |  |  |  | True | {"canonical": "entity:statue", "parents": []} |
| ent_m3 | context | side | side | object | raw_lemma | semantic_type_fallback | scene_context | m3 | raw_mention |  |  |  | True | {"canonical": "entity:side", "parents": ["entity_parent:scene_context"]} |
| ent_m4 | object | doorway | doorway | object | raw_lemma | none |  | m4 | raw_mention |  |  |  | True | {"canonical": "entity:doorway", "parents": []} |
| ent_m6 | object | step | steps | object | raw_lemma | none |  | m6 | raw_mention |  |  |  | True | {"canonical": "entity:step", "parents": []} |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | canonical_source | parent_source | action_parent_chain | particles | roles_summary | count_keys | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | stand | stand | stand | raw_action | stage9_seed:parent_seed | body_pose_action, visual_action |  | agent:m0->ent_m0 | {"canonical": "action:stand", "parents": ["action_parent:body_pose_action", "action_parent:visual_action"]} |  |
| ce1 | m8 | leading | lead | lead | raw_action | visual_action_fallback | visual_action | up | agent:m6->ent_m6 | {"canonical": "action:lead", "parents": ["action_parent:visual_action"]} |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_role | voice_normalization | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | agent | none | m0 | ent_m0 | medium | e3 | nsubj -> stand |  |  |
| ce1 | lead | agent | agent | none | m6 | ent_m6 | medium | e4 | nsubj -> leading |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | raw_relation | relation | relation_canonical_source | relation_parent_source | relation_parent_chain | confidence | raw_edge | consumed_by_event | self_after_canonicalization | source_selection | selection_reason |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | on | on | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|openimages_relationship_triplet\|visual_genome_relationship_alias\|visual_genome_relationship_count | spatial_support, visual_relation | high | e6 | False | False |  |  |
| cr1 | m3 | m4 | ent_m3 | ent_m4 | of | of | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | manual_relation_seed\|visual_genome_relationship_alias\|visual_genome_relationship_count | part_relation, visual_relation | medium | e7 | False | False |  |  |

### Stage 9 Canonical Facts
| fact_id | fact_type | source/action/canonical | relation/role/value | target | parent_chain | count_key | count_eligible | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cf0 | entity_exists | statue |  |  |  | entity_exists:statue | True | low |
| cf1 | entity_exists | side |  |  | scene_context | entity_exists:side | True | medium |
| cf2 | entity_exists | doorway |  |  |  | entity_exists:doorway | True | low |
| cf3 | entity_exists | step |  |  |  | entity_exists:step | True | low |
| cf4 | has_quantity | statue | two |  | exact_quantity, quantity | has_quantity:statue:two | True | high |
| cf5 | has_attribute | statue | stone |  | material_attribute, material, visual_attribute | has_attribute:statue:stone | True | high |
| cf6 | has_attribute | doorway | dark |  | brightness_attribute, brightness, tone, visual_attribute | has_attribute:doorway:dark | True | medium |
| cf7 | action_event | stand |  |  | body_pose_action, visual_action | action_event:stand | True | high |
| cf8 | event_role | stand | agent | statue |  | event_role:stand:agent:statue | True | medium |
| cf9 | action_event | lead |  |  | visual_action | action_event:lead | True | low |
| cf10 | event_role | lead | agent | step |  | event_role:lead:agent:step | True | medium |
| cf11 | relation | statue | on | side | spatial_support, visual_relation | relation:statue:on:side | True | high |
| cf12 | relation | side | of | doorway | part_relation, visual_relation | relation:side:of:doorway | True | medium |

### Stage 9 Canonicalization Notes
_none_
