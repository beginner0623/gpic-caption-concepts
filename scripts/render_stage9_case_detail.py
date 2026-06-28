from __future__ import annotations

import argparse
import gzip
import json
from pathlib import Path
from typing import Iterable


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


def flat(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return ", ".join(flat(item) for item in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def cell(value: object) -> str:
    return flat(value).replace("|", "\\|").replace("\n", " ")


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    if not rows:
        return "_none_"
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(cell(value) for value in row) + " |")
    return "\n".join(lines)


def concept_mention_rows(record: dict[str, object]) -> list[list[object]]:
    rows = []
    for mention in record.get("concept_mentions", []):
        rows.append(
            [
                mention.get("mention_id"),
                mention.get("concept_type"),
                mention.get("text"),
                mention.get("lemma"),
                mention.get("role"),
                mention.get("source_tag"),
                mention.get("source_token_i"),
                mention.get("confidence"),
            ]
        )
    return rows


def raw_edge_rows(record: dict[str, object]) -> list[list[object]]:
    rows = []
    for edge in record.get("edges", []):
        rows.append(
            [
                edge.get("edge_id"),
                edge.get("edge_type"),
                edge.get("source"),
                edge.get("target"),
                edge.get("confidence"),
                edge.get("evidence"),
            ]
        )
    return rows


def skipped_edge_rows(record: dict[str, object]) -> list[list[object]]:
    rows = []
    for edge in record.get("skipped_edges", []):
        rows.append(
            [
                edge.get("edge_type"),
                edge.get("source"),
                edge.get("target"),
                edge.get("confidence"),
                edge.get("reason"),
                edge.get("evidence"),
            ]
        )
    return rows


def canonical_entity_rows(stage9: dict[str, object]) -> list[list[object]]:
    rows = []
    for entity in stage9.get("canonical_entities", []):
        lexical = entity.get("lexical_canonicalization", {})
        if not isinstance(lexical, dict):
            lexical = {}
        rows.append(
            [
                entity.get("entity_id"),
                entity.get("entity_type"),
                entity.get("canonical_lemma"),
                entity.get("text"),
                entity.get("semantic_type"),
                lexical.get("canonical_source") or lexical.get("source"),
                lexical.get("parent_source"),
                entity.get("parent_chain"),
                entity.get("raw_mention_ids"),
                entity.get("source"),
                entity.get("parent_entity_id"),
                entity.get("member_entity_ids"),
                entity.get("cardinality"),
                entity.get("count_eligible"),
                entity.get("count_keys"),
            ]
        )
    return rows


def entity_link_rows(stage9: dict[str, object]) -> list[list[object]]:
    rows = []
    for link in stage9.get("entity_links", []):
        rows.append(
            [
                link.get("link_type"),
                link.get("source_mention_id"),
                link.get("source_entity_id"),
                link.get("target_mention_id"),
                link.get("target_entity_id"),
                link.get("confidence"),
                link.get("reason"),
            ]
        )
    return rows


def canonical_event_rows(stage9: dict[str, object]) -> list[list[object]]:
    rows = []
    for event in stage9.get("canonical_events", []):
        lexical = event.get("lexical_canonicalization", {})
        if not isinstance(lexical, dict):
            lexical = {}
        role_summary = []
        for role in event.get("roles", []):
            role_label = str(role.get("role") or "")
            raw_role = role.get("raw_role")
            if raw_role and raw_role != role_label:
                role_label = f"{role_label}<-{raw_role}"
            voice = role.get("voice_normalization")
            if voice and voice != "none":
                role_label = f"{role_label}[{voice}]"
            role_summary.append(
                f"{role_label}:{role.get('target')}->{role.get('canonical_target')}"
            )
        rows.append(
            [
                event.get("event_id"),
                event.get("action_mention_id"),
                event.get("raw_action_text"),
                event.get("raw_action_lemma"),
                event.get("canonical_action"),
                lexical.get("canonical_source") or lexical.get("source"),
                lexical.get("parent_source"),
                event.get("action_parent_chain"),
                event.get("particles"),
                "; ".join(role_summary),
                event.get("count_keys"),
                event.get("notes"),
            ]
        )
    return rows


def canonical_event_role_rows(stage9: dict[str, object]) -> list[list[object]]:
    rows = []
    for event in stage9.get("canonical_events", []):
        for role in event.get("roles", []):
            rows.append(
                [
                    event.get("event_id"),
                    event.get("canonical_action"),
                    role.get("role"),
                    role.get("raw_role"),
                    role.get("voice_normalization"),
                    role.get("target"),
                    role.get("canonical_target"),
                    role.get("confidence"),
                    role.get("raw_edge_id"),
                    role.get("evidence"),
                    role.get("recovered_from_skipped_edge"),
                    role.get("canonical_repair"),
                ]
            )
    return rows


def canonical_relation_rows(stage9: dict[str, object]) -> list[list[object]]:
    rows = []
    for relation in stage9.get("canonical_relations", []):
        lexical = relation.get("lexical_canonicalization", {})
        if not isinstance(lexical, dict):
            lexical = {}
        source_selection = relation.get("source_selection")
        if isinstance(source_selection, dict):
            source_selection_method = source_selection.get("method")
            source_selection_reason = source_selection.get("reason")
        else:
            source_selection_method = ""
            source_selection_reason = ""
        rows.append(
            [
                relation.get("relation_id"),
                relation.get("source"),
                relation.get("target"),
                relation.get("canonical_source"),
                relation.get("canonical_target"),
                relation.get("raw_relation"),
                relation.get("canonical_relation"),
                lexical.get("canonical_source") or lexical.get("source"),
                lexical.get("parent_source"),
                relation.get("relation_parent_chain"),
                relation.get("confidence"),
                relation.get("raw_edge_id"),
                relation.get("consumed_by_event"),
                relation.get("self_relation_after_canonicalization"),
                source_selection_method,
                source_selection_reason,
            ]
        )
    return rows


def canonical_fact_rows(stage9: dict[str, object]) -> list[list[object]]:
    rows = []
    for fact in stage9.get("canonical_facts", []):
        rows.append(
            [
                fact.get("fact_id"),
                fact.get("fact_type"),
                fact.get("source_canonical") or fact.get("action") or fact.get("canonical"),
                fact.get("relation") or fact.get("role") or fact.get("attribute") or fact.get("quantity"),
                fact.get("target_canonical"),
                fact.get("parent_chain") or fact.get("attribute_parent_chain") or fact.get("quantity_parent_chain") or fact.get("relation_parent_chain") or fact.get("action_parent_chain"),
                fact.get("count_key"),
                fact.get("count_eligible"),
                fact.get("confidence"),
            ]
        )
    return rows


def canonical_note_rows(stage9: dict[str, object]) -> list[list[object]]:
    rows = []
    for note in stage9.get("canonicalization_notes", []):
        rows.append(
            [
                note.get("kind"),
                note.get("action_mention_id"),
                note.get("raw_edge_id"),
                note.get("target"),
                note.get("canonical_target"),
                note.get("reason"),
                note,
            ]
        )
    return rows


def render_record(record: dict[str, object], index: int) -> str:
    stage9 = record.get("stage9", {})
    if not isinstance(stage9, dict):
        stage9 = {}

    blocks = [
        f"## {index:02d}",
        "",
        f"**caption_shape:** `{record.get('caption_shape', '')}`",
        f"**caption_type:** `{record.get('caption_type', '')}`",
        f"**caption_id:** `{record.get('caption_id', '')}`",
        f"**parse_path:** `{record.get('parse_path', '')}`",
        "",
        f"> {record.get('caption', '')}",
        "",
    ]
    parse_caption = record.get("parse_caption")
    if parse_caption and parse_caption != record.get("caption"):
        blocks.extend(["**parse_caption:**", "", f"> {parse_caption}", ""])

    blocks.extend(
        [
            "### Raw Concept Mentions",
            markdown_table(
                ["id", "type", "text", "lemma", "role", "source_tag", "source_token", "confidence"],
                concept_mention_rows(record),
            ),
            "",
            "### Raw Concept Edges",
            markdown_table(
                ["id", "type", "source", "target", "confidence", "evidence"],
                raw_edge_rows(record),
            ),
            "",
            "### Skipped Raw Concept Edges",
            markdown_table(
                ["type", "source", "target", "confidence", "reason", "evidence"],
                skipped_edge_rows(record),
            ),
            "",
            "### Stage 9 Canonical Entities",
            markdown_table(
                [
                    "entity_id",
                    "entity_type",
                    "canonical_lemma",
                    "text",
                    "semantic_type",
                    "canonical_source",
                    "parent_source",
                    "parent_chain",
                    "raw_mentions",
                    "source",
                    "parent_entity",
                    "member_entities",
                    "cardinality",
                    "count_eligible",
                    "count_keys",
                ],
                canonical_entity_rows(stage9),
            ),
            "",
            "### Stage 9 Entity Links",
            markdown_table(
                [
                    "link_type",
                    "source_mention",
                    "source_entity",
                    "target_mention",
                    "target_entity",
                    "confidence",
                    "reason",
                ],
                entity_link_rows(stage9),
            ),
            "",
            "### Stage 9 Canonical Events",
            markdown_table(
                [
                    "event_id",
                    "action_mention",
                    "raw_text",
                    "raw_lemma",
                    "canonical_action",
                    "canonical_source",
                    "parent_source",
                    "action_parent_chain",
                    "particles",
                    "roles_summary",
                    "count_keys",
                    "notes",
                ],
                canonical_event_rows(stage9),
            ),
            "",
            "### Stage 9 Canonical Event Roles",
            markdown_table(
                [
                    "event_id",
                    "canonical_action",
                    "role",
                    "raw_role",
                    "voice_normalization",
                    "raw_target",
                    "canonical_target",
                    "confidence",
                    "raw_edge",
                    "evidence",
                    "recovered_from_skipped",
                    "repair",
                ],
                canonical_event_role_rows(stage9),
            ),
            "",
            "### Stage 9 Canonical Relations",
            markdown_table(
                [
                    "relation_id",
                    "raw_source",
                    "raw_target",
                    "canonical_source",
                    "canonical_target",
                    "raw_relation",
                    "relation",
                    "relation_canonical_source",
                    "relation_parent_source",
                    "relation_parent_chain",
                    "confidence",
                    "raw_edge",
                    "consumed_by_event",
                    "self_after_canonicalization",
                    "source_selection",
                    "selection_reason",
                ],
                canonical_relation_rows(stage9),
            ),
            "",
            "### Stage 9 Canonical Facts",
            markdown_table(
                [
                    "fact_id",
                    "fact_type",
                    "source/action/canonical",
                    "relation/role/value",
                    "target",
                    "parent_chain",
                    "count_key",
                    "count_eligible",
                    "confidence",
                ],
                canonical_fact_rows(stage9),
            ),
            "",
            "### Stage 9 Canonicalization Notes",
            markdown_table(
                [
                    "kind",
                    "action_mention",
                    "raw_edge",
                    "target",
                    "canonical_target",
                    "reason",
                    "full_note",
                ],
                canonical_note_rows(stage9),
            ),
            "",
        ]
    )
    return "\n".join(blocks)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render per-case Stage 8/9 concept details as markdown.")
    parser.add_argument("--input", required=True, type=Path, help="Stage 9 canonical JSONL path")
    parser.add_argument("--output", required=True, type=Path, help="Output markdown path")
    parser.add_argument("--title", default="Stage 9 Case Detail")
    parser.add_argument("--max-records", type=int, default=100)
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(
            "\n".join(
                [
                    f"# {args.title}",
                    "",
                    f"- input: `{args.input}`",
                    f"- max_records: `{args.max_records}`",
                    "- contents: raw concept mentions/edges + Stage 9 canonical entities/events/relations",
                    "",
                ]
            )
        )
        handle.write("\n")
        for index, record in enumerate(iter_jsonl(args.input), 1):
            if index > args.max_records:
                break
            handle.write(render_record(record, index))
            handle.write("\n")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
