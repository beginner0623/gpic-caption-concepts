# GPIC Iterative Feedback Plan

이 문서는 GPIC caption을 실제로 돌리면서 parser, coreference, MWE, canonicalization lexicon을 어떻게 쌓아갈지 정리한 운영 계획이다. 현재 단계에서는 10k 확장은 하지 않고, 1k 샘플과 별도 coreference/Maverick 후보 수집을 중심으로 다음 개선 후보를 축적한다.

## 기본 원칙

1. GPIC 결과는 clean rule을 바로 만드는 정답이 아니라 candidate generator로만 쓴다.
2. clean lexicon에 넣는 항목은 source, decision, confidence, reason을 남긴다.
3. 외부 source 기반 후보와 GPIC failure 기반 후보를 분리해서 저장한다.
4. 버전은 freeze한다. 예를 들어 `v1` 결과는 그대로 두고, 새 후보는 `v2_candidate`로 쌓은 뒤 audit 후 승격한다.
5. caption을 100M개 처리해야 하므로, 최종 규칙은 lightweight lookup/rule이어야 한다. Maverick/LLM은 후보 생성이나 audit 단계에만 쓰는 것을 기본으로 한다.

## 반복 루프

```text
GPIC shard 실행
-> failure/candidate 자동 수집
-> source별 candidate TSV 생성
-> rubric 기반 audit
-> clean_core_vN freeze
-> Stage 8/9 재실행
-> before/after regression report
```

실제 처리 산출물은 다음처럼 나눈다.

| artifact | 목적 |
|---|---|
| `reports/feedback_candidates_<sample>.tsv` | GPIC 실행에서 발견한 후보 원천 목록 |
| `reports/feedback_dashboard_<sample>.md` | 사람이 읽는 failure/pattern 요약 |
| `resources/lexicons/*_candidate.tsv` | 승격 전 후보 |
| `resources/lexicons/*_audit_flags.tsv` | reject/maybe와 이유 |
| `resources/lexicons/*_clean_core_vN.tsv` | 실제 parser에 적용하는 frozen whitelist |
| `docs/caption_to_concept_decision_log.md` | 결정과 결과 시계열 기록 |

## 1. Generic Anaphoric Noun 후보

목표는 `the structure`, `the object`, `the individual`, `the device`처럼 앞 entity를 다시 부르는 generic noun을 찾아서, object count 오염과 relation/action target 손실을 줄이는 것이다.

### 수집 신호

| signal | 설명 |
|---|---|
| duplicate generic mention | 같은 caption 안에서 generic noun이 새 object로 생김 |
| generic noun with determiner | `the device`, `this object`, `another player` 같은 NP |
| Stage 9 entity link 없음 | 명백히 앞 entity를 다시 부르는 듯한데 `entity_links`가 비어 있음 |
| skipped self-edge | 잘못 resolve되어 source=target이 된 relation/action |
| group/instance reference | `one`, `another`, `others`, `both`, `each` |

### Maverick 1M 후보 생성 계획

Maverick을 clean rule 자체로 쓰지는 않는다. 1M caption에 대해 coreference 후보를 만들고, 다음 compact 정보만 저장한다.

| column | 내용 |
|---|---|
| `caption_id` | 원 caption id |
| `mention_text` | Maverick mention surface |
| `mention_span` | char/token span |
| `cluster_id` | predicted cluster |
| `antecedent_text` | 같은 cluster의 가장 그럴듯한 선행 mention |
| `antecedent_span` | 선행 mention span |
| `generic_head` | `device/object/structure/...` 같은 head |
| `our_mention_id` | 우리 Stage 8 mention과 span 매칭된 경우 |
| `decision_hint` | candidate only |

후보 승격 기준은 frequency만 보지 않는다.

| criterion | 의미 |
|---|---|
| high recurrence | 여러 shard에서 반복됨 |
| low ambiguity | 같은 generic head가 비슷한 parent로 안정적으로 연결됨 |
| count pollution risk | 새 object로 세면 count를 크게 오염시킴 |
| edge repair gain | self-edge/agent missing/relation missing을 복원할 가능성이 큼 |
| external plausibility | WordNet/OEWN 또는 사람이 정한 ontology에서 generic parent로 설명 가능 |

## 2. MWE 후보

MWE는 object MWE, preposition MWE, phrasal action을 분리해서 관리한다. 같은 surface라도 쓰임이 다르기 때문이다.

### Object MWE

수집 후보:

| signal | 예시 | 처리 방향 |
|---|---|---|
| POS flip | `trash can`, `music stands` | object MWE candidate |
| hyphenated noun | `hot-air balloon`, `close-up` | noun entry 확인 후 merge candidate |
| frequent compound noun | `traffic cone`, `memory module` | 외부 object label과 교차 확인 |
| parser chunk split | noun chunk root가 이상하게 잡힘 | regression candidate |

clean 승격은 GPIC 빈도만으로 하지 않는다. COCO/LVIS/Open Images/VG object labels, WordNet/OEWN noun synset, Wiktionary/Kaikki noun entry 같은 외부 근거를 같이 기록한다.

### Preposition MWE

목표는 `in front of`, `on top of`, `next to`처럼 relation span을 안정적으로 잡는 것이다. 단 `front of`, `side of`, `on the front of`처럼 region 의미가 섞인 표현은 auto canonicalize하지 않는다.

후보 source:

| source | 역할 |
|---|---|
| PDEP / TPP | phrasal preposition surface 후보 |
| SNACS / STREUSLE | semantic subtype 참고 |
| UD fixed/MWE | collapse 가능성 참고 |
| VG/GQA/Open Images relations | visual relation whitelist/frequency 참고 |
| GPIC unknown PP spans | 누락 후보 수집용 |

### Phrasal Action

구동사는 relation collapse가 아니라 action canonicalization에만 쓴다.

```text
pick + up -> action canonical pick_up
stand + on + table -> action stand + relation on
surrounded by -> phrasal action 아님, passive/by frame
filled with -> phrasal action 아님, predicate-specific argument frame
```

외부 seed 후보를 LLM/Codex로 audit할 때 rubric은 고정한다.

Accept only if:

1. visual physical action/state change다.
2. image caption에 나올 가능성이 높다.
3. particle/preposition이 action 의미나 argument 구조를 바꾼다.
4. ordinary spatial relation으로 따로 세는 것보다 action canonical로 묶는 것이 낫다.

Reject if:

1. abstract/cognitive/legal/financial/conversational idiom이다.
2. 단순 verb + ordinary spatial preposition이다.
3. passive/stative construction이다.
4. predicate-specific argument frame이다.
5. visual concept counting에 크게 도움이 되지 않는다.

## 3. Coreference / Reference Scoring 개선 후보

현재 핵심 병목은 resolver를 더 세게 만드는 것이 아니라, 위험한 resolution을 줄이고 복원 가능한 edge만 보수적으로 복원하는 것이다.

수집할 실패 유형:

| type | 예시 | 필요한 정보 |
|---|---|---|
| pronoun wrong target | `it flows`가 water가 아니라 trees로 붙음 | verb compatibility, entity parent |
| body-part vs whole-object | `its head ... it glides` | body_part penalty, animal/person preference |
| self-resolution | source와 target이 같아지는 edge | alternative antecedent ranking |
| both group error | clothing group이 human group보다 선택됨 | action compatibility, human/animal priority |
| one/other split | `one dog`, `others` | group instance split |
| generic duplicate | `The device`가 새 object로 남음 | Maverick/coref candidate |

Score feature 후보:

| feature | 방향 |
|---|---|
| syntactic salience | subject/object entity 우선 |
| recency | 가까운 mention 우선, 단독 사용 금지 |
| parent compatibility | action별 가능한 agent/patient parent 선호 |
| body-part penalty | locomotion/action subject에는 whole object 우선 |
| self-edge guard | source==target이면 reject 또는 alternative search |
| group compatibility | `both/others`는 human/animal group 우선 |
| quote/text carrier | quote 자체는 object가 아니라 attribute/text span 쪽 유지 |

## 4. Stage 9 Canonicalization 후보

현재 Stage 9는 entity/action/attribute canonicalization과 parent chain을 만든다. relation은 당분간 raw 의미를 보존하는 정책이 안전하다.

우선순위:

| bucket | 수집 기준 | 승격 방식 |
|---|---|---|
| object synonym | `cab -> taxi`, `puppy -> dog` | external source + manual/project alias |
| object parent | parent_none high-frequency | WordNet/OEWN, object label ontology, project parent |
| action synonym | `seated -> sit`, `dressed -> wear` | VerbNet/FrameNet/WordNet + conservative alias |
| action parent | action_fallback high-frequency | project action ontology |
| attribute synonym/type | raw_attribute high-frequency | clean visual attribute lexicon만 승격 |
| relation | raw 유지 | 필요할 때만 span/canonical 보강 |

relation은 지금처럼 raw를 그대로 count key로 유지하는 편이 낫다. `with`, `of`, `around`, `over`는 문맥 의존성이 커서 무리하게 parent를 강제하면 count가 더 오염될 수 있다.

## 5. GPIC 실행 중 자동으로 뽑을 feedback 항목

각 shard 실행 뒤 아래 항목을 자동 집계한다.

| feedback item | source |
|---|---|
| top parent_none entities | Stage 9 canonical_entities |
| top action_parent_fallback actions | Stage 9 canonical_events |
| top raw_attribute_role | Stage 9 canonical_facts |
| unknown relation spans | Stage 9 canonical_relations |
| skipped edge reasons | raw skipped_edges |
| self-edge repair candidates | skipped/self relation logs |
| generic anaphoric candidates | reference/generic duplicate detector |
| object MWE candidates | compound/POS flip/hyphen detector |
| preposition MWE candidates | unknown ADP span detector |
| phrasal action candidates | verb+particle detector |
| quote/text carrier anomalies | quote metadata + object pollution check |
| OCR/symbol anomalies | weird token/action/entity frequency |

## 6. 다음 실행 순서

지금 당장 10k를 돌리기보다는 다음 순서가 좋다.

1. 현재 1k plural v1 결과를 기준선으로 고정한다.
2. feedback candidate collector를 만든다.
3. 기존 1k 두 세트와 새 1k 세트에 collector를 적용한다.
4. Maverick은 1M 전체 전에 작은 pilot로 throughput과 output schema를 확정한다.
5. Maverick 1M은 full graph를 저장하지 말고 generic anaphoric/coref candidate만 압축 저장한다.
6. 후보별 audit TSV를 만든 뒤, high-confidence만 clean lexicon v2로 승격한다.
7. 같은 1k 세트에서 before/after regression을 반복한다.

이 방식이면 GPIC를 돌릴수록 rule이 누적되지만, 각 rule이 어디서 왔고 왜 들어갔는지 추적 가능하다.
