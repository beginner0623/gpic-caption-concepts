from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from html import unescape
from pathlib import Path
from typing import Any


SPECIFIC_ROLE_BLACKLIST = {"attribute"}


COCO_SUBTYPE_RULES: dict[str, dict[str, Any]] = {
    "activity_attribute": {
        "confidence": "high",
        "terms": {
            "moving",
            "flying",
            "traveling",
            "holding",
            "feeding",
            "hunting",
            "listening",
            "smelling",
            "sniffing",
            "socializing",
            "learning",
            "following",
            "fishing",
            "cuddling",
            "participating",
            "racing",
            "serving",
            "landing",
            "spectating",
            "exercising",
            "carrying",
            "vacationing",
            "shopping",
            "catching",
            "celebrating",
            "watching",
            "looking",
        },
    },
    "pose_attribute": {
        "confidence": "high",
        "terms": {"laying", "hanging", "stretching", "reaching", "perched"},
    },
    "state_attribute": {
        "confidence": "high",
        "terms": {
            "floating",
            "hanging",
            "landing",
            "unused",
            "inactive",
            "leashed",
            "captive",
            "stuffed",
            "parked",
        },
    },
    "affect_attribute": {
        "confidence": "medium",
        "terms": {
            "enjoying",
            "loving",
            "friendly",
            "lazy",
            "lonely",
            "sneaky",
            "frisky",
            "curious",
            "playful",
            "peaceful",
            "scared",
            "bored",
            "excited",
            "anxious",
            "annoyed",
            "confused",
            "adventurous",
        },
    },
    "mental_state_attribute": {
        "confidence": "medium",
        "terms": {"thinking", "learning", "curious", "confused", "bored"},
    },
    "physiological_state_attribute": {
        "confidence": "medium",
        "terms": {"hungry", "healthy", "thirsty", "tired", "panting"},
    },
    "social_attribute": {
        "confidence": "medium",
        "terms": {"alone", "lonely", "friendly", "socializing", "cuddling", "celebrating", "family friendly"},
    },
    "context_attribute": {
        "confidence": "high",
        "terms": {"urban", "rural", "domestic", "public", "commercial", "family friendly", "vacationing"},
    },
    "style_attribute": {
        "confidence": "medium",
        "terms": {
            "sporty",
            "fancy",
            "modern",
            "professional",
            "antique",
            "vintage",
            "casual",
            "elegant",
            "trendy",
            "exotic",
            "simple",
            "cool",
        },
    },
    "aesthetic_attribute": {
        "confidence": "medium",
        "terms": {"fancy", "cute", "adorable", "decorative", "elegant", "exotic", "dull", "cool"},
    },
    "functional_attribute": {
        "confidence": "medium",
        "terms": {
            "toy",
            "useful",
            "functional",
            "portable",
            "unused",
            "inactive",
            "electric",
            "electrical",
            "commercial",
        },
    },
    "safety_attribute": {
        "confidence": "medium",
        "terms": {"safe", "dangerous", "family friendly"},
    },
    "value_attribute": {
        "confidence": "high",
        "terms": {"cheap", "expensive"},
    },
    "food_quality_attribute": {
        "confidence": "medium",
        "terms": {"tasty", "delicious", "appetizing", "filling", "saucy", "glazed"},
    },
    "temperature_attribute": {
        "confidence": "medium",
        "terms": {"cold", "cool", "warm", "hot"},
    },
    "material_attribute": {
        "confidence": "high",
        "terms": {"metal", "metallic", "wood", "wooden"},
    },
    "texture_attribute": {
        "confidence": "high",
        "terms": {"fuzzy", "crumpled", "wrinkled"},
    },
    "brightness_attribute": {
        "confidence": "medium",
        "terms": {"shiny", "dull"},
    },
    "shape_attribute": {
        "confidence": "high",
        "terms": {"flat"},
    },
    "size_attribute": {
        "confidence": "high",
        "terms": {"bulky", "compact"},
    },
    "speed_attribute": {
        "confidence": "high",
        "terms": {"fast"},
    },
    "sport_attribute": {
        "confidence": "medium",
        "terms": {"sporty", "athletic", "racing", "competitive"},
    },
    "authenticity_attribute": {
        "confidence": "medium",
        "terms": {"fake", "natural"},
    },
    "behavior_attribute": {
        "confidence": "medium",
        "terms": {"wild", "tame", "sneaky", "frisky", "playful"},
    },
    "physical_property_attribute": {
        "confidence": "medium",
        "terms": {"strong", "solid"},
    },
    "technology_attribute": {
        "confidence": "high",
        "terms": {"digital", "electric", "electrical"},
    },
    "condition_attribute": {
        "confidence": "medium",
        "terms": {"comfortable", "cozy", "messy", "cluttered", "healthy", "worn", "busy", "solid"},
    },
    "order_attribute": {
        "confidence": "high",
        "terms": {"messy", "cluttered"},
    },
    "surface_finish_attribute": {
        "confidence": "medium",
        "terms": {"glazed", "shiny"},
    },
    "age_attribute": {
        "confidence": "medium",
        "terms": {"antique", "vintage"},
    },
    "complexity_attribute": {
        "confidence": "medium",
        "terms": {"simple"},
    },
}


ROLE_PRIORITY = {
    "color_attribute": 100,
    "material_attribute": 95,
    "size_attribute": 90,
    "shape_attribute": 88,
    "texture_attribute": 86,
    "brightness_attribute": 84,
    "temperature_attribute": 82,
    "activity_attribute": 80,
    "pose_attribute": 78,
    "state_attribute": 76,
    "condition_attribute": 74,
}


def normalize_term(text: str) -> str:
    text = unescape(str(text)).strip().lower()
    text = text.replace("_", " ")
    text = text.replace("-", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_aliases(term: str) -> list[str]:
    aliases = [normalize_term(part) for part in re.split(r"\s*/\s*", term)]
    return [alias for alias in aliases if alias]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def specific_roles(role_text: str) -> list[str]:
    return [role for role in str(role_text).split("|") if role and role not in SPECIFIC_ROLE_BLACKLIST]


def load_clean_role_index(path: Path) -> dict[str, dict[str, str]]:
    return {normalize_term(row["term"]): row for row in read_tsv(path)}


def clean_alias_roles(aliases: list[str], clean_index: dict[str, dict[str, str]]) -> tuple[list[str], list[str], list[str]]:
    roles: set[str] = set()
    sources: set[str] = set()
    hits: list[str] = []
    for alias in aliases:
        clean_row = clean_index.get(alias)
        if not clean_row:
            continue
        alias_roles = specific_roles(clean_row.get("roles", ""))
        if not alias_roles:
            continue
        hits.append(alias)
        roles.update(alias_roles)
        sources.update(source for source in clean_row.get("sources", "").split("|") if source)
    return sorted(roles), sorted(sources), hits


def rule_roles(aliases: list[str]) -> tuple[list[str], list[str], str]:
    roles: set[str] = set()
    rule_ids: list[str] = []
    confidence_rank = {"high": 3, "medium": 2, "low": 1}
    best_confidence = "low"
    for role, rule in COCO_SUBTYPE_RULES.items():
        matched = sorted(set(aliases) & set(rule["terms"]))
        if not matched:
            continue
        roles.add(role)
        rule_ids.append(f"{role}:{','.join(matched)}")
        if confidence_rank[rule["confidence"]] > confidence_rank[best_confidence]:
            best_confidence = rule["confidence"]
    return sorted(roles), sorted(rule_ids), best_confidence


def choose_primary_role(roles: list[str]) -> str:
    if not roles:
        return "object_attribute"
    return sorted(roles, key=lambda role: (-ROLE_PRIORITY.get(role, 0), role))[0]


def tag_new_coco_rows(rows: list[dict[str, str]], clean_index: dict[str, dict[str, str]]) -> list[dict[str, Any]]:
    tagged: list[dict[str, Any]] = []
    for row in rows:
        term = normalize_term(row["term"])
        aliases = split_aliases(term)
        alias_roles, alias_sources, alias_hits = clean_alias_roles(aliases, clean_index)
        inferred_roles, rule_ids, rule_confidence = rule_roles(aliases)
        roles = sorted(set(alias_roles) | set(inferred_roles))

        if alias_roles:
            status = "clean_alias_exact_match_plus_coco_rule" if set(inferred_roles) - set(alias_roles) else "clean_alias_exact_match"
            confidence = "high"
        elif inferred_roles:
            status = "coco_subtype_rule"
            confidence = rule_confidence
        else:
            status = "untagged_object_attribute_fallback"
            confidence = "low"

        tagged.append(
            {
                "source": row["source"],
                "term": term,
                "aliases": "|".join(aliases),
                "primary_role": choose_primary_role(roles),
                "assigned_roles": "|".join(roles) if roles else "object_attribute",
                "broad_role": "object_attribute",
                "classification_status": status,
                "confidence": confidence,
                "rule_id": "|".join(rule_ids),
                "clean_alias_hits": "|".join(alias_hits),
                "clean_alias_role_sources": "|".join(alias_sources),
                "raw_term": row.get("raw_term", ""),
                "source_id": row.get("source_id", ""),
                "count": row.get("count", ""),
                "source_url": row.get("source_url", ""),
            }
        )
    return tagged


def normalize_existing_coco_rows(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    for row in rows:
        roles = specific_roles(row.get("assigned_roles") or row.get("existing_clean_roles", ""))
        output.append(
            {
                "source": row["source"],
                "term": normalize_term(row["term"]),
                "aliases": normalize_term(row["term"]),
                "primary_role": choose_primary_role(roles),
                "assigned_roles": "|".join(roles) if roles else "object_attribute",
                "broad_role": "object_attribute",
                "classification_status": "clean_exact_overlap",
                "confidence": "high",
                "rule_id": "",
                "clean_alias_hits": normalize_term(row["term"]),
                "clean_alias_role_sources": row.get("assigned_role_sources") or row.get("existing_clean_sources", ""),
                "raw_term": row.get("raw_term", ""),
                "source_id": row.get("source_id", ""),
                "count": row.get("count", ""),
                "source_url": row.get("source_url", ""),
            }
        )
    return output


def role_count_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    counts = Counter()
    for row in rows:
        for role in str(row["assigned_roles"]).split("|"):
            if role:
                counts[role] += 1
    return [{"role": role, "count": count} for role, count in sorted(counts.items())]


def write_report(path: Path, new_rows: list[dict[str, Any]], all_rows: list[dict[str, Any]]) -> None:
    status_counts = Counter(row["classification_status"] for row in new_rows)
    confidence_counts = Counter(row["confidence"] for row in new_rows)
    role_counts = role_count_rows(new_rows)
    untagged = [row for row in new_rows if row["classification_status"] == "untagged_object_attribute_fallback"]

    lines = [
        "# COCO Attribute Subtype Tagging",
        "",
        "COCO Attributes 중 기존 typed clean 사전과 exact overlap되지 않았던 항목에 세부 role을 1차로 부여한 결과입니다.",
        "COCO 원본은 attribute vocabulary로는 clean하지만, `color/material/pose/...` 같은 subtype은 제공하지 않기 때문에 여기서는 프로젝트용 매핑을 따로 둡니다.",
        "",
        "## 요약",
        "",
        f"- COCO non-overlap terms: {len(new_rows)}",
        f"- COCO all typed terms: {len(all_rows)}",
        f"- untagged fallback: {len(untagged)}",
        "",
        "## 분류 상태",
        "",
        "| status | terms |",
        "|---|---:|",
    ]
    for status, count in sorted(status_counts.items()):
        lines.append(f"| {status} | {count} |")
    lines.extend(["", "## Confidence", "", "| confidence | terms |", "|---|---:|"])
    for confidence, count in sorted(confidence_counts.items()):
        lines.append(f"| {confidence} | {count} |")
    lines.extend(["", "## Role Counts For Non-Overlap COCO", "", "| role | terms |", "|---|---:|"])
    for row in role_counts:
        lines.append(f"| {row['role']} | {row['count']} |")
    lines.extend(
        [
            "",
            "## 생성 파일",
            "",
            "- `resources/lexicons/coco_attributes_new_subtype_tagged.tsv`: 기존 clean 사전에 없던 COCO attribute의 subtype tagging 결과",
            "- `resources/lexicons/coco_attributes_clean_typed.tsv`: 기존 overlap 85개와 새로 tag한 119개를 합친 COCO clean typed vocabulary",
            "- `resources/lexicons/coco_attributes_new_subtype_role_counts.tsv`: non-overlap COCO role별 count",
            "",
            "## 해석",
            "",
            "- `classification_status=clean_alias_exact_match`: `metal / metallic`처럼 slash label을 쪼갰을 때 기존 clean role과 매칭된 경우입니다.",
            "- `classification_status=coco_subtype_rule`: COCO controlled vocabulary를 프로젝트 role taxonomy에 매핑한 1차 rule입니다.",
            "- 새 role은 COCO가 공식 제공한 subtype이 아니라, caption-to-concept count schema를 위한 프로젝트 내부 subtype입니다.",
            "- Visual Genome raw new attribute는 이 파일에 섞지 않았습니다.",
        ]
    )
    if untagged:
        lines.extend(["", "## Untagged", "", ", ".join(f"`{row['term']}`" for row in untagged)])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Assign project subtype roles to COCO Attributes not covered by the clean typed lexicon.")
    parser.add_argument("--clean-lexicon", type=Path, default=Path("resources/lexicons/modifier_attributes_clean.tsv"))
    parser.add_argument("--coco-new", type=Path, default=Path("resources/lexicons/coco_attributes_new.tsv"))
    parser.add_argument("--coco-overlap", type=Path, default=Path("resources/lexicons/coco_attributes_role_classified.tsv"))
    parser.add_argument("--output-dir", type=Path, default=Path("resources/lexicons"))
    parser.add_argument("--report", type=Path, default=Path("reports/coco_attribute_subtype_tagging.md"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    clean_index = load_clean_role_index(args.clean_lexicon)
    new_rows = read_tsv(args.coco_new)
    overlap_rows = read_tsv(args.coco_overlap)

    tagged_new = tag_new_coco_rows(new_rows, clean_index)
    typed_overlap = normalize_existing_coco_rows(overlap_rows)
    all_typed = sorted(typed_overlap + tagged_new, key=lambda row: int(row["source_id"]) if str(row["source_id"]).isdigit() else 10**9)

    fields = [
        "source",
        "term",
        "aliases",
        "primary_role",
        "assigned_roles",
        "broad_role",
        "classification_status",
        "confidence",
        "rule_id",
        "clean_alias_hits",
        "clean_alias_role_sources",
        "raw_term",
        "source_id",
        "count",
        "source_url",
    ]
    write_tsv(args.output_dir / "coco_attributes_new_subtype_tagged.tsv", tagged_new, fields)
    write_tsv(args.output_dir / "coco_attributes_clean_typed.tsv", all_typed, fields)
    write_tsv(args.output_dir / "coco_attributes_new_subtype_role_counts.tsv", role_count_rows(tagged_new), ["role", "count"])
    write_report(args.report, tagged_new, all_typed)

    print(f"tagged COCO non-overlap terms: {len(tagged_new)}")
    print(f"COCO all typed terms: {len(all_typed)}")
    print(f"wrote: {args.output_dir / 'coco_attributes_new_subtype_tagged.tsv'}")
    print(f"wrote: {args.output_dir / 'coco_attributes_clean_typed.tsv'}")
    print(f"wrote: {args.report}")


if __name__ == "__main__":
    main()
