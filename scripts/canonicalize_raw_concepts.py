from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import gzip
import json
from pathlib import Path
from typing import Iterable

from phrasal_action_lexicon import (
    DEFAULT_PHRASAL_ACTION_LEXICON,
    load_phrasal_action_lexicon,
    phrasal_action_entry,
)


PASSIVE_SUBJECT_PREFIXES = ("nsubjpass", "csubjpass")
PASSIVE_BY_RELATION = "by"


def open_text(path: Path, mode: str):
    if path.suffix == ".gz":
        return gzip.open(path, mode, encoding="utf-8")
    return path.open(mode, encoding="utf-8")


def iter_jsonl(path: Path) -> Iterable[dict[str, object]]:
    with open_text(path, "rt") as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(line)


def is_passive_subject_edge(edge: dict[str, object]) -> bool:
    if edge.get("edge_type") != "agent":
        return False
    evidence = str(edge.get("evidence", ""))
    return evidence.startswith(PASSIVE_SUBJECT_PREFIXES)


def action_particles(
    action_id: str,
    outgoing_edges: dict[str, list[dict[str, object]]],
    mentions_by_id: dict[str, dict[str, object]],
) -> tuple[str, ...]:
    particles: list[tuple[int, str]] = []
    for edge in outgoing_edges.get(action_id, []):
        if edge.get("edge_type") != "has_particle":
            continue
        particle = mentions_by_id.get(str(edge.get("target")))
        if particle is None:
            continue
        token_i = particle.get("source_token_i")
        order = int(token_i) if isinstance(token_i, int) else 10**9
        lemma = str(particle.get("lemma", "")).lower()
        if lemma:
            particles.append((order, lemma))
    return tuple(lemma for _order, lemma in sorted(particles))


def canonicalize_record(
    record: dict[str, object],
    *,
    phrasal_lexicon,
) -> dict[str, object]:
    mentions = list(record.get("concept_mentions", []))
    edges = list(record.get("edges", []))
    mentions_by_id = {str(mention["mention_id"]): mention for mention in mentions if "mention_id" in mention}
    outgoing_edges: dict[str, list[dict[str, object]]] = defaultdict(list)
    relation_edges: list[dict[str, object]] = []
    for edge in edges:
        outgoing_edges[str(edge.get("source"))].append(edge)
        if edge.get("edge_type") == "relation":
            relation_edges.append(edge)

    consumed_relation_ids: set[str] = set()
    canonical_events: list[dict[str, object]] = []
    notes: list[dict[str, object]] = []

    for action in mentions:
        if action.get("concept_type") != "action":
            continue
        action_id = str(action["mention_id"])
        particles = action_particles(action_id, outgoing_edges, mentions_by_id)
        canonical_action = str(action.get("lemma", "")).lower()
        phrasal_entry = phrasal_action_entry(canonical_action, particles, phrasal_lexicon)
        event_notes: list[str] = []
        if phrasal_entry is not None:
            canonical_action = phrasal_entry.canonical
            event_notes.append(f"phrasal_action:{phrasal_entry.term}")
            notes.append(
                {
                    "kind": "phrasal_action_canonicalized",
                    "action_mention_id": action_id,
                    "term": phrasal_entry.term,
                    "canonical": phrasal_entry.canonical,
                    "source": phrasal_entry.source,
                }
            )

        event = {
            "event_id": f"ce{len(canonical_events)}",
            "action_mention_id": action_id,
            "raw_action_text": action.get("text"),
            "raw_action_lemma": action.get("lemma"),
            "canonical_action": canonical_action,
            "source_token_i": action.get("source_token_i"),
            "roles": [],
            "particles": list(particles),
            "notes": event_notes,
        }

        passive_themes: list[str] = []
        for edge in outgoing_edges.get(action_id, []):
            edge_type = edge.get("edge_type")
            if edge_type == "agent":
                if is_passive_subject_edge(edge):
                    role = "theme"
                    passive_themes.append(str(edge.get("target")))
                    notes.append(
                        {
                            "kind": "passive_subject_to_theme",
                            "action_mention_id": action_id,
                            "raw_edge_id": edge.get("edge_id"),
                            "target": edge.get("target"),
                        }
                    )
                else:
                    role = "agent"
            elif edge_type == "patient":
                role = "patient"
            else:
                continue

            event["roles"].append(
                {
                    "role": role,
                    "target": edge.get("target"),
                    "confidence": edge.get("confidence"),
                    "raw_edge_id": edge.get("edge_id"),
                    "evidence": edge.get("evidence"),
                }
            )

        for theme_id in passive_themes:
            for relation in relation_edges:
                if relation.get("source") != theme_id or relation.get("evidence") != PASSIVE_BY_RELATION:
                    continue
                consumed_relation_ids.add(str(relation.get("edge_id")))
                event["roles"].append(
                    {
                        "role": "by_agent_or_causer",
                        "target": relation.get("target"),
                        "confidence": relation.get("confidence"),
                        "raw_edge_id": relation.get("edge_id"),
                        "evidence": "passive by-frame",
                    }
                )
                notes.append(
                    {
                        "kind": "passive_by_frame_to_event_role",
                        "action_mention_id": action_id,
                        "theme": theme_id,
                        "by_agent_or_causer": relation.get("target"),
                        "raw_edge_id": relation.get("edge_id"),
                    }
                )

        canonical_events.append(event)

    canonical_relations = []
    for edge in relation_edges:
        canonical_relations.append(
            {
                "relation_id": f"cr{len(canonical_relations)}",
                "source": edge.get("source"),
                "target": edge.get("target"),
                "canonical_relation": edge.get("evidence"),
                "confidence": edge.get("confidence"),
                "raw_edge_id": edge.get("edge_id"),
                "consumed_by_event": str(edge.get("edge_id")) in consumed_relation_ids,
            }
        )

    output = dict(record)
    output["stage9"] = {
        "canonical_events": canonical_events,
        "canonical_relations": canonical_relations,
        "canonicalization_notes": notes,
    }
    return output


def update_summary(record: dict[str, object], counters: dict[str, Counter[str]]) -> None:
    stage9 = record.get("stage9", {})
    events = stage9.get("canonical_events", []) if isinstance(stage9, dict) else []
    relations = stage9.get("canonical_relations", []) if isinstance(stage9, dict) else []
    notes = stage9.get("canonicalization_notes", []) if isinstance(stage9, dict) else []
    counters["records"]["records"] += 1
    counters["records"][str(record.get("parse_path", "unknown"))] += 1
    for event in events:
        counters["events"][str(event.get("canonical_action", ""))] += 1
        for role in event.get("roles", []):
            counters["roles"][str(role.get("role", ""))] += 1
    for relation in relations:
        counters["relations"][str(relation.get("canonical_relation", ""))] += 1
        if relation.get("consumed_by_event"):
            counters["relations"]["consumed_by_event"] += 1
    for note in notes:
        counters["notes"][str(note.get("kind", ""))] += 1


def markdown_count_table(counter: Counter[str]) -> str:
    if not counter:
        return "_none_"
    lines = ["| item | count |", "| --- | ---: |"]
    for key, value in counter.most_common():
        lines.append(f"| `{key}` | {value} |")
    return "\n".join(lines)


def write_summary(path: Path, counters: dict[str, Counter[str]], *, input_path: Path, lexicon_path: Path) -> None:
    lines = [
        "# Stage 9 Canonicalization Summary",
        "",
        f"- input: `{input_path}`",
        f"- phrasal_action_lexicon: `{lexicon_path}`",
        "",
        "## Records",
        "",
        markdown_count_table(counters["records"]),
        "",
        "## Canonical Event Actions",
        "",
        markdown_count_table(counters["events"]),
        "",
        "## Canonical Event Roles",
        "",
        markdown_count_table(counters["roles"]),
        "",
        "## Canonical Relations",
        "",
        markdown_count_table(counters["relations"]),
        "",
        "## Canonicalization Notes",
        "",
        markdown_count_table(counters["notes"]),
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Stage 9 canonicalization for raw caption concepts.")
    parser.add_argument("--input", required=True, type=Path, help="Stage 8 raw concept JSONL path")
    parser.add_argument("--output", required=True, type=Path, help="Stage 9 canonicalized JSONL path")
    parser.add_argument("--summary-output", type=Path, help="Optional markdown summary path")
    parser.add_argument(
        "--phrasal-action-lexicon",
        type=Path,
        default=DEFAULT_PHRASAL_ACTION_LEXICON,
        help="Accepted high-confidence phrasal action lexicon TSV",
    )
    args = parser.parse_args()

    phrasal_lexicon = load_phrasal_action_lexicon(args.phrasal_action_lexicon)
    counters: dict[str, Counter[str]] = defaultdict(Counter)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open_text(args.output, "wt") as handle:
        for record in iter_jsonl(args.input):
            canonicalized = canonicalize_record(record, phrasal_lexicon=phrasal_lexicon)
            update_summary(canonicalized, counters)
            handle.write(json.dumps(canonicalized, ensure_ascii=False) + "\n")

    if args.summary_output:
        write_summary(
            args.summary_output,
            counters,
            input_path=args.input,
            lexicon_path=args.phrasal_action_lexicon,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
