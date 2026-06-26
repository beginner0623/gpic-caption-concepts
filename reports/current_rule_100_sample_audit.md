# Current Rule 100 Sample Audit

생성일: 2026-06-26 KST

현재 rule 기준으로 GPIC val 첫 100개 caption을 다시 처리한 결과다. 이 문서는 지금까지 적용한 예외처리들이 실제 raw concept 출력에서 어떤 효과를 냈는지 확인하기 위한 감사 로그다.

## 실행 설정

```text
input: data\gpic_captions_eval\val\gpic_val_00000.jsonl.gz
model: en_core_web_trf
max_records: 100
mask_quotes: true
quote_handling: raw_quote_retokenize
parse_tag_lists: true
merge_object_mwes: true
merge_hyphen_spans: true
object_mwe_lexicon: resources\lexicons\object_noun_mwe_clean_core.tsv
```

재생성한 파일:

```text
reports/raw_concepts_sample_100_trf_current.jsonl
reports/raw_concepts_sample_100_trf_current_summary.md
reports/case_detail_sample_100_trf_current.md
reports/nominal_reference_resolution_sample_100_trf_current.jsonl
reports/nominal_reference_resolution_sample_100_trf_current.md
```

## 전체 분포

| 항목 | count |
|---|---:|
| total records | 100 |
| sentence branch | 79 |
| tag-list branch | 21 |
| multi-sentence caption | 57 |
| sentence-like caption | 22 |
| tag-list-like caption | 21 |

## Concept Mention Count

| concept type | count |
|---|---:|
| object | 693 |
| attribute | 417 |
| action | 208 |
| context | 49 |
| quantity | 30 |

## Edge Count

| edge type | count |
|---|---:|
| has_attribute | 398 |
| relation | 320 |
| agent | 213 |
| patient | 80 |
| has_context | 38 |
| has_quantity | 28 |
| candidate_has_attribute | 7 |
| scene_contains | 5 |

## Skipped Edge Count

| reason | count |
|---|---:|
| self_edge_after_coref | 4 |

## 오염 검사

| 검사 항목 | 결과 |
|---|---:|
| pronoun/reference surface가 object로 들어간 개수 | 0 |
| possessive pronoun이 attribute로 들어간 개수 | 0 |
| color word가 object로 들어간 개수 | 0 |
| quote span이 object로 들어간 개수 | 0 |
| quote metadata 개수 | 13 |
| quote_text attribute 개수 | 13 |

검사 대상 예시:

```text
pronoun/reference: he, him, she, her, it, they, them, that, which, who, one, other, both, each
possessive pronoun: my, your, his, her, its, our, their, whose
color word: black, white, red, blue, green, yellow, orange, purple, pink, brown, gray, grey, ...
quote span: "..." 또는 “...”
```

## 색상 Object 예외처리 결과

이번 수정의 핵심은 "관사 + 색상"을 object로 보라는 것이 아니다. 색상 단어가 object로 잘못 올라오는 경우를 막고, 가능한 경우 attribute로 남기는 것이다.

| case | 이전 문제 | 현재 처리 |
|---:|---|---|
| 54 | `black`, `white`가 tag-list segment object 후보로 올라올 수 있음 | `black`, `white`를 `color_attribute`로 유지하고 object에서는 제외 |
| 61 | `blue`, `orange`가 noun chunk root object로 올라옴 | `blue`, `orange`를 `color_attribute`로 유지하고 `sky`, `horizon` 같은 실제 명사 object는 유지 |
| 83 | `black`, `white`가 noun chunk root object로 올라옴 | 색상은 attribute로 유지하고 object에서는 제외 |

주의할 점:

```text
orange처럼 색상 단어이면서 실제 물체명일 수 있는 단어는 지금 정책에서 object로 막힌다.
이 경우는 나중에 object lexicon 기반 예외로 따로 복구하는 편이 안전하다.
```

## Quote Object 예외처리 결과

quote 처리의 현재 정책은 다음과 같다.

```text
1. 원문 quote span 자체는 tokenizer 직후 Retokenizer로 merge한다.
2. quote span은 object 후보에서 제외한다.
3. quote span은 attribute/quote_text mention으로 반드시 1회 보존한다.
4. parser가 action patient나 object modifier로 안정적으로 연결한 경우 해당 edge는 유지한다.
5. quote token의 syntactic head가 이미 object이면 `object --has_attribute--> quote_text` carrier edge를 추가한다.
```

100개 샘플 기준 quote metadata는 13개였고, 이 13개가 모두 `attribute` / `quote_text`로 들어갔다.
반대로 quote span이 `object`로 들어간 경우는 0개다.

대표 결과:

| case | quote | 현재 처리 |
|---:|---|---|
| 08 | `"BANG GOES THE KNIGHTHOOD"` | `attribute(quote_text)`, `patient(reads, quote_text)` |
| 25 | `"ROYAL CANIN"` | `attribute(quote_text)`, `banner --has_attribute--> quote_text` |
| 32 | `"BORDERLINE BIENNALE ..."` | `attribute(quote_text)`, `patient(reads, quote_text)` |
| 51 | `"MILE 0 VICTORIA BC"` | `attribute(quote_text)`, `patient(reads, quote_text)` |
| 90 | `"1709-1"` | `attribute(quote_text)`, `number --has_attribute--> quote_text` |

주의할 점:

```text
case 90처럼 quote가 `appos -> number`로 붙는 경우에는 Stage 8에서 carrier edge까지 복원된다.
다만 더 복잡한 text-bearing structure는 Stage 9에서 추가 보강할 수 있다.
```

## Relation Evidence Top

| relation evidence | count |
|---|---:|
| with | 84 |
| in | 67 |
| on | 41 |
| of | 15 |
| near | 15 |
| under | 14 |
| at | 10 |
| behind | 8 |
| by | 8 |
| beside | 6 |
| to | 5 |
| across | 5 |

## Pronoun / Reference Regression Check

### Personal Pronoun Rewiring

| case | 기대 | 현재 결과 |
|---:|---|---|
| 35 | `He has...`에서 `He -> man` | `agent(has, man)` |
| 41 | `He stands...`에서 `He -> man` | `agent(stands, man)` |
| 41 | `behind him`에서 `him -> man` | `relation(curtains, behind, man)` |

### Pronoun Object Relation Rewiring

| case | 기대 | 현재 결과 |
|---:|---|---|
| 03 | `behind her`에서 `her -> woman` | `relation(American flag, behind, woman)` |
| 28 | `behind them`에서 `them -> person` | `relation(lights, behind, person)` |

### Relative Pronoun Rewiring

| case | 기대 | 현재 결과 |
|---:|---|---|
| 51 | `that reads...`에서 `that -> sign` | `agent(reads, sign)` |
| 51 | quote text patient 유지 | `patient(reads, "MILE 0 VICTORIA BC")` |

## Non-finite / Subject-ellipsis Action Agent 복원

이전 rule은 action token의 직접 child에 `nsubj` / `nsubjpass`가 있을 때만 agent를 만들었다.
그 결과 `speaking`, `watching`, `holding`, `wearing`, `to kick` 같은 non-finite verb나 subject-ellipsis coordination에서 agent가 빠지는 경우가 많았다.

현재 추가한 일반 rule:

```text
1. acl / relcl action은 head noun을 inherited agent 후보로 사용
2. advcl / xcomp / ccomp / conj / acomp action은 parent verb의 subject를 상속
3. parent verb도 subject가 없으면 재귀적으로 상위 action에서 subject를 찾음
4. including처럼 prep으로 붙는 일부 verbal relation은 head noun을 inherited agent 후보로 사용
5. nominal/anaphoric reference로 막힌 subject는 raw에서 억지로 복원하지 않음
```

100개 샘플 기준 결과:

| 항목 | count |
|---|---:|
| inherited agent edge 추가 | 61 |
| action 중 agent 없는 항목 | 4 |

대표 복원:

| case | 복원 |
|---:|---|
| 03 | `agent(speaking, woman)` |
| 25 | `agent(watching, man)` |
| 30 | `agent(sharing, man)`, `agent(sharing, woman)` |
| 41 | `agent(singing, man)` |
| 43 | `agent(preparing, soccer player)`, `agent(kick, soccer player)` |
| 44 | `agent(positioned, hockey player)`, `agent(looking, hockey player)` |
| 48 | `agent(holding, man)`, `agent(smiling, woman)` |

남은 4개:

| case | action | 이유 |
|---:|---|---|
| 15 | `wears` | subject가 `One`이라 nominal reference sidecar 단계에서 처리 |
| 62 | `look` | subject가 `Both`라 group reference sidecar 단계에서 처리 |
| 63 | `controlling` | subject가 `One` 계열 구조라 sidecar 필요 |
| 63 | `lying` | antecedent가 `other`라 raw 단계에서 자동 collapse 보류 |

## Self-edge / Self-resolution 방어

이번 rule은 두 가지를 좁게 적용한다.

```text
1. relation edge에서 source == target이면 drop
2. non-reflexive pronoun이 action patient로 resolve됐는데 target이 같은 action의 agent이면 reject
3. locomotion/posture action의 subject pronoun은 body part antecedent를 강하게 감점
```

현재 100개 샘플 기준 결과:

| 항목 | count |
|---|---:|
| 남은 self-edge | 0 |
| drop된 self relation | 4 |
| pronoun self-resolution patient reject | 0 |

대표 수정:

| case | 이전 문제 | 현재 결과 |
|---:|---|---|
| 22 | `agent(glides, head)` | `agent(glides, duck)` |
| 32 | `patient(surrounding, light)` self-like resolution | `patient(surrounding, eye)` |
| 39 | `relation(spoon, beside, spoon)` | drop, `self_edge_after_coref` |
| 44 | `relation(hockey player, in_front_of, hockey player)` | drop, `self_edge_after_coref` |
| 47 | `relation(person, in_front_of, person)` | drop, `self_edge_after_coref` |
| 98 | `relation(woman, beside, woman)` | drop, `self_edge_after_coref` |

### Nominal / Anaphoric Reference는 Raw Rewiring 제외

| case | reference | 현재 정책 | 현재 결과 |
|---:|---|---|---|
| 62 | `Both` | raw edge 자동 rewiring 금지 | sidecar에서 `manual_review_ambiguous_reference` |
| 98 | `each` | raw edge 자동 rewiring 금지 | sidecar에서 `link_distributive_reference` |
| 15 | `One`, `other` | raw object 제외, sidecar link | sidecar에서 `link_singular_reference`, `link_contrastive_reference` |
| 40 | `a red one` | modifier 있는 substitute만 type copy 후보 | sidecar에서 `copy_antecedent_type_apply_modifiers` |

## Nominal Reference Sidecar

| 항목 | count |
|---|---:|
| references_seen | 9 |
| resolved | 8 |
| ambiguous | 1 |
| unresolved | 0 |

| recommendation | count |
|---|---:|
| link_singular_reference | 3 |
| link_contrastive_reference | 3 |
| copy_antecedent_type_apply_modifiers | 1 |
| manual_review_ambiguous_reference | 1 |
| link_distributive_reference | 1 |

## Nominal Reference Rows

| case | reference | class | antecedent | status | recommendation |
|---:|---|---|---|---|---|
| 15 | One | singular_substitute | Two men | resolved | link_singular_reference |
| 15 | other | contrastive_reference | Two men | resolved | link_contrastive_reference |
| 16 | others | contrastive_reference | Children | resolved | link_contrastive_reference |
| 40 | one | singular_substitute | Several cars | resolved | copy_antecedent_type_apply_modifiers |
| 62 | Both | group_reference | A man and a woman | ambiguous | manual_review_ambiguous_reference |
| 63 | One | singular_substitute | Two men | resolved | link_singular_reference |
| 63 | other | contrastive_reference | Two men | resolved | link_contrastive_reference |
| 89 | one | singular_substitute | Two men | resolved | link_singular_reference |
| 98 | each | distributive_reference | Four people | resolved | link_distributive_reference |

## 현재 판정

현재 rule은 다음 조건을 만족한다.

```text
1. pronoun/reference surface object 오염 없음
2. possessive pronoun attribute 오염 없음
3. color word object 오염 없음
4. quote span object 오염 없음
5. quote span은 quote_text attribute로 전부 보존
6. non-finite / subject-ellipsis action agent 대부분 복원
7. personal pronoun edge를 antecedent object로 복원
8. clean relative pronoun edge를 dependency 기반으로 복원
9. nominal/anaphoric reference는 raw edge 자동 collapse를 피하고 sidecar로 관리
```

남은 주의점:

```text
1. nominal/anaphoric reference의 실제 Stage 9 적용은 아직 별도 구현 필요
2. nominal adjective를 전용으로 처리하는 resolver는 아직 없음
3. person/gender/number 기반 pronoun rewiring은 lightweight rule이므로 fastcoref audit과 비교 검증 필요
4. color/object 다의어, 예: orange fruit,은 object lexicon 기반 예외 복구가 필요
5. 복잡한 quote/text-bearing structure는 Stage 9에서 추가 보강 가능
6. relation evidence에는 일부 resolved target이 표시되지 않는 경우가 있어 audit 표기 개선 가능
```
