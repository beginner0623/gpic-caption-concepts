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

## Quote Text Masking

따옴표 안의 문구는 일반 object/action/relation으로 parse하지 않고
`quoted text`로 masking한 뒤 별도 metadata로 보존한다.

```text
raw:
A poster reads "BANG GOES THE KNIGHTHOOD" on the wall.

parsed caption:
A poster reads quoted text on the wall.
```

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

placeholder를 바꿔 비교하고 싶으면 `--quote-placeholder "visible text"`처럼 지정한다.

## Notes

Do not commit `data/`, `tmp/`, Hugging Face tokens, or generated large files.
