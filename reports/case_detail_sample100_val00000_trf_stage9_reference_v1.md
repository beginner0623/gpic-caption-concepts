# Stage 9 Reference v1 Case Detail - sample100 val00000

- input: `reports\canonical_concepts_sample100_val00000_trf_stage9_reference_v1.jsonl`
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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | dreadlock | dreadlocks | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | bow | bow | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | table | table | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | poster | posters | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | sticker | stickers | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | sits | sit | sit |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m0 | ent_m0 | medium | e2 | nsubj -> sits |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | high | e3 | False | False |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | with | high | e4 | False | False |
| cr2 | m0 | m4 | ent_m0 | ent_m4 | at | medium | e5 | False | False |
| cr3 | m0 | m5 | ent_m0 | ent_m5 | with | high | e6 | False | False |
| cr4 | m0 | m7 | ent_m0 | ent_m7 | with | high | e7 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | insect | insect | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | wing | wings | object | m2 | raw_mention |  |  |  |
| ent_m3 | context | surface | surface | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | wood | wood | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | sign | signs | document | m5 | raw_mention |  |  |  |
| ent_m6 | object | age | age | object | m6 | raw_mention |  |  |  |
| ent_m7 | object | split | splits | object | m7 | raw_mention |  |  |  |
| ent_m9 | object | bit | bits | object | m9 | raw_mention |  |  |  |
| ent_m11 | object | debris | debris | object | m11 | raw_mention |  |  |  |
| ent_m12 | context | scene | scene | object | m12 | raw_mention |  |  |  |
| ent_m13 | object | floor | floor | object | m13 | raw_mention |  |  |  |
| ent_m15 | object | tree_trunk | tree trunk | object | m15 | raw_mention |  |  |  |
| ent_m17 | context | outdoors | outdoors | object | m17 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | crawling | crawl | crawl |  | agent:m0->ent_m0 |  |
| ce1 | m19 | shows | show | show |  | agent:m4->ent_m4; patient:m5->ent_m5 |  |
| ce2 | m20 | scattered | scatter | scatter |  | agent:m7->ent_m7 |  |
| ce3 | m21 | appears | appear | appear |  | agent:m12->ent_m12 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | crawl | agent | m0 | ent_m0 | medium | e7 | nsubj -> crawling |  |  |
| ce1 | show | agent | m4 | ent_m4 | medium | e8 | nsubj -> shows |  |  |
| ce1 | show | patient | m5 | ent_m5 | medium | e9 | dobj -> shows |  |  |
| ce2 | scatter | agent | m7 | ent_m7 | medium | e10 | inherited agent acl -> splits |  |  |
| ce3 | appear | agent | m12 | ent_m12 | medium | e11 | nsubj -> appears |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e12 | False | False |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | on | high | e13 | False | False |
| cr2 | m5 | m6 | ent_m5 | ent_m6 | of | medium | e14 | False | False |
| cr3 | m4 | m7 | ent_m4 | ent_m7 | with | high | e15 | False | False |
| cr4 | m4 | m9 | ent_m4 | ent_m9 | with | high | e16 | False | False |
| cr5 | m9 | m11 | ent_m9 | ent_m11 | of | medium | e17 | False | False |
| cr6 | m12 | m13 | ent_m12 | ent_m13 | on | high | e18 | False | False |
| cr7 | m12 | m15 | ent_m12 | ent_m15 | on | high | e19 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | woman | woman | person | m1 | raw_mention |  |  |  |
| ent_m2 | object | podium | podium | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | audience | audience | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | american_flag | American flag | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | screen | screen | device | m5 | raw_mention |  |  |  |
| ent_m6 | object | text | text | document | m6 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | stands | stand | stand |  | agent:m1->ent_m1 |  |
| ce1 | m8 | speaking | speak | speak |  | agent:m1->ent_m1 |  |
| ce2 | m9 | shows | show | show |  | agent:m5->ent_m5; patient:m6->ent_m6 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m1 | ent_m1 | medium | e1 | nsubj -> stands |  |  |
| ce1 | speak | agent | m1 | ent_m1 | medium | e2 | inherited agent advcl -> stands |  |  |
| ce2 | show | agent | m5 | ent_m5 | medium | e3 | nsubj -> shows |  |  |
| ce2 | show | patient | m6 | ent_m6 | medium | e4 | dobj -> shows |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | at | medium | e5 | False | False |
| cr1 | m1 | m3 | ent_m1 | ent_m3 | in_front_of | high | e6 | False | False |
| cr2 | m4 | m1 | ent_m4 | ent_m1 | behind | high | e7 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | shopping_cart | shopping cart | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | grocery | groceries | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | bag | bags | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | person | person | person | m5 | raw_mention |  |  |  |
| ent_m7 | object | bag | bag | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | stand | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m11 | filled | fill | fill |  | agent:m2->ent_m2 |  |
| ce2 | m12 | holds | hold | hold |  | agent:m5->ent_m5; patient:m7->ent_m7 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e4 | nsubj -> stand |  |  |
| ce1 | fill | agent | m2 | ent_m2 | medium | e5 | inherited agent acl -> shopping cart |  |  |
| ce2 | hold | agent | m5 | ent_m5 | medium | e6 | nsubj -> holds |  |  |
| ce2 | hold | patient | m7 | ent_m7 | medium | e7 | dobj -> holds |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e8 | False | False |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | with | high | e9 | False | False |
| cr2 | m2 | m4 | ent_m2 | ent_m4 | with | high | e10 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | flower | flowers | object | m0 | raw_mention |  |  |  |
| ent_m4 | object | bed | bed | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | grass | grass | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | bloom | blooms | object | m8 | raw_mention |  |  |  |
| ent_m10 | context | background | background | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | people | people | person | m11 | raw_mention |  |  |  |
| ent_m12 | object | fence | fence | object | m12 | raw_mention |  |  |  |
| ent_m14 | object | umbrella | umbrella | object | m14 | raw_mention |  |  |  |
| ent_m16 | object | tree | Trees | object | m16 | raw_mention |  |  |  |
| ent_m17 | object | structure | structure | object | m17 | raw_mention |  |  |  |
| ent_m19 | object | area | area | object | m19 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m21 | stand | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m22 | walk | walk | walk |  | agent:m11->ent_m11 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e11 | nsubj -> stand |  |  |
| ce1 | walk | agent | m11 | ent_m11 | medium | e12 | nsubj -> walk |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | in | high | e13 | False | False |
| cr1 | m4 | m6 | ent_m4 | ent_m6 | with | high | e14 | False | False |
| cr2 | m4 | m8 | ent_m4 | ent_m8 | with | high | e15 | False | False |
| cr3 | m11 | m10 | ent_m11 | ent_m10 | in | high | e16 | False | False |
| cr4 | m11 | m12 | ent_m11 | ent_m12 | near | high | e17 | False | False |
| cr5 | m11 | m14 | ent_m11 | ent_m14 | under | high | e18 | False | False |
| cr6 | m16 | m19 | ent_m16 | ent_m19 | beyond | high | e19 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | couple | couple | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | party | party | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | flag | flags | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | chandelier | chandelier | object | m6 | raw_mention |  |  |  |
| ent_m7 | object | wine_glass | wine glasses | object | m7 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | church | church | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | cross | cross | object | m2 | raw_mention |  |  |  |
| ent_m3 | context | top | top | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | step | steps | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | door | door | object | m6 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | has | have | have |  | agent:m0->ent_m0; patient:m4->ent_m4 |  |
| ce1 | m9 | leading | lead | lead |  | agent:m4->ent_m4 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | have | agent | m0 | ent_m0 | medium | e3 | nsubj -> has |  |  |
| ce0 | have | patient | m4 | ent_m4 | medium | e4 | dobj -> has |  |  |
| ce1 | lead | agent | m4 | ent_m4 | medium | e5 | inherited agent acl -> steps |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e6 | False | False |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | on | high | e7 | False | False |
| cr2 | m4 | m6 | ent_m4 | ent_m6 | to | medium | e8 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | poster | poster | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | trash_can | trash can | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | silhouette | silhouette | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | man | man | person | m5 | raw_mention |  |  |  |
| ent_m6 | object | hat | hat | object | m6 | raw_mention |  |  |  |
| ent_m7 | context | scene | scene | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | sidewalk | sidewalk | object | m8 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | reads | read | read |  | agent:m1->ent_m1; patient:m0->None |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | read | agent | m1 | ent_m1 | medium | e3 | nsubj -> reads |  |  |
| ce0 | read | patient | m0 |  | medium | e4 | dobj -> reads |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | on | high | e5 | False | False |
| cr1 | m1 | m4 | ent_m1 | ent_m4 | with | high | e6 | False | False |
| cr2 | m4 | m5 | ent_m4 | ent_m5 | of | medium | e7 | False | False |
| cr3 | m5 | m6 | ent_m5 | ent_m6 | in | high | e8 | False | False |
| cr4 | m7 | m8 | ent_m7 | ent_m8 | on | high | e9 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | child | child | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | hair | hair | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | hat | hat | object | m4 | raw_mention |  |  |  |
| ent_m8 | object | child | child | person | m8 | raw_mention |  |  |  |
| ent_m9 | object | window | window | object | m9 | raw_mention |  |  |  |
| ent_m10 | context | background | background | object | m10 | raw_mention |  |  |  |
| ent_m11 | context | indoors | indoors | object | m11 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | smiles | smile | smile |  | agent:m0->ent_m0 |  |
| ce1 | m13 | wearing | wear | wear |  | agent:m0->ent_m0; patient:m4->ent_m4 |  |
| ce2 | m14 | appears | appear | appear |  | agent:m8->ent_m8 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | smile | agent | m0 | ent_m0 | medium | e7 | nsubj -> smiles |  |  |
| ce1 | wear | agent | m0 | ent_m0 | medium | e8 | inherited agent advcl -> smiles |  |  |
| ce1 | wear | patient | m4 | ent_m4 | medium | e9 | dobj -> wearing |  |  |
| ce2 | appear | agent | m8 | ent_m8 | medium | e10 | inherited agent conj -> is |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e11 | False | False |
| cr1 | m8 | m9 | ent_m8 | ent_m9 | with | high | e12 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | skater | skaters | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | helmet | helmet | clothing | m2 | raw_mention |  |  |  |
| ent_m3 | object | referee | referee | person | m3 | raw_mention |  |  |  |
| ent_m4 | object | court | court | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | jersey | jersey | clothing | m5 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | building | object | m0 | raw_mention |  |  |  |
| ent_m3 | object | roof | roof | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | window | windows | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | street | street | object | m7 | raw_mention |  |  |  |
| ent_m9 | object | sedan | sedan | object | m9 | raw_mention |  |  |  |
| ent_m11 | context | front | front | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | bus | bus | vehicle | m12 | raw_mention |  |  |  |
| ent_m13 | object | road | road | object | m13 | raw_mention |  |  |  |
| ent_m14 | object | sky | sky | object | m14 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | stands | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m18 | parked | park | park |  | theme:m9->ent_m9 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e8 | nsubj -> stands |  |  |
| ce1 | park | theme | m9 | ent_m9 | medium | e9 | nsubjpass -> parked |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | with | high | e10 | False | False |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | with | high | e11 | False | False |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | on | high | e12 | False | False |
| cr3 | m9 | m11 | ent_m9 | ent_m11 | in | high | e13 | False | False |
| cr4 | m12 | m13 | ent_m12 | ent_m13 | down | medium | e14 | False | False |
| cr5 | m12 | m14 | ent_m12 | ent_m14 | under | high | e15 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | shirt | shirt | clothing | m1 | raw_mention |  |  |  |
| ent_m3 | object | basketball | basketball | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | head | head | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | court | court | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | people | people | person | m7 | raw_mention |  |  |  |
| ent_m9 | object | shirt | shirts | clothing | m9 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | holds | hold | hold |  | agent:m0->ent_m0; patient:m3->ent_m3 |  |
| ce1 | m13 | play | play | play |  | agent:m7->ent_m7 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | hold | agent | m0 | ent_m0 | medium | e5 | nsubj -> holds |  |  |
| ce0 | hold | patient | m3 | ent_m3 | medium | e6 | dobj -> holds |  |  |
| ce1 | play | agent | m7 | ent_m7 | medium | e7 | nsubj -> play |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e8 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | above | high | e9 | False | False |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | on | high | e10 | False | False |
| cr3 | m7 | m9 | ent_m7 | ent_m9 | in | high | e11 | False | False |

### Stage 9 Canonicalization Notes
_none_

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | landscape | landscape | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | mountain | mountains | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | sky | sky | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | object | object | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | ground | ground | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | sits | sit | sit |  | agent:m5->ent_m5 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m5 | ent_m5 | medium | e5 | nsubj -> sits |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e6 | False | False |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | under | high | e7 | False | False |
| cr2 | m5 | m7 | ent_m5 | ent_m7 | on | high | e8 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | boot | boot | object | m0 | raw_mention |  |  |  |
| ent_m2 | context | indoor | indoor | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | wall | wall | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | display | display | object | m5 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | men | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | camera | camera | device | m2 | raw_mention |  |  |  |
| ent_m3 | object | bathroom | bathroom | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | vest | vest | clothing | m4 | raw_mention |  |  |  |
| ent_m5 | object | scarf | scarf | clothing | m5 | raw_mention |  |  |  |
| eref_m7 | instance | man | One | person | m7 | stage9_reference | ent_m0 |  | 1 |
| eref_m8 | contrastive_instance | man | other | person | m8 | stage9_reference | ent_m0 |  | 1 |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m7 | eref_m7 | m0 | ent_m0 | high |  |
| refers_to | m8 | eref_m8 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | smile | smile | smile |  | agent:m0->ent_m0 |  |
| ce1 | m10 | wears | wear | wear |  | agent:m0->eref_m7; patient:m4->ent_m4; patient:m5->ent_m5 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | smile | agent | m0 | ent_m0 | medium | e4 | nsubj -> smile |  |  |
| ce1 | wear | agent | m0 | eref_m7 | medium | e5 | nsubj -> wears; resolved One -> men |  |  |
| ce1 | wear | patient | m4 | ent_m4 | medium | e6 | dobj -> wears |  |  |
| ce1 | wear | patient | m5 | ent_m5 | medium | e7 | dobj -> wears |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | for | medium | e8 | False | False |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | in | high | e9 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | child | Children | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | dress | dresses | clothing | m1 | raw_mention |  |  |  |
| ent_m3 | object | shirt | shirts | clothing | m3 | raw_mention |  |  |  |
| ent_m4 | object | chair | chairs | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | performance | performance | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | child | child | person | m6 | raw_mention |  |  |  |
| ent_m8 | object | violin | violin | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | music_stand | music stands | object | m9 | raw_mention |  |  |  |
| ent_m10 | context | setting | setting | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | curtain | curtains | object | m11 | raw_mention |  |  |  |
| ent_m13 | object | chair | chairs | object | m13 | raw_mention |  |  |  |
| ent_m15 | context | background | background | object | m15 | raw_mention |  |  |  |
| ent_m16 | context | indoors | indoors | object | m16 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | sit | sit | sit |  | agent:m0->ent_m0 |  |
| ce1 | m18 | holds | hold | hold |  | agent:m6->ent_m6; patient:m8->ent_m8 |  |
| ce2 | m19 | seated | seat | seat |  | agent:m6->ent_m6 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m0 | ent_m0 | medium | e7 | nsubj -> sit |  |  |
| ce1 | hold | agent | m6 | ent_m6 | medium | e8 | nsubj -> holds |  |  |
| ce1 | hold | patient | m8 | ent_m8 | medium | e9 | dobj -> holds |  |  |
| ce2 | seat | agent | m6 | ent_m6 | medium | e10 | inherited agent advcl -> holds |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e11 | False | False |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | in | high | e12 | False | False |
| cr2 | m0 | m4 | ent_m0 | ent_m4 | on | high | e13 | False | False |
| cr3 | m0 | m5 | ent_m0 | ent_m5 | during | medium | e14 | False | False |

### Stage 9 Canonicalization Notes
_none_

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | wall | wall | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | worker | worker | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | sidewalk | sidewalk | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | building | building | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | reflection | reflection | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | grass | grass | object | m6 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | cityscape | cityscape | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | building | buildings | object | m1 | raw_mention |  |  |  |
| ent_m4 | context | dusk | dusk | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | street | streets | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | vehicle | vehicles | vehicle | m6 | raw_mention |  |  |  |
| ent_m7 | object | waterfront | waterfront | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | skyscraper | skyscrapers | object | m8 | raw_mention |  |  |  |
| ent_m10 | context | distance | distance | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | sky | sky | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | hue | hues | object | m12 | raw_mention |  |  |  |
| ent_m16 | object | horizon | horizon | object | m16 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | viewed | view | view |  | agent:m0->ent_m0 |  |
| ce1 | m18 | stretch | stretch | stretch |  | agent:m5->ent_m5; agent:m6->ent_m6 |  |
| ce2 | m19 | shows | show | show |  | agent:m11->ent_m11; patient:m12->ent_m12 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | view | agent | m0 | ent_m0 | medium | e8 | inherited agent acl -> cityscape |  |  |
| ce1 | stretch | agent | m5 | ent_m5 | medium | e9 | nsubj -> stretch |  |  |
| ce1 | stretch | agent | m6 | ent_m6 | medium | e10 | nsubj -> stretch |  |  |
| ce2 | show | agent | m11 | ent_m11 | medium | e11 | nsubj -> shows |  |  |
| ce2 | show | patient | m12 | ent_m12 | medium | e12 | dobj -> shows |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | at | medium | e13 | False | False |
| cr1 | m5 | m7 | ent_m5 | ent_m7 | toward | medium | e14 | False | False |
| cr2 | m7 | m8 | ent_m7 | ent_m8 | with | high | e15 | False | False |
| cr3 | m8 | m10 | ent_m8 | ent_m10 | in | high | e16 | False | False |
| cr4 | m11 | m16 | ent_m11 | ent_m16 | near | high | e17 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | road | road | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | line | line | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | frame | frame | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | field | field | object | m5 | raw_mention |  |  |  |
| ent_m8 | object | horizon | horizon | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | sky | sky | object | m9 | raw_mention |  |  |  |
| ent_m12 | object | tree | trees | object | m12 | raw_mention |  |  |  |
| ent_m15 | object | power_line | power lines | object | m15 | raw_mention |  |  |  |
| ent_m16 | context | background | background | object | m16 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | runs | run | run |  | agent:m0->ent_m0 |  |
| ce1 | m18 | stretches | stretch | stretch |  | agent:m5->ent_m5 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | run | agent | m0 | ent_m0 | medium | e9 | nsubj -> runs |  |  |
| ce1 | stretch | agent | m5 | ent_m5 | medium | e10 | nsubj -> stretches |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e11 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | bottom_of | medium | e12 | False | False |
| cr2 | m5 | m0 | ent_m5 | ent_m0 | beyond | high | e13 | False | False |
| cr3 | m5 | m8 | ent_m5 | ent_m8 | to | medium | e14 | False | False |
| cr4 | m5 | m9 | ent_m5 | ent_m9 | under | high | e15 | False | False |
| cr5 | m12 | m16 | ent_m12 | ent_m16 | in | high | e16 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | teacher | teacher | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | student | students | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | shirt | shirts | clothing | m3 | raw_mention |  |  |  |
| ent_m5 | object | rug | rug | object | m5 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | stand | stand | stand |  | agent:m0->ent_m0; agent:m1->ent_m1 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e4 | nsubj -> stand |  |  |
| ce0 | stand | agent | m1 | ent_m1 | medium | e5 | nsubj -> stand |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m3 | ent_m1 | ent_m3 | in | high | e6 | False | False |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | high | e7 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | proximity | proximity | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | man | man | person | m4 | raw_mention |  |  |  |
| ent_m5 | context | left | left | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | woman | woman | person | m6 | raw_mention |  |  |  |
| ent_m7 | context | center | center | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | woman | woman | person | m8 | raw_mention |  |  |  |
| ent_m9 | context | right | right | object | m9 | raw_mention |  |  |  |
| ent_m10 | object | woman | woman | person | m10 | raw_mention |  |  |  |
| ent_m11 | context | center | center | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | hair | hair | object | m12 | raw_mention |  |  |  |
| ent_m14 | object | lip | lips | object | m14 | raw_mention |  |  |  |
| ent_m15 | object | finger | finger | object | m15 | raw_mention |  |  |  |
| ent_m16 | object | woman | woman | person | m16 | raw_mention |  |  |  |
| ent_m17 | context | right | right | object | m17 | raw_mention |  |  |  |
| ent_m18 | object | sign | sign | document | m18 | raw_mention |  |  |  |
| ent_m20 | context | background | background | object | m20 | raw_mention |  |  |  |
| ent_m21 | context | indoors | indoors | object | m21 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m22 | has | have | have |  | agent:m10->ent_m10; patient:m12->ent_m12 |  |
| ce1 | m23 | touching | touch | touch |  | agent:m10->ent_m10; patient:m14->ent_m14 |  |
| ce2 | m24 | smiles | smile | smile |  | agent:m16->ent_m16 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | have | agent | m10 | ent_m10 | medium | e6 | nsubj -> has |  |  |
| ce0 | have | patient | m12 | ent_m12 | medium | e7 | dobj -> has |  |  |
| ce1 | touch | agent | m10 | ent_m10 | medium | e8 | inherited agent conj -> has |  |  |
| ce1 | touch | patient | m14 | ent_m14 | medium | e9 | dobj -> touching |  |  |
| ce2 | smile | agent | m16 | ent_m16 | medium | e10 | nsubj -> smiles |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | high | e11 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | high | e12 | False | False |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | with | high | e13 | False | False |
| cr3 | m0 | m8 | ent_m0 | ent_m8 | with | high | e14 | False | False |
| cr4 | m4 | m5 | ent_m4 | ent_m5 | on | high | e15 | False | False |
| cr5 | m6 | m7 | ent_m6 | ent_m7 | in | high | e16 | False | False |
| cr6 | m8 | m9 | ent_m8 | ent_m9 | on | high | e17 | False | False |
| cr7 | m10 | m11 | ent_m10 | ent_m11 | in | high | e18 | False | False |
| cr8 | m10 | m15 | ent_m10 | ent_m15 | with | high | e19 | False | False |
| cr9 | m16 | m17 | ent_m16 | ent_m17 | on | high | e20 | False | False |
| cr10 | m18 | m20 | ent_m18 | ent_m20 | in | high | e21 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | duck | duck | animal | m0 | raw_mention |  |  |  |
| ent_m2 | object | water | water | object | m2 | raw_mention |  |  |  |
| ent_m5 | object | ripple | ripples | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | body | body | object | m6 | raw_mention |  |  |  |
| ent_m7 | object | head | head | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | neck | neck | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | chest | chest | object | m9 | raw_mention |  |  |  |
| ent_m11 | context | surface | surface | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | water | water | object | m12 | raw_mention |  |  |  |
| ent_m13 | object | tree_branch | tree branches | object | m13 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | swims | swim | swim |  | agent:m0->ent_m0 |  |
| ce1 | m17 | creating | create | create |  | agent:m0->ent_m0; patient:m5->ent_m5 |  |
| ce2 | m18 | glides | glide | glide |  | agent:m0->ent_m0 |  |
| ce3 | m19 | reflects | reflect | reflect |  | agent:m12->ent_m12; patient:m13->ent_m13 |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | high | e12 | False | False |
| cr1 | m0 | m6 | ent_m0 | ent_m6 | around | high | e13 | False | False |
| cr2 | m0 | m11 | ent_m0 | ent_m11 | near | high | e14 | False | False |

### Stage 9 Canonicalization Notes
_none_

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | scoreboard | scoreboard | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | rink | rink | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | banner | banners | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | rider | riders | person | m5 | raw_mention |  |  |  |
| ent_m7 | object | surface | surface | object | m7 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | text | text | document | m0 | raw_mention |  |  |  |
| ent_m1 | object | page | page | document | m1 | raw_mention |  |  |  |
| ent_m3 | object | book | book | document | m3 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | dog | dog | animal | m1 | raw_mention |  |  |  |
| ent_m3 | object | basket | basket | object | m3 | raw_mention |  |  |  |
| ent_m7 | object | grass | grass | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | man | man | person | m8 | raw_mention |  |  |  |
| ent_m9 | object | outfit | outfit | object | m9 | raw_mention |  |  |  |
| ent_m11 | object | trim | trim | object | m11 | raw_mention |  |  |  |
| ent_m14 | object | dog | dog | animal | m14 | raw_mention |  |  |  |
| ent_m15 | context | background | background | object | m15 | raw_mention |  |  |  |
| ent_m16 | object | spectator | spectators | object | m16 | raw_mention |  |  |  |
| ent_m17 | object | fence | fence | object | m17 | raw_mention |  |  |  |
| ent_m18 | object | banner | banner | object | m18 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m19 | leaps | leap | leap |  | agent:m1->ent_m1 |  |
| ce1 | m20 | stands | stand | stand |  | agent:m8->ent_m8 |  |
| ce2 | m21 | watching | watch | watch |  | agent:m8->ent_m8; patient:m14->ent_m14 |  |
| ce3 | m22 | stand | stand | stand |  | agent:m16->ent_m16 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | leap | agent | m1 | ent_m1 | medium | e9 | nsubj -> leaps |  |  |
| ce1 | stand | agent | m8 | ent_m8 | medium | e10 | nsubj -> stands |  |  |
| ce2 | watch | agent | m8 | ent_m8 | medium | e11 | inherited agent advcl -> stands |  |  |
| ce2 | watch | patient | m14 | ent_m14 | medium | e12 | dobj -> watching |  |  |
| ce3 | stand | agent | m16 | ent_m16 | medium | e13 | nsubj -> stand |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m3 | ent_m1 | ent_m3 | over | high | e14 | False | False |
| cr1 | m3 | m7 | ent_m3 | ent_m7 | on | high | e15 | False | False |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | in | high | e16 | False | False |
| cr3 | m9 | m11 | ent_m9 | ent_m11 | with | high | e17 | False | False |
| cr4 | m16 | m15 | ent_m16 | ent_m15 | in | high | e18 | False | False |
| cr5 | m16 | m17 | ent_m16 | ent_m17 | behind | high | e19 | False | False |
| cr6 | m16 | m18 | ent_m16 | ent_m18 | near | high | e20 | False | False |

### Stage 9 Canonicalization Notes
_none_

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | axe | axe | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | mask | mask | clothing | m1 | raw_mention |  |  |  |
| ent_m2 | object | costume | costume | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | grass | grass | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | fence | fence | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | stump | stump | object | m5 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | shirt | shirt | clothing | m1 | raw_mention |  |  |  |
| ent_m3 | object | panel | panel | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | wire | wires | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | switch | switches | object | m6 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | works | work | work |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | work | agent | m0 | ent_m0 | medium | e2 | nsubj -> works |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e3 | False | False |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | on | high | e4 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | person | person | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | costume | costume | object | m1 | raw_mention |  |  |  |
| ent_m4 | object | stage | stage | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | light | lights | object | m5 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | stands | stand | stand |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e3 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e4 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | high | e5 | False | False |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | with | high | e6 | False | False |
| cr3 | m5 | m0 | ent_m5 | ent_m0 | behind | high | e7 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | helicopter | helicopter | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | hillside | hillside | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | lake | lake | object | m4 | raw_mention |  |  |  |
| ent_m6 | context | distance | distance | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | mountain | mountains | object | m8 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | flies | fly | fly |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | fly | agent | m0 | ent_m0 | medium | e4 | nsubj -> flies |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | over | high | e7 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | near | high | e8 | False | False |
| cr2 | m8 | m6 | ent_m8 | ent_m6 | in | high | e9 | False | False |

### Stage 9 Canonicalization Notes
_none_

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | woman | woman | person | m1 | raw_mention |  |  |  |
| ent_m2 | object | beach | beach | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | drink | drink | object | m4 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m5 | stand | stand | stand |  | agent:m0->ent_m0; agent:m1->ent_m1 |  |
| ce1 | m6 | sharing | share | share |  | agent:m0->ent_m0; agent:m1->ent_m1; patient:m4->ent_m4 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e1 | nsubj -> stand |  |  |
| ce0 | stand | agent | m1 | ent_m1 | medium | e2 | nsubj -> stand |  |  |
| ce1 | share | agent | m0 | ent_m0 | medium | e3 | inherited agent advcl -> stand |  |  |
| ce1 | share | agent | m1 | ent_m1 | medium | e4 | inherited agent advcl -> stand |  |  |
| ce1 | share | patient | m4 | ent_m4 | medium | e5 | dobj -> sharing |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | high | e6 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | giraffe | giraffes | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | savanna | savanna | object | m2 | raw_mention |  |  |  |
| ent_m5 | object | tree | trees | object | m5 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | stand | stand | stand |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e4 | nsubj -> stand |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | high | e5 | False | False |
| cr1 | m2 | m5 | ent_m2 | ent_m5 | with | high | e6 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | close-up | close-up | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | human_eye | human eye | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | iris | irises | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | pupil | pupils | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | eye | eye | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | eyelash | eyelashes | object | m8 | raw_mention |  |  |  |
| ent_m10 | object | skin | skin | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | light | light | object | m11 | raw_mention |  |  |  |
| ent_m14 | object | text | Text | document | m14 | raw_mention |  |  |  |
| ent_m15 | context | bottom | bottom | object | m15 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | framed | frame | frame |  | theme:m7->ent_m7; by_agent_or_causer:m8->ent_m8; by_agent_or_causer:m10->ent_m10 |  |
| ce1 | m17 | surrounding | surround | surround |  | agent:m11->ent_m11; patient:m7->ent_m7 |  |
| ce2 | m18 | reads | read | read |  | agent:m14->ent_m14; patient:m0->None |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | of | medium | e10 | False | False |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | with | high | e11 | False | False |
| cr2 | m2 | m5 | ent_m2 | ent_m5 | with | high | e12 | False | False |
| cr3 | m7 | m8 | ent_m7 | ent_m8 | by | medium | e13 | True | False |
| cr4 | m7 | m10 | ent_m7 | ent_m10 | by | medium | e14 | True | False |
| cr5 | m14 | m15 | ent_m14 | ent_m15 | at | medium | e15 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | sidewalk | sidewalk | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | phone | phone | device | m3 | raw_mention |  |  |  |
| ent_m4 | object | bag | bag | object | m4 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m6 | walks | walk | walk |  | agent:m0->ent_m0 |  |
| ce1 | m7 | talking | talk | talk |  | agent:m0->ent_m0 |  |
| ce2 | m8 | carrying | carry | carry |  | agent:m0->ent_m0; patient:m4->ent_m4 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | walk | agent | m0 | ent_m0 | medium | e2 | nsubj -> walks |  |  |
| ce1 | talk | agent | m0 | ent_m0 | medium | e3 | inherited agent advcl -> walks |  |  |
| ce2 | carry | agent | m0 | ent_m0 | medium | e4 | inherited agent advcl -> walks |  |  |
| ce2 | carry | patient | m4 | ent_m4 | medium | e5 | dobj -> carrying |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | down | medium | e6 | False | False |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | on | high | e7 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | stencil | stencil | object | m1 | raw_mention |  |  |  |
| ent_m4 | object | pillar | pillar | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | artwork | artwork | object | m6 | raw_mention |  |  |  |
| ent_m7 | object | man | man | person | m7 | raw_mention |  |  |  |
| ent_m8 | object | hat | hat | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | collar | collar | clothing | m9 | raw_mention |  |  |  |
| ent_m11 | object | circle | circle | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | pillar | pillar | object | m12 | raw_mention |  |  |  |
| ent_m13 | object | alley | alley | object | m13 | raw_mention |  |  |  |
| ent_m15 | object | wall | wall | object | m15 | raw_mention |  |  |  |
| ent_m17 | object | beam | beam | object | m17 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m19 | reads | read | read |  | agent:m1->ent_m1 |  |
| ce1 | m20 | depicts | depict | depict |  | agent:m6->ent_m6; patient:m7->ent_m7 |  |
| ce2 | m21 | surrounded | surround | surround |  | agent:m7->ent_m7 |  |
| ce3 | m22 | stands | stand | stand |  | agent:m12->ent_m12 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | read | agent | m1 | ent_m1 | medium | e7 | nsubj -> reads |  |  |
| ce1 | depict | agent | m6 | ent_m6 | medium | e8 | nsubj -> depicts |  |  |
| ce1 | depict | patient | m7 | ent_m7 | medium | e9 | dobj -> depicts |  |  |
| ce2 | surround | agent | m7 | ent_m7 | medium | e10 | inherited agent acl -> man |  |  |
| ce3 | stand | agent | m12 | ent_m12 | medium | e11 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m4 | ent_m1 | ent_m4 | on | high | e12 | False | False |
| cr1 | m7 | m8 | ent_m7 | ent_m8 | in | high | e13 | False | False |
| cr2 | m7 | m9 | ent_m7 | ent_m9 | in | high | e14 | False | False |
| cr3 | m7 | m11 | ent_m7 | ent_m11 | by | medium | e15 | False | False |
| cr4 | m12 | m13 | ent_m12 | ent_m13 | beside | high | e16 | False | False |
| cr5 | m13 | m15 | ent_m13 | ent_m15 | with | high | e17 | False | False |
| cr6 | m13 | m17 | ent_m13 | ent_m17 | with | high | e18 | False | False |

### Stage 9 Canonicalization Notes
_none_

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | hair | hair | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | goatee | goatee | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | shirt | shirt | clothing | m4 | raw_mention |  |  |  |
| ent_m6 | object | gesture | gesture | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | hand | hands | object | m8 | raw_mention |  |  |  |
| ent_m10 | object | nail_polish | nail polish | object | m10 | raw_mention |  |  |  |
| ent_m12 | object | necklace | necklace | object | m12 | raw_mention |  |  |  |
| ent_m15 | object | earring | earring | object | m15 | raw_mention |  |  |  |
| ent_m16 | object | door | door | object | m16 | raw_mention |  |  |  |
| ent_m18 | object | banner | banner | object | m18 | raw_mention |  |  |  |
| ent_m20 | context | indoors | indoors | object | m20 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m21 | wears | wear | wear |  | agent:m0->ent_m0; patient:m4->ent_m4 |  |
| ce1 | m22 | makes | make | make |  | agent:m0->ent_m0; patient:m6->ent_m6 |  |
| ce2 | m23 | has | have | have |  | agent:m0->ent_m0; patient:m10->ent_m10; patient:m12->ent_m12; patient:m15->ent_m15 |  |
| ce3 | m24 | standing | stand | stand |  | agent:m0->ent_m0 |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | high | e19 | False | False |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | with | high | e20 | False | False |
| cr2 | m0 | m8 | ent_m0 | ent_m8 | with | high | e21 | False | False |
| cr3 | m0 | m16 | ent_m0 | ent_m16 | near | high | e22 | False | False |
| cr4 | m0 | m18 | ent_m0 | ent_m18 | near | high | e23 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | building | building | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | sign | sign | document | m3 | raw_mention |  |  |  |
| ent_m4 | object | road | road | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | smokestack | smokestacks | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | power_line | power lines | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | stands | stand | stand |  | agent:m1->ent_m1 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m1 | ent_m1 | medium | e3 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m3 | ent_m1 | ent_m3 | with | high | e4 | False | False |
| cr1 | m1 | m4 | ent_m1 | ent_m4 | beside | high | e5 | False | False |
| cr2 | m1 | m5 | ent_m1 | ent_m5 | near | high | e6 | False | False |
| cr3 | m1 | m7 | ent_m1 | ent_m7 | near | high | e7 | False | False |

### Stage 9 Canonicalization Notes
_none_

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | alleyway | alleyway | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | brick | bricks | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | wall | walls | object | m3 | raw_mention |  |  |  |
| ent_m7 | context | right | right | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | tree | tree | object | m8 | raw_mention |  |  |  |
| ent_m10 | object | path | path | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | house | houses | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | shadow | Shadows | object | m12 | raw_mention |  |  |  |
| ent_m13 | object | ground | ground | object | m13 | raw_mention |  |  |  |
| ent_m14 | object | wall | wall | object | m14 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | paved | pave | pave |  | agent:m0->ent_m0 |  |
| ce1 | m17 | stretches | stretch | stretch |  | agent:m0->ent_m0 |  |
| ce2 | m18 | stands | stand | stand |  | agent:m8->ent_m8 |  |
| ce3 | m19 | stretch | stretch | stretch |  | agent:m12->ent_m12 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | pave | agent | m0 | ent_m0 | medium | e6 | inherited agent acl -> alleyway |  |  |
| ce1 | stretch | agent | m0 | ent_m0 | medium | e7 | nsubj -> stretches |  |  |
| ce2 | stand | agent | m8 | ent_m8 | medium | e8 | nsubj -> stands |  |  |
| ce3 | stretch | agent | m12 | ent_m12 | medium | e9 | nsubj -> stretch |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e10 | False | False |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | between | high | e11 | False | False |
| cr2 | m8 | m7 | ent_m8 | ent_m7 | on | high | e12 | False | False |
| cr3 | m8 | m10 | ent_m8 | ent_m10 | near_end_of | medium | e13 | False | False |
| cr4 | m12 | m13 | ent_m12 | ent_m13 | across | high | e14 | False | False |
| cr5 | m12 | m14 | ent_m12 | ent_m14 | from | medium | e15 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | building | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | column | columns | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | entrance | entrance | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | palm_tree | palm trees | object | m5 | raw_mention |  |  |  |
| ent_m8 | object | lawn | lawn | object | m8 | raw_mention |  |  |  |
| ent_m10 | object | sky | sky | object | m10 | raw_mention |  |  |  |
| ent_m13 | object | shadow | shadows | object | m13 | raw_mention |  |  |  |
| ent_m14 | object | grass | grass | object | m14 | raw_mention |  |  |  |
| ent_m15 | object | tree | trees | object | m15 | raw_mention |  |  |  |
| eref_m16 | reference | building | The structure | object | m16 | stage9_reference | ent_m0 |  |  |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m16 | eref_m16 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | surrounded | surround | surround |  | theme:m0->ent_m0; by_agent_or_causer:m5->ent_m5 |  |
| ce1 | m18 | sits | sit | sit |  | agent:m0->ent_m0 |  |
| ce2 | m19 | cast | cast | cast |  | agent:m13->ent_m13 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | surround | theme | m0 | ent_m0 | medium | e7 | nsubjpass -> surrounded |  |  |
| ce0 | surround | by_agent_or_causer | m5 | ent_m5 | medium | e12 | passive by-frame |  |  |
| ce1 | sit | agent | m0 | ent_m0 | medium | e8 | nsubj -> sits; resolved structure -> building |  |  |
| ce2 | cast | agent | m13 | ent_m13 | medium | e9 | inherited agent acl -> shadows |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e10 | False | False |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | with | high | e11 | False | False |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | by | medium | e12 | True | False |
| cr3 | m0 | m8 | ent_m0 | ent_m8 | on | high | e13 | False | False |
| cr4 | m0 | m10 | ent_m0 | ent_m10 | under | high | e14 | False | False |
| cr5 | m0 | m13 | ent_m0 | ent_m13 | with | high | e15 | False | False |
| cr6 | m13 | m14 | ent_m13 | ent_m14 | across | high | e16 | False | False |
| cr7 | m13 | m15 | ent_m13 | ent_m15 | from | medium | e17 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | glass | glass | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | macchiato | macchiato | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | table | table | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | foam | foam | object | m6 | raw_mention |  |  |  |
| ent_m7 | object | tray | tray | object | m7 | raw_mention |  |  |  |
| ent_m9 | object | doily | doily | object | m9 | raw_mention |  |  |  |
| ent_m10 | object | spoon | spoon | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | packet | packet | object | m11 | raw_mention |  |  |  |
| ent_m13 | context | background | background | object | m13 | raw_mention |  |  |  |
| ent_m16 | object | rock | rocks | object | m16 | raw_mention |  |  |  |
| ent_m17 | object | greenery | greenery | object | m17 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | sits | sit | sit |  | agent:m0->ent_m0 |  |
| ce1 | m19 | topped | top | top |  | agent:m0->ent_m0 |  |
| ce2 | m20 | resting | rest | rest |  | agent:m0->ent_m0 |  |
| ce3 | m21 | showing | show | show |  | agent:m13->ent_m13; patient:m16->ent_m16; patient:m17->ent_m17 |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | of | medium | e14 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | high | e15 | False | False |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | with | high | e16 | False | False |
| cr3 | m7 | m9 | ent_m7 | ent_m9 | with | high | e17 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | building | object | m0 | raw_mention |  |  |  |
| ent_m3 | object | window | windows | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | lot | lot | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | car | cars | vehicle | m7 | raw_mention |  |  |  |
| ent_m9 | object | sky | sky | object | m9 | raw_mention |  |  |  |
| ent_m11 | object | tree | trees | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | building | buildings | object | m12 | raw_mention |  |  |  |
| ent_m14 | context | background | background | object | m14 | raw_mention |  |  |  |
| ent_m16 | object | car | red car | vehicle | m16 | raw_mention |  |  |  |
| eref_m15 | instance | car | one | vehicle | m15 | stage9_reference | ent_m7 |  | 1 |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m15 | eref_m15 | m7 | ent_m7 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | stands | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m19 | including | include | include |  | agent:m7->ent_m7; patient:m16->ent_m16 |  |
| ce2 | m20 | parked | park | park |  | theme:m7->ent_m7 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e11 | nsubj -> stands |  |  |
| ce1 | include | agent | m7 | ent_m7 | medium | e12 | inherited agent prep -> cars |  |  |
| ce1 | include | patient | m16 | ent_m16 | medium | e13 | pobj -> including; resolved one -> red car |  |  |
| ce2 | park | theme | m7 | ent_m7 | medium | e14 | nsubjpass -> parked |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | with | high | e15 | False | False |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | high | e16 | False | False |
| cr2 | m7 | m16 | ent_m7 | ent_m16 | include | medium | e17 | False | False |
| cr3 | m7 | m9 | ent_m7 | ent_m9 | under | high | e18 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | shirt | shirt | clothing | m1 | raw_mention |  |  |  |
| ent_m3 | object | acoustic_guitar | acoustic guitar | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | microphone | microphone | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | stage | stage | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | curtain | curtains | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | keyboard | keyboard | object | m8 | raw_mention |  |  |  |
| ent_m9 | context | right | right | object | m9 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | plays | play | play |  | agent:m0->ent_m0; patient:m3->ent_m3 |  |
| ce1 | m11 | singing | sing | sing |  | agent:m0->ent_m0 |  |
| ce2 | m12 | stands | stand | stand |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | play | agent | m0 | ent_m0 | medium | e2 | nsubj -> plays |  |  |
| ce0 | play | patient | m3 | ent_m3 | medium | e3 | dobj -> plays |  |  |
| ce1 | sing | agent | m0 | ent_m0 | medium | e4 | inherited agent advcl -> plays |  |  |
| ce2 | stand | agent | m0 | ent_m0 | medium | e5 | nsubj -> stands; resolved He -> man |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e6 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | into | medium | e7 | False | False |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | on | high | e8 | False | False |
| cr3 | m0 | m6 | ent_m0 | ent_m6 | with | high | e9 | False | False |
| cr4 | m0 | m8 | ent_m0 | ent_m8 | with | high | e10 | False | False |
| cr5 | m6 | m0 | ent_m6 | ent_m0 | behind | high | e11 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | pipe | pipes | object | m0 | raw_mention |  |  |  |
| ent_m4 | object | frame | frame | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | sky | sky | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | fencing | fencing | object | m7 | raw_mention |  |  |  |
| ent_m10 | object | rebar | rebar | object | m10 | raw_mention |  |  |  |
| ent_m12 | context | distance | distance | object | m12 | raw_mention |  |  |  |
| ent_m13 | context | scene | scene | object | m13 | raw_mention |  |  |  |
| ent_m14 | object | site | site | object | m14 | raw_mention |  |  |  |
| ent_m17 | object | wall | walls | object | m17 | raw_mention |  |  |  |
| ent_m20 | object | beam | beams | object | m20 | raw_mention |  |  |  |
| ent_m23 | object | worker | workers | object | m23 | raw_mention |  |  |  |
| ent_m24 | object | equipment | equipment | object | m24 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m22 | run | run | run |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | run | agent | m0 | ent_m0 | medium | e14 | nsubj -> run |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | across | high | e17 | False | False |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | under | high | e18 | False | False |
| cr2 | m23 | m12 | ent_m23 | ent_m12 | in | high | e19 | False | False |
| cr3 | m14 | m17 | ent_m14 | ent_m17 | with | high | e20 | False | False |
| cr4 | m14 | m20 | ent_m14 | ent_m20 | with | high | e21 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | soccer_player | soccer player | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | uniform | uniform | clothing | m1 | raw_mention |  |  |  |
| ent_m3 | object | field | field | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | soccer_ball | soccer ball | object | m5 | raw_mention |  |  |  |
| ent_m8 | object | spectator | Spectators | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | fence | fence | object | m9 | raw_mention |  |  |  |
| ent_m10 | context | background | background | object | m10 | raw_mention |  |  |  |
| ent_m14 | object | tree | trees | object | m14 | raw_mention |  |  |  |
| ent_m15 | object | sky | sky | object | m15 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m11 | stands | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m12 | preparing | prepare | prepare |  | agent:m0->ent_m0 |  |
| ce2 | m13 | kick | kick | kick |  | agent:m0->ent_m0; patient:m5->ent_m5 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e5 | nsubj -> stands |  |  |
| ce1 | prepare | agent | m0 | ent_m0 | medium | e6 | inherited agent advcl -> stands |  |  |
| ce2 | kick | agent | m0 | ent_m0 | medium | e7 | inherited agent xcomp -> preparing |  |  |
| ce2 | kick | patient | m5 | ent_m5 | medium | e8 | dobj -> kick |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e12 | False | False |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | on | high | e13 | False | False |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | behind | high | e14 | False | False |
| cr3 | m9 | m10 | ent_m9 | ent_m10 | in | high | e15 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hockey_player | hockey player | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | ice_rink | ice rink | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | jersey | jersey | clothing | m3 | raw_mention |  |  |  |
| ent_m6 | object | short | shorts | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | gear | gear | object | m8 | raw_mention |  |  |  |
| ent_m10 | object | hockey_stick | hockey stick | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | hand | hands | object | m11 | raw_mention |  |  |  |
| ent_m13 | object | wall | wall | object | m13 | raw_mention |  |  |  |
| ent_m15 | object | rink | rink | object | m15 | raw_mention |  |  |  |
| ent_m16 | context | background | background | object | m16 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | stands | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m18 | wearing | wear | wear |  | agent:m0->ent_m0; patient:m3->ent_m3; patient:m6->ent_m6; patient:m8->ent_m8 |  |
| ce2 | m19 | hold | hold | hold |  | agent:m0->ent_m0; patient:m10->ent_m10 |  |
| ce3 | m20 | positioned | position | position |  | agent:m0->ent_m0 |  |
| ce4 | m21 | looking | look | look |  | agent:m0->ent_m0 |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | high | e17 | False | False |
| cr1 | m0 | m11 | ent_m0 | ent_m11 | with | high | e18 | False | False |
| cr2 | m10 | m0 | ent_m10 | ent_m0 | in_front_of; repaired_self_edge_source from hockey player | medium | e19 | False | False |
| cr3 | m13 | m15 | ent_m13 | ent_m15 | of | medium | e20 | False | False |
| cr4 | m13 | m16 | ent_m13 | ent_m16 | in | high | e21 | False | False |

### Stage 9 Canonicalization Notes
_none_

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | building | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | window | windows | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | spire | spire | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | sky | sky | object | m6 | raw_mention |  |  |  |
| ent_m9 | object | streetlamp | streetlamp | object | m9 | raw_mention |  |  |  |
| ent_m11 | object | frame | frame | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | facade | facade | object | m12 | raw_mention |  |  |  |
| ent_m14 | object | box | boxes | object | m14 | raw_mention |  |  |  |
| ent_m16 | object | window | windows | object | m16 | raw_mention |  |  |  |
| ent_m17 | object | floor | floor | object | m17 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m19 | stands | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m20 | hangs | hang | hang |  | agent:m9->ent_m9 |  |
| ce2 | m21 | line | line | line |  | agent:m14->ent_m14; patient:m16->ent_m16 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e9 | nsubj -> stands |  |  |
| ce1 | hang | agent | m9 | ent_m9 | medium | e10 | nsubj -> hangs |  |  |
| ce2 | line | agent | m14 | ent_m14 | medium | e11 | nsubj -> line |  |  |
| ce2 | line | patient | m16 | ent_m16 | medium | e12 | dobj -> line |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e13 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | high | e14 | False | False |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | under | high | e15 | False | False |
| cr3 | m9 | m11 | ent_m9 | ent_m11 | from_side_of | medium | e16 | False | False |
| cr4 | m9 | m12 | ent_m9 | ent_m12 | next_to | high | e17 | False | False |
| cr5 | m16 | m17 | ent_m16 | ent_m17 | on | high | e18 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | metal | metal | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | pile | pile | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | cornfield | cornfield | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | pipe | pipes | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | beam | beam | object | m7 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | people | people | person | m1 | raw_mention |  |  |  |
| ent_m3 | object | table | table | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | discussion | discussion | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | screen | screen | device | m6 | raw_mention |  |  |  |
| ent_m8 | object | text | text | document | m8 | raw_mention |  |  |  |
| ent_m9 | object | person | person | person | m9 | raw_mention |  |  |  |
| ent_m11 | object | microphone | microphone | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | nameplate | nameplate | object | m12 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m13 | sit | sit | sit |  | agent:m1->ent_m1 |  |
| ce1 | m14 | displays | display | display |  | agent:m6->ent_m6; patient:m8->ent_m8 |  |
| ce2 | m15 | has | have | have |  | agent:m9->ent_m9; patient:m11->ent_m11; patient:m12->ent_m12 |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m3 | ent_m1 | ent_m3 | at | medium | e11 | False | False |
| cr1 | m1 | m4 | ent_m1 | ent_m4 | during | medium | e12 | False | False |
| cr2 | m6 | m1 | ent_m6 | ent_m1 | behind | high | e13 | False | False |
| cr3 | m11 | m9 | ent_m11 | ent_m9 | in_front_of; repaired_self_edge_source from person | medium | e14 | False | False |
| cr4 | m12 | m9 | ent_m12 | ent_m9 | in_front_of; repaired_self_edge_source from person | medium | e15 | False | False |

### Stage 9 Canonicalization Notes
_none_

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | tuxedo | tuxedo | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | thumbs-up | thumbs-up | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | trophy | trophy | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | stage | stage | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | woman | woman | person | m5 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m6 | gives | give | give |  | agent:m0->ent_m0; patient:m2->ent_m2 |  |
| ce1 | m7 | holding | hold | hold |  | agent:m0->ent_m0; patient:m3->ent_m3 |  |
| ce2 | m8 | stands | stand | stand |  | agent:m5->ent_m5 |  |
| ce3 | m9 | smiling | smile | smile |  | agent:m5->ent_m5 |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e6 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | high | e7 | False | False |
| cr2 | m5 | m0 | ent_m5 | ent_m0 | beside | high | e8 | False | False |

### Stage 9 Canonicalization Notes
_none_

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | person | person | person | m1 | raw_mention |  |  |  |
| ent_m2 | object | bicycle_helmet | bicycle helmet | object | m2 | raw_mention |  |  |  |
| ent_m5 | object | sunglass | sunglasses | object | m5 | raw_mention |  |  |  |
| ent_m8 | object | grass | grass | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | sunlight | sunlight | object | m9 | raw_mention |  |  |  |
| ent_m10 | context | background | background | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | stamp | stamp | object | m11 | raw_mention |  |  |  |
| ent_m13 | context | corner | corner | object | m13 | raw_mention |  |  |  |
| ent_m14 | context | outdoors | outdoors | object | m14 | raw_mention |  |  |  |
| eref_m15 | reference | person | The individual | person | m15 | stage9_reference | ent_m1 |  |  |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m15 | eref_m15 | m1 | ent_m1 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | wears | wear | wear |  | agent:m1->ent_m1; patient:m2->ent_m2 |  |
| ce1 | m17 | reads | read | read |  | agent:m11->ent_m11; patient:m0->None |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | wear | agent | m1 | ent_m1 | medium | e7 | nsubj -> wears |  |  |
| ce0 | wear | patient | m2 | ent_m2 | medium | e8 | dobj -> wears |  |  |
| ce1 | read | agent | m11 | ent_m11 | medium | e9 | nsubj -> reads |  |  |
| ce1 | read | patient | m0 |  | medium | e10 | dobj -> reads |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m2 | m5 | ent_m2 | ent_m5 | with | high | e11 | False | False |
| cr1 | m11 | m13 | ent_m11 | ent_m13 | in | high | e12 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | flower | flower | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | leaf | leaves | object | m2 | raw_mention |  |  |  |
| ent_m4 | context | background | background | object | m4 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | man | man | person | m1 | raw_mention |  |  |  |
| ent_m2 | object | umbrella | umbrella | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | sign | sign | document | m4 | raw_mention |  |  |  |
| ent_m6 | object | park | park | object | m6 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | holds | hold | hold |  | agent:m1->ent_m1; patient:m2->ent_m2 |  |
| ce1 | m9 | stands | stand | stand |  | agent:m1->ent_m1 |  |
| ce2 | m10 | reads | read | read |  | agent:m4->ent_m4; patient:m0->None |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | hold | agent | m1 | ent_m1 | medium | e3 | nsubj -> holds |  |  |
| ce0 | hold | patient | m2 | ent_m2 | medium | e4 | dobj -> holds |  |  |
| ce1 | stand | agent | m1 | ent_m1 | medium | e5 | inherited agent conj -> holds |  |  |
| ce2 | read | agent | m4 | ent_m4 | medium | e6 | nsubj -> reads; resolved that -> sign |  |  |
| ce2 | read | patient | m0 |  | medium | e7 | dobj -> reads |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m4 | ent_m1 | ent_m4 | beside | high | e8 | False | False |
| cr1 | m1 | m6 | ent_m1 | ent_m6 | in | high | e9 | False | False |

### Stage 9 Canonicalization Notes
_none_

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | boy | boy | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | jersey | jersey | clothing | m1 | raw_mention |  |  |  |
| ent_m3 | object | soccer_ball | soccer ball | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | field | field | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | player | player | person | m6 | raw_mention |  |  |  |
| ent_m7 | object | jersey | jersey | clothing | m7 | raw_mention |  |  |  |
| ent_m9 | object | number | number | object | m9 | raw_mention |  |  |  |
| ent_m10 | object | child | children | person | m10 | raw_mention |  |  |  |
| ent_m12 | object | adult | adults | person | m12 | raw_mention |  |  |  |
| ent_m13 | context | background | background | object | m13 | raw_mention |  |  |  |
| ent_m14 | object | fence | fence | object | m14 | raw_mention |  |  |  |
| ent_m15 | object | building | building | object | m15 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | kicks | kick | kick |  | agent:m0->ent_m0; patient:m3->ent_m3 |  |
| ce1 | m17 | runs | run | run |  | agent:m6->ent_m6 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | kick | agent | m0 | ent_m0 | medium | e5 | nsubj -> kicks |  |  |
| ce0 | kick | patient | m3 | ent_m3 | medium | e6 | dobj -> kicks |  |  |
| ce1 | run | agent | m6 | ent_m6 | medium | e7 | nsubj -> runs |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e8 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | high | e9 | False | False |
| cr2 | m6 | m7 | ent_m6 | ent_m7 | in | high | e10 | False | False |
| cr3 | m7 | m9 | ent_m7 | ent_m9 | with | high | e11 | False | False |
| cr4 | m10 | m13 | ent_m10 | ent_m13 | in | high | e12 | False | False |
| cr5 | m10 | m14 | ent_m10 | ent_m14 | near | high | e13 | False | False |
| cr6 | m10 | m15 | ent_m10 | ent_m15 | near | high | e14 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | balloon | balloons | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | balloon | balloons | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | decor | decor | object | m4 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | lamp | lamp | object | m0 | raw_mention |  |  |  |
| ent_m4 | object | surface | surface | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | glass | glass | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | bulb | bulb | object | m8 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | building | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | car | cars | vehicle | m2 | raw_mention |  |  |  |
| ent_m4 | context | front | front | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | pillar | pillars | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | window | windows | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | parked | park | park |  | agent:m2->ent_m2 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | park | agent | m2 | ent_m2 | medium | e4 | inherited agent acl -> cars |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e5 | False | False |
| cr1 | m2 | m4 | ent_m2 | ent_m4 | in | high | e6 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | field | fields | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | tree | trees | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | valley | valley | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | sky | sky | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | pine_tree | Pine trees | object | m6 | raw_mention |  |  |  |
| ent_m7 | context | foreground | foreground | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | stretch | stretch | stretch |  | agent:m0->ent_m0; agent:m2->ent_m2 |  |
| ce1 | m9 | frame | frame | frame |  | agent:m6->ent_m6; patient:m7->ent_m7 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stretch | agent | m0 | ent_m0 | medium | e3 | nsubj -> stretch |  |  |
| ce0 | stretch | agent | m2 | ent_m2 | medium | e4 | nsubj -> stretch |  |  |
| ce1 | frame | agent | m6 | ent_m6 | medium | e5 | nsubj -> frame |  |  |
| ce1 | frame | patient | m7 | ent_m7 | medium | e6 | dobj -> frame |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | across | high | e7 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | under | high | e8 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | artifact | artifact | object | m1 | raw_mention |  |  |  |
| ent_m5 | context | top | top | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | base | base | object | m6 | raw_mention |  |  |  |
| ent_m8 | context | surface | surface | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | marker | marker | object | m9 | raw_mention |  |  |  |
| ent_m11 | object | size | size | object | m11 | raw_mention |  |  |  |
| ent_m13 | object | fragment | fragment | object | m13 | raw_mention |  |  |  |
| eref_m16 | reference | artifact | The object | object | m16 | stage9_reference | ent_m1 |  |  |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m16 | eref_m16 | m1 | ent_m1 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | rests | rest | rest |  | agent:m1->ent_m1 |  |
| ce1 | m18 | reads | read | read |  | agent:m9->ent_m9 |  |
| ce2 | m19 | indicating | indicate | indicate |  | agent:m9->ent_m9; patient:m11->ent_m11 |  |
| ce3 | m20 | appears | appear | appear |  | agent:m1->ent_m1 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | rest | agent | m1 | ent_m1 | medium | e8 | nsubj -> rests |  |  |
| ce1 | read | agent | m9 | ent_m9 | medium | e9 | nsubj -> reads |  |  |
| ce2 | indicate | agent | m9 | ent_m9 | medium | e10 | inherited agent advcl -> reads |  |  |
| ce2 | indicate | patient | m11 | ent_m11 | medium | e11 | dobj -> indicating |  |  |
| ce3 | appear | agent | m1 | ent_m1 | medium | e12 | nsubj -> appears; resolved object -> artifact |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m5 | ent_m1 | ent_m5 | with | high | e13 | False | False |
| cr1 | m1 | m6 | ent_m1 | ent_m6 | with | high | e14 | False | False |
| cr2 | m1 | m8 | ent_m1 | ent_m8 | on | high | e15 | False | False |
| cr3 | m9 | m1 | ent_m9 | ent_m1 | below | high | e16 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | tree | trees | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | bark | bark | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | clearing | clearing | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | branch | branches | object | m6 | raw_mention |  |  |  |
| ent_m7 | object | sunlight | sunlight | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | ground | ground | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | bush | bushes | object | m9 | raw_mention |  |  |  |
| ent_m11 | object | leaf | leaves | object | m11 | raw_mention |  |  |  |
| ent_m13 | object | floor | floor | object | m13 | raw_mention |  |  |  |
| ent_m15 | object | light | light | object | m15 | raw_mention |  |  |  |
| ent_m17 | object | spot | spots | object | m17 | raw_mention |  |  |  |
| ent_m19 | object | shadow | shadows | object | m19 | raw_mention |  |  |  |
| ent_m20 | context | scene | scene | object | m20 | raw_mention |  |  |  |
| ent_m21 | object | woodland | woodland | object | m21 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m23 | stand | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m24 | filtering | filter | filter |  | agent:m6->ent_m6; patient:m7->ent_m7 |  |
| ce2 | m25 | cover | cover | cover |  | agent:m9->ent_m9; agent:m11->ent_m11; patient:m13->ent_m13 |  |
| ce3 | m26 | creating | create | create |  | agent:m15->ent_m15; patient:m17->ent_m17 |  |
| ce4 | m27 | surrounded | surround | surround |  | agent:m20->ent_m20 |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e19 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | in | high | e20 | False | False |
| cr2 | m6 | m8 | ent_m6 | ent_m8 | onto | medium | e21 | False | False |
| cr3 | m15 | m19 | ent_m15 | ent_m19 | among | medium | e22 | False | False |
| cr4 | m20 | m21 | ent_m20 | ent_m21 | by | medium | e23 | False | False |

### Stage 9 Canonicalization Notes
_none_

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | player | player | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | uniform | uniform | clothing | m2 | raw_mention |  |  |  |
| ent_m4 | context | base | base | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | umpire | umpire | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | spectator | Spectators | object | m6 | raw_mention |  |  |  |
| ent_m7 | object | chair | chairs | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | fence | fence | object | m8 | raw_mention |  |  |  |
| ent_m9 | context | background | background | object | m9 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | stands | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m11 | walks | walk | walk |  | agent:m5->ent_m5 |  |
| ce2 | m12 | sit | sit | sit |  | agent:m6->ent_m6 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e3 | nsubj -> stands |  |  |
| ce1 | walk | agent | m5 | ent_m5 | medium | e4 | nsubj -> walks |  |  |
| ce2 | sit | agent | m6 | ent_m6 | medium | e5 | nsubj -> sit |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | high | e6 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | high | e7 | False | False |
| cr2 | m6 | m7 | ent_m6 | ent_m7 | in | high | e8 | False | False |
| cr3 | m6 | m8 | ent_m6 | ent_m8 | behind | high | e9 | False | False |
| cr4 | m6 | m9 | ent_m6 | ent_m9 | in | high | e10 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | church | church | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | cross | cross | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | tower | tower | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | sky | sky | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | entrance | entrance | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | building | building | object | m8 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | stands | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m10 | leads | lead | lead |  | agent:m6->ent_m6 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e3 | nsubj -> stands |  |  |
| ce1 | lead | agent | m6 | ent_m6 | medium | e4 | nsubj -> leads |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e5 | False | False |
| cr1 | m2 | m3 | ent_m2 | ent_m3 | on | high | e6 | False | False |
| cr2 | m0 | m4 | ent_m0 | ent_m4 | under | high | e7 | False | False |
| cr3 | m6 | m8 | ent_m6 | ent_m8 | into | medium | e8 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | sky | sky | object | m0 | raw_mention |  |  |  |
| ent_m4 | object | horizon | horizon | object | m4 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m5 | shows | show | show |  | agent:m0->ent_m0 |  |
| ce1 | m6 | fading | fade | fade |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | m0 | ent_m0 | medium | e1 | nsubj -> shows |  |  |
| ce1 | fade | agent | m0 | ent_m0 | medium | e2 | inherited agent ccomp -> shows |  |  |

### Stage 9 Canonical Relations
_none_

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | woman | woman | person | m1 | raw_mention |  |  |  |
| ent_m2 | object | room | room | object | m2 | raw_mention |  |  |  |
| ent_m5 | object | woman | woman | person | m5 | raw_mention |  |  |  |
| ent_m6 | object | rose | rose | object | m6 | raw_mention |  |  |  |
| ent_m9 | object | ribbon | ribbon | object | m9 | raw_mention |  |  |  |
| ent_m10 | object | top | top | object | m10 | raw_mention |  |  |  |
| ent_m13 | object | earring | earrings | object | m13 | raw_mention |  |  |  |
| ent_m16 | object | camera | camera | device | m16 | raw_mention |  |  |  |
| ent_m17 | object | smile | smiles | object | m17 | raw_mention |  |  |  |
| ent_m19 | group | man_and_woman | A man and a woman | group | m19 | raw_mention |  |  |  |
| eref_m20 | group | man_and_woman | Both | person | m20 | stage9_reference_group_repair | ent_m19 |  | 2 |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m20 | eref_m20 | m19 | ent_m19 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m21 | sit | sit | sit |  | agent:m0->ent_m0; agent:m1->ent_m1 |  |
| ce1 | m22 | holds | hold | hold |  | agent:m5->ent_m5; patient:m6->ent_m6 |  |
| ce2 | m23 | wearing | wear | wear |  | agent:m5->ent_m5; patient:m10->ent_m10; patient:m13->ent_m13 |  |
| ce3 | m24 | look | look | look |  | agent:m19->eref_m20 |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | high | e19 | False | False |
| cr1 | m6 | m9 | ent_m6 | ent_m9 | with | high | e20 | False | False |
| cr2 | m19 | m16 | eref_m20 | ent_m16 | toward | medium | e21 | False | False |
| cr3 | m19 | m17 | ent_m19 | ent_m17 | with | high | e22 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | men | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | uniform | uniforms | clothing | m2 | raw_mention |  |  |  |
| ent_m4 | object | mat | mat | object | m4 | raw_mention |  |  |  |
| ent_m7 | object | gym | gym | object | m7 | raw_mention |  |  |  |
| ent_m8 | context | top | top | object | m8 | raw_mention |  |  |  |
| ent_m9 | context | back | back | object | m9 | raw_mention |  |  |  |
| ent_m10 | object | fence | fence | object | m10 | raw_mention |  |  |  |
| ent_m12 | object | person | person | person | m12 | raw_mention |  |  |  |
| ent_m14 | object | gear | gear | object | m14 | raw_mention |  |  |  |
| eref_m16 | instance | man | One | person | m16 | stage9_reference | ent_m0 |  | 1 |
| eref_m17 | contrastive_instance | man | other | person | m17 | stage9_reference | ent_m0 |  | 1 |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m16 | eref_m16 | m0 | ent_m0 | high |  |
| refers_to | m17 | eref_m17 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m18 | grappling | grapple | grapple |  | agent:m0->ent_m0 |  |
| ce1 | m19 | controlling | control | control |  | agent:m0->ent_m0; patient:m0->eref_m17 |  |
| ce2 | m20 | lying | lie | lie |  | agent:m0->eref_m17 |  |
| ce3 | m21 | bent | bend | bend_over | over | agent:m12->ent_m12 | phrasal_action:bend over |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | grapple | agent | m0 | ent_m0 | medium | e9 | nsubj -> grappling |  |  |
| ce1 | control | agent | m0 | ent_m0 | medium | e10 | inherited agent advcl -> is |  |  |
| ce1 | control | patient | m0 | eref_m17 | medium |  | dobj -> controlling; resolved other -> men | pronoun_resolved_to_action_agent |  |
| ce2 | lie | agent | m0 | eref_m17 | medium | e11 | inherited agent relcl -> other |  |  |
| ce3 | bend_over | agent | m12 | ent_m12 | medium | e13 | inherited agent acomp -> is |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | high | e14 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | high | e15 | False | False |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | inside | high | e16 | False | False |
| cr3 | m0 | m8 | ent_m0 | ent_m8 | on | high | e17 | False | False |
| cr4 | m12 | m14 | ent_m12 | ent_m14 | in | high | e18 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | wall | wall | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | sign | signs | document | m2 | raw_mention |  |  |  |
| ent_m6 | object | chinese | Chinese | object | m6 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | walks | walk | walk |  | agent:m0->ent_m0 |  |
| ce1 | m8 | covered | cover | cover |  | agent:m1->ent_m1 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | walk | agent | m0 | ent_m0 | medium | e3 | nsubj -> walks |  |  |
| ce1 | cover | agent | m1 | ent_m1 | medium | e4 | inherited agent acl -> wall |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | past | medium | e5 | False | False |
| cr1 | m1 | m2 | ent_m1 | ent_m2 | with | high | e6 | False | False |
| cr2 | m2 | m6 | ent_m2 | ent_m6 | in | high | e7 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | drink | drink | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | pool | pool | object | m2 | raw_mention |  |  |  |
| ent_m3 | context | night | night | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | chair | chair | object | m4 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | grandparent | grandparent | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | child | child | person | m1 | raw_mention |  |  |  |
| ent_m2 | object | car | car | vehicle | m2 | raw_mention |  |  |  |
| ent_m4 | object | shirt | shirt | clothing | m4 | raw_mention |  |  |  |
| ent_m6 | object | shirt | shirt | clothing | m6 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | soccer_player | soccer player | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | uniform | uniform | clothing | m1 | raw_mention |  |  |  |
| ent_m3 | object | ball | ball | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | field | field | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | player | player | person | m6 | raw_mention |  |  |  |
| ent_m7 | object | uniform | uniform | clothing | m7 | raw_mention |  |  |  |
| ent_m10 | object | spectator | spectators | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | tent | tents | object | m11 | raw_mention |  |  |  |
| ent_m12 | context | background | background | object | m12 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m13 | controls | control | control |  | agent:m0->ent_m0; patient:m3->ent_m3 |  |
| ce1 | m14 | stands | stand | stand |  | agent:m6->ent_m6 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | control | agent | m0 | ent_m0 | medium | e5 | nsubj -> controls |  |  |
| ce0 | control | patient | m3 | ent_m3 | medium | e6 | dobj -> controls |  |  |
| ce1 | stand | agent | m6 | ent_m6 | medium | e7 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e8 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | high | e9 | False | False |
| cr2 | m6 | m7 | ent_m6 | ent_m7 | in | high | e10 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | pipe | pipe | object | m0 | raw_mention |  |  |  |
| ent_m4 | object | hillside | hillside | object | m4 | raw_mention |  |  |  |
| ent_m7 | object | block | blocks | object | m7 | raw_mention |  |  |  |
| ent_m9 | object | foliage | foliage | object | m9 | raw_mention |  |  |  |
| ent_m11 | object | tree | trees | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | sunlight | sunlight | object | m12 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m14 | runs | run | run |  | agent:m0->ent_m0 |  |
| ce1 | m15 | supported | support | support |  | theme:m0->ent_m0; by_agent_or_causer:m7->ent_m7; by_agent_or_causer:m9->ent_m9; by_agent_or_causer:m11->ent_m11 |  |
| ce2 | m16 | surrounded | surround | surround |  | agent:m0->ent_m0 |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | across | high | e11 | False | False |
| cr1 | m0 | m7 | ent_m0 | ent_m7 | by | medium | e12 | True | False |
| cr2 | m0 | m9 | ent_m0 | ent_m9 | by | medium | e13 | True | False |
| cr3 | m0 | m11 | ent_m0 | ent_m11 | by | medium | e14 | True | False |
| cr4 | m0 | m12 | ent_m0 | ent_m12 | under | high | e15 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | hair | hair | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | hand | hands | object | m3 | raw_mention |  |  |  |
| ent_m5 | context | background | background | object | m5 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | speaks | speak | speak |  | agent:m0->ent_m0 |  |
| ce1 | m8 | gesturing | gesture | gesture |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | speak | agent | m0 | ent_m0 | medium | e4 | nsubj -> speaks |  |  |
| ce1 | gesture | agent | m0 | ent_m0 | medium | e5 | inherited agent advcl -> speaks |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | with | high | e6 | False | False |
| cr1 | m0 | m3 | ent_m0 | ent_m3 | with | high | e7 | False | False |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | against | high | e8 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | crater | crater | object | m0 | raw_mention |  |  |  |
| ent_m3 | object | mist | mist | object | m3 | raw_mention |  |  |  |
| ent_m4 | context | edge | edge | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | ground | ground | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | stone | stones | object | m6 | raw_mention |  |  |  |
| ent_m9 | object | patch | patches | object | m9 | raw_mention |  |  |  |
| ent_m10 | object | material | material | object | m10 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | rising | rise | rise |  | agent:m3->ent_m3 |  |
| ce1 | m13 | covered | cover | cover |  | theme:m5->ent_m5 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | rise | agent | m3 | ent_m3 | medium | e5 | inherited agent acl -> mist |  |  |
| ce1 | cover | theme | m5 | ent_m5 | medium | e6 | nsubjpass -> covered |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | with | high | e7 | False | False |
| cr1 | m3 | m4 | ent_m3 | ent_m4 | from | medium | e8 | False | False |
| cr2 | m5 | m6 | ent_m5 | ent_m6 | in | high | e9 | False | False |
| cr3 | m5 | m9 | ent_m5 | ent_m9 | in | high | e10 | False | False |
| cr4 | m9 | m10 | ent_m9 | ent_m10 | of | medium | e11 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | table | table | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | statistic | statistics | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | region | regions | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | empire | Empire | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | number | numbers | object | m6 | raw_mention |  |  |  |
| ent_m7 | object | percentage | percentages | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | shows | show | show |  | agent:m0->ent_m0; patient:m1->ent_m1 |  |
| ce1 | m9 | including | include | include |  | agent:m1->ent_m1; patient:m6->ent_m6; patient:m7->ent_m7 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | m0 | ent_m0 | medium | e2 | nsubj -> shows |  |  |
| ce0 | show | patient | m1 | ent_m1 | medium | e3 | dobj -> shows |  |  |
| ce1 | include | agent | m1 | ent_m1 | medium | e4 | inherited agent prep -> statistics |  |  |
| ce1 | include | patient | m6 | ent_m6 | medium | e5 | pobj -> including |  |  |
| ce1 | include | patient | m7 | ent_m7 | medium | e6 | pobj -> including |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | for | medium | e7 | False | False |
| cr1 | m2 | m4 | ent_m2 | ent_m4 | of | medium | e8 | False | False |
| cr2 | m1 | m6 | ent_m1 | ent_m6 | include | medium | e9 | False | False |
| cr3 | m1 | m7 | ent_m1 | ent_m7 | include | medium | e10 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | dog | dog | animal | m0 | raw_mention |  |  |  |
| ent_m2 | object | eye | eyes | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | mouth | mouth | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | room | room | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | balloon | balloon | object | m8 | raw_mention |  |  |  |
| ent_m11 | context | right | right | object | m11 | raw_mention |  |  |  |
| ent_m12 | context | background | background | object | m12 | raw_mention |  |  |  |
| ent_m14 | object | dog | dog | animal | m14 | raw_mention |  |  |  |
| ent_m15 | object | camera | camera | device | m15 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | stands | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m17 | contrasting | contrast | contrast |  | agent:m8->ent_m8 |  |
| ce2 | m18 | appears | appear | appear |  | agent:m14->ent_m14 |  |
| ce3 | m19 | looking | look | look |  | agent:m14->ent_m14 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e8 | nsubj -> stands |  |  |
| ce1 | contrast | agent | m8 | ent_m8 | medium | e9 | inherited agent advcl -> is |  |  |
| ce2 | appear | agent | m14 | ent_m14 | medium | e10 | nsubj -> appears |  |  |
| ce3 | look | agent | m14 | ent_m14 | medium | e11 | inherited agent xcomp -> appears |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e12 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | with | high | e13 | False | False |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | in | high | e14 | False | False |
| cr3 | m8 | m12 | ent_m8 | ent_m12 | with | high | e15 | False | False |
| cr4 | m14 | m15 | ent_m14 | ent_m15 | at | medium | e16 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | building | building | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | section | section | object | m2 | raw_mention |  |  |  |
| ent_m5 | object | trim | trim | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | fence | fence | object | m7 | raw_mention |  |  |  |
| ent_m9 | object | area | area | object | m9 | raw_mention |  |  |  |
| ent_m11 | object | puddle | puddles | object | m11 | raw_mention |  |  |  |
| ent_m12 | context | foreground | foreground | object | m12 | raw_mention |  |  |  |
| ent_m13 | object | stair | stairs | object | m13 | raw_mention |  |  |  |
| ent_m14 | object | entrance | entrance | object | m14 | raw_mention |  |  |  |
| ent_m16 | object | sky | sky | object | m16 | raw_mention |  |  |  |
| ent_m17 | object | grass | grass | object | m17 | raw_mention |  |  |  |
| eref_m19 | reference | building | the structure | object | m19 | stage9_reference | ent_m0 |  |  |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m19 | eref_m19 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m20 | stands | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m21 | lead | lead | lead | up | agent:m13->ent_m13 |  |
| ce2 | m23 | grows | grow | grow |  | agent:m17->ent_m17 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e9 | nsubj -> stands |  |  |
| ce1 | lead | agent | m13 | ent_m13 | medium | e10 | nsubj -> lead |  |  |
| ce2 | grow | agent | m17 | ent_m17 | medium | e12 | nsubj -> grows |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e13 | False | False |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | with | high | e14 | False | False |
| cr2 | m0 | m7 | ent_m0 | ent_m7 | behind | high | e15 | False | False |
| cr3 | m9 | m11 | ent_m9 | ent_m11 | with | high | e16 | False | False |
| cr4 | m9 | m12 | ent_m9 | ent_m12 | in | high | e17 | False | False |
| cr5 | m13 | m14 | ent_m13 | ent_m14 | to | medium | e18 | False | False |
| cr6 | m17 | m0 | ent_m17 | ent_m0 | base_of | medium | e19 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | man | man | person | m1 | raw_mention |  |  |  |
| ent_m2 | object | suit | suit | clothing | m2 | raw_mention |  |  |  |
| ent_m4 | object | podium | podium | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | microphone | microphones | object | m6 | raw_mention |  |  |  |
| ent_m7 | context | left | left | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | man | man | person | m8 | raw_mention |  |  |  |
| ent_m9 | object | suit | suit | clothing | m9 | raw_mention |  |  |  |
| ent_m11 | object | mask | mask | clothing | m11 | raw_mention |  |  |  |
| ent_m12 | context | right | right | object | m12 | raw_mention |  |  |  |
| ent_m13 | object | woman | woman | person | m13 | raw_mention |  |  |  |
| ent_m14 | object | jacket | jacket | clothing | m14 | raw_mention |  |  |  |
| ent_m16 | object | mask | mask | clothing | m16 | raw_mention |  |  |  |
| ent_m17 | object | backdrop | backdrop | object | m17 | raw_mention |  |  |  |
| ent_m18 | object | logo | logos | object | m18 | raw_mention |  |  |  |
| ent_m19 | object | text | text | document | m19 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m20 | stands | stand | stand |  | agent:m1->ent_m1 |  |
| ce1 | m21 | speaking | speak | speak |  | agent:m1->ent_m1 |  |
| ce2 | m22 | sits | sit | sit |  | agent:m8->ent_m8 |  |
| ce3 | m23 | sits | sit | sit |  | agent:m13->ent_m13 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m1 | ent_m1 | medium | e4 | nsubj -> stands |  |  |
| ce1 | speak | agent | m1 | ent_m1 | medium | e5 | inherited agent advcl -> stands |  |  |
| ce2 | sit | agent | m8 | ent_m8 | medium | e6 | nsubj -> sits |  |  |
| ce3 | sit | agent | m13 | ent_m13 | medium | e7 | nsubj -> sits |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | in | high | e8 | False | False |
| cr1 | m1 | m4 | ent_m1 | ent_m4 | at | medium | e9 | False | False |
| cr2 | m1 | m6 | ent_m1 | ent_m6 | into | medium | e10 | False | False |
| cr3 | m8 | m7 | ent_m8 | ent_m7 | to | medium | e11 | False | False |
| cr4 | m8 | m9 | ent_m8 | ent_m9 | in | high | e12 | False | False |
| cr5 | m13 | m12 | ent_m13 | ent_m12 | to | medium | e13 | False | False |
| cr6 | m13 | m14 | ent_m13 | ent_m14 | in | high | e14 | False | False |
| cr7 | m13 | m17 | ent_m13 | ent_m17 | in_front_of | high | e15 | False | False |
| cr8 | m17 | m18 | ent_m17 | ent_m18 | with | high | e16 | False | False |
| cr9 | m17 | m19 | ent_m17 | ent_m19 | with | high | e17 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | pipe | pipe | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | concrete | concrete | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | dirt | dirt | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | glove | gloves | object | m4 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hand | hand | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | phone | phone | device | m2 | raw_mention |  |  |  |
| ent_m3 | object | ledge | ledge | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | town | town | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | town | town | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | building | buildings | object | m8 | raw_mention |  |  |  |
| ent_m11 | object | roof | roofs | object | m11 | raw_mention |  |  |  |
| ent_m14 | object | tree | trees | object | m14 | raw_mention |  |  |  |
| ent_m16 | object | sky | sky | object | m16 | raw_mention |  |  |  |
| ent_m18 | object | hill | hills | object | m18 | raw_mention |  |  |  |
| ent_m20 | object | cloud | clouds | object | m20 | raw_mention |  |  |  |
| ent_m22 | object | horizon | horizon | object | m22 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m23 | holds | hold | hold |  | agent:m0->ent_m0; patient:m2->ent_m2 |  |
| ce1 | m24 | overlooking | overlook | overlook |  | agent:m3->ent_m3; patient:m5->ent_m5 |  |
| ce2 | m25 | features | feature | feature |  | agent:m7->ent_m7; patient:m8->ent_m8 |  |
| ce3 | m26 | nestled | nestle | nestle |  | agent:m8->ent_m8 |  |
| ce4 | m27 | complete | complete | complete |  | agent:m18->ent_m18; agent:m20->ent_m20; patient:m22->ent_m22 |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m3 | ent_m0 | ent_m3 | on | high | e21 | False | False |
| cr1 | m8 | m11 | ent_m8 | ent_m11 | with | high | e22 | False | False |
| cr2 | m8 | m14 | ent_m8 | ent_m14 | among | medium | e23 | False | False |
| cr3 | m14 | m16 | ent_m14 | ent_m16 | under | high | e24 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | outfit | outfit | object | m1 | raw_mention |  |  |  |
| ent_m4 | object | belt | belt | object | m4 | raw_mention |  |  |  |
| ent_m7 | object | chandelier | chandeliers | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | ceiling | ceiling | object | m8 | raw_mention |  |  |  |
| ent_m9 | object | duct | ducts | object | m9 | raw_mention |  |  |  |
| ent_m11 | context | indoors | indoors | object | m11 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | holds | hold | hold_up | up | agent:m0->ent_m0; patient:m4->ent_m4 | phrasal_action:hold up |
| ce1 | m14 | stands | stand | stand |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | hold_up | agent | m0 | ent_m0 | medium | e6 | nsubj -> holds |  |  |
| ce0 | hold_up | patient | m4 | ent_m4 | medium | e8 | dobj -> holds |  |  |
| ce1 | stand | agent | m0 | ent_m0 | medium | e9 | nsubj -> stands; resolved She -> woman |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e10 | False | False |
| cr1 | m0 | m7 | ent_m0 | ent_m7 | under | high | e11 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | people | People | person | m1 | raw_mention |  |  |  |
| ent_m2 | object | suit | suits | clothing | m2 | raw_mention |  |  |  |
| ent_m3 | object | desk | desks | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | chamber | chamber | object | m5 | raw_mention |  |  |  |
| ent_m8 | object | screen | screen | device | m8 | raw_mention |  |  |  |
| ent_m10 | object | text | text | document | m10 | raw_mention |  |  |  |
| ent_m11 | object | portuguese | Portuguese | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | individual | individuals | object | m12 | raw_mention |  |  |  |
| ent_m14 | context | front | front | object | m14 | raw_mention |  |  |  |
| ent_m15 | object | screen | screen | device | m15 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m16 | sit | sit | sit |  | agent:m1->ent_m1 |  |
| ce1 | m17 | displays | display | display |  | agent:m8->ent_m8; patient:m10->ent_m10 |  |
| ce2 | m18 | including | include | include |  | agent:m10->ent_m10; patient:m0->None |  |
| ce3 | m19 | seated | seat | seat |  | theme:m12->ent_m12 |  |
| ce4 | m20 | standing | stand | stand |  | agent:m12->ent_m12 |  |
| ce5 | m21 | facing | face | face |  | agent:m12->ent_m12; patient:m15->ent_m15 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | sit | agent | m1 | ent_m1 | medium | e5 | nsubj -> sit |  |  |
| ce1 | display | agent | m8 | ent_m8 | medium | e6 | nsubj -> displays |  |  |
| ce1 | display | patient | m10 | ent_m10 | medium | e7 | dobj -> displays |  |  |
| ce2 | include | agent | m10 | ent_m10 | medium | e8 | inherited agent prep -> text |  |  |
| ce2 | include | patient | m0 |  | medium | e9 | pobj -> including |  |  |
| ce3 | seat | theme | m12 | ent_m12 | medium | e10 | nsubjpass -> seated |  |  |
| ce4 | stand | agent | m12 | ent_m12 | medium | e11 | inherited agent conj -> seated |  |  |
| ce5 | face | agent | m12 | ent_m12 | medium | e12 | inherited agent conj -> standing |  |  |
| ce5 | face | patient | m15 | ent_m15 | medium | e13 | dobj -> facing |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m2 | ent_m1 | ent_m2 | in | high | e14 | False | False |
| cr1 | m1 | m3 | ent_m1 | ent_m3 | at | medium | e15 | False | False |
| cr2 | m1 | m5 | ent_m1 | ent_m5 | in | high | e16 | False | False |
| cr3 | m10 | m11 | ent_m10 | ent_m11 | in | high | e17 | False | False |
| cr4 | m10 | m0 | ent_m10 |  | include | medium | e18 | False | False |
| cr5 | m12 | m14 | ent_m12 | ent_m14 | near | high | e19 | False | False |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | medal | medal | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | ribbon | ribbon | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | pin | pin | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | cross | cross | object | m4 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | slab | slab | object | m0 | raw_mention |  |  |  |
| ent_m4 | context | surface | surface | object | m4 | raw_mention |  |  |  |
| ent_m5 | context | background | background | object | m5 | raw_mention |  |  |  |
| ent_m9 | object | texture | texture | object | m9 | raw_mention |  |  |  |
| ent_m11 | object | imperfection | imperfections | object | m11 | raw_mention |  |  |  |
| ent_m13 | object | stone | stone | object | m13 | raw_mention |  |  |  |
| ent_m14 | object | metal | metal | object | m14 | raw_mention |  |  |  |
| ent_m15 | object | edge | edges | object | m15 | raw_mention |  |  |  |
| eref_m16 | reference | slab | The object | object | m16 | stage9_reference | ent_m0 |  |  |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m16 | eref_m16 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m17 | rests | rest | rest |  | agent:m0->ent_m0 |  |
| ce1 | m18 | has | have | have |  | agent:m0->ent_m0; patient:m9->ent_m9; patient:m11->ent_m11 |  |
| ce2 | m19 | suggesting | suggest | suggest |  | agent:m0->ent_m0 |  |
| ce3 | m20 | made | make | make |  | theme:m0->ent_m0 |  |
| ce4 | m21 | appears | appear | appear |  | agent:m15->ent_m15 |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m4 | ent_m0 | ent_m4 | with | high | e16 | False | False |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | on | high | e17 | False | False |
| cr2 | m0 | m13 | ent_m0 | ent_m13 | of | medium | e18 | False | False |
| cr3 | m0 | m14 | ent_m0 | ent_m14 | of | medium | e19 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | tree | trees | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | hill | hill | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | sky | sky | object | m4 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | stand | stand | stand |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e4 | nsubj -> stand |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | on | high | e5 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | under | high | e6 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | hair | hair | object | m2 | raw_mention |  |  |  |
| ent_m5 | object | shirt | shirt | clothing | m5 | raw_mention |  |  |  |
| ent_m9 | object | earring | earrings | object | m9 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m12 | smiles | smile | smile |  | agent:m0->ent_m0 |  |
| ce1 | m13 | wearing | wear | wear |  | agent:m0->ent_m0; patient:m5->ent_m5; patient:m9->ent_m9 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | smile | agent | m0 | ent_m0 | medium | e8 | nsubj -> smiles |  |  |
| ce1 | wear | agent | m0 | ent_m0 | medium | e9 | inherited agent advcl -> smiles |  |  |
| ce1 | wear | patient | m5 | ent_m5 | medium | e10 | dobj -> wearing |  |  |
| ce1 | wear | patient | m9 | ent_m9 | medium | e11 | dobj -> wearing |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e12 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | football_player | Football players | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | uniform | uniforms | clothing | m1 | raw_mention |  |  |  |
| ent_m4 | object | field | field | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | game | game | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | referee | referee | person | m6 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | run | run | run |  | agent:m0->ent_m0 |  |
| ce1 | m10 | stands | stand | stand |  | agent:m6->ent_m6 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | run | agent | m0 | ent_m0 | medium | e2 | nsubj -> run |  |  |
| ce1 | stand | agent | m6 | ent_m6 | medium | e3 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e4 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | on | high | e5 | False | False |
| cr2 | m0 | m5 | ent_m0 | ent_m5 | during | medium | e6 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | text | text | document | m0 | raw_mention |  |  |  |
| ent_m1 | object | page | page | document | m1 | raw_mention |  |  |  |
| ent_m2 | object | book | book | document | m2 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | ocean | ocean | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | tree | trees | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | sky | sky | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | coastline | coastline | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | wave | waves | object | m5 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | boy | boys | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | table | table | object | m2 | raw_mention |  |  |  |
| ent_m5 | object | bet | bets | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | chip | chips | object | m6 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m7 | stand | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m8 | placing | place | place |  | agent:m0->ent_m0; patient:m5->ent_m5 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e3 | nsubj -> stand |  |  |
| ce1 | place | agent | m0 | ent_m0 | medium | e4 | inherited agent advcl -> stand |  |  |
| ce1 | place | patient | m5 | ent_m5 | medium | e5 | dobj -> placing |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | around | high | e6 | False | False |
| cr1 | m0 | m6 | ent_m0 | ent_m6 | with | high | e7 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | dump_truck | dump truck | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | bed | bed | object | m1 | raw_mention |  |  |  |
| ent_m3 | context | nighttime | nighttime | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | street_light | street light | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | ground | ground | object | m5 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | woman | woman | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | grass | grass | object | m1 | raw_mention |  |  |  |
| ent_m2 | object | plant | plant | object | m2 | raw_mention |  |  |  |
| ent_m5 | object | person | person | person | m5 | raw_mention |  |  |  |
| ent_m6 | object | shoe | shoes | clothing | m6 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m8 | kneels | kneel | kneel |  | agent:m0->ent_m0 |  |
| ce1 | m9 | planting | plant | plant |  | agent:m0->ent_m0; patient:m2->ent_m2 |  |
| ce2 | m10 | stands | stand | stand |  | agent:m5->ent_m5 |  |
| ce3 | m11 | wearing | wear | wear |  | agent:m5->ent_m5; patient:m6->ent_m6 |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e9 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | men | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | fire | fire | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | food | food | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | pan | pan | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | flame | flames | object | m6 | raw_mention |  |  |  |
| ent_m7 | object | fire | fire | object | m7 | raw_mention |  |  |  |
| ent_m8 | object | ground | ground | object | m8 | raw_mention |  |  |  |
| ent_m9 | context | outdoors | outdoors | object | m9 | raw_mention |  |  |  |
| eref_m10 | instance | man | one | person | m10 | stage9_reference | ent_m0 |  | 1 |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m10 | eref_m10 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m11 | stand | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m12 | stirring | stir | stir |  | agent:m0->eref_m10; patient:m4->ent_m4 |  |
| ce2 | m13 | burns | burn | burn |  | agent:m7->ent_m7 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e4 | nsubj -> stand |  |  |
| ce1 | stir | agent | m0 | eref_m10 | medium | e5 | nsubj -> stirring; resolved one -> men |  |  |
| ce1 | stir | patient | m4 | ent_m4 | medium | e6 | dobj -> stirring |  |  |
| ce2 | burn | agent | m7 | ent_m7 | medium | e7 | nsubj -> burns |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | near | high | e8 | False | False |
| cr1 | m0 | m5 | ent_m0 | ent_m5 | in | high | e9 | False | False |
| cr2 | m0 | m6 | ent_m0 | ent_m6 | over | high | e10 | False | False |
| cr3 | m7 | m8 | ent_m7 | ent_m8 | on | high | e11 | False | False |

### Stage 9 Canonicalization Notes
_none_

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m1 | object | tag | tag | object | m1 | raw_mention |  |  |  |
| ent_m4 | object | number | number | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | garment | garment | object | m5 | raw_mention |  |  |  |
| ent_m8 | object | tag | tag | object | m8 | raw_mention |  |  |  |
| ent_m9 | context | edge | edges | object | m9 | raw_mention |  |  |  |
| ent_m10 | object | fabric | fabric | object | m10 | raw_mention |  |  |  |
| ent_m13 | object | clothing | clothing | object | m13 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m14 | stitched | stitch | stitch |  | theme:m1->ent_m1 |  |
| ce1 | m15 | frayed | fray | fray |  | theme:m8->ent_m8 |  |
| ce2 | m16 | sits | sit | sit |  | agent:m8->ent_m8 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stitch | theme | m1 | ent_m1 | medium | e7 | nsubjpass -> stitched |  |  |
| ce1 | fray | theme | m8 | ent_m8 | medium | e8 | nsubjpass -> frayed |  |  |
| ce2 | sit | agent | m8 | ent_m8 | medium | e9 | inherited agent conj -> frayed |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m1 | m4 | ent_m1 | ent_m4 | with | high | e10 | False | False |
| cr1 | m1 | m5 | ent_m1 | ent_m5 | onto | medium | e11 | False | False |
| cr2 | m8 | m9 | ent_m8 | ent_m9 | at | medium | e12 | False | False |
| cr3 | m8 | m10 | ent_m8 | ent_m10 | against | high | e13 | False | False |
| cr4 | m10 | m13 | ent_m10 | ent_m13 | of | medium | e14 | False | False |

### Stage 9 Canonicalization Notes
| kind | action_mention | raw_edge | target | canonical_target | reason | full_note |
| --- | --- | --- | --- | --- | --- | --- |
| passive_subject_to_theme | m14 | e7 | m1 |  |  | {"action_mention_id": "m14", "kind": "passive_subject_to_theme", "raw_edge_id": "e7", "target": "m1"} |
| passive_subject_to_theme | m15 | e8 | m8 |  |  | {"action_mention_id": "m15", "kind": "passive_subject_to_theme", "raw_edge_id": "e8", "target": "m8"} |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hill | hill | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | forest | forest | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | tree | trees | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | foliage | foliage | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | slope | slope | object | m5 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hall | hall | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | speaker | speaker | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | chair | chairs | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | screen | screen | device | m5 | raw_mention |  |  |  |
| ent_m7 | object | banner | banner | object | m7 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | man | man | person | m0 | raw_mention |  |  |  |
| ent_m1 | object | suit | suit | clothing | m1 | raw_mention |  |  |  |
| ent_m2 | object | officer | officers | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | uniform | uniforms | clothing | m4 | raw_mention |  |  |  |
| ent_m6 | object | hat | hats | object | m6 | raw_mention |  |  |  |
| ent_m7 | object | building | building | object | m7 | raw_mention |  |  |  |
| ent_m9 | context | outdoors | outdoors | object | m9 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m10 | stands | stand | stand |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e4 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | in | high | e5 | False | False |
| cr1 | m0 | m2 | ent_m0 | ent_m2 | with | high | e6 | False | False |
| cr2 | m2 | m4 | ent_m2 | ent_m4 | in | high | e7 | False | False |
| cr3 | m2 | m6 | ent_m2 | ent_m6 | in | high | e8 | False | False |
| cr4 | m0 | m7 | ent_m0 | ent_m7 | near | high | e9 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | hillside | hillside | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | river | river | object | m2 | raw_mention |  |  |  |
| ent_m5 | object | lake | lake | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | mountain | mountains | object | m7 | raw_mention |  |  |  |
| ent_m8 | context | background | background | object | m8 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | overlooks | overlook | overlook |  | agent:m0->ent_m0; patient:m2->ent_m2; patient:m5->ent_m5 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | overlook | agent | m0 | ent_m0 | medium | e5 | nsubj -> overlooks |  |  |
| ce0 | overlook | patient | m2 | ent_m2 | medium | e6 | dobj -> overlooks |  |  |
| ce0 | overlook | patient | m5 | ent_m5 | medium | e7 | dobj -> overlooks |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m7 | ent_m0 | ent_m7 | with | high | e8 | False | False |
| cr1 | m7 | m8 | ent_m7 | ent_m8 | in | high | e9 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | backpack | backpack | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | sign | sign | document | m2 | raw_mention |  |  |  |
| ent_m4 | object | booth | booth | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | person | person | person | m6 | raw_mention |  |  |  |
| ent_m7 | context | indoor | indoor | object | m7 | raw_mention |  |  |  |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | close-up | close-up | object | m0 | raw_mention |  |  |  |
| ent_m1 | object | bee | bee | object | m1 | raw_mention |  |  |  |
| ent_m3 | object | body | body | object | m3 | raw_mention |  |  |  |
| ent_m5 | object | wing | wings | object | m5 | raw_mention |  |  |  |
| ent_m7 | context | surface | surface | object | m7 | raw_mention |  |  |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m1 | ent_m0 | ent_m1 | of | medium | e4 | False | False |
| cr1 | m1 | m3 | ent_m1 | ent_m3 | with | high | e5 | False | False |
| cr2 | m1 | m5 | ent_m1 | ent_m5 | with | high | e6 | False | False |
| cr3 | m0 | m7 | ent_m0 | ent_m7 | on | high | e7 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | church_tower | church tower | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | roof | roof | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | sky | sky | object | m4 | raw_mention |  |  |  |
| ent_m7 | object | tree | trees | object | m7 | raw_mention |  |  |  |
| ent_m9 | object | wall | wall | object | m9 | raw_mention |  |  |  |
| ent_m11 | context | foreground | foreground | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | hillside | hillside | object | m12 | raw_mention |  |  |  |
| ent_m13 | object | building | building | object | m13 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m14 | stands | stand | stand |  | agent:m0->ent_m0 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | stand | agent | m0 | ent_m0 | medium | e7 | nsubj -> stands |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e8 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | against | high | e9 | False | False |
| cr2 | m7 | m11 | ent_m7 | ent_m11 | in | high | e10 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | people | people | person | m0 | raw_mention |  |  |  |
| ent_m2 | object | lab_coat | lab coats | object | m2 | raw_mention |  |  |  |
| ent_m4 | object | table | table | object | m4 | raw_mention |  |  |  |
| ent_m6 | object | flask | flask | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | man | men | person | m8 | raw_mention |  |  |  |
| ent_m10 | object | goggle | goggles | object | m10 | raw_mention |  |  |  |
| ent_m11 | object | liquid | liquids | object | m11 | raw_mention |  |  |  |
| ent_m12 | object | flask | flasks | object | m12 | raw_mention |  |  |  |
| ent_m13 | object | woman | woman | person | m13 | raw_mention |  |  |  |
| ent_m14 | object | hijab | hijab | object | m14 | raw_mention |  |  |  |
| ent_m16 | object | logo | logo | object | m16 | raw_mention |  |  |  |
| ent_m17 | object | text | text | document | m17 | raw_mention |  |  |  |
| ent_m18 | object | bottom | bottom | object | m18 | raw_mention |  |  |  |
| ent_m19 | object | image | image | object | m19 | raw_mention |  |  |  |
| eref_m20 | reference | people | each | person | m20 | stage9_reference | ent_m0 |  |  |

### Stage 9 Entity Links
| link_type | source_mention | source_entity | target_mention | target_entity | confidence | reason |
| --- | --- | --- | --- | --- | --- | --- |
| refers_to | m20 | eref_m20 | m0 | ent_m0 | high |  |

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m21 | stand | stand | stand |  | agent:m0->ent_m0 |  |
| ce1 | m22 | holding | hold | hold |  | agent:m0->eref_m20; patient:m6->ent_m6 |  |
| ce2 | m23 | wear | wear | wear |  | agent:m8->ent_m8; patient:m10->ent_m10 |  |
| ce3 | m24 | pour | pour | pour |  | agent:m8->ent_m8; patient:m11->ent_m11 |  |
| ce4 | m25 | stands | stand | stand |  | agent:m13->ent_m13 |  |

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
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | in | high | e14 | False | False |
| cr1 | m0 | m4 | ent_m0 | ent_m4 | at | medium | e15 | False | False |
| cr2 | m8 | m12 | ent_m8 | ent_m12 | into | medium | e16 | False | False |
| cr3 | m13 | m14 | ent_m13 | ent_m14 | in | high | e17 | False | False |
| cr4 | m13 | m8 | ent_m13 | ent_m8 | beside; repaired_self_edge_target from them->woman | medium | e18 | False | False |
| cr5 | m16 | m19 | ent_m16 | ent_m19 | at_top_of | high | e19 | False | False |

### Stage 9 Canonicalization Notes
_none_

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | ceiling | ceiling | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | pattern | patterns | object | m2 | raw_mention |  |  |  |
| ent_m5 | object | skylight | skylight | object | m5 | raw_mention |  |  |  |
| ent_m7 | object | light | light | object | m7 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | lets | let | let | in | agent:m0->ent_m0; agent:m5->ent_m5; patient:m7->ent_m7 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | let | agent | m0 | ent_m0 | medium | e5 | nsubj -> lets |  |  |
| ce0 | let | agent | m5 | ent_m5 | medium | e6 | nsubj -> lets |  |  |
| ce0 | let | patient | m7 | ent_m7 | medium | e8 | dobj -> lets |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m0 | m2 | ent_m0 | ent_m2 | with | high | e9 | False | False |

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
| entity_id | entity_type | canonical_lemma | text | semantic_type | raw_mentions | source | parent_entity | member_entities | cardinality |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ent_m0 | object | view | view | object | m0 | raw_mention |  |  |  |
| ent_m2 | object | town | town | object | m2 | raw_mention |  |  |  |
| ent_m3 | object | house | houses | object | m3 | raw_mention |  |  |  |
| ent_m4 | object | river | river | object | m4 | raw_mention |  |  |  |
| ent_m5 | object | road | roads | object | m5 | raw_mention |  |  |  |
| ent_m6 | object | field | fields | object | m6 | raw_mention |  |  |  |
| ent_m8 | object | hill | hills | object | m8 | raw_mention |  |  |  |

### Stage 9 Entity Links
_none_

### Stage 9 Canonical Events
| event_id | action_mention | raw_text | raw_lemma | canonical_action | particles | roles_summary | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | m9 | shows | show | show |  | agent:m0->ent_m0; patient:m2->ent_m2 |  |
| ce1 | m10 | winding | wind | wind |  | agent:m5->ent_m5 |  |

### Stage 9 Canonical Event Roles
| event_id | canonical_action | role | raw_target | canonical_target | confidence | raw_edge | evidence | recovered_from_skipped | repair |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ce0 | show | agent | m0 | ent_m0 | medium | e2 | nsubj -> shows |  |  |
| ce0 | show | patient | m2 | ent_m2 | medium | e3 | dobj -> shows |  |  |
| ce1 | wind | agent | m5 | ent_m5 | medium | e4 | inherited agent acl -> roads |  |  |

### Stage 9 Canonical Relations
| relation_id | raw_source | raw_target | canonical_source | canonical_target | relation | confidence | raw_edge | consumed_by_event | self_after_canonicalization |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cr0 | m2 | m3 | ent_m2 | ent_m3 | with | high | e5 | False | False |
| cr1 | m2 | m4 | ent_m2 | ent_m4 | with | high | e6 | False | False |
| cr2 | m2 | m5 | ent_m2 | ent_m5 | with | high | e7 | False | False |
| cr3 | m5 | m6 | ent_m5 | ent_m6 | through | medium | e8 | False | False |
| cr4 | m5 | m8 | ent_m5 | ent_m8 | through | medium | e9 | False | False |

### Stage 9 Canonicalization Notes
_none_
