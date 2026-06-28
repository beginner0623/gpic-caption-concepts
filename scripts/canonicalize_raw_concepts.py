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
from stage9_lexical_canonicalizer import (
    DEFAULT_ACTION_CANONICAL_LEXICON,
    DEFAULT_ACTION_PARENT_LEXICON,
    DEFAULT_ATTRIBUTE_CANONICAL_LEXICON,
    DEFAULT_OBJECT_CANONICAL_LEXICON,
    DEFAULT_OBJECT_MWE_CANONICAL_LEXICON,
    DEFAULT_OBJECT_PARENT_LEXICON,
    DEFAULT_PREPOSITION_MWE_LEXICON,
    DEFAULT_RELATION_CANONICAL_LEXICON,
    Stage9CanonicalLexicon,
    canonicalize_action,
    canonicalize_attribute,
    canonicalize_entity,
    canonicalize_quantity,
    canonicalize_relation,
    load_stage9_canonical_lexicon,
    make_fact_count_key,
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
    stage9_lexicon: Stage9CanonicalLexicon,
) -> dict[str, object]:
    mentions = list(record.get("concept_mentions", []))
    edges = list(record.get("edges", []))
    skipped_edges = list(record.get("skipped_edges", []))
    mentions_by_id = {str(mention["mention_id"]): mention for mention in mentions if "mention_id" in mention}
    reference_model = build_reference_model(mentions, edges)
    reference_model = dict(reference_model)
    inactive_entity_ids = {
        str(link.get("source_entity_id"))
        for link in reference_model.get("entity_links", [])
        if link.get("link_type") == "generic_alias" and link.get("source_entity_id")
    }
    canonical_entities = []
    for entity in reference_model["entities"]:
        canonical_entity = canonicalize_entity(entity, stage9_lexicon)
        if str(canonical_entity.get("entity_id")) in inactive_entity_ids:
            canonical_entity["count_eligible"] = False
            canonical_entity["count_exclusion_reason"] = "generic_alias_source"
        else:
            canonical_entity["count_eligible"] = True
        canonical_entities.append(canonical_entity)
    reference_model["entities"] = canonical_entities
    entities_by_id = {str(entity.get("entity_id")): entity for entity in canonical_entities}
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
        action_info = canonicalize_action(canonical_action, stage9_lexicon)
        if action_info["canonical"] != canonical_action:
            notes.append(
                {
                    "kind": "action_lexical_canonicalized",
                    "action_mention_id": action_id,
                    "raw_canonical_action": canonical_action,
                    "canonical": action_info["canonical"],
                    "source": action_info["source"],
                }
            )
        canonical_action = str(action_info["canonical"])

        event = {
            "event_id": f"ce{len(canonical_events)}",
            "action_mention_id": action_id,
            "raw_action_text": action.get("text"),
            "raw_action_lemma": action.get("lemma"),
            "canonical_action": canonical_action,
            "action_parent_chain": action_info["parent_chain"],
            "count_channel": action_info["count_channel"],
            "count_keys": action_info["count_keys"],
            "lexical_canonicalization": action_info["lexical_canonicalization"],
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
            "raw_relation": edge.get("evidence"),
            "confidence": edge.get("confidence"),
            "raw_edge_id": edge.get("edge_id"),
            "consumed_by_event": str(edge.get("edge_id")) in consumed_relation_ids,
            "self_relation_after_canonicalization": canonical_source == canonical_target,
        }
        relation_info = canonicalize_relation(edge.get("evidence"), stage9_lexicon)
        relation_record["canonical_relation"] = relation_info["canonical"]
        relation_record["relation_parent_chain"] = relation_info["parent_chain"]
        relation_record["count_channel"] = relation_info["count_channel"]
        relation_record["count_keys"] = relation_info["count_keys"]
        relation_record["lexical_canonicalization"] = relation_info["lexical_canonicalization"]
        if relation_record["canonical_relation"] != relation_record["raw_relation"]:
            notes.append(
                {
                    "kind": "relation_lexical_canonicalized",
                    "raw_edge_id": edge.get("edge_id"),
                    "raw_relation": edge.get("evidence"),
                    "canonical": relation_record["canonical_relation"],
                    "source": relation_info["source"],
                }
            )
        if source_selection is not None:
            relation_record["source_selection"] = source_selection
        canonical_relations.append(relation_record)

    canonical_facts = build_canonical_facts(
        mentions=mentions,
        edges=edges,
        reference_model=reference_model,
        entities_by_id=entities_by_id,
        canonical_events=canonical_events,
        canonical_relations=canonical_relations,
        stage9_lexicon=stage9_lexicon,
    )

    output = dict(record)
    output["stage9"] = {
        "canonical_entities": canonical_entities,
        "entity_links": reference_model["entity_links"],
        "canonical_events": canonical_events,
        "canonical_relations": canonical_relations,
        "canonical_facts": canonical_facts,
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


def build_canonical_facts(
    *,
    mentions: list[dict[str, object]],
    edges: list[dict[str, object]],
    reference_model: dict[str, object],
    entities_by_id: dict[str, dict[str, object]],
    canonical_events: list[dict[str, object]],
    canonical_relations: list[dict[str, object]],
    stage9_lexicon: Stage9CanonicalLexicon,
) -> list[dict[str, object]]:
    mention_to_entity = reference_model["mention_to_entity"]
    mentions_by_id = {str(mention.get("mention_id")): mention for mention in mentions if mention.get("mention_id")}
    facts: list[dict[str, object]] = []

    def next_id() -> str:
        return f"cf{len(facts)}"

    for entity in reference_model["entities"]:
        if not entity.get("count_eligible", True):
            continue
        canonical = str(entity.get("canonical_lemma") or "")
        parents = list(entity.get("parent_chain", []))
        facts.append(
            {
                "fact_id": next_id(),
                "fact_type": "entity_exists",
                "entity_id": entity.get("entity_id"),
                "canonical": canonical,
                "parent_chain": parents,
                "count_channel": entity.get("count_channel"),
                "count_keys": entity.get("count_keys"),
                "count_key": make_fact_count_key(["entity_exists", canonical]),
                "count_eligible": True,
                "raw_mention_ids": entity.get("raw_mention_ids", []),
                "confidence": entity.get("lexical_canonicalization", {}).get("confidence"),
            }
        )

    for edge in edges:
        edge_type = edge.get("edge_type")
        if edge_type not in {"has_attribute", "candidate_has_attribute", "has_quantity"}:
            continue
        source_entity_id = mention_to_entity.get(str(edge.get("source")))
        source_entity = entities_by_id.get(str(source_entity_id))
        target = mentions_by_id.get(str(edge.get("target")))
        if source_entity is None or target is None:
            continue
        if not source_entity.get("count_eligible", True):
            continue

        if edge_type == "has_quantity":
            value = canonicalize_quantity(target)
            fact_type = "has_quantity"
            value_key = "quantity"
        else:
            value = canonicalize_attribute(target, stage9_lexicon)
            fact_type = "has_attribute" if edge_type == "has_attribute" else "candidate_has_attribute"
            value_key = "attribute"

        source_lemma = str(source_entity.get("canonical_lemma") or "")
        value_canonical = str(value["canonical"])
        count_eligible = edge_type != "candidate_has_attribute" and edge.get("confidence") != "low"
        facts.append(
            {
                "fact_id": next_id(),
                "fact_type": fact_type,
                "source_entity": source_entity_id,
                "source_canonical": source_lemma,
                value_key: value_canonical,
                f"{value_key}_parent_chain": value["parent_chain"],
                "count_channel": value["count_channel"],
                "count_keys": value["count_keys"],
                "count_key": make_fact_count_key([fact_type, source_lemma, value_canonical]),
                "count_eligible": count_eligible,
                "raw_edge_id": edge.get("edge_id"),
                "raw_target_mention_id": edge.get("target"),
                "confidence": edge.get("confidence"),
                "lexical_canonicalization": value["lexical_canonicalization"],
            }
        )

    for event in canonical_events:
        action = str(event.get("canonical_action") or "")
        facts.append(
            {
                "fact_id": next_id(),
                "fact_type": "action_event",
                "event_id": event.get("event_id"),
                "action": action,
                "action_parent_chain": event.get("action_parent_chain", []),
                "count_channel": event.get("count_channel"),
                "count_keys": event.get("count_keys"),
                "count_key": make_fact_count_key(["action_event", action]),
                "count_eligible": bool(action),
                "raw_action_mention_id": event.get("action_mention_id"),
                "confidence": event.get("lexical_canonicalization", {}).get("confidence"),
            }
        )
        for role in event.get("roles", []):
            target_entity = entities_by_id.get(str(role.get("canonical_target")))
            target_lemma = str(target_entity.get("canonical_lemma") or "") if target_entity else ""
            facts.append(
                {
                    "fact_id": next_id(),
                    "fact_type": "event_role",
                    "event_id": event.get("event_id"),
                    "action": action,
                    "role": role.get("role"),
                    "target_entity": role.get("canonical_target"),
                    "target_canonical": target_lemma,
                    "count_key": make_fact_count_key(["event_role", action, role.get("role"), target_lemma]),
                    "count_eligible": bool(action and target_lemma),
                    "raw_edge_id": role.get("raw_edge_id"),
                    "confidence": role.get("confidence"),
                }
            )

    for relation in canonical_relations:
        source_entity = entities_by_id.get(str(relation.get("canonical_source")))
        target_entity = entities_by_id.get(str(relation.get("canonical_target")))
        source_lemma = str(source_entity.get("canonical_lemma") or "") if source_entity else ""
        target_lemma = str(target_entity.get("canonical_lemma") or "") if target_entity else ""
        relation_label = str(relation.get("canonical_relation") or "")
        count_eligible = bool(
            relation_label
            and source_lemma
            and target_lemma
            and not relation.get("consumed_by_event")
            and not relation.get("self_relation_after_canonicalization")
        )
        facts.append(
            {
                "fact_id": next_id(),
                "fact_type": "relation",
                "relation_id": relation.get("relation_id"),
                "source_entity": relation.get("canonical_source"),
                "target_entity": relation.get("canonical_target"),
                "source_canonical": source_lemma,
                "relation": relation_label,
                "relation_parent_chain": relation.get("relation_parent_chain", []),
                "target_canonical": target_lemma,
                "count_channel": relation.get("count_channel"),
                "count_keys": relation.get("count_keys"),
                "count_key": make_fact_count_key(["relation", source_lemma, relation_label, target_lemma]),
                "count_eligible": count_eligible,
                "raw_edge_id": relation.get("raw_edge_id"),
                "confidence": relation.get("confidence"),
            }
        )

    return facts


def update_summary(record: dict[str, object], counters: dict[str, Counter[str]]) -> None:
    stage9 = record.get("stage9", {})
    entities = stage9.get("canonical_entities", []) if isinstance(stage9, dict) else []
    entity_links = stage9.get("entity_links", []) if isinstance(stage9, dict) else []
    events = stage9.get("canonical_events", []) if isinstance(stage9, dict) else []
    relations = stage9.get("canonical_relations", []) if isinstance(stage9, dict) else []
    facts = stage9.get("canonical_facts", []) if isinstance(stage9, dict) else []
    notes = stage9.get("canonicalization_notes", []) if isinstance(stage9, dict) else []
    counters["records"]["records"] += 1
    counters["records"][str(record.get("parse_path", "unknown"))] += 1
    for entity in entities:
        counters["entities"][str(entity.get("entity_type", ""))] += 1
        counters["semantic_types"][str(entity.get("semantic_type", ""))] += 1
        for parent in entity.get("parent_chain", []):
            counters["entity_parents"][str(parent)] += 1
        if not entity.get("count_eligible", True):
            counters["entities"]["not_count_eligible"] += 1
        lexical = entity.get("lexical_canonicalization", {})
        if isinstance(lexical, dict):
            counters["entity_canonical_sources"][str(lexical.get("canonical_source") or lexical.get("source") or "")] += 1
            counters["entity_parent_sources"][str(lexical.get("parent_source") or "")] += 1
    for link in entity_links:
        counters["entity_links"][str(link.get("link_type", ""))] += 1
    for event in events:
        counters["events"][str(event.get("canonical_action", ""))] += 1
        for parent in event.get("action_parent_chain", []):
            counters["action_parents"][str(parent)] += 1
        lexical = event.get("lexical_canonicalization", {})
        if isinstance(lexical, dict):
            counters["action_canonical_sources"][str(lexical.get("canonical_source") or lexical.get("source") or "")] += 1
            counters["action_parent_sources"][str(lexical.get("parent_source") or "")] += 1
        for role in event.get("roles", []):
            counters["roles"][str(role.get("role", ""))] += 1
            if role.get("recovered_from_skipped_edge"):
                counters["roles"]["recovered_from_skipped_edge"] += 1
    for relation in relations:
        counters["relations"][str(relation.get("canonical_relation", ""))] += 1
        for parent in relation.get("relation_parent_chain", []):
            counters["relation_parents"][str(parent)] += 1
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
        lexical = relation.get("lexical_canonicalization", {})
        if isinstance(lexical, dict):
            counters["relation_canonical_sources"][str(lexical.get("canonical_source") or lexical.get("source") or "")] += 1
            counters["relation_parent_sources"][str(lexical.get("parent_source") or "")] += 1
    for fact in facts:
        counters["facts"][str(fact.get("fact_type", ""))] += 1
        if fact.get("count_eligible"):
            counters["facts"]["count_eligible"] += 1
            counters["fact_count_keys"][str(fact.get("count_key", ""))] += 1
        else:
            counters["facts"]["not_count_eligible"] += 1
        for parent_key in (fact.get("count_keys") or {}).get("parents", []):
            counters["fact_parent_count_keys"][str(parent_key)] += 1
    for note in notes:
        counters["notes"][str(note.get("kind", ""))] += 1


def markdown_count_table(counter: Counter[str]) -> str:
    if not counter:
        return "_none_"
    lines = ["| item | count |", "| --- | ---: |"]
    for key, value in counter.most_common():
        lines.append(f"| `{key}` | {value} |")
    return "\n".join(lines)


def write_summary(
    path: Path,
    counters: dict[str, Counter[str]],
    *,
    input_path: Path,
    lexicon_paths: dict[str, Path],
) -> None:
    lines = [
        "# Stage 9 Canonicalization Summary",
        "",
        f"- input: `{input_path}`",
        f"- phrasal_action_lexicon: `{lexicon_paths['phrasal_action']}`",
        f"- object_synonym_lexicon: `{lexicon_paths['object']}`",
        f"- object_parent_lexicon: `{lexicon_paths['object_parent']}`",
        f"- object_mwe_canonical_lexicon: `{lexicon_paths['object_mwe']}`",
        f"- action_synonym_lexicon: `{lexicon_paths['action']}`",
        f"- action_parent_lexicon: `{lexicon_paths['action_parent']}`",
        f"- attribute_canonical_lexicon: `{lexicon_paths['attribute']}`",
        f"- relation_canonical_lexicon: `{lexicon_paths['relation']}`",
        f"- preposition_mwe_lexicon: `{lexicon_paths['preposition_mwe']}`",
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
        "## Canonical Entity Parents",
        "",
        markdown_count_table(counters["entity_parents"]),
        "",
        "## Entity Canonical Sources",
        "",
        markdown_count_table(counters["entity_canonical_sources"]),
        "",
        "## Entity Parent Sources",
        "",
        markdown_count_table(counters["entity_parent_sources"]),
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
        "## Canonical Action Parents",
        "",
        markdown_count_table(counters["action_parents"]),
        "",
        "## Canonical Action Sources",
        "",
        markdown_count_table(counters["action_canonical_sources"]),
        "",
        "## Canonical Action Parent Sources",
        "",
        markdown_count_table(counters["action_parent_sources"]),
        "",
        "## Canonical Relation Parents",
        "",
        markdown_count_table(counters["relation_parents"]),
        "",
        "## Canonical Relation Sources",
        "",
        markdown_count_table(counters["relation_canonical_sources"]),
        "",
        "## Canonical Relation Parent Sources",
        "",
        markdown_count_table(counters["relation_parent_sources"]),
        "",
        "## Canonical Facts",
        "",
        markdown_count_table(counters["facts"]),
        "",
        "## Top Canonical Fact Count Keys",
        "",
        markdown_count_table(counters["fact_count_keys"]),
        "",
        "## Top Canonical Fact Parent Count Keys",
        "",
        markdown_count_table(counters["fact_parent_count_keys"]),
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
    parser.add_argument("--object-canonical-lexicon", type=Path, default=DEFAULT_OBJECT_CANONICAL_LEXICON)
    parser.add_argument("--object-parent-lexicon", type=Path, default=DEFAULT_OBJECT_PARENT_LEXICON)
    parser.add_argument("--object-mwe-canonical-lexicon", type=Path, default=DEFAULT_OBJECT_MWE_CANONICAL_LEXICON)
    parser.add_argument("--action-canonical-lexicon", type=Path, default=DEFAULT_ACTION_CANONICAL_LEXICON)
    parser.add_argument("--action-parent-lexicon", type=Path, default=DEFAULT_ACTION_PARENT_LEXICON)
    parser.add_argument("--attribute-canonical-lexicon", type=Path, default=DEFAULT_ATTRIBUTE_CANONICAL_LEXICON)
    parser.add_argument("--relation-canonical-lexicon", type=Path, default=DEFAULT_RELATION_CANONICAL_LEXICON)
    parser.add_argument("--preposition-mwe-lexicon", type=Path, default=DEFAULT_PREPOSITION_MWE_LEXICON)
    args = parser.parse_args()

    phrasal_lexicon = load_phrasal_action_lexicon(args.phrasal_action_lexicon)
    stage9_lexicon = load_stage9_canonical_lexicon(
        object_path=args.object_canonical_lexicon,
        action_path=args.action_canonical_lexicon,
        object_parent_path=args.object_parent_lexicon,
        action_parent_path=args.action_parent_lexicon,
        object_mwe_path=args.object_mwe_canonical_lexicon,
        attribute_path=args.attribute_canonical_lexicon,
        relation_path=args.relation_canonical_lexicon,
        preposition_mwe_path=args.preposition_mwe_lexicon,
    )
    counters: dict[str, Counter[str]] = defaultdict(Counter)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open_text(args.output, "wt") as handle:
        for record in iter_jsonl(args.input):
            canonicalized = canonicalize_record(
                record,
                phrasal_lexicon=phrasal_lexicon,
                stage9_lexicon=stage9_lexicon,
            )
            update_summary(canonicalized, counters)
            handle.write(json.dumps(canonicalized, ensure_ascii=False) + "\n")

    if args.summary_output:
        write_summary(
            args.summary_output,
            counters,
            input_path=args.input,
            lexicon_paths={
                "phrasal_action": args.phrasal_action_lexicon,
                "object": args.object_canonical_lexicon,
                "object_parent": args.object_parent_lexicon,
                "object_mwe": args.object_mwe_canonical_lexicon,
                "action": args.action_canonical_lexicon,
                "action_parent": args.action_parent_lexicon,
                "attribute": args.attribute_canonical_lexicon,
                "relation": args.relation_canonical_lexicon,
                "preposition_mwe": args.preposition_mwe_lexicon,
            },
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
