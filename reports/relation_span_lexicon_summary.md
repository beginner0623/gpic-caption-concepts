# Relation Span Lexicon Summary

Visual Genome relationships, Visual Genome relationship aliases/synsets, Open Images relationship triplets, and STREUSLE MWE annotations를 사용해 relation span 후보를 만든 결과입니다.

## Output Files

- `resources/lexicons/relation_span_candidates.tsv`: classified relation span 후보 전체
- `resources/lexicons/relation_multiword_span_candidates.tsv`: multi-word relation span 후보
- `resources/lexicons/relation_span_clean_core.tsv`: high-confidence parser lookup 후보
- `resources/lexicons/visual_genome_relation_predicates.tsv`: Visual Genome predicate frequency
- `resources/lexicons/visual_genome_relation_aliases.tsv`: Visual Genome alias mapping
- `resources/lexicons/openimages_relation_predicates.tsv`: Open Images relationship predicate vocabulary

## Counts

| item | count |
|---|---:|
| Visual Genome unique predicates | 36382 |
| Visual Genome alias rows | 9041 |
| Open Images relation predicates | 31 |
| relation span candidates | 148 |
| multi-word span candidates | 102 |
| clean core relation spans | 119 |

## Clean Core Relation Types

| relation_type | terms |
|---|---:|
| action_relation | 10 |
| association_relation | 2 |
| attachment_relation | 6 |
| material_relation | 4 |
| orientation_relation | 1 |
| part_relation | 2 |
| perception_relation | 2 |
| pose_location | 22 |
| pose_support | 5 |
| possession_relation | 2 |
| spatial_contact | 2 |
| spatial_containment | 7 |
| spatial_depth | 7 |
| spatial_lateral | 8 |
| spatial_location | 1 |
| spatial_outside | 2 |
| spatial_path | 3 |
| spatial_proximity | 9 |
| spatial_region | 7 |
| spatial_support | 4 |
| spatial_vertical | 6 |
| state_support | 1 |
| surface_relation | 3 |
| wearing_relation | 3 |

## Key Examples

| term | canonical | relation_type | confidence | sources | vg_count |
|---|---|---|---|---|---:|
| `on top of` | `on_top_of` | `spatial_support` | high | manual_relation_seed|streusle_mwe|visual_genome_relationship_alias|visual_genome_relationship_count | 31575 |
| `in front of` | `in_front_of` | `spatial_depth` | high | manual_relation_seed|streusle_mwe|visual_genome_relationship_alias|visual_genome_relationship_count | 13204 |
| `next to` | `next_to` | `spatial_proximity` | high | manual_relation_seed|streusle_mwe|visual_genome_relationship_alias|visual_genome_relationship_count | 26445 |
| `made of` | `made_of` | `material_relation` | high | manual_relation_seed|visual_genome_relationship_alias|visual_genome_relationship_count | 2332 |
| `covered with` | `covered_with` | `surface_relation` | high | manual_relation_seed|visual_genome_relationship_alias|visual_genome_relationship_count | 1294 |
| `hanging from` | `hanging_from` | `attachment_relation` | high | manual_relation_seed|visual_genome_relationship_alias|visual_genome_relationship_count | 5412 |
| `attached to` | `attached_to` | `attachment_relation` | high | manual_relation_seed|visual_genome_relationship_alias|visual_genome_relationship_count | 9668 |

## Notes

- Visual Genome alias는 유용하지만 noisy합니다. 예: `near a farm`, `four` 같은 row가 있으므로 rule-classified term만 후보에 넣었습니다.
- Open Images triplet predicate는 작지만 high precision source로 취급했습니다.
- STREUSLE는 visual relation vocabulary가 아니라 MWE/preposition annotation 근거입니다. 이번 파일에서는 rule과 맞는 MWE만 보조 source로 들어갑니다.
- `on top of` 같은 phrase는 parser 전 retokenize/masking 후보가 아니라, 8단계 raw tuple extraction에서 relation span으로 읽기 위한 lookup 후보입니다.
