# Multiword Relation Lexicon Layers

추천 구조에 맞춰 multi-word relation lexicon을 surface, semantic subtype, collapse rule, visual whitelist layer로 분리한 결과입니다.

## Output Files

- `resources/lexicons/multiword_relation_surface_forms.tsv`
- `resources/lexicons/multiword_relation_semantic_subtypes.tsv`
- `resources/lexicons/multiword_relation_collapse_rules.tsv`
- `resources/lexicons/multiword_relation_visual_whitelist.tsv`
- `resources/lexicons/multiword_relation_clean_core.tsv`

## Counts

| layer | rows |
|---|---:|
| surface forms | 102 |
| semantic subtypes | 102 |
| collapse rules | 102 |
| visual whitelist rows | 102 |
| final clean multiword relations | 73 |

## Surface Sources

| source | rows |
|---|---:|
| gqa_scene_graph_relation_surface | 46 |
| openimages_predicate_surface | 2 |
| streusle_mwe | 6 |
| tpp_pdep_visual_seed | 54 |
| visual_genome_predicate_surface | 97 |
| visual_genome_relationship_alias | 77 |

## Visual Sources

| source | rows |
|---|---:|
| gqa_scene_graph_relation_count | 46 |
| openimages_relationship_triplet | 2 |
| visual_genome_relationship_alias | 77 |
| visual_genome_relationship_count | 97 |

## Visual Whitelist

| whitelist | rows |
|---|---:|
| no | 29 |
| yes | 73 |

## Collapse Strategies

| strategy | rows |
|---|---:|
| complex_preposition_phrase | 24 |
| multiword_adposition_phrase | 7 |
| multiword_relation_phrase | 1 |
| predicate_plus_adposition | 23 |
| predicate_plus_adposition_or_object | 47 |

## Final Relation Types

| relation_type | rows |
|---|---:|
| action_relation | 2 |
| attachment_relation | 6 |
| material_relation | 4 |
| part_relation | 1 |
| perception_relation | 1 |
| pose_location | 22 |
| pose_support | 5 |
| spatial_contact | 1 |
| spatial_containment | 1 |
| spatial_depth | 6 |
| spatial_lateral | 8 |
| spatial_outside | 1 |
| spatial_proximity | 4 |
| spatial_region | 5 |
| spatial_support | 1 |
| state_support | 1 |
| surface_relation | 3 |
| wearing_relation | 1 |

## Notes

- `surface_forms`는 phrase 후보 출처를 분리합니다. PDEP/TPP는 현재 자동 원본 파싱 대신 visual relation seed source로 기록했습니다.
- `semantic_subtypes`는 STREUSLE/SNACS가 있으면 `snacs_supersenses`에 남기고, 없으면 project visual relation type을 기준으로 둡니다.
- `collapse_rules`는 UD fixed/MWE를 참고한 spaCy용 구현 힌트입니다. spaCy label과 UD label이 완전히 같다는 뜻은 아닙니다.
- `visual_whitelist`는 VG/GQA/OpenImages frequency 및 manual visual seed를 바탕으로 실제 caption/image relation으로 쓸지를 나눕니다.
- GQA만으로 whitelist를 올릴 때는 `gqa_count >= 100` 기준을 사용했습니다.
- `multiword_relation_clean_core.tsv`가 8단계 relation span detection에 바로 연결할 1차 파일입니다.
