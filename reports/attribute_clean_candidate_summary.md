# Attribute Clean Typed Candidate Summary

기존 typed clean lexicon에 COCO Attributes high-confidence typed 항목을 합쳐 만든 최종 clean typed 후보입니다.

## Output Files

- `resources/lexicons/attribute_clean_typed_candidate.tsv`: 기존 clean + COCO high 전체 role 후보
- `resources/lexicons/attribute_clean_core_typed_candidate.tsv`: 11개 core modifier role만 남긴 1차 parser용 후보

## Counts

| file | terms | role types |
|---|---:|---:|
| attribute_clean_typed_candidate.tsv | 933 | 41 |
| attribute_clean_core_typed_candidate.tsv | 522 | 11 |

## Core Role Counts

| role | terms |
|---|---:|
| color_attribute | 221 |
| material_attribute | 76 |
| size_attribute | 43 |
| shape_attribute | 26 |
| pattern_attribute | 40 |
| texture_attribute | 61 |
| brightness_attribute | 2 |
| condition_attribute | 12 |
| state_attribute | 28 |
| pose_attribute | 23 |
| weather_attribute | 10 |

## Notes

- COCO `confidence=medium` 항목은 여기 넣지 않았습니다.
- `attribute_clean_core_typed_candidate.tsv`는 색/재질/크기/형태/패턴/질감/밝기/상태/포즈/날씨 등 11개 core modifier role만 포함합니다.
- `attribute_clean_typed_candidate.tsv`는 activity/fashion/functional 같은 확장 role도 보존한 audit용 후보입니다.
