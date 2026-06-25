# COCO Attribute Subtype Tagging

COCO Attributes 중 기존 typed clean 사전과 exact overlap되지 않았던 항목에 세부 role을 1차로 부여한 결과입니다.
COCO 원본은 attribute vocabulary로는 clean하지만, `color/material/pose/...` 같은 subtype은 제공하지 않기 때문에 여기서는 프로젝트용 매핑을 따로 둡니다.

## 요약

- COCO non-overlap terms: 119
- COCO all typed terms: 204
- untagged fallback: 0

## 분류 상태

| status | terms |
|---|---:|
| clean_alias_exact_match | 4 |
| clean_alias_exact_match_plus_coco_rule | 1 |
| coco_subtype_rule | 114 |

## Confidence

| confidence | terms |
|---|---:|
| high | 56 |
| medium | 63 |

## Role Counts For Non-Overlap COCO

| role | terms |
|---|---:|
| activity_attribute | 26 |
| aesthetic_attribute | 7 |
| affect_attribute | 17 |
| age_attribute | 1 |
| authenticity_attribute | 2 |
| behavior_attribute | 5 |
| brightness_attribute | 2 |
| complexity_attribute | 1 |
| condition_attribute | 6 |
| context_attribute | 7 |
| food_quality_attribute | 5 |
| functional_attribute | 7 |
| material_attribute | 2 |
| mental_state_attribute | 5 |
| order_attribute | 1 |
| physical_property_attribute | 2 |
| physiological_state_attribute | 5 |
| pose_attribute | 5 |
| safety_attribute | 3 |
| shape_attribute | 1 |
| size_attribute | 2 |
| social_attribute | 6 |
| speed_attribute | 1 |
| sport_attribute | 4 |
| state_attribute | 8 |
| style_attribute | 11 |
| surface_finish_attribute | 2 |
| technology_attribute | 2 |
| temperature_attribute | 4 |
| texture_attribute | 2 |
| value_attribute | 2 |

## 생성 파일

- `resources/lexicons/coco_attributes_new_subtype_tagged.tsv`: 기존 clean 사전에 없던 COCO attribute의 subtype tagging 결과
- `resources/lexicons/coco_attributes_clean_typed.tsv`: 기존 overlap 85개와 새로 tag한 119개를 합친 COCO clean typed vocabulary
- `resources/lexicons/coco_attributes_new_subtype_role_counts.tsv`: non-overlap COCO role별 count

## 해석

- `classification_status=clean_alias_exact_match`: `metal / metallic`처럼 slash label을 쪼갰을 때 기존 clean role과 매칭된 경우입니다.
- `classification_status=coco_subtype_rule`: COCO controlled vocabulary를 프로젝트 role taxonomy에 매핑한 1차 rule입니다.
- 새 role은 COCO가 공식 제공한 subtype이 아니라, caption-to-concept count schema를 위한 프로젝트 내부 subtype입니다.
- Visual Genome raw new attribute는 이 파일에 섞지 않았습니다.
