# spaCy Parse Inspection

- input: `data\gpic_captions_eval_alt\val\gpic_val_00001.jsonl.gz`
- model: `en_core_web_trf`
- max_records: `100`
- mask_quotes: `True`
- quote_handling: `raw_quote_retokenize`
- quote_placeholder: `deprecated_unused`
- merge_object_mwes: `True`
- merge_hyphen_spans: `True`
- object_mwe_lexicon: `resources\lexicons\object_noun_mwe_clean_core.tsv`
- parse_tag_lists: `True`

## 01

**caption_shape:** `multi-sentence`
**caption_id:** `009d83aeeeb75b5ff2d8c8ee94d79d04f26d67e91f609efc71471b7e63cf6814`

> Several colorful posters are mounted on a white wall above a desk. A computer monitor displays an image, and various bottles and art supplies sit on the desk in front of it.

### Sentences
| sentence | token_span |
| --- | --- |
| Several colorful posters are mounted on a white wall above a desk. | 0:13 |
| A computer monitor displays an image, and various bottles and art supplies sit on the desk in front of it. | 13:34 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Several colorful posters | posters | poster | nsubjpass | mounted | 0:3 |
| a white wall | wall | wall | pobj | on | 6:9 |
| a desk | desk | desk | pobj | above | 10:12 |
| A computer monitor | computer monitor | computer_monitor | nsubj | displays | 13:15 |
| an image | image | image | dobj | displays | 16:18 |
| various bottles | bottles | bottle | nsubj | sit | 20:22 |
| art supplies | supplies | supply | conj | bottles | 23:25 |
| the desk | desk | desk | pobj | on | 27:29 |
| front | front | front | pobj | in | 30:31 |
| it | it | it | pobj | of | 32:33 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Several | several | ADJ | JJ | amod | posters | 2 |
| 1 | colorful | colorful | ADJ | JJ | amod | posters | 2 |
| 2 | posters | poster | NOUN | NNS | nsubjpass | mounted | 4 |
| 3 | are | be | AUX | VBP | auxpass | mounted | 4 |
| 4 | mounted | mount | VERB | VBN | ROOT | mounted | 4 |
| 5 | on | on | ADP | IN | prep | mounted | 4 |
| 6 | a | a | DET | DT | det | wall | 8 |
| 7 | white | white | ADJ | JJ | amod | wall | 8 |
| 8 | wall | wall | NOUN | NN | pobj | on | 5 |
| 9 | above | above | ADP | IN | prep | wall | 8 |
| 10 | a | a | DET | DT | det | desk | 11 |
| 11 | desk | desk | NOUN | NN | pobj | above | 9 |
| 12 | . | . | PUNCT | . | punct | mounted | 4 |
| 13 | A | a | DET | DT | det | computer monitor | 14 |
| 14 | computer monitor | computer_monitor | NOUN | NN | nsubj | displays | 15 |
| 15 | displays | display | VERB | VBZ | ROOT | displays | 15 |
| 16 | an | an | DET | DT | det | image | 17 |
| 17 | image | image | NOUN | NN | dobj | displays | 15 |
| 18 | , | , | PUNCT | , | punct | displays | 15 |
| 19 | and | and | CCONJ | CC | cc | displays | 15 |
| 20 | various | various | ADJ | JJ | amod | bottles | 21 |
| 21 | bottles | bottle | NOUN | NNS | nsubj | sit | 25 |
| 22 | and | and | CCONJ | CC | cc | bottles | 21 |
| 23 | art | art | NOUN | NN | compound | supplies | 24 |
| 24 | supplies | supply | NOUN | NNS | conj | bottles | 21 |
| 25 | sit | sit | VERB | VBP | conj | displays | 15 |
| 26 | on | on | ADP | IN | prep | sit | 25 |
| 27 | the | the | DET | DT | det | desk | 28 |
| 28 | desk | desk | NOUN | NN | pobj | on | 26 |
| 29 | in | in | ADP | IN | prep | sit | 25 |
| 30 | front | front | NOUN | NN | pobj | in | 29 |
| 31 | of | of | ADP | IN | prep | front | 30 |
| 32 | it | it | PRON | PRP | pobj | of | 31 |
| 33 | . | . | PUNCT | . | punct | sit | 25 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | posters | poster | chunk0 | 2 | noun_chunk_root | high |
| m1 | quantity | Several | several | chunk0 | 0 | approximate_quantity | medium |
| m2 | attribute | colorful | colorful | chunk0 | 1 | modifier_attribute | medium |
| m3 | object | wall | wall | chunk1 | 8 | noun_chunk_root | high |
| m4 | attribute | white | white | chunk1 | 7 | color_attribute | high |
| m5 | object | desk | desk | chunk2 | 11 | noun_chunk_root | high |
| m6 | object | computer monitor | computer_monitor | chunk3 | 14 | noun_chunk_root | high |
| m7 | object | image | image | chunk4 | 17 | noun_chunk_root | high |
| m8 | object | bottles | bottle | chunk5 | 21 | noun_chunk_root | high |
| m9 | quantity | various | various | chunk5 | 20 | approximate_quantity | medium |
| m10 | object | supplies | supply | chunk6 | 24 | noun_chunk_root | high |
| m11 | attribute | art | art | chunk6 | 23 | compound_modifier | medium |
| m12 | object | desk | desk | chunk7 | 28 | noun_chunk_root | high |
| m13 | action | mounted | mount | doc | 4 | verb_predicate | high |
| m14 | action | displays | display | doc | 15 | verb_predicate | high |
| m15 | action | sit | sit | doc | 25 | verb_predicate | high |

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

## 02

**caption_shape:** `sentence-like`
**caption_id:** `0111d88df23c0d12152d10e6b2250862b564dbdb78be57af836eb78663930014`

> A stone church with pointed towers and arched walkway stands beside a grassy garden with trimmed hedges and pink flowers.

### Sentences
| sentence | token_span |
| --- | --- |
| A stone church with pointed towers and arched walkway stands beside a grassy garden with trimmed hedges and pink flowers. | 0:21 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A stone church | church | church | nsubj | stands | 0:3 |
| pointed towers | towers | tower | pobj | with | 4:6 |
| arched walkway | walkway | walkway | conj | towers | 7:9 |
| a grassy garden | garden | garden | pobj | beside | 11:14 |
| trimmed hedges | hedges | hedge | pobj | with | 15:17 |
| pink flowers | flowers | flower | conj | hedges | 18:20 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | church | 2 |
| 1 | stone | stone | NOUN | NN | compound | church | 2 |
| 2 | church | church | NOUN | NN | nsubj | stands | 9 |
| 3 | with | with | ADP | IN | prep | church | 2 |
| 4 | pointed | pointed | ADJ | JJ | amod | towers | 5 |
| 5 | towers | tower | NOUN | NNS | pobj | with | 3 |
| 6 | and | and | CCONJ | CC | cc | towers | 5 |
| 7 | arched | arched | ADJ | JJ | amod | walkway | 8 |
| 8 | walkway | walkway | NOUN | NN | conj | towers | 5 |
| 9 | stands | stand | VERB | VBZ | ROOT | stands | 9 |
| 10 | beside | beside | ADP | IN | prep | stands | 9 |
| 11 | a | a | DET | DT | det | garden | 13 |
| 12 | grassy | grassy | ADJ | JJ | amod | garden | 13 |
| 13 | garden | garden | NOUN | NN | pobj | beside | 10 |
| 14 | with | with | ADP | IN | prep | garden | 13 |
| 15 | trimmed | trim | VERB | VBN | amod | hedges | 16 |
| 16 | hedges | hedge | NOUN | NNS | pobj | with | 14 |
| 17 | and | and | CCONJ | CC | cc | hedges | 16 |
| 18 | pink | pink | ADJ | JJ | amod | flowers | 19 |
| 19 | flowers | flower | NOUN | NNS | conj | hedges | 16 |
| 20 | . | . | PUNCT | . | punct | stands | 9 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | church | church | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | stone | stone | chunk0 | 1 | material_attribute | high |
| m2 | object | towers | tower | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | pointed | pointed | chunk1 | 4 | modifier_attribute | medium |
| m4 | object | walkway | walkway | chunk2 | 8 | noun_chunk_root | high |
| m5 | attribute | arched | arched | chunk2 | 7 | visual_attribute | medium |
| m6 | object | garden | garden | chunk3 | 13 | noun_chunk_root | high |
| m7 | attribute | grassy | grassy | chunk3 | 12 | modifier_attribute | medium |
| m8 | object | hedges | hedge | chunk4 | 16 | noun_chunk_root | high |
| m9 | attribute | trimmed | trim | chunk4 | 15 | state_attribute | medium |
| m10 | object | flowers | flower | chunk5 | 19 | noun_chunk_root | high |
| m11 | attribute | pink | pink | chunk5 | 18 | color_attribute | high |
| m12 | action | stands | stand | doc | 9 | verb_predicate | high |

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

## 03

**caption_shape:** `tag-list-like`
**caption_id:** `0196fc48ceb03b00a74261b2545370fca46dd97426e91b30193376102e523414`

> orange tricycle, man, smiling, outdoor, green trees

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | orange tricycle | orange tricycle | 0:15 |
| t1 | man | man | 17:20 |
| t2 | smiling | smiling | 22:29 |
| t3 | outdoor | outdoor | 31:38 |
| t4 | green trees | green trees | 40:51 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | orange tricycle | tricycle | tricycle | ROOT | tricycle | 0:2 | 0:15 |
| t4 | green trees | trees | tree | ROOT | trees | 0:2 | 40:51 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | orange | orange | ADJ | ADJ | JJ | JJ | amod | tricycle | 1 | 0:6 |
| t0 | 1 | tricycle | tricycle | NOUN | NOUN | NN | NN | ROOT | tricycle | 1 | 7:15 |
| t1 | 0 | man | man | INTJ | NOUN | UH | NN | ROOT | man | 0 | 17:20 |
| t2 | 0 | smiling | smile | VERB | VERB | VBG | VBG | ROOT | smiling | 0 | 22:29 |
| t3 | 0 | outdoor | outdoor | ADJ | ADJ | JJ | JJ | ROOT | outdoor | 0 | 31:38 |
| t4 | 0 | green | green | ADJ | ADJ | JJ | JJ | amod | trees | 1 | 40:45 |
| t4 | 1 | trees | tree | NOUN | NOUN | NNS | NNS | ROOT | trees | 1 | 46:51 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | tricycle | tricycle | t0 | 1 | segment_head | high |
| m1 | attribute | orange | orange | t0 | 0 | attribute | high |
| m2 | object | man | man | t1 | 0 | tag_list_person_object_override | high |
| m3 | attribute | smiling | smile | t2 | 0 | floating_attribute | medium |
| m4 | context | outdoor | outdoor | t3 | 0 | scene_context | high |
| m5 | object | trees | tree | t4 | 1 | segment_head | high |
| m6 | attribute | green | green | t4 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> tricycle |
| e1 | candidate_has_attribute | m2 | m3 | low | t2 adjacent floating attribute |
| e2 | has_context | scene | m4 | high | t3 context tag |
| e3 | has_attribute | m5 | m6 | high | t4 internal amod -> trees |

## 04

**caption_shape:** `sentence-like`
**caption_id:** `02c946ea0b2e9479de9d69341333a30547d9be6f8b097766bcbe63dae0f94c14`

> An older man and woman walk together on a city street, holding hands near a large building.

### Sentences
| sentence | token_span |
| --- | --- |
| An older man and woman walk together on a city street, holding hands near a large building. | 0:19 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| An older man | man | man | nsubj | walk | 0:3 |
| woman | woman | woman | conj | man | 4:5 |
| a city street | street | street | pobj | on | 8:11 |
| hands | hands | hand | dobj | holding | 13:14 |
| a large building | building | building | pobj | near | 15:18 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | An | an | DET | DT | det | man | 2 |
| 1 | older | old | ADJ | JJR | amod | man | 2 |
| 2 | man | man | NOUN | NN | nsubj | walk | 5 |
| 3 | and | and | CCONJ | CC | cc | man | 2 |
| 4 | woman | woman | NOUN | NN | conj | man | 2 |
| 5 | walk | walk | VERB | VBP | ROOT | walk | 5 |
| 6 | together | together | ADV | RB | advmod | walk | 5 |
| 7 | on | on | ADP | IN | prep | walk | 5 |
| 8 | a | a | DET | DT | det | street | 10 |
| 9 | city | city | NOUN | NN | compound | street | 10 |
| 10 | street | street | NOUN | NN | pobj | on | 7 |
| 11 | , | , | PUNCT | , | punct | walk | 5 |
| 12 | holding | hold | VERB | VBG | advcl | walk | 5 |
| 13 | hands | hand | NOUN | NNS | dobj | holding | 12 |
| 14 | near | near | ADP | IN | prep | holding | 12 |
| 15 | a | a | DET | DT | det | building | 17 |
| 16 | large | large | ADJ | JJ | amod | building | 17 |
| 17 | building | building | NOUN | NN | pobj | near | 14 |
| 18 | . | . | PUNCT | . | punct | walk | 5 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | older | old | chunk0 | 1 | visual_attribute | medium |
| m2 | object | woman | woman | chunk1 | 4 | noun_chunk_root | high |
| m3 | object | street | street | chunk2 | 10 | noun_chunk_root | high |
| m4 | attribute | city | city | chunk2 | 9 | compound_modifier | medium |
| m5 | object | hands | hand | chunk3 | 13 | noun_chunk_root | high |
| m6 | object | building | building | chunk4 | 17 | noun_chunk_root | high |
| m7 | attribute | large | large | chunk4 | 16 | size_attribute | high |
| m8 | action | walk | walk | doc | 5 | verb_predicate | high |
| m9 | action | holding | hold | doc | 12 | verb_predicate | high |

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

## 05

**caption_shape:** `multi-sentence`
**caption_id:** `032d1400e70fdb9548f61e378f2ab55781a01ee044a329d1b8adb85bf7f43414`

> A flooded street with water covering the road and submerging stop signs. A green digital sign stands in the background, with bare trees and a grassy hill visible beyond the floodwaters. The sky is overcast and gray.

### Sentences
| sentence | token_span |
| --- | --- |
| A flooded street with water covering the road and submerging stop signs. | 0:12 |
| A green digital sign stands in the background, with bare trees and a grassy hill visible beyond the floodwaters. | 12:33 |
| The sky is overcast and gray. | 33:40 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A flooded street | street | street | ROOT | street | 0:3 |
| water | water | water | nsubj | covering | 4:5 |
| the road | road | road | dobj | covering | 6:8 |
| stop signs | stop signs | stop_sign | dobj | submerging | 10:11 |
| A green digital sign | sign | sign | nsubj | stands | 12:16 |
| the background | background | background | pobj | in | 18:20 |
| bare trees | trees | tree | pobj | with | 22:24 |
| a grassy hill | hill | hill | conj | trees | 25:28 |
| the floodwaters | floodwaters | floodwater | pobj | beyond | 30:32 |
| The sky | sky | sky | nsubj | is | 33:35 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | street | 2 |
| 1 | flooded | flooded | ADJ | JJ | amod | street | 2 |
| 2 | street | street | NOUN | NN | ROOT | street | 2 |
| 3 | with | with | ADP | IN | prep | street | 2 |
| 4 | water | water | NOUN | NN | nsubj | covering | 5 |
| 5 | covering | cover | VERB | VBG | pcomp | with | 3 |
| 6 | the | the | DET | DT | det | road | 7 |
| 7 | road | road | NOUN | NN | dobj | covering | 5 |
| 8 | and | and | CCONJ | CC | cc | covering | 5 |
| 9 | submerging | submerge | VERB | VBG | conj | covering | 5 |
| 10 | stop signs | stop_sign | NOUN | NN | dobj | submerging | 9 |
| 11 | . | . | PUNCT | . | punct | street | 2 |
| 12 | A | a | DET | DT | det | sign | 15 |
| 13 | green | green | ADJ | JJ | amod | sign | 15 |
| 14 | digital | digital | ADJ | JJ | amod | sign | 15 |
| 15 | sign | sign | NOUN | NN | nsubj | stands | 16 |
| 16 | stands | stand | VERB | VBZ | ROOT | stands | 16 |
| 17 | in | in | ADP | IN | prep | stands | 16 |
| 18 | the | the | DET | DT | det | background | 19 |
| 19 | background | background | NOUN | NN | pobj | in | 17 |
| 20 | , | , | PUNCT | , | punct | stands | 16 |
| 21 | with | with | ADP | IN | prep | stands | 16 |
| 22 | bare | bare | ADJ | JJ | amod | trees | 23 |
| 23 | trees | tree | NOUN | NNS | pobj | with | 21 |
| 24 | and | and | CCONJ | CC | cc | trees | 23 |
| 25 | a | a | DET | DT | det | hill | 27 |
| 26 | grassy | grassy | ADJ | JJ | amod | hill | 27 |
| 27 | hill | hill | NOUN | NN | conj | trees | 23 |
| 28 | visible | visible | ADJ | JJ | amod | trees | 23 |
| 29 | beyond | beyond | ADP | IN | prep | visible | 28 |
| 30 | the | the | DET | DT | det | floodwaters | 31 |
| 31 | floodwaters | floodwater | NOUN | NNS | pobj | beyond | 29 |
| 32 | . | . | PUNCT | . | punct | stands | 16 |
| 33 | The | the | DET | DT | det | sky | 34 |
| 34 | sky | sky | NOUN | NN | nsubj | is | 35 |
| 35 | is | be | AUX | VBZ | ROOT | is | 35 |
| 36 | overcast | overcast | ADJ | JJ | acomp | is | 35 |
| 37 | and | and | CCONJ | CC | cc | overcast | 36 |
| 38 | gray | gray | ADJ | JJ | conj | overcast | 36 |
| 39 | . | . | PUNCT | . | punct | is | 35 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | street | street | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | flooded | flooded | chunk0 | 1 | modifier_attribute | medium |
| m2 | object | water | water | chunk1 | 4 | noun_chunk_root | high |
| m3 | object | road | road | chunk2 | 7 | noun_chunk_root | high |
| m4 | object | stop signs | stop_sign | chunk3 | 10 | noun_chunk_root | high |
| m5 | object | sign | sign | chunk4 | 15 | noun_chunk_root | high |
| m6 | attribute | green | green | chunk4 | 13 | color_attribute | high |
| m7 | attribute | digital | digital | chunk4 | 14 | modifier_attribute | medium |
| m8 | context | background | background | chunk5 | 19 | scene_context | high |
| m9 | object | trees | tree | chunk6 | 23 | noun_chunk_root | high |
| m10 | attribute | bare | bare | chunk6 | 22 | visual_attribute | medium |
| m11 | object | hill | hill | chunk7 | 27 | noun_chunk_root | high |
| m12 | attribute | grassy | grassy | chunk7 | 26 | modifier_attribute | medium |
| m13 | object | floodwaters | floodwater | chunk8 | 31 | noun_chunk_root | high |
| m14 | object | sky | sky | chunk9 | 34 | noun_chunk_root | high |
| m15 | action | covering | cover | doc | 5 | verb_predicate | high |
| m16 | action | submerging | submerge | doc | 9 | verb_predicate | high |
| m17 | action | stands | stand | doc | 16 | verb_predicate | high |

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

## 06

**caption_shape:** `multi-sentence`
**caption_id:** `03736f3c4bc91505f93827beba8298b54e23d2d307312341f8de4f039291e014`

> Three football players in blue and black uniforms stand on a grass field with white lines. They wear helmets and gloves, with snow visible along the sidelines and orange cones nearby. The background shows dark trees and a fence under dim lighting.

### Sentences
| sentence | token_span |
| --- | --- |
| Three football players in blue and black uniforms stand on a grass field with white lines. | 0:16 |
| They wear helmets and gloves, with snow visible along the sidelines and orange cones nearby. | 16:33 |
| The background shows dark trees and a fence under dim lighting. | 33:45 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Three football players | football players | football_player | nsubj | stand | 0:2 |
| blue and black uniforms | uniforms | uniform | pobj | in | 3:7 |
| a grass field | field | field | pobj | on | 9:12 |
| white lines | lines | line | pobj | with | 13:15 |
| They | They | they | nsubj | wear | 16:17 |
| helmets | helmets | helmet | dobj | wear | 18:19 |
| gloves | gloves | glove | conj | helmets | 20:21 |
| snow | snow | snow | pobj | with | 23:24 |
| the sidelines | sidelines | sideline | pobj | along | 26:28 |
| orange cones | cones | cone | conj | snow | 29:31 |
| The background | background | background | nsubj | shows | 33:35 |
| dark trees | trees | tree | dobj | shows | 36:38 |
| a fence | fence | fence | conj | trees | 39:41 |
| dim lighting | lighting | lighting | pobj | under | 42:44 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Three | three | NUM | CD | nummod | football players | 1 |
| 1 | football players | football_player | NOUN | NN | nsubj | stand | 7 |
| 2 | in | in | ADP | IN | prep | football players | 1 |
| 3 | blue | blue | ADJ | JJ | amod | uniforms | 6 |
| 4 | and | and | CCONJ | CC | cc | blue | 3 |
| 5 | black | black | ADJ | JJ | conj | blue | 3 |
| 6 | uniforms | uniform | NOUN | NNS | pobj | in | 2 |
| 7 | stand | stand | VERB | VBP | ROOT | stand | 7 |
| 8 | on | on | ADP | IN | prep | stand | 7 |
| 9 | a | a | DET | DT | det | field | 11 |
| 10 | grass | grass | NOUN | NN | compound | field | 11 |
| 11 | field | field | NOUN | NN | pobj | on | 8 |
| 12 | with | with | ADP | IN | prep | field | 11 |
| 13 | white | white | ADJ | JJ | amod | lines | 14 |
| 14 | lines | line | NOUN | NNS | pobj | with | 12 |
| 15 | . | . | PUNCT | . | punct | stand | 7 |
| 16 | They | they | PRON | PRP | nsubj | wear | 17 |
| 17 | wear | wear | VERB | VBP | ROOT | wear | 17 |
| 18 | helmets | helmet | NOUN | NNS | dobj | wear | 17 |
| 19 | and | and | CCONJ | CC | cc | helmets | 18 |
| 20 | gloves | glove | NOUN | NNS | conj | helmets | 18 |
| 21 | , | , | PUNCT | , | punct | wear | 17 |
| 22 | with | with | ADP | IN | prep | wear | 17 |
| 23 | snow | snow | NOUN | NN | pobj | with | 22 |
| 24 | visible | visible | ADJ | JJ | amod | snow | 23 |
| 25 | along | along | ADP | IN | prep | visible | 24 |
| 26 | the | the | DET | DT | det | sidelines | 27 |
| 27 | sidelines | sideline | NOUN | NNS | pobj | along | 25 |
| 28 | and | and | CCONJ | CC | cc | snow | 23 |
| 29 | orange | orange | NOUN | NN | compound | cones | 30 |
| 30 | cones | cone | NOUN | NNS | conj | snow | 23 |
| 31 | nearby | nearby | ADV | RB | advmod | cones | 30 |
| 32 | . | . | PUNCT | . | punct | wear | 17 |
| 33 | The | the | DET | DT | det | background | 34 |
| 34 | background | background | NOUN | NN | nsubj | shows | 35 |
| 35 | shows | show | VERB | VBZ | ROOT | shows | 35 |
| 36 | dark | dark | ADJ | JJ | amod | trees | 37 |
| 37 | trees | tree | NOUN | NNS | dobj | shows | 35 |
| 38 | and | and | CCONJ | CC | cc | trees | 37 |
| 39 | a | a | DET | DT | det | fence | 40 |
| 40 | fence | fence | NOUN | NN | conj | trees | 37 |
| 41 | under | under | ADP | IN | prep | trees | 37 |
| 42 | dim | dim | ADJ | JJ | amod | lighting | 43 |
| 43 | lighting | lighting | NOUN | NN | pobj | under | 41 |
| 44 | . | . | PUNCT | . | punct | shows | 35 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | football players | football_player | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Three | three | chunk0 | 0 | exact_quantity | high |
| m2 | object | uniforms | uniform | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | blue | blue | chunk1 | 3 | color_attribute | high |
| m4 | attribute | black | black | chunk1 | 5 | color_attribute | high |
| m5 | object | field | field | chunk2 | 11 | noun_chunk_root | high |
| m6 | attribute | grass | grass | chunk2 | 10 | compound_modifier | medium |
| m7 | object | lines | line | chunk3 | 14 | noun_chunk_root | high |
| m8 | attribute | white | white | chunk3 | 13 | color_attribute | high |
| m9 | object | helmets | helmet | chunk5 | 18 | noun_chunk_root | high |
| m10 | object | gloves | glove | chunk6 | 20 | noun_chunk_root | high |
| m11 | object | snow | snow | chunk7 | 23 | noun_chunk_root | high |
| m12 | object | sidelines | sideline | chunk8 | 27 | noun_chunk_root | high |
| m13 | object | cones | cone | chunk9 | 30 | noun_chunk_root | high |
| m14 | attribute | orange | orange | chunk9 | 29 | color_attribute | high |
| m15 | context | background | background | chunk10 | 34 | scene_context | high |
| m16 | object | trees | tree | chunk11 | 37 | noun_chunk_root | high |
| m17 | attribute | dark | dark | chunk11 | 36 | visual_attribute | medium |
| m18 | object | fence | fence | chunk12 | 40 | noun_chunk_root | high |
| m19 | object | lighting | lighting | chunk13 | 43 | noun_chunk_root | high |
| m20 | attribute | dim | dim | chunk13 | 42 | modifier_attribute | medium |
| m21 | action | stand | stand | doc | 7 | verb_predicate | high |
| m22 | action | wear | wear | doc | 17 | verb_predicate | high |
| m23 | action | shows | show | doc | 35 | verb_predicate | high |

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

## 07

**caption_shape:** `multi-sentence`
**caption_id:** `0457258811eff6ad31c0677c3d521527c46bd865e03f9c7a0f87b0f8f6229414`

> Two people stand on a paved plaza near a tall green spire building under a clear blue sky. Several parked cars line the street to the right, with a parking sign visible beside a gray lamppost.

### Sentences
| sentence | token_span |
| --- | --- |
| Two people stand on a paved plaza near a tall green spire building under a clear blue sky. | 0:19 |
| Several parked cars line the street to the right, with a parking sign visible beside a gray lamppost. | 19:39 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Two people | people | people | nsubj | stand | 0:2 |
| a paved plaza | plaza | plaza | pobj | on | 4:7 |
| a tall green spire building | building | building | pobj | near | 8:13 |
| a clear blue sky | sky | sky | pobj | under | 14:18 |
| Several parked cars | cars | car | nsubj | line | 19:22 |
| the street | street | street | dobj | line | 23:25 |
| the right | right | right | pobj | to | 26:28 |
| a parking sign | sign | sign | pobj | with | 30:33 |
| a gray lamppost | lamppost | lamppost | pobj | beside | 35:38 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Two | two | NUM | CD | nummod | people | 1 |
| 1 | people | people | NOUN | NNS | nsubj | stand | 2 |
| 2 | stand | stand | VERB | VBP | ROOT | stand | 2 |
| 3 | on | on | ADP | IN | prep | stand | 2 |
| 4 | a | a | DET | DT | det | plaza | 6 |
| 5 | paved | paved | ADJ | JJ | amod | plaza | 6 |
| 6 | plaza | plaza | NOUN | NN | pobj | on | 3 |
| 7 | near | near | ADP | IN | prep | stand | 2 |
| 8 | a | a | DET | DT | det | building | 12 |
| 9 | tall | tall | ADJ | JJ | amod | building | 12 |
| 10 | green | green | ADJ | JJ | amod | building | 12 |
| 11 | spire | spire | NOUN | NN | compound | building | 12 |
| 12 | building | building | NOUN | NN | pobj | near | 7 |
| 13 | under | under | ADP | IN | prep | stand | 2 |
| 14 | a | a | DET | DT | det | sky | 17 |
| 15 | clear | clear | ADJ | JJ | amod | sky | 17 |
| 16 | blue | blue | ADJ | JJ | amod | sky | 17 |
| 17 | sky | sky | NOUN | NN | pobj | under | 13 |
| 18 | . | . | PUNCT | . | punct | stand | 2 |
| 19 | Several | several | ADJ | JJ | amod | cars | 21 |
| 20 | parked | park | VERB | VBN | amod | cars | 21 |
| 21 | cars | car | NOUN | NNS | nsubj | line | 22 |
| 22 | line | line | VERB | VBP | ROOT | line | 22 |
| 23 | the | the | DET | DT | det | street | 24 |
| 24 | street | street | NOUN | NN | dobj | line | 22 |
| 25 | to | to | ADP | IN | prep | line | 22 |
| 26 | the | the | DET | DT | det | right | 27 |
| 27 | right | right | NOUN | NN | pobj | to | 25 |
| 28 | , | , | PUNCT | , | punct | line | 22 |
| 29 | with | with | ADP | IN | prep | line | 22 |
| 30 | a | a | DET | DT | det | sign | 32 |
| 31 | parking | parking | NOUN | NN | compound | sign | 32 |
| 32 | sign | sign | NOUN | NN | pobj | with | 29 |
| 33 | visible | visible | ADJ | JJ | amod | sign | 32 |
| 34 | beside | beside | ADP | IN | prep | visible | 33 |
| 35 | a | a | DET | DT | det | lamppost | 37 |
| 36 | gray | gray | ADJ | JJ | amod | lamppost | 37 |
| 37 | lamppost | lamppost | NOUN | NN | pobj | beside | 34 |
| 38 | . | . | PUNCT | . | punct | line | 22 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Two | two | chunk0 | 0 | exact_quantity | high |
| m2 | object | plaza | plaza | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | paved | paved | chunk1 | 5 | visual_attribute | medium |
| m4 | object | building | building | chunk2 | 12 | noun_chunk_root | high |
| m5 | attribute | tall | tall | chunk2 | 9 | size_attribute | high |
| m6 | attribute | green | green | chunk2 | 10 | color_attribute | high |
| m7 | attribute | spire | spire | chunk2 | 11 | compound_modifier | medium |
| m8 | object | sky | sky | chunk3 | 17 | noun_chunk_root | high |
| m9 | attribute | clear | clear | chunk3 | 15 | visual_attribute | medium |
| m10 | attribute | blue | blue | chunk3 | 16 | color_attribute | high |
| m11 | object | cars | car | chunk4 | 21 | noun_chunk_root | high |
| m12 | quantity | Several | several | chunk4 | 19 | approximate_quantity | medium |
| m13 | attribute | parked | park | chunk4 | 20 | state_attribute | medium |
| m14 | object | street | street | chunk5 | 24 | noun_chunk_root | high |
| m15 | context | right | right | chunk6 | 27 | spatial_region | medium |
| m16 | object | sign | sign | chunk7 | 32 | noun_chunk_root | high |
| m17 | attribute | parking | parking | chunk7 | 31 | compound_modifier | medium |
| m18 | object | lamppost | lamppost | chunk8 | 37 | noun_chunk_root | high |
| m19 | attribute | gray | gray | chunk8 | 36 | color_attribute | high |
| m20 | action | stand | stand | doc | 2 | verb_predicate | high |
| m21 | action | line | line | doc | 22 | verb_predicate | high |

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

## 08

**caption_shape:** `sentence-like`
**caption_id:** `047a4714002c7230c85d87adf7034ef1251a492dfd3e627182dd93db89a3ec14`

> A woodpecker with black, white, and red feathers perches on a broken log in tall grass.

### Sentences
| sentence | token_span |
| --- | --- |
| A woodpecker with black, white, and red feathers perches on a broken log in tall grass. | 0:19 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A woodpecker | woodpecker | woodpecker | nsubj | perches | 0:2 |
| black, white, and red feathers | feathers | feather | pobj | with | 3:10 |
| a broken log | log | log | pobj | on | 12:15 |
| tall grass | grass | grass | pobj | in | 16:18 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | woodpecker | 1 |
| 1 | woodpecker | woodpecker | NOUN | NN | nsubj | perches | 10 |
| 2 | with | with | ADP | IN | prep | woodpecker | 1 |
| 3 | black | black | ADJ | JJ | amod | feathers | 9 |
| 4 | , | , | PUNCT | , | punct | black | 3 |
| 5 | white | white | ADJ | JJ | conj | black | 3 |
| 6 | , | , | PUNCT | , | punct | white | 5 |
| 7 | and | and | CCONJ | CC | cc | white | 5 |
| 8 | red | red | ADJ | JJ | conj | white | 5 |
| 9 | feathers | feather | NOUN | NNS | pobj | with | 2 |
| 10 | perches | perch | VERB | VBZ | ROOT | perches | 10 |
| 11 | on | on | ADP | IN | prep | perches | 10 |
| 12 | a | a | DET | DT | det | log | 14 |
| 13 | broken | broken | ADJ | JJ | amod | log | 14 |
| 14 | log | log | NOUN | NN | pobj | on | 11 |
| 15 | in | in | ADP | IN | prep | perches | 10 |
| 16 | tall | tall | ADJ | JJ | amod | grass | 17 |
| 17 | grass | grass | NOUN | NN | pobj | in | 15 |
| 18 | . | . | PUNCT | . | punct | perches | 10 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woodpecker | woodpecker | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | feathers | feather | chunk1 | 9 | noun_chunk_root | high |
| m2 | attribute | black | black | chunk1 | 3 | color_attribute | high |
| m3 | attribute | white | white | chunk1 | 5 | color_attribute | high |
| m4 | attribute | red | red | chunk1 | 8 | color_attribute | high |
| m5 | object | log | log | chunk2 | 14 | noun_chunk_root | high |
| m6 | attribute | broken | broken | chunk2 | 13 | modifier_attribute | medium |
| m7 | object | grass | grass | chunk3 | 17 | noun_chunk_root | high |
| m8 | attribute | tall | tall | chunk3 | 16 | size_attribute | high |
| m9 | action | perches | perch | doc | 10 | verb_predicate | high |

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

## 09

**caption_shape:** `tag-list-like`
**caption_id:** `05e4cae85e91c5da230d50cb73b2525765091495a133f78a2330c5848367cc14`

> woman, purple pants, stone steps, classical building, autumn trees

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | woman | woman | 0:5 |
| t1 | purple pants | purple pants | 7:19 |
| t2 | stone steps | stone steps | 21:32 |
| t3 | classical building | classical building | 34:52 |
| t4 | autumn trees | autumn trees | 54:66 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | woman | woman | woman | ROOT | woman | 0:1 | 0:5 |
| t1 | purple pants | pants | pant | ROOT | pants | 0:2 | 7:19 |
| t2 | stone steps | steps | step | ROOT | steps | 0:2 | 21:32 |
| t3 | classical building | building | building | ROOT | building | 0:2 | 34:52 |
| t4 | autumn trees | trees | tree | ROOT | trees | 0:2 | 54:66 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | woman | woman | NOUN | NOUN | NN | NN | ROOT | woman | 0 | 0:5 |
| t1 | 0 | purple | purple | ADJ | ADJ | JJ | JJ | amod | pants | 1 | 7:13 |
| t1 | 1 | pants | pant | NOUN | NOUN | NNS | NNS | ROOT | pants | 1 | 14:19 |
| t2 | 0 | stone | stone | NOUN | NOUN | NN | NN | compound | steps | 1 | 21:26 |
| t2 | 1 | steps | step | NOUN | NOUN | NNS | NNS | ROOT | steps | 1 | 27:32 |
| t3 | 0 | classical | classical | ADJ | ADJ | JJ | JJ | amod | building | 1 | 34:43 |
| t3 | 1 | building | building | NOUN | NOUN | NN | NN | ROOT | building | 1 | 44:52 |
| t4 | 0 | autumn | autumn | NOUN | NOUN | NN | NN | compound | trees | 1 | 54:60 |
| t4 | 1 | trees | tree | NOUN | NOUN | NNS | NNS | ROOT | trees | 1 | 61:66 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | t0 | 0 | segment_head | high |
| m1 | object | pants | pant | t1 | 1 | segment_head | high |
| m2 | attribute | purple | purple | t1 | 0 | attribute | high |
| m3 | object | steps | step | t2 | 1 | segment_head | high |
| m4 | attribute | stone | stone | t2 | 0 | attribute | high |
| m5 | object | building | building | t3 | 1 | segment_head | high |
| m6 | attribute | classical | classical | t3 | 0 | attribute | high |
| m7 | object | trees | tree | t4 | 1 | segment_head | high |
| m8 | attribute | autumn | autumn | t4 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | t1 internal amod -> pants |
| e1 | has_attribute | m3 | m4 | high | t2 internal compound -> steps |
| e2 | has_attribute | m5 | m6 | high | t3 internal amod -> building |
| e3 | has_attribute | m7 | m8 | high | t4 internal compound -> trees |

## 10

**caption_shape:** `tag-list-like`
**caption_id:** `06b01b3b3226df78be43c09a85d68cb1ddd08979194fea12f21255cab3d63c14`

> yellow sweater, child, drawing, green lockers

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | yellow sweater | yellow sweater | 0:14 |
| t1 | child | child | 16:21 |
| t2 | drawing | drawing | 23:30 |
| t3 | green lockers | green lockers | 32:45 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | yellow sweater | sweater | sweater | ROOT | sweater | 0:2 | 0:14 |
| t1 | child | child | child | ROOT | child | 0:1 | 16:21 |
| t2 | drawing | drawing | drawing | ROOT | drawing | 0:1 | 23:30 |
| t3 | green lockers | lockers | locker | ROOT | lockers | 0:2 | 32:45 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | yellow | yellow | ADJ | ADJ | JJ | JJ | amod | sweater | 1 | 0:6 |
| t0 | 1 | sweater | sweater | NOUN | NOUN | NN | NN | ROOT | sweater | 1 | 7:14 |
| t1 | 0 | child | child | NOUN | NOUN | NN | NN | ROOT | child | 0 | 16:21 |
| t2 | 0 | drawing | drawing | NOUN | NOUN | NN | NN | ROOT | drawing | 0 | 23:30 |
| t3 | 0 | green | green | ADJ | ADJ | JJ | JJ | amod | lockers | 1 | 32:37 |
| t3 | 1 | lockers | locker | NOUN | NOUN | NNS | NNS | ROOT | lockers | 1 | 38:45 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | sweater | sweater | t0 | 1 | segment_head | high |
| m1 | attribute | yellow | yellow | t0 | 0 | attribute | high |
| m2 | object | child | child | t1 | 0 | segment_head | high |
| m3 | object | drawing | drawing | t2 | 0 | segment_head | high |
| m4 | object | lockers | locker | t3 | 1 | segment_head | high |
| m5 | attribute | green | green | t3 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> sweater |
| e1 | has_attribute | m4 | m5 | high | t3 internal amod -> lockers |

## 11

**caption_shape:** `sentence-like`
**caption_id:** `06d84e7d9080d4a002071d8fc8f84e1108c9a315ae767d2c7c7015cad57c3414`

> The image shows a page from a book with Russian text, listing numbered sections and titles like "Симбирская губерния" and "Войсковая система."

**parsed_caption:**

> The image shows a page from a book with Russian text, listing numbered sections and titles like "Симбирская губерния" and "Войсковая система."

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 06d84e7d9080d4a002071d8fc8f84e1108c9a315ae767d2c7c7015cad57c3414:q0 | Симбирская губерния | симбирская губерния | raw_quote_span |  | 96:117 | 96:117 |
| q1 | 06d84e7d9080d4a002071d8fc8f84e1108c9a315ae767d2c7c7015cad57c3414:q1 | Войсковая система. | войсковая система. | raw_quote_span |  | 122:142 | 122:142 |

### Sentences
| sentence | token_span |
| --- | --- |
| The image shows a page from a book with Russian text, listing numbered sections and titles like "Симбирская губерния" and "Войсковая система." | 0:21 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| The image | image | image | nsubj | shows | 0:2 |
| a page | page | page | dobj | shows | 3:5 |
| a book | book | book | pobj | from | 6:8 |
| Russian text | text | text | pobj | with | 9:11 |
| numbered sections | sections | section | dobj | listing | 13:15 |
| titles | titles | title | conj | sections | 16:17 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | The | the | DET | DT | det | image | 1 |
| 1 | image | image | NOUN | NN | nsubj | shows | 2 |
| 2 | shows | show | VERB | VBZ | ROOT | shows | 2 |
| 3 | a | a | DET | DT | det | page | 4 |
| 4 | page | page | NOUN | NN | dobj | shows | 2 |
| 5 | from | from | ADP | IN | prep | page | 4 |
| 6 | a | a | DET | DT | det | book | 7 |
| 7 | book | book | NOUN | NN | pobj | from | 5 |
| 8 | with | with | ADP | IN | prep | book | 7 |
| 9 | Russian | russian | ADJ | JJ | amod | text | 10 |
| 10 | text | text | NOUN | NN | pobj | with | 8 |
| 11 | , | , | PUNCT | , | punct | shows | 2 |
| 12 | listing | list | VERB | VBG | advcl | shows | 2 |
| 13 | numbered | number | VERB | VBN | amod | sections | 14 |
| 14 | sections | section | NOUN | NNS | dobj | listing | 12 |
| 15 | and | and | CCONJ | CC | cc | sections | 14 |
| 16 | titles | title | NOUN | NNS | conj | sections | 14 |
| 17 | like | like | ADP | IN | prep | titles | 16 |
| 18 | "Симбирская губерния" | симбирская_губерния | X | FW | pobj | like | 17 |
| 19 | and | and | CCONJ | CC | cc | "Симбирская губерния" | 18 |
| 20 | "Войсковая система." | войсковая_система. | X | FW | pobj | like | 17 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "Симбирская губерния" | симбирская_губерния | doc_quote | 18 | quote_text | high |
| m1 | attribute | "Войсковая система." | войсковая_система. | doc_quote | 20 | quote_text | high |
| m2 | object | image | image | chunk0 | 1 | noun_chunk_root | high |
| m3 | object | page | page | chunk1 | 4 | noun_chunk_root | high |
| m4 | object | book | book | chunk2 | 7 | noun_chunk_root | high |
| m5 | object | text | text | chunk3 | 10 | noun_chunk_root | high |
| m6 | attribute | Russian | russian | chunk3 | 9 | modifier_attribute | medium |
| m7 | object | sections | section | chunk4 | 14 | noun_chunk_root | high |
| m8 | attribute | numbered | number | chunk4 | 13 | state_attribute | medium |
| m9 | object | titles | title | chunk5 | 16 | noun_chunk_root | high |
| m10 | action | shows | show | doc | 2 | verb_predicate | high |
| m11 | action | listing | list | doc | 12 | verb_predicate | high |

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

## 12

**caption_shape:** `tag-list-like`
**caption_id:** `06decbdc22a2a9dc4dc57771004ad26736931badec1cbcd8ddfb1c57ac76c814`

> dancing people, indoor party, floral dress, denim jacket, raised arms

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | dancing people | dancing people | 0:14 |
| t1 | indoor party | indoor party | 16:28 |
| t2 | floral dress | floral dress | 30:42 |
| t3 | denim jacket | denim jacket | 44:56 |
| t4 | raised arms | raised arms | 58:69 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | dancing people | people | people | ROOT | people | 0:2 | 0:14 |
| t1 | indoor party | party | party | ROOT | party | 0:2 | 16:28 |
| t2 | floral dress | dress | dress | ROOT | dress | 0:2 | 30:42 |
| t3 | denim jacket | jacket | jacket | ROOT | jacket | 0:2 | 44:56 |
| t4 | raised arms | arms | arm | ROOT | arms | 0:2 | 58:69 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | dancing | dance | VERB | ADJ | VBG | VBG | amod | people | 1 | 0:7 |
| t0 | 1 | people | people | NOUN | NOUN | NNS | NNS | ROOT | people | 1 | 8:14 |
| t1 | 0 | indoor | indoor | PROPN | ADJ | NNP | JJ | compound | party | 1 | 16:22 |
| t1 | 1 | party | party | PROPN | NOUN | NNP | NN | ROOT | party | 1 | 23:28 |
| t2 | 0 | floral | floral | NOUN | NOUN | NN | NN | compound | dress | 1 | 30:36 |
| t2 | 1 | dress | dress | NOUN | NOUN | NN | NN | ROOT | dress | 1 | 37:42 |
| t3 | 0 | denim | denim | NOUN | NOUN | NN | NN | compound | jacket | 1 | 44:49 |
| t3 | 1 | jacket | jacket | NOUN | NOUN | NN | NN | ROOT | jacket | 1 | 50:56 |
| t4 | 0 | raised | raise | VERB | ADJ | VBN | VBN | amod | arms | 1 | 58:64 |
| t4 | 1 | arms | arm | NOUN | NOUN | NNS | NNS | ROOT | arms | 1 | 65:69 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | t0 | 1 | segment_head | high |
| m1 | attribute | dancing | dance | t0 | 0 | state_attribute | high |
| m2 | object | party | party | t1 | 1 | segment_head | high |
| m3 | attribute | indoor | indoor | t1 | 0 | attribute | high |
| m4 | object | dress | dress | t2 | 1 | segment_head | high |
| m5 | attribute | floral | floral | t2 | 0 | attribute | high |
| m6 | object | jacket | jacket | t3 | 1 | segment_head | high |
| m7 | attribute | denim | denim | t3 | 0 | attribute | high |
| m8 | object | arms | arm | t4 | 1 | segment_head | high |
| m9 | attribute | raised | raise | t4 | 0 | state_attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> people |
| e1 | has_attribute | m2 | m3 | high | t1 internal compound -> party |
| e2 | has_attribute | m4 | m5 | high | t2 internal compound -> dress |
| e3 | has_attribute | m6 | m7 | high | t3 internal compound -> jacket |
| e4 | has_attribute | m8 | m9 | high | t4 internal amod -> arms |

## 13

**caption_shape:** `multi-sentence`
**caption_id:** `073090fa7e0c6c80f67ed0c260aa4cedcef5e326343311c80603a39aa3347014`

> Players in red and maroon jerseys skate on an ice rink during a hockey game. A goalie stands near the net, while others maneuver with sticks across the ice, with “Oceanside Ice Arena” visible overhead.

**parsed_caption:**

> Players in red and maroon jerseys skate on an ice rink during a hockey game. A goalie stands near the net, while others maneuver with sticks across the ice, with “Oceanside Ice Arena” visible overhead.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 073090fa7e0c6c80f67ed0c260aa4cedcef5e326343311c80603a39aa3347014:q0 | Oceanside Ice Arena | oceanside ice arena | raw_quote_span |  | 162:183 | 162:183 |

### Sentences
| sentence | token_span |
| --- | --- |
| Players in red and maroon jerseys skate on an ice rink during a hockey game. | 0:15 |
| A goalie stands near the net, while others maneuver with sticks across the ice, with “Oceanside Ice Arena” visible overhead. | 15:36 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Players | Players | player | nsubj | skate | 0:1 |
| red and maroon jerseys | jerseys | jersey | pobj | in | 2:6 |
| an ice rink | ice rink | ice_rink | pobj | on | 8:10 |
| a hockey game | game | game | pobj | during | 11:14 |
| A goalie | goalie | goalie | nsubj | stands | 15:17 |
| the net | net | net | pobj | near | 19:21 |
| others | others | other | nsubj | maneuver | 23:24 |
| sticks | sticks | stick | pobj | with | 26:27 |
| the ice | ice | ice | pobj | across | 28:30 |
| “Oceanside Ice Arena” | “Oceanside Ice Arena” | oceanside_ice_arena | nsubj | visible | 32:33 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Players | player | NOUN | NNS | nsubj | skate | 6 |
| 1 | in | in | ADP | IN | prep | Players | 0 |
| 2 | red | red | ADJ | JJ | amod | jerseys | 5 |
| 3 | and | and | CCONJ | CC | cc | red | 2 |
| 4 | maroon | maroon | NOUN | NN | conj | red | 2 |
| 5 | jerseys | jersey | NOUN | NNS | pobj | in | 1 |
| 6 | skate | skate | VERB | VBP | ROOT | skate | 6 |
| 7 | on | on | ADP | IN | prep | skate | 6 |
| 8 | an | an | DET | DT | det | ice rink | 9 |
| 9 | ice rink | ice_rink | NOUN | NN | pobj | on | 7 |
| 10 | during | during | ADP | IN | prep | skate | 6 |
| 11 | a | a | DET | DT | det | game | 13 |
| 12 | hockey | hockey | NOUN | NN | compound | game | 13 |
| 13 | game | game | NOUN | NN | pobj | during | 10 |
| 14 | . | . | PUNCT | . | punct | skate | 6 |
| 15 | A | a | DET | DT | det | goalie | 16 |
| 16 | goalie | goalie | NOUN | NN | nsubj | stands | 17 |
| 17 | stands | stand | VERB | VBZ | ROOT | stands | 17 |
| 18 | near | near | ADP | IN | prep | stands | 17 |
| 19 | the | the | DET | DT | det | net | 20 |
| 20 | net | net | NOUN | NN | pobj | near | 18 |
| 21 | , | , | PUNCT | , | punct | stands | 17 |
| 22 | while | while | SCONJ | IN | mark | maneuver | 24 |
| 23 | others | other | NOUN | NNS | nsubj | maneuver | 24 |
| 24 | maneuver | maneuver | VERB | VBP | advcl | stands | 17 |
| 25 | with | with | ADP | IN | prep | maneuver | 24 |
| 26 | sticks | stick | NOUN | NNS | pobj | with | 25 |
| 27 | across | across | ADP | IN | prep | maneuver | 24 |
| 28 | the | the | DET | DT | det | ice | 29 |
| 29 | ice | ice | NOUN | NN | pobj | across | 27 |
| 30 | , | , | PUNCT | , | punct | maneuver | 24 |
| 31 | with | with | SCONJ | IN | mark | visible | 33 |
| 32 | “Oceanside Ice Arena” | oceanside_ice_arena | PROPN | NNP | nsubj | visible | 33 |
| 33 | visible | visible | ADJ | JJ | advcl | maneuver | 24 |
| 34 | overhead | overhead | ADV | RB | advmod | visible | 33 |
| 35 | . | . | PUNCT | . | punct | stands | 17 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “Oceanside Ice Arena” | oceanside_ice_arena | doc_quote | 32 | quote_text | high |
| m1 | object | Players | player | chunk0 | 0 | noun_chunk_root | high |
| m2 | object | jerseys | jersey | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | red | red | chunk1 | 2 | color_attribute | high |
| m4 | attribute | maroon | maroon | chunk1 | 4 | color_attribute | high |
| m5 | object | ice rink | ice_rink | chunk2 | 9 | noun_chunk_root | high |
| m6 | object | game | game | chunk3 | 13 | noun_chunk_root | high |
| m7 | attribute | hockey | hockey | chunk3 | 12 | compound_modifier | medium |
| m8 | object | goalie | goalie | chunk4 | 16 | noun_chunk_root | high |
| m9 | object | net | net | chunk5 | 20 | noun_chunk_root | high |
| m10 | object | sticks | stick | chunk7 | 26 | noun_chunk_root | high |
| m11 | object | ice | ice | chunk8 | 29 | noun_chunk_root | high |
| m12 | reference | others | other | nominal_reference | 23 | contrastive_reference | high |
| m13 | action | skate | skate | doc | 6 | verb_predicate | high |
| m14 | action | stands | stand | doc | 17 | verb_predicate | high |
| m15 | action | maneuver | maneuver | doc | 24 | verb_predicate | high |

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

## 14

**caption_shape:** `multi-sentence`
**caption_id:** `074828240e5fe34cfa12b6a1e086f86792df9fb2aaea04ed2986bdf95ae0c014`

> A flowing river rushes over rocks through a forested area. Autumn leaves in shades of orange and brown line the banks, with trees and bushes visible along the shoreline. The water moves quickly, creating white rapids as it flows past the rocky edge.

### Sentences
| sentence | token_span |
| --- | --- |
| A flowing river rushes over rocks through a forested area. | 0:11 |
| Autumn leaves in shades of orange and brown line the banks, with trees and bushes visible along the shoreline. | 11:32 |
| The water moves quickly, creating white rapids as it flows past the rocky edge. | 32:48 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A flowing river | river | river | nsubj | rushes | 0:3 |
| rocks | rocks | rock | pobj | over | 5:6 |
| a forested area | area | area | pobj | through | 7:10 |
| Autumn leaves | leaves | leaf | nsubj | line | 11:13 |
| shades | shades | shade | pobj | in | 14:15 |
| orange | orange | orange | pobj | of | 16:17 |
| brown | brown | brown | conj | orange | 18:19 |
| the banks | banks | bank | dobj | line | 20:22 |
| trees | trees | tree | nsubj | visible | 24:25 |
| bushes | bushes | bush | conj | trees | 26:27 |
| the shoreline | shoreline | shoreline | pobj | along | 29:31 |
| The water | water | water | nsubj | moves | 32:34 |
| white rapids | rapids | rapid | dobj | creating | 38:40 |
| it | it | it | nsubj | flows | 41:42 |
| the rocky edge | edge | edge | pobj | past | 44:47 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | river | 2 |
| 1 | flowing | flow | VERB | VBG | amod | river | 2 |
| 2 | river | river | NOUN | NN | nsubj | rushes | 3 |
| 3 | rushes | rush | VERB | VBZ | ROOT | rushes | 3 |
| 4 | over | over | ADP | IN | prep | rushes | 3 |
| 5 | rocks | rock | NOUN | NNS | pobj | over | 4 |
| 6 | through | through | ADP | IN | prep | rushes | 3 |
| 7 | a | a | DET | DT | det | area | 9 |
| 8 | forested | forested | ADJ | JJ | amod | area | 9 |
| 9 | area | area | NOUN | NN | pobj | through | 6 |
| 10 | . | . | PUNCT | . | punct | rushes | 3 |
| 11 | Autumn | Autumn | PROPN | NNP | compound | leaves | 12 |
| 12 | leaves | leaf | NOUN | NNS | nsubj | line | 19 |
| 13 | in | in | ADP | IN | prep | leaves | 12 |
| 14 | shades | shade | NOUN | NNS | pobj | in | 13 |
| 15 | of | of | ADP | IN | prep | shades | 14 |
| 16 | orange | orange | NOUN | NN | pobj | of | 15 |
| 17 | and | and | CCONJ | CC | cc | orange | 16 |
| 18 | brown | brown | NOUN | NN | conj | orange | 16 |
| 19 | line | line | VERB | VBP | ROOT | line | 19 |
| 20 | the | the | DET | DT | det | banks | 21 |
| 21 | banks | bank | NOUN | NNS | dobj | line | 19 |
| 22 | , | , | PUNCT | , | punct | line | 19 |
| 23 | with | with | SCONJ | IN | mark | visible | 27 |
| 24 | trees | tree | NOUN | NNS | nsubj | visible | 27 |
| 25 | and | and | CCONJ | CC | cc | trees | 24 |
| 26 | bushes | bush | NOUN | NNS | conj | trees | 24 |
| 27 | visible | visible | ADJ | JJ | advcl | line | 19 |
| 28 | along | along | ADP | IN | prep | visible | 27 |
| 29 | the | the | DET | DT | det | shoreline | 30 |
| 30 | shoreline | shoreline | NOUN | NN | pobj | along | 28 |
| 31 | . | . | PUNCT | . | punct | line | 19 |
| 32 | The | the | DET | DT | det | water | 33 |
| 33 | water | water | NOUN | NN | nsubj | moves | 34 |
| 34 | moves | move | VERB | VBZ | ROOT | moves | 34 |
| 35 | quickly | quickly | ADV | RB | advmod | moves | 34 |
| 36 | , | , | PUNCT | , | punct | moves | 34 |
| 37 | creating | create | VERB | VBG | advcl | moves | 34 |
| 38 | white | white | ADJ | JJ | amod | rapids | 39 |
| 39 | rapids | rapid | NOUN | NNS | dobj | creating | 37 |
| 40 | as | as | SCONJ | IN | mark | flows | 42 |
| 41 | it | it | PRON | PRP | nsubj | flows | 42 |
| 42 | flows | flow | VERB | VBZ | advcl | creating | 37 |
| 43 | past | past | ADP | IN | prep | flows | 42 |
| 44 | the | the | DET | DT | det | edge | 46 |
| 45 | rocky | rocky | ADJ | JJ | amod | edge | 46 |
| 46 | edge | edge | NOUN | NN | pobj | past | 43 |
| 47 | . | . | PUNCT | . | punct | moves | 34 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | river | river | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | flowing | flow | chunk0 | 1 | state_attribute | medium |
| m2 | object | rocks | rock | chunk1 | 5 | noun_chunk_root | high |
| m3 | object | area | area | chunk2 | 9 | noun_chunk_root | high |
| m4 | attribute | forested | forested | chunk2 | 8 | modifier_attribute | medium |
| m5 | object | leaves | leaf | chunk3 | 12 | noun_chunk_root | high |
| m6 | attribute | Autumn | autumn | chunk3 | 11 | compound_modifier | medium |
| m7 | object | shades | shade | chunk4 | 14 | noun_chunk_root | high |
| m8 | attribute | orange | orange | chunk5 | 16 | color_attribute | high |
| m9 | attribute | brown | brown | chunk6 | 18 | color_attribute | high |
| m10 | object | banks | bank | chunk7 | 21 | noun_chunk_root | high |
| m11 | object | trees | tree | chunk8 | 24 | noun_chunk_root | high |
| m12 | object | bushes | bush | chunk9 | 26 | noun_chunk_root | high |
| m13 | object | shoreline | shoreline | chunk10 | 30 | noun_chunk_root | high |
| m14 | object | water | water | chunk11 | 33 | noun_chunk_root | high |
| m15 | object | rapids | rapid | chunk12 | 39 | noun_chunk_root | high |
| m16 | attribute | white | white | chunk12 | 38 | color_attribute | high |
| m17 | context | edge | edge | chunk14 | 46 | spatial_region | medium |
| m18 | action | rushes | rush | doc | 3 | verb_predicate | high |
| m19 | action | line | line | doc | 19 | verb_predicate | high |
| m20 | action | moves | move | doc | 34 | verb_predicate | high |
| m21 | action | creating | create | doc | 37 | verb_predicate | high |
| m22 | action | flows | flow | doc | 42 | verb_predicate | high |

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

## 15

**caption_shape:** `sentence-like`
**caption_id:** `077ba6d8a231652e13b4231ec399624846c49c8e63d9d155fe9ed8275c884414`

> Tall cacti and spiky plants grow inside a glass greenhouse.

### Sentences
| sentence | token_span |
| --- | --- |
| Tall cacti and spiky plants grow inside a glass greenhouse. | 0:11 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Tall cacti | cacti | cactus | nsubj | grow | 0:2 |
| spiky plants | plants | plant | conj | cacti | 3:5 |
| a glass greenhouse | greenhouse | greenhouse | pobj | inside | 7:10 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Tall | tall | ADJ | JJ | amod | cacti | 1 |
| 1 | cacti | cactus | NOUN | NNS | nsubj | grow | 5 |
| 2 | and | and | CCONJ | CC | cc | cacti | 1 |
| 3 | spiky | spiky | ADJ | JJ | amod | plants | 4 |
| 4 | plants | plant | NOUN | NNS | conj | cacti | 1 |
| 5 | grow | grow | VERB | VBP | ROOT | grow | 5 |
| 6 | inside | inside | ADP | IN | prep | grow | 5 |
| 7 | a | a | DET | DT | det | greenhouse | 9 |
| 8 | glass | glass | NOUN | NN | compound | greenhouse | 9 |
| 9 | greenhouse | greenhouse | NOUN | NN | pobj | inside | 6 |
| 10 | . | . | PUNCT | . | punct | grow | 5 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | cacti | cactus | chunk0 | 1 | noun_chunk_root | high |
| m1 | attribute | Tall | tall | chunk0 | 0 | size_attribute | high |
| m2 | object | plants | plant | chunk1 | 4 | noun_chunk_root | high |
| m3 | attribute | spiky | spiky | chunk1 | 3 | modifier_attribute | medium |
| m4 | object | greenhouse | greenhouse | chunk2 | 9 | noun_chunk_root | high |
| m5 | attribute | glass | glass | chunk2 | 8 | material_attribute | high |
| m6 | action | grow | grow | doc | 5 | verb_predicate | high |

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

## 16

**caption_shape:** `sentence-like`
**caption_id:** `07c7561dff94b993369989b7144c59ce2fcd6473050e61d7fa93b75382bcf014`

> A harvested field of dry wheat stretches toward a line of green trees, with a distant town visible on the horizon.

### Sentences
| sentence | token_span |
| --- | --- |
| A harvested field of dry wheat stretches toward a line of green trees, with a distant town visible on the horizon. | 0:23 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A harvested field | field | field | nsubj | stretches | 0:3 |
| dry wheat | wheat | wheat | pobj | of | 4:6 |
| a line | line | line | pobj | toward | 8:10 |
| green trees | trees | tree | pobj | of | 11:13 |
| a distant town | town | town | nsubj | visible | 15:18 |
| the horizon | horizon | horizon | pobj | on | 20:22 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | field | 2 |
| 1 | harvested | harvest | VERB | VBN | amod | field | 2 |
| 2 | field | field | NOUN | NN | nsubj | stretches | 6 |
| 3 | of | of | ADP | IN | prep | field | 2 |
| 4 | dry | dry | ADJ | JJ | amod | wheat | 5 |
| 5 | wheat | wheat | NOUN | NN | pobj | of | 3 |
| 6 | stretches | stretch | VERB | VBZ | ROOT | stretches | 6 |
| 7 | toward | toward | ADP | IN | prep | stretches | 6 |
| 8 | a | a | DET | DT | det | line | 9 |
| 9 | line | line | NOUN | NN | pobj | toward | 7 |
| 10 | of | of | ADP | IN | prep | line | 9 |
| 11 | green | green | ADJ | JJ | amod | trees | 12 |
| 12 | trees | tree | NOUN | NNS | pobj | of | 10 |
| 13 | , | , | PUNCT | , | punct | stretches | 6 |
| 14 | with | with | SCONJ | IN | mark | visible | 18 |
| 15 | a | a | DET | DT | det | town | 17 |
| 16 | distant | distant | ADJ | JJ | amod | town | 17 |
| 17 | town | town | NOUN | NN | nsubj | visible | 18 |
| 18 | visible | visible | ADJ | JJ | advcl | stretches | 6 |
| 19 | on | on | ADP | IN | prep | visible | 18 |
| 20 | the | the | DET | DT | det | horizon | 21 |
| 21 | horizon | horizon | NOUN | NN | pobj | on | 19 |
| 22 | . | . | PUNCT | . | punct | stretches | 6 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | field | field | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | harvested | harvest | chunk0 | 1 | state_attribute | medium |
| m2 | object | wheat | wheat | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | dry | dry | chunk1 | 4 | modifier_attribute | medium |
| m4 | object | line | line | chunk2 | 9 | noun_chunk_root | high |
| m5 | object | trees | tree | chunk3 | 12 | noun_chunk_root | high |
| m6 | attribute | green | green | chunk3 | 11 | color_attribute | high |
| m7 | object | town | town | chunk4 | 17 | noun_chunk_root | high |
| m8 | attribute | distant | distant | chunk4 | 16 | modifier_attribute | medium |
| m9 | object | horizon | horizon | chunk5 | 21 | noun_chunk_root | high |
| m10 | action | stretches | stretch | doc | 6 | verb_predicate | high |

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

## 17

**caption_shape:** `tag-list-like`
**caption_id:** `09c8d891bb19dae925f67bbfa36ab9cbab8992b837627c05b2737d7f93d0dc14`

> stained glass, crucifix, altar, church interior, wooden pews, candle

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | stained glass | stained glass | 0:13 |
| t1 | crucifix | crucifix | 15:23 |
| t2 | altar | altar | 25:30 |
| t3 | church interior | church interior | 32:47 |
| t4 | wooden pews | wooden pews | 49:60 |
| t5 | candle | candle | 62:68 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | stained glass | glass | glass | ROOT | glass | 0:2 | 0:13 |
| t1 | crucifix | crucifix | crucifix | ROOT | crucifix | 0:1 | 15:23 |
| t2 | altar | altar | altar | ROOT | altar | 0:1 | 25:30 |
| t3 | church interior | interior | interior | ROOT | interior | 0:2 | 32:47 |
| t4 | wooden pews | pews | pew | ROOT | pews | 0:2 | 49:60 |
| t5 | candle | candle | candle | ROOT | candle | 0:1 | 62:68 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | stained | stained | ADJ | ADJ | JJ | JJ | amod | glass | 1 | 0:7 |
| t0 | 1 | glass | glass | NOUN | NOUN | NN | NN | ROOT | glass | 1 | 8:13 |
| t1 | 0 | crucifix | crucifix | NOUN | NOUN | NN | NN | ROOT | crucifix | 0 | 15:23 |
| t2 | 0 | altar | altar | PROPN | NOUN | NNP | NN | ROOT | altar | 0 | 25:30 |
| t3 | 0 | church | church | NOUN | NOUN | NN | NN | compound | interior | 1 | 32:38 |
| t3 | 1 | interior | interior | NOUN | NOUN | NN | NN | ROOT | interior | 1 | 39:47 |
| t4 | 0 | wooden | wooden | PROPN | ADJ | NNP | JJ | compound | pews | 1 | 49:55 |
| t4 | 1 | pews | pew | NOUN | NOUN | NNS | NNS | ROOT | pews | 1 | 56:60 |
| t5 | 0 | candle | candle | NOUN | NOUN | NN | NN | ROOT | candle | 0 | 62:68 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | glass | glass | t0 | 1 | segment_head | high |
| m1 | attribute | stained | stained | t0 | 0 | attribute | high |
| m2 | object | crucifix | crucifix | t1 | 0 | segment_head | high |
| m3 | object | altar | altar | t2 | 0 | segment_head | high |
| m4 | object | interior | interior | t3 | 1 | segment_head | high |
| m5 | attribute | church | church | t3 | 0 | attribute | high |
| m6 | object | pews | pew | t4 | 1 | segment_head | high |
| m7 | attribute | wooden | wooden | t4 | 0 | attribute | high |
| m8 | object | candle | candle | t5 | 0 | segment_head | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> glass |
| e1 | has_attribute | m4 | m5 | high | t3 internal compound -> interior |
| e2 | has_attribute | m6 | m7 | high | t4 internal compound -> pews |

## 18

**caption_shape:** `multi-sentence`
**caption_id:** `09da0bd4c73bd7a26a8c552230082783f6c4e7edebcdb4ebf9015e90bfc5f814`

> A person in a white Stormtrooper costume sits on the ground next to two children dressed as Pikachu. One child is fully in a yellow Pikachu outfit, while another wears a yellow hooded costume with red stripes. They are outdoors on a paved surface near a glass building with a yellow lamp nearby.

### Sentences
| sentence | token_span |
| --- | --- |
| A person in a white Stormtrooper costume sits on the ground next to two children dressed as Pikachu. | 0:19 |
| One child is fully in a yellow Pikachu outfit, while another wears a yellow hooded costume with red stripes. | 19:40 |
| They are outdoors on a paved surface near a glass building with a yellow lamp nearby. | 40:56 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A person | person | person | nsubj | sits | 0:2 |
| a white Stormtrooper costume | costume | costume | pobj | in | 3:7 |
| the ground | ground | ground | pobj | on | 9:11 |
| two children | children | child | pobj | to | 13:15 |
| Pikachu | Pikachu | Pikachu | pobj | as | 17:18 |
| One child | child | child | nsubj | is | 19:21 |
| a yellow Pikachu outfit | outfit | outfit | pobj | in | 24:28 |
| another | another | another | nsubj | wears | 30:31 |
| a yellow hooded costume | costume | costume | dobj | wears | 32:36 |
| red stripes | stripes | stripe | pobj | with | 37:39 |
| They | They | they | nsubj | are | 40:41 |
| a paved surface | paved surface | paved_surface | pobj | on | 44:46 |
| a glass building | building | building | pobj | near | 47:50 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | person | 1 |
| 1 | person | person | NOUN | NN | nsubj | sits | 7 |
| 2 | in | in | ADP | IN | prep | person | 1 |
| 3 | a | a | DET | DT | det | costume | 6 |
| 4 | white | white | ADJ | JJ | amod | costume | 6 |
| 5 | Stormtrooper | Stormtrooper | PROPN | NNP | compound | costume | 6 |
| 6 | costume | costume | NOUN | NN | pobj | in | 2 |
| 7 | sits | sit | VERB | VBZ | ROOT | sits | 7 |
| 8 | on | on | ADP | IN | prep | sits | 7 |
| 9 | the | the | DET | DT | det | ground | 10 |
| 10 | ground | ground | NOUN | NN | pobj | on | 8 |
| 11 | next | next | ADV | RB | advmod | sits | 7 |
| 12 | to | to | ADP | IN | prep | next | 11 |
| 13 | two | two | NUM | CD | nummod | children | 14 |
| 14 | children | child | NOUN | NNS | pobj | to | 12 |
| 15 | dressed | dress | VERB | VBN | acl | children | 14 |
| 16 | as | as | ADP | IN | prep | dressed | 15 |
| 17 | Pikachu | Pikachu | PROPN | NNP | pobj | as | 16 |
| 18 | . | . | PUNCT | . | punct | sits | 7 |
| 19 | One | one | NUM | CD | nummod | child | 20 |
| 20 | child | child | NOUN | NN | nsubj | is | 21 |
| 21 | is | be | AUX | VBZ | ROOT | is | 21 |
| 22 | fully | fully | ADV | RB | advmod | is | 21 |
| 23 | in | in | ADP | IN | prep | is | 21 |
| 24 | a | a | DET | DT | det | outfit | 27 |
| 25 | yellow | yellow | ADJ | JJ | amod | outfit | 27 |
| 26 | Pikachu | Pikachu | PROPN | NNP | compound | outfit | 27 |
| 27 | outfit | outfit | NOUN | NN | pobj | in | 23 |
| 28 | , | , | PUNCT | , | punct | is | 21 |
| 29 | while | while | SCONJ | IN | mark | wears | 31 |
| 30 | another | another | PRON | DT | nsubj | wears | 31 |
| 31 | wears | wear | VERB | VBZ | advcl | is | 21 |
| 32 | a | a | DET | DT | det | costume | 35 |
| 33 | yellow | yellow | ADJ | JJ | amod | costume | 35 |
| 34 | hooded | hooded | ADJ | JJ | amod | costume | 35 |
| 35 | costume | costume | NOUN | NN | dobj | wears | 31 |
| 36 | with | with | ADP | IN | prep | costume | 35 |
| 37 | red | red | ADJ | JJ | amod | stripes | 38 |
| 38 | stripes | stripe | NOUN | NNS | pobj | with | 36 |
| 39 | . | . | PUNCT | . | punct | is | 21 |
| 40 | They | they | PRON | PRP | nsubj | are | 41 |
| 41 | are | be | AUX | VBP | ROOT | are | 41 |
| 42 | outdoors | outdoors | ADV | RB | advmod | are | 41 |
| 43 | on | on | ADP | IN | prep | are | 41 |
| 44 | a | a | DET | DT | det | paved surface | 45 |
| 45 | paved surface | paved_surface | NOUN | NN | pobj | on | 43 |
| 46 | near | near | ADP | IN | prep | paved surface | 45 |
| 47 | a | a | DET | DT | det | building | 49 |
| 48 | glass | glass | NOUN | NN | compound | building | 49 |
| 49 | building | building | NOUN | NN | pobj | near | 46 |
| 50 | with | with | SCONJ | IN | mark | lamp | 53 |
| 51 | a | a | DET | DT | det | lamp | 53 |
| 52 | yellow | yellow | ADJ | JJ | amod | lamp | 53 |
| 53 | lamp | lamp | NOUN | NN | advcl | are | 41 |
| 54 | nearby | nearby | ADV | RB | advmod | lamp | 53 |
| 55 | . | . | PUNCT | . | punct | are | 41 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | costume | costume | chunk1 | 6 | noun_chunk_root | high |
| m2 | attribute | white | white | chunk1 | 4 | color_attribute | high |
| m3 | attribute | Stormtrooper | stormtrooper | chunk1 | 5 | compound_modifier | medium |
| m4 | object | ground | ground | chunk2 | 10 | noun_chunk_root | high |
| m5 | object | children | child | chunk3 | 14 | noun_chunk_root | high |
| m6 | quantity | two | two | chunk3 | 13 | exact_quantity | high |
| m7 | object | Pikachu | pikachu | chunk4 | 17 | noun_chunk_root | high |
| m8 | object | child | child | chunk5 | 20 | noun_chunk_root | high |
| m9 | quantity | One | one | chunk5 | 19 | exact_quantity | high |
| m10 | object | outfit | outfit | chunk6 | 27 | noun_chunk_root | high |
| m11 | attribute | yellow | yellow | chunk6 | 25 | color_attribute | high |
| m12 | attribute | Pikachu | pikachu | chunk6 | 26 | compound_modifier | medium |
| m13 | object | costume | costume | chunk8 | 35 | noun_chunk_root | high |
| m14 | attribute | yellow | yellow | chunk8 | 33 | color_attribute | high |
| m15 | attribute | hooded | hooded | chunk8 | 34 | modifier_attribute | medium |
| m16 | object | stripes | stripe | chunk9 | 38 | noun_chunk_root | high |
| m17 | attribute | red | red | chunk9 | 37 | color_attribute | high |
| m18 | object | paved surface | paved_surface | chunk11 | 45 | noun_chunk_root | high |
| m19 | object | building | building | chunk12 | 49 | noun_chunk_root | high |
| m20 | attribute | glass | glass | chunk12 | 48 | material_attribute | high |
| m21 | context | outdoors | outdoors | doc | 42 | scene_context | high |
| m22 | reference | another | another | nominal_reference | 30 | contrastive_reference | high |
| m23 | action | sits | sit | doc | 7 | verb_predicate | high |
| m24 | action | dressed | dress | doc | 15 | verb_predicate | high |
| m25 | action | wears | wear | doc | 31 | verb_predicate | high |
| m26 | object | lamp | lamp | with_absolute50 | 53 | with_absolute_recovered_object | medium |
| m27 | attribute | yellow | yellow | with_absolute50 | 52 | color_attribute | high |

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

## 19

**caption_shape:** `sentence-like`
**caption_id:** `0b00d4baf64284f327aac70f21757bae78d0d363b89b04dd1d20d9c90b864814`

> Two hockey players skate on the ice, one in a white jersey with number 93 and another in blue, near the goal.

### Sentences
| sentence | token_span |
| --- | --- |
| Two hockey players skate on the ice, one in a white jersey with number 93 and another in blue, near the goal. | 0:24 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Two hockey players | hockey players | hockey_player | nsubj | skate | 0:2 |
| the ice | ice | ice | pobj | on | 4:6 |
| a white jersey | jersey | jersey | pobj | in | 9:12 |
| number | number | number | pobj | with | 13:14 |
| another | another | another | conj | one | 16:17 |
| the goal | goal | goal | pobj | near | 21:23 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Two | two | NUM | CD | nummod | hockey players | 1 |
| 1 | hockey players | hockey_player | NOUN | NN | nsubj | skate | 2 |
| 2 | skate | skate | VERB | VBP | ROOT | skate | 2 |
| 3 | on | on | ADP | IN | prep | skate | 2 |
| 4 | the | the | DET | DT | det | ice | 5 |
| 5 | ice | ice | NOUN | NN | pobj | on | 3 |
| 6 | , | , | PUNCT | , | punct | skate | 2 |
| 7 | one | one | NUM | CD | appos | skate | 2 |
| 8 | in | in | ADP | IN | prep | one | 7 |
| 9 | a | a | DET | DT | det | jersey | 11 |
| 10 | white | white | ADJ | JJ | amod | jersey | 11 |
| 11 | jersey | jersey | NOUN | NN | pobj | in | 8 |
| 12 | with | with | ADP | IN | prep | jersey | 11 |
| 13 | number | number | NOUN | NN | pobj | with | 12 |
| 14 | 93 | 93 | NUM | CD | nummod | number | 13 |
| 15 | and | and | CCONJ | CC | cc | one | 7 |
| 16 | another | another | PRON | DT | conj | one | 7 |
| 17 | in | in | ADP | IN | prep | another | 16 |
| 18 | blue | blue | ADJ | JJ | pobj | in | 17 |
| 19 | , | , | PUNCT | , | punct | another | 16 |
| 20 | near | near | ADP | IN | conj | another | 16 |
| 21 | the | the | DET | DT | det | goal | 22 |
| 22 | goal | goal | NOUN | NN | pobj | near | 20 |
| 23 | . | . | PUNCT | . | punct | skate | 2 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hockey players | hockey_player | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Two | two | chunk0 | 0 | exact_quantity | high |
| m2 | object | ice | ice | chunk1 | 5 | noun_chunk_root | high |
| m3 | object | jersey | jersey | chunk2 | 11 | noun_chunk_root | high |
| m4 | attribute | white | white | chunk2 | 10 | color_attribute | high |
| m5 | object | number | number | chunk3 | 13 | noun_chunk_root | high |
| m6 | object | goal | goal | chunk5 | 22 | noun_chunk_root | high |
| m7 | reference | one | one | nominal_reference | 7 | singular_substitute | high |
| m8 | reference | another | another | nominal_reference | 16 | contrastive_reference | high |
| m9 | action | skate | skate | doc | 2 | verb_predicate | high |

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

## 20

**caption_shape:** `multi-sentence`
**caption_id:** `0bac1dd05b619aba37f1d15eedf4547bcfa902922da302c5d48e27264e25dc14`

> A woman in a striped skirt and black blazer walks beside a man in a blue suit, both wearing face masks. They are in a large indoor hall with seated attendees, some wearing masks and holding papers, while others stand nearby.

### Sentences
| sentence | token_span |
| --- | --- |
| A woman in a striped skirt and black blazer walks beside a man in a blue suit, both wearing face masks. | 0:22 |
| They are in a large indoor hall with seated attendees, some wearing masks and holding papers, while others stand nearby. | 22:45 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A woman | woman | woman | nsubj | walks | 0:2 |
| a striped skirt | skirt | skirt | pobj | in | 3:6 |
| black blazer | blazer | blazer | conj | skirt | 7:9 |
| a man | man | man | pobj | beside | 11:13 |
| a blue suit | suit | suit | pobj | in | 14:17 |
| both | both | both | nsubj | wearing | 18:19 |
| face masks | face masks | face_mask | dobj | wearing | 20:21 |
| They | They | they | nsubj | are | 22:23 |
| a large indoor hall | hall | hall | pobj | in | 25:29 |
| seated attendees | attendees | attendee | pobj | with | 30:32 |
| some | some | some | nsubj | wearing | 33:34 |
| masks | masks | mask | dobj | wearing | 35:36 |
| papers | papers | paper | dobj | holding | 38:39 |
| others | others | other | nsubj | stand | 41:42 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | woman | 1 |
| 1 | woman | woman | NOUN | NN | nsubj | walks | 9 |
| 2 | in | in | ADP | IN | prep | woman | 1 |
| 3 | a | a | DET | DT | det | skirt | 5 |
| 4 | striped | striped | ADJ | JJ | amod | skirt | 5 |
| 5 | skirt | skirt | NOUN | NN | pobj | in | 2 |
| 6 | and | and | CCONJ | CC | cc | skirt | 5 |
| 7 | black | black | ADJ | JJ | amod | blazer | 8 |
| 8 | blazer | blazer | NOUN | NN | conj | skirt | 5 |
| 9 | walks | walk | VERB | VBZ | ROOT | walks | 9 |
| 10 | beside | beside | ADP | IN | prep | walks | 9 |
| 11 | a | a | DET | DT | det | man | 12 |
| 12 | man | man | NOUN | NN | pobj | beside | 10 |
| 13 | in | in | ADP | IN | prep | man | 12 |
| 14 | a | a | DET | DT | det | suit | 16 |
| 15 | blue | blue | ADJ | JJ | amod | suit | 16 |
| 16 | suit | suit | NOUN | NN | pobj | in | 13 |
| 17 | , | , | PUNCT | , | punct | walks | 9 |
| 18 | both | both | PRON | DT | nsubj | wearing | 19 |
| 19 | wearing | wear | VERB | VBG | advcl | walks | 9 |
| 20 | face masks | face_mask | NOUN | NN | dobj | wearing | 19 |
| 21 | . | . | PUNCT | . | punct | walks | 9 |
| 22 | They | they | PRON | PRP | nsubj | are | 23 |
| 23 | are | be | AUX | VBP | ROOT | are | 23 |
| 24 | in | in | ADP | IN | prep | are | 23 |
| 25 | a | a | DET | DT | det | hall | 28 |
| 26 | large | large | ADJ | JJ | amod | hall | 28 |
| 27 | indoor | indoor | ADJ | JJ | amod | hall | 28 |
| 28 | hall | hall | NOUN | NN | pobj | in | 24 |
| 29 | with | with | ADP | IN | prep | hall | 28 |
| 30 | seated | seat | VERB | VBN | amod | attendees | 31 |
| 31 | attendees | attendee | NOUN | NNS | pobj | with | 29 |
| 32 | , | , | PUNCT | , | punct | are | 23 |
| 33 | some | some | PRON | DT | nsubj | wearing | 34 |
| 34 | wearing | wear | VERB | VBG | advcl | are | 23 |
| 35 | masks | mask | NOUN | NNS | dobj | wearing | 34 |
| 36 | and | and | CCONJ | CC | cc | wearing | 34 |
| 37 | holding | hold | VERB | VBG | conj | wearing | 34 |
| 38 | papers | paper | NOUN | NNS | dobj | holding | 37 |
| 39 | , | , | PUNCT | , | punct | are | 23 |
| 40 | while | while | SCONJ | IN | mark | stand | 42 |
| 41 | others | other | NOUN | NNS | nsubj | stand | 42 |
| 42 | stand | stand | VERB | VBP | advcl | are | 23 |
| 43 | nearby | nearby | ADV | RB | advmod | stand | 42 |
| 44 | . | . | PUNCT | . | punct | are | 23 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | skirt | skirt | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | striped | striped | chunk1 | 4 | modifier_attribute | medium |
| m3 | object | blazer | blazer | chunk2 | 8 | noun_chunk_root | high |
| m4 | attribute | black | black | chunk2 | 7 | color_attribute | high |
| m5 | object | man | man | chunk3 | 12 | noun_chunk_root | high |
| m6 | object | suit | suit | chunk4 | 16 | noun_chunk_root | high |
| m7 | attribute | blue | blue | chunk4 | 15 | color_attribute | high |
| m8 | quantity | both | both | chunk5 | 18 | group_quantity | high |
| m9 | object | face masks | face_mask | chunk6 | 20 | noun_chunk_root | high |
| m10 | object | hall | hall | chunk8 | 28 | noun_chunk_root | high |
| m11 | attribute | large | large | chunk8 | 26 | size_attribute | high |
| m12 | attribute | indoor | indoor | chunk8 | 27 | modifier_attribute | medium |
| m13 | object | attendees | attendee | chunk9 | 31 | noun_chunk_root | high |
| m14 | attribute | seated | seat | chunk9 | 30 | state_attribute | medium |
| m15 | quantity | some | some | chunk10 | 33 | indefinite_quantity | medium |
| m16 | object | masks | mask | chunk11 | 35 | noun_chunk_root | high |
| m17 | object | papers | paper | chunk12 | 38 | noun_chunk_root | high |
| m18 | group | a striped skirt and black blazer | skirt_and_blazer | nominal_reference | 5 | coordination_group | medium |
| m19 | reference | both | both | nominal_reference | 18 | group_reference | medium |
| m20 | action | walks | walk | doc | 9 | verb_predicate | high |
| m21 | action | wearing | wear | doc | 19 | verb_predicate | high |
| m22 | action | wearing | wear | doc | 34 | verb_predicate | high |
| m23 | action | holding | hold | doc | 37 | verb_predicate | high |
| m24 | action | stand | stand | doc | 42 | verb_predicate | high |

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

## 21

**caption_shape:** `multi-sentence`
**caption_id:** `0cd0a6340659d0c6e6c98e141a5f55de3e04855c63a4223534c3a901cda62014`

> A purple and white flower grows in the ground among brown leaves and green stems. The petals are slightly blurred, with a leaf visible to the right of the bloom. The setting appears to be outdoors on soil covered with fallen foliage.

### Sentences
| sentence | token_span |
| --- | --- |
| A purple and white flower grows in the ground among brown leaves and green stems. | 0:16 |
| The petals are slightly blurred, with a leaf visible to the right of the bloom. | 16:33 |
| The setting appears to be outdoors on soil covered with fallen foliage. | 33:46 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A purple and white flower | flower | flower | nsubj | grows | 0:5 |
| the ground | ground | ground | pobj | in | 7:9 |
| brown leaves | leaves | leaf | pobj | among | 10:12 |
| green stems | stems | stem | conj | leaves | 13:15 |
| The petals | petals | petal | nsubj | are | 16:18 |
| a leaf | leaf | leaf | pobj | with | 23:25 |
| the right | right | right | pobj | to | 27:29 |
| the bloom | bloom | bloom | pobj | of | 30:32 |
| The setting | setting | setting | nsubj | appears | 33:35 |
| soil | soil | soil | pobj | on | 40:41 |
| fallen foliage | foliage | foliage | pobj | with | 43:45 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | flower | 4 |
| 1 | purple | purple | ADJ | JJ | amod | flower | 4 |
| 2 | and | and | CCONJ | CC | cc | purple | 1 |
| 3 | white | white | ADJ | JJ | conj | purple | 1 |
| 4 | flower | flower | NOUN | NN | nsubj | grows | 5 |
| 5 | grows | grow | VERB | VBZ | ROOT | grows | 5 |
| 6 | in | in | ADP | IN | prep | grows | 5 |
| 7 | the | the | DET | DT | det | ground | 8 |
| 8 | ground | ground | NOUN | NN | pobj | in | 6 |
| 9 | among | among | ADP | IN | prep | grows | 5 |
| 10 | brown | brown | ADJ | JJ | amod | leaves | 11 |
| 11 | leaves | leaf | NOUN | NNS | pobj | among | 9 |
| 12 | and | and | CCONJ | CC | cc | leaves | 11 |
| 13 | green | green | ADJ | JJ | amod | stems | 14 |
| 14 | stems | stem | NOUN | NNS | conj | leaves | 11 |
| 15 | . | . | PUNCT | . | punct | grows | 5 |
| 16 | The | the | DET | DT | det | petals | 17 |
| 17 | petals | petal | NOUN | NNS | nsubj | are | 18 |
| 18 | are | be | AUX | VBP | ROOT | are | 18 |
| 19 | slightly | slightly | ADV | RB | advmod | blurred | 20 |
| 20 | blurred | blurred | ADJ | JJ | acomp | are | 18 |
| 21 | , | , | PUNCT | , | punct | blurred | 20 |
| 22 | with | with | ADP | IN | prep | blurred | 20 |
| 23 | a | a | DET | DT | det | leaf | 24 |
| 24 | leaf | leaf | NOUN | NN | pobj | with | 22 |
| 25 | visible | visible | ADJ | JJ | amod | leaf | 24 |
| 26 | to | to | ADP | IN | prep | visible | 25 |
| 27 | the | the | DET | DT | det | right | 28 |
| 28 | right | right | NOUN | NN | pobj | to | 26 |
| 29 | of | of | ADP | IN | prep | right | 28 |
| 30 | the | the | DET | DT | det | bloom | 31 |
| 31 | bloom | bloom | NOUN | NN | pobj | of | 29 |
| 32 | . | . | PUNCT | . | punct | are | 18 |
| 33 | The | the | DET | DT | det | setting | 34 |
| 34 | setting | setting | NOUN | NN | nsubj | appears | 35 |
| 35 | appears | appear | VERB | VBZ | ROOT | appears | 35 |
| 36 | to | to | PART | TO | aux | be | 37 |
| 37 | be | be | AUX | VB | xcomp | appears | 35 |
| 38 | outdoors | outdoors | ADV | RB | advmod | be | 37 |
| 39 | on | on | ADP | IN | prep | be | 37 |
| 40 | soil | soil | NOUN | NN | pobj | on | 39 |
| 41 | covered | cover | VERB | VBN | acl | soil | 40 |
| 42 | with | with | ADP | IN | prep | covered | 41 |
| 43 | fallen | fallen | ADJ | JJ | amod | foliage | 44 |
| 44 | foliage | foliage | NOUN | NN | pobj | with | 42 |
| 45 | . | . | PUNCT | . | punct | appears | 35 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | flower | flower | chunk0 | 4 | noun_chunk_root | high |
| m1 | attribute | purple | purple | chunk0 | 1 | color_attribute | high |
| m2 | attribute | white | white | chunk0 | 3 | color_attribute | high |
| m3 | object | ground | ground | chunk1 | 8 | noun_chunk_root | high |
| m4 | object | leaves | leaf | chunk2 | 11 | noun_chunk_root | high |
| m5 | attribute | brown | brown | chunk2 | 10 | color_attribute | high |
| m6 | object | stems | stem | chunk3 | 14 | noun_chunk_root | high |
| m7 | attribute | green | green | chunk3 | 13 | color_attribute | high |
| m8 | object | petals | petal | chunk4 | 17 | noun_chunk_root | high |
| m9 | object | leaf | leaf | chunk5 | 24 | noun_chunk_root | high |
| m10 | object | bloom | bloom | chunk7 | 31 | noun_chunk_root | high |
| m11 | context | setting | setting | chunk8 | 34 | scene_context | high |
| m12 | object | soil | soil | chunk9 | 40 | noun_chunk_root | high |
| m13 | object | foliage | foliage | chunk10 | 44 | noun_chunk_root | high |
| m14 | attribute | fallen | fallen | chunk10 | 43 | modifier_attribute | medium |
| m15 | context | outdoors | outdoors | doc | 38 | scene_context | high |
| m16 | action | grows | grow | doc | 5 | verb_predicate | high |
| m17 | action | appears | appear | doc | 35 | verb_predicate | high |
| m18 | action | covered | cover | doc | 41 | verb_predicate | high |

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

## 22

**caption_shape:** `tag-list-like`
**caption_id:** `0ceed50090c9ce8a5cd15726d04e79d1a6dc4cacd28d488f8beceb4d54d88014`

> dewy spiderweb, tree branch, natural setting

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | dewy spiderweb | dewy spiderweb | 0:14 |
| t1 | tree branch | tree branch | 16:27 |
| t2 | natural setting | natural setting | 29:44 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | dewy spiderweb | spiderweb | spiderweb | ROOT | spiderweb | 0:2 | 0:14 |
| t1 | tree branch | tree branch | tree_branch | ROOT | tree branch | 0:1 | 16:27 |
| t2 | natural setting | setting | setting | ROOT | setting | 0:2 | 29:44 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | dewy | dewy | ADJ | ADJ | JJ | JJ | amod | spiderweb | 1 | 0:4 |
| t0 | 1 | spiderweb | spiderweb | NOUN | NOUN | NN | NN | ROOT | spiderweb | 1 | 5:14 |
| t1 | 0 | tree branch | tree_branch | NOUN | NOUN | NN | NN | ROOT | tree branch | 0 | 16:27 |
| t2 | 0 | natural | natural | ADJ | ADJ | JJ | JJ | amod | setting | 1 | 29:36 |
| t2 | 1 | setting | setting | NOUN | NOUN | NN | NN | ROOT | setting | 1 | 37:44 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | spiderweb | spiderweb | t0 | 1 | segment_head | high |
| m1 | attribute | dewy | dewy | t0 | 0 | attribute | high |
| m2 | object | tree branch | tree_branch | t1 | 0 | segment_head | high |
| m3 | context | setting | setting | t2 | 1 | scene_context | high |
| m4 | attribute | natural | natural | t2 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> spiderweb |
| e1 | has_context | scene | m3 | high | t2 context tag |
| e2 | has_attribute | m3 | m4 | high | t2 internal amod -> setting |

## 23

**caption_shape:** `tag-list-like`
**caption_id:** `0d9d490cb1767dc4b6125b1e58afff17e0debdfdc2972d218ea1b3295c06b014`

> night street, brick building, lit windows, traffic light, moon

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | night street | night street | 0:12 |
| t1 | brick building | brick building | 14:28 |
| t2 | lit windows | lit windows | 30:41 |
| t3 | traffic light | traffic light | 43:56 |
| t4 | moon | moon | 58:62 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | night street | street | street | ROOT | street | 0:2 | 0:12 |
| t1 | brick building | building | building | ROOT | building | 0:2 | 14:28 |
| t2 | lit windows | windows | window | ROOT | windows | 0:2 | 30:41 |
| t3 | traffic light | traffic light | traffic_light | ROOT | traffic light | 0:1 | 43:56 |
| t4 | moon | moon | moon | ROOT | moon | 0:1 | 58:62 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | night | night | NOUN | NOUN | NN | NN | compound | street | 1 | 0:5 |
| t0 | 1 | street | street | PROPN | NOUN | NNP | NN | ROOT | street | 1 | 6:12 |
| t1 | 0 | brick | brick | NOUN | NOUN | NN | NN | compound | building | 1 | 14:19 |
| t1 | 1 | building | building | NOUN | NOUN | NN | NN | ROOT | building | 1 | 20:28 |
| t2 | 0 | lit | light | VERB | ADJ | VBN | VBN | amod | windows | 1 | 30:33 |
| t2 | 1 | windows | window | NOUN | NOUN | NNS | NNS | ROOT | windows | 1 | 34:41 |
| t3 | 0 | traffic light | traffic_light | NOUN | NOUN | NN | NN | ROOT | traffic light | 0 | 43:56 |
| t4 | 0 | moon | moon | NOUN | NOUN | NN | NN | ROOT | moon | 0 | 58:62 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | street | street | t0 | 1 | segment_head | high |
| m1 | attribute | night | night | t0 | 0 | attribute | high |
| m2 | object | building | building | t1 | 1 | segment_head | high |
| m3 | attribute | brick | brick | t1 | 0 | attribute | high |
| m4 | object | windows | window | t2 | 1 | segment_head | high |
| m5 | attribute | lit | light | t2 | 0 | state_attribute | high |
| m6 | object | traffic light | traffic_light | t3 | 0 | segment_head | high |
| m7 | object | moon | moon | t4 | 0 | segment_head | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> street |
| e1 | has_attribute | m2 | m3 | high | t1 internal compound -> building |
| e2 | has_attribute | m4 | m5 | high | t2 internal amod -> windows |

## 24

**caption_shape:** `multi-sentence`
**caption_id:** `0e22fd047812a642d9f5242be9ab5c1cacb81612bccb491c644cc77359b91814`

> Several men run along a dirt path surrounded by trees. One in a black shirt is in the foreground, while another in a red shirt runs slightly behind him to the right.

### Sentences
| sentence | token_span |
| --- | --- |
| Several men run along a dirt path surrounded by trees. | 0:11 |
| One in a black shirt is in the foreground, while another in a red shirt runs slightly behind him to the right. | 11:35 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Several men | men | man | nsubj | run | 0:2 |
| a dirt path | path | path | pobj | along | 4:7 |
| trees | trees | tree | pobj | by | 9:10 |
| a black shirt | shirt | shirt | pobj | in | 13:16 |
| the foreground | foreground | foreground | pobj | in | 18:20 |
| another | another | another | nsubj | runs | 22:23 |
| a red shirt | shirt | shirt | pobj | in | 24:27 |
| him | him | he | pobj | behind | 30:31 |
| the right | right | right | pobj | to | 32:34 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Several | several | ADJ | JJ | amod | men | 1 |
| 1 | men | man | NOUN | NNS | nsubj | run | 2 |
| 2 | run | run | VERB | VBP | ROOT | run | 2 |
| 3 | along | along | ADP | IN | prep | run | 2 |
| 4 | a | a | DET | DT | det | path | 6 |
| 5 | dirt | dirt | NOUN | NN | compound | path | 6 |
| 6 | path | path | NOUN | NN | pobj | along | 3 |
| 7 | surrounded | surround | VERB | VBN | acl | path | 6 |
| 8 | by | by | ADP | IN | agent | surrounded | 7 |
| 9 | trees | tree | NOUN | NNS | pobj | by | 8 |
| 10 | . | . | PUNCT | . | punct | run | 2 |
| 11 | One | one | NUM | CD | nsubj | is | 16 |
| 12 | in | in | ADP | IN | prep | One | 11 |
| 13 | a | a | DET | DT | det | shirt | 15 |
| 14 | black | black | ADJ | JJ | amod | shirt | 15 |
| 15 | shirt | shirt | NOUN | NN | pobj | in | 12 |
| 16 | is | be | AUX | VBZ | ROOT | is | 16 |
| 17 | in | in | ADP | IN | prep | is | 16 |
| 18 | the | the | DET | DT | det | foreground | 19 |
| 19 | foreground | foreground | NOUN | NN | pobj | in | 17 |
| 20 | , | , | PUNCT | , | punct | is | 16 |
| 21 | while | while | SCONJ | IN | mark | runs | 27 |
| 22 | another | another | PRON | DT | nsubj | runs | 27 |
| 23 | in | in | ADP | IN | prep | another | 22 |
| 24 | a | a | DET | DT | det | shirt | 26 |
| 25 | red | red | ADJ | JJ | amod | shirt | 26 |
| 26 | shirt | shirt | NOUN | NN | pobj | in | 23 |
| 27 | runs | run | VERB | VBZ | advcl | is | 16 |
| 28 | slightly | slightly | ADV | RB | advmod | behind | 29 |
| 29 | behind | behind | ADP | IN | prep | runs | 27 |
| 30 | him | he | PRON | PRP | pobj | behind | 29 |
| 31 | to | to | ADP | IN | prep | runs | 27 |
| 32 | the | the | DET | DT | det | right | 33 |
| 33 | right | right | NOUN | NN | pobj | to | 31 |
| 34 | . | . | PUNCT | . | punct | is | 16 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | men | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Several | several | chunk0 | 0 | approximate_quantity | medium |
| m2 | object | path | path | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | dirt | dirt | chunk1 | 5 | compound_modifier | medium |
| m4 | object | trees | tree | chunk2 | 9 | noun_chunk_root | high |
| m5 | object | shirt | shirt | chunk3 | 15 | noun_chunk_root | high |
| m6 | attribute | black | black | chunk3 | 14 | color_attribute | high |
| m7 | context | foreground | foreground | chunk4 | 19 | scene_context | high |
| m8 | object | shirt | shirt | chunk6 | 26 | noun_chunk_root | high |
| m9 | attribute | red | red | chunk6 | 25 | color_attribute | high |
| m10 | context | right | right | chunk8 | 33 | spatial_region | medium |
| m11 | reference | another | another | nominal_reference | 22 | contrastive_reference | high |
| m12 | action | run | run | doc | 2 | verb_predicate | high |
| m13 | action | surrounded | surround | doc | 7 | verb_predicate | high |
| m14 | action | runs | run | doc | 27 | verb_predicate | high |

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

## 25

**caption_shape:** `tag-list-like`
**caption_id:** `0e5e8ad31536aeeecbdd2699187c6ab85dbe278b1be0430def4d0f36428d3c14`

> brown couch, tiled floor, man, child, living room

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | brown couch | brown couch | 0:11 |
| t1 | tiled floor | tiled floor | 13:24 |
| t2 | man | man | 26:29 |
| t3 | child | child | 31:36 |
| t4 | living room | living room | 38:49 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | brown couch | couch | couch | ROOT | couch | 0:2 | 0:11 |
| t1 | tiled floor | floor | floor | ROOT | floor | 0:2 | 13:24 |
| t3 | child | child | child | ROOT | child | 0:1 | 31:36 |
| t4 | living room | living room | living_room | ROOT | living room | 0:1 | 38:49 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | brown | brown | ADJ | ADJ | JJ | JJ | amod | couch | 1 | 0:5 |
| t0 | 1 | couch | couch | NOUN | NOUN | NN | NN | ROOT | couch | 1 | 6:11 |
| t1 | 0 | tiled | tile | VERB | ADJ | VBN | VBN | amod | floor | 1 | 13:18 |
| t1 | 1 | floor | floor | NOUN | NOUN | NN | NN | ROOT | floor | 1 | 19:24 |
| t2 | 0 | man | man | INTJ | NOUN | UH | NN | ROOT | man | 0 | 26:29 |
| t3 | 0 | child | child | NOUN | NOUN | NN | NN | ROOT | child | 0 | 31:36 |
| t4 | 0 | living room | living_room | NOUN | NOUN | NN | NN | ROOT | living room | 0 | 38:49 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | couch | couch | t0 | 1 | segment_head | high |
| m1 | attribute | brown | brown | t0 | 0 | attribute | high |
| m2 | object | floor | floor | t1 | 1 | segment_head | high |
| m3 | attribute | tiled | tile | t1 | 0 | state_attribute | high |
| m4 | object | man | man | t2 | 0 | tag_list_person_object_override | high |
| m5 | object | child | child | t3 | 0 | segment_head | high |
| m6 | object | living room | living_room | t4 | 0 | segment_head | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> couch |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> floor |

## 26

**caption_shape:** `multi-sentence`
**caption_id:** `0f8f058deb2e280719cd84a3bbe67a8e80c6a0098904dfef002b76f2c49e4814`

> A snow-covered staircase with rusted metal railings leads upward. Snow piles on both sides, and bare trees stand beside the steps under a cloudy sky. A building with shutters is visible in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| A snow-covered staircase with rusted metal railings leads upward. | 0:10 |
| Snow piles on both sides, and bare trees stand beside the steps under a cloudy sky. | 10:28 |
| A building with shutters is visible in the background. | 28:38 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A snow-covered staircase | staircase | staircase | nsubj | leads | 0:3 |
| rusted metal railings | railings | railing | pobj | with | 4:7 |
| Snow piles | piles | pile | ROOT | piles | 10:12 |
| both sides | sides | side | pobj | on | 13:15 |
| bare trees | trees | tree | nsubj | stand | 17:19 |
| the steps | steps | step | pobj | beside | 21:23 |
| a cloudy sky | sky | sky | pobj | under | 24:27 |
| A building | building | building | nsubj | is | 28:30 |
| shutters | shutters | shutter | pobj | with | 31:32 |
| the background | background | background | pobj | in | 35:37 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | staircase | 2 |
| 1 | snow-covered | snow-covered | NOUN | NN | amod | staircase | 2 |
| 2 | staircase | staircase | NOUN | NN | nsubj | leads | 7 |
| 3 | with | with | ADP | IN | prep | staircase | 2 |
| 4 | rusted | rusted | ADJ | JJ | amod | railings | 6 |
| 5 | metal | metal | NOUN | NN | compound | railings | 6 |
| 6 | railings | railing | NOUN | NNS | pobj | with | 3 |
| 7 | leads | lead | VERB | VBZ | ROOT | leads | 7 |
| 8 | upward | upward | ADV | RB | advmod | leads | 7 |
| 9 | . | . | PUNCT | . | punct | leads | 7 |
| 10 | Snow | snow | NOUN | NN | compound | piles | 11 |
| 11 | piles | pile | NOUN | NNS | ROOT | piles | 11 |
| 12 | on | on | ADP | IN | prep | piles | 11 |
| 13 | both | both | DET | DT | det | sides | 14 |
| 14 | sides | side | NOUN | NNS | pobj | on | 12 |
| 15 | , | , | PUNCT | , | punct | piles | 11 |
| 16 | and | and | CCONJ | CC | cc | piles | 11 |
| 17 | bare | bare | ADJ | JJ | amod | trees | 18 |
| 18 | trees | tree | NOUN | NNS | nsubj | stand | 19 |
| 19 | stand | stand | VERB | VBP | conj | piles | 11 |
| 20 | beside | beside | ADP | IN | prep | stand | 19 |
| 21 | the | the | DET | DT | det | steps | 22 |
| 22 | steps | step | NOUN | NNS | pobj | beside | 20 |
| 23 | under | under | ADP | IN | prep | stand | 19 |
| 24 | a | a | DET | DT | det | sky | 26 |
| 25 | cloudy | cloudy | ADJ | JJ | amod | sky | 26 |
| 26 | sky | sky | NOUN | NN | pobj | under | 23 |
| 27 | . | . | PUNCT | . | punct | stand | 19 |
| 28 | A | a | DET | DT | det | building | 29 |
| 29 | building | building | NOUN | NN | nsubj | is | 32 |
| 30 | with | with | ADP | IN | prep | building | 29 |
| 31 | shutters | shutter | NOUN | NNS | pobj | with | 30 |
| 32 | is | be | AUX | VBZ | ROOT | is | 32 |
| 33 | visible | visible | ADJ | JJ | acomp | is | 32 |
| 34 | in | in | ADP | IN | prep | is | 32 |
| 35 | the | the | DET | DT | det | background | 36 |
| 36 | background | background | NOUN | NN | pobj | in | 34 |
| 37 | . | . | PUNCT | . | punct | is | 32 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | staircase | staircase | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | snow-covered | snow-covered | chunk0 | 1 | modifier_attribute | medium |
| m2 | object | railings | railing | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | rusted | rusted | chunk1 | 4 | modifier_attribute | medium |
| m4 | attribute | metal | metal | chunk1 | 5 | material_attribute | high |
| m5 | object | piles | pile | chunk2 | 11 | noun_chunk_root | high |
| m6 | attribute | Snow | snow | chunk2 | 10 | compound_modifier | medium |
| m7 | context | sides | side | chunk3 | 14 | spatial_region | medium |
| m8 | object | trees | tree | chunk4 | 18 | noun_chunk_root | high |
| m9 | attribute | bare | bare | chunk4 | 17 | visual_attribute | medium |
| m10 | object | steps | step | chunk5 | 22 | noun_chunk_root | high |
| m11 | object | sky | sky | chunk6 | 26 | noun_chunk_root | high |
| m12 | attribute | cloudy | cloudy | chunk6 | 25 | modifier_attribute | medium |
| m13 | object | building | building | chunk7 | 29 | noun_chunk_root | high |
| m14 | object | shutters | shutter | chunk8 | 31 | noun_chunk_root | high |
| m15 | context | background | background | chunk9 | 36 | scene_context | high |
| m16 | action | leads | lead | doc | 7 | verb_predicate | high |
| m17 | action | stand | stand | doc | 19 | verb_predicate | high |

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

## 27

**caption_shape:** `multi-sentence`
**caption_id:** `0fabd5c8b164bc555ab91c3009991f7f72fba0b91c0f61887d48ead2cf639814`

> A German Shepherd with a red collar walks forward on a paved surface. Several other dogs are nearby, including one lying down and others standing or moving around. A person in jeans stands in the background near a large black tunnel.

### Sentences
| sentence | token_span |
| --- | --- |
| A German Shepherd with a red collar walks forward on a paved surface. | 0:13 |
| Several other dogs are nearby, including one lying down and others standing or moving around. | 13:30 |
| A person in jeans stands in the background near a large black tunnel. | 30:44 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A German Shepherd | Shepherd | Shepherd | nsubj | walks | 0:3 |
| a red collar | collar | collar | pobj | with | 4:7 |
| a paved surface | paved surface | paved_surface | pobj | on | 10:12 |
| Several other dogs | dogs | dog | nsubj | are | 13:16 |
| others | others | other | conj | one | 24:25 |
| A person | person | person | nsubj | stands | 30:32 |
| jeans | jeans | jean | pobj | in | 33:34 |
| the background | background | background | pobj | in | 36:38 |
| a large black tunnel | tunnel | tunnel | pobj | near | 39:43 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | Shepherd | 2 |
| 1 | German | German | PROPN | NNP | compound | Shepherd | 2 |
| 2 | Shepherd | Shepherd | PROPN | NNP | nsubj | walks | 7 |
| 3 | with | with | ADP | IN | prep | Shepherd | 2 |
| 4 | a | a | DET | DT | det | collar | 6 |
| 5 | red | red | ADJ | JJ | amod | collar | 6 |
| 6 | collar | collar | NOUN | NN | pobj | with | 3 |
| 7 | walks | walk | VERB | VBZ | ROOT | walks | 7 |
| 8 | forward | forward | ADV | RB | advmod | walks | 7 |
| 9 | on | on | ADP | IN | prep | walks | 7 |
| 10 | a | a | DET | DT | det | paved surface | 11 |
| 11 | paved surface | paved_surface | NOUN | NN | pobj | on | 9 |
| 12 | . | . | PUNCT | . | punct | walks | 7 |
| 13 | Several | several | ADJ | JJ | amod | dogs | 15 |
| 14 | other | other | ADJ | JJ | amod | dogs | 15 |
| 15 | dogs | dog | NOUN | NNS | nsubj | are | 16 |
| 16 | are | be | AUX | VBP | ROOT | are | 16 |
| 17 | nearby | nearby | ADV | RB | advmod | are | 16 |
| 18 | , | , | PUNCT | , | punct | are | 16 |
| 19 | including | include | VERB | VBG | prep | dogs | 15 |
| 20 | one | one | NUM | CD | pobj | including | 19 |
| 21 | lying | lie | VERB | VBG | acl | one | 20 |
| 22 | down | down | ADP | RP | advmod | lying | 21 |
| 23 | and | and | CCONJ | CC | cc | one | 20 |
| 24 | others | other | NOUN | NNS | conj | one | 20 |
| 25 | standing | stand | VERB | VBG | acl | others | 24 |
| 26 | or | or | CCONJ | CC | cc | standing | 25 |
| 27 | moving | move | VERB | VBG | conj | standing | 25 |
| 28 | around | around | ADV | RB | advmod | moving | 27 |
| 29 | . | . | PUNCT | . | punct | are | 16 |
| 30 | A | a | DET | DT | det | person | 31 |
| 31 | person | person | NOUN | NN | nsubj | stands | 34 |
| 32 | in | in | ADP | IN | prep | person | 31 |
| 33 | jeans | jean | NOUN | NNS | pobj | in | 32 |
| 34 | stands | stand | VERB | VBZ | ROOT | stands | 34 |
| 35 | in | in | ADP | IN | prep | stands | 34 |
| 36 | the | the | DET | DT | det | background | 37 |
| 37 | background | background | NOUN | NN | pobj | in | 35 |
| 38 | near | near | ADP | IN | prep | stands | 34 |
| 39 | a | a | DET | DT | det | tunnel | 42 |
| 40 | large | large | ADJ | JJ | amod | tunnel | 42 |
| 41 | black | black | ADJ | JJ | amod | tunnel | 42 |
| 42 | tunnel | tunnel | NOUN | NN | pobj | near | 38 |
| 43 | . | . | PUNCT | . | punct | stands | 34 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | Shepherd | shepherd | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | German | german | chunk0 | 1 | compound_modifier | medium |
| m2 | object | collar | collar | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | red | red | chunk1 | 5 | color_attribute | high |
| m4 | object | paved surface | paved_surface | chunk2 | 11 | noun_chunk_root | high |
| m5 | object | dogs | dog | chunk3 | 15 | noun_chunk_root | high |
| m6 | quantity | Several | several | chunk3 | 13 | approximate_quantity | medium |
| m7 | attribute | other | other | chunk3 | 14 | modifier_attribute | medium |
| m8 | object | person | person | chunk5 | 31 | noun_chunk_root | high |
| m9 | object | jeans | jean | chunk6 | 33 | noun_chunk_root | high |
| m10 | context | background | background | chunk7 | 37 | scene_context | high |
| m11 | object | tunnel | tunnel | chunk8 | 42 | noun_chunk_root | high |
| m12 | attribute | large | large | chunk8 | 40 | size_attribute | high |
| m13 | attribute | black | black | chunk8 | 41 | color_attribute | high |
| m14 | reference | one | one | nominal_reference | 20 | singular_substitute | high |
| m15 | reference | others | other | nominal_reference | 24 | contrastive_reference | high |
| m16 | action | walks | walk | doc | 7 | verb_predicate | high |
| m17 | action | including | include | doc | 19 | verb_predicate | high |
| m18 | action | lying | lie | doc | 21 | verb_predicate | high |
| m19 | action | standing | stand | doc | 25 | verb_predicate | high |
| m20 | action | moving | move | doc | 27 | verb_predicate | high |
| m21 | action | stands | stand | doc | 34 | verb_predicate | high |

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

## 28

**caption_shape:** `sentence-like`
**caption_id:** `0fadd618f87235c9ee60220033aa5ac51148647eec5e8beb535c4eb6a4a4f814`

> Three water polo players swim in a pool, with one wearing a black cap marked '12'.

### Sentences
| sentence | token_span |
| --- | --- |
| Three water polo players swim in a pool, with one wearing a black cap marked '12'. | 0:20 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Three water polo players | players | player | nsubj | swim | 0:4 |
| a pool | pool | pool | pobj | in | 6:8 |
| a black cap | cap | cap | dobj | wearing | 12:15 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Three | three | NUM | CD | nummod | players | 3 |
| 1 | water | water | NOUN | NN | compound | polo | 2 |
| 2 | polo | polo | NOUN | NN | compound | players | 3 |
| 3 | players | player | NOUN | NNS | nsubj | swim | 4 |
| 4 | swim | swim | VERB | VBP | ROOT | swim | 4 |
| 5 | in | in | ADP | IN | prep | swim | 4 |
| 6 | a | a | DET | DT | det | pool | 7 |
| 7 | pool | pool | NOUN | NN | pobj | in | 5 |
| 8 | , | , | PUNCT | , | punct | swim | 4 |
| 9 | with | with | ADP | IN | prep | swim | 4 |
| 10 | one | one | NUM | CD | pobj | with | 9 |
| 11 | wearing | wear | VERB | VBG | acl | one | 10 |
| 12 | a | a | DET | DT | det | cap | 14 |
| 13 | black | black | ADJ | JJ | amod | cap | 14 |
| 14 | cap | cap | NOUN | NN | dobj | wearing | 11 |
| 15 | marked | mark | VERB | VBN | acl | cap | 14 |
| 16 | ' | ' | PUNCT | `` | punct | marked | 15 |
| 17 | 12 | 12 | NUM | CD | oprd | marked | 15 |
| 18 | ' | ' | PUNCT | '' | punct | 12 | 17 |
| 19 | . | . | PUNCT | . | punct | swim | 4 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | players | player | chunk0 | 3 | noun_chunk_root | high |
| m1 | quantity | Three | three | chunk0 | 0 | exact_quantity | high |
| m2 | attribute | water | water | chunk0 | 1 | compound_modifier | medium |
| m3 | attribute | polo | polo | chunk0 | 2 | compound_modifier | medium |
| m4 | object | pool | pool | chunk1 | 7 | noun_chunk_root | high |
| m5 | object | cap | cap | chunk2 | 14 | noun_chunk_root | high |
| m6 | attribute | black | black | chunk2 | 13 | color_attribute | high |
| m7 | reference | one | one | nominal_reference | 10 | singular_substitute | high |
| m8 | action | swim | swim | doc | 4 | verb_predicate | high |
| m9 | action | wearing | wear | doc | 11 | verb_predicate | high |
| m10 | action | marked | mark | doc | 15 | verb_predicate | high |

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

## 29

**caption_shape:** `sentence-like`
**caption_id:** `10de106710cb2aaf0f5016f7ee9ac5f8e67a647da0dc248e18da28947b17a014`

> A diagram shows different views of a futuristic aircraft with labeled parts and directional arrows.

### Sentences
| sentence | token_span |
| --- | --- |
| A diagram shows different views of a futuristic aircraft with labeled parts and directional arrows. | 0:16 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A diagram | diagram | diagram | nsubj | shows | 0:2 |
| different views | views | view | dobj | shows | 3:5 |
| a futuristic aircraft | aircraft | aircraft | pobj | of | 6:9 |
| labeled parts | parts | part | pobj | with | 10:12 |
| directional arrows | arrows | arrow | conj | parts | 13:15 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | diagram | 1 |
| 1 | diagram | diagram | NOUN | NN | nsubj | shows | 2 |
| 2 | shows | show | VERB | VBZ | ROOT | shows | 2 |
| 3 | different | different | ADJ | JJ | amod | views | 4 |
| 4 | views | view | NOUN | NNS | dobj | shows | 2 |
| 5 | of | of | ADP | IN | prep | views | 4 |
| 6 | a | a | DET | DT | det | aircraft | 8 |
| 7 | futuristic | futuristic | ADJ | JJ | amod | aircraft | 8 |
| 8 | aircraft | aircraft | NOUN | NN | pobj | of | 5 |
| 9 | with | with | ADP | IN | prep | views | 4 |
| 10 | labeled | label | VERB | VBN | amod | parts | 11 |
| 11 | parts | part | NOUN | NNS | pobj | with | 9 |
| 12 | and | and | CCONJ | CC | cc | parts | 11 |
| 13 | directional | directional | ADJ | JJ | amod | arrows | 14 |
| 14 | arrows | arrow | NOUN | NNS | conj | parts | 11 |
| 15 | . | . | PUNCT | . | punct | shows | 2 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | diagram | diagram | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | views | view | chunk1 | 4 | noun_chunk_root | high |
| m2 | attribute | different | different | chunk1 | 3 | modifier_attribute | medium |
| m3 | object | aircraft | aircraft | chunk2 | 8 | noun_chunk_root | high |
| m4 | attribute | futuristic | futuristic | chunk2 | 7 | modifier_attribute | medium |
| m5 | object | parts | part | chunk3 | 11 | noun_chunk_root | high |
| m6 | attribute | labeled | label | chunk3 | 10 | state_attribute | medium |
| m7 | object | arrows | arrow | chunk4 | 14 | noun_chunk_root | high |
| m8 | attribute | directional | directional | chunk4 | 13 | modifier_attribute | medium |
| m9 | action | shows | show | doc | 2 | verb_predicate | high |

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

## 30

**caption_shape:** `multi-sentence`
**caption_id:** `11d48be4d3ad5ca7a05c8076bc307685d865102be7417777129b9bff63465414`

> An ornate stone archway with carvings is set into a beige building wall. To its left, a red-framed window and a black chalkboard sign stand beside a small metal trash can. A green plaque is mounted on the right side of the arch.

### Sentences
| sentence | token_span |
| --- | --- |
| An ornate stone archway with carvings is set into a beige building wall. | 0:14 |
| To its left, a red-framed window and a black chalkboard sign stand beside a small metal trash can. | 14:33 |
| A green plaque is mounted on the right side of the arch. | 33:46 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| An ornate stone archway | archway | archway | nsubjpass | set | 0:4 |
| carvings | carvings | carving | pobj | with | 5:6 |
| a beige building wall | wall | wall | pobj | into | 9:13 |
| its left | left | left | pobj | To | 15:17 |
| a red-framed window | window | window | nsubj | stand | 18:21 |
| a black chalkboard sign | sign | sign | conj | window | 22:26 |
| a small metal trash can | trash can | trash_can | pobj | beside | 28:32 |
| A green plaque | plaque | plaque | nsubjpass | mounted | 33:36 |
| the right side | side | side | pobj | on | 39:42 |
| the arch | arch | arch | pobj | of | 43:45 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | An | an | DET | DT | det | archway | 3 |
| 1 | ornate | ornate | ADJ | JJ | amod | archway | 3 |
| 2 | stone | stone | NOUN | NN | compound | archway | 3 |
| 3 | archway | archway | NOUN | NN | nsubjpass | set | 7 |
| 4 | with | with | ADP | IN | prep | archway | 3 |
| 5 | carvings | carving | NOUN | NNS | pobj | with | 4 |
| 6 | is | be | AUX | VBZ | auxpass | set | 7 |
| 7 | set | set | VERB | VBN | ROOT | set | 7 |
| 8 | into | into | ADP | IN | prep | set | 7 |
| 9 | a | a | DET | DT | det | wall | 12 |
| 10 | beige | beige | ADJ | JJ | amod | wall | 12 |
| 11 | building | building | NOUN | NN | compound | wall | 12 |
| 12 | wall | wall | NOUN | NN | pobj | into | 8 |
| 13 | . | . | PUNCT | . | punct | set | 7 |
| 14 | To | to | ADP | IN | prep | stand | 26 |
| 15 | its | its | PRON | PRP$ | poss | left | 16 |
| 16 | left | left | NOUN | NN | pobj | To | 14 |
| 17 | , | , | PUNCT | , | punct | stand | 26 |
| 18 | a | a | DET | DT | det | window | 20 |
| 19 | red-framed | red-framed | ADJ | JJ | amod | window | 20 |
| 20 | window | window | NOUN | NN | nsubj | stand | 26 |
| 21 | and | and | CCONJ | CC | cc | window | 20 |
| 22 | a | a | DET | DT | det | sign | 25 |
| 23 | black | black | ADJ | JJ | amod | sign | 25 |
| 24 | chalkboard | chalkboard | NOUN | NN | compound | sign | 25 |
| 25 | sign | sign | NOUN | NN | conj | window | 20 |
| 26 | stand | stand | VERB | VBP | ROOT | stand | 26 |
| 27 | beside | beside | ADP | IN | prep | stand | 26 |
| 28 | a | a | DET | DT | det | trash can | 31 |
| 29 | small | small | ADJ | JJ | amod | trash can | 31 |
| 30 | metal | metal | NOUN | NN | compound | trash can | 31 |
| 31 | trash can | trash_can | NOUN | NN | pobj | beside | 27 |
| 32 | . | . | PUNCT | . | punct | stand | 26 |
| 33 | A | a | DET | DT | det | plaque | 35 |
| 34 | green | green | ADJ | JJ | amod | plaque | 35 |
| 35 | plaque | plaque | NOUN | NN | nsubjpass | mounted | 37 |
| 36 | is | be | AUX | VBZ | auxpass | mounted | 37 |
| 37 | mounted | mount | VERB | VBN | ROOT | mounted | 37 |
| 38 | on | on | ADP | IN | prep | mounted | 37 |
| 39 | the | the | DET | DT | det | side | 41 |
| 40 | right | right | ADJ | JJ | amod | side | 41 |
| 41 | side | side | NOUN | NN | pobj | on | 38 |
| 42 | of | of | ADP | IN | prep | side | 41 |
| 43 | the | the | DET | DT | det | arch | 44 |
| 44 | arch | arch | NOUN | NN | pobj | of | 42 |
| 45 | . | . | PUNCT | . | punct | mounted | 37 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | archway | archway | chunk0 | 3 | noun_chunk_root | high |
| m1 | attribute | ornate | ornate | chunk0 | 1 | modifier_attribute | medium |
| m2 | attribute | stone | stone | chunk0 | 2 | material_attribute | high |
| m3 | object | carvings | carving | chunk1 | 5 | noun_chunk_root | high |
| m4 | object | wall | wall | chunk2 | 12 | noun_chunk_root | high |
| m5 | attribute | beige | beige | chunk2 | 10 | color_attribute | high |
| m6 | attribute | building | building | chunk2 | 11 | compound_modifier | medium |
| m7 | context | left | left | chunk3 | 16 | spatial_region | medium |
| m8 | object | window | window | chunk4 | 20 | noun_chunk_root | high |
| m9 | attribute | red-framed | red-framed | chunk4 | 19 | modifier_attribute | medium |
| m10 | object | sign | sign | chunk5 | 25 | noun_chunk_root | high |
| m11 | attribute | black | black | chunk5 | 23 | color_attribute | high |
| m12 | attribute | chalkboard | chalkboard | chunk5 | 24 | compound_modifier | medium |
| m13 | object | trash can | trash_can | chunk6 | 31 | noun_chunk_root | high |
| m14 | attribute | small | small | chunk6 | 29 | size_attribute | high |
| m15 | attribute | metal | metal | chunk6 | 30 | material_attribute | high |
| m16 | object | plaque | plaque | chunk7 | 35 | noun_chunk_root | high |
| m17 | attribute | green | green | chunk7 | 34 | color_attribute | high |
| m18 | context | side | side | chunk8 | 41 | spatial_region | medium |
| m19 | object | arch | arch | chunk9 | 44 | noun_chunk_root | high |
| m20 | action | set | set | doc | 7 | verb_predicate | high |
| m21 | action | stand | stand | doc | 26 | verb_predicate | high |
| m22 | action | mounted | mount | doc | 37 | verb_predicate | high |

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

## 31

**caption_shape:** `sentence-like`
**caption_id:** `12961bafd17111c4818794da65cc4639924bca427bfced0b4ea1fb386e7d1c14`

> A vibrant pink flower with long petals stands tall against a blurred green background.

### Sentences
| sentence | token_span |
| --- | --- |
| A vibrant pink flower with long petals stands tall against a blurred green background. | 0:15 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A vibrant pink flower | flower | flower | nsubj | stands | 0:4 |
| long petals | petals | petal | pobj | with | 5:7 |
| a blurred green background | background | background | pobj | against | 10:14 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | flower | 3 |
| 1 | vibrant | vibrant | ADJ | JJ | amod | flower | 3 |
| 2 | pink | pink | ADJ | JJ | amod | flower | 3 |
| 3 | flower | flower | NOUN | NN | nsubj | stands | 7 |
| 4 | with | with | ADP | IN | prep | flower | 3 |
| 5 | long | long | ADJ | JJ | amod | petals | 6 |
| 6 | petals | petal | NOUN | NNS | pobj | with | 4 |
| 7 | stands | stand | VERB | VBZ | ROOT | stands | 7 |
| 8 | tall | tall | ADJ | JJ | advmod | stands | 7 |
| 9 | against | against | ADP | IN | prep | stands | 7 |
| 10 | a | a | DET | DT | det | background | 13 |
| 11 | blurred | blurred | ADJ | JJ | amod | background | 13 |
| 12 | green | green | ADJ | JJ | amod | background | 13 |
| 13 | background | background | NOUN | NN | pobj | against | 9 |
| 14 | . | . | PUNCT | . | punct | stands | 7 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | flower | flower | chunk0 | 3 | noun_chunk_root | high |
| m1 | attribute | vibrant | vibrant | chunk0 | 1 | modifier_attribute | medium |
| m2 | attribute | pink | pink | chunk0 | 2 | color_attribute | high |
| m3 | object | petals | petal | chunk1 | 6 | noun_chunk_root | high |
| m4 | attribute | long | long | chunk1 | 5 | size_attribute | high |
| m5 | context | background | background | chunk2 | 13 | scene_context | high |
| m6 | attribute | blurred | blurred | chunk2 | 11 | modifier_attribute | medium |
| m7 | attribute | green | green | chunk2 | 12 | color_attribute | high |
| m8 | action | stands | stand | doc | 7 | verb_predicate | high |

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

## 32

**caption_shape:** `tag-list-like`
**caption_id:** `12d151d075972300fd5e1b992ae54d639244f6449ccc9366e108de100c416814`

> women, protest, banner, trees, rainbow dress

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | women | women | 0:5 |
| t1 | protest | protest | 7:14 |
| t2 | banner | banner | 16:22 |
| t3 | trees | trees | 24:29 |
| t4 | rainbow dress | rainbow dress | 31:44 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | women | women | woman | ROOT | women | 0:1 | 0:5 |
| t1 | protest | protest | protest | ROOT | protest | 0:1 | 7:14 |
| t2 | banner | banner | banner | ROOT | banner | 0:1 | 16:22 |
| t3 | trees | trees | tree | ROOT | trees | 0:1 | 24:29 |
| t4 | rainbow dress | dress | dress | ROOT | dress | 0:2 | 31:44 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | women | woman | NOUN | NOUN | NNS | NNS | ROOT | women | 0 | 0:5 |
| t1 | 0 | protest | protest | NOUN | NOUN | NN | NN | ROOT | protest | 0 | 7:14 |
| t2 | 0 | banner | banner | PROPN | NOUN | NNP | NN | ROOT | banner | 0 | 16:22 |
| t3 | 0 | trees | tree | NOUN | NOUN | NNS | NNS | ROOT | trees | 0 | 24:29 |
| t4 | 0 | rainbow | rainbow | NOUN | NOUN | NN | NN | compound | dress | 1 | 31:38 |
| t4 | 1 | dress | dress | NOUN | NOUN | NN | NN | ROOT | dress | 1 | 39:44 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | women | woman | t0 | 0 | segment_head | high |
| m1 | object | protest | protest | t1 | 0 | segment_head | high |
| m2 | object | banner | banner | t2 | 0 | segment_head | high |
| m3 | object | trees | tree | t3 | 0 | segment_head | high |
| m4 | object | dress | dress | t4 | 1 | segment_head | high |
| m5 | attribute | rainbow | rainbow | t4 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m4 | m5 | high | t4 internal compound -> dress |

## 33

**caption_shape:** `tag-list-like`
**caption_id:** `138cd27f18aae997ac6ac36cae743a4f9bd1ef3fff2d732038d504da5b456014`

> woman, soap, bathtub, mirror, white tiles

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | woman | woman | 0:5 |
| t1 | soap | soap | 7:11 |
| t2 | bathtub | bathtub | 13:20 |
| t3 | mirror | mirror | 22:28 |
| t4 | white tiles | white tiles | 30:41 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | woman | woman | woman | ROOT | woman | 0:1 | 0:5 |
| t1 | soap | soap | soap | ROOT | soap | 0:1 | 7:11 |
| t2 | bathtub | bathtub | bathtub | ROOT | bathtub | 0:1 | 13:20 |
| t3 | mirror | mirror | mirror | ROOT | mirror | 0:1 | 22:28 |
| t4 | white tiles | tiles | tile | ROOT | tiles | 0:2 | 30:41 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | woman | woman | NOUN | NOUN | NN | NN | ROOT | woman | 0 | 0:5 |
| t1 | 0 | soap | soap | NOUN | NOUN | NN | NN | ROOT | soap | 0 | 7:11 |
| t2 | 0 | bathtub | bathtub | NOUN | NOUN | NN | NN | ROOT | bathtub | 0 | 13:20 |
| t3 | 0 | mirror | mirror | NOUN | NOUN | NN | NN | ROOT | mirror | 0 | 22:28 |
| t4 | 0 | white | white | ADJ | ADJ | JJ | JJ | amod | tiles | 1 | 30:35 |
| t4 | 1 | tiles | tile | NOUN | NOUN | NNS | NNS | ROOT | tiles | 1 | 36:41 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | t0 | 0 | segment_head | high |
| m1 | object | soap | soap | t1 | 0 | segment_head | high |
| m2 | object | bathtub | bathtub | t2 | 0 | segment_head | high |
| m3 | object | mirror | mirror | t3 | 0 | segment_head | high |
| m4 | object | tiles | tile | t4 | 1 | segment_head | high |
| m5 | attribute | white | white | t4 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m4 | m5 | high | t4 internal amod -> tiles |

## 34

**caption_shape:** `multi-sentence`
**caption_id:** `13f49f32bbfec63699d6ffbf711593bce779463a6349b0f1ff1b201fa50da014`

> A blurry view of a forest with tall trees and dense underbrush. Green and brown leaves cover the ground, with tree trunks rising upward into a bright, out-of-focus sky. The motion blur suggests movement through the woods.

### Sentences
| sentence | token_span |
| --- | --- |
| A blurry view of a forest with tall trees and dense underbrush. | 0:13 |
| Green and brown leaves cover the ground, with tree trunks rising upward into a bright, out-of-focus sky. | 13:32 |
| The motion blur suggests movement through the woods. | 32:41 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A blurry view | view | view | ROOT | view | 0:3 |
| a forest | forest | forest | pobj | of | 4:6 |
| tall trees | trees | tree | pobj | with | 7:9 |
| dense underbrush | underbrush | underbrush | conj | trees | 10:12 |
| Green and brown leaves | leaves | leaf | nsubj | cover | 13:17 |
| the ground | ground | ground | dobj | cover | 18:20 |
| tree trunks | tree trunks | tree_trunk | nsubj | rising | 22:23 |
| a bright, out-of-focus | out-of-focus | out-of-focus | pobj | into | 26:30 |
| sky | sky | sky | pobj | into | 30:31 |
| The motion blur | blur | blur | nsubj | suggests | 32:35 |
| movement | movement | movement | dobj | suggests | 36:37 |
| the woods | woods | wood | pobj | through | 38:40 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | view | 2 |
| 1 | blurry | blurry | ADJ | JJ | amod | view | 2 |
| 2 | view | view | NOUN | NN | ROOT | view | 2 |
| 3 | of | of | ADP | IN | prep | view | 2 |
| 4 | a | a | DET | DT | det | forest | 5 |
| 5 | forest | forest | NOUN | NN | pobj | of | 3 |
| 6 | with | with | ADP | IN | prep | forest | 5 |
| 7 | tall | tall | ADJ | JJ | amod | trees | 8 |
| 8 | trees | tree | NOUN | NNS | pobj | with | 6 |
| 9 | and | and | CCONJ | CC | cc | trees | 8 |
| 10 | dense | dense | ADJ | JJ | amod | underbrush | 11 |
| 11 | underbrush | underbrush | NOUN | NN | conj | trees | 8 |
| 12 | . | . | PUNCT | . | punct | view | 2 |
| 13 | Green | green | ADJ | JJ | amod | leaves | 16 |
| 14 | and | and | CCONJ | CC | cc | Green | 13 |
| 15 | brown | brown | ADJ | JJ | conj | Green | 13 |
| 16 | leaves | leaf | NOUN | NNS | nsubj | cover | 17 |
| 17 | cover | cover | VERB | VBP | ROOT | cover | 17 |
| 18 | the | the | DET | DT | det | ground | 19 |
| 19 | ground | ground | NOUN | NN | dobj | cover | 17 |
| 20 | , | , | PUNCT | , | punct | cover | 17 |
| 21 | with | with | ADP | IN | prep | cover | 17 |
| 22 | tree trunks | tree_trunk | NOUN | NN | nsubj | rising | 23 |
| 23 | rising | rise | VERB | VBG | pcomp | with | 21 |
| 24 | upward | upward | ADV | RB | advmod | rising | 23 |
| 25 | into | into | ADP | IN | prep | rising | 23 |
| 26 | a | a | DET | DT | det | out-of-focus | 29 |
| 27 | bright | bright | ADJ | JJ | amod | out-of-focus | 29 |
| 28 | , | , | PUNCT | , | punct | out-of-focus | 29 |
| 29 | out-of-focus | out-of-focus | NOUN | NN | pobj | into | 25 |
| 30 | sky | sky | NOUN | NN | pobj | into | 25 |
| 31 | . | . | PUNCT | . | punct | cover | 17 |
| 32 | The | the | DET | DT | det | blur | 34 |
| 33 | motion | motion | NOUN | NN | compound | blur | 34 |
| 34 | blur | blur | NOUN | NN | nsubj | suggests | 35 |
| 35 | suggests | suggest | VERB | VBZ | ROOT | suggests | 35 |
| 36 | movement | movement | NOUN | NN | dobj | suggests | 35 |
| 37 | through | through | ADP | IN | prep | movement | 36 |
| 38 | the | the | DET | DT | det | woods | 39 |
| 39 | woods | wood | NOUN | NNS | pobj | through | 37 |
| 40 | . | . | PUNCT | . | punct | suggests | 35 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | view | view | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | blurry | blurry | chunk0 | 1 | visual_attribute | medium |
| m2 | object | forest | forest | chunk1 | 5 | noun_chunk_root | high |
| m3 | object | trees | tree | chunk2 | 8 | noun_chunk_root | high |
| m4 | attribute | tall | tall | chunk2 | 7 | size_attribute | high |
| m5 | object | underbrush | underbrush | chunk3 | 11 | noun_chunk_root | high |
| m6 | attribute | dense | dense | chunk3 | 10 | modifier_attribute | medium |
| m7 | object | leaves | leaf | chunk4 | 16 | noun_chunk_root | high |
| m8 | attribute | Green | green | chunk4 | 13 | color_attribute | high |
| m9 | attribute | brown | brown | chunk4 | 15 | color_attribute | high |
| m10 | object | ground | ground | chunk5 | 19 | noun_chunk_root | high |
| m11 | object | tree trunks | tree_trunk | chunk6 | 22 | noun_chunk_root | high |
| m12 | object | out-of-focus | out-of-focus | chunk7 | 29 | noun_chunk_root | high |
| m13 | attribute | bright | bright | chunk7 | 27 | visual_attribute | medium |
| m14 | object | sky | sky | chunk8 | 30 | noun_chunk_root | high |
| m15 | object | blur | blur | chunk9 | 34 | noun_chunk_root | high |
| m16 | attribute | motion | motion | chunk9 | 33 | compound_modifier | medium |
| m17 | object | movement | movement | chunk10 | 36 | noun_chunk_root | high |
| m18 | object | woods | wood | chunk11 | 39 | noun_chunk_root | high |
| m19 | action | cover | cover | doc | 17 | verb_predicate | high |
| m20 | action | rising | rise | doc | 23 | verb_predicate | high |
| m21 | action | suggests | suggest | doc | 35 | verb_predicate | high |

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

## 35

**caption_shape:** `sentence-like`
**caption_id:** `141781ae9aed9737cb5b87309987b0a531ef8ec36b80f5df514fc9cc613a3014`

> A small dark mouse eats seeds from a green plastic lid on a wooden surface.

### Sentences
| sentence | token_span |
| --- | --- |
| A small dark mouse eats seeds from a green plastic lid on a wooden surface. | 0:16 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A small dark mouse | mouse | mouse | nsubj | eats | 0:4 |
| seeds | seeds | seed | dobj | eats | 5:6 |
| a green plastic lid | lid | lid | pobj | from | 7:11 |
| a wooden surface | surface | surface | pobj | on | 12:15 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | mouse | 3 |
| 1 | small | small | ADJ | JJ | amod | mouse | 3 |
| 2 | dark | dark | ADJ | JJ | amod | mouse | 3 |
| 3 | mouse | mouse | NOUN | NN | nsubj | eats | 4 |
| 4 | eats | eat | VERB | VBZ | ROOT | eats | 4 |
| 5 | seeds | seed | NOUN | NNS | dobj | eats | 4 |
| 6 | from | from | ADP | IN | prep | eats | 4 |
| 7 | a | a | DET | DT | det | lid | 10 |
| 8 | green | green | ADJ | JJ | amod | lid | 10 |
| 9 | plastic | plastic | NOUN | NN | compound | lid | 10 |
| 10 | lid | lid | NOUN | NN | pobj | from | 6 |
| 11 | on | on | ADP | IN | prep | lid | 10 |
| 12 | a | a | DET | DT | det | surface | 14 |
| 13 | wooden | wooden | ADJ | JJ | amod | surface | 14 |
| 14 | surface | surface | NOUN | NN | pobj | on | 11 |
| 15 | . | . | PUNCT | . | punct | eats | 4 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | mouse | mouse | chunk0 | 3 | noun_chunk_root | high |
| m1 | attribute | small | small | chunk0 | 1 | size_attribute | high |
| m2 | attribute | dark | dark | chunk0 | 2 | visual_attribute | medium |
| m3 | object | seeds | seed | chunk1 | 5 | noun_chunk_root | high |
| m4 | object | lid | lid | chunk2 | 10 | noun_chunk_root | high |
| m5 | attribute | green | green | chunk2 | 8 | color_attribute | high |
| m6 | attribute | plastic | plastic | chunk2 | 9 | material_attribute | high |
| m7 | context | surface | surface | chunk3 | 14 | spatial_region | medium |
| m8 | action | eats | eat | doc | 4 | verb_predicate | high |

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

## 36

**caption_shape:** `sentence-like`
**caption_id:** `14b68438947aaa187dd5a08cd9df57dd702dd3450c54c8042dfd4d32e7ea2014`

> A woman speaks at a podium with "UNIP" branding, standing before an audience in a lecture hall.

**parsed_caption:**

> A woman speaks at a podium with "UNIP" branding, standing before an audience in a lecture hall.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 14b68438947aaa187dd5a08cd9df57dd702dd3450c54c8042dfd4d32e7ea2014:q0 | UNIP | unip | raw_quote_span |  | 32:38 | 32:38 |

### Sentences
| sentence | token_span |
| --- | --- |
| A woman speaks at a podium with "UNIP" branding, standing before an audience in a lecture hall. | 0:19 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A woman | woman | woman | nsubj | speaks | 0:2 |
| a podium | podium | podium | pobj | at | 4:6 |
| "UNIP" branding | branding | branding | pobj | with | 7:9 |
| an audience | audience | audience | pobj | before | 12:14 |
| a lecture hall | hall | hall | pobj | in | 15:18 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | woman | 1 |
| 1 | woman | woman | NOUN | NN | nsubj | speaks | 2 |
| 2 | speaks | speak | VERB | VBZ | ROOT | speaks | 2 |
| 3 | at | at | ADP | IN | prep | speaks | 2 |
| 4 | a | a | DET | DT | det | podium | 5 |
| 5 | podium | podium | NOUN | NN | pobj | at | 3 |
| 6 | with | with | ADP | IN | prep | podium | 5 |
| 7 | "UNIP" | unip | PROPN | NNP | punct | branding | 8 |
| 8 | branding | branding | NOUN | NN | pobj | with | 6 |
| 9 | , | , | PUNCT | , | punct | speaks | 2 |
| 10 | standing | stand | VERB | VBG | advcl | speaks | 2 |
| 11 | before | before | ADP | IN | prep | standing | 10 |
| 12 | an | an | DET | DT | det | audience | 13 |
| 13 | audience | audience | NOUN | NN | pobj | before | 11 |
| 14 | in | in | ADP | IN | prep | standing | 10 |
| 15 | a | a | DET | DT | det | hall | 17 |
| 16 | lecture | lecture | NOUN | NN | compound | hall | 17 |
| 17 | hall | hall | NOUN | NN | pobj | in | 14 |
| 18 | . | . | PUNCT | . | punct | speaks | 2 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "UNIP" | unip | doc_quote | 7 | quote_text | high |
| m1 | object | woman | woman | chunk0 | 1 | noun_chunk_root | high |
| m2 | object | podium | podium | chunk1 | 5 | noun_chunk_root | high |
| m3 | object | branding | branding | chunk2 | 8 | noun_chunk_root | high |
| m4 | object | audience | audience | chunk3 | 13 | noun_chunk_root | high |
| m5 | object | hall | hall | chunk4 | 17 | noun_chunk_root | high |
| m6 | attribute | lecture | lecture | chunk4 | 16 | compound_modifier | medium |
| m7 | action | speaks | speak | doc | 2 | verb_predicate | high |
| m8 | action | standing | stand | doc | 10 | verb_predicate | high |

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

## 37

**caption_shape:** `multi-sentence`
**caption_id:** `14bcd3b32d58bbb5a4a6e7a74c9e2a2122879e32a6df7a32e57f096c2e9d0414`

> A woman in a white, orange, and blue cycling jersey smiles. She wears a red and blue collar with "Rabobank" printed on it.

**parsed_caption:**

> A woman in a white, orange, and blue cycling jersey smiles. She wears a red and blue collar with "Rabobank" printed on it.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 14bcd3b32d58bbb5a4a6e7a74c9e2a2122879e32a6df7a32e57f096c2e9d0414:q0 | Rabobank | rabobank | raw_quote_span |  | 97:107 | 97:107 |

### Sentences
| sentence | token_span |
| --- | --- |
| A woman in a white, orange, and blue cycling jersey smiles. | 0:14 |
| She wears a red and blue collar with "Rabobank" printed on it. | 14:27 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A woman | woman | woman | nsubj | smiles | 0:2 |
| a white, orange, and blue cycling jersey | jersey | jersey | pobj | in | 3:12 |
| She | She | she | nsubj | wears | 14:15 |
| a red and blue collar | collar | collar | dobj | wears | 16:21 |
| "Rabobank" | "Rabobank" | rabobank | nsubj | printed | 22:23 |
| it | it | it | pobj | on | 25:26 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | woman | 1 |
| 1 | woman | woman | NOUN | NN | nsubj | smiles | 12 |
| 2 | in | in | ADP | IN | prep | woman | 1 |
| 3 | a | a | DET | DT | det | jersey | 11 |
| 4 | white | white | ADJ | JJ | amod | jersey | 11 |
| 5 | , | , | PUNCT | , | punct | white | 4 |
| 6 | orange | orange | ADJ | JJ | conj | white | 4 |
| 7 | , | , | PUNCT | , | punct | orange | 6 |
| 8 | and | and | CCONJ | CC | cc | orange | 6 |
| 9 | blue | blue | ADJ | JJ | conj | orange | 6 |
| 10 | cycling | cycling | NOUN | NN | compound | jersey | 11 |
| 11 | jersey | jersey | NOUN | NN | pobj | in | 2 |
| 12 | smiles | smile | VERB | VBZ | ROOT | smiles | 12 |
| 13 | . | . | PUNCT | . | punct | smiles | 12 |
| 14 | She | she | PRON | PRP | nsubj | wears | 15 |
| 15 | wears | wear | VERB | VBZ | ROOT | wears | 15 |
| 16 | a | a | DET | DT | det | collar | 20 |
| 17 | red | red | ADJ | JJ | amod | collar | 20 |
| 18 | and | and | CCONJ | CC | cc | red | 17 |
| 19 | blue | blue | ADJ | JJ | conj | red | 17 |
| 20 | collar | collar | NOUN | NN | dobj | wears | 15 |
| 21 | with | with | ADP | IN | prep | collar | 20 |
| 22 | "Rabobank" | rabobank | PROPN | NNP | nsubj | printed | 23 |
| 23 | printed | print | VERB | VBN | pcomp | with | 21 |
| 24 | on | on | ADP | IN | prep | printed | 23 |
| 25 | it | it | PRON | PRP | pobj | on | 24 |
| 26 | . | . | PUNCT | . | punct | wears | 15 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "Rabobank" | rabobank | doc_quote | 22 | quote_text | high |
| m1 | object | woman | woman | chunk0 | 1 | noun_chunk_root | high |
| m2 | object | jersey | jersey | chunk1 | 11 | noun_chunk_root | high |
| m3 | attribute | white | white | chunk1 | 4 | color_attribute | high |
| m4 | attribute | orange | orange | chunk1 | 6 | color_attribute | high |
| m5 | attribute | blue | blue | chunk1 | 9 | color_attribute | high |
| m6 | attribute | cycling | cycling | chunk1 | 10 | compound_modifier | medium |
| m7 | object | collar | collar | chunk3 | 20 | noun_chunk_root | high |
| m8 | attribute | red | red | chunk3 | 17 | color_attribute | high |
| m9 | attribute | blue | blue | chunk3 | 19 | color_attribute | high |
| m10 | action | smiles | smile | doc | 12 | verb_predicate | high |
| m11 | action | wears | wear | doc | 15 | verb_predicate | high |
| m12 | action | printed | print | doc | 23 | verb_predicate | high |

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

## 38

**caption_shape:** `multi-sentence`
**caption_id:** `14cda51b33a33137a7819417ba7cbfe200dc2b9f347129c3797fbdfb8be6b814`

> An older man in a white shirt smiles with his eyes closed, hand near his chin. Another man stands behind him near a red flag.

### Sentences
| sentence | token_span |
| --- | --- |
| An older man in a white shirt smiles with his eyes closed, hand near his chin. | 0:18 |
| Another man stands behind him near a red flag. | 18:28 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| An older man | man | man | nsubj | smiles | 0:3 |
| a white shirt | shirt | shirt | pobj | in | 4:7 |
| his eyes | eyes | eye | nsubj | closed | 9:11 |
| his chin | chin | chin | pobj | near | 15:17 |
| Another man | man | man | nsubj | stands | 18:20 |
| him | him | he | pobj | behind | 22:23 |
| a red flag | flag | flag | pobj | near | 24:27 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | An | an | DET | DT | det | man | 2 |
| 1 | older | old | ADJ | JJR | amod | man | 2 |
| 2 | man | man | NOUN | NN | nsubj | smiles | 7 |
| 3 | in | in | ADP | IN | prep | man | 2 |
| 4 | a | a | DET | DT | det | shirt | 6 |
| 5 | white | white | ADJ | JJ | amod | shirt | 6 |
| 6 | shirt | shirt | NOUN | NN | pobj | in | 3 |
| 7 | smiles | smile | VERB | VBZ | ROOT | smiles | 7 |
| 8 | with | with | SCONJ | IN | mark | closed | 11 |
| 9 | his | his | PRON | PRP$ | poss | eyes | 10 |
| 10 | eyes | eye | NOUN | NNS | nsubj | closed | 11 |
| 11 | closed | close | VERB | VBN | advcl | smiles | 7 |
| 12 | , | , | PUNCT | , | punct | smiles | 7 |
| 13 | hand | hand | NOUN | NN | advcl | smiles | 7 |
| 14 | near | near | ADP | IN | prep | hand | 13 |
| 15 | his | his | PRON | PRP$ | poss | chin | 16 |
| 16 | chin | chin | NOUN | NN | pobj | near | 14 |
| 17 | . | . | PUNCT | . | punct | smiles | 7 |
| 18 | Another | another | DET | DT | det | man | 19 |
| 19 | man | man | NOUN | NN | nsubj | stands | 20 |
| 20 | stands | stand | VERB | VBZ | ROOT | stands | 20 |
| 21 | behind | behind | ADP | IN | prep | stands | 20 |
| 22 | him | he | PRON | PRP | pobj | behind | 21 |
| 23 | near | near | ADP | IN | prep | stands | 20 |
| 24 | a | a | DET | DT | det | flag | 26 |
| 25 | red | red | ADJ | JJ | amod | flag | 26 |
| 26 | flag | flag | NOUN | NN | pobj | near | 23 |
| 27 | . | . | PUNCT | . | punct | stands | 20 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | older | old | chunk0 | 1 | visual_attribute | medium |
| m2 | object | shirt | shirt | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | white | white | chunk1 | 5 | color_attribute | high |
| m4 | object | eyes | eye | chunk2 | 10 | noun_chunk_root | high |
| m5 | object | chin | chin | chunk3 | 16 | noun_chunk_root | high |
| m6 | object | man | man | chunk4 | 19 | noun_chunk_root | high |
| m7 | object | flag | flag | chunk6 | 26 | noun_chunk_root | high |
| m8 | attribute | red | red | chunk6 | 25 | color_attribute | high |
| m9 | action | smiles | smile | doc | 7 | verb_predicate | high |
| m10 | action | closed | close | doc | 11 | verb_predicate | high |
| m11 | action | stands | stand | doc | 20 | verb_predicate | high |
| m12 | object | hand | hand | with_absolute8 | 13 | with_absolute_recovered_object | medium |

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

## 39

**caption_shape:** `multi-sentence`
**caption_id:** `14ce6ea91f458477c952f4c1ae223be78e62c40f49c03f1b1b0ea52ca062a014`

> Two men smile at the camera, standing close together indoors. One wears a blue shirt with a bandana around his neck, while the other in a white shirt has a black face mask hanging from his collar. A window and colorful wall art are visible behind them.

### Sentences
| sentence | token_span |
| --- | --- |
| Two men smile at the camera, standing close together indoors. | 0:12 |
| One wears a blue shirt with a bandana around his neck, while the other in a white shirt has a black face mask hanging from his collar. | 12:40 |
| A window and colorful wall art are visible behind them. | 40:51 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Two men | men | man | nsubj | smile | 0:2 |
| the camera | camera | camera | pobj | at | 4:6 |
| a blue shirt | shirt | shirt | dobj | wears | 14:17 |
| a bandana | bandana | bandana | pobj | with | 18:20 |
| his neck | neck | neck | pobj | around | 21:23 |
| a white shirt | shirt | shirt | pobj | in | 28:31 |
| a black face mask | face mask | face_mask | dobj | has | 32:35 |
| his collar | collar | collar | pobj | from | 37:39 |
| A window | window | window | nsubj | are | 40:42 |
| colorful wall art | art | art | conj | window | 43:46 |
| them | them | they | pobj | behind | 49:50 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Two | two | NUM | CD | nummod | men | 1 |
| 1 | men | man | NOUN | NNS | nsubj | smile | 2 |
| 2 | smile | smile | VERB | VBP | ROOT | smile | 2 |
| 3 | at | at | ADP | IN | prep | smile | 2 |
| 4 | the | the | DET | DT | det | camera | 5 |
| 5 | camera | camera | NOUN | NN | pobj | at | 3 |
| 6 | , | , | PUNCT | , | punct | smile | 2 |
| 7 | standing | stand | VERB | VBG | advcl | smile | 2 |
| 8 | close | close | ADV | RB | advmod | together | 9 |
| 9 | together | together | ADV | RB | advmod | standing | 7 |
| 10 | indoors | indoors | ADV | RB | advmod | standing | 7 |
| 11 | . | . | PUNCT | . | punct | smile | 2 |
| 12 | One | one | NUM | CD | nsubj | wears | 13 |
| 13 | wears | wear | VERB | VBZ | ROOT | wears | 13 |
| 14 | a | a | DET | DT | det | shirt | 16 |
| 15 | blue | blue | ADJ | JJ | amod | shirt | 16 |
| 16 | shirt | shirt | NOUN | NN | dobj | wears | 13 |
| 17 | with | with | ADP | IN | prep | shirt | 16 |
| 18 | a | a | DET | DT | det | bandana | 19 |
| 19 | bandana | bandana | NOUN | NN | pobj | with | 17 |
| 20 | around | around | ADP | IN | prep | bandana | 19 |
| 21 | his | his | PRON | PRP$ | poss | neck | 22 |
| 22 | neck | neck | NOUN | NN | pobj | around | 20 |
| 23 | , | , | PUNCT | , | punct | wears | 13 |
| 24 | while | while | SCONJ | IN | mark | has | 31 |
| 25 | the | the | DET | DT | det | other | 26 |
| 26 | other | other | ADJ | JJ | nsubj | has | 31 |
| 27 | in | in | ADP | IN | prep | other | 26 |
| 28 | a | a | DET | DT | det | shirt | 30 |
| 29 | white | white | ADJ | JJ | amod | shirt | 30 |
| 30 | shirt | shirt | NOUN | NN | pobj | in | 27 |
| 31 | has | have | VERB | VBZ | advcl | wears | 13 |
| 32 | a | a | DET | DT | det | face mask | 34 |
| 33 | black | black | ADJ | JJ | amod | face mask | 34 |
| 34 | face mask | face_mask | NOUN | NN | dobj | has | 31 |
| 35 | hanging | hang | VERB | VBG | acl | face mask | 34 |
| 36 | from | from | ADP | IN | prep | hanging | 35 |
| 37 | his | his | PRON | PRP$ | poss | collar | 38 |
| 38 | collar | collar | NOUN | NN | pobj | from | 36 |
| 39 | . | . | PUNCT | . | punct | wears | 13 |
| 40 | A | a | DET | DT | det | window | 41 |
| 41 | window | window | NOUN | NN | nsubj | are | 46 |
| 42 | and | and | CCONJ | CC | cc | window | 41 |
| 43 | colorful | colorful | ADJ | JJ | amod | art | 45 |
| 44 | wall | wall | NOUN | NN | compound | art | 45 |
| 45 | art | art | NOUN | NN | conj | window | 41 |
| 46 | are | be | AUX | VBP | ROOT | are | 46 |
| 47 | visible | visible | ADJ | JJ | acomp | are | 46 |
| 48 | behind | behind | ADP | IN | prep | are | 46 |
| 49 | them | they | PRON | PRP | pobj | behind | 48 |
| 50 | . | . | PUNCT | . | punct | are | 46 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | men | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Two | two | chunk0 | 0 | exact_quantity | high |
| m2 | object | camera | camera | chunk1 | 5 | noun_chunk_root | high |
| m3 | object | shirt | shirt | chunk2 | 16 | noun_chunk_root | high |
| m4 | attribute | blue | blue | chunk2 | 15 | color_attribute | high |
| m5 | object | bandana | bandana | chunk3 | 19 | noun_chunk_root | high |
| m6 | object | neck | neck | chunk4 | 22 | noun_chunk_root | high |
| m7 | object | shirt | shirt | chunk5 | 30 | noun_chunk_root | high |
| m8 | attribute | white | white | chunk5 | 29 | color_attribute | high |
| m9 | object | face mask | face_mask | chunk6 | 34 | noun_chunk_root | high |
| m10 | attribute | black | black | chunk6 | 33 | color_attribute | high |
| m11 | object | collar | collar | chunk7 | 38 | noun_chunk_root | high |
| m12 | object | window | window | chunk8 | 41 | noun_chunk_root | high |
| m13 | object | art | art | chunk9 | 45 | noun_chunk_root | high |
| m14 | attribute | colorful | colorful | chunk9 | 43 | modifier_attribute | medium |
| m15 | attribute | wall | wall | chunk9 | 44 | compound_modifier | medium |
| m16 | context | indoors | indoors | doc | 10 | scene_context | high |
| m17 | reference | One | one | nominal_reference | 12 | singular_substitute | high |
| m18 | reference | other | other | nominal_reference | 26 | contrastive_reference | high |
| m19 | action | smile | smile | doc | 2 | verb_predicate | high |
| m20 | action | standing | stand | doc | 7 | verb_predicate | high |
| m21 | action | wears | wear | doc | 13 | verb_predicate | high |
| m22 | action | has | have | doc | 31 | verb_predicate | high |
| m23 | action | hanging | hang | doc | 35 | verb_predicate | high |

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

## 40

**caption_shape:** `sentence-like`
**caption_id:** `1605f6676e726e65314c65203f0a83685636c214d328bfb75aae0031df0b8014`

> A historic cathedral with a tall tower and a red dome stands under a bright blue sky.

### Sentences
| sentence | token_span |
| --- | --- |
| A historic cathedral with a tall tower and a red dome stands under a bright blue sky. | 0:18 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A historic cathedral | cathedral | cathedral | nsubj | stands | 0:3 |
| a tall tower | tower | tower | pobj | with | 4:7 |
| a red dome | dome | dome | conj | tower | 8:11 |
| a bright blue sky | sky | sky | pobj | under | 13:17 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | cathedral | 2 |
| 1 | historic | historic | ADJ | JJ | amod | cathedral | 2 |
| 2 | cathedral | cathedral | NOUN | NN | nsubj | stands | 11 |
| 3 | with | with | ADP | IN | prep | cathedral | 2 |
| 4 | a | a | DET | DT | det | tower | 6 |
| 5 | tall | tall | ADJ | JJ | amod | tower | 6 |
| 6 | tower | tower | NOUN | NN | pobj | with | 3 |
| 7 | and | and | CCONJ | CC | cc | tower | 6 |
| 8 | a | a | DET | DT | det | dome | 10 |
| 9 | red | red | ADJ | JJ | amod | dome | 10 |
| 10 | dome | dome | NOUN | NN | conj | tower | 6 |
| 11 | stands | stand | VERB | VBZ | ROOT | stands | 11 |
| 12 | under | under | ADP | IN | prep | stands | 11 |
| 13 | a | a | DET | DT | det | sky | 16 |
| 14 | bright | bright | ADJ | JJ | amod | blue | 15 |
| 15 | blue | blue | ADJ | JJ | amod | sky | 16 |
| 16 | sky | sky | NOUN | NN | pobj | under | 12 |
| 17 | . | . | PUNCT | . | punct | stands | 11 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | cathedral | cathedral | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | historic | historic | chunk0 | 1 | modifier_attribute | medium |
| m2 | object | tower | tower | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | tall | tall | chunk1 | 5 | size_attribute | high |
| m4 | object | dome | dome | chunk2 | 10 | noun_chunk_root | high |
| m5 | attribute | red | red | chunk2 | 9 | color_attribute | high |
| m6 | object | sky | sky | chunk3 | 16 | noun_chunk_root | high |
| m7 | attribute | bright | bright | chunk3 | 14 | visual_attribute | medium |
| m8 | attribute | blue | blue | chunk3 | 15 | color_attribute | high |
| m9 | action | stands | stand | doc | 11 | verb_predicate | high |

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

## 41

**caption_shape:** `sentence-like`
**caption_id:** `16a2207dbb6320b5f61e69daeac0aa557b0398dd8d0a4e09c3d38f79dd0dc814`

> A brightly lit bridge with traditional Chinese architecture spans a river at night, its lights reflecting on the water.

### Sentences
| sentence | token_span |
| --- | --- |
| A brightly lit bridge with traditional Chinese architecture spans a river at night, its lights reflecting on the water. | 0:21 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A brightly lit bridge | bridge | bridge | nsubj | spans | 0:4 |
| traditional Chinese architecture | architecture | architecture | pobj | with | 5:8 |
| a river | river | river | dobj | spans | 9:11 |
| night | night | night | pobj | at | 12:13 |
| its lights | lights | light | nsubj | reflecting | 14:16 |
| the water | water | water | pobj | on | 18:20 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | bridge | 3 |
| 1 | brightly | brightly | ADV | RB | advmod | lit | 2 |
| 2 | lit | light | VERB | VBN | amod | bridge | 3 |
| 3 | bridge | bridge | NOUN | NN | nsubj | spans | 8 |
| 4 | with | with | ADP | IN | prep | bridge | 3 |
| 5 | traditional | traditional | ADJ | JJ | amod | architecture | 7 |
| 6 | Chinese | chinese | ADJ | JJ | amod | architecture | 7 |
| 7 | architecture | architecture | NOUN | NN | pobj | with | 4 |
| 8 | spans | span | VERB | VBZ | ROOT | spans | 8 |
| 9 | a | a | DET | DT | det | river | 10 |
| 10 | river | river | NOUN | NN | dobj | spans | 8 |
| 11 | at | at | ADP | IN | prep | spans | 8 |
| 12 | night | night | NOUN | NN | pobj | at | 11 |
| 13 | , | , | PUNCT | , | punct | spans | 8 |
| 14 | its | its | PRON | PRP$ | poss | lights | 15 |
| 15 | lights | light | NOUN | NNS | nsubj | reflecting | 16 |
| 16 | reflecting | reflect | VERB | VBG | advcl | spans | 8 |
| 17 | on | on | ADP | IN | prep | reflecting | 16 |
| 18 | the | the | DET | DT | det | water | 19 |
| 19 | water | water | NOUN | NN | pobj | on | 17 |
| 20 | . | . | PUNCT | . | punct | spans | 8 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | bridge | bridge | chunk0 | 3 | noun_chunk_root | high |
| m1 | attribute | brightly | brightly | chunk0 | 1 | modifier_attribute | medium |
| m2 | attribute | lit | light | chunk0 | 2 | visual_attribute | medium |
| m3 | object | architecture | architecture | chunk1 | 7 | noun_chunk_root | high |
| m4 | attribute | traditional | traditional | chunk1 | 5 | modifier_attribute | medium |
| m5 | attribute | Chinese | chinese | chunk1 | 6 | modifier_attribute | medium |
| m6 | object | river | river | chunk2 | 10 | noun_chunk_root | high |
| m7 | context | night | night | chunk3 | 12 | scene_context | medium |
| m8 | object | lights | light | chunk4 | 15 | noun_chunk_root | high |
| m9 | object | water | water | chunk5 | 19 | noun_chunk_root | high |
| m10 | action | spans | span | doc | 8 | verb_predicate | high |
| m11 | action | reflecting | reflect | doc | 16 | verb_predicate | high |

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

## 42

**caption_shape:** `tag-list-like`
**caption_id:** `17189150ed62a17be1e9c143c5ee30f47cd5b5c6026c36739702e340533c4c14`

> red jerseys, soccer players, grass field, team huddle

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | red jerseys | red jerseys | 0:11 |
| t1 | soccer players | soccer players | 13:27 |
| t2 | grass field | grass field | 29:40 |
| t3 | team huddle | team huddle | 42:53 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | red jerseys | jerseys | jersey | ROOT | jerseys | 0:2 | 0:11 |
| t1 | soccer players | soccer players | soccer_player | ROOT | soccer players | 0:1 | 13:27 |
| t2 | grass field | field | field | ROOT | field | 0:2 | 29:40 |
| t3 | team huddle | huddle | huddle | ROOT | huddle | 0:2 | 42:53 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | red | red | ADJ | ADJ | JJ | JJ | amod | jerseys | 1 | 0:3 |
| t0 | 1 | jerseys | jersey | NOUN | NOUN | NNS | NNS | ROOT | jerseys | 1 | 4:11 |
| t1 | 0 | soccer players | soccer_player | NOUN | NOUN | NN | NN | ROOT | soccer players | 0 | 13:27 |
| t2 | 0 | grass | grass | NOUN | NOUN | NN | NN | compound | field | 1 | 29:34 |
| t2 | 1 | field | field | NOUN | NOUN | NN | NN | ROOT | field | 1 | 35:40 |
| t3 | 0 | team | team | NOUN | NOUN | NN | NN | compound | huddle | 1 | 42:46 |
| t3 | 1 | huddle | huddle | NOUN | NOUN | NN | NN | ROOT | huddle | 1 | 47:53 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | jerseys | jersey | t0 | 1 | segment_head | high |
| m1 | attribute | red | red | t0 | 0 | attribute | high |
| m2 | object | soccer players | soccer_player | t1 | 0 | segment_head | high |
| m3 | object | field | field | t2 | 1 | segment_head | high |
| m4 | attribute | grass | grass | t2 | 0 | attribute | high |
| m5 | object | huddle | huddle | t3 | 1 | segment_head | high |
| m6 | attribute | team | team | t3 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> jerseys |
| e1 | has_attribute | m3 | m4 | high | t2 internal compound -> field |
| e2 | has_attribute | m5 | m6 | high | t3 internal compound -> huddle |

## 43

**caption_shape:** `multi-sentence`
**caption_id:** `173fffdc074a0d1191247922c97a20b543a27d12047ff7e244466a02f5da9814`

> The open trunk of a black car contains a custom audio setup with a subwoofer and a framed display. A gray, monster-like figurine stands on the right side near the rear seats. The interior is lined with black leather, and another car is visible in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| The open trunk of a black car contains a custom audio setup with a subwoofer and a framed display. | 0:20 |
| A gray, monster-like figurine stands on the right side near the rear seats. | 20:35 |
| The interior is lined with black leather, and another car is visible in the background. | 35:52 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| The open trunk | trunk | trunk | nsubj | contains | 0:3 |
| a black car | car | car | pobj | of | 4:7 |
| a custom audio setup | setup | setup | dobj | contains | 8:12 |
| a subwoofer | subwoofer | subwoofer | pobj | with | 13:15 |
| a framed display | display | display | conj | subwoofer | 16:19 |
| A gray, monster-like figurine | figurine | figurine | nsubj | stands | 20:25 |
| the right side | side | side | pobj | on | 27:30 |
| the rear seats | seats | seat | pobj | near | 31:34 |
| The interior | interior | interior | nsubjpass | lined | 35:37 |
| black leather | leather | leather | pobj | with | 40:42 |
| another car | car | car | nsubj | is | 44:46 |
| the background | background | background | pobj | in | 49:51 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | The | the | DET | DT | det | trunk | 2 |
| 1 | open | open | ADJ | JJ | amod | trunk | 2 |
| 2 | trunk | trunk | NOUN | NN | nsubj | contains | 7 |
| 3 | of | of | ADP | IN | prep | trunk | 2 |
| 4 | a | a | DET | DT | det | car | 6 |
| 5 | black | black | ADJ | JJ | amod | car | 6 |
| 6 | car | car | NOUN | NN | pobj | of | 3 |
| 7 | contains | contain | VERB | VBZ | ROOT | contains | 7 |
| 8 | a | a | DET | DT | det | setup | 11 |
| 9 | custom | custom | NOUN | NN | nmod | setup | 11 |
| 10 | audio | audio | ADJ | JJ | amod | setup | 11 |
| 11 | setup | setup | NOUN | NN | dobj | contains | 7 |
| 12 | with | with | ADP | IN | prep | setup | 11 |
| 13 | a | a | DET | DT | det | subwoofer | 14 |
| 14 | subwoofer | subwoofer | NOUN | NN | pobj | with | 12 |
| 15 | and | and | CCONJ | CC | cc | subwoofer | 14 |
| 16 | a | a | DET | DT | det | display | 18 |
| 17 | framed | frame | VERB | VBN | amod | display | 18 |
| 18 | display | display | NOUN | NN | conj | subwoofer | 14 |
| 19 | . | . | PUNCT | . | punct | contains | 7 |
| 20 | A | a | DET | DT | det | figurine | 24 |
| 21 | gray | gray | ADJ | JJ | amod | figurine | 24 |
| 22 | , | , | PUNCT | , | punct | figurine | 24 |
| 23 | monster-like | monster-like | ADJ | JJ | amod | figurine | 24 |
| 24 | figurine | figurine | NOUN | NN | nsubj | stands | 25 |
| 25 | stands | stand | VERB | VBZ | ROOT | stands | 25 |
| 26 | on | on | ADP | IN | prep | stands | 25 |
| 27 | the | the | DET | DT | det | side | 29 |
| 28 | right | right | ADJ | JJ | amod | side | 29 |
| 29 | side | side | NOUN | NN | pobj | on | 26 |
| 30 | near | near | ADP | IN | prep | stands | 25 |
| 31 | the | the | DET | DT | det | seats | 33 |
| 32 | rear | rear | ADJ | JJ | amod | seats | 33 |
| 33 | seats | seat | NOUN | NNS | pobj | near | 30 |
| 34 | . | . | PUNCT | . | punct | stands | 25 |
| 35 | The | the | DET | DT | det | interior | 36 |
| 36 | interior | interior | NOUN | NN | nsubjpass | lined | 38 |
| 37 | is | be | AUX | VBZ | auxpass | lined | 38 |
| 38 | lined | line | VERB | VBN | ROOT | lined | 38 |
| 39 | with | with | ADP | IN | prep | lined | 38 |
| 40 | black | black | ADJ | JJ | amod | leather | 41 |
| 41 | leather | leather | NOUN | NN | pobj | with | 39 |
| 42 | , | , | PUNCT | , | punct | lined | 38 |
| 43 | and | and | CCONJ | CC | cc | lined | 38 |
| 44 | another | another | DET | DT | det | car | 45 |
| 45 | car | car | NOUN | NN | nsubj | is | 46 |
| 46 | is | be | AUX | VBZ | conj | lined | 38 |
| 47 | visible | visible | ADJ | JJ | acomp | is | 46 |
| 48 | in | in | ADP | IN | prep | is | 46 |
| 49 | the | the | DET | DT | det | background | 50 |
| 50 | background | background | NOUN | NN | pobj | in | 48 |
| 51 | . | . | PUNCT | . | punct | is | 46 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | trunk | trunk | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | open | open | chunk0 | 1 | modifier_attribute | medium |
| m2 | object | car | car | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | black | black | chunk1 | 5 | color_attribute | high |
| m4 | object | setup | setup | chunk2 | 11 | noun_chunk_root | high |
| m5 | attribute | audio | audio | chunk2 | 10 | modifier_attribute | medium |
| m6 | object | subwoofer | subwoofer | chunk3 | 14 | noun_chunk_root | high |
| m7 | object | display | display | chunk4 | 18 | noun_chunk_root | high |
| m8 | attribute | framed | frame | chunk4 | 17 | state_attribute | medium |
| m9 | object | figurine | figurine | chunk5 | 24 | noun_chunk_root | high |
| m10 | attribute | gray | gray | chunk5 | 21 | color_attribute | high |
| m11 | attribute | monster-like | monster-like | chunk5 | 23 | modifier_attribute | medium |
| m12 | context | side | side | chunk6 | 29 | spatial_region | medium |
| m13 | object | seats | seat | chunk7 | 33 | noun_chunk_root | high |
| m14 | attribute | rear | rear | chunk7 | 32 | modifier_attribute | medium |
| m15 | object | interior | interior | chunk8 | 36 | noun_chunk_root | high |
| m16 | object | leather | leather | chunk9 | 41 | noun_chunk_root | high |
| m17 | attribute | black | black | chunk9 | 40 | color_attribute | high |
| m18 | object | car | car | chunk10 | 45 | noun_chunk_root | high |
| m19 | context | background | background | chunk11 | 50 | scene_context | high |
| m20 | action | contains | contain | doc | 7 | verb_predicate | high |
| m21 | action | stands | stand | doc | 25 | verb_predicate | high |
| m22 | action | lined | line | doc | 38 | verb_predicate | high |

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

## 44

**caption_shape:** `sentence-like`
**caption_id:** `193c8da25cf4cf5a476da04622867cdbbd9870e204facf9d63d41427341d3c14`

> A black-and-white aerial view shows a patchwork of farmland divided into rectangular fields.

### Sentences
| sentence | token_span |
| --- | --- |
| A black-and-white aerial view shows a patchwork of farmland divided into rectangular fields. | 0:14 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A black-and-white aerial view | view | view | nsubj | shows | 0:4 |
| a patchwork | patchwork | patchwork | dobj | shows | 5:7 |
| farmland | farmland | farmland | pobj | of | 8:9 |
| rectangular fields | fields | field | pobj | into | 11:13 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | view | 3 |
| 1 | black-and-white | black-and-white | ADJ | JJ | amod | view | 3 |
| 2 | aerial | aerial | ADJ | JJ | amod | view | 3 |
| 3 | view | view | NOUN | NN | nsubj | shows | 4 |
| 4 | shows | show | VERB | VBZ | ROOT | shows | 4 |
| 5 | a | a | DET | DT | det | patchwork | 6 |
| 6 | patchwork | patchwork | NOUN | NN | dobj | shows | 4 |
| 7 | of | of | ADP | IN | prep | patchwork | 6 |
| 8 | farmland | farmland | NOUN | NN | pobj | of | 7 |
| 9 | divided | divide | VERB | VBN | acl | farmland | 8 |
| 10 | into | into | ADP | IN | prep | divided | 9 |
| 11 | rectangular | rectangular | ADJ | JJ | amod | fields | 12 |
| 12 | fields | field | NOUN | NNS | pobj | into | 10 |
| 13 | . | . | PUNCT | . | punct | shows | 4 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | view | view | chunk0 | 3 | noun_chunk_root | high |
| m1 | attribute | black-and-white | black-and-white | chunk0 | 1 | modifier_attribute | medium |
| m2 | attribute | aerial | aerial | chunk0 | 2 | modifier_attribute | medium |
| m3 | object | patchwork | patchwork | chunk1 | 6 | noun_chunk_root | high |
| m4 | object | farmland | farmland | chunk2 | 8 | noun_chunk_root | high |
| m5 | object | fields | field | chunk3 | 12 | noun_chunk_root | high |
| m6 | attribute | rectangular | rectangular | chunk3 | 11 | modifier_attribute | medium |
| m7 | action | shows | show | doc | 4 | verb_predicate | high |
| m8 | action | divided | divide | doc | 9 | verb_predicate | high |

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

## 45

**caption_shape:** `tag-list-like`
**caption_id:** `1a67a5e6fc7fc7f52fc413539887acd32937b29d38364ff00522ad1372764414`

> man speaking, suit, water bottle, nameplate

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | man speaking | man speaking | 0:12 |
| t1 | suit | suit | 14:18 |
| t2 | water bottle | water bottle | 20:32 |
| t3 | nameplate | nameplate | 34:43 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | man | man | man | nsubj | speaking | 0:1 | 0:3 |
| t1 | suit | suit | suit | ROOT | suit | 0:1 | 14:18 |
| t2 | water bottle | bottle | bottle | ROOT | bottle | 0:2 | 20:32 |
| t3 | nameplate | nameplate | nameplate | ROOT | nameplate | 0:1 | 34:43 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | man | man | PROPN | NOUN | NNP | NN | nsubj | speaking | 1 | 0:3 |
| t0 | 1 | speaking | speak | VERB | ADJ | VBG | VBG | ROOT | speaking | 1 | 4:12 |
| t1 | 0 | suit | suit | NOUN | NOUN | NN | NN | ROOT | suit | 0 | 14:18 |
| t2 | 0 | water | water | NOUN | NOUN | NN | NN | compound | bottle | 1 | 20:25 |
| t2 | 1 | bottle | bottle | NOUN | NOUN | NN | NN | ROOT | bottle | 1 | 26:32 |
| t3 | 0 | nameplate | nameplate | NOUN | NOUN | NN | NN | ROOT | nameplate | 0 | 34:43 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | t0 | 0 | segment_head | high |
| m1 | object | suit | suit | t1 | 0 | segment_head | high |
| m2 | object | bottle | bottle | t2 | 1 | segment_head | high |
| m3 | attribute | water | water | t2 | 0 | attribute | high |
| m4 | object | nameplate | nameplate | t3 | 0 | segment_head | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | t2 internal compound -> bottle |

## 46

**caption_shape:** `tag-list-like`
**caption_id:** `1cb6a222d3d9321d4c56d2de803c0e749d84c866122202d7ad305cca64c15014`

> ice rink, hockey player, goalie, blue jersey, protective gear

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | ice rink | ice rink | 0:8 |
| t1 | hockey player | hockey player | 10:23 |
| t2 | goalie | goalie | 25:31 |
| t3 | blue jersey | blue jersey | 33:44 |
| t4 | protective gear | protective gear | 46:61 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | ice rink | ice rink | ice_rink | ROOT | ice rink | 0:1 | 0:8 |
| t1 | hockey player | hockey player | hockey_player | ROOT | hockey player | 0:1 | 10:23 |
| t2 | goalie | goalie | goalie | ROOT | goalie | 0:1 | 25:31 |
| t3 | blue jersey | jersey | jersey | ROOT | jersey | 0:2 | 33:44 |
| t4 | protective gear | gear | gear | ROOT | gear | 0:2 | 46:61 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | ice rink | ice_rink | NOUN | NOUN | NN | NN | ROOT | ice rink | 0 | 0:8 |
| t1 | 0 | hockey player | hockey_player | NOUN | NOUN | NN | NN | ROOT | hockey player | 0 | 10:23 |
| t2 | 0 | goalie | goalie | NOUN | NOUN | NN | NN | ROOT | goalie | 0 | 25:31 |
| t3 | 0 | blue | blue | PROPN | ADJ | NNP | JJ | compound | jersey | 1 | 33:37 |
| t3 | 1 | jersey | jersey | PROPN | NOUN | NNP | NN | ROOT | jersey | 1 | 38:44 |
| t4 | 0 | protective | protective | ADJ | ADJ | JJ | JJ | amod | gear | 1 | 46:56 |
| t4 | 1 | gear | gear | NOUN | NOUN | NN | NN | ROOT | gear | 1 | 57:61 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | ice rink | ice_rink | t0 | 0 | segment_head | high |
| m1 | object | hockey player | hockey_player | t1 | 0 | segment_head | high |
| m2 | object | goalie | goalie | t2 | 0 | segment_head | high |
| m3 | object | jersey | jersey | t3 | 1 | segment_head | high |
| m4 | attribute | blue | blue | t3 | 0 | attribute | high |
| m5 | object | gear | gear | t4 | 1 | segment_head | high |
| m6 | attribute | protective | protective | t4 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m3 | m4 | high | t3 internal compound -> jersey |
| e1 | has_attribute | m5 | m6 | high | t4 internal amod -> gear |

## 47

**caption_shape:** `sentence-like`
**caption_id:** `1dda6c4dd9a5dc36750df82f622cd494428d712da6c3be28c32459395a813c14`

> A person wearing a conical hat walks through tall green corn plants in a field.

### Sentences
| sentence | token_span |
| --- | --- |
| A person wearing a conical hat walks through tall green corn plants in a field. | 0:16 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A person | person | person | nsubj | walks | 0:2 |
| a conical hat | hat | hat | dobj | wearing | 3:6 |
| tall green corn plants | plants | plant | pobj | through | 8:12 |
| a field | field | field | pobj | in | 13:15 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | person | 1 |
| 1 | person | person | NOUN | NN | nsubj | walks | 6 |
| 2 | wearing | wear | VERB | VBG | acl | person | 1 |
| 3 | a | a | DET | DT | det | hat | 5 |
| 4 | conical | conical | ADJ | JJ | amod | hat | 5 |
| 5 | hat | hat | NOUN | NN | dobj | wearing | 2 |
| 6 | walks | walk | VERB | VBZ | ROOT | walks | 6 |
| 7 | through | through | ADP | IN | prep | walks | 6 |
| 8 | tall | tall | ADJ | JJ | amod | plants | 11 |
| 9 | green | green | ADJ | JJ | amod | plants | 11 |
| 10 | corn | corn | NOUN | NN | compound | plants | 11 |
| 11 | plants | plant | NOUN | NNS | pobj | through | 7 |
| 12 | in | in | ADP | IN | prep | walks | 6 |
| 13 | a | a | DET | DT | det | field | 14 |
| 14 | field | field | NOUN | NN | pobj | in | 12 |
| 15 | . | . | PUNCT | . | punct | walks | 6 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | hat | hat | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | conical | conical | chunk1 | 4 | modifier_attribute | medium |
| m3 | object | plants | plant | chunk2 | 11 | noun_chunk_root | high |
| m4 | attribute | tall | tall | chunk2 | 8 | size_attribute | high |
| m5 | attribute | green | green | chunk2 | 9 | color_attribute | high |
| m6 | attribute | corn | corn | chunk2 | 10 | compound_modifier | medium |
| m7 | object | field | field | chunk3 | 14 | noun_chunk_root | high |
| m8 | action | wearing | wear | doc | 2 | verb_predicate | high |
| m9 | action | walks | walk | doc | 6 | verb_predicate | high |

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

## 48

**caption_shape:** `tag-list-like`
**caption_id:** `206ea33b318039c8b699513c268fbdd208745194d679338b72093f3038337814`

> beach, palm trees, people, van, grass, ocean

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | beach | beach | 0:5 |
| t1 | palm trees | palm trees | 7:17 |
| t2 | people | people | 19:25 |
| t3 | van | van | 27:30 |
| t4 | grass | grass | 32:37 |
| t5 | ocean | ocean | 39:44 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | beach | beach | beach | ROOT | beach | 0:1 | 0:5 |
| t1 | palm trees | palm trees | palm_tree | ROOT | palm trees | 0:1 | 7:17 |
| t2 | people | people | people | ROOT | people | 0:1 | 19:25 |
| t3 | van | van | van | ROOT | van | 0:1 | 27:30 |
| t4 | grass | grass | grass | ROOT | grass | 0:1 | 32:37 |
| t5 | ocean | ocean | ocean | ROOT | ocean | 0:1 | 39:44 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | beach | beach | NOUN | NOUN | NN | NN | ROOT | beach | 0 | 0:5 |
| t1 | 0 | palm trees | palm_tree | NOUN | NOUN | NN | NN | ROOT | palm trees | 0 | 7:17 |
| t2 | 0 | people | people | NOUN | NOUN | NNS | NNS | ROOT | people | 0 | 19:25 |
| t3 | 0 | van | van | PROPN | NOUN | NNP | NN | ROOT | van | 0 | 27:30 |
| t4 | 0 | grass | grass | NOUN | NOUN | NN | NN | ROOT | grass | 0 | 32:37 |
| t5 | 0 | ocean | ocean | NOUN | NOUN | NN | NN | ROOT | ocean | 0 | 39:44 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | beach | beach | t0 | 0 | segment_head | high |
| m1 | object | palm trees | palm_tree | t1 | 0 | segment_head | high |
| m2 | object | people | people | t2 | 0 | segment_head | high |
| m3 | object | van | van | t3 | 0 | segment_head | high |
| m4 | object | grass | grass | t4 | 0 | segment_head | high |
| m5 | object | ocean | ocean | t5 | 0 | segment_head | high |

### Edges
_none_

## 49

**caption_shape:** `tag-list-like`
**caption_id:** `20f9f6aa1b9882a46648386e9ee87f61be444356d78b198b99fb10f2cdb9dc14`

> snowy path, frosted trees, blue sky, winter landscape, bare branches

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | snowy path | snowy path | 0:10 |
| t1 | frosted trees | frosted trees | 12:25 |
| t2 | blue sky | blue sky | 27:35 |
| t3 | winter landscape | winter landscape | 37:53 |
| t4 | bare branches | bare branches | 55:68 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | snowy path | path | path | ROOT | path | 0:2 | 0:10 |
| t1 | frosted trees | trees | tree | ROOT | trees | 0:2 | 12:25 |
| t2 | blue sky | sky | sky | ROOT | sky | 0:2 | 27:35 |
| t3 | winter landscape | landscape | landscape | ROOT | landscape | 0:2 | 37:53 |
| t4 | bare branches | branches | branch | ROOT | branches | 0:2 | 55:68 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | snowy | snowy | ADJ | ADJ | JJ | JJ | amod | path | 1 | 0:5 |
| t0 | 1 | path | path | NOUN | NOUN | NN | NN | ROOT | path | 1 | 6:10 |
| t1 | 0 | frosted | frosted | ADJ | ADJ | JJ | JJ | amod | trees | 1 | 12:19 |
| t1 | 1 | trees | tree | NOUN | NOUN | NNS | NNS | ROOT | trees | 1 | 20:25 |
| t2 | 0 | blue | blue | ADJ | ADJ | JJ | JJ | amod | sky | 1 | 27:31 |
| t2 | 1 | sky | sky | NOUN | NOUN | NN | NN | ROOT | sky | 1 | 32:35 |
| t3 | 0 | winter | winter | NOUN | NOUN | NN | NN | compound | landscape | 1 | 37:43 |
| t3 | 1 | landscape | landscape | NOUN | NOUN | NN | NN | ROOT | landscape | 1 | 44:53 |
| t4 | 0 | bare | bare | ADJ | ADJ | JJ | JJ | amod | branches | 1 | 55:59 |
| t4 | 1 | branches | branch | NOUN | NOUN | NNS | NNS | ROOT | branches | 1 | 60:68 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | path | path | t0 | 1 | segment_head | high |
| m1 | attribute | snowy | snowy | t0 | 0 | attribute | high |
| m2 | object | trees | tree | t1 | 1 | segment_head | high |
| m3 | attribute | frosted | frosted | t1 | 0 | attribute | high |
| m4 | object | sky | sky | t2 | 1 | segment_head | high |
| m5 | attribute | blue | blue | t2 | 0 | attribute | high |
| m6 | object | landscape | landscape | t3 | 1 | segment_head | high |
| m7 | attribute | winter | winter | t3 | 0 | attribute | high |
| m8 | object | branches | branch | t4 | 1 | segment_head | high |
| m9 | attribute | bare | bare | t4 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> path |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> trees |
| e2 | has_attribute | m4 | m5 | high | t2 internal amod -> sky |
| e3 | has_attribute | m6 | m7 | high | t3 internal compound -> landscape |
| e4 | has_attribute | m8 | m9 | high | t4 internal amod -> branches |

## 50

**caption_shape:** `sentence-like`
**caption_id:** `211c24a95c3516500269ebd16ea4c6fc0ad5745b24794fcc1df25d5d7327f014`

> A Hard Rock Cafe sign is on a red building at Pier 39, with an American flag flying above.

### Sentences
| sentence | token_span |
| --- | --- |
| A Hard Rock Cafe sign is on a red building at Pier 39, with an American flag flying above. | 0:20 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A Hard Rock Cafe sign | sign | sign | nsubj | is | 0:5 |
| a red building | building | building | pobj | on | 7:10 |
| Pier | Pier | Pier | pobj | at | 11:12 |
| an American flag | American flag | american_flag | nsubj | flying | 15:17 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | sign | 4 |
| 1 | Hard | Hard | PROPN | NNP | compound | Rock | 2 |
| 2 | Rock | Rock | PROPN | NNP | compound | Cafe | 3 |
| 3 | Cafe | Cafe | PROPN | NNP | compound | sign | 4 |
| 4 | sign | sign | NOUN | NN | nsubj | is | 5 |
| 5 | is | be | AUX | VBZ | ROOT | is | 5 |
| 6 | on | on | ADP | IN | prep | is | 5 |
| 7 | a | a | DET | DT | det | building | 9 |
| 8 | red | red | ADJ | JJ | amod | building | 9 |
| 9 | building | building | NOUN | NN | pobj | on | 6 |
| 10 | at | at | ADP | IN | prep | building | 9 |
| 11 | Pier | Pier | PROPN | NNP | pobj | at | 10 |
| 12 | 39 | 39 | NUM | CD | nummod | Pier | 11 |
| 13 | , | , | PUNCT | , | punct | is | 5 |
| 14 | with | with | ADP | IN | prep | is | 5 |
| 15 | an | an | DET | DT | det | American flag | 16 |
| 16 | American flag | american_flag | NOUN | NN | nsubj | flying | 17 |
| 17 | flying | fly | VERB | VBG | pcomp | with | 14 |
| 18 | above | above | ADV | RB | advmod | flying | 17 |
| 19 | . | . | PUNCT | . | punct | is | 5 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | sign | sign | chunk0 | 4 | noun_chunk_root | high |
| m1 | attribute | Hard | hard | chunk0 | 1 | compound_modifier | medium |
| m2 | attribute | Rock | rock | chunk0 | 2 | compound_modifier | medium |
| m3 | attribute | Cafe | cafe | chunk0 | 3 | compound_modifier | medium |
| m4 | object | building | building | chunk1 | 9 | noun_chunk_root | high |
| m5 | attribute | red | red | chunk1 | 8 | color_attribute | high |
| m6 | object | Pier | pier | chunk2 | 11 | noun_chunk_root | high |
| m7 | object | American flag | american_flag | chunk3 | 16 | noun_chunk_root | high |
| m8 | action | flying | fly | doc | 17 | verb_predicate | high |

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

## 51

**caption_shape:** `multi-sentence`
**caption_id:** `2212e683c5261f5a8d61ac3b532609ea0dfdcf733e158178ebfd2dac85ca6814`

> A man stands on a rocky hillside with sparse bushes, wearing a yellow jacket and blue shirt. Distant mountains rise under a pale sky.

### Sentences
| sentence | token_span |
| --- | --- |
| A man stands on a rocky hillside with sparse bushes, wearing a yellow jacket and blue shirt. | 0:19 |
| Distant mountains rise under a pale sky. | 19:27 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A man | man | man | nsubj | stands | 0:2 |
| a rocky hillside | hillside | hillside | pobj | on | 4:7 |
| sparse bushes | bushes | bush | pobj | with | 8:10 |
| a yellow jacket | jacket | jacket | dobj | wearing | 12:15 |
| blue shirt | shirt | shirt | conj | jacket | 16:18 |
| Distant mountains | mountains | mountain | nsubj | rise | 19:21 |
| a pale sky | sky | sky | pobj | under | 23:26 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | man | 1 |
| 1 | man | man | NOUN | NN | nsubj | stands | 2 |
| 2 | stands | stand | VERB | VBZ | ROOT | stands | 2 |
| 3 | on | on | ADP | IN | prep | stands | 2 |
| 4 | a | a | DET | DT | det | hillside | 6 |
| 5 | rocky | rocky | ADJ | JJ | amod | hillside | 6 |
| 6 | hillside | hillside | NOUN | NN | pobj | on | 3 |
| 7 | with | with | ADP | IN | prep | hillside | 6 |
| 8 | sparse | sparse | ADJ | JJ | amod | bushes | 9 |
| 9 | bushes | bush | NOUN | NNS | pobj | with | 7 |
| 10 | , | , | PUNCT | , | punct | stands | 2 |
| 11 | wearing | wear | VERB | VBG | advcl | stands | 2 |
| 12 | a | a | DET | DT | det | jacket | 14 |
| 13 | yellow | yellow | ADJ | JJ | amod | jacket | 14 |
| 14 | jacket | jacket | NOUN | NN | dobj | wearing | 11 |
| 15 | and | and | CCONJ | CC | cc | jacket | 14 |
| 16 | blue | blue | ADJ | JJ | amod | shirt | 17 |
| 17 | shirt | shirt | NOUN | NN | conj | jacket | 14 |
| 18 | . | . | PUNCT | . | punct | stands | 2 |
| 19 | Distant | distant | ADJ | JJ | amod | mountains | 20 |
| 20 | mountains | mountain | NOUN | NNS | nsubj | rise | 21 |
| 21 | rise | rise | VERB | VBP | ROOT | rise | 21 |
| 22 | under | under | ADP | IN | prep | rise | 21 |
| 23 | a | a | DET | DT | det | sky | 25 |
| 24 | pale | pale | ADJ | JJ | amod | sky | 25 |
| 25 | sky | sky | NOUN | NN | pobj | under | 22 |
| 26 | . | . | PUNCT | . | punct | rise | 21 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | hillside | hillside | chunk1 | 6 | noun_chunk_root | high |
| m2 | attribute | rocky | rocky | chunk1 | 5 | modifier_attribute | medium |
| m3 | object | bushes | bush | chunk2 | 9 | noun_chunk_root | high |
| m4 | attribute | sparse | sparse | chunk2 | 8 | modifier_attribute | medium |
| m5 | object | jacket | jacket | chunk3 | 14 | noun_chunk_root | high |
| m6 | attribute | yellow | yellow | chunk3 | 13 | color_attribute | high |
| m7 | object | shirt | shirt | chunk4 | 17 | noun_chunk_root | high |
| m8 | attribute | blue | blue | chunk4 | 16 | color_attribute | high |
| m9 | object | mountains | mountain | chunk5 | 20 | noun_chunk_root | high |
| m10 | attribute | Distant | distant | chunk5 | 19 | modifier_attribute | medium |
| m11 | object | sky | sky | chunk6 | 25 | noun_chunk_root | high |
| m12 | attribute | pale | pale | chunk6 | 24 | modifier_attribute | medium |
| m13 | action | stands | stand | doc | 2 | verb_predicate | high |
| m14 | action | wearing | wear | doc | 11 | verb_predicate | high |
| m15 | action | rise | rise | doc | 21 | verb_predicate | high |

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

## 52

**caption_shape:** `tag-list-like`
**caption_id:** `22934f61d98bca9733a9e09fee584a49438e4b06a954b581673247f3ef307014`

> football players, red uniforms, blue jerseys, stadium entrance, crowd, young boy

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | football players | football players | 0:16 |
| t1 | red uniforms | red uniforms | 18:30 |
| t2 | blue jerseys | blue jerseys | 32:44 |
| t3 | stadium entrance | stadium entrance | 46:62 |
| t4 | crowd | crowd | 64:69 |
| t5 | young boy | young boy | 71:80 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | football players | football players | football_player | ROOT | football players | 0:1 | 0:16 |
| t1 | red uniforms | uniforms | uniform | ROOT | uniforms | 0:2 | 18:30 |
| t2 | blue jerseys | jerseys | jersey | ROOT | jerseys | 0:2 | 32:44 |
| t3 | stadium entrance | entrance | entrance | ROOT | entrance | 0:2 | 46:62 |
| t4 | crowd | crowd | crowd | ROOT | crowd | 0:1 | 64:69 |
| t5 | young boy | boy | boy | ROOT | boy | 0:2 | 71:80 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | football players | football_player | NOUN | NOUN | NN | NN | ROOT | football players | 0 | 0:16 |
| t1 | 0 | red | red | ADJ | ADJ | JJ | JJ | amod | uniforms | 1 | 18:21 |
| t1 | 1 | uniforms | uniform | NOUN | NOUN | NNS | NNS | ROOT | uniforms | 1 | 22:30 |
| t2 | 0 | blue | blue | ADJ | ADJ | JJ | JJ | amod | jerseys | 1 | 32:36 |
| t2 | 1 | jerseys | jersey | NOUN | NOUN | NNS | NNS | ROOT | jerseys | 1 | 37:44 |
| t3 | 0 | stadium | stadium | NOUN | NOUN | NN | NN | compound | entrance | 1 | 46:53 |
| t3 | 1 | entrance | entrance | NOUN | NOUN | NN | NN | ROOT | entrance | 1 | 54:62 |
| t4 | 0 | crowd | crowd | NOUN | NOUN | NN | NN | ROOT | crowd | 0 | 64:69 |
| t5 | 0 | young | young | ADJ | ADJ | JJ | JJ | amod | boy | 1 | 71:76 |
| t5 | 1 | boy | boy | NOUN | NOUN | NN | NN | ROOT | boy | 1 | 77:80 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | football players | football_player | t0 | 0 | segment_head | high |
| m1 | object | uniforms | uniform | t1 | 1 | segment_head | high |
| m2 | attribute | red | red | t1 | 0 | attribute | high |
| m3 | object | jerseys | jersey | t2 | 1 | segment_head | high |
| m4 | attribute | blue | blue | t2 | 0 | attribute | high |
| m5 | object | entrance | entrance | t3 | 1 | segment_head | high |
| m6 | attribute | stadium | stadium | t3 | 0 | attribute | high |
| m7 | object | crowd | crowd | t4 | 0 | segment_head | high |
| m8 | object | boy | boy | t5 | 1 | segment_head | high |
| m9 | attribute | young | young | t5 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | t1 internal amod -> uniforms |
| e1 | has_attribute | m3 | m4 | high | t2 internal amod -> jerseys |
| e2 | has_attribute | m5 | m6 | high | t3 internal compound -> entrance |
| e3 | has_attribute | m8 | m9 | high | t5 internal amod -> boy |

## 53

**caption_shape:** `multi-sentence`
**caption_id:** `2357777249fc3c53b6aba571795157f507c24b93ffb180994e7c09ce69012c14`

> A man with gray hair speaks into a microphone while wearing a blue patterned shirt. He stands outdoors under a large white structure, with buildings and trees visible in the background. A person in a green vest is partially seen to his left.

### Sentences
| sentence | token_span |
| --- | --- |
| A man with gray hair speaks into a microphone while wearing a blue patterned shirt. | 0:16 |
| He stands outdoors under a large white structure, with buildings and trees visible in the background. | 16:34 |
| A person in a green vest is partially seen to his left. | 34:47 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A man | man | man | nsubj | speaks | 0:2 |
| gray hair | hair | hair | pobj | with | 3:5 |
| a microphone | microphone | microphone | pobj | into | 7:9 |
| a blue patterned shirt | shirt | shirt | dobj | wearing | 11:15 |
| He | He | he | nsubj | stands | 16:17 |
| a large white structure | structure | structure | pobj | under | 20:24 |
| buildings | buildings | building | nsubj | visible | 26:27 |
| trees | trees | tree | conj | buildings | 28:29 |
| the background | background | background | pobj | in | 31:33 |
| A person | person | person | nsubjpass | seen | 34:36 |
| a green vest | vest | vest | pobj | in | 37:40 |
| his left | left | left | pobj | to | 44:46 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | man | 1 |
| 1 | man | man | NOUN | NN | nsubj | speaks | 5 |
| 2 | with | with | ADP | IN | prep | man | 1 |
| 3 | gray | gray | ADJ | JJ | amod | hair | 4 |
| 4 | hair | hair | NOUN | NN | pobj | with | 2 |
| 5 | speaks | speak | VERB | VBZ | ROOT | speaks | 5 |
| 6 | into | into | ADP | IN | prep | speaks | 5 |
| 7 | a | a | DET | DT | det | microphone | 8 |
| 8 | microphone | microphone | NOUN | NN | pobj | into | 6 |
| 9 | while | while | SCONJ | IN | mark | wearing | 10 |
| 10 | wearing | wear | VERB | VBG | advcl | speaks | 5 |
| 11 | a | a | DET | DT | det | shirt | 14 |
| 12 | blue | blue | ADJ | JJ | amod | shirt | 14 |
| 13 | patterned | patterned | ADJ | JJ | amod | shirt | 14 |
| 14 | shirt | shirt | NOUN | NN | dobj | wearing | 10 |
| 15 | . | . | PUNCT | . | punct | speaks | 5 |
| 16 | He | he | PRON | PRP | nsubj | stands | 17 |
| 17 | stands | stand | VERB | VBZ | ROOT | stands | 17 |
| 18 | outdoors | outdoors | ADV | RB | advmod | stands | 17 |
| 19 | under | under | ADP | IN | prep | stands | 17 |
| 20 | a | a | DET | DT | det | structure | 23 |
| 21 | large | large | ADJ | JJ | amod | structure | 23 |
| 22 | white | white | ADJ | JJ | amod | structure | 23 |
| 23 | structure | structure | NOUN | NN | pobj | under | 19 |
| 24 | , | , | PUNCT | , | punct | stands | 17 |
| 25 | with | with | SCONJ | IN | mark | visible | 29 |
| 26 | buildings | building | NOUN | NNS | nsubj | visible | 29 |
| 27 | and | and | CCONJ | CC | cc | buildings | 26 |
| 28 | trees | tree | NOUN | NNS | conj | buildings | 26 |
| 29 | visible | visible | ADJ | JJ | advcl | stands | 17 |
| 30 | in | in | ADP | IN | prep | visible | 29 |
| 31 | the | the | DET | DT | det | background | 32 |
| 32 | background | background | NOUN | NN | pobj | in | 30 |
| 33 | . | . | PUNCT | . | punct | stands | 17 |
| 34 | A | a | DET | DT | det | person | 35 |
| 35 | person | person | NOUN | NN | nsubjpass | seen | 42 |
| 36 | in | in | ADP | IN | prep | person | 35 |
| 37 | a | a | DET | DT | det | vest | 39 |
| 38 | green | green | ADJ | JJ | amod | vest | 39 |
| 39 | vest | vest | NOUN | NN | pobj | in | 36 |
| 40 | is | be | AUX | VBZ | auxpass | seen | 42 |
| 41 | partially | partially | ADV | RB | advmod | seen | 42 |
| 42 | seen | see | VERB | VBN | ROOT | seen | 42 |
| 43 | to | to | ADP | IN | prep | seen | 42 |
| 44 | his | his | PRON | PRP$ | poss | left | 45 |
| 45 | left | left | NOUN | NN | pobj | to | 43 |
| 46 | . | . | PUNCT | . | punct | seen | 42 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | hair | hair | chunk1 | 4 | noun_chunk_root | high |
| m2 | attribute | gray | gray | chunk1 | 3 | color_attribute | high |
| m3 | object | microphone | microphone | chunk2 | 8 | noun_chunk_root | high |
| m4 | object | shirt | shirt | chunk3 | 14 | noun_chunk_root | high |
| m5 | attribute | blue | blue | chunk3 | 12 | color_attribute | high |
| m6 | attribute | patterned | patterned | chunk3 | 13 | modifier_attribute | medium |
| m7 | object | structure | structure | chunk5 | 23 | noun_chunk_root | high |
| m8 | attribute | large | large | chunk5 | 21 | size_attribute | high |
| m9 | attribute | white | white | chunk5 | 22 | color_attribute | high |
| m10 | object | buildings | building | chunk6 | 26 | noun_chunk_root | high |
| m11 | object | trees | tree | chunk7 | 28 | noun_chunk_root | high |
| m12 | context | background | background | chunk8 | 32 | scene_context | high |
| m13 | object | person | person | chunk9 | 35 | noun_chunk_root | high |
| m14 | object | vest | vest | chunk10 | 39 | noun_chunk_root | high |
| m15 | attribute | green | green | chunk10 | 38 | color_attribute | high |
| m16 | context | left | left | chunk11 | 45 | spatial_region | medium |
| m17 | context | outdoors | outdoors | doc | 18 | scene_context | high |
| m18 | action | speaks | speak | doc | 5 | verb_predicate | high |
| m19 | action | wearing | wear | doc | 10 | verb_predicate | high |
| m20 | action | stands | stand | doc | 17 | verb_predicate | high |
| m21 | action | seen | see | doc | 42 | verb_predicate | high |

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

## 54

**caption_shape:** `multi-sentence`
**caption_id:** `2382247db8d0f0d04bf57da902caf01fd96c226a7358f95da81fcb909adcf014`

> A person rides a red motorcycle on a road beside a field. They wear a black helmet and jacket.

### Sentences
| sentence | token_span |
| --- | --- |
| A person rides a red motorcycle on a road beside a field. | 0:13 |
| They wear a black helmet and jacket. | 13:21 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A person | person | person | nsubj | rides | 0:2 |
| a red motorcycle | motorcycle | motorcycle | dobj | rides | 3:6 |
| a road | road | road | pobj | on | 7:9 |
| a field | field | field | pobj | beside | 10:12 |
| They | They | they | nsubj | wear | 13:14 |
| a black helmet | helmet | helmet | dobj | wear | 15:18 |
| jacket | jacket | jacket | conj | helmet | 19:20 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | person | 1 |
| 1 | person | person | NOUN | NN | nsubj | rides | 2 |
| 2 | rides | rid | VERB | VBZ | ROOT | rides | 2 |
| 3 | a | a | DET | DT | det | motorcycle | 5 |
| 4 | red | red | ADJ | JJ | amod | motorcycle | 5 |
| 5 | motorcycle | motorcycle | NOUN | NN | dobj | rides | 2 |
| 6 | on | on | ADP | IN | prep | rides | 2 |
| 7 | a | a | DET | DT | det | road | 8 |
| 8 | road | road | NOUN | NN | pobj | on | 6 |
| 9 | beside | beside | ADP | IN | prep | road | 8 |
| 10 | a | a | DET | DT | det | field | 11 |
| 11 | field | field | NOUN | NN | pobj | beside | 9 |
| 12 | . | . | PUNCT | . | punct | rides | 2 |
| 13 | They | they | PRON | PRP | nsubj | wear | 14 |
| 14 | wear | wear | VERB | VBP | ROOT | wear | 14 |
| 15 | a | a | DET | DT | det | helmet | 17 |
| 16 | black | black | ADJ | JJ | amod | helmet | 17 |
| 17 | helmet | helmet | NOUN | NN | dobj | wear | 14 |
| 18 | and | and | CCONJ | CC | cc | helmet | 17 |
| 19 | jacket | jacket | NOUN | NN | conj | helmet | 17 |
| 20 | . | . | PUNCT | . | punct | wear | 14 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | motorcycle | motorcycle | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | red | red | chunk1 | 4 | color_attribute | high |
| m3 | object | road | road | chunk2 | 8 | noun_chunk_root | high |
| m4 | object | field | field | chunk3 | 11 | noun_chunk_root | high |
| m5 | object | helmet | helmet | chunk5 | 17 | noun_chunk_root | high |
| m6 | attribute | black | black | chunk5 | 16 | color_attribute | high |
| m7 | object | jacket | jacket | chunk6 | 19 | noun_chunk_root | high |
| m8 | action | rides | rid | doc | 2 | verb_predicate | high |
| m9 | action | wear | wear | doc | 14 | verb_predicate | high |

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

## 55

**caption_shape:** `sentence-like`
**caption_id:** `23ff5ece4644748c87739562585deccd29314becc568b42b37327d09bec93c14`

> A young alpaca with long neck and fluffy white fur looks directly at the camera.

### Sentences
| sentence | token_span |
| --- | --- |
| A young alpaca with long neck and fluffy white fur looks directly at the camera. | 0:16 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A young alpaca | alpaca | alpaca | nsubj | looks | 0:3 |
| long neck | neck | neck | pobj | with | 4:6 |
| fluffy white fur | fur | fur | conj | neck | 7:10 |
| the camera | camera | camera | pobj | at | 13:15 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | alpaca | 2 |
| 1 | young | young | ADJ | JJ | amod | alpaca | 2 |
| 2 | alpaca | alpaca | NOUN | NN | nsubj | looks | 10 |
| 3 | with | with | ADP | IN | prep | alpaca | 2 |
| 4 | long | long | ADJ | JJ | amod | neck | 5 |
| 5 | neck | neck | NOUN | NN | pobj | with | 3 |
| 6 | and | and | CCONJ | CC | cc | neck | 5 |
| 7 | fluffy | fluffy | ADJ | JJ | amod | fur | 9 |
| 8 | white | white | ADJ | JJ | amod | fur | 9 |
| 9 | fur | fur | NOUN | NN | conj | neck | 5 |
| 10 | looks | look | VERB | VBZ | ROOT | looks | 10 |
| 11 | directly | directly | ADV | RB | advmod | looks | 10 |
| 12 | at | at | ADP | IN | prep | looks | 10 |
| 13 | the | the | DET | DT | det | camera | 14 |
| 14 | camera | camera | NOUN | NN | pobj | at | 12 |
| 15 | . | . | PUNCT | . | punct | looks | 10 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | alpaca | alpaca | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | young | young | chunk0 | 1 | modifier_attribute | medium |
| m2 | object | neck | neck | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | long | long | chunk1 | 4 | size_attribute | high |
| m4 | object | fur | fur | chunk2 | 9 | noun_chunk_root | high |
| m5 | attribute | fluffy | fluffy | chunk2 | 7 | modifier_attribute | medium |
| m6 | attribute | white | white | chunk2 | 8 | color_attribute | high |
| m7 | object | camera | camera | chunk3 | 14 | noun_chunk_root | high |
| m8 | action | looks | look | doc | 10 | verb_predicate | high |

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

## 56

**caption_shape:** `sentence-like`
**caption_id:** `255de17e3c6b90c0e792442b32720e2cf575b2e3176e55fc0418e266884d7414`

> A person hangs mid-air from ropes inside a large indoor facility with white walls and a high ceiling.

### Sentences
| sentence | token_span |
| --- | --- |
| A person hangs mid-air from ropes inside a large indoor facility with white walls and a high ceiling. | 0:19 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A person | person | person | nsubj | hangs | 0:2 |
| mid-air | mid-air | mid-air | dobj | hangs | 3:4 |
| ropes | ropes | rope | pobj | from | 5:6 |
| a large indoor facility | facility | facility | pobj | inside | 7:11 |
| white walls | walls | wall | pobj | with | 12:14 |
| a high ceiling | ceiling | ceiling | conj | walls | 15:18 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | person | 1 |
| 1 | person | person | NOUN | NN | nsubj | hangs | 2 |
| 2 | hangs | hang | VERB | VBZ | ROOT | hangs | 2 |
| 3 | mid-air | mid-air | NOUN | NN | dobj | hangs | 2 |
| 4 | from | from | ADP | IN | prep | hangs | 2 |
| 5 | ropes | rope | NOUN | NNS | pobj | from | 4 |
| 6 | inside | inside | ADP | IN | prep | hangs | 2 |
| 7 | a | a | DET | DT | det | facility | 10 |
| 8 | large | large | ADJ | JJ | amod | facility | 10 |
| 9 | indoor | indoor | ADJ | JJ | amod | facility | 10 |
| 10 | facility | facility | NOUN | NN | pobj | inside | 6 |
| 11 | with | with | ADP | IN | prep | facility | 10 |
| 12 | white | white | ADJ | JJ | amod | walls | 13 |
| 13 | walls | wall | NOUN | NNS | pobj | with | 11 |
| 14 | and | and | CCONJ | CC | cc | walls | 13 |
| 15 | a | a | DET | DT | det | ceiling | 17 |
| 16 | high | high | ADJ | JJ | amod | ceiling | 17 |
| 17 | ceiling | ceiling | NOUN | NN | conj | walls | 13 |
| 18 | . | . | PUNCT | . | punct | hangs | 2 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | mid-air | mid-air | chunk1 | 3 | noun_chunk_root | high |
| m2 | object | ropes | rope | chunk2 | 5 | noun_chunk_root | high |
| m3 | object | facility | facility | chunk3 | 10 | noun_chunk_root | high |
| m4 | attribute | large | large | chunk3 | 8 | size_attribute | high |
| m5 | attribute | indoor | indoor | chunk3 | 9 | modifier_attribute | medium |
| m6 | object | walls | wall | chunk4 | 13 | noun_chunk_root | high |
| m7 | attribute | white | white | chunk4 | 12 | color_attribute | high |
| m8 | object | ceiling | ceiling | chunk5 | 17 | noun_chunk_root | high |
| m9 | attribute | high | high | chunk5 | 16 | modifier_attribute | medium |
| m10 | action | hangs | hang | doc | 2 | verb_predicate | high |

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

## 57

**caption_shape:** `multi-sentence`
**caption_id:** `26107b4d1da8a1acacc9ef8c65bf8585743ac92978974539ddaeaa9f873f8414`

> A soccer player in a red jersey controls the ball while being challenged by opponents on a green field. Spectators fill the stands behind them.

### Sentences
| sentence | token_span |
| --- | --- |
| A soccer player in a red jersey controls the ball while being challenged by opponents on a green field. | 0:19 |
| Spectators fill the stands behind them. | 19:26 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A soccer player | soccer player | soccer_player | nsubj | controls | 0:2 |
| a red jersey | jersey | jersey | pobj | in | 3:6 |
| the ball | ball | ball | dobj | controls | 7:9 |
| opponents | opponents | opponent | pobj | by | 13:14 |
| a green field | field | field | pobj | on | 15:18 |
| Spectators | Spectators | spectator | nsubj | fill | 19:20 |
| the stands | stands | stand | dobj | fill | 21:23 |
| them | them | they | pobj | behind | 24:25 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | soccer player | 1 |
| 1 | soccer player | soccer_player | NOUN | NN | nsubj | controls | 6 |
| 2 | in | in | ADP | IN | prep | soccer player | 1 |
| 3 | a | a | DET | DT | det | jersey | 5 |
| 4 | red | red | ADJ | JJ | amod | jersey | 5 |
| 5 | jersey | jersey | NOUN | NN | pobj | in | 2 |
| 6 | controls | control | VERB | VBZ | ROOT | controls | 6 |
| 7 | the | the | DET | DT | det | ball | 8 |
| 8 | ball | ball | NOUN | NN | dobj | controls | 6 |
| 9 | while | while | SCONJ | IN | mark | challenged | 11 |
| 10 | being | be | AUX | VBG | auxpass | challenged | 11 |
| 11 | challenged | challenge | VERB | VBN | advcl | controls | 6 |
| 12 | by | by | ADP | IN | agent | challenged | 11 |
| 13 | opponents | opponent | NOUN | NNS | pobj | by | 12 |
| 14 | on | on | ADP | IN | prep | challenged | 11 |
| 15 | a | a | DET | DT | det | field | 17 |
| 16 | green | green | ADJ | JJ | amod | field | 17 |
| 17 | field | field | NOUN | NN | pobj | on | 14 |
| 18 | . | . | PUNCT | . | punct | controls | 6 |
| 19 | Spectators | spectator | NOUN | NNS | nsubj | fill | 20 |
| 20 | fill | fill | VERB | VBP | ROOT | fill | 20 |
| 21 | the | the | DET | DT | det | stands | 22 |
| 22 | stands | stand | NOUN | NNS | dobj | fill | 20 |
| 23 | behind | behind | ADP | IN | prep | stands | 22 |
| 24 | them | they | PRON | PRP | pobj | behind | 23 |
| 25 | . | . | PUNCT | . | punct | fill | 20 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | soccer player | soccer_player | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | jersey | jersey | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | red | red | chunk1 | 4 | color_attribute | high |
| m3 | object | ball | ball | chunk2 | 8 | noun_chunk_root | high |
| m4 | object | opponents | opponent | chunk3 | 13 | noun_chunk_root | high |
| m5 | object | field | field | chunk4 | 17 | noun_chunk_root | high |
| m6 | attribute | green | green | chunk4 | 16 | color_attribute | high |
| m7 | object | Spectators | spectator | chunk5 | 19 | noun_chunk_root | high |
| m8 | object | stands | stand | chunk6 | 22 | noun_chunk_root | high |
| m9 | action | controls | control | doc | 6 | verb_predicate | high |
| m10 | action | challenged | challenge | doc | 11 | verb_predicate | high |
| m11 | action | fill | fill | doc | 20 | verb_predicate | high |

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

## 58

**caption_shape:** `sentence-like`
**caption_id:** `26b99eb0823d368a743bcbdbd61e2f41774123487d9d219593d62a9136239414`

> A person in a white shirt and apron walks away from a group of people in a restaurant.

### Sentences
| sentence | token_span |
| --- | --- |
| A person in a white shirt and apron walks away from a group of people in a restaurant. | 0:19 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A person | person | person | nsubj | walks | 0:2 |
| a white shirt | shirt | shirt | pobj | in | 3:6 |
| apron | apron | apron | conj | shirt | 7:8 |
| a group | group | group | pobj | from | 11:13 |
| people | people | people | pobj | of | 14:15 |
| a restaurant | restaurant | restaurant | pobj | in | 16:18 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | person | 1 |
| 1 | person | person | NOUN | NN | nsubj | walks | 8 |
| 2 | in | in | ADP | IN | prep | person | 1 |
| 3 | a | a | DET | DT | det | shirt | 5 |
| 4 | white | white | ADJ | JJ | amod | shirt | 5 |
| 5 | shirt | shirt | NOUN | NN | pobj | in | 2 |
| 6 | and | and | CCONJ | CC | cc | shirt | 5 |
| 7 | apron | apron | NOUN | NN | conj | shirt | 5 |
| 8 | walks | walk | VERB | VBZ | ROOT | walks | 8 |
| 9 | away | away | ADV | RB | advmod | walks | 8 |
| 10 | from | from | ADP | IN | prep | away | 9 |
| 11 | a | a | DET | DT | det | group | 12 |
| 12 | group | group | NOUN | NN | pobj | from | 10 |
| 13 | of | of | ADP | IN | prep | group | 12 |
| 14 | people | people | NOUN | NNS | pobj | of | 13 |
| 15 | in | in | ADP | IN | prep | group | 12 |
| 16 | a | a | DET | DT | det | restaurant | 17 |
| 17 | restaurant | restaurant | NOUN | NN | pobj | in | 15 |
| 18 | . | . | PUNCT | . | punct | walks | 8 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | shirt | shirt | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | white | white | chunk1 | 4 | color_attribute | high |
| m3 | object | apron | apron | chunk2 | 7 | noun_chunk_root | high |
| m4 | object | group | group | chunk3 | 12 | noun_chunk_root | high |
| m5 | object | people | people | chunk4 | 14 | noun_chunk_root | high |
| m6 | object | restaurant | restaurant | chunk5 | 17 | noun_chunk_root | high |
| m7 | action | walks | walk | doc | 8 | verb_predicate | high |

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

## 59

**caption_shape:** `multi-sentence`
**caption_id:** `28159d2f1eb69798cdc14f4de25ac7aeea229acf6a1a253bef728896c3861014`

> A row of historic buildings with green shutters lines a cobblestone street. Several cars are parked along the curb, including a white SUV on the left and a silver sedan next to it. The scene is set under an overcast sky with trees visible in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| A row of historic buildings with green shutters lines a cobblestone street. | 0:13 |
| Several cars are parked along the curb, including a white SUV on the left and a silver sedan next to it. | 13:36 |
| The scene is set under an overcast sky with trees visible in the background. | 36:51 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A row | row | row | nsubj | lines | 0:2 |
| historic buildings | buildings | building | pobj | of | 3:5 |
| green shutters | shutters | shutter | pobj | with | 6:8 |
| a cobblestone street | street | street | dobj | lines | 9:12 |
| Several cars | cars | car | nsubjpass | parked | 13:15 |
| the curb | curb | curb | pobj | along | 18:20 |
| a white SUV | SUV | suv | pobj | including | 22:25 |
| the left | left | left | pobj | on | 26:28 |
| a silver sedan | sedan | sedan | conj | SUV | 29:32 |
| it | it | it | pobj | to | 34:35 |
| The scene | scene | scene | nsubjpass | set | 36:38 |
| an overcast sky | sky | sky | pobj | under | 41:44 |
| trees | trees | tree | nsubj | visible | 45:46 |
| the background | background | background | pobj | in | 48:50 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | row | 1 |
| 1 | row | row | NOUN | NN | nsubj | lines | 8 |
| 2 | of | of | ADP | IN | prep | row | 1 |
| 3 | historic | historic | ADJ | JJ | amod | buildings | 4 |
| 4 | buildings | building | NOUN | NNS | pobj | of | 2 |
| 5 | with | with | ADP | IN | prep | buildings | 4 |
| 6 | green | green | ADJ | JJ | amod | shutters | 7 |
| 7 | shutters | shutter | NOUN | NNS | pobj | with | 5 |
| 8 | lines | line | VERB | VBZ | ROOT | lines | 8 |
| 9 | a | a | DET | DT | det | street | 11 |
| 10 | cobblestone | cobblestone | NOUN | NN | amod | street | 11 |
| 11 | street | street | NOUN | NN | dobj | lines | 8 |
| 12 | . | . | PUNCT | . | punct | lines | 8 |
| 13 | Several | several | ADJ | JJ | amod | cars | 14 |
| 14 | cars | car | NOUN | NNS | nsubjpass | parked | 16 |
| 15 | are | be | AUX | VBP | auxpass | parked | 16 |
| 16 | parked | park | VERB | VBN | ROOT | parked | 16 |
| 17 | along | along | ADP | IN | prep | parked | 16 |
| 18 | the | the | DET | DT | det | curb | 19 |
| 19 | curb | curb | NOUN | NN | pobj | along | 17 |
| 20 | , | , | PUNCT | , | punct | parked | 16 |
| 21 | including | include | VERB | VBG | prep | cars | 14 |
| 22 | a | a | DET | DT | det | SUV | 24 |
| 23 | white | white | ADJ | JJ | amod | SUV | 24 |
| 24 | SUV | suv | NOUN | NN | pobj | including | 21 |
| 25 | on | on | ADP | IN | prep | SUV | 24 |
| 26 | the | the | DET | DT | det | left | 27 |
| 27 | left | left | NOUN | NN | pobj | on | 25 |
| 28 | and | and | CCONJ | CC | cc | SUV | 24 |
| 29 | a | a | DET | DT | det | sedan | 31 |
| 30 | silver | silver | ADJ | JJ | amod | sedan | 31 |
| 31 | sedan | sedan | NOUN | NN | conj | SUV | 24 |
| 32 | next | next | ADV | RB | advmod | sedan | 31 |
| 33 | to | to | ADP | IN | prep | next | 32 |
| 34 | it | it | PRON | PRP | pobj | to | 33 |
| 35 | . | . | PUNCT | . | punct | parked | 16 |
| 36 | The | the | DET | DT | det | scene | 37 |
| 37 | scene | scene | NOUN | NN | nsubjpass | set | 39 |
| 38 | is | be | AUX | VBZ | auxpass | set | 39 |
| 39 | set | set | VERB | VBN | ROOT | set | 39 |
| 40 | under | under | ADP | IN | prep | set | 39 |
| 41 | an | an | DET | DT | det | sky | 43 |
| 42 | overcast | overcast | ADJ | JJ | amod | sky | 43 |
| 43 | sky | sky | NOUN | NN | pobj | under | 40 |
| 44 | with | with | SCONJ | IN | mark | visible | 46 |
| 45 | trees | tree | NOUN | NNS | nsubj | visible | 46 |
| 46 | visible | visible | ADJ | JJ | advcl | set | 39 |
| 47 | in | in | ADP | IN | prep | visible | 46 |
| 48 | the | the | DET | DT | det | background | 49 |
| 49 | background | background | NOUN | NN | pobj | in | 47 |
| 50 | . | . | PUNCT | . | punct | set | 39 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | row | row | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | buildings | building | chunk1 | 4 | noun_chunk_root | high |
| m2 | attribute | historic | historic | chunk1 | 3 | modifier_attribute | medium |
| m3 | object | shutters | shutter | chunk2 | 7 | noun_chunk_root | high |
| m4 | attribute | green | green | chunk2 | 6 | color_attribute | high |
| m5 | object | street | street | chunk3 | 11 | noun_chunk_root | high |
| m6 | attribute | cobblestone | cobblestone | chunk3 | 10 | modifier_attribute | medium |
| m7 | object | cars | car | chunk4 | 14 | noun_chunk_root | high |
| m8 | quantity | Several | several | chunk4 | 13 | approximate_quantity | medium |
| m9 | object | curb | curb | chunk5 | 19 | noun_chunk_root | high |
| m10 | object | SUV | suv | chunk6 | 24 | noun_chunk_root | high |
| m11 | attribute | white | white | chunk6 | 23 | color_attribute | high |
| m12 | context | left | left | chunk7 | 27 | spatial_region | medium |
| m13 | object | sedan | sedan | chunk8 | 31 | noun_chunk_root | high |
| m14 | attribute | silver | silver | chunk8 | 30 | color_attribute | high |
| m15 | object | scene | scene | chunk10 | 37 | noun_chunk_root | high |
| m16 | object | sky | sky | chunk11 | 43 | noun_chunk_root | high |
| m17 | attribute | overcast | overcast | chunk11 | 42 | modifier_attribute | medium |
| m18 | object | trees | tree | chunk12 | 45 | noun_chunk_root | high |
| m19 | context | background | background | chunk13 | 49 | scene_context | high |
| m20 | action | lines | line | doc | 8 | verb_predicate | high |
| m21 | action | parked | park | doc | 16 | verb_predicate | high |
| m22 | action | including | include | doc | 21 | verb_predicate | high |
| m23 | action | set | set | doc | 39 | verb_predicate | high |

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

## 60

**caption_shape:** `multi-sentence`
**caption_id:** `2841a2913036cf5f9c2bdec35c13133be2151c77258abf6f61743512eb8ec814`

> A dark, muddy buffalo grazes on green grass in a field. Another buffalo stands nearby in the background, also on the grassy slope.

### Sentences
| sentence | token_span |
| --- | --- |
| A dark, muddy buffalo grazes on green grass in a field. | 0:13 |
| Another buffalo stands nearby in the background, also on the grassy slope. | 13:27 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A dark, muddy buffalo | buffalo | buffalo | nsubj | grazes | 0:5 |
| green grass | grass | grass | pobj | on | 7:9 |
| a field | field | field | pobj | in | 10:12 |
| Another buffalo | buffalo | buffalo | nsubj | stands | 13:15 |
| the background | background | background | pobj | in | 18:20 |
| the grassy slope | slope | slope | pobj | on | 23:26 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | buffalo | 4 |
| 1 | dark | dark | ADJ | JJ | amod | buffalo | 4 |
| 2 | , | , | PUNCT | , | punct | buffalo | 4 |
| 3 | muddy | muddy | ADJ | JJ | amod | buffalo | 4 |
| 4 | buffalo | buffalo | NOUN | NN | nsubj | grazes | 5 |
| 5 | grazes | graze | VERB | VBZ | ROOT | grazes | 5 |
| 6 | on | on | ADP | IN | prep | grazes | 5 |
| 7 | green | green | ADJ | JJ | amod | grass | 8 |
| 8 | grass | grass | NOUN | NN | pobj | on | 6 |
| 9 | in | in | ADP | IN | prep | grazes | 5 |
| 10 | a | a | DET | DT | det | field | 11 |
| 11 | field | field | NOUN | NN | pobj | in | 9 |
| 12 | . | . | PUNCT | . | punct | grazes | 5 |
| 13 | Another | another | DET | DT | det | buffalo | 14 |
| 14 | buffalo | buffalo | NOUN | NN | nsubj | stands | 15 |
| 15 | stands | stand | VERB | VBZ | ROOT | stands | 15 |
| 16 | nearby | nearby | ADV | RB | advmod | stands | 15 |
| 17 | in | in | ADP | IN | prep | stands | 15 |
| 18 | the | the | DET | DT | det | background | 19 |
| 19 | background | background | NOUN | NN | pobj | in | 17 |
| 20 | , | , | PUNCT | , | punct | stands | 15 |
| 21 | also | also | ADV | RB | advmod | on | 22 |
| 22 | on | on | ADP | IN | prep | stands | 15 |
| 23 | the | the | DET | DT | det | slope | 25 |
| 24 | grassy | grassy | ADJ | JJ | amod | slope | 25 |
| 25 | slope | slope | NOUN | NN | pobj | on | 22 |
| 26 | . | . | PUNCT | . | punct | stands | 15 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | buffalo | buffalo | chunk0 | 4 | noun_chunk_root | high |
| m1 | attribute | dark | dark | chunk0 | 1 | visual_attribute | medium |
| m2 | attribute | muddy | muddy | chunk0 | 3 | modifier_attribute | medium |
| m3 | object | grass | grass | chunk1 | 8 | noun_chunk_root | high |
| m4 | attribute | green | green | chunk1 | 7 | color_attribute | high |
| m5 | object | field | field | chunk2 | 11 | noun_chunk_root | high |
| m6 | object | buffalo | buffalo | chunk3 | 14 | noun_chunk_root | high |
| m7 | context | background | background | chunk4 | 19 | scene_context | high |
| m8 | object | slope | slope | chunk5 | 25 | noun_chunk_root | high |
| m9 | attribute | grassy | grassy | chunk5 | 24 | modifier_attribute | medium |
| m10 | action | grazes | graze | doc | 5 | verb_predicate | high |
| m11 | action | stands | stand | doc | 15 | verb_predicate | high |

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

## 61

**caption_shape:** `multi-sentence`
**caption_id:** `2c1a3df2e080b489aabe477866e6631bf79ca8c0ba02181926c37675f98fec14`

> A black hearing aid rests next to a white charging case on a light surface. The device has a curved shape and a small button, while the case has a round base with a white cable extending from it.

### Sentences
| sentence | token_span |
| --- | --- |
| A black hearing aid rests next to a white charging case on a light surface. | 0:15 |
| The device has a curved shape and a small button, while the case has a round base with a white cable extending from it. | 15:41 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A black hearing aid | hearing aid | hearing_aid | nsubj | rests | 0:3 |
| a white charging case | case | case | pobj | to | 6:10 |
| a light surface | surface | surface | pobj | on | 11:14 |
| The device | device | device | nsubj | has | 15:17 |
| a curved shape | shape | shape | dobj | has | 18:21 |
| a small button | button | button | conj | shape | 22:25 |
| the case | case | case | nsubj | has | 27:29 |
| a round base | base | base | dobj | has | 30:33 |
| a white cable | cable | cable | pobj | with | 34:37 |
| it | it | it | pobj | from | 39:40 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | hearing aid | 2 |
| 1 | black | black | ADJ | JJ | amod | hearing aid | 2 |
| 2 | hearing aid | hearing_aid | NOUN | NN | nsubj | rests | 3 |
| 3 | rests | rest | VERB | VBZ | ROOT | rests | 3 |
| 4 | next | next | ADV | RB | advmod | rests | 3 |
| 5 | to | to | ADP | IN | prep | next | 4 |
| 6 | a | a | DET | DT | det | case | 9 |
| 7 | white | white | ADJ | JJ | amod | case | 9 |
| 8 | charging | charging | NOUN | NN | compound | case | 9 |
| 9 | case | case | NOUN | NN | pobj | to | 5 |
| 10 | on | on | ADP | IN | prep | rests | 3 |
| 11 | a | a | DET | DT | det | surface | 13 |
| 12 | light | light | ADJ | JJ | amod | surface | 13 |
| 13 | surface | surface | NOUN | NN | pobj | on | 10 |
| 14 | . | . | PUNCT | . | punct | rests | 3 |
| 15 | The | the | DET | DT | det | device | 16 |
| 16 | device | device | NOUN | NN | nsubj | has | 17 |
| 17 | has | have | VERB | VBZ | ROOT | has | 17 |
| 18 | a | a | DET | DT | det | shape | 20 |
| 19 | curved | curved | ADJ | JJ | amod | shape | 20 |
| 20 | shape | shape | NOUN | NN | dobj | has | 17 |
| 21 | and | and | CCONJ | CC | cc | shape | 20 |
| 22 | a | a | DET | DT | det | button | 24 |
| 23 | small | small | ADJ | JJ | amod | button | 24 |
| 24 | button | button | NOUN | NN | conj | shape | 20 |
| 25 | , | , | PUNCT | , | punct | has | 17 |
| 26 | while | while | SCONJ | IN | mark | has | 29 |
| 27 | the | the | DET | DT | det | case | 28 |
| 28 | case | case | NOUN | NN | nsubj | has | 29 |
| 29 | has | have | VERB | VBZ | advcl | has | 17 |
| 30 | a | a | DET | DT | det | base | 32 |
| 31 | round | round | ADJ | JJ | amod | base | 32 |
| 32 | base | base | NOUN | NN | dobj | has | 29 |
| 33 | with | with | ADP | IN | prep | base | 32 |
| 34 | a | a | DET | DT | det | cable | 36 |
| 35 | white | white | ADJ | JJ | amod | cable | 36 |
| 36 | cable | cable | NOUN | NN | pobj | with | 33 |
| 37 | extending | extend | VERB | VBG | acl | cable | 36 |
| 38 | from | from | ADP | IN | prep | extending | 37 |
| 39 | it | it | PRON | PRP | pobj | from | 38 |
| 40 | . | . | PUNCT | . | punct | has | 17 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hearing aid | hearing_aid | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | black | black | chunk0 | 1 | color_attribute | high |
| m2 | object | case | case | chunk1 | 9 | noun_chunk_root | high |
| m3 | attribute | white | white | chunk1 | 7 | color_attribute | high |
| m4 | attribute | charging | charging | chunk1 | 8 | compound_modifier | medium |
| m5 | context | surface | surface | chunk2 | 13 | spatial_region | medium |
| m6 | object | device | device | chunk3 | 16 | noun_chunk_root | high |
| m7 | object | shape | shape | chunk4 | 20 | noun_chunk_root | high |
| m8 | attribute | curved | curved | chunk4 | 19 | modifier_attribute | medium |
| m9 | object | button | button | chunk5 | 24 | noun_chunk_root | high |
| m10 | attribute | small | small | chunk5 | 23 | size_attribute | high |
| m11 | object | case | case | chunk6 | 28 | noun_chunk_root | high |
| m12 | object | base | base | chunk7 | 32 | noun_chunk_root | high |
| m13 | attribute | round | round | chunk7 | 31 | modifier_attribute | medium |
| m14 | object | cable | cable | chunk8 | 36 | noun_chunk_root | high |
| m15 | attribute | white | white | chunk8 | 35 | color_attribute | high |
| m16 | action | rests | rest | doc | 3 | verb_predicate | high |
| m17 | action | has | have | doc | 17 | verb_predicate | high |
| m18 | action | has | have | doc | 29 | verb_predicate | high |
| m19 | action | extending | extend | doc | 37 | verb_predicate | high |

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

## 62

**caption_shape:** `tag-list-like`
**caption_id:** `2c8d57f87a2faffdb49a205924b495b56874aeaf4b3b8a8a7f1d90d53f3e3414`

> mountain, trees, sky, car, clouds

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | mountain | mountain | 0:8 |
| t1 | trees | trees | 10:15 |
| t2 | sky | sky | 17:20 |
| t3 | car | car | 22:25 |
| t4 | clouds | clouds | 27:33 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | mountain | mountain | mountain | ROOT | mountain | 0:1 | 0:8 |
| t1 | trees | trees | tree | ROOT | trees | 0:1 | 10:15 |
| t2 | sky | sky | sky | ROOT | sky | 0:1 | 17:20 |
| t3 | car | car | car | ROOT | car | 0:1 | 22:25 |
| t4 | clouds | clouds | cloud | ROOT | clouds | 0:1 | 27:33 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | mountain | mountain | NOUN | NOUN | NN | NN | ROOT | mountain | 0 | 0:8 |
| t1 | 0 | trees | tree | NOUN | NOUN | NNS | NNS | ROOT | trees | 0 | 10:15 |
| t2 | 0 | sky | sky | NOUN | NOUN | NN | NN | ROOT | sky | 0 | 17:20 |
| t3 | 0 | car | car | NOUN | NOUN | NN | NN | ROOT | car | 0 | 22:25 |
| t4 | 0 | clouds | cloud | NOUN | NOUN | NNS | NNS | ROOT | clouds | 0 | 27:33 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | mountain | mountain | t0 | 0 | segment_head | high |
| m1 | object | trees | tree | t1 | 0 | segment_head | high |
| m2 | object | sky | sky | t2 | 0 | segment_head | high |
| m3 | object | car | car | t3 | 0 | segment_head | high |
| m4 | object | clouds | cloud | t4 | 0 | segment_head | high |

### Edges
_none_

## 63

**caption_shape:** `multi-sentence`
**caption_id:** `2dc7c048d8f8187055314d252e2703a3d3f89662b051b5f1c840127f22f42414`

> Three race cars speed along a curved track, with a red car in the foreground and two others behind it. Orange cones mark the edge of the track, surrounded by grass and trees in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| Three race cars speed along a curved track, with a red car in the foreground and two others behind it. | 0:21 |
| Orange cones mark the edge of the track, surrounded by grass and trees in the background. | 21:39 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| race cars | race cars | race_car | nsubj | speed | 1:2 |
| a curved track | track | track | pobj | along | 4:7 |
| a red car | car | car | pobj | with | 9:12 |
| the foreground | foreground | foreground | pobj | in | 13:15 |
| two others | others | other | conj | car | 16:18 |
| it | it | it | pobj | behind | 19:20 |
| Orange cones | cones | cone | nsubj | mark | 21:23 |
| the edge | edge | edge | dobj | mark | 24:26 |
| the track | track | track | pobj | of | 27:29 |
| grass | grass | grass | pobj | by | 32:33 |
| trees | trees | tree | conj | grass | 34:35 |
| the background | background | background | pobj | in | 36:38 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Three | three | NUM | CD | nummod | speed | 2 |
| 1 | race cars | race_car | NOUN | NN | nsubj | speed | 2 |
| 2 | speed | speed | VERB | VBP | ROOT | speed | 2 |
| 3 | along | along | ADP | IN | prep | speed | 2 |
| 4 | a | a | DET | DT | det | track | 6 |
| 5 | curved | curved | ADJ | JJ | amod | track | 6 |
| 6 | track | track | NOUN | NN | pobj | along | 3 |
| 7 | , | , | PUNCT | , | punct | speed | 2 |
| 8 | with | with | ADP | IN | prep | speed | 2 |
| 9 | a | a | DET | DT | det | car | 11 |
| 10 | red | red | ADJ | JJ | amod | car | 11 |
| 11 | car | car | NOUN | NN | pobj | with | 8 |
| 12 | in | in | ADP | IN | prep | car | 11 |
| 13 | the | the | DET | DT | det | foreground | 14 |
| 14 | foreground | foreground | NOUN | NN | pobj | in | 12 |
| 15 | and | and | CCONJ | CC | cc | car | 11 |
| 16 | two | two | NUM | CD | nummod | others | 17 |
| 17 | others | other | NOUN | NNS | conj | car | 11 |
| 18 | behind | behind | ADP | IN | prep | others | 17 |
| 19 | it | it | PRON | PRP | pobj | behind | 18 |
| 20 | . | . | PUNCT | . | punct | speed | 2 |
| 21 | Orange | orange | NOUN | NN | compound | cones | 22 |
| 22 | cones | cone | NOUN | NNS | nsubj | mark | 23 |
| 23 | mark | mark | VERB | VBP | ROOT | mark | 23 |
| 24 | the | the | DET | DT | det | edge | 25 |
| 25 | edge | edge | NOUN | NN | dobj | mark | 23 |
| 26 | of | of | ADP | IN | prep | edge | 25 |
| 27 | the | the | DET | DT | det | track | 28 |
| 28 | track | track | NOUN | NN | pobj | of | 26 |
| 29 | , | , | PUNCT | , | punct | mark | 23 |
| 30 | surrounded | surround | VERB | VBN | advcl | mark | 23 |
| 31 | by | by | ADP | IN | agent | surrounded | 30 |
| 32 | grass | grass | NOUN | NN | pobj | by | 31 |
| 33 | and | and | CCONJ | CC | cc | grass | 32 |
| 34 | trees | tree | NOUN | NNS | conj | grass | 32 |
| 35 | in | in | ADP | IN | prep | grass | 32 |
| 36 | the | the | DET | DT | det | background | 37 |
| 37 | background | background | NOUN | NN | pobj | in | 35 |
| 38 | . | . | PUNCT | . | punct | mark | 23 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | race cars | race_car | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | track | track | chunk1 | 6 | noun_chunk_root | high |
| m2 | attribute | curved | curved | chunk1 | 5 | modifier_attribute | medium |
| m3 | object | car | car | chunk2 | 11 | noun_chunk_root | high |
| m4 | attribute | red | red | chunk2 | 10 | color_attribute | high |
| m5 | context | foreground | foreground | chunk3 | 14 | scene_context | high |
| m6 | object | cones | cone | chunk6 | 22 | noun_chunk_root | high |
| m7 | attribute | Orange | orange | chunk6 | 21 | color_attribute | high |
| m8 | object | track | track | chunk8 | 28 | noun_chunk_root | high |
| m9 | object | grass | grass | chunk9 | 32 | noun_chunk_root | high |
| m10 | object | trees | tree | chunk10 | 34 | noun_chunk_root | high |
| m11 | context | background | background | chunk11 | 37 | scene_context | high |
| m12 | action | speed | speed | doc | 2 | verb_predicate | high |
| m13 | action | mark | mark | doc | 23 | verb_predicate | high |
| m14 | object | edge | edge | doc | 25 | verb_object | medium |
| m15 | action | surrounded | surround | doc | 30 | verb_predicate | high |

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

## 64

**caption_shape:** `multi-sentence`
**caption_id:** `2e770d74f49aba6dcaec3dd5d64fe6c050f061791bcc10f025024298b09b3414`

> A gallery space displays various small objects on white shelves and pedestals. The walls are illuminated by overhead lights, and a large black woven vase sits on a central pedestal. Several figurines and decorative items are arranged across the shelves in an indoor setting.

### Sentences
| sentence | token_span |
| --- | --- |
| A gallery space displays various small objects on white shelves and pedestals. | 0:13 |
| The walls are illuminated by overhead lights, and a large black woven vase sits on a central pedestal. | 13:33 |
| Several figurines and decorative items are arranged across the shelves in an indoor setting. | 33:48 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A gallery space | space | space | nsubj | displays | 0:3 |
| various small objects | objects | object | dobj | displays | 4:7 |
| white shelves | shelves | shelf | pobj | on | 8:10 |
| pedestals | pedestals | pedestal | conj | shelves | 11:12 |
| The walls | walls | wall | nsubjpass | illuminated | 13:15 |
| overhead lights | lights | light | pobj | by | 18:20 |
| a large black woven vase | vase | vase | nsubj | sits | 22:27 |
| a central pedestal | pedestal | pedestal | pobj | on | 29:32 |
| Several figurines | figurines | figurine | nsubjpass | arranged | 33:35 |
| decorative items | items | item | conj | figurines | 36:38 |
| the shelves | shelves | shelf | pobj | across | 41:43 |
| an indoor setting | setting | setting | pobj | in | 44:47 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | space | 2 |
| 1 | gallery | gallery | NOUN | NN | compound | space | 2 |
| 2 | space | space | NOUN | NN | nsubj | displays | 3 |
| 3 | displays | display | VERB | VBZ | ROOT | displays | 3 |
| 4 | various | various | ADJ | JJ | amod | objects | 6 |
| 5 | small | small | ADJ | JJ | amod | objects | 6 |
| 6 | objects | object | NOUN | NNS | dobj | displays | 3 |
| 7 | on | on | ADP | IN | prep | displays | 3 |
| 8 | white | white | ADJ | JJ | amod | shelves | 9 |
| 9 | shelves | shelf | NOUN | NNS | pobj | on | 7 |
| 10 | and | and | CCONJ | CC | cc | shelves | 9 |
| 11 | pedestals | pedestal | NOUN | NNS | conj | shelves | 9 |
| 12 | . | . | PUNCT | . | punct | displays | 3 |
| 13 | The | the | DET | DT | det | walls | 14 |
| 14 | walls | wall | NOUN | NNS | nsubjpass | illuminated | 16 |
| 15 | are | be | AUX | VBP | auxpass | illuminated | 16 |
| 16 | illuminated | illuminate | VERB | VBN | ROOT | illuminated | 16 |
| 17 | by | by | ADP | IN | agent | illuminated | 16 |
| 18 | overhead | overhead | ADJ | JJ | amod | lights | 19 |
| 19 | lights | light | NOUN | NNS | pobj | by | 17 |
| 20 | , | , | PUNCT | , | punct | illuminated | 16 |
| 21 | and | and | CCONJ | CC | cc | illuminated | 16 |
| 22 | a | a | DET | DT | det | vase | 26 |
| 23 | large | large | ADJ | JJ | amod | vase | 26 |
| 24 | black | black | ADJ | JJ | amod | vase | 26 |
| 25 | woven | weave | VERB | VBN | amod | vase | 26 |
| 26 | vase | vase | NOUN | NN | nsubj | sits | 27 |
| 27 | sits | sit | VERB | VBZ | conj | illuminated | 16 |
| 28 | on | on | ADP | IN | prep | sits | 27 |
| 29 | a | a | DET | DT | det | pedestal | 31 |
| 30 | central | central | ADJ | JJ | amod | pedestal | 31 |
| 31 | pedestal | pedestal | NOUN | NN | pobj | on | 28 |
| 32 | . | . | PUNCT | . | punct | sits | 27 |
| 33 | Several | several | ADJ | JJ | amod | figurines | 34 |
| 34 | figurines | figurine | NOUN | NNS | nsubjpass | arranged | 39 |
| 35 | and | and | CCONJ | CC | cc | figurines | 34 |
| 36 | decorative | decorative | ADJ | JJ | amod | items | 37 |
| 37 | items | item | NOUN | NNS | conj | figurines | 34 |
| 38 | are | be | AUX | VBP | auxpass | arranged | 39 |
| 39 | arranged | arrange | VERB | VBN | ROOT | arranged | 39 |
| 40 | across | across | ADP | IN | prep | arranged | 39 |
| 41 | the | the | DET | DT | det | shelves | 42 |
| 42 | shelves | shelf | NOUN | NNS | pobj | across | 40 |
| 43 | in | in | ADP | IN | prep | arranged | 39 |
| 44 | an | an | DET | DT | det | setting | 46 |
| 45 | indoor | indoor | ADJ | JJ | amod | setting | 46 |
| 46 | setting | setting | NOUN | NN | pobj | in | 43 |
| 47 | . | . | PUNCT | . | punct | arranged | 39 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | space | space | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | gallery | gallery | chunk0 | 1 | compound_modifier | medium |
| m2 | object | objects | object | chunk1 | 6 | noun_chunk_root | high |
| m3 | quantity | various | various | chunk1 | 4 | approximate_quantity | medium |
| m4 | attribute | small | small | chunk1 | 5 | size_attribute | high |
| m5 | object | shelves | shelf | chunk2 | 9 | noun_chunk_root | high |
| m6 | attribute | white | white | chunk2 | 8 | color_attribute | high |
| m7 | object | pedestals | pedestal | chunk3 | 11 | noun_chunk_root | high |
| m8 | object | walls | wall | chunk4 | 14 | noun_chunk_root | high |
| m9 | object | lights | light | chunk5 | 19 | noun_chunk_root | high |
| m10 | attribute | overhead | overhead | chunk5 | 18 | modifier_attribute | medium |
| m11 | object | vase | vase | chunk6 | 26 | noun_chunk_root | high |
| m12 | attribute | large | large | chunk6 | 23 | size_attribute | high |
| m13 | attribute | black | black | chunk6 | 24 | color_attribute | high |
| m14 | attribute | woven | weave | chunk6 | 25 | state_attribute | medium |
| m15 | object | pedestal | pedestal | chunk7 | 31 | noun_chunk_root | high |
| m16 | attribute | central | central | chunk7 | 30 | modifier_attribute | medium |
| m17 | object | figurines | figurine | chunk8 | 34 | noun_chunk_root | high |
| m18 | quantity | Several | several | chunk8 | 33 | approximate_quantity | medium |
| m19 | object | items | item | chunk9 | 37 | noun_chunk_root | high |
| m20 | attribute | decorative | decorative | chunk9 | 36 | modifier_attribute | medium |
| m21 | object | shelves | shelf | chunk10 | 42 | noun_chunk_root | high |
| m22 | context | setting | setting | chunk11 | 46 | scene_context | high |
| m23 | attribute | indoor | indoor | chunk11 | 45 | modifier_attribute | medium |
| m24 | action | displays | display | doc | 3 | verb_predicate | high |
| m25 | action | illuminated | illuminate | doc | 16 | verb_predicate | high |
| m26 | action | sits | sit | doc | 27 | verb_predicate | high |
| m27 | action | arranged | arrange | doc | 39 | verb_predicate | high |

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

## 65

**caption_shape:** `multi-sentence`
**caption_id:** `2ea7e3419477bceca7256393dfb88f8d01c1ef0286b54daac7e1555e4901fc14`

> A man in a white shirt and jeans holds up a framed plaque above his head. Several people around him, some wearing masks, clap and look on under a large tent with “SÃO PAULO” visible on the wall behind.

**parsed_caption:**

> A man in a white shirt and jeans holds up a framed plaque above his head. Several people around him, some wearing masks, clap and look on under a large tent with “SÃO PAULO” visible on the wall behind.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 2ea7e3419477bceca7256393dfb88f8d01c1ef0286b54daac7e1555e4901fc14:q0 | SÃO PAULO | são paulo | raw_quote_span |  | 162:173 | 162:173 |

### Sentences
| sentence | token_span |
| --- | --- |
| A man in a white shirt and jeans holds up a framed plaque above his head. | 0:17 |
| Several people around him, some wearing masks, clap and look on under a large tent with “SÃO PAULO” visible on the wall behind. | 17:42 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A man | man | man | nsubj | holds | 0:2 |
| a white shirt | shirt | shirt | pobj | in | 3:6 |
| jeans | jeans | jean | conj | shirt | 7:8 |
| a framed plaque | plaque | plaque | dobj | holds | 10:13 |
| his head | head | head | pobj | above | 14:16 |
| Several people | people | people | nsubj | clap | 17:19 |
| him | him | he | pobj | around | 20:21 |
| some | some | some | nsubj | wearing | 22:23 |
| masks | masks | mask | dobj | wearing | 24:25 |
| a large tent | tent | tent | pobj | under | 31:34 |
| “SÃO PAULO” | “SÃO PAULO” | são_paulo | nsubj | visible | 35:36 |
| the wall | wall | wall | pobj | on | 38:40 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | man | 1 |
| 1 | man | man | NOUN | NN | nsubj | holds | 8 |
| 2 | in | in | ADP | IN | prep | man | 1 |
| 3 | a | a | DET | DT | det | shirt | 5 |
| 4 | white | white | ADJ | JJ | amod | shirt | 5 |
| 5 | shirt | shirt | NOUN | NN | pobj | in | 2 |
| 6 | and | and | CCONJ | CC | cc | shirt | 5 |
| 7 | jeans | jean | NOUN | NNS | conj | shirt | 5 |
| 8 | holds | hold | VERB | VBZ | ROOT | holds | 8 |
| 9 | up | up | ADP | RP | prt | holds | 8 |
| 10 | a | a | DET | DT | det | plaque | 12 |
| 11 | framed | frame | VERB | VBN | amod | plaque | 12 |
| 12 | plaque | plaque | NOUN | NN | dobj | holds | 8 |
| 13 | above | above | ADP | IN | prep | holds | 8 |
| 14 | his | his | PRON | PRP$ | poss | head | 15 |
| 15 | head | head | NOUN | NN | pobj | above | 13 |
| 16 | . | . | PUNCT | . | punct | holds | 8 |
| 17 | Several | several | ADJ | JJ | amod | people | 18 |
| 18 | people | people | NOUN | NNS | nsubj | clap | 26 |
| 19 | around | around | ADP | IN | prep | people | 18 |
| 20 | him | he | PRON | PRP | pobj | around | 19 |
| 21 | , | , | PUNCT | , | punct | people | 18 |
| 22 | some | some | PRON | DT | nsubj | wearing | 23 |
| 23 | wearing | wear | VERB | VBG | relcl | people | 18 |
| 24 | masks | mask | NOUN | NNS | dobj | wearing | 23 |
| 25 | , | , | PUNCT | , | punct | clap | 26 |
| 26 | clap | clap | VERB | VBP | ROOT | clap | 26 |
| 27 | and | and | CCONJ | CC | cc | clap | 26 |
| 28 | look | look | VERB | VBP | conj | clap | 26 |
| 29 | on | on | ADP | RP | prt | look | 28 |
| 30 | under | under | ADP | IN | prep | look | 28 |
| 31 | a | a | DET | DT | det | tent | 33 |
| 32 | large | large | ADJ | JJ | amod | tent | 33 |
| 33 | tent | tent | NOUN | NN | pobj | under | 30 |
| 34 | with | with | SCONJ | IN | mark | visible | 36 |
| 35 | “SÃO PAULO” | são_paulo | PROPN | NNP | nsubj | visible | 36 |
| 36 | visible | visible | ADJ | JJ | amod | tent | 33 |
| 37 | on | on | ADP | IN | prep | visible | 36 |
| 38 | the | the | DET | DT | det | wall | 39 |
| 39 | wall | wall | NOUN | NN | pobj | on | 37 |
| 40 | behind | behind | ADV | RB | advmod | wall | 39 |
| 41 | . | . | PUNCT | . | punct | clap | 26 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “SÃO PAULO” | são_paulo | doc_quote | 35 | quote_text | high |
| m1 | object | man | man | chunk0 | 1 | noun_chunk_root | high |
| m2 | object | shirt | shirt | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | white | white | chunk1 | 4 | color_attribute | high |
| m4 | object | jeans | jean | chunk2 | 7 | noun_chunk_root | high |
| m5 | object | plaque | plaque | chunk3 | 12 | noun_chunk_root | high |
| m6 | attribute | framed | frame | chunk3 | 11 | state_attribute | medium |
| m7 | object | head | head | chunk4 | 15 | noun_chunk_root | high |
| m8 | object | people | people | chunk5 | 18 | noun_chunk_root | high |
| m9 | quantity | Several | several | chunk5 | 17 | approximate_quantity | medium |
| m10 | quantity | some | some | chunk7 | 22 | indefinite_quantity | medium |
| m11 | object | masks | mask | chunk8 | 24 | noun_chunk_root | high |
| m12 | object | tent | tent | chunk9 | 33 | noun_chunk_root | high |
| m13 | attribute | large | large | chunk9 | 32 | size_attribute | high |
| m14 | object | wall | wall | chunk11 | 39 | noun_chunk_root | high |
| m15 | action | holds | hold | doc | 8 | verb_predicate | high |
| m16 | action | wearing | wear | doc | 23 | verb_predicate | high |
| m17 | action | clap | clap | doc | 26 | verb_predicate | high |
| m18 | action | look | look | doc | 28 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | chunk1 amod -> shirt |
| e1 | has_attribute | m5 | m6 | medium | chunk3 amod -> plaque |
| e2 | has_quantity | m8 | m9 | medium | chunk5 quantity -> people |
| e3 | has_attribute | m12 | m13 | high | chunk9 amod -> tent |
| e4 | agent | m15 | m1 | medium | nsubj -> holds |
| e5 | patient | m15 | m5 | medium | dobj -> holds |
| e6 | agent | m16 | m8 | medium | inherited agent relcl -> people |
| e7 | patient | m16 | m11 | medium | dobj -> wearing |
| e8 | agent | m17 | m8 | medium | nsubj -> clap |
| e9 | agent | m18 | m8 | medium | inherited agent conj -> clap |
| e10 | relation | m1 | m2 | high | in |
| e11 | relation | m1 | m4 | high | in |
| e12 | relation | m1 | m7 | high | above |
| e13 | relation | m8 | m1 | high | around |
| e14 | relation | m8 | m12 | high | under |

### Skipped Raw Concept Edges
_none_

## 66

**caption_shape:** `multi-sentence`
**caption_id:** `2edad03d414cd9df97abed25e0e65973c277bf42adbb760c0ec6ff029323a814`

> A young child in a white dress stands on an ornate chair. Curtains are visible behind them in the studio setting.

### Sentences
| sentence | token_span |
| --- | --- |
| A young child in a white dress stands on an ornate chair. | 0:13 |
| Curtains are visible behind them in the studio setting. | 13:23 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A young child | child | child | nsubj | stands | 0:3 |
| a white dress | dress | dress | pobj | in | 4:7 |
| an ornate chair | chair | chair | pobj | on | 9:12 |
| Curtains | Curtains | curtain | nsubj | are | 13:14 |
| them | them | they | pobj | behind | 17:18 |
| the studio setting | setting | setting | pobj | in | 19:22 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | child | 2 |
| 1 | young | young | ADJ | JJ | amod | child | 2 |
| 2 | child | child | NOUN | NN | nsubj | stands | 7 |
| 3 | in | in | ADP | IN | prep | child | 2 |
| 4 | a | a | DET | DT | det | dress | 6 |
| 5 | white | white | ADJ | JJ | amod | dress | 6 |
| 6 | dress | dress | NOUN | NN | pobj | in | 3 |
| 7 | stands | stand | VERB | VBZ | ROOT | stands | 7 |
| 8 | on | on | ADP | IN | prep | stands | 7 |
| 9 | an | an | DET | DT | det | chair | 11 |
| 10 | ornate | ornate | ADJ | JJ | amod | chair | 11 |
| 11 | chair | chair | NOUN | NN | pobj | on | 8 |
| 12 | . | . | PUNCT | . | punct | stands | 7 |
| 13 | Curtains | curtain | NOUN | NNS | nsubj | are | 14 |
| 14 | are | be | AUX | VBP | ROOT | are | 14 |
| 15 | visible | visible | ADJ | JJ | acomp | are | 14 |
| 16 | behind | behind | ADP | IN | prep | are | 14 |
| 17 | them | they | PRON | PRP | pobj | behind | 16 |
| 18 | in | in | ADP | IN | prep | are | 14 |
| 19 | the | the | DET | DT | det | setting | 21 |
| 20 | studio | studio | NOUN | NN | compound | setting | 21 |
| 21 | setting | setting | NOUN | NN | pobj | in | 18 |
| 22 | . | . | PUNCT | . | punct | are | 14 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | child | child | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | young | young | chunk0 | 1 | modifier_attribute | medium |
| m2 | object | dress | dress | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | white | white | chunk1 | 5 | color_attribute | high |
| m4 | object | chair | chair | chunk2 | 11 | noun_chunk_root | high |
| m5 | attribute | ornate | ornate | chunk2 | 10 | modifier_attribute | medium |
| m6 | object | Curtains | curtain | chunk3 | 13 | noun_chunk_root | high |
| m7 | context | setting | setting | chunk5 | 21 | scene_context | high |
| m8 | attribute | studio | studio | chunk5 | 20 | compound_modifier | medium |
| m9 | action | stands | stand | doc | 7 | verb_predicate | high |

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

## 67

**caption_shape:** `sentence-like`
**caption_id:** `2f2ce66431e5451a01520b02af91689e6522fad31385be669f56dadb3aede414`

> People walk on a paved path near the Royal Festival Hall building.

### Sentences
| sentence | token_span |
| --- | --- |
| People walk on a paved path near the Royal Festival Hall building. | 0:13 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| People | People | People | nsubj | walk | 0:1 |
| a paved path | path | path | pobj | on | 3:6 |
| the Royal Festival Hall building | building | building | pobj | near | 7:12 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | People | People | NOUN | NNS | nsubj | walk | 1 |
| 1 | walk | walk | VERB | VBP | ROOT | walk | 1 |
| 2 | on | on | ADP | IN | prep | walk | 1 |
| 3 | a | a | DET | DT | det | path | 5 |
| 4 | paved | paved | ADJ | JJ | amod | path | 5 |
| 5 | path | path | NOUN | NN | pobj | on | 2 |
| 6 | near | near | ADP | IN | prep | walk | 1 |
| 7 | the | the | DET | DT | det | building | 11 |
| 8 | Royal | Royal | PROPN | NNP | compound | Hall | 10 |
| 9 | Festival | Festival | PROPN | NNP | compound | Hall | 10 |
| 10 | Hall | Hall | PROPN | NNP | compound | building | 11 |
| 11 | building | building | NOUN | NN | pobj | near | 6 |
| 12 | . | . | PUNCT | . | punct | walk | 1 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | People | people | chunk0 | 0 | noun_chunk_root | high |
| m1 | object | path | path | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | paved | paved | chunk1 | 4 | visual_attribute | medium |
| m3 | object | building | building | chunk2 | 11 | noun_chunk_root | high |
| m4 | attribute | Royal | royal | chunk2 | 8 | compound_modifier | medium |
| m5 | attribute | Festival | festival | chunk2 | 9 | compound_modifier | medium |
| m6 | attribute | Hall | hall | chunk2 | 10 | compound_modifier | medium |
| m7 | action | walk | walk | doc | 1 | verb_predicate | high |

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

## 68

**caption_shape:** `multi-sentence`
**caption_id:** `3156569e74ddc3825ce976fcaee3c3b3785db75d9d7d869ec496d5cb4daa5c14`

> A rugged canyon with steep cliffs and sparse greenery. A small white house sits at the bottom of the valley.

### Sentences
| sentence | token_span |
| --- | --- |
| A rugged canyon with steep cliffs and sparse greenery. | 0:10 |
| A small white house sits at the bottom of the valley. | 10:22 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A rugged canyon | canyon | canyon | ROOT | canyon | 0:3 |
| steep cliffs | cliffs | cliff | pobj | with | 4:6 |
| sparse greenery | greenery | greenery | conj | cliffs | 7:9 |
| A small white house | house | house | nsubj | sits | 10:14 |
| the bottom | bottom | bottom | pobj | at | 16:18 |
| the valley | valley | valley | pobj | of | 19:21 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | canyon | 2 |
| 1 | rugged | rugged | ADJ | JJ | amod | canyon | 2 |
| 2 | canyon | canyon | NOUN | NN | ROOT | canyon | 2 |
| 3 | with | with | ADP | IN | prep | canyon | 2 |
| 4 | steep | steep | ADJ | JJ | amod | cliffs | 5 |
| 5 | cliffs | cliff | NOUN | NNS | pobj | with | 3 |
| 6 | and | and | CCONJ | CC | cc | cliffs | 5 |
| 7 | sparse | sparse | ADJ | JJ | amod | greenery | 8 |
| 8 | greenery | greenery | NOUN | NN | conj | cliffs | 5 |
| 9 | . | . | PUNCT | . | punct | canyon | 2 |
| 10 | A | a | DET | DT | det | house | 13 |
| 11 | small | small | ADJ | JJ | amod | house | 13 |
| 12 | white | white | ADJ | JJ | amod | house | 13 |
| 13 | house | house | NOUN | NN | nsubj | sits | 14 |
| 14 | sits | sit | VERB | VBZ | ROOT | sits | 14 |
| 15 | at | at | ADP | IN | prep | sits | 14 |
| 16 | the | the | DET | DT | det | bottom | 17 |
| 17 | bottom | bottom | NOUN | NN | pobj | at | 15 |
| 18 | of | of | ADP | IN | prep | bottom | 17 |
| 19 | the | the | DET | DT | det | valley | 20 |
| 20 | valley | valley | NOUN | NN | pobj | of | 18 |
| 21 | . | . | PUNCT | . | punct | sits | 14 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | canyon | canyon | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | rugged | rugged | chunk0 | 1 | modifier_attribute | medium |
| m2 | object | cliffs | cliff | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | steep | steep | chunk1 | 4 | modifier_attribute | medium |
| m4 | object | greenery | greenery | chunk2 | 8 | noun_chunk_root | high |
| m5 | attribute | sparse | sparse | chunk2 | 7 | modifier_attribute | medium |
| m6 | object | house | house | chunk3 | 13 | noun_chunk_root | high |
| m7 | attribute | small | small | chunk3 | 11 | size_attribute | high |
| m8 | attribute | white | white | chunk3 | 12 | color_attribute | high |
| m9 | object | valley | valley | chunk5 | 20 | noun_chunk_root | high |
| m10 | action | sits | sit | doc | 14 | verb_predicate | high |

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

## 69

**caption_shape:** `multi-sentence`
**caption_id:** `3302576e9b3fa334f206532a50a7c9f7dcd858f3ea8b2990723b089efcee1c14`

> A phylogenetic tree shows evolutionary relationships among rodents, with icons of a leporid rabbit and an ocotoid rodent. Below, a graph tracks global temperature and vegetation changes over time, marked with key events like C3 grass origin and C4 expansion.

### Sentences
| sentence | token_span |
| --- | --- |
| A phylogenetic tree shows evolutionary relationships among rodents, with icons of a leporid rabbit and an ocotoid rodent. | 0:20 |
| Below, a graph tracks global temperature and vegetation changes over time, marked with key events like C3 grass origin and C4 expansion. | 20:45 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A phylogenetic tree | tree | tree | nsubj | shows | 0:3 |
| evolutionary relationships | relationships | relationship | dobj | shows | 4:6 |
| rodents | rodents | rodent | pobj | among | 7:8 |
| icons | icons | icon | pobj | with | 10:11 |
| a leporid rabbit | rabbit | rabbit | pobj | of | 12:15 |
| an ocotoid rodent | rodent | rodent | conj | rabbit | 16:19 |
| a graph | graph | graph | nsubj | tracks | 22:24 |
| global temperature | temperature | temperature | dobj | tracks | 25:27 |
| vegetation changes | changes | change | conj | temperature | 28:30 |
| time | time | time | pobj | over | 31:32 |
| key events | events | event | pobj | with | 35:37 |
| C3 grass origin | origin | origin | pobj | like | 38:41 |
| C4 expansion | expansion | expansion | conj | origin | 42:44 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | tree | 2 |
| 1 | phylogenetic | phylogenetic | ADJ | JJ | amod | tree | 2 |
| 2 | tree | tree | NOUN | NN | nsubj | shows | 3 |
| 3 | shows | show | VERB | VBZ | ROOT | shows | 3 |
| 4 | evolutionary | evolutionary | ADJ | JJ | amod | relationships | 5 |
| 5 | relationships | relationship | NOUN | NNS | dobj | shows | 3 |
| 6 | among | among | ADP | IN | prep | relationships | 5 |
| 7 | rodents | rodent | NOUN | NNS | pobj | among | 6 |
| 8 | , | , | PUNCT | , | punct | shows | 3 |
| 9 | with | with | ADP | IN | prep | shows | 3 |
| 10 | icons | icon | NOUN | NNS | pobj | with | 9 |
| 11 | of | of | ADP | IN | prep | icons | 10 |
| 12 | a | a | DET | DT | det | rabbit | 14 |
| 13 | leporid | leporid | ADJ | JJ | amod | rabbit | 14 |
| 14 | rabbit | rabbit | NOUN | NN | pobj | of | 11 |
| 15 | and | and | CCONJ | CC | cc | rabbit | 14 |
| 16 | an | an | DET | DT | det | rodent | 18 |
| 17 | ocotoid | ocotoid | NOUN | NN | compound | rodent | 18 |
| 18 | rodent | rodent | NOUN | NN | conj | rabbit | 14 |
| 19 | . | . | PUNCT | . | punct | shows | 3 |
| 20 | Below | below | ADV | RB | advmod | tracks | 24 |
| 21 | , | , | PUNCT | , | punct | tracks | 24 |
| 22 | a | a | DET | DT | det | graph | 23 |
| 23 | graph | graph | NOUN | NN | nsubj | tracks | 24 |
| 24 | tracks | track | VERB | VBZ | ROOT | tracks | 24 |
| 25 | global | global | ADJ | JJ | amod | temperature | 26 |
| 26 | temperature | temperature | NOUN | NN | dobj | tracks | 24 |
| 27 | and | and | CCONJ | CC | cc | temperature | 26 |
| 28 | vegetation | vegetation | NOUN | NN | compound | changes | 29 |
| 29 | changes | change | NOUN | NNS | conj | temperature | 26 |
| 30 | over | over | ADP | IN | prep | temperature | 26 |
| 31 | time | time | NOUN | NN | pobj | over | 30 |
| 32 | , | , | PUNCT | , | punct | tracks | 24 |
| 33 | marked | mark | VERB | VBN | advcl | tracks | 24 |
| 34 | with | with | ADP | IN | prep | marked | 33 |
| 35 | key | key | ADJ | JJ | amod | events | 36 |
| 36 | events | event | NOUN | NNS | pobj | with | 34 |
| 37 | like | like | ADP | IN | prep | events | 36 |
| 38 | C3 | c3 | NOUN | NN | compound | grass | 39 |
| 39 | grass | grass | NOUN | NN | compound | origin | 40 |
| 40 | origin | origin | NOUN | NN | pobj | like | 37 |
| 41 | and | and | CCONJ | CC | cc | origin | 40 |
| 42 | C4 | c4 | NOUN | NN | compound | expansion | 43 |
| 43 | expansion | expansion | NOUN | NN | conj | origin | 40 |
| 44 | . | . | PUNCT | . | punct | tracks | 24 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | tree | tree | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | phylogenetic | phylogenetic | chunk0 | 1 | modifier_attribute | medium |
| m2 | object | relationships | relationship | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | evolutionary | evolutionary | chunk1 | 4 | modifier_attribute | medium |
| m4 | object | rodents | rodent | chunk2 | 7 | noun_chunk_root | high |
| m5 | object | icons | icon | chunk3 | 10 | noun_chunk_root | high |
| m6 | object | rabbit | rabbit | chunk4 | 14 | noun_chunk_root | high |
| m7 | attribute | leporid | leporid | chunk4 | 13 | modifier_attribute | medium |
| m8 | object | rodent | rodent | chunk5 | 18 | noun_chunk_root | high |
| m9 | attribute | ocotoid | ocotoid | chunk5 | 17 | compound_modifier | medium |
| m10 | object | graph | graph | chunk6 | 23 | noun_chunk_root | high |
| m11 | object | temperature | temperature | chunk7 | 26 | noun_chunk_root | high |
| m12 | attribute | global | global | chunk7 | 25 | modifier_attribute | medium |
| m13 | object | changes | change | chunk8 | 29 | noun_chunk_root | high |
| m14 | attribute | vegetation | vegetation | chunk8 | 28 | compound_modifier | medium |
| m15 | object | time | time | chunk9 | 31 | noun_chunk_root | high |
| m16 | object | events | event | chunk10 | 36 | noun_chunk_root | high |
| m17 | attribute | key | key | chunk10 | 35 | modifier_attribute | medium |
| m18 | object | origin | origin | chunk11 | 40 | noun_chunk_root | high |
| m19 | attribute | C3 | c3 | chunk11 | 38 | compound_modifier | medium |
| m20 | attribute | grass | grass | chunk11 | 39 | compound_modifier | medium |
| m21 | object | expansion | expansion | chunk12 | 43 | noun_chunk_root | high |
| m22 | attribute | C4 | c4 | chunk12 | 42 | compound_modifier | medium |
| m23 | action | shows | show | doc | 3 | verb_predicate | high |
| m24 | action | tracks | track | doc | 24 | verb_predicate | high |
| m25 | action | marked | mark | doc | 33 | verb_predicate | high |

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

## 70

**caption_shape:** `sentence-like`
**caption_id:** `33197bd517edd2b2a5fb1c6efdd1b00b2583e2a3ebe9acf2249c6cce3afa3414`

> A man in a blue and gray vest stands next to a woman in a gray corset, both at a party.

### Sentences
| sentence | token_span |
| --- | --- |
| A man in a blue and gray vest stands next to a woman in a gray corset, both at a party. | 0:23 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A man | man | man | nsubj | stands | 0:2 |
| a blue and gray vest | vest | vest | pobj | in | 3:8 |
| a woman | woman | woman | pobj | to | 11:13 |
| a gray corset | corset | corset | pobj | in | 14:17 |
| a party | party | party | pobj | at | 20:22 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | man | 1 |
| 1 | man | man | NOUN | NN | nsubj | stands | 8 |
| 2 | in | in | ADP | IN | prep | man | 1 |
| 3 | a | a | DET | DT | det | vest | 7 |
| 4 | blue | blue | ADJ | JJ | amod | vest | 7 |
| 5 | and | and | CCONJ | CC | cc | blue | 4 |
| 6 | gray | gray | ADJ | JJ | conj | blue | 4 |
| 7 | vest | vest | NOUN | NN | pobj | in | 2 |
| 8 | stands | stand | VERB | VBZ | ROOT | stands | 8 |
| 9 | next | next | ADV | RB | advmod | stands | 8 |
| 10 | to | to | ADP | IN | prep | next | 9 |
| 11 | a | a | DET | DT | det | woman | 12 |
| 12 | woman | woman | NOUN | NN | pobj | to | 10 |
| 13 | in | in | ADP | IN | prep | woman | 12 |
| 14 | a | a | DET | DT | det | corset | 16 |
| 15 | gray | gray | ADJ | JJ | amod | corset | 16 |
| 16 | corset | corset | NOUN | NN | pobj | in | 13 |
| 17 | , | , | PUNCT | , | punct | stands | 8 |
| 18 | both | both | PRON | DT | advcl | stands | 8 |
| 19 | at | at | ADP | IN | prep | both | 18 |
| 20 | a | a | DET | DT | det | party | 21 |
| 21 | party | party | NOUN | NN | pobj | at | 19 |
| 22 | . | . | PUNCT | . | punct | stands | 8 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | vest | vest | chunk1 | 7 | noun_chunk_root | high |
| m2 | attribute | blue | blue | chunk1 | 4 | color_attribute | high |
| m3 | attribute | gray | gray | chunk1 | 6 | color_attribute | high |
| m4 | object | woman | woman | chunk2 | 12 | noun_chunk_root | high |
| m5 | object | corset | corset | chunk3 | 16 | noun_chunk_root | high |
| m6 | attribute | gray | gray | chunk3 | 15 | color_attribute | high |
| m7 | object | party | party | chunk4 | 21 | noun_chunk_root | high |
| m8 | action | stands | stand | doc | 8 | verb_predicate | high |

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

## 71

**caption_shape:** `multi-sentence`
**caption_id:** `331f38a142eb3d5bffb9d33eaec80a194a9f24567abee2b86a20b4258139c414`

> A man in a blue suit and tie stands at a clear podium, waving with his right hand. Behind him is a large white backdrop with the “POLAND25.EU” logo repeated across it. He wears glasses and has a lanyard around his neck.

**parsed_caption:**

> A man in a blue suit and tie stands at a clear podium, waving with his right hand. Behind him is a large white backdrop with the “POLAND25.EU” logo repeated across it. He wears glasses and has a lanyard around his neck.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 331f38a142eb3d5bffb9d33eaec80a194a9f24567abee2b86a20b4258139c414:q0 | POLAND25.EU | poland25.eu | raw_quote_span |  | 129:142 | 129:142 |

### Sentences
| sentence | token_span |
| --- | --- |
| A man in a blue suit and tie stands at a clear podium, waving with his right hand. | 0:19 |
| Behind him is a large white backdrop with the “POLAND25.EU” logo repeated across it. | 19:34 |
| He wears glasses and has a lanyard around his neck. | 34:45 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A man | man | man | nsubj | stands | 0:2 |
| a blue suit | suit | suit | pobj | in | 3:6 |
| tie | tie | tie | conj | suit | 7:8 |
| a clear podium | podium | podium | pobj | at | 10:13 |
| his right hand | right hand | right_hand | pobj | with | 16:18 |
| him | him | he | pobj | Behind | 20:21 |
| a large white backdrop | backdrop | backdrop | nsubj | is | 22:26 |
| the “POLAND25.EU” logo | logo | logo | pobj | with | 27:30 |
| it | it | it | pobj | across | 32:33 |
| He | He | he | nsubj | wears | 34:35 |
| glasses | glasses | glass | dobj | wears | 36:37 |
| a lanyard | lanyard | lanyard | dobj | has | 39:41 |
| his neck | neck | neck | pobj | around | 42:44 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | man | 1 |
| 1 | man | man | NOUN | NN | nsubj | stands | 8 |
| 2 | in | in | ADP | IN | prep | man | 1 |
| 3 | a | a | DET | DT | det | suit | 5 |
| 4 | blue | blue | ADJ | JJ | amod | suit | 5 |
| 5 | suit | suit | NOUN | NN | pobj | in | 2 |
| 6 | and | and | CCONJ | CC | cc | suit | 5 |
| 7 | tie | tie | NOUN | NN | conj | suit | 5 |
| 8 | stands | stand | VERB | VBZ | ROOT | stands | 8 |
| 9 | at | at | ADP | IN | prep | stands | 8 |
| 10 | a | a | DET | DT | det | podium | 12 |
| 11 | clear | clear | ADJ | JJ | amod | podium | 12 |
| 12 | podium | podium | NOUN | NN | pobj | at | 9 |
| 13 | , | , | PUNCT | , | punct | stands | 8 |
| 14 | waving | wave | VERB | VBG | advcl | stands | 8 |
| 15 | with | with | ADP | IN | prep | waving | 14 |
| 16 | his | his | PRON | PRP$ | poss | right hand | 17 |
| 17 | right hand | right_hand | NOUN | NN | pobj | with | 15 |
| 18 | . | . | PUNCT | . | punct | stands | 8 |
| 19 | Behind | behind | ADP | IN | prep | is | 21 |
| 20 | him | he | PRON | PRP | pobj | Behind | 19 |
| 21 | is | be | AUX | VBZ | ROOT | is | 21 |
| 22 | a | a | DET | DT | det | backdrop | 25 |
| 23 | large | large | ADJ | JJ | amod | backdrop | 25 |
| 24 | white | white | ADJ | JJ | amod | backdrop | 25 |
| 25 | backdrop | backdrop | NOUN | NN | nsubj | is | 21 |
| 26 | with | with | ADP | IN | prep | backdrop | 25 |
| 27 | the | the | DET | DT | det | logo | 29 |
| 28 | “POLAND25.EU” | poland25.eu | PROPN | NNP | punct | logo | 29 |
| 29 | logo | logo | NOUN | NN | pobj | with | 26 |
| 30 | repeated | repeat | VERB | VBN | acl | logo | 29 |
| 31 | across | across | ADP | IN | prep | repeated | 30 |
| 32 | it | it | PRON | PRP | pobj | across | 31 |
| 33 | . | . | PUNCT | . | punct | is | 21 |
| 34 | He | he | PRON | PRP | nsubj | wears | 35 |
| 35 | wears | wear | VERB | VBZ | ROOT | wears | 35 |
| 36 | glasses | glass | NOUN | NNS | dobj | wears | 35 |
| 37 | and | and | CCONJ | CC | cc | wears | 35 |
| 38 | has | have | VERB | VBZ | conj | wears | 35 |
| 39 | a | a | DET | DT | det | lanyard | 40 |
| 40 | lanyard | lanyard | NOUN | NN | dobj | has | 38 |
| 41 | around | around | ADP | IN | prep | has | 38 |
| 42 | his | his | PRON | PRP$ | poss | neck | 43 |
| 43 | neck | neck | NOUN | NN | pobj | around | 41 |
| 44 | . | . | PUNCT | . | punct | wears | 35 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “POLAND25.EU” | poland25.eu | doc_quote | 28 | quote_text | high |
| m1 | object | man | man | chunk0 | 1 | noun_chunk_root | high |
| m2 | object | suit | suit | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | blue | blue | chunk1 | 4 | color_attribute | high |
| m4 | object | tie | tie | chunk2 | 7 | noun_chunk_root | high |
| m5 | object | podium | podium | chunk3 | 12 | noun_chunk_root | high |
| m6 | attribute | clear | clear | chunk3 | 11 | visual_attribute | medium |
| m7 | object | right hand | right_hand | chunk4 | 17 | noun_chunk_root | high |
| m8 | object | backdrop | backdrop | chunk6 | 25 | noun_chunk_root | high |
| m9 | attribute | large | large | chunk6 | 23 | size_attribute | high |
| m10 | attribute | white | white | chunk6 | 24 | color_attribute | high |
| m11 | object | logo | logo | chunk7 | 29 | noun_chunk_root | high |
| m12 | object | glasses | glass | chunk10 | 36 | noun_chunk_root | high |
| m13 | object | lanyard | lanyard | chunk11 | 40 | noun_chunk_root | high |
| m14 | object | neck | neck | chunk12 | 43 | noun_chunk_root | high |
| m15 | action | stands | stand | doc | 8 | verb_predicate | high |
| m16 | action | waving | wave | doc | 14 | verb_predicate | high |
| m17 | action | repeated | repeat | doc | 30 | verb_predicate | high |
| m18 | action | wears | wear | doc | 35 | verb_predicate | high |
| m19 | action | has | have | doc | 38 | verb_predicate | high |

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

## 72

**caption_shape:** `sentence-like`
**caption_id:** `34cc48489fc531611fc9cdcecbf86ecd6a5ea1c440dce0396926c8f2fb6b5814`

> A large, old machine stands in a dimly lit room with brick walls and pipes.

### Sentences
| sentence | token_span |
| --- | --- |
| A large, old machine stands in a dimly lit room with brick walls and pipes. | 0:17 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A large, old machine | machine | machine | nsubj | stands | 0:5 |
| a dimly lit room | room | room | pobj | in | 7:11 |
| brick walls | walls | wall | pobj | with | 12:14 |
| pipes | pipes | pipe | conj | walls | 15:16 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | machine | 4 |
| 1 | large | large | ADJ | JJ | amod | machine | 4 |
| 2 | , | , | PUNCT | , | punct | machine | 4 |
| 3 | old | old | ADJ | JJ | amod | machine | 4 |
| 4 | machine | machine | NOUN | NN | nsubj | stands | 5 |
| 5 | stands | stand | VERB | VBZ | ROOT | stands | 5 |
| 6 | in | in | ADP | IN | prep | stands | 5 |
| 7 | a | a | DET | DT | det | room | 10 |
| 8 | dimly | dimly | ADV | RB | advmod | lit | 9 |
| 9 | lit | light | VERB | VBN | amod | room | 10 |
| 10 | room | room | NOUN | NN | pobj | in | 6 |
| 11 | with | with | ADP | IN | prep | room | 10 |
| 12 | brick | brick | NOUN | NN | compound | walls | 13 |
| 13 | walls | wall | NOUN | NNS | pobj | with | 11 |
| 14 | and | and | CCONJ | CC | cc | walls | 13 |
| 15 | pipes | pipe | NOUN | NNS | conj | walls | 13 |
| 16 | . | . | PUNCT | . | punct | stands | 5 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | machine | machine | chunk0 | 4 | noun_chunk_root | high |
| m1 | attribute | large | large | chunk0 | 1 | size_attribute | high |
| m2 | attribute | old | old | chunk0 | 3 | visual_attribute | medium |
| m3 | object | room | room | chunk1 | 10 | noun_chunk_root | high |
| m4 | attribute | dimly | dimly | chunk1 | 8 | modifier_attribute | medium |
| m5 | attribute | lit | light | chunk1 | 9 | visual_attribute | medium |
| m6 | object | walls | wall | chunk2 | 13 | noun_chunk_root | high |
| m7 | attribute | brick | brick | chunk2 | 12 | material_attribute | high |
| m8 | object | pipes | pipe | chunk3 | 15 | noun_chunk_root | high |
| m9 | action | stands | stand | doc | 5 | verb_predicate | high |

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

## 73

**caption_shape:** `multi-sentence`
**caption_id:** `34d700de50423ef5fba9bd0844a97c65242517a160b5fd1d1f1efde9bb74c414`

> A red sports car with the number 27 is parked on a racetrack. Two people stand next to it—one in a blue jacket and another in a black jacket—on a paved surface with hills and trees in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| A red sports car with the number 27 is parked on a racetrack. | 0:13 |
| Two people stand next to it—one in a blue jacket and another in a black jacket—on a paved surface with hills and trees in the background. | 13:43 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| sports car | sports car | sports_car | nsubjpass | parked | 2:3 |
| the number | number | number | pobj | with | 4:6 |
| a racetrack | racetrack | racetrack | pobj | on | 10:12 |
| Two people | people | people | nsubj | stand | 13:15 |
| it | it | it | pobj | to | 18:19 |
| a blue jacket | jacket | jacket | pobj | in | 22:25 |
| another | another | another | conj | one | 26:27 |
| a black jacket | jacket | jacket | pobj | in | 28:31 |
| a paved surface | paved surface | paved_surface | pobj | on | 33:35 |
| hills | hills | hill | pobj | with | 36:37 |
| trees | trees | tree | conj | hills | 38:39 |
| the background | background | background | pobj | in | 40:42 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | parked | 8 |
| 1 | red | red | ADJ | JJ | amod | parked | 8 |
| 2 | sports car | sports_car | NOUN | NN | nsubjpass | parked | 8 |
| 3 | with | with | ADP | IN | prep | sports car | 2 |
| 4 | the | the | DET | DT | det | number | 5 |
| 5 | number | number | NOUN | NN | pobj | with | 3 |
| 6 | 27 | 27 | NUM | CD | nummod | number | 5 |
| 7 | is | be | AUX | VBZ | auxpass | parked | 8 |
| 8 | parked | park | VERB | VBN | ROOT | parked | 8 |
| 9 | on | on | ADP | IN | prep | parked | 8 |
| 10 | a | a | DET | DT | det | racetrack | 11 |
| 11 | racetrack | racetrack | NOUN | NN | pobj | on | 9 |
| 12 | . | . | PUNCT | . | punct | parked | 8 |
| 13 | Two | two | NUM | CD | nummod | people | 14 |
| 14 | people | people | NOUN | NNS | nsubj | stand | 15 |
| 15 | stand | stand | VERB | VBP | ROOT | stand | 15 |
| 16 | next | next | ADV | RB | advmod | stand | 15 |
| 17 | to | to | ADP | IN | prep | next | 16 |
| 18 | it | it | PRON | PRP | pobj | to | 17 |
| 19 | — | — | PUNCT | : | punct | stand | 15 |
| 20 | one | one | NUM | CD | appos | people | 14 |
| 21 | in | in | ADP | IN | prep | one | 20 |
| 22 | a | a | DET | DT | det | jacket | 24 |
| 23 | blue | blue | ADJ | JJ | amod | jacket | 24 |
| 24 | jacket | jacket | NOUN | NN | pobj | in | 21 |
| 25 | and | and | CCONJ | CC | cc | one | 20 |
| 26 | another | another | PRON | DT | conj | one | 20 |
| 27 | in | in | ADP | IN | prep | another | 26 |
| 28 | a | a | DET | DT | det | jacket | 30 |
| 29 | black | black | ADJ | JJ | amod | jacket | 30 |
| 30 | jacket | jacket | NOUN | NN | pobj | in | 27 |
| 31 | — | — | PUNCT | : | punct | stand | 15 |
| 32 | on | on | ADP | IN | prep | stand | 15 |
| 33 | a | a | DET | DT | det | paved surface | 34 |
| 34 | paved surface | paved_surface | NOUN | NN | pobj | on | 32 |
| 35 | with | with | ADP | IN | prep | paved surface | 34 |
| 36 | hills | hill | NOUN | NNS | pobj | with | 35 |
| 37 | and | and | CCONJ | CC | cc | hills | 36 |
| 38 | trees | tree | NOUN | NNS | conj | hills | 36 |
| 39 | in | in | ADP | IN | prep | hills | 36 |
| 40 | the | the | DET | DT | det | background | 41 |
| 41 | background | background | NOUN | NN | pobj | in | 39 |
| 42 | . | . | PUNCT | . | punct | stand | 15 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | sports car | sports_car | chunk0 | 2 | noun_chunk_root | high |
| m1 | object | number | number | chunk1 | 5 | noun_chunk_root | high |
| m2 | object | racetrack | racetrack | chunk2 | 11 | noun_chunk_root | high |
| m3 | object | people | people | chunk3 | 14 | noun_chunk_root | high |
| m4 | quantity | Two | two | chunk3 | 13 | exact_quantity | high |
| m5 | object | jacket | jacket | chunk5 | 24 | noun_chunk_root | high |
| m6 | attribute | blue | blue | chunk5 | 23 | color_attribute | high |
| m7 | object | jacket | jacket | chunk7 | 30 | noun_chunk_root | high |
| m8 | attribute | black | black | chunk7 | 29 | color_attribute | high |
| m9 | object | paved surface | paved_surface | chunk8 | 34 | noun_chunk_root | high |
| m10 | object | hills | hill | chunk9 | 36 | noun_chunk_root | high |
| m11 | object | trees | tree | chunk10 | 38 | noun_chunk_root | high |
| m12 | context | background | background | chunk11 | 41 | scene_context | high |
| m13 | reference | one | one | nominal_reference | 20 | singular_substitute | high |
| m14 | reference | another | another | nominal_reference | 26 | contrastive_reference | high |
| m15 | action | parked | park | doc | 8 | verb_predicate | high |
| m16 | action | stand | stand | doc | 15 | verb_predicate | high |

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

## 74

**caption_shape:** `multi-sentence`
**caption_id:** `350de576a5a0ff340ea1b59f179de89068808c02979c1eb6ae6f29e29b104414`

> A handwritten list on lined paper shows names and details in a table format. The document is labeled "Shipping Office, Canterbury Association" at the top with printed and typed text. Several entries are filled out by hand, including dates and signatures.

**parsed_caption:**

> A handwritten list on lined paper shows names and details in a table format. The document is labeled "Shipping Office, Canterbury Association" at the top with printed and typed text. Several entries are filled out by hand, including dates and signatures.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 350de576a5a0ff340ea1b59f179de89068808c02979c1eb6ae6f29e29b104414:q0 | Shipping Office, Canterbury Association | shipping office, canterbury association | raw_quote_span |  | 101:142 | 101:142 |

### Sentences
| sentence | token_span |
| --- | --- |
| A handwritten list on lined paper shows names and details in a table format. | 0:15 |
| The document is labeled "Shipping Office, Canterbury Association" at the top with printed and typed text. | 15:29 |
| Several entries are filled out by hand, including dates and signatures. | 29:42 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A handwritten list | list | list | nsubj | shows | 0:3 |
| lined paper | paper | paper | pobj | on | 4:6 |
| names | names | name | dobj | shows | 7:8 |
| details | details | detail | conj | names | 9:10 |
| a table format | format | format | pobj | in | 11:14 |
| The document | document | document | nsubjpass | labeled | 15:17 |
| "Shipping Office, Canterbury Association" | "Shipping Office, Canterbury Association" | shipping_office,_canterbury_association | oprd | labeled | 19:20 |
| the top | top | top | pobj | at | 21:23 |
| printed and typed text | text | text | pobj | with | 24:28 |
| Several entries | entries | entry | nsubjpass | filled | 29:31 |
| hand | hand | hand | pobj | by | 35:36 |
| dates | dates | date | pobj | including | 38:39 |
| signatures | signatures | signature | conj | dates | 40:41 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | list | 2 |
| 1 | handwritten | handwritten | ADJ | JJ | amod | list | 2 |
| 2 | list | list | NOUN | NN | nsubj | shows | 6 |
| 3 | on | on | ADP | IN | prep | list | 2 |
| 4 | lined | lined | ADJ | JJ | amod | paper | 5 |
| 5 | paper | paper | NOUN | NN | pobj | on | 3 |
| 6 | shows | show | VERB | VBZ | ROOT | shows | 6 |
| 7 | names | name | NOUN | NNS | dobj | shows | 6 |
| 8 | and | and | CCONJ | CC | cc | names | 7 |
| 9 | details | detail | NOUN | NNS | conj | names | 7 |
| 10 | in | in | ADP | IN | prep | shows | 6 |
| 11 | a | a | DET | DT | det | format | 13 |
| 12 | table | table | NOUN | NN | compound | format | 13 |
| 13 | format | format | NOUN | NN | pobj | in | 10 |
| 14 | . | . | PUNCT | . | punct | shows | 6 |
| 15 | The | the | DET | DT | det | document | 16 |
| 16 | document | document | NOUN | NN | nsubjpass | labeled | 18 |
| 17 | is | be | AUX | VBZ | auxpass | labeled | 18 |
| 18 | labeled | label | VERB | VBN | ROOT | labeled | 18 |
| 19 | "Shipping Office, Canterbury Association" | shipping_office,_canterbury_association | PROPN | NNP | oprd | labeled | 18 |
| 20 | at | at | ADP | IN | prep | labeled | 18 |
| 21 | the | the | DET | DT | det | top | 22 |
| 22 | top | top | NOUN | NN | pobj | at | 20 |
| 23 | with | with | ADP | IN | prep | labeled | 18 |
| 24 | printed | print | VERB | VBN | amod | text | 27 |
| 25 | and | and | CCONJ | CC | cc | printed | 24 |
| 26 | typed | type | VERB | VBN | conj | printed | 24 |
| 27 | text | text | NOUN | NN | pobj | with | 23 |
| 28 | . | . | PUNCT | . | punct | labeled | 18 |
| 29 | Several | several | ADJ | JJ | amod | entries | 30 |
| 30 | entries | entry | NOUN | NNS | nsubjpass | filled | 32 |
| 31 | are | be | AUX | VBP | auxpass | filled | 32 |
| 32 | filled | fill | VERB | VBN | ROOT | filled | 32 |
| 33 | out | out | ADP | RP | prt | filled | 32 |
| 34 | by | by | ADP | IN | prep | filled | 32 |
| 35 | hand | hand | NOUN | NN | pobj | by | 34 |
| 36 | , | , | PUNCT | , | punct | filled | 32 |
| 37 | including | include | VERB | VBG | prep | entries | 30 |
| 38 | dates | date | NOUN | NNS | pobj | including | 37 |
| 39 | and | and | CCONJ | CC | cc | dates | 38 |
| 40 | signatures | signature | NOUN | NNS | conj | dates | 38 |
| 41 | . | . | PUNCT | . | punct | filled | 32 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | "Shipping Office, Canterbury Association" | shipping_office,_canterbury_association | doc_quote | 19 | quote_text | high |
| m1 | object | list | list | chunk0 | 2 | noun_chunk_root | high |
| m2 | attribute | handwritten | handwritten | chunk0 | 1 | modifier_attribute | medium |
| m3 | object | paper | paper | chunk1 | 5 | noun_chunk_root | high |
| m4 | attribute | lined | lined | chunk1 | 4 | modifier_attribute | medium |
| m5 | object | names | name | chunk2 | 7 | noun_chunk_root | high |
| m6 | object | details | detail | chunk3 | 9 | noun_chunk_root | high |
| m7 | object | format | format | chunk4 | 13 | noun_chunk_root | high |
| m8 | attribute | table | table | chunk4 | 12 | compound_modifier | medium |
| m9 | object | document | document | chunk5 | 16 | noun_chunk_root | high |
| m10 | context | top | top | chunk7 | 22 | spatial_region | medium |
| m11 | object | text | text | chunk8 | 27 | noun_chunk_root | high |
| m12 | attribute | printed | print | chunk8 | 24 | state_attribute | medium |
| m13 | object | entries | entry | chunk9 | 30 | noun_chunk_root | high |
| m14 | quantity | Several | several | chunk9 | 29 | approximate_quantity | medium |
| m15 | object | hand | hand | chunk10 | 35 | noun_chunk_root | high |
| m16 | object | dates | date | chunk11 | 38 | noun_chunk_root | high |
| m17 | object | signatures | signature | chunk12 | 40 | noun_chunk_root | high |
| m18 | action | shows | show | doc | 6 | verb_predicate | high |
| m19 | action | labeled | label | doc | 18 | verb_predicate | high |
| m20 | action | typed | type | doc | 26 | verb_predicate | high |
| m21 | action | filled | fill | doc | 32 | verb_predicate | high |
| m22 | action | including | include | doc | 37 | verb_predicate | high |

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
| e11 | agent | m22 | m13 | medium | inherited agent prep -> entries |
| e12 | patient | m22 | m16 | medium | pobj -> including |
| e13 | patient | m22 | m17 | medium | pobj -> including |
| e14 | relation | m1 | m3 | high | on |
| e15 | relation | m1 | m7 | high | in |
| e16 | relation | m9 | m10 | medium | at |
| e17 | relation | m9 | m11 | high | with |
| e18 | relation | m13 | m15 | medium | by |
| e19 | relation | m13 | m16 | medium | include |
| e20 | relation | m13 | m17 | medium | include |

### Skipped Raw Concept Edges
_none_

## 75

**caption_shape:** `tag-list-like`
**caption_id:** `35a8a2cb41d086897a80f0315db645719b1baf055872b152dfc5f95630924c14`

> person, path, trees, lake, fence

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | person | person | 0:6 |
| t1 | path | path | 8:12 |
| t2 | trees | trees | 14:19 |
| t3 | lake | lake | 21:25 |
| t4 | fence | fence | 27:32 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | person | person | person | ROOT | person | 0:1 | 0:6 |
| t1 | path | path | path | ROOT | path | 0:1 | 8:12 |
| t2 | trees | trees | tree | ROOT | trees | 0:1 | 14:19 |
| t3 | lake | lake | lake | ROOT | lake | 0:1 | 21:25 |
| t4 | fence | fence | fence | ROOT | fence | 0:1 | 27:32 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | person | person | NOUN | NOUN | NN | NN | ROOT | person | 0 | 0:6 |
| t1 | 0 | path | path | NOUN | NOUN | NN | NN | ROOT | path | 0 | 8:12 |
| t2 | 0 | trees | tree | NOUN | NOUN | NNS | NNS | ROOT | trees | 0 | 14:19 |
| t3 | 0 | lake | lake | PROPN | NOUN | NNP | NN | ROOT | lake | 0 | 21:25 |
| t4 | 0 | fence | fence | NOUN | NOUN | NN | NN | ROOT | fence | 0 | 27:32 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | t0 | 0 | segment_head | high |
| m1 | object | path | path | t1 | 0 | segment_head | high |
| m2 | object | trees | tree | t2 | 0 | segment_head | high |
| m3 | object | lake | lake | t3 | 0 | segment_head | high |
| m4 | object | fence | fence | t4 | 0 | segment_head | high |

### Edges
_none_

## 76

**caption_shape:** `multi-sentence`
**caption_id:** `361f12f9479f0114f214410da64dfdec98173f5d972c21e3be8d788c62f2a414`

> Three men in suits stand at a podium with a microphone. One man speaks while the others listen, positioned behind him near flags and a marble wall. A plaque on the podium reads “ASSEMBLEIA LEGISLATIVA.”

**parsed_caption:**

> Three men in suits stand at a podium with a microphone. One man speaks while the others listen, positioned behind him near flags and a marble wall. A plaque on the podium reads “ASSEMBLEIA LEGISLATIVA.”

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 361f12f9479f0114f214410da64dfdec98173f5d972c21e3be8d788c62f2a414:q0 | ASSEMBLEIA LEGISLATIVA. | assembleia legislativa. | raw_quote_span |  | 177:202 | 177:202 |

### Sentences
| sentence | token_span |
| --- | --- |
| Three men in suits stand at a podium with a microphone. | 0:12 |
| One man speaks while the others listen, positioned behind him near flags and a marble wall. | 12:30 |
| A plaque on the podium reads “ASSEMBLEIA LEGISLATIVA.” | 30:37 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Three men | men | man | nsubj | stand | 0:2 |
| suits | suits | suit | pobj | in | 3:4 |
| a podium | podium | podium | pobj | at | 6:8 |
| a microphone | microphone | microphone | pobj | with | 9:11 |
| One man | man | man | nsubj | speaks | 12:14 |
| the others | others | other | nsubj | listen | 16:18 |
| him | him | he | pobj | behind | 22:23 |
| flags | flags | flag | pobj | near | 24:25 |
| a marble wall | wall | wall | conj | flags | 26:29 |
| A plaque | plaque | plaque | nsubj | reads | 30:32 |
| the podium | podium | podium | pobj | on | 33:35 |
| “ASSEMBLEIA LEGISLATIVA.” | “ASSEMBLEIA LEGISLATIVA.” | assembleia_legislativa. | dobj | reads | 36:37 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Three | three | NUM | CD | nummod | men | 1 |
| 1 | men | man | NOUN | NNS | nsubj | stand | 4 |
| 2 | in | in | ADP | IN | prep | men | 1 |
| 3 | suits | suit | NOUN | NNS | pobj | in | 2 |
| 4 | stand | stand | VERB | VBP | ROOT | stand | 4 |
| 5 | at | at | ADP | IN | prep | stand | 4 |
| 6 | a | a | DET | DT | det | podium | 7 |
| 7 | podium | podium | NOUN | NN | pobj | at | 5 |
| 8 | with | with | ADP | IN | prep | stand | 4 |
| 9 | a | a | DET | DT | det | microphone | 10 |
| 10 | microphone | microphone | NOUN | NN | pobj | with | 8 |
| 11 | . | . | PUNCT | . | punct | stand | 4 |
| 12 | One | one | NUM | CD | nummod | man | 13 |
| 13 | man | man | NOUN | NN | nsubj | speaks | 14 |
| 14 | speaks | speak | VERB | VBZ | ROOT | speaks | 14 |
| 15 | while | while | SCONJ | IN | mark | listen | 18 |
| 16 | the | the | DET | DT | det | others | 17 |
| 17 | others | other | NOUN | NNS | nsubj | listen | 18 |
| 18 | listen | listen | VERB | VBP | advcl | speaks | 14 |
| 19 | , | , | PUNCT | , | punct | speaks | 14 |
| 20 | positioned | position | VERB | VBN | advcl | speaks | 14 |
| 21 | behind | behind | ADP | IN | prep | positioned | 20 |
| 22 | him | he | PRON | PRP | pobj | behind | 21 |
| 23 | near | near | ADP | IN | prep | positioned | 20 |
| 24 | flags | flag | NOUN | NNS | pobj | near | 23 |
| 25 | and | and | CCONJ | CC | cc | flags | 24 |
| 26 | a | a | DET | DT | det | wall | 28 |
| 27 | marble | marble | NOUN | NN | compound | wall | 28 |
| 28 | wall | wall | NOUN | NN | conj | flags | 24 |
| 29 | . | . | PUNCT | . | punct | speaks | 14 |
| 30 | A | a | DET | DT | det | plaque | 31 |
| 31 | plaque | plaque | NOUN | NN | nsubj | reads | 35 |
| 32 | on | on | ADP | IN | prep | plaque | 31 |
| 33 | the | the | DET | DT | det | podium | 34 |
| 34 | podium | podium | NOUN | NN | pobj | on | 32 |
| 35 | reads | read | VERB | VBZ | ROOT | reads | 35 |
| 36 | “ASSEMBLEIA LEGISLATIVA.” | assembleia_legislativa. | PROPN | NNP | dobj | reads | 35 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | attribute | “ASSEMBLEIA LEGISLATIVA.” | assembleia_legislativa. | doc_quote | 36 | quote_text | high |
| m1 | object | men | man | chunk0 | 1 | noun_chunk_root | high |
| m2 | quantity | Three | three | chunk0 | 0 | exact_quantity | high |
| m3 | object | suits | suit | chunk1 | 3 | noun_chunk_root | high |
| m4 | object | podium | podium | chunk2 | 7 | noun_chunk_root | high |
| m5 | object | microphone | microphone | chunk3 | 10 | noun_chunk_root | high |
| m6 | object | man | man | chunk4 | 13 | noun_chunk_root | high |
| m7 | quantity | One | one | chunk4 | 12 | exact_quantity | high |
| m8 | object | flags | flag | chunk7 | 24 | noun_chunk_root | high |
| m9 | object | wall | wall | chunk8 | 28 | noun_chunk_root | high |
| m10 | attribute | marble | marble | chunk8 | 27 | compound_modifier | medium |
| m11 | object | plaque | plaque | chunk9 | 31 | noun_chunk_root | high |
| m12 | object | podium | podium | chunk10 | 34 | noun_chunk_root | high |
| m13 | reference | others | other | nominal_reference | 17 | contrastive_reference | high |
| m14 | action | stand | stand | doc | 4 | verb_predicate | high |
| m15 | action | speaks | speak | doc | 14 | verb_predicate | high |
| m16 | action | listen | listen | doc | 18 | verb_predicate | high |
| m17 | action | positioned | position | doc | 20 | verb_predicate | high |
| m18 | action | reads | read | doc | 35 | verb_predicate | high |

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

## 77

**caption_shape:** `multi-sentence`
**caption_id:** `376ebd462683c1f3eb28ed9be54e2482e19ec9b94cfd32c1a5173b08d722d814`

> Many white angel figurines are displayed closely together on a dark surface. One angel in the foreground has gold trim around its head and is lying down with wings spread. Some have small tags attached, suggesting they are for sale.

### Sentences
| sentence | token_span |
| --- | --- |
| Many white angel figurines are displayed closely together on a dark surface. | 0:13 |
| One angel in the foreground has gold trim around its head and is lying down with wings spread. | 13:32 |
| Some have small tags attached, suggesting they are for sale. | 32:44 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Many white angel figurines | figurines | figurine | nsubjpass | displayed | 0:4 |
| a dark surface | surface | surface | pobj | on | 9:12 |
| One angel | angel | angel | nsubj | has | 13:15 |
| the foreground | foreground | foreground | pobj | in | 16:18 |
| gold trim | trim | trim | dobj | has | 19:21 |
| its head | head | head | pobj | around | 22:24 |
| wings | wings | wing | nsubj | spread | 29:30 |
| Some | Some | some | nsubj | have | 32:33 |
| small tags | tags | tag | nsubj | attached | 34:36 |
| they | they | they | nsubj | are | 39:40 |
| sale | sale | sale | pobj | for | 42:43 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Many | many | ADJ | JJ | amod | figurines | 3 |
| 1 | white | white | ADJ | JJ | amod | figurines | 3 |
| 2 | angel | angel | NOUN | NN | compound | figurines | 3 |
| 3 | figurines | figurine | NOUN | NNS | nsubjpass | displayed | 5 |
| 4 | are | be | AUX | VBP | auxpass | displayed | 5 |
| 5 | displayed | display | VERB | VBN | ROOT | displayed | 5 |
| 6 | closely | closely | ADV | RB | advmod | together | 7 |
| 7 | together | together | ADV | RB | advmod | displayed | 5 |
| 8 | on | on | ADP | IN | prep | displayed | 5 |
| 9 | a | a | DET | DT | det | surface | 11 |
| 10 | dark | dark | ADJ | JJ | amod | surface | 11 |
| 11 | surface | surface | NOUN | NN | pobj | on | 8 |
| 12 | . | . | PUNCT | . | punct | displayed | 5 |
| 13 | One | one | NUM | CD | nummod | angel | 14 |
| 14 | angel | angel | NOUN | NN | nsubj | has | 18 |
| 15 | in | in | ADP | IN | prep | angel | 14 |
| 16 | the | the | DET | DT | det | foreground | 17 |
| 17 | foreground | foreground | NOUN | NN | pobj | in | 15 |
| 18 | has | have | VERB | VBZ | ROOT | has | 18 |
| 19 | gold | gold | NOUN | NN | compound | trim | 20 |
| 20 | trim | trim | NOUN | NN | dobj | has | 18 |
| 21 | around | around | ADP | IN | prep | has | 18 |
| 22 | its | its | PRON | PRP$ | poss | head | 23 |
| 23 | head | head | NOUN | NN | pobj | around | 21 |
| 24 | and | and | CCONJ | CC | cc | has | 18 |
| 25 | is | be | AUX | VBZ | aux | lying | 26 |
| 26 | lying | lie | VERB | VBG | conj | has | 18 |
| 27 | down | down | ADV | RB | advmod | lying | 26 |
| 28 | with | with | SCONJ | IN | mark | spread | 30 |
| 29 | wings | wing | NOUN | NNS | nsubj | spread | 30 |
| 30 | spread | spread | VERB | VBN | advcl | lying | 26 |
| 31 | . | . | PUNCT | . | punct | has | 18 |
| 32 | Some | some | PRON | DT | nsubj | have | 33 |
| 33 | have | have | VERB | VBP | ROOT | have | 33 |
| 34 | small | small | ADJ | JJ | amod | tags | 35 |
| 35 | tags | tag | NOUN | NNS | nsubj | attached | 36 |
| 36 | attached | attach | VERB | VBN | ccomp | have | 33 |
| 37 | , | , | PUNCT | , | punct | have | 33 |
| 38 | suggesting | suggest | VERB | VBG | advcl | have | 33 |
| 39 | they | they | PRON | PRP | nsubj | are | 40 |
| 40 | are | be | AUX | VBP | ccomp | suggesting | 38 |
| 41 | for | for | ADP | IN | prep | are | 40 |
| 42 | sale | sale | NOUN | NN | pobj | for | 41 |
| 43 | . | . | PUNCT | . | punct | have | 33 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | figurines | figurine | chunk0 | 3 | noun_chunk_root | high |
| m1 | quantity | Many | many | chunk0 | 0 | approximate_quantity | medium |
| m2 | attribute | white | white | chunk0 | 1 | color_attribute | high |
| m3 | attribute | angel | angel | chunk0 | 2 | compound_modifier | medium |
| m4 | context | surface | surface | chunk1 | 11 | spatial_region | medium |
| m5 | object | angel | angel | chunk2 | 14 | noun_chunk_root | high |
| m6 | quantity | One | one | chunk2 | 13 | exact_quantity | high |
| m7 | context | foreground | foreground | chunk3 | 17 | scene_context | high |
| m8 | object | trim | trim | chunk4 | 20 | noun_chunk_root | high |
| m9 | attribute | gold | gold | chunk4 | 19 | color_attribute | high |
| m10 | object | head | head | chunk5 | 23 | noun_chunk_root | high |
| m11 | object | wings | wing | chunk6 | 29 | noun_chunk_root | high |
| m12 | quantity | Some | some | chunk7 | 32 | indefinite_quantity | medium |
| m13 | object | tags | tag | chunk8 | 35 | noun_chunk_root | high |
| m14 | attribute | small | small | chunk8 | 34 | size_attribute | high |
| m15 | object | sale | sale | chunk10 | 42 | noun_chunk_root | high |
| m16 | action | displayed | display | doc | 5 | verb_predicate | high |
| m17 | action | has | have | doc | 18 | verb_predicate | high |
| m18 | action | lying | lie | doc | 26 | verb_predicate | high |
| m19 | action | spread | spread | doc | 30 | verb_predicate | high |
| m20 | action | have | have | doc | 33 | verb_predicate | high |
| m21 | action | attached | attach | doc | 36 | verb_predicate | high |
| m22 | action | suggesting | suggest | doc | 38 | verb_predicate | high |

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

## 78

**caption_shape:** `multi-sentence`
**caption_id:** `38edf47d709d02a968cba65d1dfca5a24d612e5654f458d0287c380bc18a2014`

> A narrow pathway leads through an arched entrance to a building at night. Several glowing spherical lights line the path, and two people are visible walking inside the archway. Snow covers the ground on either side of the walkway.

### Sentences
| sentence | token_span |
| --- | --- |
| A narrow pathway leads through an arched entrance to a building at night. | 0:14 |
| Several glowing spherical lights line the path, and two people are visible walking inside the archway. | 14:32 |
| Snow covers the ground on either side of the walkway. | 32:43 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A narrow pathway | pathway | pathway | nsubj | leads | 0:3 |
| an arched entrance | entrance | entrance | pobj | through | 5:8 |
| a building | building | building | pobj | to | 9:11 |
| night | night | night | pobj | at | 12:13 |
| Several glowing spherical lights | lights | light | nsubj | line | 14:18 |
| the path | path | path | dobj | line | 19:21 |
| two people | people | people | nsubj | are | 23:25 |
| the archway | archway | archway | pobj | inside | 29:31 |
| Snow | Snow | snow | nsubj | covers | 32:33 |
| the ground | ground | ground | dobj | covers | 34:36 |
| either side | side | side | pobj | on | 37:39 |
| the walkway | walkway | walkway | pobj | of | 40:42 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | pathway | 2 |
| 1 | narrow | narrow | ADJ | JJ | amod | pathway | 2 |
| 2 | pathway | pathway | NOUN | NN | nsubj | leads | 3 |
| 3 | leads | lead | VERB | VBZ | ROOT | leads | 3 |
| 4 | through | through | ADP | IN | prep | leads | 3 |
| 5 | an | an | DET | DT | det | entrance | 7 |
| 6 | arched | arched | ADJ | JJ | amod | entrance | 7 |
| 7 | entrance | entrance | NOUN | NN | pobj | through | 4 |
| 8 | to | to | ADP | IN | prep | entrance | 7 |
| 9 | a | a | DET | DT | det | building | 10 |
| 10 | building | building | NOUN | NN | pobj | to | 8 |
| 11 | at | at | ADP | IN | prep | leads | 3 |
| 12 | night | night | NOUN | NN | pobj | at | 11 |
| 13 | . | . | PUNCT | . | punct | leads | 3 |
| 14 | Several | several | ADJ | JJ | amod | lights | 17 |
| 15 | glowing | glow | VERB | VBG | amod | lights | 17 |
| 16 | spherical | spherical | ADJ | JJ | amod | lights | 17 |
| 17 | lights | light | NOUN | NNS | nsubj | line | 18 |
| 18 | line | line | VERB | VBP | ROOT | line | 18 |
| 19 | the | the | DET | DT | det | path | 20 |
| 20 | path | path | NOUN | NN | dobj | line | 18 |
| 21 | , | , | PUNCT | , | punct | line | 18 |
| 22 | and | and | CCONJ | CC | cc | line | 18 |
| 23 | two | two | NUM | CD | nummod | people | 24 |
| 24 | people | people | NOUN | NNS | nsubj | are | 25 |
| 25 | are | be | AUX | VBP | conj | line | 18 |
| 26 | visible | visible | ADJ | JJ | acomp | are | 25 |
| 27 | walking | walk | VERB | VBG | xcomp | visible | 26 |
| 28 | inside | inside | ADP | IN | prep | walking | 27 |
| 29 | the | the | DET | DT | det | archway | 30 |
| 30 | archway | archway | NOUN | NN | pobj | inside | 28 |
| 31 | . | . | PUNCT | . | punct | are | 25 |
| 32 | Snow | snow | NOUN | NN | nsubj | covers | 33 |
| 33 | covers | cover | VERB | VBZ | ROOT | covers | 33 |
| 34 | the | the | DET | DT | det | ground | 35 |
| 35 | ground | ground | NOUN | NN | dobj | covers | 33 |
| 36 | on | on | ADP | IN | prep | covers | 33 |
| 37 | either | either | DET | DT | det | side | 38 |
| 38 | side | side | NOUN | NN | pobj | on | 36 |
| 39 | of | of | ADP | IN | prep | side | 38 |
| 40 | the | the | DET | DT | det | walkway | 41 |
| 41 | walkway | walkway | NOUN | NN | pobj | of | 39 |
| 42 | . | . | PUNCT | . | punct | covers | 33 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | pathway | pathway | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | narrow | narrow | chunk0 | 1 | size_attribute | high |
| m2 | object | entrance | entrance | chunk1 | 7 | noun_chunk_root | high |
| m3 | attribute | arched | arched | chunk1 | 6 | visual_attribute | medium |
| m4 | object | building | building | chunk2 | 10 | noun_chunk_root | high |
| m5 | context | night | night | chunk3 | 12 | scene_context | medium |
| m6 | object | lights | light | chunk4 | 17 | noun_chunk_root | high |
| m7 | quantity | Several | several | chunk4 | 14 | approximate_quantity | medium |
| m8 | attribute | glowing | glow | chunk4 | 15 | state_attribute | medium |
| m9 | attribute | spherical | spherical | chunk4 | 16 | modifier_attribute | medium |
| m10 | object | path | path | chunk5 | 20 | noun_chunk_root | high |
| m11 | object | people | people | chunk6 | 24 | noun_chunk_root | high |
| m12 | quantity | two | two | chunk6 | 23 | exact_quantity | high |
| m13 | object | archway | archway | chunk7 | 30 | noun_chunk_root | high |
| m14 | object | Snow | snow | chunk8 | 32 | noun_chunk_root | high |
| m15 | object | ground | ground | chunk9 | 35 | noun_chunk_root | high |
| m16 | context | side | side | chunk10 | 38 | spatial_region | medium |
| m17 | object | walkway | walkway | chunk11 | 41 | noun_chunk_root | high |
| m18 | action | leads | lead | doc | 3 | verb_predicate | high |
| m19 | action | line | line | doc | 18 | verb_predicate | high |
| m20 | action | walking | walk | doc | 27 | verb_predicate | high |
| m21 | action | covers | cover | doc | 33 | verb_predicate | high |

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

## 79

**caption_shape:** `sentence-like`
**caption_id:** `3c5d43d61ed3ed53aa6b4588d4819a066946baf99be8b7d2bf7da9521a0c0414`

> A person with white hair holds a tangled red rope in front of their face.

### Sentences
| sentence | token_span |
| --- | --- |
| A person with white hair holds a tangled red rope in front of their face. | 0:16 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A person | person | person | nsubj | holds | 0:2 |
| white hair | hair | hair | pobj | with | 3:5 |
| a tangled red rope | rope | rope | dobj | holds | 6:10 |
| front | front | front | pobj | in | 11:12 |
| their face | face | face | pobj | of | 13:15 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | person | 1 |
| 1 | person | person | NOUN | NN | nsubj | holds | 5 |
| 2 | with | with | ADP | IN | prep | person | 1 |
| 3 | white | white | ADJ | JJ | amod | hair | 4 |
| 4 | hair | hair | NOUN | NN | pobj | with | 2 |
| 5 | holds | hold | VERB | VBZ | ROOT | holds | 5 |
| 6 | a | a | DET | DT | det | rope | 9 |
| 7 | tangled | tangle | VERB | VBN | amod | rope | 9 |
| 8 | red | red | ADJ | JJ | amod | rope | 9 |
| 9 | rope | rope | NOUN | NN | dobj | holds | 5 |
| 10 | in | in | ADP | IN | prep | holds | 5 |
| 11 | front | front | NOUN | NN | pobj | in | 10 |
| 12 | of | of | ADP | IN | prep | front | 11 |
| 13 | their | their | PRON | PRP$ | poss | face | 14 |
| 14 | face | face | NOUN | NN | pobj | of | 12 |
| 15 | . | . | PUNCT | . | punct | holds | 5 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | hair | hair | chunk1 | 4 | noun_chunk_root | high |
| m2 | attribute | white | white | chunk1 | 3 | color_attribute | high |
| m3 | object | rope | rope | chunk2 | 9 | noun_chunk_root | high |
| m4 | attribute | tangled | tangle | chunk2 | 7 | state_attribute | medium |
| m5 | attribute | red | red | chunk2 | 8 | color_attribute | high |
| m6 | object | face | face | chunk4 | 14 | noun_chunk_root | high |
| m7 | action | holds | hold | doc | 5 | verb_predicate | high |

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

## 80

**caption_shape:** `sentence-like`
**caption_id:** `3c89dbf4ddc032df960c22d5b36ad91d9d785b52c535a524129808269fe56014`

> Two hockey players skate on the ice, one in green and one in blue, while a referee watches nearby.

### Sentences
| sentence | token_span |
| --- | --- |
| Two hockey players skate on the ice, one in green and one in blue, while a referee watches nearby. | 0:21 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Two hockey players | hockey players | hockey_player | nsubj | skate | 0:2 |
| the ice | ice | ice | pobj | on | 4:6 |
| green | green | green | pobj | in | 9:10 |
| a referee | referee | referee | nsubj | watches | 16:18 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Two | two | NUM | CD | nummod | hockey players | 1 |
| 1 | hockey players | hockey_player | NOUN | NN | nsubj | skate | 2 |
| 2 | skate | skate | VERB | VBP | ROOT | skate | 2 |
| 3 | on | on | ADP | IN | prep | skate | 2 |
| 4 | the | the | DET | DT | det | ice | 5 |
| 5 | ice | ice | NOUN | NN | pobj | on | 3 |
| 6 | , | , | PUNCT | , | punct | skate | 2 |
| 7 | one | one | NUM | CD | appos | hockey players | 1 |
| 8 | in | in | ADP | IN | prep | one | 7 |
| 9 | green | green | NOUN | NN | pobj | in | 8 |
| 10 | and | and | CCONJ | CC | cc | one | 7 |
| 11 | one | one | NUM | CD | conj | one | 7 |
| 12 | in | in | ADP | IN | prep | one | 11 |
| 13 | blue | blue | ADJ | JJ | pobj | in | 12 |
| 14 | , | , | PUNCT | , | punct | skate | 2 |
| 15 | while | while | SCONJ | IN | mark | watches | 18 |
| 16 | a | a | DET | DT | det | referee | 17 |
| 17 | referee | referee | NOUN | NN | nsubj | watches | 18 |
| 18 | watches | watch | VERB | VBZ | advcl | skate | 2 |
| 19 | nearby | nearby | ADV | RB | advmod | watches | 18 |
| 20 | . | . | PUNCT | . | punct | skate | 2 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hockey players | hockey_player | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Two | two | chunk0 | 0 | exact_quantity | high |
| m2 | object | ice | ice | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | green | green | chunk2 | 9 | color_attribute | high |
| m4 | object | referee | referee | chunk3 | 17 | noun_chunk_root | high |
| m5 | reference | one | one | nominal_reference | 7 | singular_substitute | high |
| m6 | reference | one | one | nominal_reference | 11 | singular_substitute | high |
| m7 | action | skate | skate | doc | 2 | verb_predicate | high |
| m8 | action | watches | watch | doc | 18 | verb_predicate | high |

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

## 81

**caption_shape:** `sentence-like`
**caption_id:** `3ce6ad26275a45c220438a773a16b0b3cafb709c25f367f6bc3f2bf74a0fa414`

> A person with orange hair and tattoos wears a light green shirt, raising one arm against a dark background.

### Sentences
| sentence | token_span |
| --- | --- |
| A person with orange hair and tattoos wears a light green shirt, raising one arm against a dark background. | 0:21 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A person | person | person | nsubj | wears | 0:2 |
| orange hair | hair | hair | pobj | with | 3:5 |
| tattoos | tattoos | tattoo | conj | hair | 6:7 |
| a light green shirt | shirt | shirt | dobj | wears | 8:12 |
| one arm | arm | arm | dobj | raising | 14:16 |
| a dark background | background | background | pobj | against | 17:20 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | person | 1 |
| 1 | person | person | NOUN | NN | nsubj | wears | 7 |
| 2 | with | with | ADP | IN | prep | person | 1 |
| 3 | orange | orange | ADJ | JJ | amod | hair | 4 |
| 4 | hair | hair | NOUN | NN | pobj | with | 2 |
| 5 | and | and | CCONJ | CC | cc | hair | 4 |
| 6 | tattoos | tattoo | NOUN | NNS | conj | hair | 4 |
| 7 | wears | wear | VERB | VBZ | ROOT | wears | 7 |
| 8 | a | a | DET | DT | det | shirt | 11 |
| 9 | light | light | ADJ | JJ | amod | green | 10 |
| 10 | green | green | ADJ | JJ | amod | shirt | 11 |
| 11 | shirt | shirt | NOUN | NN | dobj | wears | 7 |
| 12 | , | , | PUNCT | , | punct | wears | 7 |
| 13 | raising | raise | VERB | VBG | advcl | wears | 7 |
| 14 | one | one | NUM | CD | nummod | arm | 15 |
| 15 | arm | arm | NOUN | NN | dobj | raising | 13 |
| 16 | against | against | ADP | IN | prep | raising | 13 |
| 17 | a | a | DET | DT | det | background | 19 |
| 18 | dark | dark | ADJ | JJ | amod | background | 19 |
| 19 | background | background | NOUN | NN | pobj | against | 16 |
| 20 | . | . | PUNCT | . | punct | wears | 7 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | hair | hair | chunk1 | 4 | noun_chunk_root | high |
| m2 | attribute | orange | orange | chunk1 | 3 | color_attribute | high |
| m3 | object | tattoos | tattoo | chunk2 | 6 | noun_chunk_root | high |
| m4 | object | shirt | shirt | chunk3 | 11 | noun_chunk_root | high |
| m5 | attribute | light | light | chunk3 | 9 | visual_attribute | medium |
| m6 | attribute | green | green | chunk3 | 10 | color_attribute | high |
| m7 | object | arm | arm | chunk4 | 15 | noun_chunk_root | high |
| m8 | quantity | one | one | chunk4 | 14 | exact_quantity | high |
| m9 | context | background | background | chunk5 | 19 | scene_context | high |
| m10 | attribute | dark | dark | chunk5 | 18 | visual_attribute | medium |
| m11 | action | wears | wear | doc | 7 | verb_predicate | high |
| m12 | action | raising | raise | doc | 13 | verb_predicate | high |

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

## 82

**caption_shape:** `multi-sentence`
**caption_id:** `3e2fb02a7420ac1fa49156d7cb913bd6b855d9bdbbb933336bd093e91e7f4414`

> Soldiers wade through water in a landing craft, heading toward the Lincoln Memorial. The scene is set on a sunny day with trees lining the path and the monument visible in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| Soldiers wade through water in a landing craft, heading toward the Lincoln Memorial. | 0:15 |
| The scene is set on a sunny day with trees lining the path and the monument visible in the background. | 15:36 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Soldiers | Soldiers | soldier | nsubj | wade | 0:1 |
| water | water | water | pobj | through | 3:4 |
| a landing craft | craft | craft | pobj | in | 5:8 |
| the Lincoln Memorial | Memorial | Memorial | pobj | toward | 11:14 |
| The scene | scene | scene | nsubjpass | set | 15:17 |
| a sunny day | day | day | pobj | on | 20:23 |
| trees | trees | tree | nsubj | lining | 24:25 |
| the path | path | path | dobj | lining | 26:28 |
| the monument | monument | monument | nsubj | visible | 29:31 |
| the background | background | background | pobj | in | 33:35 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Soldiers | soldier | NOUN | NNS | nsubj | wade | 1 |
| 1 | wade | wade | VERB | VBP | ROOT | wade | 1 |
| 2 | through | through | ADP | IN | prep | wade | 1 |
| 3 | water | water | NOUN | NN | pobj | through | 2 |
| 4 | in | in | ADP | IN | prep | wade | 1 |
| 5 | a | a | DET | DT | det | craft | 7 |
| 6 | landing | landing | NOUN | NN | compound | craft | 7 |
| 7 | craft | craft | NOUN | NN | pobj | in | 4 |
| 8 | , | , | PUNCT | , | punct | wade | 1 |
| 9 | heading | head | VERB | VBG | advcl | wade | 1 |
| 10 | toward | toward | ADP | IN | prep | heading | 9 |
| 11 | the | the | DET | DT | det | Memorial | 13 |
| 12 | Lincoln | Lincoln | PROPN | NNP | compound | Memorial | 13 |
| 13 | Memorial | Memorial | PROPN | NNP | pobj | toward | 10 |
| 14 | . | . | PUNCT | . | punct | wade | 1 |
| 15 | The | the | DET | DT | det | scene | 16 |
| 16 | scene | scene | NOUN | NN | nsubjpass | set | 18 |
| 17 | is | be | AUX | VBZ | auxpass | set | 18 |
| 18 | set | set | VERB | VBN | ROOT | set | 18 |
| 19 | on | on | ADP | IN | prep | set | 18 |
| 20 | a | a | DET | DT | det | day | 22 |
| 21 | sunny | sunny | ADJ | JJ | amod | day | 22 |
| 22 | day | day | NOUN | NN | pobj | on | 19 |
| 23 | with | with | SCONJ | IN | mark | lining | 25 |
| 24 | trees | tree | NOUN | NNS | nsubj | lining | 25 |
| 25 | lining | line | VERB | VBG | advcl | set | 18 |
| 26 | the | the | DET | DT | det | path | 27 |
| 27 | path | path | NOUN | NN | dobj | lining | 25 |
| 28 | and | and | CCONJ | CC | cc | lining | 25 |
| 29 | the | the | DET | DT | det | monument | 30 |
| 30 | monument | monument | NOUN | NN | nsubj | visible | 31 |
| 31 | visible | visible | ADJ | JJ | conj | lining | 25 |
| 32 | in | in | ADP | IN | prep | visible | 31 |
| 33 | the | the | DET | DT | det | background | 34 |
| 34 | background | background | NOUN | NN | pobj | in | 32 |
| 35 | . | . | PUNCT | . | punct | set | 18 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | Soldiers | soldier | chunk0 | 0 | noun_chunk_root | high |
| m1 | object | water | water | chunk1 | 3 | noun_chunk_root | high |
| m2 | object | craft | craft | chunk2 | 7 | noun_chunk_root | high |
| m3 | attribute | landing | landing | chunk2 | 6 | compound_modifier | medium |
| m4 | object | Memorial | memorial | chunk3 | 13 | noun_chunk_root | high |
| m5 | attribute | Lincoln | lincoln | chunk3 | 12 | compound_modifier | medium |
| m6 | object | scene | scene | chunk4 | 16 | noun_chunk_root | high |
| m7 | context | day | day | chunk5 | 22 | scene_context | medium |
| m8 | attribute | sunny | sunny | chunk5 | 21 | modifier_attribute | medium |
| m9 | object | trees | tree | chunk6 | 24 | noun_chunk_root | high |
| m10 | object | path | path | chunk7 | 27 | noun_chunk_root | high |
| m11 | object | monument | monument | chunk8 | 30 | noun_chunk_root | high |
| m12 | context | background | background | chunk9 | 34 | scene_context | high |
| m13 | action | wade | wade | doc | 1 | verb_predicate | high |
| m14 | action | heading | head | doc | 9 | verb_predicate | high |
| m15 | action | set | set | doc | 18 | verb_predicate | high |
| m16 | action | lining | line | doc | 25 | verb_predicate | high |

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

## 83

**caption_shape:** `tag-list-like`
**caption_id:** `3f2627a92b621bc5323f53361344ffe6603365aca0a7e45511dafc143b4e8414`

> buddha statue, mountain, green sky, bare tree, stone base

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | buddha statue | buddha statue | 0:13 |
| t1 | mountain | mountain | 15:23 |
| t2 | green sky | green sky | 25:34 |
| t3 | bare tree | bare tree | 36:45 |
| t4 | stone base | stone base | 47:57 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | buddha statue | statue | statue | ROOT | statue | 0:2 | 0:13 |
| t1 | mountain | mountain | mountain | ROOT | mountain | 0:1 | 15:23 |
| t2 | green sky | sky | sky | ROOT | sky | 0:2 | 25:34 |
| t3 | bare tree | tree | tree | ROOT | tree | 0:2 | 36:45 |
| t4 | stone base | base | base | ROOT | base | 0:2 | 47:57 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | buddha | buddha | PROPN | ADJ | NNP | JJ | compound | statue | 1 | 0:6 |
| t0 | 1 | statue | statue | NOUN | NOUN | NN | NN | ROOT | statue | 1 | 7:13 |
| t1 | 0 | mountain | mountain | NOUN | NOUN | NN | NN | ROOT | mountain | 0 | 15:23 |
| t2 | 0 | green | green | ADJ | ADJ | JJ | JJ | amod | sky | 1 | 25:30 |
| t2 | 1 | sky | sky | NOUN | NOUN | NN | NN | ROOT | sky | 1 | 31:34 |
| t3 | 0 | bare | bare | PROPN | ADJ | NNP | JJ | compound | tree | 1 | 36:40 |
| t3 | 1 | tree | tree | PROPN | NOUN | NNP | NN | ROOT | tree | 1 | 41:45 |
| t4 | 0 | stone | stone | NOUN | NOUN | NN | NN | compound | base | 1 | 47:52 |
| t4 | 1 | base | base | NOUN | NOUN | NN | NN | ROOT | base | 1 | 53:57 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | statue | statue | t0 | 1 | segment_head | high |
| m1 | attribute | buddha | buddha | t0 | 0 | attribute | high |
| m2 | object | mountain | mountain | t1 | 0 | segment_head | high |
| m3 | object | sky | sky | t2 | 1 | segment_head | high |
| m4 | attribute | green | green | t2 | 0 | attribute | high |
| m5 | object | tree | tree | t3 | 1 | segment_head | high |
| m6 | attribute | bare | bare | t3 | 0 | attribute | high |
| m7 | object | base | base | t4 | 1 | segment_head | high |
| m8 | attribute | stone | stone | t4 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> statue |
| e1 | has_attribute | m3 | m4 | high | t2 internal amod -> sky |
| e2 | has_attribute | m5 | m6 | high | t3 internal compound -> tree |
| e3 | has_attribute | m7 | m8 | high | t4 internal compound -> base |

## 84

**caption_shape:** `tag-list-like`
**caption_id:** `3fcf2cc6b872a60103a0fa9cd041a37e58747dd4be0d298fb54cfac259f59c14`

> four women, beach, island, turquoise water

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | four women | four women | 0:10 |
| t1 | beach | beach | 12:17 |
| t2 | island | island | 19:25 |
| t3 | turquoise water | turquoise water | 27:42 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | four women | women | woman | ROOT | women | 0:2 | 0:10 |
| t1 | beach | beach | beach | ROOT | beach | 0:1 | 12:17 |
| t2 | island | island | island | ROOT | island | 0:1 | 19:25 |
| t3 | turquoise water | water | water | ROOT | water | 0:2 | 27:42 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | four | four | NUM | NUM | CD | CD | nummod | women | 1 | 0:4 |
| t0 | 1 | women | woman | NOUN | NOUN | NNS | NNS | ROOT | women | 1 | 5:10 |
| t1 | 0 | beach | beach | NOUN | NOUN | NN | NN | ROOT | beach | 0 | 12:17 |
| t2 | 0 | island | island | NOUN | NOUN | NN | NN | ROOT | island | 0 | 19:25 |
| t3 | 0 | turquoise | turquoise | NOUN | ADJ | NN | JJ | compound | water | 1 | 27:36 |
| t3 | 1 | water | water | NOUN | NOUN | NN | NN | ROOT | water | 1 | 37:42 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | women | woman | t0 | 1 | segment_head | high |
| m1 | quantity | four | four | t0 | 0 | exact_quantity | high |
| m2 | object | beach | beach | t1 | 0 | segment_head | high |
| m3 | object | island | island | t2 | 0 | segment_head | high |
| m4 | object | water | water | t3 | 1 | segment_head | high |
| m5 | attribute | turquoise | turquoise | t3 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | t0 internal nummod -> women |
| e1 | has_attribute | m4 | m5 | high | t3 internal compound -> water |

## 85

**caption_shape:** `tag-list-like`
**caption_id:** `4161c3fb3b79a5bec82d938c290ab6901f1716801e59b3578499ba911c4ea414`

> ancient pyramid, stone steps, green grass, tree shadows, jungle setting

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | ancient pyramid | ancient pyramid | 0:15 |
| t1 | stone steps | stone steps | 17:28 |
| t2 | green grass | green grass | 30:41 |
| t3 | tree shadows | tree shadows | 43:55 |
| t4 | jungle setting | jungle setting | 57:71 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | ancient pyramid | pyramid | pyramid | ROOT | pyramid | 0:2 | 0:15 |
| t1 | stone steps | steps | step | ROOT | steps | 0:2 | 17:28 |
| t2 | green grass | grass | grass | ROOT | grass | 0:2 | 30:41 |
| t3 | tree shadows | shadows | shadow | ROOT | shadows | 0:2 | 43:55 |
| t4 | jungle setting | setting | setting | ROOT | setting | 0:2 | 57:71 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | ancient | ancient | ADJ | ADJ | JJ | JJ | amod | pyramid | 1 | 0:7 |
| t0 | 1 | pyramid | pyramid | NOUN | NOUN | NN | NN | ROOT | pyramid | 1 | 8:15 |
| t1 | 0 | stone | stone | NOUN | NOUN | NN | NN | compound | steps | 1 | 17:22 |
| t1 | 1 | steps | step | NOUN | NOUN | NNS | NNS | ROOT | steps | 1 | 23:28 |
| t2 | 0 | green | green | ADJ | ADJ | JJ | JJ | amod | grass | 1 | 30:35 |
| t2 | 1 | grass | grass | NOUN | NOUN | NN | NN | ROOT | grass | 1 | 36:41 |
| t3 | 0 | tree | tree | NOUN | NOUN | NN | NN | compound | shadows | 1 | 43:47 |
| t3 | 1 | shadows | shadow | NOUN | NOUN | NNS | NNS | ROOT | shadows | 1 | 48:55 |
| t4 | 0 | jungle | jungle | NOUN | NOUN | NN | NN | compound | setting | 1 | 57:63 |
| t4 | 1 | setting | setting | NOUN | NOUN | NN | NN | ROOT | setting | 1 | 64:71 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | pyramid | pyramid | t0 | 1 | segment_head | high |
| m1 | attribute | ancient | ancient | t0 | 0 | attribute | high |
| m2 | object | steps | step | t1 | 1 | segment_head | high |
| m3 | attribute | stone | stone | t1 | 0 | attribute | high |
| m4 | object | grass | grass | t2 | 1 | segment_head | high |
| m5 | attribute | green | green | t2 | 0 | attribute | high |
| m6 | object | shadows | shadow | t3 | 1 | segment_head | high |
| m7 | attribute | tree | tree | t3 | 0 | attribute | high |
| m8 | context | setting | setting | t4 | 1 | scene_context | high |
| m9 | attribute | jungle | jungle | t4 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> pyramid |
| e1 | has_attribute | m2 | m3 | high | t1 internal compound -> steps |
| e2 | has_attribute | m4 | m5 | high | t2 internal amod -> grass |
| e3 | has_attribute | m6 | m7 | high | t3 internal compound -> shadows |
| e4 | has_context | scene | m8 | high | t4 context tag |
| e5 | has_attribute | m8 | m9 | high | t4 internal compound -> setting |

## 86

**caption_shape:** `multi-sentence`
**caption_id:** `41cf3165de139e05001208a95820ee600a8211e254de5226434227a9370a2c14`

> Two cricket players in white uniforms play on a grass field. One bats, the other runs toward the wicket.

### Sentences
| sentence | token_span |
| --- | --- |
| Two cricket players in white uniforms play on a grass field. | 0:12 |
| One bats, the other runs toward the wicket. | 12:22 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Two cricket players | players | player | nsubj | play | 0:3 |
| white uniforms | uniforms | uniform | pobj | in | 4:6 |
| a grass field | field | field | pobj | on | 8:11 |
| the wicket | wicket | wicket | pobj | toward | 19:21 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Two | two | NUM | CD | nummod | players | 2 |
| 1 | cricket | cricket | NOUN | NN | compound | players | 2 |
| 2 | players | player | NOUN | NNS | nsubj | play | 6 |
| 3 | in | in | ADP | IN | prep | players | 2 |
| 4 | white | white | ADJ | JJ | amod | uniforms | 5 |
| 5 | uniforms | uniform | NOUN | NNS | pobj | in | 3 |
| 6 | play | play | VERB | VBP | ROOT | play | 6 |
| 7 | on | on | ADP | IN | prep | play | 6 |
| 8 | a | a | DET | DT | det | field | 10 |
| 9 | grass | grass | NOUN | NN | compound | field | 10 |
| 10 | field | field | NOUN | NN | pobj | on | 7 |
| 11 | . | . | PUNCT | . | punct | play | 6 |
| 12 | One | one | NUM | CD | nsubj | bats | 13 |
| 13 | bats | bat | VERB | VBZ | ccomp | runs | 17 |
| 14 | , | , | PUNCT | , | punct | runs | 17 |
| 15 | the | the | DET | DT | det | other | 16 |
| 16 | other | other | ADJ | JJ | nsubj | runs | 17 |
| 17 | runs | run | VERB | VBZ | ROOT | runs | 17 |
| 18 | toward | toward | ADP | IN | prep | runs | 17 |
| 19 | the | the | DET | DT | det | wicket | 20 |
| 20 | wicket | wicket | NOUN | NN | pobj | toward | 18 |
| 21 | . | . | PUNCT | . | punct | runs | 17 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | players | player | chunk0 | 2 | noun_chunk_root | high |
| m1 | quantity | Two | two | chunk0 | 0 | exact_quantity | high |
| m2 | attribute | cricket | cricket | chunk0 | 1 | compound_modifier | medium |
| m3 | object | uniforms | uniform | chunk1 | 5 | noun_chunk_root | high |
| m4 | attribute | white | white | chunk1 | 4 | color_attribute | high |
| m5 | object | field | field | chunk2 | 10 | noun_chunk_root | high |
| m6 | attribute | grass | grass | chunk2 | 9 | compound_modifier | medium |
| m7 | object | wicket | wicket | chunk3 | 20 | noun_chunk_root | high |
| m8 | reference | other | other | nominal_reference | 16 | contrastive_reference | high |
| m9 | action | play | play | doc | 6 | verb_predicate | high |
| m10 | action | bats | bat | doc | 13 | verb_predicate | high |
| m11 | action | runs | run | doc | 17 | verb_predicate | high |

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

## 87

**caption_shape:** `multi-sentence`
**caption_id:** `43f23c61603ba21988593b02f24d0b27d1e8b7717ff3e41efe599cb785826c14`

> A large brick building with a sloped roof stands at the corner of a paved street. Trees and a low wall are visible to the left, while a few distant structures appear in the background under an overcast sky.

### Sentences
| sentence | token_span |
| --- | --- |
| A large brick building with a sloped roof stands at the corner of a paved street. | 0:17 |
| Trees and a low wall are visible to the left, while a few distant structures appear in the background under an overcast sky. | 17:42 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A large brick building | building | building | nsubj | stands | 0:4 |
| a sloped roof | roof | roof | pobj | with | 5:8 |
| the corner | corner | corner | pobj | at | 10:12 |
| a paved street | street | street | pobj | of | 13:16 |
| Trees | Trees | tree | nsubj | are | 17:18 |
| a low wall | wall | wall | conj | Trees | 19:22 |
| a few distant structures | structures | structure | nsubj | appear | 29:33 |
| the background | background | background | pobj | in | 35:37 |
| an overcast sky | sky | sky | pobj | under | 38:41 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | building | 3 |
| 1 | large | large | ADJ | JJ | amod | building | 3 |
| 2 | brick | brick | NOUN | NN | compound | building | 3 |
| 3 | building | building | NOUN | NN | nsubj | stands | 8 |
| 4 | with | with | ADP | IN | prep | building | 3 |
| 5 | a | a | DET | DT | det | roof | 7 |
| 6 | sloped | sloped | ADJ | JJ | amod | roof | 7 |
| 7 | roof | roof | NOUN | NN | pobj | with | 4 |
| 8 | stands | stand | VERB | VBZ | ROOT | stands | 8 |
| 9 | at | at | ADP | IN | prep | stands | 8 |
| 10 | the | the | DET | DT | det | corner | 11 |
| 11 | corner | corner | NOUN | NN | pobj | at | 9 |
| 12 | of | of | ADP | IN | prep | corner | 11 |
| 13 | a | a | DET | DT | det | street | 15 |
| 14 | paved | paved | ADJ | JJ | amod | street | 15 |
| 15 | street | street | NOUN | NN | pobj | of | 12 |
| 16 | . | . | PUNCT | . | punct | stands | 8 |
| 17 | Trees | tree | NOUN | NNS | nsubj | are | 22 |
| 18 | and | and | CCONJ | CC | cc | Trees | 17 |
| 19 | a | a | DET | DT | det | wall | 21 |
| 20 | low | low | ADJ | JJ | amod | wall | 21 |
| 21 | wall | wall | NOUN | NN | conj | Trees | 17 |
| 22 | are | be | AUX | VBP | ROOT | are | 22 |
| 23 | visible | visible | ADJ | JJ | acomp | are | 22 |
| 24 | to | to | ADP | IN | prep | are | 22 |
| 25 | the | the | DET | DT | det | left | 26 |
| 26 | left | left | ADJ | JJ | pobj | to | 24 |
| 27 | , | , | PUNCT | , | punct | are | 22 |
| 28 | while | while | SCONJ | IN | mark | appear | 33 |
| 29 | a | a | DET | DT | quantmod | few | 30 |
| 30 | few | few | ADJ | JJ | nummod | structures | 32 |
| 31 | distant | distant | ADJ | JJ | amod | structures | 32 |
| 32 | structures | structure | NOUN | NNS | nsubj | appear | 33 |
| 33 | appear | appear | VERB | VBP | advcl | are | 22 |
| 34 | in | in | ADP | IN | prep | appear | 33 |
| 35 | the | the | DET | DT | det | background | 36 |
| 36 | background | background | NOUN | NN | pobj | in | 34 |
| 37 | under | under | ADP | IN | prep | appear | 33 |
| 38 | an | an | DET | DT | det | sky | 40 |
| 39 | overcast | overcast | ADJ | JJ | amod | sky | 40 |
| 40 | sky | sky | NOUN | NN | pobj | under | 37 |
| 41 | . | . | PUNCT | . | punct | are | 22 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | chunk0 | 3 | noun_chunk_root | high |
| m1 | attribute | large | large | chunk0 | 1 | size_attribute | high |
| m2 | attribute | brick | brick | chunk0 | 2 | material_attribute | high |
| m3 | object | roof | roof | chunk1 | 7 | noun_chunk_root | high |
| m4 | attribute | sloped | sloped | chunk1 | 6 | modifier_attribute | medium |
| m5 | object | street | street | chunk3 | 15 | noun_chunk_root | high |
| m6 | attribute | paved | paved | chunk3 | 14 | visual_attribute | medium |
| m7 | object | Trees | tree | chunk4 | 17 | noun_chunk_root | high |
| m8 | object | wall | wall | chunk5 | 21 | noun_chunk_root | high |
| m9 | attribute | low | low | chunk5 | 20 | modifier_attribute | medium |
| m10 | object | structures | structure | chunk6 | 32 | noun_chunk_root | high |
| m11 | quantity | few | few | chunk6 | 30 | approximate_quantity | medium |
| m12 | attribute | distant | distant | chunk6 | 31 | modifier_attribute | medium |
| m13 | context | background | background | chunk7 | 36 | scene_context | high |
| m14 | object | sky | sky | chunk8 | 40 | noun_chunk_root | high |
| m15 | attribute | overcast | overcast | chunk8 | 39 | modifier_attribute | medium |
| m16 | action | stands | stand | doc | 8 | verb_predicate | high |
| m17 | action | appear | appear | doc | 33 | verb_predicate | high |

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

## 88

**caption_shape:** `tag-list-like`
**caption_id:** `45428ee1d9a35ad63241938ce5e4ffc58c9443946d4676f4c388c189a14c7814`

> top hats, crowd, men, seated, formal attire

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | top hats | top hats | 0:8 |
| t1 | crowd | crowd | 10:15 |
| t2 | men | men | 17:20 |
| t3 | seated | seated | 22:28 |
| t4 | formal attire | formal attire | 30:43 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | top hats | top hats | top_hat | ROOT | top hats | 0:1 | 0:8 |
| t1 | crowd | crowd | crowd | ROOT | crowd | 0:1 | 10:15 |
| t2 | men | men | men | ROOT | men | 0:1 | 17:20 |
| t4 | formal attire | attire | attire | ROOT | attire | 0:2 | 30:43 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | top hats | top_hat | NOUN | NOUN | NN | NN | ROOT | top hats | 0 | 0:8 |
| t1 | 0 | crowd | crowd | NOUN | NOUN | NN | NN | ROOT | crowd | 0 | 10:15 |
| t2 | 0 | men | men | NOUN | NOUN | NN | NNS | ROOT | men | 0 | 17:20 |
| t3 | 0 | seated | seat | VERB | ADJ | VBN | VBN | ROOT | seated | 0 | 22:28 |
| t4 | 0 | formal | formal | ADJ | ADJ | JJ | JJ | amod | attire | 1 | 30:36 |
| t4 | 1 | attire | attire | NOUN | NOUN | NN | NN | ROOT | attire | 1 | 37:43 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | top hats | top_hat | t0 | 0 | segment_head | high |
| m1 | object | crowd | crowd | t1 | 0 | segment_head | high |
| m2 | object | men | men | t2 | 0 | segment_head | high |
| m3 | attribute | seated | seat | t3 | 0 | floating_attribute | medium |
| m4 | object | attire | attire | t4 | 1 | segment_head | high |
| m5 | attribute | formal | formal | t4 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | candidate_has_attribute | m2 | m3 | low | t3 adjacent floating attribute |
| e1 | has_attribute | m4 | m5 | high | t4 internal amod -> attire |

## 89

**caption_shape:** `multi-sentence`
**caption_id:** `466babec43683bc6662ef5a0c610bc0e5f693f41da37b46f74f7aa0ca3b7d814`

> Several sea lions rest on a wooden dock near the water. Some are lying down, while others sit or stand, with the calm blue water visible behind them. A few sea lions are on a platform further back, near a wooden post.

### Sentences
| sentence | token_span |
| --- | --- |
| Several sea lions rest on a wooden dock near the water. | 0:11 |
| Some are lying down, while others sit or stand, with the calm blue water visible behind them. | 11:31 |
| A few sea lions are on a platform further back, near a wooden post. | 31:46 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| sea lions | sea lions | sea_lion | nsubj | rest | 1:2 |
| a wooden dock | dock | dock | pobj | on | 4:7 |
| the water | water | water | pobj | near | 8:10 |
| Some | Some | some | nsubj | lying | 11:12 |
| others | others | other | nsubj | sit | 17:18 |
| the calm blue water | water | water | nsubj | visible | 23:27 |
| them | them | they | pobj | behind | 29:30 |
| sea lions | sea lions | sea_lion | nsubj | are | 33:34 |
| a platform | platform | platform | pobj | on | 36:38 |
| a wooden post | post | post | pobj | near | 42:45 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Several | several | ADJ | JJ | amod | rest | 2 |
| 1 | sea lions | sea_lion | NOUN | NN | nsubj | rest | 2 |
| 2 | rest | rest | VERB | VBP | ROOT | rest | 2 |
| 3 | on | on | ADP | IN | prep | rest | 2 |
| 4 | a | a | DET | DT | det | dock | 6 |
| 5 | wooden | wooden | ADJ | JJ | amod | dock | 6 |
| 6 | dock | dock | NOUN | NN | pobj | on | 3 |
| 7 | near | near | ADP | IN | prep | rest | 2 |
| 8 | the | the | DET | DT | det | water | 9 |
| 9 | water | water | NOUN | NN | pobj | near | 7 |
| 10 | . | . | PUNCT | . | punct | rest | 2 |
| 11 | Some | some | PRON | DT | nsubj | lying | 13 |
| 12 | are | be | AUX | VBP | aux | lying | 13 |
| 13 | lying | lie | VERB | VBG | ROOT | lying | 13 |
| 14 | down | down | ADV | RB | prt | lying | 13 |
| 15 | , | , | PUNCT | , | punct | lying | 13 |
| 16 | while | while | SCONJ | IN | mark | sit | 18 |
| 17 | others | other | NOUN | NNS | nsubj | sit | 18 |
| 18 | sit | sit | VERB | VBP | advcl | lying | 13 |
| 19 | or | or | CCONJ | CC | cc | sit | 18 |
| 20 | stand | stand | VERB | VBP | conj | sit | 18 |
| 21 | , | , | PUNCT | , | punct | stand | 20 |
| 22 | with | with | SCONJ | IN | mark | visible | 27 |
| 23 | the | the | DET | DT | det | water | 26 |
| 24 | calm | calm | ADJ | JJ | amod | water | 26 |
| 25 | blue | blue | ADJ | JJ | amod | water | 26 |
| 26 | water | water | NOUN | NN | nsubj | visible | 27 |
| 27 | visible | visible | ADJ | JJ | conj | stand | 20 |
| 28 | behind | behind | ADP | IN | prep | visible | 27 |
| 29 | them | they | PRON | PRP | pobj | behind | 28 |
| 30 | . | . | PUNCT | . | punct | lying | 13 |
| 31 | A | a | DET | DT | quantmod | few | 32 |
| 32 | few | few | ADJ | JJ | amod | are | 34 |
| 33 | sea lions | sea_lion | NOUN | NN | nsubj | are | 34 |
| 34 | are | be | AUX | VBP | ROOT | are | 34 |
| 35 | on | on | ADP | IN | prep | are | 34 |
| 36 | a | a | DET | DT | det | platform | 37 |
| 37 | platform | platform | NOUN | NN | pobj | on | 35 |
| 38 | further | far | ADV | RBR | advmod | back | 39 |
| 39 | back | back | ADV | RB | advmod | platform | 37 |
| 40 | , | , | PUNCT | , | punct | platform | 37 |
| 41 | near | near | ADP | IN | prep | platform | 37 |
| 42 | a | a | DET | DT | det | post | 44 |
| 43 | wooden | wooden | ADJ | JJ | amod | post | 44 |
| 44 | post | post | NOUN | NN | pobj | near | 41 |
| 45 | . | . | PUNCT | . | punct | are | 34 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | sea lions | sea_lion | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | dock | dock | chunk1 | 6 | noun_chunk_root | high |
| m2 | attribute | wooden | wooden | chunk1 | 5 | material_attribute | high |
| m3 | object | water | water | chunk2 | 9 | noun_chunk_root | high |
| m4 | quantity | Some | some | chunk3 | 11 | indefinite_quantity | medium |
| m5 | object | water | water | chunk5 | 26 | noun_chunk_root | high |
| m6 | attribute | calm | calm | chunk5 | 24 | modifier_attribute | medium |
| m7 | attribute | blue | blue | chunk5 | 25 | color_attribute | high |
| m8 | object | sea lions | sea_lion | chunk7 | 33 | noun_chunk_root | high |
| m9 | object | platform | platform | chunk8 | 37 | noun_chunk_root | high |
| m10 | object | post | post | chunk9 | 44 | noun_chunk_root | high |
| m11 | attribute | wooden | wooden | chunk9 | 43 | material_attribute | high |
| m12 | action | rest | rest | doc | 2 | verb_predicate | high |
| m13 | action | lying | lie | doc | 13 | verb_predicate | high |
| m14 | action | sit | sit | doc | 18 | verb_predicate | high |
| m15 | action | stand | stand | doc | 20 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> dock |
| e1 | has_attribute | m5 | m6 | medium | chunk5 amod -> water |
| e2 | has_attribute | m5 | m7 | high | chunk5 amod -> water |
| e3 | has_attribute | m10 | m11 | high | chunk9 amod -> post |
| e4 | agent | m12 | m0 | medium | nsubj -> rest |
| e5 | relation | m0 | m1 | high | on |
| e6 | relation | m0 | m3 | high | near |
| e7 | relation | m8 | m9 | high | on |
| e8 | relation | m9 | m10 | high | near |

### Skipped Raw Concept Edges
_none_

## 90

**caption_shape:** `multi-sentence`
**caption_id:** `47fc5c5143d58519323971343cf2e71769a9cfc2caf6516465d258a6d88bc014`

> A man stands at a table, pointing to a screen showing video calls with several people. Others sit around the table in a modern room.

### Sentences
| sentence | token_span |
| --- | --- |
| A man stands at a table, pointing to a screen showing video calls with several people. | 0:18 |
| Others sit around the table in a modern room. | 18:28 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A man | man | man | nsubj | stands | 0:2 |
| a table | table | table | pobj | at | 4:6 |
| a screen | screen | screen | pobj | to | 9:11 |
| video calls | calls | call | dobj | showing | 12:14 |
| several people | people | people | pobj | with | 15:17 |
| Others | Others | other | nsubj | sit | 18:19 |
| the table | table | table | pobj | around | 21:23 |
| a modern room | room | room | pobj | in | 24:27 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | man | 1 |
| 1 | man | man | NOUN | NN | nsubj | stands | 2 |
| 2 | stands | stand | VERB | VBZ | ROOT | stands | 2 |
| 3 | at | at | ADP | IN | prep | stands | 2 |
| 4 | a | a | DET | DT | det | table | 5 |
| 5 | table | table | NOUN | NN | pobj | at | 3 |
| 6 | , | , | PUNCT | , | punct | stands | 2 |
| 7 | pointing | point | VERB | VBG | advcl | stands | 2 |
| 8 | to | to | ADP | IN | prep | pointing | 7 |
| 9 | a | a | DET | DT | det | screen | 10 |
| 10 | screen | screen | NOUN | NN | pobj | to | 8 |
| 11 | showing | show | VERB | VBG | acl | screen | 10 |
| 12 | video | video | NOUN | NN | compound | calls | 13 |
| 13 | calls | call | NOUN | NNS | dobj | showing | 11 |
| 14 | with | with | ADP | IN | prep | calls | 13 |
| 15 | several | several | ADJ | JJ | amod | people | 16 |
| 16 | people | people | NOUN | NNS | pobj | with | 14 |
| 17 | . | . | PUNCT | . | punct | stands | 2 |
| 18 | Others | other | NOUN | NNS | nsubj | sit | 19 |
| 19 | sit | sit | VERB | VBP | ROOT | sit | 19 |
| 20 | around | around | ADP | IN | prep | sit | 19 |
| 21 | the | the | DET | DT | det | table | 22 |
| 22 | table | table | NOUN | NN | pobj | around | 20 |
| 23 | in | in | ADP | IN | prep | sit | 19 |
| 24 | a | a | DET | DT | det | room | 26 |
| 25 | modern | modern | ADJ | JJ | amod | room | 26 |
| 26 | room | room | NOUN | NN | pobj | in | 23 |
| 27 | . | . | PUNCT | . | punct | sit | 19 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | table | table | chunk1 | 5 | noun_chunk_root | high |
| m2 | object | screen | screen | chunk2 | 10 | noun_chunk_root | high |
| m3 | object | calls | call | chunk3 | 13 | noun_chunk_root | high |
| m4 | attribute | video | video | chunk3 | 12 | compound_modifier | medium |
| m5 | object | people | people | chunk4 | 16 | noun_chunk_root | high |
| m6 | quantity | several | several | chunk4 | 15 | approximate_quantity | medium |
| m7 | object | table | table | chunk6 | 22 | noun_chunk_root | high |
| m8 | object | room | room | chunk7 | 26 | noun_chunk_root | high |
| m9 | attribute | modern | modern | chunk7 | 25 | modifier_attribute | medium |
| m10 | reference | Others | other | nominal_reference | 18 | contrastive_reference | high |
| m11 | action | stands | stand | doc | 2 | verb_predicate | high |
| m12 | action | pointing | point | doc | 7 | verb_predicate | high |
| m13 | action | showing | show | doc | 11 | verb_predicate | high |
| m14 | action | sit | sit | doc | 19 | verb_predicate | high |

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

## 91

**caption_shape:** `sentence-like`
**caption_id:** `482c9be0128cf7750aa70cd0831ac3ee03a6f39a18d1b8ab7347b2f724564c14`

> An old airplane with a bicycle frame hangs from the ceiling in a large indoor space.

### Sentences
| sentence | token_span |
| --- | --- |
| An old airplane with a bicycle frame hangs from the ceiling in a large indoor space. | 0:17 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| An old airplane | airplane | airplane | nsubj | hangs | 0:3 |
| a bicycle frame | frame | frame | pobj | with | 4:7 |
| the ceiling | ceiling | ceiling | pobj | from | 9:11 |
| a large indoor space | space | space | pobj | in | 12:16 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | An | an | DET | DT | det | airplane | 2 |
| 1 | old | old | ADJ | JJ | amod | airplane | 2 |
| 2 | airplane | airplane | NOUN | NN | nsubj | hangs | 7 |
| 3 | with | with | ADP | IN | prep | airplane | 2 |
| 4 | a | a | DET | DT | det | frame | 6 |
| 5 | bicycle | bicycle | NOUN | NN | compound | frame | 6 |
| 6 | frame | frame | NOUN | NN | pobj | with | 3 |
| 7 | hangs | hang | VERB | VBZ | ROOT | hangs | 7 |
| 8 | from | from | ADP | IN | prep | hangs | 7 |
| 9 | the | the | DET | DT | det | ceiling | 10 |
| 10 | ceiling | ceiling | NOUN | NN | pobj | from | 8 |
| 11 | in | in | ADP | IN | prep | hangs | 7 |
| 12 | a | a | DET | DT | det | space | 15 |
| 13 | large | large | ADJ | JJ | amod | space | 15 |
| 14 | indoor | indoor | ADJ | JJ | amod | space | 15 |
| 15 | space | space | NOUN | NN | pobj | in | 11 |
| 16 | . | . | PUNCT | . | punct | hangs | 7 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | airplane | airplane | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | old | old | chunk0 | 1 | visual_attribute | medium |
| m2 | object | frame | frame | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | bicycle | bicycle | chunk1 | 5 | compound_modifier | medium |
| m4 | object | ceiling | ceiling | chunk2 | 10 | noun_chunk_root | high |
| m5 | object | space | space | chunk3 | 15 | noun_chunk_root | high |
| m6 | attribute | large | large | chunk3 | 13 | size_attribute | high |
| m7 | attribute | indoor | indoor | chunk3 | 14 | modifier_attribute | medium |
| m8 | action | hangs | hang | doc | 7 | verb_predicate | high |

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

## 92

**caption_shape:** `multi-sentence`
**caption_id:** `48c9d293a0e9e6816cfba07c73fa10b8733db96f953058d04db0edef64064414`

> Several people sit at wooden tables outdoors, playing chess under trees. A young girl in a gray shirt is seated at a table with a chessboard in front of her, while others are focused on their games nearby. The setting is a sunny park-like area with buildings and greenery in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| Several people sit at wooden tables outdoors, playing chess under trees. | 0:13 |
| A young girl in a gray shirt is seated at a table with a chessboard in front of her, while others are focused on their games nearby. | 13:42 |
| The setting is a sunny park-like area with buildings and greenery in the background. | 42:57 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Several people | people | people | nsubj | sit | 0:2 |
| wooden tables | tables | table | pobj | at | 4:6 |
| chess | chess | chess | dobj | playing | 9:10 |
| trees | trees | tree | pobj | under | 11:12 |
| A young girl | girl | girl | nsubjpass | seated | 13:16 |
| a gray shirt | shirt | shirt | pobj | in | 17:20 |
| a table | table | table | pobj | at | 23:25 |
| a chessboard | chessboard | chessboard | pobj | with | 26:28 |
| front | front | front | pobj | in | 29:30 |
| her | her | she | pobj | of | 31:32 |
| others | others | other | nsubj | are | 34:35 |
| their games | games | game | pobj | on | 38:40 |
| The setting | setting | setting | nsubj | is | 42:44 |
| a sunny park-like area | area | area | attr | is | 45:49 |
| buildings | buildings | building | pobj | with | 50:51 |
| greenery | greenery | greenery | conj | buildings | 52:53 |
| the background | background | background | pobj | in | 54:56 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Several | several | ADJ | JJ | amod | people | 1 |
| 1 | people | people | NOUN | NNS | nsubj | sit | 2 |
| 2 | sit | sit | VERB | VBP | ROOT | sit | 2 |
| 3 | at | at | ADP | IN | prep | sit | 2 |
| 4 | wooden | wooden | ADJ | JJ | amod | tables | 5 |
| 5 | tables | table | NOUN | NNS | pobj | at | 3 |
| 6 | outdoors | outdoors | ADV | RB | advmod | sit | 2 |
| 7 | , | , | PUNCT | , | punct | sit | 2 |
| 8 | playing | play | VERB | VBG | advcl | sit | 2 |
| 9 | chess | chess | NOUN | NN | dobj | playing | 8 |
| 10 | under | under | ADP | IN | prep | playing | 8 |
| 11 | trees | tree | NOUN | NNS | pobj | under | 10 |
| 12 | . | . | PUNCT | . | punct | sit | 2 |
| 13 | A | a | DET | DT | det | girl | 15 |
| 14 | young | young | ADJ | JJ | amod | girl | 15 |
| 15 | girl | girl | NOUN | NN | nsubjpass | seated | 21 |
| 16 | in | in | ADP | IN | prep | girl | 15 |
| 17 | a | a | DET | DT | det | shirt | 19 |
| 18 | gray | gray | ADJ | JJ | amod | shirt | 19 |
| 19 | shirt | shirt | NOUN | NN | pobj | in | 16 |
| 20 | is | be | AUX | VBZ | auxpass | seated | 21 |
| 21 | seated | seat | VERB | VBN | ROOT | seated | 21 |
| 22 | at | at | ADP | IN | prep | seated | 21 |
| 23 | a | a | DET | DT | det | table | 24 |
| 24 | table | table | NOUN | NN | pobj | at | 22 |
| 25 | with | with | ADP | IN | prep | table | 24 |
| 26 | a | a | DET | DT | det | chessboard | 27 |
| 27 | chessboard | chessboard | NOUN | NN | pobj | with | 25 |
| 28 | in | in | ADP | IN | prep | chessboard | 27 |
| 29 | front | front | NOUN | NN | pobj | in | 28 |
| 30 | of | of | ADP | IN | prep | front | 29 |
| 31 | her | she | PRON | PRP | pobj | of | 30 |
| 32 | , | , | PUNCT | , | punct | seated | 21 |
| 33 | while | while | SCONJ | IN | mark | are | 35 |
| 34 | others | other | NOUN | NNS | nsubj | are | 35 |
| 35 | are | be | AUX | VBP | advcl | seated | 21 |
| 36 | focused | focus | VERB | VBN | acomp | are | 35 |
| 37 | on | on | ADP | IN | prep | focused | 36 |
| 38 | their | their | PRON | PRP$ | poss | games | 39 |
| 39 | games | game | NOUN | NNS | pobj | on | 37 |
| 40 | nearby | nearby | ADV | RB | advmod | games | 39 |
| 41 | . | . | PUNCT | . | punct | seated | 21 |
| 42 | The | the | DET | DT | det | setting | 43 |
| 43 | setting | setting | NOUN | NN | nsubj | is | 44 |
| 44 | is | be | AUX | VBZ | ROOT | is | 44 |
| 45 | a | a | DET | DT | det | area | 48 |
| 46 | sunny | sunny | ADJ | JJ | amod | area | 48 |
| 47 | park-like | park-like | ADJ | JJ | amod | area | 48 |
| 48 | area | area | NOUN | NN | attr | is | 44 |
| 49 | with | with | ADP | IN | prep | area | 48 |
| 50 | buildings | building | NOUN | NNS | pobj | with | 49 |
| 51 | and | and | CCONJ | CC | cc | buildings | 50 |
| 52 | greenery | greenery | NOUN | NN | conj | buildings | 50 |
| 53 | in | in | ADP | IN | prep | buildings | 50 |
| 54 | the | the | DET | DT | det | background | 55 |
| 55 | background | background | NOUN | NN | pobj | in | 53 |
| 56 | . | . | PUNCT | . | punct | is | 44 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Several | several | chunk0 | 0 | approximate_quantity | medium |
| m2 | object | tables | table | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | wooden | wooden | chunk1 | 4 | material_attribute | high |
| m4 | object | chess | chess | chunk2 | 9 | noun_chunk_root | high |
| m5 | object | trees | tree | chunk3 | 11 | noun_chunk_root | high |
| m6 | object | girl | girl | chunk4 | 15 | noun_chunk_root | high |
| m7 | attribute | young | young | chunk4 | 14 | modifier_attribute | medium |
| m8 | object | shirt | shirt | chunk5 | 19 | noun_chunk_root | high |
| m9 | attribute | gray | gray | chunk5 | 18 | color_attribute | high |
| m10 | object | table | table | chunk6 | 24 | noun_chunk_root | high |
| m11 | object | chessboard | chessboard | chunk7 | 27 | noun_chunk_root | high |
| m12 | object | games | game | chunk11 | 39 | noun_chunk_root | high |
| m13 | context | setting | setting | chunk12 | 43 | scene_context | high |
| m14 | object | area | area | chunk13 | 48 | noun_chunk_root | high |
| m15 | attribute | sunny | sunny | chunk13 | 46 | modifier_attribute | medium |
| m16 | attribute | park-like | park-like | chunk13 | 47 | modifier_attribute | medium |
| m17 | object | buildings | building | chunk14 | 50 | noun_chunk_root | high |
| m18 | object | greenery | greenery | chunk15 | 52 | noun_chunk_root | high |
| m19 | context | background | background | chunk16 | 55 | scene_context | high |
| m20 | context | outdoors | outdoors | doc | 6 | scene_context | high |
| m21 | reference | others | other | nominal_reference | 34 | contrastive_reference | high |
| m22 | action | sit | sit | doc | 2 | verb_predicate | high |
| m23 | action | playing | play | doc | 8 | verb_predicate | high |
| m24 | action | seated | seat | doc | 21 | verb_predicate | high |
| m25 | action | focused | focus | doc | 36 | verb_predicate | high |

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

## 93

**caption_shape:** `sentence-like`
**caption_id:** `4bfd0342561c4cded12246ed215bdbe897f68be5c3f69a52dbfbc1b45cdc7414`

> People sit at tables in a room, with one woman in bright yellow pants standing near a man in a plaid shirt.

### Sentences
| sentence | token_span |
| --- | --- |
| People sit at tables in a room, with one woman in bright yellow pants standing near a man in a plaid shirt. | 0:24 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| People | People | People | nsubj | sit | 0:1 |
| tables | tables | table | pobj | at | 3:4 |
| a room | room | room | pobj | in | 5:7 |
| one woman | woman | woman | nsubj | standing | 9:11 |
| bright yellow pants | pants | pant | pobj | in | 12:15 |
| a man | man | man | pobj | near | 17:19 |
| a plaid shirt | shirt | shirt | pobj | in | 20:23 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | People | People | NOUN | NNS | nsubj | sit | 1 |
| 1 | sit | sit | VERB | VBP | ROOT | sit | 1 |
| 2 | at | at | ADP | IN | prep | sit | 1 |
| 3 | tables | table | NOUN | NNS | pobj | at | 2 |
| 4 | in | in | ADP | IN | prep | sit | 1 |
| 5 | a | a | DET | DT | det | room | 6 |
| 6 | room | room | NOUN | NN | pobj | in | 4 |
| 7 | , | , | PUNCT | , | punct | sit | 1 |
| 8 | with | with | ADP | IN | prep | sit | 1 |
| 9 | one | one | NUM | CD | nummod | woman | 10 |
| 10 | woman | woman | NOUN | NN | nsubj | standing | 15 |
| 11 | in | in | ADP | IN | prep | woman | 10 |
| 12 | bright | bright | ADJ | JJ | amod | yellow | 13 |
| 13 | yellow | yellow | ADJ | JJ | amod | pants | 14 |
| 14 | pants | pant | NOUN | NNS | pobj | in | 11 |
| 15 | standing | stand | VERB | VBG | pcomp | with | 8 |
| 16 | near | near | ADP | IN | prep | standing | 15 |
| 17 | a | a | DET | DT | det | man | 18 |
| 18 | man | man | NOUN | NN | pobj | near | 16 |
| 19 | in | in | ADP | IN | prep | man | 18 |
| 20 | a | a | DET | DT | det | shirt | 22 |
| 21 | plaid | plaid | ADJ | JJ | amod | shirt | 22 |
| 22 | shirt | shirt | NOUN | NN | pobj | in | 19 |
| 23 | . | . | PUNCT | . | punct | sit | 1 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | People | people | chunk0 | 0 | noun_chunk_root | high |
| m1 | object | tables | table | chunk1 | 3 | noun_chunk_root | high |
| m2 | object | room | room | chunk2 | 6 | noun_chunk_root | high |
| m3 | object | woman | woman | chunk3 | 10 | noun_chunk_root | high |
| m4 | quantity | one | one | chunk3 | 9 | exact_quantity | high |
| m5 | object | pants | pant | chunk4 | 14 | noun_chunk_root | high |
| m6 | attribute | bright | bright | chunk4 | 12 | visual_attribute | medium |
| m7 | attribute | yellow | yellow | chunk4 | 13 | color_attribute | high |
| m8 | object | man | man | chunk5 | 18 | noun_chunk_root | high |
| m9 | object | shirt | shirt | chunk6 | 22 | noun_chunk_root | high |
| m10 | attribute | plaid | plaid | chunk6 | 21 | modifier_attribute | medium |
| m11 | action | sit | sit | doc | 1 | verb_predicate | high |
| m12 | action | standing | stand | doc | 15 | verb_predicate | high |

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

## 94

**caption_shape:** `sentence-like`
**caption_id:** `4c03ab0fe6b9ecbdf3f5eba512d6bab380a75a7b12f710780f3e67e2c1e38414`

> Three runners compete on an indoor track, with one in an orange jersey and another in a gold and blue uniform.

### Sentences
| sentence | token_span |
| --- | --- |
| Three runners compete on an indoor track, with one in an orange jersey and another in a gold and blue uniform. | 0:23 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Three runners | runners | runner | nsubj | compete | 0:2 |
| an indoor track | track | track | pobj | on | 4:7 |
| an orange jersey | jersey | jersey | pobj | in | 11:14 |
| another | another | another | conj | one | 15:16 |
| a gold and blue uniform | uniform | uniform | pobj | in | 17:22 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Three | three | NUM | CD | nummod | runners | 1 |
| 1 | runners | runner | NOUN | NNS | nsubj | compete | 2 |
| 2 | compete | compete | VERB | VBP | ROOT | compete | 2 |
| 3 | on | on | ADP | IN | prep | compete | 2 |
| 4 | an | an | DET | DT | det | track | 6 |
| 5 | indoor | indoor | ADJ | JJ | amod | track | 6 |
| 6 | track | track | NOUN | NN | pobj | on | 3 |
| 7 | , | , | PUNCT | , | punct | compete | 2 |
| 8 | with | with | ADP | IN | prep | compete | 2 |
| 9 | one | one | NUM | CD | pobj | with | 8 |
| 10 | in | in | ADP | IN | prep | one | 9 |
| 11 | an | an | DET | DT | det | jersey | 13 |
| 12 | orange | orange | ADJ | JJ | amod | jersey | 13 |
| 13 | jersey | jersey | NOUN | NN | pobj | in | 10 |
| 14 | and | and | CCONJ | CC | cc | one | 9 |
| 15 | another | another | PRON | DT | conj | one | 9 |
| 16 | in | in | ADP | IN | prep | another | 15 |
| 17 | a | a | DET | DT | det | uniform | 21 |
| 18 | gold | gold | ADJ | JJ | amod | uniform | 21 |
| 19 | and | and | CCONJ | CC | cc | gold | 18 |
| 20 | blue | blue | ADJ | JJ | conj | gold | 18 |
| 21 | uniform | uniform | NOUN | NN | pobj | in | 16 |
| 22 | . | . | PUNCT | . | punct | compete | 2 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | runners | runner | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Three | three | chunk0 | 0 | exact_quantity | high |
| m2 | object | track | track | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | indoor | indoor | chunk1 | 5 | modifier_attribute | medium |
| m4 | object | jersey | jersey | chunk2 | 13 | noun_chunk_root | high |
| m5 | attribute | orange | orange | chunk2 | 12 | color_attribute | high |
| m6 | object | uniform | uniform | chunk4 | 21 | noun_chunk_root | high |
| m7 | attribute | gold | gold | chunk4 | 18 | color_attribute | high |
| m8 | attribute | blue | blue | chunk4 | 20 | color_attribute | high |
| m9 | reference | one | one | nominal_reference | 9 | singular_substitute | high |
| m10 | reference | another | another | nominal_reference | 15 | contrastive_reference | high |
| m11 | action | compete | compete | doc | 2 | verb_predicate | high |

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

## 95

**caption_shape:** `multi-sentence`
**caption_id:** `4e942957441ee06442c3d3cfc0720fc33d15d3a18bb37504d895e759c98da014`

> Two bronze military badges show a sunburst design with a crown and text. They are placed on a plain white surface.

### Sentences
| sentence | token_span |
| --- | --- |
| Two bronze military badges show a sunburst design with a crown and text. | 0:14 |
| They are placed on a plain white surface. | 14:23 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Two bronze military badges | badges | badge | nsubj | show | 0:4 |
| a sunburst design | design | design | dobj | show | 5:8 |
| a crown | crown | crown | pobj | with | 9:11 |
| text | text | text | conj | crown | 12:13 |
| They | They | they | nsubjpass | placed | 14:15 |
| a plain white surface | surface | surface | pobj | on | 18:22 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Two | two | NUM | CD | nummod | badges | 3 |
| 1 | bronze | bronze | NOUN | NN | nmod | badges | 3 |
| 2 | military | military | ADJ | JJ | amod | badges | 3 |
| 3 | badges | badge | NOUN | NNS | nsubj | show | 4 |
| 4 | show | show | VERB | VBP | ROOT | show | 4 |
| 5 | a | a | DET | DT | det | design | 7 |
| 6 | sunburst | sunburst | NOUN | NN | compound | design | 7 |
| 7 | design | design | NOUN | NN | dobj | show | 4 |
| 8 | with | with | ADP | IN | prep | design | 7 |
| 9 | a | a | DET | DT | det | crown | 10 |
| 10 | crown | crown | NOUN | NN | pobj | with | 8 |
| 11 | and | and | CCONJ | CC | cc | crown | 10 |
| 12 | text | text | NOUN | NN | conj | crown | 10 |
| 13 | . | . | PUNCT | . | punct | show | 4 |
| 14 | They | they | PRON | PRP | nsubjpass | placed | 16 |
| 15 | are | be | AUX | VBP | auxpass | placed | 16 |
| 16 | placed | place | VERB | VBN | ROOT | placed | 16 |
| 17 | on | on | ADP | IN | prep | placed | 16 |
| 18 | a | a | DET | DT | det | surface | 21 |
| 19 | plain | plain | ADJ | JJ | amod | white | 20 |
| 20 | white | white | ADJ | JJ | amod | surface | 21 |
| 21 | surface | surface | NOUN | NN | pobj | on | 17 |
| 22 | . | . | PUNCT | . | punct | placed | 16 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | badges | badge | chunk0 | 3 | noun_chunk_root | high |
| m1 | quantity | Two | two | chunk0 | 0 | exact_quantity | high |
| m2 | attribute | military | military | chunk0 | 2 | modifier_attribute | medium |
| m3 | object | design | design | chunk1 | 7 | noun_chunk_root | high |
| m4 | attribute | sunburst | sunburst | chunk1 | 6 | compound_modifier | medium |
| m5 | object | crown | crown | chunk2 | 10 | noun_chunk_root | high |
| m6 | object | text | text | chunk3 | 12 | noun_chunk_root | high |
| m7 | context | surface | surface | chunk5 | 21 | spatial_region | medium |
| m8 | action | show | show | doc | 4 | verb_predicate | high |
| m9 | action | placed | place | doc | 16 | verb_predicate | high |

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

## 96

**caption_shape:** `multi-sentence`
**caption_id:** `4ef94ef77dceaed5575f2fab38c07ce284810be3c71dde7af7e464bd0ccc8414`

> A snow-covered sidewalk runs between parked cars and a house. A silver SUV is parked on the right, with a large bush and snow piled beside it. The street is lined with bare trees and houses under a dusky sky.

### Sentences
| sentence | token_span |
| --- | --- |
| A snow-covered sidewalk runs between parked cars and a house. | 0:11 |
| A silver SUV is parked on the right, with a large bush and snow piled beside it. | 11:30 |
| The street is lined with bare trees and houses under a dusky sky. | 30:44 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A snow-covered sidewalk | sidewalk | sidewalk | nsubj | runs | 0:3 |
| parked cars | cars | car | pobj | between | 5:7 |
| a house | house | house | conj | cars | 8:10 |
| A silver SUV | SUV | SUV | nsubjpass | parked | 11:14 |
| the right | right | right | pobj | on | 17:19 |
| a large bush | bush | bush | pobj | with | 21:24 |
| snow | snow | snow | conj | bush | 25:26 |
| it | it | it | pobj | beside | 28:29 |
| The street | street | street | nsubjpass | lined | 30:32 |
| bare trees | trees | tree | pobj | with | 35:37 |
| houses | houses | house | conj | trees | 38:39 |
| a dusky sky | sky | sky | pobj | under | 40:43 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | sidewalk | 2 |
| 1 | snow-covered | snow-covered | NOUN | NN | amod | sidewalk | 2 |
| 2 | sidewalk | sidewalk | NOUN | NN | nsubj | runs | 3 |
| 3 | runs | run | VERB | VBZ | ROOT | runs | 3 |
| 4 | between | between | ADP | IN | prep | runs | 3 |
| 5 | parked | park | VERB | VBN | amod | cars | 6 |
| 6 | cars | car | NOUN | NNS | pobj | between | 4 |
| 7 | and | and | CCONJ | CC | cc | cars | 6 |
| 8 | a | a | DET | DT | det | house | 9 |
| 9 | house | house | NOUN | NN | conj | cars | 6 |
| 10 | . | . | PUNCT | . | punct | runs | 3 |
| 11 | A | a | DET | DT | det | SUV | 13 |
| 12 | silver | silver | ADJ | JJ | amod | SUV | 13 |
| 13 | SUV | SUV | PROPN | NNP | nsubjpass | parked | 15 |
| 14 | is | be | AUX | VBZ | auxpass | parked | 15 |
| 15 | parked | park | VERB | VBN | ROOT | parked | 15 |
| 16 | on | on | ADP | IN | prep | parked | 15 |
| 17 | the | the | DET | DT | det | right | 18 |
| 18 | right | right | NOUN | NN | pobj | on | 16 |
| 19 | , | , | PUNCT | , | punct | parked | 15 |
| 20 | with | with | ADP | IN | prep | parked | 15 |
| 21 | a | a | DET | DT | det | bush | 23 |
| 22 | large | large | ADJ | JJ | amod | bush | 23 |
| 23 | bush | bush | NOUN | NN | pobj | with | 20 |
| 24 | and | and | CCONJ | CC | cc | bush | 23 |
| 25 | snow | snow | NOUN | NN | conj | bush | 23 |
| 26 | piled | pile | VERB | VBN | acl | bush | 23 |
| 27 | beside | beside | ADP | IN | prep | piled | 26 |
| 28 | it | it | PRON | PRP | pobj | beside | 27 |
| 29 | . | . | PUNCT | . | punct | parked | 15 |
| 30 | The | the | DET | DT | det | street | 31 |
| 31 | street | street | NOUN | NN | nsubjpass | lined | 33 |
| 32 | is | be | AUX | VBZ | auxpass | lined | 33 |
| 33 | lined | line | VERB | VBN | ROOT | lined | 33 |
| 34 | with | with | ADP | IN | prep | lined | 33 |
| 35 | bare | bare | ADJ | JJ | amod | trees | 36 |
| 36 | trees | tree | NOUN | NNS | pobj | with | 34 |
| 37 | and | and | CCONJ | CC | cc | trees | 36 |
| 38 | houses | house | NOUN | NNS | conj | trees | 36 |
| 39 | under | under | ADP | IN | prep | houses | 38 |
| 40 | a | a | DET | DT | det | sky | 42 |
| 41 | dusky | dusky | ADJ | JJ | amod | sky | 42 |
| 42 | sky | sky | NOUN | NN | pobj | under | 39 |
| 43 | . | . | PUNCT | . | punct | lined | 33 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | sidewalk | sidewalk | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | snow-covered | snow-covered | chunk0 | 1 | modifier_attribute | medium |
| m2 | object | cars | car | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | parked | park | chunk1 | 5 | state_attribute | medium |
| m4 | object | house | house | chunk2 | 9 | noun_chunk_root | high |
| m5 | object | SUV | suv | chunk3 | 13 | noun_chunk_root | high |
| m6 | attribute | silver | silver | chunk3 | 12 | color_attribute | high |
| m7 | context | right | right | chunk4 | 18 | spatial_region | medium |
| m8 | object | bush | bush | chunk5 | 23 | noun_chunk_root | high |
| m9 | attribute | large | large | chunk5 | 22 | size_attribute | high |
| m10 | object | snow | snow | chunk6 | 25 | noun_chunk_root | high |
| m11 | object | street | street | chunk8 | 31 | noun_chunk_root | high |
| m12 | object | trees | tree | chunk9 | 36 | noun_chunk_root | high |
| m13 | attribute | bare | bare | chunk9 | 35 | visual_attribute | medium |
| m14 | object | houses | house | chunk10 | 38 | noun_chunk_root | high |
| m15 | object | sky | sky | chunk11 | 42 | noun_chunk_root | high |
| m16 | attribute | dusky | dusky | chunk11 | 41 | modifier_attribute | medium |
| m17 | action | runs | run | doc | 3 | verb_predicate | high |
| m18 | action | parked | park | doc | 15 | verb_predicate | high |
| m19 | action | piled | pile | doc | 26 | verb_predicate | high |
| m20 | action | lined | line | doc | 33 | verb_predicate | high |

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

## 97

**caption_shape:** `multi-sentence`
**caption_id:** `51d7da189059dc55749d66b73dd715b598f2b475ef29bd301d4d1ae312bee414`

> A skier in an orange helmet races down a snowy slope. Other skiers are visible in the background on the mountain.

### Sentences
| sentence | token_span |
| --- | --- |
| A skier in an orange helmet races down a snowy slope. | 0:12 |
| Other skiers are visible in the background on the mountain. | 12:23 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A skier | skier | skier | nsubj | races | 0:2 |
| an orange helmet | helmet | helmet | pobj | in | 3:6 |
| a snowy slope | slope | slope | pobj | down | 8:11 |
| Other skiers | skiers | skier | nsubj | are | 12:14 |
| the background | background | background | pobj | in | 17:19 |
| the mountain | mountain | mountain | pobj | on | 20:22 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | skier | 1 |
| 1 | skier | skier | NOUN | NN | nsubj | races | 6 |
| 2 | in | in | ADP | IN | prep | skier | 1 |
| 3 | an | an | DET | DT | det | helmet | 5 |
| 4 | orange | orange | ADJ | JJ | amod | helmet | 5 |
| 5 | helmet | helmet | NOUN | NN | pobj | in | 2 |
| 6 | races | race | VERB | VBZ | ROOT | races | 6 |
| 7 | down | down | ADP | IN | prep | races | 6 |
| 8 | a | a | DET | DT | det | slope | 10 |
| 9 | snowy | snowy | ADJ | JJ | amod | slope | 10 |
| 10 | slope | slope | NOUN | NN | pobj | down | 7 |
| 11 | . | . | PUNCT | . | punct | races | 6 |
| 12 | Other | other | ADJ | JJ | amod | skiers | 13 |
| 13 | skiers | skier | NOUN | NNS | nsubj | are | 14 |
| 14 | are | be | AUX | VBP | ROOT | are | 14 |
| 15 | visible | visible | ADJ | JJ | acomp | are | 14 |
| 16 | in | in | ADP | IN | prep | are | 14 |
| 17 | the | the | DET | DT | det | background | 18 |
| 18 | background | background | NOUN | NN | pobj | in | 16 |
| 19 | on | on | ADP | IN | prep | background | 18 |
| 20 | the | the | DET | DT | det | mountain | 21 |
| 21 | mountain | mountain | NOUN | NN | pobj | on | 19 |
| 22 | . | . | PUNCT | . | punct | are | 14 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | skier | skier | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | helmet | helmet | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | orange | orange | chunk1 | 4 | color_attribute | high |
| m3 | object | slope | slope | chunk2 | 10 | noun_chunk_root | high |
| m4 | attribute | snowy | snowy | chunk2 | 9 | modifier_attribute | medium |
| m5 | object | skiers | skier | chunk3 | 13 | noun_chunk_root | high |
| m6 | attribute | Other | other | chunk3 | 12 | modifier_attribute | medium |
| m7 | context | background | background | chunk4 | 18 | scene_context | high |
| m8 | object | mountain | mountain | chunk5 | 21 | noun_chunk_root | high |
| m9 | action | races | race | doc | 6 | verb_predicate | high |

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

## 98

**caption_shape:** `sentence-like`
**caption_id:** `521fef55b6e923e6376bef8ab4a4158436176b892a5537365ca12f4670742014`

> A football team in white uniforms stands on the field with a referee nearby.

### Sentences
| sentence | token_span |
| --- | --- |
| A football team in white uniforms stands on the field with a referee nearby. | 0:15 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A football team | team | team | nsubj | stands | 0:3 |
| white uniforms | uniforms | uniform | pobj | in | 4:6 |
| the field | field | field | pobj | on | 8:10 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | team | 2 |
| 1 | football | football | NOUN | NN | compound | team | 2 |
| 2 | team | team | NOUN | NN | nsubj | stands | 6 |
| 3 | in | in | ADP | IN | prep | team | 2 |
| 4 | white | white | ADJ | JJ | amod | uniforms | 5 |
| 5 | uniforms | uniform | NOUN | NNS | pobj | in | 3 |
| 6 | stands | stand | VERB | VBZ | ROOT | stands | 6 |
| 7 | on | on | ADP | IN | prep | stands | 6 |
| 8 | the | the | DET | DT | det | field | 9 |
| 9 | field | field | NOUN | NN | pobj | on | 7 |
| 10 | with | with | SCONJ | IN | mark | referee | 12 |
| 11 | a | a | DET | DT | det | referee | 12 |
| 12 | referee | referee | NOUN | NN | advcl | stands | 6 |
| 13 | nearby | nearby | ADV | RB | advmod | referee | 12 |
| 14 | . | . | PUNCT | . | punct | stands | 6 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | team | team | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | football | football | chunk0 | 1 | compound_modifier | medium |
| m2 | object | uniforms | uniform | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | white | white | chunk1 | 4 | color_attribute | high |
| m4 | object | field | field | chunk2 | 9 | noun_chunk_root | high |
| m5 | action | stands | stand | doc | 6 | verb_predicate | high |
| m6 | object | referee | referee | with_absolute10 | 12 | with_absolute_recovered_object | medium |

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

## 99

**caption_shape:** `multi-sentence`
**caption_id:** `526c45c3e9f454f37c321a0e77be015a03b5384b98c2d52132db519bd9b88c14`

> A woman in a red and black bikini jumps to hit a volleyball over the net on a sandy beach. Other people are visible in the background under white umbrellas, with the sun shining brightly overhead.

### Sentences
| sentence | token_span |
| --- | --- |
| A woman in a red and black bikini jumps to hit a volleyball over the net on a sandy beach. | 0:21 |
| Other people are visible in the background under white umbrellas, with the sun shining brightly overhead. | 21:39 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A woman | woman | woman | nsubj | jumps | 0:2 |
| a red and black bikini | bikini | bikini | pobj | in | 3:8 |
| a volleyball | volleyball | volleyball | dobj | hit | 11:13 |
| the net | net | net | pobj | over | 14:16 |
| a sandy beach | beach | beach | pobj | on | 17:20 |
| Other people | people | people | nsubj | are | 21:23 |
| the background | background | background | pobj | in | 26:28 |
| white umbrellas | umbrellas | umbrella | pobj | under | 29:31 |
| the sun | sun | sun | nsubj | shining | 33:35 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | woman | 1 |
| 1 | woman | woman | NOUN | NN | nsubj | jumps | 8 |
| 2 | in | in | ADP | IN | prep | woman | 1 |
| 3 | a | a | DET | DT | det | bikini | 7 |
| 4 | red | red | ADJ | JJ | amod | bikini | 7 |
| 5 | and | and | CCONJ | CC | cc | red | 4 |
| 6 | black | black | ADJ | JJ | conj | red | 4 |
| 7 | bikini | bikini | NOUN | NN | pobj | in | 2 |
| 8 | jumps | jump | VERB | VBZ | ROOT | jumps | 8 |
| 9 | to | to | PART | TO | aux | hit | 10 |
| 10 | hit | hit | VERB | VB | advcl | jumps | 8 |
| 11 | a | a | DET | DT | det | volleyball | 12 |
| 12 | volleyball | volleyball | NOUN | NN | dobj | hit | 10 |
| 13 | over | over | ADP | IN | prep | hit | 10 |
| 14 | the | the | DET | DT | det | net | 15 |
| 15 | net | net | NOUN | NN | pobj | over | 13 |
| 16 | on | on | ADP | IN | prep | hit | 10 |
| 17 | a | a | DET | DT | det | beach | 19 |
| 18 | sandy | sandy | ADJ | JJ | amod | beach | 19 |
| 19 | beach | beach | NOUN | NN | pobj | on | 16 |
| 20 | . | . | PUNCT | . | punct | jumps | 8 |
| 21 | Other | other | ADJ | JJ | amod | people | 22 |
| 22 | people | people | NOUN | NNS | nsubj | are | 23 |
| 23 | are | be | AUX | VBP | ROOT | are | 23 |
| 24 | visible | visible | ADJ | JJ | acomp | are | 23 |
| 25 | in | in | ADP | IN | prep | are | 23 |
| 26 | the | the | DET | DT | det | background | 27 |
| 27 | background | background | NOUN | NN | pobj | in | 25 |
| 28 | under | under | ADP | IN | prep | are | 23 |
| 29 | white | white | ADJ | JJ | amod | umbrellas | 30 |
| 30 | umbrellas | umbrella | NOUN | NNS | pobj | under | 28 |
| 31 | , | , | PUNCT | , | punct | are | 23 |
| 32 | with | with | ADP | IN | prep | are | 23 |
| 33 | the | the | DET | DT | det | sun | 34 |
| 34 | sun | sun | NOUN | NN | nsubj | shining | 35 |
| 35 | shining | shin | VERB | VBG | pcomp | with | 32 |
| 36 | brightly | brightly | ADV | RB | advmod | shining | 35 |
| 37 | overhead | overhead | ADV | RB | advmod | shining | 35 |
| 38 | . | . | PUNCT | . | punct | are | 23 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | bikini | bikini | chunk1 | 7 | noun_chunk_root | high |
| m2 | attribute | red | red | chunk1 | 4 | color_attribute | high |
| m3 | attribute | black | black | chunk1 | 6 | color_attribute | high |
| m4 | object | volleyball | volleyball | chunk2 | 12 | noun_chunk_root | high |
| m5 | object | net | net | chunk3 | 15 | noun_chunk_root | high |
| m6 | object | beach | beach | chunk4 | 19 | noun_chunk_root | high |
| m7 | attribute | sandy | sandy | chunk4 | 18 | modifier_attribute | medium |
| m8 | object | people | people | chunk5 | 22 | noun_chunk_root | high |
| m9 | attribute | Other | other | chunk5 | 21 | modifier_attribute | medium |
| m10 | context | background | background | chunk6 | 27 | scene_context | high |
| m11 | object | umbrellas | umbrella | chunk7 | 30 | noun_chunk_root | high |
| m12 | attribute | white | white | chunk7 | 29 | color_attribute | high |
| m13 | object | sun | sun | chunk8 | 34 | noun_chunk_root | high |
| m14 | action | jumps | jump | doc | 8 | verb_predicate | high |
| m15 | action | hit | hit | doc | 10 | verb_predicate | high |
| m16 | action | shining | shin | doc | 35 | verb_predicate | high |

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

## 100

**caption_shape:** `multi-sentence`
**caption_id:** `528344da5e40f3da37b258a8808a079d436258cfb3f3f2fe991db7fb1672c014`

> A lacrosse player in a white uniform runs through heavy snow on a snowy field. Another player in red is nearby.

### Sentences
| sentence | token_span |
| --- | --- |
| A lacrosse player in a white uniform runs through heavy snow on a snowy field. | 0:16 |
| Another player in red is nearby. | 16:23 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A lacrosse player | player | player | nsubj | runs | 0:3 |
| a white uniform | uniform | uniform | pobj | in | 4:7 |
| heavy snow | snow | snow | pobj | through | 9:11 |
| a snowy field | field | field | pobj | on | 12:15 |
| Another player | player | player | nsubj | is | 16:18 |
| red | red | red | pobj | in | 19:20 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | player | 2 |
| 1 | lacrosse | lacrosse | NOUN | NN | compound | player | 2 |
| 2 | player | player | NOUN | NN | nsubj | runs | 7 |
| 3 | in | in | ADP | IN | prep | player | 2 |
| 4 | a | a | DET | DT | det | uniform | 6 |
| 5 | white | white | ADJ | JJ | amod | uniform | 6 |
| 6 | uniform | uniform | NOUN | NN | pobj | in | 3 |
| 7 | runs | run | VERB | VBZ | ROOT | runs | 7 |
| 8 | through | through | ADP | IN | prep | runs | 7 |
| 9 | heavy | heavy | ADJ | JJ | amod | snow | 10 |
| 10 | snow | snow | NOUN | NN | pobj | through | 8 |
| 11 | on | on | ADP | IN | prep | runs | 7 |
| 12 | a | a | DET | DT | det | field | 14 |
| 13 | snowy | snowy | ADJ | JJ | amod | field | 14 |
| 14 | field | field | NOUN | NN | pobj | on | 11 |
| 15 | . | . | PUNCT | . | punct | runs | 7 |
| 16 | Another | another | DET | DT | det | player | 17 |
| 17 | player | player | NOUN | NN | nsubj | is | 20 |
| 18 | in | in | ADP | IN | prep | player | 17 |
| 19 | red | red | NOUN | NN | pobj | in | 18 |
| 20 | is | be | AUX | VBZ | ROOT | is | 20 |
| 21 | nearby | nearby | ADV | RB | advmod | is | 20 |
| 22 | . | . | PUNCT | . | punct | is | 20 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | player | player | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | lacrosse | lacrosse | chunk0 | 1 | compound_modifier | medium |
| m2 | object | uniform | uniform | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | white | white | chunk1 | 5 | color_attribute | high |
| m4 | object | snow | snow | chunk2 | 10 | noun_chunk_root | high |
| m5 | attribute | heavy | heavy | chunk2 | 9 | modifier_attribute | medium |
| m6 | object | field | field | chunk3 | 14 | noun_chunk_root | high |
| m7 | attribute | snowy | snowy | chunk3 | 13 | modifier_attribute | medium |
| m8 | object | player | player | chunk4 | 17 | noun_chunk_root | high |
| m9 | attribute | red | red | chunk5 | 19 | color_attribute | high |
| m10 | action | runs | run | doc | 7 | verb_predicate | high |

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
