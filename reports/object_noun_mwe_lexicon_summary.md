# Object Noun MWE Lexicon Summary

High-confidence visual object labels and filtered WordNet noun MWEs로 만든 parser-time object MWE 사전입니다.

## Output Files

- `resources/lexicons/object_noun_mwe_clean_core.tsv`

## Source Label Counts

| source | raw labels |
|---|---:|
| coco_object | 80 |
| lvis_object | 3028 |
| openimages_boxable | 602 |
| visual_genome_object_synset | 40154 |
| wordnet_noun_mwe | 62411 |

## Lexicon Counts

| item | count |
|---|---:|
| candidates | 97558 |
| clean_core | 3548 |

## Clean Core Source Membership

| source | terms |
|---|---:|
| coco_object | 30 |
| lvis_object | 1277 |
| openimages_boxable | 331 |
| plural_variant | 1792 |
| visual_genome_object_synset | 2602 |
| wordnet_noun_mwe | 3096 |

## Key Examples

| term | canonical | confidence | sources |
|---|---|---|---|
| `trash can` | `trash_can` | high | lvis_object|visual_genome_object_synset|wordnet_noun_mwe |
| `trash cans` | `trash_can` | high | lvis_object|plural_variant|visual_genome_object_synset|wordnet_noun_mwe |
| `music stand` | `music_stand` | high | wordnet_noun_mwe |
| `music stands` | `music_stand` | high | plural_variant|wordnet_noun_mwe |
| `traffic light` | `traffic_light` | high | coco_object|lvis_object|openimages_boxable|visual_genome_object_synset|wordnet_noun_mwe |
| `hot dog` | `hot_dog` | high | coco_object|openimages_boxable|visual_genome_object_synset|wordnet_noun_mwe |
| `tennis court` | `tennis_court` | high | visual_genome_object_synset|wordnet_noun_mwe |

## Notes

- Clean core는 visual object dataset label을 우선한다.
- 단, clean modifier attribute 사전에 있는 수식어가 prefix로 붙은 compositional attribute+noun phrase는 merge 대상에서 제외한다.
- WordNet-only MWE는 너무 넓기 때문에 `can`, `stand`처럼 실제 POS 오류를 자주 만드는 head에 한해 clean core에 넣는다.
- plural variant는 parser-time matching용 surface이며 canonical은 singular phrase로 유지한다.
