# Tag-list Branch Summary

- input: `data\gpic_captions_test\val\gpic_val_00000.jsonl.gz`
- sample size: 20 captions
- tag-list cases: 4 captions (`06`, `10`, `14`, `17`)
- models: `en_core_web_sm`, `en_core_web_lg`, `en_core_web_trf`
- options: `--mask-quotes --parse-tag-lists`

## Branch Policy

`caption_type == "tag"` rows are not parsed as one full sentence. They are split by comma into tag segments, and each segment is parsed independently with spaCy.

The report keeps segment-level noun chunks plus POS/lemma/dependency/head information, but those chunks and dependencies are segment-internal only. Cross-segment dependency edges are not created. Final concepts are represented in the same downstream shape as sentence captions: `Concept Mentions` plus `Edges`.

## Generated Reports

| model | report |
|---|---|
| `en_core_web_sm` | `reports\spacy_parse_sample_20_sm_tag_branch.md` |
| `en_core_web_lg` | `reports\spacy_parse_sample_20_lg_tag_branch.md` |
| `en_core_web_trf` | `reports\spacy_parse_sample_20_trf_tag_branch.md` |

## Aggregate Counts

All three models produced the same concept/edge counts on the 4 tag-list captions.

| model | objects | attributes | contexts | `has_attribute` | `has_context` | `candidate_has_attribute` |
|---|---:|---:|---:|---:|---:|---:|
| `sm` | 19 | 10 | 1 | 9 | 1 | 1 |
| `lg` | 19 | 10 | 1 | 9 | 1 | 1 |
| `trf` | 19 | 10 | 1 | 9 | 1 | 1 |

## Confidence Counts

| model | high mentions | medium mentions | main medium cases |
|---|---:|---:|---|
| `sm` | 26 | 4 | `display`, `large`, `sidewalk`, `building` |
| `lg` | 27 | 3 | `display`, `large`, `building` |
| `trf` | 29 | 1 | `large` |

## Case Results

### Case 06

Caption:

```text
smiling couple, formal party, british flags, chandelier, wine glasses
```

All models:

| output | count | notes |
|---|---:|---|
| object | 5 | `couple`, `party`, `flags`, `chandelier`, `glasses` |
| attribute | 4 | `smiling`, `formal`, `british`, `wine` |
| edge | 4 | all segment-internal `has_attribute` |

### Case 10

Caption:

```text
roller skaters, helmet, referee, court, blue jersey
```

All models:

| output | count | notes |
|---|---:|---|
| object | 5 | `skaters`, `helmet`, `referee`, `court`, `jersey` |
| attribute | 2 | `roller`, `blue` |
| edge | 2 | `roller -> skaters`, `blue -> jersey` |

### Case 14

Caption:

```text
brown boot, indoor, brick wall, display, large
```

All models:

| output | count | notes |
|---|---:|---|
| object | 3 | `boot`, `wall`, `display` |
| attribute | 3 | `brown`, `brick`, `large` |
| context | 1 | `indoor` |
| edge | 4 | `brown -> boot`, `scene -> indoor`, `brick -> wall`, candidate `large -> display` |

Model difference:

| model | `display` handling |
|---|---|
| `sm` | POS is `VERB/VB`, preserved as `object` with role `ambiguous_segment_head`, confidence `medium` |
| `lg` | POS is `VERB/VB`, preserved as `object` with role `ambiguous_segment_head`, confidence `medium` |
| `trf` | POS is `NOUN/NN`, preserved as high-confidence object |

### Case 17

Caption:

```text
glass wall, worker, sidewalk, building, reflection, grass
```

All models:

| output | count | notes |
|---|---:|---|
| object | 6 | `wall`, `worker`, `sidewalk`, `building`, `reflection`, `grass` |
| attribute | 1 | `glass` |
| edge | 1 | `glass -> wall` |

Model difference:

| model | lower-confidence items |
|---|---|
| `sm` | `sidewalk`, `building` are preserved as medium-confidence object heads because POS is unstable |
| `lg` | `building` is preserved as medium-confidence object head |
| `trf` | all object heads are high confidence |

## Interpretation

The tag-list branch removes the old dependency-parse failure mode for cases `06`, `10`, `14`, and `17`. Those captions no longer produce misleading global `conj`, `appos`, or root relations.

The branch still keeps POS, lemma, dep, and head information, but only inside each comma segment. This gives us a common downstream representation with sentence captions while avoiding false cross-segment relations.

Remaining uncertainty is not structural; it is local POS ambiguity in single-token tags such as `display`, `sidewalk`, and `building`. The current rule keeps these as object mentions with medium confidence instead of dropping them.
