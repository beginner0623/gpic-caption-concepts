from __future__ import annotations

import csv
from collections import OrderedDict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
LEXICON_DIR = ROOT / "resources" / "lexicons"

SPECS = [
    (
        LEXICON_DIR / "stage9_object_canonical_seed.tsv",
        LEXICON_DIR / "stage9_object_synonym_seed.tsv",
        LEXICON_DIR / "stage9_object_parent_seed.tsv",
        "entity",
    ),
    (
        LEXICON_DIR / "stage9_action_canonical_seed.tsv",
        LEXICON_DIR / "stage9_action_synonym_seed.tsv",
        LEXICON_DIR / "stage9_action_parent_seed.tsv",
        "action",
    ),
]


def norm_space(value: object) -> str:
    return " ".join(str(value or "").strip().lower().replace("_", " ").split())


def norm_key(value: object) -> str:
    return norm_space(value).replace(" ", "_")


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def split_seed(input_path: Path, synonym_path: Path, parent_path: Path, default_count_channel: str) -> tuple[int, int]:
    rows = read_tsv(input_path)
    synonym_rows: list[dict[str, str]] = []
    parent_rows_by_canonical: OrderedDict[str, dict[str, str]] = OrderedDict()

    for row in rows:
        term = norm_key(row.get("term", ""))
        canonical = norm_key(row.get("canonical") or term)
        if not term or not canonical:
            continue
        count_channel = norm_key(row.get("count_channel") or default_count_channel)
        confidence = norm_key(row.get("confidence") or "medium")
        source = row.get("source", "").strip() or input_path.name
        notes = row.get("notes", "").strip()

        if term != canonical:
            synonym_rows.append(
                {
                    "term": term,
                    "canonical": canonical,
                    "count_channel": count_channel,
                    "confidence": confidence,
                    "source": f"{source}:synonym_seed",
                    "notes": notes,
                }
            )

        parent_chain = row.get("parent_chain", "").strip()
        if parent_chain and canonical not in parent_rows_by_canonical:
            parent_rows_by_canonical[canonical] = {
                "term": canonical,
                "parent_chain": parent_chain,
                "count_channel": count_channel,
                "confidence": confidence,
                "source": f"{source}:parent_seed",
                "notes": notes,
            }

    write_tsv(
        synonym_path,
        synonym_rows,
        ["term", "canonical", "count_channel", "confidence", "source", "notes"],
    )
    write_tsv(
        parent_path,
        list(parent_rows_by_canonical.values()),
        ["term", "parent_chain", "count_channel", "confidence", "source", "notes"],
    )
    return len(synonym_rows), len(parent_rows_by_canonical)


def main() -> int:
    for input_path, synonym_path, parent_path, default_count_channel in SPECS:
        synonym_count, parent_count = split_seed(input_path, synonym_path, parent_path, default_count_channel)
        print(f"{input_path.name}: synonym={synonym_count} parent={parent_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
