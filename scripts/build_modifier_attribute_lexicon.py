from __future__ import annotations

import argparse
import ast
import csv
import io
import json
import re
import tarfile
import urllib.request
import zipfile
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from html import unescape
from pathlib import Path


VAW_ATTRIBUTE_TYPES_URL = "https://raw.githubusercontent.com/adobe-research/vaw_dataset/main/data/attribute_types.json"
OVAD_ZIP_URL = "https://lmb.informatik.uni-freiburg.de/resources/datasets/ovad.zip"
PACO_CATEGORIES_URL = "https://raw.githubusercontent.com/facebookresearch/paco/main/paco/data/datasets/paco_categories.py"
FASHIONPEDIA_VAL_URL = "https://s3.amazonaws.com/ifashionist-dataset/annotations/instances_attributes_val2020.json"
CSS_COLOR_URL = "https://www.w3.org/TR/css-color-4/"
DTD_LABELS_URL = "https://www.robots.ox.ac.uk/~vgg/data/dtd/download/dtd-r1.0.1-labels.tar.gz"


FIELDNAMES = [
    "term",
    "canonical",
    "role",
    "source",
    "source_type",
    "parent_type",
    "confidence",
    "raw_name",
    "source_url",
]


ROLE_BY_SOURCE_TYPE = {
    "activity": "activity_attribute",
    "animal": "motif_attribute",
    "brightness": "brightness_attribute",
    "cleanliness": "condition_attribute",
    "closeness": "spatial_attribute",
    "color": "color_attribute",
    "color quantity": "color_attribute",
    "cooked": "food_state_attribute",
    "depth": "size_attribute",
    "face expression": "expression_attribute",
    "face pose": "pose_attribute",
    "fatness": "size_attribute",
    "gender": "gender_attribute",
    "group": "group_attribute",
    "hair color": "color_attribute",
    "hand movement": "activity_attribute",
    "hardness": "texture_attribute",
    "height": "size_attribute",
    "hair type": "hair_attribute",
    "length": "size_attribute",
    "leather": "material_attribute",
    "letter color": "color_attribute",
    "location": "context_attribute",
    "material": "material_attribute",
    "maturity": "age_attribute",
    "neckline type": "clothing_cut_attribute",
    "newness": "condition_attribute",
    "nickname": "fashion_style_attribute",
    "non textile material type": "material_attribute",
    "opaqeness": "opacity_attribute",
    "opacity": "opacity_attribute",
    "opening type": "clothing_opening_attribute",
    "optical property": "opacity_attribute",
    "order": "order_attribute",
    "orientation": "orientation_attribute",
    "pattern": "pattern_attribute",
    "pattern marking": "pattern_attribute",
    "pattern_marking": "pattern_attribute",
    "place": "context_attribute",
    "position": "spatial_attribute",
    "pose": "pose_attribute",
    "race": "race_attribute",
    "shape": "shape_attribute",
    "silhouette": "silhouette_attribute",
    "size": "size_attribute",
    "size comparison": "size_attribute",
    "skin color": "color_attribute",
    "sport activity": "activity_attribute",
    "state": "state_attribute",
    "textile finishing, manufacturing techniques": "textile_finish_attribute",
    "textile pattern": "pattern_attribute",
    "texture": "texture_attribute",
    "thickness": "size_attribute",
    "tone": "tone_attribute",
    "transparency": "opacity_attribute",
    "waistline": "clothing_cut_attribute",
    "weather": "weather_attribute",
    "wearing accessories": "accessory_attribute",
    "wearing color": "color_attribute",
    "weight": "weight_attribute",
    "width": "size_attribute",
}


LOW_CONFIDENCE_TYPES = {"other"}


@dataclass(frozen=True)
class LexiconEntry:
    term: str
    canonical: str
    role: str
    source: str
    source_type: str
    parent_type: str
    confidence: str
    raw_name: str
    source_url: str


def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "gpic-caption-concepts/0.1"})
    with urllib.request.urlopen(req, timeout=90) as response:
        return response.read()


def normalize_term(text: str) -> str:
    text = unescape(text).strip().lower()
    text = text.replace("_", " ")
    text = text.replace("-", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def is_generic_other(term: str) -> bool:
    return term == "other" or term.startswith("other(") or term.startswith("other ")


def role_for_type(source_type: str) -> str:
    return ROLE_BY_SOURCE_TYPE.get(source_type.strip().lower(), "attribute")


def add_entry(
    entries: list[LexiconEntry],
    *,
    term: str,
    source: str,
    source_type: str,
    parent_type: str = "",
    raw_name: str = "",
    source_url: str = "",
    confidence: str = "high",
) -> None:
    term_norm = normalize_term(term)
    if not term_norm:
        return
    if is_generic_other(term_norm):
        return
    source_type_norm = normalize_term(source_type)
    parent_type_norm = normalize_term(parent_type)
    if source_type_norm in LOW_CONFIDENCE_TYPES or parent_type_norm in LOW_CONFIDENCE_TYPES:
        confidence = "low"
    role_key = parent_type_norm if parent_type_norm in ROLE_BY_SOURCE_TYPE else source_type_norm
    entries.append(
        LexiconEntry(
            term=term_norm,
            canonical=term_norm,
            role=role_for_type(role_key),
            source=source,
            source_type=source_type_norm,
            parent_type=parent_type_norm,
            confidence=confidence,
            raw_name=raw_name or term,
            source_url=source_url,
        )
    )


def collect_vaw() -> list[LexiconEntry]:
    data = json.loads(fetch_bytes(VAW_ATTRIBUTE_TYPES_URL))
    entries: list[LexiconEntry] = []
    for source_type, terms in data.items():
        for term in terms:
            add_entry(
                entries,
                term=term,
                source="vaw",
                source_type=source_type,
                parent_type=source_type,
                raw_name=term,
                source_url=VAW_ATTRIBUTE_TYPES_URL,
                confidence="low" if source_type == "other" else "high",
            )
    return entries


def parse_ovad_attribute_name(name: str) -> tuple[str, list[str]]:
    if ":" not in name:
        return "", [name]
    prefix, values = name.split(":", 1)
    terms = [item.strip() for item in re.split(r"/|,", values) if item.strip()]
    return prefix.strip(), terms


def collect_ovad() -> list[LexiconEntry]:
    raw_zip = fetch_bytes(OVAD_ZIP_URL)
    with zipfile.ZipFile(io.BytesIO(raw_zip)) as archive:
        data = json.loads(archive.read("ovad2000.json"))
    entries: list[LexiconEntry] = []
    for attr in data["attributes"]:
        name = attr["name"]
        prefix_type, terms = parse_ovad_attribute_name(name)
        source_type = attr.get("type") or prefix_type
        parent_type = attr.get("parent_type") or source_type
        for term in terms:
            add_entry(
                entries,
                term=term,
                source="ovad",
                source_type=source_type,
                parent_type=parent_type,
                raw_name=name,
                source_url=OVAD_ZIP_URL,
                confidence="high",
            )
    return entries


def collect_paco() -> list[LexiconEntry]:
    text = fetch_bytes(PACO_CATEGORIES_URL).decode("utf-8")
    match = re.search(r"PACO_ATTRIBUTES\s*=\s*(\[.*?\])\s*# fmt: on", text, flags=re.S)
    if not match:
        raise ValueError("Could not find PACO_ATTRIBUTES in paco_categories.py")
    attrs = ast.literal_eval(match.group(1))
    entries: list[LexiconEntry] = []
    for attr in attrs:
        name = attr["name"]
        attr_id = int(attr["id"])
        if 0 <= attr_id <= 29:
            source_type = "color"
        elif 30 <= attr_id <= 40:
            source_type = "pattern_marking"
        elif 41 <= attr_id <= 54:
            source_type = "material"
        elif 55 <= attr_id <= 58:
            source_type = "transparency"
        else:
            source_type = "attribute"
        add_entry(
            entries,
            term=name,
            source="paco",
            source_type=source_type,
            parent_type=source_type,
            raw_name=name,
            source_url=PACO_CATEGORIES_URL,
            confidence="high",
        )
    return entries


def collect_fashionpedia() -> list[LexiconEntry]:
    data = json.loads(fetch_bytes(FASHIONPEDIA_VAL_URL))
    entries: list[LexiconEntry] = []
    for attr in data["attributes"]:
        source_type = attr.get("supercategory") or "fashion_attribute"
        name = attr["name"]
        add_entry(
            entries,
            term=name,
            source="fashionpedia",
            source_type=source_type,
            parent_type=source_type,
            raw_name=name,
            source_url=FASHIONPEDIA_VAL_URL,
            confidence="medium",
        )
    return entries


def collect_css_named_colors() -> list[LexiconEntry]:
    html = fetch_bytes(CSS_COLOR_URL).decode("utf-8", errors="replace")
    table_match = re.search(r'<table class="named-color-table">(.*?)</table>', html, flags=re.S)
    if not table_match:
        raise ValueError("Could not find CSS named-color-table")
    names = sorted(set(re.findall(r'id="valdef-color-([a-z]+)"', table_match.group(1))))
    entries: list[LexiconEntry] = []
    for name in names:
        add_entry(
            entries,
            term=name,
            source="css_color_4",
            source_type="color",
            parent_type="color",
            raw_name=name,
            source_url=CSS_COLOR_URL,
            confidence="high",
        )
    return entries


def collect_dtd() -> list[LexiconEntry]:
    raw_tar = fetch_bytes(DTD_LABELS_URL)
    labels: set[str] = set()
    with tarfile.open(fileobj=io.BytesIO(raw_tar), mode="r:gz") as archive:
        for member in archive.getmembers():
            if not member.name.startswith("labels/") or not member.name.endswith(".txt"):
                continue
            extracted = archive.extractfile(member)
            if extracted is None:
                continue
            for raw_line in extracted.read().decode("utf-8", errors="replace").splitlines():
                line = raw_line.strip()
                if not line:
                    continue
                label = line.split("/")[0]
                labels.add(label)
    entries: list[LexiconEntry] = []
    for label in sorted(labels):
        add_entry(
            entries,
            term=label,
            source="dtd",
            source_type="texture",
            parent_type="texture",
            raw_name=label,
            source_url=DTD_LABELS_URL,
            confidence="high",
        )
    return entries


COLLECTORS = {
    "vaw": collect_vaw,
    "ovad": collect_ovad,
    "paco": collect_paco,
    "fashionpedia": collect_fashionpedia,
    "css_color_4": collect_css_named_colors,
    "dtd": collect_dtd,
}


def merge_entries(entries: list[LexiconEntry]) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    grouped: dict[str, list[LexiconEntry]] = defaultdict(list)
    for entry in entries:
        grouped[entry.term].append(entry)

    merged_rows: list[dict[str, str]] = []
    detail_rows: list[dict[str, str]] = []
    confidence_rank = {"high": 3, "medium": 2, "low": 1}
    for term in sorted(grouped):
        group = grouped[term]
        roles = sorted({entry.role for entry in group})
        sources = sorted({entry.source for entry in group})
        source_types = sorted({entry.source_type for entry in group})
        parent_types = sorted({entry.parent_type for entry in group if entry.parent_type})
        best_confidence = max(group, key=lambda item: confidence_rank.get(item.confidence, 0)).confidence
        merged_rows.append(
            {
                "term": term,
                "canonical": term,
                "roles": "|".join(roles),
                "sources": "|".join(sources),
                "source_types": "|".join(source_types),
                "parent_types": "|".join(parent_types),
                "confidence": best_confidence,
                "source_count": str(len(sources)),
                "entry_count": str(len(group)),
            }
        )
        for entry in sorted(group, key=lambda item: (item.source, item.source_type, item.raw_name)):
            detail_rows.append(asdict(entry))
    return merged_rows, detail_rows


def write_tsv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def clean_merged_rows(merged_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for row in merged_rows:
        roles = set(row["roles"].split("|"))
        if row["confidence"] == "low":
            continue
        if roles == {"attribute"}:
            continue
        rows.append(row)
    return rows


def write_summary(
    path: Path,
    merged_rows: list[dict[str, str]],
    clean_rows: list[dict[str, str]],
    detail_rows: list[dict[str, str]],
) -> None:
    source_counts = Counter(row["source"] for row in detail_rows)
    role_counts = Counter()
    for row in merged_rows:
        for role in row["roles"].split("|"):
            role_counts[role] += 1
    confidence_counts = Counter(row["confidence"] for row in merged_rows)

    lines = [
        "# Modifier Attribute Lexicon Summary",
        "",
        "확실한 외부 typed attribute source를 다운로드해서 합친 modifier attribute lexicon 요약입니다.",
        "",
        f"- unique terms: {len(merged_rows)}",
        f"- clean unique terms: {len(clean_rows)}",
        f"- source entries: {len(detail_rows)}",
        "",
        "## Sources",
        "",
        "| source | entries |",
        "|---|---:|",
    ]
    for source, count in sorted(source_counts.items()):
        lines.append(f"| {source} | {count} |")
    lines.extend(["", "## Roles", "", "| role | unique terms |", "|---|---:|"])
    for role, count in sorted(role_counts.items()):
        lines.append(f"| {role} | {count} |")
    lines.extend(["", "## Confidence", "", "| confidence | unique terms |", "|---|---:|"])
    for confidence, count in sorted(confidence_counts.items()):
        lines.append(f"| {confidence} | {count} |")
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- `modifier_attributes_merged.tsv`: term 단위로 source/role을 합친 파일입니다.",
            "- `modifier_attributes_clean.tsv`: parser rule lookup에 바로 쓰기 쉬운 high/medium-confidence 파일입니다.",
            "- `modifier_attributes_detailed.tsv`: source별 원본 entry를 보존한 파일입니다.",
            "- VAW의 `other` bucket과 `other(...)` placeholder는 clean modifier rule에 바로 쓰기 어렵기 때문에 generic placeholder는 제외했습니다.",
            "- Fashionpedia는 fashion domain attribute라 `confidence=medium`으로 둡니다.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a typed modifier attribute lexicon from public sources.")
    parser.add_argument(
        "--sources",
        nargs="+",
        default=list(COLLECTORS),
        choices=sorted(COLLECTORS),
        help="Sources to download and merge.",
    )
    parser.add_argument("--output-dir", type=Path, default=Path("resources/lexicons"))
    parser.add_argument("--report", type=Path, default=Path("reports/modifier_attribute_lexicon_summary.md"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    all_entries: list[LexiconEntry] = []
    for source in args.sources:
        entries = COLLECTORS[source]()
        print(f"{source}: {len(entries)} entries")
        all_entries.extend(entries)

    merged_rows, detail_rows = merge_entries(all_entries)
    clean_rows = clean_merged_rows(merged_rows)
    write_tsv(
        args.output_dir / "modifier_attributes_merged.tsv",
        merged_rows,
        [
            "term",
            "canonical",
            "roles",
            "sources",
            "source_types",
            "parent_types",
            "confidence",
            "source_count",
            "entry_count",
        ],
    )
    write_tsv(
        args.output_dir / "modifier_attributes_clean.tsv",
        clean_rows,
        [
            "term",
            "canonical",
            "roles",
            "sources",
            "source_types",
            "parent_types",
            "confidence",
            "source_count",
            "entry_count",
        ],
    )
    write_tsv(args.output_dir / "modifier_attributes_detailed.tsv", detail_rows, FIELDNAMES)
    write_summary(args.report, merged_rows, clean_rows, detail_rows)
    print(f"merged unique terms: {len(merged_rows)}")
    print(f"clean unique terms: {len(clean_rows)}")
    print(f"wrote: {args.output_dir / 'modifier_attributes_merged.tsv'}")
    print(f"wrote: {args.output_dir / 'modifier_attributes_clean.tsv'}")
    print(f"wrote: {args.output_dir / 'modifier_attributes_detailed.tsv'}")
    print(f"wrote: {args.report}")


if __name__ == "__main__":
    main()
