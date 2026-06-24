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

```powershell
$env:HF_TOKEN="hf_xxx"

& 'C:\Users\rlath\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' `
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
& 'C:\Users\rlath\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' `
  scripts\extract_gpic_captions.py `
  --split val `
  --start 0 `
  --end 2 `
  --dry-run
```

## Notes

Do not commit `data/`, `tmp/`, Hugging Face tokens, or generated large files.

