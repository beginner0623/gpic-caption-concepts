from __future__ import annotations

import argparse
import csv
import io
import json
import os
import re
import urllib.request
import zipfile
from collections import Counter
from html import unescape
from pathlib import Path
from typing import Any

import joblib.numpy_pickle_compat as joblib_compat


COCO_ATTRIBUTES_URL = "https://cs.brown.edu/people/gmpatter/cocottributes/cocottributes_eccv_version.jbl"
VG_ATTRIBUTES_URL = "https://homes.cs.washington.edu/~ranjay/visualgenome/data/dataset/attributes.json.zip"
VG_ATTRIBUTE_SYNSETS_URL = "https://homes.cs.washington.edu/~ranjay/visualgenome/data/dataset/attribute_synsets.json.zip"


def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "gpic-caption-concepts/0.1"})
    with urllib.request.urlopen(req, timeout=300) as response:
        return response.read()


def cached_download(url: str, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.stat().st_size > 0:
        return path
    path.write_bytes(fetch_bytes(url))
    return path


def normalize_term(text: str) -> str:
    text = unescape(str(text)).strip().lower()
    text = text.replace("_", " ")
    text = text.replace("-", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


class Latin1JoblibUnpickler(joblib_compat.ZipNumpyUnpickler):
    """Read old Python 2 joblib files that current joblib rejects by default."""

    def __init__(self, filename: str, file_handle: Any, mmap_mode: str | None = None):
        self._filename = os.path.basename(filename)
        self._dirname = os.path.dirname(filename)
        self.mmap_mode = mmap_mode
        self.file_handle = self._open_pickle(file_handle)
        joblib_compat.Unpickler.__init__(self, self.file_handle, encoding="latin1")
        try:
            import numpy as np
        except ImportError:
            np = None
        self.np = np


def load_python2_joblib(path: Path) -> Any:
    with path.open("rb") as handle:
        return Latin1JoblibUnpickler(str(path), handle).load()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name, "") for name in fieldnames})


def load_existing_terms(clean_path: Path, merged_path: Path) -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    clean_rows = {normalize_term(row["term"]): row for row in read_tsv(clean_path)}
    merged_rows = {normalize_term(row["term"]): row for row in read_tsv(merged_path)}
    return clean_rows, merged_rows


def collect_coco_attributes(cache_dir: Path) -> list[dict[str, Any]]:
    data_path = cached_download(COCO_ATTRIBUTES_URL, cache_dir / "cocottributes_eccv_version.jbl")
    data = load_python2_joblib(data_path)
    attrs = sorted(data["attributes"], key=lambda item: int(item["id"]))

    positive_counts = Counter()
    ann_vecs = data.get("ann_vecs") or {}
    for vector in ann_vecs.values():
        for idx, score in enumerate(vector):
            try:
                if float(score) > 0.5:
                    positive_counts[idx] += 1
            except (TypeError, ValueError):
                continue

    rows: list[dict[str, Any]] = []
    for idx, attr in enumerate(attrs):
        raw = str(attr["name"])
        term = normalize_term(raw)
        if not term:
            continue
        rows.append(
            {
                "source": "coco_attributes",
                "term": term,
                "raw_term": raw,
                "source_id": attr.get("id", ""),
                "source_type": attr.get("supercategory", ""),
                "count": positive_counts.get(idx, ""),
                "source_url": COCO_ATTRIBUTES_URL,
            }
        )
    return rows


def collect_vg_attribute_synsets(cache_dir: Path) -> dict[str, str]:
    zip_path = cached_download(VG_ATTRIBUTE_SYNSETS_URL, cache_dir / "visual_genome_attribute_synsets.json.zip")
    with zipfile.ZipFile(zip_path) as archive:
        data = json.loads(archive.read("attribute_synsets.json"))
    return {normalize_term(term): synset for term, synset in data.items() if normalize_term(term)}


def collect_vg_attributes(cache_dir: Path) -> list[dict[str, Any]]:
    zip_path = cached_download(VG_ATTRIBUTES_URL, cache_dir / "visual_genome_attributes.json.zip")
    synsets = collect_vg_attribute_synsets(cache_dir)
    counts: Counter[str] = Counter()
    raw_examples: dict[str, str] = {}

    with zipfile.ZipFile(zip_path) as archive:
        data = json.loads(archive.read("attributes.json"))

    for image_row in data:
        for obj in image_row.get("attributes", []):
            for attr in obj.get("attributes", []) or []:
                raw = str(attr)
                term = normalize_term(raw)
                if not term:
                    continue
                counts[term] += 1
                raw_examples.setdefault(term, raw)

    rows: list[dict[str, Any]] = []
    for term, count in counts.most_common():
        rows.append(
            {
                "source": "visual_genome_attributes",
                "term": term,
                "raw_term": raw_examples.get(term, term),
                "source_id": "",
                "source_type": "raw_attribute",
                "count": count,
                "synset": synsets.get(term, ""),
                "source_url": VG_ATTRIBUTES_URL,
            }
        )
    return rows


def add_overlap_columns(
    rows: list[dict[str, Any]],
    clean_terms: dict[str, dict[str, str]],
    merged_terms: dict[str, dict[str, str]],
) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for row in rows:
        term = normalize_term(row["term"])
        clean_row = clean_terms.get(term)
        merged_row = merged_terms.get(term)
        out = dict(row)
        out["overlap_clean"] = "yes" if clean_row else "no"
        out["overlap_merged"] = "yes" if merged_row else "no"
        out["existing_clean_roles"] = clean_row.get("roles", "") if clean_row else ""
        out["existing_clean_sources"] = clean_row.get("sources", "") if clean_row else ""
        out["existing_merged_roles"] = merged_row.get("roles", "") if merged_row else ""
        out["existing_merged_sources"] = merged_row.get("sources", "") if merged_row else ""
        output.append(out)
    return output


def specific_roles(role_text: str) -> list[str]:
    return [role for role in str(role_text).split("|") if role and role != "attribute"]


def role_classified_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    classified: list[dict[str, Any]] = []
    for row in rows:
        if row.get("overlap_clean") != "yes":
            continue
        roles = specific_roles(row.get("existing_clean_roles", ""))
        if not roles:
            continue
        out = dict(row)
        out["assigned_roles"] = "|".join(roles)
        out["assigned_role_sources"] = row.get("existing_clean_sources", "")
        out["classification_status"] = "classified_by_clean_lexicon_exact_overlap"
        classified.append(out)
    return classified


def write_report(path: Path, coco_rows: list[dict[str, Any]], vg_rows: list[dict[str, Any]]) -> None:
    def stats(rows: list[dict[str, Any]]) -> tuple[int, int, int]:
        total = len(rows)
        overlap = sum(1 for row in rows if row["overlap_clean"] == "yes")
        new = total - overlap
        return total, overlap, new

    coco_total, coco_overlap, coco_new = stats(coco_rows)
    vg_total, vg_overlap, vg_new = stats(vg_rows)
    coco_classified = role_classified_rows(coco_rows)
    vg_classified = role_classified_rows(vg_rows)

    role_counts = Counter()
    for row in coco_classified + vg_classified:
        for role in str(row["assigned_roles"]).split("|"):
            role_counts[role] += 1

    def examples(rows: list[dict[str, Any]], overlap: str, limit: int = 20) -> str:
        selected = [row["term"] for row in rows if row["overlap_clean"] == overlap][:limit]
        return ", ".join(f"`{term}`" for term in selected) if selected else "-"

    lines = [
        "# COCO Attributes / Visual Genome Attribute Overlap",
        "",
        "기존 `modifier_attributes_clean.tsv` 사전을 기준으로 COCO Attributes와 Visual Genome attribute vocabulary가 겹치는지 확인한 결과입니다.",
        "이번 파일은 분류를 새로 하지 않고, 외부 source의 attribute 후보가 기존 사전에 이미 있는지 여부만 나눕니다.",
        "",
        "## 기준",
        "",
        "- overlap 기준: `resources/lexicons/modifier_attributes_clean.tsv`의 `term`과 정규화된 exact match",
        "- 보조 확인: `modifier_attributes_merged.tsv` 기준 overlap 여부도 TSV 컬럼에 함께 기록",
        "- 정규화: lowercase, underscore/hyphen -> space, consecutive whitespace collapse",
        "",
        "## 요약",
        "",
        "| source | unique terms | overlap with clean | not in clean |",
        "|---|---:|---:|---:|",
        f"| COCO Attributes | {coco_total} | {coco_overlap} | {coco_new} |",
        f"| Visual Genome attributes | {vg_total} | {vg_overlap} | {vg_new} |",
        "",
        "## Role-Classified Subset",
        "",
        "아래 숫자는 새 분류 규칙을 적용한 것이 아니라, 기존 clean 사전에 이미 있던 term만 우리 role을 그대로 승계한 결과입니다.",
        "",
        "| source | role-classified terms | rule |",
        "|---|---:|---|",
        f"| COCO Attributes | {len(coco_classified)} | clean exact overlap |",
        f"| Visual Genome attributes | {len(vg_classified)} | clean exact overlap |",
        "",
        "| assigned role | terms |",
        "|---|---:|",
    ]
    for role, count in sorted(role_counts.items()):
        lines.append(f"| {role} | {count} |")
    lines.extend(
        [
            "",
        "## 예시",
        "",
        "| source | 기존 사전과 겹침 예시 | 기존 사전에 없음 예시 |",
        "|---|---|---|",
        f"| COCO Attributes | {examples(coco_rows, 'yes')} | {examples(coco_rows, 'no')} |",
        f"| Visual Genome | {examples(vg_rows, 'yes')} | {examples(vg_rows, 'no')} |",
        "",
        "## 생성 파일",
        "",
        "- `resources/external/coco_attributes_vocab.tsv`: COCO Attributes 원본 vocabulary",
        "- `resources/external/visual_genome_attributes_vocab.tsv`: Visual Genome full attributes에서 뽑은 raw attribute vocabulary와 빈도",
        "- `resources/external/visual_genome_attribute_synsets.tsv`: Visual Genome attribute synset vocabulary",
        "- `resources/lexicons/coco_attributes_overlap.tsv`: COCO 중 기존 clean 사전과 겹치는 항목",
        "- `resources/lexicons/coco_attributes_new.tsv`: COCO 중 기존 clean 사전에 없는 항목",
        "- `resources/lexicons/visual_genome_attributes_overlap.tsv`: Visual Genome 중 기존 clean 사전과 겹치는 항목",
        "- `resources/lexicons/visual_genome_attributes_new.tsv`: Visual Genome 중 기존 clean 사전에 없는 항목",
        "- `resources/lexicons/external_attribute_overlap.tsv`: COCO와 Visual Genome 비교 결과 통합본",
        "- `resources/lexicons/coco_attributes_role_classified.tsv`: COCO 중 clean role을 승계할 수 있는 항목만 모은 파일",
        "- `resources/lexicons/visual_genome_attributes_role_classified.tsv`: Visual Genome 중 clean role을 승계할 수 있는 항목만 모은 파일",
        "- `resources/lexicons/external_attribute_role_classified.tsv`: COCO와 Visual Genome role-classified subset 통합본",
        "",
        "## 주의",
        "",
        "- Visual Genome은 raw annotation 기반이라 `young`, `standing`, `open`처럼 attribute로 쓸 만한 표현과 `sidewalk`, `sky`처럼 object/context에 가까운 표현이 섞일 수 있습니다.",
        "- 그래서 이 결과는 parser 사전에 바로 병합하는 용도가 아니라, 다음 단계에서 검토할 candidate pool입니다.",
        "- `*_role_classified.tsv`는 안전한 subset입니다. 기존 clean 사전에 없던 항목은 role을 새로 추론하지 않았습니다.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Compare COCO/VG attribute vocabulary against the local modifier lexicon.")
    parser.add_argument("--cache-dir", type=Path, default=Path("resources/external/cache"))
    parser.add_argument("--external-dir", type=Path, default=Path("resources/external"))
    parser.add_argument("--lexicon-dir", type=Path, default=Path("resources/lexicons"))
    parser.add_argument("--report", type=Path, default=Path("reports/coco_vg_attribute_overlap.md"))
    parser.add_argument("--clean-lexicon", type=Path, default=Path("resources/lexicons/modifier_attributes_clean.tsv"))
    parser.add_argument("--merged-lexicon", type=Path, default=Path("resources/lexicons/modifier_attributes_merged.tsv"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    clean_terms, merged_terms = load_existing_terms(args.clean_lexicon, args.merged_lexicon)

    print("collecting COCO Attributes")
    coco_vocab = collect_coco_attributes(args.cache_dir)
    print(f"COCO unique terms: {len(coco_vocab)}")

    print("collecting Visual Genome attributes")
    vg_vocab = collect_vg_attributes(args.cache_dir)
    print(f"Visual Genome unique terms: {len(vg_vocab)}")

    print("writing source vocabularies")
    source_fieldnames = ["source", "term", "raw_term", "source_id", "source_type", "count", "synset", "source_url"]
    write_tsv(args.external_dir / "coco_attributes_vocab.tsv", coco_vocab, source_fieldnames)
    write_tsv(args.external_dir / "visual_genome_attributes_vocab.tsv", vg_vocab, source_fieldnames)

    vg_synsets = collect_vg_attribute_synsets(args.cache_dir)
    write_tsv(
        args.external_dir / "visual_genome_attribute_synsets.tsv",
        [{"term": term, "synset": synset, "source_url": VG_ATTRIBUTE_SYNSETS_URL} for term, synset in sorted(vg_synsets.items())],
        ["term", "synset", "source_url"],
    )

    print("computing overlaps")
    coco_overlap_rows = add_overlap_columns(coco_vocab, clean_terms, merged_terms)
    vg_overlap_rows = add_overlap_columns(vg_vocab, clean_terms, merged_terms)
    combined = sorted(coco_overlap_rows + vg_overlap_rows, key=lambda row: (row["source"], row["overlap_clean"], row["term"]))

    overlap_fieldnames = [
        "source",
        "term",
        "raw_term",
        "source_id",
        "source_type",
        "count",
        "synset",
        "overlap_clean",
        "overlap_merged",
        "existing_clean_roles",
        "existing_clean_sources",
        "existing_merged_roles",
        "existing_merged_sources",
        "source_url",
    ]
    write_tsv(args.lexicon_dir / "external_attribute_overlap.tsv", combined, overlap_fieldnames)
    write_tsv(
        args.lexicon_dir / "coco_attributes_overlap.tsv",
        [row for row in coco_overlap_rows if row["overlap_clean"] == "yes"],
        overlap_fieldnames,
    )
    write_tsv(
        args.lexicon_dir / "coco_attributes_new.tsv",
        [row for row in coco_overlap_rows if row["overlap_clean"] == "no"],
        overlap_fieldnames,
    )
    write_tsv(
        args.lexicon_dir / "visual_genome_attributes_overlap.tsv",
        [row for row in vg_overlap_rows if row["overlap_clean"] == "yes"],
        overlap_fieldnames,
    )
    write_tsv(
        args.lexicon_dir / "visual_genome_attributes_new.tsv",
        [row for row in vg_overlap_rows if row["overlap_clean"] == "no"],
        overlap_fieldnames,
    )

    role_fieldnames = [
        "source",
        "term",
        "assigned_roles",
        "assigned_role_sources",
        "classification_status",
        "raw_term",
        "source_id",
        "source_type",
        "count",
        "synset",
        "overlap_clean",
        "overlap_merged",
        "existing_merged_roles",
        "existing_merged_sources",
        "source_url",
    ]
    coco_classified = role_classified_rows(coco_overlap_rows)
    vg_classified = role_classified_rows(vg_overlap_rows)
    write_tsv(args.lexicon_dir / "coco_attributes_role_classified.tsv", coco_classified, role_fieldnames)
    write_tsv(args.lexicon_dir / "visual_genome_attributes_role_classified.tsv", vg_classified, role_fieldnames)
    write_tsv(
        args.lexicon_dir / "external_attribute_role_classified.tsv",
        sorted(coco_classified + vg_classified, key=lambda row: (row["source"], row["term"])),
        role_fieldnames,
    )

    write_report(args.report, coco_overlap_rows, vg_overlap_rows)
    print(f"wrote: {args.report}")


if __name__ == "__main__":
    main()
