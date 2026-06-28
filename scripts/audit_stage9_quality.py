from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import gzip
import json
from pathlib import Path
from typing import Any, Iterable


REFERENCE_LIKE_ENTITY_TYPES = {
    "reference",
    "instance",
    "contrastive_instance",
    "complement_subset",
    "group",
}

GENERIC_ENTITY_LEMMAS = {
    "area",
    "background",
    "center",
    "distance",
    "edge",
    "foreground",
    "front",
    "image",
    "individual",
    "item",
    "object",
    "one",
    "other",
    "part",
    "photo",
    "picture",
    "scene",
    "section",
    "side",
    "site",
    "structure",
    "surface",
    "thing",
    "view",
}

ACTION_WATCHLIST = {
    "appear",
    "be",
    "complete",
    "contain",
    "feature",
    "have",
    "include",
    "indicate",
    "let",
    "make",
    "mean",
    "seem",
    "show",
    "suggest",
}


class Audit:
    def __init__(self, max_examples: int) -> None:
        self.max_examples = max_examples
        self.totals: Counter[str] = Counter()
        self.by_dataset: dict[str, Counter[str]] = defaultdict(Counter)
        self.parent_none: Counter[str] = Counter()
        self.parent_none_semantic: Counter[str] = Counter()
        self.parent_none_examples: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.action_fallback: Counter[str] = Counter()
        self.action_fallback_examples: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.raw_relation: Counter[str] = Counter()
        self.raw_relation_examples: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.raw_attribute: Counter[str] = Counter()
        self.raw_attribute_examples: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.generic_entities: Counter[str] = Counter()
        self.generic_entity_examples: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.reference_like_entities: Counter[str] = Counter()
        self.reference_like_examples: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.self_relations: Counter[str] = Counter()
        self.self_relation_examples: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.skipped_edges: Counter[str] = Counter()
        self.skipped_edge_examples: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.missing_event_targets: Counter[str] = Counter()
        self.missing_relation_targets: Counter[str] = Counter()
        self.note_kinds: Counter[str] = Counter()
        self.entity_link_kinds: Counter[str] = Counter()
        self.action_watchlist: Counter[str] = Counter()
        self.action_watchlist_examples: dict[str, list[dict[str, Any]]] = defaultdict(list)

    def add_example(self, store: dict[str, list[dict[str, Any]]], key: str, example: dict[str, Any]) -> None:
        if len(store[key]) < self.max_examples:
            store[key].append(example)


def open_text(path: Path, mode: str):
    if path.suffix == ".gz":
        return gzip.open(path, mode, encoding="utf-8")
    return path.open(mode, encoding="utf-8")


def iter_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with open_text(path, "rt") as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(line)


def dataset_label(path: Path) -> str:
    name = path.name
    if name.startswith("canonical_concepts_"):
        name = name.removeprefix("canonical_concepts_")
    if name.endswith("_stage9_canonical_v2.jsonl"):
        name = name.removesuffix("_stage9_canonical_v2.jsonl")
    return name


def compact(value: object, limit: int = 150) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def case_ref(dataset: str, record: dict[str, Any]) -> str:
    row = record.get("row_index")
    caption_id = str(record.get("caption_id") or "")[:10]
    return f"{dataset}#{row} ({caption_id})"


def example(record: dict[str, Any], dataset: str, **extra: Any) -> dict[str, Any]:
    out = {
        "case": case_ref(dataset, record),
        "caption": compact(record.get("caption")),
    }
    out.update(extra)
    return out


def mention_lookup(record: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(mention.get("mention_id")): mention
        for mention in record.get("concept_mentions", [])
        if mention.get("mention_id") is not None
    }


def entity_lookup(stage9: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        str(entity.get("entity_id")): entity
        for entity in stage9.get("canonical_entities", [])
        if entity.get("entity_id") is not None
    }


def audit_record(record: dict[str, Any], dataset: str, audit: Audit) -> None:
    stage9 = record.get("stage9", {}) or {}
    entities = stage9.get("canonical_entities", []) or []
    events = stage9.get("canonical_events", []) or []
    relations = stage9.get("canonical_relations", []) or []
    facts = stage9.get("canonical_facts", []) or []
    notes = stage9.get("canonicalization_notes", []) or []
    links = stage9.get("entity_links", []) or []
    skipped = record.get("skipped_edges", []) or []
    entities_by_id = entity_lookup(stage9)

    audit.totals["records"] += 1
    audit.totals["entities"] += len(entities)
    audit.totals["events"] += len(events)
    audit.totals["relations"] += len(relations)
    audit.totals["facts"] += len(facts)
    audit.totals["skipped_edges"] += len(skipped)
    audit.by_dataset[dataset]["records"] += 1
    audit.by_dataset[dataset]["entities"] += len(entities)
    audit.by_dataset[dataset]["events"] += len(events)
    audit.by_dataset[dataset]["relations"] += len(relations)
    audit.by_dataset[dataset]["facts"] += len(facts)
    audit.by_dataset[dataset]["skipped_edges"] += len(skipped)

    for entity in entities:
        canonical = str(entity.get("canonical_lemma") or "")
        entity_type = str(entity.get("entity_type") or "")
        semantic = str(entity.get("semantic_type") or "")
        parent_chain = entity.get("parent_chain") or []
        if entity.get("count_eligible", True) and not parent_chain:
            audit.parent_none[canonical] += 1
            audit.parent_none_semantic[semantic or entity_type or "unknown"] += 1
            audit.by_dataset[dataset]["entity_parent_none"] += 1
            audit.add_example(
                audit.parent_none_examples,
                canonical,
                example(
                    record,
                    dataset,
                    text=entity.get("text"),
                    entity_type=entity_type,
                    semantic_type=semantic,
                    entity_id=entity.get("entity_id"),
                ),
            )
        if canonical in GENERIC_ENTITY_LEMMAS and entity.get("count_eligible", True):
            key = f"{canonical} [{entity_type}]"
            audit.generic_entities[key] += 1
            audit.add_example(
                audit.generic_entity_examples,
                key,
                example(record, dataset, text=entity.get("text"), parent="|".join(parent_chain)),
            )
        if entity_type in REFERENCE_LIKE_ENTITY_TYPES and entity.get("count_eligible", True):
            key = f"{entity_type}:{canonical}"
            audit.reference_like_entities[key] += 1
            audit.add_example(
                audit.reference_like_examples,
                key,
                example(record, dataset, text=entity.get("text"), raw_mentions=",".join(entity.get("raw_mention_ids", []))),
            )

    for event in events:
        action = str(event.get("canonical_action") or "")
        lexical = event.get("lexical_canonicalization", {}) or {}
        if lexical.get("parent_source") == "visual_action_fallback":
            audit.action_fallback[action] += 1
            audit.by_dataset[dataset]["action_parent_fallback"] += 1
            audit.add_example(
                audit.action_fallback_examples,
                action,
                example(
                    record,
                    dataset,
                    raw_action=event.get("raw_action_text"),
                    raw_lemma=event.get("raw_action_lemma"),
                    event_id=event.get("event_id"),
                ),
            )
        if action in ACTION_WATCHLIST:
            audit.action_watchlist[action] += 1
            audit.add_example(
                audit.action_watchlist_examples,
                action,
                example(record, dataset, raw_action=event.get("raw_action_text"), parent="|".join(event.get("action_parent_chain", []))),
            )
        for role in event.get("roles", []) or []:
            target = str(role.get("canonical_target") or "")
            if not target or target not in entities_by_id:
                key = f"{action}:{role.get('role') or ''}"
                audit.missing_event_targets[key] += 1

    for relation in relations:
        rel = str(relation.get("canonical_relation") or relation.get("raw_relation") or "")
        lexical = relation.get("lexical_canonicalization", {}) or {}
        if lexical.get("canonical_source") == "raw_relation" or lexical.get("parent_source") == "raw_relation":
            key = str(relation.get("raw_relation") or rel)
            audit.raw_relation[key] += 1
            audit.by_dataset[dataset]["raw_relation"] += 1
            audit.add_example(
                audit.raw_relation_examples,
                key,
                example(
                    record,
                    dataset,
                    source=relation.get("canonical_source"),
                    relation=rel,
                    target=relation.get("canonical_target"),
                ),
            )
        if relation.get("self_relation_after_canonicalization"):
            audit.self_relations[rel] += 1
            audit.by_dataset[dataset]["self_relation_after_canonicalization"] += 1
            audit.add_example(
                audit.self_relation_examples,
                rel,
                example(record, dataset, raw_edge_id=relation.get("raw_edge_id"), raw_relation=relation.get("raw_relation")),
            )
        for endpoint in ("canonical_source", "canonical_target"):
            target = str(relation.get(endpoint) or "")
            if not target or target not in entities_by_id:
                audit.missing_relation_targets[f"{rel}:{endpoint}"] += 1

    for fact in facts:
        if fact.get("fact_type") not in {"has_attribute", "candidate_has_attribute"}:
            continue
        lexical = fact.get("lexical_canonicalization", {}) or {}
        if lexical.get("canonical_source") == "raw_attribute_role" or lexical.get("parent_source") == "raw_attribute_role":
            attr = str(fact.get("attribute") or "")
            audit.raw_attribute[attr] += 1
            audit.by_dataset[dataset]["raw_attribute_role"] += 1
            audit.add_example(
                audit.raw_attribute_examples,
                attr,
                example(
                    record,
                    dataset,
                    source=fact.get("source_canonical"),
                    fact_type=fact.get("fact_type"),
                    confidence=fact.get("confidence"),
                ),
            )

    for skipped_edge in skipped:
        reason = str(
            skipped_edge.get("reason")
            or skipped_edge.get("skip_reason")
            or skipped_edge.get("edge_type")
            or "unknown"
        )
        audit.skipped_edges[reason] += 1
        audit.add_example(audit.skipped_edge_examples, reason, example(record, dataset, skipped_edge=skipped_edge))
    for note in notes:
        audit.note_kinds[str(note.get("kind") or "unknown")] += 1
    for link in links:
        audit.entity_link_kinds[str(link.get("link_type") or "unknown")] += 1


def md_table(headers: list[str], rows: list[list[Any]]) -> str:
    if not rows:
        return "_none_"
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(md_cell(item) for item in row) + " |")
    return "\n".join(lines)


def md_cell(value: Any) -> str:
    text = str(value if value is not None else "")
    text = text.replace("|", "\\|").replace("\n", " ")
    return text


def counter_table(counter: Counter[str], *, top_n: int, label: str = "item") -> str:
    return md_table([label, "count"], [[key, value] for key, value in counter.most_common(top_n)])


def example_lines(examples: list[dict[str, Any]]) -> str:
    if not examples:
        return ""
    chunks = []
    for item in examples:
        fields = [f"`{item.get('case')}`"]
        for key, value in item.items():
            if key in {"case", "caption"}:
                continue
            if value is not None and value != "":
                fields.append(f"{key}={compact(value, 120)}")
        fields.append(f"caption=\"{item.get('caption')}\"")
        chunks.append("; ".join(fields))
    return "<br>".join(chunks)


def issue_table(counter: Counter[str], examples: dict[str, list[dict[str, Any]]], *, top_n: int, label: str) -> str:
    rows = []
    for key, value in counter.most_common(top_n):
        rows.append([key, value, example_lines(examples.get(key, []))])
    return md_table([label, "count", "examples"], rows)


def write_report(path: Path, inputs: list[Path], audit: Audit, top_n: int) -> None:
    lines: list[str] = []
    total_records = audit.totals.get("records", 0)
    parent_none_count = sum(audit.parent_none.values())
    action_fallback_count = sum(audit.action_fallback.values())
    raw_relation_count = sum(audit.raw_relation.values())
    raw_attribute_count = sum(audit.raw_attribute.values())
    lines.append(f"# Stage 9 Quality Audit: {total_records} Captions")
    lines.append("")
    lines.append("이 문서는 Stage 9 canonical 결과에서 다음 확장/수정 후보를 자동으로 긁은 audit report다. 여기 나온 항목은 오류 확정이 아니라, fixed rubric 기반 automatic audit과 regression test로 승격 여부를 판단할 후보 queue다.")
    lines.append("")
    lines.append("## Inputs")
    lines.append("")
    for p in inputs:
        lines.append(f"- `{p}`")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append("")
    summary_rows = []
    for dataset, counter in audit.by_dataset.items():
        summary_rows.append([
            dataset,
            counter.get("records", 0),
            counter.get("entities", 0),
            counter.get("entity_parent_none", 0),
            counter.get("events", 0),
            counter.get("action_parent_fallback", 0),
            counter.get("relations", 0),
            counter.get("raw_relation", 0),
            counter.get("raw_attribute_role", 0),
            counter.get("self_relation_after_canonicalization", 0),
            counter.get("skipped_edges", 0),
        ])
    summary_rows.append([
        "combined",
        audit.totals.get("records", 0),
        audit.totals.get("entities", 0),
        sum(audit.parent_none.values()),
        audit.totals.get("events", 0),
        sum(audit.action_fallback.values()),
        audit.totals.get("relations", 0),
        sum(audit.raw_relation.values()),
        sum(audit.raw_attribute.values()),
        sum(audit.self_relations.values()),
        audit.totals.get("skipped_edges", 0),
    ])
    lines.append(md_table([
        "dataset", "records", "entities", "parent_none", "events", "action_fallback", "relations", "raw_relation", "raw_attribute", "self_relation", "skipped_edges"
    ], summary_rows))
    lines.append("")
    lines.append("## Priority Read")
    lines.append("")
    lines.append(f"1. `entity_parent_none`이 가장 큰 병목이다. 현재 입력 {total_records}개 기준 {parent_none_count}개가 남아 있다.")
    lines.append(f"2. `action_parent_fallback`은 {action_fallback_count}개다. 이 중 일부는 parent만 추가하면 되고, 일부는 action으로 세면 안 되는 predicate인지 automatic audit rubric으로 분리해야 한다.")
    lines.append(f"3. `raw_relation`은 {raw_relation_count}개다. relation은 의미 분류를 강제하지 않고 raw-preserving key로 유지하는 정책이 더 안전하다.")
    lines.append(f"4. `raw_attribute_role`은 {raw_attribute_count}개다. 외부 attribute 사전에 없거나 compound modifier로만 들어온 표현이며, 명확한 것만 subtype/synonym v2 후보로 본다.")
    lines.append("5. reference-like entity는 실패 확정이 아니다. `one/other/another`류 instance split이 제대로 됐는지 보는 자동 후보 큐로 쓰면 된다.")
    lines.append("")
    lines.append("## Entity Parent None")
    lines.append("")
    lines.append("parent가 비어 있으면 coarse count가 불가능하다. high-frequency 항목부터 WordNet/OpenImages/LVIS/COCO parent 후보를 만들어 `stage9_object_parent_expansion_v2.tsv`로 승격하는 게 다음 작업이다.")
    lines.append("")
    lines.append("### By Semantic Type")
    lines.append("")
    lines.append(counter_table(audit.parent_none_semantic, top_n=top_n, label="semantic/entity type"))
    lines.append("")
    lines.append("### Top Missing Parents")
    lines.append("")
    lines.append(issue_table(audit.parent_none, audit.parent_none_examples, top_n=top_n, label="canonical entity"))
    lines.append("")
    lines.append("## Action Parent Fallback")
    lines.append("")
    lines.append("`visual_action_fallback`은 action parent lexicon에 없는 predicate다. 단순히 parent를 추가할지, action count에서 제외할지, relation/state로 옮길지 나눠야 한다.")
    lines.append("")
    lines.append(issue_table(audit.action_fallback, audit.action_fallback_examples, top_n=top_n, label="canonical action"))
    lines.append("")
    lines.append("## Action Watchlist")
    lines.append("")
    lines.append("아래는 parent가 있더라도 countable visual action으로 세는 정책을 automatic audit rubric으로 다시 분류할 만한 predicate다.")
    lines.append("")
    lines.append(issue_table(audit.action_watchlist, audit.action_watchlist_examples, top_n=top_n, label="watch action"))
    lines.append("")
    lines.append("## Raw Relations")
    lines.append("")
    lines.append("relation lexicon에 잡히지 않아 `raw_relation`으로 남은 항목이다. 일부는 그대로 두고, 일부는 semantic relation으로 승격할 후보다.")
    lines.append("")
    lines.append(issue_table(audit.raw_relation, audit.raw_relation_examples, top_n=top_n, label="raw relation"))
    lines.append("")
    lines.append("## Raw Attributes")
    lines.append("")
    lines.append("attribute lexicon 또는 synonym map에 없는 attribute 표현이다. 빈도 높은 항목부터 subtype 분류 후보로 보면 된다.")
    lines.append("")
    lines.append(issue_table(audit.raw_attribute, audit.raw_attribute_examples, top_n=top_n, label="raw attribute"))
    lines.append("")
    lines.append("## Generic / Ambiguous Entities")
    lines.append("")
    lines.append("이 항목들은 항상 오류는 아니지만, count table을 흐릴 가능성이 높다. `scene_context`, `spatial_region`, `generic_alias` 처리 후보로 본다.")
    lines.append("")
    lines.append(issue_table(audit.generic_entities, audit.generic_entity_examples, top_n=top_n, label="generic entity"))
    lines.append("")
    lines.append("## Reference-Like Entities")
    lines.append("")
    lines.append("`one`, `other`, `another`, subgroup split류가 남은 흔적이다. 여기서 높은 빈도는 Stage 9 reference model 개선 후보가 된다.")
    lines.append("")
    lines.append(issue_table(audit.reference_like_entities, audit.reference_like_examples, top_n=top_n, label="reference-like entity"))
    lines.append("")
    lines.append("## Reference / Graph Integrity Signals")
    lines.append("")
    lines.append("### Skipped Edges")
    lines.append("")
    lines.append(issue_table(audit.skipped_edges, audit.skipped_edge_examples, top_n=top_n, label="skip reason"))
    lines.append("")
    lines.append("### Self Relations After Canonicalization")
    lines.append("")
    lines.append(issue_table(audit.self_relations, audit.self_relation_examples, top_n=top_n, label="relation"))
    lines.append("")
    lines.append("### Missing Event Targets")
    lines.append("")
    lines.append(counter_table(audit.missing_event_targets, top_n=top_n, label="event role"))
    lines.append("")
    lines.append("### Missing Relation Targets")
    lines.append("")
    lines.append(counter_table(audit.missing_relation_targets, top_n=top_n, label="relation endpoint"))
    lines.append("")
    lines.append("### Entity Links")
    lines.append("")
    lines.append(counter_table(audit.entity_link_kinds, top_n=top_n, label="link type"))
    lines.append("")
    lines.append("### Canonicalization Notes")
    lines.append("")
    lines.append(counter_table(audit.note_kinds, top_n=top_n, label="note kind"))
    lines.append("")
    lines.append("## Recommended Next Work")
    lines.append("")
    lines.append("1. `Top Missing Parents` 상위 30개를 외부 source 기반으로 parent 후보화한다.")
    lines.append("2. `Action Parent Fallback` 상위 30개를 `visual action parent 추가`, `state/relation으로 이동`, `count 제외 후보`로 3분류한다.")
    lines.append("3. `Raw Relations` 상위 항목을 relation alias/MWE lexicon v2 후보로 만든다.")
    lines.append("4. `Raw Attributes` 중 색/재질/상태/문양으로 명확한 항목만 attribute synonym/subtype v2로 승격한다.")
    lines.append("5. reference-like entity는 1k 샘플에서 반복되는 패턴만 손댄다. 200개에서 case-specific rule을 넣으면 위험하다.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Stage 9 canonicalized caption concept quality.")
    parser.add_argument("--input", action="append", required=True, type=Path, help="Stage 9 canonical JSONL. Can be repeated.")
    parser.add_argument("--output", required=True, type=Path, help="Markdown audit report path.")
    parser.add_argument("--top-n", type=int, default=40)
    parser.add_argument("--max-examples", type=int, default=3)
    args = parser.parse_args()

    audit = Audit(max_examples=args.max_examples)
    for path in args.input:
        dataset = dataset_label(path)
        for record in iter_jsonl(path):
            audit_record(record, dataset, audit)
    write_report(args.output, args.input, audit, args.top_n)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
