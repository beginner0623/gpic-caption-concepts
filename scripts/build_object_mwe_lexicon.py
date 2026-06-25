from __future__ import annotations

import argparse
import csv
import json
import re
import tarfile
import urllib.request
import zipfile
from collections import Counter, defaultdict
from html import unescape
from pathlib import Path
from typing import Any


COCO_ANNOTATIONS_URL = "https://images.cocodataset.org/annotations/annotations_trainval2017.zip"
LVIS_VAL_URL = "https://s3-us-west-2.amazonaws.com/dl.fbaipublicfiles.com/LVIS/lvis_v1_val.json.zip"
OPEN_IMAGES_BOXABLE_URL = "https://storage.googleapis.com/openimages/v7/oidv7-class-descriptions-boxable.csv"
VG_OBJECT_SYNSETS_URL = "https://homes.cs.washington.edu/~ranjay/visualgenome/data/dataset/object_synsets.json.zip"
WORDNET_DB_URL = "https://wordnetcode.princeton.edu/3.0/WNdb-3.0.tar.gz"

VISUAL_SOURCES = {"coco_object", "lvis_object", "openimages_boxable", "visual_genome_object_synset"}
DEFAULT_ATTRIBUTE_PREFIX_LEXICON = Path("resources/lexicons/modifier_attributes_clean.tsv")
ALLOWED_WORDNET_LEXFILES = {
    "05",  # noun.animal
    "06",  # noun.artifact
    "08",  # noun.body
    "13",  # noun.food
    "15",  # noun.location
    "17",  # noun.object
    "20",  # noun.plant
    "27",  # noun.substance
}
COCO_CATEGORY_NAMES = [
    "person",
    "bicycle",
    "car",
    "motorcycle",
    "airplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "backpack",
    "umbrella",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis",
    "snowboard",
    "sports ball",
    "kite",
    "baseball bat",
    "baseball glove",
    "skateboard",
    "surfboard",
    "tennis racket",
    "bottle",
    "wine glass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hot dog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "couch",
    "potted plant",
    "bed",
    "dining table",
    "toilet",
    "tv",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cell phone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddy bear",
    "hair drier",
    "toothbrush",
]
FIELDNAMES = [
    "term",
    "canonical",
    "confidence",
    "sources",
    "source_count",
    "variant_of",
    "synsets",
    "rule_id",
]

BAD_HEADS = {
    "area",
    "background",
    "bottom",
    "center",
    "colour",
    "color",
    "edge",
    "foreground",
    "front",
    "image",
    "kind",
    "middle",
    "number",
    "part",
    "photo",
    "picture",
    "scene",
    "side",
    "sort",
    "stuff",
    "text",
    "thing",
    "top",
    "type",
    "view",
    "word",
}
BAD_TERMS = {
    "black and white",
    "close up",
    "front view",
    "side view",
}
BAD_PREFIXES = {"other", "unknown", "unidentified", "misc", "miscellaneous"}
WORDNET_ONLY_HEAD_ALLOWLIST = {
    # Heads that frequently break POS/dependency when used as compound nouns.
    "can",
    "stand",
}
COMPOSITIONAL_ATTRIBUTE_ROLES = {
    "age_attribute",
    "brightness_attribute",
    "color_attribute",
    "condition_attribute",
    "material_attribute",
    "pattern_attribute",
    "pose_attribute",
    "shape_attribute",
    "size_attribute",
    "state_attribute",
    "texture_attribute",
    "weather_attribute",
}
ORDINAL_PREFIXES = {
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
}
IRREGULAR_PLURALS = {
    "bus": "buses",
    "child": "children",
    "foot": "feet",
    "goose": "geese",
    "man": "men",
    "mouse": "mice",
    "person": "people",
    "tooth": "teeth",
    "woman": "women",
}


def fetch_bytes(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "gpic-caption-concepts/0.1"})
    with urllib.request.urlopen(request, timeout=300) as response:
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
    text = text.replace("/", " / ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def canonicalize(term: str) -> str:
    term = normalize_term(term)
    term = term.replace("-", " ")
    term = re.sub(r"[^a-z0-9]+", "_", term)
    return term.strip("_")


def split_words(term: str) -> list[str]:
    return re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)?", normalize_term(term))


def load_attribute_prefixes(path: Path) -> set[str]:
    if not path.exists():
        return set()
    prefixes: set[str] = set()
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            term = normalize_term(row.get("term", ""))
            words = split_words(term)
            if len(words) != 1:
                continue
            roles = set((row.get("roles", "") or "").split("|"))
            confidence = row.get("confidence", "")
            if confidence == "high" and roles & COMPOSITIONAL_ATTRIBUTE_ROLES:
                prefixes.add(words[0])
    return prefixes


def is_compositional_attribute_phrase(term: str, attribute_prefixes: set[str]) -> bool:
    words = split_words(term)
    if len(words) < 2:
        return False
    prefixes = words[:-1]
    if any(word in ORDINAL_PREFIXES for word in prefixes):
        return True
    return any(word in attribute_prefixes for word in prefixes)


def is_multiword_noun_label(term: str) -> bool:
    norm = normalize_term(term)
    words = split_words(norm)
    if len(words) < 2:
        return "-" in norm and len(words) == 1
    if len(words) > 5:
        return False
    if norm in BAD_TERMS:
        return False
    if words[0] in BAD_PREFIXES:
        return False
    if words[-1] in BAD_HEADS:
        return False
    if any(word in {"and", "or", "of", "with", "without"} for word in words):
        return False
    return True


def pluralize_last_word(term: str) -> str | None:
    words = split_words(term)
    if len(words) < 2:
        return None
    last = words[-1]
    if last in IRREGULAR_PLURALS:
        plural = IRREGULAR_PLURALS[last]
    elif last.endswith("y") and len(last) > 1 and last[-2] not in "aeiou":
        plural = f"{last[:-1]}ies"
    elif last.endswith(("ss", "x", "z", "ch", "sh")):
        plural = f"{last}es"
    elif last.endswith("s"):
        return None
    else:
        plural = f"{last}s"
    if plural == last:
        return None
    return " ".join([*words[:-1], plural])


def write_tsv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def add_label(
    grouped: dict[str, dict[str, Any]],
    term: str,
    source: str,
    *,
    synset: str = "",
    variant_of: str = "",
) -> None:
    term = normalize_term(term)
    if not is_multiword_noun_label(term):
        return
    row = grouped.setdefault(
        term,
        {
            "term": term,
            "canonical": canonicalize(variant_of or term),
            "sources": set(),
            "variant_of": variant_of,
            "synsets": set(),
        },
    )
    row["sources"].add(source)
    if synset:
        row["synsets"].add(synset)


def parse_coco(cache_dir: Path) -> list[tuple[str, str]]:
    try:
        path = cached_download(COCO_ANNOTATIONS_URL, cache_dir / "coco_annotations_trainval2017.zip")
        with zipfile.ZipFile(path) as archive:
            with archive.open("annotations/instances_val2017.json") as handle:
                data = json.loads(handle.read().decode("utf-8"))
        return [(category["name"], "") for category in data.get("categories", [])]
    except Exception:
        return [(name, "") for name in COCO_CATEGORY_NAMES]


def parse_lvis(cache_dir: Path) -> list[tuple[str, str]]:
    path = cached_download(LVIS_VAL_URL, cache_dir / "lvis_v1_val.json.zip")
    with zipfile.ZipFile(path) as archive:
        json_name = next(name for name in archive.namelist() if name.endswith(".json"))
        data = json.loads(archive.read(json_name).decode("utf-8"))
    labels: list[tuple[str, str]] = []
    for category in data.get("categories", []):
        synset = category.get("synset", "")
        labels.append((category.get("name", ""), synset))
        for synonym in category.get("synonyms", []) or []:
            labels.append((synonym, synset))
    return labels


def parse_openimages(cache_dir: Path) -> list[tuple[str, str]]:
    path = cached_download(OPEN_IMAGES_BOXABLE_URL, cache_dir / "openimages_v7_class_descriptions_boxable.csv")
    labels: list[tuple[str, str]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        for row in reader:
            if len(row) >= 2:
                labels.append((row[1], ""))
    return labels


def parse_vg_object_synsets(cache_dir: Path) -> list[tuple[str, str]]:
    path = cached_download(VG_OBJECT_SYNSETS_URL, cache_dir / "visual_genome_object_synsets.json.zip")
    with zipfile.ZipFile(path) as archive:
        json_name = next(name for name in archive.namelist() if name.endswith(".json"))
        data = json.loads(archive.read(json_name).decode("utf-8"))
    return [(term, synset) for term, synset in data.items()]


def parse_wordnet_mwe_nouns(cache_dir: Path) -> list[tuple[str, str]]:
    path = cached_download(WORDNET_DB_URL, cache_dir / "WNdb-3.0.tar.gz")
    labels: list[tuple[str, str]] = []
    with tarfile.open(path, "r:gz") as archive:
        member = archive.getmember("dict/index.noun")
        handle = archive.extractfile(member)
        if handle is None:
            return labels
        for raw_line in handle:
            line = raw_line.decode("utf-8", errors="replace").strip()
            if not line or line.startswith(" "):
                continue
            lemma = line.split(" ", 1)[0]
            if "_" not in lemma and "-" not in lemma:
                continue
            labels.append((lemma.replace("_", " "), "wordnet_noun"))
    return labels


def parse_wordnet_synset_lexfiles(cache_dir: Path) -> dict[str, str]:
    path = cached_download(WORDNET_DB_URL, cache_dir / "WNdb-3.0.tar.gz")
    mapping: dict[str, str] = {}
    with tarfile.open(path, "r:gz") as archive:
        member = archive.getmember("dict/index.sense")
        handle = archive.extractfile(member)
        if handle is None:
            return mapping
        for raw_line in handle:
            parts = raw_line.decode("utf-8", errors="replace").strip().split()
            if len(parts) < 3:
                continue
            sense_key = parts[0]
            sense_number = parts[2]
            if "%" not in sense_key:
                continue
            lemma, sense_info = sense_key.split("%", 1)
            sense_parts = sense_info.split(":")
            if len(sense_parts) < 2:
                continue
            ss_type, lex_filenum = sense_parts[0], sense_parts[1]
            if ss_type != "1":
                continue
            mapping[f"{lemma}.n.{int(sense_number):02d}"] = lex_filenum
    return mapping


def build_rows(
    cache_dir: Path,
    attribute_prefix_lexicon: Path = DEFAULT_ATTRIBUTE_PREFIX_LEXICON,
) -> tuple[list[dict[str, str]], list[dict[str, str]], Counter[str]]:
    grouped: dict[str, dict[str, Any]] = {}
    source_counts: Counter[str] = Counter()

    visual_label_sets: dict[str, set[str]] = defaultdict(set)
    source_specs = [
        ("coco_object", parse_coco),
        ("lvis_object", parse_lvis),
        ("openimages_boxable", parse_openimages),
        ("visual_genome_object_synset", parse_vg_object_synsets),
    ]

    for source, parser in source_specs:
        labels = parser(cache_dir)
        source_counts[source] = len(labels)
        for label, synset in labels:
            term = normalize_term(label)
            visual_label_sets[source].add(term)
            add_label(grouped, term, source, synset=synset)

    visual_heads = {
        words[-1]
        for labels in visual_label_sets.values()
        for label in labels
        for words in [split_words(label)]
        if len(words) >= 1 and words[-1] not in BAD_HEADS
    }
    trusted_visual_heads = {
        words[-1]
        for source, labels in visual_label_sets.items()
        if source in {"coco_object", "lvis_object", "openimages_boxable"}
        for label in labels
        for words in [split_words(label)]
        if len(words) >= 1 and words[-1] not in BAD_HEADS
    }
    attribute_prefixes = load_attribute_prefixes(attribute_prefix_lexicon)

    wordnet_labels = parse_wordnet_mwe_nouns(cache_dir)
    wordnet_synset_lexfiles = parse_wordnet_synset_lexfiles(cache_dir)
    source_counts["wordnet_noun_mwe"] = len(wordnet_labels)
    for label, synset in wordnet_labels:
        term = normalize_term(label)
        words = split_words(term)
        if len(words) >= 2 and words[-1] in visual_heads:
            add_label(grouped, term, "wordnet_noun_mwe", synset=synset)

    # Add plural surface variants for parser-time matching while preserving singular canonical form.
    for term, row in list(grouped.items()):
        plural = pluralize_last_word(term)
        if not plural:
            continue
        if plural not in grouped:
            add_label(grouped, plural, "plural_variant", variant_of=term)
        plural_row = grouped[plural]
        if not plural_row["variant_of"]:
            plural_row["variant_of"] = term
        plural_row["canonical"] = row["canonical"]
        plural_row["sources"].add("plural_variant")
        plural_row["sources"].update(row["sources"])
        plural_row["synsets"].update(row["synsets"])

    candidates: list[dict[str, str]] = []
    clean_core: list[dict[str, str]] = []
    for term in sorted(grouped):
        row = grouped[term]
        sources = sorted(row["sources"])
        evidence_sources = [source for source in sources if source != "plural_variant"]
        visual_source_count = sum(1 for source in evidence_sources if source in VISUAL_SOURCES)
        trusted_visual_source_count = sum(
            1 for source in evidence_sources if source in {"coco_object", "lvis_object", "openimages_boxable"}
        )
        has_wordnet = "wordnet_noun_mwe" in sources
        words = split_words(row["variant_of"] or term)
        head = words[-1] if words else ""
        synset_lexfiles = {
            wordnet_synset_lexfiles[synset]
            for synset in row["synsets"]
            if synset in wordnet_synset_lexfiles
        }
        compositional_attribute_phrase = is_compositional_attribute_phrase(
            row["variant_of"] or term,
            attribute_prefixes,
        )
        trusted_wordnet = (
            has_wordnet
            and visual_source_count == 0
            and head in trusted_visual_heads
            and head in WORDNET_ONLY_HEAD_ALLOWLIST
            and len(words) <= 3
        )
        high_confidence = not compositional_attribute_phrase and (
            trusted_visual_source_count >= 1
            or visual_source_count >= 2
            or (
                "visual_genome_object_synset" in sources
                and has_wordnet
                and (head in trusted_visual_heads or bool(synset_lexfiles & ALLOWED_WORDNET_LEXFILES))
            )
            or trusted_wordnet
        )
        confidence = "high" if high_confidence else "medium"
        if compositional_attribute_phrase:
            rule_id = "compositional_attribute_phrase"
        elif trusted_visual_source_count >= 1:
            rule_id = "trusted_visual_object_label"
        elif visual_source_count >= 2:
            rule_id = "multi_visual_object_label"
        elif (
            "visual_genome_object_synset" in sources
            and has_wordnet
            and (head in trusted_visual_heads or bool(synset_lexfiles & ALLOWED_WORDNET_LEXFILES))
        ):
            rule_id = "vg_object_synset_plus_wordnet"
        elif trusted_wordnet:
            rule_id = "wordnet_trusted_visual_head"
        else:
            rule_id = "candidate_only"
        out = {
            "term": term,
            "canonical": row["canonical"],
            "confidence": confidence,
            "sources": "|".join(sources),
            "source_count": str(len(evidence_sources)),
            "variant_of": row["variant_of"],
            "synsets": "|".join(sorted(row["synsets"])),
            "rule_id": rule_id,
        }
        candidates.append(out)
        if high_confidence:
            clean_core.append(out)

    return candidates, clean_core, source_counts


def write_report(path: Path, candidates: list[dict[str, str]], clean_core: list[dict[str, str]], source_counts: Counter[str]) -> None:
    source_membership: Counter[str] = Counter()
    for row in clean_core:
        for source in row["sources"].split("|"):
            source_membership[source] += 1

    examples = ["trash can", "trash cans", "music stand", "music stands", "traffic light", "hot dog", "tennis court"]
    lookup = {row["term"]: row for row in candidates}
    lines = [
        "# Object Noun MWE Lexicon Summary",
        "",
        "High-confidence visual object labels and filtered WordNet noun MWEs로 만든 parser-time object MWE 사전입니다.",
        "",
        "## Output Files",
        "",
        "- `resources/lexicons/object_noun_mwe_clean_core.tsv`",
        "",
        "## Source Label Counts",
        "",
        "| source | raw labels |",
        "|---|---:|",
    ]
    for source, count in sorted(source_counts.items()):
        lines.append(f"| {source} | {count} |")
    lines.extend(["", "## Lexicon Counts", "", "| item | count |", "|---|---:|"])
    lines.append(f"| candidates | {len(candidates)} |")
    lines.append(f"| clean_core | {len(clean_core)} |")
    lines.extend(["", "## Clean Core Source Membership", "", "| source | terms |", "|---|---:|"])
    for source, count in sorted(source_membership.items()):
        lines.append(f"| {source} | {count} |")
    lines.extend(["", "## Key Examples", "", "| term | canonical | confidence | sources |", "|---|---|---|---|"])
    for term in examples:
        row = lookup.get(term)
        if row:
            lines.append(f"| `{term}` | `{row['canonical']}` | {row['confidence']} | {row['sources']} |")
        else:
            lines.append(f"| `{term}` | - | - | - |")
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- Clean core는 visual object dataset label을 우선한다.",
            "- 단, clean modifier attribute 사전에 있는 수식어가 prefix로 붙은 compositional attribute+noun phrase는 merge 대상에서 제외한다.",
            "- WordNet-only MWE는 너무 넓기 때문에 `can`, `stand`처럼 실제 POS 오류를 자주 만드는 head에 한해 clean core에 넣는다.",
            "- plural variant는 parser-time matching용 surface이며 canonical은 singular phrase로 유지한다.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build high-confidence object noun MWE lexicon.")
    parser.add_argument("--cache-dir", type=Path, default=Path("resources/external/cache"))
    parser.add_argument("--output-dir", type=Path, default=Path("resources/lexicons"))
    parser.add_argument(
        "--attribute-prefix-lexicon",
        type=Path,
        default=DEFAULT_ATTRIBUTE_PREFIX_LEXICON,
        help="Clean modifier attribute TSV used to avoid merging compositional attribute+noun phrases.",
    )
    parser.add_argument(
        "--candidates-output",
        type=Path,
        help="Optional audit TSV for every candidate before high-confidence filtering.",
    )
    parser.add_argument("--report", type=Path, default=Path("reports/object_noun_mwe_lexicon_summary.md"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    candidates, clean_core, source_counts = build_rows(args.cache_dir, args.attribute_prefix_lexicon)
    write_tsv(args.output_dir / "object_noun_mwe_clean_core.tsv", clean_core, FIELDNAMES)
    if args.candidates_output:
        write_tsv(args.candidates_output, candidates, FIELDNAMES)
    write_report(args.report, candidates, clean_core, source_counts)
    print(f"object noun MWE candidates: {len(candidates)}")
    print(f"object noun MWE clean core: {len(clean_core)}")
    print(f"wrote: {args.output_dir / 'object_noun_mwe_clean_core.tsv'}")
    if args.candidates_output:
        print(f"wrote: {args.candidates_output}")
    print(f"wrote: {args.report}")


if __name__ == "__main__":
    main()
