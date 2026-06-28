# Stage 9 Parent Coverage Audit

- date: `2026-06-28`
- target: Stage 9 `canonical_entities[*].parent_chain`
- files:
  - `reports/canonical_concepts_sample100_val00000_trf_stage9_canonical_parent_v1.jsonl`
  - `reports/canonical_concepts_alt100_val00001_trf_stage9_canonical_parent_v1.jsonl`

## Summary

| dataset | canonical entities | no parent | parent coverage |
|---|---:|---:|---:|
| `sample100 val00000` | 724 | 460 | 36.46% |
| `alt100 val00001` | 701 | 448 | 36.09% |

This means Stage 9 parent mapping is currently only an initial conservative layer. It is not yet a broad ontology mapping.

## Why Parent Is Missing

Current parent assignment comes from only two places:

1. `resources/lexicons/stage9_object_canonical_seed.tsv`
   - small, high-confidence seed list
   - people, animals, vehicles, clothing, devices, documents, scene contexts, body parts, furniture, sports equipment

2. `semantic_type_fallback`
   - only when the earlier Stage 9 semantic type is already one of the known classes such as `person`, `animal`, `vehicle`, `clothing`, `device`, `document`

Everything else falls back to:

```text
canonical_lemma = raw lemma
parent_chain = []
source = raw_lemma
```

That is why common scene/object words such as `building`, `sky`, `tree`, `wall`, `grass`, `field`, and `window` currently have no parent.

## Missing Parent by Type

| dataset | no-parent type | count |
|---|---|---:|
| `sample100 val00000` | `object` | 455 |
| `sample100 val00000` | `reference` | 4 |
| `sample100 val00000` | `group` | 1 |
| `alt100 val00001` | `object` | 443 |
| `alt100 val00001` | `instance` | 3 |
| `alt100 val00001` | `contrastive_instance` | 1 |
| `alt100 val00001` | `group` | 1 |

## Top Missing Parent Lemmas

### sample100 val00000

| lemma | count |
|---|---:|
| `building` | 17 |
| `sky` | 17 |
| `tree` | 15 |
| `wall` | 9 |
| `grass` | 8 |
| `fence` | 8 |
| `field` | 7 |
| `window` | 6 |
| `ground` | 6 |
| `hat` | 4 |
| `road` | 4 |
| `horizon` | 4 |
| `spectator` | 4 |
| `light` | 4 |
| `hillside` | 4 |
| `pipe` | 4 |
| `hill` | 4 |
| `floor` | 3 |
| `bag` | 3 |
| `cross` | 3 |
| `sidewalk` | 3 |
| `roof` | 3 |
| `mountain` | 3 |
| `frame` | 3 |
| `stage` | 3 |
| `pillar` | 3 |
| `beam` | 3 |
| `earring` | 3 |
| `shadow` | 3 |
| `entrance` | 3 |

### alt100 val00001

| lemma | count |
|---|---:|
| `tree` | 23 |
| `building` | 13 |
| `sky` | 12 |
| `field` | 11 |
| `wall` | 8 |
| `street` | 7 |
| `water` | 7 |
| `hockey_player` | 7 |
| `path` | 6 |
| `grass` | 5 |
| `snow` | 4 |
| `leaf` | 4 |
| `ground` | 4 |
| `podium` | 4 |
| `mountain` | 4 |
| `flower` | 3 |
| `step` | 3 |
| `ice` | 3 |
| `bush` | 3 |
| `paved_surface` | 3 |
| `window` | 3 |
| `view` | 3 |
| `light` | 3 |
| `figurine` | 3 |
| `beach` | 3 |
| `track` | 3 |
| `house` | 3 |
| `room` | 3 |
| `image` | 2 |
| `bottle` | 2 |

## Recommended Fix

Do not solve this by adding arbitrary case-by-case parent labels.

The next Stage 9 step should build a separate parent lexicon candidate file:

```text
raw/canonical object lemma
-> candidate parent chain
-> source
-> confidence
-> audit status
```

Recommended source priority:

1. visual object datasets:
   - COCO
   - LVIS
   - Open Images
   - Visual Genome object synsets

2. lexical ontology:
   - WordNet / Open English WordNet hypernyms

3. high-frequency GPIC missing-parent audit:
   - only for prioritizing what to inspect
   - not for deciding parent labels by itself

The actual parent mapping should be frozen as a versioned TSV before large-scale GPIC processing.
