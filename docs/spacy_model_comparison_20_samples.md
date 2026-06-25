# spaCy Model Comparison on 20 GPIC Captions

목적: MWE merge 없이 spaCy English 모델 자체만 비교한다.

비교 모델:

```text
en_core_web_sm
en_core_web_md
en_core_web_lg
en_core_web_trf
```

입력:

```text
data/gpic_captions_test/val/gpic_val_00000.jsonl.gz
```

출력 리포트:

```text
reports/spacy_parse_sample_20.md
reports/spacy_parse_sample_20_md.md
reports/spacy_parse_sample_20_lg.md
reports/spacy_parse_sample_20_trf.md
```

## 핵심 결론

```text
md:
  sm 대비 큰 개선 없음.

lg:
  road/runs, arched windows, vest/scarf 같은 일부 구조 오류를 고침.
  trash can은 여전히 실패.

trf:
  가장 많이 개선됨.
  trash can, road/runs, speaking attachment, indoors, blue jersey, arched windows, vest/scarf에서 개선 확인.
  music stands는 여전히 실패.
```

## 에러 케이스별 비교

| case | 문제 | sm | md | lg | trf | 판단 |
|---:|---|---|---|---|---|---|
| 03 | `speaking` attachment | `speaking -> podium` | 동일 | 동일 | `speaking -> stands` | `trf` 개선 |
| 08 | `trash can` | `can=AUX`, `trash=pobj` | 동일 | 동일 | `can=NOUN`, `trash=compound`, chunk=`a black trash can` | `trf` 해결 |
| 09 | `indoors` | `NOUN`, `dobj` | 동일 | `ADV`지만 `dobj` | `ADV`, `advmod` | `trf` 해결 |
| 10 | `blue jersey` | `PROPN/PROPN` | 동일 | 동일 | `blue=ADJ`, `jersey=NOUN` | `trf` 개선. 단 tag-list parser는 여전히 필요 |
| 11 | `arched windows` | `arched=VERB/VBD`, `windows=dobj` | `arched=VERB/VBN`이지만 `amod` | `arched=ADJ`, `windows=NOUN` | `arched=ADJ`, `windows=NOUN` | `lg/trf` 해결 |
| 15 | `a vest and red scarf` | 하나의 chunk로 뭉침 | 동일 | `a vest`, `red scarf` 분리 | `a vest`, `red scarf` 분리 | `lg/trf` 해결 |
| 16 | `music stands` | `music` + `stands=VERB` | 실패 | 실패 | 실패 | 모델 교체만으로 해결 안 됨 |
| 19 | `road/runs` | `road=ROOT`, `runs=pobj(with)` | 동일 | `road=nsubj`, `runs=ROOT` | `road=nsubj`, `runs=ROOT` | `lg/trf` 해결 |

## 구체 예시

### case 08: trash can

`sm/md/lg`:

```text
trash | NOUN | pobj | on
can   | AUX  | aux  | reads
```

`trf`:

```text
trash | NOUN | compound | can
can   | NOUN | pobj     | on
```

해석:

```text
trf는 trash can을 복합명사로 봄.
sm/md/lg는 can reads 패턴에 끌려 can을 조동사로 오분류.
```

### case 19: road/runs

`sm/md`:

```text
road | NOUN | ROOT
runs | VERB | pobj | with
```

`lg/trf`:

```text
road | NOUN | nsubj | runs
runs | VERB | ROOT
line | NOUN | pobj | with
```

해석:

```text
lg/trf는 이 문장 구조를 정상 복구.
```

### case 16: music stands

모든 모델에서 실패:

```text
music | NOUN
stands | VERB
```

해석:

```text
music stands는 모델 교체만으로는 안정적으로 해결되지 않음.
이런 케이스는 object MWE 또는 phrase lexicon이 필요할 수 있음.
```

## 속도 비교

조건:

```text
20개 caption을 1,000개로 반복
n_process=1
MWE merge 없음
```

| model | batch_size | parse seconds | docs/sec |
|---|---:|---:|---:|
| `en_core_web_sm` | 128 | 9.15 | 109.3 |
| `en_core_web_md` | 128 | 9.90 | 101.0 |
| `en_core_web_lg` | 128 | 10.10 | 99.0 |
| `en_core_web_trf` | 32 | 21.00 | 47.6 |

주의:

```text
이 속도는 로컬 Windows, 1k 반복 샘플, n_process=1 기준.
100M 실제 처리 속도는 shard 병렬화, GPU 사용 여부, batch size, I/O에 따라 다시 측정해야 함.
```

## 현재 판단

```text
en_core_web_md:
  쓸 이유가 약함.

en_core_web_lg:
  sm보다 품질 개선이 있고 속도 저하는 작음.
  CPU 기반 대량 처리 후보로 재검토 가치 있음.

en_core_web_trf:
  품질은 가장 좋음.
  하지만 100M 전체 적용은 별도 GPU benchmark 필요.
  H200 환경에서는 실제 throughput을 다시 측정해야 함.
```

추천:

```text
1. 20개 말고 실제 GPIC 1k~10k 샘플로 sm/lg/trf 비교
2. lg와 trf의 parser 오류율을 수동 audit
3. trf의 H200 throughput 측정
4. 그래도 실패하는 music stands/tag-list/text mention은 rule branch로 처리
```
