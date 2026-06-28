# Stage 9 Plural Lexical Object v1 Regression Check

## Inputs

- before: `reports\canonical_concepts_1k_val00002_00011_trf_stage9_parent_action_v3.jsonl`
- after: `reports\canonical_concepts_1k_val00002_00011_trf_stage9_plural_v1.jsonl`

## Executive Summary

| metric | before | after | delta |
|---|---:|---:|---:|
| `records` | 1000 | 1000 | +0 |
| `entities` | 7344 | 7344 | +0 |
| `parent_none` | 1078 | 1078 | +0 |
| `events` | 2294 | 2294 | +0 |
| `action_fallback` | 76 | 76 | +0 |
| `relations` | 3382 | 3382 | +0 |
| `raw_relation` | 245 | 245 | +0 |
| `raw_attribute` | 1519 | 1519 | +0 |
| `self_relation` | 0 | 0 | +0 |
| `skipped_edges` | 36 | 36 | +0 |
| `facts` | 20618 | 20618 | +0 |

## Record-Level Difference

- common records: 1000
- changed records: 31
- only before: 0
- only after: 0
- changed ids preview: `015256263a73fe50af4535bf363c7798640617f581db22e21559c3587f4a9414, 035bb4cdb8ca56dc0a7530e6683f8a363751d714c6d4be3b0cf2d057ee186c14, 041b2ed39865ab20e37e73cf63c0d4644fe46726e21f3637bbddeae0ec0e9c14, 05298b10f372436be8301e8a38ec3780d3d72b06dbfa81b038339e54667b7814, 05d08faaf73fc5442b94561f03b30bd5fd7b56a17b88c1d84a08a12476698c14, 08d60a27d8ff9e147af4a593e44842b2f411974a2bc5309e515b3f354c5e4814, 0a3407edb870bc97cc4569404a08a576fa5a445bfd18d83b28015bd126aca814, 10b201388a1aaea146d19988d64a0ff8b5de4058bbbbc38731ad151a60b2d414, 11c5ce40f47f4f793e9b7afbadfb02cfa880ae5b3a48818a62b2b645253d9c14, 153f8c270af8d287caf9f6fc25979d75d19ef0a1e55f465d6d08a62f5d152c14, 18cab9b7e122f21dedb9a6f010c681fc3bbf157bbd1aca272e281c100513f414, 19356508f057677b1fbe427ed56b85e1618bbb971ad47731dc8599d553f1d414, 1b0acd33c3d9b0d42ae8e6ceba63add1710ed4f650c85e1928a6ebae029e2014, 1c0b1f651a8c8b2291705e3f0c16ad121607fffd5872ea906cb2811b21a65414, 21a9a87961d7b6dfb5468474125c99759d8d3c1c4b813af52692aa6e07612c14, 24f8fc8c95c4229dd9f864e831930d3d324ddd41d1df6c03f242717f5bfdb014, 25028d698641af5565e4e953983789e6f8b8917b8c9999da077df059106da414, 2895533b9661e7a31f6b65c9299bd282604b5db3af8a4ca7137b5cead5694014, 28b4c38703622982f6502a5962011eb1c15cd5659f40e58672d59f476544e414, 2deae4041d286b657e0e62e504b821b93a878e3f8be4ac360389708ef74b4014`

## Target Term Check

### Entity canonical counts

| item | before | after | delta |
|---|---:|---:|---:|
| `glass` | 38 | 6 | -32 |
| `glasses` | 0 | 32 | +32 |
| `orange` | 0 | 0 | +0 |
| `oranges` | 0 | 0 | +0 |

### Entity surface counts

| item | before | after | delta |
|---|---:|---:|---:|
| `glass` | 6 | 6 | +0 |
| `glasses` | 32 | 32 | +0 |
| `orange` | 0 | 0 | +0 |
| `oranges` | 0 | 0 | +0 |

### Attribute counts

| item | before | after | delta |
|---|---:|---:|---:|
| `glass` | 15 | 15 | +0 |
| `glasses` | 0 | 0 | +0 |
| `orange` | 45 | 45 | +0 |
| `oranges` | 0 | 0 | +0 |

## Changed Counter Deltas

### Entity canonical deltas

| item | before | after | delta |
|---|---:|---:|---:|
| `glasses` | 0 | 32 | +32 |
| `glass` | 38 | 6 | -32 |

### Entity parent deltas

| item | before | after | delta |
|---|---:|---:|---:|
| `material_source` | 42 | 10 | -32 |
| `eyewear_or_drinking_vessel` | 0 | 32 | +32 |
| `accessory` | 38 | 70 | +32 |

### Attribute value deltas

- 변화 없음.

### Action canonical deltas

- 변화 없음.

### Relation canonical deltas

- 변화 없음.

## Target Examples After

### `attribute:glass|parents:material_attribute/material/visual_attribute`

- `#25` `1791e009c3` source=facade; fact_type=has_attribute; caption="Tall palm trees stand in front of a modern building with a reflective glass facade. The building mirrors the trees and sky, while a dark car is par..."
- `#132` `13c5e22b39` source=structure; fact_type=has_attribute; caption="Construction vehicles, including a crane and excavators, are parked on a dirt lot at a building site. A large glass dome structure stands to the le..."
- `#187` `463ad2e221` source=railing; fact_type=has_attribute; caption="A staircase with glass railings leads upward on the left. To the right, a wall is decorated with colorful, circular glass art pieces arranged in ro..."
- `#187` `463ad2e221` source=piece; fact_type=has_attribute; caption="A staircase with glass railings leads upward on the left. To the right, a wall is decorated with colorful, circular glass art pieces arranged in ro..."
- `#208` `064d9d2729` source=mug; fact_type=has_attribute; caption="A glass mug with a pink straw holds a frothy white drink, sitting on a table."

### `attribute:orange|parents:color_attribute/color/visual_attribute`

- `#9` `08a998bcf6` source=bicycle; fact_type=has_attribute; caption="A person in a pink shirt stands next to an orange bicycle on a paved road. Green signs for “Gilltown Stud” and “Gilltown Stud Offices” are mounted ..."
- `#10` `08acaf299a` source=sky; fact_type=has_attribute; caption="A car's side mirror reflects a highway at sunset, showing orange and yellow skies above trees. Orange and white traffic cones line the road, with a..."
- `#16` `100e688aa0` source=foot; fact_type=has_attribute; caption="A brown goose stands on snow-covered ground, its orange feet visible. It has a dark head and is surrounded by scattered leaves."
- `#24` `15ca060b0e` source=shirt; fact_type=has_attribute; caption="A person in a cap and orange shirt draws back a bow, aiming at a colorful target on a grassy field."
- `#45` `29bc2961ca` source=shirt; fact_type=has_attribute; caption="Several children sit on the floor around a large cardboard game mat with a space-themed design. One boy in an orange shirt holds a controller, whil..."

### `entity:glasses|text:glasses|parent:eyewear_or_drinking_vessel/accessory/artifact`

- `#29` `1b0acd33c3` entity_id=ent_m4; type=object; caption="Two people sit at a white table wearing 3D glasses. Shadows and light patterns are projected onto the table surface, with one person adjusting thei..."
- `#29` `1b0acd33c3` entity_id=ent_m12; type=object; caption="Two people sit at a white table wearing 3D glasses. Shadows and light patterns are projected onto the table surface, with one person adjusting thei..."
- `#98` `55dddc3d49` entity_id=ent_m2; type=object; caption="An older woman with glasses stands at a microphone, wearing a red embroidered vest over a dark shirt. She is in a room with ornate gold decorations..."
- `#103` `035bb4cdb8` entity_id=ent_m11; type=object; caption="A man in a suit stands at a podium speaking into a microphone, holding a small object. Two women stand beside him, one on each side, both wearing m..."
- `#104` `041b2ed398` entity_id=ent_m1; type=object; caption="A child wearing glasses and an orange headscarf sits on a wooden stage, smiling at the camera. The stage has a light-colored floor with a patterned..."

### `entity:glass|text:glass|parent:artifact/material_source`

- `#396` `4d13f3a37c` entity_id=ent_m4; type=object; caption="bottles, beer, paulaner, labels, glass, row"
- `#647` `20ec1cd8be` entity_id=ent_m12; type=object; caption="A dish of savory food sits on a dark stone plate, topped with a sunny-side-up egg and chopped green herbs. A spoon rests on the plate, and a glass ..."
- `#725` `15d477cf67` entity_id=ent_m2; type=object; caption="octagonal ceiling, stained glass, stone arches, light rays, ornate windows"
- `#741` `25329704eb` entity_id=ent_m8; type=object; caption="A person sits on a chair holding a guitar, wearing a blue vest and jeans. A red cup and glass sit on the table in front of them."
- `#965` `2f3febde47` entity_id=ent_m7; type=object; caption="Two men sit at a round table covered with a white tablecloth, smiling at the camera. One holds a glass of water and the other a glass of wine, with..."

## Interpretation

- 전체 metric 또는 record signature에 변화가 있다. 위 delta와 target example을 우선 확인해야 한다.
- focused probe에서는 `oranges`와 `glasses`를 object로 유지하고, 단수/수식어 `orange`, `glass`는 attribute 쪽으로 유지하는 동작을 확인했다.
- 다음 대규모 적용 전에는 GPIC에서 target phenomenon 후보를 자동 수집해서, 실제 빈도와 실패 패턴을 먼저 축적하는 것이 더 효율적이다.
