# Model Success Rate Summary

- input: `data\gpic_captions_test\val\gpic_val_00000.jsonl.gz`
- sample size: 20 captions
- models: `en_core_web_sm`, `en_core_web_lg`, `en_core_web_trf`
- enabled branches: quote masking, tag-list branch
- 기준일: 2026-06-25

## Success Criteria

성공률을 두 가지로 나눈다.

| metric | 의미 |
|---|---|
| strict success | 바로 downstream extraction에 넣어도 큰 보정이 필요 없고, tag-list에서도 medium/candidate ambiguity가 없는 경우 |
| usable success | 남은 ambiguity가 confidence/candidate로 명시되어 있고, 기존처럼 global dependency parse가 깨지는 실패는 피한 경우 |

즉 tag-list caption에서 `large` 같은 floating attribute는 strict success에서는 partial로 보지만, usable success에서는 schema로 안전하게 보존되므로 성공으로 본다.

## Overall Success Rate

| model | strict success | usable success | partial | fail |
|---|---:|---:|---:|---:|
| `sm` | 9 / 20 = 45% | 11 / 20 = 55% | 2 / 20 | 9 / 20 |
| `lg` | 10 / 20 = 50% | 12 / 20 = 60% | 2 / 20 | 8 / 20 |
| `trf` | 15 / 20 = 75% | 16 / 20 = 80% | 1 / 20 | 4 / 20 |

## Change From Previous Direct-use Rate

이전 direct-use 기준은 quote masking과 tag-list branch를 적용하기 전 기준이다.

| model | previous direct-use | after quote + tag-list branch | gain |
|---|---:|---:|---:|
| `sm` | 7 / 20 = 35% | 11 / 20 = 55% | +20 pp |
| `lg` | 8 / 20 = 40% | 12 / 20 = 60% | +20 pp |
| `trf` | 10 / 20 = 50% | 16 / 20 = 80% | +30 pp |

## Case-level Result

### `en_core_web_sm`

| status | cases | reason |
|---|---|---|
| strict success | 02, 04, 05, 06, 07, 10, 12, 13, 20 | 기존 direct-use + high-confidence tag-list cases |
| partial | 14, 17 | tag-list branch는 성공했지만 `display`, `sidewalk`, `building`, `large`가 medium/candidate로 남음 |
| fail | 01, 03, 08, 09, 11, 15, 16, 18, 19 | coordination, participle, MWE object, context, ellipsis, root/attachment issues |

### `en_core_web_lg`

| status | cases | reason |
|---|---|---|
| strict success | 02, 04, 06, 07, 10, 11, 12, 13, 19, 20 | 기존 direct-use + high-confidence tag-list cases |
| partial | 14, 17 | tag-list branch는 성공했지만 `display`, `building`, `large`가 medium/candidate로 남음 |
| fail | 01, 03, 05, 08, 09, 15, 16, 18 | attachment, participle, MWE object, context/POS, ellipsis issues |

### `en_core_web_trf`

| status | cases | reason |
|---|---|---|
| strict success | 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 17, 19, 20 | quote masking resolves 03/08, tag-list branch resolves 06/10/17, parser quality is best |
| partial | 14 | tag-list branch는 성공했지만 `large`가 floating attribute/candidate로 남음 |
| fail | 01, 15, 16, 18 | semantic attachment, ellipsis, `music stands`, borderline relation attachment |

## Branch Contribution

| branch | affected cases | `sm` gain | `lg` gain | `trf` gain | notes |
|---|---|---:|---:|---:|---|
| quote masking | 03, 08 | 0 | 0 | +2 | sm/lg는 같은 caption 안에 participle/MWE 오류가 남음 |
| tag-list branch | 06, 10, 14, 17 | +4 usable / +2 strict | +4 usable / +2 strict | +4 usable / +3 strict | tag-list global dependency parse failure 제거 |

## Interpretation

현재 20개 샘플 기준으로는 `trf`가 가장 안정적이다. 특히 quote masking과 tag-list branch를 붙였을 때 usable success가 80%까지 올라간다.

`sm`과 `lg`도 tag-list branch 덕분에 성공률이 올라가지만, 남은 실패의 대부분은 tag-list가 아니라 sentence caption 쪽의 parser 오류다. 대표적으로 `trash can`, `music stands`, participle attachment, ellipsis, root failure가 남아 있다.

따라서 다음 우선순위는 tag-list가 아니라 다음 세 가지다.

1. object MWE 보호: `trash can`, `music stands`
2. ellipsis repair: `one wears X, the other Y`
3. semantic attachment repair: PP/coordination/participle
