# 10k Auto-Frozen V1 Feedback Summary

## Run

- input: `data/gpic_captions_10k_train00000_00099/train/gpic_train_00000_00099_merged_10000.jsonl.gz`
- raw output: `reports/raw_concepts_10k_train00000_00099_trf_auto_frozen_v1.jsonl`
- stage9 output: `reports/canonical_concepts_10k_train00000_00099_trf_auto_frozen_v1.jsonl`
- quality audit: `reports/stage9_quality_audit_10k_train00000_00099_auto_frozen_v1_rerun.md`
- feedback candidates: `reports/feedback_candidates_10k_train00000_00099_auto_frozen_v1_rerun.tsv`
- feedback dashboard: `reports/feedback_dashboard_10k_train00000_00099_auto_frozen_v1_rerun.md`

## What Changed

이번 업데이트는 10k feedback 후보를 사람이 직접 고르는 방식이 아니라, fixed rubric 기준으로 위험이 낮은 항목만 `auto_frozen_v1` lexicon으로 분리해 반영한 첫 번째 update다.

추가된 파일:

```text
resources/lexicons/stage9_object_synonym_auto_frozen_v1.tsv
resources/lexicons/stage9_object_parent_auto_frozen_v1.tsv
resources/lexicons/stage9_action_synonym_auto_frozen_v1.tsv
resources/lexicons/stage9_action_parent_auto_frozen_v1.tsv
resources/lexicons/stage9_attribute_auto_frozen_v1.tsv
resources/lexicons/stage9_attribute_synonym_auto_frozen_v1.tsv
```

Stage 9 loader는 기존 seed/expansion lexicon을 유지한 뒤, 위 auto-frozen lexicon을 추가로 읽는다. 기존 항목을 덮어쓰지 않고 비어 있는 항목만 채우는 방향이다.

Stage 8에는 `’s`, `'s`, `’re`, `'re` 같은 apostrophe 조각이 `VERB`로 잘못 올라오는 경우만 action에서 제외하는 방어 rule을 추가했다. `be`는 아직 막지 않았다.

## Before / After

| metric | auto_feedback_v1 | auto_frozen_v1 rerun | delta |
|---|---:|---:|---:|
| records | 10,000 | 10,000 | 0 |
| entities | 98,291 | 98,291 | 0 |
| events | 35,769 | 35,670 | -99 |
| entity_parent_none | 18,290 | 16,223 | -2,067 |
| action_parent_fallback | 3,176 | 1,872 | -1,304 |
| raw_attribute_role | 23,778 | 17,419 | -6,359 |
| raw_relation | 4,570 | 4,570 | 0 |
| skipped_edges | 412 | 412 | 0 |
| self_relation_after_canonicalization | 10 | 10 | 0 |

해석:

- `entity_parent_none`은 약 11.3% 줄었다.
- `action_parent_fallback`은 약 41.1% 줄었다.
- `raw_attribute_role`은 약 26.7% 줄었다.
- relation은 의도대로 raw-preserving 정책을 유지했으므로 변화가 없다.
- Stage 8 action noise block으로 `’` action 99개가 제거됐다.

## Regression Samples

기존 회귀용 100개 두 세트도 새 코드로 다시 돌렸다.

| dataset | entities | parent_none | events | action_fallback | raw_relation | raw_attribute | self_relation | skipped_edges |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| sample100 val00000 | 724 | 123 | 208 | 12 | 28 | 103 | 0 | 2 |
| alt100 val00001 | 701 | 111 | 200 | 12 | 32 | 112 | 0 | 10 |

두 100세트 모두 `self_relation_after_canonicalization=0`을 유지했다.

## Frozen Items

이번 v1에서 반영한 항목은 다음 범위다.

- object synonym: `individual -> person`, `right_hand/left_hand -> hand`, `streetlight -> streetlamp`
- object parent: body part, surface/furniture, celestial/natural object, visual element, artifact, clothing part, place/context 계열의 고빈도 안전 후보
- action synonym: `bath -> bathe`, `slop -> slope`
- action parent: `filter`, `obscure`, `tilt`, `support`, `tie`, `stack`, `paddle`, `dribble`, `suspend` 등 visual action/state 후보
- attribute type: `grassy`, `paved`, `visible`, `distant`, `ornate`, `blurred`, `arched`, `handwritten`, `black-and-white` 등 시각 속성 후보

이번에 일부러 보류한 항목:

- `be`: copular/state 정책이 필요하므로 보류
- `come`, `let`, `feel`: 의미가 넓어서 action parent로 바로 freeze하지 않음
- `focus`, `meeting`, `set`: entity parent 후보로는 자주 나오지만 count 의미가 불안정해서 보류
- `other`, `more`, `possibly`, `overall`: visual attribute가 아니라 reference/determiner 또는 discourse marker 쪽 문제로 보류

## Next Queue

다음 자동 보완 우선순위:

1. 남은 `entity_parent_none` 상위 후보 v2: `ripple`, `kitchen`, `debris`, `face_mask`, `ink`, `electric_guitar`, `trunk`, `land`, `cone`, `spot`.
2. `be`를 countable action에서 제외할지, stative/copular event로 별도 channel에 둘지 결정.
3. `come`, `let`, `feel` 같은 wide predicate를 action으로 유지할지 exclusion queue로 보낼지 rubric 분리.
4. self-edge repair는 아직 수치가 그대로이므로 별도 analyzer/repair rule이 필요하다.
5. object MWE와 phrasal action은 후보 수집만 된 상태라, 다음 v2에서 별도 automatic audit/freeze가 필요하다.
