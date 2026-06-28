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
from stage9_pp_source_disambiguation import pp_source_disambiguation
from stage9_reference_model import (
    build_reference_model,
    canonical_relation_endpoint,
    canonical_target_for_role,
    recovered_roles_from_skipped_edges,
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


def norm_text(value: object) -> str:
    return " ".join(str(value or "").strip().lower().split())


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
    skipped_edges = list(record.get("skipped_edges", []))
    mentions_by_id = {str(mention["mention_id"]): mention for mention in mentions if "mention_id" in mention}
    reference_model = build_reference_model(mentions, edges)
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
                    "canonical_target": canonical_target_for_role(
                        str(edge.get("target")),
                        edge,
                        action,
                        reference_model,
                    ),
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
                        "canonical_target": reference_model["mention_to_entity"].get(str(relation.get("target"))),
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

        for recovered_role in recovered_roles_from_skipped_edges(action, skipped_edges, reference_model):
            event["roles"].append(recovered_role)
            notes.append(
                {
                    "kind": "skipped_reference_role_recovered",
                    "action_mention_id": action_id,
                    "role": recovered_role.get("role"),
                    "canonical_target": recovered_role.get("canonical_target"),
                    "reason": recovered_role.get("recovered_from_skipped_edge"),
                }
            )

        canonical_events.append(event)

    repair_conj_agent_reference_targets(canonical_events, notes)

    canonical_relations = []
    for edge in relation_edges:
        source = str(edge.get("source"))
        target = str(edge.get("target"))
        canonical_source = canonical_relation_endpoint(source, edge, "source", reference_model)
        canonical_target = canonical_relation_endpoint(target, edge, "target", reference_model)
        source_selection = pp_source_disambiguation(
            edge=edge,
            canonical_source=canonical_source,
            canonical_target=canonical_target,
            canonical_events=canonical_events,
            mentions_by_id=mentions_by_id,
        )
        if source_selection is not None:
            canonical_source = source_selection["selected_source"]
            notes.append(
                {
                    "kind": "pp_source_disambiguated",
                    "raw_edge_id": edge.get("edge_id"),
                    "relation": edge.get("evidence"),
                    "raw_source": edge.get("source"),
                    "raw_target": edge.get("target"),
                    "previous_canonical_source": source_selection.get("previous_canonical_source"),
                    "canonical_source": canonical_source,
                    "canonical_target": canonical_target,
                    "action_mention_id": source_selection.get("action_mention_id"),
                    "canonical_action": source_selection.get("canonical_action"),
                    "reason": source_selection.get("reason"),
                    "confidence": source_selection.get("confidence"),
                }
            )
        relation_record = {
            "relation_id": f"cr{len(canonical_relations)}",
            "source": edge.get("source"),
            "target": edge.get("target"),
            "canonical_source": canonical_source,
            "canonical_target": canonical_target,
            "canonical_relation": edge.get("evidence"),
            "confidence": edge.get("confidence"),
            "raw_edge_id": edge.get("edge_id"),
            "consumed_by_event": str(edge.get("edge_id")) in consumed_relation_ids,
            "self_relation_after_canonicalization": canonical_source == canonical_target,
        }
        if source_selection is not None:
            relation_record["source_selection"] = source_selection
        canonical_relations.append(relation_record)

    output = dict(record)
    output["stage9"] = {
        "canonical_entities": reference_model["entities"],
        "entity_links": reference_model["entity_links"],
        "canonical_events": canonical_events,
        "canonical_relations": canonical_relations,
        "canonicalization_notes": notes,
    }
    return output


def repair_conj_agent_reference_targets(
    canonical_events: list[dict[str, object]],
    notes: list[dict[str, object]],
) -> None:
    events_by_text: dict[str, list[dict[str, object]]] = defaultdict(list)
    for event in canonical_events:
        events_by_text[norm_text(event.get("raw_action_text"))].append(event)
        events_by_text[norm_text(event.get("raw_action_lemma"))].append(event)

    for event in canonical_events:
        event_i = event.get("source_token_i")
        for role in event.get("roles", []):
            if role.get("role") != "agent":
                continue
            evidence = str(role.get("evidence", ""))
            marker = "inherited agent conj -> "
            if marker not in evidence:
                continue
            raw_target = role.get("target")
            default_target = f"ent_{raw_target}"
            if role.get("canonical_target") != default_target:
                continue
            inherited_surface = norm_text(evidence.split(marker, 1)[1].split(";", 1)[0])
            candidates = []
            for candidate in events_by_text.get(inherited_surface, []):
                candidate_i = candidate.get("source_token_i")
                if isinstance(event_i, int) and isinstance(candidate_i, int) and candidate_i > event_i:
                    continue
                for candidate_role in candidate.get("roles", []):
                    if candidate_role.get("role") != "agent" or candidate_role.get("target") != raw_target:
                        continue
                    candidate_target = candidate_role.get("canonical_target")
                    if candidate_target and candidate_target != default_target:
                        distance = abs((event_i if isinstance(event_i, int) else 0) - (candidate_i if isinstance(candidate_i, int) else 0))
                        candidates.append((distance, candidate_target, candidate.get("action_mention_id")))
            if not candidates:
                continue
            _distance, canonical_target, source_action_id = sorted(candidates)[0]
            role["canonical_target"] = canonical_target
            role["canonical_repair"] = "conj_agent_inherited_from_reference_canonical_target"
            notes.append(
                {
                    "kind": "conj_agent_reference_target_inherited",
                    "action_mention_id": event.get("action_mention_id"),
                    "source_action_mention_id": source_action_id,
                    "canonical_target": canonical_target,
                }
            )


def update_summary(record: dict[str, object], counters: dict[str, Counter[str]]) -> None:
    stage9 = record.get("stage9", {})
    entities = stage9.get("canonical_entities", []) if isinstance(stage9, dict) else []
    entity_links = stage9.get("entity_links", []) if isinstance(stage9, dict) else []
    events = stage9.get("canonical_events", []) if isinstance(stage9, dict) else []
    relations = stage9.get("canonical_relations", []) if isinstance(stage9, dict) else []
    notes = stage9.get("canonicalization_notes", []) if isinstance(stage9, dict) else []
    counters["records"]["records"] += 1
    counters["records"][str(record.get("parse_path", "unknown"))] += 1
    for entity in entities:
        counters["entities"][str(entity.get("entity_type", ""))] += 1
        counters["semantic_types"][str(entity.get("semantic_type", ""))] += 1
    for link in entity_links:
        counters["entity_links"][str(link.get("link_type", ""))] += 1
    for event in events:
        counters["events"][str(event.get("canonical_action", ""))] += 1
        for role in event.get("roles", []):
            counters["roles"][str(role.get("role", ""))] += 1
            if role.get("recovered_from_skipped_edge"):
                counters["roles"]["recovered_from_skipped_edge"] += 1
    for relation in relations:
        counters["relations"][str(relation.get("canonical_relation", ""))] += 1
        if relation.get("consumed_by_event"):
            counters["relations"]["consumed_by_event"] += 1
        if relation.get("source_selection"):
            counters["relations"]["pp_source_disambiguated"] += 1
        default_source = f"ent_{relation.get('source')}"
        default_target = f"ent_{relation.get('target')}"
        if relation.get("canonical_source") != default_source or relation.get("canonical_target") != default_target:
            counters["relations"]["reference_scoped_endpoint"] += 1
        if relation.get("self_relation_after_canonicalization"):
            counters["relations"]["self_after_canonicalization"] += 1
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
        "## Canonical Entities",
        "",
        markdown_count_table(counters["entities"]),
        "",
        "## Canonical Entity Semantic Types",
        "",
        markdown_count_table(counters["semantic_types"]),
        "",
        "## Entity Links",
        "",
        markdown_count_table(counters["entity_links"]),
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
