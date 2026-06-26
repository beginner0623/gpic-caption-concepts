from __future__ import annotations

import argparse
import gzip
import json
import time
from itertools import cycle, islice
from pathlib import Path
from typing import Iterable

import spacy

from benchmark_spacy_parse import (
    disable_cupy_reduction_accelerators,
    patch_cupy_nvrtc_include,
)
from hyphen_span_retokenizer import ensure_hyphen_span_merger
from inspect_spacy_parse import caption_shape
from object_mwe_retokenizer import DEFAULT_OBJECT_MWE_LEXICON, ensure_object_mwe_merger
from quote_masking import collect_quoted_text
from quote_retokenizer import ensure_raw_quote_merger
from raw_concept_extractor import extract_raw_concepts
from tag_list_parser import is_tag_list_row, parse_tag_list


def open_text(path: Path):
    if path.suffix == ".gz":
        return gzip.open(path, "rt", encoding="utf-8")
    return path.open("rt", encoding="utf-8")


def iter_rows(path: Path, max_input_records: int | None = None) -> Iterable[dict]:
    count = 0
    with open_text(path) as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if row.get("caption"):
                yield row
                count += 1
                if max_input_records is not None and count >= max_input_records:
                    break


def expand_rows(rows: list[dict], target_records: int | None) -> list[dict]:
    if not rows:
        raise ValueError("No rows found in input file.")
    if target_records is None or target_records <= len(rows):
        return rows if target_records is None else rows[:target_records]
    return list(islice(cycle(rows), target_records))


def round_float(value: float) -> float:
    return round(value, 4)


def row_caption_id(row: dict, index: int) -> str:
    return str(row.get("caption_id") or row.get("id") or index)


def consume_rows(
    nlp,
    rows: list[dict],
    *,
    mask_quotes: bool,
    parse_tag_lists: bool,
    serialize_json: bool,
) -> dict[str, int]:
    counts = {
        "records": 0,
        "sentence_records": 0,
        "tag_list_records": 0,
        "quote_mentions": 0,
        "concept_mentions": 0,
        "edges": 0,
        "skipped_edges": 0,
        "json_bytes": 0,
    }

    for index, row in enumerate(rows, 1):
        caption = row.get("caption", "")
        caption_id = row_caption_id(row, index)
        quote_result = collect_quoted_text(caption, caption_id=caption_id) if mask_quotes else None
        quote_mentions = [mention.to_dict() for mention in quote_result.mentions] if quote_result else []

        if parse_tag_lists and is_tag_list_row(row, caption):
            tag_result = parse_tag_list(nlp, caption)
            parse_path = "tag_list"
            mentions = [mention.to_dict() for mention in tag_result.concept_mentions]
            edges = [edge.to_dict() for edge in tag_result.edges]
            skipped_edges = []
            counts["tag_list_records"] += 1
        else:
            doc = nlp(caption)
            raw_result = extract_raw_concepts(doc)
            parse_path = "sentence"
            mentions = [mention.to_dict() for mention in raw_result.concept_mentions]
            edges = [edge.to_dict() for edge in raw_result.edges]
            skipped_edges = raw_result.skipped_edges
            counts["sentence_records"] += 1

        counts["records"] += 1
        counts["quote_mentions"] += len(quote_mentions)
        counts["concept_mentions"] += len(mentions)
        counts["edges"] += len(edges)
        counts["skipped_edges"] += len(skipped_edges)

        if serialize_json:
            record = {
                "row_index": index,
                "caption_id": caption_id,
                "caption_type": row.get("caption_type"),
                "caption_shape": caption_shape(caption),
                "parse_path": parse_path,
                "caption": caption,
                "quote_mentions": quote_mentions,
                "concept_mentions": mentions,
                "edges": edges,
                "skipped_edges": skipped_edges,
            }
            counts["json_bytes"] += len(json.dumps(record, ensure_ascii=False))

    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description="Benchmark current row-by-row raw concept extraction throughput.")
    parser.add_argument("--input", required=True, type=Path, help="Input GPIC caption JSONL or JSONL.GZ")
    parser.add_argument("--model", default="en_core_web_trf")
    parser.add_argument("--max-input-records", type=int, default=None)
    parser.add_argument("--target-records", type=int, default=None)
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
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    read_start = time.perf_counter()
    source_rows = list(iter_rows(args.input, args.max_input_records))
    read_seconds = time.perf_counter() - read_start
    rows = expand_rows(source_rows, args.target_records)

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
    load_seconds = time.perf_counter() - load_start

    warmup_count = min(args.warmup_records, len(rows))
    if warmup_count:
        consume_rows(
            nlp,
            rows[:warmup_count],
            mask_quotes=args.mask_quotes,
            parse_tag_lists=args.parse_tag_lists,
            serialize_json=args.serialize_json,
        )

    run_start = time.perf_counter()
    counts = consume_rows(
        nlp,
        rows,
        mask_quotes=args.mask_quotes,
        parse_tag_lists=args.parse_tag_lists,
        serialize_json=args.serialize_json,
    )
    run_seconds = time.perf_counter() - run_start
    docs_per_second = counts["records"] / run_seconds if run_seconds > 0 else 0.0
    estimated_100m_seconds = 100_000_000 / docs_per_second if docs_per_second > 0 else 0.0

    result = {
        "input": str(args.input),
        "model": args.model,
        "source_input_records": len(source_rows),
        "target_records": len(rows),
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
        "pipe_names": nlp.pipe_names,
        "read_seconds": round_float(read_seconds),
        "model_load_seconds": round_float(load_seconds),
        "run_seconds": round_float(run_seconds),
        "docs_per_second_run_only": round_float(docs_per_second),
        "estimated_100m_hours_run_only": round_float(estimated_100m_seconds / 3600),
        "estimated_100m_days_run_only": round_float(estimated_100m_seconds / 86400),
        **counts,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())