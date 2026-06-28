# 10k Auto Feedback Summary

## Run

- input: `data/gpic_captions_10k_train00000_00099/train/gpic_train_00000_00099_merged_10000.jsonl.gz`
- raw output: `reports/raw_concepts_10k_train00000_00099_trf_auto_feedback_v1.jsonl`
- stage9 output: `reports/canonical_concepts_10k_train00000_00099_trf_auto_feedback_v1.jsonl`
- quality audit: `reports/stage9_quality_audit_10k_train00000_00099_auto_feedback_v1.md`
- feedback candidates: `reports/feedback_candidates_10k_train00000_00099_auto_feedback_v1.tsv`
- feedback dashboard: `reports/feedback_dashboard_10k_train00000_00099_auto_feedback_v1.md`
- first 1000 detail: `reports/case_detail_10k_train00000_00099_trf_auto_feedback_v1_first1000.md`

## Scale

| item | count |
|---|---:|
| captions | 10,000 |
| sentence path | 9,896 |
| tag-list path | 104 |
| objects | 86,560 |
| attributes | 59,390 |
| actions | 35,769 |
| relations | 50,948 |
| canonical entities | 98,291 |
| canonical events | 35,769 |
| canonical facts | 261,830 |

Stage 8 raw extraction took about 116 seconds on GPU 0. Stage 9 canonicalization took about 12 seconds.

## Quality Bottlenecks

| metric | count | per caption |
|---|---:|---:|
| entity_parent_none | 18,290 | 1.829 |
| action_parent_fallback | 3,176 | 0.318 |
| raw_relation | 4,570 | 0.457 |
| raw_attribute_role | 23,778 | 2.378 |
| skipped_edges | 412 | 0.041 |
| self_edge_repair_candidate | 308 | 0.031 |

Compared with the previous 1k run, this 10k train sample is much richer and noisier. The main increase is not parser failure alone; it is broader visual vocabulary, text-heavy captions, diagrams/documents, and more generic reference language.

## Feedback Candidate Categories

| category | unique candidates | total hits |
|---|---:|---:|
| action_parent_fallback | 563 | 3,176 |
| entity_parent_none | 3,356 | 18,290 |
| generic_reference_candidate | 147 | 3,759 |
| hyphen_object_candidate | 60 | 294 |
| object_mwe_candidate | 546 | 1,729 |
| ocr_symbol_action_candidate | 27 | 125 |
| ocr_symbol_attribute_candidate | 53 | 55 |
| ocr_symbol_entity_candidate | 16 | 31 |
| phrasal_action_candidate | 58 | 369 |
| quote_object_anomaly | 1 | 2 |
| raw_attribute_role | 3,696 | 23,778 |
| raw_relation | 25 | 4,570 |
| self_edge_repair_candidate | 1 | 308 |
| self_relation_after_canonicalization | 7 | 10 |
| skipped_edge | 2 | 412 |

## New High-Priority Patterns

### 1. Stage 9 parent coverage is now the largest bottleneck

Top missing parent candidates include:

```text
individual, shoulder, right_hand, counter, sun, trim, board,
illustration, emblem, expression, portion, wheel, dirt, ring,
script, rope, container, basket, balloon, tile
```

This is mostly Stage 9 ontology work, not Stage 8 parser work. The next automatic expansion should focus on:

- body parts and body-part-with-side: `shoulder`, `right_hand`, `sleeve`
- scene/place/media objects: `counter`, `board`, `illustration`, `diagram`, `script`
- natural/landscape entities: `sun`, `dirt`, `moss`, `shrub`, `ripple`
- artifacts/accessories: `emblem`, `rope`, `basket`, `balloon`, `sticker`
- generic humans: `individual -> person`

### 2. Action fallback has two different causes

Top action fallback candidates include:

```text
be, ’, filter, obscure, overlook, center, engage, tilt,
support, prepare, angle, tie, pass, emphasize, title
```

These should not all be handled the same way.

| subtype | examples | likely action |
|---|---|---|
| noise/tokenization | `’`, `’re` | block or normalize before action extraction |
| visual state/effect | `obscure`, `filter`, `center`, `tilt`, `angle`, `emphasize` | action parent expansion |
| real physical action | `tie`, `prepare`, `pass`, `support` | action parent expansion |
| text/document predicate | `title`, `mention`, `discuss` | text/document action parent or count exclusion |
| weak copula/stative | `be` | likely block from countable action, or map to state only |

### 3. Raw attributes are high-volume and useful

Top raw attribute candidates include:

```text
grassy, other, paved, light, indoor, young, bare, calm
```

The useful part is attribute lexicon expansion. The dangerous part is `other`, which is not a visual attribute and should move toward reference/determiner handling.

### 4. Coreference/self-edge is still a real queue

The 10k run has 308 `self_edge_repair_candidate` hits. This confirms that self-edge repair is not a rare corner case.

The next general improvement should use the existing skipped edge evidence and search for an alternative antecedent excluding the source entity itself. Priority cases:

- relation evidence: `in_front_of`, `behind`, `near`, `beside`
- references: `it`, `them`, `him`, `her`, `one`, `other`, `both`
- generic noun aliases: `individual`, `structure`, `object`, `device`

### 5. Relation raw preservation is still acceptable

The largest raw relations are `to`, `from`, `include`, `into`, `for`. Since relation semantics are intentionally raw-preserving for now, this is not an immediate blocker.

The actionable relation work is not broad canonicalization. It is:

- preposition MWE candidate detection
- PP source repair
- self-edge repair
- passive/by-frame handling

## Recommended Next Automatic Tasks

1. Add a Stage 9 auto-frozen parent expansion candidate builder from the 10k `entity_parent_none` queue.
2. Split `action_parent_fallback` into `countable_action`, `visual_state`, `text_document_predicate`, `noise_or_auxiliary`.
3. Add a small action block/normalization rule for `’`, `’re`, and likely copular `be` count pollution.
4. Build an attribute expansion candidate TSV from high-frequency `raw_attribute_role`, excluding reference/determiner words such as `other`.
5. Implement a self-edge repair candidate analyzer that records relation evidence, source entity, rejected antecedent, and alternative antecedent candidates.
6. Keep relation canonicalization raw-preserving for now.

## Interpretation

The 10k run validates the feedback-loop plan. The biggest bottleneck is no longer whether Stage 8 can extract tuples; it can. The next gains come from automatic Stage 9 vocabulary/ontology expansion and reference repair queues.

Do not use this 10k output as a gold correction source. Use it as a frequency-ranked candidate generator, then freeze only items that pass source checks, fixed rubric audit, confidence thresholds, and regression tests.
