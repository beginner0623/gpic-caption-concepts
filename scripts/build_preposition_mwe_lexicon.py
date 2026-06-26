from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass, field
from pathlib import Path


LEXICON_DIR = Path("resources/lexicons")
MIXED_RELATION_RULES = LEXICON_DIR / "multiword_relation_collapse_rules.tsv"
PREPOSITION_MWE_CANDIDATES = LEXICON_DIR / "preposition_mwe_candidates.tsv"
PREPOSITION_MWE_CLEAN_CORE = LEXICON_DIR / "preposition_mwe_clean_core.tsv"
PREPOSITION_MWE_AUDIT_FLAGS = LEXICON_DIR / "preposition_mwe_audit_flags.tsv"

CLEAN_FIELDNAMES = [
    "term",
    "canonical",
    "relation_type",
    "pattern",
    "middle",
    "final_adp",
    "confidence",
    "source",
    "notes",
]

CANDIDATE_FIELDNAMES = CLEAN_FIELDNAMES + [
    "decision",
    "reason",
    "source_detail",
]

AUDIT_FIELDNAMES = [
    "term",
    "canonical",
    "relation_type",
    "pattern",
    "decision",
    "reason",
    "source",
    "source_detail",
    "notes",
]

ALLOWED_MIXED_STRATEGIES = {
    "complex_preposition_phrase",
    "multiword_adposition_phrase",
}

PREDICATE_HEADS = {
    "attached",
    "built",
    "composed",
    "connected",
    "constructed",
    "covered",
    "decorated",
    "filled",
    "hanging",
    "interacts",
    "laying",
    "leaning",
    "looking",
    "lying",
    "made",
    "mounted",
    "painted",
    "parked",
    "pointing",
    "printed",
    "running",
    "sitting",
    "standing",
    "surrounded",
    "walking",
    "written",
}

NON_VISUAL_ADPOSITIONS = {
    "according to",
    "because of",
    "due to",
    "instead of",
    "in addition to",
    "in case of",
    "in lieu of",
    "in spite of",
    "regardless of",
    "with respect to",
}

ADPOSITION_OF_HEADS = {
    "ahead",
    "alongside",
    "inside",
    "off",
    "opposite",
    "out",
    "outside",
}

RELATION_CONFIDENCE_RANK = {"high": 3, "medium": 2, "low": 1}


@dataclass
class Candidate:
    term: str
    canonical: str
    relation_type: str
    pattern: str
    middle: str
    final_adp: str
    confidence: str
    sources: set[str] = field(default_factory=set)
    source_details: set[str] = field(default_factory=set)
    notes: set[str] = field(default_factory=set)


def normalize(text: str) -> str:
    text = str(text).strip().lower().replace("_", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def canonical_slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", normalize(text)).strip("_")


def better_confidence(left: str, right: str) -> str:
    if RELATION_CONFIDENCE_RANK.get(right, 0) > RELATION_CONFIDENCE_RANK.get(left, 0):
        return right
    return left


def infer_pattern(term: str) -> tuple[str, str, str]:
    words = normalize(term).split()
    if len(words) < 2:
        return "", "", ""
    final_adp = words[-1]
    if final_adp == "of":
        if len(words) >= 4 and words[-3] in {"the", "a", "an"}:
            return "adp_det_mid_of", words[-2], final_adp
        if len(words) == 3:
            return "adp_mid_of", words[-2], final_adp
        if len(words) == 2 and words[0] in ADPOSITION_OF_HEADS:
            return "adp_of", words[0], final_adp
        if len(words) == 2:
            return "mid_of", words[0], final_adp
        return "adp_mid_of", words[-2], final_adp
    if len(words) == 2:
        return "adp_adp", words[0], final_adp
    if len(words) == 3 and words[1] in {"the", "a", "an"}:
        return "adp_det_adp", words[0], final_adp
    return "multiword_adposition", words[-2], final_adp


def add_candidate(
    candidates: dict[str, Candidate],
    term: str,
    canonical: str,
    relation_type: str,
    confidence: str,
    source: str,
    source_detail: str,
    notes: str = "",
) -> None:
    term = normalize(term)
    if not term or " " not in term:
        return
    pattern, middle, final_adp = infer_pattern(term)
    if not pattern:
        return
    canonical = canonical or canonical_slug(term)
    relation_type = relation_type or "spatial_relation"
    confidence = confidence or "medium"
    if term not in candidates:
        candidates[term] = Candidate(
            term=term,
            canonical=canonical,
            relation_type=relation_type,
            pattern=pattern,
            middle=middle,
            final_adp=final_adp,
            confidence=confidence,
        )
    candidate = candidates[term]
    candidate.confidence = better_confidence(candidate.confidence, confidence)
    if RELATION_CONFIDENCE_RANK.get(confidence, 0) > RELATION_CONFIDENCE_RANK.get(candidate.confidence, 0):
        candidate.canonical = canonical
        candidate.relation_type = relation_type
    candidate.sources.add(source)
    if source_detail:
        candidate.source_details.add(source_detail)
    if notes:
        candidate.notes.add(notes)


def add_region_candidates(candidates: dict[str, Candidate]) -> None:
    def add(term: str, canonical: str, relation_type: str, confidence: str = "high", note: str = "generated spatial region pattern") -> None:
        add_candidate(
            candidates,
            term,
            canonical,
            relation_type,
            confidence,
            "generated_region_pattern",
            note,
            note,
        )

    region_groups = {
        "top": {
            "bare": ("at_top_of", "spatial_region", "medium"),
            "at": ("at_top_of", "spatial_region", "high"),
            "on": ("on_top_of", "spatial_support", "high"),
            "from": ("from_top_of", "spatial_source", "medium"),
            "near": ("near_top_of", "spatial_region", "medium"),
        },
        "bottom": {
            "bare": ("bottom_of", "spatial_region", "medium"),
            "at": ("bottom_of", "spatial_region", "high"),
            "on": ("bottom_of", "spatial_region", "high"),
            "from": ("from_bottom_of", "spatial_source", "medium"),
            "near": ("near_bottom_of", "spatial_region", "medium"),
        },
        "front": {
            "bare": ("in_front_of", "spatial_depth", "high"),
            "in": ("in_front_of", "spatial_depth", "high"),
            "at": ("at_front_of", "spatial_region", "medium"),
            "on": ("in_front_of", "spatial_depth", "medium"),
            "from": ("from_front_of", "spatial_source", "medium"),
            "near": ("near_front_of", "spatial_region", "medium"),
        },
        "back": {
            "bare": ("behind", "spatial_depth", "medium"),
            "in": ("behind", "spatial_depth", "high"),
            "at": ("at_back_of", "spatial_region", "medium"),
            "on": ("at_back_of", "spatial_region", "medium"),
            "from": ("from_back_of", "spatial_source", "medium"),
            "near": ("near_back_of", "spatial_region", "medium"),
        },
        "side": {
            "bare": ("side_of", "spatial_lateral", "high"),
            "at": ("side_of", "spatial_lateral", "medium"),
            "on": ("side_of", "spatial_lateral", "high"),
            "by": ("side_of", "spatial_lateral", "medium"),
            "from": ("from_side_of", "spatial_source", "medium"),
            "near": ("near_side_of", "spatial_region", "medium"),
            "along": ("along_side_of", "spatial_path", "medium"),
        },
        "edge": {
            "bare": ("edge_of", "spatial_region", "medium"),
            "at": ("at_edge_of", "spatial_region", "high"),
            "on": ("edge_of", "spatial_region", "medium"),
            "from": ("from_edge_of", "spatial_source", "medium"),
            "near": ("near_edge_of", "spatial_region", "high"),
            "along": ("along_edge_of", "spatial_path", "medium"),
        },
        "center": {
            "bare": ("center_of", "spatial_region", "medium"),
            "in": ("center_of", "spatial_region", "high"),
            "at": ("center_of", "spatial_region", "high"),
            "from": ("from_center_of", "spatial_source", "medium"),
            "near": ("near_center_of", "spatial_region", "medium"),
        },
        "middle": {
            "bare": ("middle_of", "spatial_region", "medium"),
            "in": ("middle_of", "spatial_region", "high"),
            "at": ("middle_of", "spatial_region", "high"),
            "from": ("from_middle_of", "spatial_source", "medium"),
            "near": ("near_middle_of", "spatial_region", "medium"),
        },
        "left": {
            "bare": ("left_of", "spatial_lateral", "high"),
            "to": ("left_of", "spatial_lateral", "high"),
            "on": ("left_of", "spatial_lateral", "high"),
            "at": ("left_of", "spatial_lateral", "medium"),
            "from": ("from_left_of", "spatial_source", "medium"),
        },
        "right": {
            "bare": ("right_of", "spatial_lateral", "high"),
            "to": ("right_of", "spatial_lateral", "high"),
            "on": ("right_of", "spatial_lateral", "high"),
            "at": ("right_of", "spatial_lateral", "medium"),
            "from": ("from_right_of", "spatial_source", "medium"),
        },
        "corner": {
            "bare": ("corner_of", "spatial_region", "medium"),
            "at": ("corner_of", "spatial_region", "high"),
            "in": ("corner_of", "spatial_region", "high"),
            "near": ("near_corner_of", "spatial_region", "medium"),
        },
        "end": {
            "bare": ("end_of", "spatial_region", "medium"),
            "at": ("end_of", "spatial_region", "high"),
            "near": ("near_end_of", "spatial_region", "medium"),
            "toward": ("toward_end_of", "spatial_path", "medium"),
        },
        "base": {
            "bare": ("base_of", "spatial_region", "medium"),
            "at": ("base_of", "spatial_region", "high"),
            "near": ("near_base_of", "spatial_region", "medium"),
        },
        "surface": {
            "bare": ("surface_of", "spatial_region", "medium"),
            "on": ("surface_of", "spatial_support", "high"),
            "at": ("surface_of", "spatial_region", "medium"),
        },
    }

    for middle, prep_specs in region_groups.items():
        bare = prep_specs.get("bare")
        if bare:
            canonical, relation_type, confidence = bare
            add(f"{middle} of", canonical, relation_type, confidence)
        for prep, spec in prep_specs.items():
            if prep == "bare":
                continue
            canonical, relation_type, confidence = spec
            add(f"{prep} {middle} of", canonical, relation_type, confidence)
            add(f"{prep} the {middle} of", canonical, relation_type, confidence)


def add_simple_adposition_candidates(candidates: dict[str, Candidate]) -> None:
    rows = [
        ("across from", "across_from", "spatial_opposition", "high"),
        ("adjacent to", "next_to", "spatial_proximity", "high"),
        ("ahead of", "ahead_of", "spatial_depth", "high"),
        ("alongside of", "next_to", "spatial_proximity", "medium"),
        ("away from", "away_from", "spatial_separation", "medium"),
        ("close to", "near", "spatial_proximity", "high"),
        ("in between", "between", "spatial_region", "medium"),
        ("inside of", "inside", "spatial_containment", "high"),
        ("near to", "near", "spatial_proximity", "high"),
        ("next to", "next_to", "spatial_proximity", "high"),
        ("off of", "off_of", "spatial_separation", "medium"),
        ("opposite from", "opposite_from", "spatial_opposition", "medium"),
        ("opposite of", "opposite_of", "spatial_opposition", "medium"),
        ("opposite to", "opposite_to", "spatial_opposition", "medium"),
        ("out of", "out_of", "spatial_path", "high"),
        ("outside of", "outside", "spatial_outside", "high"),
        ("up against", "against", "spatial_contact", "medium"),
    ]
    for term, canonical, relation_type, confidence in rows:
        add_candidate(
            candidates,
            term,
            canonical,
            relation_type,
            confidence,
            "manual_clean_adposition",
            "curated visual multiword adposition",
            "curated visual multiword adposition",
        )


def add_mixed_relation_candidates(candidates: dict[str, Candidate], path: Path) -> None:
    if not path.exists():
        return
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            strategy = row.get("collapse_strategy", "")
            if strategy not in ALLOWED_MIXED_STRATEGIES:
                continue
            term = normalize(row.get("term", ""))
            if " " not in term:
                continue
            add_candidate(
                candidates,
                term,
                row.get("canonical", ""),
                row.get("project_relation_type", ""),
                row.get("confidence", "medium"),
                "mixed_relation_collapse_rules",
                strategy,
                f"imported from {path.name}:{strategy}",
            )


def decision_for(candidate: Candidate) -> tuple[str, str]:
    term = candidate.term
    words = term.split()
    first = words[0] if words else ""
    if term in NON_VISUAL_ADPOSITIONS:
        return "reject", "non_visual_adposition"
    if first in PREDICATE_HEADS:
        return "reject", "predicate_head_not_preposition_mwe"
    if first.endswith("ing") or first.endswith("ed"):
        return "reject", "verb_like_head_not_preposition_mwe"
    if not candidate.relation_type.startswith("spatial_"):
        return "reject", "non_spatial_relation_type"
    if candidate.pattern not in {
        "adp_adp",
        "adp_det_adp",
        "adp_of",
        "adp_mid_of",
        "adp_det_mid_of",
        "mid_of",
        "multiword_adposition",
    }:
        return "reject", "unsupported_pattern"
    return "accept", "clean_visual_preposition_mwe"


def row_from_candidate(candidate: Candidate, decision: str, reason: str) -> dict[str, str]:
    source = "|".join(sorted(candidate.sources))
    notes = "|".join(sorted(candidate.notes))
    source_detail = "|".join(sorted(candidate.source_details))
    return {
        "term": candidate.term,
        "canonical": candidate.canonical,
        "relation_type": candidate.relation_type,
        "pattern": candidate.pattern,
        "middle": candidate.middle,
        "final_adp": candidate.final_adp,
        "confidence": candidate.confidence,
        "source": source,
        "notes": notes,
        "decision": decision,
        "reason": reason,
        "source_detail": source_detail,
    }


def write_tsv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def build(args: argparse.Namespace) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    candidates: dict[str, Candidate] = {}
    add_region_candidates(candidates)
    add_simple_adposition_candidates(candidates)
    add_mixed_relation_candidates(candidates, args.mixed_relation_rules)

    candidate_rows: list[dict[str, str]] = []
    clean_rows: list[dict[str, str]] = []
    audit_rows: list[dict[str, str]] = []

    for candidate in sorted(candidates.values(), key=lambda item: item.term):
        decision, reason = decision_for(candidate)
        row = row_from_candidate(candidate, decision, reason)
        candidate_rows.append(row)
        if decision == "accept":
            clean_rows.append({field: row.get(field, "") for field in CLEAN_FIELDNAMES})
        else:
            audit_rows.append({field: row.get(field, "") for field in AUDIT_FIELDNAMES})

    write_tsv(args.candidates_output, candidate_rows, CANDIDATE_FIELDNAMES)
    write_tsv(args.clean_output, clean_rows, CLEAN_FIELDNAMES)
    write_tsv(args.audit_output, audit_rows, AUDIT_FIELDNAMES)
    return candidate_rows, clean_rows, audit_rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Build clean visual preposition MWE lexicons.")
    parser.add_argument("--mixed-relation-rules", type=Path, default=MIXED_RELATION_RULES)
    parser.add_argument("--candidates-output", type=Path, default=PREPOSITION_MWE_CANDIDATES)
    parser.add_argument("--clean-output", type=Path, default=PREPOSITION_MWE_CLEAN_CORE)
    parser.add_argument("--audit-output", type=Path, default=PREPOSITION_MWE_AUDIT_FLAGS)
    args = parser.parse_args()
    candidate_rows, clean_rows, audit_rows = build(args)
    print(f"candidates: {len(candidate_rows)}")
    print(f"clean_core: {len(clean_rows)}")
    print(f"audit_flags: {len(audit_rows)}")
    print(args.candidates_output)
    print(args.clean_output)
    print(args.audit_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
