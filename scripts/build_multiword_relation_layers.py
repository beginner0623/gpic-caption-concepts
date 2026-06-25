from __future__ import annotations

import argparse
import csv
import json
import re
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from build_relation_span_lexicon import (
    MANUAL_RELATION_RULES,
    STREUSLE_CONLLU_URL,
    build_lexicons,
    cached_download,
    normalize_term,
    split_pipe,
    write_tsv,
)


GQA_SCENE_GRAPHS_URL = "https://downloads.cs.stanford.edu/nlp/data/gqa/sceneGraphs.zip"
GQA_WHITELIST_COUNT_THRESHOLD = 100

SURFACE_FIELDNAMES = [
    "term",
    "canonical",
    "surface_sources",
    "source_detail",
    "is_multiword",
    "confidence",
    "visual_whitelist",
    "vg_count",
    "gqa_count",
    "openimages_triplet_count",
]

SEMANTIC_FIELDNAMES = [
    "term",
    "canonical",
    "project_relation_type",
    "snacs_supersenses",
    "semantic_sources",
    "confidence",
    "notes",
]

COLLAPSE_FIELDNAMES = [
    "term",
    "canonical",
    "collapse_strategy",
    "matcher_type",
    "ud_reference",
    "spacy_rule_hint",
    "project_relation_type",
    "confidence",
]

VISUAL_FIELDNAMES = [
    "term",
    "canonical",
    "project_relation_type",
    "visual_whitelist",
    "visual_sources",
    "vg_count",
    "gqa_count",
    "openimages_triplet_count",
    "confidence",
]

FINAL_FIELDNAMES = [
    "term",
    "canonical",
    "project_relation_type",
    "snacs_supersenses",
    "collapse_strategy",
    "matcher_type",
    "surface_sources",
    "visual_sources",
    "vg_count",
    "gqa_count",
    "openimages_triplet_count",
    "confidence",
]

GQA_FIELDNAMES = ["predicate", "count", "is_multiword"]


SNACS_BY_PROJECT_RELATION = {
    "spatial_support": "p.Locus",
    "spatial_contact": "p.Locus",
    "spatial_containment": "p.Locus",
    "spatial_depth": "p.Locus",
    "spatial_lateral": "p.Locus",
    "spatial_location": "p.Locus",
    "spatial_outside": "p.Locus",
    "spatial_proximity": "p.Locus",
    "spatial_region": "p.Locus",
    "spatial_vertical": "p.Locus",
    "spatial_path": "p.Path",
    "material_relation": "p.Stuff",
    "part_relation": "p.Whole",
    "possession_relation": "p.Gestalt",
    "association_relation": "p.Circumstance",
    "attachment_relation": "p.Locus",
    "surface_relation": "p.Locus",
}


TPP_PDEP_VISUAL_SURFACE_SEEDS = {
    term
    for term in MANUAL_RELATION_RULES
    if len(normalize_term(term).split()) > 1
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def mwe_relation_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    return [row for row in rows if row.get("is_multiword") == "yes"]


def visual_sources(row: dict[str, str], gqa_count: int) -> list[str]:
    sources = [
        source
        for source in split_pipe(row.get("sources", ""))
        if source in {"visual_genome_relationship_alias", "visual_genome_relationship_count", "openimages_relationship_triplet"}
    ]
    if gqa_count > 0:
        sources.append("gqa_scene_graph_relation_count")
    return sources


def surface_sources(row: dict[str, str], gqa_count: int) -> list[str]:
    sources = set()
    raw_sources = set(split_pipe(row.get("sources", "")))
    term = row["term"]
    if term in TPP_PDEP_VISUAL_SURFACE_SEEDS or "manual_relation_seed" in raw_sources:
        sources.add("tpp_pdep_visual_seed")
    if "streusle_mwe" in raw_sources:
        sources.add("streusle_mwe")
    if "visual_genome_relationship_alias" in raw_sources:
        sources.add("visual_genome_relationship_alias")
    if "visual_genome_relationship_count" in raw_sources:
        sources.add("visual_genome_predicate_surface")
    if "openimages_relationship_triplet" in raw_sources:
        sources.add("openimages_predicate_surface")
    if gqa_count > 0:
        sources.add("gqa_scene_graph_relation_surface")
    return sorted(sources)


def parse_streusle_snacs(cache_dir: Path) -> dict[str, Counter[str]]:
    path = cached_download(STREUSLE_CONLLU_URL, cache_dir / "streusle.conllu")
    snacs: dict[str, Counter[str]] = defaultdict(Counter)
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 10:
            continue
        lemma = normalize_term(parts[2])
        misc = parts[9]
        supersenses = set(re.findall(r"Supersense(?:\[[^\]]+\])?=(p\.[A-Za-z]+)", misc))
        if not supersenses:
            continue
        terms = {lemma}
        for match in re.finditer(r"MWELemma(?:\[[^\]]+\])?=([^|]+)", misc):
            mwe = normalize_term(match.group(1))
            if "<" not in mwe:
                terms.add(mwe)
        for term in terms:
            if not term:
                continue
            for supersense in supersenses:
                snacs[term][supersense] += 1
    return snacs


def parse_gqa_relation_counts(cache_dir: Path) -> Counter[str]:
    path = cached_download(GQA_SCENE_GRAPHS_URL, cache_dir / "gqa_sceneGraphs.zip")
    counts: Counter[str] = Counter()
    with zipfile.ZipFile(path) as archive:
        names = [name for name in archive.namelist() if name.lower().endswith(".json")]
        for name in names:
            scene_graphs = json.loads(archive.read(name).decode("utf-8"))
            for graph in scene_graphs.values():
                objects = graph.get("objects", {})
                for obj in objects.values():
                    relations = obj.get("relations", [])
                    if isinstance(relations, dict):
                        relation_iter = relations.values()
                    else:
                        relation_iter = relations
                    for relation in relation_iter:
                        if not isinstance(relation, dict):
                            continue
                        predicate = normalize_term(str(relation.get("name", "")))
                        if predicate:
                            counts[predicate] += 1
    return counts


def gqa_rows(gqa_counts: Counter[str]) -> list[dict[str, Any]]:
    rows = []
    for predicate, count in sorted(gqa_counts.items()):
        rows.append(
            {
                "predicate": predicate,
                "count": count,
                "is_multiword": "yes" if len(predicate.split()) > 1 else "no",
            }
        )
    return rows


def snacs_for_row(row: dict[str, str], streusle_snacs: dict[str, Counter[str]]) -> list[str]:
    term = row["term"]
    supersenses = set(streusle_snacs.get(term, Counter()).keys())
    projected = SNACS_BY_PROJECT_RELATION.get(row["relation_type"])
    if projected:
        supersenses.add(projected)
    return sorted(supersenses)


def collapse_rule_for(row: dict[str, str]) -> tuple[str, str, str, str]:
    term = row["term"]
    relation_type = row["relation_type"]
    words = term.split()

    region_words = {"front", "back", "left", "right", "side", "edge", "middle", "center", "top"}
    first_word = words[0] if words else ""

    if relation_type in {"material_relation", "surface_relation", "attachment_relation"}:
        return (
            "predicate_plus_adposition",
            "DependencyMatcher + PhraseMatcher fallback",
            "VERB/ADJ + ADP/case/obl; UD may use fixed for complex ADP tails",
            "match relation head plus following preposition span; canonicalize full surface",
        )
    if relation_type in {"pose_location", "pose_support", "state_support", "wearing_relation", "action_relation", "perception_relation"}:
        return (
            "predicate_plus_adposition_or_object",
            "DependencyMatcher",
            "VERB/VBG/VBN predicate with pobj/obl/dobj argument",
            "match predicate lemma and attached preposition/object argument",
        )
    if any(word in region_words for word in words) or first_word in {"in", "to", "at", "on"} and len(words) >= 3:
        return (
            "complex_preposition_phrase",
            "PhraseMatcher longest span + dependency validation",
            "UD fixed/case chain, often ADP + DET? + NOUN + ADP",
            "pre-detect longest phrase, then bind left/right noun chunks in raw tuple extraction",
        )
    if relation_type.startswith("spatial_"):
        return (
            "multiword_adposition_phrase",
            "PhraseMatcher longest span",
            "UD fixed or case chain",
            "match longest surface span before interpreting dependency edges",
        )
    return (
        "multiword_relation_phrase",
        "PhraseMatcher longest span",
        "UD fixed/MWE reference",
        "match full surface span as relation candidate",
    )


def build_layer_rows(
    candidates: list[dict[str, str]],
    clean_core: list[dict[str, str]],
    streusle_snacs: dict[str, Counter[str]],
    gqa_counts: Counter[str],
) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    clean_terms = {row["term"] for row in clean_core}
    multiword_candidates = mwe_relation_rows(candidates)

    surface_rows: list[dict[str, str]] = []
    semantic_rows: list[dict[str, str]] = []
    collapse_rows: list[dict[str, str]] = []
    visual_rows: list[dict[str, str]] = []
    final_rows: list[dict[str, str]] = []

    for row in multiword_candidates:
        term = row["term"]
        gqa_count = gqa_counts.get(term, 0)
        src_surface = surface_sources(row, gqa_count)
        src_visual = visual_sources(row, gqa_count)
        is_clean = "yes" if term in clean_terms or gqa_count >= GQA_WHITELIST_COUNT_THRESHOLD else "no"
        snacs = snacs_for_row(row, streusle_snacs)
        semantic_sources = []
        if term in streusle_snacs:
            semantic_sources.append("streusle_snacs")
        if row["relation_type"] in SNACS_BY_PROJECT_RELATION:
            semantic_sources.append("project_relation_to_snacs_mapping")
        semantic_sources.append("project_visual_relation_type")

        collapse_strategy, matcher_type, ud_reference, spacy_rule_hint = collapse_rule_for(row)

        surface_rows.append(
            {
                "term": term,
                "canonical": row["canonical"],
                "surface_sources": "|".join(src_surface),
                "source_detail": row["sources"],
                "is_multiword": row["is_multiword"],
                "confidence": row["confidence"],
                "visual_whitelist": is_clean,
                "vg_count": row["vg_count"],
                "gqa_count": str(gqa_count),
                "openimages_triplet_count": row["openimages_triplet_count"],
            }
        )
        semantic_rows.append(
            {
                "term": term,
                "canonical": row["canonical"],
                "project_relation_type": row["relation_type"],
                "snacs_supersenses": "|".join(snacs),
                "semantic_sources": "|".join(sorted(set(semantic_sources))),
                "confidence": row["confidence"],
                "notes": "SNACS is a general-language adposition semantic layer; project_relation_type is the visual relation schema.",
            }
        )
        collapse_rows.append(
            {
                "term": term,
                "canonical": row["canonical"],
                "collapse_strategy": collapse_strategy,
                "matcher_type": matcher_type,
                "ud_reference": ud_reference,
                "spacy_rule_hint": spacy_rule_hint,
                "project_relation_type": row["relation_type"],
                "confidence": row["confidence"],
            }
        )
        visual_rows.append(
            {
                "term": term,
                "canonical": row["canonical"],
                "project_relation_type": row["relation_type"],
                "visual_whitelist": is_clean,
                "visual_sources": "|".join(src_visual),
                "vg_count": row["vg_count"],
                "gqa_count": str(gqa_count),
                "openimages_triplet_count": row["openimages_triplet_count"],
                "confidence": row["confidence"],
            }
        )
        if is_clean == "yes":
            final_rows.append(
                {
                    "term": term,
                    "canonical": row["canonical"],
                    "project_relation_type": row["relation_type"],
                    "snacs_supersenses": "|".join(snacs),
                    "collapse_strategy": collapse_strategy,
                    "matcher_type": matcher_type,
                    "surface_sources": "|".join(src_surface),
                    "visual_sources": "|".join(src_visual),
                    "vg_count": row["vg_count"],
                    "gqa_count": str(gqa_count),
                    "openimages_triplet_count": row["openimages_triplet_count"],
                    "confidence": row["confidence"],
                }
            )

    return surface_rows, semantic_rows, collapse_rows, visual_rows, final_rows


def counter_from(rows: list[dict[str, str]], key: str) -> Counter[str]:
    counts: Counter[str] = Counter()
    for row in rows:
        for item in split_pipe(row.get(key, "")):
            counts[item] += 1
    return counts


def write_report(
    path: Path,
    surface_rows: list[dict[str, str]],
    semantic_rows: list[dict[str, str]],
    collapse_rows: list[dict[str, str]],
    visual_rows: list[dict[str, str]],
    final_rows: list[dict[str, str]],
) -> None:
    surface_counts = counter_from(surface_rows, "surface_sources")
    visual_source_counts = counter_from(visual_rows, "visual_sources")
    visual_whitelist = Counter(row["visual_whitelist"] for row in visual_rows)
    collapse_counts = Counter(row["collapse_strategy"] for row in collapse_rows)
    relation_counts = Counter(row["project_relation_type"] for row in final_rows)

    lines = [
        "# Multiword Relation Lexicon Layers",
        "",
        "추천 구조에 맞춰 multi-word relation lexicon을 surface, semantic subtype, collapse rule, visual whitelist layer로 분리한 결과입니다.",
        "",
        "## Output Files",
        "",
        "- `resources/lexicons/multiword_relation_surface_forms.tsv`",
        "- `resources/lexicons/multiword_relation_semantic_subtypes.tsv`",
        "- `resources/lexicons/multiword_relation_collapse_rules.tsv`",
        "- `resources/lexicons/multiword_relation_visual_whitelist.tsv`",
        "- `resources/lexicons/multiword_relation_clean_core.tsv`",
        "",
        "## Counts",
        "",
        "| layer | rows |",
        "|---|---:|",
        f"| surface forms | {len(surface_rows)} |",
        f"| semantic subtypes | {len(semantic_rows)} |",
        f"| collapse rules | {len(collapse_rows)} |",
        f"| visual whitelist rows | {len(visual_rows)} |",
        f"| final clean multiword relations | {len(final_rows)} |",
        "",
        "## Surface Sources",
        "",
        "| source | rows |",
        "|---|---:|",
    ]
    for source, count in sorted(surface_counts.items()):
        lines.append(f"| {source} | {count} |")
    lines.extend(["", "## Visual Sources", "", "| source | rows |", "|---|---:|"])
    for source, count in sorted(visual_source_counts.items()):
        lines.append(f"| {source} | {count} |")
    lines.extend(["", "## Visual Whitelist", "", "| whitelist | rows |", "|---|---:|"])
    for key, count in sorted(visual_whitelist.items()):
        lines.append(f"| {key} | {count} |")
    lines.extend(["", "## Collapse Strategies", "", "| strategy | rows |", "|---|---:|"])
    for strategy, count in sorted(collapse_counts.items()):
        lines.append(f"| {strategy} | {count} |")
    lines.extend(["", "## Final Relation Types", "", "| relation_type | rows |", "|---|---:|"])
    for relation_type, count in sorted(relation_counts.items()):
        lines.append(f"| {relation_type} | {count} |")
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- `surface_forms`는 phrase 후보 출처를 분리합니다. PDEP/TPP는 현재 자동 원본 파싱 대신 visual relation seed source로 기록했습니다.",
            "- `semantic_subtypes`는 STREUSLE/SNACS가 있으면 `snacs_supersenses`에 남기고, 없으면 project visual relation type을 기준으로 둡니다.",
            "- `collapse_rules`는 UD fixed/MWE를 참고한 spaCy용 구현 힌트입니다. spaCy label과 UD label이 완전히 같다는 뜻은 아닙니다.",
            "- `visual_whitelist`는 VG/GQA/OpenImages frequency 및 manual visual seed를 바탕으로 실제 caption/image relation으로 쓸지를 나눕니다.",
            f"- GQA만으로 whitelist를 올릴 때는 `gqa_count >= {GQA_WHITELIST_COUNT_THRESHOLD}` 기준을 사용했습니다.",
            "- `multiword_relation_clean_core.tsv`가 8단계 relation span detection에 바로 연결할 1차 파일입니다.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Split multiword relation lexicon into surface/semantic/collapse/visual layers.")
    parser.add_argument("--cache-dir", type=Path, default=Path("resources/external/cache"))
    parser.add_argument("--output-dir", type=Path, default=Path("resources/lexicons"))
    parser.add_argument("--report", type=Path, default=Path("reports/multiword_relation_layers_summary.md"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    candidates, _multiword, clean_core, _alias_rows, _predicate_rows, _openimages_rows = build_lexicons(args.cache_dir)
    streusle_snacs = parse_streusle_snacs(args.cache_dir)
    gqa_counts = parse_gqa_relation_counts(args.cache_dir)
    surface_rows, semantic_rows, collapse_rows, visual_rows, final_rows = build_layer_rows(candidates, clean_core, streusle_snacs, gqa_counts)

    write_tsv(args.output_dir / "multiword_relation_surface_forms.tsv", surface_rows, SURFACE_FIELDNAMES)
    write_tsv(args.output_dir / "multiword_relation_semantic_subtypes.tsv", semantic_rows, SEMANTIC_FIELDNAMES)
    write_tsv(args.output_dir / "multiword_relation_collapse_rules.tsv", collapse_rows, COLLAPSE_FIELDNAMES)
    write_tsv(args.output_dir / "multiword_relation_visual_whitelist.tsv", visual_rows, VISUAL_FIELDNAMES)
    write_tsv(args.output_dir / "multiword_relation_clean_core.tsv", final_rows, FINAL_FIELDNAMES)
    write_tsv(args.output_dir / "gqa_relation_predicates.tsv", gqa_rows(gqa_counts), GQA_FIELDNAMES)
    write_report(args.report, surface_rows, semantic_rows, collapse_rows, visual_rows, final_rows)

    print(f"gqa relation predicates: {len(gqa_counts)}")
    print(f"surface forms: {len(surface_rows)}")
    print(f"semantic subtypes: {len(semantic_rows)}")
    print(f"collapse rules: {len(collapse_rows)}")
    print(f"visual whitelist rows: {len(visual_rows)}")
    print(f"final clean multiword relations: {len(final_rows)}")
    print(f"wrote: {args.report}")


if __name__ == "__main__":
    main()
