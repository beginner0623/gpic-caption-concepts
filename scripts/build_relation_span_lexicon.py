from __future__ import annotations

import argparse
import csv
import io
import json
import re
import urllib.request
import zipfile
from collections import Counter, defaultdict
from html import unescape
from pathlib import Path
from typing import Any


VG_RELATIONSHIP_ALIAS_URL = "https://homes.cs.washington.edu/~ranjay/visualgenome/data/dataset/relationship_alias.txt"
VG_RELATIONSHIP_SYNSETS_URL = "https://homes.cs.washington.edu/~ranjay/visualgenome/data/dataset/relationship_synsets.json.zip"
VG_RELATIONSHIPS_URL = "https://homes.cs.washington.edu/~ranjay/visualgenome/data/dataset/relationships.json.zip"
OPEN_IMAGES_RELATION_TRIPLETS_URL = "https://storage.googleapis.com/openimages/v6/oidv6-relationship-triplets.csv"
STREUSLE_CONLLU_URL = "https://raw.githubusercontent.com/nert-nlp/streusle/master/streusle.conllu"


FIELDNAMES = [
    "term",
    "canonical",
    "relation_type",
    "confidence",
    "is_multiword",
    "sources",
    "vg_count",
    "openimages_triplet_count",
    "synsets",
    "alias_group",
    "rule_id",
    "provenance",
]


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
    text = text.replace("/", " / ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def slug(text: str) -> str:
    text = normalize_term(text)
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")


def split_pipe(text: str) -> list[str]:
    return [item for item in str(text).split("|") if item]


def confidence_rank(confidence: str) -> int:
    return {"high": 3, "medium": 2, "low": 1}.get(confidence, 0)


def is_multiword(term: str) -> str:
    return "yes" if len(normalize_term(term).split()) > 1 else "no"


def write_tsv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


MANUAL_RELATION_RULES: dict[str, tuple[str, str, str]] = {
    # spatial support / contact
    "on": ("on", "spatial_support", "high"),
    "onto": ("on", "spatial_support", "high"),
    "on top of": ("on_top_of", "spatial_support", "high"),
    "atop": ("on_top_of", "spatial_support", "high"),
    "sitting on": ("sitting_on", "pose_support", "high"),
    "standing on": ("standing_on", "pose_support", "high"),
    "parked on": ("parked_on", "state_support", "high"),
    "lying on": ("lying_on", "pose_support", "high"),
    "laying on": ("lying_on", "pose_support", "high"),
    "leaning on": ("leaning_on", "pose_support", "high"),
    "leaning against": ("leaning_against", "spatial_contact", "high"),
    "against": ("against", "spatial_contact", "high"),
    "attached to": ("attached_to", "attachment_relation", "high"),
    "connected to": ("connected_to", "attachment_relation", "high"),
    "hanging from": ("hanging_from", "attachment_relation", "high"),
    "hanging on": ("hanging_on", "attachment_relation", "high"),
    "mounted on": ("mounted_on", "attachment_relation", "high"),
    # spatial vertical/depth/lateral/proximity
    "above": ("above", "spatial_vertical", "high"),
    "over": ("above", "spatial_vertical", "high"),
    "under": ("under", "spatial_vertical", "high"),
    "underneath": ("under", "spatial_vertical", "high"),
    "below": ("below", "spatial_vertical", "high"),
    "beneath": ("below", "spatial_vertical", "high"),
    "behind": ("behind", "spatial_depth", "high"),
    "in back of": ("behind", "spatial_depth", "high"),
    "in the back of": ("behind", "spatial_depth", "high"),
    "in front of": ("in_front_of", "spatial_depth", "high"),
    "in the front of": ("in_front_of", "spatial_depth", "high"),
    "front of": ("in_front_of", "spatial_depth", "medium"),
    "on front of": ("in_front_of", "spatial_depth", "medium"),
    "next to": ("next_to", "spatial_proximity", "high"),
    "beside": ("next_to", "spatial_proximity", "high"),
    "near": ("near", "spatial_proximity", "high"),
    "near to": ("near", "spatial_proximity", "high"),
    "close to": ("near", "spatial_proximity", "high"),
    "by": ("by", "spatial_proximity", "medium"),
    "around": ("around", "spatial_proximity", "high"),
    "surrounding": ("around", "spatial_proximity", "high"),
    "surrounded by": ("surrounded_by", "spatial_proximity", "high"),
    "left of": ("left_of", "spatial_lateral", "high"),
    "to left of": ("left_of", "spatial_lateral", "high"),
    "to the left of": ("left_of", "spatial_lateral", "high"),
    "right of": ("right_of", "spatial_lateral", "high"),
    "to right of": ("right_of", "spatial_lateral", "high"),
    "to the right of": ("right_of", "spatial_lateral", "high"),
    "side of": ("side_of", "spatial_lateral", "medium"),
    "on side of": ("side_of", "spatial_lateral", "medium"),
    # containment / path / region
    "in": ("in", "spatial_containment", "high"),
    "inside": ("inside", "spatial_containment", "high"),
    "inside of": ("inside", "spatial_containment", "high"),
    "within": ("inside", "spatial_containment", "high"),
    "contain": ("contain", "spatial_containment", "high"),
    "contains": ("contain", "spatial_containment", "high"),
    "containing": ("contain", "spatial_containment", "high"),
    "outside": ("outside", "spatial_outside", "high"),
    "outside of": ("outside", "spatial_outside", "high"),
    "between": ("between", "spatial_region", "high"),
    "among": ("among", "spatial_region", "medium"),
    "across": ("across", "spatial_path", "high"),
    "along": ("along", "spatial_path", "medium"),
    "through": ("through", "spatial_path", "high"),
    "at": ("at", "spatial_location", "medium"),
    "at edge of": ("at_edge_of", "spatial_region", "high"),
    "edge of": ("edge_of", "spatial_region", "medium"),
    "middle of": ("middle_of", "spatial_region", "medium"),
    "in middle of": ("middle_of", "spatial_region", "high"),
    "in the middle of": ("middle_of", "spatial_region", "high"),
    "center of": ("center_of", "spatial_region", "medium"),
    "in center of": ("center_of", "spatial_region", "high"),
    "in the center of": ("center_of", "spatial_region", "high"),
    # material / part / possession
    "made of": ("made_of", "material_relation", "high"),
    "made from": ("made_of", "material_relation", "high"),
    "made out of": ("made_of", "material_relation", "high"),
    "composed of": ("made_of", "material_relation", "high"),
    "constructed of": ("made_of", "material_relation", "medium"),
    "built of": ("made_of", "material_relation", "medium"),
    "covered with": ("covered_with", "surface_relation", "high"),
    "covered in": ("covered_with", "surface_relation", "high"),
    "part of": ("part_of", "part_relation", "high"),
    "of": ("of", "part_relation", "medium"),
    "has": ("has", "possession_relation", "high"),
    "have": ("has", "possession_relation", "high"),
    "with": ("with", "association_relation", "medium"),
    "without": ("without", "association_relation", "high"),
    # action / interaction
    "wearing": ("wearing", "wearing_relation", "high"),
    "wears": ("wearing", "wearing_relation", "high"),
    "worn by": ("worn_by", "wearing_relation", "high"),
    "holding": ("holding", "action_relation", "high"),
    "holds": ("holding", "action_relation", "high"),
    "hold": ("holding", "action_relation", "high"),
    "carrying": ("carrying", "action_relation", "high"),
    "riding": ("riding", "action_relation", "high"),
    "ride": ("riding", "action_relation", "high"),
    "plays": ("playing", "action_relation", "high"),
    "playing": ("playing", "action_relation", "high"),
    "interacts with": ("interacts_with", "action_relation", "high"),
    "looking at": ("looking_at", "perception_relation", "high"),
    "watching": ("watching", "perception_relation", "high"),
    "pointing at": ("pointing_at", "action_relation", "high"),
    "facing": ("facing", "orientation_relation", "high"),
}


RELATION_REGEX_RULES: list[tuple[str, str, str, str]] = [
    (r"^(sitting|standing|lying|laying|parked|walking|running) (on|in|near|under|beside|next to)$", "pose_location", "medium", "pose_location"),
    (r"^(hanging|attached|connected|mounted) (from|on|to)$", "attachment_relation", "high", "attachment"),
    (r"^(made|built|constructed|composed) (of|from|out of)$", "material_relation", "high", "material"),
    (r"^(covered) (with|in|by)$", "surface_relation", "high", "surface"),
    (r"^(left|right|front|back|side|edge|middle|center) of$", "spatial_region", "medium", "spatial_region"),
]


def classify_relation(term: str) -> tuple[str, str, str, str]:
    norm = normalize_term(term)
    if norm in MANUAL_RELATION_RULES:
        canonical, relation_type, confidence = MANUAL_RELATION_RULES[norm]
        return canonical, relation_type, confidence, f"manual:{norm}"
    for pattern, relation_type, confidence, rule_id in RELATION_REGEX_RULES:
        if re.match(pattern, norm):
            return slug(norm), relation_type, confidence, f"regex:{rule_id}"
    return slug(norm), "", "low", ""


def parse_vg_aliases(cache_dir: Path) -> tuple[list[dict[str, Any]], dict[str, set[str]], dict[str, str]]:
    path = cached_download(VG_RELATIONSHIP_ALIAS_URL, cache_dir / "visual_genome_relationship_alias.txt")
    rows: list[dict[str, Any]] = []
    canonical_to_aliases: dict[str, set[str]] = defaultdict(set)
    alias_to_group: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        parts = [normalize_term(part) for part in line.split(",") if normalize_term(part)]
        if not parts:
            continue
        group = parts[0]
        for alias in parts:
            canonical_to_aliases[group].add(alias)
            alias_to_group[alias] = group
            rows.append({"alias": alias, "alias_group": group, "source": "visual_genome_relationship_alias"})
    return rows, canonical_to_aliases, alias_to_group


def parse_vg_synsets(cache_dir: Path) -> dict[str, str]:
    path = cached_download(VG_RELATIONSHIP_SYNSETS_URL, cache_dir / "visual_genome_relationship_synsets.json.zip")
    with zipfile.ZipFile(path) as archive:
        data = json.loads(archive.read("relationship_synsets.json"))
    return {normalize_term(term): synset for term, synset in data.items() if normalize_term(term)}


def parse_vg_relationship_counts(cache_dir: Path) -> tuple[Counter[str], dict[str, set[str]]]:
    path = cached_download(VG_RELATIONSHIPS_URL, cache_dir / "visual_genome_relationships.json.zip")
    counts: Counter[str] = Counter()
    synsets: dict[str, set[str]] = defaultdict(set)
    with zipfile.ZipFile(path) as archive:
        data = json.loads(archive.read("relationships.json"))
    for image_row in data:
        for rel in image_row.get("relationships", []):
            term = normalize_term(rel.get("predicate", ""))
            if not term:
                continue
            counts[term] += 1
            for synset in rel.get("synsets", []) or []:
                if synset:
                    synsets[term].add(synset)
    return counts, synsets


def parse_openimages_triplets(cache_dir: Path) -> Counter[str]:
    path = cached_download(OPEN_IMAGES_RELATION_TRIPLETS_URL, cache_dir / "openimages_v6_relationship_triplets.csv")
    counts: Counter[str] = Counter()
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            term = normalize_term(row["RelationshipLabel"])
            if term:
                counts[term] += 1
    return counts


def parse_streusle_mwe_candidates(cache_dir: Path) -> set[str]:
    path = cached_download(STREUSLE_CONLLU_URL, cache_dir / "streusle.conllu")
    candidates: set[str] = set()
    prep_words = {
        "of",
        "in",
        "on",
        "at",
        "to",
        "from",
        "with",
        "without",
        "under",
        "over",
        "above",
        "below",
        "behind",
        "front",
        "between",
        "against",
        "through",
        "around",
        "inside",
        "outside",
        "next",
        "near",
    }
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 10:
            continue
        misc = parts[9]
        for match in re.finditer(r"MWELemma(?:\[[^\]]+\])?=([^|]+)", misc):
            term = normalize_term(match.group(1))
            if "<" in term:
                continue
            words = set(term.split())
            if len(words) < 2 or not (words & prep_words):
                continue
            _, relation_type, _, _ = classify_relation(term)
            if relation_type:
                candidates.add(term)
    return candidates


def add_candidate(
    grouped: dict[str, list[dict[str, Any]]],
    *,
    term: str,
    source: str,
    vg_count: int = 0,
    openimages_triplet_count: int = 0,
    synsets: set[str] | None = None,
    alias_group: str = "",
    provenance: str = "",
) -> None:
    term = normalize_term(term)
    if not term:
        return
    canonical, relation_type, confidence, rule_id = classify_relation(term)
    if not relation_type:
        return
    if source in {"visual_genome_relationship_count", "visual_genome_relationship_alias"} and vg_count >= 100:
        confidence = "high" if confidence != "low" else "medium"
    if source == "openimages_relationship_triplet":
        confidence = "high" if confidence != "low" else "medium"
    grouped[term].append(
        {
            "term": term,
            "canonical": canonical,
            "relation_type": relation_type,
            "confidence": confidence,
            "source": source,
            "vg_count": vg_count,
            "openimages_triplet_count": openimages_triplet_count,
            "synsets": synsets or set(),
            "alias_group": alias_group,
            "rule_id": rule_id,
            "provenance": provenance or source,
        }
    )


def merge_candidates(grouped: dict[str, list[dict[str, Any]]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for term in sorted(grouped):
        items = grouped[term]
        canonical = max((item["canonical"] for item in items), key=lambda value: sum(1 for item in items if item["canonical"] == value))
        relation_type = max((item["relation_type"] for item in items), key=lambda value: sum(1 for item in items if item["relation_type"] == value))
        confidence = max((item["confidence"] for item in items), key=confidence_rank)
        sources = sorted({item["source"] for item in items})
        vg_count = max(int(item["vg_count"]) for item in items)
        oi_count = max(int(item["openimages_triplet_count"]) for item in items)
        synsets = sorted({synset for item in items for synset in item["synsets"] if synset})
        alias_groups = sorted({item["alias_group"] for item in items if item["alias_group"]})
        rule_ids = sorted({item["rule_id"] for item in items if item["rule_id"]})
        provenance = sorted({item["provenance"] for item in items if item["provenance"]})
        rows.append(
            {
                "term": term,
                "canonical": canonical,
                "relation_type": relation_type,
                "confidence": confidence,
                "is_multiword": is_multiword(term),
                "sources": "|".join(sources),
                "vg_count": str(vg_count),
                "openimages_triplet_count": str(oi_count),
                "synsets": "|".join(synsets),
                "alias_group": "|".join(alias_groups),
                "rule_id": "|".join(rule_ids),
                "provenance": "|".join(provenance),
            }
        )
    return rows


def build_lexicons(cache_dir: Path) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    alias_rows, canonical_to_aliases, alias_to_group = parse_vg_aliases(cache_dir)
    vg_synsets = parse_vg_synsets(cache_dir)
    vg_counts, vg_count_synsets = parse_vg_relationship_counts(cache_dir)
    openimages_counts = parse_openimages_triplets(cache_dir)
    streusle_mwes = parse_streusle_mwe_candidates(cache_dir)

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for term, count in vg_counts.items():
        synsets = set()
        if term in vg_synsets:
            synsets.add(vg_synsets[term])
        synsets.update(vg_count_synsets.get(term, set()))
        add_candidate(
            grouped,
            term=term,
            source="visual_genome_relationship_count",
            vg_count=count,
            synsets=synsets,
            alias_group=alias_to_group.get(term, ""),
        )

    for group, aliases in canonical_to_aliases.items():
        group_count = max(vg_counts.get(alias, 0) for alias in aliases)
        for alias in aliases:
            add_candidate(
                grouped,
                term=alias,
                source="visual_genome_relationship_alias",
                vg_count=max(vg_counts.get(alias, 0), group_count),
                alias_group=group,
                synsets={vg_synsets[alias]} if alias in vg_synsets else set(),
            )

    for term, count in openimages_counts.items():
        add_candidate(
            grouped,
            term=term,
            source="openimages_relationship_triplet",
            openimages_triplet_count=count,
        )

    for term in streusle_mwes:
        add_candidate(grouped, term=term, source="streusle_mwe", provenance="streusle_mwe")

    for term in MANUAL_RELATION_RULES:
        add_candidate(grouped, term=term, source="manual_relation_seed", provenance="manual_relation_seed")

    candidates = merge_candidates(grouped)
    multiword = [row for row in candidates if row["is_multiword"] == "yes"]
    clean_core = [
        row
        for row in candidates
        if row["confidence"] == "high"
        and (
            "openimages_relationship_triplet" in split_pipe(row["sources"])
            or "manual_relation_seed" in split_pipe(row["sources"])
            or int(row["vg_count"] or 0) >= 100
        )
    ]

    predicate_rows = [
        {
            "term": term,
            "count": count,
            "synsets": "|".join(sorted(vg_count_synsets.get(term, set()) | ({vg_synsets[term]} if term in vg_synsets else set()))),
            "alias_group": alias_to_group.get(term, ""),
        }
        for term, count in vg_counts.most_common()
    ]
    openimages_rows = [{"term": term, "triplet_count": count} for term, count in sorted(openimages_counts.items())]
    return candidates, multiword, clean_core, alias_rows, predicate_rows, openimages_rows


def relation_type_counts(rows: list[dict[str, str]]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for row in rows:
        counts[row["relation_type"]] += 1
    return counts


def write_report(path: Path, candidates: list[dict[str, str]], multiword: list[dict[str, str]], clean_core: list[dict[str, str]], predicate_rows: list[dict[str, Any]], alias_rows: list[dict[str, Any]], openimages_rows: list[dict[str, Any]]) -> None:
    type_counts = relation_type_counts(clean_core)
    examples = ["on top of", "in front of", "next to", "made of", "covered with", "hanging from", "attached to"]
    lookup = {row["term"]: row for row in candidates}
    lines = [
        "# Relation Span Lexicon Summary",
        "",
        "Visual Genome relationships, Visual Genome relationship aliases/synsets, Open Images relationship triplets, and STREUSLE MWE annotations를 사용해 relation span 후보를 만든 결과입니다.",
        "",
        "## Output Files",
        "",
        "- `resources/lexicons/relation_span_candidates.tsv`: classified relation span 후보 전체",
        "- `resources/lexicons/relation_multiword_span_candidates.tsv`: multi-word relation span 후보",
        "- `resources/lexicons/relation_span_clean_core.tsv`: high-confidence parser lookup 후보",
        "- `resources/lexicons/visual_genome_relation_predicates.tsv`: Visual Genome predicate frequency",
        "- `resources/lexicons/visual_genome_relation_aliases.tsv`: Visual Genome alias mapping",
        "- `resources/lexicons/openimages_relation_predicates.tsv`: Open Images relationship predicate vocabulary",
        "",
        "## Counts",
        "",
        "| item | count |",
        "|---|---:|",
        f"| Visual Genome unique predicates | {len(predicate_rows)} |",
        f"| Visual Genome alias rows | {len(alias_rows)} |",
        f"| Open Images relation predicates | {len(openimages_rows)} |",
        f"| relation span candidates | {len(candidates)} |",
        f"| multi-word span candidates | {len(multiword)} |",
        f"| clean core relation spans | {len(clean_core)} |",
        "",
        "## Clean Core Relation Types",
        "",
        "| relation_type | terms |",
        "|---|---:|",
    ]
    for relation_type, count in sorted(type_counts.items()):
        lines.append(f"| {relation_type} | {count} |")
    lines.extend(["", "## Key Examples", "", "| term | canonical | relation_type | confidence | sources | vg_count |", "|---|---|---|---|---|---:|"])
    for term in examples:
        row = lookup.get(term)
        if row:
            lines.append(
                f"| `{term}` | `{row['canonical']}` | `{row['relation_type']}` | {row['confidence']} | {row['sources']} | {row['vg_count']} |"
            )
        else:
            lines.append(f"| `{term}` | - | - | - | - | - |")
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- Visual Genome alias는 유용하지만 noisy합니다. 예: `near a farm`, `four` 같은 row가 있으므로 rule-classified term만 후보에 넣었습니다.",
            "- Open Images triplet predicate는 작지만 high precision source로 취급했습니다.",
            "- STREUSLE는 visual relation vocabulary가 아니라 MWE/preposition annotation 근거입니다. 이번 파일에서는 rule과 맞는 MWE만 보조 source로 들어갑니다.",
            "- `on top of` 같은 phrase는 parser 전 retokenize/masking 후보가 아니라, 8단계 raw tuple extraction에서 relation span으로 읽기 위한 lookup 후보입니다.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build relation span lexicons from Visual Genome, Open Images, and STREUSLE.")
    parser.add_argument("--cache-dir", type=Path, default=Path("resources/external/cache"))
    parser.add_argument("--output-dir", type=Path, default=Path("resources/lexicons"))
    parser.add_argument("--report", type=Path, default=Path("reports/relation_span_lexicon_summary.md"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    candidates, multiword, clean_core, alias_rows, predicate_rows, openimages_rows = build_lexicons(args.cache_dir)
    write_tsv(args.output_dir / "relation_span_candidates.tsv", candidates, FIELDNAMES)
    write_tsv(args.output_dir / "relation_multiword_span_candidates.tsv", multiword, FIELDNAMES)
    write_tsv(args.output_dir / "relation_span_clean_core.tsv", clean_core, FIELDNAMES)
    write_tsv(args.output_dir / "visual_genome_relation_aliases.tsv", alias_rows, ["alias", "alias_group", "source"])
    write_tsv(args.output_dir / "visual_genome_relation_predicates.tsv", predicate_rows, ["term", "count", "synsets", "alias_group"])
    write_tsv(args.output_dir / "openimages_relation_predicates.tsv", openimages_rows, ["term", "triplet_count"])
    write_report(args.report, candidates, multiword, clean_core, predicate_rows, alias_rows, openimages_rows)
    print(f"relation span candidates: {len(candidates)}")
    print(f"multi-word span candidates: {len(multiword)}")
    print(f"clean core relation spans: {len(clean_core)}")
    print(f"wrote: {args.output_dir / 'relation_span_candidates.tsv'}")
    print(f"wrote: {args.output_dir / 'relation_multiword_span_candidates.tsv'}")
    print(f"wrote: {args.output_dir / 'relation_span_clean_core.tsv'}")
    print(f"wrote: {args.report}")


if __name__ == "__main__":
    main()
