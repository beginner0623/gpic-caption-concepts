# COCO Attributes / Visual Genome Attribute Overlap

기존 `modifier_attributes_clean.tsv` 사전을 기준으로 COCO Attributes와 Visual Genome attribute vocabulary가 겹치는지 확인한 결과입니다.
이번 파일은 분류를 새로 하지 않고, 외부 source의 attribute 후보가 기존 사전에 이미 있는지 여부만 나눕니다.

## 기준

- overlap 기준: `resources/lexicons/modifier_attributes_clean.tsv`의 `term`과 정규화된 exact match
- 보조 확인: `modifier_attributes_merged.tsv` 기준 overlap 여부도 TSV 컬럼에 함께 기록
- 정규화: lowercase, underscore/hyphen -> space, consecutive whitespace collapse

## 요약

| source | unique terms | overlap with clean | not in clean |
|---|---:|---:|---:|
| COCO Attributes | 204 | 85 | 119 |
| Visual Genome attributes | 63787 | 557 | 63230 |

## Role-Classified Subset

아래 숫자는 새 분류 규칙을 적용한 것이 아니라, 기존 clean 사전에 이미 있던 term만 우리 role을 그대로 승계한 결과입니다.

| source | role-classified terms | rule |
|---|---:|---|
| COCO Attributes | 85 | clean exact overlap |
| Visual Genome attributes | 557 | clean exact overlap |

| assigned role | terms |
|---|---:|
| accessory_attribute | 6 |
| activity_attribute | 69 |
| age_attribute | 9 |
| brightness_attribute | 2 |
| clothing_cut_attribute | 3 |
| clothing_opening_attribute | 5 |
| color_attribute | 126 |
| condition_attribute | 15 |
| context_attribute | 8 |
| expression_attribute | 28 |
| fashion_style_attribute | 14 |
| food_state_attribute | 7 |
| gender_attribute | 9 |
| group_attribute | 7 |
| hair_attribute | 4 |
| material_attribute | 73 |
| motif_attribute | 5 |
| opacity_attribute | 5 |
| order_attribute | 11 |
| orientation_attribute | 8 |
| pattern_attribute | 38 |
| pose_attribute | 26 |
| race_attribute | 2 |
| shape_attribute | 28 |
| silhouette_attribute | 18 |
| size_attribute | 33 |
| spatial_attribute | 13 |
| state_attribute | 30 |
| textile_finish_attribute | 13 |
| texture_attribute | 60 |
| tone_attribute | 5 |
| weather_attribute | 10 |
| weight_attribute | 3 |

## 예시

| source | 기존 사전과 겹침 예시 | 기존 사전에 없음 예시 |
|---|---|---|
| COCO Attributes | `standing`, `sitting`, `walking`, `eating`, `waiting`, `playing`, `sleeping`, `working`, `running`, `hiding`, `riding`, `drinking`, `swimming`, `smiling`, `jumping`, `talking`, `skiing`, `grazing`, `skating`, `leaning` | `laying`, `watching / looking`, `moving`, `flying`, `traveling`, `enjoying`, `thinking`, `loving`, `holding`, `feeding`, `floating`, `hunting`, `listening`, `hanging`, `smelling / sniffing`, `socializing`, `stretching`, `learning`, `following`, `fishing` |
| Visual Genome | `white`, `black`, `blue`, `green`, `red`, `brown`, `yellow`, `small`, `large`, `wooden`, `gray`, `silver`, `metal`, `orange`, `grey`, `tall`, `long`, `dark`, `pink`, `clear` | `here`, `parked`, `hanging`, `bare`, `blonde`, `shiny`, `flying`, `painted`, `part`, `sliced`, `tennis`, `distant`, `looking`, `grassy`, `leafy`, `wearing`, `man's`, `baseball`, `pictured`, `decorative` |

## 생성 파일

- `resources/external/coco_attributes_vocab.tsv`: COCO Attributes 원본 vocabulary
- `resources/external/visual_genome_attributes_vocab.tsv`: Visual Genome full attributes에서 뽑은 raw attribute vocabulary와 빈도
- `resources/external/visual_genome_attribute_synsets.tsv`: Visual Genome attribute synset vocabulary
- `resources/lexicons/coco_attributes_overlap.tsv`: COCO 중 기존 clean 사전과 겹치는 항목
- `resources/lexicons/coco_attributes_new.tsv`: COCO 중 기존 clean 사전에 없는 항목
- `resources/lexicons/visual_genome_attributes_overlap.tsv`: Visual Genome 중 기존 clean 사전과 겹치는 항목
- `resources/lexicons/visual_genome_attributes_new.tsv`: Visual Genome 중 기존 clean 사전에 없는 항목
- `resources/lexicons/external_attribute_overlap.tsv`: COCO와 Visual Genome 비교 결과 통합본
- `resources/lexicons/coco_attributes_role_classified.tsv`: COCO 중 clean role을 승계할 수 있는 항목만 모은 파일
- `resources/lexicons/visual_genome_attributes_role_classified.tsv`: Visual Genome 중 clean role을 승계할 수 있는 항목만 모은 파일
- `resources/lexicons/external_attribute_role_classified.tsv`: COCO와 Visual Genome role-classified subset 통합본

## 주의

- Visual Genome은 raw annotation 기반이라 `young`, `standing`, `open`처럼 attribute로 쓸 만한 표현과 `sidewalk`, `sky`처럼 object/context에 가까운 표현이 섞일 수 있습니다.
- 그래서 이 결과는 parser 사전에 바로 병합하는 용도가 아니라, 다음 단계에서 검토할 candidate pool입니다.
- `*_role_classified.tsv`는 안전한 subset입니다. 기존 clean 사전에 없던 항목은 role을 새로 추론하지 않았습니다.
