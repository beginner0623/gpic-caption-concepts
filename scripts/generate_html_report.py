"""Generate a static HTML report for GPIC caption-to-concept results.

The report is intentionally static: it can be opened from disk and shared
without a local web server.  HTML pages show the top rows and example captions;
complete count tables are written as TSV files in the report's data directory.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


DEFAULT_INPUT = Path(
    "reports/canonical_concepts_10k_train00000_00099_trf_auto_frozen_v1.jsonl"
)
DEFAULT_OUTPUT = Path("reports/html_report_10k_auto_frozen_v1")


@dataclass
class CountEntry:
    count: int = 0
    captions: set[int] = field(default_factory=set)
    examples: list[tuple[int, str, str]] = field(default_factory=list)
    raws: Counter[str] = field(default_factory=Counter)
    parents: Counter[str] = field(default_factory=Counter)
    sources: Counter[str] = field(default_factory=Counter)
    extra: Counter[str] = field(default_factory=Counter)


def esc(value: Any) -> str:
    if value is None:
        return ""
    return html.escape(str(value), quote=True)


def norm(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


def first_parent(chain: list[str] | None) -> str:
    return chain[0] if chain else ""


def parent_str(chain: list[str] | None) -> str:
    return " > ".join(chain or [])


def short_text(text: str, limit: int = 170) -> str:
    text = " ".join((text or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


def top_items(counter: Counter[str], n: int = 8) -> str:
    if not counter:
        return ""
    return ", ".join(f"{item} ({count})" for item, count in counter.most_common(n))


def source_from_lexical(obj: dict[str, Any] | None) -> str:
    if not obj:
        return ""
    lex = obj.get("lexical_canonicalization") or {}
    parts = []
    for key in (
        "source",
        "canonical_source",
        "parent_source",
        "confidence",
        "canonical_confidence",
        "parent_confidence",
    ):
        value = lex.get(key)
        if value:
            parts.append(f"{key}={value}")
    return "; ".join(parts)


def add_count(
    table: dict[tuple[str, ...], CountEntry],
    key: tuple[str, ...],
    row_index: int,
    caption_id: str,
    caption: str,
    raw: str = "",
    parents: list[str] | None = None,
    source: str = "",
    extra: str = "",
) -> None:
    entry = table[key]
    entry.count += 1
    entry.captions.add(row_index)
    if raw:
        entry.raws[raw] += 1
    for parent in parents or []:
        if parent:
            entry.parents[parent] += 1
    if source:
        entry.sources[source] += 1
    if extra:
        entry.extra[extra] += 1
    if len(entry.examples) < 8:
        entry.examples.append((row_index, caption_id, short_text(caption, 140)))


def case_link(row_index: int, page_size: int, label: str | None = None) -> str:
    page_start = ((row_index - 1) // page_size) * page_size + 1
    page_end = page_start + page_size - 1
    page = f"cases/cases_{page_start:05d}_{page_end:05d}.html"
    return f'<a href="{page}#case-{row_index}">{esc(label or row_index)}</a>'


def example_links(examples: list[tuple[int, str, str]], page_size: int) -> str:
    links = []
    for row_index, _, caption in examples[:5]:
        links.append(f"{case_link(row_index, page_size)}: {esc(short_text(caption, 70))}")
    return "<br>".join(links)


def page_shell(title: str, active: str, body: str, depth: str = "") -> str:
    nav_groups = [
        ("Overview", [("index.html", "Home"), ("results_overview.html", "10k Overview")]),
        ("Method", [("method_rulebook.html", "Method Rulebook"), ("stage_rules.html", "Stage Rules")]),
        ("Concepts", [
            ("objects.html", "Objects"),
            ("attributes.html", "Attributes"),
            ("attribute_types.html", "Attr Types"),
            ("object_attribute_pairs.html", "Obj-Attr Pairs"),
        ]),
        ("Structure", [
            ("actions.html", "Actions"),
            ("event_roles.html", "Agent / Patient"),
            ("relations.html", "Relations"),
            ("relation_triples.html", "Relation Triples"),
            ("facts.html", "Facts"),
        ]),
        ("Audit", [("parents.html", "Parents"), ("quality_audit.html", "Quality")]),
    ]
    nav_parts = []
    for group_label, links in nav_groups:
        active_child = next((label for _, label in links if label == active), "")
        summary_class = "active" if active_child else ""
        summary_label = group_label + (f'<span>{esc(active_child)}</span>' if active_child else "")
        item_html = "\n".join(
            f'<a class="{"active" if label == active else ""}" href="{depth}{href}">{label}</a>'
            for href, label in links
        )
        nav_parts.append(
            f'<details class="nav-menu"><summary class="{summary_class}">{summary_label}</summary><div class="nav-menu-items">{item_html}</div></details>'
        )
    nav_html = "\n".join(nav_parts)
    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <link rel="stylesheet" href="{depth}assets/report.css">
  <script defer src="{depth}assets/report.js"></script>
</head>
<body>
  <header class="topbar">
    <div>
      <div class="eyebrow">GPIC Caption-To-Concept</div>
      <h1>{esc(title)}</h1>
    </div>
    <nav>{nav_html}</nav>
  </header>
  <main>
{body}
  </main>
</body>
</html>
"""


def metric_card(label: str, value: Any, note: str = "") -> str:
    return (
        '<div class="metric">'
        f'<div class="metric-label">{esc(label)}</div>'
        f'<div class="metric-value">{esc(value)}</div>'
        f'<div class="metric-note">{esc(note)}</div>'
        "</div>"
    )


def html_table(headers: list[str], rows: list[list[Any]], classes: str = "") -> str:
    thead = "".join(f"<th>{esc(h)}</th>" for h in headers)
    body_rows = []
    for row in rows:
        body_rows.append("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>")
    return (
        f'<div class="table-wrap"><table class="{classes}">'
        f"<thead><tr>{thead}</tr></thead><tbody>{''.join(body_rows)}</tbody></table></div>"
    )


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_tsv(path: Path, headers: list[str], rows: list[list[Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        writer.writerow(headers)
        writer.writerows(rows)


def count_rows(
    table: dict[tuple[str, ...], CountEntry],
    columns: list[str],
    page_size: int,
    limit: int | None = None,
) -> list[list[Any]]:
    rows = []
    sorted_items = sorted(table.items(), key=lambda kv: (-kv[1].count, kv[0]))
    if limit is not None:
        sorted_items = sorted_items[:limit]
    for key, entry in sorted_items:
        row = [esc(item) for item in key]
        row.extend(
            [
                esc(entry.count),
                esc(len(entry.captions)),
                esc(top_items(entry.raws)),
                esc(top_items(entry.parents)),
                esc(top_items(entry.sources, 4)),
                esc(top_items(entry.extra, 4)),
                example_links(entry.examples, page_size),
            ]
        )
        rows.append(row)
    return rows


def count_tsv_rows(table: dict[tuple[str, ...], CountEntry]) -> list[list[Any]]:
    rows = []
    for key, entry in sorted(table.items(), key=lambda kv: (-kv[1].count, kv[0])):
        examples = "|".join(str(row_index) for row_index, _, _ in entry.examples)
        captions = "|".join(caption_id for _, caption_id, _ in entry.examples)
        rows.append(
            list(key)
            + [
                entry.count,
                len(entry.captions),
                top_items(entry.raws, 20),
                top_items(entry.parents, 20),
                top_items(entry.sources, 12),
                top_items(entry.extra, 12),
                examples,
                captions,
            ]
        )
    return rows


def table_section(
    title: str,
    description: str,
    headers: list[str],
    rows: list[list[Any]],
) -> str:
    return f"""
<section class="panel">
  <div class="section-head">
    <h2>{esc(title)}</h2>
    <p>{esc(description)}</p>
  </div>
  <input class="table-filter" placeholder="filter rows..." data-filter-next-table>
  {html_table(headers, rows, "sortable")}
</section>
"""


def render_case_summary_record(record: dict[str, Any]) -> str:
    row_index = int(record.get("row_index") or 0)
    caption_id = norm(record.get("caption_id"))
    caption = norm(record.get("caption"))
    skipped = record.get("skipped_edges") or []
    stage9 = record.get("stage9") or {}
    entities = [
        e.get("canonical_lemma")
        for e in stage9.get("canonical_entities") or []
        if e.get("count_eligible", True)
    ]
    actions = [e.get("canonical_action") for e in stage9.get("canonical_events") or []]
    relations = [
        r.get("canonical_relation") or r.get("raw_relation")
        for r in stage9.get("canonical_relations") or []
    ]
    facts = stage9.get("canonical_facts") or []
    detail_href = f"../case_details/case_{row_index:05d}.html"

    def compact(items: list[str], limit: int = 10) -> str:
        counts = Counter(item for item in items if item)
        if not counts:
            return '<span class="muted">none</span>'
        shown = [f"<span>{esc(k)} ({v})</span>" for k, v in counts.most_common(limit)]
        if len(counts) > limit:
            shown.append(f'<span class="muted">+{len(counts) - limit} more</span>')
        return "".join(shown)

    return f"""
<section class="case case-summary" id="case-{row_index}">
  <div class="case-title">
    <h2>Case {row_index:05d}</h2>
    <a class="button-link" href="{detail_href}">Open Detail</a>
  </div>
  <div class="caption-box">{esc(caption)}</div>
  <div class="chips">
    <span>caption_id: {esc(caption_id)}</span>
    <span>shape: {esc(record.get("caption_shape"))}</span>
    <span>parse: {esc(record.get("parse_path"))}</span>
    <span>quotes: {len(record.get("quote_mentions") or [])}</span>
    <span>entities: {len(entities)}</span>
    <span>actions: {len(actions)}</span>
    <span>relations: {len(relations)}</span>
    <span>facts: {len(facts)}</span>
    <span>skipped: {len(skipped)}</span>
  </div>
  <div class="mini-grid">
    <div><h3>Top Entities</h3><div class="chips compact">{compact(entities)}</div></div>
    <div><h3>Top Actions</h3><div class="chips compact">{compact(actions)}</div></div>
    <div><h3>Top Relations</h3><div class="chips compact">{compact(relations)}</div></div>
  </div>
</section>
"""


def render_case_detail_record(record: dict[str, Any]) -> str:
    row_index = int(record.get("row_index") or 0)
    caption_id = norm(record.get("caption_id"))
    caption = norm(record.get("caption"))
    mentions = record.get("concept_mentions") or []
    edges = record.get("edges") or []
    skipped = record.get("skipped_edges") or []
    stage9 = record.get("stage9") or {}
    mention_by_id = {m.get("mention_id"): m for m in mentions}
    entity_by_id = {e.get("entity_id"): e for e in stage9.get("canonical_entities") or []}

    def mention_label(mid: str) -> str:
        m = mention_by_id.get(mid) or {}
        text = m.get("text") or mid
        typ = m.get("concept_type") or ""
        return f"{esc(text)} <span class=\"muted\">{esc(mid)} {esc(typ)}</span>"

    entity_rows = []
    for entity in stage9.get("canonical_entities") or []:
        entity_rows.append(
            [
                esc(entity.get("entity_id")),
                esc(entity.get("text")),
                esc(entity.get("canonical_lemma")),
                esc(parent_str(entity.get("parent_chain") or [])),
                esc(source_from_lexical(entity)),
            ]
        )

    attribute_rows = []
    for fact in stage9.get("canonical_facts") or []:
        if fact.get("fact_type") == "has_attribute":
            attribute_rows.append(
                [
                    esc(fact.get("source_canonical")),
                    esc(fact.get("attribute")),
                    esc(parent_str(fact.get("attribute_parent_chain") or [])),
                    esc(fact.get("confidence")),
                ]
            )

    event_rows = []
    for event in stage9.get("canonical_events") or []:
        role_bits = []
        for role in event.get("roles") or []:
            target_id = role.get("canonical_target")
            target = entity_by_id.get(target_id, {})
            target_text = target.get("canonical_lemma") or target_id or role.get("target")
            voice = role.get("voice_normalization")
            role_bits.append(
                f"{esc(role.get('role'))}: {esc(target_text)}"
                + (f" <span class=\"muted\">{esc(voice)}</span>" if voice and voice != "none" else "")
            )
        event_rows.append(
            [
                esc(event.get("raw_action_text")),
                esc(event.get("canonical_action")),
                esc(parent_str(event.get("action_parent_chain") or [])),
                "<br>".join(role_bits),
                esc(source_from_lexical(event)),
            ]
        )

    relation_rows = []
    for rel in stage9.get("canonical_relations") or []:
        source = entity_by_id.get(rel.get("canonical_source"), {})
        target = entity_by_id.get(rel.get("canonical_target"), {})
        relation_rows.append(
            [
                esc(source.get("canonical_lemma") or rel.get("canonical_source")),
                esc(rel.get("raw_relation")),
                esc(rel.get("canonical_relation")),
                esc(target.get("canonical_lemma") or rel.get("canonical_target")),
                esc(parent_str(rel.get("relation_parent_chain") or [])),
                esc(rel.get("confidence")),
            ]
        )

    mention_rows = []
    for m in mentions:
        mention_rows.append(
            [
                esc(m.get("mention_id")),
                esc(m.get("concept_type")),
                esc(m.get("text")),
                esc(m.get("lemma")),
                esc(m.get("role")),
                esc(m.get("confidence")),
            ]
        )

    edge_rows = []
    for edge in edges:
        edge_rows.append(
            [
                esc(edge.get("edge_id")),
                esc(edge.get("edge_type")),
                mention_label(edge.get("source")),
                mention_label(edge.get("target")),
                esc(edge.get("evidence")),
                esc(edge.get("confidence")),
            ]
        )

    fact_rows = []
    for fact in stage9.get("canonical_facts") or []:
        fact_rows.append(
            [
                esc(fact.get("fact_id")),
                esc(fact.get("fact_type")),
                esc(fact.get("count_key")),
                esc(fact.get("confidence")),
            ]
        )

    skipped_rows = []
    for edge in skipped:
        skipped_rows.append(
            [
                esc(edge.get("edge_id")),
                esc(edge.get("edge_type")),
                esc(edge.get("source")),
                esc(edge.get("target")),
                esc(edge.get("reason") or edge.get("evidence")),
            ]
        )

    return f"""
<section class="case" id="case-{row_index}">
  <div class="case-title">
    <h2>Case {row_index:05d}</h2>
    <a href="#case-{row_index}">anchor</a>
  </div>
  <div class="caption-box">{esc(caption)}</div>
  <div class="chips">
    <span>caption_id: {esc(caption_id)}</span>
    <span>shape: {esc(record.get("caption_shape"))}</span>
    <span>parse: {esc(record.get("parse_path"))}</span>
    <span>quotes: {len(record.get("quote_mentions") or [])}</span>
    <span>skipped: {len(skipped)}</span>
  </div>
  <details open>
    <summary>Canonical entities / attributes / events / relations</summary>
    <h3>Entities</h3>
    {html_table(["id", "raw text", "canonical", "parent chain", "source"], entity_rows)}
    <h3>Attributes</h3>
    {html_table(["target", "attribute", "parent chain", "confidence"], attribute_rows)}
    <h3>Events</h3>
    {html_table(["raw action", "canonical", "parent chain", "roles", "source"], event_rows)}
    <h3>Relations</h3>
    {html_table(["source", "raw relation", "canonical", "target", "parent chain", "confidence"], relation_rows)}
  </details>
  <details>
    <summary>Raw mentions / edges</summary>
    <h3>Raw concept mentions</h3>
    {html_table(["id", "type", "text", "lemma", "role", "confidence"], mention_rows)}
    <h3>Raw edges</h3>
    {html_table(["id", "type", "source", "target", "evidence", "confidence"], edge_rows)}
  </details>
  <details>
    <summary>Final countable facts ({len(fact_rows)})</summary>
    {html_table(["id", "type", "count key", "confidence"], fact_rows)}
  </details>
  {('<details><summary>Skipped edges</summary>' + html_table(["id", "type", "source", "target", "reason"], skipped_rows) + '</details>') if skipped_rows else ''}
</section>
"""


def write_assets(output_dir: Path) -> None:
    css = """
:root {
  --bg: #f7f8fb;
  --panel: #ffffff;
  --ink: #18202a;
  --muted: #6b7280;
  --line: #d7dce3;
  --accent: #2563eb;
  --accent-soft: #e8f0ff;
  --good: #0f766e;
  --warn: #b45309;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: Arial, "Malgun Gothic", sans-serif;
  line-height: 1.55;
}
.topbar {
  position: sticky;
  top: 0;
  z-index: 5;
  display: flex;
  gap: 24px;
  align-items: flex-end;
  justify-content: space-between;
  padding: 22px 32px 14px;
  background: rgba(255,255,255,.96);
  border-bottom: 1px solid var(--line);
  backdrop-filter: blur(8px);
}
.topbar h1 { margin: 0; font-size: 26px; letter-spacing: 0; }
.eyebrow { color: var(--muted); font-size: 12px; text-transform: uppercase; }
nav {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  justify-content: flex-end;
  align-items: center;
  max-width: 980px;
}
.nav-menu {
  position: relative;
}
.nav-menu summary {
  list-style: none;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  color: var(--ink);
  text-decoration: none;
  padding: 7px 11px;
  border: 1px solid var(--line);
  background: #fff;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
}
.nav-menu summary::-webkit-details-marker { display: none; }
.nav-menu summary::after {
  content: "v";
  color: var(--muted);
  font-size: 10px;
  margin-left: 2px;
}
.nav-menu summary span {
  color: var(--accent);
  font-weight: 700;
}
.nav-menu summary.active,
.nav-menu[open] summary,
.nav-menu summary:hover {
  background: var(--accent-soft);
  border-color: #9bbcff;
  color: #1d4ed8;
}
.nav-menu-items {
  position: absolute;
  right: 0;
  top: calc(100% + 6px);
  min-width: 190px;
  display: grid;
  gap: 4px;
  padding: 6px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 14px 34px rgba(15, 23, 42, .16);
  z-index: 20;
}
.nav-menu:not([open]) .nav-menu-items { display: none; }
.nav-menu-items a {
  display: block;
  color: var(--ink);
  text-decoration: none;
  padding: 7px 9px;
  border-radius: 5px;
  font-size: 13px;
  white-space: nowrap;
}
.nav-menu-items a.active,
.nav-menu-items a:hover {
  background: var(--accent-soft);
  color: #1d4ed8;
}
.button-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  color: #1d4ed8;
  text-decoration: none;
  padding: 6px 10px;
  border: 1px solid #9bbcff;
  background: var(--accent-soft);
  border-radius: 6px;
  font-size: 13px;
  white-space: nowrap;
}
main { padding: 28px 32px 64px; max-width: 1500px; margin: 0 auto; }
.hero, .panel, .case {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 22px;
  margin-bottom: 22px;
}
.hero h2, .panel h2, .case h2 { margin: 0 0 8px; }
.hero p, .section-head p { margin: 4px 0 16px; color: var(--muted); }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
.metric {
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 14px;
  background: #fbfcff;
}
.metric-label { color: var(--muted); font-size: 12px; }
.metric-value { font-size: 28px; font-weight: 700; margin-top: 4px; }
.metric-note { color: var(--muted); font-size: 12px; margin-top: 2px; }
.table-wrap { overflow: auto; border: 1px solid var(--line); border-radius: 8px; }
table { width: 100%; border-collapse: collapse; background: #fff; font-size: 13px; }
th, td { padding: 8px 10px; border-bottom: 1px solid var(--line); vertical-align: top; }
th { position: sticky; top: 0; background: #eef2f7; text-align: left; white-space: nowrap; }
table.sortable th {
  cursor: pointer;
  user-select: none;
  padding-right: 24px;
}
table.sortable th::after {
  content: " sort";
  color: #9ca3af;
  font-size: 10px;
  font-weight: 400;
}
table.sortable th.sort-asc::after {
  content: " asc";
  color: var(--accent);
}
table.sortable th.sort-desc::after {
  content: " desc";
  color: var(--accent);
}
tr:hover td { background: #f9fbff; }
.table-filter {
  width: 100%;
  max-width: 420px;
  margin: 0 0 10px;
  padding: 8px 10px;
  border: 1px solid var(--line);
  border-radius: 6px;
}
.column-filter-toolbar {
  display: flex;
  gap: 8px;
  align-items: center;
  margin: 0 0 10px;
}
.column-filter-toolbar button {
  padding: 7px 10px;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: #fff;
  color: var(--ink);
  cursor: pointer;
}
.column-filter-toolbar span {
  color: var(--muted);
  font-size: 12px;
}
.column-filter-bar {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
  gap: 8px;
  margin: 0 0 10px;
  padding: 10px;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fbfcff;
}
.column-filter-bar .filter-actions {
  display: flex;
  align-items: flex-start;
}
.column-filter-bar button {
  width: 100%;
  padding: 7px 9px;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: #fff;
  color: var(--ink);
  cursor: pointer;
}
.column-filter {
  margin: 0;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: #fff;
  padding: 7px;
}
.column-filter summary {
  font-size: 12px;
  font-weight: 700;
  color: #374151;
  cursor: pointer;
}
.column-filter input,
.column-filter select {
  width: 100%;
  margin-top: 6px;
  padding: 6px 7px;
  border: 1px solid var(--line);
  border-radius: 5px;
  font: inherit;
  font-size: 12px;
}
.column-filter select {
  min-height: 92px;
}
.column-filter .filter-note {
  margin-top: 5px;
  color: var(--muted);
  font-size: 11px;
}
.caption-box {
  border-left: 4px solid #60a5fa;
  background: #f1f5f9;
  padding: 12px 14px;
  margin: 10px 0;
  font-size: 15px;
}
.chips { display: flex; flex-wrap: wrap; gap: 8px; margin: 10px 0 14px; }
.chips span {
  border: 1px solid var(--line);
  background: #fff;
  padding: 4px 8px;
  border-radius: 999px;
  font-size: 12px;
  color: var(--muted);
}
.chips.compact { margin-bottom: 0; }
.case-summary h3 { margin: 0 0 6px; font-size: 13px; color: #4b5563; }
.mini-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px; }
.mini-grid > div {
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 10px;
  background: #fbfcff;
}
details { margin-top: 12px; }
summary { cursor: pointer; font-weight: 700; color: #1f2937; }
.case-title { display: flex; justify-content: space-between; align-items: center; gap: 12px; }
.muted { color: var(--muted); font-size: 12px; }
.callout { border-left: 4px solid var(--accent); background: var(--accent-soft); padding: 12px 14px; border-radius: 6px; }
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
code { background: #eef2f7; padding: 2px 5px; border-radius: 4px; }
@media (max-width: 900px) {
  .topbar { position: static; display: block; padding: 18px; }
  nav { justify-content: flex-start; margin-top: 12px; }
  main { padding: 18px; }
  .two-col { grid-template-columns: 1fr; }
}
"""
    js = """
const MAX_SELECT_OPTIONS = 250;

function tableRows(table) {
  return Array.from((table.tBodies[0] && table.tBodies[0].rows) || []);
}

function compactText(node) {
  return (node && node.innerText ? node.innerText : '').trim().split(/\s+/).join(' ');
}

function isColumnFilterableHeader(label) {
  const normalized = (label || '').trim().toLowerCase();
  return normalized !== 'sources' && normalized !== 'examples';
}

function parseFilterTerms(value) {
  return (value || '')
    .toLowerCase()
    .split(/[|,]/)
    .map(term => term.trim())
    .filter(Boolean);
}

function textMatchesTerms(text, terms) {
  if (!terms.length) return true;
  const lower = (text || '').toLowerCase();
  return terms.some(term => lower.includes(term));
}

function tableForColumnControl(control) {
  const bar = control.closest('.column-filter-bar');
  const wrap = bar && bar.nextElementSibling;
  return wrap ? wrap.querySelector('table') : null;
}

function applyTableFilters(table) {
  if (!table) return;
  const scope = table.closest('section') || table.parentElement;
  const globalInput = scope ? scope.querySelector('[data-filter-next-table]') : null;
  const globalTerms = parseFilterTerms(globalInput ? globalInput.value : '');
  const filters = table._columnFilters || [];

  for (const row of tableRows(table)) {
    let visible = true;
    const rowText = row.textContent;
    if (!textMatchesTerms(rowText, globalTerms)) visible = false;

    if (visible) {
      for (const filter of filters) {
        const cell = compactText(row.cells[filter.index]);
        const containsTerms = parseFilterTerms(filter.input.value);
        if (!textMatchesTerms(cell, containsTerms)) {
          visible = false;
          break;
        }
        if (filter.select) {
          const selected = Array.from(filter.select.selectedOptions).map(option => option.value);
          if (selected.length && !selected.includes(cell)) {
            visible = false;
            break;
          }
        }
      }
    }

    row.style.display = visible ? '' : 'none';
  }
}

function buildColumnFiltersForTable(table) {
  if (!table || table.dataset.columnFiltersInstalled === '1') return;
  const wrap = table.closest('.table-wrap');
  if (!wrap || !wrap.parentElement) return;
  const headers = Array.from(table.tHead ? table.tHead.rows[0].cells : []);
  if (!headers.length) return;

  const bar = document.createElement('div');
  bar.className = 'column-filter-bar';
  const filters = [];
  const rows = tableRows(table);

  for (const [index, th] of headers.entries()) {
    const headerLabel = compactText(th) || 'column';
    if (!isColumnFilterableHeader(headerLabel)) continue;

    const details = document.createElement('details');
    details.className = 'column-filter';

    const summary = document.createElement('summary');
    summary.textContent = headerLabel;
    details.appendChild(summary);

    const input = document.createElement('input');
    input.type = 'search';
    input.className = 'column-filter-input';
    input.placeholder = 'contains: a|b or a, b';
    input.autocomplete = 'off';
    details.appendChild(input);

    const counts = new Map();
    for (const row of rows) {
      const value = compactText(row.cells[index]);
      if (!value) continue;
      counts.set(value, (counts.get(value) || 0) + 1);
    }
    const values = Array.from(counts.entries()).sort((a, b) => {
      if (b[1] !== a[1]) return b[1] - a[1];
      return a[0].localeCompare(b[0], undefined, {numeric: true, sensitivity: 'base'});
    });

    let select = null;
    if (values.length && values.length <= MAX_SELECT_OPTIONS) {
      select = document.createElement('select');
      select.className = 'column-filter-select';
      select.multiple = true;
      select.size = Math.min(8, Math.max(3, values.length));
      select.title = 'Ctrl/Cmd click으로 여러 값을 선택';
      for (const [value, count] of values) {
        const option = document.createElement('option');
        option.value = value;
        option.textContent = value.length > 80 ? value.slice(0, 77) + '... (' + count + ')' : value + ' (' + count + ')';
        select.appendChild(option);
      }
      details.appendChild(select);
    } else {
      const note = document.createElement('div');
      note.className = 'filter-note';
      note.textContent = values.length + ' unique values. Use contains filter. OR: a|b or a, b';
      details.appendChild(note);
    }

    filters.push({index, input, select});
    bar.appendChild(details);
  }

  const actions = document.createElement('div');
  actions.className = 'filter-actions';
  const reset = document.createElement('button');
  reset.type = 'button';
  reset.className = 'column-filter-reset';
  reset.textContent = 'Reset filters';
  actions.appendChild(reset);
  bar.appendChild(actions);

  table._columnFilters = filters;
  table.dataset.columnFiltersInstalled = '1';
  wrap.parentElement.insertBefore(bar, wrap);
}

function installColumnFilterButtons() {
  for (const table of document.querySelectorAll('table.sortable')) {
    const wrap = table.closest('.table-wrap');
    if (!wrap || !wrap.parentElement || table.dataset.columnFilterButtonInstalled === '1') continue;
    const toolbar = document.createElement('div');
    toolbar.className = 'column-filter-toolbar';
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'column-filter-build';
    button.textContent = 'Show column filters';
    const note = document.createElement('span');
    note.textContent = 'Builds filters only when needed.';
    toolbar.appendChild(button);
    toolbar.appendChild(note);
    wrap.parentElement.insertBefore(toolbar, wrap);
    table.dataset.columnFilterButtonInstalled = '1';
  }
}

document.addEventListener('DOMContentLoaded', installColumnFilterButtons);

document.addEventListener('input', (event) => {
  const input = event.target;
  if (input.matches('[data-filter-next-table]')) {
    applyTableFilters(input.parentElement.querySelector('table'));
    return;
  }
  if (input.matches('.column-filter-input')) {
    applyTableFilters(tableForColumnControl(input));
  }
});

document.addEventListener('change', (event) => {
  const select = event.target;
  if (select.matches('.column-filter-select')) {
    applyTableFilters(tableForColumnControl(select));
  }
});

document.addEventListener('click', (event) => {
  const build = event.target.closest('.column-filter-build');
  if (build) {
    const toolbar = build.closest('.column-filter-toolbar');
    const wrap = toolbar && toolbar.nextElementSibling;
    const table = wrap ? wrap.querySelector('table') : null;
    if (table) {
      build.disabled = true;
      build.textContent = 'Building filters...';
      setTimeout(() => {
        buildColumnFiltersForTable(table);
        toolbar.remove();
      }, 0);
    }
    return;
  }

  const reset = event.target.closest('.column-filter-reset');
  if (reset) {
    const table = tableForColumnControl(reset);
    if (table) {
      for (const filter of table._columnFilters || []) {
        filter.input.value = '';
        if (filter.select) {
          for (const option of filter.select.options) option.selected = false;
        }
      }
      const scope = table.closest('section') || table.parentElement;
      const globalInput = scope ? scope.querySelector('[data-filter-next-table]') : null;
      if (globalInput) globalInput.value = '';
      applyTableFilters(table);
    }
    return;
  }

  const th = event.target.closest('th');
  if (!th || !th.closest('table.sortable')) return;
  const table = th.closest('table');
  const idx = Array.from(th.parentElement.children).indexOf(th);
  const rows = tableRows(table);
  const nextDir = th.dataset.sortDir === 'asc' ? 'desc' : 'asc';
  for (const other of th.parentElement.children) {
    other.classList.remove('sort-asc', 'sort-desc');
    other.removeAttribute('data-sort-dir');
    other.removeAttribute('aria-sort');
  }
  th.dataset.sortDir = nextDir;
  th.classList.add(nextDir === 'asc' ? 'sort-asc' : 'sort-desc');
  th.setAttribute('aria-sort', nextDir === 'asc' ? 'ascending' : 'descending');
  const dir = nextDir === 'asc' ? 1 : -1;
  rows.sort((a, b) => {
    const av = compactText(a.cells[idx]);
    const bv = compactText(b.cells[idx]);
    const an = Number(av.replaceAll(',', '').replace(/%$/, ''));
    const bn = Number(bv.replaceAll(',', '').replace(/%$/, ''));
    if (!Number.isNaN(an) && !Number.isNaN(bn)) return (an - bn) * dir;
    return av.localeCompare(bv, undefined, {numeric: true, sensitivity: 'base'}) * dir;
  });
  rows.forEach(row => table.tBodies[0].appendChild(row));
});
"""
    write_text(output_dir / "assets/report.css", css.strip() + "\n")
    write_text(output_dir / "assets/report.js", js.strip() + "\n")


def method_page() -> str:
    stages = [
        ["1", "Noise removal / caption routing", "raw GPIC caption", "noise 제거는 현재 기본 적용 X. 대신 caption_id/raw caption을 보존하고 tag-list-like 여부를 먼저 기록한다.", "raw caption + caption_shape + parse_path"],
        ["2", "Tokenization", "caption text", "spaCy tokenizer로 token boundary와 offset을 만든다. quote/object MWE/hyphen span protection은 tokenization 직후 하위 rule로 처리한다.", "tokens + protected spans"],
        ["3", "POS tagging", "tokens", "spaCy tagger가 POS/tag를 예측한다. tag-list segment에서는 POS를 보조 신호로만 쓴다.", "POS/tag"],
        ["4", "Predicate span detecting", "tokens + POS", "multi-word predicate/preposition/phrasal-action 후보를 lexicon으로 찾는다. 현재는 parser용 강제 merge보다 Stage 8/9 해석용 span으로 주로 쓴다.", "predicate spans + particles + relation MWE candidates"],
        ["5", "Lemmatize", "tokens + POS/tag", "spaCy lemma를 기본 lemma로 저장한다. lemma는 canonical과 다르며, canonical은 Stage 9에서 한다.", "token/action/object/attribute lemma"],
        ["6", "Dependency parsing", "tokens + POS/lemma", "spaCy parser가 head/dep 구조를 만든다. 여기서는 nsubj, dobj, prep 같은 syntactic edge만 생기고 tuple은 아직 아니다.", "dependency tree"],
        ["7", "Noun chunking", "parsed Doc", "spaCy noun_chunks로 명사구 span/root를 얻는다. object 확정이나 attribute 분리는 아직 하지 않는다.", "noun chunks"],
        ["8", "Raw tuple extractor", "tokens/POS/lemma/dep/noun chunks + routing metadata", "7단계까지의 linguistic evidence를 이용해 object, attribute, quantity, action role, relation, reference raw tuple을 만든다.", "raw mentions + raw edges"],
        ["9", "Canonicalize / countable export", "raw mentions + raw edges", "synonym/frozen lexicon으로 raw를 canonical과 parent로 바꾸고 count_key가 있는 canonical facts와 report table로 내보낸다.", "canonical entities/events/relations/facts"],
    ]
    stage_rows = []
    for stage, name, input_text, summary, output in stages:
        stage_rows.append(
            [
                esc(stage),
                esc(name),
                esc(input_text),
                esc(summary),
                esc(output),
                f'<a href="stage_rules.html#stage-{int(stage):02d}">rules</a>',
            ]
        )
    body = f"""
<section class="hero">
  <h2>최상위 pipeline은 9개 stage로 본다</h2>
  <p>이 report는 네가 정한 caption-to-concept 흐름을 기준으로 정리한다. LLM에게 caption 전체를 맡긴 결과가 아니라, spaCy parse + retokenizer + lexicon + deterministic rule + Stage 9 canonicalization으로 만든 caption-only concept extraction 결과다.</p>
  <div class="callout">핵심 rule은 “문장을 새로 생성하지 않고, GPIC caption의 정보를 countable object, attribute, action, role, relation, parent concept로 바꾸는 것”이다.</div>
</section>
<section class="panel">
  <h2>Stage Overview</h2>
  <p>아래 표가 먼저 봐야 할 전체 지도다. `caption shape routing`, `quote span`, `object MWE`, `scene context`, `reference repair` 같은 세부 처리는 독립 최상위 stage가 아니라 해당 stage의 하위 rule로 배치한다.</p>
  {html_table(["Stage", "이름", "입력", "하는 일", "산출물", "상세"], stage_rows)}
</section>
<section class="panel">
  <h2>Hierarchy Rule</h2>
  {html_table(["하위 rule", "속하는 최상위 stage", "이유"], [
    ["caption shape / tag-list routing", "Stage 1", "dependency나 noun chunk 후에 생기는 정보가 아니라, raw caption 형태를 보고 이후 Stage 8 extractor가 parse를 얼마나 믿을지 정하는 routing metadata다."],
    ["quote span retokenization", "Stage 2", "tokenization 직후 raw quote span을 보호하는 span rule이다."],
    ["object MWE / hyphen noun protection", "Stage 2", "POS/dependency가 깨지기 전에 token span을 보호하는 rule이다."],
    ["multi-word preposition / phrasal action 후보", "Stage 4", "predicate-like span을 찾는 rule이다. 다만 현재 구현에서는 parser 입력을 모두 바꾸기보다 Stage 8/9 해석에 사용한다."],
    ["명사구 root를 object candidate로 삼는 rule", "Stage 8", "noun chunking 자체는 Stage 7이고, object/context/reference로 해석하는 것은 raw tuple extraction이다."],
    ["attribute / quantity 분리", "Stage 8", "noun chunk 내부 modifier를 countable tuple로 바꾸는 extractor rule이다."],
    ["reference/coref/self-edge repair", "Stage 8/9", "Stage 8에서 reference mention/edge를 만들고 Stage 9에서 canonical entity link와 role/relation 복구를 한다."],
    ["synonym, parent, source/provenance", "Stage 9", "raw tuple 이후 countable schema로 정리하는 canonicalization rule이다."],
  ])}
</section>
<section class="panel">
  <h2>Reading Order</h2>
  <ol>
    <li>먼저 이 page에서 9개 최상위 stage와 각 하위 rule의 위치를 본다.</li>
    <li><a href="stage_rules.html">Stage Rules</a>에서 각 stage별 상세 rule과 방어 rule을 본다.</li>
    <li>그 다음 Objects, Attributes, Actions, Agent / Patient, Relations, Facts page에서 실제 count 결과를 확인한다.</li>
    <li>이상한 항목은 Case Detail에서 raw token, dependency, canonical fact로 역추적한다.</li>
  </ol>
</section>
<section class="panel">
  <h2>Canonicalization Scope</h2>
  {html_table(["domain", "report column", "canonicalization 상태", "fallback 의미"], [
    ["Object", "canonical_object", "synonym lexicon, object MWE, plural disambiguation, parent ontology를 적용한다.", "매칭이 없으면 raw lemma를 canonical_object로 둔다."],
    ["Attribute", "canonical_attribute", "attribute clean lexicon과 synonym map을 적용한다. color/material/size/pattern 같은 parent를 붙인다.", "매칭이 없으면 modifier lemma와 raw_attribute_role을 쓴다."],
    ["Action", "canonical_action", "phrasal action whitelist와 action synonym/parent lexicon을 적용한다.", "매칭이 없으면 spaCy lemma 기반 raw_action fallback이라 lemma처럼 보인다."],
    ["Relation", "relation_label", "relation은 raw-preserving 정책이다. 일부 MWE만 정리하고 과도한 synonym collapse는 하지 않는다.", "raw relation label을 거의 그대로 둔다."],
  ])}
</section>
<section class="panel">
  <h2>Source / Provenance Naming</h2>
  <p>sources column은 외부 lexical source, GPIC feedback에서 자동 승격한 내부 source, project ontology, fallback을 섞어서 보여준다. `10k_auto_feedback_v1`은 외부 source가 아니라 GPIC 10k 실행에서 발견한 후보를 fixed rubric으로 자동 승격한 project-internal provenance다.</p>
  {html_table(["source label pattern", "의미", "외부 source 여부"], [
    ["wordnet_synset:*, wordnet_hypernym:*, visual_genome_*, openimages_*, lvis_object, coco_attributes, ovad, vaw, paco, fashionpedia, css_color_4", "외부 사전/데이터셋/벤치마크에서 온 lexical evidence", "external"],
    ["10k_auto_feedback_v1", "GPIC 10k caption 실행에서 수집한 후보", "project-internal GPIC feedback"],
    ["auto_feedback_candidate", "GPIC feedback 후보에서 온 attribute/source type marker", "project-internal GPIC feedback"],
    ["stage9_auto_frozen_v1", "automatic rubric과 regression을 통과해 적용한 frozen lexicon version", "project-internal freeze version"],
    ["fixed_rubric, project_ontology, object_ontology, action_ontology, body_part_ontology", "외부 source가 아니라 프로젝트 기준으로 부여한 판단/상위범주", "project-internal rule"],
    ["raw_lemma, raw_action, raw_attribute_role, semantic_type_fallback, visual_action_fallback, none", "lexicon 매칭 실패 시 원 lemma/role/type으로 남긴 fallback", "fallback"],
  ])}
</section>
<section class="panel">
  <h2>Key Design Decisions</h2>
  <div class="two-col">
    <div>
      <h3>보존하는 것</h3>
      <ul>
        <li>caption_id, row_index, token 근거, raw text</li>
        <li>quote 원문. placeholder 문장을 만들지 않고 raw quote span을 retokenize한다.</li>
        <li>relation raw label. relation은 과도한 synonym collapse를 피하고 원의미를 유지한다.</li>
        <li>canonical과 parent를 분리한다. canonical은 대표어, parent는 countable 상위 범주다.</li>
      </ul>
    </div>
    <div>
      <h3>방어하는 것</h3>
      <ul>
        <li>quote가 object로 들어가는 오염</li>
        <li>tag-list caption에서 dependency를 과신하는 문제</li>
        <li>pronoun/reference가 object count를 오염시키는 문제</li>
        <li>self-edge after coref</li>
        <li>front/side region 표현을 in_front_of 같은 공간관계로 잘못 접는 문제</li>
      </ul>
    </div>
  </div>
</section>
<section class="panel">
  <h2>Auto-Frozen Lexicon Policy</h2>
  <p>100M caption 처리를 전제로 사람이 모든 후보를 직접 audit하지 않는 방향이다. 외부 source와 GPIC feedback candidate를 fixed rubric으로 자동 분류하고, high-confidence 후보만 versioned lexicon으로 freeze한다.</p>
  <ul>
    <li>object synonym / parent</li>
    <li>action synonym / parent</li>
    <li>attribute canonical / subtype</li>
    <li>preposition MWE와 phrasal action은 relation collapse와 action canonicalization을 분리해서 관리</li>
  </ul>
</section>
<section class="panel">
  <h2>Known Limitations</h2>
  <ul>
    <li>hard coreference와 subgroup split(one/another/both)은 아직 long-tail이 남아 있다.</li>
    <li>relation은 raw-preserving 정책이라 parent/canonical relation 분석은 보조 정보로만 본다.</li>
    <li>parent concept가 비어 있는 long-tail object/action은 계속 auto feedback loop로 줄여야 한다.</li>
    <li>HTML case detail은 inspection용이고, 전체 정량 분석은 data/*.tsv를 기준으로 보는 것이 안전하다.</li>
  </ul>
</section>
"""
    return page_shell("Method Rulebook", "Method Rulebook", body)


def stage_rules_page() -> str:
    stage_rules = [
        (
            "01",
            "Noise 성분 제거 / Caption Routing",
            [
                ["최상위 stage", "네가 정의한 1단계다. 현재 기본값은 noise 제거 시행 X.", "caption 원문 정보 손실을 피하고, 반복되는 오염만 나중에 별도 rule 후보로 올린다."],
                ["원문 보존", "caption_id, row_index, raw caption을 그대로 저장한다.", "나중에 어떤 count가 어떤 caption에서 왔는지 역추적할 수 있다."],
                ["caption shape routing", "single-sentence, multi-sentence, tag-list-like caption을 early metadata로 표시한다.", "분기는 여기서 기록한다. 이후 Stage 8에서 tag-list는 dependency를 과신하지 않는 path로 처리한다."],
            ],
        ),
        (
            "02",
            "Tokenization",
            [
                ["최상위 stage", "spaCy tokenizer로 caption을 token sequence로 만든다.", "이후 POS, lemma, dependency, noun chunk가 모두 같은 Doc/token offset을 공유한다."],
                ["quote span retokenize", '"MILE 0" 같은 원문 quote span 자체를 tokenizer 직후 하나의 token으로 merge하고 metadata를 보존한다.', "quote가 object로 새는 문제를 줄이고 원문 텍스트를 잃지 않는다."],
                ["placeholder 금지", 'quote를 "the quoted text" 같은 가짜 문장으로 바꾸지 않는다.', "a the quoted text banner 같은 문법 깨짐을 피한다."],
                ["object MWE / hyphen noun 보호", "신뢰 가능한 object MWE와 hyphen noun span을 tokenizer 직후 merge한다.", "trash can, hot-air balloon처럼 POS/dependency가 깨지는 사례를 줄인다."],
                ["hyphen noun", "hyphenated noun span은 먼저 묶고, 명사/형용사 판정은 이후 단계에서 보수적으로 한다.", "close-up, hot-air balloon 같은 span 붕괴를 줄인다."],
            ],
        ),
        (
            "03",
            "POS Tagging",
            [
                ["최상위 stage", "token마다 coarse POS와 fine-grained tag를 부여한다.", "NOUN/VERB/ADJ/ADP 같은 품사 정보가 뒤 단계의 후보 필터가 된다."],
                ["raw POS 보존", "spaCy가 낸 POS/tag를 raw evidence로 남긴다.", "can, stands, blue jersey 같은 오분석을 숨기지 않고 확인할 수 있다."],
                ["normalized 해석은 후단", "tag-list나 ambiguous token의 보정은 원 POS를 덮어쓰기보다 Stage 8/9 해석에서 제한적으로 한다.", "parser 결과와 후처리 판단을 분리해서 추적 가능하게 한다."],
            ],
        ),
        (
            "04",
            "Predicate Span Detecting",
            [
                ["최상위 stage", "여러 token이 하나의 predicate 의미를 만들 수 있는 span을 찾는다.", "on top of, in front of, next to, pick up 같은 표현을 단일 의미 단위 후보로 관리한다."],
                ["preposition MWE", "preposition_mwe lexicon으로 in front of, on top of, next to 같은 관계 span을 감지한다.", "dependency에서 token이 쪼개져도 Stage 8 relation label은 하나로 만들 수 있다."],
                ["phrasal action 후보", "외부 구동사 seed를 rubric으로 auto-audit한 high-confidence 항목만 action canonicalization 후보로 둔다.", "pick up은 pick_up 후보지만 stand on table은 action stand + relation on으로 유지한다."],
                ["region caution", "front of, on the front of, side of 같은 region 표현은 in_front_of로 자동 접지 않는다.", "logo on the front of shirt 같은 표현을 공간 앞뒤 관계로 오해하지 않게 한다."],
                ["parser merge 원칙", "모든 predicate span을 parser 전에 억지로 한 token으로 만들지는 않는다.", "구문 분석은 가능한 원 구조를 유지하고, span 해석은 Stage 8/9에서 evidence로 쓴다."],
            ],
        ),
        (
            "05",
            "Lemmatize",
            [
                ["최상위 stage", "token별 lemma를 만든다.", "dogs -> dog, wearing -> wear처럼 inflection을 줄여 raw tuple extraction의 기본 표기를 안정화한다."],
                ["lemma != canonical", "lemma는 단어 원형이고 canonical은 synonym까지 합친 대표어다.", "puppy -> puppy는 lemma지만 Stage 9 canonical은 dog가 될 수 있다."],
                ["raw lemma 보존", "object/action/attribute 후보는 raw text와 lemma를 함께 들고 간다.", "나중에 canonicalization이 과한지, lemma fallback인지 확인할 수 있다."],
            ],
        ),
        (
            "06",
            "Dependency Parsing",
            [
                ["최상위 stage", "token 사이의 head/dependency tree를 만든다.", "nsubj, dobj, prep, pobj, amod, compound 같은 구문 근거가 Stage 8 rule의 입력이 된다."],
                ["parse는 tuple이 아님", "dependency edge 자체가 바로 concept tuple은 아니다.", "Stage 8에서 어떤 dep를 object/action/relation/attribute evidence로 쓸지 별도 rule로 결정한다."],
                ["tag-list 주의", "tag-list-like caption은 dependency relation을 과신하지 않는다.", "comma 나열형에서는 parser가 억지 문장 구조를 만들 수 있어서 Stage 8에서 segment/chunk 중심으로 본다."],
                ["batch 처리", "대량 caption은 nlp(caption) 반복이 아니라 nlp.pipe(batch)로 처리한다.", "100M 처리에서 parser 호출 overhead를 줄인다."],
            ],
        ),
        (
            "07",
            "Noun Chunking",
            [
                ["최상위 stage", "spaCy noun_chunks로 명사구 span과 root를 얻는다.", "a blue and white striped hat 같은 span을 object/attribute 후보의 기본 단위로 삼는다."],
                ["아직 object 확정 아님", "noun chunk root를 얻는 것과 object mention으로 확정하는 것은 다르다.", "quote, pronoun, reference, scene_context 오염 제거는 Stage 8에서 한다."],
                ["modifier evidence", "chunk 내부의 amod/compound/det/num 등을 보존한다.", "Stage 8에서 attribute/quantity/object head를 분리하는 데 쓴다."],
                ["segment noun chunk", "tag-list segment 내부에서도 가능한 chunk/root를 만든다.", "tag-list도 sentence caption과 비슷한 output schema로 내보내기 위한 입력이다."],
            ],
        ),
        (
            "08",
            "Raw Tuple Extractor",
            [
                ["최상위 stage", "Stage 2-7의 결과를 이용해 raw concept mention과 raw edge를 만든다.", "여기서부터 object, attribute, quantity, action, relation, reference 같은 tuple이 생긴다."],
                ["object/context/reference", "noun chunk root를 object candidate로 삼되 quote/pronoun/reference/scene context를 분리한다.", "텍스트, 대명사, 배경표현이 object count에 섞이는 것을 줄인다."],
                ["attribute/quantity", "chunk 내부 modifier와 lexicon으로 color/material/size/pattern/quantity 등을 object에서 분리한다.", "blue sky, wooden fence, three dogs 같은 countable attribute/quantity fact를 만든다."],
                ["action/event role", "verb predicate를 action mention으로 만들고 nsubj/dobj/pobj 등으로 agent/patient/theme 후보를 연결한다.", "누가 무엇을 하는지 action-role-target triple로 볼 수 있다."],
                ["preposition relation", "ADP와 Stage 4 MWE span을 이용해 source-relation-target raw relation을 만든다.", "on, under, next to, in front of 같은 spatial/association relation을 count한다."],
                ["reference repair", "pronoun, one/another/both, generic anaphoric noun은 antecedent 후보와 score로 연결하고 self-edge는 drop/repair한다.", "object count 오염을 막으면서 가능한 relation/action role recall을 복구한다."],
                ["tag-list path", "Stage 1에서 tag-list-like로 표시된 caption은 dependency보다 segment noun chunk와 modifier evidence를 더 신뢰한다.", "display, large, indoor 같은 comma-list 오해석을 줄인다."],
            ],
        ),
        (
            "09",
            "Canonicalize",
            [
                ["최상위 stage", "Stage 8 raw tuple을 synonym/frozen lexicon/ontology로 count 가능한 대표형에 매핑한다.", "raw/canonical/parent 세 수준으로 집계할 수 있게 한다."],
                ["object canonical", "puppy/canine -> dog, cab/taxicab -> taxi처럼 object synonym을 대표 concept으로 모은다.", "같은 의미의 object가 여러 표기로 쪼개지는 것을 줄인다."],
                ["attribute canonical", "scarlet/crimson/navy/wooden 같은 attribute를 red/blue/wood 등 대표어와 subtype parent로 정리한다.", "색/재질/상태 등을 raw 단어와 parent subtype 양쪽으로 볼 수 있다."],
                ["action canonical", "wearing/dressed -> wear, seated -> sit, high-confidence phrasal action -> pick_up처럼 action 대표어를 부여한다.", "동작도 lemma만이 아니라 synonym 단위로 점진적으로 합친다."],
                ["parent chain", "canonical concept에 animal, vehicle, clothing, color_attribute, locomotion_action 같은 parent chain을 붙인다.", "raw/canonical/parent 단위의 count table을 모두 만들 수 있다."],
                ["relation policy", "relation은 과한 synonym collapse를 피하고 raw-preserving 정책을 유지한다.", "관계어는 문맥 의존성이 커서 의미를 억지로 합치지 않는다."],
                ["source/confidence", "lexicon source, canonical_source, parent_source, confidence를 같이 보존한다.", "외부 source와 GPIC auto feedback source를 구분해서 audit할 수 있다."],
                ["countable export", "canonical entity/event/relation/fact를 TSV와 HTML table로 내보낸다.", "Objects, Attributes, Actions, Agent / Patient, Relations, Facts, Parents page의 기준이 된다."],
            ],
        ),
    ]
    sections = []
    for stage_id, title, rules in stage_rules:
        rows = [[esc(cell) for cell in row] for row in rules]
        sections.append(
            f"""
<section class="panel" id="stage-{stage_id}">
  <h2>Stage {stage_id}. {esc(title)}</h2>
  {html_table(["rule group", "적용 rule", "이유 / 효과"], rows)}
</section>
"""
        )
    body = f"""
<section class="hero">
  <h2>9개 최상위 stage의 하위 rule</h2>
  <p>이 page는 네가 잡은 pipeline 9단계를 바깥 구조로 두고, 우리가 실제로 넣은 구현 rule을 각 stage 아래에 배치한 것이다. 먼저 전체 흐름은 <a href="method_rulebook.html">Method Rulebook</a>에서 보고, 여기서는 각 stage 안에 어떤 방어 rule과 추출 rule이 들어갔는지 확인한다.</p>
  <div class="callout">caption shape routing, quote span 보호, MWE, scene context, reference repair 같은 항목은 별도 최상위 stage가 아니라 해당 stage 안에서 동작하는 하위 rule이다.</div>
</section>
{''.join(sections)}
"""
    return page_shell("Stage Rules", "Stage Rules", body)


def build_report(args: argparse.Namespace) -> None:
    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    page_size = int(args.case_page_size)
    max_rows = int(args.max_count_rows)

    if not input_path.exists():
        raise FileNotFoundError(input_path)

    write_assets(output_dir)
    (output_dir / "cases").mkdir(parents=True, exist_ok=True)
    (output_dir / "case_details").mkdir(parents=True, exist_ok=True)
    (output_dir / "data").mkdir(parents=True, exist_ok=True)

    object_counts: dict[tuple[str, str], CountEntry] = defaultdict(CountEntry)
    attribute_counts: dict[tuple[str, str], CountEntry] = defaultdict(CountEntry)
    attribute_type_counts: dict[tuple[str], CountEntry] = defaultdict(CountEntry)
    object_attribute_counts: dict[tuple[str, str, str], CountEntry] = defaultdict(CountEntry)
    action_counts: dict[tuple[str, str], CountEntry] = defaultdict(CountEntry)
    event_role_counts: dict[tuple[str, str, str], CountEntry] = defaultdict(CountEntry)
    relation_counts: dict[tuple[str, str], CountEntry] = defaultdict(CountEntry)
    relation_triple_counts: dict[tuple[str, str, str], CountEntry] = defaultdict(CountEntry)
    fact_counts: dict[tuple[str, str], CountEntry] = defaultdict(CountEntry)
    parent_counts: dict[tuple[str, str], CountEntry] = defaultdict(CountEntry)

    totals = Counter()
    parse_path = Counter()
    caption_shape = Counter()
    mention_type = Counter()
    edge_type = Counter()
    fact_type = Counter()
    skipped_reason = Counter()
    parent_none_entities = Counter()
    action_parent_none = Counter()
    raw_attribute_role = Counter()
    self_relations = 0

    case_file = None
    current_start = 0
    case_pages: list[tuple[int, int, str]] = []

    def open_case_page(start: int):
        end = start + page_size - 1
        filename = f"cases_{start:05d}_{end:05d}.html"
        path = output_dir / "cases" / filename
        f = path.open("w", encoding="utf-8", newline="\n")
        links = []
        if start > 1:
            prev_start = max(1, start - page_size)
            prev_end = prev_start + page_size - 1
            links.append(f'<a href="cases_{prev_start:05d}_{prev_end:05d}.html">Previous</a>')
        links.append('<a href="../results_overview.html">Overview</a>')
        links.append('<a href="../objects.html">Objects</a>')
        shell = page_shell(
            f"Cases {start:05d}-{end:05d}",
            "10k Overview",
            '<section class="panel"><p>' + " | ".join(links) + "</p></section>",
            depth="../",
        )
        f.write(shell.replace("  </main>\n</body>\n</html>\n", ""))
        case_pages.append((start, end, "cases/" + filename))
        return f

    def close_case_page(f):
        if f is not None:
            f.write("  </main>\n</body>\n</html>\n")
            f.close()

    def case_group_href(row_index: int) -> str:
        start = ((row_index - 1) // page_size) * page_size + 1
        end = start + page_size - 1
        return f"../cases/cases_{start:05d}_{end:05d}.html#case-{row_index}"

    def write_case_detail_page(record: dict[str, Any]) -> None:
        row_index = int(record.get("row_index") or 0)
        prev_link = ""
        if row_index > 1:
            prev_link = f'<a href="case_{row_index - 1:05d}.html">Previous Case</a>'
        links = [
            '<a href="../results_overview.html">Overview</a>',
            f'<a href="{case_group_href(row_index)}">Back to Case List</a>',
            prev_link,
        ]
        links = [link for link in links if link]
        body = (
            '<section class="panel"><p>'
            + " | ".join(links)
            + "</p><p class=\"muted\">Heavy raw mentions, edges, and facts are isolated on this per-case page so the 500-case list pages stay fast.</p></section>"
            + render_case_detail_record(record)
        )
        write_text(
            output_dir / "case_details" / f"case_{row_index:05d}.html",
            page_shell(f"Case {row_index:05d} Detail", "10k Overview", body, depth="../"),
        )

    with input_path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            record = json.loads(line)
            row_index = int(record.get("row_index") or 0)
            caption_id = norm(record.get("caption_id"))
            caption = norm(record.get("caption"))
            stage9 = record.get("stage9") or {}
            totals["records"] += 1
            parse_path[norm(record.get("parse_path") or "unknown")] += 1
            caption_shape[norm(record.get("caption_shape") or "unknown")] += 1
            totals["quote_mentions"] += len(record.get("quote_mentions") or [])
            totals["skipped_edges"] += len(record.get("skipped_edges") or [])

            for m in record.get("concept_mentions") or []:
                mention_type[norm(m.get("concept_type") or "unknown")] += 1
            for e in record.get("edges") or []:
                edge_type[norm(e.get("edge_type") or "unknown")] += 1
            for e in record.get("skipped_edges") or []:
                skipped_reason[norm(e.get("reason") or e.get("evidence") or "unknown")] += 1

            if (row_index - 1) % page_size == 0:
                close_case_page(case_file)
                current_start = row_index
                case_file = open_case_page(current_start)
            if case_file is not None:
                case_file.write(render_case_summary_record(record))
            write_case_detail_page(record)

            for entity in stage9.get("canonical_entities") or []:
                if not entity.get("count_eligible", True):
                    continue
                canonical = norm(entity.get("canonical_lemma"))
                parent_chain = entity.get("parent_chain") or []
                parent = first_parent(parent_chain)
                raw = norm(entity.get("text"))
                source = source_from_lexical(entity)
                add_count(
                    object_counts,
                    (canonical, parent),
                    row_index,
                    caption_id,
                    caption,
                    raw=raw,
                    parents=parent_chain,
                    source=source,
                    extra=norm(entity.get("semantic_type")),
                )
                if not parent_chain:
                    parent_none_entities[canonical] += 1
                for depth, p in enumerate(parent_chain):
                    add_count(
                        parent_counts,
                        ("entity", p),
                        row_index,
                        caption_id,
                        caption,
                        raw=canonical,
                        extra=f"depth_{depth}",
                    )

            entity_by_id = {
                e.get("entity_id"): e for e in stage9.get("canonical_entities") or []
            }
            mentions_by_id = {
                str(m.get("mention_id")): m
                for m in record.get("concept_mentions") or []
                if m.get("mention_id") is not None
            }

            for fact in stage9.get("canonical_facts") or []:
                ftype = norm(fact.get("fact_type"))
                fact_type[ftype] += 1
                count_key = norm(fact.get("count_key"))
                if count_key:
                    add_count(
                        fact_counts,
                        (ftype, count_key),
                        row_index,
                        caption_id,
                        caption,
                        source=source_from_lexical(fact),
                    )
                if ftype == "has_attribute":
                    attr = norm(fact.get("attribute"))
                    source_obj = norm(fact.get("source_canonical"))
                    parent_chain = fact.get("attribute_parent_chain") or []
                    parent = first_parent(parent_chain)
                    source = source_from_lexical(fact)
                    raw_attr_mention = mentions_by_id.get(str(fact.get("raw_target_mention_id")))
                    raw_attr = norm(
                        (raw_attr_mention or {}).get("text")
                        or (raw_attr_mention or {}).get("lemma")
                        or attr
                    )
                    add_count(
                        attribute_counts,
                        (attr, parent),
                        row_index,
                        caption_id,
                        caption,
                        raw=raw_attr,
                        parents=parent_chain,
                        source=source,
                    )
                    add_count(
                        attribute_type_counts,
                        (parent or "_missing_parent",),
                        row_index,
                        caption_id,
                        caption,
                        raw=attr,
                        parents=parent_chain,
                        source=source,
                    )
                    add_count(
                        object_attribute_counts,
                        (source_obj, attr, parent),
                        row_index,
                        caption_id,
                        caption,
                        raw=raw_attr,
                        parents=parent_chain,
                        source=source,
                    )
                    if "raw_attribute_role" in source:
                        raw_attribute_role[attr] += 1
                    for depth, p in enumerate(parent_chain):
                        add_count(
                            parent_counts,
                            ("attribute", p),
                            row_index,
                            caption_id,
                            caption,
                            raw=attr,
                            extra=f"depth_{depth}",
                        )

            for event in stage9.get("canonical_events") or []:
                action = norm(event.get("canonical_action"))
                parent_chain = event.get("action_parent_chain") or []
                parent = first_parent(parent_chain)
                source = source_from_lexical(event)
                add_count(
                    action_counts,
                    (action, parent),
                    row_index,
                    caption_id,
                    caption,
                    raw=norm(event.get("raw_action_text")),
                    parents=parent_chain,
                    source=source,
                )
                if not parent_chain:
                    action_parent_none[action] += 1
                for depth, p in enumerate(parent_chain):
                    add_count(
                        parent_counts,
                        ("action", p),
                        row_index,
                        caption_id,
                        caption,
                        raw=action,
                        extra=f"depth_{depth}",
                    )
                for role in event.get("roles") or []:
                    target = entity_by_id.get(role.get("canonical_target")) or {}
                    target_canonical = norm(target.get("canonical_lemma") or role.get("canonical_target"))
                    add_count(
                        event_role_counts,
                        (action, norm(role.get("role")), target_canonical),
                        row_index,
                        caption_id,
                        caption,
                        raw=norm(event.get("raw_action_text")),
                        source=norm(role.get("evidence")),
                        extra=norm(role.get("voice_normalization")),
                    )

            for rel in stage9.get("canonical_relations") or []:
                relation = norm(rel.get("canonical_relation") or rel.get("raw_relation"))
                parent_chain = rel.get("relation_parent_chain") or []
                parent = first_parent(parent_chain)
                source_entity = entity_by_id.get(rel.get("canonical_source")) or {}
                target_entity = entity_by_id.get(rel.get("canonical_target")) or {}
                source_obj = norm(source_entity.get("canonical_lemma") or rel.get("canonical_source"))
                target_obj = norm(target_entity.get("canonical_lemma") or rel.get("canonical_target"))
                source = source_from_lexical(rel)
                if rel.get("self_relation_after_canonicalization"):
                    self_relations += 1
                add_count(
                    relation_counts,
                    (relation, parent),
                    row_index,
                    caption_id,
                    caption,
                    raw=norm(rel.get("raw_relation")),
                    parents=parent_chain,
                    source=source,
                )
                add_count(
                    relation_triple_counts,
                    (source_obj, relation, target_obj),
                    row_index,
                    caption_id,
                    caption,
                    raw=norm(rel.get("raw_relation")),
                    parents=parent_chain,
                    source=source,
                )
                for depth, p in enumerate(parent_chain):
                    add_count(
                        parent_counts,
                        ("relation", p),
                        row_index,
                        caption_id,
                        caption,
                        raw=relation,
                        extra=f"depth_{depth}",
                    )

    close_case_page(case_file)

    totals["raw_concept_mentions"] = sum(mention_type.values())
    totals["raw_edges"] = sum(edge_type.values())
    totals["canonical_entities"] = sum(e.count for e in object_counts.values())
    totals["canonical_events"] = sum(e.count for e in action_counts.values())
    totals["canonical_relations"] = sum(e.count for e in relation_counts.values())
    totals["canonical_facts"] = sum(fact_type.values())
    totals["self_relations"] = self_relations

    common_headers = [
        "count",
        "caption_count",
        "raw_variants",
        "parents",
        "sources",
        "extra",
        "examples",
    ]
    write_tsv(
        output_dir / "data/object_counts.tsv",
        ["canonical_object", "parent"] + common_headers[:-1] + ["example_rows", "example_caption_ids"],
        count_tsv_rows(object_counts),
    )
    write_tsv(
        output_dir / "data/attribute_counts.tsv",
        ["canonical_attribute", "parent"] + common_headers[:-1] + ["example_rows", "example_caption_ids"],
        count_tsv_rows(attribute_counts),
    )
    write_tsv(
        output_dir / "data/attribute_type_counts.tsv",
        ["attribute_type"] + common_headers[:-1] + ["example_rows", "example_caption_ids"],
        count_tsv_rows(attribute_type_counts),
    )
    write_tsv(
        output_dir / "data/object_attribute_counts.tsv",
        ["canonical_object", "canonical_attribute", "attribute_parent"] + common_headers[:-1] + ["example_rows", "example_caption_ids"],
        count_tsv_rows(object_attribute_counts),
    )
    write_tsv(
        output_dir / "data/action_counts.tsv",
        ["canonical_action", "parent"] + common_headers[:-1] + ["example_rows", "example_caption_ids"],
        count_tsv_rows(action_counts),
    )
    write_tsv(
        output_dir / "data/event_role_counts.tsv",
        ["canonical_action", "role", "canonical_target"] + common_headers[:-1] + ["example_rows", "example_caption_ids"],
        count_tsv_rows(event_role_counts),
    )
    write_tsv(
        output_dir / "data/relation_counts.tsv",
        ["relation_label", "parent"] + common_headers[:-1] + ["example_rows", "example_caption_ids"],
        count_tsv_rows(relation_counts),
    )
    write_tsv(
        output_dir / "data/relation_triple_counts.tsv",
        ["canonical_source", "relation_label", "canonical_target"] + common_headers[:-1] + ["example_rows", "example_caption_ids"],
        count_tsv_rows(relation_triple_counts),
    )
    write_tsv(
        output_dir / "data/fact_counts.tsv",
        ["fact_type", "count_key"] + common_headers[:-1] + ["example_rows", "example_caption_ids"],
        count_tsv_rows(fact_counts),
    )
    write_tsv(
        output_dir / "data/parent_counts.tsv",
        ["domain", "parent"] + common_headers[:-1] + ["example_rows", "example_caption_ids"],
        count_tsv_rows(parent_counts),
    )

    metric_html = "".join(
        [
            metric_card("captions", f"{totals['records']:,}", "input rows"),
            metric_card("raw mentions", f"{totals['raw_concept_mentions']:,}", "Stage 8 concept mentions"),
            metric_card("raw edges", f"{totals['raw_edges']:,}", "Stage 8 edges"),
            metric_card("entities", f"{totals['canonical_entities']:,}", "canonical object entities"),
            metric_card("events", f"{totals['canonical_events']:,}", "canonical actions"),
            metric_card("relations", f"{totals['canonical_relations']:,}", "canonical/raw-preserved relations"),
            metric_card("facts", f"{totals['canonical_facts']:,}", "final countable facts"),
            metric_card("skipped edges", f"{totals['skipped_edges']:,}", "defensive drops/repairs"),
        ]
    )

    index_body = f"""
<section class="hero">
  <h2>Caption을 countable concept source로 변환한 10k 결과</h2>
  <p>이 HTML report는 GPIC 10k caption에서 Stage 8 raw extraction과 Stage 9 canonicalization을 거쳐 얻은 object, attribute, action, agent, patient, relation, parent concept를 탐색하기 위한 정적 dashboard다.</p>
  <div class="grid">{metric_html}</div>
</section>
<section class="panel">
  <h2>How to Read</h2>
  <ul>
    <li><a href="method_rulebook.html">Method Rulebook</a>: 전체 9개 stage 개요와 핵심 결정 사항.</li>
    <li><a href="stage_rules.html">Stage Rules</a>: 각 stage에서 적용한 상세 rule과 방어 rule.</li>
    <li><a href="results_overview.html">10k Overview</a>: 전체 규모, caption shape, schema별 통계.</li>
    <li><a href="objects.html">Objects</a>, <a href="attributes.html">Attributes</a>, <a href="attribute_types.html">Attr Types</a>, <a href="object_attribute_pairs.html">Obj-Attr Pairs</a>, <a href="actions.html">Actions</a>, <a href="event_roles.html">Agent / Patient</a>, <a href="relations.html">Relations</a>, <a href="relation_triples.html">Relation Triples</a>: countable schema별 top table과 예시 caption link.</li>
    <li><a href="quality_audit.html">Quality</a>: parent missing, fallback, skipped edge 등 다음 개선 지점.</li>
    <li><a href="cases/cases_00001_00500.html">Case Detail</a>: 각 caption별 raw/canonical trace.</li>
  </ul>
</section>
"""
    write_text(output_dir / "index.html", page_shell("Report Home", "Home", index_body))
    write_text(output_dir / "method_rulebook.html", method_page())
    write_text(output_dir / "stage_rules.html", stage_rules_page())

    overview_rows = (
        [[esc(k), esc(v)] for k, v in totals.most_common()]
        + [["parse_path:" + esc(k), esc(v)] for k, v in parse_path.most_common()]
        + [["caption_shape:" + esc(k), esc(v)] for k, v in caption_shape.most_common()]
    )
    schema_rows = (
        [[esc("mention:" + k), esc(v)] for k, v in mention_type.most_common()]
        + [[esc("edge:" + k), esc(v)] for k, v in edge_type.most_common()]
        + [[esc("fact:" + k), esc(v)] for k, v in fact_type.most_common()]
    )
    case_page_rows = [
        [f"{start:,}-{end:,}", f'<a href="{href}">{esc(href)}</a>']
        for start, end, href in case_pages
    ]
    overview_body = f"""
<section class="hero"><div class="grid">{metric_html}</div></section>
{table_section("Run Metrics", "10k report generation에서 집계한 전체 수치.", ["metric", "value"], overview_rows)}
{table_section("Schema Breakdown", "Stage 8 mention/edge와 Stage 9 fact type별 분포.", ["schema", "count"], schema_rows)}
{table_section("Case Detail Pages", "각 case page는 caption별 raw/canonical trace를 포함한다.", ["case range", "page"], case_page_rows)}
"""
    write_text(output_dir / "results_overview.html", page_shell("10k Overview", "10k Overview", overview_body))

    object_headers = ["canonical_object", "parent"] + common_headers
    object_body = table_section(
        "Objects",
        "canonical object 기준 count. raw variants와 parent/source, example caption으로 역추적 가능하다.",
        object_headers,
        count_rows(object_counts, object_headers, page_size, max_rows),
    )
    write_text(output_dir / "objects.html", page_shell("Objects", "Objects", object_body))

    attribute_headers = ["canonical_attribute", "parent"] + common_headers
    obj_attr_headers = ["canonical_object", "canonical_attribute", "attribute_parent"] + common_headers
    attr_body = table_section(
        "Attributes",
        "canonical_attribute 기준 count. parent 컬럼이 color_attribute, size_attribute 같은 subtype이다. 표 header를 클릭하면 각 컬럼 기준으로 오름차순/내림차순 정렬된다.",
        attribute_headers,
        count_rows(attribute_counts, attribute_headers, page_size, max_rows),
    )
    write_text(output_dir / "attributes.html", page_shell("Attributes", "Attributes", attr_body))

    attr_type_headers = ["attribute_type"] + common_headers
    attr_type_body = table_section(
        "Attribute Types",
        "attribute subtype 기준 count. raw_variants에는 해당 subtype 안에서 자주 나온 canonical_attribute가 표시된다.",
        attr_type_headers,
        count_rows(attribute_type_counts, attr_type_headers, page_size, max_rows),
    )
    write_text(output_dir / "attribute_types.html", page_shell("Attribute Types", "Attr Types", attr_type_body))

    obj_attr_body = table_section(
        "Object-Attribute Pairs",
        "어떤 canonical_object에 어떤 canonical_attribute가 붙었는지 보는 table.",
        obj_attr_headers,
        count_rows(object_attribute_counts, obj_attr_headers, page_size, max_rows),
    )
    write_text(
        output_dir / "object_attribute_pairs.html",
        page_shell("Object-Attribute Pairs", "Obj-Attr Pairs", obj_attr_body),
    )

    action_headers = ["canonical_action", "parent"] + common_headers
    role_headers = ["canonical_action", "role", "canonical_target"] + common_headers
    action_body = table_section(
        "Actions",
        "canonical_action 기준 count. action synonym이 없으면 raw_action fallback이라 lemma처럼 보일 수 있다.",
        action_headers,
        count_rows(action_counts, action_headers, page_size, max_rows),
    )
    write_text(output_dir / "actions.html", page_shell("Actions", "Actions", action_body))

    roles_body = table_section(
        "Agent / Patient",
        "canonical_action-role-canonical_target triple 기준 count. 최종 count용 role은 agent/patient로 정리해서 보여준다.",
        role_headers,
        count_rows(event_role_counts, role_headers, page_size, max_rows),
    )
    write_text(output_dir / "event_roles.html", page_shell("Agent / Patient", "Agent / Patient", roles_body))

    relation_headers = ["relation_label", "parent"] + common_headers
    triple_headers = ["canonical_source", "relation_label", "canonical_target"] + common_headers
    relation_body = table_section(
        "Relations",
        "relation_label 기준 count. relation은 raw-preserving 정책을 유지하므로 canonical collapse보다 원문 의미 보존을 우선한다.",
        relation_headers,
        count_rows(relation_counts, relation_headers, page_size, max_rows),
    )
    write_text(output_dir / "relations.html", page_shell("Relations", "Relations", relation_body))

    relation_triple_body = table_section(
        "Relation Triples",
        "canonical_source-relation_label-canonical_target triple 기준 count.",
        triple_headers,
        count_rows(relation_triple_counts, triple_headers, page_size, max_rows),
    )
    write_text(
        output_dir / "relation_triples.html",
        page_shell("Relation Triples", "Relation Triples", relation_triple_body),
    )

    fact_headers = ["fact_type", "count_key"] + common_headers
    fact_body = table_section(
        "Final Countable Facts",
        "Stage 9에서 만든 최종 count_key 기준 count.",
        fact_headers,
        count_rows(fact_counts, fact_headers, page_size, max_rows),
    )
    write_text(output_dir / "facts.html", page_shell("Facts", "Facts", fact_body))

    parent_headers = ["domain", "parent"] + common_headers
    parent_body = table_section(
        "Parent Concepts",
        "entity/action/attribute/relation parent concept 기준 count.",
        parent_headers,
        count_rows(parent_counts, parent_headers, page_size, max_rows),
    )
    write_text(output_dir / "parents.html", page_shell("Parents", "Parents", parent_body))

    quality_rows = [
        ["entity parent missing", f"{sum(parent_none_entities.values()):,}", esc(top_items(parent_none_entities, 20))],
        ["action parent missing", f"{sum(action_parent_none.values()):,}", esc(top_items(action_parent_none, 20))],
        ["raw_attribute_role", f"{sum(raw_attribute_role.values()):,}", esc(top_items(raw_attribute_role, 20))],
        ["self_relation_after_canonicalization", f"{self_relations:,}", ""],
        ["skipped_edges", f"{totals['skipped_edges']:,}", esc(top_items(skipped_reason, 20))],
    ]
    quality_body = f"""
<section class="hero">
  <h2>Quality / Audit Surface</h2>
  <p>잘 된 결과뿐 아니라 parent missing, fallback, skipped edge를 같이 보여줘서 다음 feedback loop의 방향을 잡는다.</p>
</section>
{html_table(["audit item", "count", "top examples"], quality_rows)}
{table_section("Parent Missing Objects", "parent concept가 아직 없는 canonical entity top-N.", ["canonical", "count"], [[esc(k), esc(v)] for k, v in parent_none_entities.most_common(max_rows)])}
{table_section("Action Parent Missing", "action parent가 아직 비어 있는 canonical action top-N.", ["action", "count"], [[esc(k), esc(v)] for k, v in action_parent_none.most_common(max_rows)])}
{table_section("Skipped Edge Reasons", "defensive drop/repair가 발생한 이유.", ["reason", "count"], [[esc(k), esc(v)] for k, v in skipped_reason.most_common(max_rows)])}
"""
    write_text(output_dir / "quality_audit.html", page_shell("Quality Audit", "Quality", quality_body))

    metadata = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "input": str(input_path),
        "output_dir": str(output_dir),
        "case_page_size": page_size,
        "max_count_rows": max_rows,
        "totals": dict(totals),
        "parse_path": dict(parse_path),
        "caption_shape": dict(caption_shape),
    }
    write_text(output_dir / "report_metadata.json", json.dumps(metadata, ensure_ascii=False, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default=str(DEFAULT_INPUT))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--max-count-rows", type=int, default=500)
    parser.add_argument("--case-page-size", type=int, default=500)
    return parser.parse_args()


if __name__ == "__main__":
    build_report(parse_args())


















