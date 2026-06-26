# spaCy POS / Tag / Dependency Label Glossary

Last updated: 2026-06-26 KST

이 문서는 현재 프로젝트에서 쓰는 영어 spaCy 모델(`en_core_web_trf`) 기준으로 `POS`, `tag`, `dep` 라벨 전체를 정리한 glossary다.

라벨 출처:

```text
POS:
  Universal POS coarse labels

tag:
  현재 en_core_web_trf tagger labels
  nlp.get_pipe("tagger").labels

dep:
  현재 en_core_web_trf parser labels
  nlp.get_pipe("parser").labels
```

주의:

- `POS`는 coarse 품사다.
- `tag`는 더 세밀한 영어 Penn Treebank 계열 품사 tag다.
- `dep`는 dependency parser가 token과 head 사이에 붙인 문법 관계 label이다.
- `tag`와 `dep`의 전체 목록은 모델/언어에 따라 달라질 수 있다. 이 문서는 현재 프로젝트의 영어 spaCy 모델 기준이다.

---

## 1. POS Labels

POS는 coarse-grained 품사다. `token.pos_`로 확인한다.

| POS | English meaning | 한국어 의미 | 예시 |
|---|---|---|---|
| `ADJ` | adjective | 형용사 | `red`, `large`, `visible` |
| `ADP` | adposition | 전치사/후치사 계열 | `in`, `on`, `with`, `behind` |
| `ADV` | adverb | 부사 | `quickly`, `nearby`, `above` |
| `AUX` | auxiliary | 조동사/보조동사 | `is`, `are`, `has`, `can` |
| `CCONJ` | coordinating conjunction | 등위접속사 | `and`, `or`, `but` |
| `DET` | determiner | 한정사/관사 | `a`, `the`, `this` |
| `INTJ` | interjection | 감탄사 | `wow`, tag-list에서 오인된 `man` |
| `NOUN` | noun | 일반 명사 | `dog`, `mountains`, `chair` |
| `NUM` | numeral | 수사/숫자 | `two`, `3`, `2024` |
| `PART` | particle | 불변화사/소사 | infinitive `to`, particle |
| `PRON` | pronoun | 대명사 | `he`, `they`, `one`, `others` |
| `PROPN` | proper noun | 고유명사 | `London`, `Nike`, `John` |
| `PUNCT` | punctuation | 문장부호 | `.`, `,`, `:` |
| `SCONJ` | subordinating conjunction | 종속접속사 | `if`, `because`, with-absolute의 `with` 오인 가능 |
| `SYM` | symbol | 기호 | `$`, `%`, mathematical symbols |
| `VERB` | verb | 일반 동사 | `run`, `stand`, `kick` |
| `X` | other | 기타/분류 불가 | foreign/unknown fragments |
| `SPACE` | space | 공백 | whitespace token |

---

## 2. Fine-grained Tag Labels

Fine tag는 영어 모델의 세부 품사 tag다. `token.tag_`로 확인한다.

| tag | English meaning | 한국어 의미 / 해석 |
|---|---|---|
| `$` | symbol, currency | 통화 기호 |
| `''` | closing quotation mark | 닫는 따옴표 |
| `,` | punctuation mark, comma | 쉼표 |
| `-LRB-` | left round bracket | 여는 괄호 |
| `-RRB-` | right round bracket | 닫는 괄호 |
| `.` | punctuation mark, sentence closer | 문장 종료 부호 |
| `:` | punctuation mark, colon or ellipsis | 콜론/말줄임표 |
| `ADD` | email | 이메일/주소류 token |
| `AFX` | affix | 접사 |
| `CC` | conjunction, coordinating | 등위접속사 |
| `CD` | cardinal number | 기수/숫자 |
| `DT` | determiner | 한정사/관사 |
| `EX` | existential there | 존재구문의 `there` |
| `FW` | foreign word | 외국어 단어 |
| `HYPH` | punctuation mark, hyphen | 하이픈 |
| `IN` | conjunction, subordinating or preposition | 전치사 또는 종속접속사 |
| `JJ` | adjective | 형용사 |
| `JJR` | adjective, comparative | 비교급 형용사 |
| `JJS` | adjective, superlative | 최상급 형용사 |
| `LS` | list item marker | 목록 표시 |
| `MD` | verb, modal auxiliary | 조동사 |
| `NFP` | superfluous punctuation | 부가/불필요 문장부호 |
| `NN` | noun, singular or mass | 단수/질량 명사 |
| `NNP` | noun, proper singular | 단수 고유명사 |
| `NNPS` | noun, proper plural | 복수 고유명사 |
| `NNS` | noun, plural | 복수 명사 |
| `PDT` | predeterminer | 전치한정사 |
| `POS` | possessive ending | 소유격 어미, `'s` |
| `PRP` | pronoun, personal | 인칭대명사 |
| `PRP$` | pronoun, possessive | 소유대명사/소유 한정사 |
| `RB` | adverb | 부사 |
| `RBR` | adverb, comparative | 비교급 부사 |
| `RBS` | adverb, superlative | 최상급 부사 |
| `RP` | adverb, particle | particle/부사성 소사 |
| `SYM` | symbol | 기호 |
| `TO` | infinitival "to" | 부정사 `to` |
| `UH` | interjection | 감탄사 |
| `VB` | verb, base form | 동사 원형 |
| `VBD` | verb, past tense | 과거형 동사 |
| `VBG` | verb, gerund or present participle | 동명사/현재분사 |
| `VBN` | verb, past participle | 과거분사 |
| `VBP` | verb, non-3rd person singular present | 현재형 동사, 3인칭 단수 아님 |
| `VBZ` | verb, 3rd person singular present | 현재형 동사, 3인칭 단수 |
| `WDT` | wh-determiner | wh-한정사 |
| `WP` | wh-pronoun, personal | wh-대명사 |
| `WP$` | wh-pronoun, possessive | wh-소유대명사 |
| `WRB` | wh-adverb | wh-부사 |
| `XX` | unknown | 알 수 없는 token |
| <code>``</code> | opening quotation mark | 여는 따옴표 |

Note:

spaCy label은 opening quotation mark를 실제로 backtick 두 개 형태로 출력한다. Markdown 표에서는 깨질 수 있어 위 표에서는 HTML `<code>` 표기를 썼다.

---

## 3. Dependency Labels

Dependency label은 `token.dep_`로 확인한다. token이 head token과 어떤 문법 관계인지 나타낸다.

| dep | English meaning | 한국어 의미 / 해석 |
|---|---|---|
| `ROOT` | root | 문장의 root |
| `acl` | clausal modifier of noun | 명사를 수식하는 절 |
| `acomp` | adjectival complement | 형용사 보어 |
| `advcl` | adverbial clause modifier | 부사절 수식어 |
| `advmod` | adverbial modifier | 부사 수식어 |
| `agent` | agent | 행위자, 주로 passive by-phrase |
| `amod` | adjectival modifier | 형용사 수식어 |
| `appos` | appositional modifier | 동격 수식어 |
| `attr` | attribute | 속성 보어 |
| `aux` | auxiliary | 조동사 |
| `auxpass` | auxiliary (passive) | 수동 조동사 |
| `case` | case marking | 격 표시/전치사성 case |
| `cc` | coordinating conjunction | 등위접속사 |
| `ccomp` | clausal complement | 절 보어 |
| `compound` | compound | 복합명사/compound modifier |
| `conj` | conjunct | 병렬구조의 conjunct |
| `csubj` | clausal subject | 절 주어 |
| `csubjpass` | clausal subject (passive) | 수동 절 주어 |
| `dative` | dative | 여격/간접목적어류 |
| `dep` | unclassified dependent | 분류되지 않은 dependent |
| `det` | determiner | 한정사 |
| `dobj` | direct object | 직접목적어 |
| `expl` | expletive | 허사, expletive |
| `intj` | interjection | 감탄사 |
| `mark` | marker | 종속절 marker |
| `meta` | meta modifier | 메타 수식어 |
| `neg` | negation modifier | 부정 수식어 |
| `nmod` | modifier of nominal | 명사류 수식어 |
| `npadvmod` | noun phrase as adverbial modifier | 부사적으로 쓰인 명사구 |
| `nsubj` | nominal subject | 명사 주어 |
| `nsubjpass` | nominal subject (passive) | 수동 명사 주어 |
| `nummod` | numeric modifier | 숫자 수식어 |
| `oprd` | object predicate | 목적어 서술/목적격 보어 |
| `parataxis` | parataxis | 병렬적 독립절/삽입절 관계 |
| `pcomp` | complement of preposition | 전치사 보어 |
| `pobj` | object of preposition | 전치사의 목적어 |
| `poss` | possession modifier | 소유 수식어 |
| `preconj` | pre-correlative conjunction | 선행 상관접속사 |
| `predet` | predeterminer | 전치한정사 |
| `prep` | prepositional modifier | 전치사 수식어 |
| `prt` | particle | particle |
| `punct` | punctuation | 문장부호 |
| `quantmod` | modifier of quantifier | 수량사 수식어 |
| `relcl` | relative clause modifier | 관계절 수식어 |
| `xcomp` | open clausal complement | open clausal complement, 주어를 공유하는 절 보어 |

Note:

`predet`은 현재 spaCy glossary에서 설명이 비어 있었지만, dependency/parser label로는 존재한다. 의미는 predeterminer, 즉 전치한정사로 정리했다.

---

## 4. 자주 헷갈리는 라벨

| label | 종류 | 헷갈리는 이유 | 해석 |
|---|---|---|---|
| `IN` | tag | 전치사도 되고 종속접속사도 됨 | `with`, `in`, `because` 등이 모두 가능 |
| `ADP` | POS | 전치사 계열 coarse POS | relation cue로 많이 사용 |
| `SCONJ` | POS | 종속접속사 coarse POS | with-absolute에서 `with`가 이렇게 잡힐 수 있음 |
| `prep` | dep | POS가 아니라 dependency label | token이 전치사 modifier로 head에 붙었다는 뜻 |
| `pobj` | dep | 전치사 목적어 | `on table`의 `table` |
| `mark` | dep | 종속절 marker | with-absolute의 `with`가 `mark`로 잡히는 경우가 있음 |
| `nsubj` | dep | 주어 | action agent edge 만들 때 사용 |
| `dobj` / `obj` | dep | 목적어 | action patient edge 만들 때 사용 |
| `amod` | dep | 형용사 수식어 | attribute 후보 |
| `compound` | dep | compound modifier | object가 아니라 attribute/compound modifier 후보 |
| `conj` | dep | 병렬 항목 | object/relation target 확장에 사용 |
| `dep` | dep | 미분류 dependent | 애매한 fallback label |
| `VBN` | tag | 과거분사 | `rusted`, `snow-capped`, `seated` 같은 state attribute 가능 |
| `VBG` | tag | 현재분사/동명사 | `standing`, `walking`, `playing` |
| `NN` / `NNS` | tag | 일반명사 단수/복수 | POS가 흔들릴 때 object fallback으로 사용 |
| `NNP` / `NNPS` | tag | 고유명사 단수/복수 | proper noun object 후보 |
| `UH` | tag | 감탄사 | tag-list 단일 `man`이 이걸로 오인된 적 있음 |

---

## 5. 이 프로젝트에서 특히 중요한 라벨

| 목적 | 주로 보는 라벨 |
|---|---|
| object 후보 | POS `NOUN`, `PROPN`, `PRON`; tag `NN`, `NNS`, `NNP`, `NNPS` |
| action 후보 | POS `VERB` |
| attribute 후보 | POS `ADJ`, `ADV`, `NUM`; dep `amod`, `compound`, `nummod`, `poss`, `acl`; tag `VBG`, `VBN` |
| quantity 후보 | POS `NUM`; dep `nummod`; tag `CD` |
| relation cue | POS `ADP`; dep `prep`; tag `IN` |
| action agent | dep `nsubj`, `nsubjpass` |
| action patient | dep `dobj`, `obj`, `attr`, `oprd`, `pobj` |
| negation | dep `neg` |
| with-absolute cue | text `with`, tag `IN`, dep `mark` |
| with-absolute recovered object | POS `NOUN/PROPN` 또는 tag `NN/NNS/NNP/NNPS`; dep `advcl/conj/dep/nsubj/nsubjpass` |
