# Modifier Attribute Lexicon Summary

확실한 외부 typed attribute source를 다운로드해서 합친 modifier attribute lexicon 요약입니다.

- unique terms: 1136
- clean unique terms: 877
- source entries: 1425

## Sources

| source | entries |
|---|---:|
| css_color_4 | 148 |
| dtd | 47 |
| fashionpedia | 294 |
| ovad | 229 |
| paco | 55 |
| vaw | 652 |

## Roles

| role | unique terms |
|---|---:|
| accessory_attribute | 6 |
| activity_attribute | 46 |
| age_attribute | 6 |
| attribute | 285 |
| brightness_attribute | 2 |
| clothing_cut_attribute | 32 |
| clothing_opening_attribute | 10 |
| color_attribute | 221 |
| condition_attribute | 11 |
| context_attribute | 8 |
| expression_attribute | 20 |
| fashion_style_attribute | 153 |
| food_state_attribute | 5 |
| gender_attribute | 7 |
| group_attribute | 7 |
| hair_attribute | 3 |
| material_attribute | 74 |
| motif_attribute | 6 |
| opacity_attribute | 5 |
| order_attribute | 11 |
| orientation_attribute | 6 |
| pattern_attribute | 40 |
| pose_attribute | 18 |
| race_attribute | 2 |
| shape_attribute | 25 |
| silhouette_attribute | 25 |
| size_attribute | 41 |
| spatial_attribute | 9 |
| state_attribute | 20 |
| textile_finish_attribute | 21 |
| texture_attribute | 59 |
| tone_attribute | 5 |
| weather_attribute | 10 |
| weight_attribute | 2 |

## Confidence

| confidence | unique terms |
|---|---:|
| high | 592 |
| low | 259 |
| medium | 285 |

## Notes

- `modifier_attributes_merged.tsv`: term 단위로 source/role을 합친 파일입니다.
- `modifier_attributes_clean.tsv`: parser rule lookup에 바로 쓰기 쉬운 high/medium-confidence 파일입니다.
- `modifier_attributes_detailed.tsv`: source별 원본 entry를 보존한 파일입니다.
- VAW의 `other` bucket과 `other(...)` placeholder는 clean modifier rule에 바로 쓰기 어렵기 때문에 generic placeholder는 제외했습니다.
- Fashionpedia는 fashion domain attribute라 `confidence=medium`으로 둡니다.
