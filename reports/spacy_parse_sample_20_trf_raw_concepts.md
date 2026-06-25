# spaCy Parse Inspection

- input: `data\gpic_captions_test\val\gpic_val_00000.jsonl.gz`
- model: `en_core_web_trf`
- max_records: `20`
- mask_quotes: `True`
- quote_placeholder: `the quoted text`
- parse_tag_lists: `True`

## 01

**caption_shape:** `sentence-like`
**caption_id:** `005a13525e45210df2a71777a9060032b3221dbee0e39d5344213385b23c8814`

> A person with dreadlocks and a red bow sits at a table with art posters and stickers.

### Sentences
| sentence | token_span |
| --- | --- |
| A person with dreadlocks and a red bow sits at a table with art posters and stickers. | 0:18 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A person | person | person | nsubj | sits | 0:2 |
| dreadlocks | dreadlocks | dreadlock | pobj | with | 3:4 |
| a red bow | bow | bow | conj | dreadlocks | 5:8 |
| a table | table | table | pobj | at | 10:12 |
| art posters | posters | poster | pobj | with | 13:15 |
| stickers | stickers | sticker | conj | posters | 16:17 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | person | 1 |
| 1 | person | person | NOUN | NN | nsubj | sits | 8 |
| 2 | with | with | ADP | IN | prep | person | 1 |
| 3 | dreadlocks | dreadlock | NOUN | NNS | pobj | with | 2 |
| 4 | and | and | CCONJ | CC | cc | dreadlocks | 3 |
| 5 | a | a | DET | DT | det | bow | 7 |
| 6 | red | red | ADJ | JJ | amod | bow | 7 |
| 7 | bow | bow | NOUN | NN | conj | dreadlocks | 3 |
| 8 | sits | sit | VERB | VBZ | ROOT | sits | 8 |
| 9 | at | at | ADP | IN | prep | sits | 8 |
| 10 | a | a | DET | DT | det | table | 11 |
| 11 | table | table | NOUN | NN | pobj | at | 9 |
| 12 | with | with | ADP | IN | prep | sits | 8 |
| 13 | art | art | NOUN | NN | compound | posters | 14 |
| 14 | posters | poster | NOUN | NNS | pobj | with | 12 |
| 15 | and | and | CCONJ | CC | cc | posters | 14 |
| 16 | stickers | sticker | NOUN | NNS | conj | posters | 14 |
| 17 | . | . | PUNCT | . | punct | sits | 8 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | dreadlocks | dreadlock | chunk1 | 3 | noun_chunk_root | high |
| m2 | object | bow | bow | chunk2 | 7 | noun_chunk_root | high |
| m3 | attribute | red | red | chunk2 | 6 | color_attribute | high |
| m4 | object | table | table | chunk3 | 11 | noun_chunk_root | high |
| m5 | object | posters | poster | chunk4 | 14 | noun_chunk_root | high |
| m6 | attribute | art | art | chunk4 | 13 | compound_modifier | medium |
| m7 | object | stickers | sticker | chunk5 | 16 | noun_chunk_root | high |
| m8 | action | sits | sit | doc | 8 | verb_predicate | high |

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

## 02

**caption_shape:** `multi-sentence`
**caption_id:** `010bb91bf88524cee960135440eff96892d317358f1ef9e027accc6882429c14`

> A brown insect with wings is crawling on a cracked, weathered wooden surface. The wood shows signs of age with visible splits and small bits of debris scattered around. The scene appears outdoors on a forest floor or fallen tree trunk.

### Sentences
| sentence | token_span |
| --- | --- |
| A brown insect with wings is crawling on a cracked, weathered wooden surface. | 0:15 |
| The wood shows signs of age with visible splits and small bits of debris scattered around. | 15:32 |
| The scene appears outdoors on a forest floor or fallen tree trunk. | 32:45 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A brown insect | insect | insect | nsubj | crawling | 0:3 |
| wings | wings | wing | pobj | with | 4:5 |
| a cracked, weathered wooden surface | surface | surface | pobj | on | 8:14 |
| The wood | wood | wood | nsubj | shows | 15:17 |
| signs | signs | sign | dobj | shows | 18:19 |
| age | age | age | pobj | of | 20:21 |
| visible splits | splits | split | pobj | with | 22:24 |
| small bits | bits | bit | conj | splits | 25:27 |
| debris | debris | debris | pobj | of | 28:29 |
| The scene | scene | scene | nsubj | appears | 32:34 |
| a forest floor | floor | floor | pobj | on | 37:40 |
| fallen tree trunk | trunk | trunk | conj | floor | 41:44 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | insect | 2 |
| 1 | brown | brown | ADJ | JJ | amod | insect | 2 |
| 2 | insect | insect | NOUN | NN | nsubj | crawling | 6 |
| 3 | with | with | ADP | IN | prep | insect | 2 |
| 4 | wings | wing | NOUN | NNS | pobj | with | 3 |
| 5 | is | be | AUX | VBZ | aux | crawling | 6 |
| 6 | crawling | crawl | VERB | VBG | ROOT | crawling | 6 |
| 7 | on | on | ADP | IN | prep | crawling | 6 |
| 8 | a | a | DET | DT | det | surface | 13 |
| 9 | cracked | cracked | ADJ | JJ | amod | surface | 13 |
| 10 | , | , | PUNCT | , | punct | surface | 13 |
| 11 | weathered | weathered | ADJ | JJ | amod | surface | 13 |
| 12 | wooden | wooden | ADJ | JJ | amod | surface | 13 |
| 13 | surface | surface | NOUN | NN | pobj | on | 7 |
| 14 | . | . | PUNCT | . | punct | crawling | 6 |
| 15 | The | the | DET | DT | det | wood | 16 |
| 16 | wood | wood | NOUN | NN | nsubj | shows | 17 |
| 17 | shows | show | VERB | VBZ | ROOT | shows | 17 |
| 18 | signs | sign | NOUN | NNS | dobj | shows | 17 |
| 19 | of | of | ADP | IN | prep | signs | 18 |
| 20 | age | age | NOUN | NN | pobj | of | 19 |
| 21 | with | with | ADP | IN | prep | shows | 17 |
| 22 | visible | visible | ADJ | JJ | amod | splits | 23 |
| 23 | splits | split | NOUN | NNS | pobj | with | 21 |
| 24 | and | and | CCONJ | CC | cc | splits | 23 |
| 25 | small | small | ADJ | JJ | amod | bits | 26 |
| 26 | bits | bit | NOUN | NNS | conj | splits | 23 |
| 27 | of | of | ADP | IN | prep | bits | 26 |
| 28 | debris | debris | NOUN | NN | pobj | of | 27 |
| 29 | scattered | scatter | VERB | VBN | acl | splits | 23 |
| 30 | around | around | ADV | RB | advmod | scattered | 29 |
| 31 | . | . | PUNCT | . | punct | shows | 17 |
| 32 | The | the | DET | DT | det | scene | 33 |
| 33 | scene | scene | NOUN | NN | nsubj | appears | 34 |
| 34 | appears | appear | VERB | VBZ | ROOT | appears | 34 |
| 35 | outdoors | outdoors | ADV | RB | advmod | appears | 34 |
| 36 | on | on | ADP | IN | prep | appears | 34 |
| 37 | a | a | DET | DT | det | floor | 39 |
| 38 | forest | forest | NOUN | NN | compound | floor | 39 |
| 39 | floor | floor | NOUN | NN | pobj | on | 36 |
| 40 | or | or | CCONJ | CC | cc | floor | 39 |
| 41 | fallen | fallen | ADJ | JJ | amod | trunk | 43 |
| 42 | tree | tree | NOUN | NN | compound | trunk | 43 |
| 43 | trunk | trunk | NOUN | NN | conj | floor | 39 |
| 44 | . | . | PUNCT | . | punct | appears | 34 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | insect | insect | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | brown | brown | chunk0 | 1 | color_attribute | high |
| m2 | object | wings | wing | chunk1 | 4 | noun_chunk_root | high |
| m3 | object | surface | surface | chunk2 | 13 | noun_chunk_root | high |
| m4 | attribute | cracked | cracked | chunk2 | 9 | modifier_attribute | medium |
| m5 | attribute | weathered | weathered | chunk2 | 11 | modifier_attribute | medium |
| m6 | attribute | wooden | wooden | chunk2 | 12 | material_attribute | high |
| m7 | object | wood | wood | chunk3 | 16 | noun_chunk_root | high |
| m8 | object | signs | sign | chunk4 | 18 | noun_chunk_root | high |
| m9 | object | age | age | chunk5 | 20 | noun_chunk_root | high |
| m10 | object | splits | split | chunk6 | 23 | noun_chunk_root | high |
| m11 | attribute | visible | visible | chunk6 | 22 | modifier_attribute | medium |
| m12 | object | bits | bit | chunk7 | 26 | noun_chunk_root | high |
| m13 | attribute | small | small | chunk7 | 25 | size_attribute | high |
| m14 | object | debris | debris | chunk8 | 28 | noun_chunk_root | high |
| m15 | object | scene | scene | chunk9 | 33 | noun_chunk_root | high |
| m16 | object | floor | floor | chunk10 | 39 | noun_chunk_root | high |
| m17 | attribute | forest | forest | chunk10 | 38 | compound_modifier | medium |
| m18 | object | trunk | trunk | chunk11 | 43 | noun_chunk_root | high |
| m19 | attribute | fallen | fallen | chunk11 | 41 | modifier_attribute | medium |
| m20 | attribute | tree | tree | chunk11 | 42 | compound_modifier | medium |
| m21 | context | outdoors | outdoors | doc | 35 | context_word | medium |
| m22 | action | crawling | crawl | doc | 6 | verb_predicate | high |
| m23 | action | shows | show | doc | 17 | verb_predicate | high |
| m24 | action | scattered | scatter | doc | 29 | verb_predicate | high |
| m25 | action | appears | appear | doc | 34 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> insect |
| e1 | has_attribute | m3 | m4 | medium | chunk2 amod -> surface |
| e2 | has_attribute | m3 | m5 | medium | chunk2 amod -> surface |
| e3 | has_attribute | m3 | m6 | high | chunk2 amod -> surface |
| e4 | has_attribute | m10 | m11 | medium | chunk6 amod -> splits |
| e5 | has_attribute | m12 | m13 | high | chunk7 amod -> bits |
| e6 | has_attribute | m16 | m17 | medium | chunk10 compound -> floor |
| e7 | has_attribute | m18 | m19 | medium | chunk11 amod -> trunk |
| e8 | has_attribute | m18 | m20 | medium | chunk11 compound -> trunk |
| e9 | has_context | scene | m21 | medium | context token outdoors |
| e10 | agent | m22 | m0 | medium | nsubj -> crawling |
| e11 | agent | m23 | m7 | medium | nsubj -> shows |
| e12 | patient | m23 | m8 | medium | dobj -> shows |
| e13 | agent | m25 | m15 | medium | nsubj -> appears |
| e14 | relation | m0 | m2 | high | with |
| e15 | relation | m0 | m3 | high | on |
| e16 | relation | m8 | m9 | medium | of |
| e17 | relation | m7 | m10 | high | with |
| e18 | relation | m7 | m12 | high | with |
| e19 | relation | m12 | m14 | medium | of |
| e20 | relation | m15 | m16 | high | on |
| e21 | relation | m15 | m18 | high | on |

## 03

**caption_shape:** `multi-sentence`
**caption_id:** `0326facce37e93230108fb311cc653eecb8ee62a67a1f0d9f95525ddd9fe3014`

> A woman stands at a podium speaking in front of an audience. An American flag is behind her, and a screen shows the text "Closing the Access Divide."

**parsed_caption:**

> A woman stands at a podium speaking in front of an audience. An American flag is behind her, and a screen shows the quoted text.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | masked_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 0326facce37e93230108fb311cc653eecb8ee62a67a1f0d9f95525ddd9fe3014:q0 | Closing the Access Divide. | closing the access divide. | the quoted text | the text | 121:149 | 112:127 |

### Sentences
| sentence | token_span |
| --- | --- |
| A woman stands at a podium speaking in front of an audience. | 0:13 |
| An American flag is behind her, and a screen shows the quoted text. | 13:28 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A woman | woman | woman | nsubj | stands | 0:2 |
| a podium | podium | podium | pobj | at | 4:6 |
| front | front | front | pobj | in | 8:9 |
| an audience | audience | audience | pobj | of | 10:12 |
| An American flag | flag | flag | nsubj | is | 13:16 |
| her | her | she | pobj | behind | 18:19 |
| a screen | screen | screen | nsubj | shows | 21:23 |
| the quoted text | text | text | dobj | shows | 24:27 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | woman | 1 |
| 1 | woman | woman | NOUN | NN | nsubj | stands | 2 |
| 2 | stands | stand | VERB | VBZ | ROOT | stands | 2 |
| 3 | at | at | ADP | IN | prep | stands | 2 |
| 4 | a | a | DET | DT | det | podium | 5 |
| 5 | podium | podium | NOUN | NN | pobj | at | 3 |
| 6 | speaking | speak | VERB | VBG | advcl | stands | 2 |
| 7 | in | in | ADP | IN | prep | speaking | 6 |
| 8 | front | front | NOUN | NN | pobj | in | 7 |
| 9 | of | of | ADP | IN | prep | front | 8 |
| 10 | an | an | DET | DT | det | audience | 11 |
| 11 | audience | audience | NOUN | NN | pobj | of | 9 |
| 12 | . | . | PUNCT | . | punct | stands | 2 |
| 13 | An | an | DET | DT | det | flag | 15 |
| 14 | American | american | ADJ | JJ | amod | flag | 15 |
| 15 | flag | flag | NOUN | NN | nsubj | is | 16 |
| 16 | is | be | AUX | VBZ | ROOT | is | 16 |
| 17 | behind | behind | ADP | IN | prep | is | 16 |
| 18 | her | she | PRON | PRP | pobj | behind | 17 |
| 19 | , | , | PUNCT | , | punct | is | 16 |
| 20 | and | and | CCONJ | CC | cc | is | 16 |
| 21 | a | a | DET | DT | det | screen | 22 |
| 22 | screen | screen | NOUN | NN | nsubj | shows | 23 |
| 23 | shows | show | VERB | VBZ | conj | is | 16 |
| 24 | the | the | DET | DT | det | text | 26 |
| 25 | quoted | quote | VERB | VBN | amod | text | 26 |
| 26 | text | text | NOUN | NN | dobj | shows | 23 |
| 27 | . | . | PUNCT | . | punct | shows | 23 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | podium | podium | chunk1 | 5 | noun_chunk_root | high |
| m2 | object | audience | audience | chunk3 | 11 | noun_chunk_root | high |
| m3 | object | flag | flag | chunk4 | 15 | noun_chunk_root | high |
| m4 | attribute | American | american | chunk4 | 14 | modifier_attribute | medium |
| m5 | object | her | she | chunk5 | 18 | noun_chunk_root | high |
| m6 | object | screen | screen | chunk6 | 22 | noun_chunk_root | high |
| m7 | object | text | text | chunk7 | 26 | noun_chunk_root | high |
| m8 | attribute | quoted | quote | chunk7 | 25 | state_attribute | medium |
| m9 | action | stands | stand | doc | 2 | verb_predicate | high |
| m10 | action | speaking | speak | doc | 6 | verb_predicate | high |
| m11 | action | shows | show | doc | 23 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m3 | m4 | medium | chunk4 amod -> flag |
| e1 | has_attribute | m7 | m8 | medium | chunk7 amod -> text |
| e2 | agent | m9 | m0 | medium | nsubj -> stands |
| e3 | agent | m11 | m6 | medium | nsubj -> shows |
| e4 | patient | m11 | m7 | medium | dobj -> shows |
| e5 | relation | m0 | m1 | medium | at |
| e6 | relation | m0 | m2 | high | in_front_of |
| e7 | relation | m3 | m5 | high | behind |

## 04

**caption_shape:** `multi-sentence`
**caption_id:** `03dfd14a3d7fc8b961a00424e43bfbdfcb9eded2464416b15cc6e9441a503814`

> Three people stand with a shopping cart filled with groceries and bags. One person holds a red snack bag.

### Sentences
| sentence | token_span |
| --- | --- |
| Three people stand with a shopping cart filled with groceries and bags. | 0:13 |
| One person holds a red snack bag. | 13:21 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Three people | people | people | nsubj | stand | 0:2 |
| a shopping cart | cart | cart | pobj | with | 4:7 |
| groceries | groceries | grocery | pobj | with | 9:10 |
| bags | bags | bag | conj | groceries | 11:12 |
| One person | person | person | nsubj | holds | 13:15 |
| a red snack bag | bag | bag | dobj | holds | 16:20 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Three | three | NUM | CD | nummod | people | 1 |
| 1 | people | people | NOUN | NNS | nsubj | stand | 2 |
| 2 | stand | stand | VERB | VBP | ROOT | stand | 2 |
| 3 | with | with | ADP | IN | prep | stand | 2 |
| 4 | a | a | DET | DT | det | cart | 6 |
| 5 | shopping | shopping | NOUN | NN | compound | cart | 6 |
| 6 | cart | cart | NOUN | NN | pobj | with | 3 |
| 7 | filled | fill | VERB | VBN | acl | cart | 6 |
| 8 | with | with | ADP | IN | prep | filled | 7 |
| 9 | groceries | grocery | NOUN | NNS | pobj | with | 8 |
| 10 | and | and | CCONJ | CC | cc | groceries | 9 |
| 11 | bags | bag | NOUN | NNS | conj | groceries | 9 |
| 12 | . | . | PUNCT | . | punct | stand | 2 |
| 13 | One | one | NUM | CD | nummod | person | 14 |
| 14 | person | person | NOUN | NN | nsubj | holds | 15 |
| 15 | holds | hold | VERB | VBZ | ROOT | holds | 15 |
| 16 | a | a | DET | DT | det | bag | 19 |
| 17 | red | red | ADJ | JJ | amod | bag | 19 |
| 18 | snack | snack | NOUN | NN | compound | bag | 19 |
| 19 | bag | bag | NOUN | NN | dobj | holds | 15 |
| 20 | . | . | PUNCT | . | punct | holds | 15 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Three | three | chunk0 | 0 | quantity | high |
| m2 | object | cart | cart | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | shopping | shopping | chunk1 | 5 | compound_modifier | medium |
| m4 | object | groceries | grocery | chunk2 | 9 | noun_chunk_root | high |
| m5 | object | bags | bag | chunk3 | 11 | noun_chunk_root | high |
| m6 | object | person | person | chunk4 | 14 | noun_chunk_root | high |
| m7 | quantity | One | one | chunk4 | 13 | quantity | high |
| m8 | object | bag | bag | chunk5 | 19 | noun_chunk_root | high |
| m9 | attribute | red | red | chunk5 | 17 | color_attribute | high |
| m10 | attribute | snack | snack | chunk5 | 18 | compound_modifier | medium |
| m11 | action | stand | stand | doc | 2 | verb_predicate | high |
| m12 | action | filled | fill | doc | 7 | verb_predicate | high |
| m13 | action | holds | hold | doc | 15 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 nummod -> people |
| e1 | has_attribute | m2 | m3 | medium | chunk1 compound -> cart |
| e2 | has_quantity | m6 | m7 | high | chunk4 nummod -> person |
| e3 | has_attribute | m8 | m9 | high | chunk5 amod -> bag |
| e4 | has_attribute | m8 | m10 | medium | chunk5 compound -> bag |
| e5 | agent | m11 | m0 | medium | nsubj -> stand |
| e6 | agent | m13 | m6 | medium | nsubj -> holds |
| e7 | patient | m13 | m8 | medium | dobj -> holds |
| e8 | relation | m0 | m2 | high | with |
| e9 | relation | m2 | m4 | high | with |
| e10 | relation | m2 | m5 | high | with |

## 05

**caption_shape:** `multi-sentence`
**caption_id:** `049ccab2d0384df0e916b4cb21c0840387d630be1c36548aa7f05dad5f5d4014`

> Bright orange glass flowers stand in a garden bed with green grass and purple blooms. In the background, people walk near a wooden fence under a large umbrella. Trees and a blue structure are visible beyond the garden area.

### Sentences
| sentence | token_span |
| --- | --- |
| Bright orange glass flowers stand in a garden bed with green grass and purple blooms. | 0:16 |
| In the background, people walk near a wooden fence under a large umbrella. | 16:31 |
| Trees and a blue structure are visible beyond the garden area. | 31:43 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Bright orange glass flowers | flowers | flower | nsubj | stand | 0:4 |
| a garden bed | bed | bed | pobj | in | 6:9 |
| green grass | grass | grass | pobj | with | 10:12 |
| purple blooms | blooms | bloom | conj | grass | 13:15 |
| the background | background | background | pobj | In | 17:19 |
| people | people | people | nsubj | walk | 20:21 |
| a wooden fence | fence | fence | pobj | near | 23:26 |
| a large umbrella | umbrella | umbrella | pobj | under | 27:30 |
| Trees | Trees | tree | nsubj | are | 31:32 |
| a blue structure | structure | structure | conj | Trees | 33:36 |
| the garden area | area | area | pobj | beyond | 39:42 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Bright | bright | ADJ | JJ | amod | orange | 1 |
| 1 | orange | orange | NOUN | NN | compound | flowers | 3 |
| 2 | glass | glass | NOUN | NN | compound | flowers | 3 |
| 3 | flowers | flower | NOUN | NNS | nsubj | stand | 4 |
| 4 | stand | stand | VERB | VBP | ROOT | stand | 4 |
| 5 | in | in | ADP | IN | prep | stand | 4 |
| 6 | a | a | DET | DT | det | bed | 8 |
| 7 | garden | garden | NOUN | NN | compound | bed | 8 |
| 8 | bed | bed | NOUN | NN | pobj | in | 5 |
| 9 | with | with | ADP | IN | prep | bed | 8 |
| 10 | green | green | ADJ | JJ | amod | grass | 11 |
| 11 | grass | grass | NOUN | NN | pobj | with | 9 |
| 12 | and | and | CCONJ | CC | cc | grass | 11 |
| 13 | purple | purple | ADJ | JJ | amod | blooms | 14 |
| 14 | blooms | bloom | NOUN | NNS | conj | grass | 11 |
| 15 | . | . | PUNCT | . | punct | stand | 4 |
| 16 | In | in | ADP | IN | prep | walk | 21 |
| 17 | the | the | DET | DT | det | background | 18 |
| 18 | background | background | NOUN | NN | pobj | In | 16 |
| 19 | , | , | PUNCT | , | punct | walk | 21 |
| 20 | people | people | NOUN | NNS | nsubj | walk | 21 |
| 21 | walk | walk | VERB | VBP | ROOT | walk | 21 |
| 22 | near | near | ADP | IN | prep | walk | 21 |
| 23 | a | a | DET | DT | det | fence | 25 |
| 24 | wooden | wooden | ADJ | JJ | amod | fence | 25 |
| 25 | fence | fence | NOUN | NN | pobj | near | 22 |
| 26 | under | under | ADP | IN | prep | walk | 21 |
| 27 | a | a | DET | DT | det | umbrella | 29 |
| 28 | large | large | ADJ | JJ | amod | umbrella | 29 |
| 29 | umbrella | umbrella | NOUN | NN | pobj | under | 26 |
| 30 | . | . | PUNCT | . | punct | walk | 21 |
| 31 | Trees | tree | NOUN | NNS | nsubj | are | 36 |
| 32 | and | and | CCONJ | CC | cc | Trees | 31 |
| 33 | a | a | DET | DT | det | structure | 35 |
| 34 | blue | blue | ADJ | JJ | amod | structure | 35 |
| 35 | structure | structure | NOUN | NN | conj | Trees | 31 |
| 36 | are | be | AUX | VBP | ROOT | are | 36 |
| 37 | visible | visible | ADJ | JJ | acomp | are | 36 |
| 38 | beyond | beyond | ADP | IN | prep | are | 36 |
| 39 | the | the | DET | DT | det | area | 41 |
| 40 | garden | garden | NOUN | NN | compound | area | 41 |
| 41 | area | area | NOUN | NN | pobj | beyond | 38 |
| 42 | . | . | PUNCT | . | punct | are | 36 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | flowers | flower | chunk0 | 3 | noun_chunk_root | high |
| m1 | attribute | Bright | bright | chunk0 | 0 | visual_attribute | medium |
| m2 | attribute | orange | orange | chunk0 | 1 | color_attribute | high |
| m3 | attribute | glass | glass | chunk0 | 2 | material_attribute | high |
| m4 | object | bed | bed | chunk1 | 8 | noun_chunk_root | high |
| m5 | attribute | garden | garden | chunk1 | 7 | compound_modifier | medium |
| m6 | object | grass | grass | chunk2 | 11 | noun_chunk_root | high |
| m7 | attribute | green | green | chunk2 | 10 | color_attribute | high |
| m8 | object | blooms | bloom | chunk3 | 14 | noun_chunk_root | high |
| m9 | attribute | purple | purple | chunk3 | 13 | color_attribute | high |
| m10 | object | background | background | chunk4 | 18 | noun_chunk_root | high |
| m11 | object | people | people | chunk5 | 20 | noun_chunk_root | high |
| m12 | object | fence | fence | chunk6 | 25 | noun_chunk_root | high |
| m13 | attribute | wooden | wooden | chunk6 | 24 | material_attribute | high |
| m14 | object | umbrella | umbrella | chunk7 | 29 | noun_chunk_root | high |
| m15 | attribute | large | large | chunk7 | 28 | size_attribute | high |
| m16 | object | Trees | tree | chunk8 | 31 | noun_chunk_root | high |
| m17 | object | structure | structure | chunk9 | 35 | noun_chunk_root | high |
| m18 | attribute | blue | blue | chunk9 | 34 | color_attribute | high |
| m19 | object | area | area | chunk10 | 41 | noun_chunk_root | high |
| m20 | attribute | garden | garden | chunk10 | 40 | compound_modifier | medium |
| m21 | context | background | background | doc | 18 | context_word | medium |
| m22 | action | stand | stand | doc | 4 | verb_predicate | high |
| m23 | action | walk | walk | doc | 21 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> flowers |
| e1 | has_attribute | m0 | m2 | high | chunk0 compound -> flowers |
| e2 | has_attribute | m0 | m3 | high | chunk0 compound -> flowers |
| e3 | has_attribute | m4 | m5 | medium | chunk1 compound -> bed |
| e4 | has_attribute | m6 | m7 | high | chunk2 amod -> grass |
| e5 | has_attribute | m8 | m9 | high | chunk3 amod -> blooms |
| e6 | has_attribute | m12 | m13 | high | chunk6 amod -> fence |
| e7 | has_attribute | m14 | m15 | high | chunk7 amod -> umbrella |
| e8 | has_attribute | m17 | m18 | high | chunk9 amod -> structure |
| e9 | has_attribute | m19 | m20 | medium | chunk10 compound -> area |
| e10 | has_context | scene | m21 | medium | context token background |
| e11 | agent | m22 | m0 | medium | nsubj -> stand |
| e12 | agent | m23 | m11 | medium | nsubj -> walk |
| e13 | relation | m0 | m4 | high | in |
| e14 | relation | m4 | m6 | high | with |
| e15 | relation | m4 | m8 | high | with |
| e16 | relation | m11 | m21 | high | in |
| e17 | relation | m11 | m12 | high | near |
| e18 | relation | m11 | m14 | high | under |
| e19 | relation | m16 | m19 | high | beyond |

## 06

**caption_shape:** `tag-list-like`
**caption_id:** `050521436694404336ade2d13e39d7635191e3ea8eccf2a0c80cf128880d7414`

> smiling couple, formal party, british flags, chandelier, wine glasses

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | smiling couple | smiling couple | 0:14 |
| t1 | formal party | formal party | 16:28 |
| t2 | british flags | british flags | 30:43 |
| t3 | chandelier | chandelier | 45:55 |
| t4 | wine glasses | wine glasses | 57:69 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | smiling couple | couple | couple | ROOT | couple | 0:2 | 0:14 |
| t1 | formal party | party | party | ROOT | party | 0:2 | 16:28 |
| t2 | british flags | flags | flag | ROOT | flags | 0:2 | 30:43 |
| t3 | chandelier | chandelier | chandelier | ROOT | chandelier | 0:1 | 45:55 |
| t4 | wine glasses | glasses | glass | ROOT | glasses | 0:2 | 57:69 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | smiling | smile | VERB | ADJ | VBG | VBG | amod | couple | 1 | 0:7 |
| t0 | 1 | couple | couple | NOUN | NOUN | NN | NN | ROOT | couple | 1 | 8:14 |
| t1 | 0 | formal | formal | ADJ | ADJ | JJ | JJ | amod | party | 1 | 16:22 |
| t1 | 1 | party | party | NOUN | NOUN | NN | NN | ROOT | party | 1 | 23:28 |
| t2 | 0 | british | british | ADJ | ADJ | JJ | JJ | amod | flags | 1 | 30:37 |
| t2 | 1 | flags | flag | NOUN | NOUN | NNS | NNS | ROOT | flags | 1 | 38:43 |
| t3 | 0 | chandelier | chandelier | NOUN | NOUN | NN | NN | ROOT | chandelier | 0 | 45:55 |
| t4 | 0 | wine | wine | NOUN | NOUN | NN | NN | compound | glasses | 1 | 57:61 |
| t4 | 1 | glasses | glass | NOUN | NOUN | NNS | NNS | ROOT | glasses | 1 | 62:69 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | couple | couple | t0 | 1 | segment_head | high |
| m1 | attribute | smiling | smile | t0 | 0 | state_attribute | high |
| m2 | object | party | party | t1 | 1 | segment_head | high |
| m3 | attribute | formal | formal | t1 | 0 | attribute | high |
| m4 | object | flags | flag | t2 | 1 | segment_head | high |
| m5 | attribute | british | british | t2 | 0 | attribute | high |
| m6 | object | chandelier | chandelier | t3 | 0 | segment_head | high |
| m7 | object | glasses | glass | t4 | 1 | segment_head | high |
| m8 | attribute | wine | wine | t4 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> couple |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> party |
| e2 | has_attribute | m4 | m5 | high | t2 internal amod -> flags |
| e3 | has_attribute | m7 | m8 | high | t4 internal compound -> glasses |

## 07

**caption_shape:** `sentence-like`
**caption_id:** `054a504fff891dae0e43522f858a2e7df4e2a5c21d99937f70462b69a4386414`

> A white church with a cross on top has stone steps leading to a wooden door.

### Sentences
| sentence | token_span |
| --- | --- |
| A white church with a cross on top has stone steps leading to a wooden door. | 0:17 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A white church | church | church | nsubj | has | 0:3 |
| a cross | cross | cross | pcomp | with | 4:6 |
| top | top | top | pobj | on | 7:8 |
| stone steps | steps | step | dobj | has | 9:11 |
| a wooden door | door | door | pobj | to | 13:16 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | church | 2 |
| 1 | white | white | ADJ | JJ | amod | church | 2 |
| 2 | church | church | NOUN | NN | nsubj | has | 8 |
| 3 | with | with | ADP | IN | prep | church | 2 |
| 4 | a | a | DET | DT | det | cross | 5 |
| 5 | cross | cross | NOUN | NN | pcomp | with | 3 |
| 6 | on | on | ADP | IN | prep | cross | 5 |
| 7 | top | top | NOUN | NN | pobj | on | 6 |
| 8 | has | have | VERB | VBZ | ROOT | has | 8 |
| 9 | stone | stone | NOUN | NN | compound | steps | 10 |
| 10 | steps | step | NOUN | NNS | dobj | has | 8 |
| 11 | leading | lead | VERB | VBG | acl | steps | 10 |
| 12 | to | to | ADP | IN | prep | leading | 11 |
| 13 | a | a | DET | DT | det | door | 15 |
| 14 | wooden | wooden | ADJ | JJ | amod | door | 15 |
| 15 | door | door | NOUN | NN | pobj | to | 12 |
| 16 | . | . | PUNCT | . | punct | has | 8 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | church | church | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | white | white | chunk0 | 1 | color_attribute | high |
| m2 | object | cross | cross | chunk1 | 5 | noun_chunk_root | high |
| m3 | context | top | top | chunk2 | 7 | spatial_region | medium |
| m4 | object | steps | step | chunk3 | 10 | noun_chunk_root | high |
| m5 | attribute | stone | stone | chunk3 | 9 | material_attribute | high |
| m6 | object | door | door | chunk4 | 15 | noun_chunk_root | high |
| m7 | attribute | wooden | wooden | chunk4 | 14 | material_attribute | high |
| m8 | action | has | have | doc | 8 | verb_predicate | high |
| m9 | action | leading | lead | doc | 11 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> church |
| e1 | has_attribute | m4 | m5 | high | chunk3 compound -> steps |
| e2 | has_attribute | m6 | m7 | high | chunk4 amod -> door |
| e3 | agent | m8 | m0 | medium | nsubj -> has |
| e4 | patient | m8 | m4 | medium | dobj -> has |
| e5 | relation | m0 | m2 | high | with |
| e6 | relation | m2 | m3 | high | on |
| e7 | relation | m4 | m6 | medium | to |

## 08

**caption_shape:** `multi-sentence`
**caption_id:** `05784a8cb72a17349e2cd4389708153527b40af80a043636d0ff17fdcf16c014`

> A poster on a black trash can reads "BANG GOES THE KNIGHTHOOD" with a silhouette of a man in a hat. The scene is on a city sidewalk.

**parsed_caption:**

> A poster on a black trash can reads the quoted text with a silhouette of a man in a hat. The scene is on a city sidewalk.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | masked_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 05784a8cb72a17349e2cd4389708153527b40af80a043636d0ff17fdcf16c014:q0 | BANG GOES THE KNIGHTHOOD | bang goes the knighthood | the quoted text |  | 36:62 | 36:51 |

### Sentences
| sentence | token_span |
| --- | --- |
| A poster on a black trash can reads the quoted text with a silhouette of a man in a hat. | 0:21 |
| The scene is on a city sidewalk. | 21:29 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A poster | poster | poster | nsubj | reads | 0:2 |
| a black trash can | can | can | pobj | on | 3:7 |
| the quoted text | text | text | dobj | reads | 8:11 |
| a silhouette | silhouette | silhouette | pobj | with | 12:14 |
| a man | man | man | pobj | of | 15:17 |
| a hat | hat | hat | pobj | in | 18:20 |
| The scene | scene | scene | nsubj | is | 21:23 |
| a city sidewalk | sidewalk | sidewalk | pobj | on | 25:28 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | poster | 1 |
| 1 | poster | poster | NOUN | NN | nsubj | reads | 7 |
| 2 | on | on | ADP | IN | prep | poster | 1 |
| 3 | a | a | DET | DT | det | can | 6 |
| 4 | black | black | ADJ | JJ | amod | can | 6 |
| 5 | trash | trash | NOUN | NN | compound | can | 6 |
| 6 | can | can | NOUN | NN | pobj | on | 2 |
| 7 | reads | read | VERB | VBZ | ROOT | reads | 7 |
| 8 | the | the | DET | DT | det | text | 10 |
| 9 | quoted | quote | VERB | VBN | amod | text | 10 |
| 10 | text | text | NOUN | NN | dobj | reads | 7 |
| 11 | with | with | ADP | IN | prep | reads | 7 |
| 12 | a | a | DET | DT | det | silhouette | 13 |
| 13 | silhouette | silhouette | NOUN | NN | pobj | with | 11 |
| 14 | of | of | ADP | IN | prep | silhouette | 13 |
| 15 | a | a | DET | DT | det | man | 16 |
| 16 | man | man | NOUN | NN | pobj | of | 14 |
| 17 | in | in | ADP | IN | prep | man | 16 |
| 18 | a | a | DET | DT | det | hat | 19 |
| 19 | hat | hat | NOUN | NN | pobj | in | 17 |
| 20 | . | . | PUNCT | . | punct | reads | 7 |
| 21 | The | the | DET | DT | det | scene | 22 |
| 22 | scene | scene | NOUN | NN | nsubj | is | 23 |
| 23 | is | be | AUX | VBZ | ROOT | is | 23 |
| 24 | on | on | ADP | IN | prep | is | 23 |
| 25 | a | a | DET | DT | det | sidewalk | 27 |
| 26 | city | city | NOUN | NN | compound | sidewalk | 27 |
| 27 | sidewalk | sidewalk | NOUN | NN | pobj | on | 24 |
| 28 | . | . | PUNCT | . | punct | is | 23 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | poster | poster | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | can | can | chunk1 | 6 | noun_chunk_root | high |
| m2 | attribute | black | black | chunk1 | 4 | color_attribute | high |
| m3 | attribute | trash | trash | chunk1 | 5 | compound_modifier | medium |
| m4 | object | text | text | chunk2 | 10 | noun_chunk_root | high |
| m5 | attribute | quoted | quote | chunk2 | 9 | state_attribute | medium |
| m6 | object | silhouette | silhouette | chunk3 | 13 | noun_chunk_root | high |
| m7 | object | man | man | chunk4 | 16 | noun_chunk_root | high |
| m8 | object | hat | hat | chunk5 | 19 | noun_chunk_root | high |
| m9 | object | scene | scene | chunk6 | 22 | noun_chunk_root | high |
| m10 | object | sidewalk | sidewalk | chunk7 | 27 | noun_chunk_root | high |
| m11 | attribute | city | city | chunk7 | 26 | compound_modifier | medium |
| m12 | action | reads | read | doc | 7 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> can |
| e1 | has_attribute | m1 | m3 | medium | chunk1 compound -> can |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> text |
| e3 | has_attribute | m10 | m11 | medium | chunk7 compound -> sidewalk |
| e4 | agent | m12 | m0 | medium | nsubj -> reads |
| e5 | patient | m12 | m4 | medium | dobj -> reads |
| e6 | relation | m0 | m1 | high | on |
| e7 | relation | m0 | m6 | high | with |
| e8 | relation | m6 | m7 | medium | of |
| e9 | relation | m7 | m8 | high | in |
| e10 | relation | m9 | m10 | high | on |

## 09

**caption_shape:** `multi-sentence`
**caption_id:** `0670190ac8436d736a62a8bf08625ad242a7891121da4f518b00c9642570bc14`

> A young child with blonde hair smiles widely while wearing a blue and white striped hat. The child is bare-shouldered and appears indoors, with a window visible in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| A young child with blonde hair smiles widely while wearing a blue and white striped hat. | 0:17 |
| The child is bare-shouldered and appears indoors, with a window visible in the background. | 17:35 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A young child | child | child | nsubj | smiles | 0:3 |
| blonde hair | hair | hair | pobj | with | 4:6 |
| a blue and white striped hat | hat | hat | dobj | wearing | 10:16 |
| The child | child | child | nsubj | is | 17:19 |
| a window | window | window | pobj | with | 28:30 |
| the background | background | background | pobj | in | 32:34 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | child | 2 |
| 1 | young | young | ADJ | JJ | amod | child | 2 |
| 2 | child | child | NOUN | NN | nsubj | smiles | 6 |
| 3 | with | with | ADP | IN | prep | child | 2 |
| 4 | blonde | blonde | ADJ | JJ | amod | hair | 5 |
| 5 | hair | hair | NOUN | NN | pobj | with | 3 |
| 6 | smiles | smile | VERB | VBZ | ROOT | smiles | 6 |
| 7 | widely | widely | ADV | RB | advmod | smiles | 6 |
| 8 | while | while | SCONJ | IN | mark | wearing | 9 |
| 9 | wearing | wear | VERB | VBG | advcl | smiles | 6 |
| 10 | a | a | DET | DT | det | hat | 15 |
| 11 | blue | blue | ADJ | JJ | amod | hat | 15 |
| 12 | and | and | CCONJ | CC | cc | blue | 11 |
| 13 | white | white | ADJ | JJ | conj | blue | 11 |
| 14 | striped | strip | VERB | VBN | amod | hat | 15 |
| 15 | hat | hat | NOUN | NN | dobj | wearing | 9 |
| 16 | . | . | PUNCT | . | punct | smiles | 6 |
| 17 | The | the | DET | DT | det | child | 18 |
| 18 | child | child | NOUN | NN | nsubj | is | 19 |
| 19 | is | be | AUX | VBZ | ROOT | is | 19 |
| 20 | bare | bare | ADJ | JJ | amod | shouldered | 22 |
| 21 | - | - | PUNCT | HYPH | punct | shouldered | 22 |
| 22 | shouldered | shouldered | ADJ | JJ | acomp | is | 19 |
| 23 | and | and | CCONJ | CC | cc | is | 19 |
| 24 | appears | appear | VERB | VBZ | conj | is | 19 |
| 25 | indoors | indoors | ADV | RB | advmod | appears | 24 |
| 26 | , | , | PUNCT | , | punct | appears | 24 |
| 27 | with | with | ADP | IN | prep | appears | 24 |
| 28 | a | a | DET | DT | det | window | 29 |
| 29 | window | window | NOUN | NN | pobj | with | 27 |
| 30 | visible | visible | ADJ | JJ | amod | window | 29 |
| 31 | in | in | ADP | IN | prep | visible | 30 |
| 32 | the | the | DET | DT | det | background | 33 |
| 33 | background | background | NOUN | NN | pobj | in | 31 |
| 34 | . | . | PUNCT | . | punct | is | 19 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | child | child | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | young | young | chunk0 | 1 | modifier_attribute | medium |
| m2 | object | hair | hair | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | blonde | blonde | chunk1 | 4 | modifier_attribute | medium |
| m4 | object | hat | hat | chunk2 | 15 | noun_chunk_root | high |
| m5 | attribute | blue | blue | chunk2 | 11 | color_attribute | high |
| m6 | attribute | white | white | chunk2 | 13 | color_attribute | high |
| m7 | attribute | striped | strip | chunk2 | 14 | state_attribute | medium |
| m8 | object | child | child | chunk3 | 18 | noun_chunk_root | high |
| m9 | object | window | window | chunk4 | 29 | noun_chunk_root | high |
| m10 | object | background | background | chunk5 | 33 | noun_chunk_root | high |
| m11 | context | indoors | indoors | doc | 25 | context_word | medium |
| m12 | context | background | background | doc | 33 | context_word | medium |
| m13 | action | smiles | smile | doc | 6 | verb_predicate | high |
| m14 | action | wearing | wear | doc | 9 | verb_predicate | high |
| m15 | action | appears | appear | doc | 24 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> child |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> hair |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> hat |
| e3 | has_attribute | m4 | m6 | high | chunk2 conj -> hat |
| e4 | has_attribute | m4 | m7 | medium | chunk2 amod -> hat |
| e5 | has_context | scene | m11 | medium | context token indoors |
| e6 | has_context | scene | m12 | medium | context token background |
| e7 | agent | m13 | m0 | medium | nsubj -> smiles |
| e8 | patient | m14 | m4 | medium | dobj -> wearing |
| e9 | relation | m0 | m2 | high | with |
| e10 | relation | m8 | m9 | high | with |

## 10

**caption_shape:** `tag-list-like`
**caption_id:** `068c9ac59345edb43cd2e03ceec8f57ee0c0fbf399ff97f5f348ac0e716b0014`

> roller skaters, helmet, referee, court, blue jersey

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | roller skaters | roller skaters | 0:14 |
| t1 | helmet | helmet | 16:22 |
| t2 | referee | referee | 24:31 |
| t3 | court | court | 33:38 |
| t4 | blue jersey | blue jersey | 40:51 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | roller skaters | skaters | skater | ROOT | skaters | 0:2 | 0:14 |
| t1 | helmet | helmet | helmet | ROOT | helmet | 0:1 | 16:22 |
| t2 | referee | referee | referee | ROOT | referee | 0:1 | 24:31 |
| t3 | court | court | court | ROOT | court | 0:1 | 33:38 |
| t4 | blue jersey | jersey | jersey | ROOT | jersey | 0:2 | 40:51 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | roller | roller | NOUN | NOUN | NN | NN | compound | skaters | 1 | 0:6 |
| t0 | 1 | skaters | skater | NOUN | NOUN | NNS | NNS | ROOT | skaters | 1 | 7:14 |
| t1 | 0 | helmet | helmet | PROPN | NOUN | NNP | NN | ROOT | helmet | 0 | 16:22 |
| t2 | 0 | referee | referee | NOUN | NOUN | NN | NN | ROOT | referee | 0 | 24:31 |
| t3 | 0 | court | court | NOUN | NOUN | NN | NN | ROOT | court | 0 | 33:38 |
| t4 | 0 | blue | blue | PROPN | ADJ | NNP | JJ | compound | jersey | 1 | 40:44 |
| t4 | 1 | jersey | jersey | PROPN | NOUN | NNP | NN | ROOT | jersey | 1 | 45:51 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | skaters | skater | t0 | 1 | segment_head | high |
| m1 | attribute | roller | roller | t0 | 0 | attribute | high |
| m2 | object | helmet | helmet | t1 | 0 | segment_head | high |
| m3 | object | referee | referee | t2 | 0 | segment_head | high |
| m4 | object | court | court | t3 | 0 | segment_head | high |
| m5 | object | jersey | jersey | t4 | 1 | segment_head | high |
| m6 | attribute | blue | blue | t4 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> skaters |
| e1 | has_attribute | m5 | m6 | high | t4 internal compound -> jersey |

## 11

**caption_shape:** `multi-sentence`
**caption_id:** `08612f90283dcb7b3b1fa62f0512b84c577e5a2635a5e1e5346c33e0505ad414`

> A large stone building with a gray roof and arched windows stands on a cobblestone street. A dark sedan is parked in front, and a bus is visible further down the road under a partly cloudy sky.

### Sentences
| sentence | token_span |
| --- | --- |
| A large stone building with a gray roof and arched windows stands on a cobblestone street. | 0:17 |
| A dark sedan is parked in front, and a bus is visible further down the road under a partly cloudy sky. | 17:40 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A large stone building | building | building | nsubj | stands | 0:4 |
| a gray roof | roof | roof | pobj | with | 5:8 |
| arched windows | windows | window | conj | roof | 9:11 |
| a cobblestone street | street | street | pobj | on | 13:16 |
| A dark sedan | sedan | sedan | nsubjpass | parked | 17:20 |
| front | front | front | pobj | in | 23:24 |
| a bus | bus | bus | nsubj | is | 26:28 |
| the road | road | road | pobj | down | 32:34 |
| a partly cloudy sky | sky | sky | pobj | under | 35:39 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | building | 3 |
| 1 | large | large | ADJ | JJ | amod | building | 3 |
| 2 | stone | stone | NOUN | NN | compound | building | 3 |
| 3 | building | building | NOUN | NN | nsubj | stands | 11 |
| 4 | with | with | ADP | IN | prep | building | 3 |
| 5 | a | a | DET | DT | det | roof | 7 |
| 6 | gray | gray | ADJ | JJ | amod | roof | 7 |
| 7 | roof | roof | NOUN | NN | pobj | with | 4 |
| 8 | and | and | CCONJ | CC | cc | roof | 7 |
| 9 | arched | arched | ADJ | JJ | amod | windows | 10 |
| 10 | windows | window | NOUN | NNS | conj | roof | 7 |
| 11 | stands | stand | VERB | VBZ | ROOT | stands | 11 |
| 12 | on | on | ADP | IN | prep | stands | 11 |
| 13 | a | a | DET | DT | det | street | 15 |
| 14 | cobblestone | cobblestone | NOUN | NN | amod | street | 15 |
| 15 | street | street | NOUN | NN | pobj | on | 12 |
| 16 | . | . | PUNCT | . | punct | stands | 11 |
| 17 | A | a | DET | DT | det | sedan | 19 |
| 18 | dark | dark | ADJ | JJ | amod | sedan | 19 |
| 19 | sedan | sedan | NOUN | NN | nsubjpass | parked | 21 |
| 20 | is | be | AUX | VBZ | auxpass | parked | 21 |
| 21 | parked | park | VERB | VBN | ROOT | parked | 21 |
| 22 | in | in | ADP | IN | prep | parked | 21 |
| 23 | front | front | NOUN | NN | pobj | in | 22 |
| 24 | , | , | PUNCT | , | punct | parked | 21 |
| 25 | and | and | CCONJ | CC | cc | parked | 21 |
| 26 | a | a | DET | DT | det | bus | 27 |
| 27 | bus | bus | NOUN | NN | nsubj | is | 28 |
| 28 | is | be | AUX | VBZ | conj | parked | 21 |
| 29 | visible | visible | ADJ | JJ | acomp | is | 28 |
| 30 | further | far | ADV | RBR | advmod | down | 31 |
| 31 | down | down | ADP | IN | prep | is | 28 |
| 32 | the | the | DET | DT | det | road | 33 |
| 33 | road | road | NOUN | NN | pobj | down | 31 |
| 34 | under | under | ADP | IN | prep | is | 28 |
| 35 | a | a | DET | DT | det | sky | 38 |
| 36 | partly | partly | ADV | RB | advmod | cloudy | 37 |
| 37 | cloudy | cloudy | ADJ | JJ | amod | sky | 38 |
| 38 | sky | sky | NOUN | NN | pobj | under | 34 |
| 39 | . | . | PUNCT | . | punct | is | 28 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | chunk0 | 3 | noun_chunk_root | high |
| m1 | attribute | large | large | chunk0 | 1 | size_attribute | high |
| m2 | attribute | stone | stone | chunk0 | 2 | material_attribute | high |
| m3 | object | roof | roof | chunk1 | 7 | noun_chunk_root | high |
| m4 | attribute | gray | gray | chunk1 | 6 | color_attribute | high |
| m5 | object | windows | window | chunk2 | 10 | noun_chunk_root | high |
| m6 | attribute | arched | arched | chunk2 | 9 | visual_attribute | medium |
| m7 | object | street | street | chunk3 | 15 | noun_chunk_root | high |
| m8 | attribute | cobblestone | cobblestone | chunk3 | 14 | modifier_attribute | medium |
| m9 | object | sedan | sedan | chunk4 | 19 | noun_chunk_root | high |
| m10 | attribute | dark | dark | chunk4 | 18 | visual_attribute | medium |
| m11 | context | front | front | chunk5 | 23 | spatial_region | medium |
| m12 | object | bus | bus | chunk6 | 27 | noun_chunk_root | high |
| m13 | object | road | road | chunk7 | 33 | noun_chunk_root | high |
| m14 | object | sky | sky | chunk8 | 38 | noun_chunk_root | high |
| m15 | attribute | partly | partly | chunk8 | 36 | modifier_attribute | medium |
| m16 | attribute | cloudy | cloudy | chunk8 | 37 | modifier_attribute | medium |
| m17 | action | stands | stand | doc | 11 | verb_predicate | high |
| m18 | action | parked | park | doc | 21 | verb_predicate | high |

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

## 12

**caption_shape:** `multi-sentence`
**caption_id:** `0882bfa152ac30901673edf8d30aba5ce433439a9a71153fea1e970f9f0f4c14`

> A man in a white shirt holds a basketball above his head on a gym court. Several people in pink and gray shirts play nearby.

### Sentences
| sentence | token_span |
| --- | --- |
| A man in a white shirt holds a basketball above his head on a gym court. | 0:17 |
| Several people in pink and gray shirts play nearby. | 17:27 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A man | man | man | nsubj | holds | 0:2 |
| a white shirt | shirt | shirt | pobj | in | 3:6 |
| a basketball | basketball | basketball | dobj | holds | 7:9 |
| his head | head | head | pobj | above | 10:12 |
| a gym court | court | court | pobj | on | 13:16 |
| Several people | people | people | nsubj | play | 17:19 |
| pink and gray shirts | shirts | shirt | pobj | in | 20:24 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | man | 1 |
| 1 | man | man | NOUN | NN | nsubj | holds | 6 |
| 2 | in | in | ADP | IN | prep | man | 1 |
| 3 | a | a | DET | DT | det | shirt | 5 |
| 4 | white | white | ADJ | JJ | amod | shirt | 5 |
| 5 | shirt | shirt | NOUN | NN | pobj | in | 2 |
| 6 | holds | hold | VERB | VBZ | ROOT | holds | 6 |
| 7 | a | a | DET | DT | det | basketball | 8 |
| 8 | basketball | basketball | NOUN | NN | dobj | holds | 6 |
| 9 | above | above | ADP | IN | prep | holds | 6 |
| 10 | his | his | PRON | PRP$ | poss | head | 11 |
| 11 | head | head | NOUN | NN | pobj | above | 9 |
| 12 | on | on | ADP | IN | prep | holds | 6 |
| 13 | a | a | DET | DT | det | court | 15 |
| 14 | gym | gym | NOUN | NN | compound | court | 15 |
| 15 | court | court | NOUN | NN | pobj | on | 12 |
| 16 | . | . | PUNCT | . | punct | holds | 6 |
| 17 | Several | several | ADJ | JJ | amod | people | 18 |
| 18 | people | people | NOUN | NNS | nsubj | play | 24 |
| 19 | in | in | ADP | IN | prep | people | 18 |
| 20 | pink | pink | ADJ | JJ | amod | shirts | 23 |
| 21 | and | and | CCONJ | CC | cc | pink | 20 |
| 22 | gray | gray | ADJ | JJ | conj | pink | 20 |
| 23 | shirts | shirt | NOUN | NNS | pobj | in | 19 |
| 24 | play | play | VERB | VBP | ROOT | play | 24 |
| 25 | nearby | nearby | ADV | RB | advmod | play | 24 |
| 26 | . | . | PUNCT | . | punct | play | 24 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | shirt | shirt | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | white | white | chunk1 | 4 | color_attribute | high |
| m3 | object | basketball | basketball | chunk2 | 8 | noun_chunk_root | high |
| m4 | object | head | head | chunk3 | 11 | noun_chunk_root | high |
| m5 | attribute | his | his | chunk3 | 10 | modifier_attribute | medium |
| m6 | object | court | court | chunk4 | 15 | noun_chunk_root | high |
| m7 | attribute | gym | gym | chunk4 | 14 | compound_modifier | medium |
| m8 | object | people | people | chunk5 | 18 | noun_chunk_root | high |
| m9 | attribute | Several | several | chunk5 | 17 | modifier_attribute | medium |
| m10 | object | shirts | shirt | chunk6 | 23 | noun_chunk_root | high |
| m11 | attribute | pink | pink | chunk6 | 20 | color_attribute | high |
| m12 | attribute | gray | gray | chunk6 | 22 | color_attribute | high |
| m13 | action | holds | hold | doc | 6 | verb_predicate | high |
| m14 | action | play | play | doc | 24 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> shirt |
| e1 | has_attribute | m4 | m5 | medium | chunk3 poss -> head |
| e2 | has_attribute | m6 | m7 | medium | chunk4 compound -> court |
| e3 | has_attribute | m8 | m9 | medium | chunk5 amod -> people |
| e4 | has_attribute | m10 | m11 | high | chunk6 amod -> shirts |
| e5 | has_attribute | m10 | m12 | high | chunk6 conj -> shirts |
| e6 | agent | m13 | m0 | medium | nsubj -> holds |
| e7 | patient | m13 | m3 | medium | dobj -> holds |
| e8 | agent | m14 | m8 | medium | nsubj -> play |
| e9 | relation | m0 | m1 | high | in |
| e10 | relation | m0 | m4 | high | above |
| e11 | relation | m0 | m6 | high | on |
| e12 | relation | m8 | m10 | high | in |

## 13

**caption_shape:** `multi-sentence`
**caption_id:** `097c49356f8c365fc2a90e92a076d206bee7aa6abeea8fadad4ca092b9c5c414`

> A desert landscape with mountains under a cloudy sky. A black object sits on the dry, rocky ground.

### Sentences
| sentence | token_span |
| --- | --- |
| A desert landscape with mountains under a cloudy sky. | 0:10 |
| A black object sits on the dry, rocky ground. | 10:21 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A desert landscape | landscape | landscape | ROOT | landscape | 0:3 |
| mountains | mountains | mountain | pobj | with | 4:5 |
| a cloudy sky | sky | sky | pobj | under | 6:9 |
| A black object | object | object | nsubj | sits | 10:13 |
| the dry, rocky ground | ground | ground | pobj | on | 15:20 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | landscape | 2 |
| 1 | desert | desert | NOUN | NN | compound | landscape | 2 |
| 2 | landscape | landscape | NOUN | NN | ROOT | landscape | 2 |
| 3 | with | with | ADP | IN | prep | landscape | 2 |
| 4 | mountains | mountain | NOUN | NNS | pobj | with | 3 |
| 5 | under | under | ADP | IN | prep | mountains | 4 |
| 6 | a | a | DET | DT | det | sky | 8 |
| 7 | cloudy | cloudy | ADJ | JJ | amod | sky | 8 |
| 8 | sky | sky | NOUN | NN | pobj | under | 5 |
| 9 | . | . | PUNCT | . | punct | landscape | 2 |
| 10 | A | a | DET | DT | det | object | 12 |
| 11 | black | black | ADJ | JJ | amod | object | 12 |
| 12 | object | object | NOUN | NN | nsubj | sits | 13 |
| 13 | sits | sit | VERB | VBZ | ROOT | sits | 13 |
| 14 | on | on | ADP | IN | prep | sits | 13 |
| 15 | the | the | DET | DT | det | ground | 19 |
| 16 | dry | dry | ADJ | JJ | amod | ground | 19 |
| 17 | , | , | PUNCT | , | punct | ground | 19 |
| 18 | rocky | rocky | ADJ | JJ | amod | ground | 19 |
| 19 | ground | ground | NOUN | NN | pobj | on | 14 |
| 20 | . | . | PUNCT | . | punct | sits | 13 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | landscape | landscape | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | desert | desert | chunk0 | 1 | compound_modifier | medium |
| m2 | object | mountains | mountain | chunk1 | 4 | noun_chunk_root | high |
| m3 | object | sky | sky | chunk2 | 8 | noun_chunk_root | high |
| m4 | attribute | cloudy | cloudy | chunk2 | 7 | modifier_attribute | medium |
| m5 | object | object | object | chunk3 | 12 | noun_chunk_root | high |
| m6 | attribute | black | black | chunk3 | 11 | color_attribute | high |
| m7 | object | ground | ground | chunk4 | 19 | noun_chunk_root | high |
| m8 | attribute | dry | dry | chunk4 | 16 | modifier_attribute | medium |
| m9 | attribute | rocky | rocky | chunk4 | 18 | modifier_attribute | medium |
| m10 | action | sits | sit | doc | 13 | verb_predicate | high |

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

## 14

**caption_shape:** `tag-list-like`
**caption_id:** `0a404060dc0c39ea0ea98fdd78558ac2b78bfd5c7e8cce93647fda2de2964014`

> brown boot, indoor, brick wall, display, large

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | brown boot | brown boot | 0:10 |
| t1 | indoor | indoor | 12:18 |
| t2 | brick wall | brick wall | 20:30 |
| t3 | display | display | 32:39 |
| t4 | large | large | 41:46 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | brown boot | boot | boot | ROOT | boot | 0:2 | 0:10 |
| t1 | indoor | indoor | indoor | ROOT | indoor | 0:1 | 12:18 |
| t2 | brick wall | wall | wall | ROOT | wall | 0:2 | 20:30 |
| t3 | display | display | display | ROOT | display | 0:1 | 32:39 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | brown | brown | ADJ | ADJ | JJ | JJ | amod | boot | 1 | 0:5 |
| t0 | 1 | boot | boot | NOUN | NOUN | NN | NN | ROOT | boot | 1 | 6:10 |
| t1 | 0 | indoor | indoor | NOUN | NOUN | NN | NN | ROOT | indoor | 0 | 12:18 |
| t2 | 0 | brick | brick | NOUN | NOUN | NN | NN | compound | wall | 1 | 20:25 |
| t2 | 1 | wall | wall | NOUN | NOUN | NN | NN | ROOT | wall | 1 | 26:30 |
| t3 | 0 | display | display | NOUN | NOUN | NN | NN | ROOT | display | 0 | 32:39 |
| t4 | 0 | large | large | ADJ | ADJ | JJ | JJ | ROOT | large | 0 | 41:46 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | boot | boot | t0 | 1 | segment_head | high |
| m1 | attribute | brown | brown | t0 | 0 | attribute | high |
| m2 | context | indoor | indoor | t1 | 0 | scene_context | high |
| m3 | object | wall | wall | t2 | 1 | segment_head | high |
| m4 | attribute | brick | brick | t2 | 0 | attribute | high |
| m5 | object | display | display | t3 | 0 | segment_head | high |
| m6 | attribute | large | large | t4 | 0 | floating_attribute | medium |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> boot |
| e1 | has_context | scene | m2 | high | t1 context tag |
| e2 | has_attribute | m3 | m4 | high | t2 internal compound -> wall |
| e3 | candidate_has_attribute | m5 | m6 | low | t4 adjacent floating attribute |

## 15

**caption_shape:** `multi-sentence`
**caption_id:** `0a74bd648e7249dd4137548b30a087f07b1abb266189a2dd623d122f285af814`

> Two men smile for the camera in a bathroom. One wears a vest and red scarf, the other a yellow shirt.

### Sentences
| sentence | token_span |
| --- | --- |
| Two men smile for the camera in a bathroom. | 0:10 |
| One wears a vest and red scarf, the other a yellow shirt. | 10:24 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Two men | men | man | nsubj | smile | 0:2 |
| the camera | camera | camera | pobj | for | 4:6 |
| a bathroom | bathroom | bathroom | pobj | in | 7:9 |
| a vest | vest | vest | dobj | wears | 12:14 |
| red scarf | scarf | scarf | conj | vest | 15:17 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Two | two | NUM | CD | nummod | men | 1 |
| 1 | men | man | NOUN | NNS | nsubj | smile | 2 |
| 2 | smile | smile | VERB | VBP | ROOT | smile | 2 |
| 3 | for | for | ADP | IN | prep | smile | 2 |
| 4 | the | the | DET | DT | det | camera | 5 |
| 5 | camera | camera | NOUN | NN | pobj | for | 3 |
| 6 | in | in | ADP | IN | prep | smile | 2 |
| 7 | a | a | DET | DT | det | bathroom | 8 |
| 8 | bathroom | bathroom | NOUN | NN | pobj | in | 6 |
| 9 | . | . | PUNCT | . | punct | smile | 2 |
| 10 | One | one | NUM | CD | nsubj | wears | 11 |
| 11 | wears | wear | VERB | VBZ | ccomp | shirt | 22 |
| 12 | a | a | DET | DT | det | vest | 13 |
| 13 | vest | vest | NOUN | NN | dobj | wears | 11 |
| 14 | and | and | CCONJ | CC | cc | vest | 13 |
| 15 | red | red | ADJ | JJ | amod | scarf | 16 |
| 16 | scarf | scarf | NOUN | NN | conj | vest | 13 |
| 17 | , | , | PUNCT | , | punct | shirt | 22 |
| 18 | the | the | DET | DT | det | other | 19 |
| 19 | other | other | ADJ | JJ | nsubj | shirt | 22 |
| 20 | a | a | DET | DT | det | shirt | 22 |
| 21 | yellow | yellow | ADJ | JJ | amod | shirt | 22 |
| 22 | shirt | shirt | NOUN | NN | ROOT | shirt | 22 |
| 23 | . | . | PUNCT | . | punct | shirt | 22 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | men | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Two | two | chunk0 | 0 | quantity | high |
| m2 | object | camera | camera | chunk1 | 5 | noun_chunk_root | high |
| m3 | object | bathroom | bathroom | chunk2 | 8 | noun_chunk_root | high |
| m4 | object | vest | vest | chunk3 | 13 | noun_chunk_root | high |
| m5 | object | scarf | scarf | chunk4 | 16 | noun_chunk_root | high |
| m6 | attribute | red | red | chunk4 | 15 | color_attribute | high |
| m7 | action | smile | smile | doc | 2 | verb_predicate | high |
| m8 | action | wears | wear | doc | 11 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 nummod -> men |
| e1 | has_attribute | m5 | m6 | high | chunk4 amod -> scarf |
| e2 | agent | m7 | m0 | medium | nsubj -> smile |
| e3 | patient | m8 | m4 | medium | dobj -> wears |
| e4 | patient | m8 | m5 | medium | dobj -> wears |
| e5 | relation | m0 | m2 | medium | for |
| e6 | relation | m0 | m3 | high | in |

## 16

**caption_shape:** `multi-sentence`
**caption_id:** `0b51847b650bf2311e48557b7b3619abd6c1246de89f64a33bb833c172fe4014`

> Children in white dresses and shirts sit on chairs during a performance. One child holds a violin, while others are seated with music stands nearby. The setting is indoors, with red curtains and blue chairs visible in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| Children in white dresses and shirts sit on chairs during a performance. | 0:13 |
| One child holds a violin, while others are seated with music stands nearby. | 13:28 |
| The setting is indoors, with red curtains and blue chairs visible in the background. | 28:44 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Children | Children | child | nsubj | sit | 0:1 |
| white dresses | dresses | dress | pobj | in | 2:4 |
| shirts | shirts | shirt | conj | dresses | 5:6 |
| chairs | chairs | chair | pobj | on | 8:9 |
| a performance | performance | performance | pobj | during | 10:12 |
| One child | child | child | nsubj | holds | 13:15 |
| a violin | violin | violin | dobj | holds | 16:18 |
| others | others | other | nsubjpass | seated | 20:21 |
| music | music | music | nsubj | stands | 24:25 |
| The setting | setting | setting | nsubj | is | 28:30 |
| red curtains | curtains | curtain | nsubj | visible | 34:36 |
| blue chairs | chairs | chair | conj | curtains | 37:39 |
| the background | background | background | pobj | in | 41:43 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Children | child | NOUN | NNS | nsubj | sit | 6 |
| 1 | in | in | ADP | IN | prep | Children | 0 |
| 2 | white | white | ADJ | JJ | amod | dresses | 3 |
| 3 | dresses | dress | NOUN | NNS | pobj | in | 1 |
| 4 | and | and | CCONJ | CC | cc | dresses | 3 |
| 5 | shirts | shirt | NOUN | NNS | conj | dresses | 3 |
| 6 | sit | sit | VERB | VBP | ROOT | sit | 6 |
| 7 | on | on | ADP | IN | prep | sit | 6 |
| 8 | chairs | chair | NOUN | NNS | pobj | on | 7 |
| 9 | during | during | ADP | IN | prep | sit | 6 |
| 10 | a | a | DET | DT | det | performance | 11 |
| 11 | performance | performance | NOUN | NN | pobj | during | 9 |
| 12 | . | . | PUNCT | . | punct | sit | 6 |
| 13 | One | one | NUM | CD | nummod | child | 14 |
| 14 | child | child | NOUN | NN | nsubj | holds | 15 |
| 15 | holds | hold | VERB | VBZ | ROOT | holds | 15 |
| 16 | a | a | DET | DT | det | violin | 17 |
| 17 | violin | violin | NOUN | NN | dobj | holds | 15 |
| 18 | , | , | PUNCT | , | punct | holds | 15 |
| 19 | while | while | SCONJ | IN | mark | seated | 22 |
| 20 | others | other | NOUN | NNS | nsubjpass | seated | 22 |
| 21 | are | be | AUX | VBP | auxpass | seated | 22 |
| 22 | seated | seat | VERB | VBN | advcl | holds | 15 |
| 23 | with | with | SCONJ | IN | mark | stands | 25 |
| 24 | music | music | NOUN | NN | nsubj | stands | 25 |
| 25 | stands | stand | VERB | VBZ | advcl | seated | 22 |
| 26 | nearby | nearby | ADV | RB | advmod | stands | 25 |
| 27 | . | . | PUNCT | . | punct | holds | 15 |
| 28 | The | the | DET | DT | det | setting | 29 |
| 29 | setting | setting | NOUN | NN | nsubj | is | 30 |
| 30 | is | be | AUX | VBZ | ROOT | is | 30 |
| 31 | indoors | indoors | ADV | RB | advmod | is | 30 |
| 32 | , | , | PUNCT | , | punct | is | 30 |
| 33 | with | with | SCONJ | IN | mark | visible | 39 |
| 34 | red | red | ADJ | JJ | amod | curtains | 35 |
| 35 | curtains | curtain | NOUN | NNS | nsubj | visible | 39 |
| 36 | and | and | CCONJ | CC | cc | curtains | 35 |
| 37 | blue | blue | ADJ | JJ | amod | chairs | 38 |
| 38 | chairs | chair | NOUN | NNS | conj | curtains | 35 |
| 39 | visible | visible | ADJ | JJ | advcl | is | 30 |
| 40 | in | in | ADP | IN | prep | visible | 39 |
| 41 | the | the | DET | DT | det | background | 42 |
| 42 | background | background | NOUN | NN | pobj | in | 40 |
| 43 | . | . | PUNCT | . | punct | is | 30 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | Children | child | chunk0 | 0 | noun_chunk_root | high |
| m1 | object | dresses | dress | chunk1 | 3 | noun_chunk_root | high |
| m2 | attribute | white | white | chunk1 | 2 | color_attribute | high |
| m3 | object | shirts | shirt | chunk2 | 5 | noun_chunk_root | high |
| m4 | object | chairs | chair | chunk3 | 8 | noun_chunk_root | high |
| m5 | object | performance | performance | chunk4 | 11 | noun_chunk_root | high |
| m6 | object | child | child | chunk5 | 14 | noun_chunk_root | high |
| m7 | quantity | One | one | chunk5 | 13 | quantity | high |
| m8 | object | violin | violin | chunk6 | 17 | noun_chunk_root | high |
| m9 | object | others | other | chunk7 | 20 | noun_chunk_root | high |
| m10 | object | music | music | chunk8 | 24 | noun_chunk_root | high |
| m11 | object | setting | setting | chunk9 | 29 | noun_chunk_root | high |
| m12 | object | curtains | curtain | chunk10 | 35 | noun_chunk_root | high |
| m13 | attribute | red | red | chunk10 | 34 | color_attribute | high |
| m14 | object | chairs | chair | chunk11 | 38 | noun_chunk_root | high |
| m15 | attribute | blue | blue | chunk11 | 37 | color_attribute | high |
| m16 | object | background | background | chunk12 | 42 | noun_chunk_root | high |
| m17 | context | indoors | indoors | doc | 31 | context_word | medium |
| m18 | context | background | background | doc | 42 | context_word | medium |
| m19 | action | sit | sit | doc | 6 | verb_predicate | high |
| m20 | action | holds | hold | doc | 15 | verb_predicate | high |
| m21 | action | seated | seat | doc | 22 | verb_predicate | high |
| m22 | action | stands | stand | doc | 25 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> dresses |
| e1 | has_quantity | m6 | m7 | high | chunk5 nummod -> child |
| e2 | has_attribute | m12 | m13 | high | chunk10 amod -> curtains |
| e3 | has_attribute | m14 | m15 | high | chunk11 amod -> chairs |
| e4 | has_context | scene | m17 | medium | context token indoors |
| e5 | has_context | scene | m18 | medium | context token background |
| e6 | agent | m19 | m0 | medium | nsubj -> sit |
| e7 | agent | m20 | m6 | medium | nsubj -> holds |
| e8 | patient | m20 | m8 | medium | dobj -> holds |
| e9 | agent | m21 | m9 | medium | nsubjpass -> seated |
| e10 | agent | m22 | m10 | medium | nsubj -> stands |
| e11 | relation | m0 | m1 | high | in |
| e12 | relation | m0 | m3 | high | in |
| e13 | relation | m0 | m4 | high | on |
| e14 | relation | m0 | m5 | medium | during |

## 17

**caption_shape:** `tag-list-like`
**caption_id:** `0bb595b117e1184dd61d50f4c00209733e3beeb7d2cce3851c9878f87971fc14`

> glass wall, worker, sidewalk, building, reflection, grass

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | glass wall | glass wall | 0:10 |
| t1 | worker | worker | 12:18 |
| t2 | sidewalk | sidewalk | 20:28 |
| t3 | building | building | 30:38 |
| t4 | reflection | reflection | 40:50 |
| t5 | grass | grass | 52:57 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | glass wall | wall | wall | ROOT | wall | 0:2 | 0:10 |
| t1 | worker | worker | worker | ROOT | worker | 0:1 | 12:18 |
| t2 | sidewalk | sidewalk | sidewalk | ROOT | sidewalk | 0:1 | 20:28 |
| t3 | building | building | building | ROOT | building | 0:1 | 30:38 |
| t4 | reflection | reflection | reflection | ROOT | reflection | 0:1 | 40:50 |
| t5 | grass | grass | grass | ROOT | grass | 0:1 | 52:57 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | glass | glass | NOUN | NOUN | NN | NN | compound | wall | 1 | 0:5 |
| t0 | 1 | wall | wall | NOUN | NOUN | NN | NN | ROOT | wall | 1 | 6:10 |
| t1 | 0 | worker | worker | NOUN | NOUN | NN | NN | ROOT | worker | 0 | 12:18 |
| t2 | 0 | sidewalk | sidewalk | NOUN | NOUN | NN | NN | ROOT | sidewalk | 0 | 20:28 |
| t3 | 0 | building | building | NOUN | NOUN | NN | NN | ROOT | building | 0 | 30:38 |
| t4 | 0 | reflection | reflection | NOUN | NOUN | NN | NN | ROOT | reflection | 0 | 40:50 |
| t5 | 0 | grass | grass | NOUN | NOUN | NN | NN | ROOT | grass | 0 | 52:57 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | wall | wall | t0 | 1 | segment_head | high |
| m1 | attribute | glass | glass | t0 | 0 | attribute | high |
| m2 | object | worker | worker | t1 | 0 | segment_head | high |
| m3 | object | sidewalk | sidewalk | t2 | 0 | segment_head | high |
| m4 | object | building | building | t3 | 0 | segment_head | high |
| m5 | object | reflection | reflection | t4 | 0 | segment_head | high |
| m6 | object | grass | grass | t5 | 0 | segment_head | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> wall |

## 18

**caption_shape:** `multi-sentence`
**caption_id:** `0c7588f2c805503462f15a197d85e1aa77344f20e2a1a6231d2f8726d4f1e414`

> A cityscape viewed from between two tall buildings at dusk. Below, streets and vehicles stretch toward a waterfront with lit-up skyscrapers in the distance. The sky shows soft orange and gray hues near the horizon.

### Sentences
| sentence | token_span |
| --- | --- |
| A cityscape viewed from between two tall buildings at dusk. | 0:11 |
| Below, streets and vehicles stretch toward a waterfront with lit-up skyscrapers in the distance. | 11:29 |
| The sky shows soft orange and gray hues near the horizon. | 29:41 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A cityscape | cityscape | cityscape | ROOT | cityscape | 0:2 |
| two tall buildings | buildings | building | pobj | between | 5:8 |
| dusk | dusk | dusk | pobj | at | 9:10 |
| streets | streets | street | nsubj | stretch | 13:14 |
| vehicles | vehicles | vehicle | conj | streets | 15:16 |
| a waterfront | waterfront | waterfront | pobj | toward | 18:20 |
| lit-up skyscrapers | skyscrapers | skyscraper | pobj | with | 21:25 |
| the distance | distance | distance | pobj | in | 26:28 |
| The sky | sky | sky | nsubj | shows | 29:31 |
| soft orange and gray hues | hues | hue | dobj | shows | 32:37 |
| the horizon | horizon | horizon | pobj | near | 38:40 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | cityscape | 1 |
| 1 | cityscape | cityscape | NOUN | NN | ROOT | cityscape | 1 |
| 2 | viewed | view | VERB | VBN | acl | cityscape | 1 |
| 3 | from | from | ADP | IN | prep | viewed | 2 |
| 4 | between | between | ADP | IN | prep | from | 3 |
| 5 | two | two | NUM | CD | nummod | buildings | 7 |
| 6 | tall | tall | ADJ | JJ | amod | buildings | 7 |
| 7 | buildings | building | NOUN | NNS | pobj | between | 4 |
| 8 | at | at | ADP | IN | prep | viewed | 2 |
| 9 | dusk | dusk | NOUN | NN | pobj | at | 8 |
| 10 | . | . | PUNCT | . | punct | cityscape | 1 |
| 11 | Below | below | ADV | RB | advmod | stretch | 16 |
| 12 | , | , | PUNCT | , | punct | stretch | 16 |
| 13 | streets | street | NOUN | NNS | nsubj | stretch | 16 |
| 14 | and | and | CCONJ | CC | cc | streets | 13 |
| 15 | vehicles | vehicle | NOUN | NNS | conj | streets | 13 |
| 16 | stretch | stretch | VERB | VBP | ROOT | stretch | 16 |
| 17 | toward | toward | ADP | IN | prep | stretch | 16 |
| 18 | a | a | DET | DT | det | waterfront | 19 |
| 19 | waterfront | waterfront | NOUN | NN | pobj | toward | 17 |
| 20 | with | with | ADP | IN | prep | waterfront | 19 |
| 21 | lit | light | VERB | VBN | amod | skyscrapers | 24 |
| 22 | - | - | PUNCT | HYPH | punct | lit | 21 |
| 23 | up | up | ADP | RP | prt | lit | 21 |
| 24 | skyscrapers | skyscraper | NOUN | NNS | pobj | with | 20 |
| 25 | in | in | ADP | IN | prep | skyscrapers | 24 |
| 26 | the | the | DET | DT | det | distance | 27 |
| 27 | distance | distance | NOUN | NN | pobj | in | 25 |
| 28 | . | . | PUNCT | . | punct | stretch | 16 |
| 29 | The | the | DET | DT | det | sky | 30 |
| 30 | sky | sky | NOUN | NN | nsubj | shows | 31 |
| 31 | shows | show | VERB | VBZ | ROOT | shows | 31 |
| 32 | soft | soft | ADJ | JJ | amod | hues | 36 |
| 33 | orange | orange | NOUN | NN | nmod | hues | 36 |
| 34 | and | and | CCONJ | CC | cc | orange | 33 |
| 35 | gray | gray | ADJ | JJ | conj | orange | 33 |
| 36 | hues | hue | NOUN | NNS | dobj | shows | 31 |
| 37 | near | near | ADP | IN | prep | shows | 31 |
| 38 | the | the | DET | DT | det | horizon | 39 |
| 39 | horizon | horizon | NOUN | NN | pobj | near | 37 |
| 40 | . | . | PUNCT | . | punct | shows | 31 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | cityscape | cityscape | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | buildings | building | chunk1 | 7 | noun_chunk_root | high |
| m2 | quantity | two | two | chunk1 | 5 | quantity | high |
| m3 | attribute | tall | tall | chunk1 | 6 | size_attribute | high |
| m4 | object | dusk | dusk | chunk2 | 9 | noun_chunk_root | high |
| m5 | object | streets | street | chunk3 | 13 | noun_chunk_root | high |
| m6 | object | vehicles | vehicle | chunk4 | 15 | noun_chunk_root | high |
| m7 | object | waterfront | waterfront | chunk5 | 19 | noun_chunk_root | high |
| m8 | object | skyscrapers | skyscraper | chunk6 | 24 | noun_chunk_root | high |
| m9 | attribute | lit | light | chunk6 | 21 | visual_attribute | medium |
| m10 | object | distance | distance | chunk7 | 27 | noun_chunk_root | high |
| m11 | object | sky | sky | chunk8 | 30 | noun_chunk_root | high |
| m12 | object | hues | hue | chunk9 | 36 | noun_chunk_root | high |
| m13 | attribute | soft | soft | chunk9 | 32 | modifier_attribute | medium |
| m14 | attribute | orange | orange | chunk9 | 33 | color_attribute | high |
| m15 | attribute | gray | gray | chunk9 | 35 | color_attribute | high |
| m16 | object | horizon | horizon | chunk10 | 39 | noun_chunk_root | high |
| m17 | context | dusk | dusk | doc | 9 | context_word | medium |
| m18 | action | viewed | view | doc | 2 | verb_predicate | high |
| m19 | action | stretch | stretch | doc | 16 | verb_predicate | high |
| m20 | action | shows | show | doc | 31 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m1 | m2 | high | chunk1 nummod -> buildings |
| e1 | has_attribute | m1 | m3 | high | chunk1 amod -> buildings |
| e2 | has_attribute | m8 | m9 | medium | chunk6 amod -> skyscrapers |
| e3 | has_attribute | m12 | m13 | medium | chunk9 amod -> hues |
| e4 | has_attribute | m12 | m14 | high | chunk9 nmod -> hues |
| e5 | has_attribute | m12 | m15 | high | chunk9 conj -> hues |
| e6 | has_context | scene | m17 | medium | context token dusk |
| e7 | agent | m19 | m5 | medium | nsubj -> stretch |
| e8 | agent | m19 | m6 | medium | nsubj -> stretch |
| e9 | agent | m20 | m11 | medium | nsubj -> shows |
| e10 | patient | m20 | m12 | medium | dobj -> shows |
| e11 | relation | m0 | m17 | medium | at |
| e12 | relation | m5 | m7 | medium | toward |
| e13 | relation | m7 | m8 | high | with |
| e14 | relation | m8 | m10 | high | in |
| e15 | relation | m11 | m16 | high | near |

## 19

**caption_shape:** `multi-sentence`
**caption_id:** `0e1b08528f25adc13662435f45a0bd1f5e90270018e6ae5fb0a30d822a589c14`

> A paved road with a yellow line runs along the bottom of the frame. Beyond it, a vast green field stretches to the horizon under a clear blue sky. A few distant trees and power lines are visible in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| A paved road with a yellow line runs along the bottom of the frame. | 0:15 |
| Beyond it, a vast green field stretches to the horizon under a clear blue sky. | 15:32 |
| A few distant trees and power lines are visible in the background. | 32:45 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A paved road | road | road | nsubj | runs | 0:3 |
| a yellow line | line | line | pobj | with | 4:7 |
| the bottom | bottom | bottom | pobj | along | 9:11 |
| the frame | frame | frame | pobj | of | 12:14 |
| it | it | it | pobj | Beyond | 16:17 |
| a vast green field | field | field | nsubj | stretches | 18:22 |
| the horizon | horizon | horizon | pobj | to | 24:26 |
| a clear blue sky | sky | sky | pobj | under | 27:31 |
| A few distant trees | trees | tree | nsubj | are | 32:36 |
| power lines | lines | line | conj | trees | 37:39 |
| the background | background | background | pobj | in | 42:44 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | road | 2 |
| 1 | paved | paved | ADJ | JJ | amod | road | 2 |
| 2 | road | road | NOUN | NN | nsubj | runs | 7 |
| 3 | with | with | ADP | IN | prep | road | 2 |
| 4 | a | a | DET | DT | det | line | 6 |
| 5 | yellow | yellow | ADJ | JJ | amod | line | 6 |
| 6 | line | line | NOUN | NN | pobj | with | 3 |
| 7 | runs | run | VERB | VBZ | ROOT | runs | 7 |
| 8 | along | along | ADP | IN | prep | runs | 7 |
| 9 | the | the | DET | DT | det | bottom | 10 |
| 10 | bottom | bottom | NOUN | NN | pobj | along | 8 |
| 11 | of | of | ADP | IN | prep | bottom | 10 |
| 12 | the | the | DET | DT | det | frame | 13 |
| 13 | frame | frame | NOUN | NN | pobj | of | 11 |
| 14 | . | . | PUNCT | . | punct | runs | 7 |
| 15 | Beyond | beyond | ADP | IN | prep | stretches | 22 |
| 16 | it | it | PRON | PRP | pobj | Beyond | 15 |
| 17 | , | , | PUNCT | , | punct | stretches | 22 |
| 18 | a | a | DET | DT | det | field | 21 |
| 19 | vast | vast | ADJ | JJ | amod | field | 21 |
| 20 | green | green | ADJ | JJ | amod | field | 21 |
| 21 | field | field | NOUN | NN | nsubj | stretches | 22 |
| 22 | stretches | stretch | VERB | VBZ | ROOT | stretches | 22 |
| 23 | to | to | ADP | IN | prep | stretches | 22 |
| 24 | the | the | DET | DT | det | horizon | 25 |
| 25 | horizon | horizon | NOUN | NN | pobj | to | 23 |
| 26 | under | under | ADP | IN | prep | stretches | 22 |
| 27 | a | a | DET | DT | det | sky | 30 |
| 28 | clear | clear | ADJ | JJ | amod | sky | 30 |
| 29 | blue | blue | ADJ | JJ | amod | sky | 30 |
| 30 | sky | sky | NOUN | NN | pobj | under | 26 |
| 31 | . | . | PUNCT | . | punct | stretches | 22 |
| 32 | A | a | DET | DT | quantmod | few | 33 |
| 33 | few | few | ADJ | JJ | nummod | trees | 35 |
| 34 | distant | distant | ADJ | JJ | amod | trees | 35 |
| 35 | trees | tree | NOUN | NNS | nsubj | are | 39 |
| 36 | and | and | CCONJ | CC | cc | trees | 35 |
| 37 | power | power | NOUN | NN | compound | lines | 38 |
| 38 | lines | line | NOUN | NNS | conj | trees | 35 |
| 39 | are | be | AUX | VBP | ROOT | are | 39 |
| 40 | visible | visible | ADJ | JJ | acomp | are | 39 |
| 41 | in | in | ADP | IN | prep | are | 39 |
| 42 | the | the | DET | DT | det | background | 43 |
| 43 | background | background | NOUN | NN | pobj | in | 41 |
| 44 | . | . | PUNCT | . | punct | are | 39 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | road | road | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | paved | paved | chunk0 | 1 | visual_attribute | medium |
| m2 | object | line | line | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | yellow | yellow | chunk1 | 5 | color_attribute | high |
| m4 | object | bottom | bottom | chunk2 | 10 | noun_chunk_root | high |
| m5 | object | frame | frame | chunk3 | 13 | noun_chunk_root | high |
| m6 | object | it | it | chunk4 | 16 | noun_chunk_root | high |
| m7 | object | field | field | chunk5 | 21 | noun_chunk_root | high |
| m8 | attribute | vast | vast | chunk5 | 19 | modifier_attribute | medium |
| m9 | attribute | green | green | chunk5 | 20 | color_attribute | high |
| m10 | object | horizon | horizon | chunk6 | 25 | noun_chunk_root | high |
| m11 | object | sky | sky | chunk7 | 30 | noun_chunk_root | high |
| m12 | attribute | clear | clear | chunk7 | 28 | visual_attribute | medium |
| m13 | attribute | blue | blue | chunk7 | 29 | color_attribute | high |
| m14 | object | trees | tree | chunk8 | 35 | noun_chunk_root | high |
| m15 | quantity | few | few | chunk8 | 33 | quantity | high |
| m16 | attribute | distant | distant | chunk8 | 34 | modifier_attribute | medium |
| m17 | object | lines | line | chunk9 | 38 | noun_chunk_root | high |
| m18 | attribute | power | power | chunk9 | 37 | compound_modifier | medium |
| m19 | object | background | background | chunk10 | 43 | noun_chunk_root | high |
| m20 | context | background | background | doc | 43 | context_word | medium |
| m21 | action | runs | run | doc | 7 | verb_predicate | high |
| m22 | action | stretches | stretch | doc | 22 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> road |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> line |
| e2 | has_attribute | m7 | m8 | medium | chunk5 amod -> field |
| e3 | has_attribute | m7 | m9 | high | chunk5 amod -> field |
| e4 | has_attribute | m11 | m12 | medium | chunk7 amod -> sky |
| e5 | has_attribute | m11 | m13 | high | chunk7 amod -> sky |
| e6 | has_quantity | m14 | m15 | high | chunk8 nummod -> trees |
| e7 | has_attribute | m14 | m16 | medium | chunk8 amod -> trees |
| e8 | has_attribute | m17 | m18 | medium | chunk9 compound -> lines |
| e9 | has_context | scene | m20 | medium | context token background |
| e10 | agent | m21 | m0 | medium | nsubj -> runs |
| e11 | agent | m22 | m7 | medium | nsubj -> stretches |
| e12 | relation | m0 | m2 | high | with |
| e13 | relation | m0 | m4 | medium | along |
| e14 | relation | m4 | m5 | medium | of |
| e15 | relation | m7 | m6 | high | beyond |
| e16 | relation | m7 | m10 | medium | to |
| e17 | relation | m7 | m11 | high | under |
| e18 | relation | m14 | m20 | high | in |

## 20

**caption_shape:** `sentence-like`
**caption_id:** `0e1b59c09008af99453425a727c0feab2c5e69433138763b5813eb069b64a814`

> A teacher and six students in white shirts stand together on a colorful classroom rug.

### Sentences
| sentence | token_span |
| --- | --- |
| A teacher and six students in white shirts stand together on a colorful classroom rug. | 0:16 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A teacher | teacher | teacher | nsubj | stand | 0:2 |
| six students | students | student | conj | teacher | 3:5 |
| white shirts | shirts | shirt | pobj | in | 6:8 |
| a colorful classroom rug | rug | rug | pobj | on | 11:15 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | teacher | 1 |
| 1 | teacher | teacher | NOUN | NN | nsubj | stand | 8 |
| 2 | and | and | CCONJ | CC | cc | teacher | 1 |
| 3 | six | six | NUM | CD | nummod | students | 4 |
| 4 | students | student | NOUN | NNS | conj | teacher | 1 |
| 5 | in | in | ADP | IN | prep | students | 4 |
| 6 | white | white | ADJ | JJ | amod | shirts | 7 |
| 7 | shirts | shirt | NOUN | NNS | pobj | in | 5 |
| 8 | stand | stand | VERB | VBP | ROOT | stand | 8 |
| 9 | together | together | ADV | RB | advmod | stand | 8 |
| 10 | on | on | ADP | IN | prep | stand | 8 |
| 11 | a | a | DET | DT | det | rug | 14 |
| 12 | colorful | colorful | ADJ | JJ | amod | rug | 14 |
| 13 | classroom | classroom | NOUN | NN | compound | rug | 14 |
| 14 | rug | rug | NOUN | NN | pobj | on | 10 |
| 15 | . | . | PUNCT | . | punct | stand | 8 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | teacher | teacher | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | students | student | chunk1 | 4 | noun_chunk_root | high |
| m2 | quantity | six | six | chunk1 | 3 | quantity | high |
| m3 | object | shirts | shirt | chunk2 | 7 | noun_chunk_root | high |
| m4 | attribute | white | white | chunk2 | 6 | color_attribute | high |
| m5 | object | rug | rug | chunk3 | 14 | noun_chunk_root | high |
| m6 | attribute | colorful | colorful | chunk3 | 12 | modifier_attribute | medium |
| m7 | attribute | classroom | classroom | chunk3 | 13 | compound_modifier | medium |
| m8 | action | stand | stand | doc | 8 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m1 | m2 | high | chunk1 nummod -> students |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> shirts |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> rug |
| e3 | has_attribute | m5 | m7 | medium | chunk3 compound -> rug |
| e4 | agent | m8 | m0 | medium | nsubj -> stand |
| e5 | agent | m8 | m1 | medium | nsubj -> stand |
| e6 | relation | m1 | m3 | high | in |
| e7 | relation | m0 | m5 | high | on |
