# spaCy Parse Inspection

- input: `data\gpic_captions_eval\val\gpic_val_00000.jsonl.gz`
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
| The scene appears outdoors on a forest floor or fallen tree trunk. | 32:44 |

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
| fallen tree trunk | tree trunk | tree_trunk | conj | floor | 41:43 |

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
| 41 | fallen | fallen | ADJ | JJ | amod | tree trunk | 42 |
| 42 | tree trunk | tree_trunk | NOUN | NN | conj | floor | 39 |
| 43 | . | . | PUNCT | . | punct | appears | 34 |

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
| m18 | object | tree trunk | tree_trunk | chunk11 | 42 | noun_chunk_root | high |
| m19 | attribute | fallen | fallen | chunk11 | 41 | modifier_attribute | medium |
| m20 | context | outdoors | outdoors | doc | 35 | context_word | medium |
| m21 | action | crawling | crawl | doc | 6 | verb_predicate | high |
| m22 | action | shows | show | doc | 17 | verb_predicate | high |
| m23 | action | scattered | scatter | doc | 29 | verb_predicate | high |
| m24 | action | appears | appear | doc | 34 | verb_predicate | high |

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
| e7 | has_attribute | m18 | m19 | medium | chunk11 amod -> tree trunk |
| e8 | has_context | scene | m20 | medium | context token outdoors |
| e9 | agent | m21 | m0 | medium | nsubj -> crawling |
| e10 | agent | m22 | m7 | medium | nsubj -> shows |
| e11 | patient | m22 | m8 | medium | dobj -> shows |
| e12 | agent | m24 | m15 | medium | nsubj -> appears |
| e13 | relation | m0 | m2 | high | with |
| e14 | relation | m0 | m3 | high | on |
| e15 | relation | m8 | m9 | medium | of |
| e16 | relation | m7 | m10 | high | with |
| e17 | relation | m7 | m12 | high | with |
| e18 | relation | m12 | m14 | medium | of |
| e19 | relation | m15 | m16 | high | on |
| e20 | relation | m15 | m18 | high | on |

## 03

**caption_shape:** `multi-sentence`
**caption_id:** `0326facce37e93230108fb311cc653eecb8ee62a67a1f0d9f95525ddd9fe3014`

> A woman stands at a podium speaking in front of an audience. An American flag is behind her, and a screen shows the text "Closing the Access Divide."

**parsed_caption:**

> A woman stands at a podium speaking in front of an audience. An American flag is behind her, and a screen shows the text "Closing the Access Divide."

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 0326facce37e93230108fb311cc653eecb8ee62a67a1f0d9f95525ddd9fe3014:q0 | Closing the Access Divide. | closing the access divide. | raw_quote_span | the text | 121:149 | 121:149 |

### Sentences
| sentence | token_span |
| --- | --- |
| A woman stands at a podium speaking in front of an audience. | 0:13 |
| An American flag is behind her, and a screen shows the text "Closing the Access Divide." | 13:26 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A woman | woman | woman | nsubj | stands | 0:2 |
| a podium | podium | podium | pobj | at | 4:6 |
| front | front | front | pobj | in | 8:9 |
| an audience | audience | audience | pobj | of | 10:12 |
| An American flag | American flag | american_flag | nsubj | is | 13:15 |
| her | her | she | pobj | behind | 17:18 |
| a screen | screen | screen | nsubj | shows | 20:22 |
| the text | text | text | dobj | shows | 23:25 |
| "Closing the Access Divide." | "Closing the Access Divide." | closing_the_access_divide. | appos | text | 25:26 |

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
| 13 | An | an | DET | DT | det | American flag | 14 |
| 14 | American flag | american_flag | NOUN | NN | nsubj | is | 15 |
| 15 | is | be | AUX | VBZ | ROOT | is | 15 |
| 16 | behind | behind | ADP | IN | prep | is | 15 |
| 17 | her | she | PRON | PRP | pobj | behind | 16 |
| 18 | , | , | PUNCT | , | punct | is | 15 |
| 19 | and | and | CCONJ | CC | cc | is | 15 |
| 20 | a | a | DET | DT | det | screen | 21 |
| 21 | screen | screen | NOUN | NN | nsubj | shows | 22 |
| 22 | shows | show | VERB | VBZ | conj | is | 15 |
| 23 | the | the | DET | DT | det | text | 24 |
| 24 | text | text | NOUN | NN | dobj | shows | 22 |
| 25 | "Closing the Access Divide." | closing_the_access_divide. | NOUN | NN | appos | text | 24 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | podium | podium | chunk1 | 5 | noun_chunk_root | high |
| m2 | object | audience | audience | chunk3 | 11 | noun_chunk_root | high |
| m3 | object | American flag | american_flag | chunk4 | 14 | noun_chunk_root | high |
| m4 | object | her | she | chunk5 | 17 | noun_chunk_root | high |
| m5 | object | screen | screen | chunk6 | 21 | noun_chunk_root | high |
| m6 | object | text | text | chunk7 | 24 | noun_chunk_root | high |
| m7 | object | "Closing the Access Divide." | closing_the_access_divide. | chunk8 | 25 | noun_chunk_root | high |
| m8 | action | stands | stand | doc | 2 | verb_predicate | high |
| m9 | action | speaking | speak | doc | 6 | verb_predicate | high |
| m10 | action | shows | show | doc | 22 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | agent | m8 | m0 | medium | nsubj -> stands |
| e1 | agent | m10 | m5 | medium | nsubj -> shows |
| e2 | patient | m10 | m6 | medium | dobj -> shows |
| e3 | relation | m0 | m1 | medium | at |
| e4 | relation | m0 | m2 | high | in_front_of |
| e5 | relation | m3 | m4 | high | behind |

## 04

**caption_shape:** `multi-sentence`
**caption_id:** `03dfd14a3d7fc8b961a00424e43bfbdfcb9eded2464416b15cc6e9441a503814`

> Three people stand with a shopping cart filled with groceries and bags. One person holds a red snack bag.

### Sentences
| sentence | token_span |
| --- | --- |
| Three people stand with a shopping cart filled with groceries and bags. | 0:12 |
| One person holds a red snack bag. | 12:20 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Three people | people | people | nsubj | stand | 0:2 |
| a shopping cart | shopping cart | shopping_cart | pobj | with | 4:6 |
| groceries | groceries | grocery | pobj | with | 8:9 |
| bags | bags | bag | conj | groceries | 10:11 |
| One person | person | person | nsubj | holds | 12:14 |
| a red snack bag | bag | bag | dobj | holds | 15:19 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Three | three | NUM | CD | nummod | people | 1 |
| 1 | people | people | NOUN | NNS | nsubj | stand | 2 |
| 2 | stand | stand | VERB | VBP | ROOT | stand | 2 |
| 3 | with | with | ADP | IN | prep | stand | 2 |
| 4 | a | a | DET | DT | det | shopping cart | 5 |
| 5 | shopping cart | shopping_cart | NOUN | NN | pobj | with | 3 |
| 6 | filled | fill | VERB | VBN | acl | shopping cart | 5 |
| 7 | with | with | ADP | IN | prep | filled | 6 |
| 8 | groceries | grocery | NOUN | NNS | pobj | with | 7 |
| 9 | and | and | CCONJ | CC | cc | groceries | 8 |
| 10 | bags | bag | NOUN | NNS | conj | groceries | 8 |
| 11 | . | . | PUNCT | . | punct | stand | 2 |
| 12 | One | one | NUM | CD | nummod | person | 13 |
| 13 | person | person | NOUN | NN | nsubj | holds | 14 |
| 14 | holds | hold | VERB | VBZ | ROOT | holds | 14 |
| 15 | a | a | DET | DT | det | bag | 18 |
| 16 | red | red | ADJ | JJ | amod | bag | 18 |
| 17 | snack | snack | NOUN | NN | compound | bag | 18 |
| 18 | bag | bag | NOUN | NN | dobj | holds | 14 |
| 19 | . | . | PUNCT | . | punct | holds | 14 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Three | three | chunk0 | 0 | quantity | high |
| m2 | object | shopping cart | shopping_cart | chunk1 | 5 | noun_chunk_root | high |
| m3 | object | groceries | grocery | chunk2 | 8 | noun_chunk_root | high |
| m4 | object | bags | bag | chunk3 | 10 | noun_chunk_root | high |
| m5 | object | person | person | chunk4 | 13 | noun_chunk_root | high |
| m6 | quantity | One | one | chunk4 | 12 | quantity | high |
| m7 | object | bag | bag | chunk5 | 18 | noun_chunk_root | high |
| m8 | attribute | red | red | chunk5 | 16 | color_attribute | high |
| m9 | attribute | snack | snack | chunk5 | 17 | compound_modifier | medium |
| m10 | action | stand | stand | doc | 2 | verb_predicate | high |
| m11 | action | filled | fill | doc | 6 | verb_predicate | high |
| m12 | action | holds | hold | doc | 14 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 nummod -> people |
| e1 | has_quantity | m5 | m6 | high | chunk4 nummod -> person |
| e2 | has_attribute | m7 | m8 | high | chunk5 amod -> bag |
| e3 | has_attribute | m7 | m9 | medium | chunk5 compound -> bag |
| e4 | agent | m10 | m0 | medium | nsubj -> stand |
| e5 | agent | m12 | m5 | medium | nsubj -> holds |
| e6 | patient | m12 | m7 | medium | dobj -> holds |
| e7 | relation | m0 | m2 | high | with |
| e8 | relation | m2 | m3 | high | with |
| e9 | relation | m2 | m4 | high | with |

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
| t4 | wine glasses | wine glasses | wine_glass | ROOT | wine glasses | 0:1 | 57:69 |

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
| t4 | 0 | wine glasses | wine_glass | NOUN | NOUN | NN | NN | ROOT | wine glasses | 0 | 57:69 |

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
| m7 | object | wine glasses | wine_glass | t4 | 0 | segment_head | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> couple |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> party |
| e2 | has_attribute | m4 | m5 | high | t2 internal amod -> flags |

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

> A poster on a black trash can reads "BANG GOES THE KNIGHTHOOD" with a silhouette of a man in a hat. The scene is on a city sidewalk.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 05784a8cb72a17349e2cd4389708153527b40af80a043636d0ff17fdcf16c014:q0 | BANG GOES THE KNIGHTHOOD | bang goes the knighthood | raw_quote_span |  | 36:62 | 36:62 |

### Sentences
| sentence | token_span |
| --- | --- |
| A poster on a black trash can reads "BANG GOES THE KNIGHTHOOD" with a silhouette of a man in a hat. | 0:18 |
| The scene is on a city sidewalk. | 18:26 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A poster | poster | poster | nsubj | reads | 0:2 |
| a black trash can | trash can | trash_can | pobj | on | 3:6 |
| "BANG GOES THE KNIGHTHOOD" | "BANG GOES THE KNIGHTHOOD" | bang_goes_the_knighthood | dobj | reads | 7:8 |
| a silhouette | silhouette | silhouette | pobj | with | 9:11 |
| a man | man | man | pobj | of | 12:14 |
| a hat | hat | hat | pobj | in | 15:17 |
| The scene | scene | scene | nsubj | is | 18:20 |
| a city sidewalk | sidewalk | sidewalk | pobj | on | 22:25 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | poster | 1 |
| 1 | poster | poster | NOUN | NN | nsubj | reads | 6 |
| 2 | on | on | ADP | IN | prep | poster | 1 |
| 3 | a | a | DET | DT | det | trash can | 5 |
| 4 | black | black | ADJ | JJ | amod | trash can | 5 |
| 5 | trash can | trash_can | NOUN | NN | pobj | on | 2 |
| 6 | reads | read | VERB | VBZ | ROOT | reads | 6 |
| 7 | "BANG GOES THE KNIGHTHOOD" | bang_goes_the_knighthood | PROPN | NNP | dobj | reads | 6 |
| 8 | with | with | ADP | IN | prep | reads | 6 |
| 9 | a | a | DET | DT | det | silhouette | 10 |
| 10 | silhouette | silhouette | NOUN | NN | pobj | with | 8 |
| 11 | of | of | ADP | IN | prep | silhouette | 10 |
| 12 | a | a | DET | DT | det | man | 13 |
| 13 | man | man | NOUN | NN | pobj | of | 11 |
| 14 | in | in | ADP | IN | prep | man | 13 |
| 15 | a | a | DET | DT | det | hat | 16 |
| 16 | hat | hat | NOUN | NN | pobj | in | 14 |
| 17 | . | . | PUNCT | . | punct | reads | 6 |
| 18 | The | the | DET | DT | det | scene | 19 |
| 19 | scene | scene | NOUN | NN | nsubj | is | 20 |
| 20 | is | be | AUX | VBZ | ROOT | is | 20 |
| 21 | on | on | ADP | IN | prep | is | 20 |
| 22 | a | a | DET | DT | det | sidewalk | 24 |
| 23 | city | city | NOUN | NN | compound | sidewalk | 24 |
| 24 | sidewalk | sidewalk | NOUN | NN | pobj | on | 21 |
| 25 | . | . | PUNCT | . | punct | is | 20 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | poster | poster | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | trash can | trash_can | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | black | black | chunk1 | 4 | color_attribute | high |
| m3 | object | "BANG GOES THE KNIGHTHOOD" | bang_goes_the_knighthood | chunk2 | 7 | noun_chunk_root | high |
| m4 | object | silhouette | silhouette | chunk3 | 10 | noun_chunk_root | high |
| m5 | object | man | man | chunk4 | 13 | noun_chunk_root | high |
| m6 | object | hat | hat | chunk5 | 16 | noun_chunk_root | high |
| m7 | object | scene | scene | chunk6 | 19 | noun_chunk_root | high |
| m8 | object | sidewalk | sidewalk | chunk7 | 24 | noun_chunk_root | high |
| m9 | attribute | city | city | chunk7 | 23 | compound_modifier | medium |
| m10 | action | reads | read | doc | 6 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> trash can |
| e1 | has_attribute | m8 | m9 | medium | chunk7 compound -> sidewalk |
| e2 | agent | m10 | m0 | medium | nsubj -> reads |
| e3 | patient | m10 | m3 | medium | dobj -> reads |
| e4 | relation | m0 | m1 | high | on |
| e5 | relation | m0 | m4 | high | with |
| e6 | relation | m4 | m5 | medium | of |
| e7 | relation | m5 | m6 | high | in |
| e8 | relation | m7 | m8 | high | on |

## 09

**caption_shape:** `multi-sentence`
**caption_id:** `0670190ac8436d736a62a8bf08625ad242a7891121da4f518b00c9642570bc14`

> A young child with blonde hair smiles widely while wearing a blue and white striped hat. The child is bare-shouldered and appears indoors, with a window visible in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| A young child with blonde hair smiles widely while wearing a blue and white striped hat. | 0:17 |
| The child is bare-shouldered and appears indoors, with a window visible in the background. | 17:33 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A young child | child | child | nsubj | smiles | 0:3 |
| blonde hair | hair | hair | pobj | with | 4:6 |
| a blue and white striped hat | hat | hat | dobj | wearing | 10:16 |
| The child | child | child | nsubj | is | 17:19 |
| a window | window | window | pobj | with | 26:28 |
| the background | background | background | pobj | in | 30:32 |

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
| 20 | bare-shouldered | bare-shouldered | ADJ | JJ | acomp | is | 19 |
| 21 | and | and | CCONJ | CC | cc | is | 19 |
| 22 | appears | appear | VERB | VBZ | conj | is | 19 |
| 23 | indoors | indoors | ADV | RB | advmod | appears | 22 |
| 24 | , | , | PUNCT | , | punct | appears | 22 |
| 25 | with | with | ADP | IN | prep | appears | 22 |
| 26 | a | a | DET | DT | det | window | 27 |
| 27 | window | window | NOUN | NN | pobj | with | 25 |
| 28 | visible | visible | ADJ | JJ | amod | window | 27 |
| 29 | in | in | ADP | IN | prep | visible | 28 |
| 30 | the | the | DET | DT | det | background | 31 |
| 31 | background | background | NOUN | NN | pobj | in | 29 |
| 32 | . | . | PUNCT | . | punct | is | 19 |

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
| m9 | object | window | window | chunk4 | 27 | noun_chunk_root | high |
| m10 | object | background | background | chunk5 | 31 | noun_chunk_root | high |
| m11 | context | indoors | indoors | doc | 23 | context_word | medium |
| m12 | context | background | background | doc | 31 | context_word | medium |
| m13 | action | smiles | smile | doc | 6 | verb_predicate | high |
| m14 | action | wearing | wear | doc | 9 | verb_predicate | high |
| m15 | action | appears | appear | doc | 22 | verb_predicate | high |

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
| One child holds a violin, while others are seated with music stands nearby. | 13:27 |
| The setting is indoors, with red curtains and blue chairs visible in the background. | 27:43 |

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
| music stands | music stands | music_stand | pobj | with | 24:25 |
| The setting | setting | setting | nsubj | is | 27:29 |
| red curtains | curtains | curtain | nsubj | visible | 33:35 |
| blue chairs | chairs | chair | conj | curtains | 36:38 |
| the background | background | background | pobj | in | 40:42 |

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
| 23 | with | with | ADP | IN | prep | seated | 22 |
| 24 | music stands | music_stand | NOUN | NN | pobj | with | 23 |
| 25 | nearby | nearby | ADV | RB | advmod | music stands | 24 |
| 26 | . | . | PUNCT | . | punct | holds | 15 |
| 27 | The | the | DET | DT | det | setting | 28 |
| 28 | setting | setting | NOUN | NN | nsubj | is | 29 |
| 29 | is | be | AUX | VBZ | ROOT | is | 29 |
| 30 | indoors | indoors | ADV | RB | advmod | is | 29 |
| 31 | , | , | PUNCT | , | punct | is | 29 |
| 32 | with | with | SCONJ | IN | mark | visible | 38 |
| 33 | red | red | ADJ | JJ | amod | curtains | 34 |
| 34 | curtains | curtain | NOUN | NNS | nsubj | visible | 38 |
| 35 | and | and | CCONJ | CC | cc | curtains | 34 |
| 36 | blue | blue | ADJ | JJ | amod | chairs | 37 |
| 37 | chairs | chair | NOUN | NNS | conj | curtains | 34 |
| 38 | visible | visible | ADJ | JJ | advcl | is | 29 |
| 39 | in | in | ADP | IN | prep | visible | 38 |
| 40 | the | the | DET | DT | det | background | 41 |
| 41 | background | background | NOUN | NN | pobj | in | 39 |
| 42 | . | . | PUNCT | . | punct | is | 29 |

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
| m10 | object | music stands | music_stand | chunk8 | 24 | noun_chunk_root | high |
| m11 | object | setting | setting | chunk9 | 28 | noun_chunk_root | high |
| m12 | object | curtains | curtain | chunk10 | 34 | noun_chunk_root | high |
| m13 | attribute | red | red | chunk10 | 33 | color_attribute | high |
| m14 | object | chairs | chair | chunk11 | 37 | noun_chunk_root | high |
| m15 | attribute | blue | blue | chunk11 | 36 | color_attribute | high |
| m16 | object | background | background | chunk12 | 41 | noun_chunk_root | high |
| m17 | context | indoors | indoors | doc | 30 | context_word | medium |
| m18 | context | background | background | doc | 41 | context_word | medium |
| m19 | action | sit | sit | doc | 6 | verb_predicate | high |
| m20 | action | holds | hold | doc | 15 | verb_predicate | high |
| m21 | action | seated | seat | doc | 22 | verb_predicate | high |

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
| e10 | relation | m0 | m1 | high | in |
| e11 | relation | m0 | m3 | high | in |
| e12 | relation | m0 | m4 | high | on |
| e13 | relation | m0 | m5 | medium | during |
| e14 | relation | m9 | m10 | high | with |

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
| Below, streets and vehicles stretch toward a waterfront with lit-up skyscrapers in the distance. | 11:27 |
| The sky shows soft orange and gray hues near the horizon. | 27:39 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A cityscape | cityscape | cityscape | ROOT | cityscape | 0:2 |
| two tall buildings | buildings | building | pobj | between | 5:8 |
| dusk | dusk | dusk | pobj | at | 9:10 |
| streets | streets | street | nsubj | stretch | 13:14 |
| vehicles | vehicles | vehicle | conj | streets | 15:16 |
| a waterfront | waterfront | waterfront | pobj | toward | 18:20 |
| lit-up skyscrapers | skyscrapers | skyscraper | pobj | with | 21:23 |
| the distance | distance | distance | pobj | in | 24:26 |
| The sky | sky | sky | nsubj | shows | 27:29 |
| soft orange and gray hues | hues | hue | dobj | shows | 30:35 |
| the horizon | horizon | horizon | pobj | near | 36:38 |

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
| 21 | lit-up | lit-up | VERB | VBN | amod | skyscrapers | 22 |
| 22 | skyscrapers | skyscraper | NOUN | NNS | pobj | with | 20 |
| 23 | in | in | ADP | IN | prep | skyscrapers | 22 |
| 24 | the | the | DET | DT | det | distance | 25 |
| 25 | distance | distance | NOUN | NN | pobj | in | 23 |
| 26 | . | . | PUNCT | . | punct | stretch | 16 |
| 27 | The | the | DET | DT | det | sky | 28 |
| 28 | sky | sky | NOUN | NN | nsubj | shows | 29 |
| 29 | shows | show | VERB | VBZ | ROOT | shows | 29 |
| 30 | soft | soft | ADJ | JJ | amod | hues | 34 |
| 31 | orange | orange | NOUN | NN | nmod | hues | 34 |
| 32 | and | and | CCONJ | CC | cc | orange | 31 |
| 33 | gray | gray | ADJ | JJ | conj | orange | 31 |
| 34 | hues | hue | NOUN | NNS | dobj | shows | 29 |
| 35 | near | near | ADP | IN | prep | shows | 29 |
| 36 | the | the | DET | DT | det | horizon | 37 |
| 37 | horizon | horizon | NOUN | NN | pobj | near | 35 |
| 38 | . | . | PUNCT | . | punct | shows | 29 |

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
| m8 | object | skyscrapers | skyscraper | chunk6 | 22 | noun_chunk_root | high |
| m9 | attribute | lit-up | lit-up | chunk6 | 21 | state_attribute | medium |
| m10 | object | distance | distance | chunk7 | 25 | noun_chunk_root | high |
| m11 | object | sky | sky | chunk8 | 28 | noun_chunk_root | high |
| m12 | object | hues | hue | chunk9 | 34 | noun_chunk_root | high |
| m13 | attribute | soft | soft | chunk9 | 30 | modifier_attribute | medium |
| m14 | attribute | orange | orange | chunk9 | 31 | color_attribute | high |
| m15 | attribute | gray | gray | chunk9 | 33 | color_attribute | high |
| m16 | object | horizon | horizon | chunk10 | 37 | noun_chunk_root | high |
| m17 | context | dusk | dusk | doc | 9 | context_word | medium |
| m18 | action | viewed | view | doc | 2 | verb_predicate | high |
| m19 | action | stretch | stretch | doc | 16 | verb_predicate | high |
| m20 | action | shows | show | doc | 29 | verb_predicate | high |

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
| A few distant trees and power lines are visible in the background. | 32:44 |

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
| power lines | power lines | power_line | conj | trees | 37:38 |
| the background | background | background | pobj | in | 41:43 |

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
| 35 | trees | tree | NOUN | NNS | nsubj | are | 38 |
| 36 | and | and | CCONJ | CC | cc | trees | 35 |
| 37 | power lines | power_line | NOUN | NN | conj | trees | 35 |
| 38 | are | be | AUX | VBP | ROOT | are | 38 |
| 39 | visible | visible | ADJ | JJ | acomp | are | 38 |
| 40 | in | in | ADP | IN | prep | are | 38 |
| 41 | the | the | DET | DT | det | background | 42 |
| 42 | background | background | NOUN | NN | pobj | in | 40 |
| 43 | . | . | PUNCT | . | punct | are | 38 |

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
| m17 | object | power lines | power_line | chunk9 | 37 | noun_chunk_root | high |
| m18 | object | background | background | chunk10 | 42 | noun_chunk_root | high |
| m19 | context | background | background | doc | 42 | context_word | medium |
| m20 | action | runs | run | doc | 7 | verb_predicate | high |
| m21 | action | stretches | stretch | doc | 22 | verb_predicate | high |

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
| e8 | has_context | scene | m19 | medium | context token background |
| e9 | agent | m20 | m0 | medium | nsubj -> runs |
| e10 | agent | m21 | m7 | medium | nsubj -> stretches |
| e11 | relation | m0 | m2 | high | with |
| e12 | relation | m0 | m4 | medium | along |
| e13 | relation | m4 | m5 | medium | of |
| e14 | relation | m7 | m6 | high | beyond |
| e15 | relation | m7 | m10 | medium | to |
| e16 | relation | m7 | m11 | high | under |
| e17 | relation | m14 | m19 | high | in |

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

## 21

**caption_shape:** `multi-sentence`
**caption_id:** `0e2296e144a650da6a374a53a16be972deaa045439c5c44eb5e0be47913ad414`

> Three people are in close proximity indoors, with a man on the left, a woman in the center, and another woman on the right. The woman in the center has dark hair and is touching her lips with her finger, while the woman on the right smiles broadly. A green-lit sign is visible in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| Three people are in close proximity indoors, with a man on the left, a woman in the center, and another woman on the right. | 0:28 |
| The woman in the center has dark hair and is touching her lips with her finger, while the woman on the right smiles broadly. | 28:54 |
| A green-lit sign is visible in the background. | 54:63 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Three people | people | people | nsubj | are | 0:2 |
| close proximity | proximity | proximity | pobj | in | 4:6 |
| a man | man | man | pobj | with | 9:11 |
| the left | left | left | pobj | on | 12:14 |
| a woman | woman | woman | conj | man | 15:17 |
| the center | center | center | pobj | in | 18:20 |
| another woman | woman | woman | conj | woman | 22:24 |
| the right | right | right | pobj | on | 25:27 |
| The woman | woman | woman | nsubj | has | 28:30 |
| the center | center | center | pobj | in | 31:33 |
| dark hair | hair | hair | dobj | has | 34:36 |
| her lips | lips | lip | dobj | touching | 39:41 |
| her finger | finger | finger | pobj | with | 42:44 |
| the woman | woman | woman | nsubj | smiles | 46:48 |
| the right | right | right | pobj | on | 49:51 |
| A green-lit sign | sign | sign | nsubj | is | 54:57 |
| the background | background | background | pobj | in | 60:62 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Three | three | NUM | CD | nummod | people | 1 |
| 1 | people | people | NOUN | NNS | nsubj | are | 2 |
| 2 | are | be | AUX | VBP | ROOT | are | 2 |
| 3 | in | in | ADP | IN | prep | are | 2 |
| 4 | close | close | ADJ | JJ | amod | proximity | 5 |
| 5 | proximity | proximity | NOUN | NN | pobj | in | 3 |
| 6 | indoors | indoors | ADV | RB | advmod | are | 2 |
| 7 | , | , | PUNCT | , | punct | are | 2 |
| 8 | with | with | ADP | IN | prep | are | 2 |
| 9 | a | a | DET | DT | det | man | 10 |
| 10 | man | man | NOUN | NN | pobj | with | 8 |
| 11 | on | on | ADP | IN | prep | man | 10 |
| 12 | the | the | DET | DT | det | left | 13 |
| 13 | left | left | NOUN | NN | pobj | on | 11 |
| 14 | , | , | PUNCT | , | punct | man | 10 |
| 15 | a | a | DET | DT | det | woman | 16 |
| 16 | woman | woman | NOUN | NN | conj | man | 10 |
| 17 | in | in | ADP | IN | prep | woman | 16 |
| 18 | the | the | DET | DT | det | center | 19 |
| 19 | center | center | NOUN | NN | pobj | in | 17 |
| 20 | , | , | PUNCT | , | punct | woman | 16 |
| 21 | and | and | CCONJ | CC | cc | woman | 16 |
| 22 | another | another | DET | DT | det | woman | 23 |
| 23 | woman | woman | NOUN | NN | conj | woman | 16 |
| 24 | on | on | ADP | IN | prep | woman | 23 |
| 25 | the | the | DET | DT | det | right | 26 |
| 26 | right | right | NOUN | NN | pobj | on | 24 |
| 27 | . | . | PUNCT | . | punct | are | 2 |
| 28 | The | the | DET | DT | det | woman | 29 |
| 29 | woman | woman | NOUN | NN | nsubj | has | 33 |
| 30 | in | in | ADP | IN | prep | woman | 29 |
| 31 | the | the | DET | DT | det | center | 32 |
| 32 | center | center | NOUN | NN | pobj | in | 30 |
| 33 | has | have | VERB | VBZ | ROOT | has | 33 |
| 34 | dark | dark | ADJ | JJ | amod | hair | 35 |
| 35 | hair | hair | NOUN | NN | dobj | has | 33 |
| 36 | and | and | CCONJ | CC | cc | has | 33 |
| 37 | is | be | AUX | VBZ | aux | touching | 38 |
| 38 | touching | touch | VERB | VBG | conj | has | 33 |
| 39 | her | her | PRON | PRP$ | poss | lips | 40 |
| 40 | lips | lip | NOUN | NNS | dobj | touching | 38 |
| 41 | with | with | ADP | IN | prep | touching | 38 |
| 42 | her | her | PRON | PRP$ | poss | finger | 43 |
| 43 | finger | finger | NOUN | NN | pobj | with | 41 |
| 44 | , | , | PUNCT | , | punct | touching | 38 |
| 45 | while | while | SCONJ | IN | mark | smiles | 51 |
| 46 | the | the | DET | DT | det | woman | 47 |
| 47 | woman | woman | NOUN | NN | nsubj | smiles | 51 |
| 48 | on | on | ADP | IN | prep | woman | 47 |
| 49 | the | the | DET | DT | det | right | 50 |
| 50 | right | right | NOUN | NN | pobj | on | 48 |
| 51 | smiles | smile | VERB | VBZ | advcl | touching | 38 |
| 52 | broadly | broadly | ADV | RB | advmod | smiles | 51 |
| 53 | . | . | PUNCT | . | punct | has | 33 |
| 54 | A | a | DET | DT | det | sign | 56 |
| 55 | green-lit | green-lit | ADJ | JJ | amod | sign | 56 |
| 56 | sign | sign | NOUN | NN | nsubj | is | 57 |
| 57 | is | be | AUX | VBZ | ROOT | is | 57 |
| 58 | visible | visible | ADJ | JJ | acomp | is | 57 |
| 59 | in | in | ADP | IN | prep | is | 57 |
| 60 | the | the | DET | DT | det | background | 61 |
| 61 | background | background | NOUN | NN | pobj | in | 59 |
| 62 | . | . | PUNCT | . | punct | is | 57 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Three | three | chunk0 | 0 | quantity | high |
| m2 | object | proximity | proximity | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | close | close | chunk1 | 4 | modifier_attribute | medium |
| m4 | object | man | man | chunk2 | 10 | noun_chunk_root | high |
| m5 | object | left | left | chunk3 | 13 | noun_chunk_root | high |
| m6 | object | woman | woman | chunk4 | 16 | noun_chunk_root | high |
| m7 | context | center | center | chunk5 | 19 | spatial_region | medium |
| m8 | object | woman | woman | chunk6 | 23 | noun_chunk_root | high |
| m9 | object | right | right | chunk7 | 26 | noun_chunk_root | high |
| m10 | object | woman | woman | chunk8 | 29 | noun_chunk_root | high |
| m11 | context | center | center | chunk9 | 32 | spatial_region | medium |
| m12 | object | hair | hair | chunk10 | 35 | noun_chunk_root | high |
| m13 | attribute | dark | dark | chunk10 | 34 | visual_attribute | medium |
| m14 | object | lips | lip | chunk11 | 40 | noun_chunk_root | high |
| m15 | attribute | her | her | chunk11 | 39 | modifier_attribute | medium |
| m16 | object | finger | finger | chunk12 | 43 | noun_chunk_root | high |
| m17 | attribute | her | her | chunk12 | 42 | modifier_attribute | medium |
| m18 | object | woman | woman | chunk13 | 47 | noun_chunk_root | high |
| m19 | object | right | right | chunk14 | 50 | noun_chunk_root | high |
| m20 | object | sign | sign | chunk15 | 56 | noun_chunk_root | high |
| m21 | attribute | green-lit | green-lit | chunk15 | 55 | modifier_attribute | medium |
| m22 | object | background | background | chunk16 | 61 | noun_chunk_root | high |
| m23 | context | indoors | indoors | doc | 6 | context_word | medium |
| m24 | context | background | background | doc | 61 | context_word | medium |
| m25 | action | has | have | doc | 33 | verb_predicate | high |
| m26 | action | touching | touch | doc | 38 | verb_predicate | high |
| m27 | action | smiles | smile | doc | 51 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 nummod -> people |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> proximity |
| e2 | has_attribute | m12 | m13 | medium | chunk10 amod -> hair |
| e3 | has_attribute | m14 | m15 | medium | chunk11 poss -> lips |
| e4 | has_attribute | m16 | m17 | medium | chunk12 poss -> finger |
| e5 | has_attribute | m20 | m21 | medium | chunk15 amod -> sign |
| e6 | has_context | scene | m23 | medium | context token indoors |
| e7 | has_context | scene | m24 | medium | context token background |
| e8 | agent | m25 | m10 | medium | nsubj -> has |
| e9 | patient | m25 | m12 | medium | dobj -> has |
| e10 | patient | m26 | m14 | medium | dobj -> touching |
| e11 | agent | m27 | m18 | medium | nsubj -> smiles |
| e12 | relation | m0 | m2 | high | in |
| e13 | relation | m0 | m4 | high | with |
| e14 | relation | m0 | m6 | high | with |
| e15 | relation | m0 | m8 | high | with |
| e16 | relation | m4 | m5 | high | on |
| e17 | relation | m6 | m7 | high | in |
| e18 | relation | m8 | m9 | high | on |
| e19 | relation | m10 | m11 | high | in |
| e20 | relation | m10 | m16 | high | with |
| e21 | relation | m18 | m19 | high | on |
| e22 | relation | m20 | m24 | high | in |

## 22

**caption_shape:** `multi-sentence`
**caption_id:** `0e7307588e1bd7a8877769b4ba2d54353f365910c3843e59fba4f25c14119014`

> A brown duck swims in calm blue water, creating ripples around its body. Its head and neck are dark brown, with a lighter chest, and it glides smoothly near the surface. The water reflects light and faint tree branches above.

### Sentences
| sentence | token_span |
| --- | --- |
| A brown duck swims in calm blue water, creating ripples around its body. | 0:15 |
| Its head and neck are dark brown, with a lighter chest, and it glides smoothly near the surface. | 15:36 |
| The water reflects light and faint tree branches above. | 36:45 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A brown duck | duck | duck | nsubj | swims | 0:3 |
| calm blue water | water | water | pobj | in | 5:8 |
| ripples | ripples | ripple | dobj | creating | 10:11 |
| its body | body | body | pobj | around | 12:14 |
| Its head | head | head | nsubj | are | 15:17 |
| neck | neck | neck | conj | head | 18:19 |
| a lighter chest | chest | chest | pobj | with | 24:27 |
| it | it | it | nsubj | glides | 29:30 |
| the surface | surface | surface | pobj | near | 33:35 |
| The water | water | water | nsubj | reflects | 36:38 |
| light and faint tree branches | tree branches | tree_branch | dobj | reflects | 39:43 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | duck | 2 |
| 1 | brown | brown | ADJ | JJ | amod | duck | 2 |
| 2 | duck | duck | NOUN | NN | nsubj | swims | 3 |
| 3 | swims | swim | VERB | VBZ | ROOT | swims | 3 |
| 4 | in | in | ADP | IN | prep | swims | 3 |
| 5 | calm | calm | ADJ | JJ | amod | water | 7 |
| 6 | blue | blue | ADJ | JJ | amod | water | 7 |
| 7 | water | water | NOUN | NN | pobj | in | 4 |
| 8 | , | , | PUNCT | , | punct | swims | 3 |
| 9 | creating | create | VERB | VBG | advcl | swims | 3 |
| 10 | ripples | ripple | NOUN | NNS | dobj | creating | 9 |
| 11 | around | around | ADP | IN | prep | creating | 9 |
| 12 | its | its | PRON | PRP$ | poss | body | 13 |
| 13 | body | body | NOUN | NN | pobj | around | 11 |
| 14 | . | . | PUNCT | . | punct | swims | 3 |
| 15 | Its | its | PRON | PRP$ | poss | head | 16 |
| 16 | head | head | NOUN | NN | nsubj | are | 19 |
| 17 | and | and | CCONJ | CC | cc | head | 16 |
| 18 | neck | neck | NOUN | NN | conj | head | 16 |
| 19 | are | be | AUX | VBP | ROOT | are | 19 |
| 20 | dark | dark | ADJ | JJ | amod | brown | 21 |
| 21 | brown | brown | ADJ | JJ | acomp | are | 19 |
| 22 | , | , | PUNCT | , | punct | brown | 21 |
| 23 | with | with | ADP | IN | prep | brown | 21 |
| 24 | a | a | DET | DT | det | chest | 26 |
| 25 | lighter | light | ADJ | JJR | amod | chest | 26 |
| 26 | chest | chest | NOUN | NN | pobj | with | 23 |
| 27 | , | , | PUNCT | , | punct | are | 19 |
| 28 | and | and | CCONJ | CC | cc | are | 19 |
| 29 | it | it | PRON | PRP | nsubj | glides | 30 |
| 30 | glides | glide | VERB | VBZ | conj | are | 19 |
| 31 | smoothly | smoothly | ADV | RB | advmod | glides | 30 |
| 32 | near | near | ADP | IN | prep | glides | 30 |
| 33 | the | the | DET | DT | det | surface | 34 |
| 34 | surface | surface | NOUN | NN | pobj | near | 32 |
| 35 | . | . | PUNCT | . | punct | glides | 30 |
| 36 | The | the | DET | DT | det | water | 37 |
| 37 | water | water | NOUN | NN | nsubj | reflects | 38 |
| 38 | reflects | reflect | VERB | VBZ | ROOT | reflects | 38 |
| 39 | light | light | ADJ | JJ | amod | tree branches | 42 |
| 40 | and | and | CCONJ | CC | cc | light | 39 |
| 41 | faint | faint | ADJ | JJ | conj | light | 39 |
| 42 | tree branches | tree_branch | NOUN | NN | dobj | reflects | 38 |
| 43 | above | above | ADP | IN | advmod | tree branches | 42 |
| 44 | . | . | PUNCT | . | punct | reflects | 38 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | duck | duck | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | brown | brown | chunk0 | 1 | color_attribute | high |
| m2 | object | water | water | chunk1 | 7 | noun_chunk_root | high |
| m3 | attribute | calm | calm | chunk1 | 5 | modifier_attribute | medium |
| m4 | attribute | blue | blue | chunk1 | 6 | color_attribute | high |
| m5 | object | ripples | ripple | chunk2 | 10 | noun_chunk_root | high |
| m6 | object | body | body | chunk3 | 13 | noun_chunk_root | high |
| m7 | attribute | its | its | chunk3 | 12 | modifier_attribute | medium |
| m8 | object | head | head | chunk4 | 16 | noun_chunk_root | high |
| m9 | attribute | Its | its | chunk4 | 15 | modifier_attribute | medium |
| m10 | object | neck | neck | chunk5 | 18 | noun_chunk_root | high |
| m11 | object | chest | chest | chunk6 | 26 | noun_chunk_root | high |
| m12 | attribute | lighter | light | chunk6 | 25 | visual_attribute | medium |
| m13 | object | it | it | chunk7 | 29 | noun_chunk_root | high |
| m14 | object | surface | surface | chunk8 | 34 | noun_chunk_root | high |
| m15 | object | water | water | chunk9 | 37 | noun_chunk_root | high |
| m16 | object | tree branches | tree_branch | chunk10 | 42 | noun_chunk_root | high |
| m17 | attribute | light | light | chunk10 | 39 | visual_attribute | medium |
| m18 | attribute | faint | faint | chunk10 | 41 | modifier_attribute | medium |
| m19 | action | swims | swim | doc | 3 | verb_predicate | high |
| m20 | action | creating | create | doc | 9 | verb_predicate | high |
| m21 | action | glides | glide | doc | 30 | verb_predicate | high |
| m22 | action | reflects | reflect | doc | 38 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> duck |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> water |
| e2 | has_attribute | m2 | m4 | high | chunk1 amod -> water |
| e3 | has_attribute | m6 | m7 | medium | chunk3 poss -> body |
| e4 | has_attribute | m8 | m9 | medium | chunk4 poss -> head |
| e5 | has_attribute | m11 | m12 | medium | chunk6 amod -> chest |
| e6 | has_attribute | m16 | m17 | medium | chunk10 amod -> tree branches |
| e7 | has_attribute | m16 | m18 | medium | chunk10 conj -> tree branches |
| e8 | agent | m19 | m0 | medium | nsubj -> swims |
| e9 | patient | m20 | m5 | medium | dobj -> creating |
| e10 | agent | m21 | m13 | medium | nsubj -> glides |
| e11 | agent | m22 | m15 | medium | nsubj -> reflects |
| e12 | patient | m22 | m16 | medium | dobj -> reflects |
| e13 | relation | m0 | m2 | high | in |
| e14 | relation | m0 | m6 | high | around |
| e15 | relation | m13 | m14 | high | near |

## 23

**caption_shape:** `tag-list-like`
**caption_id:** `0e976bfb7bcfe7c0ea36a64e605bba151e5a5a2b6e739540e24c3b07d68ce014`

> green scoreboard, hockey rink, banners, rough riders, ice surface

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | green scoreboard | green scoreboard | 0:16 |
| t1 | hockey rink | hockey rink | 18:29 |
| t2 | banners | banners | 31:38 |
| t3 | rough riders | rough riders | 40:52 |
| t4 | ice surface | ice surface | 54:65 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | green scoreboard | scoreboard | scoreboard | ROOT | scoreboard | 0:2 | 0:16 |
| t1 | hockey rink | rink | rink | ROOT | rink | 0:2 | 18:29 |
| t2 | banners | banners | banner | ROOT | banners | 0:1 | 31:38 |
| t3 | rough riders | riders | rider | ROOT | riders | 0:2 | 40:52 |
| t4 | ice surface | surface | surface | ROOT | surface | 0:2 | 54:65 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | green | green | PROPN | ADJ | NNP | JJ | compound | scoreboard | 1 | 0:5 |
| t0 | 1 | scoreboard | scoreboard | NOUN | NOUN | NN | NN | ROOT | scoreboard | 1 | 6:16 |
| t1 | 0 | hockey | hockey | NOUN | NOUN | NN | NN | compound | rink | 1 | 18:24 |
| t1 | 1 | rink | rink | NOUN | NOUN | NN | NN | ROOT | rink | 1 | 25:29 |
| t2 | 0 | banners | banner | NOUN | NOUN | NNS | NNS | ROOT | banners | 0 | 31:38 |
| t3 | 0 | rough | rough | ADJ | ADJ | JJ | JJ | compound | riders | 1 | 40:45 |
| t3 | 1 | riders | rider | NOUN | NOUN | NNS | NNS | ROOT | riders | 1 | 46:52 |
| t4 | 0 | ice | ice | NOUN | NOUN | NN | NN | compound | surface | 1 | 54:57 |
| t4 | 1 | surface | surface | NOUN | NOUN | NN | NN | ROOT | surface | 1 | 58:65 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | scoreboard | scoreboard | t0 | 1 | segment_head | high |
| m1 | attribute | green | green | t0 | 0 | attribute | high |
| m2 | object | rink | rink | t1 | 1 | segment_head | high |
| m3 | attribute | hockey | hockey | t1 | 0 | attribute | high |
| m4 | object | banners | banner | t2 | 0 | segment_head | high |
| m5 | object | riders | rider | t3 | 1 | segment_head | high |
| m6 | attribute | rough | rough | t3 | 0 | attribute | high |
| m7 | object | surface | surface | t4 | 1 | segment_head | high |
| m8 | attribute | ice | ice | t4 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> scoreboard |
| e1 | has_attribute | m2 | m3 | high | t1 internal compound -> rink |
| e2 | has_attribute | m5 | m6 | high | t3 internal compound -> riders |
| e3 | has_attribute | m7 | m8 | high | t4 internal compound -> surface |

## 24

**caption_shape:** `tag-list-like`
**caption_id:** `102c1e28a6c0c106f8ef32999591aa85fae258f045731fe97d3cde7bcf7cd014`

> text, page, russian, book, printed

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | text | text | 0:4 |
| t1 | page | page | 6:10 |
| t2 | russian | russian | 12:19 |
| t3 | book | book | 21:25 |
| t4 | printed | printed | 27:34 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | text | text | text | ROOT | text | 0:1 | 0:4 |
| t1 | page | page | page | ROOT | page | 0:1 | 6:10 |
| t3 | book | book | book | ROOT | book | 0:1 | 21:25 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | text | text | NOUN | NOUN | NN | NN | ROOT | text | 0 | 0:4 |
| t1 | 0 | page | page | NOUN | NOUN | NN | NN | ROOT | page | 0 | 6:10 |
| t2 | 0 | russian | russian | ADJ | ADJ | JJ | JJ | ROOT | russian | 0 | 12:19 |
| t3 | 0 | book | book | NOUN | NOUN | NN | NN | ROOT | book | 0 | 21:25 |
| t4 | 0 | printed | print | VERB | ADJ | VBN | VBN | ROOT | printed | 0 | 27:34 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | text | text | t0 | 0 | segment_head | high |
| m1 | object | page | page | t1 | 0 | segment_head | high |
| m2 | attribute | russian | russian | t2 | 0 | floating_attribute | medium |
| m3 | object | book | book | t3 | 0 | segment_head | high |
| m4 | attribute | printed | print | t4 | 0 | floating_attribute | medium |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | candidate_has_attribute | m1 | m2 | low | t2 adjacent floating attribute |
| e1 | candidate_has_attribute | m3 | m4 | low | t4 adjacent floating attribute |

## 25

**caption_shape:** `multi-sentence`
**caption_id:** `10360632429015a31bb702f2f1582216021cbd4735544d73052a16099d4d6014`

> A brown dog leaps over a blue, white, and red basket on grass. A man in a black outfit with red and blue trim stands nearby, watching the dog. In the background, spectators stand behind a fence near a "ROYAL CANIN" banner.

**parsed_caption:**

> A brown dog leaps over a blue, white, and red basket on grass. A man in a black outfit with red and blue trim stands nearby, watching the dog. In the background, spectators stand behind a fence near a "ROYAL CANIN" banner.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 10360632429015a31bb702f2f1582216021cbd4735544d73052a16099d4d6014:q0 | ROYAL CANIN | royal canin | raw_quote_span |  | 201:214 | 201:214 |

### Sentences
| sentence | token_span |
| --- | --- |
| A brown dog leaps over a blue, white, and red basket on grass. | 0:16 |
| A man in a black outfit with red and blue trim stands nearby, watching the dog. | 16:34 |
| In the background, spectators stand behind a fence near a "ROYAL CANIN" banner. | 34:48 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A brown dog | dog | dog | nsubj | leaps | 0:3 |
| a blue, white, and red basket | basket | basket | pobj | over | 5:13 |
| grass | grass | grass | pobj | on | 14:15 |
| A man | man | man | nsubj | stands | 16:18 |
| a black outfit | outfit | outfit | pobj | in | 19:22 |
| red and blue trim | trim | trim | pobj | with | 23:27 |
| the dog | dog | dog | dobj | watching | 31:33 |
| the background | background | background | pobj | In | 35:37 |
| spectators | spectators | spectator | nsubj | stand | 38:39 |
| a fence | fence | fence | pobj | behind | 41:43 |
| a "ROYAL CANIN" banner | banner | banner | pobj | near | 44:47 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | dog | 2 |
| 1 | brown | brown | ADJ | JJ | amod | dog | 2 |
| 2 | dog | dog | NOUN | NN | nsubj | leaps | 3 |
| 3 | leaps | leap | VERB | VBZ | ROOT | leaps | 3 |
| 4 | over | over | ADP | IN | prep | leaps | 3 |
| 5 | a | a | DET | DT | det | basket | 12 |
| 6 | blue | blue | ADJ | JJ | amod | basket | 12 |
| 7 | , | , | PUNCT | , | punct | blue | 6 |
| 8 | white | white | ADJ | JJ | conj | blue | 6 |
| 9 | , | , | PUNCT | , | punct | white | 8 |
| 10 | and | and | CCONJ | CC | cc | white | 8 |
| 11 | red | red | ADJ | JJ | conj | white | 8 |
| 12 | basket | basket | NOUN | NN | pobj | over | 4 |
| 13 | on | on | ADP | IN | prep | basket | 12 |
| 14 | grass | grass | NOUN | NN | pobj | on | 13 |
| 15 | . | . | PUNCT | . | punct | leaps | 3 |
| 16 | A | a | DET | DT | det | man | 17 |
| 17 | man | man | NOUN | NN | nsubj | stands | 27 |
| 18 | in | in | ADP | IN | prep | man | 17 |
| 19 | a | a | DET | DT | det | outfit | 21 |
| 20 | black | black | ADJ | JJ | amod | outfit | 21 |
| 21 | outfit | outfit | NOUN | NN | pobj | in | 18 |
| 22 | with | with | ADP | IN | prep | outfit | 21 |
| 23 | red | red | ADJ | JJ | amod | trim | 26 |
| 24 | and | and | CCONJ | CC | cc | red | 23 |
| 25 | blue | blue | ADJ | JJ | conj | red | 23 |
| 26 | trim | trim | NOUN | NN | pobj | with | 22 |
| 27 | stands | stand | VERB | VBZ | ROOT | stands | 27 |
| 28 | nearby | nearby | ADV | RB | advmod | stands | 27 |
| 29 | , | , | PUNCT | , | punct | stands | 27 |
| 30 | watching | watch | VERB | VBG | advcl | stands | 27 |
| 31 | the | the | DET | DT | det | dog | 32 |
| 32 | dog | dog | NOUN | NN | dobj | watching | 30 |
| 33 | . | . | PUNCT | . | punct | stands | 27 |
| 34 | In | in | ADP | IN | prep | stand | 39 |
| 35 | the | the | DET | DT | det | background | 36 |
| 36 | background | background | NOUN | NN | pobj | In | 34 |
| 37 | , | , | PUNCT | , | punct | stand | 39 |
| 38 | spectators | spectator | NOUN | NNS | nsubj | stand | 39 |
| 39 | stand | stand | VERB | VBP | ROOT | stand | 39 |
| 40 | behind | behind | ADP | IN | prep | stand | 39 |
| 41 | a | a | DET | DT | det | fence | 42 |
| 42 | fence | fence | NOUN | NN | pobj | behind | 40 |
| 43 | near | near | ADP | IN | prep | stand | 39 |
| 44 | a | a | DET | DT | det | banner | 46 |
| 45 | "ROYAL CANIN" | royal_canin | PROPN | NNP | nmod | banner | 46 |
| 46 | banner | banner | NOUN | NN | pobj | near | 43 |
| 47 | . | . | PUNCT | . | punct | stand | 39 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | dog | dog | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | brown | brown | chunk0 | 1 | color_attribute | high |
| m2 | object | basket | basket | chunk1 | 12 | noun_chunk_root | high |
| m3 | attribute | blue | blue | chunk1 | 6 | color_attribute | high |
| m4 | attribute | white | white | chunk1 | 8 | color_attribute | high |
| m5 | attribute | red | red | chunk1 | 11 | color_attribute | high |
| m6 | object | grass | grass | chunk2 | 14 | noun_chunk_root | high |
| m7 | object | man | man | chunk3 | 17 | noun_chunk_root | high |
| m8 | object | outfit | outfit | chunk4 | 21 | noun_chunk_root | high |
| m9 | attribute | black | black | chunk4 | 20 | color_attribute | high |
| m10 | object | trim | trim | chunk5 | 26 | noun_chunk_root | high |
| m11 | attribute | red | red | chunk5 | 23 | color_attribute | high |
| m12 | attribute | blue | blue | chunk5 | 25 | color_attribute | high |
| m13 | object | dog | dog | chunk6 | 32 | noun_chunk_root | high |
| m14 | object | background | background | chunk7 | 36 | noun_chunk_root | high |
| m15 | object | spectators | spectator | chunk8 | 38 | noun_chunk_root | high |
| m16 | object | fence | fence | chunk9 | 42 | noun_chunk_root | high |
| m17 | object | banner | banner | chunk10 | 46 | noun_chunk_root | high |
| m18 | context | background | background | doc | 36 | context_word | medium |
| m19 | action | leaps | leap | doc | 3 | verb_predicate | high |
| m20 | action | stands | stand | doc | 27 | verb_predicate | high |
| m21 | action | watching | watch | doc | 30 | verb_predicate | high |
| m22 | action | stand | stand | doc | 39 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> dog |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> basket |
| e2 | has_attribute | m2 | m4 | high | chunk1 conj -> basket |
| e3 | has_attribute | m2 | m5 | high | chunk1 conj -> basket |
| e4 | has_attribute | m8 | m9 | high | chunk4 amod -> outfit |
| e5 | has_attribute | m10 | m11 | high | chunk5 amod -> trim |
| e6 | has_attribute | m10 | m12 | high | chunk5 conj -> trim |
| e7 | has_context | scene | m18 | medium | context token background |
| e8 | agent | m19 | m0 | medium | nsubj -> leaps |
| e9 | agent | m20 | m7 | medium | nsubj -> stands |
| e10 | patient | m21 | m13 | medium | dobj -> watching |
| e11 | agent | m22 | m15 | medium | nsubj -> stand |
| e12 | relation | m0 | m2 | high | over |
| e13 | relation | m2 | m6 | high | on |
| e14 | relation | m7 | m8 | high | in |
| e15 | relation | m8 | m10 | high | with |
| e16 | relation | m15 | m18 | high | in |
| e17 | relation | m15 | m16 | high | behind |
| e18 | relation | m15 | m17 | high | near |

## 26

**caption_shape:** `tag-list-like`
**caption_id:** `10b5d5feebae9613d0e6b4b6b39da6c83f0a783ab363bf8549cb72e231fdf814`

> axe, mask, costume, grass, fence, stump

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | axe | axe | 0:3 |
| t1 | mask | mask | 5:9 |
| t2 | costume | costume | 11:18 |
| t3 | grass | grass | 20:25 |
| t4 | fence | fence | 27:32 |
| t5 | stump | stump | 34:39 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | axe | axe | axe | ROOT | axe | 0:1 | 0:3 |
| t1 | mask | mask | mask | ROOT | mask | 0:1 | 5:9 |
| t2 | costume | costume | costume | ROOT | costume | 0:1 | 11:18 |
| t3 | grass | grass | grass | ROOT | grass | 0:1 | 20:25 |
| t4 | fence | fence | fence | ROOT | fence | 0:1 | 27:32 |
| t5 | stump | stump | stump | ROOT | stump | 0:1 | 34:39 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | axe | axe | PROPN | NOUN | NNP | NN | ROOT | axe | 0 | 0:3 |
| t1 | 0 | mask | mask | NOUN | NOUN | NN | NN | ROOT | mask | 0 | 5:9 |
| t2 | 0 | costume | costume | NOUN | NOUN | NN | NN | ROOT | costume | 0 | 11:18 |
| t3 | 0 | grass | grass | NOUN | NOUN | NN | NN | ROOT | grass | 0 | 20:25 |
| t4 | 0 | fence | fence | NOUN | NOUN | NN | NN | ROOT | fence | 0 | 27:32 |
| t5 | 0 | stump | stump | NOUN | NOUN | NN | NN | ROOT | stump | 0 | 34:39 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | axe | axe | t0 | 0 | segment_head | high |
| m1 | object | mask | mask | t1 | 0 | segment_head | high |
| m2 | object | costume | costume | t2 | 0 | segment_head | high |
| m3 | object | grass | grass | t3 | 0 | segment_head | high |
| m4 | object | fence | fence | t4 | 0 | segment_head | high |
| m5 | object | stump | stump | t5 | 0 | segment_head | high |

### Edges
_none_

## 27

**caption_shape:** `sentence-like`
**caption_id:** `10c4cd7231ff6d3987ddff17376eb7350864aaa2611b70c16fdee2a87f458014`

> A man in a white shirt works on an electrical panel with wires and switches visible.

### Sentences
| sentence | token_span |
| --- | --- |
| A man in a white shirt works on an electrical panel with wires and switches visible. | 0:17 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A man | man | man | nsubj | works | 0:2 |
| a white shirt | shirt | shirt | pobj | in | 3:6 |
| an electrical panel | panel | panel | pobj | on | 8:11 |
| wires | wires | wire | nsubj | visible | 12:13 |
| switches | switches | switch | conj | wires | 14:15 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | man | 1 |
| 1 | man | man | NOUN | NN | nsubj | works | 6 |
| 2 | in | in | ADP | IN | prep | man | 1 |
| 3 | a | a | DET | DT | det | shirt | 5 |
| 4 | white | white | ADJ | JJ | amod | shirt | 5 |
| 5 | shirt | shirt | NOUN | NN | pobj | in | 2 |
| 6 | works | work | VERB | VBZ | ROOT | works | 6 |
| 7 | on | on | ADP | IN | prep | works | 6 |
| 8 | an | an | DET | DT | det | panel | 10 |
| 9 | electrical | electrical | ADJ | JJ | amod | panel | 10 |
| 10 | panel | panel | NOUN | NN | pobj | on | 7 |
| 11 | with | with | SCONJ | IN | mark | visible | 15 |
| 12 | wires | wire | NOUN | NNS | nsubj | visible | 15 |
| 13 | and | and | CCONJ | CC | cc | wires | 12 |
| 14 | switches | switch | NOUN | NNS | conj | wires | 12 |
| 15 | visible | visible | ADJ | JJ | advcl | works | 6 |
| 16 | . | . | PUNCT | . | punct | works | 6 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | shirt | shirt | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | white | white | chunk1 | 4 | color_attribute | high |
| m3 | object | panel | panel | chunk2 | 10 | noun_chunk_root | high |
| m4 | attribute | electrical | electrical | chunk2 | 9 | modifier_attribute | medium |
| m5 | object | wires | wire | chunk3 | 12 | noun_chunk_root | high |
| m6 | object | switches | switch | chunk4 | 14 | noun_chunk_root | high |
| m7 | action | works | work | doc | 6 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> shirt |
| e1 | has_attribute | m3 | m4 | medium | chunk2 amod -> panel |
| e2 | agent | m7 | m0 | medium | nsubj -> works |
| e3 | relation | m0 | m1 | high | in |
| e4 | relation | m0 | m3 | high | on |

## 28

**caption_shape:** `sentence-like`
**caption_id:** `11adbf857279ff850b9bd6768acdaeb86ddecd51daf3f5980282a815b9e0c414`

> A person in a blue and pink costume stands on a stage with glowing lights behind them.

### Sentences
| sentence | token_span |
| --- | --- |
| A person in a blue and pink costume stands on a stage with glowing lights behind them. | 0:18 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A person | person | person | nsubj | stands | 0:2 |
| a blue and pink costume | costume | costume | pobj | in | 3:8 |
| a stage | stage | stage | pobj | on | 10:12 |
| glowing lights | lights | light | pcomp | with | 13:15 |
| them | them | they | pobj | behind | 16:17 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | person | 1 |
| 1 | person | person | NOUN | NN | nsubj | stands | 8 |
| 2 | in | in | ADP | IN | prep | person | 1 |
| 3 | a | a | DET | DT | det | costume | 7 |
| 4 | blue | blue | ADJ | JJ | amod | costume | 7 |
| 5 | and | and | CCONJ | CC | cc | blue | 4 |
| 6 | pink | pink | ADJ | JJ | conj | blue | 4 |
| 7 | costume | costume | NOUN | NN | pobj | in | 2 |
| 8 | stands | stand | VERB | VBZ | ROOT | stands | 8 |
| 9 | on | on | ADP | IN | prep | stands | 8 |
| 10 | a | a | DET | DT | det | stage | 11 |
| 11 | stage | stage | NOUN | NN | pobj | on | 9 |
| 12 | with | with | ADP | IN | prep | stands | 8 |
| 13 | glowing | glow | VERB | VBG | amod | lights | 14 |
| 14 | lights | light | NOUN | NNS | pcomp | with | 12 |
| 15 | behind | behind | ADP | IN | prep | lights | 14 |
| 16 | them | they | PRON | PRP | pobj | behind | 15 |
| 17 | . | . | PUNCT | . | punct | stands | 8 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | costume | costume | chunk1 | 7 | noun_chunk_root | high |
| m2 | attribute | blue | blue | chunk1 | 4 | color_attribute | high |
| m3 | attribute | pink | pink | chunk1 | 6 | color_attribute | high |
| m4 | object | stage | stage | chunk2 | 11 | noun_chunk_root | high |
| m5 | object | lights | light | chunk3 | 14 | noun_chunk_root | high |
| m6 | attribute | glowing | glow | chunk3 | 13 | state_attribute | medium |
| m7 | object | them | they | chunk4 | 16 | noun_chunk_root | high |
| m8 | action | stands | stand | doc | 8 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> costume |
| e1 | has_attribute | m1 | m3 | high | chunk1 conj -> costume |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> lights |
| e3 | agent | m8 | m0 | medium | nsubj -> stands |
| e4 | relation | m0 | m1 | high | in |
| e5 | relation | m0 | m4 | high | on |
| e6 | relation | m0 | m5 | high | with |
| e7 | relation | m5 | m7 | high | behind |

## 29

**caption_shape:** `sentence-like`
**caption_id:** `120906119bf352f1e5f89c8f05a94ab5c8931e2066ff546366a6fbbd3540b414`

> A yellow helicopter flies over a green hillside near a blue lake, with snow-capped mountains in the distance.

### Sentences
| sentence | token_span |
| --- | --- |
| A yellow helicopter flies over a green hillside near a blue lake, with snow-capped mountains in the distance. | 0:20 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A yellow helicopter | helicopter | helicopter | nsubj | flies | 0:3 |
| a green hillside | hillside | hillside | pobj | over | 5:8 |
| a blue lake | lake | lake | pobj | near | 9:12 |
| the distance | distance | distance | pobj | in | 17:19 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | helicopter | 2 |
| 1 | yellow | yellow | ADJ | JJ | amod | helicopter | 2 |
| 2 | helicopter | helicopter | NOUN | NN | nsubj | flies | 3 |
| 3 | flies | fly | VERB | VBZ | ROOT | flies | 3 |
| 4 | over | over | ADP | IN | prep | flies | 3 |
| 5 | a | a | DET | DT | det | hillside | 7 |
| 6 | green | green | ADJ | JJ | amod | hillside | 7 |
| 7 | hillside | hillside | NOUN | NN | pobj | over | 4 |
| 8 | near | near | ADP | IN | prep | flies | 3 |
| 9 | a | a | DET | DT | det | lake | 11 |
| 10 | blue | blue | ADJ | JJ | amod | lake | 11 |
| 11 | lake | lake | NOUN | NN | pobj | near | 8 |
| 12 | , | , | PUNCT | , | punct | flies | 3 |
| 13 | with | with | SCONJ | IN | mark | mountains | 15 |
| 14 | snow-capped | snow-cappe | VERB | VBN | amod | mountains | 15 |
| 15 | mountains | mountain | NOUN | NNS | advcl | flies | 3 |
| 16 | in | in | ADP | IN | prep | mountains | 15 |
| 17 | the | the | DET | DT | det | distance | 18 |
| 18 | distance | distance | NOUN | NN | pobj | in | 16 |
| 19 | . | . | PUNCT | . | punct | flies | 3 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | helicopter | helicopter | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | yellow | yellow | chunk0 | 1 | color_attribute | high |
| m2 | object | hillside | hillside | chunk1 | 7 | noun_chunk_root | high |
| m3 | attribute | green | green | chunk1 | 6 | color_attribute | high |
| m4 | object | lake | lake | chunk2 | 11 | noun_chunk_root | high |
| m5 | attribute | blue | blue | chunk2 | 10 | color_attribute | high |
| m6 | object | distance | distance | chunk3 | 18 | noun_chunk_root | high |
| m7 | action | flies | fly | doc | 3 | verb_predicate | high |
| m8 | object | mountains | mountain | with_absolute13 | 15 | with_absolute_recovered_object | medium |
| m9 | attribute | snow-capped | snow-cappe | with_absolute13 | 14 | state_attribute | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> helicopter |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> hillside |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> lake |
| e3 | agent | m7 | m0 | medium | nsubj -> flies |
| e4 | scene_contains | scene | m8 | medium | with_absolute13 recovered mountains |
| e5 | has_attribute | m8 | m9 | medium | with_absolute13 amod -> mountains |
| e6 | relation | m0 | m2 | high | over |
| e7 | relation | m0 | m4 | high | near |
| e8 | relation | m8 | m6 | high | in |

## 30

**caption_shape:** `sentence-like`
**caption_id:** `128f7b170ef59050b227c1707de8baf01bdbd6538ddd1a66b840bd1586d83414`

> A man and woman stand on a sandy beach, sharing a drink together.

### Sentences
| sentence | token_span |
| --- | --- |
| A man and woman stand on a sandy beach, sharing a drink together. | 0:15 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A man | man | man | nsubj | stand | 0:2 |
| woman | woman | woman | conj | man | 3:4 |
| a sandy beach | beach | beach | pobj | on | 6:9 |
| a drink | drink | drink | dobj | sharing | 11:13 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | man | 1 |
| 1 | man | man | NOUN | NN | nsubj | stand | 4 |
| 2 | and | and | CCONJ | CC | cc | man | 1 |
| 3 | woman | woman | NOUN | NN | conj | man | 1 |
| 4 | stand | stand | VERB | VBP | ROOT | stand | 4 |
| 5 | on | on | ADP | IN | prep | stand | 4 |
| 6 | a | a | DET | DT | det | beach | 8 |
| 7 | sandy | sandy | ADJ | JJ | amod | beach | 8 |
| 8 | beach | beach | NOUN | NN | pobj | on | 5 |
| 9 | , | , | PUNCT | , | punct | stand | 4 |
| 10 | sharing | share | VERB | VBG | advcl | stand | 4 |
| 11 | a | a | DET | DT | det | drink | 12 |
| 12 | drink | drink | NOUN | NN | dobj | sharing | 10 |
| 13 | together | together | ADV | RB | advmod | sharing | 10 |
| 14 | . | . | PUNCT | . | punct | stand | 4 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | woman | woman | chunk1 | 3 | noun_chunk_root | high |
| m2 | object | beach | beach | chunk2 | 8 | noun_chunk_root | high |
| m3 | attribute | sandy | sandy | chunk2 | 7 | modifier_attribute | medium |
| m4 | object | drink | drink | chunk3 | 12 | noun_chunk_root | high |
| m5 | action | stand | stand | doc | 4 | verb_predicate | high |
| m6 | action | sharing | share | doc | 10 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | medium | chunk2 amod -> beach |
| e1 | agent | m5 | m0 | medium | nsubj -> stand |
| e2 | agent | m5 | m1 | medium | nsubj -> stand |
| e3 | patient | m6 | m4 | medium | dobj -> sharing |
| e4 | relation | m0 | m2 | high | on |

## 31

**caption_shape:** `sentence-like`
**caption_id:** `131382c8917ce69624883320df35ad846216456fba6b33e40b541b016aab9014`

> Several giraffes stand in a dry, dusty savanna with scattered trees.

### Sentences
| sentence | token_span |
| --- | --- |
| Several giraffes stand in a dry, dusty savanna with scattered trees. | 0:13 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Several giraffes | giraffes | giraffe | nsubj | stand | 0:2 |
| a dry, dusty savanna | savanna | savanna | pobj | in | 4:9 |
| scattered trees | trees | tree | pobj | with | 10:12 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Several | several | ADJ | JJ | amod | giraffes | 1 |
| 1 | giraffes | giraffe | NOUN | NNS | nsubj | stand | 2 |
| 2 | stand | stand | VERB | VBP | ROOT | stand | 2 |
| 3 | in | in | ADP | IN | prep | stand | 2 |
| 4 | a | a | DET | DT | det | savanna | 8 |
| 5 | dry | dry | ADJ | JJ | amod | savanna | 8 |
| 6 | , | , | PUNCT | , | punct | savanna | 8 |
| 7 | dusty | dusty | ADJ | JJ | amod | savanna | 8 |
| 8 | savanna | savanna | NOUN | NN | pobj | in | 3 |
| 9 | with | with | ADP | IN | prep | savanna | 8 |
| 10 | scattered | scatter | VERB | VBN | amod | trees | 11 |
| 11 | trees | tree | NOUN | NNS | pobj | with | 9 |
| 12 | . | . | PUNCT | . | punct | stand | 2 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | giraffes | giraffe | chunk0 | 1 | noun_chunk_root | high |
| m1 | attribute | Several | several | chunk0 | 0 | modifier_attribute | medium |
| m2 | object | savanna | savanna | chunk1 | 8 | noun_chunk_root | high |
| m3 | attribute | dry | dry | chunk1 | 5 | modifier_attribute | medium |
| m4 | attribute | dusty | dusty | chunk1 | 7 | modifier_attribute | medium |
| m5 | object | trees | tree | chunk2 | 11 | noun_chunk_root | high |
| m6 | attribute | scattered | scatter | chunk2 | 10 | state_attribute | medium |
| m7 | action | stand | stand | doc | 2 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> giraffes |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> savanna |
| e2 | has_attribute | m2 | m4 | medium | chunk1 amod -> savanna |
| e3 | has_attribute | m5 | m6 | medium | chunk2 amod -> trees |
| e4 | agent | m7 | m0 | medium | nsubj -> stand |
| e5 | relation | m0 | m2 | high | in |
| e6 | relation | m2 | m5 | high | with |

## 32

**caption_shape:** `multi-sentence`
**caption_id:** `13f6ef667e3a8e279fbed679e2ff0eabef743354d2696c3b4164764c8b362414`

> A close-up of a human eye with green irises and dark pupils. The eye is framed by blurred eyelashes and skin, with warm, glowing light surrounding it. Text at the bottom reads "BORDERLINE BIENNALE 2011 | Week-end 02 | Hacking, T.A.Z. & Utopies Pirates."

**parsed_caption:**

> A close-up of a human eye with green irises and dark pupils. The eye is framed by blurred eyelashes and skin, with warm, glowing light surrounding it. Text at the bottom reads "BORDERLINE BIENNALE 2011 | Week-end 02 | Hacking, T.A.Z. & Utopies Pirates."

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 13f6ef667e3a8e279fbed679e2ff0eabef743354d2696c3b4164764c8b362414:q0 | BORDERLINE BIENNALE 2011 \| Week-end 02 \| Hacking, T.A.Z. & Utopies Pirates. | borderline biennale 2011 \| week-end 02 \| hacking, t.a.z. & utopies pirates. | raw_quote_span |  | 176:253 | 176:253 |

### Sentences
| sentence | token_span |
| --- | --- |
| A close-up of a human eye with green irises and dark pupils. | 0:12 |
| The eye is framed by blurred eyelashes and skin, with warm, glowing light surrounding it. | 12:30 |
| Text at the bottom reads "BORDERLINE BIENNALE 2011 \| Week-end 02 \| Hacking, T.A.Z. & Utopies Pirates." | 30:36 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A close-up | close-up | close-up | ROOT | close-up | 0:2 |
| a human eye | human eye | human_eye | pobj | of | 3:5 |
| green irises | irises | iris | pobj | with | 6:8 |
| dark pupils | pupils | pupil | conj | irises | 9:11 |
| The eye | eye | eye | nsubjpass | framed | 12:14 |
| blurred eyelashes | eyelashes | eyelash | pobj | by | 17:19 |
| skin | skin | skin | conj | eyelashes | 20:21 |
| warm, glowing light | light | light | nsubj | surrounding | 23:27 |
| it | it | it | dobj | surrounding | 28:29 |
| Text | Text | text | nsubj | reads | 30:31 |
| the bottom | bottom | bottom | pobj | at | 32:34 |
| "BORDERLINE BIENNALE 2011 \| Week-end 02 \| Hacking, T.A.Z. & Utopies Pirates." | "BORDERLINE BIENNALE 2011 \| Week-end 02 \| Hacking, T.A.Z. & Utopies Pirates." | borderline_biennale_2011_\|_week-end_02_\|_hacking,_t.a.z._&_utopies_pirates. | dobj | reads | 35:36 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | close-up | 1 |
| 1 | close-up | close-up | NOUN | NN | ROOT | close-up | 1 |
| 2 | of | of | ADP | IN | prep | close-up | 1 |
| 3 | a | a | DET | DT | det | human eye | 4 |
| 4 | human eye | human_eye | NOUN | NN | pobj | of | 2 |
| 5 | with | with | ADP | IN | prep | human eye | 4 |
| 6 | green | green | ADJ | JJ | amod | irises | 7 |
| 7 | irises | iris | NOUN | NNS | pobj | with | 5 |
| 8 | and | and | CCONJ | CC | cc | irises | 7 |
| 9 | dark | dark | ADJ | JJ | amod | pupils | 10 |
| 10 | pupils | pupil | NOUN | NNS | conj | irises | 7 |
| 11 | . | . | PUNCT | . | punct | close-up | 1 |
| 12 | The | the | DET | DT | det | eye | 13 |
| 13 | eye | eye | NOUN | NN | nsubjpass | framed | 15 |
| 14 | is | be | AUX | VBZ | auxpass | framed | 15 |
| 15 | framed | frame | VERB | VBN | ROOT | framed | 15 |
| 16 | by | by | ADP | IN | agent | framed | 15 |
| 17 | blurred | blurred | ADJ | JJ | amod | eyelashes | 18 |
| 18 | eyelashes | eyelash | NOUN | NNS | pobj | by | 16 |
| 19 | and | and | CCONJ | CC | cc | eyelashes | 18 |
| 20 | skin | skin | NOUN | NN | conj | eyelashes | 18 |
| 21 | , | , | PUNCT | , | punct | framed | 15 |
| 22 | with | with | ADP | IN | prep | framed | 15 |
| 23 | warm | warm | ADJ | JJ | amod | light | 26 |
| 24 | , | , | PUNCT | , | punct | light | 26 |
| 25 | glowing | glow | VERB | VBG | amod | light | 26 |
| 26 | light | light | NOUN | NN | nsubj | surrounding | 27 |
| 27 | surrounding | surround | VERB | VBG | pcomp | with | 22 |
| 28 | it | it | PRON | PRP | dobj | surrounding | 27 |
| 29 | . | . | PUNCT | . | punct | framed | 15 |
| 30 | Text | text | NOUN | NN | nsubj | reads | 34 |
| 31 | at | at | ADP | IN | prep | Text | 30 |
| 32 | the | the | DET | DT | det | bottom | 33 |
| 33 | bottom | bottom | NOUN | NN | pobj | at | 31 |
| 34 | reads | read | VERB | VBZ | ROOT | reads | 34 |
| 35 | "BORDERLINE BIENNALE 2011 \| Week-end 02 \| Hacking, T.A.Z. & Utopies Pirates." | borderline_biennale_2011_\|_week-end_02_\|_hacking,_t.a.z._&_utopies_pirates. | PROPN | NNP | dobj | reads | 34 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | close-up | close-up | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | human eye | human_eye | chunk1 | 4 | noun_chunk_root | high |
| m2 | object | irises | iris | chunk2 | 7 | noun_chunk_root | high |
| m3 | attribute | green | green | chunk2 | 6 | color_attribute | high |
| m4 | object | pupils | pupil | chunk3 | 10 | noun_chunk_root | high |
| m5 | attribute | dark | dark | chunk3 | 9 | visual_attribute | medium |
| m6 | object | eye | eye | chunk4 | 13 | noun_chunk_root | high |
| m7 | object | eyelashes | eyelash | chunk5 | 18 | noun_chunk_root | high |
| m8 | attribute | blurred | blurred | chunk5 | 17 | modifier_attribute | medium |
| m9 | object | skin | skin | chunk6 | 20 | noun_chunk_root | high |
| m10 | object | light | light | chunk7 | 26 | noun_chunk_root | high |
| m11 | attribute | warm | warm | chunk7 | 23 | modifier_attribute | medium |
| m12 | attribute | glowing | glow | chunk7 | 25 | state_attribute | medium |
| m13 | object | it | it | chunk8 | 28 | noun_chunk_root | high |
| m14 | object | Text | text | chunk9 | 30 | noun_chunk_root | high |
| m15 | object | bottom | bottom | chunk10 | 33 | noun_chunk_root | high |
| m16 | object | "BORDERLINE BIENNALE 2011 \| Week-end 02 \| Hacking, T.A.Z. & Utopies Pirates." | borderline_biennale_2011_\|_week-end_02_\|_hacking,_t.a.z._&_utopies_pirates. | chunk11 | 35 | noun_chunk_root | high |
| m17 | action | framed | frame | doc | 15 | verb_predicate | high |
| m18 | action | surrounding | surround | doc | 27 | verb_predicate | high |
| m19 | action | reads | read | doc | 34 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | chunk2 amod -> irises |
| e1 | has_attribute | m4 | m5 | medium | chunk3 amod -> pupils |
| e2 | has_attribute | m7 | m8 | medium | chunk5 amod -> eyelashes |
| e3 | has_attribute | m10 | m11 | medium | chunk7 amod -> light |
| e4 | has_attribute | m10 | m12 | medium | chunk7 amod -> light |
| e5 | agent | m17 | m6 | medium | nsubjpass -> framed |
| e6 | agent | m18 | m10 | medium | nsubj -> surrounding |
| e7 | patient | m18 | m13 | medium | dobj -> surrounding |
| e8 | agent | m19 | m14 | medium | nsubj -> reads |
| e9 | patient | m19 | m16 | medium | dobj -> reads |
| e10 | relation | m0 | m1 | medium | of |
| e11 | relation | m1 | m2 | high | with |
| e12 | relation | m1 | m4 | high | with |
| e13 | relation | m6 | m7 | medium | by |
| e14 | relation | m6 | m9 | medium | by |
| e15 | relation | m14 | m15 | medium | at |

## 33

**caption_shape:** `sentence-like`
**caption_id:** `1524f40396e3ee37f6ab4234e0783cbbdab0250d92b25f92a011fc39bd2a4014`

> A woman walks down a city sidewalk while talking on her phone, carrying a black bag.

### Sentences
| sentence | token_span |
| --- | --- |
| A woman walks down a city sidewalk while talking on her phone, carrying a black bag. | 0:18 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A woman | woman | woman | nsubj | walks | 0:2 |
| a city sidewalk | sidewalk | sidewalk | pobj | down | 4:7 |
| her phone | phone | phone | pobj | on | 10:12 |
| a black bag | bag | bag | dobj | carrying | 14:17 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | woman | 1 |
| 1 | woman | woman | NOUN | NN | nsubj | walks | 2 |
| 2 | walks | walk | VERB | VBZ | ROOT | walks | 2 |
| 3 | down | down | ADP | IN | prep | walks | 2 |
| 4 | a | a | DET | DT | det | sidewalk | 6 |
| 5 | city | city | NOUN | NN | compound | sidewalk | 6 |
| 6 | sidewalk | sidewalk | NOUN | NN | pobj | down | 3 |
| 7 | while | while | SCONJ | IN | mark | talking | 8 |
| 8 | talking | talk | VERB | VBG | advcl | walks | 2 |
| 9 | on | on | ADP | IN | prep | talking | 8 |
| 10 | her | her | PRON | PRP$ | poss | phone | 11 |
| 11 | phone | phone | NOUN | NN | pobj | on | 9 |
| 12 | , | , | PUNCT | , | punct | walks | 2 |
| 13 | carrying | carry | VERB | VBG | advcl | walks | 2 |
| 14 | a | a | DET | DT | det | bag | 16 |
| 15 | black | black | ADJ | JJ | amod | bag | 16 |
| 16 | bag | bag | NOUN | NN | dobj | carrying | 13 |
| 17 | . | . | PUNCT | . | punct | walks | 2 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | sidewalk | sidewalk | chunk1 | 6 | noun_chunk_root | high |
| m2 | attribute | city | city | chunk1 | 5 | compound_modifier | medium |
| m3 | object | phone | phone | chunk2 | 11 | noun_chunk_root | high |
| m4 | attribute | her | her | chunk2 | 10 | modifier_attribute | medium |
| m5 | object | bag | bag | chunk3 | 16 | noun_chunk_root | high |
| m6 | attribute | black | black | chunk3 | 15 | color_attribute | high |
| m7 | action | walks | walk | doc | 2 | verb_predicate | high |
| m8 | action | talking | talk | doc | 8 | verb_predicate | high |
| m9 | action | carrying | carry | doc | 13 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 compound -> sidewalk |
| e1 | has_attribute | m3 | m4 | medium | chunk2 poss -> phone |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> bag |
| e3 | agent | m7 | m0 | medium | nsubj -> walks |
| e4 | patient | m9 | m5 | medium | dobj -> carrying |
| e5 | relation | m0 | m1 | medium | down |
| e6 | relation | m0 | m3 | high | on |

## 34

**caption_shape:** `multi-sentence`
**caption_id:** `1703f280c90701c4aef227f67111f898a019781df197ca00271778204d4e0014`

> A black-and-white graffiti stencil on a concrete pillar reads “THE ONLY MAN TO ENTER PARLIAMENT WITH HONEST INTENTIONS.” The artwork depicts a man in a hat and ruff collar, surrounded by a circle. The pillar stands beside a narrow alley with a stone wall and a wooden beam above.

**parsed_caption:**

> A black-and-white graffiti stencil on a concrete pillar reads “THE ONLY MAN TO ENTER PARLIAMENT WITH HONEST INTENTIONS.” The artwork depicts a man in a hat and ruff collar, surrounded by a circle. The pillar stands beside a narrow alley with a stone wall and a wooden beam above.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 1703f280c90701c4aef227f67111f898a019781df197ca00271778204d4e0014:q0 | THE ONLY MAN TO ENTER PARLIAMENT WITH HONEST INTENTIONS. | the only man to enter parliament with honest intentions. | raw_quote_span |  | 62:120 | 62:120 |

### Sentences
| sentence | token_span |
| --- | --- |
| A black-and-white graffiti stencil on a concrete pillar reads “THE ONLY MAN TO ENTER PARLIAMENT WITH HONEST INTENTIONS.” The artwork depicts a man in a hat and ruff collar, surrounded by a circle. | 0:27 |
| The pillar stands beside a narrow alley with a stone wall and a wooden beam above. | 27:44 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A black-and-white graffiti stencil | stencil | stencil | nsubj | reads | 0:4 |
| a concrete pillar | pillar | pillar | pobj | on | 5:8 |
| The artwork | artwork | artwork | nsubj | depicts | 10:12 |
| a man | man | man | dobj | depicts | 13:15 |
| a hat | hat | hat | pobj | in | 16:18 |
| ruff collar | collar | collar | conj | hat | 19:21 |
| a circle | circle | circle | pobj | by | 24:26 |
| The pillar | pillar | pillar | nsubj | stands | 27:29 |
| a narrow alley | alley | alley | pobj | beside | 31:34 |
| a stone wall | wall | wall | pobj | with | 35:38 |
| a wooden beam | beam | beam | conj | wall | 39:42 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | stencil | 3 |
| 1 | black-and-white | black-and-white | ADJ | JJ | amod | stencil | 3 |
| 2 | graffiti | graffiti | NOUN | NN | compound | stencil | 3 |
| 3 | stencil | stencil | NOUN | NN | nsubj | reads | 8 |
| 4 | on | on | ADP | IN | prep | stencil | 3 |
| 5 | a | a | DET | DT | det | pillar | 7 |
| 6 | concrete | concrete | ADJ | JJ | amod | pillar | 7 |
| 7 | pillar | pillar | NOUN | NN | pobj | on | 4 |
| 8 | reads | read | VERB | VBZ | ROOT | reads | 8 |
| 9 | “THE ONLY MAN TO ENTER PARLIAMENT WITH HONEST INTENTIONS.” | the_only_man_to_enter_parliament_with_honest_intentions. | NOUN | NN | punct | reads | 8 |
| 10 | The | the | DET | DT | det | artwork | 11 |
| 11 | artwork | artwork | NOUN | NN | nsubj | depicts | 12 |
| 12 | depicts | depict | VERB | VBZ | ccomp | reads | 8 |
| 13 | a | a | DET | DT | det | man | 14 |
| 14 | man | man | NOUN | NN | dobj | depicts | 12 |
| 15 | in | in | ADP | IN | prep | man | 14 |
| 16 | a | a | DET | DT | det | hat | 17 |
| 17 | hat | hat | NOUN | NN | pobj | in | 15 |
| 18 | and | and | CCONJ | CC | cc | hat | 17 |
| 19 | ruff | ruff | NOUN | NN | compound | collar | 20 |
| 20 | collar | collar | NOUN | NN | conj | hat | 17 |
| 21 | , | , | PUNCT | , | punct | man | 14 |
| 22 | surrounded | surround | VERB | VBN | acl | man | 14 |
| 23 | by | by | ADP | IN | agent | surrounded | 22 |
| 24 | a | a | DET | DT | det | circle | 25 |
| 25 | circle | circle | NOUN | NN | pobj | by | 23 |
| 26 | . | . | PUNCT | . | punct | depicts | 12 |
| 27 | The | the | DET | DT | det | pillar | 28 |
| 28 | pillar | pillar | NOUN | NN | nsubj | stands | 29 |
| 29 | stands | stand | VERB | VBZ | ROOT | stands | 29 |
| 30 | beside | beside | ADP | IN | prep | stands | 29 |
| 31 | a | a | DET | DT | det | alley | 33 |
| 32 | narrow | narrow | ADJ | JJ | amod | alley | 33 |
| 33 | alley | alley | NOUN | NN | pobj | beside | 30 |
| 34 | with | with | ADP | IN | prep | alley | 33 |
| 35 | a | a | DET | DT | det | wall | 37 |
| 36 | stone | stone | NOUN | NN | compound | wall | 37 |
| 37 | wall | wall | NOUN | NN | pobj | with | 34 |
| 38 | and | and | CCONJ | CC | cc | wall | 37 |
| 39 | a | a | DET | DT | det | beam | 41 |
| 40 | wooden | wooden | ADJ | JJ | amod | beam | 41 |
| 41 | beam | beam | NOUN | NN | conj | wall | 37 |
| 42 | above | above | ADV | RB | advmod | wall | 37 |
| 43 | . | . | PUNCT | . | punct | stands | 29 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | stencil | stencil | chunk0 | 3 | noun_chunk_root | high |
| m1 | attribute | black-and-white | black-and-white | chunk0 | 1 | modifier_attribute | medium |
| m2 | attribute | graffiti | graffiti | chunk0 | 2 | compound_modifier | medium |
| m3 | object | pillar | pillar | chunk1 | 7 | noun_chunk_root | high |
| m4 | attribute | concrete | concrete | chunk1 | 6 | material_attribute | high |
| m5 | object | artwork | artwork | chunk2 | 11 | noun_chunk_root | high |
| m6 | object | man | man | chunk3 | 14 | noun_chunk_root | high |
| m7 | object | hat | hat | chunk4 | 17 | noun_chunk_root | high |
| m8 | object | collar | collar | chunk5 | 20 | noun_chunk_root | high |
| m9 | attribute | ruff | ruff | chunk5 | 19 | compound_modifier | medium |
| m10 | object | circle | circle | chunk6 | 25 | noun_chunk_root | high |
| m11 | object | pillar | pillar | chunk7 | 28 | noun_chunk_root | high |
| m12 | object | alley | alley | chunk8 | 33 | noun_chunk_root | high |
| m13 | attribute | narrow | narrow | chunk8 | 32 | size_attribute | high |
| m14 | object | wall | wall | chunk9 | 37 | noun_chunk_root | high |
| m15 | attribute | stone | stone | chunk9 | 36 | material_attribute | high |
| m16 | object | beam | beam | chunk10 | 41 | noun_chunk_root | high |
| m17 | attribute | wooden | wooden | chunk10 | 40 | material_attribute | high |
| m18 | action | reads | read | doc | 8 | verb_predicate | high |
| m19 | action | depicts | depict | doc | 12 | verb_predicate | high |
| m20 | action | surrounded | surround | doc | 22 | verb_predicate | high |
| m21 | action | stands | stand | doc | 29 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> stencil |
| e1 | has_attribute | m0 | m2 | medium | chunk0 compound -> stencil |
| e2 | has_attribute | m3 | m4 | high | chunk1 amod -> pillar |
| e3 | has_attribute | m8 | m9 | medium | chunk5 compound -> collar |
| e4 | has_attribute | m12 | m13 | high | chunk8 amod -> alley |
| e5 | has_attribute | m14 | m15 | high | chunk9 compound -> wall |
| e6 | has_attribute | m16 | m17 | high | chunk10 amod -> beam |
| e7 | agent | m18 | m0 | medium | nsubj -> reads |
| e8 | agent | m19 | m5 | medium | nsubj -> depicts |
| e9 | patient | m19 | m6 | medium | dobj -> depicts |
| e10 | agent | m21 | m11 | medium | nsubj -> stands |
| e11 | relation | m0 | m3 | high | on |
| e12 | relation | m6 | m7 | high | in |
| e13 | relation | m6 | m8 | high | in |
| e14 | relation | m6 | m10 | medium | by |
| e15 | relation | m11 | m12 | high | beside |
| e16 | relation | m12 | m14 | high | with |
| e17 | relation | m12 | m16 | high | with |

## 35

**caption_shape:** `multi-sentence`
**caption_id:** `17bb3cbac28bf54f3adf0a0392bde680a28bcd74014af96019175bcafd55a414`

> A man with dark hair and a goatee wears a black shirt and makes a hand gesture with both hands. He has red nail polish, a silver chain necklace, and an earring, standing indoors near a wooden door and a colorful banner.

### Sentences
| sentence | token_span |
| --- | --- |
| A man with dark hair and a goatee wears a black shirt and makes a hand gesture with both hands. | 0:21 |
| He has red nail polish, a silver chain necklace, and an earring, standing indoors near a wooden door and a colorful banner. | 21:46 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A man | man | man | nsubj | wears | 0:2 |
| dark hair | hair | hair | pobj | with | 3:5 |
| a goatee | goatee | goatee | conj | hair | 6:8 |
| a black shirt | shirt | shirt | dobj | wears | 9:12 |
| a hand gesture | gesture | gesture | dobj | makes | 14:17 |
| both hands | hands | hand | pobj | with | 18:20 |
| He | He | he | nsubj | has | 21:22 |
| red nail polish | nail polish | nail_polish | dobj | has | 23:25 |
| a silver chain necklace | necklace | necklace | conj | nail polish | 26:30 |
| an earring | earring | earring | conj | necklace | 32:34 |
| a wooden door | door | door | pobj | near | 38:41 |
| a colorful banner | banner | banner | conj | door | 42:45 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | man | 1 |
| 1 | man | man | NOUN | NN | nsubj | wears | 8 |
| 2 | with | with | ADP | IN | prep | man | 1 |
| 3 | dark | dark | ADJ | JJ | amod | hair | 4 |
| 4 | hair | hair | NOUN | NN | pobj | with | 2 |
| 5 | and | and | CCONJ | CC | cc | hair | 4 |
| 6 | a | a | DET | DT | det | goatee | 7 |
| 7 | goatee | goatee | NOUN | NN | conj | hair | 4 |
| 8 | wears | wear | VERB | VBZ | ROOT | wears | 8 |
| 9 | a | a | DET | DT | det | shirt | 11 |
| 10 | black | black | ADJ | JJ | amod | shirt | 11 |
| 11 | shirt | shirt | NOUN | NN | dobj | wears | 8 |
| 12 | and | and | CCONJ | CC | cc | wears | 8 |
| 13 | makes | make | VERB | VBZ | conj | wears | 8 |
| 14 | a | a | DET | DT | det | gesture | 16 |
| 15 | hand | hand | NOUN | NN | compound | gesture | 16 |
| 16 | gesture | gesture | NOUN | NN | dobj | makes | 13 |
| 17 | with | with | ADP | IN | prep | makes | 13 |
| 18 | both | both | DET | DT | det | hands | 19 |
| 19 | hands | hand | NOUN | NNS | pobj | with | 17 |
| 20 | . | . | PUNCT | . | punct | wears | 8 |
| 21 | He | he | PRON | PRP | nsubj | has | 22 |
| 22 | has | have | VERB | VBZ | ROOT | has | 22 |
| 23 | red | red | ADJ | JJ | amod | nail polish | 24 |
| 24 | nail polish | nail_polish | NOUN | NN | dobj | has | 22 |
| 25 | , | , | PUNCT | , | punct | nail polish | 24 |
| 26 | a | a | DET | DT | det | necklace | 29 |
| 27 | silver | silver | ADJ | JJ | amod | necklace | 29 |
| 28 | chain | chain | NOUN | NN | compound | necklace | 29 |
| 29 | necklace | necklace | NOUN | NN | conj | nail polish | 24 |
| 30 | , | , | PUNCT | , | punct | necklace | 29 |
| 31 | and | and | CCONJ | CC | cc | necklace | 29 |
| 32 | an | an | DET | DT | det | earring | 33 |
| 33 | earring | earring | NOUN | NN | conj | necklace | 29 |
| 34 | , | , | PUNCT | , | punct | has | 22 |
| 35 | standing | stand | VERB | VBG | advcl | has | 22 |
| 36 | indoors | indoors | ADV | RB | advmod | standing | 35 |
| 37 | near | near | ADP | IN | prep | standing | 35 |
| 38 | a | a | DET | DT | det | door | 40 |
| 39 | wooden | wooden | ADJ | JJ | amod | door | 40 |
| 40 | door | door | NOUN | NN | pobj | near | 37 |
| 41 | and | and | CCONJ | CC | cc | door | 40 |
| 42 | a | a | DET | DT | det | banner | 44 |
| 43 | colorful | colorful | ADJ | JJ | amod | banner | 44 |
| 44 | banner | banner | NOUN | NN | conj | door | 40 |
| 45 | . | . | PUNCT | . | punct | has | 22 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | hair | hair | chunk1 | 4 | noun_chunk_root | high |
| m2 | attribute | dark | dark | chunk1 | 3 | visual_attribute | medium |
| m3 | object | goatee | goatee | chunk2 | 7 | noun_chunk_root | high |
| m4 | object | shirt | shirt | chunk3 | 11 | noun_chunk_root | high |
| m5 | attribute | black | black | chunk3 | 10 | color_attribute | high |
| m6 | object | gesture | gesture | chunk4 | 16 | noun_chunk_root | high |
| m7 | attribute | hand | hand | chunk4 | 15 | compound_modifier | medium |
| m8 | object | hands | hand | chunk5 | 19 | noun_chunk_root | high |
| m9 | object | He | he | chunk6 | 21 | noun_chunk_root | high |
| m10 | object | nail polish | nail_polish | chunk7 | 24 | noun_chunk_root | high |
| m11 | attribute | red | red | chunk7 | 23 | color_attribute | high |
| m12 | object | necklace | necklace | chunk8 | 29 | noun_chunk_root | high |
| m13 | attribute | silver | silver | chunk8 | 27 | color_attribute | high |
| m14 | attribute | chain | chain | chunk8 | 28 | compound_modifier | medium |
| m15 | object | earring | earring | chunk9 | 33 | noun_chunk_root | high |
| m16 | object | door | door | chunk10 | 40 | noun_chunk_root | high |
| m17 | attribute | wooden | wooden | chunk10 | 39 | material_attribute | high |
| m18 | object | banner | banner | chunk11 | 44 | noun_chunk_root | high |
| m19 | attribute | colorful | colorful | chunk11 | 43 | modifier_attribute | medium |
| m20 | context | indoors | indoors | doc | 36 | context_word | medium |
| m21 | action | wears | wear | doc | 8 | verb_predicate | high |
| m22 | action | makes | make | doc | 13 | verb_predicate | high |
| m23 | action | has | have | doc | 22 | verb_predicate | high |
| m24 | action | standing | stand | doc | 35 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 amod -> hair |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> shirt |
| e2 | has_attribute | m6 | m7 | medium | chunk4 compound -> gesture |
| e3 | has_attribute | m10 | m11 | high | chunk7 amod -> nail polish |
| e4 | has_attribute | m12 | m13 | high | chunk8 amod -> necklace |
| e5 | has_attribute | m12 | m14 | medium | chunk8 compound -> necklace |
| e6 | has_attribute | m16 | m17 | high | chunk10 amod -> door |
| e7 | has_attribute | m18 | m19 | medium | chunk11 amod -> banner |
| e8 | has_context | scene | m20 | medium | context token indoors |
| e9 | agent | m21 | m0 | medium | nsubj -> wears |
| e10 | patient | m21 | m4 | medium | dobj -> wears |
| e11 | patient | m22 | m6 | medium | dobj -> makes |
| e12 | agent | m23 | m9 | medium | nsubj -> has |
| e13 | patient | m23 | m10 | medium | dobj -> has |
| e14 | patient | m23 | m12 | medium | dobj -> has |
| e15 | patient | m23 | m15 | medium | dobj -> has |
| e16 | relation | m0 | m1 | high | with |
| e17 | relation | m0 | m3 | high | with |
| e18 | relation | m0 | m8 | high | with |
| e19 | relation | m9 | m16 | high | near |
| e20 | relation | m9 | m18 | high | near |

## 36

**caption_shape:** `multi-sentence`
**caption_id:** `1bd607b3ebbc9d4a0a56e7195d5cb8de4411b1fa93b2690f1555eb336d366814`

> A large building with "P.J. HURPHY MOVING & STORAGE" sign stands beside a road, near tall smokestacks and power lines.

**parsed_caption:**

> A large building with "P.J. HURPHY MOVING & STORAGE" sign stands beside a road, near tall smokestacks and power lines.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 1bd607b3ebbc9d4a0a56e7195d5cb8de4411b1fa93b2690f1555eb336d366814:q0 | P.J. HURPHY MOVING & STORAGE | p.j. hurphy moving & storage | raw_quote_span |  | 22:52 | 22:52 |

### Sentences
| sentence | token_span |
| --- | --- |
| A large building with "P.J. HURPHY MOVING & STORAGE" sign stands beside a road, near tall smokestacks and power lines. | 0:17 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A large building | building | building | nsubj | stands | 0:3 |
| "P.J. HURPHY MOVING & STORAGE" sign | sign | sign | pobj | with | 4:6 |
| a road | road | road | pobj | beside | 8:10 |
| tall smokestacks | smokestacks | smokestack | pobj | near | 12:14 |
| power lines | power lines | power_line | conj | smokestacks | 15:16 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | building | 2 |
| 1 | large | large | ADJ | JJ | amod | building | 2 |
| 2 | building | building | NOUN | NN | nsubj | stands | 6 |
| 3 | with | with | ADP | IN | prep | building | 2 |
| 4 | "P.J. HURPHY MOVING & STORAGE" | p.j._hurphy_moving_&_storage | PROPN | NNP | nmod | sign | 5 |
| 5 | sign | sign | NOUN | NN | pobj | with | 3 |
| 6 | stands | stand | VERB | VBZ | ROOT | stands | 6 |
| 7 | beside | beside | ADP | IN | prep | stands | 6 |
| 8 | a | a | DET | DT | det | road | 9 |
| 9 | road | road | NOUN | NN | pobj | beside | 7 |
| 10 | , | , | PUNCT | , | punct | stands | 6 |
| 11 | near | near | ADP | IN | prep | stands | 6 |
| 12 | tall | tall | ADJ | JJ | amod | smokestacks | 13 |
| 13 | smokestacks | smokestack | NOUN | NNS | pobj | near | 11 |
| 14 | and | and | CCONJ | CC | cc | smokestacks | 13 |
| 15 | power lines | power_line | NOUN | NN | conj | smokestacks | 13 |
| 16 | . | . | PUNCT | . | punct | stands | 6 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | large | large | chunk0 | 1 | size_attribute | high |
| m2 | object | sign | sign | chunk1 | 5 | noun_chunk_root | high |
| m3 | object | road | road | chunk2 | 9 | noun_chunk_root | high |
| m4 | object | smokestacks | smokestack | chunk3 | 13 | noun_chunk_root | high |
| m5 | attribute | tall | tall | chunk3 | 12 | size_attribute | high |
| m6 | object | power lines | power_line | chunk4 | 15 | noun_chunk_root | high |
| m7 | action | stands | stand | doc | 6 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> building |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> smokestacks |
| e2 | agent | m7 | m0 | medium | nsubj -> stands |
| e3 | relation | m0 | m2 | high | with |
| e4 | relation | m0 | m3 | high | beside |
| e5 | relation | m0 | m4 | high | near |
| e6 | relation | m0 | m6 | high | near |

## 37

**caption_shape:** `multi-sentence`
**caption_id:** `1c4fa5d0c6c46c6b268a9729dce637adb5c2e3c0167d2364feb3a039ba805414`

> A narrow alleyway paved with bricks stretches between two tall brick walls. On the right, a bare tree stands near the end of the path, with houses visible beyond. Shadows stretch across the ground from the left wall.

### Sentences
| sentence | token_span |
| --- | --- |
| A narrow alleyway paved with bricks stretches between two tall brick walls. | 0:13 |
| On the right, a bare tree stands near the end of the path, with houses visible beyond. | 13:33 |
| Shadows stretch across the ground from the left wall. | 33:43 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A narrow alleyway | alleyway | alleyway | nsubj | stretches | 0:3 |
| bricks | bricks | brick | pobj | with | 5:6 |
| two tall brick walls | walls | wall | pobj | between | 8:12 |
| the right | right | right | pobj | On | 14:16 |
| a bare tree | tree | tree | nsubj | stands | 17:20 |
| the end | end | end | pobj | near | 22:24 |
| the path | path | path | pobj | of | 25:27 |
| houses | houses | house | nsubj | visible | 29:30 |
| Shadows | Shadows | shadow | nsubj | stretch | 33:34 |
| the ground | ground | ground | pobj | across | 36:38 |
| the left wall | wall | wall | pobj | from | 39:42 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | alleyway | 2 |
| 1 | narrow | narrow | ADJ | JJ | amod | alleyway | 2 |
| 2 | alleyway | alleyway | NOUN | NN | nsubj | stretches | 6 |
| 3 | paved | pave | VERB | VBN | acl | alleyway | 2 |
| 4 | with | with | ADP | IN | prep | paved | 3 |
| 5 | bricks | brick | NOUN | NNS | pobj | with | 4 |
| 6 | stretches | stretch | VERB | VBZ | ROOT | stretches | 6 |
| 7 | between | between | ADP | IN | prep | stretches | 6 |
| 8 | two | two | NUM | CD | nummod | walls | 11 |
| 9 | tall | tall | ADJ | JJ | amod | walls | 11 |
| 10 | brick | brick | NOUN | NN | compound | walls | 11 |
| 11 | walls | wall | NOUN | NNS | pobj | between | 7 |
| 12 | . | . | PUNCT | . | punct | stretches | 6 |
| 13 | On | on | ADP | IN | prep | stands | 20 |
| 14 | the | the | DET | DT | det | right | 15 |
| 15 | right | right | NOUN | NN | pobj | On | 13 |
| 16 | , | , | PUNCT | , | punct | stands | 20 |
| 17 | a | a | DET | DT | det | tree | 19 |
| 18 | bare | bare | ADJ | JJ | amod | tree | 19 |
| 19 | tree | tree | NOUN | NN | nsubj | stands | 20 |
| 20 | stands | stand | VERB | VBZ | ROOT | stands | 20 |
| 21 | near | near | ADP | IN | prep | stands | 20 |
| 22 | the | the | DET | DT | det | end | 23 |
| 23 | end | end | NOUN | NN | pobj | near | 21 |
| 24 | of | of | ADP | IN | prep | end | 23 |
| 25 | the | the | DET | DT | det | path | 26 |
| 26 | path | path | NOUN | NN | pobj | of | 24 |
| 27 | , | , | PUNCT | , | punct | stands | 20 |
| 28 | with | with | SCONJ | IN | mark | visible | 30 |
| 29 | houses | house | NOUN | NNS | nsubj | visible | 30 |
| 30 | visible | visible | ADJ | JJ | advcl | stands | 20 |
| 31 | beyond | beyond | ADV | RB | advmod | visible | 30 |
| 32 | . | . | PUNCT | . | punct | stands | 20 |
| 33 | Shadows | shadow | NOUN | NNS | nsubj | stretch | 34 |
| 34 | stretch | stretch | VERB | VBP | ROOT | stretch | 34 |
| 35 | across | across | ADP | IN | prep | stretch | 34 |
| 36 | the | the | DET | DT | det | ground | 37 |
| 37 | ground | ground | NOUN | NN | pobj | across | 35 |
| 38 | from | from | ADP | IN | prep | stretch | 34 |
| 39 | the | the | DET | DT | det | wall | 41 |
| 40 | left | left | ADJ | JJ | amod | wall | 41 |
| 41 | wall | wall | NOUN | NN | pobj | from | 38 |
| 42 | . | . | PUNCT | . | punct | stretch | 34 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | alleyway | alleyway | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | narrow | narrow | chunk0 | 1 | size_attribute | high |
| m2 | object | bricks | brick | chunk1 | 5 | noun_chunk_root | high |
| m3 | object | walls | wall | chunk2 | 11 | noun_chunk_root | high |
| m4 | quantity | two | two | chunk2 | 8 | quantity | high |
| m5 | attribute | tall | tall | chunk2 | 9 | size_attribute | high |
| m6 | attribute | brick | brick | chunk2 | 10 | material_attribute | high |
| m7 | object | right | right | chunk3 | 15 | noun_chunk_root | high |
| m8 | object | tree | tree | chunk4 | 19 | noun_chunk_root | high |
| m9 | attribute | bare | bare | chunk4 | 18 | visual_attribute | medium |
| m10 | object | end | end | chunk5 | 23 | noun_chunk_root | high |
| m11 | object | path | path | chunk6 | 26 | noun_chunk_root | high |
| m12 | object | houses | house | chunk7 | 29 | noun_chunk_root | high |
| m13 | object | Shadows | shadow | chunk8 | 33 | noun_chunk_root | high |
| m14 | object | ground | ground | chunk9 | 37 | noun_chunk_root | high |
| m15 | object | wall | wall | chunk10 | 41 | noun_chunk_root | high |
| m16 | attribute | left | left | chunk10 | 40 | modifier_attribute | medium |
| m17 | action | paved | pave | doc | 3 | verb_predicate | high |
| m18 | action | stretches | stretch | doc | 6 | verb_predicate | high |
| m19 | action | stands | stand | doc | 20 | verb_predicate | high |
| m20 | action | stretch | stretch | doc | 34 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> alleyway |
| e1 | has_quantity | m3 | m4 | high | chunk2 nummod -> walls |
| e2 | has_attribute | m3 | m5 | high | chunk2 amod -> walls |
| e3 | has_attribute | m3 | m6 | high | chunk2 compound -> walls |
| e4 | has_attribute | m8 | m9 | medium | chunk4 amod -> tree |
| e5 | has_attribute | m15 | m16 | medium | chunk10 amod -> wall |
| e6 | agent | m18 | m0 | medium | nsubj -> stretches |
| e7 | agent | m19 | m8 | medium | nsubj -> stands |
| e8 | agent | m20 | m13 | medium | nsubj -> stretch |
| e9 | relation | m0 | m2 | high | with |
| e10 | relation | m0 | m3 | high | between |
| e11 | relation | m8 | m7 | high | on |
| e12 | relation | m8 | m10 | high | near |
| e13 | relation | m10 | m11 | medium | of |
| e14 | relation | m13 | m14 | high | across |
| e15 | relation | m13 | m15 | medium | from |

## 38

**caption_shape:** `multi-sentence`
**caption_id:** `219a6de5da69d0a3b9cee9914590eb7a70c6495c2e2aa659e88a3d3a4c4f0014`

> A beige building with columns and a golden entrance is surrounded by tall palm trees. The structure sits on a green lawn under a clear blue sky, with shadows cast across the grass from the trees.

### Sentences
| sentence | token_span |
| --- | --- |
| A beige building with columns and a golden entrance is surrounded by tall palm trees. | 0:15 |
| The structure sits on a green lawn under a clear blue sky, with shadows cast across the grass from the trees. | 15:38 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A beige building | building | building | nsubjpass | surrounded | 0:3 |
| columns | columns | column | pobj | with | 4:5 |
| a golden entrance | entrance | entrance | conj | columns | 6:9 |
| tall palm trees | palm trees | palm_tree | pobj | by | 12:14 |
| The structure | structure | structure | nsubj | sits | 15:17 |
| a green lawn | lawn | lawn | pobj | on | 19:22 |
| a clear blue sky | sky | sky | pobj | under | 23:27 |
| shadows | shadows | shadow | pobj | with | 29:30 |
| the grass | grass | grass | pobj | across | 32:34 |
| the trees | trees | tree | pobj | from | 35:37 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | building | 2 |
| 1 | beige | beige | ADJ | JJ | amod | building | 2 |
| 2 | building | building | NOUN | NN | nsubjpass | surrounded | 10 |
| 3 | with | with | ADP | IN | prep | building | 2 |
| 4 | columns | column | NOUN | NNS | pobj | with | 3 |
| 5 | and | and | CCONJ | CC | cc | columns | 4 |
| 6 | a | a | DET | DT | det | entrance | 8 |
| 7 | golden | golden | ADJ | JJ | amod | entrance | 8 |
| 8 | entrance | entrance | NOUN | NN | conj | columns | 4 |
| 9 | is | be | AUX | VBZ | auxpass | surrounded | 10 |
| 10 | surrounded | surround | VERB | VBN | ROOT | surrounded | 10 |
| 11 | by | by | ADP | IN | agent | surrounded | 10 |
| 12 | tall | tall | ADJ | JJ | amod | palm trees | 13 |
| 13 | palm trees | palm_tree | NOUN | NN | pobj | by | 11 |
| 14 | . | . | PUNCT | . | punct | surrounded | 10 |
| 15 | The | the | DET | DT | det | structure | 16 |
| 16 | structure | structure | NOUN | NN | nsubj | sits | 17 |
| 17 | sits | sit | VERB | VBZ | ROOT | sits | 17 |
| 18 | on | on | ADP | IN | prep | sits | 17 |
| 19 | a | a | DET | DT | det | lawn | 21 |
| 20 | green | green | ADJ | JJ | amod | lawn | 21 |
| 21 | lawn | lawn | NOUN | NN | pobj | on | 18 |
| 22 | under | under | ADP | IN | prep | sits | 17 |
| 23 | a | a | DET | DT | det | sky | 26 |
| 24 | clear | clear | ADJ | JJ | amod | sky | 26 |
| 25 | blue | blue | ADJ | JJ | amod | sky | 26 |
| 26 | sky | sky | NOUN | NN | pobj | under | 22 |
| 27 | , | , | PUNCT | , | punct | sits | 17 |
| 28 | with | with | ADP | IN | prep | sits | 17 |
| 29 | shadows | shadow | NOUN | NNS | pobj | with | 28 |
| 30 | cast | cast | VERB | VBN | acl | shadows | 29 |
| 31 | across | across | ADP | IN | prep | cast | 30 |
| 32 | the | the | DET | DT | det | grass | 33 |
| 33 | grass | grass | NOUN | NN | pobj | across | 31 |
| 34 | from | from | ADP | IN | prep | cast | 30 |
| 35 | the | the | DET | DT | det | trees | 36 |
| 36 | trees | tree | NOUN | NNS | pobj | from | 34 |
| 37 | . | . | PUNCT | . | punct | sits | 17 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | beige | beige | chunk0 | 1 | color_attribute | high |
| m2 | object | columns | column | chunk1 | 4 | noun_chunk_root | high |
| m3 | object | entrance | entrance | chunk2 | 8 | noun_chunk_root | high |
| m4 | attribute | golden | golden | chunk2 | 7 | color_attribute | high |
| m5 | object | palm trees | palm_tree | chunk3 | 13 | noun_chunk_root | high |
| m6 | attribute | tall | tall | chunk3 | 12 | size_attribute | high |
| m7 | object | structure | structure | chunk4 | 16 | noun_chunk_root | high |
| m8 | object | lawn | lawn | chunk5 | 21 | noun_chunk_root | high |
| m9 | attribute | green | green | chunk5 | 20 | color_attribute | high |
| m10 | object | sky | sky | chunk6 | 26 | noun_chunk_root | high |
| m11 | attribute | clear | clear | chunk6 | 24 | visual_attribute | medium |
| m12 | attribute | blue | blue | chunk6 | 25 | color_attribute | high |
| m13 | object | shadows | shadow | chunk7 | 29 | noun_chunk_root | high |
| m14 | object | grass | grass | chunk8 | 33 | noun_chunk_root | high |
| m15 | object | trees | tree | chunk9 | 36 | noun_chunk_root | high |
| m16 | action | surrounded | surround | doc | 10 | verb_predicate | high |
| m17 | action | sits | sit | doc | 17 | verb_predicate | high |
| m18 | action | cast | cast | doc | 30 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> building |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> entrance |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> palm trees |
| e3 | has_attribute | m8 | m9 | high | chunk5 amod -> lawn |
| e4 | has_attribute | m10 | m11 | medium | chunk6 amod -> sky |
| e5 | has_attribute | m10 | m12 | high | chunk6 amod -> sky |
| e6 | agent | m16 | m0 | medium | nsubjpass -> surrounded |
| e7 | agent | m17 | m7 | medium | nsubj -> sits |
| e8 | relation | m0 | m2 | high | with |
| e9 | relation | m0 | m3 | high | with |
| e10 | relation | m0 | m5 | medium | by |
| e11 | relation | m7 | m8 | high | on |
| e12 | relation | m7 | m10 | high | under |
| e13 | relation | m7 | m13 | high | with |
| e14 | relation | m13 | m14 | high | across |
| e15 | relation | m13 | m15 | medium | from |

## 39

**caption_shape:** `multi-sentence`
**caption_id:** `21f64d6e3be344388d8ed0dc49bd94c22a5ba9c555a96cdfc624524854997c14`

> A tall glass of latte macchiato sits on a wooden table, topped with foam and resting on a black tray with a doily. A spoon and sugar packet are beside it, with a blurred outdoor background showing rocks and greenery.

### Sentences
| sentence | token_span |
| --- | --- |
| A tall glass of latte macchiato sits on a wooden table, topped with foam and resting on a black tray with a doily. | 0:25 |
| A spoon and sugar packet are beside it, with a blurred outdoor background showing rocks and greenery. | 25:44 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A tall glass | glass | glass | nsubj | sits | 0:3 |
| latte macchiato | macchiato | macchiato | pobj | of | 4:6 |
| a wooden table | table | table | pobj | on | 8:11 |
| foam | foam | foam | pobj | with | 14:15 |
| a black tray | tray | tray | pobj | on | 18:21 |
| a doily | doily | doily | pobj | with | 22:24 |
| A spoon | spoon | spoon | nsubj | are | 25:27 |
| sugar packet | packet | packet | conj | spoon | 28:30 |
| it | it | it | pobj | beside | 32:33 |
| a blurred outdoor background | background | background | nsubj | showing | 35:39 |
| rocks | rocks | rock | dobj | showing | 40:41 |
| greenery | greenery | greenery | conj | rocks | 42:43 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | glass | 2 |
| 1 | tall | tall | ADJ | JJ | amod | glass | 2 |
| 2 | glass | glass | NOUN | NN | nsubj | sits | 6 |
| 3 | of | of | ADP | IN | prep | glass | 2 |
| 4 | latte | latte | NOUN | NN | compound | macchiato | 5 |
| 5 | macchiato | macchiato | NOUN | NN | pobj | of | 3 |
| 6 | sits | sit | VERB | VBZ | ROOT | sits | 6 |
| 7 | on | on | ADP | IN | prep | sits | 6 |
| 8 | a | a | DET | DT | det | table | 10 |
| 9 | wooden | wooden | ADJ | JJ | amod | table | 10 |
| 10 | table | table | NOUN | NN | pobj | on | 7 |
| 11 | , | , | PUNCT | , | punct | sits | 6 |
| 12 | topped | top | VERB | VBN | advcl | sits | 6 |
| 13 | with | with | ADP | IN | prep | topped | 12 |
| 14 | foam | foam | NOUN | NN | pobj | with | 13 |
| 15 | and | and | CCONJ | CC | cc | topped | 12 |
| 16 | resting | rest | VERB | VBG | conj | topped | 12 |
| 17 | on | on | ADP | IN | prep | resting | 16 |
| 18 | a | a | DET | DT | det | tray | 20 |
| 19 | black | black | ADJ | JJ | amod | tray | 20 |
| 20 | tray | tray | NOUN | NN | pobj | on | 17 |
| 21 | with | with | ADP | IN | prep | tray | 20 |
| 22 | a | a | DET | DT | det | doily | 23 |
| 23 | doily | doily | NOUN | NN | pobj | with | 21 |
| 24 | . | . | PUNCT | . | punct | sits | 6 |
| 25 | A | a | DET | DT | det | spoon | 26 |
| 26 | spoon | spoon | NOUN | NN | nsubj | are | 30 |
| 27 | and | and | CCONJ | CC | cc | spoon | 26 |
| 28 | sugar | sugar | NOUN | NN | compound | packet | 29 |
| 29 | packet | packet | NOUN | NN | conj | spoon | 26 |
| 30 | are | be | AUX | VBP | ROOT | are | 30 |
| 31 | beside | beside | ADP | IN | prep | are | 30 |
| 32 | it | it | PRON | PRP | pobj | beside | 31 |
| 33 | , | , | PUNCT | , | punct | are | 30 |
| 34 | with | with | ADP | IN | prep | are | 30 |
| 35 | a | a | DET | DT | det | background | 38 |
| 36 | blurred | blurred | ADJ | JJ | amod | background | 38 |
| 37 | outdoor | outdoor | ADJ | JJ | amod | background | 38 |
| 38 | background | background | NOUN | NN | nsubj | showing | 39 |
| 39 | showing | show | VERB | VBG | pcomp | with | 34 |
| 40 | rocks | rock | NOUN | NNS | dobj | showing | 39 |
| 41 | and | and | CCONJ | CC | cc | rocks | 40 |
| 42 | greenery | greenery | NOUN | NN | conj | rocks | 40 |
| 43 | . | . | PUNCT | . | punct | are | 30 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | glass | glass | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | tall | tall | chunk0 | 1 | size_attribute | high |
| m2 | object | macchiato | macchiato | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | latte | latte | chunk1 | 4 | compound_modifier | medium |
| m4 | object | table | table | chunk2 | 10 | noun_chunk_root | high |
| m5 | attribute | wooden | wooden | chunk2 | 9 | material_attribute | high |
| m6 | object | foam | foam | chunk3 | 14 | noun_chunk_root | high |
| m7 | object | tray | tray | chunk4 | 20 | noun_chunk_root | high |
| m8 | attribute | black | black | chunk4 | 19 | color_attribute | high |
| m9 | object | doily | doily | chunk5 | 23 | noun_chunk_root | high |
| m10 | object | spoon | spoon | chunk6 | 26 | noun_chunk_root | high |
| m11 | object | packet | packet | chunk7 | 29 | noun_chunk_root | high |
| m12 | attribute | sugar | sugar | chunk7 | 28 | compound_modifier | medium |
| m13 | object | it | it | chunk8 | 32 | noun_chunk_root | high |
| m14 | object | background | background | chunk9 | 38 | noun_chunk_root | high |
| m15 | attribute | blurred | blurred | chunk9 | 36 | modifier_attribute | medium |
| m16 | attribute | outdoor | outdoor | chunk9 | 37 | modifier_attribute | medium |
| m17 | object | rocks | rock | chunk10 | 40 | noun_chunk_root | high |
| m18 | object | greenery | greenery | chunk11 | 42 | noun_chunk_root | high |
| m19 | context | outdoor | outdoor | doc | 37 | context_word | medium |
| m20 | context | background | background | doc | 38 | context_word | medium |
| m21 | action | sits | sit | doc | 6 | verb_predicate | high |
| m22 | action | topped | top | doc | 12 | verb_predicate | high |
| m23 | action | resting | rest | doc | 16 | verb_predicate | high |
| m24 | action | showing | show | doc | 39 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> glass |
| e1 | has_attribute | m2 | m3 | medium | chunk1 compound -> macchiato |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> table |
| e3 | has_attribute | m7 | m8 | high | chunk4 amod -> tray |
| e4 | has_attribute | m11 | m12 | medium | chunk7 compound -> packet |
| e5 | has_attribute | m14 | m15 | medium | chunk9 amod -> background |
| e6 | has_attribute | m14 | m16 | medium | chunk9 amod -> background |
| e7 | has_context | scene | m19 | medium | context token outdoor |
| e8 | has_context | scene | m20 | medium | context token background |
| e9 | agent | m21 | m0 | medium | nsubj -> sits |
| e10 | agent | m24 | m20 | medium | nsubj -> showing |
| e11 | patient | m24 | m17 | medium | dobj -> showing |
| e12 | patient | m24 | m18 | medium | dobj -> showing |
| e13 | relation | m0 | m2 | medium | of |
| e14 | relation | m0 | m4 | high | on |
| e15 | relation | m0 | m6 | high | with |
| e16 | relation | m7 | m9 | high | with |
| e17 | relation | m10 | m13 | high | beside |

## 40

**caption_shape:** `multi-sentence`
**caption_id:** `2287af524065dd30ea7e24c23568f4ad086da9db7aa0bc9e9be343f573a60c14`

> A curved brick building with large windows stands on a paved lot. Several cars, including a red one, are parked nearby under a bright sky, with trees and other buildings visible in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| A curved brick building with large windows stands on a paved lot. | 0:13 |
| Several cars, including a red one, are parked nearby under a bright sky, with trees and other buildings visible in the background. | 13:39 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A curved brick building | building | building | nsubj | stands | 0:4 |
| large windows | windows | window | pobj | with | 5:7 |
| a paved lot | lot | lot | pobj | on | 9:12 |
| Several cars | cars | car | nsubjpass | parked | 13:15 |
| a bright sky | sky | sky | pobj | under | 25:28 |
| trees | trees | tree | nsubj | visible | 30:31 |
| other buildings | buildings | building | conj | trees | 32:34 |
| the background | background | background | pobj | in | 36:38 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | building | 3 |
| 1 | curved | curved | ADJ | JJ | amod | building | 3 |
| 2 | brick | brick | NOUN | NN | compound | building | 3 |
| 3 | building | building | NOUN | NN | nsubj | stands | 7 |
| 4 | with | with | ADP | IN | prep | building | 3 |
| 5 | large | large | ADJ | JJ | amod | windows | 6 |
| 6 | windows | window | NOUN | NNS | pobj | with | 4 |
| 7 | stands | stand | VERB | VBZ | ROOT | stands | 7 |
| 8 | on | on | ADP | IN | prep | stands | 7 |
| 9 | a | a | DET | DT | det | lot | 11 |
| 10 | paved | paved | ADJ | JJ | amod | lot | 11 |
| 11 | lot | lot | NOUN | NN | pobj | on | 8 |
| 12 | . | . | PUNCT | . | punct | stands | 7 |
| 13 | Several | several | ADJ | JJ | amod | cars | 14 |
| 14 | cars | car | NOUN | NNS | nsubjpass | parked | 22 |
| 15 | , | , | PUNCT | , | punct | cars | 14 |
| 16 | including | include | VERB | VBG | prep | cars | 14 |
| 17 | a | a | DET | DT | det | one | 19 |
| 18 | red | red | ADJ | JJ | amod | one | 19 |
| 19 | one | one | NUM | CD | pobj | including | 16 |
| 20 | , | , | PUNCT | , | punct | cars | 14 |
| 21 | are | be | AUX | VBP | auxpass | parked | 22 |
| 22 | parked | park | VERB | VBN | ROOT | parked | 22 |
| 23 | nearby | nearby | ADV | RB | advmod | parked | 22 |
| 24 | under | under | ADP | IN | prep | parked | 22 |
| 25 | a | a | DET | DT | det | sky | 27 |
| 26 | bright | bright | ADJ | JJ | amod | sky | 27 |
| 27 | sky | sky | NOUN | NN | pobj | under | 24 |
| 28 | , | , | PUNCT | , | punct | parked | 22 |
| 29 | with | with | SCONJ | IN | mark | visible | 34 |
| 30 | trees | tree | NOUN | NNS | nsubj | visible | 34 |
| 31 | and | and | CCONJ | CC | cc | trees | 30 |
| 32 | other | other | ADJ | JJ | amod | buildings | 33 |
| 33 | buildings | building | NOUN | NNS | conj | trees | 30 |
| 34 | visible | visible | ADJ | JJ | advcl | parked | 22 |
| 35 | in | in | ADP | IN | prep | visible | 34 |
| 36 | the | the | DET | DT | det | background | 37 |
| 37 | background | background | NOUN | NN | pobj | in | 35 |
| 38 | . | . | PUNCT | . | punct | parked | 22 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | chunk0 | 3 | noun_chunk_root | high |
| m1 | attribute | curved | curved | chunk0 | 1 | modifier_attribute | medium |
| m2 | attribute | brick | brick | chunk0 | 2 | material_attribute | high |
| m3 | object | windows | window | chunk1 | 6 | noun_chunk_root | high |
| m4 | attribute | large | large | chunk1 | 5 | size_attribute | high |
| m5 | object | lot | lot | chunk2 | 11 | noun_chunk_root | high |
| m6 | attribute | paved | paved | chunk2 | 10 | visual_attribute | medium |
| m7 | object | cars | car | chunk3 | 14 | noun_chunk_root | high |
| m8 | attribute | Several | several | chunk3 | 13 | modifier_attribute | medium |
| m9 | object | sky | sky | chunk4 | 27 | noun_chunk_root | high |
| m10 | attribute | bright | bright | chunk4 | 26 | visual_attribute | medium |
| m11 | object | trees | tree | chunk5 | 30 | noun_chunk_root | high |
| m12 | object | buildings | building | chunk6 | 33 | noun_chunk_root | high |
| m13 | attribute | other | other | chunk6 | 32 | modifier_attribute | medium |
| m14 | object | background | background | chunk7 | 37 | noun_chunk_root | high |
| m15 | context | background | background | doc | 37 | context_word | medium |
| m16 | action | stands | stand | doc | 7 | verb_predicate | high |
| m17 | action | including | include | doc | 16 | verb_predicate | high |
| m18 | action | parked | park | doc | 22 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> building |
| e1 | has_attribute | m0 | m2 | high | chunk0 compound -> building |
| e2 | has_attribute | m3 | m4 | high | chunk1 amod -> windows |
| e3 | has_attribute | m5 | m6 | medium | chunk2 amod -> lot |
| e4 | has_attribute | m7 | m8 | medium | chunk3 amod -> cars |
| e5 | has_attribute | m9 | m10 | medium | chunk4 amod -> sky |
| e6 | has_attribute | m12 | m13 | medium | chunk6 amod -> buildings |
| e7 | has_context | scene | m15 | medium | context token background |
| e8 | agent | m16 | m0 | medium | nsubj -> stands |
| e9 | agent | m18 | m7 | medium | nsubjpass -> parked |
| e10 | relation | m0 | m3 | high | with |
| e11 | relation | m0 | m5 | high | on |
| e12 | relation | m7 | m9 | high | under |

## 41

**caption_shape:** `multi-sentence`
**caption_id:** `22d73ce6e1983f13f62e0e06d5dac7795e38f3c9f1ff1a64409ea01ab45f4814`

> A man in a blue shirt plays an acoustic guitar while singing into a microphone. He stands on a stage with black curtains behind him and a keyboard visible to his right.

### Sentences
| sentence | token_span |
| --- | --- |
| A man in a blue shirt plays an acoustic guitar while singing into a microphone. | 0:15 |
| He stands on a stage with black curtains behind him and a keyboard visible to his right. | 15:33 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A man | man | man | nsubj | plays | 0:2 |
| a blue shirt | shirt | shirt | pobj | in | 3:6 |
| an acoustic guitar | acoustic guitar | acoustic_guitar | dobj | plays | 7:9 |
| a microphone | microphone | microphone | pobj | into | 12:14 |
| He | He | he | nsubj | stands | 15:16 |
| a stage | stage | stage | pobj | on | 18:20 |
| black curtains | curtains | curtain | pobj | with | 21:23 |
| him | him | he | pobj | behind | 24:25 |
| a keyboard | keyboard | keyboard | conj | curtains | 26:28 |
| his right | right | right | pobj | to | 30:32 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | man | 1 |
| 1 | man | man | NOUN | NN | nsubj | plays | 6 |
| 2 | in | in | ADP | IN | prep | man | 1 |
| 3 | a | a | DET | DT | det | shirt | 5 |
| 4 | blue | blue | ADJ | JJ | amod | shirt | 5 |
| 5 | shirt | shirt | NOUN | NN | pobj | in | 2 |
| 6 | plays | play | VERB | VBZ | ROOT | plays | 6 |
| 7 | an | an | DET | DT | det | acoustic guitar | 8 |
| 8 | acoustic guitar | acoustic_guitar | NOUN | NN | dobj | plays | 6 |
| 9 | while | while | SCONJ | IN | mark | singing | 10 |
| 10 | singing | sing | VERB | VBG | advcl | plays | 6 |
| 11 | into | into | ADP | IN | prep | singing | 10 |
| 12 | a | a | DET | DT | det | microphone | 13 |
| 13 | microphone | microphone | NOUN | NN | pobj | into | 11 |
| 14 | . | . | PUNCT | . | punct | plays | 6 |
| 15 | He | he | PRON | PRP | nsubj | stands | 16 |
| 16 | stands | stand | VERB | VBZ | ROOT | stands | 16 |
| 17 | on | on | ADP | IN | prep | stands | 16 |
| 18 | a | a | DET | DT | det | stage | 19 |
| 19 | stage | stage | NOUN | NN | pobj | on | 17 |
| 20 | with | with | ADP | IN | prep | stands | 16 |
| 21 | black | black | ADJ | JJ | amod | curtains | 22 |
| 22 | curtains | curtain | NOUN | NNS | pobj | with | 20 |
| 23 | behind | behind | ADP | IN | prep | curtains | 22 |
| 24 | him | he | PRON | PRP | pobj | behind | 23 |
| 25 | and | and | CCONJ | CC | cc | curtains | 22 |
| 26 | a | a | DET | DT | det | keyboard | 27 |
| 27 | keyboard | keyboard | NOUN | NN | conj | curtains | 22 |
| 28 | visible | visible | ADJ | JJ | amod | keyboard | 27 |
| 29 | to | to | ADP | IN | prep | visible | 28 |
| 30 | his | his | PRON | PRP$ | poss | right | 31 |
| 31 | right | right | NOUN | NN | pobj | to | 29 |
| 32 | . | . | PUNCT | . | punct | stands | 16 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | shirt | shirt | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | blue | blue | chunk1 | 4 | color_attribute | high |
| m3 | object | acoustic guitar | acoustic_guitar | chunk2 | 8 | noun_chunk_root | high |
| m4 | object | microphone | microphone | chunk3 | 13 | noun_chunk_root | high |
| m5 | object | He | he | chunk4 | 15 | noun_chunk_root | high |
| m6 | object | stage | stage | chunk5 | 19 | noun_chunk_root | high |
| m7 | object | curtains | curtain | chunk6 | 22 | noun_chunk_root | high |
| m8 | attribute | black | black | chunk6 | 21 | color_attribute | high |
| m9 | object | him | he | chunk7 | 24 | noun_chunk_root | high |
| m10 | object | keyboard | keyboard | chunk8 | 27 | noun_chunk_root | high |
| m11 | object | right | right | chunk9 | 31 | noun_chunk_root | high |
| m12 | attribute | his | his | chunk9 | 30 | modifier_attribute | medium |
| m13 | action | plays | play | doc | 6 | verb_predicate | high |
| m14 | action | singing | sing | doc | 10 | verb_predicate | high |
| m15 | action | stands | stand | doc | 16 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> shirt |
| e1 | has_attribute | m7 | m8 | high | chunk6 amod -> curtains |
| e2 | has_attribute | m11 | m12 | medium | chunk9 poss -> right |
| e3 | agent | m13 | m0 | medium | nsubj -> plays |
| e4 | patient | m13 | m3 | medium | dobj -> plays |
| e5 | agent | m15 | m5 | medium | nsubj -> stands |
| e6 | relation | m0 | m1 | high | in |
| e7 | relation | m0 | m4 | medium | into |
| e8 | relation | m5 | m6 | high | on |
| e9 | relation | m5 | m7 | high | with |
| e10 | relation | m5 | m10 | high | with |
| e11 | relation | m7 | m9 | high | behind |

## 42

**caption_shape:** `multi-sentence`
**caption_id:** `24f96a09612e1e5fdd421dc7fc39eeb0c8aaf431c50ed9152c49237f7f98bc14`

> Large rusted metal pipes run diagonally across the frame under a blue sky. Below, green construction fencing and steel rebar are visible, with workers and equipment in the distance. The scene is an outdoor construction site with exposed concrete walls and structural beams.

### Sentences
| sentence | token_span |
| --- | --- |
| Large rusted metal pipes run diagonally across the frame under a blue sky. | 0:14 |
| Below, green construction fencing and steel rebar are visible, with workers and equipment in the distance. | 14:33 |
| The scene is an outdoor construction site with exposed concrete walls and structural beams. | 33:48 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Large rusted metal pipes | pipes | pipe | nsubj | run | 0:4 |
| the frame | frame | frame | pobj | across | 7:9 |
| a blue sky | sky | sky | pobj | under | 10:13 |
| green construction fencing | fencing | fencing | nsubj | are | 16:19 |
| steel rebar | rebar | rebar | conj | fencing | 20:22 |
| the distance | distance | distance | pobj | in | 30:32 |
| The scene | scene | scene | nsubj | is | 33:35 |
| an outdoor construction site | site | site | attr | is | 36:40 |
| exposed concrete walls | walls | wall | pobj | with | 41:44 |
| structural beams | beams | beam | conj | walls | 45:47 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Large | large | ADJ | JJ | amod | pipes | 3 |
| 1 | rusted | rusted | ADJ | JJ | amod | pipes | 3 |
| 2 | metal | metal | NOUN | NN | compound | pipes | 3 |
| 3 | pipes | pipe | NOUN | NNS | nsubj | run | 4 |
| 4 | run | run | VERB | VBP | ROOT | run | 4 |
| 5 | diagonally | diagonally | ADV | RB | advmod | run | 4 |
| 6 | across | across | ADP | IN | prep | run | 4 |
| 7 | the | the | DET | DT | det | frame | 8 |
| 8 | frame | frame | NOUN | NN | pobj | across | 6 |
| 9 | under | under | ADP | IN | prep | run | 4 |
| 10 | a | a | DET | DT | det | sky | 12 |
| 11 | blue | blue | ADJ | JJ | amod | sky | 12 |
| 12 | sky | sky | NOUN | NN | pobj | under | 9 |
| 13 | . | . | PUNCT | . | punct | run | 4 |
| 14 | Below | below | ADV | RB | advmod | are | 22 |
| 15 | , | , | PUNCT | , | punct | are | 22 |
| 16 | green | green | ADJ | JJ | amod | fencing | 18 |
| 17 | construction | construction | NOUN | NN | compound | fencing | 18 |
| 18 | fencing | fencing | NOUN | NN | nsubj | are | 22 |
| 19 | and | and | CCONJ | CC | cc | fencing | 18 |
| 20 | steel | steel | NOUN | NN | compound | rebar | 21 |
| 21 | rebar | rebar | NOUN | NN | conj | fencing | 18 |
| 22 | are | be | AUX | VBP | ROOT | are | 22 |
| 23 | visible | visible | ADJ | JJ | acomp | are | 22 |
| 24 | , | , | PUNCT | , | punct | are | 22 |
| 25 | with | with | SCONJ | IN | mark | workers | 26 |
| 26 | workers | worker | NOUN | NNS | advcl | are | 22 |
| 27 | and | and | CCONJ | CC | cc | workers | 26 |
| 28 | equipment | equipment | NOUN | NN | conj | workers | 26 |
| 29 | in | in | ADP | IN | prep | workers | 26 |
| 30 | the | the | DET | DT | det | distance | 31 |
| 31 | distance | distance | NOUN | NN | pobj | in | 29 |
| 32 | . | . | PUNCT | . | punct | are | 22 |
| 33 | The | the | DET | DT | det | scene | 34 |
| 34 | scene | scene | NOUN | NN | nsubj | is | 35 |
| 35 | is | be | AUX | VBZ | ROOT | is | 35 |
| 36 | an | an | DET | DT | det | site | 39 |
| 37 | outdoor | outdoor | ADJ | JJ | amod | site | 39 |
| 38 | construction | construction | NOUN | NN | compound | site | 39 |
| 39 | site | site | NOUN | NN | attr | is | 35 |
| 40 | with | with | ADP | IN | prep | site | 39 |
| 41 | exposed | expose | VERB | VBN | amod | walls | 43 |
| 42 | concrete | concrete | ADJ | JJ | amod | walls | 43 |
| 43 | walls | wall | NOUN | NNS | pobj | with | 40 |
| 44 | and | and | CCONJ | CC | cc | walls | 43 |
| 45 | structural | structural | ADJ | JJ | amod | beams | 46 |
| 46 | beams | beam | NOUN | NNS | conj | walls | 43 |
| 47 | . | . | PUNCT | . | punct | is | 35 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | pipes | pipe | chunk0 | 3 | noun_chunk_root | high |
| m1 | attribute | Large | large | chunk0 | 0 | size_attribute | high |
| m2 | attribute | rusted | rusted | chunk0 | 1 | modifier_attribute | medium |
| m3 | attribute | metal | metal | chunk0 | 2 | material_attribute | high |
| m4 | object | frame | frame | chunk1 | 8 | noun_chunk_root | high |
| m5 | object | sky | sky | chunk2 | 12 | noun_chunk_root | high |
| m6 | attribute | blue | blue | chunk2 | 11 | color_attribute | high |
| m7 | object | fencing | fencing | chunk3 | 18 | noun_chunk_root | high |
| m8 | attribute | green | green | chunk3 | 16 | color_attribute | high |
| m9 | attribute | construction | construction | chunk3 | 17 | compound_modifier | medium |
| m10 | object | rebar | rebar | chunk4 | 21 | noun_chunk_root | high |
| m11 | attribute | steel | steel | chunk4 | 20 | material_attribute | high |
| m12 | object | distance | distance | chunk5 | 31 | noun_chunk_root | high |
| m13 | object | scene | scene | chunk6 | 34 | noun_chunk_root | high |
| m14 | object | site | site | chunk7 | 39 | noun_chunk_root | high |
| m15 | attribute | outdoor | outdoor | chunk7 | 37 | modifier_attribute | medium |
| m16 | attribute | construction | construction | chunk7 | 38 | compound_modifier | medium |
| m17 | object | walls | wall | chunk8 | 43 | noun_chunk_root | high |
| m18 | attribute | exposed | expose | chunk8 | 41 | state_attribute | medium |
| m19 | attribute | concrete | concrete | chunk8 | 42 | material_attribute | high |
| m20 | object | beams | beam | chunk9 | 46 | noun_chunk_root | high |
| m21 | attribute | structural | structural | chunk9 | 45 | modifier_attribute | medium |
| m22 | context | outdoor | outdoor | doc | 37 | context_word | medium |
| m23 | action | run | run | doc | 4 | verb_predicate | high |
| m24 | object | workers | worker | with_absolute25 | 26 | with_absolute_recovered_object | medium |
| m25 | object | equipment | equipment | with_absolute25 | 28 | with_absolute_recovered_object | medium |

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
| e7 | has_attribute | m14 | m15 | medium | chunk7 amod -> site |
| e8 | has_attribute | m14 | m16 | medium | chunk7 compound -> site |
| e9 | has_attribute | m17 | m18 | medium | chunk8 amod -> walls |
| e10 | has_attribute | m17 | m19 | high | chunk8 amod -> walls |
| e11 | has_attribute | m20 | m21 | medium | chunk9 amod -> beams |
| e12 | has_context | scene | m22 | medium | context token outdoor |
| e13 | agent | m23 | m0 | medium | nsubj -> run |
| e14 | scene_contains | scene | m24 | medium | with_absolute25 recovered workers |
| e15 | scene_contains | scene | m25 | medium | with_absolute25 recovered equipment |
| e16 | relation | m0 | m4 | high | across |
| e17 | relation | m0 | m5 | high | under |
| e18 | relation | m24 | m12 | high | in |
| e19 | relation | m14 | m17 | high | with |
| e20 | relation | m14 | m20 | high | with |

## 43

**caption_shape:** `multi-sentence`
**caption_id:** `257035d6745c0795663db829fc580f78c93e5c49f954babc40906661a92b7414`

> A female soccer player in a black uniform stands on a grass field, preparing to kick a white and black soccer ball. Spectators are visible behind a fence in the background, with trees and an overcast sky above.

### Sentences
| sentence | token_span |
| --- | --- |
| A female soccer player in a black uniform stands on a grass field, preparing to kick a white and black soccer ball. | 0:22 |
| Spectators are visible behind a fence in the background, with trees and an overcast sky above. | 22:40 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| soccer player | soccer player | soccer_player | nsubj | stands | 2:3 |
| a black uniform | uniform | uniform | pobj | in | 4:7 |
| a grass field | field | field | pobj | on | 9:12 |
| a white and black soccer ball | soccer ball | soccer_ball | dobj | kick | 16:21 |
| Spectators | Spectators | spectator | nsubj | are | 22:23 |
| a fence | fence | fence | pobj | behind | 26:28 |
| the background | background | background | pobj | in | 29:31 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | stands | 7 |
| 1 | female | female | ADJ | JJ | amod | stands | 7 |
| 2 | soccer player | soccer_player | NOUN | NN | nsubj | stands | 7 |
| 3 | in | in | ADP | IN | prep | soccer player | 2 |
| 4 | a | a | DET | DT | det | uniform | 6 |
| 5 | black | black | ADJ | JJ | amod | uniform | 6 |
| 6 | uniform | uniform | NOUN | NN | pobj | in | 3 |
| 7 | stands | stand | VERB | VBZ | ROOT | stands | 7 |
| 8 | on | on | ADP | IN | prep | stands | 7 |
| 9 | a | a | DET | DT | det | field | 11 |
| 10 | grass | grass | NOUN | NN | compound | field | 11 |
| 11 | field | field | NOUN | NN | pobj | on | 8 |
| 12 | , | , | PUNCT | , | punct | stands | 7 |
| 13 | preparing | prepare | VERB | VBG | advcl | stands | 7 |
| 14 | to | to | PART | TO | aux | kick | 15 |
| 15 | kick | kick | VERB | VB | xcomp | preparing | 13 |
| 16 | a | a | DET | DT | det | soccer ball | 20 |
| 17 | white | white | ADJ | JJ | amod | soccer ball | 20 |
| 18 | and | and | CCONJ | CC | cc | white | 17 |
| 19 | black | black | ADJ | JJ | conj | white | 17 |
| 20 | soccer ball | soccer_ball | NOUN | NN | dobj | kick | 15 |
| 21 | . | . | PUNCT | . | punct | stands | 7 |
| 22 | Spectators | spectator | NOUN | NNS | nsubj | are | 23 |
| 23 | are | be | AUX | VBP | ROOT | are | 23 |
| 24 | visible | visible | ADJ | JJ | acomp | are | 23 |
| 25 | behind | behind | ADP | IN | prep | are | 23 |
| 26 | a | a | DET | DT | det | fence | 27 |
| 27 | fence | fence | NOUN | NN | pobj | behind | 25 |
| 28 | in | in | ADP | IN | prep | fence | 27 |
| 29 | the | the | DET | DT | det | background | 30 |
| 30 | background | background | NOUN | NN | pobj | in | 28 |
| 31 | , | , | PUNCT | , | punct | are | 23 |
| 32 | with | with | SCONJ | IN | mark | trees | 33 |
| 33 | trees | tree | NOUN | NNS | dep | are | 23 |
| 34 | and | and | CCONJ | CC | cc | trees | 33 |
| 35 | an | an | DET | DT | det | sky | 37 |
| 36 | overcast | overcast | ADJ | JJ | amod | sky | 37 |
| 37 | sky | sky | NOUN | NN | conj | trees | 33 |
| 38 | above | above | ADV | RB | advmod | trees | 33 |
| 39 | . | . | PUNCT | . | punct | are | 23 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | soccer player | soccer_player | chunk0 | 2 | noun_chunk_root | high |
| m1 | object | uniform | uniform | chunk1 | 6 | noun_chunk_root | high |
| m2 | attribute | black | black | chunk1 | 5 | color_attribute | high |
| m3 | object | field | field | chunk2 | 11 | noun_chunk_root | high |
| m4 | attribute | grass | grass | chunk2 | 10 | compound_modifier | medium |
| m5 | object | soccer ball | soccer_ball | chunk3 | 20 | noun_chunk_root | high |
| m6 | attribute | white | white | chunk3 | 17 | color_attribute | high |
| m7 | attribute | black | black | chunk3 | 19 | color_attribute | high |
| m8 | object | Spectators | spectator | chunk4 | 22 | noun_chunk_root | high |
| m9 | object | fence | fence | chunk5 | 27 | noun_chunk_root | high |
| m10 | object | background | background | chunk6 | 30 | noun_chunk_root | high |
| m11 | context | background | background | doc | 30 | context_word | medium |
| m12 | action | stands | stand | doc | 7 | verb_predicate | high |
| m13 | action | preparing | prepare | doc | 13 | verb_predicate | high |
| m14 | action | kick | kick | doc | 15 | verb_predicate | high |
| m15 | object | trees | tree | with_absolute32 | 33 | with_absolute_recovered_object | medium |
| m16 | object | sky | sky | with_absolute32 | 37 | with_absolute_recovered_object | medium |
| m17 | attribute | overcast | overcast | with_absolute32 | 36 | modifier_attribute | medium |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> uniform |
| e1 | has_attribute | m3 | m4 | medium | chunk2 compound -> field |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> soccer ball |
| e3 | has_attribute | m5 | m7 | high | chunk3 conj -> soccer ball |
| e4 | has_context | scene | m11 | medium | context token background |
| e5 | agent | m12 | m0 | medium | nsubj -> stands |
| e6 | patient | m14 | m5 | medium | dobj -> kick |
| e7 | scene_contains | scene | m15 | medium | with_absolute32 recovered trees |
| e8 | scene_contains | scene | m16 | medium | with_absolute32 recovered sky |
| e9 | has_attribute | m16 | m17 | medium | with_absolute32 amod -> sky |
| e10 | relation | m0 | m1 | high | in |
| e11 | relation | m0 | m3 | high | on |
| e12 | relation | m8 | m9 | high | behind |
| e13 | relation | m9 | m11 | high | in |

## 44

**caption_shape:** `multi-sentence`
**caption_id:** `26bf5861cff19fa38f02fc4a87aad03013cd7b1ec644d44ddef69bc384efbc14`

> A young hockey player stands on an ice rink wearing a maroon and white jersey, black shorts, and protective gear. They hold a hockey stick with both hands, positioned in front of them, while looking forward. The yellow wall of the rink is visible in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| A young hockey player stands on an ice rink wearing a maroon and white jersey, black shorts, and protective gear. | 0:21 |
| They hold a hockey stick with both hands, positioned in front of them, while looking forward. | 21:39 |
| The yellow wall of the rink is visible in the background. | 39:51 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| young hockey player | hockey player | hockey_player | nsubj | stands | 1:3 |
| an ice rink | ice rink | ice_rink | pobj | on | 5:7 |
| a maroon and white jersey | jersey | jersey | dobj | wearing | 8:13 |
| black shorts | shorts | short | conj | jersey | 14:16 |
| protective gear | gear | gear | conj | shorts | 18:20 |
| They | They | they | nsubj | hold | 21:22 |
| a hockey stick | hockey stick | hockey_stick | dobj | hold | 23:25 |
| both hands | hands | hand | pobj | with | 26:28 |
| front | front | front | pobj | in | 31:32 |
| them | them | they | pobj | of | 33:34 |
| The yellow wall | wall | wall | nsubj | is | 39:42 |
| the rink | rink | rink | pobj | of | 43:45 |
| the background | background | background | pobj | in | 48:50 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | stands | 3 |
| 1 | young | young | ADJ | JJ | amod | hockey player | 2 |
| 2 | hockey player | hockey_player | NOUN | NN | nsubj | stands | 3 |
| 3 | stands | stand | VERB | VBZ | ROOT | stands | 3 |
| 4 | on | on | ADP | IN | prep | stands | 3 |
| 5 | an | an | DET | DT | det | ice rink | 6 |
| 6 | ice rink | ice_rink | NOUN | NN | pobj | on | 4 |
| 7 | wearing | wear | VERB | VBG | advcl | stands | 3 |
| 8 | a | a | DET | DT | det | jersey | 12 |
| 9 | maroon | maroon | NOUN | NN | nmod | jersey | 12 |
| 10 | and | and | CCONJ | CC | cc | maroon | 9 |
| 11 | white | white | ADJ | JJ | conj | maroon | 9 |
| 12 | jersey | jersey | NOUN | NN | dobj | wearing | 7 |
| 13 | , | , | PUNCT | , | punct | jersey | 12 |
| 14 | black | black | ADJ | JJ | amod | shorts | 15 |
| 15 | shorts | short | NOUN | NNS | conj | jersey | 12 |
| 16 | , | , | PUNCT | , | punct | shorts | 15 |
| 17 | and | and | CCONJ | CC | cc | shorts | 15 |
| 18 | protective | protective | ADJ | JJ | amod | gear | 19 |
| 19 | gear | gear | NOUN | NN | conj | shorts | 15 |
| 20 | . | . | PUNCT | . | punct | stands | 3 |
| 21 | They | they | PRON | PRP | nsubj | hold | 22 |
| 22 | hold | hold | VERB | VBP | ROOT | hold | 22 |
| 23 | a | a | DET | DT | det | hockey stick | 24 |
| 24 | hockey stick | hockey_stick | NOUN | NN | dobj | hold | 22 |
| 25 | with | with | ADP | IN | prep | hold | 22 |
| 26 | both | both | DET | DT | det | hands | 27 |
| 27 | hands | hand | NOUN | NNS | pobj | with | 25 |
| 28 | , | , | PUNCT | , | punct | hold | 22 |
| 29 | positioned | position | VERB | VBN | advcl | hold | 22 |
| 30 | in | in | ADP | IN | prep | positioned | 29 |
| 31 | front | front | NOUN | NN | pobj | in | 30 |
| 32 | of | of | ADP | IN | prep | front | 31 |
| 33 | them | they | PRON | PRP | pobj | of | 32 |
| 34 | , | , | PUNCT | , | punct | positioned | 29 |
| 35 | while | while | SCONJ | IN | mark | looking | 36 |
| 36 | looking | look | VERB | VBG | advcl | positioned | 29 |
| 37 | forward | forward | ADV | RB | advmod | looking | 36 |
| 38 | . | . | PUNCT | . | punct | hold | 22 |
| 39 | The | the | DET | DT | det | wall | 41 |
| 40 | yellow | yellow | ADJ | JJ | amod | wall | 41 |
| 41 | wall | wall | NOUN | NN | nsubj | is | 45 |
| 42 | of | of | ADP | IN | prep | wall | 41 |
| 43 | the | the | DET | DT | det | rink | 44 |
| 44 | rink | rink | NOUN | NN | pobj | of | 42 |
| 45 | is | be | AUX | VBZ | ROOT | is | 45 |
| 46 | visible | visible | ADJ | JJ | acomp | is | 45 |
| 47 | in | in | ADP | IN | prep | is | 45 |
| 48 | the | the | DET | DT | det | background | 49 |
| 49 | background | background | NOUN | NN | pobj | in | 47 |
| 50 | . | . | PUNCT | . | punct | is | 45 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hockey player | hockey_player | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | young | young | chunk0 | 1 | modifier_attribute | medium |
| m2 | object | ice rink | ice_rink | chunk1 | 6 | noun_chunk_root | high |
| m3 | object | jersey | jersey | chunk2 | 12 | noun_chunk_root | high |
| m4 | attribute | maroon | maroon | chunk2 | 9 | color_attribute | high |
| m5 | attribute | white | white | chunk2 | 11 | color_attribute | high |
| m6 | object | shorts | short | chunk3 | 15 | noun_chunk_root | high |
| m7 | attribute | black | black | chunk3 | 14 | color_attribute | high |
| m8 | object | gear | gear | chunk4 | 19 | noun_chunk_root | high |
| m9 | attribute | protective | protective | chunk4 | 18 | modifier_attribute | medium |
| m10 | object | They | they | chunk5 | 21 | noun_chunk_root | high |
| m11 | object | hockey stick | hockey_stick | chunk6 | 24 | noun_chunk_root | high |
| m12 | object | hands | hand | chunk7 | 27 | noun_chunk_root | high |
| m13 | object | them | they | chunk9 | 33 | noun_chunk_root | high |
| m14 | object | wall | wall | chunk10 | 41 | noun_chunk_root | high |
| m15 | attribute | yellow | yellow | chunk10 | 40 | color_attribute | high |
| m16 | object | rink | rink | chunk11 | 44 | noun_chunk_root | high |
| m17 | object | background | background | chunk12 | 49 | noun_chunk_root | high |
| m18 | context | background | background | doc | 49 | context_word | medium |
| m19 | action | stands | stand | doc | 3 | verb_predicate | high |
| m20 | action | wearing | wear | doc | 7 | verb_predicate | high |
| m21 | action | hold | hold | doc | 22 | verb_predicate | high |
| m22 | action | positioned | position | doc | 29 | verb_predicate | high |
| m23 | action | looking | look | doc | 36 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> hockey player |
| e1 | has_attribute | m3 | m4 | high | chunk2 nmod -> jersey |
| e2 | has_attribute | m3 | m5 | high | chunk2 conj -> jersey |
| e3 | has_attribute | m6 | m7 | high | chunk3 amod -> shorts |
| e4 | has_attribute | m8 | m9 | medium | chunk4 amod -> gear |
| e5 | has_attribute | m14 | m15 | high | chunk10 amod -> wall |
| e6 | has_context | scene | m18 | medium | context token background |
| e7 | agent | m19 | m0 | medium | nsubj -> stands |
| e8 | patient | m20 | m3 | medium | dobj -> wearing |
| e9 | patient | m20 | m6 | medium | dobj -> wearing |
| e10 | patient | m20 | m8 | medium | dobj -> wearing |
| e11 | agent | m21 | m10 | medium | nsubj -> hold |
| e12 | patient | m21 | m11 | medium | dobj -> hold |
| e13 | relation | m0 | m2 | high | on |
| e14 | relation | m10 | m12 | high | with |
| e15 | relation | m10 | m13 | high | in_front_of |
| e16 | relation | m14 | m16 | medium | of |
| e17 | relation | m14 | m18 | high | in |

## 45

**caption_shape:** `multi-sentence`
**caption_id:** `26c7740ca0bb561574835f609a8a1cc602f57ba46a5a2e8be20264cbdd9ef814`

> A stone building with arched windows and a decorative spire stands under a clear blue sky. A black streetlamp hangs from the right side of the frame, next to the building’s facade. Flower boxes line the windows on the upper floor.

### Sentences
| sentence | token_span |
| --- | --- |
| A stone building with arched windows and a decorative spire stands under a clear blue sky. | 0:17 |
| A black streetlamp hangs from the right side of the frame, next to the building’s facade. | 17:36 |
| Flower boxes line the windows on the upper floor. | 36:46 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A stone building | building | building | nsubj | stands | 0:3 |
| arched windows | windows | window | pobj | with | 4:6 |
| a decorative spire | spire | spire | conj | windows | 7:10 |
| a clear blue sky | sky | sky | pobj | under | 12:16 |
| A black streetlamp | streetlamp | streetlamp | nsubj | hangs | 17:20 |
| the right side | side | side | pobj | from | 22:25 |
| the frame | frame | frame | pobj | of | 26:28 |
| the building’s facade | facade | facade | pobj | to | 31:35 |
| Flower boxes | boxes | box | nsubj | line | 36:38 |
| the windows | windows | window | dobj | line | 39:41 |
| the upper floor | floor | floor | pobj | on | 42:45 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | building | 2 |
| 1 | stone | stone | NOUN | NN | compound | building | 2 |
| 2 | building | building | NOUN | NN | nsubj | stands | 10 |
| 3 | with | with | ADP | IN | prep | building | 2 |
| 4 | arched | arched | ADJ | JJ | amod | windows | 5 |
| 5 | windows | window | NOUN | NNS | pobj | with | 3 |
| 6 | and | and | CCONJ | CC | cc | windows | 5 |
| 7 | a | a | DET | DT | det | spire | 9 |
| 8 | decorative | decorative | ADJ | JJ | amod | spire | 9 |
| 9 | spire | spire | NOUN | NN | conj | windows | 5 |
| 10 | stands | stand | VERB | VBZ | ROOT | stands | 10 |
| 11 | under | under | ADP | IN | prep | stands | 10 |
| 12 | a | a | DET | DT | det | sky | 15 |
| 13 | clear | clear | ADJ | JJ | amod | blue | 14 |
| 14 | blue | blue | ADJ | JJ | amod | sky | 15 |
| 15 | sky | sky | NOUN | NN | pobj | under | 11 |
| 16 | . | . | PUNCT | . | punct | stands | 10 |
| 17 | A | a | DET | DT | det | streetlamp | 19 |
| 18 | black | black | ADJ | JJ | amod | streetlamp | 19 |
| 19 | streetlamp | streetlamp | NOUN | NN | nsubj | hangs | 20 |
| 20 | hangs | hang | VERB | VBZ | ROOT | hangs | 20 |
| 21 | from | from | ADP | IN | prep | hangs | 20 |
| 22 | the | the | DET | DT | det | side | 24 |
| 23 | right | right | ADJ | JJ | amod | side | 24 |
| 24 | side | side | NOUN | NN | pobj | from | 21 |
| 25 | of | of | ADP | IN | prep | side | 24 |
| 26 | the | the | DET | DT | det | frame | 27 |
| 27 | frame | frame | NOUN | NN | pobj | of | 25 |
| 28 | , | , | PUNCT | , | punct | hangs | 20 |
| 29 | next | next | ADV | RB | advmod | hangs | 20 |
| 30 | to | to | ADP | IN | prep | next | 29 |
| 31 | the | the | DET | DT | det | building | 32 |
| 32 | building | building | NOUN | NN | poss | facade | 34 |
| 33 | ’s | ’s | PART | POS | case | building | 32 |
| 34 | facade | facade | NOUN | NN | pobj | to | 30 |
| 35 | . | . | PUNCT | . | punct | hangs | 20 |
| 36 | Flower | flower | NOUN | NN | compound | boxes | 37 |
| 37 | boxes | box | NOUN | NNS | nsubj | line | 38 |
| 38 | line | line | VERB | VBP | ROOT | line | 38 |
| 39 | the | the | DET | DT | det | windows | 40 |
| 40 | windows | window | NOUN | NNS | dobj | line | 38 |
| 41 | on | on | ADP | IN | prep | windows | 40 |
| 42 | the | the | DET | DT | det | floor | 44 |
| 43 | upper | upper | ADJ | JJ | amod | floor | 44 |
| 44 | floor | floor | NOUN | NN | pobj | on | 41 |
| 45 | . | . | PUNCT | . | punct | line | 38 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | stone | stone | chunk0 | 1 | material_attribute | high |
| m2 | object | windows | window | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | arched | arched | chunk1 | 4 | visual_attribute | medium |
| m4 | object | spire | spire | chunk2 | 9 | noun_chunk_root | high |
| m5 | attribute | decorative | decorative | chunk2 | 8 | modifier_attribute | medium |
| m6 | object | sky | sky | chunk3 | 15 | noun_chunk_root | high |
| m7 | attribute | clear | clear | chunk3 | 13 | visual_attribute | medium |
| m8 | attribute | blue | blue | chunk3 | 14 | color_attribute | high |
| m9 | object | streetlamp | streetlamp | chunk4 | 19 | noun_chunk_root | high |
| m10 | attribute | black | black | chunk4 | 18 | color_attribute | high |
| m11 | object | frame | frame | chunk6 | 27 | noun_chunk_root | high |
| m12 | object | facade | facade | chunk7 | 34 | noun_chunk_root | high |
| m13 | attribute | building | building | chunk7 | 32 | modifier_attribute | medium |
| m14 | object | boxes | box | chunk8 | 37 | noun_chunk_root | high |
| m15 | attribute | Flower | flower | chunk8 | 36 | compound_modifier | medium |
| m16 | object | windows | window | chunk9 | 40 | noun_chunk_root | high |
| m17 | object | floor | floor | chunk10 | 44 | noun_chunk_root | high |
| m18 | attribute | upper | upper | chunk10 | 43 | modifier_attribute | medium |
| m19 | action | stands | stand | doc | 10 | verb_predicate | high |
| m20 | action | hangs | hang | doc | 20 | verb_predicate | high |
| m21 | action | line | line | doc | 38 | verb_predicate | high |

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
| e16 | relation | m9 | m11 | high | from_side_of |
| e17 | relation | m16 | m17 | high | on |

## 46

**caption_shape:** `tag-list-like`
**caption_id:** `2787924a005a3274c2f1298b97e68af52c84f0abb4317613b3d60836705b4c14`

> rusty metal, scrap pile, cornfield, broken pipes, red beam

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | rusty metal | rusty metal | 0:11 |
| t1 | scrap pile | scrap pile | 13:23 |
| t2 | cornfield | cornfield | 25:34 |
| t3 | broken pipes | broken pipes | 36:48 |
| t4 | red beam | red beam | 50:58 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | rusty metal | metal | metal | ROOT | metal | 0:2 | 0:11 |
| t1 | scrap pile | pile | pile | ROOT | pile | 0:2 | 13:23 |
| t2 | cornfield | cornfield | cornfield | ROOT | cornfield | 0:1 | 25:34 |
| t3 | broken pipes | pipes | pipe | ROOT | pipes | 0:2 | 36:48 |
| t4 | red beam | beam | beam | ROOT | beam | 0:2 | 50:58 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | rusty | rusty | ADJ | ADJ | JJ | JJ | amod | metal | 1 | 0:5 |
| t0 | 1 | metal | metal | NOUN | NOUN | NN | NN | ROOT | metal | 1 | 6:11 |
| t1 | 0 | scrap | scrap | NOUN | NOUN | NN | NN | compound | pile | 1 | 13:18 |
| t1 | 1 | pile | pile | NOUN | NOUN | NN | NN | ROOT | pile | 1 | 19:23 |
| t2 | 0 | cornfield | cornfield | PROPN | NOUN | NNP | NN | ROOT | cornfield | 0 | 25:34 |
| t3 | 0 | broken | broken | ADJ | ADJ | JJ | JJ | amod | pipes | 1 | 36:42 |
| t3 | 1 | pipes | pipe | NOUN | NOUN | NNS | NNS | ROOT | pipes | 1 | 43:48 |
| t4 | 0 | red | red | ADJ | ADJ | JJ | JJ | amod | beam | 1 | 50:53 |
| t4 | 1 | beam | beam | NOUN | NOUN | NN | NN | ROOT | beam | 1 | 54:58 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | metal | metal | t0 | 1 | segment_head | high |
| m1 | attribute | rusty | rusty | t0 | 0 | attribute | high |
| m2 | object | pile | pile | t1 | 1 | segment_head | high |
| m3 | attribute | scrap | scrap | t1 | 0 | attribute | high |
| m4 | object | cornfield | cornfield | t2 | 0 | segment_head | high |
| m5 | object | pipes | pipe | t3 | 1 | segment_head | high |
| m6 | attribute | broken | broken | t3 | 0 | attribute | high |
| m7 | object | beam | beam | t4 | 1 | segment_head | high |
| m8 | attribute | red | red | t4 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> metal |
| e1 | has_attribute | m2 | m3 | high | t1 internal compound -> pile |
| e2 | has_attribute | m5 | m6 | high | t3 internal amod -> pipes |
| e3 | has_attribute | m7 | m8 | high | t4 internal amod -> beam |

## 47

**caption_shape:** `multi-sentence`
**caption_id:** `27b9261b58a992423ef196b870b3213354abab3bfcabd4ea4016363cf8e8b814`

> Four people sit at a table during a panel discussion. Behind them, a large screen displays the text “edición, diversidad cultural y desarrollo.” Each person has a microphone and nameplate in front of them.

**parsed_caption:**

> Four people sit at a table during a panel discussion. Behind them, a large screen displays the text “edición, diversidad cultural y desarrollo.” Each person has a microphone and nameplate in front of them.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 27b9261b58a992423ef196b870b3213354abab3bfcabd4ea4016363cf8e8b814:q0 | edición, diversidad cultural y desarrollo. | edición, diversidad cultural y desarrollo. | raw_quote_span | the text | 100:144 | 100:144 |

### Sentences
| sentence | token_span |
| --- | --- |
| Four people sit at a table during a panel discussion. | 0:11 |
| Behind them, a large screen displays the text “edición, diversidad cultural y desarrollo.” Each person has a microphone and nameplate in front of them. | 11:33 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Four people | people | people | nsubj | sit | 0:2 |
| a table | table | table | pobj | at | 4:6 |
| a panel discussion | discussion | discussion | pobj | during | 7:10 |
| them | them | they | pobj | Behind | 12:13 |
| a large screen | screen | screen | nsubj | displays | 14:17 |
| the text | text | text | dobj | displays | 18:20 |
| “edición, diversidad cultural y desarrollo.” | “edición, diversidad cultural y desarrollo.” | edición,_diversidad_cultural_y_desarrollo. | appos | text | 20:21 |
| Each person | person | person | nsubj | has | 21:23 |
| a microphone | microphone | microphone | dobj | has | 24:26 |
| nameplate | nameplate | nameplate | conj | microphone | 27:28 |
| front | front | front | pobj | in | 29:30 |
| them | them | they | pobj | of | 31:32 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Four | four | NUM | CD | nummod | people | 1 |
| 1 | people | people | NOUN | NNS | nsubj | sit | 2 |
| 2 | sit | sit | VERB | VBP | ROOT | sit | 2 |
| 3 | at | at | ADP | IN | prep | sit | 2 |
| 4 | a | a | DET | DT | det | table | 5 |
| 5 | table | table | NOUN | NN | pobj | at | 3 |
| 6 | during | during | ADP | IN | prep | sit | 2 |
| 7 | a | a | DET | DT | det | discussion | 9 |
| 8 | panel | panel | NOUN | NN | compound | discussion | 9 |
| 9 | discussion | discussion | NOUN | NN | pobj | during | 6 |
| 10 | . | . | PUNCT | . | punct | sit | 2 |
| 11 | Behind | behind | ADP | IN | prep | displays | 17 |
| 12 | them | they | PRON | PRP | pobj | Behind | 11 |
| 13 | , | , | PUNCT | , | punct | displays | 17 |
| 14 | a | a | DET | DT | det | screen | 16 |
| 15 | large | large | ADJ | JJ | amod | screen | 16 |
| 16 | screen | screen | NOUN | NN | nsubj | displays | 17 |
| 17 | displays | display | VERB | VBZ | ROOT | displays | 17 |
| 18 | the | the | DET | DT | det | text | 19 |
| 19 | text | text | NOUN | NN | dobj | displays | 17 |
| 20 | “edición, diversidad cultural y desarrollo.” | edición,_diversidad_cultural_y_desarrollo. | NOUN | NN | appos | text | 19 |
| 21 | Each | each | DET | DT | det | person | 22 |
| 22 | person | person | NOUN | NN | nsubj | has | 23 |
| 23 | has | have | VERB | VBZ | ccomp | displays | 17 |
| 24 | a | a | DET | DT | det | microphone | 25 |
| 25 | microphone | microphone | NOUN | NN | dobj | has | 23 |
| 26 | and | and | CCONJ | CC | cc | microphone | 25 |
| 27 | nameplate | nameplate | NOUN | NN | conj | microphone | 25 |
| 28 | in | in | ADP | IN | prep | has | 23 |
| 29 | front | front | NOUN | NN | pobj | in | 28 |
| 30 | of | of | ADP | IN | prep | front | 29 |
| 31 | them | they | PRON | PRP | pobj | of | 30 |
| 32 | . | . | PUNCT | . | punct | has | 23 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Four | four | chunk0 | 0 | quantity | high |
| m2 | object | table | table | chunk1 | 5 | noun_chunk_root | high |
| m3 | object | discussion | discussion | chunk2 | 9 | noun_chunk_root | high |
| m4 | attribute | panel | panel | chunk2 | 8 | compound_modifier | medium |
| m5 | object | them | they | chunk3 | 12 | noun_chunk_root | high |
| m6 | object | screen | screen | chunk4 | 16 | noun_chunk_root | high |
| m7 | attribute | large | large | chunk4 | 15 | size_attribute | high |
| m8 | object | text | text | chunk5 | 19 | noun_chunk_root | high |
| m9 | object | “edición, diversidad cultural y desarrollo.” | edición,_diversidad_cultural_y_desarrollo. | chunk6 | 20 | noun_chunk_root | high |
| m10 | object | person | person | chunk7 | 22 | noun_chunk_root | high |
| m11 | object | microphone | microphone | chunk8 | 25 | noun_chunk_root | high |
| m12 | object | nameplate | nameplate | chunk9 | 27 | noun_chunk_root | high |
| m13 | object | them | they | chunk11 | 31 | noun_chunk_root | high |
| m14 | action | sit | sit | doc | 2 | verb_predicate | high |
| m15 | action | displays | display | doc | 17 | verb_predicate | high |
| m16 | action | has | have | doc | 23 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 nummod -> people |
| e1 | has_attribute | m3 | m4 | medium | chunk2 compound -> discussion |
| e2 | has_attribute | m6 | m7 | high | chunk4 amod -> screen |
| e3 | agent | m14 | m0 | medium | nsubj -> sit |
| e4 | agent | m15 | m6 | medium | nsubj -> displays |
| e5 | patient | m15 | m8 | medium | dobj -> displays |
| e6 | agent | m16 | m10 | medium | nsubj -> has |
| e7 | patient | m16 | m11 | medium | dobj -> has |
| e8 | patient | m16 | m12 | medium | dobj -> has |
| e9 | relation | m0 | m2 | medium | at |
| e10 | relation | m0 | m3 | medium | during |
| e11 | relation | m6 | m5 | high | behind |
| e12 | relation | m10 | m13 | high | in_front_of |

## 48

**caption_shape:** `multi-sentence`
**caption_id:** `2852b9dad94ae23a32a05bfce5ec5c5eea0eef8648c433e1e5464e376cbc9814`

> A man in a tuxedo gives a thumbs-up while holding a trophy on stage. A woman stands beside him, smiling.

### Sentences
| sentence | token_span |
| --- | --- |
| A man in a tuxedo gives a thumbs-up while holding a trophy on stage. | 0:15 |
| A woman stands beside him, smiling. | 15:23 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A man | man | man | nsubj | gives | 0:2 |
| a tuxedo | tuxedo | tuxedo | pobj | in | 3:5 |
| a thumbs-up | thumbs-up | thumbs-up | dobj | gives | 6:8 |
| a trophy | trophy | trophy | dobj | holding | 10:12 |
| stage | stage | stage | pobj | on | 13:14 |
| A woman | woman | woman | nsubj | stands | 15:17 |
| him | him | he | pobj | beside | 19:20 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | man | 1 |
| 1 | man | man | NOUN | NN | nsubj | gives | 5 |
| 2 | in | in | ADP | IN | prep | man | 1 |
| 3 | a | a | DET | DT | det | tuxedo | 4 |
| 4 | tuxedo | tuxedo | NOUN | NN | pobj | in | 2 |
| 5 | gives | give | VERB | VBZ | ROOT | gives | 5 |
| 6 | a | a | DET | DT | det | thumbs-up | 7 |
| 7 | thumbs-up | thumbs-up | NOUN | NNS | dobj | gives | 5 |
| 8 | while | while | SCONJ | IN | mark | holding | 9 |
| 9 | holding | hold | VERB | VBG | advcl | gives | 5 |
| 10 | a | a | DET | DT | det | trophy | 11 |
| 11 | trophy | trophy | NOUN | NN | dobj | holding | 9 |
| 12 | on | on | ADP | IN | prep | holding | 9 |
| 13 | stage | stage | NOUN | NN | pobj | on | 12 |
| 14 | . | . | PUNCT | . | punct | gives | 5 |
| 15 | A | a | DET | DT | det | woman | 16 |
| 16 | woman | woman | NOUN | NN | nsubj | stands | 17 |
| 17 | stands | stand | VERB | VBZ | ROOT | stands | 17 |
| 18 | beside | beside | ADP | IN | prep | stands | 17 |
| 19 | him | he | PRON | PRP | pobj | beside | 18 |
| 20 | , | , | PUNCT | , | punct | stands | 17 |
| 21 | smiling | smile | VERB | VBG | advcl | stands | 17 |
| 22 | . | . | PUNCT | . | punct | stands | 17 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | tuxedo | tuxedo | chunk1 | 4 | noun_chunk_root | high |
| m2 | object | thumbs-up | thumbs-up | chunk2 | 7 | noun_chunk_root | high |
| m3 | object | trophy | trophy | chunk3 | 11 | noun_chunk_root | high |
| m4 | object | stage | stage | chunk4 | 13 | noun_chunk_root | high |
| m5 | object | woman | woman | chunk5 | 16 | noun_chunk_root | high |
| m6 | object | him | he | chunk6 | 19 | noun_chunk_root | high |
| m7 | action | gives | give | doc | 5 | verb_predicate | high |
| m8 | action | holding | hold | doc | 9 | verb_predicate | high |
| m9 | action | stands | stand | doc | 17 | verb_predicate | high |
| m10 | action | smiling | smile | doc | 21 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | agent | m7 | m0 | medium | nsubj -> gives |
| e1 | patient | m7 | m2 | medium | dobj -> gives |
| e2 | patient | m8 | m3 | medium | dobj -> holding |
| e3 | agent | m9 | m5 | medium | nsubj -> stands |
| e4 | relation | m0 | m1 | high | in |
| e5 | relation | m0 | m4 | high | on |
| e6 | relation | m5 | m6 | high | beside |

## 49

**caption_shape:** `multi-sentence`
**caption_id:** `297167f329b8ff2480dda2037bd067eb4f305c39aff064b27927358c36f74814`

> A person wears a black and yellow bicycle helmet with blue sunglasses. The individual is outdoors, with grass and sunlight visible in the background. A date stamp reads “2007/06/09 01:14” in the corner.

**parsed_caption:**

> A person wears a black and yellow bicycle helmet with blue sunglasses. The individual is outdoors, with grass and sunlight visible in the background. A date stamp reads “2007/06/09 01:14” in the corner.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 297167f329b8ff2480dda2037bd067eb4f305c39aff064b27927358c36f74814:q0 | 2007/06/09 01:14 | 2007/06/09 01:14 | raw_quote_span |  | 169:187 | 169:187 |

### Sentences
| sentence | token_span |
| --- | --- |
| A person wears a black and yellow bicycle helmet with blue sunglasses. | 0:12 |
| The individual is outdoors, with grass and sunlight visible in the background. | 12:26 |
| A date stamp reads “2007/06/09 01:14” in the corner. | 26:35 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A person | person | person | nsubj | wears | 0:2 |
| a black and yellow bicycle helmet | bicycle helmet | bicycle_helmet | dobj | wears | 3:8 |
| blue sunglasses | sunglasses | sunglass | pobj | with | 9:11 |
| The individual | individual | individual | nsubj | is | 12:14 |
| grass | grass | grass | nsubj | visible | 18:19 |
| sunlight | sunlight | sunlight | conj | grass | 20:21 |
| the background | background | background | pobj | in | 23:25 |
| A date stamp | stamp | stamp | nsubj | reads | 26:29 |
| the corner | corner | corner | pobj | in | 32:34 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | person | 1 |
| 1 | person | person | NOUN | NN | nsubj | wears | 2 |
| 2 | wears | wear | VERB | VBZ | ROOT | wears | 2 |
| 3 | a | a | DET | DT | det | bicycle helmet | 7 |
| 4 | black | black | ADJ | JJ | amod | bicycle helmet | 7 |
| 5 | and | and | CCONJ | CC | cc | black | 4 |
| 6 | yellow | yellow | ADJ | JJ | conj | black | 4 |
| 7 | bicycle helmet | bicycle_helmet | NOUN | NN | dobj | wears | 2 |
| 8 | with | with | ADP | IN | prep | bicycle helmet | 7 |
| 9 | blue | blue | ADJ | JJ | amod | sunglasses | 10 |
| 10 | sunglasses | sunglass | NOUN | NNS | pobj | with | 8 |
| 11 | . | . | PUNCT | . | punct | wears | 2 |
| 12 | The | the | DET | DT | det | individual | 13 |
| 13 | individual | individual | NOUN | NN | nsubj | is | 14 |
| 14 | is | be | AUX | VBZ | ROOT | is | 14 |
| 15 | outdoors | outdoors | ADV | RB | advmod | is | 14 |
| 16 | , | , | PUNCT | , | punct | is | 14 |
| 17 | with | with | SCONJ | IN | mark | visible | 21 |
| 18 | grass | grass | NOUN | NN | nsubj | visible | 21 |
| 19 | and | and | CCONJ | CC | cc | grass | 18 |
| 20 | sunlight | sunlight | NOUN | NN | conj | grass | 18 |
| 21 | visible | visible | ADJ | JJ | advcl | is | 14 |
| 22 | in | in | ADP | IN | prep | visible | 21 |
| 23 | the | the | DET | DT | det | background | 24 |
| 24 | background | background | NOUN | NN | pobj | in | 22 |
| 25 | . | . | PUNCT | . | punct | is | 14 |
| 26 | A | a | DET | DT | det | stamp | 28 |
| 27 | date | date | NOUN | NN | compound | stamp | 28 |
| 28 | stamp | stamp | NOUN | NN | nsubj | reads | 29 |
| 29 | reads | read | VERB | VBZ | ROOT | reads | 29 |
| 30 | “2007/06/09 01:14” | 2007/06/09_01:14 | NUM | CD | dobj | reads | 29 |
| 31 | in | in | ADP | IN | prep | reads | 29 |
| 32 | the | the | DET | DT | det | corner | 33 |
| 33 | corner | corner | NOUN | NN | pobj | in | 31 |
| 34 | . | . | PUNCT | . | punct | reads | 29 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | person | person | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | bicycle helmet | bicycle_helmet | chunk1 | 7 | noun_chunk_root | high |
| m2 | attribute | black | black | chunk1 | 4 | color_attribute | high |
| m3 | attribute | yellow | yellow | chunk1 | 6 | color_attribute | high |
| m4 | object | sunglasses | sunglass | chunk2 | 10 | noun_chunk_root | high |
| m5 | attribute | blue | blue | chunk2 | 9 | color_attribute | high |
| m6 | object | individual | individual | chunk3 | 13 | noun_chunk_root | high |
| m7 | object | grass | grass | chunk4 | 18 | noun_chunk_root | high |
| m8 | object | sunlight | sunlight | chunk5 | 20 | noun_chunk_root | high |
| m9 | object | background | background | chunk6 | 24 | noun_chunk_root | high |
| m10 | object | stamp | stamp | chunk7 | 28 | noun_chunk_root | high |
| m11 | attribute | date | date | chunk7 | 27 | compound_modifier | medium |
| m12 | object | corner | corner | chunk8 | 33 | noun_chunk_root | high |
| m13 | context | outdoors | outdoors | doc | 15 | context_word | medium |
| m14 | context | background | background | doc | 24 | context_word | medium |
| m15 | action | wears | wear | doc | 2 | verb_predicate | high |
| m16 | action | reads | read | doc | 29 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> bicycle helmet |
| e1 | has_attribute | m1 | m3 | high | chunk1 conj -> bicycle helmet |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> sunglasses |
| e3 | has_attribute | m10 | m11 | medium | chunk7 compound -> stamp |
| e4 | has_context | scene | m13 | medium | context token outdoors |
| e5 | has_context | scene | m14 | medium | context token background |
| e6 | agent | m15 | m0 | medium | nsubj -> wears |
| e7 | patient | m15 | m1 | medium | dobj -> wears |
| e8 | agent | m16 | m10 | medium | nsubj -> reads |
| e9 | relation | m1 | m4 | high | with |
| e10 | relation | m10 | m12 | high | in |

## 50

**caption_shape:** `tag-list-like`
**caption_id:** `2a74cb3297dae2956b9597135736563591d14b31bbc8d75474c9d828d0a15414`

> orange flower, green leaves, blurred background

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | orange flower | orange flower | 0:13 |
| t1 | green leaves | green leaves | 15:27 |
| t2 | blurred background | blurred background | 29:47 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | orange flower | flower | flower | ROOT | flower | 0:2 | 0:13 |
| t1 | green leaves | leaves | leaf | ROOT | leaves | 0:2 | 15:27 |
| t2 | blurred background | background | background | ROOT | background | 0:2 | 29:47 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | orange | orange | ADJ | ADJ | JJ | JJ | amod | flower | 1 | 0:6 |
| t0 | 1 | flower | flower | NOUN | NOUN | NN | NN | ROOT | flower | 1 | 7:13 |
| t1 | 0 | green | green | ADJ | ADJ | JJ | JJ | amod | leaves | 1 | 15:20 |
| t1 | 1 | leaves | leaf | NOUN | NOUN | NNS | NNS | ROOT | leaves | 1 | 21:27 |
| t2 | 0 | blurred | blurred | ADJ | ADJ | JJ | JJ | amod | background | 1 | 29:36 |
| t2 | 1 | background | background | NOUN | NOUN | NN | NN | ROOT | background | 1 | 37:47 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | flower | flower | t0 | 1 | segment_head | high |
| m1 | attribute | orange | orange | t0 | 0 | attribute | high |
| m2 | object | leaves | leaf | t1 | 1 | segment_head | high |
| m3 | attribute | green | green | t1 | 0 | attribute | high |
| m4 | object | background | background | t2 | 1 | segment_head | high |
| m5 | attribute | blurred | blurred | t2 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> flower |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> leaves |
| e2 | has_attribute | m4 | m5 | high | t2 internal amod -> background |

## 51

**caption_shape:** `sentence-like`
**caption_id:** `2a852a207447331ae329e1f42115b77bd23852e22e630f967738b27a9a8ca014`

> A man holds a black umbrella and stands beside a stone sign that reads "MILE 0 VICTORIA BC" in a grassy park.

**parsed_caption:**

> A man holds a black umbrella and stands beside a stone sign that reads "MILE 0 VICTORIA BC" in a grassy park.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 2a852a207447331ae329e1f42115b77bd23852e22e630f967738b27a9a8ca014:q0 | MILE 0 VICTORIA BC | mile 0 victoria bc | raw_quote_span |  | 71:91 | 71:91 |

### Sentences
| sentence | token_span |
| --- | --- |
| A man holds a black umbrella and stands beside a stone sign that reads "MILE 0 VICTORIA BC" in a grassy park. | 0:20 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A man | man | man | nsubj | holds | 0:2 |
| a black umbrella | umbrella | umbrella | dobj | holds | 3:6 |
| a stone sign | sign | sign | pobj | beside | 9:12 |
| that | that | that | nsubj | reads | 12:13 |
| "MILE 0 VICTORIA BC" | "MILE 0 VICTORIA BC" | mile_0_victoria_bc | dobj | reads | 14:15 |
| a grassy park | park | park | pobj | in | 16:19 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | man | 1 |
| 1 | man | man | NOUN | NN | nsubj | holds | 2 |
| 2 | holds | hold | VERB | VBZ | ROOT | holds | 2 |
| 3 | a | a | DET | DT | det | umbrella | 5 |
| 4 | black | black | ADJ | JJ | amod | umbrella | 5 |
| 5 | umbrella | umbrella | NOUN | NN | dobj | holds | 2 |
| 6 | and | and | CCONJ | CC | cc | holds | 2 |
| 7 | stands | stand | VERB | VBZ | conj | holds | 2 |
| 8 | beside | beside | ADP | IN | prep | stands | 7 |
| 9 | a | a | DET | DT | det | sign | 11 |
| 10 | stone | stone | NOUN | NN | compound | sign | 11 |
| 11 | sign | sign | NOUN | NN | pobj | beside | 8 |
| 12 | that | that | PRON | WDT | nsubj | reads | 13 |
| 13 | reads | read | VERB | VBZ | relcl | sign | 11 |
| 14 | "MILE 0 VICTORIA BC" | mile_0_victoria_bc | PROPN | NNP | dobj | reads | 13 |
| 15 | in | in | ADP | IN | prep | stands | 7 |
| 16 | a | a | DET | DT | det | park | 18 |
| 17 | grassy | grassy | ADJ | JJ | amod | park | 18 |
| 18 | park | park | NOUN | NN | pobj | in | 15 |
| 19 | . | . | PUNCT | . | punct | holds | 2 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | umbrella | umbrella | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | black | black | chunk1 | 4 | color_attribute | high |
| m3 | object | sign | sign | chunk2 | 11 | noun_chunk_root | high |
| m4 | attribute | stone | stone | chunk2 | 10 | material_attribute | high |
| m5 | object | that | that | chunk3 | 12 | noun_chunk_root | high |
| m6 | object | "MILE 0 VICTORIA BC" | mile_0_victoria_bc | chunk4 | 14 | noun_chunk_root | high |
| m7 | object | park | park | chunk5 | 18 | noun_chunk_root | high |
| m8 | attribute | grassy | grassy | chunk5 | 17 | modifier_attribute | medium |
| m9 | action | holds | hold | doc | 2 | verb_predicate | high |
| m10 | action | stands | stand | doc | 7 | verb_predicate | high |
| m11 | action | reads | read | doc | 13 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> umbrella |
| e1 | has_attribute | m3 | m4 | high | chunk2 compound -> sign |
| e2 | has_attribute | m7 | m8 | medium | chunk5 amod -> park |
| e3 | agent | m9 | m0 | medium | nsubj -> holds |
| e4 | patient | m9 | m1 | medium | dobj -> holds |
| e5 | agent | m11 | m5 | medium | nsubj -> reads |
| e6 | patient | m11 | m6 | medium | dobj -> reads |
| e7 | relation | m0 | m3 | high | beside |
| e8 | relation | m0 | m7 | high | in |

## 52

**caption_shape:** `multi-sentence`
**caption_id:** `2abf634f1e2fadbc15793d84fb42b2c069992fa23cafc566cc5be2e943246814`

> A boy in a yellow jersey kicks a soccer ball on a green field. Another player in a white jersey with the number 10 runs nearby, while other children and adults are visible in the background near a fence and building.

### Sentences
| sentence | token_span |
| --- | --- |
| A boy in a yellow jersey kicks a soccer ball on a green field. | 0:14 |
| Another player in a white jersey with the number 10 runs nearby, while other children and adults are visible in the background near a fence and building. | 14:43 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A boy | boy | boy | nsubj | kicks | 0:2 |
| a yellow jersey | jersey | jersey | pobj | in | 3:6 |
| a soccer ball | soccer ball | soccer_ball | dobj | kicks | 7:9 |
| a green field | field | field | pobj | on | 10:13 |
| Another player | player | player | nsubj | runs | 14:16 |
| a white jersey | jersey | jersey | pobj | in | 17:20 |
| the number | number | number | pobj | with | 21:23 |
| other children | children | child | nsubj | are | 28:30 |
| adults | adults | adult | conj | children | 31:32 |
| the background | background | background | pobj | in | 35:37 |
| a fence | fence | fence | pobj | near | 38:40 |
| building | building | building | conj | fence | 41:42 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | boy | 1 |
| 1 | boy | boy | NOUN | NN | nsubj | kicks | 6 |
| 2 | in | in | ADP | IN | prep | boy | 1 |
| 3 | a | a | DET | DT | det | jersey | 5 |
| 4 | yellow | yellow | ADJ | JJ | amod | jersey | 5 |
| 5 | jersey | jersey | NOUN | NN | pobj | in | 2 |
| 6 | kicks | kick | VERB | VBZ | ROOT | kicks | 6 |
| 7 | a | a | DET | DT | det | soccer ball | 8 |
| 8 | soccer ball | soccer_ball | NOUN | NN | dobj | kicks | 6 |
| 9 | on | on | ADP | IN | prep | kicks | 6 |
| 10 | a | a | DET | DT | det | field | 12 |
| 11 | green | green | ADJ | JJ | amod | field | 12 |
| 12 | field | field | NOUN | NN | pobj | on | 9 |
| 13 | . | . | PUNCT | . | punct | kicks | 6 |
| 14 | Another | another | DET | DT | det | player | 15 |
| 15 | player | player | NOUN | NN | nsubj | runs | 24 |
| 16 | in | in | ADP | IN | prep | player | 15 |
| 17 | a | a | DET | DT | det | jersey | 19 |
| 18 | white | white | ADJ | JJ | amod | jersey | 19 |
| 19 | jersey | jersey | NOUN | NN | pobj | in | 16 |
| 20 | with | with | ADP | IN | prep | jersey | 19 |
| 21 | the | the | DET | DT | det | number | 22 |
| 22 | number | number | NOUN | NN | pobj | with | 20 |
| 23 | 10 | 10 | NUM | CD | nummod | number | 22 |
| 24 | runs | run | VERB | VBZ | ROOT | runs | 24 |
| 25 | nearby | nearby | ADV | RB | advmod | runs | 24 |
| 26 | , | , | PUNCT | , | punct | runs | 24 |
| 27 | while | while | SCONJ | IN | mark | are | 32 |
| 28 | other | other | ADJ | JJ | amod | children | 29 |
| 29 | children | child | NOUN | NNS | nsubj | are | 32 |
| 30 | and | and | CCONJ | CC | cc | children | 29 |
| 31 | adults | adult | NOUN | NNS | conj | children | 29 |
| 32 | are | be | AUX | VBP | advcl | runs | 24 |
| 33 | visible | visible | ADJ | JJ | acomp | are | 32 |
| 34 | in | in | ADP | IN | prep | are | 32 |
| 35 | the | the | DET | DT | det | background | 36 |
| 36 | background | background | NOUN | NN | pobj | in | 34 |
| 37 | near | near | ADP | IN | prep | are | 32 |
| 38 | a | a | DET | DT | det | fence | 39 |
| 39 | fence | fence | NOUN | NN | pobj | near | 37 |
| 40 | and | and | CCONJ | CC | cc | fence | 39 |
| 41 | building | building | NOUN | NN | conj | fence | 39 |
| 42 | . | . | PUNCT | . | punct | runs | 24 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | boy | boy | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | jersey | jersey | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | yellow | yellow | chunk1 | 4 | color_attribute | high |
| m3 | object | soccer ball | soccer_ball | chunk2 | 8 | noun_chunk_root | high |
| m4 | object | field | field | chunk3 | 12 | noun_chunk_root | high |
| m5 | attribute | green | green | chunk3 | 11 | color_attribute | high |
| m6 | object | player | player | chunk4 | 15 | noun_chunk_root | high |
| m7 | object | jersey | jersey | chunk5 | 19 | noun_chunk_root | high |
| m8 | attribute | white | white | chunk5 | 18 | color_attribute | high |
| m9 | object | number | number | chunk6 | 22 | noun_chunk_root | high |
| m10 | object | children | child | chunk7 | 29 | noun_chunk_root | high |
| m11 | attribute | other | other | chunk7 | 28 | modifier_attribute | medium |
| m12 | object | adults | adult | chunk8 | 31 | noun_chunk_root | high |
| m13 | object | background | background | chunk9 | 36 | noun_chunk_root | high |
| m14 | object | fence | fence | chunk10 | 39 | noun_chunk_root | high |
| m15 | object | building | building | chunk11 | 41 | noun_chunk_root | high |
| m16 | context | background | background | doc | 36 | context_word | medium |
| m17 | action | kicks | kick | doc | 6 | verb_predicate | high |
| m18 | action | runs | run | doc | 24 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> jersey |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> field |
| e2 | has_attribute | m7 | m8 | high | chunk5 amod -> jersey |
| e3 | has_attribute | m10 | m11 | medium | chunk7 amod -> children |
| e4 | has_context | scene | m16 | medium | context token background |
| e5 | agent | m17 | m0 | medium | nsubj -> kicks |
| e6 | patient | m17 | m3 | medium | dobj -> kicks |
| e7 | agent | m18 | m6 | medium | nsubj -> runs |
| e8 | relation | m0 | m1 | high | in |
| e9 | relation | m0 | m4 | high | on |
| e10 | relation | m6 | m7 | high | in |
| e11 | relation | m7 | m9 | high | with |
| e12 | relation | m10 | m16 | high | in |
| e13 | relation | m10 | m14 | high | near |
| e14 | relation | m10 | m15 | high | near |

## 53

**caption_shape:** `tag-list-like`
**caption_id:** `2cd35fda2e263d175868d6361038cddb75310861b6ff222d7924305a5e347c14`

> green balloons, yellow balloons, party decor

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | green balloons | green balloons | 0:14 |
| t1 | yellow balloons | yellow balloons | 16:31 |
| t2 | party decor | party decor | 33:44 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | green balloons | balloons | balloon | ROOT | balloons | 0:2 | 0:14 |
| t1 | yellow balloons | balloons | balloon | ROOT | balloons | 0:2 | 16:31 |
| t2 | party decor | decor | decor | ROOT | decor | 0:2 | 33:44 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | green | green | ADJ | ADJ | JJ | JJ | amod | balloons | 1 | 0:5 |
| t0 | 1 | balloons | balloon | NOUN | NOUN | NNS | NNS | ROOT | balloons | 1 | 6:14 |
| t1 | 0 | yellow | yellow | ADJ | ADJ | JJ | JJ | amod | balloons | 1 | 16:22 |
| t1 | 1 | balloons | balloon | NOUN | NOUN | NNS | NNS | ROOT | balloons | 1 | 23:31 |
| t2 | 0 | party | party | NOUN | NOUN | NN | NN | compound | decor | 1 | 33:38 |
| t2 | 1 | decor | decor | NOUN | NOUN | NN | NN | ROOT | decor | 1 | 39:44 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | balloons | balloon | t0 | 1 | segment_head | high |
| m1 | attribute | green | green | t0 | 0 | attribute | high |
| m2 | object | balloons | balloon | t1 | 1 | segment_head | high |
| m3 | attribute | yellow | yellow | t1 | 0 | attribute | high |
| m4 | object | decor | decor | t2 | 1 | segment_head | high |
| m5 | attribute | party | party | t2 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> balloons |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> balloons |
| e2 | has_attribute | m4 | m5 | high | t2 internal compound -> decor |

## 54

**caption_shape:** `tag-list-like`
**caption_id:** `2dfa309f889152f451bddf6323a66c94e8d9d743da86609cddd26af1ccd00c14`

> glass lamp, black and white, reflective surface, cracked glass, bulb

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | glass lamp | glass lamp | 0:10 |
| t1 | black and white | black and white | 12:27 |
| t2 | reflective surface | reflective surface | 29:47 |
| t3 | cracked glass | cracked glass | 49:62 |
| t4 | bulb | bulb | 64:68 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | glass lamp | lamp | lamp | ROOT | lamp | 0:2 | 0:10 |
| t1 | white | white | white | conj | black | 2:3 | 22:27 |
| t2 | reflective surface | surface | surface | ROOT | surface | 0:2 | 29:47 |
| t3 | cracked glass | glass | glass | ROOT | glass | 0:2 | 49:62 |
| t4 | bulb | bulb | bulb | ROOT | bulb | 0:1 | 64:68 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | glass | glass | NOUN | NOUN | NN | NN | compound | lamp | 1 | 0:5 |
| t0 | 1 | lamp | lamp | NOUN | NOUN | NN | NN | ROOT | lamp | 1 | 6:10 |
| t1 | 0 | black | black | ADJ | ADJ | JJ | JJ | ROOT | black | 0 | 12:17 |
| t1 | 1 | and | and | CCONJ | CCONJ | CC | CC | cc | black | 0 | 18:21 |
| t1 | 2 | white | white | NOUN | ADJ | NN | JJ | conj | black | 0 | 22:27 |
| t2 | 0 | reflective | reflective | ADJ | ADJ | JJ | JJ | amod | surface | 1 | 29:39 |
| t2 | 1 | surface | surface | NOUN | NOUN | NN | NN | ROOT | surface | 1 | 40:47 |
| t3 | 0 | cracked | crack | VERB | ADJ | VBN | VBN | amod | glass | 1 | 49:56 |
| t3 | 1 | glass | glass | NOUN | NOUN | NN | NN | ROOT | glass | 1 | 57:62 |
| t4 | 0 | bulb | bulb | NOUN | NOUN | NN | NN | ROOT | bulb | 0 | 64:68 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | lamp | lamp | t0 | 1 | segment_head | high |
| m1 | attribute | glass | glass | t0 | 0 | attribute | high |
| m2 | object | white | white | t1 | 2 | segment_head | high |
| m3 | attribute | black | black | t1 | 0 | attribute | high |
| m4 | object | surface | surface | t2 | 1 | segment_head | high |
| m5 | attribute | reflective | reflective | t2 | 0 | attribute | high |
| m6 | object | glass | glass | t3 | 1 | segment_head | high |
| m7 | attribute | cracked | crack | t3 | 0 | state_attribute | high |
| m8 | object | bulb | bulb | t4 | 0 | segment_head | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> lamp |
| e1 | has_attribute | m2 | m3 | high | t1 internal ROOT -> white |
| e2 | has_attribute | m4 | m5 | high | t2 internal amod -> surface |
| e3 | has_attribute | m6 | m7 | high | t3 internal amod -> glass |

## 55

**caption_shape:** `multi-sentence`
**caption_id:** `2e4e7755258469126a5cba139a7f39e0d9ea63233ac4a7cae2d43cde2adb7c14`

> A Mercedes-Benz building with several cars parked in front. Blue pillars and glass windows are visible.

### Sentences
| sentence | token_span |
| --- | --- |
| A Mercedes-Benz building with several cars parked in front. | 0:10 |
| Blue pillars and glass windows are visible. | 10:18 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A Mercedes-Benz building | building | building | ROOT | building | 0:3 |
| several cars | cars | car | pobj | with | 4:6 |
| front | front | front | pobj | in | 8:9 |
| Blue pillars | pillars | pillar | nsubj | are | 10:12 |
| glass windows | windows | window | conj | pillars | 13:15 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | building | 2 |
| 1 | Mercedes-Benz | Mercedes-Benz | PROPN | NNP | compound | building | 2 |
| 2 | building | building | NOUN | NN | ROOT | building | 2 |
| 3 | with | with | ADP | IN | prep | building | 2 |
| 4 | several | several | ADJ | JJ | amod | cars | 5 |
| 5 | cars | car | NOUN | NNS | pobj | with | 3 |
| 6 | parked | park | VERB | VBN | acl | cars | 5 |
| 7 | in | in | ADP | IN | prep | parked | 6 |
| 8 | front | front | NOUN | NN | pobj | in | 7 |
| 9 | . | . | PUNCT | . | punct | building | 2 |
| 10 | Blue | blue | ADJ | JJ | amod | pillars | 11 |
| 11 | pillars | pillar | NOUN | NNS | nsubj | are | 15 |
| 12 | and | and | CCONJ | CC | cc | pillars | 11 |
| 13 | glass | glass | NOUN | NN | compound | windows | 14 |
| 14 | windows | window | NOUN | NNS | conj | pillars | 11 |
| 15 | are | be | AUX | VBP | ROOT | are | 15 |
| 16 | visible | visible | ADJ | JJ | acomp | are | 15 |
| 17 | . | . | PUNCT | . | punct | are | 15 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | Mercedes-Benz | mercedes-benz | chunk0 | 1 | compound_modifier | medium |
| m2 | object | cars | car | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | several | several | chunk1 | 4 | modifier_attribute | medium |
| m4 | context | front | front | chunk2 | 8 | spatial_region | medium |
| m5 | object | pillars | pillar | chunk3 | 11 | noun_chunk_root | high |
| m6 | attribute | Blue | blue | chunk3 | 10 | color_attribute | high |
| m7 | object | windows | window | chunk4 | 14 | noun_chunk_root | high |
| m8 | attribute | glass | glass | chunk4 | 13 | material_attribute | high |
| m9 | action | parked | park | doc | 6 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 compound -> building |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> cars |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> pillars |
| e3 | has_attribute | m7 | m8 | high | chunk4 compound -> windows |
| e4 | relation | m0 | m2 | high | with |
| e5 | relation | m2 | m4 | high | in |

## 56

**caption_shape:** `multi-sentence`
**caption_id:** `2e7e96b37fb008c7a81a490d20b0e27c614469755665c93183a59dff62163014`

> Green fields and trees stretch across a valley under a cloudy sky. Pine trees frame the foreground.

### Sentences
| sentence | token_span |
| --- | --- |
| Green fields and trees stretch across a valley under a cloudy sky. | 0:13 |
| Pine trees frame the foreground. | 13:18 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Green fields | fields | field | nsubj | stretch | 0:2 |
| trees | trees | tree | conj | fields | 3:4 |
| a valley | valley | valley | pobj | across | 6:8 |
| a cloudy sky | sky | sky | pobj | under | 9:12 |
| Pine trees | Pine trees | pine_tree | nsubj | frame | 13:14 |
| the foreground | foreground | foreground | dobj | frame | 15:17 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Green | green | ADJ | JJ | amod | fields | 1 |
| 1 | fields | field | NOUN | NNS | nsubj | stretch | 4 |
| 2 | and | and | CCONJ | CC | cc | fields | 1 |
| 3 | trees | tree | NOUN | NNS | conj | fields | 1 |
| 4 | stretch | stretch | VERB | VBP | ROOT | stretch | 4 |
| 5 | across | across | ADP | IN | prep | stretch | 4 |
| 6 | a | a | DET | DT | det | valley | 7 |
| 7 | valley | valley | NOUN | NN | pobj | across | 5 |
| 8 | under | under | ADP | IN | prep | stretch | 4 |
| 9 | a | a | DET | DT | det | sky | 11 |
| 10 | cloudy | cloudy | ADJ | JJ | amod | sky | 11 |
| 11 | sky | sky | NOUN | NN | pobj | under | 8 |
| 12 | . | . | PUNCT | . | punct | stretch | 4 |
| 13 | Pine trees | pine_tree | NOUN | NN | nsubj | frame | 14 |
| 14 | frame | frame | VERB | VBP | ROOT | frame | 14 |
| 15 | the | the | DET | DT | det | foreground | 16 |
| 16 | foreground | foreground | NOUN | NN | dobj | frame | 14 |
| 17 | . | . | PUNCT | . | punct | frame | 14 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | fields | field | chunk0 | 1 | noun_chunk_root | high |
| m1 | attribute | Green | green | chunk0 | 0 | color_attribute | high |
| m2 | object | trees | tree | chunk1 | 3 | noun_chunk_root | high |
| m3 | object | valley | valley | chunk2 | 7 | noun_chunk_root | high |
| m4 | object | sky | sky | chunk3 | 11 | noun_chunk_root | high |
| m5 | attribute | cloudy | cloudy | chunk3 | 10 | modifier_attribute | medium |
| m6 | object | Pine trees | pine_tree | chunk4 | 13 | noun_chunk_root | high |
| m7 | object | foreground | foreground | chunk5 | 16 | noun_chunk_root | high |
| m8 | context | foreground | foreground | doc | 16 | context_word | medium |
| m9 | action | stretch | stretch | doc | 4 | verb_predicate | high |
| m10 | action | frame | frame | doc | 14 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> fields |
| e1 | has_attribute | m4 | m5 | medium | chunk3 amod -> sky |
| e2 | has_context | scene | m8 | medium | context token foreground |
| e3 | agent | m9 | m0 | medium | nsubj -> stretch |
| e4 | agent | m9 | m2 | medium | nsubj -> stretch |
| e5 | agent | m10 | m6 | medium | nsubj -> frame |
| e6 | patient | m10 | m8 | medium | dobj -> frame |
| e7 | relation | m0 | m3 | high | across |
| e8 | relation | m0 | m4 | high | under |

## 57

**caption_shape:** `multi-sentence`
**caption_id:** `2f1810981f1e7a25986b6d3d1b18205489e3d0812d69ac51e9f4121a83be3814`

> A small, weathered orange-brown artifact with a rounded top and flat base rests on a white surface. Below it, a scale marker reads "50 mm," indicating its size. The object appears to be an ancient or archaeological fragment.

**parsed_caption:**

> A small, weathered orange-brown artifact with a rounded top and flat base rests on a white surface. Below it, a scale marker reads "50 mm," indicating its size. The object appears to be an ancient or archaeological fragment.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 2f1810981f1e7a25986b6d3d1b18205489e3d0812d69ac51e9f4121a83be3814:q0 | 50 mm, | 50 mm, | raw_quote_span |  | 131:139 | 131:139 |

### Sentences
| sentence | token_span |
| --- | --- |
| A small, weathered orange-brown artifact with a rounded top and flat base rests on a white surface. | 0:19 |
| Below it, a scale marker reads "50 mm," indicating its size. | 19:31 |
| The object appears to be an ancient or archaeological fragment. | 31:42 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A small, weathered orange-brown artifact | artifact | artifact | nsubj | rests | 0:6 |
| a rounded top | top | top | pobj | with | 7:10 |
| flat base | base | base | conj | top | 11:13 |
| a white surface | surface | surface | pobj | on | 15:18 |
| it | it | it | pobj | Below | 20:21 |
| a scale marker | marker | marker | nsubj | reads | 22:25 |
| its size | size | size | dobj | indicating | 28:30 |
| The object | object | object | nsubj | appears | 31:33 |
| an ancient or archaeological fragment | fragment | fragment | attr | be | 36:41 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | artifact | 5 |
| 1 | small | small | ADJ | JJ | amod | artifact | 5 |
| 2 | , | , | PUNCT | , | punct | artifact | 5 |
| 3 | weathered | weathered | ADJ | JJ | amod | artifact | 5 |
| 4 | orange-brown | orange-brown | ADJ | JJ | amod | artifact | 5 |
| 5 | artifact | artifact | NOUN | NN | nsubj | rests | 13 |
| 6 | with | with | ADP | IN | prep | artifact | 5 |
| 7 | a | a | DET | DT | det | top | 9 |
| 8 | rounded | rounded | ADJ | JJ | amod | top | 9 |
| 9 | top | top | NOUN | NN | pobj | with | 6 |
| 10 | and | and | CCONJ | CC | cc | top | 9 |
| 11 | flat | flat | ADJ | JJ | amod | base | 12 |
| 12 | base | base | NOUN | NN | conj | top | 9 |
| 13 | rests | rest | VERB | VBZ | ROOT | rests | 13 |
| 14 | on | on | ADP | IN | prep | rests | 13 |
| 15 | a | a | DET | DT | det | surface | 17 |
| 16 | white | white | ADJ | JJ | amod | surface | 17 |
| 17 | surface | surface | NOUN | NN | pobj | on | 14 |
| 18 | . | . | PUNCT | . | punct | rests | 13 |
| 19 | Below | below | ADP | IN | prep | reads | 25 |
| 20 | it | it | PRON | PRP | pobj | Below | 19 |
| 21 | , | , | PUNCT | , | punct | reads | 25 |
| 22 | a | a | DET | DT | det | marker | 24 |
| 23 | scale | scale | NOUN | NN | compound | marker | 24 |
| 24 | marker | marker | NOUN | NN | nsubj | reads | 25 |
| 25 | reads | read | VERB | VBZ | ROOT | reads | 25 |
| 26 | "50 mm," | 50_mm, | NUM | CD | punct | reads | 25 |
| 27 | indicating | indicate | VERB | VBG | advcl | reads | 25 |
| 28 | its | its | PRON | PRP$ | poss | size | 29 |
| 29 | size | size | NOUN | NN | dobj | indicating | 27 |
| 30 | . | . | PUNCT | . | punct | reads | 25 |
| 31 | The | the | DET | DT | det | object | 32 |
| 32 | object | object | NOUN | NN | nsubj | appears | 33 |
| 33 | appears | appear | VERB | VBZ | ROOT | appears | 33 |
| 34 | to | to | PART | TO | aux | be | 35 |
| 35 | be | be | AUX | VB | xcomp | appears | 33 |
| 36 | an | an | DET | DT | det | fragment | 40 |
| 37 | ancient | ancient | ADJ | JJ | amod | fragment | 40 |
| 38 | or | or | CCONJ | CC | cc | ancient | 37 |
| 39 | archaeological | archaeological | ADJ | JJ | conj | ancient | 37 |
| 40 | fragment | fragment | NOUN | NN | attr | be | 35 |
| 41 | . | . | PUNCT | . | punct | appears | 33 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | artifact | artifact | chunk0 | 5 | noun_chunk_root | high |
| m1 | attribute | small | small | chunk0 | 1 | size_attribute | high |
| m2 | attribute | weathered | weathered | chunk0 | 3 | modifier_attribute | medium |
| m3 | attribute | orange-brown | orange-brown | chunk0 | 4 | modifier_attribute | medium |
| m4 | context | top | top | chunk1 | 9 | spatial_region | medium |
| m5 | object | base | base | chunk2 | 12 | noun_chunk_root | high |
| m6 | attribute | flat | flat | chunk2 | 11 | modifier_attribute | medium |
| m7 | object | surface | surface | chunk3 | 17 | noun_chunk_root | high |
| m8 | attribute | white | white | chunk3 | 16 | color_attribute | high |
| m9 | object | it | it | chunk4 | 20 | noun_chunk_root | high |
| m10 | object | marker | marker | chunk5 | 24 | noun_chunk_root | high |
| m11 | attribute | scale | scale | chunk5 | 23 | compound_modifier | medium |
| m12 | object | size | size | chunk6 | 29 | noun_chunk_root | high |
| m13 | attribute | its | its | chunk6 | 28 | modifier_attribute | medium |
| m14 | object | object | object | chunk7 | 32 | noun_chunk_root | high |
| m15 | object | fragment | fragment | chunk8 | 40 | noun_chunk_root | high |
| m16 | attribute | ancient | ancient | chunk8 | 37 | modifier_attribute | medium |
| m17 | attribute | archaeological | archaeological | chunk8 | 39 | modifier_attribute | medium |
| m18 | action | rests | rest | doc | 13 | verb_predicate | high |
| m19 | action | reads | read | doc | 25 | verb_predicate | high |
| m20 | action | indicating | indicate | doc | 27 | verb_predicate | high |
| m21 | action | appears | appear | doc | 33 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> artifact |
| e1 | has_attribute | m0 | m2 | medium | chunk0 amod -> artifact |
| e2 | has_attribute | m0 | m3 | medium | chunk0 amod -> artifact |
| e3 | has_attribute | m5 | m6 | medium | chunk2 amod -> base |
| e4 | has_attribute | m7 | m8 | high | chunk3 amod -> surface |
| e5 | has_attribute | m10 | m11 | medium | chunk5 compound -> marker |
| e6 | has_attribute | m12 | m13 | medium | chunk6 poss -> size |
| e7 | has_attribute | m15 | m16 | medium | chunk8 amod -> fragment |
| e8 | has_attribute | m15 | m17 | medium | chunk8 conj -> fragment |
| e9 | agent | m18 | m0 | medium | nsubj -> rests |
| e10 | agent | m19 | m10 | medium | nsubj -> reads |
| e11 | patient | m20 | m12 | medium | dobj -> indicating |
| e12 | agent | m21 | m14 | medium | nsubj -> appears |
| e13 | relation | m0 | m4 | high | with |
| e14 | relation | m0 | m5 | high | with |
| e15 | relation | m0 | m7 | high | on |
| e16 | relation | m10 | m9 | high | below |

## 58

**caption_shape:** `multi-sentence`
**caption_id:** `2f295fa7a4dda24b537ab1663d4e055c2255d51e5b9d545e3e0b84827872d414`

> Tall trees with rough bark stand in a forest clearing, their branches filtering sunlight onto the ground. Green bushes and dry leaves cover the forest floor, with dappled light creating bright spots among the shadows. The scene is quiet and natural, surrounded by dense woodland.

### Sentences
| sentence | token_span |
| --- | --- |
| Tall trees with rough bark stand in a forest clearing, their branches filtering sunlight onto the ground. | 0:19 |
| Green bushes and dry leaves cover the forest floor, with dappled light creating bright spots among the shadows. | 19:39 |
| The scene is quiet and natural, surrounded by dense woodland. | 39:51 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Tall trees | trees | tree | nsubj | stand | 0:2 |
| rough bark | bark | bark | pobj | with | 3:5 |
| a forest clearing | clearing | clearing | pobj | in | 7:10 |
| their branches | branches | branch | nsubj | filtering | 11:13 |
| sunlight | sunlight | sunlight | dobj | filtering | 14:15 |
| the ground | ground | ground | pobj | onto | 16:18 |
| Green bushes | bushes | bush | nsubj | cover | 19:21 |
| dry leaves | leaves | leaf | conj | bushes | 22:24 |
| the forest floor | floor | floor | dobj | cover | 25:28 |
| dappled light | light | light | nsubj | creating | 30:32 |
| bright spots | spots | spot | dobj | creating | 33:35 |
| the shadows | shadows | shadow | pobj | among | 36:38 |
| The scene | scene | scene | nsubj | is | 39:41 |
| dense woodland | woodland | woodland | pobj | by | 48:50 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Tall | tall | ADJ | JJ | amod | trees | 1 |
| 1 | trees | tree | NOUN | NNS | nsubj | stand | 5 |
| 2 | with | with | ADP | IN | prep | trees | 1 |
| 3 | rough | rough | ADJ | JJ | amod | bark | 4 |
| 4 | bark | bark | NOUN | NN | pobj | with | 2 |
| 5 | stand | stand | VERB | VBP | ROOT | stand | 5 |
| 6 | in | in | ADP | IN | prep | stand | 5 |
| 7 | a | a | DET | DT | det | clearing | 9 |
| 8 | forest | forest | NOUN | NN | compound | clearing | 9 |
| 9 | clearing | clearing | NOUN | NN | pobj | in | 6 |
| 10 | , | , | PUNCT | , | punct | stand | 5 |
| 11 | their | their | PRON | PRP$ | poss | branches | 12 |
| 12 | branches | branch | NOUN | NNS | nsubj | filtering | 13 |
| 13 | filtering | filter | VERB | VBG | advcl | stand | 5 |
| 14 | sunlight | sunlight | NOUN | NN | dobj | filtering | 13 |
| 15 | onto | onto | ADP | IN | prep | filtering | 13 |
| 16 | the | the | DET | DT | det | ground | 17 |
| 17 | ground | ground | NOUN | NN | pobj | onto | 15 |
| 18 | . | . | PUNCT | . | punct | stand | 5 |
| 19 | Green | green | ADJ | JJ | amod | bushes | 20 |
| 20 | bushes | bush | NOUN | NNS | nsubj | cover | 24 |
| 21 | and | and | CCONJ | CC | cc | bushes | 20 |
| 22 | dry | dry | ADJ | JJ | amod | leaves | 23 |
| 23 | leaves | leaf | NOUN | NNS | conj | bushes | 20 |
| 24 | cover | cover | VERB | VBP | ROOT | cover | 24 |
| 25 | the | the | DET | DT | det | floor | 27 |
| 26 | forest | forest | NOUN | NN | compound | floor | 27 |
| 27 | floor | floor | NOUN | NN | dobj | cover | 24 |
| 28 | , | , | PUNCT | , | punct | cover | 24 |
| 29 | with | with | ADP | IN | prep | cover | 24 |
| 30 | dappled | dappled | ADJ | JJ | amod | light | 31 |
| 31 | light | light | NOUN | NN | nsubj | creating | 32 |
| 32 | creating | create | VERB | VBG | pcomp | with | 29 |
| 33 | bright | bright | ADJ | JJ | amod | spots | 34 |
| 34 | spots | spot | NOUN | NNS | dobj | creating | 32 |
| 35 | among | among | ADP | IN | prep | creating | 32 |
| 36 | the | the | DET | DT | det | shadows | 37 |
| 37 | shadows | shadow | NOUN | NNS | pobj | among | 35 |
| 38 | . | . | PUNCT | . | punct | cover | 24 |
| 39 | The | the | DET | DT | det | scene | 40 |
| 40 | scene | scene | NOUN | NN | nsubj | is | 41 |
| 41 | is | be | AUX | VBZ | ROOT | is | 41 |
| 42 | quiet | quiet | ADJ | JJ | acomp | is | 41 |
| 43 | and | and | CCONJ | CC | cc | quiet | 42 |
| 44 | natural | natural | ADJ | JJ | conj | quiet | 42 |
| 45 | , | , | PUNCT | , | punct | is | 41 |
| 46 | surrounded | surround | VERB | VBN | advcl | is | 41 |
| 47 | by | by | ADP | IN | agent | surrounded | 46 |
| 48 | dense | dense | ADJ | JJ | amod | woodland | 49 |
| 49 | woodland | woodland | NOUN | NN | pobj | by | 47 |
| 50 | . | . | PUNCT | . | punct | is | 41 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | trees | tree | chunk0 | 1 | noun_chunk_root | high |
| m1 | attribute | Tall | tall | chunk0 | 0 | size_attribute | high |
| m2 | object | bark | bark | chunk1 | 4 | noun_chunk_root | high |
| m3 | attribute | rough | rough | chunk1 | 3 | modifier_attribute | medium |
| m4 | object | clearing | clearing | chunk2 | 9 | noun_chunk_root | high |
| m5 | attribute | forest | forest | chunk2 | 8 | compound_modifier | medium |
| m6 | object | branches | branch | chunk3 | 12 | noun_chunk_root | high |
| m7 | attribute | their | their | chunk3 | 11 | modifier_attribute | medium |
| m8 | object | sunlight | sunlight | chunk4 | 14 | noun_chunk_root | high |
| m9 | object | ground | ground | chunk5 | 17 | noun_chunk_root | high |
| m10 | object | bushes | bush | chunk6 | 20 | noun_chunk_root | high |
| m11 | attribute | Green | green | chunk6 | 19 | color_attribute | high |
| m12 | object | leaves | leaf | chunk7 | 23 | noun_chunk_root | high |
| m13 | attribute | dry | dry | chunk7 | 22 | modifier_attribute | medium |
| m14 | object | floor | floor | chunk8 | 27 | noun_chunk_root | high |
| m15 | attribute | forest | forest | chunk8 | 26 | compound_modifier | medium |
| m16 | object | light | light | chunk9 | 31 | noun_chunk_root | high |
| m17 | attribute | dappled | dappled | chunk9 | 30 | modifier_attribute | medium |
| m18 | object | spots | spot | chunk10 | 34 | noun_chunk_root | high |
| m19 | attribute | bright | bright | chunk10 | 33 | visual_attribute | medium |
| m20 | object | shadows | shadow | chunk11 | 37 | noun_chunk_root | high |
| m21 | object | scene | scene | chunk12 | 40 | noun_chunk_root | high |
| m22 | object | woodland | woodland | chunk13 | 49 | noun_chunk_root | high |
| m23 | attribute | dense | dense | chunk13 | 48 | modifier_attribute | medium |
| m24 | action | stand | stand | doc | 5 | verb_predicate | high |
| m25 | action | filtering | filter | doc | 13 | verb_predicate | high |
| m26 | action | cover | cover | doc | 24 | verb_predicate | high |
| m27 | action | creating | create | doc | 32 | verb_predicate | high |
| m28 | action | surrounded | surround | doc | 46 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> trees |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> bark |
| e2 | has_attribute | m4 | m5 | medium | chunk2 compound -> clearing |
| e3 | has_attribute | m6 | m7 | medium | chunk3 poss -> branches |
| e4 | has_attribute | m10 | m11 | high | chunk6 amod -> bushes |
| e5 | has_attribute | m12 | m13 | medium | chunk7 amod -> leaves |
| e6 | has_attribute | m14 | m15 | medium | chunk8 compound -> floor |
| e7 | has_attribute | m16 | m17 | medium | chunk9 amod -> light |
| e8 | has_attribute | m18 | m19 | medium | chunk10 amod -> spots |
| e9 | has_attribute | m22 | m23 | medium | chunk13 amod -> woodland |
| e10 | agent | m24 | m0 | medium | nsubj -> stand |
| e11 | agent | m25 | m6 | medium | nsubj -> filtering |
| e12 | patient | m25 | m8 | medium | dobj -> filtering |
| e13 | agent | m26 | m10 | medium | nsubj -> cover |
| e14 | agent | m26 | m12 | medium | nsubj -> cover |
| e15 | patient | m26 | m14 | medium | dobj -> cover |
| e16 | agent | m27 | m16 | medium | nsubj -> creating |
| e17 | patient | m27 | m18 | medium | dobj -> creating |
| e18 | relation | m0 | m2 | high | with |
| e19 | relation | m0 | m4 | high | in |
| e20 | relation | m6 | m9 | medium | onto |
| e21 | relation | m16 | m20 | medium | among |
| e22 | relation | m21 | m22 | medium | by |

## 59

**caption_shape:** `multi-sentence`
**caption_id:** `3067f6b54759f2cb448fa4e611600ffbe88bd51c44e60b4c44d135baea3b2c14`

> A softball player in a maroon uniform stands on a base as an umpire walks nearby. Spectators sit in chairs behind a fence in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| A softball player in a maroon uniform stands on a base as an umpire walks nearby. | 0:17 |
| Spectators sit in chairs behind a fence in the background. | 17:28 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A softball player | player | player | nsubj | stands | 0:3 |
| a maroon uniform | uniform | uniform | pobj | in | 4:7 |
| a base | base | base | pobj | on | 9:11 |
| an umpire | umpire | umpire | nsubj | walks | 12:14 |
| Spectators | Spectators | spectator | nsubj | sit | 17:18 |
| chairs | chairs | chair | pobj | in | 20:21 |
| a fence | fence | fence | pobj | behind | 22:24 |
| the background | background | background | pobj | in | 25:27 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | player | 2 |
| 1 | softball | softball | NOUN | NN | compound | player | 2 |
| 2 | player | player | NOUN | NN | nsubj | stands | 7 |
| 3 | in | in | ADP | IN | prep | player | 2 |
| 4 | a | a | DET | DT | det | uniform | 6 |
| 5 | maroon | maroon | NOUN | NN | compound | uniform | 6 |
| 6 | uniform | uniform | NOUN | NN | pobj | in | 3 |
| 7 | stands | stand | VERB | VBZ | ROOT | stands | 7 |
| 8 | on | on | ADP | IN | prep | stands | 7 |
| 9 | a | a | DET | DT | det | base | 10 |
| 10 | base | base | NOUN | NN | pobj | on | 8 |
| 11 | as | as | SCONJ | IN | mark | walks | 14 |
| 12 | an | an | DET | DT | det | umpire | 13 |
| 13 | umpire | umpire | NOUN | NN | nsubj | walks | 14 |
| 14 | walks | walk | VERB | VBZ | advcl | stands | 7 |
| 15 | nearby | nearby | ADV | RB | advmod | walks | 14 |
| 16 | . | . | PUNCT | . | punct | stands | 7 |
| 17 | Spectators | spectator | NOUN | NNS | nsubj | sit | 18 |
| 18 | sit | sit | VERB | VBP | ROOT | sit | 18 |
| 19 | in | in | ADP | IN | prep | sit | 18 |
| 20 | chairs | chair | NOUN | NNS | pobj | in | 19 |
| 21 | behind | behind | ADP | IN | prep | sit | 18 |
| 22 | a | a | DET | DT | det | fence | 23 |
| 23 | fence | fence | NOUN | NN | pobj | behind | 21 |
| 24 | in | in | ADP | IN | prep | sit | 18 |
| 25 | the | the | DET | DT | det | background | 26 |
| 26 | background | background | NOUN | NN | pobj | in | 24 |
| 27 | . | . | PUNCT | . | punct | sit | 18 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | player | player | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | softball | softball | chunk0 | 1 | compound_modifier | medium |
| m2 | object | uniform | uniform | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | maroon | maroon | chunk1 | 5 | color_attribute | high |
| m4 | object | base | base | chunk2 | 10 | noun_chunk_root | high |
| m5 | object | umpire | umpire | chunk3 | 13 | noun_chunk_root | high |
| m6 | object | Spectators | spectator | chunk4 | 17 | noun_chunk_root | high |
| m7 | object | chairs | chair | chunk5 | 20 | noun_chunk_root | high |
| m8 | object | fence | fence | chunk6 | 23 | noun_chunk_root | high |
| m9 | object | background | background | chunk7 | 26 | noun_chunk_root | high |
| m10 | context | background | background | doc | 26 | context_word | medium |
| m11 | action | stands | stand | doc | 7 | verb_predicate | high |
| m12 | action | walks | walk | doc | 14 | verb_predicate | high |
| m13 | action | sit | sit | doc | 18 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 compound -> player |
| e1 | has_attribute | m2 | m3 | high | chunk1 compound -> uniform |
| e2 | has_context | scene | m10 | medium | context token background |
| e3 | agent | m11 | m0 | medium | nsubj -> stands |
| e4 | agent | m12 | m5 | medium | nsubj -> walks |
| e5 | agent | m13 | m6 | medium | nsubj -> sit |
| e6 | relation | m0 | m2 | high | in |
| e7 | relation | m0 | m4 | high | on |
| e8 | relation | m6 | m7 | high | in |
| e9 | relation | m6 | m8 | high | behind |
| e10 | relation | m6 | m10 | high | in |

## 60

**caption_shape:** `multi-sentence`
**caption_id:** `3071b315a1e687d13684eb7dfce218b5cc007d8b21f2fd2ea5126c6308acf014`

> A stone church with a cross on its tower stands under a blue sky. An arched entrance leads into the building.

### Sentences
| sentence | token_span |
| --- | --- |
| A stone church with a cross on its tower stands under a blue sky. | 0:15 |
| An arched entrance leads into the building. | 15:23 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A stone church | church | church | nsubj | stands | 0:3 |
| a cross | cross | cross | pcomp | with | 4:6 |
| its tower | tower | tower | pobj | on | 7:9 |
| a blue sky | sky | sky | pobj | under | 11:14 |
| An arched entrance | entrance | entrance | nsubj | leads | 15:18 |
| the building | building | building | pobj | into | 20:22 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | church | 2 |
| 1 | stone | stone | NOUN | NN | compound | church | 2 |
| 2 | church | church | NOUN | NN | nsubj | stands | 9 |
| 3 | with | with | ADP | IN | prep | church | 2 |
| 4 | a | a | DET | DT | det | cross | 5 |
| 5 | cross | cross | NOUN | NN | pcomp | with | 3 |
| 6 | on | on | ADP | IN | prep | cross | 5 |
| 7 | its | its | PRON | PRP$ | poss | tower | 8 |
| 8 | tower | tower | NOUN | NN | pobj | on | 6 |
| 9 | stands | stand | VERB | VBZ | ROOT | stands | 9 |
| 10 | under | under | ADP | IN | prep | stands | 9 |
| 11 | a | a | DET | DT | det | sky | 13 |
| 12 | blue | blue | ADJ | JJ | amod | sky | 13 |
| 13 | sky | sky | NOUN | NN | pobj | under | 10 |
| 14 | . | . | PUNCT | . | punct | stands | 9 |
| 15 | An | an | DET | DT | det | entrance | 17 |
| 16 | arched | arched | ADJ | JJ | amod | entrance | 17 |
| 17 | entrance | entrance | NOUN | NN | nsubj | leads | 18 |
| 18 | leads | lead | VERB | VBZ | ROOT | leads | 18 |
| 19 | into | into | ADP | IN | prep | leads | 18 |
| 20 | the | the | DET | DT | det | building | 21 |
| 21 | building | building | NOUN | NN | pobj | into | 19 |
| 22 | . | . | PUNCT | . | punct | leads | 18 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | church | church | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | stone | stone | chunk0 | 1 | material_attribute | high |
| m2 | object | cross | cross | chunk1 | 5 | noun_chunk_root | high |
| m3 | object | tower | tower | chunk2 | 8 | noun_chunk_root | high |
| m4 | attribute | its | its | chunk2 | 7 | modifier_attribute | medium |
| m5 | object | sky | sky | chunk3 | 13 | noun_chunk_root | high |
| m6 | attribute | blue | blue | chunk3 | 12 | color_attribute | high |
| m7 | object | entrance | entrance | chunk4 | 17 | noun_chunk_root | high |
| m8 | attribute | arched | arched | chunk4 | 16 | visual_attribute | medium |
| m9 | object | building | building | chunk5 | 21 | noun_chunk_root | high |
| m10 | action | stands | stand | doc | 9 | verb_predicate | high |
| m11 | action | leads | lead | doc | 18 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 compound -> church |
| e1 | has_attribute | m3 | m4 | medium | chunk2 poss -> tower |
| e2 | has_attribute | m5 | m6 | high | chunk3 amod -> sky |
| e3 | has_attribute | m7 | m8 | medium | chunk4 amod -> entrance |
| e4 | agent | m10 | m0 | medium | nsubj -> stands |
| e5 | agent | m11 | m7 | medium | nsubj -> leads |
| e6 | relation | m0 | m2 | high | with |
| e7 | relation | m2 | m3 | high | on |
| e8 | relation | m0 | m5 | high | under |
| e9 | relation | m7 | m9 | medium | into |

## 61

**caption_shape:** `sentence-like`
**caption_id:** `310880df54b4043e639fa4c97eb815ee953daef624af9115d22bd9ca06542c14`

> A gradient sky shows blue fading into orange near the horizon.

### Sentences
| sentence | token_span |
| --- | --- |
| A gradient sky shows blue fading into orange near the horizon. | 0:12 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A gradient sky | sky | sky | nsubj | shows | 0:3 |
| blue | blue | blue | nsubj | fading | 4:5 |
| orange | orange | orange | pobj | into | 7:8 |
| the horizon | horizon | horizon | pobj | near | 9:11 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | sky | 2 |
| 1 | gradient | gradient | NOUN | NN | compound | sky | 2 |
| 2 | sky | sky | NOUN | NN | nsubj | shows | 3 |
| 3 | shows | show | VERB | VBZ | ROOT | shows | 3 |
| 4 | blue | blue | NOUN | NN | nsubj | fading | 5 |
| 5 | fading | fade | VERB | VBG | ccomp | shows | 3 |
| 6 | into | into | ADP | IN | prep | fading | 5 |
| 7 | orange | orange | NOUN | NN | pobj | into | 6 |
| 8 | near | near | ADP | IN | prep | fading | 5 |
| 9 | the | the | DET | DT | det | horizon | 10 |
| 10 | horizon | horizon | NOUN | NN | pobj | near | 8 |
| 11 | . | . | PUNCT | . | punct | shows | 3 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | sky | sky | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | gradient | gradient | chunk0 | 1 | compound_modifier | medium |
| m2 | object | blue | blue | chunk1 | 4 | noun_chunk_root | high |
| m3 | object | orange | orange | chunk2 | 7 | noun_chunk_root | high |
| m4 | object | horizon | horizon | chunk3 | 10 | noun_chunk_root | high |
| m5 | action | shows | show | doc | 3 | verb_predicate | high |
| m6 | action | fading | fade | doc | 5 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 compound -> sky |
| e1 | agent | m5 | m0 | medium | nsubj -> shows |
| e2 | agent | m6 | m2 | medium | nsubj -> fading |
| e3 | relation | m2 | m3 | medium | into |
| e4 | relation | m2 | m4 | high | near |

## 62

**caption_shape:** `multi-sentence`
**caption_id:** `31175b7ae109233857b3b712027236ce9b67be47e5a0660848273ad48d080c14`

> A man and a woman sit close together in a dimly lit room. The woman holds a single red rose with a ribbon, wearing a dark purple top and dangling earrings. Both look toward the camera with gentle smiles.

### Sentences
| sentence | token_span |
| --- | --- |
| A man and a woman sit close together in a dimly lit room. | 0:14 |
| The woman holds a single red rose with a ribbon, wearing a dark purple top and dangling earrings. | 14:34 |
| Both look toward the camera with gentle smiles. | 34:43 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A man | man | man | nsubj | sit | 0:2 |
| a woman | woman | woman | conj | man | 3:5 |
| a dimly lit room | room | room | pobj | in | 9:13 |
| The woman | woman | woman | nsubj | holds | 14:16 |
| a single red rose | rose | rose | dobj | holds | 17:21 |
| a ribbon | ribbon | ribbon | pobj | with | 22:24 |
| a dark purple top | top | top | dobj | wearing | 26:30 |
| dangling earrings | earrings | earring | conj | top | 31:33 |
| Both | Both | both | nsubj | look | 34:35 |
| the camera | camera | camera | pobj | toward | 37:39 |
| gentle smiles | smiles | smile | pobj | with | 40:42 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | man | 1 |
| 1 | man | man | NOUN | NN | nsubj | sit | 5 |
| 2 | and | and | CCONJ | CC | cc | man | 1 |
| 3 | a | a | DET | DT | det | woman | 4 |
| 4 | woman | woman | NOUN | NN | conj | man | 1 |
| 5 | sit | sit | VERB | VBP | ROOT | sit | 5 |
| 6 | close | close | ADV | RB | advmod | together | 7 |
| 7 | together | together | ADV | RB | advmod | sit | 5 |
| 8 | in | in | ADP | IN | prep | sit | 5 |
| 9 | a | a | DET | DT | det | room | 12 |
| 10 | dimly | dimly | ADV | RB | advmod | lit | 11 |
| 11 | lit | light | VERB | VBN | amod | room | 12 |
| 12 | room | room | NOUN | NN | pobj | in | 8 |
| 13 | . | . | PUNCT | . | punct | sit | 5 |
| 14 | The | the | DET | DT | det | woman | 15 |
| 15 | woman | woman | NOUN | NN | nsubj | holds | 16 |
| 16 | holds | hold | VERB | VBZ | ROOT | holds | 16 |
| 17 | a | a | DET | DT | det | rose | 20 |
| 18 | single | single | ADJ | JJ | amod | rose | 20 |
| 19 | red | red | ADJ | JJ | amod | rose | 20 |
| 20 | rose | rose | NOUN | NN | dobj | holds | 16 |
| 21 | with | with | ADP | IN | prep | rose | 20 |
| 22 | a | a | DET | DT | det | ribbon | 23 |
| 23 | ribbon | ribbon | NOUN | NN | pobj | with | 21 |
| 24 | , | , | PUNCT | , | punct | holds | 16 |
| 25 | wearing | wear | VERB | VBG | advcl | holds | 16 |
| 26 | a | a | DET | DT | det | top | 29 |
| 27 | dark | dark | ADJ | JJ | amod | purple | 28 |
| 28 | purple | purple | ADJ | JJ | amod | top | 29 |
| 29 | top | top | NOUN | NN | dobj | wearing | 25 |
| 30 | and | and | CCONJ | CC | cc | top | 29 |
| 31 | dangling | dangle | VERB | VBG | amod | earrings | 32 |
| 32 | earrings | earring | NOUN | NNS | conj | top | 29 |
| 33 | . | . | PUNCT | . | punct | holds | 16 |
| 34 | Both | both | PRON | DT | nsubj | look | 35 |
| 35 | look | look | VERB | VBP | ROOT | look | 35 |
| 36 | toward | toward | ADP | IN | prep | look | 35 |
| 37 | the | the | DET | DT | det | camera | 38 |
| 38 | camera | camera | NOUN | NN | pobj | toward | 36 |
| 39 | with | with | ADP | IN | prep | look | 35 |
| 40 | gentle | gentle | ADJ | JJ | amod | smiles | 41 |
| 41 | smiles | smile | NOUN | NNS | pobj | with | 39 |
| 42 | . | . | PUNCT | . | punct | look | 35 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | woman | woman | chunk1 | 4 | noun_chunk_root | high |
| m2 | object | room | room | chunk2 | 12 | noun_chunk_root | high |
| m3 | attribute | dimly | dimly | chunk2 | 10 | modifier_attribute | medium |
| m4 | attribute | lit | light | chunk2 | 11 | visual_attribute | medium |
| m5 | object | woman | woman | chunk3 | 15 | noun_chunk_root | high |
| m6 | object | rose | rose | chunk4 | 20 | noun_chunk_root | high |
| m7 | attribute | single | single | chunk4 | 18 | modifier_attribute | medium |
| m8 | attribute | red | red | chunk4 | 19 | color_attribute | high |
| m9 | object | ribbon | ribbon | chunk5 | 23 | noun_chunk_root | high |
| m10 | object | top | top | chunk6 | 29 | noun_chunk_root | high |
| m11 | attribute | dark | dark | chunk6 | 27 | visual_attribute | medium |
| m12 | attribute | purple | purple | chunk6 | 28 | color_attribute | high |
| m13 | object | earrings | earring | chunk7 | 32 | noun_chunk_root | high |
| m14 | attribute | dangling | dangle | chunk7 | 31 | state_attribute | medium |
| m15 | object | Both | both | chunk8 | 34 | noun_chunk_root | high |
| m16 | object | camera | camera | chunk9 | 38 | noun_chunk_root | high |
| m17 | object | smiles | smile | chunk10 | 41 | noun_chunk_root | high |
| m18 | attribute | gentle | gentle | chunk10 | 40 | modifier_attribute | medium |
| m19 | action | sit | sit | doc | 5 | verb_predicate | high |
| m20 | action | holds | hold | doc | 16 | verb_predicate | high |
| m21 | action | wearing | wear | doc | 25 | verb_predicate | high |
| m22 | action | look | look | doc | 35 | verb_predicate | high |

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
| e8 | agent | m19 | m0 | medium | nsubj -> sit |
| e9 | agent | m19 | m1 | medium | nsubj -> sit |
| e10 | agent | m20 | m5 | medium | nsubj -> holds |
| e11 | patient | m20 | m6 | medium | dobj -> holds |
| e12 | patient | m21 | m10 | medium | dobj -> wearing |
| e13 | patient | m21 | m13 | medium | dobj -> wearing |
| e14 | agent | m22 | m15 | medium | nsubj -> look |
| e15 | relation | m0 | m2 | high | in |
| e16 | relation | m6 | m9 | high | with |
| e17 | relation | m15 | m16 | medium | toward |
| e18 | relation | m15 | m17 | high | with |

## 63

**caption_shape:** `multi-sentence`
**caption_id:** `3177bcfa49aa3f7319ad241b1f6f7217718fb646fe189a246c1ab7685830b414`

> Two men in camouflage uniforms are grappling on a blue and red mat inside a gym. One is on top, controlling the other who is lying on their back, with a chain-link fence visible behind them. A third person in similar gear is bent over nearby.

### Sentences
| sentence | token_span |
| --- | --- |
| Two men in camouflage uniforms are grappling on a blue and red mat inside a gym. | 0:17 |
| One is on top, controlling the other who is lying on their back, with a chain-link fence visible behind them. | 17:40 |
| A third person in similar gear is bent over nearby. | 40:51 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Two men | men | man | nsubj | grappling | 0:2 |
| camouflage uniforms | uniforms | uniform | pobj | in | 3:5 |
| a blue and red mat | mat | mat | pobj | on | 8:13 |
| a gym | gym | gym | pobj | inside | 14:16 |
| top | top | top | pobj | on | 20:21 |
| who | who | who | nsubj | lying | 25:26 |
| their back | back | back | pobj | on | 29:31 |
| a chain-link fence | fence | fence | pobj | with | 33:36 |
| them | them | they | pobj | behind | 38:39 |
| A third person | person | person | nsubj | is | 40:43 |
| similar gear | gear | gear | pobj | in | 44:46 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Two | two | NUM | CD | nummod | men | 1 |
| 1 | men | man | NOUN | NNS | nsubj | grappling | 6 |
| 2 | in | in | ADP | IN | prep | men | 1 |
| 3 | camouflage | camouflage | NOUN | NN | compound | uniforms | 4 |
| 4 | uniforms | uniform | NOUN | NNS | pobj | in | 2 |
| 5 | are | be | AUX | VBP | aux | grappling | 6 |
| 6 | grappling | grapple | VERB | VBG | ROOT | grappling | 6 |
| 7 | on | on | ADP | IN | prep | grappling | 6 |
| 8 | a | a | DET | DT | det | mat | 12 |
| 9 | blue | blue | ADJ | JJ | amod | mat | 12 |
| 10 | and | and | CCONJ | CC | cc | blue | 9 |
| 11 | red | red | ADJ | JJ | conj | blue | 9 |
| 12 | mat | mat | NOUN | NN | pobj | on | 7 |
| 13 | inside | inside | ADP | IN | prep | grappling | 6 |
| 14 | a | a | DET | DT | det | gym | 15 |
| 15 | gym | gym | NOUN | NN | pobj | inside | 13 |
| 16 | . | . | PUNCT | . | punct | grappling | 6 |
| 17 | One | one | NUM | CD | nsubj | is | 18 |
| 18 | is | be | AUX | VBZ | ROOT | is | 18 |
| 19 | on | on | ADP | IN | prep | is | 18 |
| 20 | top | top | NOUN | NN | pobj | on | 19 |
| 21 | , | , | PUNCT | , | punct | is | 18 |
| 22 | controlling | control | VERB | VBG | advcl | is | 18 |
| 23 | the | the | DET | DT | det | other | 24 |
| 24 | other | other | ADJ | JJ | dobj | controlling | 22 |
| 25 | who | who | PRON | WP | nsubj | lying | 27 |
| 26 | is | be | AUX | VBZ | aux | lying | 27 |
| 27 | lying | lie | VERB | VBG | relcl | other | 24 |
| 28 | on | on | ADP | IN | prep | lying | 27 |
| 29 | their | their | PRON | PRP$ | poss | back | 30 |
| 30 | back | back | NOUN | NN | pobj | on | 28 |
| 31 | , | , | PUNCT | , | punct | lying | 27 |
| 32 | with | with | ADP | IN | prep | lying | 27 |
| 33 | a | a | DET | DT | det | fence | 35 |
| 34 | chain-link | chain-link | NOUN | NN | compound | fence | 35 |
| 35 | fence | fence | NOUN | NN | pobj | with | 32 |
| 36 | visible | visible | ADJ | JJ | amod | fence | 35 |
| 37 | behind | behind | ADP | IN | prep | visible | 36 |
| 38 | them | they | PRON | PRP | pobj | behind | 37 |
| 39 | . | . | PUNCT | . | punct | is | 18 |
| 40 | A | a | DET | DT | det | person | 42 |
| 41 | third | third | ADJ | JJ | amod | person | 42 |
| 42 | person | person | NOUN | NN | nsubj | is | 46 |
| 43 | in | in | ADP | IN | prep | person | 42 |
| 44 | similar | similar | ADJ | JJ | amod | gear | 45 |
| 45 | gear | gear | NOUN | NN | pobj | in | 43 |
| 46 | is | be | AUX | VBZ | ROOT | is | 46 |
| 47 | bent | bend | VERB | VBN | acomp | is | 46 |
| 48 | over | over | ADP | RP | prt | bent | 47 |
| 49 | nearby | nearby | ADV | RB | advmod | bent | 47 |
| 50 | . | . | PUNCT | . | punct | is | 46 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | men | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Two | two | chunk0 | 0 | quantity | high |
| m2 | object | uniforms | uniform | chunk1 | 4 | noun_chunk_root | high |
| m3 | attribute | camouflage | camouflage | chunk1 | 3 | compound_modifier | medium |
| m4 | object | mat | mat | chunk2 | 12 | noun_chunk_root | high |
| m5 | attribute | blue | blue | chunk2 | 9 | color_attribute | high |
| m6 | attribute | red | red | chunk2 | 11 | color_attribute | high |
| m7 | object | gym | gym | chunk3 | 15 | noun_chunk_root | high |
| m8 | context | top | top | chunk4 | 20 | spatial_region | medium |
| m9 | object | who | who | chunk5 | 25 | noun_chunk_root | high |
| m10 | context | back | back | chunk6 | 30 | spatial_region | medium |
| m11 | object | fence | fence | chunk7 | 35 | noun_chunk_root | high |
| m12 | attribute | chain-link | chain-link | chunk7 | 34 | compound_modifier | medium |
| m13 | object | them | they | chunk8 | 38 | noun_chunk_root | high |
| m14 | object | person | person | chunk9 | 42 | noun_chunk_root | high |
| m15 | attribute | third | third | chunk9 | 41 | modifier_attribute | medium |
| m16 | object | gear | gear | chunk10 | 45 | noun_chunk_root | high |
| m17 | attribute | similar | similar | chunk10 | 44 | modifier_attribute | medium |
| m18 | context | inside | inside | doc | 13 | context_word | medium |
| m19 | action | grappling | grapple | doc | 6 | verb_predicate | high |
| m20 | action | controlling | control | doc | 22 | verb_predicate | high |
| m21 | action | lying | lie | doc | 27 | verb_predicate | high |
| m22 | action | bent | bend | doc | 47 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 nummod -> men |
| e1 | has_attribute | m2 | m3 | medium | chunk1 compound -> uniforms |
| e2 | has_attribute | m4 | m5 | high | chunk2 amod -> mat |
| e3 | has_attribute | m4 | m6 | high | chunk2 conj -> mat |
| e4 | has_attribute | m11 | m12 | medium | chunk7 compound -> fence |
| e5 | has_attribute | m14 | m15 | medium | chunk9 amod -> person |
| e6 | has_attribute | m16 | m17 | medium | chunk10 amod -> gear |
| e7 | has_context | scene | m18 | medium | context token inside |
| e8 | agent | m19 | m0 | medium | nsubj -> grappling |
| e9 | agent | m21 | m9 | medium | nsubj -> lying |
| e10 | relation | m0 | m2 | high | in |
| e11 | relation | m0 | m4 | high | on |
| e12 | relation | m0 | m7 | high | inside |
| e13 | relation | m9 | m10 | high | on |
| e14 | relation | m9 | m11 | high | with |
| e15 | relation | m14 | m16 | high | in |

## 64

**caption_shape:** `sentence-like`
**caption_id:** `319fb2034f0f1e660f1018f787b0ee1fb3ddff1a65e6543f4556fae5c3b85814`

> A woman walks past a wall covered with colorful real estate signs in Chinese.

### Sentences
| sentence | token_span |
| --- | --- |
| A woman walks past a wall covered with colorful real estate signs in Chinese. | 0:15 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A woman | woman | woman | nsubj | walks | 0:2 |
| a wall | wall | wall | pobj | past | 4:6 |
| colorful real estate signs | signs | sign | pobj | with | 8:12 |
| Chinese | Chinese | Chinese | pobj | in | 13:14 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | woman | 1 |
| 1 | woman | woman | NOUN | NN | nsubj | walks | 2 |
| 2 | walks | walk | VERB | VBZ | ROOT | walks | 2 |
| 3 | past | past | ADP | IN | prep | walks | 2 |
| 4 | a | a | DET | DT | det | wall | 5 |
| 5 | wall | wall | NOUN | NN | pobj | past | 3 |
| 6 | covered | cover | VERB | VBN | acl | wall | 5 |
| 7 | with | with | ADP | IN | prep | covered | 6 |
| 8 | colorful | colorful | ADJ | JJ | amod | signs | 11 |
| 9 | real | real | ADJ | JJ | amod | estate | 10 |
| 10 | estate | estate | NOUN | NN | compound | signs | 11 |
| 11 | signs | sign | NOUN | NNS | pobj | with | 7 |
| 12 | in | in | ADP | IN | prep | signs | 11 |
| 13 | Chinese | Chinese | PROPN | NNP | pobj | in | 12 |
| 14 | . | . | PUNCT | . | punct | walks | 2 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | wall | wall | chunk1 | 5 | noun_chunk_root | high |
| m2 | object | signs | sign | chunk2 | 11 | noun_chunk_root | high |
| m3 | attribute | colorful | colorful | chunk2 | 8 | modifier_attribute | medium |
| m4 | attribute | real | real | chunk2 | 9 | modifier_attribute | medium |
| m5 | attribute | estate | estate | chunk2 | 10 | compound_modifier | medium |
| m6 | object | Chinese | chinese | chunk3 | 13 | noun_chunk_root | high |
| m7 | action | walks | walk | doc | 2 | verb_predicate | high |
| m8 | action | covered | cover | doc | 6 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | medium | chunk2 amod -> signs |
| e1 | has_attribute | m2 | m4 | medium | chunk2 amod -> signs |
| e2 | has_attribute | m2 | m5 | medium | chunk2 compound -> signs |
| e3 | agent | m7 | m0 | medium | nsubj -> walks |
| e4 | relation | m0 | m1 | medium | past |
| e5 | relation | m1 | m2 | high | with |
| e6 | relation | m2 | m6 | high | in |

## 65

**caption_shape:** `tag-list-like`
**caption_id:** `32bdeb0aa470fea2161e734b82fa841661fcaaed423d1b7274f831210a489c14`

> man, drink, pool, night, chair

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | man | man | 0:3 |
| t1 | drink | drink | 5:10 |
| t2 | pool | pool | 12:16 |
| t3 | night | night | 18:23 |
| t4 | chair | chair | 25:30 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t1 | drink | drink | drink | ROOT | drink | 0:1 | 5:10 |
| t2 | pool | pool | pool | ROOT | pool | 0:1 | 12:16 |
| t3 | night | night | night | ROOT | night | 0:1 | 18:23 |
| t4 | chair | chair | chair | ROOT | chair | 0:1 | 25:30 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | man | man | INTJ | NOUN | UH | NN | ROOT | man | 0 | 0:3 |
| t1 | 0 | drink | drink | NOUN | NOUN | NN | NN | ROOT | drink | 0 | 5:10 |
| t2 | 0 | pool | pool | NOUN | NOUN | NN | NN | ROOT | pool | 0 | 12:16 |
| t3 | 0 | night | night | NOUN | NOUN | NN | NN | ROOT | night | 0 | 18:23 |
| t4 | 0 | chair | chair | NOUN | NOUN | NN | NN | ROOT | chair | 0 | 25:30 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | t0 | 0 | tag_list_person_object_override | high |
| m1 | object | drink | drink | t1 | 0 | segment_head | high |
| m2 | object | pool | pool | t2 | 0 | segment_head | high |
| m3 | context | night | night | t3 | 0 | scene_context | high |
| m4 | object | chair | chair | t4 | 0 | segment_head | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_context | scene | m3 | high | t3 context tag |

## 66

**caption_shape:** `tag-list-like`
**caption_id:** `3324412e9131638c6f5171d825b2f4408edaeeaf42702e4a7d12dc415afbe414`

> grandparent, child, toy car, striped shirt, red shirt

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | grandparent | grandparent | 0:11 |
| t1 | child | child | 13:18 |
| t2 | toy car | toy car | 20:27 |
| t3 | striped shirt | striped shirt | 29:42 |
| t4 | red shirt | red shirt | 44:53 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | grandparent | grandparent | grandparent | ROOT | grandparent | 0:1 | 0:11 |
| t1 | child | child | child | ROOT | child | 0:1 | 13:18 |
| t2 | toy car | car | car | ROOT | car | 0:2 | 20:27 |
| t3 | striped shirt | shirt | shirt | ROOT | shirt | 0:2 | 29:42 |
| t4 | red shirt | shirt | shirt | ROOT | shirt | 0:2 | 44:53 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | grandparent | grandparent | NOUN | NOUN | NN | NN | ROOT | grandparent | 0 | 0:11 |
| t1 | 0 | child | child | NOUN | NOUN | NN | NN | ROOT | child | 0 | 13:18 |
| t2 | 0 | toy | toy | PROPN | ADJ | NNP | JJ | compound | car | 1 | 20:23 |
| t2 | 1 | car | car | PROPN | NOUN | NNP | NN | ROOT | car | 1 | 24:27 |
| t3 | 0 | striped | striped | ADJ | ADJ | JJ | JJ | amod | shirt | 1 | 29:36 |
| t3 | 1 | shirt | shirt | NOUN | NOUN | NN | NN | ROOT | shirt | 1 | 37:42 |
| t4 | 0 | red | red | ADJ | ADJ | JJ | JJ | compound | shirt | 1 | 44:47 |
| t4 | 1 | shirt | shirt | NOUN | NOUN | NN | NN | ROOT | shirt | 1 | 48:53 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | grandparent | grandparent | t0 | 0 | segment_head | high |
| m1 | object | child | child | t1 | 0 | segment_head | high |
| m2 | object | car | car | t2 | 1 | segment_head | high |
| m3 | attribute | toy | toy | t2 | 0 | attribute | high |
| m4 | object | shirt | shirt | t3 | 1 | segment_head | high |
| m5 | attribute | striped | striped | t3 | 0 | attribute | high |
| m6 | object | shirt | shirt | t4 | 1 | segment_head | high |
| m7 | attribute | red | red | t4 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | t2 internal compound -> car |
| e1 | has_attribute | m4 | m5 | high | t3 internal amod -> shirt |
| e2 | has_attribute | m6 | m7 | high | t4 internal compound -> shirt |

## 67

**caption_shape:** `multi-sentence`
**caption_id:** `338c0b314d1beee6ba81fa613f7f9bca53a4ad5bad1cefb3cf625a6cbc0f1014`

> A soccer player in a black uniform controls the ball on a grassy field. Another player in a light blue uniform stands nearby, with spectators and tents visible in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| A soccer player in a black uniform controls the ball on a grassy field. | 0:14 |
| Another player in a light blue uniform stands nearby, with spectators and tents visible in the background. | 14:33 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A soccer player | soccer player | soccer_player | nsubj | controls | 0:2 |
| a black uniform | uniform | uniform | pobj | in | 3:6 |
| the ball | ball | ball | dobj | controls | 7:9 |
| a grassy field | field | field | pobj | on | 10:13 |
| Another player | player | player | nsubj | stands | 14:16 |
| a light blue uniform | uniform | uniform | pobj | in | 17:21 |
| spectators | spectators | spectator | nsubj | visible | 25:26 |
| tents | tents | tent | conj | spectators | 27:28 |
| the background | background | background | pobj | in | 30:32 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | soccer player | 1 |
| 1 | soccer player | soccer_player | NOUN | NN | nsubj | controls | 6 |
| 2 | in | in | ADP | IN | prep | soccer player | 1 |
| 3 | a | a | DET | DT | det | uniform | 5 |
| 4 | black | black | ADJ | JJ | amod | uniform | 5 |
| 5 | uniform | uniform | NOUN | NN | pobj | in | 2 |
| 6 | controls | control | VERB | VBZ | ROOT | controls | 6 |
| 7 | the | the | DET | DT | det | ball | 8 |
| 8 | ball | ball | NOUN | NN | dobj | controls | 6 |
| 9 | on | on | ADP | IN | prep | controls | 6 |
| 10 | a | a | DET | DT | det | field | 12 |
| 11 | grassy | grassy | ADJ | JJ | amod | field | 12 |
| 12 | field | field | NOUN | NN | pobj | on | 9 |
| 13 | . | . | PUNCT | . | punct | controls | 6 |
| 14 | Another | another | DET | DT | det | player | 15 |
| 15 | player | player | NOUN | NN | nsubj | stands | 21 |
| 16 | in | in | ADP | IN | prep | player | 15 |
| 17 | a | a | DET | DT | det | uniform | 20 |
| 18 | light | light | ADJ | JJ | amod | blue | 19 |
| 19 | blue | blue | ADJ | JJ | amod | uniform | 20 |
| 20 | uniform | uniform | NOUN | NN | pobj | in | 16 |
| 21 | stands | stand | VERB | VBZ | ROOT | stands | 21 |
| 22 | nearby | nearby | ADV | RB | advmod | stands | 21 |
| 23 | , | , | PUNCT | , | punct | stands | 21 |
| 24 | with | with | SCONJ | IN | mark | visible | 28 |
| 25 | spectators | spectator | NOUN | NNS | nsubj | visible | 28 |
| 26 | and | and | CCONJ | CC | cc | spectators | 25 |
| 27 | tents | tent | NOUN | NNS | conj | spectators | 25 |
| 28 | visible | visible | ADJ | JJ | advcl | stands | 21 |
| 29 | in | in | ADP | IN | prep | visible | 28 |
| 30 | the | the | DET | DT | det | background | 31 |
| 31 | background | background | NOUN | NN | pobj | in | 29 |
| 32 | . | . | PUNCT | . | punct | stands | 21 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | soccer player | soccer_player | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | uniform | uniform | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | black | black | chunk1 | 4 | color_attribute | high |
| m3 | object | ball | ball | chunk2 | 8 | noun_chunk_root | high |
| m4 | object | field | field | chunk3 | 12 | noun_chunk_root | high |
| m5 | attribute | grassy | grassy | chunk3 | 11 | modifier_attribute | medium |
| m6 | object | player | player | chunk4 | 15 | noun_chunk_root | high |
| m7 | object | uniform | uniform | chunk5 | 20 | noun_chunk_root | high |
| m8 | attribute | light | light | chunk5 | 18 | visual_attribute | medium |
| m9 | attribute | blue | blue | chunk5 | 19 | color_attribute | high |
| m10 | object | spectators | spectator | chunk6 | 25 | noun_chunk_root | high |
| m11 | object | tents | tent | chunk7 | 27 | noun_chunk_root | high |
| m12 | object | background | background | chunk8 | 31 | noun_chunk_root | high |
| m13 | context | background | background | doc | 31 | context_word | medium |
| m14 | action | controls | control | doc | 6 | verb_predicate | high |
| m15 | action | stands | stand | doc | 21 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> uniform |
| e1 | has_attribute | m4 | m5 | medium | chunk3 amod -> field |
| e2 | has_attribute | m7 | m8 | medium | chunk5 amod -> uniform |
| e3 | has_attribute | m7 | m9 | high | chunk5 amod -> uniform |
| e4 | has_context | scene | m13 | medium | context token background |
| e5 | agent | m14 | m0 | medium | nsubj -> controls |
| e6 | patient | m14 | m3 | medium | dobj -> controls |
| e7 | agent | m15 | m6 | medium | nsubj -> stands |
| e8 | relation | m0 | m1 | high | in |
| e9 | relation | m0 | m4 | high | on |
| e10 | relation | m6 | m7 | high | in |

## 68

**caption_shape:** `multi-sentence`
**caption_id:** `35393afd2046cb36424127001a7c11fd60ac76df2218391c52e6f0a687b6c014`

> A long, rusty metal pipe runs diagonally across a lush green hillside. It is supported by concrete blocks and surrounded by dense foliage and trees under bright sunlight.

### Sentences
| sentence | token_span |
| --- | --- |
| A long, rusty metal pipe runs diagonally across a lush green hillside. | 0:14 |
| It is supported by concrete blocks and surrounded by dense foliage and trees under bright sunlight. | 14:31 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A long, rusty metal pipe | pipe | pipe | nsubj | runs | 0:6 |
| a lush green hillside | hillside | hillside | pobj | across | 9:13 |
| It | It | it | nsubjpass | supported | 14:15 |
| concrete blocks | blocks | block | pobj | by | 18:20 |
| dense foliage | foliage | foliage | pobj | by | 23:25 |
| trees | trees | tree | conj | foliage | 26:27 |
| bright sunlight | sunlight | sunlight | pobj | under | 28:30 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | pipe | 5 |
| 1 | long | long | ADJ | JJ | amod | pipe | 5 |
| 2 | , | , | PUNCT | , | punct | pipe | 5 |
| 3 | rusty | rusty | ADJ | JJ | amod | pipe | 5 |
| 4 | metal | metal | NOUN | NN | compound | pipe | 5 |
| 5 | pipe | pipe | NOUN | NN | nsubj | runs | 6 |
| 6 | runs | run | VERB | VBZ | ROOT | runs | 6 |
| 7 | diagonally | diagonally | ADV | RB | advmod | runs | 6 |
| 8 | across | across | ADP | IN | prep | runs | 6 |
| 9 | a | a | DET | DT | det | hillside | 12 |
| 10 | lush | lush | ADJ | JJ | amod | hillside | 12 |
| 11 | green | green | ADJ | JJ | amod | hillside | 12 |
| 12 | hillside | hillside | NOUN | NN | pobj | across | 8 |
| 13 | . | . | PUNCT | . | punct | runs | 6 |
| 14 | It | it | PRON | PRP | nsubjpass | supported | 16 |
| 15 | is | be | AUX | VBZ | auxpass | supported | 16 |
| 16 | supported | support | VERB | VBN | ROOT | supported | 16 |
| 17 | by | by | ADP | IN | agent | supported | 16 |
| 18 | concrete | concrete | NOUN | NN | compound | blocks | 19 |
| 19 | blocks | block | NOUN | NNS | pobj | by | 17 |
| 20 | and | and | CCONJ | CC | cc | supported | 16 |
| 21 | surrounded | surround | VERB | VBN | conj | supported | 16 |
| 22 | by | by | ADP | IN | agent | surrounded | 21 |
| 23 | dense | dense | ADJ | JJ | amod | foliage | 24 |
| 24 | foliage | foliage | NOUN | NN | pobj | by | 22 |
| 25 | and | and | CCONJ | CC | cc | foliage | 24 |
| 26 | trees | tree | NOUN | NNS | conj | foliage | 24 |
| 27 | under | under | ADP | IN | prep | surrounded | 21 |
| 28 | bright | bright | ADJ | JJ | amod | sunlight | 29 |
| 29 | sunlight | sunlight | NOUN | NN | pobj | under | 27 |
| 30 | . | . | PUNCT | . | punct | supported | 16 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | pipe | pipe | chunk0 | 5 | noun_chunk_root | high |
| m1 | attribute | long | long | chunk0 | 1 | size_attribute | high |
| m2 | attribute | rusty | rusty | chunk0 | 3 | modifier_attribute | medium |
| m3 | attribute | metal | metal | chunk0 | 4 | material_attribute | high |
| m4 | object | hillside | hillside | chunk1 | 12 | noun_chunk_root | high |
| m5 | attribute | lush | lush | chunk1 | 10 | modifier_attribute | medium |
| m6 | attribute | green | green | chunk1 | 11 | color_attribute | high |
| m7 | object | It | it | chunk2 | 14 | noun_chunk_root | high |
| m8 | object | blocks | block | chunk3 | 19 | noun_chunk_root | high |
| m9 | attribute | concrete | concrete | chunk3 | 18 | material_attribute | high |
| m10 | object | foliage | foliage | chunk4 | 24 | noun_chunk_root | high |
| m11 | attribute | dense | dense | chunk4 | 23 | modifier_attribute | medium |
| m12 | object | trees | tree | chunk5 | 26 | noun_chunk_root | high |
| m13 | object | sunlight | sunlight | chunk6 | 29 | noun_chunk_root | high |
| m14 | attribute | bright | bright | chunk6 | 28 | visual_attribute | medium |
| m15 | action | runs | run | doc | 6 | verb_predicate | high |
| m16 | action | supported | support | doc | 16 | verb_predicate | high |
| m17 | action | surrounded | surround | doc | 21 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> pipe |
| e1 | has_attribute | m0 | m2 | medium | chunk0 amod -> pipe |
| e2 | has_attribute | m0 | m3 | high | chunk0 compound -> pipe |
| e3 | has_attribute | m4 | m5 | medium | chunk1 amod -> hillside |
| e4 | has_attribute | m4 | m6 | high | chunk1 amod -> hillside |
| e5 | has_attribute | m8 | m9 | high | chunk3 compound -> blocks |
| e6 | has_attribute | m10 | m11 | medium | chunk4 amod -> foliage |
| e7 | has_attribute | m13 | m14 | medium | chunk6 amod -> sunlight |
| e8 | agent | m15 | m0 | medium | nsubj -> runs |
| e9 | agent | m16 | m7 | medium | nsubjpass -> supported |
| e10 | relation | m0 | m4 | high | across |
| e11 | relation | m7 | m8 | medium | by |
| e12 | relation | m7 | m10 | medium | by |
| e13 | relation | m7 | m12 | medium | by |
| e14 | relation | m7 | m13 | high | under |

## 69

**caption_shape:** `sentence-like`
**caption_id:** `364c26cb7e32d9e444ebc8af7227977754b9c5bfd04f524c894693089c490414`

> A woman with long hair speaks while gesturing with both hands against a dark background.

### Sentences
| sentence | token_span |
| --- | --- |
| A woman with long hair speaks while gesturing with both hands against a dark background. | 0:16 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A woman | woman | woman | nsubj | speaks | 0:2 |
| long hair | hair | hair | pobj | with | 3:5 |
| both hands | hands | hand | pobj | with | 9:11 |
| a dark background | background | background | pobj | against | 12:15 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | woman | 1 |
| 1 | woman | woman | NOUN | NN | nsubj | speaks | 5 |
| 2 | with | with | ADP | IN | prep | woman | 1 |
| 3 | long | long | ADJ | JJ | amod | hair | 4 |
| 4 | hair | hair | NOUN | NN | pobj | with | 2 |
| 5 | speaks | speak | VERB | VBZ | ROOT | speaks | 5 |
| 6 | while | while | SCONJ | IN | mark | gesturing | 7 |
| 7 | gesturing | gesture | VERB | VBG | advcl | speaks | 5 |
| 8 | with | with | ADP | IN | prep | gesturing | 7 |
| 9 | both | both | DET | DT | det | hands | 10 |
| 10 | hands | hand | NOUN | NNS | pobj | with | 8 |
| 11 | against | against | ADP | IN | prep | gesturing | 7 |
| 12 | a | a | DET | DT | det | background | 14 |
| 13 | dark | dark | ADJ | JJ | amod | background | 14 |
| 14 | background | background | NOUN | NN | pobj | against | 11 |
| 15 | . | . | PUNCT | . | punct | speaks | 5 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | hair | hair | chunk1 | 4 | noun_chunk_root | high |
| m2 | attribute | long | long | chunk1 | 3 | size_attribute | high |
| m3 | object | hands | hand | chunk2 | 10 | noun_chunk_root | high |
| m4 | object | background | background | chunk3 | 14 | noun_chunk_root | high |
| m5 | attribute | dark | dark | chunk3 | 13 | visual_attribute | medium |
| m6 | context | background | background | doc | 14 | context_word | medium |
| m7 | action | speaks | speak | doc | 5 | verb_predicate | high |
| m8 | action | gesturing | gesture | doc | 7 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> hair |
| e1 | has_attribute | m4 | m5 | medium | chunk3 amod -> background |
| e2 | has_context | scene | m6 | medium | context token background |
| e3 | agent | m7 | m0 | medium | nsubj -> speaks |
| e4 | relation | m0 | m1 | high | with |
| e5 | relation | m0 | m3 | high | with |
| e6 | relation | m0 | m6 | high | against |

## 70

**caption_shape:** `multi-sentence`
**caption_id:** `37399b25943350293d011927c3fbd226e1c5e79dea38f98134b620ef8ccfbc14`

> A rocky, steamy crater with mist rising from its edge. The ground is covered in dark, rough stones and patches of white material.

### Sentences
| sentence | token_span |
| --- | --- |
| A rocky, steamy crater with mist rising from its edge. | 0:12 |
| The ground is covered in dark, rough stones and patches of white material. | 12:27 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A rocky, steamy crater | crater | crater | ROOT | crater | 0:5 |
| mist | mist | mist | pobj | with | 6:7 |
| its edge | edge | edge | pobj | from | 9:11 |
| The ground | ground | ground | nsubjpass | covered | 12:14 |
| dark, rough stones | stones | stone | pobj | in | 17:21 |
| patches | patches | patch | conj | stones | 22:23 |
| white material | material | material | pobj | of | 24:26 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | crater | 4 |
| 1 | rocky | rocky | ADJ | JJ | amod | crater | 4 |
| 2 | , | , | PUNCT | , | punct | crater | 4 |
| 3 | steamy | steamy | ADJ | JJ | amod | crater | 4 |
| 4 | crater | crater | NOUN | NN | ROOT | crater | 4 |
| 5 | with | with | ADP | IN | prep | crater | 4 |
| 6 | mist | mist | NOUN | NN | pobj | with | 5 |
| 7 | rising | rise | VERB | VBG | acl | mist | 6 |
| 8 | from | from | ADP | IN | prep | rising | 7 |
| 9 | its | its | PRON | PRP$ | poss | edge | 10 |
| 10 | edge | edge | NOUN | NN | pobj | from | 8 |
| 11 | . | . | PUNCT | . | punct | crater | 4 |
| 12 | The | the | DET | DT | det | ground | 13 |
| 13 | ground | ground | NOUN | NN | nsubjpass | covered | 15 |
| 14 | is | be | AUX | VBZ | auxpass | covered | 15 |
| 15 | covered | cover | VERB | VBN | ROOT | covered | 15 |
| 16 | in | in | ADP | IN | prep | covered | 15 |
| 17 | dark | dark | ADJ | JJ | amod | stones | 20 |
| 18 | , | , | PUNCT | , | punct | stones | 20 |
| 19 | rough | rough | ADJ | JJ | amod | stones | 20 |
| 20 | stones | stone | NOUN | NNS | pobj | in | 16 |
| 21 | and | and | CCONJ | CC | cc | stones | 20 |
| 22 | patches | patch | NOUN | NNS | conj | stones | 20 |
| 23 | of | of | ADP | IN | prep | patches | 22 |
| 24 | white | white | ADJ | JJ | amod | material | 25 |
| 25 | material | material | NOUN | NN | pobj | of | 23 |
| 26 | . | . | PUNCT | . | punct | covered | 15 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | crater | crater | chunk0 | 4 | noun_chunk_root | high |
| m1 | attribute | rocky | rocky | chunk0 | 1 | modifier_attribute | medium |
| m2 | attribute | steamy | steamy | chunk0 | 3 | modifier_attribute | medium |
| m3 | object | mist | mist | chunk1 | 6 | noun_chunk_root | high |
| m4 | context | edge | edge | chunk2 | 10 | spatial_region | medium |
| m5 | object | ground | ground | chunk3 | 13 | noun_chunk_root | high |
| m6 | object | stones | stone | chunk4 | 20 | noun_chunk_root | high |
| m7 | attribute | dark | dark | chunk4 | 17 | visual_attribute | medium |
| m8 | attribute | rough | rough | chunk4 | 19 | modifier_attribute | medium |
| m9 | object | patches | patch | chunk5 | 22 | noun_chunk_root | high |
| m10 | object | material | material | chunk6 | 25 | noun_chunk_root | high |
| m11 | attribute | white | white | chunk6 | 24 | color_attribute | high |
| m12 | action | rising | rise | doc | 7 | verb_predicate | high |
| m13 | action | covered | cover | doc | 15 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> crater |
| e1 | has_attribute | m0 | m2 | medium | chunk0 amod -> crater |
| e2 | has_attribute | m6 | m7 | medium | chunk4 amod -> stones |
| e3 | has_attribute | m6 | m8 | medium | chunk4 amod -> stones |
| e4 | has_attribute | m10 | m11 | high | chunk6 amod -> material |
| e5 | agent | m13 | m5 | medium | nsubjpass -> covered |
| e6 | relation | m0 | m3 | high | with |
| e7 | relation | m3 | m4 | medium | from |
| e8 | relation | m5 | m6 | high | in |
| e9 | relation | m5 | m9 | high | in |
| e10 | relation | m9 | m10 | medium | of |

## 71

**caption_shape:** `sentence-like`
**caption_id:** `37d073e88ed18fd0db9727b4d89445dfd62a421b6926982817521f733def6c14`

> A table shows statistics for various regions of the Russian Empire, including numbers and percentages.

### Sentences
| sentence | token_span |
| --- | --- |
| A table shows statistics for various regions of the Russian Empire, including numbers and percentages. | 0:17 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A table | table | table | nsubj | shows | 0:2 |
| statistics | statistics | statistic | dobj | shows | 3:4 |
| various regions | regions | region | pobj | for | 5:7 |
| the Russian Empire | Empire | Empire | pobj | of | 8:11 |
| numbers | numbers | number | pobj | including | 13:14 |
| percentages | percentages | percentage | conj | numbers | 15:16 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | table | 1 |
| 1 | table | table | NOUN | NN | nsubj | shows | 2 |
| 2 | shows | show | VERB | VBZ | ROOT | shows | 2 |
| 3 | statistics | statistic | NOUN | NNS | dobj | shows | 2 |
| 4 | for | for | ADP | IN | prep | statistics | 3 |
| 5 | various | various | ADJ | JJ | amod | regions | 6 |
| 6 | regions | region | NOUN | NNS | pobj | for | 4 |
| 7 | of | of | ADP | IN | prep | regions | 6 |
| 8 | the | the | DET | DT | det | Empire | 10 |
| 9 | Russian | Russian | PROPN | NNP | compound | Empire | 10 |
| 10 | Empire | Empire | PROPN | NNP | pobj | of | 7 |
| 11 | , | , | PUNCT | , | punct | statistics | 3 |
| 12 | including | include | VERB | VBG | prep | statistics | 3 |
| 13 | numbers | number | NOUN | NNS | pobj | including | 12 |
| 14 | and | and | CCONJ | CC | cc | numbers | 13 |
| 15 | percentages | percentage | NOUN | NNS | conj | numbers | 13 |
| 16 | . | . | PUNCT | . | punct | shows | 2 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | table | table | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | statistics | statistic | chunk1 | 3 | noun_chunk_root | high |
| m2 | object | regions | region | chunk2 | 6 | noun_chunk_root | high |
| m3 | attribute | various | various | chunk2 | 5 | modifier_attribute | medium |
| m4 | object | Empire | empire | chunk3 | 10 | noun_chunk_root | high |
| m5 | attribute | Russian | russian | chunk3 | 9 | compound_modifier | medium |
| m6 | object | numbers | number | chunk4 | 13 | noun_chunk_root | high |
| m7 | object | percentages | percentage | chunk5 | 15 | noun_chunk_root | high |
| m8 | action | shows | show | doc | 2 | verb_predicate | high |
| m9 | action | including | include | doc | 12 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | medium | chunk2 amod -> regions |
| e1 | has_attribute | m4 | m5 | medium | chunk3 compound -> Empire |
| e2 | agent | m8 | m0 | medium | nsubj -> shows |
| e3 | patient | m8 | m1 | medium | dobj -> shows |
| e4 | patient | m9 | m6 | medium | pobj -> including |
| e5 | patient | m9 | m7 | medium | pobj -> including |
| e6 | relation | m1 | m2 | medium | for |
| e7 | relation | m2 | m4 | medium | of |
| e8 | relation | m1 | m6 | medium | include |
| e9 | relation | m1 | m7 | medium | include |

## 72

**caption_shape:** `multi-sentence`
**caption_id:** `3a18b4bdc7ca12c3129ed90ba2b225be2e83234f2f1de35bd8cf9e137192e414`

> A yellow dog with wide eyes and an open mouth stands in a dark room. A bright red balloon is visible to the right, contrasting with the black-and-white background. The dog appears to be looking directly at the camera.

### Sentences
| sentence | token_span |
| --- | --- |
| A yellow dog with wide eyes and an open mouth stands in a dark room. | 0:16 |
| A bright red balloon is visible to the right, contrasting with the black-and-white background. | 16:32 |
| The dog appears to be looking directly at the camera. | 32:43 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A yellow dog | dog | dog | nsubj | stands | 0:3 |
| wide eyes | eyes | eye | pobj | with | 4:6 |
| an open mouth | mouth | mouth | conj | eyes | 7:10 |
| a dark room | room | room | pobj | in | 12:15 |
| A bright red balloon | balloon | balloon | nsubj | is | 16:20 |
| the right | right | right | pobj | to | 23:25 |
| the black-and-white background | background | background | pobj | with | 28:31 |
| The dog | dog | dog | nsubj | appears | 32:34 |
| the camera | camera | camera | pobj | at | 40:42 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | dog | 2 |
| 1 | yellow | yellow | ADJ | JJ | amod | dog | 2 |
| 2 | dog | dog | NOUN | NN | nsubj | stands | 10 |
| 3 | with | with | ADP | IN | prep | dog | 2 |
| 4 | wide | wide | ADJ | JJ | amod | eyes | 5 |
| 5 | eyes | eye | NOUN | NNS | pobj | with | 3 |
| 6 | and | and | CCONJ | CC | cc | eyes | 5 |
| 7 | an | an | DET | DT | det | mouth | 9 |
| 8 | open | open | ADJ | JJ | amod | mouth | 9 |
| 9 | mouth | mouth | NOUN | NN | conj | eyes | 5 |
| 10 | stands | stand | VERB | VBZ | ROOT | stands | 10 |
| 11 | in | in | ADP | IN | prep | stands | 10 |
| 12 | a | a | DET | DT | det | room | 14 |
| 13 | dark | dark | ADJ | JJ | amod | room | 14 |
| 14 | room | room | NOUN | NN | pobj | in | 11 |
| 15 | . | . | PUNCT | . | punct | stands | 10 |
| 16 | A | a | DET | DT | det | balloon | 19 |
| 17 | bright | bright | ADJ | JJ | amod | red | 18 |
| 18 | red | red | ADJ | JJ | amod | balloon | 19 |
| 19 | balloon | balloon | NOUN | NN | nsubj | is | 20 |
| 20 | is | be | AUX | VBZ | ROOT | is | 20 |
| 21 | visible | visible | ADJ | JJ | acomp | is | 20 |
| 22 | to | to | ADP | IN | prep | visible | 21 |
| 23 | the | the | DET | DT | det | right | 24 |
| 24 | right | right | NOUN | NN | pobj | to | 22 |
| 25 | , | , | PUNCT | , | punct | is | 20 |
| 26 | contrasting | contrast | VERB | VBG | advcl | is | 20 |
| 27 | with | with | ADP | IN | prep | contrasting | 26 |
| 28 | the | the | DET | DT | det | background | 30 |
| 29 | black-and-white | black-and-white | ADJ | JJ | amod | background | 30 |
| 30 | background | background | NOUN | NN | pobj | with | 27 |
| 31 | . | . | PUNCT | . | punct | is | 20 |
| 32 | The | the | DET | DT | det | dog | 33 |
| 33 | dog | dog | NOUN | NN | nsubj | appears | 34 |
| 34 | appears | appear | VERB | VBZ | ROOT | appears | 34 |
| 35 | to | to | PART | TO | aux | looking | 37 |
| 36 | be | be | AUX | VB | aux | looking | 37 |
| 37 | looking | look | VERB | VBG | xcomp | appears | 34 |
| 38 | directly | directly | ADV | RB | advmod | looking | 37 |
| 39 | at | at | ADP | IN | prep | looking | 37 |
| 40 | the | the | DET | DT | det | camera | 41 |
| 41 | camera | camera | NOUN | NN | pobj | at | 39 |
| 42 | . | . | PUNCT | . | punct | appears | 34 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | dog | dog | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | yellow | yellow | chunk0 | 1 | color_attribute | high |
| m2 | object | eyes | eye | chunk1 | 5 | noun_chunk_root | high |
| m3 | attribute | wide | wide | chunk1 | 4 | size_attribute | high |
| m4 | object | mouth | mouth | chunk2 | 9 | noun_chunk_root | high |
| m5 | attribute | open | open | chunk2 | 8 | modifier_attribute | medium |
| m6 | object | room | room | chunk3 | 14 | noun_chunk_root | high |
| m7 | attribute | dark | dark | chunk3 | 13 | visual_attribute | medium |
| m8 | object | balloon | balloon | chunk4 | 19 | noun_chunk_root | high |
| m9 | attribute | bright | bright | chunk4 | 17 | visual_attribute | medium |
| m10 | attribute | red | red | chunk4 | 18 | color_attribute | high |
| m11 | object | right | right | chunk5 | 24 | noun_chunk_root | high |
| m12 | object | background | background | chunk6 | 30 | noun_chunk_root | high |
| m13 | attribute | black-and-white | black-and-white | chunk6 | 29 | modifier_attribute | medium |
| m14 | object | dog | dog | chunk7 | 33 | noun_chunk_root | high |
| m15 | object | camera | camera | chunk8 | 41 | noun_chunk_root | high |
| m16 | context | background | background | doc | 30 | context_word | medium |
| m17 | action | stands | stand | doc | 10 | verb_predicate | high |
| m18 | action | contrasting | contrast | doc | 26 | verb_predicate | high |
| m19 | action | appears | appear | doc | 34 | verb_predicate | high |
| m20 | action | looking | look | doc | 37 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> dog |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> eyes |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> mouth |
| e3 | has_attribute | m6 | m7 | medium | chunk3 amod -> room |
| e4 | has_attribute | m8 | m9 | medium | chunk4 amod -> balloon |
| e5 | has_attribute | m8 | m10 | high | chunk4 amod -> balloon |
| e6 | has_attribute | m12 | m13 | medium | chunk6 amod -> background |
| e7 | has_context | scene | m16 | medium | context token background |
| e8 | agent | m17 | m0 | medium | nsubj -> stands |
| e9 | agent | m19 | m14 | medium | nsubj -> appears |
| e10 | relation | m0 | m2 | high | with |
| e11 | relation | m0 | m4 | high | with |
| e12 | relation | m0 | m6 | high | in |
| e13 | relation | m8 | m16 | high | with |
| e14 | relation | m14 | m15 | medium | at |

## 73

**caption_shape:** `multi-sentence`
**caption_id:** `3a3e745a8aea22b051a37ba29b47fd4059bb427e9b44d0d3f43bba15c3703c14`

> A gray building with a blue lower section and red trim stands behind a green fence. A concrete area with puddles is in the foreground, and stairs lead up to the building’s entrance. The sky is overcast, and grass grows around the base of the structure.

### Sentences
| sentence | token_span |
| --- | --- |
| A gray building with a blue lower section and red trim stands behind a green fence. | 0:17 |
| A concrete area with puddles is in the foreground, and stairs lead up to the building’s entrance. | 17:37 |
| The sky is overcast, and grass grows around the base of the structure. | 37:52 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A gray building | building | building | nsubj | stands | 0:3 |
| a blue lower section | section | section | pobj | with | 4:8 |
| red trim | trim | trim | conj | section | 9:11 |
| a green fence | fence | fence | pobj | behind | 13:16 |
| A concrete area | area | area | nsubj | is | 17:20 |
| puddles | puddles | puddle | pobj | with | 21:22 |
| the foreground | foreground | foreground | pobj | in | 24:26 |
| stairs | stairs | stair | nsubj | lead | 28:29 |
| the building’s entrance | entrance | entrance | pobj | to | 32:36 |
| The sky | sky | sky | nsubj | is | 37:39 |
| grass | grass | grass | nsubj | grows | 43:44 |
| the base | base | base | pobj | around | 46:48 |
| the structure | structure | structure | pobj | of | 49:51 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | building | 2 |
| 1 | gray | gray | ADJ | JJ | amod | building | 2 |
| 2 | building | building | NOUN | NN | nsubj | stands | 11 |
| 3 | with | with | ADP | IN | prep | building | 2 |
| 4 | a | a | DET | DT | det | section | 7 |
| 5 | blue | blue | ADJ | JJ | amod | section | 7 |
| 6 | lower | low | ADJ | JJR | amod | section | 7 |
| 7 | section | section | NOUN | NN | pobj | with | 3 |
| 8 | and | and | CCONJ | CC | cc | section | 7 |
| 9 | red | red | ADJ | JJ | amod | trim | 10 |
| 10 | trim | trim | NOUN | NN | conj | section | 7 |
| 11 | stands | stand | VERB | VBZ | ROOT | stands | 11 |
| 12 | behind | behind | ADP | IN | prep | stands | 11 |
| 13 | a | a | DET | DT | det | fence | 15 |
| 14 | green | green | ADJ | JJ | amod | fence | 15 |
| 15 | fence | fence | NOUN | NN | pobj | behind | 12 |
| 16 | . | . | PUNCT | . | punct | stands | 11 |
| 17 | A | a | DET | DT | det | area | 19 |
| 18 | concrete | concrete | ADJ | JJ | amod | area | 19 |
| 19 | area | area | NOUN | NN | nsubj | is | 22 |
| 20 | with | with | ADP | IN | prep | area | 19 |
| 21 | puddles | puddle | NOUN | NNS | pobj | with | 20 |
| 22 | is | be | AUX | VBZ | ROOT | is | 22 |
| 23 | in | in | ADP | IN | prep | is | 22 |
| 24 | the | the | DET | DT | det | foreground | 25 |
| 25 | foreground | foreground | NOUN | NN | pobj | in | 23 |
| 26 | , | , | PUNCT | , | punct | is | 22 |
| 27 | and | and | CCONJ | CC | cc | is | 22 |
| 28 | stairs | stair | NOUN | NNS | nsubj | lead | 29 |
| 29 | lead | lead | VERB | VBP | conj | is | 22 |
| 30 | up | up | ADP | RP | prt | lead | 29 |
| 31 | to | to | ADP | IN | prep | lead | 29 |
| 32 | the | the | DET | DT | det | building | 33 |
| 33 | building | building | NOUN | NN | poss | entrance | 35 |
| 34 | ’s | ’s | PART | POS | case | building | 33 |
| 35 | entrance | entrance | NOUN | NN | pobj | to | 31 |
| 36 | . | . | PUNCT | . | punct | lead | 29 |
| 37 | The | the | DET | DT | det | sky | 38 |
| 38 | sky | sky | NOUN | NN | nsubj | is | 39 |
| 39 | is | be | AUX | VBZ | ROOT | is | 39 |
| 40 | overcast | overcast | ADJ | JJ | acomp | is | 39 |
| 41 | , | , | PUNCT | , | punct | is | 39 |
| 42 | and | and | CCONJ | CC | cc | is | 39 |
| 43 | grass | grass | NOUN | NN | nsubj | grows | 44 |
| 44 | grows | grow | VERB | VBZ | conj | is | 39 |
| 45 | around | around | ADP | IN | prep | grows | 44 |
| 46 | the | the | DET | DT | det | base | 47 |
| 47 | base | base | NOUN | NN | pobj | around | 45 |
| 48 | of | of | ADP | IN | prep | base | 47 |
| 49 | the | the | DET | DT | det | structure | 50 |
| 50 | structure | structure | NOUN | NN | pobj | of | 48 |
| 51 | . | . | PUNCT | . | punct | grows | 44 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | gray | gray | chunk0 | 1 | color_attribute | high |
| m2 | object | section | section | chunk1 | 7 | noun_chunk_root | high |
| m3 | attribute | blue | blue | chunk1 | 5 | color_attribute | high |
| m4 | attribute | lower | low | chunk1 | 6 | modifier_attribute | medium |
| m5 | object | trim | trim | chunk2 | 10 | noun_chunk_root | high |
| m6 | attribute | red | red | chunk2 | 9 | color_attribute | high |
| m7 | object | fence | fence | chunk3 | 15 | noun_chunk_root | high |
| m8 | attribute | green | green | chunk3 | 14 | color_attribute | high |
| m9 | object | area | area | chunk4 | 19 | noun_chunk_root | high |
| m10 | attribute | concrete | concrete | chunk4 | 18 | material_attribute | high |
| m11 | object | puddles | puddle | chunk5 | 21 | noun_chunk_root | high |
| m12 | object | foreground | foreground | chunk6 | 25 | noun_chunk_root | high |
| m13 | object | stairs | stair | chunk7 | 28 | noun_chunk_root | high |
| m14 | object | entrance | entrance | chunk8 | 35 | noun_chunk_root | high |
| m15 | attribute | building | building | chunk8 | 33 | modifier_attribute | medium |
| m16 | object | sky | sky | chunk9 | 38 | noun_chunk_root | high |
| m17 | object | grass | grass | chunk10 | 43 | noun_chunk_root | high |
| m18 | object | base | base | chunk11 | 47 | noun_chunk_root | high |
| m19 | object | structure | structure | chunk12 | 50 | noun_chunk_root | high |
| m20 | context | foreground | foreground | doc | 25 | context_word | medium |
| m21 | action | stands | stand | doc | 11 | verb_predicate | high |
| m22 | action | lead | lead | doc | 29 | verb_predicate | high |
| m23 | action | grows | grow | doc | 44 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> building |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> section |
| e2 | has_attribute | m2 | m4 | medium | chunk1 amod -> section |
| e3 | has_attribute | m5 | m6 | high | chunk2 amod -> trim |
| e4 | has_attribute | m7 | m8 | high | chunk3 amod -> fence |
| e5 | has_attribute | m9 | m10 | high | chunk4 amod -> area |
| e6 | has_attribute | m14 | m15 | medium | chunk8 poss -> entrance |
| e7 | has_context | scene | m20 | medium | context token foreground |
| e8 | agent | m21 | m0 | medium | nsubj -> stands |
| e9 | agent | m22 | m13 | medium | nsubj -> lead |
| e10 | agent | m23 | m17 | medium | nsubj -> grows |
| e11 | relation | m0 | m2 | high | with |
| e12 | relation | m0 | m5 | high | with |
| e13 | relation | m0 | m7 | high | behind |
| e14 | relation | m9 | m11 | high | with |
| e15 | relation | m9 | m20 | high | in |
| e16 | relation | m13 | m14 | medium | to |
| e17 | relation | m17 | m18 | high | around |
| e18 | relation | m18 | m19 | medium | of |

## 74

**caption_shape:** `multi-sentence`
**caption_id:** `3a94bef6569e8de11d6f22d1351ebabb5559cbd80977398b0ed11b3f5a3be414`

> A man in a blue suit stands at a wooden podium speaking into microphones. To his left, a man in a gray suit sits with a mask on, and to his right, a woman in a yellow jacket sits with a mask on. They are in front of a backdrop with "Philadelphia Flyers" logos and text.

**parsed_caption:**

> A man in a blue suit stands at a wooden podium speaking into microphones. To his left, a man in a gray suit sits with a mask on, and to his right, a woman in a yellow jacket sits with a mask on. They are in front of a backdrop with "Philadelphia Flyers" logos and text.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 3a94bef6569e8de11d6f22d1351ebabb5559cbd80977398b0ed11b3f5a3be414:q0 | Philadelphia Flyers | philadelphia flyers | raw_quote_span |  | 232:253 | 232:253 |

### Sentences
| sentence | token_span |
| --- | --- |
| A man in a blue suit stands at a wooden podium speaking into microphones. | 0:15 |
| To his left, a man in a gray suit sits with a mask on, and to his right, a woman in a yellow jacket sits with a mask on. | 15:48 |
| They are in front of a backdrop with "Philadelphia Flyers" logos and text. | 48:61 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A man | man | man | nsubj | stands | 0:2 |
| a blue suit | suit | suit | pobj | in | 3:6 |
| a wooden podium | podium | podium | pobj | at | 8:11 |
| microphones | microphones | microphone | pobj | into | 13:14 |
| his left | left | left | pobj | To | 16:18 |
| a man | man | man | nsubj | sits | 19:21 |
| a gray suit | suit | suit | pobj | in | 22:25 |
| a mask | mask | mask | nsubj | on | 27:29 |
| his right | right | right | pobj | to | 33:35 |
| a woman | woman | woman | nsubj | sits | 36:38 |
| a yellow jacket | jacket | jacket | pobj | in | 39:42 |
| a mask | mask | mask | nsubj | on | 44:46 |
| They | They | they | nsubj | are | 48:49 |
| front | front | front | pobj | in | 51:52 |
| a backdrop | backdrop | backdrop | pobj | of | 53:55 |
| "Philadelphia Flyers" logos | logos | logo | pobj | with | 56:58 |
| text | text | text | conj | logos | 59:60 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | man | 1 |
| 1 | man | man | NOUN | NN | nsubj | stands | 6 |
| 2 | in | in | ADP | IN | prep | man | 1 |
| 3 | a | a | DET | DT | det | suit | 5 |
| 4 | blue | blue | ADJ | JJ | amod | suit | 5 |
| 5 | suit | suit | NOUN | NN | pobj | in | 2 |
| 6 | stands | stand | VERB | VBZ | ROOT | stands | 6 |
| 7 | at | at | ADP | IN | prep | stands | 6 |
| 8 | a | a | DET | DT | det | podium | 10 |
| 9 | wooden | wooden | ADJ | JJ | amod | podium | 10 |
| 10 | podium | podium | NOUN | NN | pobj | at | 7 |
| 11 | speaking | speak | VERB | VBG | advcl | stands | 6 |
| 12 | into | into | ADP | IN | prep | speaking | 11 |
| 13 | microphones | microphone | NOUN | NNS | pobj | into | 12 |
| 14 | . | . | PUNCT | . | punct | stands | 6 |
| 15 | To | to | ADP | IN | prep | sits | 25 |
| 16 | his | his | PRON | PRP$ | poss | left | 17 |
| 17 | left | left | NOUN | NN | pobj | To | 15 |
| 18 | , | , | PUNCT | , | punct | sits | 25 |
| 19 | a | a | DET | DT | det | man | 20 |
| 20 | man | man | NOUN | NN | nsubj | sits | 25 |
| 21 | in | in | ADP | IN | prep | man | 20 |
| 22 | a | a | DET | DT | det | suit | 24 |
| 23 | gray | gray | ADJ | JJ | amod | suit | 24 |
| 24 | suit | suit | NOUN | NN | pobj | in | 21 |
| 25 | sits | sit | VERB | VBZ | ROOT | sits | 25 |
| 26 | with | with | ADP | IN | prep | sits | 25 |
| 27 | a | a | DET | DT | det | mask | 28 |
| 28 | mask | mask | NOUN | NN | nsubj | on | 29 |
| 29 | on | on | ADV | RB | pcomp | with | 26 |
| 30 | , | , | PUNCT | , | punct | sits | 25 |
| 31 | and | and | CCONJ | CC | cc | sits | 25 |
| 32 | to | to | ADP | IN | prep | sits | 42 |
| 33 | his | his | PRON | PRP$ | poss | right | 34 |
| 34 | right | right | NOUN | NN | pobj | to | 32 |
| 35 | , | , | PUNCT | , | punct | sits | 42 |
| 36 | a | a | DET | DT | det | woman | 37 |
| 37 | woman | woman | NOUN | NN | nsubj | sits | 42 |
| 38 | in | in | ADP | IN | prep | woman | 37 |
| 39 | a | a | DET | DT | det | jacket | 41 |
| 40 | yellow | yellow | ADJ | JJ | amod | jacket | 41 |
| 41 | jacket | jacket | NOUN | NN | pobj | in | 38 |
| 42 | sits | sit | VERB | VBZ | conj | sits | 25 |
| 43 | with | with | ADP | IN | prep | sits | 42 |
| 44 | a | a | DET | DT | det | mask | 45 |
| 45 | mask | mask | NOUN | NN | nsubj | on | 46 |
| 46 | on | on | ADV | RB | pcomp | with | 43 |
| 47 | . | . | PUNCT | . | punct | sits | 42 |
| 48 | They | they | PRON | PRP | nsubj | are | 49 |
| 49 | are | be | AUX | VBP | ROOT | are | 49 |
| 50 | in | in | ADP | IN | prep | are | 49 |
| 51 | front | front | NOUN | NN | pobj | in | 50 |
| 52 | of | of | ADP | IN | prep | front | 51 |
| 53 | a | a | DET | DT | det | backdrop | 54 |
| 54 | backdrop | backdrop | NOUN | NN | pobj | of | 52 |
| 55 | with | with | ADP | IN | prep | backdrop | 54 |
| 56 | "Philadelphia Flyers" | philadelphia_flyers | PROPN | NNP | punct | logos | 57 |
| 57 | logos | logo | NOUN | NNS | pobj | with | 55 |
| 58 | and | and | CCONJ | CC | cc | logos | 57 |
| 59 | text | text | NOUN | NN | conj | logos | 57 |
| 60 | . | . | PUNCT | . | punct | are | 49 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | suit | suit | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | blue | blue | chunk1 | 4 | color_attribute | high |
| m3 | object | podium | podium | chunk2 | 10 | noun_chunk_root | high |
| m4 | attribute | wooden | wooden | chunk2 | 9 | material_attribute | high |
| m5 | object | microphones | microphone | chunk3 | 13 | noun_chunk_root | high |
| m6 | object | left | left | chunk4 | 17 | noun_chunk_root | high |
| m7 | attribute | his | his | chunk4 | 16 | modifier_attribute | medium |
| m8 | object | man | man | chunk5 | 20 | noun_chunk_root | high |
| m9 | object | suit | suit | chunk6 | 24 | noun_chunk_root | high |
| m10 | attribute | gray | gray | chunk6 | 23 | color_attribute | high |
| m11 | object | mask | mask | chunk7 | 28 | noun_chunk_root | high |
| m12 | object | right | right | chunk8 | 34 | noun_chunk_root | high |
| m13 | attribute | his | his | chunk8 | 33 | modifier_attribute | medium |
| m14 | object | woman | woman | chunk9 | 37 | noun_chunk_root | high |
| m15 | object | jacket | jacket | chunk10 | 41 | noun_chunk_root | high |
| m16 | attribute | yellow | yellow | chunk10 | 40 | color_attribute | high |
| m17 | object | mask | mask | chunk11 | 45 | noun_chunk_root | high |
| m18 | object | They | they | chunk12 | 48 | noun_chunk_root | high |
| m19 | object | backdrop | backdrop | chunk14 | 54 | noun_chunk_root | high |
| m20 | object | logos | logo | chunk15 | 57 | noun_chunk_root | high |
| m21 | object | text | text | chunk16 | 59 | noun_chunk_root | high |
| m22 | action | stands | stand | doc | 6 | verb_predicate | high |
| m23 | action | speaking | speak | doc | 11 | verb_predicate | high |
| m24 | action | sits | sit | doc | 25 | verb_predicate | high |
| m25 | action | sits | sit | doc | 42 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> suit |
| e1 | has_attribute | m3 | m4 | high | chunk2 amod -> podium |
| e2 | has_attribute | m6 | m7 | medium | chunk4 poss -> left |
| e3 | has_attribute | m9 | m10 | high | chunk6 amod -> suit |
| e4 | has_attribute | m12 | m13 | medium | chunk8 poss -> right |
| e5 | has_attribute | m15 | m16 | high | chunk10 amod -> jacket |
| e6 | agent | m22 | m0 | medium | nsubj -> stands |
| e7 | agent | m24 | m8 | medium | nsubj -> sits |
| e8 | agent | m25 | m14 | medium | nsubj -> sits |
| e9 | relation | m0 | m1 | high | in |
| e10 | relation | m0 | m3 | medium | at |
| e11 | relation | m0 | m5 | medium | into |
| e12 | relation | m8 | m6 | medium | to |
| e13 | relation | m8 | m9 | high | in |
| e14 | relation | m14 | m12 | medium | to |
| e15 | relation | m14 | m15 | high | in |
| e16 | relation | m18 | m19 | high | in_front_of |
| e17 | relation | m19 | m20 | high | with |
| e18 | relation | m19 | m21 | high | with |

## 75

**caption_shape:** `tag-list-like`
**caption_id:** `3af8f056cfe76e2dac26e55da0973df75cb449f6d54b6c2a0428c9bd66a2d814`

> man, pipe, concrete, dirt, gloves

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | man | man | 0:3 |
| t1 | pipe | pipe | 5:9 |
| t2 | concrete | concrete | 11:19 |
| t3 | dirt | dirt | 21:25 |
| t4 | gloves | gloves | 27:33 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t1 | pipe | pipe | pipe | ROOT | pipe | 0:1 | 5:9 |
| t2 | concrete | concrete | concrete | ROOT | concrete | 0:1 | 11:19 |
| t3 | dirt | dirt | dirt | ROOT | dirt | 0:1 | 21:25 |
| t4 | gloves | gloves | glove | ROOT | gloves | 0:1 | 27:33 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | man | man | INTJ | NOUN | UH | NN | ROOT | man | 0 | 0:3 |
| t1 | 0 | pipe | pipe | NOUN | NOUN | NN | NN | ROOT | pipe | 0 | 5:9 |
| t2 | 0 | concrete | concrete | NOUN | NOUN | NN | NN | ROOT | concrete | 0 | 11:19 |
| t3 | 0 | dirt | dirt | NOUN | NOUN | NN | NN | ROOT | dirt | 0 | 21:25 |
| t4 | 0 | gloves | glove | NOUN | NOUN | NNS | NNS | ROOT | gloves | 0 | 27:33 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | t0 | 0 | tag_list_person_object_override | high |
| m1 | object | pipe | pipe | t1 | 0 | segment_head | high |
| m2 | object | concrete | concrete | t2 | 0 | segment_head | high |
| m3 | object | dirt | dirt | t3 | 0 | segment_head | high |
| m4 | object | gloves | glove | t4 | 0 | segment_head | high |

### Edges
_none_

## 76

**caption_shape:** `multi-sentence`
**caption_id:** `3b29dd4a058b71aa53a74f8fb31acb6906beda323ec3a8f8aa9410c838afa014`

> A person’s hand holds a phone on a stone ledge overlooking a sprawling town. The town features many white buildings with some colorful roofs, nestled among green trees under a bright sky. Distant hills and scattered clouds complete the horizon.

### Sentences
| sentence | token_span |
| --- | --- |
| A person’s hand holds a phone on a stone ledge overlooking a sprawling town. | 0:16 |
| The town features many white buildings with some colorful roofs, nestled among green trees under a bright sky. | 16:36 |
| Distant hills and scattered clouds complete the horizon. | 36:45 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A person’s hand | hand | hand | nsubj | holds | 0:4 |
| a phone | phone | phone | dobj | holds | 5:7 |
| a stone ledge | ledge | ledge | pobj | on | 8:11 |
| a sprawling town | town | town | dobj | overlooking | 12:15 |
| The town | town | town | nsubj | features | 16:18 |
| many white buildings | buildings | building | dobj | features | 19:22 |
| some colorful roofs | roofs | roof | pobj | with | 23:26 |
| green trees | trees | tree | pobj | among | 29:31 |
| a bright sky | sky | sky | pobj | under | 32:35 |
| Distant hills | hills | hill | nsubj | complete | 36:38 |
| scattered clouds | clouds | cloud | conj | hills | 39:41 |
| the horizon | horizon | horizon | dobj | complete | 42:44 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | person | 1 |
| 1 | person | person | NOUN | NN | poss | hand | 3 |
| 2 | ’s | ’s | PART | POS | case | person | 1 |
| 3 | hand | hand | NOUN | NN | nsubj | holds | 4 |
| 4 | holds | hold | VERB | VBZ | ROOT | holds | 4 |
| 5 | a | a | DET | DT | det | phone | 6 |
| 6 | phone | phone | NOUN | NN | dobj | holds | 4 |
| 7 | on | on | ADP | IN | prep | holds | 4 |
| 8 | a | a | DET | DT | det | ledge | 10 |
| 9 | stone | stone | NOUN | NN | compound | ledge | 10 |
| 10 | ledge | ledge | NOUN | NN | pobj | on | 7 |
| 11 | overlooking | overlook | VERB | VBG | acl | ledge | 10 |
| 12 | a | a | DET | DT | det | town | 14 |
| 13 | sprawling | sprawl | VERB | VBG | amod | town | 14 |
| 14 | town | town | NOUN | NN | dobj | overlooking | 11 |
| 15 | . | . | PUNCT | . | punct | holds | 4 |
| 16 | The | the | DET | DT | det | town | 17 |
| 17 | town | town | NOUN | NN | nsubj | features | 18 |
| 18 | features | feature | VERB | VBZ | ROOT | features | 18 |
| 19 | many | many | ADJ | JJ | amod | buildings | 21 |
| 20 | white | white | ADJ | JJ | amod | buildings | 21 |
| 21 | buildings | building | NOUN | NNS | dobj | features | 18 |
| 22 | with | with | ADP | IN | prep | buildings | 21 |
| 23 | some | some | DET | DT | det | roofs | 25 |
| 24 | colorful | colorful | ADJ | JJ | amod | roofs | 25 |
| 25 | roofs | roof | NOUN | NNS | pobj | with | 22 |
| 26 | , | , | PUNCT | , | punct | buildings | 21 |
| 27 | nestled | nestle | VERB | VBN | acl | buildings | 21 |
| 28 | among | among | ADP | IN | prep | nestled | 27 |
| 29 | green | green | ADJ | JJ | amod | trees | 30 |
| 30 | trees | tree | NOUN | NNS | pobj | among | 28 |
| 31 | under | under | ADP | IN | prep | trees | 30 |
| 32 | a | a | DET | DT | det | sky | 34 |
| 33 | bright | bright | ADJ | JJ | amod | sky | 34 |
| 34 | sky | sky | NOUN | NN | pobj | under | 31 |
| 35 | . | . | PUNCT | . | punct | features | 18 |
| 36 | Distant | distant | ADJ | JJ | amod | hills | 37 |
| 37 | hills | hill | NOUN | NNS | nsubj | complete | 41 |
| 38 | and | and | CCONJ | CC | cc | hills | 37 |
| 39 | scattered | scatter | VERB | VBN | amod | clouds | 40 |
| 40 | clouds | cloud | NOUN | NNS | conj | hills | 37 |
| 41 | complete | complete | VERB | VBP | ROOT | complete | 41 |
| 42 | the | the | DET | DT | det | horizon | 43 |
| 43 | horizon | horizon | NOUN | NN | dobj | complete | 41 |
| 44 | . | . | PUNCT | . | punct | complete | 41 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hand | hand | chunk0 | 3 | noun_chunk_root | high |
| m1 | attribute | person | person | chunk0 | 1 | modifier_attribute | medium |
| m2 | object | phone | phone | chunk1 | 6 | noun_chunk_root | high |
| m3 | object | ledge | ledge | chunk2 | 10 | noun_chunk_root | high |
| m4 | attribute | stone | stone | chunk2 | 9 | material_attribute | high |
| m5 | object | town | town | chunk3 | 14 | noun_chunk_root | high |
| m6 | attribute | sprawling | sprawl | chunk3 | 13 | state_attribute | medium |
| m7 | object | town | town | chunk4 | 17 | noun_chunk_root | high |
| m8 | object | buildings | building | chunk5 | 21 | noun_chunk_root | high |
| m9 | attribute | many | many | chunk5 | 19 | modifier_attribute | medium |
| m10 | attribute | white | white | chunk5 | 20 | color_attribute | high |
| m11 | object | roofs | roof | chunk6 | 25 | noun_chunk_root | high |
| m12 | attribute | colorful | colorful | chunk6 | 24 | modifier_attribute | medium |
| m13 | object | trees | tree | chunk7 | 30 | noun_chunk_root | high |
| m14 | attribute | green | green | chunk7 | 29 | color_attribute | high |
| m15 | object | sky | sky | chunk8 | 34 | noun_chunk_root | high |
| m16 | attribute | bright | bright | chunk8 | 33 | visual_attribute | medium |
| m17 | object | hills | hill | chunk9 | 37 | noun_chunk_root | high |
| m18 | attribute | Distant | distant | chunk9 | 36 | modifier_attribute | medium |
| m19 | object | clouds | cloud | chunk10 | 40 | noun_chunk_root | high |
| m20 | attribute | scattered | scatter | chunk10 | 39 | state_attribute | medium |
| m21 | object | horizon | horizon | chunk11 | 43 | noun_chunk_root | high |
| m22 | action | holds | hold | doc | 4 | verb_predicate | high |
| m23 | action | overlooking | overlook | doc | 11 | verb_predicate | high |
| m24 | action | features | feature | doc | 18 | verb_predicate | high |
| m25 | action | nestled | nestle | doc | 27 | verb_predicate | high |
| m26 | action | complete | complete | doc | 41 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 poss -> hand |
| e1 | has_attribute | m3 | m4 | high | chunk2 compound -> ledge |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> town |
| e3 | has_attribute | m8 | m9 | medium | chunk5 amod -> buildings |
| e4 | has_attribute | m8 | m10 | high | chunk5 amod -> buildings |
| e5 | has_attribute | m11 | m12 | medium | chunk6 amod -> roofs |
| e6 | has_attribute | m13 | m14 | high | chunk7 amod -> trees |
| e7 | has_attribute | m15 | m16 | medium | chunk8 amod -> sky |
| e8 | has_attribute | m17 | m18 | medium | chunk9 amod -> hills |
| e9 | has_attribute | m19 | m20 | medium | chunk10 amod -> clouds |
| e10 | agent | m22 | m0 | medium | nsubj -> holds |
| e11 | patient | m22 | m2 | medium | dobj -> holds |
| e12 | patient | m23 | m5 | medium | dobj -> overlooking |
| e13 | agent | m24 | m7 | medium | nsubj -> features |
| e14 | patient | m24 | m8 | medium | dobj -> features |
| e15 | agent | m26 | m17 | medium | nsubj -> complete |
| e16 | agent | m26 | m19 | medium | nsubj -> complete |
| e17 | patient | m26 | m21 | medium | dobj -> complete |
| e18 | relation | m0 | m3 | high | on |
| e19 | relation | m8 | m11 | high | with |
| e20 | relation | m8 | m13 | medium | among |
| e21 | relation | m13 | m15 | high | under |

## 77

**caption_shape:** `multi-sentence`
**caption_id:** `3b5770a7546308c5e0951bca64a4e13b3c91834d525b06b373afbe6b6eaf2814`

> A woman in a black, American flag-themed outfit holds up a shiny championship belt. She stands indoors under chandeliers with a ceiling and ventilation ducts visible behind her.

### Sentences
| sentence | token_span |
| --- | --- |
| A woman in a black, American flag-themed outfit holds up a shiny championship belt. | 0:17 |
| She stands indoors under chandeliers with a ceiling and ventilation ducts visible behind her. | 17:32 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A woman | woman | woman | nsubj | holds | 0:2 |
| a black, American flag-themed outfit | outfit | outfit | pobj | in | 3:10 |
| a shiny championship belt | belt | belt | dobj | holds | 12:16 |
| She | She | she | nsubj | stands | 17:18 |
| chandeliers | chandeliers | chandelier | pobj | under | 21:22 |
| a ceiling | ceiling | ceiling | nsubj | visible | 23:25 |
| ventilation ducts | ducts | duct | conj | ceiling | 26:28 |
| her | her | she | pobj | behind | 30:31 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | woman | 1 |
| 1 | woman | woman | NOUN | NN | nsubj | holds | 10 |
| 2 | in | in | ADP | IN | prep | woman | 1 |
| 3 | a | a | DET | DT | det | outfit | 9 |
| 4 | black | black | ADJ | JJ | amod | outfit | 9 |
| 5 | , | , | PUNCT | , | punct | outfit | 9 |
| 6 | American flag | american_flag | NOUN | NN | npadvmod | themed | 8 |
| 7 | - | - | PUNCT | HYPH | punct | themed | 8 |
| 8 | themed | theme | VERB | VBN | amod | outfit | 9 |
| 9 | outfit | outfit | NOUN | NN | pobj | in | 2 |
| 10 | holds | hold | VERB | VBZ | ROOT | holds | 10 |
| 11 | up | up | ADP | RP | prt | holds | 10 |
| 12 | a | a | DET | DT | det | belt | 15 |
| 13 | shiny | shiny | ADJ | JJ | amod | belt | 15 |
| 14 | championship | championship | NOUN | NN | compound | belt | 15 |
| 15 | belt | belt | NOUN | NN | dobj | holds | 10 |
| 16 | . | . | PUNCT | . | punct | holds | 10 |
| 17 | She | she | PRON | PRP | nsubj | stands | 18 |
| 18 | stands | stand | VERB | VBZ | ROOT | stands | 18 |
| 19 | indoors | indoors | ADV | RB | advmod | stands | 18 |
| 20 | under | under | ADP | IN | prep | stands | 18 |
| 21 | chandeliers | chandelier | NOUN | NNS | pobj | under | 20 |
| 22 | with | with | SCONJ | IN | mark | visible | 28 |
| 23 | a | a | DET | DT | det | ceiling | 24 |
| 24 | ceiling | ceiling | NOUN | NN | nsubj | visible | 28 |
| 25 | and | and | CCONJ | CC | cc | ceiling | 24 |
| 26 | ventilation | ventilation | NOUN | NN | compound | ducts | 27 |
| 27 | ducts | duct | NOUN | NNS | conj | ceiling | 24 |
| 28 | visible | visible | ADJ | JJ | advcl | stands | 18 |
| 29 | behind | behind | ADP | IN | prep | visible | 28 |
| 30 | her | she | PRON | PRP | pobj | behind | 29 |
| 31 | . | . | PUNCT | . | punct | stands | 18 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | outfit | outfit | chunk1 | 9 | noun_chunk_root | high |
| m2 | attribute | black | black | chunk1 | 4 | color_attribute | high |
| m3 | attribute | themed | theme | chunk1 | 8 | state_attribute | medium |
| m4 | object | belt | belt | chunk2 | 15 | noun_chunk_root | high |
| m5 | attribute | shiny | shiny | chunk2 | 13 | visual_attribute | medium |
| m6 | attribute | championship | championship | chunk2 | 14 | compound_modifier | medium |
| m7 | object | She | she | chunk3 | 17 | noun_chunk_root | high |
| m8 | object | chandeliers | chandelier | chunk4 | 21 | noun_chunk_root | high |
| m9 | object | ceiling | ceiling | chunk5 | 24 | noun_chunk_root | high |
| m10 | object | ducts | duct | chunk6 | 27 | noun_chunk_root | high |
| m11 | attribute | ventilation | ventilation | chunk6 | 26 | compound_modifier | medium |
| m12 | object | her | she | chunk7 | 30 | noun_chunk_root | high |
| m13 | context | indoors | indoors | doc | 19 | context_word | medium |
| m14 | action | holds | hold | doc | 10 | verb_predicate | high |
| m15 | action | stands | stand | doc | 18 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> outfit |
| e1 | has_attribute | m1 | m3 | medium | chunk1 amod -> outfit |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> belt |
| e3 | has_attribute | m4 | m6 | medium | chunk2 compound -> belt |
| e4 | has_attribute | m10 | m11 | medium | chunk6 compound -> ducts |
| e5 | has_context | scene | m13 | medium | context token indoors |
| e6 | agent | m14 | m0 | medium | nsubj -> holds |
| e7 | patient | m14 | m4 | medium | dobj -> holds |
| e8 | agent | m15 | m7 | medium | nsubj -> stands |
| e9 | relation | m0 | m1 | high | in |
| e10 | relation | m7 | m8 | high | under |

## 78

**caption_shape:** `multi-sentence`
**caption_id:** `3d615bf81b2edbc0ddf312c8e46aeff2ced9ab2d0015e50b4be5dc566214c414`

> People in suits sit at wooden desks in a large legislative chamber. A large screen above displays text in Portuguese, including “Assembleia Legislativa do Estado do Espírito Santo” and meeting details. Several individuals are seated or standing near the front, facing the screen.

**parsed_caption:**

> People in suits sit at wooden desks in a large legislative chamber. A large screen above displays text in Portuguese, including “Assembleia Legislativa do Estado do Espírito Santo” and meeting details. Several individuals are seated or standing near the front, facing the screen.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 3d615bf81b2edbc0ddf312c8e46aeff2ced9ab2d0015e50b4be5dc566214c414:q0 | Assembleia Legislativa do Estado do Espírito Santo | assembleia legislativa do estado do espírito santo | raw_quote_span |  | 128:180 | 128:180 |

### Sentences
| sentence | token_span |
| --- | --- |
| People in suits sit at wooden desks in a large legislative chamber. | 0:13 |
| A large screen above displays text in Portuguese, including “Assembleia Legislativa do Estado do Espírito Santo” and meeting details. | 13:28 |
| Several individuals are seated or standing near the front, facing the screen. | 28:42 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| People | People | People | nsubj | sit | 0:1 |
| suits | suits | suit | pobj | in | 2:3 |
| wooden desks | desks | desk | pobj | at | 5:7 |
| a large legislative chamber | chamber | chamber | pobj | in | 8:12 |
| A large screen | screen | screen | nsubj | displays | 13:16 |
| text | text | text | dobj | displays | 18:19 |
| Portuguese | Portuguese | Portuguese | pobj | in | 20:21 |
| “Assembleia Legislativa do Estado do Espírito Santo” | “Assembleia Legislativa do Estado do Espírito Santo” | assembleia_legislativa_do_estado_do_espírito_santo | pobj | including | 23:24 |
| Several individuals | individuals | individual | nsubjpass | seated | 28:30 |
| the front | front | front | pobj | near | 35:37 |
| the screen | screen | screen | dobj | facing | 39:41 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | People | People | NOUN | NNS | nsubj | sit | 3 |
| 1 | in | in | ADP | IN | prep | People | 0 |
| 2 | suits | suit | NOUN | NNS | pobj | in | 1 |
| 3 | sit | sit | VERB | VBP | ROOT | sit | 3 |
| 4 | at | at | ADP | IN | prep | sit | 3 |
| 5 | wooden | wooden | ADJ | JJ | amod | desks | 6 |
| 6 | desks | desk | NOUN | NNS | pobj | at | 4 |
| 7 | in | in | ADP | IN | prep | sit | 3 |
| 8 | a | a | DET | DT | det | chamber | 11 |
| 9 | large | large | ADJ | JJ | amod | chamber | 11 |
| 10 | legislative | legislative | ADJ | JJ | amod | chamber | 11 |
| 11 | chamber | chamber | NOUN | NN | pobj | in | 7 |
| 12 | . | . | PUNCT | . | punct | sit | 3 |
| 13 | A | a | DET | DT | det | screen | 15 |
| 14 | large | large | ADJ | JJ | amod | screen | 15 |
| 15 | screen | screen | NOUN | NN | nsubj | displays | 17 |
| 16 | above | above | ADV | RB | advmod | screen | 15 |
| 17 | displays | display | VERB | VBZ | ROOT | displays | 17 |
| 18 | text | text | NOUN | NN | dobj | displays | 17 |
| 19 | in | in | ADP | IN | prep | text | 18 |
| 20 | Portuguese | Portuguese | PROPN | NNP | pobj | in | 19 |
| 21 | , | , | PUNCT | , | punct | text | 18 |
| 22 | including | include | VERB | VBG | prep | text | 18 |
| 23 | “Assembleia Legislativa do Estado do Espírito Santo” | assembleia_legislativa_do_estado_do_espírito_santo | PROPN | NNP | pobj | including | 22 |
| 24 | and | and | CCONJ | CC | cc | including | 22 |
| 25 | meeting | meeting | NOUN | NN | compound | details | 26 |
| 26 | details | detail | NOUN | NNS | conj | including | 22 |
| 27 | . | . | PUNCT | . | punct | displays | 17 |
| 28 | Several | several | ADJ | JJ | amod | individuals | 29 |
| 29 | individuals | individual | NOUN | NNS | nsubjpass | seated | 31 |
| 30 | are | be | AUX | VBP | aux | seated | 31 |
| 31 | seated | seat | VERB | VBN | ROOT | seated | 31 |
| 32 | or | or | CCONJ | CC | cc | seated | 31 |
| 33 | standing | stand | VERB | VBG | conj | seated | 31 |
| 34 | near | near | ADP | IN | prep | standing | 33 |
| 35 | the | the | DET | DT | det | front | 36 |
| 36 | front | front | NOUN | NN | pobj | near | 34 |
| 37 | , | , | PUNCT | , | punct | standing | 33 |
| 38 | facing | face | VERB | VBG | conj | standing | 33 |
| 39 | the | the | DET | DT | det | screen | 40 |
| 40 | screen | screen | NOUN | NN | dobj | facing | 38 |
| 41 | . | . | PUNCT | . | punct | seated | 31 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | People | people | chunk0 | 0 | noun_chunk_root | high |
| m1 | object | suits | suit | chunk1 | 2 | noun_chunk_root | high |
| m2 | object | desks | desk | chunk2 | 6 | noun_chunk_root | high |
| m3 | attribute | wooden | wooden | chunk2 | 5 | material_attribute | high |
| m4 | object | chamber | chamber | chunk3 | 11 | noun_chunk_root | high |
| m5 | attribute | large | large | chunk3 | 9 | size_attribute | high |
| m6 | attribute | legislative | legislative | chunk3 | 10 | modifier_attribute | medium |
| m7 | object | screen | screen | chunk4 | 15 | noun_chunk_root | high |
| m8 | attribute | large | large | chunk4 | 14 | size_attribute | high |
| m9 | object | text | text | chunk5 | 18 | noun_chunk_root | high |
| m10 | object | Portuguese | portuguese | chunk6 | 20 | noun_chunk_root | high |
| m11 | object | “Assembleia Legislativa do Estado do Espírito Santo” | assembleia_legislativa_do_estado_do_espírito_santo | chunk7 | 23 | noun_chunk_root | high |
| m12 | object | individuals | individual | chunk8 | 29 | noun_chunk_root | high |
| m13 | attribute | Several | several | chunk8 | 28 | modifier_attribute | medium |
| m14 | context | front | front | chunk9 | 36 | spatial_region | medium |
| m15 | object | screen | screen | chunk10 | 40 | noun_chunk_root | high |
| m16 | action | sit | sit | doc | 3 | verb_predicate | high |
| m17 | action | displays | display | doc | 17 | verb_predicate | high |
| m18 | action | including | include | doc | 22 | verb_predicate | high |
| m19 | action | seated | seat | doc | 31 | verb_predicate | high |
| m20 | action | standing | stand | doc | 33 | verb_predicate | high |
| m21 | action | facing | face | doc | 38 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | chunk2 amod -> desks |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> chamber |
| e2 | has_attribute | m4 | m6 | medium | chunk3 amod -> chamber |
| e3 | has_attribute | m7 | m8 | high | chunk4 amod -> screen |
| e4 | has_attribute | m12 | m13 | medium | chunk8 amod -> individuals |
| e5 | agent | m16 | m0 | medium | nsubj -> sit |
| e6 | agent | m17 | m7 | medium | nsubj -> displays |
| e7 | patient | m17 | m9 | medium | dobj -> displays |
| e8 | patient | m18 | m11 | medium | pobj -> including |
| e9 | agent | m19 | m12 | medium | nsubjpass -> seated |
| e10 | patient | m21 | m15 | medium | dobj -> facing |
| e11 | relation | m0 | m1 | high | in |
| e12 | relation | m0 | m2 | medium | at |
| e13 | relation | m0 | m4 | high | in |
| e14 | relation | m9 | m10 | high | in |
| e15 | relation | m9 | m11 | medium | include |
| e16 | relation | m12 | m14 | high | near |

## 79

**caption_shape:** `tag-list-like`
**caption_id:** `3fd213aa27d03cea945474fbd22867b9a96db60cb511f2579c214920945ccc14`

> gold medal, ribbon, pin, cross

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | gold medal | gold medal | 0:10 |
| t1 | ribbon | ribbon | 12:18 |
| t2 | pin | pin | 20:23 |
| t3 | cross | cross | 25:30 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | gold medal | medal | medal | ROOT | medal | 0:2 | 0:10 |
| t1 | ribbon | ribbon | ribbon | ROOT | ribbon | 0:1 | 12:18 |
| t2 | pin | pin | pin | ROOT | pin | 0:1 | 20:23 |
| t3 | cross | cross | cross | ROOT | cross | 0:1 | 25:30 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | gold | gold | NOUN | ADJ | NN | JJ | compound | medal | 1 | 0:4 |
| t0 | 1 | medal | medal | NOUN | NOUN | NN | NN | ROOT | medal | 1 | 5:10 |
| t1 | 0 | ribbon | ribbon | NOUN | NOUN | NN | NN | ROOT | ribbon | 0 | 12:18 |
| t2 | 0 | pin | pin | NOUN | NOUN | NN | NN | ROOT | pin | 0 | 20:23 |
| t3 | 0 | cross | cross | NOUN | NOUN | NN | NN | ROOT | cross | 0 | 25:30 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | medal | medal | t0 | 1 | segment_head | high |
| m1 | attribute | gold | gold | t0 | 0 | attribute | high |
| m2 | object | ribbon | ribbon | t1 | 0 | segment_head | high |
| m3 | object | pin | pin | t2 | 0 | segment_head | high |
| m4 | object | cross | cross | t3 | 0 | segment_head | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> medal |

## 80

**caption_shape:** `multi-sentence`
**caption_id:** `40ccbff955e113a1f352c3648a1521830574e2870d90a14c32cf857d1d185814`

> A square, dark gray slab with a rough, uneven surface rests on a light-colored flat background. The object has visible texture and minor imperfections, suggesting it may be made of stone or metal. Its edges are slightly irregular, and it appears stationary.

### Sentences
| sentence | token_span |
| --- | --- |
| A square, dark gray slab with a rough, uneven surface rests on a light-colored flat background. | 0:19 |
| The object has visible texture and minor imperfections, suggesting it may be made of stone or metal. | 19:38 |
| Its edges are slightly irregular, and it appears stationary. | 38:49 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A square, dark gray slab | slab | slab | nsubj | rests | 0:6 |
| a rough, uneven surface | surface | surface | pobj | with | 7:12 |
| a light-colored flat background | background | background | pobj | on | 14:18 |
| The object | object | object | nsubj | has | 19:21 |
| visible texture | texture | texture | dobj | has | 22:24 |
| minor imperfections | imperfections | imperfection | conj | texture | 25:27 |
| it | it | it | nsubjpass | made | 29:30 |
| stone | stone | stone | pobj | of | 34:35 |
| metal | metal | metal | conj | stone | 36:37 |
| Its edges | edges | edge | nsubj | are | 38:40 |
| it | it | it | nsubj | appears | 45:46 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | slab | 5 |
| 1 | square | square | ADJ | JJ | amod | slab | 5 |
| 2 | , | , | PUNCT | , | punct | slab | 5 |
| 3 | dark | dark | ADJ | JJ | amod | gray | 4 |
| 4 | gray | gray | ADJ | JJ | amod | slab | 5 |
| 5 | slab | slab | NOUN | NN | nsubj | rests | 12 |
| 6 | with | with | ADP | IN | prep | slab | 5 |
| 7 | a | a | DET | DT | det | surface | 11 |
| 8 | rough | rough | ADJ | JJ | amod | surface | 11 |
| 9 | , | , | PUNCT | , | punct | surface | 11 |
| 10 | uneven | uneven | ADJ | JJ | amod | surface | 11 |
| 11 | surface | surface | NOUN | NN | pobj | with | 6 |
| 12 | rests | rest | VERB | VBZ | ROOT | rests | 12 |
| 13 | on | on | ADP | IN | prep | rests | 12 |
| 14 | a | a | DET | DT | det | background | 17 |
| 15 | light-colored | light-colored | ADJ | JJ | amod | background | 17 |
| 16 | flat | flat | ADJ | JJ | amod | background | 17 |
| 17 | background | background | NOUN | NN | pobj | on | 13 |
| 18 | . | . | PUNCT | . | punct | rests | 12 |
| 19 | The | the | DET | DT | det | object | 20 |
| 20 | object | object | NOUN | NN | nsubj | has | 21 |
| 21 | has | have | VERB | VBZ | ROOT | has | 21 |
| 22 | visible | visible | ADJ | JJ | amod | texture | 23 |
| 23 | texture | texture | NOUN | NN | dobj | has | 21 |
| 24 | and | and | CCONJ | CC | cc | texture | 23 |
| 25 | minor | minor | ADJ | JJ | amod | imperfections | 26 |
| 26 | imperfections | imperfection | NOUN | NNS | conj | texture | 23 |
| 27 | , | , | PUNCT | , | punct | has | 21 |
| 28 | suggesting | suggest | VERB | VBG | advcl | has | 21 |
| 29 | it | it | PRON | PRP | nsubjpass | made | 32 |
| 30 | may | may | AUX | MD | aux | made | 32 |
| 31 | be | be | AUX | VB | auxpass | made | 32 |
| 32 | made | make | VERB | VBN | ccomp | suggesting | 28 |
| 33 | of | of | ADP | IN | prep | made | 32 |
| 34 | stone | stone | NOUN | NN | pobj | of | 33 |
| 35 | or | or | CCONJ | CC | cc | stone | 34 |
| 36 | metal | metal | NOUN | NN | conj | stone | 34 |
| 37 | . | . | PUNCT | . | punct | has | 21 |
| 38 | Its | its | PRON | PRP$ | poss | edges | 39 |
| 39 | edges | edge | NOUN | NNS | nsubj | are | 40 |
| 40 | are | be | AUX | VBP | ROOT | are | 40 |
| 41 | slightly | slightly | ADV | RB | advmod | irregular | 42 |
| 42 | irregular | irregular | ADJ | JJ | acomp | are | 40 |
| 43 | , | , | PUNCT | , | punct | are | 40 |
| 44 | and | and | CCONJ | CC | cc | are | 40 |
| 45 | it | it | PRON | PRP | nsubj | appears | 46 |
| 46 | appears | appear | VERB | VBZ | conj | are | 40 |
| 47 | stationary | stationary | ADJ | JJ | oprd | appears | 46 |
| 48 | . | . | PUNCT | . | punct | appears | 46 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | slab | slab | chunk0 | 5 | noun_chunk_root | high |
| m1 | attribute | square | square | chunk0 | 1 | modifier_attribute | medium |
| m2 | attribute | dark | dark | chunk0 | 3 | visual_attribute | medium |
| m3 | attribute | gray | gray | chunk0 | 4 | color_attribute | high |
| m4 | object | surface | surface | chunk1 | 11 | noun_chunk_root | high |
| m5 | attribute | rough | rough | chunk1 | 8 | modifier_attribute | medium |
| m6 | attribute | uneven | uneven | chunk1 | 10 | modifier_attribute | medium |
| m7 | object | background | background | chunk2 | 17 | noun_chunk_root | high |
| m8 | attribute | light-colored | light-colored | chunk2 | 15 | modifier_attribute | medium |
| m9 | attribute | flat | flat | chunk2 | 16 | modifier_attribute | medium |
| m10 | object | object | object | chunk3 | 20 | noun_chunk_root | high |
| m11 | object | texture | texture | chunk4 | 23 | noun_chunk_root | high |
| m12 | attribute | visible | visible | chunk4 | 22 | modifier_attribute | medium |
| m13 | object | imperfections | imperfection | chunk5 | 26 | noun_chunk_root | high |
| m14 | attribute | minor | minor | chunk5 | 25 | modifier_attribute | medium |
| m15 | object | it | it | chunk6 | 29 | noun_chunk_root | high |
| m16 | object | stone | stone | chunk7 | 34 | noun_chunk_root | high |
| m17 | object | metal | metal | chunk8 | 36 | noun_chunk_root | high |
| m18 | object | edges | edge | chunk9 | 39 | noun_chunk_root | high |
| m19 | attribute | Its | its | chunk9 | 38 | modifier_attribute | medium |
| m20 | object | it | it | chunk10 | 45 | noun_chunk_root | high |
| m21 | context | background | background | doc | 17 | context_word | medium |
| m22 | action | rests | rest | doc | 12 | verb_predicate | high |
| m23 | action | has | have | doc | 21 | verb_predicate | high |
| m24 | action | suggesting | suggest | doc | 28 | verb_predicate | high |
| m25 | action | made | make | doc | 32 | verb_predicate | high |
| m26 | action | appears | appear | doc | 46 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> slab |
| e1 | has_attribute | m0 | m2 | medium | chunk0 amod -> slab |
| e2 | has_attribute | m0 | m3 | high | chunk0 amod -> slab |
| e3 | has_attribute | m4 | m5 | medium | chunk1 amod -> surface |
| e4 | has_attribute | m4 | m6 | medium | chunk1 amod -> surface |
| e5 | has_attribute | m7 | m8 | medium | chunk2 amod -> background |
| e6 | has_attribute | m7 | m9 | medium | chunk2 amod -> background |
| e7 | has_attribute | m11 | m12 | medium | chunk4 amod -> texture |
| e8 | has_attribute | m13 | m14 | medium | chunk5 amod -> imperfections |
| e9 | has_attribute | m18 | m19 | medium | chunk9 poss -> edges |
| e10 | has_context | scene | m21 | medium | context token background |
| e11 | agent | m22 | m0 | medium | nsubj -> rests |
| e12 | agent | m23 | m10 | medium | nsubj -> has |
| e13 | patient | m23 | m11 | medium | dobj -> has |
| e14 | patient | m23 | m13 | medium | dobj -> has |
| e15 | agent | m25 | m15 | medium | nsubjpass -> made |
| e16 | agent | m26 | m20 | medium | nsubj -> appears |
| e17 | relation | m0 | m4 | high | with |
| e18 | relation | m0 | m21 | high | on |
| e19 | relation | m15 | m16 | medium | of |
| e20 | relation | m15 | m17 | medium | of |

## 81

**caption_shape:** `sentence-like`
**caption_id:** `4137bc66f4d1f6035892ec5f727cc91dc7d31ade7927509d1882e3b883915014`

> Snow-covered trees stand on a snowy hill under a clear blue sky.

### Sentences
| sentence | token_span |
| --- | --- |
| Snow-covered trees stand on a snowy hill under a clear blue sky. | 0:13 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Snow-covered trees | trees | tree | nsubj | stand | 0:2 |
| a snowy hill | hill | hill | pobj | on | 4:7 |
| a clear blue sky | sky | sky | pobj | under | 8:12 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Snow-covered | snow-covered | ADJ | JJ | amod | trees | 1 |
| 1 | trees | tree | NOUN | NNS | nsubj | stand | 2 |
| 2 | stand | stand | VERB | VBP | ROOT | stand | 2 |
| 3 | on | on | ADP | IN | prep | stand | 2 |
| 4 | a | a | DET | DT | det | hill | 6 |
| 5 | snowy | snowy | ADJ | JJ | amod | hill | 6 |
| 6 | hill | hill | NOUN | NN | pobj | on | 3 |
| 7 | under | under | ADP | IN | prep | stand | 2 |
| 8 | a | a | DET | DT | det | sky | 11 |
| 9 | clear | clear | ADJ | JJ | amod | sky | 11 |
| 10 | blue | blue | ADJ | JJ | amod | sky | 11 |
| 11 | sky | sky | NOUN | NN | pobj | under | 7 |
| 12 | . | . | PUNCT | . | punct | stand | 2 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | trees | tree | chunk0 | 1 | noun_chunk_root | high |
| m1 | attribute | Snow-covered | snow-covered | chunk0 | 0 | modifier_attribute | medium |
| m2 | object | hill | hill | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | snowy | snowy | chunk1 | 5 | modifier_attribute | medium |
| m4 | object | sky | sky | chunk2 | 11 | noun_chunk_root | high |
| m5 | attribute | clear | clear | chunk2 | 9 | visual_attribute | medium |
| m6 | attribute | blue | blue | chunk2 | 10 | color_attribute | high |
| m7 | action | stand | stand | doc | 2 | verb_predicate | high |

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

## 82

**caption_shape:** `sentence-like`
**caption_id:** `4220764c409a789c7cf2ce02bf17e8ed251f5213b62c1e2adbe9ec0687c82014`

> A young woman with long brown hair smiles, wearing a red and black striped shirt and large hoop earrings.

### Sentences
| sentence | token_span |
| --- | --- |
| A young woman with long brown hair smiles, wearing a red and black striped shirt and large hoop earrings. | 0:21 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A young woman | woman | woman | nsubj | smiles | 0:3 |
| long brown hair | hair | hair | pobj | with | 4:7 |
| a red and black striped shirt | shirt | shirt | dobj | wearing | 10:16 |
| large hoop earrings | earrings | earring | conj | shirt | 17:20 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | woman | 2 |
| 1 | young | young | ADJ | JJ | amod | woman | 2 |
| 2 | woman | woman | NOUN | NN | nsubj | smiles | 7 |
| 3 | with | with | ADP | IN | prep | woman | 2 |
| 4 | long | long | ADJ | JJ | amod | hair | 6 |
| 5 | brown | brown | ADJ | JJ | amod | hair | 6 |
| 6 | hair | hair | NOUN | NN | pobj | with | 3 |
| 7 | smiles | smile | VERB | VBZ | ROOT | smiles | 7 |
| 8 | , | , | PUNCT | , | punct | smiles | 7 |
| 9 | wearing | wear | VERB | VBG | advcl | smiles | 7 |
| 10 | a | a | DET | DT | det | shirt | 15 |
| 11 | red | red | ADJ | JJ | amod | shirt | 15 |
| 12 | and | and | CCONJ | CC | cc | red | 11 |
| 13 | black | black | ADJ | JJ | conj | red | 11 |
| 14 | striped | striped | ADJ | JJ | amod | shirt | 15 |
| 15 | shirt | shirt | NOUN | NN | dobj | wearing | 9 |
| 16 | and | and | CCONJ | CC | cc | shirt | 15 |
| 17 | large | large | ADJ | JJ | amod | earrings | 19 |
| 18 | hoop | hoop | NOUN | NN | compound | earrings | 19 |
| 19 | earrings | earring | NOUN | NNS | conj | shirt | 15 |
| 20 | . | . | PUNCT | . | punct | smiles | 7 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | young | young | chunk0 | 1 | modifier_attribute | medium |
| m2 | object | hair | hair | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | long | long | chunk1 | 4 | size_attribute | high |
| m4 | attribute | brown | brown | chunk1 | 5 | color_attribute | high |
| m5 | object | shirt | shirt | chunk2 | 15 | noun_chunk_root | high |
| m6 | attribute | red | red | chunk2 | 11 | color_attribute | high |
| m7 | attribute | black | black | chunk2 | 13 | color_attribute | high |
| m8 | attribute | striped | striped | chunk2 | 14 | modifier_attribute | medium |
| m9 | object | earrings | earring | chunk3 | 19 | noun_chunk_root | high |
| m10 | attribute | large | large | chunk3 | 17 | size_attribute | high |
| m11 | attribute | hoop | hoop | chunk3 | 18 | compound_modifier | medium |
| m12 | action | smiles | smile | doc | 7 | verb_predicate | high |
| m13 | action | wearing | wear | doc | 9 | verb_predicate | high |

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
| e9 | patient | m13 | m5 | medium | dobj -> wearing |
| e10 | patient | m13 | m9 | medium | dobj -> wearing |
| e11 | relation | m0 | m2 | high | with |

## 83

**caption_shape:** `multi-sentence`
**caption_id:** `44f8a614329a02e0c0056eaab4a12c0a514594fe2368415f7e48097ac9189014`

> Football players in green and white uniforms run on a field during a game. A referee in black and white stands nearby.

### Sentences
| sentence | token_span |
| --- | --- |
| Football players in green and white uniforms run on a field during a game. | 0:14 |
| A referee in black and white stands nearby. | 14:23 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Football players | Football players | football_player | nsubj | run | 0:1 |
| green and white uniforms | uniforms | uniform | pobj | in | 2:6 |
| a field | field | field | pobj | on | 8:10 |
| a game | game | game | pobj | during | 11:13 |
| A referee | referee | referee | nsubj | stands | 14:16 |
| black | black | black | pobj | in | 17:18 |
| white | white | white | conj | black | 19:20 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Football players | football_player | NOUN | NN | nsubj | run | 6 |
| 1 | in | in | ADP | IN | prep | Football players | 0 |
| 2 | green | green | ADJ | JJ | amod | uniforms | 5 |
| 3 | and | and | CCONJ | CC | cc | green | 2 |
| 4 | white | white | ADJ | JJ | conj | green | 2 |
| 5 | uniforms | uniform | NOUN | NNS | pobj | in | 1 |
| 6 | run | run | VERB | VBP | ROOT | run | 6 |
| 7 | on | on | ADP | IN | prep | run | 6 |
| 8 | a | a | DET | DT | det | field | 9 |
| 9 | field | field | NOUN | NN | pobj | on | 7 |
| 10 | during | during | ADP | IN | prep | run | 6 |
| 11 | a | a | DET | DT | det | game | 12 |
| 12 | game | game | NOUN | NN | pobj | during | 10 |
| 13 | . | . | PUNCT | . | punct | run | 6 |
| 14 | A | a | DET | DT | det | referee | 15 |
| 15 | referee | referee | NOUN | NN | nsubj | stands | 20 |
| 16 | in | in | ADP | IN | prep | referee | 15 |
| 17 | black | black | NOUN | NN | pobj | in | 16 |
| 18 | and | and | CCONJ | CC | cc | black | 17 |
| 19 | white | white | NOUN | NN | conj | black | 17 |
| 20 | stands | stand | VERB | VBZ | ROOT | stands | 20 |
| 21 | nearby | nearby | ADV | RB | advmod | stands | 20 |
| 22 | . | . | PUNCT | . | punct | stands | 20 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | Football players | football_player | chunk0 | 0 | noun_chunk_root | high |
| m1 | object | uniforms | uniform | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | green | green | chunk1 | 2 | color_attribute | high |
| m3 | attribute | white | white | chunk1 | 4 | color_attribute | high |
| m4 | object | field | field | chunk2 | 9 | noun_chunk_root | high |
| m5 | object | game | game | chunk3 | 12 | noun_chunk_root | high |
| m6 | object | referee | referee | chunk4 | 15 | noun_chunk_root | high |
| m7 | object | black | black | chunk5 | 17 | noun_chunk_root | high |
| m8 | object | white | white | chunk6 | 19 | noun_chunk_root | high |
| m9 | action | run | run | doc | 6 | verb_predicate | high |
| m10 | action | stands | stand | doc | 20 | verb_predicate | high |

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
| e7 | relation | m6 | m7 | high | in |
| e8 | relation | m6 | m8 | high | in |

## 84

**caption_shape:** `tag-list-like`
**caption_id:** `4520335aa9590d3ac5578d1b581822595dc7c25487d871a33c943f90890c4414`

> text, page, book, russian, printed

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | text | text | 0:4 |
| t1 | page | page | 6:10 |
| t2 | book | book | 12:16 |
| t3 | russian | russian | 18:25 |
| t4 | printed | printed | 27:34 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | text | text | text | ROOT | text | 0:1 | 0:4 |
| t1 | page | page | page | ROOT | page | 0:1 | 6:10 |
| t2 | book | book | book | ROOT | book | 0:1 | 12:16 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | text | text | NOUN | NOUN | NN | NN | ROOT | text | 0 | 0:4 |
| t1 | 0 | page | page | NOUN | NOUN | NN | NN | ROOT | page | 0 | 6:10 |
| t2 | 0 | book | book | NOUN | NOUN | NN | NN | ROOT | book | 0 | 12:16 |
| t3 | 0 | russian | russian | ADJ | ADJ | JJ | JJ | ROOT | russian | 0 | 18:25 |
| t4 | 0 | printed | print | VERB | ADJ | VBN | VBN | ROOT | printed | 0 | 27:34 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | text | text | t0 | 0 | segment_head | high |
| m1 | object | page | page | t1 | 0 | segment_head | high |
| m2 | object | book | book | t2 | 0 | segment_head | high |
| m3 | attribute | russian | russian | t3 | 0 | floating_attribute | medium |
| m4 | attribute | printed | print | t4 | 0 | floating_attribute | medium |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | candidate_has_attribute | m2 | m3 | low | t3 adjacent floating attribute |
| e1 | candidate_has_attribute | m2 | m4 | low | t4 adjacent floating attribute |

## 85

**caption_shape:** `tag-list-like`
**caption_id:** `4534c60ad9d43cb8de486c52e3839889e81b20688b0308d02dff250997cf5014`

> ocean, trees, cloudy sky, coastline, waves

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | ocean | ocean | 0:5 |
| t1 | trees | trees | 7:12 |
| t2 | cloudy sky | cloudy sky | 14:24 |
| t3 | coastline | coastline | 26:35 |
| t4 | waves | waves | 37:42 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | ocean | ocean | ocean | ROOT | ocean | 0:1 | 0:5 |
| t1 | trees | trees | tree | ROOT | trees | 0:1 | 7:12 |
| t2 | cloudy sky | sky | sky | ROOT | sky | 0:2 | 14:24 |
| t3 | coastline | coastline | coastline | ROOT | coastline | 0:1 | 26:35 |
| t4 | waves | waves | wave | ROOT | waves | 0:1 | 37:42 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | ocean | ocean | NOUN | NOUN | NN | NN | ROOT | ocean | 0 | 0:5 |
| t1 | 0 | trees | tree | NOUN | NOUN | NNS | NNS | ROOT | trees | 0 | 7:12 |
| t2 | 0 | cloudy | cloudy | ADJ | ADJ | JJ | JJ | amod | sky | 1 | 14:20 |
| t2 | 1 | sky | sky | NOUN | NOUN | NN | NN | ROOT | sky | 1 | 21:24 |
| t3 | 0 | coastline | coastline | PROPN | NOUN | NNP | NN | ROOT | coastline | 0 | 26:35 |
| t4 | 0 | waves | wave | NOUN | NOUN | NNS | NNS | ROOT | waves | 0 | 37:42 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | ocean | ocean | t0 | 0 | segment_head | high |
| m1 | object | trees | tree | t1 | 0 | segment_head | high |
| m2 | object | sky | sky | t2 | 1 | segment_head | high |
| m3 | attribute | cloudy | cloudy | t2 | 0 | attribute | high |
| m4 | object | coastline | coastline | t3 | 0 | segment_head | high |
| m5 | object | waves | wave | t4 | 0 | segment_head | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | t2 internal amod -> sky |

## 86

**caption_shape:** `sentence-like`
**caption_id:** `4629060f393ba0054f5f960b0b8f890a0bd363cac2b8baf241e4d37186c28414`

> Three boys stand around a green roulette table, placing bets with chips.

### Sentences
| sentence | token_span |
| --- | --- |
| Three boys stand around a green roulette table, placing bets with chips. | 0:14 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Three boys | boys | boy | nsubj | stand | 0:2 |
| a green roulette table | table | table | pobj | around | 4:8 |
| bets | bets | bet | dobj | placing | 10:11 |
| chips | chips | chip | pobj | with | 12:13 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Three | three | NUM | CD | nummod | boys | 1 |
| 1 | boys | boy | NOUN | NNS | nsubj | stand | 2 |
| 2 | stand | stand | VERB | VBP | ROOT | stand | 2 |
| 3 | around | around | ADP | IN | prep | stand | 2 |
| 4 | a | a | DET | DT | det | table | 7 |
| 5 | green | green | ADJ | JJ | amod | table | 7 |
| 6 | roulette | roulette | NOUN | NN | compound | table | 7 |
| 7 | table | table | NOUN | NN | pobj | around | 3 |
| 8 | , | , | PUNCT | , | punct | stand | 2 |
| 9 | placing | place | VERB | VBG | advcl | stand | 2 |
| 10 | bets | bet | NOUN | NNS | dobj | placing | 9 |
| 11 | with | with | ADP | IN | prep | placing | 9 |
| 12 | chips | chip | NOUN | NNS | pobj | with | 11 |
| 13 | . | . | PUNCT | . | punct | stand | 2 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | boys | boy | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Three | three | chunk0 | 0 | quantity | high |
| m2 | object | table | table | chunk1 | 7 | noun_chunk_root | high |
| m3 | attribute | green | green | chunk1 | 5 | color_attribute | high |
| m4 | attribute | roulette | roulette | chunk1 | 6 | compound_modifier | medium |
| m5 | object | bets | bet | chunk2 | 10 | noun_chunk_root | high |
| m6 | object | chips | chip | chunk3 | 12 | noun_chunk_root | high |
| m7 | action | stand | stand | doc | 2 | verb_predicate | high |
| m8 | action | placing | place | doc | 9 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 nummod -> boys |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> table |
| e2 | has_attribute | m2 | m4 | medium | chunk1 compound -> table |
| e3 | agent | m7 | m0 | medium | nsubj -> stand |
| e4 | patient | m8 | m5 | medium | dobj -> placing |
| e5 | relation | m0 | m2 | high | around |
| e6 | relation | m0 | m6 | high | with |

## 87

**caption_shape:** `tag-list-like`
**caption_id:** `46ded0945fa518dcf266d085b23d00b0f7e091b16de462d808e44473fc1d4414`

> dump truck, orange bed, nighttime, street light, wet ground

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | dump truck | dump truck | 0:10 |
| t1 | orange bed | orange bed | 12:22 |
| t2 | nighttime | nighttime | 24:33 |
| t3 | street light | street light | 35:47 |
| t4 | wet ground | wet ground | 49:59 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | dump truck | dump truck | dump_truck | ROOT | dump truck | 0:1 | 0:10 |
| t1 | orange bed | bed | bed | ROOT | bed | 0:2 | 12:22 |
| t2 | nighttime | nighttime | nighttime | ROOT | nighttime | 0:1 | 24:33 |
| t3 | street light | street light | street_light | ROOT | street light | 0:1 | 35:47 |
| t4 | wet ground | ground | ground | ROOT | ground | 0:2 | 49:59 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | dump truck | dump_truck | NOUN | NOUN | NN | NN | ROOT | dump truck | 0 | 0:10 |
| t1 | 0 | orange | orange | ADJ | ADJ | JJ | JJ | amod | bed | 1 | 12:18 |
| t1 | 1 | bed | bed | NOUN | NOUN | NN | NN | ROOT | bed | 1 | 19:22 |
| t2 | 0 | nighttime | nighttime | NOUN | NOUN | NN | NN | ROOT | nighttime | 0 | 24:33 |
| t3 | 0 | street light | street_light | NOUN | NOUN | NN | NN | ROOT | street light | 0 | 35:47 |
| t4 | 0 | wet | wet | ADJ | ADJ | JJ | JJ | amod | ground | 1 | 49:52 |
| t4 | 1 | ground | ground | NOUN | NOUN | NN | NN | ROOT | ground | 1 | 53:59 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | dump truck | dump_truck | t0 | 0 | segment_head | high |
| m1 | object | bed | bed | t1 | 1 | segment_head | high |
| m2 | attribute | orange | orange | t1 | 0 | attribute | high |
| m3 | context | nighttime | nighttime | t2 | 0 | scene_context | high |
| m4 | object | street light | street_light | t3 | 0 | segment_head | high |
| m5 | object | ground | ground | t4 | 1 | segment_head | high |
| m6 | attribute | wet | wet | t4 | 0 | attribute | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | t1 internal amod -> bed |
| e1 | has_context | scene | m3 | high | t2 context tag |
| e2 | has_attribute | m5 | m6 | high | t4 internal amod -> ground |

## 88

**caption_shape:** `multi-sentence`
**caption_id:** `4796dfef4cc06424f06ef22a84b9650c73e479905f025701ec03baab64fd0414`

> A woman kneels in grass, planting a small green plant. Another person stands nearby wearing black shoes.

### Sentences
| sentence | token_span |
| --- | --- |
| A woman kneels in grass, planting a small green plant. | 0:12 |
| Another person stands nearby wearing black shoes. | 12:20 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A woman | woman | woman | nsubj | kneels | 0:2 |
| grass | grass | grass | pobj | in | 4:5 |
| a small green plant | plant | plant | dobj | planting | 7:11 |
| Another person | person | person | nsubj | stands | 12:14 |
| black shoes | shoes | shoe | dobj | wearing | 17:19 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | woman | 1 |
| 1 | woman | woman | NOUN | NN | nsubj | kneels | 2 |
| 2 | kneels | kneel | VERB | VBZ | ROOT | kneels | 2 |
| 3 | in | in | ADP | IN | prep | kneels | 2 |
| 4 | grass | grass | NOUN | NN | pobj | in | 3 |
| 5 | , | , | PUNCT | , | punct | kneels | 2 |
| 6 | planting | plant | VERB | VBG | advcl | kneels | 2 |
| 7 | a | a | DET | DT | det | plant | 10 |
| 8 | small | small | ADJ | JJ | amod | plant | 10 |
| 9 | green | green | ADJ | JJ | amod | plant | 10 |
| 10 | plant | plant | NOUN | NN | dobj | planting | 6 |
| 11 | . | . | PUNCT | . | punct | kneels | 2 |
| 12 | Another | another | DET | DT | det | person | 13 |
| 13 | person | person | NOUN | NN | nsubj | stands | 14 |
| 14 | stands | stand | VERB | VBZ | ROOT | stands | 14 |
| 15 | nearby | nearby | ADV | RB | advmod | stands | 14 |
| 16 | wearing | wear | VERB | VBG | advcl | stands | 14 |
| 17 | black | black | ADJ | JJ | amod | shoes | 18 |
| 18 | shoes | shoe | NOUN | NNS | dobj | wearing | 16 |
| 19 | . | . | PUNCT | . | punct | stands | 14 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | grass | grass | chunk1 | 4 | noun_chunk_root | high |
| m2 | object | plant | plant | chunk2 | 10 | noun_chunk_root | high |
| m3 | attribute | small | small | chunk2 | 8 | size_attribute | high |
| m4 | attribute | green | green | chunk2 | 9 | color_attribute | high |
| m5 | object | person | person | chunk3 | 13 | noun_chunk_root | high |
| m6 | object | shoes | shoe | chunk4 | 18 | noun_chunk_root | high |
| m7 | attribute | black | black | chunk4 | 17 | color_attribute | high |
| m8 | action | kneels | kneel | doc | 2 | verb_predicate | high |
| m9 | action | planting | plant | doc | 6 | verb_predicate | high |
| m10 | action | stands | stand | doc | 14 | verb_predicate | high |
| m11 | action | wearing | wear | doc | 16 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m2 | m3 | high | chunk2 amod -> plant |
| e1 | has_attribute | m2 | m4 | high | chunk2 amod -> plant |
| e2 | has_attribute | m6 | m7 | high | chunk4 amod -> shoes |
| e3 | agent | m8 | m0 | medium | nsubj -> kneels |
| e4 | patient | m9 | m2 | medium | dobj -> planting |
| e5 | agent | m10 | m5 | medium | nsubj -> stands |
| e6 | patient | m11 | m6 | medium | dobj -> wearing |
| e7 | relation | m0 | m1 | high | in |

## 89

**caption_shape:** `multi-sentence`
**caption_id:** `4b92bad03af761f9f17b04d31ec5e98b2a3d7f91093f3ed8a263fbf2b5043c14`

> Two men stand near a large fire outdoors, one stirring food in a pan over the flames. Another fire burns nearby on the ground.

### Sentences
| sentence | token_span |
| --- | --- |
| Two men stand near a large fire outdoors, one stirring food in a pan over the flames. | 0:19 |
| Another fire burns nearby on the ground. | 19:27 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Two men | men | man | nsubj | stand | 0:2 |
| a large fire | fire | fire | pobj | near | 4:7 |
| food | food | food | dobj | stirring | 11:12 |
| a pan | pan | pan | pobj | in | 13:15 |
| the flames | flames | flame | pobj | over | 16:18 |
| Another fire | fire | fire | nsubj | burns | 19:21 |
| the ground | ground | ground | pobj | on | 24:26 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Two | two | NUM | CD | nummod | men | 1 |
| 1 | men | man | NOUN | NNS | nsubj | stand | 2 |
| 2 | stand | stand | VERB | VBP | ROOT | stand | 2 |
| 3 | near | near | ADP | IN | prep | stand | 2 |
| 4 | a | a | DET | DT | det | fire | 6 |
| 5 | large | large | ADJ | JJ | amod | fire | 6 |
| 6 | fire | fire | NOUN | NN | pobj | near | 3 |
| 7 | outdoors | outdoors | ADV | RB | advmod | fire | 6 |
| 8 | , | , | PUNCT | , | punct | stand | 2 |
| 9 | one | one | NUM | CD | nsubj | stirring | 10 |
| 10 | stirring | stir | VERB | VBG | advcl | stand | 2 |
| 11 | food | food | NOUN | NN | dobj | stirring | 10 |
| 12 | in | in | ADP | IN | prep | stirring | 10 |
| 13 | a | a | DET | DT | det | pan | 14 |
| 14 | pan | pan | NOUN | NN | pobj | in | 12 |
| 15 | over | over | ADP | IN | prep | stirring | 10 |
| 16 | the | the | DET | DT | det | flames | 17 |
| 17 | flames | flame | NOUN | NNS | pobj | over | 15 |
| 18 | . | . | PUNCT | . | punct | stand | 2 |
| 19 | Another | another | DET | DT | det | fire | 20 |
| 20 | fire | fire | NOUN | NN | nsubj | burns | 21 |
| 21 | burns | burn | VERB | VBZ | ROOT | burns | 21 |
| 22 | nearby | nearby | ADV | RB | advmod | burns | 21 |
| 23 | on | on | ADP | IN | prep | burns | 21 |
| 24 | the | the | DET | DT | det | ground | 25 |
| 25 | ground | ground | NOUN | NN | pobj | on | 23 |
| 26 | . | . | PUNCT | . | punct | burns | 21 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | men | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Two | two | chunk0 | 0 | quantity | high |
| m2 | object | fire | fire | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | large | large | chunk1 | 5 | size_attribute | high |
| m4 | object | food | food | chunk2 | 11 | noun_chunk_root | high |
| m5 | object | pan | pan | chunk3 | 14 | noun_chunk_root | high |
| m6 | object | flames | flame | chunk4 | 17 | noun_chunk_root | high |
| m7 | object | fire | fire | chunk5 | 20 | noun_chunk_root | high |
| m8 | object | ground | ground | chunk6 | 25 | noun_chunk_root | high |
| m9 | context | outdoors | outdoors | doc | 7 | context_word | medium |
| m10 | action | stand | stand | doc | 2 | verb_predicate | high |
| m11 | action | stirring | stir | doc | 10 | verb_predicate | high |
| m12 | action | burns | burn | doc | 21 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 nummod -> men |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> fire |
| e2 | has_context | scene | m9 | medium | context token outdoors |
| e3 | agent | m10 | m0 | medium | nsubj -> stand |
| e4 | patient | m11 | m4 | medium | dobj -> stirring |
| e5 | agent | m12 | m7 | medium | nsubj -> burns |
| e6 | relation | m0 | m2 | high | near |
| e7 | relation | m7 | m8 | high | on |

## 90

**caption_shape:** `multi-sentence`
**caption_id:** `4bdbef927b2be02d84676c5d4761e2273071526b2c5224f2a1e2195169fc6814`

> A white fabric tag with the number "1709-1" is stitched onto a bright yellow garment. The tag is slightly frayed at the edges and sits against the textured, wrinkled fabric of the clothing.

**parsed_caption:**

> A white fabric tag with the number "1709-1" is stitched onto a bright yellow garment. The tag is slightly frayed at the edges and sits against the textured, wrinkled fabric of the clothing.

### Quote Mentions
| id | global_id | text_raw | text_norm | placeholder | consumed_prefix | raw_char_span | parse_char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| q0 | 4bdbef927b2be02d84676c5d4761e2273071526b2c5224f2a1e2195169fc6814:q0 | 1709-1 | 1709-1 | raw_quote_span |  | 35:43 | 35:43 |

### Sentences
| sentence | token_span |
| --- | --- |
| A white fabric tag with the number "1709-1" is stitched onto a bright yellow garment. | 0:16 |
| The tag is slightly frayed at the edges and sits against the textured, wrinkled fabric of the clothing. | 16:36 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A white fabric tag | tag | tag | nsubjpass | stitched | 0:4 |
| the number | number | number | pobj | with | 5:7 |
| a bright yellow garment | garment | garment | pobj | onto | 11:15 |
| The tag | tag | tag | nsubjpass | frayed | 16:18 |
| the edges | edges | edge | pobj | at | 22:24 |
| the textured, wrinkled fabric | fabric | fabric | pobj | against | 27:32 |
| the clothing | clothing | clothing | pobj | of | 33:35 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | tag | 3 |
| 1 | white | white | ADJ | JJ | amod | tag | 3 |
| 2 | fabric | fabric | NOUN | NN | compound | tag | 3 |
| 3 | tag | tag | NOUN | NN | nsubjpass | stitched | 9 |
| 4 | with | with | ADP | IN | prep | tag | 3 |
| 5 | the | the | DET | DT | det | number | 6 |
| 6 | number | number | NOUN | NN | pobj | with | 4 |
| 7 | "1709-1" | 1709-1 | NUM | CD | appos | number | 6 |
| 8 | is | be | AUX | VBZ | auxpass | stitched | 9 |
| 9 | stitched | stitch | VERB | VBN | ROOT | stitched | 9 |
| 10 | onto | onto | ADP | IN | prep | stitched | 9 |
| 11 | a | a | DET | DT | det | garment | 14 |
| 12 | bright | bright | ADJ | JJ | amod | yellow | 13 |
| 13 | yellow | yellow | ADJ | JJ | amod | garment | 14 |
| 14 | garment | garment | NOUN | NN | pobj | onto | 10 |
| 15 | . | . | PUNCT | . | punct | stitched | 9 |
| 16 | The | the | DET | DT | det | tag | 17 |
| 17 | tag | tag | NOUN | NN | nsubjpass | frayed | 20 |
| 18 | is | be | AUX | VBZ | auxpass | frayed | 20 |
| 19 | slightly | slightly | ADV | RB | advmod | frayed | 20 |
| 20 | frayed | fray | VERB | VBN | ROOT | frayed | 20 |
| 21 | at | at | ADP | IN | prep | frayed | 20 |
| 22 | the | the | DET | DT | det | edges | 23 |
| 23 | edges | edge | NOUN | NNS | pobj | at | 21 |
| 24 | and | and | CCONJ | CC | cc | frayed | 20 |
| 25 | sits | sit | VERB | VBZ | conj | frayed | 20 |
| 26 | against | against | ADP | IN | prep | sits | 25 |
| 27 | the | the | DET | DT | det | fabric | 31 |
| 28 | textured | textured | ADJ | JJ | amod | fabric | 31 |
| 29 | , | , | PUNCT | , | punct | fabric | 31 |
| 30 | wrinkled | wrinkled | ADJ | JJ | amod | fabric | 31 |
| 31 | fabric | fabric | NOUN | NN | pobj | against | 26 |
| 32 | of | of | ADP | IN | prep | fabric | 31 |
| 33 | the | the | DET | DT | det | clothing | 34 |
| 34 | clothing | clothing | NOUN | NN | pobj | of | 32 |
| 35 | . | . | PUNCT | . | punct | frayed | 20 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | tag | tag | chunk0 | 3 | noun_chunk_root | high |
| m1 | attribute | white | white | chunk0 | 1 | color_attribute | high |
| m2 | attribute | fabric | fabric | chunk0 | 2 | material_attribute | high |
| m3 | object | number | number | chunk1 | 6 | noun_chunk_root | high |
| m4 | object | garment | garment | chunk2 | 14 | noun_chunk_root | high |
| m5 | attribute | bright | bright | chunk2 | 12 | visual_attribute | medium |
| m6 | attribute | yellow | yellow | chunk2 | 13 | color_attribute | high |
| m7 | object | tag | tag | chunk3 | 17 | noun_chunk_root | high |
| m8 | context | edges | edge | chunk4 | 23 | spatial_region | medium |
| m9 | object | fabric | fabric | chunk5 | 31 | noun_chunk_root | high |
| m10 | attribute | textured | textured | chunk5 | 28 | modifier_attribute | medium |
| m11 | attribute | wrinkled | wrinkled | chunk5 | 30 | modifier_attribute | medium |
| m12 | object | clothing | clothing | chunk6 | 34 | noun_chunk_root | high |
| m13 | action | stitched | stitch | doc | 9 | verb_predicate | high |
| m14 | action | frayed | fray | doc | 20 | verb_predicate | high |
| m15 | action | sits | sit | doc | 25 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> tag |
| e1 | has_attribute | m0 | m2 | high | chunk0 compound -> tag |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> garment |
| e3 | has_attribute | m4 | m6 | high | chunk2 amod -> garment |
| e4 | has_attribute | m9 | m10 | medium | chunk5 amod -> fabric |
| e5 | has_attribute | m9 | m11 | medium | chunk5 amod -> fabric |
| e6 | agent | m13 | m0 | medium | nsubjpass -> stitched |
| e7 | agent | m14 | m7 | medium | nsubjpass -> frayed |
| e8 | relation | m0 | m3 | high | with |
| e9 | relation | m0 | m4 | medium | onto |
| e10 | relation | m7 | m8 | medium | at |
| e11 | relation | m7 | m9 | high | against |
| e12 | relation | m9 | m12 | medium | of |

## 91

**caption_shape:** `tag-list-like`
**caption_id:** `4c3c734e1a2f098c9b6b84ea0d285fc45132f0b736138635798ee19b16700c14`

> green hill, forest, trees, foliage, slope

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | green hill | green hill | 0:10 |
| t1 | forest | forest | 12:18 |
| t2 | trees | trees | 20:25 |
| t3 | foliage | foliage | 27:34 |
| t4 | slope | slope | 36:41 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | green hill | hill | hill | ROOT | hill | 0:2 | 0:10 |
| t1 | forest | forest | forest | ROOT | forest | 0:1 | 12:18 |
| t2 | trees | trees | tree | ROOT | trees | 0:1 | 20:25 |
| t3 | foliage | foliage | foliage | ROOT | foliage | 0:1 | 27:34 |
| t4 | slope | slope | slope | ROOT | slope | 0:1 | 36:41 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | green | green | PROPN | ADJ | NNP | JJ | compound | hill | 1 | 0:5 |
| t0 | 1 | hill | hill | PROPN | NOUN | NNP | NN | ROOT | hill | 1 | 6:10 |
| t1 | 0 | forest | forest | NOUN | NOUN | NN | NN | ROOT | forest | 0 | 12:18 |
| t2 | 0 | trees | tree | NOUN | NOUN | NNS | NNS | ROOT | trees | 0 | 20:25 |
| t3 | 0 | foliage | foliage | NOUN | NOUN | NN | NN | ROOT | foliage | 0 | 27:34 |
| t4 | 0 | slope | slope | NOUN | NOUN | NN | NN | ROOT | slope | 0 | 36:41 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hill | hill | t0 | 1 | segment_head | high |
| m1 | attribute | green | green | t0 | 0 | attribute | high |
| m2 | object | forest | forest | t1 | 0 | segment_head | high |
| m3 | object | trees | tree | t2 | 0 | segment_head | high |
| m4 | object | foliage | foliage | t3 | 0 | segment_head | high |
| m5 | object | slope | slope | t4 | 0 | segment_head | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> hill |

## 92

**caption_shape:** `tag-list-like`
**caption_id:** `4c4766ae1c27a85a6d4897a868761e118b7ea64c82d65d1438a894aaedeed814`

> conference hall, speaker, red chairs, presentation screen, banner

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | conference hall | conference hall | 0:15 |
| t1 | speaker | speaker | 17:24 |
| t2 | red chairs | red chairs | 26:36 |
| t3 | presentation screen | presentation screen | 38:57 |
| t4 | banner | banner | 59:65 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | conference hall | hall | hall | ROOT | hall | 0:2 | 0:15 |
| t1 | speaker | speaker | speaker | ROOT | speaker | 0:1 | 17:24 |
| t2 | red chairs | chairs | chair | ROOT | chairs | 0:2 | 26:36 |
| t3 | presentation screen | screen | screen | ROOT | screen | 0:2 | 38:57 |
| t4 | banner | banner | banner | ROOT | banner | 0:1 | 59:65 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | conference | conference | NOUN | NOUN | NN | NN | compound | hall | 1 | 0:10 |
| t0 | 1 | hall | hall | NOUN | NOUN | NN | NN | ROOT | hall | 1 | 11:15 |
| t1 | 0 | speaker | speaker | NOUN | NOUN | NN | NN | ROOT | speaker | 0 | 17:24 |
| t2 | 0 | red | red | ADJ | ADJ | JJ | JJ | amod | chairs | 1 | 26:29 |
| t2 | 1 | chairs | chair | NOUN | NOUN | NNS | NNS | ROOT | chairs | 1 | 30:36 |
| t3 | 0 | presentation | presentation | NOUN | NOUN | NN | NN | compound | screen | 1 | 38:50 |
| t3 | 1 | screen | screen | NOUN | NOUN | NN | NN | ROOT | screen | 1 | 51:57 |
| t4 | 0 | banner | banner | PROPN | NOUN | NNP | NN | ROOT | banner | 0 | 59:65 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hall | hall | t0 | 1 | segment_head | high |
| m1 | attribute | conference | conference | t0 | 0 | attribute | high |
| m2 | object | speaker | speaker | t1 | 0 | segment_head | high |
| m3 | object | chairs | chair | t2 | 1 | segment_head | high |
| m4 | attribute | red | red | t2 | 0 | attribute | high |
| m5 | object | screen | screen | t3 | 1 | segment_head | high |
| m6 | attribute | presentation | presentation | t3 | 0 | attribute | high |
| m7 | object | banner | banner | t4 | 0 | segment_head | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal compound -> hall |
| e1 | has_attribute | m3 | m4 | high | t2 internal amod -> chairs |
| e2 | has_attribute | m5 | m6 | high | t3 internal compound -> screen |

## 93

**caption_shape:** `sentence-like`
**caption_id:** `4c56e1b58491d0d3a411f339954e03386183a18bfa198776807c15df358bc014`

> A man in a suit stands with two officers in brown uniforms and hats outdoors near a brick building.

### Sentences
| sentence | token_span |
| --- | --- |
| A man in a suit stands with two officers in brown uniforms and hats outdoors near a brick building. | 0:20 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A man | man | man | nsubj | stands | 0:2 |
| a suit | suit | suit | pobj | in | 3:5 |
| two officers | officers | officer | pobj | with | 7:9 |
| brown uniforms | uniforms | uniform | pobj | in | 10:12 |
| hats | hats | hat | conj | uniforms | 13:14 |
| a brick building | building | building | pobj | near | 16:19 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | man | 1 |
| 1 | man | man | NOUN | NN | nsubj | stands | 5 |
| 2 | in | in | ADP | IN | prep | man | 1 |
| 3 | a | a | DET | DT | det | suit | 4 |
| 4 | suit | suit | NOUN | NN | pobj | in | 2 |
| 5 | stands | stand | VERB | VBZ | ROOT | stands | 5 |
| 6 | with | with | ADP | IN | prep | stands | 5 |
| 7 | two | two | NUM | CD | nummod | officers | 8 |
| 8 | officers | officer | NOUN | NNS | pobj | with | 6 |
| 9 | in | in | ADP | IN | prep | officers | 8 |
| 10 | brown | brown | ADJ | JJ | amod | uniforms | 11 |
| 11 | uniforms | uniform | NOUN | NNS | pobj | in | 9 |
| 12 | and | and | CCONJ | CC | cc | uniforms | 11 |
| 13 | hats | hat | NOUN | NNS | conj | uniforms | 11 |
| 14 | outdoors | outdoors | ADV | RB | advmod | stands | 5 |
| 15 | near | near | ADP | IN | prep | stands | 5 |
| 16 | a | a | DET | DT | det | building | 18 |
| 17 | brick | brick | NOUN | NN | compound | building | 18 |
| 18 | building | building | NOUN | NN | pobj | near | 15 |
| 19 | . | . | PUNCT | . | punct | stands | 5 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | man | man | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | suit | suit | chunk1 | 4 | noun_chunk_root | high |
| m2 | object | officers | officer | chunk2 | 8 | noun_chunk_root | high |
| m3 | quantity | two | two | chunk2 | 7 | quantity | high |
| m4 | object | uniforms | uniform | chunk3 | 11 | noun_chunk_root | high |
| m5 | attribute | brown | brown | chunk3 | 10 | color_attribute | high |
| m6 | object | hats | hat | chunk4 | 13 | noun_chunk_root | high |
| m7 | object | building | building | chunk5 | 18 | noun_chunk_root | high |
| m8 | attribute | brick | brick | chunk5 | 17 | material_attribute | high |
| m9 | context | outdoors | outdoors | doc | 14 | context_word | medium |
| m10 | action | stands | stand | doc | 5 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m2 | m3 | high | chunk2 nummod -> officers |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> uniforms |
| e2 | has_attribute | m7 | m8 | high | chunk5 compound -> building |
| e3 | has_context | scene | m9 | medium | context token outdoors |
| e4 | agent | m10 | m0 | medium | nsubj -> stands |
| e5 | relation | m0 | m1 | high | in |
| e6 | relation | m0 | m2 | high | with |
| e7 | relation | m2 | m4 | high | in |
| e8 | relation | m2 | m6 | high | in |
| e9 | relation | m0 | m7 | high | near |

## 94

**caption_shape:** `sentence-like`
**caption_id:** `4d32641dbcf279e49f454f162fee1519d21d7d06d7bb7a3670cf3b687045b414`

> A forested hillside overlooks a wide, winding river and a turquoise lake, with mountains in the background.

### Sentences
| sentence | token_span |
| --- | --- |
| A forested hillside overlooks a wide, winding river and a turquoise lake, with mountains in the background. | 0:20 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A forested hillside | hillside | hillside | nsubj | overlooks | 0:3 |
| a wide, winding river | river | river | dobj | overlooks | 4:9 |
| a turquoise lake | lake | lake | conj | river | 10:13 |
| mountains | mountains | mountain | pobj | with | 15:16 |
| the background | background | background | pobj | in | 17:19 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | hillside | 2 |
| 1 | forested | forested | ADJ | JJ | amod | hillside | 2 |
| 2 | hillside | hillside | NOUN | NN | nsubj | overlooks | 3 |
| 3 | overlooks | overlook | VERB | VBZ | ROOT | overlooks | 3 |
| 4 | a | a | DET | DT | det | river | 8 |
| 5 | wide | wide | ADJ | JJ | amod | river | 8 |
| 6 | , | , | PUNCT | , | punct | river | 8 |
| 7 | winding | wind | VERB | VBG | amod | river | 8 |
| 8 | river | river | NOUN | NN | dobj | overlooks | 3 |
| 9 | and | and | CCONJ | CC | cc | river | 8 |
| 10 | a | a | DET | DT | det | lake | 12 |
| 11 | turquoise | turquoise | ADJ | JJ | amod | lake | 12 |
| 12 | lake | lake | NOUN | NN | conj | river | 8 |
| 13 | , | , | PUNCT | , | punct | overlooks | 3 |
| 14 | with | with | ADP | IN | prep | overlooks | 3 |
| 15 | mountains | mountain | NOUN | NNS | pobj | with | 14 |
| 16 | in | in | ADP | IN | prep | mountains | 15 |
| 17 | the | the | DET | DT | det | background | 18 |
| 18 | background | background | NOUN | NN | pobj | in | 16 |
| 19 | . | . | PUNCT | . | punct | overlooks | 3 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | hillside | hillside | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | forested | forested | chunk0 | 1 | modifier_attribute | medium |
| m2 | object | river | river | chunk1 | 8 | noun_chunk_root | high |
| m3 | attribute | wide | wide | chunk1 | 5 | size_attribute | high |
| m4 | attribute | winding | wind | chunk1 | 7 | state_attribute | medium |
| m5 | object | lake | lake | chunk2 | 12 | noun_chunk_root | high |
| m6 | attribute | turquoise | turquoise | chunk2 | 11 | color_attribute | high |
| m7 | object | mountains | mountain | chunk3 | 15 | noun_chunk_root | high |
| m8 | object | background | background | chunk4 | 18 | noun_chunk_root | high |
| m9 | context | background | background | doc | 18 | context_word | medium |
| m10 | action | overlooks | overlook | doc | 3 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> hillside |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> river |
| e2 | has_attribute | m2 | m4 | medium | chunk1 amod -> river |
| e3 | has_attribute | m5 | m6 | high | chunk2 amod -> lake |
| e4 | has_context | scene | m9 | medium | context token background |
| e5 | agent | m10 | m0 | medium | nsubj -> overlooks |
| e6 | patient | m10 | m2 | medium | dobj -> overlooks |
| e7 | patient | m10 | m5 | medium | dobj -> overlooks |
| e8 | relation | m0 | m7 | high | with |
| e9 | relation | m7 | m9 | high | in |

## 95

**caption_shape:** `tag-list-like`
**caption_id:** `4dc463b2d8ef33464459810bb14ebafc29c1274af7b8e1f4ed9219b4b951d814`

> green backpack, blue sign, exhibition booth, person, indoor

### Tag Segments
| tag_id | raw | norm | char_span |
| --- | --- | --- | --- |
| t0 | green backpack | green backpack | 0:14 |
| t1 | blue sign | blue sign | 16:25 |
| t2 | exhibition booth | exhibition booth | 27:43 |
| t3 | person | person | 45:51 |
| t4 | indoor | indoor | 53:59 |

### Segment Noun Chunks
| tag_id | chunk | root | root_lemma | root_dep | root_head | token_span | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | green backpack | backpack | backpack | ROOT | backpack | 0:2 | 0:14 |
| t1 | blue sign | sign | sign | ROOT | sign | 0:2 | 16:25 |
| t2 | exhibition booth | booth | booth | ROOT | booth | 0:2 | 27:43 |
| t3 | person | person | person | ROOT | person | 0:1 | 45:51 |
| t4 | indoor | indoor | indoor | ROOT | indoor | 0:1 | 53:59 |

### Segment Tokens / POS / Lemma / Dependency
| tag_id | i | text | lemma | pos_raw | pos_norm | tag_raw | tag_norm | dep | head | head_i | char_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| t0 | 0 | green | green | ADJ | ADJ | JJ | JJ | amod | backpack | 1 | 0:5 |
| t0 | 1 | backpack | backpack | NOUN | NOUN | NN | NN | ROOT | backpack | 1 | 6:14 |
| t1 | 0 | blue | blue | ADJ | ADJ | JJ | JJ | amod | sign | 1 | 16:20 |
| t1 | 1 | sign | sign | NOUN | NOUN | NN | NN | ROOT | sign | 1 | 21:25 |
| t2 | 0 | exhibition | exhibition | NOUN | NOUN | NN | NN | compound | booth | 1 | 27:37 |
| t2 | 1 | booth | booth | NOUN | NOUN | NN | NN | ROOT | booth | 1 | 38:43 |
| t3 | 0 | person | person | NOUN | NOUN | NN | NN | ROOT | person | 0 | 45:51 |
| t4 | 0 | indoor | indoor | NOUN | NOUN | NN | NN | ROOT | indoor | 0 | 53:59 |

### Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | backpack | backpack | t0 | 1 | segment_head | high |
| m1 | attribute | green | green | t0 | 0 | attribute | high |
| m2 | object | sign | sign | t1 | 1 | segment_head | high |
| m3 | attribute | blue | blue | t1 | 0 | attribute | high |
| m4 | object | booth | booth | t2 | 1 | segment_head | high |
| m5 | attribute | exhibition | exhibition | t2 | 0 | attribute | high |
| m6 | object | person | person | t3 | 0 | segment_head | high |
| m7 | context | indoor | indoor | t4 | 0 | scene_context | high |

### Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | t0 internal amod -> backpack |
| e1 | has_attribute | m2 | m3 | high | t1 internal amod -> sign |
| e2 | has_attribute | m4 | m5 | high | t2 internal compound -> booth |
| e3 | has_context | scene | m7 | high | t4 context tag |

## 96

**caption_shape:** `sentence-like`
**caption_id:** `4ee72aa601ec49378a9d19b957a90696b5de2c99d1d4efdde87fad946346d814`

> A close-up of a dark bee with fuzzy body and transparent wings stands on a dark surface.

### Sentences
| sentence | token_span |
| --- | --- |
| A close-up of a dark bee with fuzzy body and transparent wings stands on a dark surface. | 0:18 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A close-up | close-up | close-up | nsubj | stands | 0:2 |
| a dark bee | bee | bee | pobj | of | 3:6 |
| fuzzy body | body | body | pobj | with | 7:9 |
| transparent wings | wings | wing | conj | body | 10:12 |
| a dark surface | surface | surface | pobj | on | 14:17 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | close-up | 1 |
| 1 | close-up | close-up | NOUN | NN | nsubj | stands | 12 |
| 2 | of | of | ADP | IN | prep | close-up | 1 |
| 3 | a | a | DET | DT | det | bee | 5 |
| 4 | dark | dark | ADJ | JJ | amod | bee | 5 |
| 5 | bee | bee | NOUN | NN | pobj | of | 2 |
| 6 | with | with | ADP | IN | prep | bee | 5 |
| 7 | fuzzy | fuzzy | ADJ | JJ | amod | body | 8 |
| 8 | body | body | NOUN | NN | pobj | with | 6 |
| 9 | and | and | CCONJ | CC | cc | body | 8 |
| 10 | transparent | transparent | ADJ | JJ | amod | wings | 11 |
| 11 | wings | wing | NOUN | NNS | conj | body | 8 |
| 12 | stands | stand | VERB | VBZ | ROOT | stands | 12 |
| 13 | on | on | ADP | IN | prep | stands | 12 |
| 14 | a | a | DET | DT | det | surface | 16 |
| 15 | dark | dark | ADJ | JJ | amod | surface | 16 |
| 16 | surface | surface | NOUN | NN | pobj | on | 13 |
| 17 | . | . | PUNCT | . | punct | stands | 12 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | close-up | close-up | chunk0 | 1 | noun_chunk_root | high |
| m1 | object | bee | bee | chunk1 | 5 | noun_chunk_root | high |
| m2 | attribute | dark | dark | chunk1 | 4 | visual_attribute | medium |
| m3 | object | body | body | chunk2 | 8 | noun_chunk_root | high |
| m4 | attribute | fuzzy | fuzzy | chunk2 | 7 | modifier_attribute | medium |
| m5 | object | wings | wing | chunk3 | 11 | noun_chunk_root | high |
| m6 | attribute | transparent | transparent | chunk3 | 10 | modifier_attribute | medium |
| m7 | object | surface | surface | chunk4 | 16 | noun_chunk_root | high |
| m8 | attribute | dark | dark | chunk4 | 15 | visual_attribute | medium |
| m9 | action | stands | stand | doc | 12 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | medium | chunk1 amod -> bee |
| e1 | has_attribute | m3 | m4 | medium | chunk2 amod -> body |
| e2 | has_attribute | m5 | m6 | medium | chunk3 amod -> wings |
| e3 | has_attribute | m7 | m8 | medium | chunk4 amod -> surface |
| e4 | agent | m9 | m0 | medium | nsubj -> stands |
| e5 | relation | m0 | m1 | medium | of |
| e6 | relation | m1 | m3 | high | with |
| e7 | relation | m1 | m5 | high | with |
| e8 | relation | m0 | m7 | high | on |

## 97

**caption_shape:** `multi-sentence`
**caption_id:** `4f56ca8847a4a005e4c454c9e252f4b7320e5d66beb78072b93832ab5627e414`

> A stone church tower with a pointed roof stands against a clear blue sky. Evergreen trees and a stone wall are in the foreground, with a hillside visible behind the building.

### Sentences
| sentence | token_span |
| --- | --- |
| A stone church tower with a pointed roof stands against a clear blue sky. | 0:14 |
| Evergreen trees and a stone wall are in the foreground, with a hillside visible behind the building. | 14:33 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A stone church tower | church tower | church_tower | nsubj | stands | 0:3 |
| a pointed roof | roof | roof | pobj | with | 4:7 |
| a clear blue sky | sky | sky | pobj | against | 9:13 |
| Evergreen trees | trees | tree | nsubj | are | 14:16 |
| a stone wall | wall | wall | conj | trees | 17:20 |
| the foreground | foreground | foreground | pobj | in | 22:24 |
| a hillside | hillside | hillside | nsubj | visible | 26:28 |
| the building | building | building | pobj | behind | 30:32 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | church tower | 2 |
| 1 | stone | stone | NOUN | NN | compound | church tower | 2 |
| 2 | church tower | church_tower | NOUN | NN | nsubj | stands | 7 |
| 3 | with | with | ADP | IN | prep | church tower | 2 |
| 4 | a | a | DET | DT | det | roof | 6 |
| 5 | pointed | pointed | ADJ | JJ | amod | roof | 6 |
| 6 | roof | roof | NOUN | NN | pobj | with | 3 |
| 7 | stands | stand | VERB | VBZ | ROOT | stands | 7 |
| 8 | against | against | ADP | IN | prep | stands | 7 |
| 9 | a | a | DET | DT | det | sky | 12 |
| 10 | clear | clear | ADJ | JJ | amod | sky | 12 |
| 11 | blue | blue | ADJ | JJ | amod | sky | 12 |
| 12 | sky | sky | NOUN | NN | pobj | against | 8 |
| 13 | . | . | PUNCT | . | punct | stands | 7 |
| 14 | Evergreen | evergreen | ADJ | JJ | amod | trees | 15 |
| 15 | trees | tree | NOUN | NNS | nsubj | are | 20 |
| 16 | and | and | CCONJ | CC | cc | trees | 15 |
| 17 | a | a | DET | DT | det | wall | 19 |
| 18 | stone | stone | NOUN | NN | compound | wall | 19 |
| 19 | wall | wall | NOUN | NN | conj | trees | 15 |
| 20 | are | be | AUX | VBP | ROOT | are | 20 |
| 21 | in | in | ADP | IN | prep | are | 20 |
| 22 | the | the | DET | DT | det | foreground | 23 |
| 23 | foreground | foreground | NOUN | NN | pobj | in | 21 |
| 24 | , | , | PUNCT | , | punct | are | 20 |
| 25 | with | with | SCONJ | IN | mark | visible | 28 |
| 26 | a | a | DET | DT | det | hillside | 27 |
| 27 | hillside | hillside | NOUN | NN | nsubj | visible | 28 |
| 28 | visible | visible | ADJ | JJ | advcl | are | 20 |
| 29 | behind | behind | ADP | IN | prep | visible | 28 |
| 30 | the | the | DET | DT | det | building | 31 |
| 31 | building | building | NOUN | NN | pobj | behind | 29 |
| 32 | . | . | PUNCT | . | punct | are | 20 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | church tower | church_tower | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | stone | stone | chunk0 | 1 | material_attribute | high |
| m2 | object | roof | roof | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | pointed | pointed | chunk1 | 5 | modifier_attribute | medium |
| m4 | object | sky | sky | chunk2 | 12 | noun_chunk_root | high |
| m5 | attribute | clear | clear | chunk2 | 10 | visual_attribute | medium |
| m6 | attribute | blue | blue | chunk2 | 11 | color_attribute | high |
| m7 | object | trees | tree | chunk3 | 15 | noun_chunk_root | high |
| m8 | attribute | Evergreen | evergreen | chunk3 | 14 | modifier_attribute | medium |
| m9 | object | wall | wall | chunk4 | 19 | noun_chunk_root | high |
| m10 | attribute | stone | stone | chunk4 | 18 | material_attribute | high |
| m11 | object | foreground | foreground | chunk5 | 23 | noun_chunk_root | high |
| m12 | object | hillside | hillside | chunk6 | 27 | noun_chunk_root | high |
| m13 | object | building | building | chunk7 | 31 | noun_chunk_root | high |
| m14 | context | foreground | foreground | doc | 23 | context_word | medium |
| m15 | action | stands | stand | doc | 7 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 compound -> church tower |
| e1 | has_attribute | m2 | m3 | medium | chunk1 amod -> roof |
| e2 | has_attribute | m4 | m5 | medium | chunk2 amod -> sky |
| e3 | has_attribute | m4 | m6 | high | chunk2 amod -> sky |
| e4 | has_attribute | m7 | m8 | medium | chunk3 amod -> trees |
| e5 | has_attribute | m9 | m10 | high | chunk4 compound -> wall |
| e6 | has_context | scene | m14 | medium | context token foreground |
| e7 | agent | m15 | m0 | medium | nsubj -> stands |
| e8 | relation | m0 | m2 | high | with |
| e9 | relation | m0 | m4 | high | against |
| e10 | relation | m7 | m14 | high | in |

## 98

**caption_shape:** `multi-sentence`
**caption_id:** `503da8cbdc4c15313e8d7891c32a5893a947513d5b58aaf7d26f4b76e852a014`

> Four people in white lab coats stand at a table, each holding a glass flask. Three men wear goggles and pour liquids into flasks, while a woman in a patterned hijab stands beside them. A logo and text are visible at the top and bottom of the image.

### Sentences
| sentence | token_span |
| --- | --- |
| Four people in white lab coats stand at a table, each holding a glass flask. | 0:16 |
| Three men wear goggles and pour liquids into flasks, while a woman in a patterned hijab stands beside them. | 16:37 |
| A logo and text are visible at the top and bottom of the image. | 37:52 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| Four people | people | people | nsubj | stand | 0:2 |
| white lab coats | lab coats | lab_coat | pobj | in | 3:5 |
| a table | table | table | pobj | at | 7:9 |
| each | each | each | nsubj | holding | 10:11 |
| a glass flask | flask | flask | dobj | holding | 12:15 |
| Three men | men | man | nsubj | wear | 16:18 |
| goggles | goggles | goggle | dobj | wear | 19:20 |
| liquids | liquids | liquid | dobj | pour | 22:23 |
| flasks | flasks | flask | pobj | into | 24:25 |
| a woman | woman | woman | nsubj | stands | 27:29 |
| a patterned hijab | hijab | hijab | pobj | in | 30:33 |
| them | them | they | pobj | beside | 35:36 |
| A logo | logo | logo | nsubj | are | 37:39 |
| text | text | text | conj | logo | 40:41 |
| the top | top | top | pobj | at | 44:46 |
| bottom | bottom | bottom | conj | top | 47:48 |
| the image | image | image | pobj | of | 49:51 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Four | four | NUM | CD | nummod | people | 1 |
| 1 | people | people | NOUN | NNS | nsubj | stand | 5 |
| 2 | in | in | ADP | IN | prep | people | 1 |
| 3 | white | white | ADJ | JJ | amod | lab coats | 4 |
| 4 | lab coats | lab_coat | NOUN | NN | pobj | in | 2 |
| 5 | stand | stand | VERB | VBP | ROOT | stand | 5 |
| 6 | at | at | ADP | IN | prep | stand | 5 |
| 7 | a | a | DET | DT | det | table | 8 |
| 8 | table | table | NOUN | NN | pobj | at | 6 |
| 9 | , | , | PUNCT | , | punct | stand | 5 |
| 10 | each | each | PRON | DT | nsubj | holding | 11 |
| 11 | holding | hold | VERB | VBG | advcl | stand | 5 |
| 12 | a | a | DET | DT | det | flask | 14 |
| 13 | glass | glass | NOUN | NN | compound | flask | 14 |
| 14 | flask | flask | NOUN | NN | dobj | holding | 11 |
| 15 | . | . | PUNCT | . | punct | stand | 5 |
| 16 | Three | three | NUM | CD | nummod | men | 17 |
| 17 | men | man | NOUN | NNS | nsubj | wear | 18 |
| 18 | wear | wear | VERB | VBP | ROOT | wear | 18 |
| 19 | goggles | goggle | NOUN | NNS | dobj | wear | 18 |
| 20 | and | and | CCONJ | CC | cc | wear | 18 |
| 21 | pour | pour | VERB | VBP | conj | wear | 18 |
| 22 | liquids | liquid | NOUN | NNS | dobj | pour | 21 |
| 23 | into | into | ADP | IN | prep | pour | 21 |
| 24 | flasks | flask | NOUN | NNS | pobj | into | 23 |
| 25 | , | , | PUNCT | , | punct | pour | 21 |
| 26 | while | while | SCONJ | IN | mark | stands | 33 |
| 27 | a | a | DET | DT | det | woman | 28 |
| 28 | woman | woman | NOUN | NN | nsubj | stands | 33 |
| 29 | in | in | ADP | IN | prep | woman | 28 |
| 30 | a | a | DET | DT | det | hijab | 32 |
| 31 | patterned | patterned | ADJ | JJ | amod | hijab | 32 |
| 32 | hijab | hijab | NOUN | NN | pobj | in | 29 |
| 33 | stands | stand | VERB | VBZ | conj | pour | 21 |
| 34 | beside | beside | ADP | IN | prep | stands | 33 |
| 35 | them | they | PRON | PRP | pobj | beside | 34 |
| 36 | . | . | PUNCT | . | punct | wear | 18 |
| 37 | A | a | DET | DT | det | logo | 38 |
| 38 | logo | logo | NOUN | NN | nsubj | are | 41 |
| 39 | and | and | CCONJ | CC | cc | logo | 38 |
| 40 | text | text | NOUN | NN | conj | logo | 38 |
| 41 | are | be | AUX | VBP | ROOT | are | 41 |
| 42 | visible | visible | ADJ | JJ | acomp | are | 41 |
| 43 | at | at | ADP | IN | prep | are | 41 |
| 44 | the | the | DET | DT | det | top | 45 |
| 45 | top | top | NOUN | NN | pobj | at | 43 |
| 46 | and | and | CCONJ | CC | cc | top | 45 |
| 47 | bottom | bottom | NOUN | NN | conj | top | 45 |
| 48 | of | of | ADP | IN | prep | top | 45 |
| 49 | the | the | DET | DT | det | image | 50 |
| 50 | image | image | NOUN | NN | pobj | of | 48 |
| 51 | . | . | PUNCT | . | punct | are | 41 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | people | people | chunk0 | 1 | noun_chunk_root | high |
| m1 | quantity | Four | four | chunk0 | 0 | quantity | high |
| m2 | object | lab coats | lab_coat | chunk1 | 4 | noun_chunk_root | high |
| m3 | attribute | white | white | chunk1 | 3 | color_attribute | high |
| m4 | object | table | table | chunk2 | 8 | noun_chunk_root | high |
| m5 | object | each | each | chunk3 | 10 | noun_chunk_root | high |
| m6 | object | flask | flask | chunk4 | 14 | noun_chunk_root | high |
| m7 | attribute | glass | glass | chunk4 | 13 | material_attribute | high |
| m8 | object | men | man | chunk5 | 17 | noun_chunk_root | high |
| m9 | quantity | Three | three | chunk5 | 16 | quantity | high |
| m10 | object | goggles | goggle | chunk6 | 19 | noun_chunk_root | high |
| m11 | object | liquids | liquid | chunk7 | 22 | noun_chunk_root | high |
| m12 | object | flasks | flask | chunk8 | 24 | noun_chunk_root | high |
| m13 | object | woman | woman | chunk9 | 28 | noun_chunk_root | high |
| m14 | object | hijab | hijab | chunk10 | 32 | noun_chunk_root | high |
| m15 | attribute | patterned | patterned | chunk10 | 31 | modifier_attribute | medium |
| m16 | object | them | they | chunk11 | 35 | noun_chunk_root | high |
| m17 | object | logo | logo | chunk12 | 38 | noun_chunk_root | high |
| m18 | object | text | text | chunk13 | 40 | noun_chunk_root | high |
| m19 | object | bottom | bottom | chunk15 | 47 | noun_chunk_root | high |
| m20 | object | image | image | chunk16 | 50 | noun_chunk_root | high |
| m21 | action | stand | stand | doc | 5 | verb_predicate | high |
| m22 | action | holding | hold | doc | 11 | verb_predicate | high |
| m23 | action | wear | wear | doc | 18 | verb_predicate | high |
| m24 | action | pour | pour | doc | 21 | verb_predicate | high |
| m25 | action | stands | stand | doc | 33 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_quantity | m0 | m1 | high | chunk0 nummod -> people |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> lab coats |
| e2 | has_attribute | m6 | m7 | high | chunk4 compound -> flask |
| e3 | has_quantity | m8 | m9 | high | chunk5 nummod -> men |
| e4 | has_attribute | m14 | m15 | medium | chunk10 amod -> hijab |
| e5 | agent | m21 | m0 | medium | nsubj -> stand |
| e6 | agent | m22 | m5 | medium | nsubj -> holding |
| e7 | patient | m22 | m6 | medium | dobj -> holding |
| e8 | agent | m23 | m8 | medium | nsubj -> wear |
| e9 | patient | m23 | m10 | medium | dobj -> wear |
| e10 | patient | m24 | m11 | medium | dobj -> pour |
| e11 | agent | m25 | m13 | medium | nsubj -> stands |
| e12 | relation | m0 | m2 | high | in |
| e13 | relation | m0 | m4 | medium | at |
| e14 | relation | m8 | m12 | medium | into |
| e15 | relation | m13 | m14 | high | in |
| e16 | relation | m13 | m16 | high | beside |
| e17 | relation | m17 | m20 | high | at_top_of |

## 99

**caption_shape:** `sentence-like`
**caption_id:** `5207ae2f4f54cd83ab86dd91b37fd66a2f511a9c2d803f88e8709886baf89c14`

> A domed ceiling with repeating octagonal patterns and a central skylight lets in bright light.

### Sentences
| sentence | token_span |
| --- | --- |
| A domed ceiling with repeating octagonal patterns and a central skylight lets in bright light. | 0:16 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A domed ceiling | ceiling | ceiling | nsubj | lets | 0:3 |
| repeating octagonal patterns | patterns | pattern | pobj | with | 4:7 |
| a central skylight | skylight | skylight | conj | ceiling | 8:11 |
| bright light | light | light | dobj | lets | 13:15 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | ceiling | 2 |
| 1 | domed | domed | ADJ | JJ | amod | ceiling | 2 |
| 2 | ceiling | ceiling | NOUN | NN | nsubj | lets | 11 |
| 3 | with | with | ADP | IN | prep | ceiling | 2 |
| 4 | repeating | repeat | VERB | VBG | amod | patterns | 6 |
| 5 | octagonal | octagonal | ADJ | JJ | amod | patterns | 6 |
| 6 | patterns | pattern | NOUN | NNS | pobj | with | 3 |
| 7 | and | and | CCONJ | CC | cc | ceiling | 2 |
| 8 | a | a | DET | DT | det | skylight | 10 |
| 9 | central | central | ADJ | JJ | amod | skylight | 10 |
| 10 | skylight | skylight | NOUN | NN | conj | ceiling | 2 |
| 11 | lets | let | VERB | VBZ | ROOT | lets | 11 |
| 12 | in | in | ADP | RP | prt | lets | 11 |
| 13 | bright | bright | ADJ | JJ | amod | light | 14 |
| 14 | light | light | NOUN | NN | dobj | lets | 11 |
| 15 | . | . | PUNCT | . | punct | lets | 11 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | ceiling | ceiling | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | domed | domed | chunk0 | 1 | modifier_attribute | medium |
| m2 | object | patterns | pattern | chunk1 | 6 | noun_chunk_root | high |
| m3 | attribute | repeating | repeat | chunk1 | 4 | state_attribute | medium |
| m4 | attribute | octagonal | octagonal | chunk1 | 5 | modifier_attribute | medium |
| m5 | object | skylight | skylight | chunk2 | 10 | noun_chunk_root | high |
| m6 | attribute | central | central | chunk2 | 9 | modifier_attribute | medium |
| m7 | object | light | light | chunk3 | 14 | noun_chunk_root | high |
| m8 | attribute | bright | bright | chunk3 | 13 | visual_attribute | medium |
| m9 | action | lets | let | doc | 11 | verb_predicate | high |

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
| e7 | patient | m9 | m7 | medium | dobj -> lets |
| e8 | relation | m0 | m2 | high | with |

## 100

**caption_shape:** `sentence-like`
**caption_id:** `52c6598a381abe73c3610f5d91093f1c455d382883d1a9f5a94877f489cdc814`

> An aerial view shows a town with houses, a river, and roads winding through green fields and hills.

### Sentences
| sentence | token_span |
| --- | --- |
| An aerial view shows a town with houses, a river, and roads winding through green fields and hills. | 0:21 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| An aerial view | view | view | nsubj | shows | 0:3 |
| a town | town | town | dobj | shows | 4:6 |
| houses | houses | house | pobj | with | 7:8 |
| a river | river | river | conj | houses | 9:11 |
| roads | roads | road | conj | river | 13:14 |
| green fields | fields | field | pobj | through | 16:18 |
| hills | hills | hill | conj | fields | 19:20 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | An | an | DET | DT | det | view | 2 |
| 1 | aerial | aerial | ADJ | JJ | amod | view | 2 |
| 2 | view | view | NOUN | NN | nsubj | shows | 3 |
| 3 | shows | show | VERB | VBZ | ROOT | shows | 3 |
| 4 | a | a | DET | DT | det | town | 5 |
| 5 | town | town | NOUN | NN | dobj | shows | 3 |
| 6 | with | with | ADP | IN | prep | town | 5 |
| 7 | houses | house | NOUN | NNS | pobj | with | 6 |
| 8 | , | , | PUNCT | , | punct | houses | 7 |
| 9 | a | a | DET | DT | det | river | 10 |
| 10 | river | river | NOUN | NN | conj | houses | 7 |
| 11 | , | , | PUNCT | , | punct | river | 10 |
| 12 | and | and | CCONJ | CC | cc | river | 10 |
| 13 | roads | road | NOUN | NNS | conj | river | 10 |
| 14 | winding | wind | VERB | VBG | acl | roads | 13 |
| 15 | through | through | ADP | IN | prep | winding | 14 |
| 16 | green | green | ADJ | JJ | amod | fields | 17 |
| 17 | fields | field | NOUN | NNS | pobj | through | 15 |
| 18 | and | and | CCONJ | CC | cc | fields | 17 |
| 19 | hills | hill | NOUN | NNS | conj | fields | 17 |
| 20 | . | . | PUNCT | . | punct | shows | 3 |

### Raw Concept Mentions
| id | type | text | lemma | source_tag | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| m0 | object | view | view | chunk0 | 2 | noun_chunk_root | high |
| m1 | attribute | aerial | aerial | chunk0 | 1 | modifier_attribute | medium |
| m2 | object | town | town | chunk1 | 5 | noun_chunk_root | high |
| m3 | object | houses | house | chunk2 | 7 | noun_chunk_root | high |
| m4 | object | river | river | chunk3 | 10 | noun_chunk_root | high |
| m5 | object | roads | road | chunk4 | 13 | noun_chunk_root | high |
| m6 | object | fields | field | chunk5 | 17 | noun_chunk_root | high |
| m7 | attribute | green | green | chunk5 | 16 | color_attribute | high |
| m8 | object | hills | hill | chunk6 | 19 | noun_chunk_root | high |
| m9 | action | shows | show | doc | 3 | verb_predicate | high |
| m10 | action | winding | wind | doc | 14 | verb_predicate | high |

### Raw Concept Edges
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | medium | chunk0 amod -> view |
| e1 | has_attribute | m6 | m7 | high | chunk5 amod -> fields |
| e2 | agent | m9 | m0 | medium | nsubj -> shows |
| e3 | patient | m9 | m2 | medium | dobj -> shows |
| e4 | relation | m2 | m3 | high | with |
| e5 | relation | m2 | m4 | high | with |
| e6 | relation | m2 | m5 | high | with |
| e7 | relation | m5 | m6 | medium | through |
| e8 | relation | m5 | m8 | medium | through |
