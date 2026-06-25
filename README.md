# GPIC Caption-To-Concept Pipeline

This workspace contains notes and prototype scripts for building a caption-only
concept extraction pipeline for GPIC.

## Current Contents

- `scripts/extract_gpic_captions.py`: streams GPIC Hugging Face tar shards and
  writes only JSON metadata/caption rows to JSONL. Images are not saved.
- `outputs/`: research notes and method surveys for caption-to-concept schema
  design.

## GPIC Caption Extraction

GPIC is gated on Hugging Face. Accept the dataset terms first, then set
`HF_TOKEN`.

## Environment

Use a project-local micromamba environment. This does not require installing
Python globally.

```powershell
micromamba create -y -p ".mamba\env" -f environment.yml
```

Run Python through the helper:

```powershell
.\scripts\run_python.ps1 --version
```

```powershell
$env:HF_TOKEN="hf_xxx"

.\scripts\run_python.ps1 `
  scripts\extract_gpic_captions.py `
  --split val `
  --start 0 `
  --end 1 `
  --max-records-per-shard 5 `
  --output-dir data\gpic_captions_test `
  --overwrite
```

For a dry run that only prints shard URLs:

```powershell
.\scripts\run_python.ps1 `
  scripts\extract_gpic_captions.py `
  --split val `
  --start 0 `
  --end 2 `
  --dry-run
```

## Quote Text Retokenization

따옴표 안의 문구는 placeholder로 바꾸지 않는다. 원문 caption을 유지한 채
spaCy tokenizer 직후 Retokenizer로 `"..."` span 자체를 하나의 token으로
merge하고, quote 원문은 별도 metadata로 보존한다.

```text
raw:
A poster reads "BANG GOES THE KNIGHTHOOD" on the wall.

parsed caption:
A poster reads "BANG GOES THE KNIGHTHOOD" on the wall.

merged quote token:
"BANG GOES THE KNIGHTHOOD"
```

각 quote는 caption 내부 local id인 `quote_id`와 dataset 전체에서 연결하기 위한
`global_quote_id = caption_id + ":" + quote_id`를 함께 가진다. 원문 복구에는
`text_raw`, 원문 위치 확인과 parser output 연결에는 `char_start`/`char_end`를
사용한다. 기존 CLI 호환 때문에 옵션 이름은 `--mask-quotes`이지만, 현재 동작은
raw quote span retokenization이다.

샘플 parse 리포트:

```powershell
.\scripts\run_python.ps1 `
  scripts\inspect_spacy_parse.py `
  --input data\gpic_captions_test\val\gpic_val_00000.jsonl.gz `
  --output reports\spacy_parse_sample_20_trf_quote_masked.md `
  --max-records 20 `
  --model en_core_web_trf `
  --mask-quotes
```

## Notes

Do not commit `data/`, `tmp/`, Hugging Face tokens, or generated large files.
