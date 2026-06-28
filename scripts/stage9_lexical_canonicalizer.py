from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
LEXICON_DIR = ROOT / "resources" / "lexicons"

DEFAULT_OBJECT_CANONICAL_LEXICON = LEXICON_DIR / "stage9_object_canonical_seed.tsv"
DEFAULT_ACTION_CANONICAL_LEXICON = LEXICON_DIR / "stage9_action_canonical_seed.tsv"
DEFAULT_ATTRIBUTE_CANONICAL_LEXICON = LEXICON_DIR / "attribute_clean_core_typed_candidate.tsv"
DEFAULT_RELATION_CANONICAL_LEXICON = LEXICON_DIR / "relation_span_clean_core.tsv"
DEFAULT_PREPOSITION_MWE_LEXICON = LEXICON_DIR / "preposition_mwe_clean_core.tsv"


@dataclass(frozen=True)
class LexicalEntry:
    term: str
    canonical: str
    parent_chain: tuple[str, ...]
    count_channel: str
    confidence: str
    source: str
    notes: str = ""


@dataclass(frozen=True)
class Stage9CanonicalLexicon:
    objects: dict[str, LexicalEntry]
    actions: dict[str, LexicalEntry]
    attributes: dict[str, LexicalEntry]
    relations: dict[str, LexicalEntry]


def norm_space(value: object) -> str:
    return " ".join(str(value or "").strip().lower().replace("_", " ").split())


def norm_key(value: object) -> str:
    return norm_space(value).replace(" ", "_")


def slug(value: object) -> str:
    return norm_key(value)


def split_pipe(value: object) -> tuple[str, ...]:
    seen: set[str] = set()
    out: list[str] = []
    for item in str(value or "").split("|"):
        item_norm = norm_key(item)
        if item_norm and item_norm not in seen:
            seen.add(item_norm)
            out.append(item_norm)
    return tuple(out)


def lookup_keys(value: object) -> tuple[str, ...]:
    spaced = norm_space(value)
    underscored = spaced.replace(" ", "_")
    if not spaced:
        return ()
    return tuple(dict.fromkeys([underscored, spaced]))


def add_entry(entries: dict[str, LexicalEntry], entry: LexicalEntry) -> None:
    for key in lookup_keys(entry.term):
        entries.setdefault(key, entry)
    for key in lookup_keys(entry.canonical):
        entries.setdefault(key, entry)


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_seed_entries(path: Path) -> dict[str, LexicalEntry]:
    entries: dict[str, LexicalEntry] = {}
    for row in read_tsv(path):
        term = norm_key(row.get("term", ""))
        if not term:
            continue
        canonical = norm_key(row.get("canonical") or term)
        parent_chain = split_pipe(row.get("parent_chain", ""))
        count_channel = norm_key(row.get("count_channel") or "concept")
        entry = LexicalEntry(
            term=term,
            canonical=canonical,
            parent_chain=parent_chain,
            count_channel=count_channel,
            confidence=norm_key(row.get("confidence") or "medium"),
            source=row.get("source", "").strip() or path.name,
            notes=row.get("notes", "").strip(),
        )
        add_entry(entries, entry)
    return entries


def load_attribute_entries(path: Path) -> dict[str, LexicalEntry]:
    entries: dict[str, LexicalEntry] = {}
    for row in read_tsv(path):
        term = norm_key(row.get("term", ""))
        if not term:
            continue
        canonical = norm_key(row.get("canonical") or term)
        primary_role = norm_key(row.get("primary_role") or "attribute")
        parents = tuple(
            dict.fromkeys(
                item
                for item in (primary_role, *split_pipe(row.get("parent_types", "")), "visual_attribute")
                if item
            )
        )
        entry = LexicalEntry(
            term=term,
            canonical=canonical,
            parent_chain=parents,
            count_channel=primary_role,
            confidence=norm_key(row.get("confidence") or "medium"),
            source=row.get("sources", "").strip() or row.get("provenance", "").strip() or path.name,
            notes=row.get("provenance", "").strip(),
        )
        add_entry(entries, entry)
    return entries


def load_relation_entries(*paths: Path) -> dict[str, LexicalEntry]:
    entries: dict[str, LexicalEntry] = {}
    for path in paths:
        for row in read_tsv(path):
            term = norm_key(row.get("term", ""))
            if not term:
                continue
            canonical = norm_key(row.get("canonical") or term)
            relation_type = norm_key(row.get("relation_type") or "relation")
            entry = LexicalEntry(
                term=term,
                canonical=canonical,
                parent_chain=tuple(dict.fromkeys([relation_type, "visual_relation"])),
                count_channel=relation_type,
                confidence=norm_key(row.get("confidence") or "medium"),
                source=row.get("sources", "").strip() or row.get("source", "").strip() or path.name,
                notes=row.get("notes", "").strip() or row.get("provenance", "").strip(),
            )
            add_entry(entries, entry)
    return entries


def load_stage9_canonical_lexicon(
    *,
    object_path: Path = DEFAULT_OBJECT_CANONICAL_LEXICON,
    action_path: Path = DEFAULT_ACTION_CANONICAL_LEXICON,
    attribute_path: Path = DEFAULT_ATTRIBUTE_CANONICAL_LEXICON,
    relation_path: Path = DEFAULT_RELATION_CANONICAL_LEXICON,
    preposition_mwe_path: Path = DEFAULT_PREPOSITION_MWE_LEXICON,
) -> Stage9CanonicalLexicon:
    return Stage9CanonicalLexicon(
        objects=load_seed_entries(object_path),
        actions=load_seed_entries(action_path),
        attributes=load_attribute_entries(attribute_path),
        relations=load_relation_entries(relation_path, preposition_mwe_path),
    )


def lookup_entry(entries: dict[str, LexicalEntry], *values: object) -> LexicalEntry | None:
    for value in values:
        for key in lookup_keys(value):
            entry = entries.get(key)
            if entry is not None:
                return entry
    return None


def count_keys(kind: str, canonical: str, parent_chain: tuple[str, ...]) -> dict[str, object]:
    canonical_key = slug(canonical)
    parent_keys = [f"{kind}_parent:{parent}" for parent in parent_chain]
    return {
        "canonical": f"{kind}:{canonical_key}" if canonical_key else "",
        "parents": parent_keys,
    }


def entity_parent_fallback(entity: dict[str, Any]) -> tuple[str, ...]:
    entity_type = norm_key(entity.get("entity_type"))
    semantic = norm_key(entity.get("semantic_type"))
    if entity_type == "context":
        return ("scene_context",)
    if semantic and semantic not in {"object", "group"}:
        if semantic == "person":
            return ("person", "human")
        if semantic == "animal":
            return ("animal", "living_thing")
        if semantic == "clothing":
            return ("clothing", "wearable")
        if semantic == "vehicle":
            return ("vehicle",)
        if semantic == "device":
            return ("device", "artifact")
        if semantic == "document":
            return ("document", "text_carrier", "artifact")
        return (semantic,)
    return ()


def canonicalize_entity(
    entity: dict[str, Any],
    lexicon: Stage9CanonicalLexicon,
) -> dict[str, Any]:
    raw_lemma = entity.get("canonical_lemma") or entity.get("text") or ""
    entry = lookup_entry(lexicon.objects, raw_lemma, entity.get("text"))
    if entry is not None:
        canonical = entry.canonical
        parent_chain = entry.parent_chain
        source = entry.source
        confidence = entry.confidence
    else:
        canonical = slug(raw_lemma)
        parent_chain = entity_parent_fallback(entity)
        source = "semantic_type_fallback" if parent_chain else "raw_lemma"
        confidence = "medium" if parent_chain else "low"

    out = dict(entity)
    out["raw_canonical_lemma"] = raw_lemma
    out["canonical_lemma"] = canonical
    out["parent_chain"] = list(parent_chain)
    out["count_channel"] = "entity"
    out["count_keys"] = count_keys("entity", canonical, parent_chain)
    out["lexical_canonicalization"] = {
        "source": source,
        "confidence": confidence,
    }
    return out


def canonicalize_action(
    canonical_action: object,
    lexicon: Stage9CanonicalLexicon,
) -> dict[str, Any]:
    entry = lookup_entry(lexicon.actions, canonical_action)
    if entry is not None:
        canonical = entry.canonical
        parent_chain = entry.parent_chain
        source = entry.source
        confidence = entry.confidence
    else:
        canonical = slug(canonical_action)
        parent_chain = ("visual_action",) if canonical else ()
        source = "raw_action"
        confidence = "low"
    return {
        "canonical": canonical,
        "parent_chain": list(parent_chain),
        "count_channel": "action",
        "count_keys": count_keys("action", canonical, parent_chain),
        "source": source,
        "confidence": confidence,
    }


def canonicalize_attribute(
    mention: dict[str, Any],
    lexicon: Stage9CanonicalLexicon,
) -> dict[str, Any]:
    entry = lookup_entry(lexicon.attributes, mention.get("lemma"), mention.get("text"))
    if entry is not None:
        canonical = entry.canonical
        parent_chain = entry.parent_chain
        count_channel = entry.count_channel
        source = entry.source
        confidence = entry.confidence
    else:
        role = norm_key(mention.get("role"))
        canonical = slug(mention.get("lemma") or mention.get("text"))
        parent_chain = tuple(dict.fromkeys([role, "visual_attribute"] if role else ["visual_attribute"]))
        count_channel = role or "attribute"
        source = "raw_attribute_role"
        confidence = norm_key(mention.get("confidence") or "low")
    return {
        "canonical": canonical,
        "parent_chain": list(parent_chain),
        "count_channel": count_channel,
        "count_keys": count_keys("attribute", canonical, parent_chain),
        "source": source,
        "confidence": confidence,
    }


def canonicalize_quantity(mention: dict[str, Any]) -> dict[str, Any]:
    role = norm_key(mention.get("role")) or "quantity"
    canonical = slug(mention.get("lemma") or mention.get("text"))
    parent_chain = tuple(dict.fromkeys([role, "quantity"]))
    return {
        "canonical": canonical,
        "parent_chain": list(parent_chain),
        "count_channel": role,
        "count_keys": count_keys("quantity", canonical, parent_chain),
        "source": "raw_quantity_role",
        "confidence": norm_key(mention.get("confidence") or "medium"),
    }


def canonicalize_relation(
    relation: object,
    lexicon: Stage9CanonicalLexicon,
) -> dict[str, Any]:
    relation_surface = str(relation or "").split(";", 1)[0]
    entry = lookup_entry(lexicon.relations, relation_surface)
    if entry is not None:
        canonical = entry.canonical
        parent_chain = entry.parent_chain
        count_channel = entry.count_channel
        source = entry.source
        confidence = entry.confidence
    else:
        canonical = slug(relation_surface)
        parent_chain = ("visual_relation",) if canonical else ()
        count_channel = "relation"
        source = "raw_relation"
        confidence = "low"
    return {
        "canonical": canonical,
        "parent_chain": list(parent_chain),
        "count_channel": count_channel,
        "count_keys": count_keys("relation", canonical, parent_chain),
        "source": source,
        "confidence": confidence,
    }


def entity_display(entity_id: object, entities_by_id: dict[str, dict[str, Any]]) -> str:
    entity = entities_by_id.get(str(entity_id))
    if not entity:
        return ""
    return str(entity.get("canonical_lemma") or "")


def make_fact_count_key(parts: list[object]) -> str:
    return ":".join(slug(part) for part in parts if slug(part))
