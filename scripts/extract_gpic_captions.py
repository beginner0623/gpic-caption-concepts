#!/usr/bin/env python
"""Extract caption metadata JSON files from GPIC tar shards.

GPIC is distributed as tar shards containing alternating JSON/image records.
This script streams each tar shard, writes only JSON metadata rows to JSONL,
and does not save images.

Access notes:
- The Hugging Face dataset is gated. Accept the terms in the browser first.
- Set HF_TOKEN or pass --hf-token so HTTP downloads can authenticate.
"""

from __future__ import annotations

import argparse
import gzip
import json
import os
import sys
import tarfile
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Iterable


REPO_ID = "stanford-vision-lab/gpic"
SHARD_COUNTS = {
    "train": 8000,
    "val": 32,
    "test": 128,
}


def shard_name(split: str, index: int) -> str:
    return f"gpic_{split}_{index:05d}.tar"


def shard_url(repo_id: str, split: str, index: int) -> str:
    filename = shard_name(split, index)
    return f"https://huggingface.co/datasets/{repo_id}/resolve/main/{split}/{filename}"


def iter_shard_indices(split: str, start: int, end: int | None) -> range:
    total = SHARD_COUNTS[split]
    if end is None:
        end = total
    if start < 0 or end < start or end > total:
        raise ValueError(f"Invalid shard range: split={split}, start={start}, end={end}, total={total}")
    return range(start, end)


def open_text_output(path: Path, compress: bool):
    path.parent.mkdir(parents=True, exist_ok=True)
    if compress:
        return gzip.open(path, "wt", encoding="utf-8", newline="\n")
    return path.open("w", encoding="utf-8", newline="\n")


def make_request(url: str, token: str | None, timeout: int):
    headers = {"User-Agent": "gpic-caption-extractor/0.1"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request, timeout=timeout)


def normalize_record(
    obj: dict,
    *,
    split_name: str,
    shard_index: int,
    shard_member: str,
    record_index: int,
    keep_all_metadata: bool,
) -> dict:
    if keep_all_metadata:
        row = dict(obj)
    else:
        row = {
            "key": obj.get("key"),
            "caption": obj.get("caption"),
            "caption_type": obj.get("caption_type"),
            "dataset_split": obj.get("split"),
            "img_width": obj.get("img_width"),
            "img_height": obj.get("img_height"),
            "license": obj.get("license"),
            "license_url": obj.get("license_url"),
        }
    row["_gpic_split_dir"] = split_name
    row["_gpic_shard_index"] = shard_index
    row["_gpic_shard_member"] = shard_member
    row["_gpic_record_index"] = record_index
    return row


def extract_one_shard(
    *,
    repo_id: str,
    split_name: str,
    shard_index: int,
    output_dir: Path,
    token: str | None,
    compress: bool,
    overwrite: bool,
    timeout: int,
    max_records: int | None,
    keep_all_metadata: bool,
) -> dict:
    suffix = ".jsonl.gz" if compress else ".jsonl"
    out_path = output_dir / split_name / f"gpic_{split_name}_{shard_index:05d}{suffix}"
    done_path = out_path.with_suffix(out_path.suffix + ".done")

    if done_path.exists() and out_path.exists() and not overwrite:
        return {
            "split": split_name,
            "shard": shard_index,
            "status": "skipped",
            "records": None,
            "output": str(out_path),
        }

    tmp_path = out_path.with_suffix(out_path.suffix + ".tmp")
    url = shard_url(repo_id, split_name, shard_index)
    start_time = time.time()
    records = 0

    try:
        with make_request(url, token, timeout) as response:
            # Streaming mode lets tarfile iterate members without materializing the tar.
            with tarfile.open(fileobj=response, mode="r|*") as tar:
                with open_text_output(tmp_path, compress) as fout:
                    for member in tar:
                        if not member.isfile() or not member.name.endswith(".json"):
                            continue
                        extracted = tar.extractfile(member)
                        if extracted is None:
                            continue
                        raw = extracted.read()
                        obj = json.loads(raw.decode("utf-8"))
                        row = normalize_record(
                            obj,
                            split_name=split_name,
                            shard_index=shard_index,
                            shard_member=member.name,
                            record_index=records,
                            keep_all_metadata=keep_all_metadata,
                        )
                        fout.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
                        records += 1
                        if max_records is not None and records >= max_records:
                            break
    except urllib.error.HTTPError as exc:
        if exc.code in (401, 403):
            raise RuntimeError(
                f"HTTP {exc.code} for {url}. Accept the GPIC dataset terms on Hugging Face "
                "and provide a valid HF_TOKEN."
            ) from exc
        raise

    tmp_path.replace(out_path)
    done_path.write_text(
        json.dumps(
            {
                "split": split_name,
                "shard": shard_index,
                "records": records,
                "seconds": round(time.time() - start_time, 3),
                "url": url,
                "output": str(out_path),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    return {
        "split": split_name,
        "shard": shard_index,
        "status": "ok",
        "records": records,
        "output": str(out_path),
        "seconds": round(time.time() - start_time, 3),
    }


def parse_args(argv: Iterable[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Stream GPIC tar shards and extract only caption JSON rows.")
    parser.add_argument("--repo-id", default=REPO_ID)
    parser.add_argument("--split", choices=sorted(SHARD_COUNTS), default="val")
    parser.add_argument("--start", type=int, default=0, help="First shard index, inclusive.")
    parser.add_argument("--end", type=int, default=None, help="Last shard index, exclusive.")
    parser.add_argument("--output-dir", default="data/gpic_captions")
    parser.add_argument("--hf-token", default=os.environ.get("HF_TOKEN"))
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--max-records-per-shard", type=int, default=None)
    parser.add_argument("--no-compress", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--keep-all-metadata", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(list(argv))


def main(argv: Iterable[str] = sys.argv[1:]) -> int:
    args = parse_args(argv)
    output_dir = Path(args.output_dir)
    shard_indices = list(iter_shard_indices(args.split, args.start, args.end))

    if args.dry_run:
        for idx in shard_indices:
            print(shard_url(args.repo_id, args.split, idx))
        return 0

    if not args.hf_token:
        print(
            "WARNING: no HF token provided. If the dataset is gated for your account, "
            "set HF_TOKEN or pass --hf-token.",
            file=sys.stderr,
        )

    kwargs = {
        "repo_id": args.repo_id,
        "split_name": args.split,
        "output_dir": output_dir,
        "token": args.hf_token,
        "compress": not args.no_compress,
        "overwrite": args.overwrite,
        "timeout": args.timeout,
        "max_records": args.max_records_per_shard,
        "keep_all_metadata": args.keep_all_metadata,
    }

    total_records = 0
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = [
            executor.submit(extract_one_shard, shard_index=idx, **kwargs)
            for idx in shard_indices
        ]
        for future in as_completed(futures):
            result = future.result()
            if result["records"]:
                total_records += result["records"]
            print(json.dumps(result, ensure_ascii=False), flush=True)

    print(json.dumps({"status": "done", "shards": len(shard_indices), "records": total_records}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

