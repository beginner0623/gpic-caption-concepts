from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import gzip
import json
from pathlib import Path
import re
from typing import Any


GENERIC_ENTITY_LEMMAS = {
    "another",
    "area",
    "both",
    "device",
    "document",
    "each",
    "figure",
    "individual",
    "item",
    "object",
    "one",
    "other",
    "others",
    "piece",
    "scene",
    "structure",
    "thing",
    "vehicle",
}

REFERENCE_ENTITY_TYPES = {"reference", "group"}
ODD_TEXT_RE = re.compile(r"[^A-Za-z0-9_ '.,:/()&-]+")


def open_text(path: Path):
    if path.suffix == ".gz":
        return gzip.open(path, "rt", encoding="utf-8")
    return path.open("r", encoding="utf-8")


def iter_jsonl(path: Path):
    with open_text(path) as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(line)


def preview(text: str | None, limit: int = 180) -> str:
    value = " ".join((text or "").split())
    return value if len(value) <= limit else value[: limit - 3] + "..."


def norm(value: Any) -> str:
    return str(value or "").strip()


def add_example(examples: dict[tuple[str, str], list[str]], key: tuple[str, str], record: dict[str, Any], detail: str, max_examples: int) -> None:
    if len(examples[key]) >= max_examples:
        return
    row_index = record.get("row_index")
    caption_id = norm(record.get("caption_id"))[:12]
    caption = preview(record.get("caption"))
    examples[key].append(f"#{row_index} {caption_id} | {detail} | {caption}")


def update_counter(
    counter: Counter[tuple[str, str]],
    examples: dict[tuple[str, str], list[str]],
    category: str,
    candidate: str,
    record: dict[str, Any],
    detail: str,
    *,
    max_examples: int,
) -> None:
    candidate = candidate.strip()
    if not candidate:
        return
    key = (category, candidate)
    counter[key] += 1
    add_example(examples, key, record, detail, max_examples)


def relation_is_raw(relation: dict[str, Any]) -> bool:
    lexical = relation.get("lexical_canonicalization") or {}
    return lexical.get("canonical_source") == "raw_relation" or lexical.get("parent_source") == "raw_relation"


def fact_is_raw_attribute(fact: dict[str, Any]) -> bool:
    if fact.get("fact_type") not in {"has_attribute", "candidate_has_attribute"}:
        return False
    lexical = fact.get("lexical_canonicalization") or {}
    return lexical.get("canonical_source") == "raw_attribute_role" or lexical.get("parent_source") == "raw_attribute_role"


def particle_value(particle: Any) -> str:
    if isinstance(particle, dict):
        return norm(particle.get("text") or particle.get("lemma"))
    return norm(particle)


def collect_record(
    record: dict[str, Any],
    counter: Counter[tuple[str, str]],
    examples: dict[tuple[str, str], list[str]],
    *,
    max_examples: int,
) -> None:
    stage9 = record.get("stage9") or {}
    entities = stage9.get("canonical_entities") or []
    events = stage9.get("canonical_events") or []
    relations = stage9.get("canonical_relations") or []
    facts = stage9.get("canonical_facts") or []
    skipped_edges = record.get("skipped_edges") or []

    for entity in entities:
        canonical = norm(entity.get("canonical_lemma"))
        text = norm(entity.get("text"))
        entity_type = norm(entity.get("entity_type"))
        semantic_type = norm(entity.get("semantic_type"))
        parent_chain = entity.get("parent_chain") or []
        count_eligible = entity.get("count_eligible", True)
        detail = f"text={text}; type={entity_type}; semantic={semantic_type}; entity_id={entity.get('entity_id')}"

        if count_eligible and not parent_chain:
            update_counter(counter, examples, "entity_parent_none", canonical, record, detail, max_examples=max_examples)

        if entity_type in REFERENCE_ENTITY_TYPES or canonical in GENERIC_ENTITY_LEMMAS:
            update_counter(counter, examples, "generic_reference_candidate", canonical or text, record, detail, max_examples=max_examples)

        if ("-" in text or "-" in canonical) and count_eligible:
            update_counter(counter, examples, "hyphen_object_candidate", canonical or text, record, detail, max_examples=max_examples)

        if (" " in text.strip()) and count_eligible and entity_type in {"object", "group"}:
            lexical = entity.get("lexical_canonicalization") or {}
            source = norm(lexical.get("canonical_source"))
            parent_source = norm(lexical.get("parent_source"))
            if source in {"raw_lemma", "raw_object", ""} or parent_source in {"", "raw_lemma"} or not parent_chain:
                update_counter(
                    counter,
                    examples,
                    "object_mwe_candidate",
                    text.lower(),
                    record,
                    f"{detail}; canonical={canonical}; source={source}; parent_source={parent_source}",
                    max_examples=max_examples,
                )

        if entity_type == "object" and ("quote" in canonical or "quoted" in text.lower()):
            update_counter(counter, examples, "quote_object_anomaly", canonical or text, record, detail, max_examples=max_examples)

        if ODD_TEXT_RE.search(text) or ODD_TEXT_RE.search(canonical):
            update_counter(counter, examples, "ocr_symbol_entity_candidate", canonical or text, record, detail, max_examples=max_examples)

    for event in events:
        action = norm(event.get("canonical_action"))
        raw_text = norm(event.get("raw_action_text"))
        raw_lemma = norm(event.get("raw_action_lemma"))
        lexical = event.get("lexical_canonicalization") or {}
        detail = f"raw={raw_text}; lemma={raw_lemma}; event_id={event.get('event_id')}"

        if lexical.get("parent_source") == "visual_action_fallback":
            update_counter(counter, examples, "action_parent_fallback", action, record, detail, max_examples=max_examples)

        particles = event.get("particles") or []
        if particles and lexical.get("canonical_source") in {"raw_action", "", None}:
            particle_text = "_".join(value for value in (particle_value(p) for p in particles) if value)
            candidate = f"{raw_lemma}_{particle_text}" if particle_text else raw_lemma
            update_counter(counter, examples, "phrasal_action_candidate", candidate, record, detail, max_examples=max_examples)

        if ODD_TEXT_RE.search(raw_text) or ODD_TEXT_RE.search(action):
            update_counter(counter, examples, "ocr_symbol_action_candidate", action or raw_text, record, detail, max_examples=max_examples)

    for relation in relations:
        raw_relation = norm(relation.get("raw_relation"))
        canonical_relation = norm(relation.get("canonical_relation") or raw_relation)
        detail = (
            f"raw={raw_relation}; canonical={canonical_relation}; "
            f"source={relation.get('canonical_source')}; target={relation.get('canonical_target')}; relation_id={relation.get('relation_id')}"
        )
        if relation_is_raw(relation):
            update_counter(counter, examples, "raw_relation", raw_relation or canonical_relation, record, detail, max_examples=max_examples)

        if "_" in raw_relation and relation_is_raw(relation):
            update_counter(counter, examples, "preposition_mwe_candidate", raw_relation, record, detail, max_examples=max_examples)

        if relation.get("self_relation_after_canonicalization"):
            update_counter(counter, examples, "self_relation_after_canonicalization", canonical_relation, record, detail, max_examples=max_examples)

    for fact in facts:
        if fact_is_raw_attribute(fact):
            attr = norm(fact.get("attribute"))
            detail = f"source={fact.get('source_canonical')}; fact_type={fact.get('fact_type')}; confidence={fact.get('confidence')}"
            update_counter(counter, examples, "raw_attribute_role", attr, record, detail, max_examples=max_examples)

        attr = norm(fact.get("attribute"))
        if attr and ODD_TEXT_RE.search(attr):
            detail = f"source={fact.get('source_canonical')}; fact_type={fact.get('fact_type')}"
            update_counter(counter, examples, "ocr_symbol_attribute_candidate", attr, record, detail, max_examples=max_examples)

    for skipped in skipped_edges:
        reason = norm(skipped.get("reason") or skipped.get("skip_reason") or skipped.get("edge_type") or "unknown")
        detail = "; ".join(f"{k}={v}" for k, v in skipped.items() if k in {"edge_type", "source", "target", "reason", "evidence"})
        update_counter(counter, examples, "skipped_edge", reason, record, detail, max_examples=max_examples)
        if reason == "self_edge_after_coref":
            update_counter(counter, examples, "self_edge_repair_candidate", reason, record, detail, max_examples=max_examples)


def write_tsv(
    output: Path,
    counter: Counter[tuple[str, str]],
    examples: dict[tuple[str, str], list[str]],
) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(counter.items(), key=lambda item: (-item[1], item[0][0], item[0][1]))
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["category", "candidate", "count", "examples"],
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        for (category, candidate), count in rows:
            writer.writerow(
                {
                    "category": category,
                    "candidate": candidate,
                    "count": count,
                    "examples": " || ".join(examples.get((category, candidate), [])),
                }
            )


def write_dashboard(
    output: Path,
    counter: Counter[tuple[str, str]],
    examples: dict[tuple[str, str], list[str]],
    *,
    input_path: Path,
    top_n: int,
) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    by_category: dict[str, Counter[str]] = defaultdict(Counter)
    for (category, candidate), count in counter.items():
        by_category[category][candidate] = count

    lines = [
        "# Feedback Candidate Dashboard",
        "",
        "## Inputs",
        "",
        f"- input: `{input_path}`",
        "",
        "## Category Summary",
        "",
        "| category | unique candidates | total hits |",
        "|---|---:|---:|",
    ]
    for category in sorted(by_category):
        total = sum(by_category[category].values())
        lines.append(f"| `{category}` | {len(by_category[category])} | {total} |")

    for category in sorted(by_category):
        lines += ["", f"## {category}", "", "| candidate | count | examples |", "|---|---:|---|"]
        for candidate, count in by_category[category].most_common(top_n):
            ex = "<br>".join(examples.get((category, candidate), []))
            lines.append(f"| `{candidate}` | {count} | {ex} |")

    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Collect automatic feedback candidates from Stage 9 canonical JSONL output.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--candidate-output", required=True, type=Path)
    parser.add_argument("--dashboard-output", required=True, type=Path)
    parser.add_argument("--top-n", type=int, default=50)
    parser.add_argument("--max-examples", type=int, default=3)
    args = parser.parse_args()

    counter: Counter[tuple[str, str]] = Counter()
    examples: dict[tuple[str, str], list[str]] = defaultdict(list)
    records = 0
    for record in iter_jsonl(args.input):
        records += 1
        collect_record(record, counter, examples, max_examples=args.max_examples)

    write_tsv(args.candidate_output, counter, examples)
    write_dashboard(args.dashboard_output, counter, examples, input_path=args.input, top_n=args.top_n)
    print(json.dumps({"records": records, "unique_candidates": len(counter), "candidate_output": str(args.candidate_output), "dashboard_output": str(args.dashboard_output)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
