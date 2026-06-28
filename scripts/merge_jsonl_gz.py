from __future__ import annotations

import argparse
import gzip
from pathlib import Path


def open_input(path: Path):
    if path.suffix == ".gz":
        return gzip.open(path, "rt", encoding="utf-8")
    return path.open("r", encoding="utf-8")


def open_output(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".gz":
        return gzip.open(path, "wt", encoding="utf-8", newline="\n")
    return path.open("w", encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Merge JSONL/JSONL.GZ shards into one JSONL/JSONL.GZ file.")
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument("--pattern", default="*.jsonl.gz")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-records", type=int, default=None)
    args = parser.parse_args()

    paths = sorted(args.input_dir.glob(args.pattern))
    records = 0
    with open_output(args.output) as out:
        for path in paths:
            with open_input(path) as handle:
                for line in handle:
                    line = line.rstrip("\n")
                    if not line:
                        continue
                    out.write(line + "\n")
                    records += 1
                    if args.max_records is not None and records >= args.max_records:
                        print(f"merged {records} records from {len(paths)} candidate shards into {args.output}")
                        return 0
    print(f"merged {records} records from {len(paths)} shards into {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
