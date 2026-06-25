# spaCy Parse Inspection

- input: `data\gpic_captions_test\val\gpic_val_00000.jsonl.gz`
- model: `en_core_web_lg`
- max_records: `20`

## 01

**caption_shape:** `sentence-like`

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
| a red bow | bow | bow | conj | person | 5:8 |
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
| 4 | and | and | CCONJ | CC | cc | person | 1 |
| 5 | a | a | DET | DT | det | bow | 7 |
| 6 | red | red | ADJ | JJ | amod | bow | 7 |
| 7 | bow | bow | NOUN | NN | conj | person | 1 |
| 8 | sits | sit | VERB | VBZ | ROOT | sits | 8 |
| 9 | at | at | ADP | IN | prep | sits | 8 |
| 10 | a | a | DET | DT | det | table | 11 |
| 11 | table | table | NOUN | NN | pobj | at | 9 |
| 12 | with | with | ADP | IN | prep | table | 11 |
| 13 | art | art | NOUN | NN | compound | posters | 14 |
| 14 | posters | poster | NOUN | NNS | pobj | with | 12 |
| 15 | and | and | CCONJ | CC | cc | posters | 14 |
| 16 | stickers | sticker | NOUN | NNS | conj | posters | 14 |
| 17 | . | . | PUNCT | . | punct | sits | 8 |

## 02

**caption_shape:** `multi-sentence`

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
| 9 | cracked | crack | VERB | VBN | amod | surface | 13 |
| 10 | , | , | PUNCT | , | punct | surface | 13 |
| 11 | weathered | weather | VERB | VBN | amod | surface | 13 |
| 12 | wooden | wooden | ADJ | JJ | amod | surface | 13 |
| 13 | surface | surface | NOUN | NN | pobj | on | 7 |
| 14 | . | . | PUNCT | . | punct | crawling | 6 |
| 15 | The | the | DET | DT | det | wood | 16 |
| 16 | wood | wood | NOUN | NN | nsubj | shows | 17 |
| 17 | shows | show | VERB | VBZ | ROOT | shows | 17 |
| 18 | signs | sign | NOUN | NNS | dobj | shows | 17 |
| 19 | of | of | ADP | IN | prep | signs | 18 |
| 20 | age | age | NOUN | NN | pobj | of | 19 |
| 21 | with | with | ADP | IN | prep | signs | 18 |
| 22 | visible | visible | ADJ | JJ | amod | splits | 23 |
| 23 | splits | split | NOUN | NNS | pobj | with | 21 |
| 24 | and | and | CCONJ | CC | cc | splits | 23 |
| 25 | small | small | ADJ | JJ | amod | bits | 26 |
| 26 | bits | bit | NOUN | NNS | conj | splits | 23 |
| 27 | of | of | ADP | IN | prep | bits | 26 |
| 28 | debris | debris | NOUN | NN | pobj | of | 27 |
| 29 | scattered | scatter | VERB | VBN | acl | signs | 18 |
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
| 41 | fallen | fall | VERB | VBN | amod | trunk | 43 |
| 42 | tree | tree | NOUN | NN | compound | trunk | 43 |
| 43 | trunk | trunk | NOUN | NN | conj | floor | 39 |
| 44 | . | . | PUNCT | . | punct | appears | 34 |

## 03

**caption_shape:** `multi-sentence`

> A woman stands at a podium speaking in front of an audience. An American flag is behind her, and a screen shows the text "Closing the Access Divide."

### Sentences
| sentence | token_span |
| --- | --- |
| A woman stands at a podium speaking in front of an audience. | 0:13 |
| An American flag is behind her, and a screen shows the text "Closing the Access Divide." | 13:33 |

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
| the text | text | text | dobj | shows | 24:26 |
| the Access Divide | Divide | Divide | dobj | Closing | 28:31 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | woman | 1 |
| 1 | woman | woman | NOUN | NN | nsubj | stands | 2 |
| 2 | stands | stand | VERB | VBZ | ROOT | stands | 2 |
| 3 | at | at | ADP | IN | prep | stands | 2 |
| 4 | a | a | DET | DT | det | podium | 5 |
| 5 | podium | podium | NOUN | NN | pobj | at | 3 |
| 6 | speaking | speak | VERB | VBG | acl | podium | 5 |
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
| 24 | the | the | DET | DT | det | text | 25 |
| 25 | text | text | NOUN | NN | dobj | shows | 23 |
| 26 | " | " | PUNCT | `` | punct | Closing | 27 |
| 27 | Closing | close | VERB | VBG | acl | text | 25 |
| 28 | the | the | DET | DT | det | Divide | 30 |
| 29 | Access | Access | PROPN | NNP | compound | Divide | 30 |
| 30 | Divide | Divide | PROPN | NNP | dobj | Closing | 27 |
| 31 | . | . | PUNCT | . | punct | shows | 23 |
| 32 | " | " | PUNCT | '' | punct | shows | 23 |

## 04

**caption_shape:** `multi-sentence`

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

## 05

**caption_shape:** `multi-sentence`

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
| 0 | Bright | bright | ADJ | JJ | amod | flowers | 3 |
| 1 | orange | orange | ADJ | JJ | amod | glass | 2 |
| 2 | glass | glass | NOUN | NN | compound | flowers | 3 |
| 3 | flowers | flower | NOUN | NNS | nsubj | stand | 4 |
| 4 | stand | stand | VERB | VBP | ROOT | stand | 4 |
| 5 | in | in | ADP | IN | prep | stand | 4 |
| 6 | a | a | DET | DT | det | bed | 8 |
| 7 | garden | garden | NOUN | NN | compound | bed | 8 |
| 8 | bed | bed | NOUN | NN | pobj | in | 5 |
| 9 | with | with | ADP | IN | prep | stand | 4 |
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
| 38 | beyond | beyond | ADP | IN | prep | visible | 37 |
| 39 | the | the | DET | DT | det | area | 41 |
| 40 | garden | garden | NOUN | NN | compound | area | 41 |
| 41 | area | area | NOUN | NN | pobj | beyond | 38 |
| 42 | . | . | PUNCT | . | punct | are | 36 |

## 06

**caption_shape:** `tag-list-like`

> smiling couple, formal party, british flags, chandelier, wine glasses

### Sentences
| sentence | token_span |
| --- | --- |
| smiling couple, formal party, british flags, chandelier, wine glasses | 0:13 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| smiling couple | couple | couple | ROOT | couple | 0:2 |
| formal party | party | party | conj | couple | 3:5 |
| british flags | flags | flag | conj | party | 6:8 |
| chandelier | chandelier | chandelier | conj | flags | 9:10 |
| wine glasses | glasses | glass | appos | couple | 11:13 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | smiling | smile | VERB | VBG | amod | couple | 1 |
| 1 | couple | couple | NOUN | NN | ROOT | couple | 1 |
| 2 | , | , | PUNCT | , | punct | couple | 1 |
| 3 | formal | formal | ADJ | JJ | amod | party | 4 |
| 4 | party | party | NOUN | NN | conj | couple | 1 |
| 5 | , | , | PUNCT | , | punct | party | 4 |
| 6 | british | british | ADJ | JJ | amod | flags | 7 |
| 7 | flags | flag | NOUN | NNS | conj | party | 4 |
| 8 | , | , | PUNCT | , | punct | flags | 7 |
| 9 | chandelier | chandelier | NOUN | NN | conj | flags | 7 |
| 10 | , | , | PUNCT | , | punct | flags | 7 |
| 11 | wine | wine | NOUN | NN | compound | glasses | 12 |
| 12 | glasses | glass | NOUN | NNS | appos | couple | 1 |

## 07

**caption_shape:** `sentence-like`

> A white church with a cross on top has stone steps leading to a wooden door.

### Sentences
| sentence | token_span |
| --- | --- |
| A white church with a cross on top has stone steps leading to a wooden door. | 0:17 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A white church | church | church | nsubj | has | 0:3 |
| a cross | cross | cross | pobj | with | 4:6 |
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
| 5 | cross | cross | NOUN | NN | pobj | with | 3 |
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

## 08

**caption_shape:** `multi-sentence`

> A poster on a black trash can reads "BANG GOES THE KNIGHTHOOD" with a silhouette of a man in a hat. The scene is on a city sidewalk.

### Sentences
| sentence | token_span |
| --- | --- |
| A poster on a black trash can reads "BANG GOES THE KNIGHTHOOD" with a silhouette of a man in a hat. | 0:24 |
| The scene is on a city sidewalk. | 24:32 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| A poster | poster | poster | nsubj | reads | 0:2 |
| a black trash | trash | trash | pobj | on | 3:6 |
| BANG | BANG | bang | nsubj | GOES | 9:10 |
| THE KNIGHTHOOD | KNIGHTHOOD | KNIGHTHOOD | dobj | GOES | 11:13 |
| a silhouette | silhouette | silhouette | pobj | with | 15:17 |
| a man | man | man | pobj | of | 18:20 |
| a hat | hat | hat | pobj | in | 21:23 |
| The scene | scene | scene | nsubj | is | 24:26 |
| a city sidewalk | sidewalk | sidewalk | pobj | on | 28:31 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | A | a | DET | DT | det | poster | 1 |
| 1 | poster | poster | NOUN | NN | nsubj | reads | 7 |
| 2 | on | on | ADP | IN | prep | poster | 1 |
| 3 | a | a | DET | DT | det | trash | 5 |
| 4 | black | black | ADJ | JJ | amod | trash | 5 |
| 5 | trash | trash | NOUN | NN | pobj | on | 2 |
| 6 | can | can | AUX | MD | aux | reads | 7 |
| 7 | reads | read | VERB | VBZ | ROOT | reads | 7 |
| 8 | " | " | PUNCT | `` | punct | reads | 7 |
| 9 | BANG | bang | NOUN | NN | nsubj | GOES | 10 |
| 10 | GOES | go | VERB | VBZ | ccomp | reads | 7 |
| 11 | THE | the | DET | DT | det | KNIGHTHOOD | 12 |
| 12 | KNIGHTHOOD | KNIGHTHOOD | PROPN | NNP | dobj | GOES | 10 |
| 13 | " | " | PUNCT | '' | punct | KNIGHTHOOD | 12 |
| 14 | with | with | ADP | IN | prep | GOES | 10 |
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

## 09

**caption_shape:** `multi-sentence`

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
| 6 | smiles | smile | NOUN | NNS | ROOT | smiles | 6 |
| 7 | widely | widely | ADV | RB | advmod | smiles | 6 |
| 8 | while | while | SCONJ | IN | mark | wearing | 9 |
| 9 | wearing | wear | VERB | VBG | advcl | smiles | 6 |
| 10 | a | a | DET | DT | det | hat | 15 |
| 11 | blue | blue | ADJ | JJ | amod | hat | 15 |
| 12 | and | and | CCONJ | CC | cc | blue | 11 |
| 13 | white | white | ADJ | JJ | conj | blue | 11 |
| 14 | striped | striped | ADJ | JJ | conj | blue | 11 |
| 15 | hat | hat | NOUN | NN | dobj | wearing | 9 |
| 16 | . | . | PUNCT | . | punct | smiles | 6 |
| 17 | The | the | DET | DT | det | child | 18 |
| 18 | child | child | NOUN | NN | nsubj | is | 19 |
| 19 | is | be | AUX | VBZ | ROOT | is | 19 |
| 20 | bare | bare | ADJ | JJ | advmod | shouldered | 22 |
| 21 | - | - | PUNCT | HYPH | punct | shouldered | 22 |
| 22 | shouldered | shouldered | ADJ | JJ | acomp | is | 19 |
| 23 | and | and | CCONJ | CC | cc | is | 19 |
| 24 | appears | appear | VERB | VBZ | conj | is | 19 |
| 25 | indoors | indoors | ADV | RB | dobj | appears | 24 |
| 26 | , | , | PUNCT | , | punct | appears | 24 |
| 27 | with | with | ADP | IN | prep | appears | 24 |
| 28 | a | a | DET | DT | det | window | 29 |
| 29 | window | window | NOUN | NN | pobj | with | 27 |
| 30 | visible | visible | ADJ | JJ | amod | window | 29 |
| 31 | in | in | ADP | IN | prep | visible | 30 |
| 32 | the | the | DET | DT | det | background | 33 |
| 33 | background | background | NOUN | NN | pobj | in | 31 |
| 34 | . | . | PUNCT | . | punct | is | 19 |

## 10

**caption_shape:** `tag-list-like`

> roller skaters, helmet, referee, court, blue jersey

### Sentences
| sentence | token_span |
| --- | --- |
| roller skaters, helmet, referee, court, blue jersey | 0:11 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| roller skaters | skaters | skater | ROOT | skaters | 0:2 |
| helmet | helmet | helmet | conj | skaters | 3:4 |
| referee | referee | referee | conj | helmet | 5:6 |
| court | court | court | conj | referee | 7:8 |
| blue jersey | jersey | jersey | appos | skaters | 9:11 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | roller | roller | NOUN | NN | compound | skaters | 1 |
| 1 | skaters | skater | NOUN | NNS | ROOT | skaters | 1 |
| 2 | , | , | PUNCT | , | punct | skaters | 1 |
| 3 | helmet | helmet | NOUN | NN | conj | skaters | 1 |
| 4 | , | , | PUNCT | , | punct | helmet | 3 |
| 5 | referee | referee | NOUN | NN | conj | helmet | 3 |
| 6 | , | , | PUNCT | , | punct | referee | 5 |
| 7 | court | court | NOUN | NN | conj | referee | 5 |
| 8 | , | , | PUNCT | , | punct | court | 7 |
| 9 | blue | blue | PROPN | NNP | compound | jersey | 10 |
| 10 | jersey | jersey | PROPN | NNP | appos | skaters | 1 |

## 11

**caption_shape:** `multi-sentence`

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
| 14 | cobblestone | cobblestone | ADJ | JJ | amod | street | 15 |
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
| 30 | further | far | ADV | RB | advmod | down | 31 |
| 31 | down | down | ADP | IN | prep | is | 28 |
| 32 | the | the | DET | DT | det | road | 33 |
| 33 | road | road | NOUN | NN | pobj | down | 31 |
| 34 | under | under | ADP | IN | prep | is | 28 |
| 35 | a | a | DET | DT | det | sky | 38 |
| 36 | partly | partly | ADV | RB | advmod | cloudy | 37 |
| 37 | cloudy | cloudy | ADJ | JJ | amod | sky | 38 |
| 38 | sky | sky | NOUN | NN | pobj | under | 34 |
| 39 | . | . | PUNCT | . | punct | is | 28 |

## 12

**caption_shape:** `multi-sentence`

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
| 9 | above | above | ADP | IN | prep | basketball | 8 |
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

## 13

**caption_shape:** `multi-sentence`

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
| 5 | under | under | ADP | IN | prep | landscape | 2 |
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

## 14

**caption_shape:** `tag-list-like`

> brown boot, indoor, brick wall, display, large

### Sentences
| sentence | token_span |
| --- | --- |
| brown boot, indoor, brick wall, display, large | 0:11 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| brown boot, indoor, brick wall | wall | wall | ROOT | wall | 0:7 |
| display | display | display | appos | wall | 8:9 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | brown | brown | PROPN | NNP | compound | boot | 1 |
| 1 | boot | boot | PROPN | NNP | nmod | wall | 6 |
| 2 | , | , | PUNCT | , | punct | boot | 1 |
| 3 | indoor | indoor | ADJ | JJ | amod | boot | 1 |
| 4 | , | , | PUNCT | , | punct | indoor | 3 |
| 5 | brick | brick | NOUN | NN | compound | wall | 6 |
| 6 | wall | wall | NOUN | NN | ROOT | wall | 6 |
| 7 | , | , | PUNCT | , | punct | wall | 6 |
| 8 | display | display | NOUN | NN | appos | wall | 6 |
| 9 | , | , | PUNCT | , | punct | wall | 6 |
| 10 | large | large | ADJ | JJ | amod | wall | 6 |

## 15

**caption_shape:** `multi-sentence`

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
| the other a yellow shirt | shirt | shirt | dobj | wears | 18:23 |

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
| 11 | wears | wear | VERB | VBZ | ROOT | wears | 11 |
| 12 | a | a | DET | DT | det | vest | 13 |
| 13 | vest | vest | NOUN | NN | dobj | wears | 11 |
| 14 | and | and | CCONJ | CC | cc | vest | 13 |
| 15 | red | red | ADJ | JJ | amod | scarf | 16 |
| 16 | scarf | scarf | NOUN | NN | conj | vest | 13 |
| 17 | , | , | PUNCT | , | punct | wears | 11 |
| 18 | the | the | DET | DT | det | shirt | 22 |
| 19 | other | other | ADJ | JJ | amod | shirt | 22 |
| 20 | a | a | DET | DT | det | shirt | 22 |
| 21 | yellow | yellow | ADJ | JJ | amod | shirt | 22 |
| 22 | shirt | shirt | NOUN | NN | dobj | wears | 11 |
| 23 | . | . | PUNCT | . | punct | wears | 11 |

## 16

**caption_shape:** `multi-sentence`

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
| music | music | music | pobj | with | 24:25 |
| The setting | setting | setting | nsubj | is | 28:30 |
| indoors | indoors | indoor | attr | is | 31:32 |
| red curtains | curtains | curtain | pobj | with | 34:36 |
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
| 22 | seated | seat | VERB | VBN | advcl | stands | 25 |
| 23 | with | with | ADP | IN | prep | seated | 22 |
| 24 | music | music | NOUN | NN | pobj | with | 23 |
| 25 | stands | stand | VERB | VBZ | advcl | holds | 15 |
| 26 | nearby | nearby | ADV | RB | advmod | stands | 25 |
| 27 | . | . | PUNCT | . | punct | holds | 15 |
| 28 | The | the | DET | DT | det | setting | 29 |
| 29 | setting | setting | NOUN | NN | nsubj | is | 30 |
| 30 | is | be | AUX | VBZ | ROOT | is | 30 |
| 31 | indoors | indoor | NOUN | NNS | attr | is | 30 |
| 32 | , | , | PUNCT | , | punct | is | 30 |
| 33 | with | with | ADP | IN | prep | is | 30 |
| 34 | red | red | ADJ | JJ | amod | curtains | 35 |
| 35 | curtains | curtain | NOUN | NNS | pobj | with | 33 |
| 36 | and | and | CCONJ | CC | cc | curtains | 35 |
| 37 | blue | blue | ADJ | JJ | amod | chairs | 38 |
| 38 | chairs | chair | NOUN | NNS | conj | curtains | 35 |
| 39 | visible | visible | ADJ | JJ | amod | chairs | 38 |
| 40 | in | in | ADP | IN | prep | visible | 39 |
| 41 | the | the | DET | DT | det | background | 42 |
| 42 | background | background | NOUN | NN | pobj | in | 40 |
| 43 | . | . | PUNCT | . | punct | is | 30 |

## 17

**caption_shape:** `tag-list-like`

> glass wall, worker, sidewalk, building, reflection, grass

### Sentences
| sentence | token_span |
| --- | --- |
| glass wall, worker, sidewalk, building, reflection, grass | 0:12 |

### Noun Chunks
| chunk | root | root_lemma | root_dep | root_head | token_span |
| --- | --- | --- | --- | --- | --- |
| glass wall | wall | wall | ROOT | wall | 0:2 |
| grass | grass | grass | appos | wall | 11:12 |

### Tokens / POS / Lemma / Dependency
| i | text | lemma | pos | tag | dep | head | head_i |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | glass | glass | NOUN | NN | compound | wall | 1 |
| 1 | wall | wall | NOUN | NN | ROOT | wall | 1 |
| 2 | , | , | PUNCT | , | punct | wall | 1 |
| 3 | worker | worker | NOUN | NN | npadvmod | wall | 1 |
| 4 | , | , | PUNCT | , | punct | worker | 3 |
| 5 | sidewalk | sidewalk | NOUN | NN | conj | worker | 3 |
| 6 | , | , | PUNCT | , | punct | sidewalk | 5 |
| 7 | building | building | NOUN | NN | conj | sidewalk | 5 |
| 8 | , | , | PUNCT | , | punct | building | 7 |
| 9 | reflection | reflection | NOUN | NN | conj | building | 7 |
| 10 | , | , | PUNCT | , | punct | reflection | 9 |
| 11 | grass | grass | NOUN | NN | appos | wall | 1 |

## 18

**caption_shape:** `multi-sentence`

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
| 20 | with | with | ADP | IN | prep | stretch | 16 |
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
| 33 | orange | orange | ADJ | JJ | dep | soft | 32 |
| 34 | and | and | CCONJ | CC | cc | orange | 33 |
| 35 | gray | gray | ADJ | JJ | conj | orange | 33 |
| 36 | hues | hue | NOUN | NNS | dobj | shows | 31 |
| 37 | near | near | ADP | IN | prep | hues | 36 |
| 38 | the | the | DET | DT | det | horizon | 39 |
| 39 | horizon | horizon | NOUN | NN | pobj | near | 37 |
| 40 | . | . | PUNCT | . | punct | shows | 31 |

## 19

**caption_shape:** `multi-sentence`

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
| 41 | in | in | ADP | IN | prep | visible | 40 |
| 42 | the | the | DET | DT | det | background | 43 |
| 43 | background | background | NOUN | NN | pobj | in | 41 |
| 44 | . | . | PUNCT | . | punct | are | 39 |

## 20

**caption_shape:** `sentence-like`

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
