from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


CORE_ATTRIBUTE_ROLES = {
    "color_attribute",
    "material_attribute",
    "size_attribute",
    "shape_attribute",
    "pattern_attribute",
    "texture_attribute",
    "brightness_attribute",
    "condition_attribute",
    "state_attribute",
    "pose_attribute",
    "weather_attribute",
}


ROLE_PRIORITY = [
    "color_attribute",
    "material_attribute",
    "size_attribute",
    "shape_attribute",
    "pattern_attribute",
    "texture_attribute",
    "brightness_attribute",
    "condition_attribute",
    "state_attribute",
    "pose_attribute",
    "weather_attribute",
]


FIELDNAMES = [
    "term",
    "canonical",
    "roles",
    "primary_role",
    "sources",
    "source_types",
    "parent_types",
    "confidence",
    "source_count",
    "entry_count",
    "provenance",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] = FIELDNAMES) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def split_pipe(text: str) -> list[str]:
    return [item for item in str(text).split("|") if item]


def confidence_rank(confidence: str) -> int:
    return {"high": 3, "medium": 2, "low": 1}.get(confidence, 0)


def choose_primary_role(roles: set[str]) -> str:
    for role in ROLE_PRIORITY:
        if role in roles:
            return role
    return sorted(roles)[0] if roles else ""


def add_grouped(
    grouped: dict[str, list[dict[str, Any]]],
    *,
    term: str,
    canonical: str,
    roles: list[str],
    sources: list[str],
    source_types: list[str],
    parent_types: list[str],
    confidence: str,
    entry_count: int,
    provenance: str,
) -> None:
    if not term or not roles:
        return
    grouped[term].append(
        {
            "term": term,
            "canonical": canonical or term,
            "roles": roles,
            "sources": sources,
            "source_types": source_types,
            "parent_types": parent_types,
            "confidence": confidence,
            "entry_count": entry_count,
            "provenance": provenance,
        }
    )


def merge_grouped(grouped: dict[str, list[dict[str, Any]]], *, core_only: bool = False) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for term in sorted(grouped):
        items = grouped[term]
        roles = {role for item in items for role in item["roles"] if role and role != "attribute"}
        if core_only:
            roles = roles & CORE_ATTRIBUTE_ROLES
        if not roles:
            continue
        sources = sorted({source for item in items for source in item["sources"] if source})
        source_types = sorted({source_type for item in items for source_type in item["source_types"] if source_type})
        parent_types = sorted({parent_type for item in items for parent_type in item["parent_types"] if parent_type})
        confidence = max((item["confidence"] for item in items), key=confidence_rank)
        entry_count = sum(int(item["entry_count"]) for item in items)
        provenance = sorted({item["provenance"] for item in items if item["provenance"]})
        rows.append(
            {
                "term": term,
                "canonical": term,
                "roles": "|".join(sorted(roles)),
                "primary_role": choose_primary_role(roles),
                "sources": "|".join(sources),
                "source_types": "|".join(source_types),
                "parent_types": "|".join(parent_types),
                "confidence": confidence,
                "source_count": str(len(sources)),
                "entry_count": str(entry_count),
                "provenance": "|".join(provenance),
            }
        )
    return rows


def build_candidates(base_rows: list[dict[str, str]], coco_rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in base_rows:
        add_grouped(
            grouped,
            term=row["term"],
            canonical=row.get("canonical", row["term"]),
            roles=split_pipe(row.get("roles", "")),
            sources=split_pipe(row.get("sources", "")),
            source_types=split_pipe(row.get("source_types", "")),
            parent_types=split_pipe(row.get("parent_types", "")),
            confidence=row.get("confidence", ""),
            entry_count=int(row.get("entry_count") or 1),
            provenance="modifier_attributes_clean",
        )

    for row in coco_rows:
        if row.get("confidence") != "high":
            continue
        add_grouped(
            grouped,
            term=row["term"],
            canonical=row["term"],
            roles=split_pipe(row.get("assigned_roles", "")),
            sources=["coco_attributes"],
            source_types=["object_attribute"],
            parent_types=[row.get("classification_status", "")],
            confidence="high",
            entry_count=1,
            provenance="coco_high_typed",
        )

    all_typed = merge_grouped(grouped, core_only=False)
    core_typed = merge_grouped(grouped, core_only=True)
    return all_typed, core_typed


def role_counts(rows: list[dict[str, str]]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for row in rows:
        for role in split_pipe(row["roles"]):
            counts[role] += 1
    return counts


def write_report(path: Path, all_typed: list[dict[str, str]], core_typed: list[dict[str, str]]) -> None:
    all_roles = role_counts(all_typed)
    core_roles = role_counts(core_typed)
    lines = [
        "# Attribute Clean Typed Candidate Summary",
        "",
        "기존 typed clean lexicon에 COCO Attributes high-confidence typed 항목을 합쳐 만든 최종 clean typed 후보입니다.",
        "",
        "## Output Files",
        "",
        "- `resources/lexicons/attribute_clean_typed_candidate.tsv`: 기존 clean + COCO high 전체 role 후보",
        "- `resources/lexicons/attribute_clean_core_typed_candidate.tsv`: 11개 core modifier role만 남긴 1차 parser용 후보",
        "",
        "## Counts",
        "",
        "| file | terms | role types |",
        "|---|---:|---:|",
        f"| attribute_clean_typed_candidate.tsv | {len(all_typed)} | {len(all_roles)} |",
        f"| attribute_clean_core_typed_candidate.tsv | {len(core_typed)} | {len(core_roles)} |",
        "",
        "## Core Role Counts",
        "",
        "| role | terms |",
        "|---|---:|",
    ]
    for role in ROLE_PRIORITY:
        lines.append(f"| {role} | {core_roles.get(role, 0)} |")
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- COCO `confidence=medium` 항목은 여기 넣지 않았습니다.",
            "- `attribute_clean_core_typed_candidate.tsv`는 색/재질/크기/형태/패턴/질감/밝기/상태/포즈/날씨 등 11개 core modifier role만 포함합니다.",
            "- `attribute_clean_typed_candidate.tsv`는 activity/fashion/functional 같은 확장 role도 보존한 audit용 후보입니다.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build final clean typed attribute candidates from base clean lexicon and COCO high-confidence attributes.")
    parser.add_argument("--base-clean", type=Path, default=Path("resources/lexicons/modifier_attributes_clean.tsv"))
    parser.add_argument("--coco-typed", type=Path, default=Path("resources/lexicons/coco_attributes_clean_typed.tsv"))
    parser.add_argument("--output-dir", type=Path, default=Path("resources/lexicons"))
    parser.add_argument("--report", type=Path, default=Path("reports/attribute_clean_candidate_summary.md"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base_rows = read_tsv(args.base_clean)
    coco_rows = read_tsv(args.coco_typed)
    all_typed, core_typed = build_candidates(base_rows, coco_rows)
    write_tsv(args.output_dir / "attribute_clean_typed_candidate.tsv", all_typed)
    write_tsv(args.output_dir / "attribute_clean_core_typed_candidate.tsv", core_typed)
    write_report(args.report, all_typed, core_typed)
    print(f"attribute_clean_typed_candidate terms: {len(all_typed)}")
    print(f"attribute_clean_core_typed_candidate terms: {len(core_typed)}")
    print(f"wrote: {args.output_dir / 'attribute_clean_typed_candidate.tsv'}")
    print(f"wrote: {args.output_dir / 'attribute_clean_core_typed_candidate.tsv'}")
    print(f"wrote: {args.report}")


if __name__ == "__main__":
    main()
