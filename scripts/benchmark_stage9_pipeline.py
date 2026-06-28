from __future__ import annotations

import argparse
from collections import Counter
import json
import time
from pathlib import Path

import spacy

from benchmark_raw_concepts import expand_rows, iter_rows
from benchmark_spacy_parse import (
    disable_cupy_reduction_accelerators,
    patch_cupy_nvrtc_include,
)
from canonicalize_raw_concepts import canonicalize_record
from extract_raw_concepts import batched, process_indexed_row_batch
from hyphen_span_retokenizer import ensure_hyphen_span_merger
from object_mwe_retokenizer import DEFAULT_OBJECT_MWE_LEXICON, ensure_object_mwe_merger
from phrasal_action_lexicon import DEFAULT_PHRASAL_ACTION_LEXICON, load_phrasal_action_lexicon
from quote_retokenizer import ensure_raw_quote_merger
from stage9_lexical_canonicalizer import load_stage9_canonical_lexicon


def round_float(value: float) -> float:
    return round(value, 4)


def consume_stage9_rows(
    nlp,
    indexed_rows: list[tuple[int, dict]],
    *,
    mask_quotes: bool,
    parse_tag_lists: bool,
    batch_size: int,
    n_process: int,
    phrasal_lexicon,
    stage9_lexicon,
    serialize_json: bool,
) -> dict[str, int]:
    counts = Counter()
    for row_batch in batched(indexed_rows, batch_size):
        raw_records = process_indexed_row_batch(
            nlp,
            row_batch,
            mask_quotes=mask_quotes,
            parse_tag_lists=parse_tag_lists,
            batch_size=batch_size,
            n_process=n_process,
        )
        for raw_record in raw_records:
            record = canonicalize_record(
                raw_record,
                phrasal_lexicon=phrasal_lexicon,
                stage9_lexicon=stage9_lexicon,
            )
            stage9 = record["stage9"]
            counts["records"] += 1
            counts[f"parse_path:{record['parse_path']}"] += 1
            counts["quote_mentions"] += len(record["quote_mentions"])
            counts["raw_concept_mentions"] += len(record["concept_mentions"])
            counts["raw_edges"] += len(record["edges"])
            counts["raw_skipped_edges"] += len(record["skipped_edges"])
            counts["canonical_entities"] += len(stage9["canonical_entities"])
            counts["entity_links"] += len(stage9["entity_links"])
            counts["canonical_events"] += len(stage9["canonical_events"])
            counts["canonical_relations"] += len(stage9["canonical_relations"])
            counts["canonical_facts"] += len(stage9["canonical_facts"])
            for fact in stage9["canonical_facts"]:
                counts[f"fact_type:{fact['fact_type']}"] += 1
                if fact.get("count_eligible"):
                    counts["count_eligible_facts"] += 1
            if serialize_json:
                counts["json_bytes"] += len(json.dumps(record, ensure_ascii=False))
    return dict(counts)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Benchmark end-to-end Stage 8 raw extraction + Stage 9 canonical parent/fact throughput."
    )
    parser.add_argument("--input", required=True, type=Path, help="Input GPIC caption JSONL or JSONL.GZ")
    parser.add_argument("--model", default="en_core_web_trf")
    parser.add_argument("--max-input-records", type=int, default=None)
    parser.add_argument("--target-records", type=int, default=None)
    parser.add_argument("--batch-size", type=int, default=256)
    parser.add_argument("--n-process", type=int, default=1)
    parser.add_argument("--warmup-records", type=int, default=100)
    parser.add_argument("--gpu-id", type=int, default=None)
    parser.add_argument("--prefer-gpu", action="store_true")
    parser.add_argument("--cupy-include-dir", type=Path, default=None)
    parser.add_argument("--disable-cupy-reduction-accelerators", action="store_true")
    parser.add_argument("--mask-quotes", action="store_true")
    parser.add_argument("--parse-tag-lists", action="store_true")
    parser.add_argument("--merge-object-mwes", action="store_true")
    parser.add_argument("--merge-hyphen-spans", action="store_true")
    parser.add_argument("--serialize-json", action="store_true")
    parser.add_argument("--object-mwe-lexicon", type=Path, default=DEFAULT_OBJECT_MWE_LEXICON)
    parser.add_argument("--phrasal-action-lexicon", type=Path, default=DEFAULT_PHRASAL_ACTION_LEXICON)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    read_start = time.perf_counter()
    source_rows = list(iter_rows(args.input, args.max_input_records))
    read_seconds = time.perf_counter() - read_start
    rows = expand_rows(source_rows, args.target_records)
    indexed_rows = list(enumerate(rows, 1))

    if args.cupy_include_dir is not None:
        patch_cupy_nvrtc_include(args.cupy_include_dir)
    if args.disable_cupy_reduction_accelerators:
        disable_cupy_reduction_accelerators()

    gpu_enabled = False
    if args.gpu_id is not None:
        spacy.require_gpu(args.gpu_id)
        gpu_enabled = True
    elif args.prefer_gpu:
        gpu_enabled = spacy.prefer_gpu()

    load_start = time.perf_counter()
    nlp = spacy.load(args.model)
    if args.mask_quotes:
        ensure_raw_quote_merger(nlp)
    if args.merge_object_mwes:
        ensure_object_mwe_merger(nlp, args.object_mwe_lexicon)
    if args.merge_hyphen_spans:
        ensure_hyphen_span_merger(nlp)
    phrasal_lexicon = load_phrasal_action_lexicon(args.phrasal_action_lexicon)
    stage9_lexicon = load_stage9_canonical_lexicon()
    load_seconds = time.perf_counter() - load_start

    warmup_count = min(args.warmup_records, len(indexed_rows))
    if warmup_count:
        consume_stage9_rows(
            nlp,
            indexed_rows[:warmup_count],
            mask_quotes=args.mask_quotes,
            parse_tag_lists=args.parse_tag_lists,
            batch_size=args.batch_size,
            n_process=args.n_process,
            phrasal_lexicon=phrasal_lexicon,
            stage9_lexicon=stage9_lexicon,
            serialize_json=args.serialize_json,
        )

    run_start = time.perf_counter()
    counts = consume_stage9_rows(
        nlp,
        indexed_rows,
        mask_quotes=args.mask_quotes,
        parse_tag_lists=args.parse_tag_lists,
        batch_size=args.batch_size,
        n_process=args.n_process,
        phrasal_lexicon=phrasal_lexicon,
        stage9_lexicon=stage9_lexicon,
        serialize_json=args.serialize_json,
    )
    run_seconds = time.perf_counter() - run_start

    docs_per_second = counts["records"] / run_seconds if run_seconds > 0 else 0.0
    estimated_100m_seconds = 100_000_000 / docs_per_second if docs_per_second > 0 else 0.0
    required_for_100m_3days = 100_000_000 / (3 * 24 * 3600)
    linear_workers_for_3days = required_for_100m_3days / docs_per_second if docs_per_second > 0 else 0.0

    result = {
        "input": str(args.input),
        "model": args.model,
        "source_input_records": len(source_rows),
        "target_records": len(rows),
        "batch_size": args.batch_size,
        "n_process": args.n_process,
        "warmup_records": warmup_count,
        "gpu_id": args.gpu_id,
        "prefer_gpu": args.prefer_gpu,
        "gpu_enabled": gpu_enabled,
        "cupy_include_dir": str(args.cupy_include_dir) if args.cupy_include_dir is not None else None,
        "disable_cupy_reduction_accelerators": args.disable_cupy_reduction_accelerators,
        "mask_quotes": args.mask_quotes,
        "parse_tag_lists": args.parse_tag_lists,
        "merge_object_mwes": args.merge_object_mwes,
        "merge_hyphen_spans": args.merge_hyphen_spans,
        "serialize_json": args.serialize_json,
        "object_mwe_lexicon": str(args.object_mwe_lexicon),
        "phrasal_action_lexicon": str(args.phrasal_action_lexicon),
        "pipe_names": nlp.pipe_names,
        "read_seconds": round_float(read_seconds),
        "model_and_lexicon_load_seconds": round_float(load_seconds),
        "run_seconds": round_float(run_seconds),
        "docs_per_second_run_only": round_float(docs_per_second),
        "estimated_100m_hours_run_only": round_float(estimated_100m_seconds / 3600),
        "estimated_100m_days_run_only": round_float(estimated_100m_seconds / 86400),
        "required_docs_per_second_for_100m_3days": round_float(required_for_100m_3days),
        "linear_workers_needed_for_100m_3days_at_this_speed": round_float(linear_workers_for_3days),
        **counts,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
