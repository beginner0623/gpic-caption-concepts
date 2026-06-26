# Raw Quote Retokenizer Experiment

- model: `en_core_web_trf`
- `raw_no_merge`: 원문 caption을 그대로 parsing
- `raw_merge_after_parser`: spaCy 전체 pipeline 후 `"..."` span을 merge
- `raw_merge_first`: tokenizer 직후, transformer/tagger/parser 전에 `"..."` span을 merge
- `raw_merge_before_parser`: transformer/tagger 뒤, parser 전에 `"..."` span을 merge

## Summary

이 실험은 quote를 `the quoted text`로 바꾸지 않고, 원문 `"..."` span 자체를 Retokenizer로 합쳤을 때 parser와 Stage 8 후보가 어떻게 달라지는지 확인하기 위한 것입니다.

## Observed Result

- `raw_merge_first`가 이번 비교에서 가장 낫습니다. quote span을 tokenizer 직후 하나의 token으로 합치면 `a "ROYAL CANIN" banner`, `the number "1709-1"`, `screen shows "..."`, `poster reads "..."` 구조가 대체로 자연스럽게 유지됩니다.
- `raw_merge_first`는 `the quoted text` placeholder를 만들지 않으므로 `a the quoted text banner` 같은 문법 오염이 생기지 않습니다.
- `raw_merge_after_parser`는 token만 합칠 뿐 이미 끝난 dependency/POS 판단을 되돌리지 못합니다. 그래서 quote 안 첫 단어가 동사처럼 분석된 경우에는 action 오염이 남을 수 있습니다.
- `raw_merge_before_parser`처럼 transformer/tagger 뒤, parser 앞에서만 합치는 방식은 권장하지 않습니다. POS/tag 정보가 quote-open token 쪽으로 남아 merged token이 `PUNCT`처럼 취급되고 dependency가 크게 깨졌습니다.
- 그래도 최종 Stage 9에서는 merged quote token을 실제 object 이름으로 세지 말고 `TEXT_SPAN(qid)` 또는 `LABEL_VALUE(qid)` 같은 quote mention으로 canonicalize해야 합니다.

## royal_canin_banner

**raw_caption:**

> A brown dog leaps over a blue, white, and red basket on grass. A man in a black outfit with red and blue trim stands nearby, watching the dog. In the background, spectators stand behind a fence near a "ROYAL CANIN" banner.

**masked_caption_reference:**

> A brown dog leaps over a blue, white, and red basket on grass. A man in a black outfit with red and blue trim stands nearby, watching the dog. In the background, spectators stand behind a fence near a the quoted text banner.

### Quote Mentions
| id | text_raw | placeholder | consumed_prefix | raw_span | masked_span |
| --- | --- | --- | --- | --- | --- |
| q0 | ROYAL CANIN | the quoted text |  | 201:214 | 201:216 |

### raw_no_merge

**Noun Chunks**
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
| a "ROYAL CANIN" banner | banner | banner | pobj | near | 44:50 |

**Tokens**
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
| 44 | a | a | DET | DT | det | banner | 49 |
| 45 | " | " | PUNCT | `` | punct | banner | 49 |
| 46 | ROYAL | ROYAL | PROPN | NNP | nmod | CANIN | 47 |
| 47 | CANIN | CANIN | PROPN | NNP | nmod | banner | 49 |
| 48 | " | " | PUNCT | '' | punct | banner | 49 |
| 49 | banner | banner | NOUN | NN | pobj | near | 43 |
| 50 | . | . | PUNCT | . | punct | stand | 39 |

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | dog | dog | 2 | noun_chunk_root | high |
| m1 | attribute | brown | brown | 1 | color_attribute | high |
| m2 | object | basket | basket | 12 | noun_chunk_root | high |
| m3 | attribute | blue | blue | 6 | color_attribute | high |
| m4 | attribute | white | white | 8 | color_attribute | high |
| m5 | attribute | red | red | 11 | color_attribute | high |
| m6 | object | grass | grass | 14 | noun_chunk_root | high |
| m7 | object | man | man | 17 | noun_chunk_root | high |
| m8 | object | outfit | outfit | 21 | noun_chunk_root | high |
| m9 | attribute | black | black | 20 | color_attribute | high |
| m10 | object | trim | trim | 26 | noun_chunk_root | high |
| m11 | attribute | red | red | 23 | color_attribute | high |
| m12 | attribute | blue | blue | 25 | color_attribute | high |
| m13 | object | dog | dog | 32 | noun_chunk_root | high |
| m14 | object | background | background | 36 | noun_chunk_root | high |
| m15 | object | spectators | spectator | 38 | noun_chunk_root | high |
| m16 | object | fence | fence | 42 | noun_chunk_root | high |
| m17 | object | banner | banner | 49 | noun_chunk_root | high |
| m18 | context | background | background | 36 | context_word | medium |
| m19 | action | leaps | leap | 3 | verb_predicate | high |
| m20 | action | stands | stand | 27 | verb_predicate | high |
| m21 | action | watching | watch | 30 | verb_predicate | high |
| m22 | action | stand | stand | 39 | verb_predicate | high |

**Raw Concept Edges**
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

### raw_merge_after_parser

**Noun Chunks**
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

**Tokens**
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

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | dog | dog | 2 | noun_chunk_root | high |
| m1 | attribute | brown | brown | 1 | color_attribute | high |
| m2 | object | basket | basket | 12 | noun_chunk_root | high |
| m3 | attribute | blue | blue | 6 | color_attribute | high |
| m4 | attribute | white | white | 8 | color_attribute | high |
| m5 | attribute | red | red | 11 | color_attribute | high |
| m6 | object | grass | grass | 14 | noun_chunk_root | high |
| m7 | object | man | man | 17 | noun_chunk_root | high |
| m8 | object | outfit | outfit | 21 | noun_chunk_root | high |
| m9 | attribute | black | black | 20 | color_attribute | high |
| m10 | object | trim | trim | 26 | noun_chunk_root | high |
| m11 | attribute | red | red | 23 | color_attribute | high |
| m12 | attribute | blue | blue | 25 | color_attribute | high |
| m13 | object | dog | dog | 32 | noun_chunk_root | high |
| m14 | object | background | background | 36 | noun_chunk_root | high |
| m15 | object | spectators | spectator | 38 | noun_chunk_root | high |
| m16 | object | fence | fence | 42 | noun_chunk_root | high |
| m17 | object | banner | banner | 46 | noun_chunk_root | high |
| m18 | context | background | background | 36 | context_word | medium |
| m19 | action | leaps | leap | 3 | verb_predicate | high |
| m20 | action | stands | stand | 27 | verb_predicate | high |
| m21 | action | watching | watch | 30 | verb_predicate | high |
| m22 | action | stand | stand | 39 | verb_predicate | high |

**Raw Concept Edges**
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

### raw_merge_first

**Noun Chunks**
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

**Tokens**
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

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | dog | dog | 2 | noun_chunk_root | high |
| m1 | attribute | brown | brown | 1 | color_attribute | high |
| m2 | object | basket | basket | 12 | noun_chunk_root | high |
| m3 | attribute | blue | blue | 6 | color_attribute | high |
| m4 | attribute | white | white | 8 | color_attribute | high |
| m5 | attribute | red | red | 11 | color_attribute | high |
| m6 | object | grass | grass | 14 | noun_chunk_root | high |
| m7 | object | man | man | 17 | noun_chunk_root | high |
| m8 | object | outfit | outfit | 21 | noun_chunk_root | high |
| m9 | attribute | black | black | 20 | color_attribute | high |
| m10 | object | trim | trim | 26 | noun_chunk_root | high |
| m11 | attribute | red | red | 23 | color_attribute | high |
| m12 | attribute | blue | blue | 25 | color_attribute | high |
| m13 | object | dog | dog | 32 | noun_chunk_root | high |
| m14 | object | background | background | 36 | noun_chunk_root | high |
| m15 | object | spectators | spectator | 38 | noun_chunk_root | high |
| m16 | object | fence | fence | 42 | noun_chunk_root | high |
| m17 | object | banner | banner | 46 | noun_chunk_root | high |
| m18 | context | background | background | 36 | context_word | medium |
| m19 | action | leaps | leap | 3 | verb_predicate | high |
| m20 | action | stands | stand | 27 | verb_predicate | high |
| m21 | action | watching | watch | 30 | verb_predicate | high |
| m22 | action | stand | stand | 39 | verb_predicate | high |

**Raw Concept Edges**
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

### raw_merge_before_parser

**Noun Chunks**
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

**Tokens**
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
| 44 | a | a | DET | DT | det | . | 47 |
| 45 | "ROYAL CANIN" | royal_canin | PUNCT | `` | punct | . | 47 |
| 46 | banner | banner | NOUN | NN | nmod | . | 47 |
| 47 | . | . | PUNCT | . | pobj | near | 43 |

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | dog | dog | 2 | noun_chunk_root | high |
| m1 | attribute | brown | brown | 1 | color_attribute | high |
| m2 | object | basket | basket | 12 | noun_chunk_root | high |
| m3 | attribute | blue | blue | 6 | color_attribute | high |
| m4 | attribute | white | white | 8 | color_attribute | high |
| m5 | attribute | red | red | 11 | color_attribute | high |
| m6 | object | grass | grass | 14 | noun_chunk_root | high |
| m7 | object | man | man | 17 | noun_chunk_root | high |
| m8 | object | outfit | outfit | 21 | noun_chunk_root | high |
| m9 | attribute | black | black | 20 | color_attribute | high |
| m10 | object | trim | trim | 26 | noun_chunk_root | high |
| m11 | attribute | red | red | 23 | color_attribute | high |
| m12 | attribute | blue | blue | 25 | color_attribute | high |
| m13 | object | dog | dog | 32 | noun_chunk_root | high |
| m14 | object | background | background | 36 | noun_chunk_root | high |
| m15 | object | spectators | spectator | 38 | noun_chunk_root | high |
| m16 | object | fence | fence | 42 | noun_chunk_root | high |
| m17 | context | background | background | 36 | context_word | medium |
| m18 | action | leaps | leap | 3 | verb_predicate | high |
| m19 | action | stands | stand | 27 | verb_predicate | high |
| m20 | action | watching | watch | 30 | verb_predicate | high |
| m21 | action | stand | stand | 39 | verb_predicate | high |

**Raw Concept Edges**
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> dog |
| e1 | has_attribute | m2 | m3 | high | chunk1 amod -> basket |
| e2 | has_attribute | m2 | m4 | high | chunk1 conj -> basket |
| e3 | has_attribute | m2 | m5 | high | chunk1 conj -> basket |
| e4 | has_attribute | m8 | m9 | high | chunk4 amod -> outfit |
| e5 | has_attribute | m10 | m11 | high | chunk5 amod -> trim |
| e6 | has_attribute | m10 | m12 | high | chunk5 conj -> trim |
| e7 | has_context | scene | m17 | medium | context token background |
| e8 | agent | m18 | m0 | medium | nsubj -> leaps |
| e9 | agent | m19 | m7 | medium | nsubj -> stands |
| e10 | patient | m20 | m13 | medium | dobj -> watching |
| e11 | agent | m21 | m15 | medium | nsubj -> stand |
| e12 | relation | m0 | m2 | high | over |
| e13 | relation | m2 | m6 | high | on |
| e14 | relation | m7 | m8 | high | in |
| e15 | relation | m8 | m10 | high | with |
| e16 | relation | m15 | m17 | high | in |
| e17 | relation | m15 | m16 | high | behind |

## number_tag

**raw_caption:**

> A white fabric tag with the number "1709-1" is stitched onto a bright yellow garment. The tag is slightly frayed at the edges and sits against the textured, wrinkled fabric of the clothing.

**masked_caption_reference:**

> A white fabric tag with the number the quoted text is stitched onto a bright yellow garment. The tag is slightly frayed at the edges and sits against the textured, wrinkled fabric of the clothing.

### Quote Mentions
| id | text_raw | placeholder | consumed_prefix | raw_span | masked_span |
| --- | --- | --- | --- | --- | --- |
| q0 | 1709-1 | the quoted text |  | 35:43 | 35:50 |

### raw_no_merge

**Noun Chunks**
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A white fabric tag | tag | tag | nsubjpass | stitched | 0:4 |
| the number | number | number | pobj | with | 5:7 |
| a bright yellow garment | garment | garment | pobj | onto | 15:19 |
| The tag | tag | tag | nsubjpass | frayed | 20:22 |
| the edges | edges | edge | pobj | at | 26:28 |
| the textured, wrinkled fabric | fabric | fabric | pobj | against | 31:36 |
| the clothing | clothing | clothing | pobj | of | 37:39 |

**Tokens**
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | tag | 3 |
| 1 | white | white | ADJ | JJ | amod | tag | 3 |
| 2 | fabric | fabric | NOUN | NN | compound | tag | 3 |
| 3 | tag | tag | NOUN | NN | nsubjpass | stitched | 13 |
| 4 | with | with | ADP | IN | prep | tag | 3 |
| 5 | the | the | DET | DT | det | number | 6 |
| 6 | number | number | NOUN | NN | pobj | with | 4 |
| 7 | " | " | PUNCT | `` | punct | number | 6 |
| 8 | 1709 | 1709 | NUM | CD | appos | number | 6 |
| 9 | - | - | PUNCT | HYPH | punct | number | 6 |
| 10 | 1 | 1 | NUM | CD | appos | number | 6 |
| 11 | " | " | PUNCT | '' | punct | number | 6 |
| 12 | is | be | AUX | VBZ | auxpass | stitched | 13 |
| 13 | stitched | stitch | VERB | VBN | ROOT | stitched | 13 |
| 14 | onto | onto | ADP | IN | prep | stitched | 13 |
| 15 | a | a | DET | DT | det | garment | 18 |
| 16 | bright | bright | ADJ | JJ | amod | yellow | 17 |
| 17 | yellow | yellow | ADJ | JJ | amod | garment | 18 |
| 18 | garment | garment | NOUN | NN | pobj | onto | 14 |
| 19 | . | . | PUNCT | . | punct | stitched | 13 |
| 20 | The | the | DET | DT | det | tag | 21 |
| 21 | tag | tag | NOUN | NN | nsubjpass | frayed | 24 |
| 22 | is | be | AUX | VBZ | auxpass | frayed | 24 |
| 23 | slightly | slightly | ADV | RB | advmod | frayed | 24 |
| 24 | frayed | fray | VERB | VBN | ROOT | frayed | 24 |
| 25 | at | at | ADP | IN | prep | frayed | 24 |
| 26 | the | the | DET | DT | det | edges | 27 |
| 27 | edges | edge | NOUN | NNS | pobj | at | 25 |
| 28 | and | and | CCONJ | CC | cc | frayed | 24 |
| 29 | sits | sit | VERB | VBZ | conj | frayed | 24 |
| 30 | against | against | ADP | IN | prep | sits | 29 |
| 31 | the | the | DET | DT | det | fabric | 35 |
| 32 | textured | textured | ADJ | JJ | amod | fabric | 35 |
| 33 | , | , | PUNCT | , | punct | fabric | 35 |
| 34 | wrinkled | wrinkled | ADJ | JJ | amod | fabric | 35 |
| 35 | fabric | fabric | NOUN | NN | pobj | against | 30 |
| 36 | of | of | ADP | IN | prep | fabric | 35 |
| 37 | the | the | DET | DT | det | clothing | 38 |
| 38 | clothing | clothing | NOUN | NN | pobj | of | 36 |
| 39 | . | . | PUNCT | . | punct | frayed | 24 |

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | tag | tag | 3 | noun_chunk_root | high |
| m1 | attribute | white | white | 1 | color_attribute | high |
| m2 | attribute | fabric | fabric | 2 | material_attribute | high |
| m3 | object | number | number | 6 | noun_chunk_root | high |
| m4 | object | garment | garment | 18 | noun_chunk_root | high |
| m5 | attribute | bright | bright | 16 | visual_attribute | medium |
| m6 | attribute | yellow | yellow | 17 | color_attribute | high |
| m7 | object | tag | tag | 21 | noun_chunk_root | high |
| m8 | context | edges | edge | 27 | spatial_region | medium |
| m9 | object | fabric | fabric | 35 | noun_chunk_root | high |
| m10 | attribute | textured | textured | 32 | modifier_attribute | medium |
| m11 | attribute | wrinkled | wrinkled | 34 | modifier_attribute | medium |
| m12 | object | clothing | clothing | 38 | noun_chunk_root | high |
| m13 | action | stitched | stitch | 13 | verb_predicate | high |
| m14 | action | frayed | fray | 24 | verb_predicate | high |
| m15 | action | sits | sit | 29 | verb_predicate | high |

**Raw Concept Edges**
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

### raw_merge_after_parser

**Noun Chunks**
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A white fabric tag | tag | tag | nsubjpass | stitched | 0:4 |
| the number | number | number | pobj | with | 5:7 |
| a bright yellow garment | garment | garment | pobj | onto | 11:15 |
| The tag | tag | tag | nsubjpass | frayed | 16:18 |
| the edges | edges | edge | pobj | at | 22:24 |
| the textured, wrinkled fabric | fabric | fabric | pobj | against | 27:32 |
| the clothing | clothing | clothing | pobj | of | 33:35 |

**Tokens**
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

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | tag | tag | 3 | noun_chunk_root | high |
| m1 | attribute | white | white | 1 | color_attribute | high |
| m2 | attribute | fabric | fabric | 2 | material_attribute | high |
| m3 | object | number | number | 6 | noun_chunk_root | high |
| m4 | object | garment | garment | 14 | noun_chunk_root | high |
| m5 | attribute | bright | bright | 12 | visual_attribute | medium |
| m6 | attribute | yellow | yellow | 13 | color_attribute | high |
| m7 | object | tag | tag | 17 | noun_chunk_root | high |
| m8 | context | edges | edge | 23 | spatial_region | medium |
| m9 | object | fabric | fabric | 31 | noun_chunk_root | high |
| m10 | attribute | textured | textured | 28 | modifier_attribute | medium |
| m11 | attribute | wrinkled | wrinkled | 30 | modifier_attribute | medium |
| m12 | object | clothing | clothing | 34 | noun_chunk_root | high |
| m13 | action | stitched | stitch | 9 | verb_predicate | high |
| m14 | action | frayed | fray | 20 | verb_predicate | high |
| m15 | action | sits | sit | 25 | verb_predicate | high |

**Raw Concept Edges**
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

### raw_merge_first

**Noun Chunks**
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A white fabric tag | tag | tag | nsubjpass | stitched | 0:4 |
| the number | number | number | pobj | with | 5:7 |
| a bright yellow garment | garment | garment | pobj | onto | 11:15 |
| The tag | tag | tag | nsubjpass | frayed | 16:18 |
| the edges | edges | edge | pobj | at | 22:24 |
| the textured, wrinkled fabric | fabric | fabric | pobj | against | 27:32 |
| the clothing | clothing | clothing | pobj | of | 33:35 |

**Tokens**
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

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | tag | tag | 3 | noun_chunk_root | high |
| m1 | attribute | white | white | 1 | color_attribute | high |
| m2 | attribute | fabric | fabric | 2 | material_attribute | high |
| m3 | object | number | number | 6 | noun_chunk_root | high |
| m4 | object | garment | garment | 14 | noun_chunk_root | high |
| m5 | attribute | bright | bright | 12 | visual_attribute | medium |
| m6 | attribute | yellow | yellow | 13 | color_attribute | high |
| m7 | object | tag | tag | 17 | noun_chunk_root | high |
| m8 | context | edges | edge | 23 | spatial_region | medium |
| m9 | object | fabric | fabric | 31 | noun_chunk_root | high |
| m10 | attribute | textured | textured | 28 | modifier_attribute | medium |
| m11 | attribute | wrinkled | wrinkled | 30 | modifier_attribute | medium |
| m12 | object | clothing | clothing | 34 | noun_chunk_root | high |
| m13 | action | stitched | stitch | 9 | verb_predicate | high |
| m14 | action | frayed | fray | 20 | verb_predicate | high |
| m15 | action | sits | sit | 25 | verb_predicate | high |

**Raw Concept Edges**
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

### raw_merge_before_parser

**Noun Chunks**
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A white fabric tag | tag | tag | nsubjpass | yellow | 0:4 |
| the number | number | number | pobj | with | 5:7 |
| against the | the | the | pobj | sits | 26:28 |

**Tokens**
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | tag | 3 |
| 1 | white | white | ADJ | JJ | amod | tag | 3 |
| 2 | fabric | fabric | NOUN | NN | compound | tag | 3 |
| 3 | tag | tag | NOUN | NN | nsubjpass | yellow | 13 |
| 4 | with | with | ADP | IN | prep | tag | 3 |
| 5 | the | the | DET | DT | det | number | 6 |
| 6 | number | number | NOUN | NN | pobj | with | 4 |
| 7 | "1709-1" | 1709-1 | PUNCT | `` | punct | number | 6 |
| 8 | is | be | AUX | VBZ | appos | number | 6 |
| 9 | stitched | stitch | VERB | VBN | punct | number | 6 |
| 10 | onto | onto | ADP | IN | appos | number | 6 |
| 11 | a | a | PRON | DT | punct | number | 6 |
| 12 | bright | bright | AUX | JJ | auxpass | yellow | 13 |
| 13 | yellow | yellow | ADJ | JJ | ROOT | yellow | 13 |
| 14 | garment | garment | NOUN | NN | prep | yellow | 13 |
| 15 | . | . | PUNCT | . | det | is | 18 |
| 16 | The | the | PRON | DT | amod | tag | 17 |
| 17 | tag | tag | NOUN | NN | amod | is | 18 |
| 18 | is | be | AUX | VBZ | pobj | garment | 14 |
| 19 | slightly | slightly | ADV | RB | punct | yellow | 13 |
| 20 | frayed | fray | VERB | VBN | det | at | 21 |
| 21 | at | at | ADP | IN | nsubjpass | and | 24 |
| 22 | the | the | PRON | DT | auxpass | and | 24 |
| 23 | edges | edge | NOUN | NNS | advmod | and | 24 |
| 24 | and | and | CCONJ | CC | ROOT | and | 24 |
| 25 | sits | sit | VERB | VBZ | prep | and | 24 |
| 26 | against | against | ADP | IN | det | the | 27 |
| 27 | the | the | PRON | DT | pobj | sits | 25 |
| 28 | textured | textured | ADJ | JJ | cc | and | 24 |
| 29 | , | , | PUNCT | , | conj | and | 24 |
| 30 | wrinkled | wrinkled | ADJ | JJ | prep | , | 29 |
| 31 | fabric | fabric | NOUN | NN | det | . | 35 |
| 32 | of | of | ADP | IN | amod | . | 35 |
| 33 | the | the | PRON | DT | punct | . | 35 |
| 34 | clothing | clothing | NOUN | NN | amod | . | 35 |
| 35 | . | . | PUNCT | . | pobj | wrinkled | 30 |

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | tag | tag | 3 | noun_chunk_root | high |
| m1 | attribute | white | white | 1 | color_attribute | high |
| m2 | attribute | fabric | fabric | 2 | material_attribute | high |
| m3 | object | number | number | 6 | noun_chunk_root | high |
| m4 | action | stitched | stitch | 9 | verb_predicate | high |
| m5 | action | frayed | fray | 20 | verb_predicate | high |
| m6 | action | sits | sit | 25 | verb_predicate | high |

**Raw Concept Edges**
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> tag |
| e1 | has_attribute | m0 | m2 | high | chunk0 compound -> tag |
| e2 | relation | m0 | m3 | high | with |

## screen_shows_text

**raw_caption:**

> A woman stands at a podium speaking in front of an audience. An American flag is behind her, and a screen shows "Closing the Access Divide."

**masked_caption_reference:**

> A woman stands at a podium speaking in front of an audience. An American flag is behind her, and a screen shows the quoted text.

### Quote Mentions
| id | text_raw | placeholder | consumed_prefix | raw_span | masked_span |
| --- | --- | --- | --- | --- | --- |
| q0 | Closing the Access Divide. | the quoted text |  | 112:140 | 112:127 |

### raw_no_merge

**Noun Chunks**
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A woman | woman | woman | nsubj | stands | 0:2 |
| a podium | podium | podium | pobj | at | 4:6 |
| front | front | front | pobj | in | 8:9 |
| an audience | audience | audience | pobj | of | 10:12 |
| An American flag | flag | flag | nsubj | is | 13:16 |
| her | her | she | pobj | behind | 18:19 |
| a screen | screen | screen | nsubj | shows | 21:23 |
| the Access Divide | Divide | divide | dobj | Closing | 26:29 |

**Tokens**
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
| 24 | " | " | PUNCT | `` | punct | shows | 23 |
| 25 | Closing | close | VERB | VBG | xcomp | shows | 23 |
| 26 | the | the | DET | DT | det | Divide | 28 |
| 27 | Access | Access | PROPN | NNP | compound | Divide | 28 |
| 28 | Divide | divide | NOUN | NN | dobj | Closing | 25 |
| 29 | . | . | PUNCT | . | punct | shows | 23 |
| 30 | " | " | PUNCT | '' | punct | shows | 23 |

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | 1 | noun_chunk_root | high |
| m1 | object | podium | podium | 5 | noun_chunk_root | high |
| m2 | object | audience | audience | 11 | noun_chunk_root | high |
| m3 | object | flag | flag | 15 | noun_chunk_root | high |
| m4 | attribute | American | american | 14 | modifier_attribute | medium |
| m5 | object | screen | screen | 22 | noun_chunk_root | high |
| m6 | object | Divide | divide | 28 | noun_chunk_root | high |
| m7 | attribute | Access | access | 27 | compound_modifier | medium |
| m8 | action | stands | stand | 2 | verb_predicate | high |
| m9 | action | speaking | speak | 6 | verb_predicate | high |
| m10 | action | shows | show | 23 | verb_predicate | high |
| m11 | action | Closing | close | 25 | verb_predicate | high |

**Raw Concept Edges**
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m3 | m4 | medium | chunk4 amod -> flag |
| e1 | has_attribute | m6 | m7 | medium | chunk7 compound -> Divide |
| e2 | agent | m8 | m0 | medium | nsubj -> stands |
| e3 | agent | m10 | m5 | medium | nsubj -> shows |
| e4 | patient | m11 | m6 | medium | dobj -> Closing |
| e5 | relation | m0 | m1 | medium | at |
| e6 | relation | m0 | m2 | high | in_front_of |
| e7 | relation | m3 | m0 | high | behind |

### raw_merge_after_parser

**Noun Chunks**
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A woman | woman | woman | nsubj | stands | 0:2 |
| a podium | podium | podium | pobj | at | 4:6 |
| front | front | front | pobj | in | 8:9 |
| an audience | audience | audience | pobj | of | 10:12 |
| An American flag | flag | flag | nsubj | is | 13:16 |
| her | her | she | pobj | behind | 18:19 |
| a screen | screen | screen | nsubj | shows | 21:23 |

**Tokens**
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
| 24 | "Closing the Access Divide." | closing_the_access_divide. | VERB | VBG | xcomp | shows | 23 |

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | 1 | noun_chunk_root | high |
| m1 | object | podium | podium | 5 | noun_chunk_root | high |
| m2 | object | audience | audience | 11 | noun_chunk_root | high |
| m3 | object | flag | flag | 15 | noun_chunk_root | high |
| m4 | attribute | American | american | 14 | modifier_attribute | medium |
| m5 | object | screen | screen | 22 | noun_chunk_root | high |
| m6 | action | stands | stand | 2 | verb_predicate | high |
| m7 | action | speaking | speak | 6 | verb_predicate | high |
| m8 | action | shows | show | 23 | verb_predicate | high |
| m9 | action | "Closing the Access Divide." | closing_the_access_divide. | 24 | verb_predicate | high |

**Raw Concept Edges**
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m3 | m4 | medium | chunk4 amod -> flag |
| e1 | agent | m6 | m0 | medium | nsubj -> stands |
| e2 | agent | m8 | m5 | medium | nsubj -> shows |
| e3 | relation | m0 | m1 | medium | at |
| e4 | relation | m0 | m2 | high | in_front_of |
| e5 | relation | m3 | m0 | high | behind |

### raw_merge_first

**Noun Chunks**
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A woman | woman | woman | nsubj | stands | 0:2 |
| a podium | podium | podium | pobj | at | 4:6 |
| front | front | front | pobj | in | 8:9 |
| an audience | audience | audience | pobj | of | 10:12 |
| An American flag | flag | flag | nsubj | is | 13:16 |
| her | her | she | pobj | behind | 18:19 |
| a screen | screen | screen | nsubj | shows | 21:23 |
| "Closing the Access Divide." | "Closing the Access Divide." | closing_the_access_divide. | dobj | shows | 24:25 |

**Tokens**
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
| 24 | "Closing the Access Divide." | closing_the_access_divide. | PROPN | NNP | dobj | shows | 23 |

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | 1 | noun_chunk_root | high |
| m1 | object | podium | podium | 5 | noun_chunk_root | high |
| m2 | object | audience | audience | 11 | noun_chunk_root | high |
| m3 | object | flag | flag | 15 | noun_chunk_root | high |
| m4 | attribute | American | american | 14 | modifier_attribute | medium |
| m5 | object | screen | screen | 22 | noun_chunk_root | high |
| m6 | object | "Closing the Access Divide." | closing_the_access_divide. | 24 | noun_chunk_root | high |
| m7 | action | stands | stand | 2 | verb_predicate | high |
| m8 | action | speaking | speak | 6 | verb_predicate | high |
| m9 | action | shows | show | 23 | verb_predicate | high |

**Raw Concept Edges**
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m3 | m4 | medium | chunk4 amod -> flag |
| e1 | agent | m7 | m0 | medium | nsubj -> stands |
| e2 | agent | m9 | m5 | medium | nsubj -> shows |
| e3 | patient | m9 | m6 | medium | dobj -> shows |
| e4 | relation | m0 | m1 | medium | at |
| e5 | relation | m0 | m2 | high | in_front_of |
| e6 | relation | m3 | m0 | high | behind |

### raw_merge_before_parser

**Noun Chunks**
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A woman | woman | woman | nsubj | stands | 0:2 |
| a podium | podium | podium | pobj | at | 4:6 |
| front | front | front | pobj | in | 8:9 |
| an audience | audience | audience | pobj | of | 10:12 |
| An American flag | flag | flag | nsubj | is | 13:16 |
| her | her | she | pobj | behind | 18:19 |
| a screen | screen | screen | nsubj | shows | 21:23 |

**Tokens**
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
| 24 | "Closing the Access Divide." | closing_the_access_divide. | PUNCT | `` | punct | shows | 23 |

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | woman | woman | 1 | noun_chunk_root | high |
| m1 | object | podium | podium | 5 | noun_chunk_root | high |
| m2 | object | audience | audience | 11 | noun_chunk_root | high |
| m3 | object | flag | flag | 15 | noun_chunk_root | high |
| m4 | attribute | American | american | 14 | modifier_attribute | medium |
| m5 | object | screen | screen | 22 | noun_chunk_root | high |
| m6 | action | stands | stand | 2 | verb_predicate | high |
| m7 | action | speaking | speak | 6 | verb_predicate | high |
| m8 | action | shows | show | 23 | verb_predicate | high |

**Raw Concept Edges**
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m3 | m4 | medium | chunk4 amod -> flag |
| e1 | agent | m6 | m0 | medium | nsubj -> stands |
| e2 | agent | m8 | m5 | medium | nsubj -> shows |
| e3 | relation | m0 | m1 | medium | at |
| e4 | relation | m0 | m2 | high | in_front_of |
| e5 | relation | m3 | m0 | high | behind |

## poster_reads_text

**raw_caption:**

> A poster on a black trash can reads "BANG GOES THE KNIGHTHOOD" with a silhouette of a man in a hat. The scene is on a city sidewalk.

**masked_caption_reference:**

> A poster on a black trash can reads the quoted text with a silhouette of a man in a hat. The scene is on a city sidewalk.

### Quote Mentions
| id | text_raw | placeholder | consumed_prefix | raw_span | masked_span |
| --- | --- | --- | --- | --- | --- |
| q0 | BANG GOES THE KNIGHTHOOD | the quoted text |  | 36:62 | 36:51 |

### raw_no_merge

**Noun Chunks**
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A poster | poster | poster | nsubj | reads | 0:2 |
| a black trash can | can | can | pobj | on | 3:7 |
| BANG | BANG | BANG | nsubj | GOES | 9:10 |
| THE KNIGHTHOOD | KNIGHTHOOD | knighthood | dobj | GOES | 11:13 |
| a silhouette | silhouette | silhouette | pobj | with | 15:17 |
| a man | man | man | pobj | of | 18:20 |
| a hat | hat | hat | pobj | in | 21:23 |
| The scene | scene | scene | nsubj | is | 24:26 |
| a city sidewalk | sidewalk | sidewalk | pobj | on | 28:31 |

**Tokens**
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
| 8 | " | " | PUNCT | `` | punct | reads | 7 |
| 9 | BANG | BANG | PROPN | NNP | nsubj | GOES | 10 |
| 10 | GOES | go | VERB | VBZ | ccomp | reads | 7 |
| 11 | THE | the | DET | DT | det | KNIGHTHOOD | 12 |
| 12 | KNIGHTHOOD | knighthood | NOUN | NN | dobj | GOES | 10 |
| 13 | " | " | PUNCT | '' | punct | GOES | 10 |
| 14 | with | with | ADP | IN | prep | reads | 7 |
| 15 | a | a | DET | DT | det | silhouette | 16 |
| 16 | silhouette | silhouette | NOUN | NN | pobj | with | 14 |
| 17 | of | of | ADP | IN | prep | silhouette | 16 |
| 18 | a | a | DET | DT | det | man | 19 |
| 19 | man | man | NOUN | NN | pobj | of | 17 |
| 20 | in | in | ADP | IN | prep | man | 19 |
| 21 | a | a | DET | DT | det | hat | 22 |
| 22 | hat | hat | NOUN | NN | pobj | in | 20 |
| 23 | . | . | PUNCT | . | punct | reads | 7 |
| 24 | The | the | DET | DT | det | scene | 25 |
| 25 | scene | scene | NOUN | NN | nsubj | is | 26 |
| 26 | is | be | AUX | VBZ | ROOT | is | 26 |
| 27 | on | on | ADP | IN | prep | is | 26 |
| 28 | a | a | DET | DT | det | sidewalk | 30 |
| 29 | city | city | NOUN | NN | compound | sidewalk | 30 |
| 30 | sidewalk | sidewalk | NOUN | NN | pobj | on | 27 |
| 31 | . | . | PUNCT | . | punct | is | 26 |

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | poster | poster | 1 | noun_chunk_root | high |
| m1 | object | can | can | 6 | noun_chunk_root | high |
| m2 | attribute | black | black | 4 | color_attribute | high |
| m3 | attribute | trash | trash | 5 | compound_modifier | medium |
| m4 | object | BANG | bang | 9 | noun_chunk_root | high |
| m5 | object | KNIGHTHOOD | knighthood | 12 | noun_chunk_root | high |
| m6 | object | silhouette | silhouette | 16 | noun_chunk_root | high |
| m7 | object | man | man | 19 | noun_chunk_root | high |
| m8 | object | hat | hat | 22 | noun_chunk_root | high |
| m9 | object | scene | scene | 25 | noun_chunk_root | high |
| m10 | object | sidewalk | sidewalk | 30 | noun_chunk_root | high |
| m11 | attribute | city | city | 29 | compound_modifier | medium |
| m12 | action | reads | read | 7 | verb_predicate | high |
| m13 | action | GOES | go | 10 | verb_predicate | high |

**Raw Concept Edges**
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> can |
| e1 | has_attribute | m1 | m3 | medium | chunk1 compound -> can |
| e2 | has_attribute | m10 | m11 | medium | chunk8 compound -> sidewalk |
| e3 | agent | m12 | m0 | medium | nsubj -> reads |
| e4 | agent | m13 | m4 | medium | nsubj -> GOES |
| e5 | patient | m13 | m5 | medium | dobj -> GOES |
| e6 | relation | m0 | m1 | high | on |
| e7 | relation | m0 | m6 | high | with |
| e8 | relation | m6 | m7 | medium | of |
| e9 | relation | m7 | m8 | high | in |
| e10 | relation | m9 | m10 | high | on |

### raw_merge_after_parser

**Noun Chunks**
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A poster | poster | poster | nsubj | reads | 0:2 |
| a black trash can | can | can | pobj | on | 3:7 |
| a silhouette | silhouette | silhouette | pobj | with | 10:12 |
| a man | man | man | pobj | of | 13:15 |
| a hat | hat | hat | pobj | in | 16:18 |
| The scene | scene | scene | nsubj | is | 19:21 |
| a city sidewalk | sidewalk | sidewalk | pobj | on | 23:26 |

**Tokens**
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
| 8 | "BANG GOES THE KNIGHTHOOD" | bang_goes_the_knighthood | VERB | VBZ | ccomp | reads | 7 |
| 9 | with | with | ADP | IN | prep | reads | 7 |
| 10 | a | a | DET | DT | det | silhouette | 11 |
| 11 | silhouette | silhouette | NOUN | NN | pobj | with | 9 |
| 12 | of | of | ADP | IN | prep | silhouette | 11 |
| 13 | a | a | DET | DT | det | man | 14 |
| 14 | man | man | NOUN | NN | pobj | of | 12 |
| 15 | in | in | ADP | IN | prep | man | 14 |
| 16 | a | a | DET | DT | det | hat | 17 |
| 17 | hat | hat | NOUN | NN | pobj | in | 15 |
| 18 | . | . | PUNCT | . | punct | reads | 7 |
| 19 | The | the | DET | DT | det | scene | 20 |
| 20 | scene | scene | NOUN | NN | nsubj | is | 21 |
| 21 | is | be | AUX | VBZ | ROOT | is | 21 |
| 22 | on | on | ADP | IN | prep | is | 21 |
| 23 | a | a | DET | DT | det | sidewalk | 25 |
| 24 | city | city | NOUN | NN | compound | sidewalk | 25 |
| 25 | sidewalk | sidewalk | NOUN | NN | pobj | on | 22 |
| 26 | . | . | PUNCT | . | punct | is | 21 |

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | poster | poster | 1 | noun_chunk_root | high |
| m1 | object | can | can | 6 | noun_chunk_root | high |
| m2 | attribute | black | black | 4 | color_attribute | high |
| m3 | attribute | trash | trash | 5 | compound_modifier | medium |
| m4 | object | silhouette | silhouette | 11 | noun_chunk_root | high |
| m5 | object | man | man | 14 | noun_chunk_root | high |
| m6 | object | hat | hat | 17 | noun_chunk_root | high |
| m7 | object | scene | scene | 20 | noun_chunk_root | high |
| m8 | object | sidewalk | sidewalk | 25 | noun_chunk_root | high |
| m9 | attribute | city | city | 24 | compound_modifier | medium |
| m10 | action | reads | read | 7 | verb_predicate | high |
| m11 | action | "BANG GOES THE KNIGHTHOOD" | bang_goes_the_knighthood | 8 | verb_predicate | high |

**Raw Concept Edges**
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> can |
| e1 | has_attribute | m1 | m3 | medium | chunk1 compound -> can |
| e2 | has_attribute | m8 | m9 | medium | chunk6 compound -> sidewalk |
| e3 | agent | m10 | m0 | medium | nsubj -> reads |
| e4 | relation | m0 | m1 | high | on |
| e5 | relation | m0 | m4 | high | with |
| e6 | relation | m4 | m5 | medium | of |
| e7 | relation | m5 | m6 | high | in |
| e8 | relation | m7 | m8 | high | on |

### raw_merge_first

**Noun Chunks**
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A poster | poster | poster | nsubj | reads | 0:2 |
| a black trash can | can | can | pobj | on | 3:7 |
| "BANG GOES THE KNIGHTHOOD" | "BANG GOES THE KNIGHTHOOD" | bang_goes_the_knighthood | dobj | reads | 8:9 |
| a silhouette | silhouette | silhouette | pobj | with | 10:12 |
| a man | man | man | pobj | of | 13:15 |
| a hat | hat | hat | pobj | in | 16:18 |
| The scene | scene | scene | nsubj | is | 19:21 |
| a city sidewalk | sidewalk | sidewalk | pobj | on | 23:26 |

**Tokens**
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
| 8 | "BANG GOES THE KNIGHTHOOD" | bang_goes_the_knighthood | PROPN | NNP | dobj | reads | 7 |
| 9 | with | with | ADP | IN | prep | reads | 7 |
| 10 | a | a | DET | DT | det | silhouette | 11 |
| 11 | silhouette | silhouette | NOUN | NN | pobj | with | 9 |
| 12 | of | of | ADP | IN | prep | silhouette | 11 |
| 13 | a | a | DET | DT | det | man | 14 |
| 14 | man | man | NOUN | NN | pobj | of | 12 |
| 15 | in | in | ADP | IN | prep | man | 14 |
| 16 | a | a | DET | DT | det | hat | 17 |
| 17 | hat | hat | NOUN | NN | pobj | in | 15 |
| 18 | . | . | PUNCT | . | punct | reads | 7 |
| 19 | The | the | DET | DT | det | scene | 20 |
| 20 | scene | scene | NOUN | NN | nsubj | is | 21 |
| 21 | is | be | AUX | VBZ | ROOT | is | 21 |
| 22 | on | on | ADP | IN | prep | is | 21 |
| 23 | a | a | DET | DT | det | sidewalk | 25 |
| 24 | city | city | NOUN | NN | compound | sidewalk | 25 |
| 25 | sidewalk | sidewalk | NOUN | NN | pobj | on | 22 |
| 26 | . | . | PUNCT | . | punct | is | 21 |

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | poster | poster | 1 | noun_chunk_root | high |
| m1 | object | can | can | 6 | noun_chunk_root | high |
| m2 | attribute | black | black | 4 | color_attribute | high |
| m3 | attribute | trash | trash | 5 | compound_modifier | medium |
| m4 | object | "BANG GOES THE KNIGHTHOOD" | bang_goes_the_knighthood | 8 | noun_chunk_root | high |
| m5 | object | silhouette | silhouette | 11 | noun_chunk_root | high |
| m6 | object | man | man | 14 | noun_chunk_root | high |
| m7 | object | hat | hat | 17 | noun_chunk_root | high |
| m8 | object | scene | scene | 20 | noun_chunk_root | high |
| m9 | object | sidewalk | sidewalk | 25 | noun_chunk_root | high |
| m10 | attribute | city | city | 24 | compound_modifier | medium |
| m11 | action | reads | read | 7 | verb_predicate | high |

**Raw Concept Edges**
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> can |
| e1 | has_attribute | m1 | m3 | medium | chunk1 compound -> can |
| e2 | has_attribute | m9 | m10 | medium | chunk7 compound -> sidewalk |
| e3 | agent | m11 | m0 | medium | nsubj -> reads |
| e4 | patient | m11 | m4 | medium | dobj -> reads |
| e5 | relation | m0 | m1 | high | on |
| e6 | relation | m0 | m5 | high | with |
| e7 | relation | m5 | m6 | medium | of |
| e8 | relation | m6 | m7 | high | in |
| e9 | relation | m8 | m9 | high | on |

### raw_merge_before_parser

**Noun Chunks**
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A poster | poster | poster | nsubj | reads | 0:2 |
| a black trash can | can | can | pobj | on | 3:7 |
| in a | a | a | pobj | man | 15:17 |
| . The | The | the | pobj | hat | 18:20 |
| city sidewalk | sidewalk | sidewalk | nsubj | . | 24:26 |

**Tokens**
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
| 8 | "BANG GOES THE KNIGHTHOOD" | bang_goes_the_knighthood | PUNCT | `` | punct | reads | 7 |
| 9 | with | with | ADP | IN | nsubj | a | 10 |
| 10 | a | a | PRON | DT | ccomp | reads | 7 |
| 11 | silhouette | silhouette | NOUN | NN | det | of | 12 |
| 12 | of | of | ADP | IN | dobj | a | 10 |
| 13 | a | a | PRON | DT | punct | a | 10 |
| 14 | man | man | NOUN | NN | prep | reads | 7 |
| 15 | in | in | ADP | IN | det | a | 16 |
| 16 | a | a | PRON | DT | pobj | man | 14 |
| 17 | hat | hat | NOUN | NN | prep | a | 16 |
| 18 | . | . | PUNCT | . | det | The | 19 |
| 19 | The | the | PRON | DT | pobj | hat | 17 |
| 20 | scene | scene | NOUN | NN | prep | The | 19 |
| 21 | is | be | AUX | VBZ | det | on | 22 |
| 22 | on | on | ADP | IN | pobj | scene | 20 |
| 23 | a | a | PRON | DT | punct | reads | 7 |
| 24 | city | city | NOUN | NN | det | sidewalk | 25 |
| 25 | sidewalk | sidewalk | NOUN | NN | nsubj | . | 26 |
| 26 | . | . | PUNCT | . | ROOT | . | 26 |

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | poster | poster | 1 | noun_chunk_root | high |
| m1 | object | can | can | 6 | noun_chunk_root | high |
| m2 | attribute | black | black | 4 | color_attribute | high |
| m3 | attribute | trash | trash | 5 | compound_modifier | medium |
| m4 | object | sidewalk | sidewalk | 25 | noun_chunk_root | high |
| m5 | action | reads | read | 7 | verb_predicate | high |
| m6 | object | scene | scene | 20 | relation_head | medium |

**Raw Concept Edges**
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m1 | m2 | high | chunk1 amod -> can |
| e1 | has_attribute | m1 | m3 | medium | chunk1 compound -> can |
| e2 | agent | m5 | m0 | medium | nsubj -> reads |
| e3 | relation | m0 | m1 | high | on |

## building_with_sign

**raw_caption:**

> A large building with "P.J. HURPHY MOVING & STORAGE" sign stands beside a road, near tall smokestacks and power lines.

**masked_caption_reference:**

> A large building with the quoted text sign stands beside a road, near tall smokestacks and power lines.

### Quote Mentions
| id | text_raw | placeholder | consumed_prefix | raw_span | masked_span |
| --- | --- | --- | --- | --- | --- |
| q0 | P.J. HURPHY MOVING & STORAGE | the quoted text |  | 22:52 | 22:37 |

### raw_no_merge

**Noun Chunks**
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A large building | building | building | nsubj | stands | 0:3 |
| P.J. HURPHY | HURPHY | HURPHY | nsubj | MOVING | 5:7 |
| a road | road | road | pobj | beside | 14:16 |
| tall smokestacks | smokestacks | smokestack | pobj | near | 18:20 |
| power lines | lines | line | conj | smokestacks | 21:23 |

**Tokens**
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | building | 2 |
| 1 | large | large | ADJ | JJ | amod | building | 2 |
| 2 | building | building | NOUN | NN | nsubj | stands | 12 |
| 3 | with | with | ADP | IN | prep | building | 2 |
| 4 | " | " | PUNCT | `` | punct | MOVING | 7 |
| 5 | P.J. | P.J. | PROPN | NNP | nmod | HURPHY | 6 |
| 6 | HURPHY | HURPHY | PROPN | NNP | nsubj | MOVING | 7 |
| 7 | MOVING | MOVING | PROPN | NNP | nmod | sign | 11 |
| 8 | & | & | CCONJ | CC | cc | MOVING | 7 |
| 9 | STORAGE | storage | NOUN | NN | conj | MOVING | 7 |
| 10 | " | " | PUNCT | '' | punct | MOVING | 7 |
| 11 | sign | sign | NOUN | NN | pobj | with | 3 |
| 12 | stands | stand | VERB | VBZ | ROOT | stands | 12 |
| 13 | beside | beside | ADP | IN | prep | stands | 12 |
| 14 | a | a | DET | DT | det | road | 15 |
| 15 | road | road | NOUN | NN | pobj | beside | 13 |
| 16 | , | , | PUNCT | , | punct | stands | 12 |
| 17 | near | near | ADP | IN | prep | stands | 12 |
| 18 | tall | tall | ADJ | JJ | amod | smokestacks | 19 |
| 19 | smokestacks | smokestack | NOUN | NNS | pobj | near | 17 |
| 20 | and | and | CCONJ | CC | cc | smokestacks | 19 |
| 21 | power | power | NOUN | NN | compound | lines | 22 |
| 22 | lines | line | NOUN | NNS | conj | smokestacks | 19 |
| 23 | . | . | PUNCT | . | punct | stands | 12 |

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | 2 | noun_chunk_root | high |
| m1 | attribute | large | large | 1 | size_attribute | high |
| m2 | object | HURPHY | hurphy | 6 | noun_chunk_root | high |
| m3 | object | road | road | 15 | noun_chunk_root | high |
| m4 | object | smokestacks | smokestack | 19 | noun_chunk_root | high |
| m5 | attribute | tall | tall | 18 | size_attribute | high |
| m6 | object | lines | line | 22 | noun_chunk_root | high |
| m7 | attribute | power | power | 21 | compound_modifier | medium |
| m8 | action | stands | stand | 12 | verb_predicate | high |
| m9 | object | sign | sign | 11 | prep_object | medium |

**Raw Concept Edges**
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> building |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> smokestacks |
| e2 | has_attribute | m6 | m7 | medium | chunk4 compound -> lines |
| e3 | agent | m8 | m0 | medium | nsubj -> stands |
| e4 | relation | m0 | m9 | high | with |
| e5 | relation | m0 | m3 | high | beside |
| e6 | relation | m0 | m4 | high | near |
| e7 | relation | m0 | m6 | high | near |

### raw_merge_after_parser

**Noun Chunks**
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A large building | building | building | nsubj | stands | 0:3 |
| "P.J. HURPHY MOVING & STORAGE" sign | sign | sign | pobj | with | 4:6 |
| a road | road | road | pobj | beside | 8:10 |
| tall smokestacks | smokestacks | smokestack | pobj | near | 12:14 |
| power lines | lines | line | conj | smokestacks | 15:17 |

**Tokens**
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
| 15 | power | power | NOUN | NN | compound | lines | 16 |
| 16 | lines | line | NOUN | NNS | conj | smokestacks | 13 |
| 17 | . | . | PUNCT | . | punct | stands | 6 |

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | 2 | noun_chunk_root | high |
| m1 | attribute | large | large | 1 | size_attribute | high |
| m2 | object | sign | sign | 5 | noun_chunk_root | high |
| m3 | object | road | road | 9 | noun_chunk_root | high |
| m4 | object | smokestacks | smokestack | 13 | noun_chunk_root | high |
| m5 | attribute | tall | tall | 12 | size_attribute | high |
| m6 | object | lines | line | 16 | noun_chunk_root | high |
| m7 | attribute | power | power | 15 | compound_modifier | medium |
| m8 | action | stands | stand | 6 | verb_predicate | high |

**Raw Concept Edges**
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> building |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> smokestacks |
| e2 | has_attribute | m6 | m7 | medium | chunk4 compound -> lines |
| e3 | agent | m8 | m0 | medium | nsubj -> stands |
| e4 | relation | m0 | m2 | high | with |
| e5 | relation | m0 | m3 | high | beside |
| e6 | relation | m0 | m4 | high | near |
| e7 | relation | m0 | m6 | high | near |

### raw_merge_first

**Noun Chunks**
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A large building | building | building | nsubj | stands | 0:3 |
| "P.J. HURPHY MOVING & STORAGE" sign | sign | sign | pobj | with | 4:6 |
| a road | road | road | pobj | beside | 8:10 |
| tall smokestacks | smokestacks | smokestack | pobj | near | 12:14 |
| power lines | lines | line | conj | smokestacks | 15:17 |

**Tokens**
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
| 15 | power | power | NOUN | NN | compound | lines | 16 |
| 16 | lines | line | NOUN | NNS | conj | smokestacks | 13 |
| 17 | . | . | PUNCT | . | punct | stands | 6 |

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | 2 | noun_chunk_root | high |
| m1 | attribute | large | large | 1 | size_attribute | high |
| m2 | object | sign | sign | 5 | noun_chunk_root | high |
| m3 | object | road | road | 9 | noun_chunk_root | high |
| m4 | object | smokestacks | smokestack | 13 | noun_chunk_root | high |
| m5 | attribute | tall | tall | 12 | size_attribute | high |
| m6 | object | lines | line | 16 | noun_chunk_root | high |
| m7 | attribute | power | power | 15 | compound_modifier | medium |
| m8 | action | stands | stand | 6 | verb_predicate | high |

**Raw Concept Edges**
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> building |
| e1 | has_attribute | m4 | m5 | high | chunk3 amod -> smokestacks |
| e2 | has_attribute | m6 | m7 | medium | chunk4 compound -> lines |
| e3 | agent | m8 | m0 | medium | nsubj -> stands |
| e4 | relation | m0 | m2 | high | with |
| e5 | relation | m0 | m3 | high | beside |
| e6 | relation | m0 | m4 | high | near |
| e7 | relation | m0 | m6 | high | near |

### raw_merge_before_parser

**Noun Chunks**
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A large building | building | building | nsubj | tall | 0:3 |
| and power | power | power | pobj | smokestacks | 14:16 |

**Tokens**
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | building | 2 |
| 1 | large | large | ADJ | JJ | amod | building | 2 |
| 2 | building | building | NOUN | NN | nsubj | tall | 12 |
| 3 | with | with | ADP | IN | prep | building | 2 |
| 4 | "P.J. HURPHY MOVING & STORAGE" | p.j._hurphy_moving_&_storage | PUNCT | `` | punct | beside | 7 |
| 5 | sign | sign | NOUN | NN | nmod | stands | 6 |
| 6 | stands | stand | VERB | VBZ | nsubj | beside | 7 |
| 7 | beside | beside | ADP | IN | nmod | near | 11 |
| 8 | a | a | PRON | DT | cc | beside | 7 |
| 9 | road | road | NOUN | NN | conj | beside | 7 |
| 10 | , | , | PUNCT | , | punct | beside | 7 |
| 11 | near | near | ADP | IN | pobj | with | 3 |
| 12 | tall | tall | ADJ | JJ | ROOT | tall | 12 |
| 13 | smokestacks | smokestack | NOUN | NNS | prep | tall | 12 |
| 14 | and | and | CCONJ | CC | det | power | 15 |
| 15 | power | power | NOUN | NN | pobj | smokestacks | 13 |
| 16 | lines | line | NOUN | NNS | punct | tall | 12 |
| 17 | . | . | PUNCT | . | prep | tall | 12 |

**Raw Concept Mentions**
| id | type | text | lemma | source_token | role | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| m0 | object | building | building | 2 | noun_chunk_root | high |
| m1 | attribute | large | large | 1 | size_attribute | high |
| m2 | object | power | power | 15 | noun_chunk_root | high |
| m3 | action | stands | stand | 6 | verb_predicate | high |

**Raw Concept Edges**
| id | type | source | target | confidence | evidence |
| --- | --- | --- | --- | --- | --- |
| e0 | has_attribute | m0 | m1 | high | chunk0 amod -> building |
