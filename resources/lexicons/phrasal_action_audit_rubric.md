# Phrasal Action Audit Rubric

이 파일은 Stage 9 canonicalization에서 사용할 구동사 후보를 고르는 기준이다. GPIC caption을 직접 보고 고르는 것이 아니라, 외부 seed resource의 후보만 대상으로 고정 rubric을 적용한다.

## Accept

`accept/high`는 아래 조건을 모두 만족할 때만 사용한다.

- 시각적으로 관찰 가능한 물리적 action 또는 body pose/action이다.
- image caption에 자연스럽게 나타날 수 있다.
- particle/preposition이 단순 공간관계가 아니라 action 의미 자체를 바꾼다.
- `action + relation`으로 분리하면 핵심 event 의미가 약해진다.
- Stage 9에서 canonical action label로 접어도 relation count를 크게 훼손하지 않는다.

예: `pick up -> pick_up`, `sit down -> sit_down`, `bend over -> bend_over`.

## Reject

아래 조건 중 하나라도 해당하면 parser 적용 core에는 넣지 않는다.

- 추상적, 인지적, 법률/금융/대화 idiom이다.
- `stand on`, `sit in`, `walk through`처럼 action + 일반 spatial relation이다.
- `surrounded by`처럼 passive by-frame이다.
- `filled with`, `covered with`처럼 predicate-specific argument frame이다.
- visual concept counting에 직접 유용하지 않거나 collapse 부작용이 크다.

## Maybe

`look at`, `reach for`, `point at`처럼 visual target은 중요하지만 particle-action collapse가 아니라 `action_target` role이 필요한 경우 `maybe/medium`으로 둔다. 이들은 core whitelist에는 넣지 않는다.
