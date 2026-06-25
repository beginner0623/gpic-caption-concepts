from __future__ import annotations

import argparse
import gzip
import json
import time
from itertools import cycle, islice
from pathlib import Path
from typing import Iterable

import spacy

from hyphen_span_retokenizer import ensure_hyphen_span_merger
from object_mwe_retokenizer import DEFAULT_OBJECT_MWE_LEXICON, ensure_object_mwe_merger
from quote_retokenizer import ensure_raw_quote_merger


def open_text(path: Path):
    if path.suffix == ".gz":
        return gzip.open(path, "rt", encoding="utf-8")
    return path.open("rt", encoding="utf-8")


def iter_captions(path: Path, max_input_records: int | None = None) -> Iterable[str]:
    count = 0
    with open_text(path) as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            caption = row.get("caption")
            if caption:
                yield caption
                count += 1
                if max_input_records is not None and count >= max_input_records:
                    break


def expand_captions(captions: list[str], target_records: int | None) -> list[str]:
    if not captions:
        raise ValueError("No captions found in input file.")
    if target_records is None or target_records <= len(captions):
        return captions if target_records is None else captions[:target_records]
    return list(islice(cycle(captions), target_records))


def consume_docs(nlp, captions: list[str], batch_size: int, n_process: int) -> dict[str, int]:
    docs = 0
    tokens = 0
    sentences = 0
    noun_chunks = 0

    for doc in nlp.pipe(captions, batch_size=batch_size, n_process=n_process):
        docs += 1
        tokens += len(doc)
        sentences += sum(1 for _ in doc.sents)
        noun_chunks += sum(1 for _ in doc.noun_chunks)

    return {
        "docs": docs,
        "tokens": tokens,
        "sentences": sentences,
        "noun_chunks": noun_chunks,
    }


def round_float(value: float) -> float:
    return round(value, 4)


def patch_cupy_nvrtc_include(include_dir: Path) -> None:
    if not include_dir.exists():
        raise FileNotFoundError(f"CuPy include dir does not exist: {include_dir}")

    import cupy
    from cupy.cuda import compiler

    include_option = f"-I{include_dir}"
    original_compile = compiler._compile_with_cache_cuda

    def compile_with_include(
        source,
        options=(),
        arch=None,
        extra_source=None,
        backend="nvrtc",
        enable_cooperative_groups=False,
        name_expressions=None,
        log_stream=None,
        cache_in_memory=False,
        jitify=False,
        to_ltoir=False,
    ):
        patched_options = tuple(options)
        if include_option not in patched_options:
            patched_options = (*patched_options, include_option)
        return original_compile(
            source,
            patched_options,
            arch,
            extra_source,
            backend,
            enable_cooperative_groups,
            name_expressions,
            log_stream,
            cache_in_memory,
            jitify,
            to_ltoir,
        )

    compiler._compile_with_cache_cuda = compile_with_include
    cupy.cuda.runtime.getDeviceCount()


def disable_cupy_reduction_accelerators() -> None:
    from cupy._core import _accelerator

    _accelerator.set_reduction_accelerators([])


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Benchmark spaCy token/POS/lemma/dependency/noun-chunk parsing throughput."
    )
    parser.add_argument("--input", required=True, type=Path, help="Input GPIC caption JSONL or JSONL.GZ")
    parser.add_argument("--model", default="en_core_web_sm")
    parser.add_argument("--max-input-records", type=int, default=None)
    parser.add_argument(
        "--target-records",
        type=int,
        default=None,
        help="Repeat loaded captions up to this count. Useful for parse-only throughput tests.",
    )
    parser.add_argument("--batch-size", type=int, default=512)
    parser.add_argument("--n-process", type=int, default=1)
    parser.add_argument("--warmup-records", type=int, default=100)
    parser.add_argument(
        "--gpu-id",
        type=int,
        default=None,
        help="Require spaCy GPU execution on this device id before loading the model.",
    )
    parser.add_argument(
        "--prefer-gpu",
        action="store_true",
        help="Use GPU if spaCy can enable it, but continue on CPU if it cannot.",
    )
    parser.add_argument(
        "--cupy-include-dir",
        type=Path,
        default=None,
        help="Inject this CuPy include directory into NVRTC compilation options.",
    )
    parser.add_argument(
        "--disable-cupy-reduction-accelerators",
        action="store_true",
        help="Disable CuPy reduction accelerators such as CUB to avoid local NVRTC/MSVC header issues.",
    )
    parser.add_argument(
        "--mask-quotes",
        action="store_true",
        help="Merge raw double-quoted spans before spaCy parsing.",
    )
    parser.add_argument(
        "--merge-object-mwes",
        action="store_true",
        help="Merge high-confidence object noun MWEs before spaCy parsing.",
    )
    parser.add_argument(
        "--merge-hyphen-spans",
        action="store_true",
        help="Merge remaining plain hyphen spans before spaCy parsing without forcing POS.",
    )
    parser.add_argument(
        "--object-mwe-lexicon",
        type=Path,
        default=DEFAULT_OBJECT_MWE_LEXICON,
        help="TSV lexicon used by --merge-object-mwes.",
    )
    parser.add_argument("--output", type=Path, default=None, help="Optional JSON result path")
    args = parser.parse_args()

    start = time.perf_counter()
    captions = list(iter_captions(args.input, args.max_input_records))
    read_seconds = time.perf_counter() - start

    source_records = len(captions)
    captions = expand_captions(captions, args.target_records)

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

    warmup_count = min(args.warmup_records, len(captions))
    if warmup_count:
        consume_docs(nlp, captions[:warmup_count], args.batch_size, args.n_process)

    parse_start = time.perf_counter()
    counts = consume_docs(nlp, captions, args.batch_size, args.n_process)
    parse_seconds = time.perf_counter() - parse_start

    total_seconds = read_seconds + load_seconds + parse_seconds
    docs_per_second = counts["docs"] / parse_seconds if parse_seconds > 0 else 0.0
    tokens_per_second = counts["tokens"] / parse_seconds if parse_seconds > 0 else 0.0
    estimated_100m_seconds = 100_000_000 / docs_per_second if docs_per_second > 0 else 0.0

    result = {
        "input": str(args.input),
        "model": args.model,
        "source_input_records": source_records,
        "target_records": len(captions),
        "batch_size": args.batch_size,
        "n_process": args.n_process,
        "gpu_id": args.gpu_id,
        "prefer_gpu": args.prefer_gpu,
        "gpu_enabled": gpu_enabled,
        "cupy_include_dir": str(args.cupy_include_dir) if args.cupy_include_dir is not None else None,
        "disable_cupy_reduction_accelerators": args.disable_cupy_reduction_accelerators,
        "mask_quotes": args.mask_quotes,
        "merge_object_mwes": args.merge_object_mwes,
        "merge_hyphen_spans": args.merge_hyphen_spans,
        "object_mwe_lexicon": str(args.object_mwe_lexicon),
        "pipe_names": nlp.pipe_names,
        "read_seconds": round_float(read_seconds),
        "model_load_seconds": round_float(load_seconds),
        "parse_seconds": round_float(parse_seconds),
        "total_seconds_including_read_and_model_load": round_float(total_seconds),
        "docs_per_second_parse_only": round_float(docs_per_second),
        "tokens_per_second_parse_only": round_float(tokens_per_second),
        "estimated_100m_hours_parse_only": round_float(estimated_100m_seconds / 3600),
        "estimated_100m_days_parse_only": round_float(estimated_100m_seconds / 86400),
        **counts,
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))

    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
