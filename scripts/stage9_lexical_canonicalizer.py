from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
LEXICON_DIR = ROOT / "resources" / "lexicons"

LEGACY_OBJECT_CANONICAL_LEXICON = LEXICON_DIR / "stage9_object_canonical_seed.tsv"
LEGACY_ACTION_CANONICAL_LEXICON = LEXICON_DIR / "stage9_action_canonical_seed.tsv"

DEFAULT_OBJECT_CANONICAL_LEXICON = LEXICON_DIR / "stage9_object_synonym_seed.tsv"
DEFAULT_OBJECT_SYNONYM_EXPANSION_LEXICON = LEXICON_DIR / "stage9_object_synonym_expansion_v1.tsv"
DEFAULT_OBJECT_SYNONYM_AUTO_FROZEN_LEXICON = LEXICON_DIR / "stage9_object_synonym_auto_frozen_v1.tsv"
DEFAULT_ACTION_CANONICAL_LEXICON = LEXICON_DIR / "stage9_action_synonym_seed.tsv"
DEFAULT_ACTION_SYNONYM_EXPANSION_LEXICON = LEXICON_DIR / "stage9_action_synonym_expansion_v1.tsv"
DEFAULT_ACTION_SYNONYM_AUTO_FROZEN_LEXICON = LEXICON_DIR / "stage9_action_synonym_auto_frozen_v1.tsv"
DEFAULT_OBJECT_PARENT_LEXICON = LEXICON_DIR / "stage9_object_parent_seed.tsv"
DEFAULT_OBJECT_PARENT_EXPANSION_LEXICON = LEXICON_DIR / "stage9_object_parent_expansion_v1.tsv"
DEFAULT_OBJECT_PARENT_EXPANSION_V2_LEXICON = LEXICON_DIR / "stage9_object_parent_expansion_v2.tsv"
DEFAULT_OBJECT_PARENT_EXPANSION_V3_LEXICON = LEXICON_DIR / "stage9_object_parent_expansion_v3.tsv"
DEFAULT_OBJECT_PARENT_AUTO_FROZEN_LEXICON = LEXICON_DIR / "stage9_object_parent_auto_frozen_v1.tsv"
DEFAULT_ACTION_PARENT_LEXICON = LEXICON_DIR / "stage9_action_parent_seed.tsv"
DEFAULT_ACTION_PARENT_EXPANSION_LEXICON = LEXICON_DIR / "stage9_action_parent_expansion_v1.tsv"
DEFAULT_ACTION_PARENT_EXPANSION_V2_LEXICON = LEXICON_DIR / "stage9_action_parent_expansion_v2.tsv"
DEFAULT_ACTION_PARENT_AUTO_FROZEN_LEXICON = LEXICON_DIR / "stage9_action_parent_auto_frozen_v1.tsv"
DEFAULT_OBJECT_MWE_CANONICAL_LEXICON = LEXICON_DIR / "object_noun_mwe_clean_core.tsv"
DEFAULT_ATTRIBUTE_CANONICAL_LEXICON = LEXICON_DIR / "attribute_clean_core_typed_candidate.tsv"
DEFAULT_ATTRIBUTE_AUTO_FROZEN_LEXICON = LEXICON_DIR / "stage9_attribute_auto_frozen_v1.tsv"
DEFAULT_ATTRIBUTE_SYNONYM_LEXICON = LEXICON_DIR / "stage9_attribute_synonym_seed.tsv"
DEFAULT_ATTRIBUTE_SYNONYM_AUTO_FROZEN_LEXICON = LEXICON_DIR / "stage9_attribute_synonym_auto_frozen_v1.tsv"
DEFAULT_RELATION_CANONICAL_LEXICON = LEXICON_DIR / "relation_span_clean_core.tsv"
DEFAULT_PREPOSITION_MWE_LEXICON = LEXICON_DIR / "preposition_mwe_clean_core.tsv"


@dataclass(frozen=True)
class CanonicalEntry:
    term: str
    canonical: str
    count_channel: str
    confidence: str
    source: str
    notes: str = ""


@dataclass(frozen=True)
class ParentEntry:
    term: str
    parent_chain: tuple[str, ...]
    count_channel: str
    confidence: str
    source: str
    notes: str = ""


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
    object_synonyms: dict[str, CanonicalEntry]
    object_parents: dict[str, ParentEntry]
    action_synonyms: dict[str, CanonicalEntry]
    action_parents: dict[str, ParentEntry]
    attribute_synonyms: dict[str, CanonicalEntry]
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


def source_from_row(row: dict[str, str], path: Path) -> str:
    return (
        row.get("source", "").strip()
        or row.get("sources", "").strip()
        or row.get("provenance", "").strip()
        or path.name
    )


def notes_from_row(row: dict[str, str]) -> str:
    return (
        row.get("notes", "").strip()
        or row.get("reason", "").strip()
        or row.get("rule_id", "").strip()
        or row.get("provenance", "").strip()
    )


def confidence_from_row(row: dict[str, str]) -> str:
    return norm_key(row.get("confidence") or "medium")


def add_entry(entries: dict[str, LexicalEntry], entry: LexicalEntry) -> None:
    for key in lookup_keys(entry.term):
        entries.setdefault(key, entry)
    for key in lookup_keys(entry.canonical):
        entries.setdefault(key, entry)


def add_canonical_entry(entries: dict[str, CanonicalEntry], entry: CanonicalEntry) -> None:
    # Synonym lookup must be source-surface based. Registering canonical keys here would make
    # already-canonical words look as if they came from an unrelated synonym entry.
    for key in lookup_keys(entry.term):
        entries.setdefault(key, entry)


def add_parent_entry(entries: dict[str, ParentEntry], entry: ParentEntry) -> None:
    for key in lookup_keys(entry.term):
        entries.setdefault(key, entry)


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def load_synonym_entries(
    path: Path,
    *,
    default_count_channel: str,
    entries: dict[str, CanonicalEntry] | None = None,
) -> dict[str, CanonicalEntry]:
    entries = entries if entries is not None else {}
    for row in read_tsv(path):
        term = norm_key(row.get("term", ""))
        if not term:
            continue
        canonical = norm_key(row.get("canonical") or term)
        if not canonical:
            continue
        entry = CanonicalEntry(
            term=term,
            canonical=canonical,
            count_channel=norm_key(row.get("count_channel") or default_count_channel),
            confidence=confidence_from_row(row),
            source=source_from_row(row, path),
            notes=notes_from_row(row),
        )
        add_canonical_entry(entries, entry)
    return entries


def load_parent_entries(
    path: Path,
    *,
    default_count_channel: str,
    entries: dict[str, ParentEntry] | None = None,
) -> dict[str, ParentEntry]:
    entries = entries if entries is not None else {}
    for row in read_tsv(path):
        term = norm_key(row.get("canonical") or row.get("term", ""))
        parent_chain = split_pipe(row.get("parent_chain", ""))
        if not term or not parent_chain:
            continue
        entry = ParentEntry(
            term=term,
            parent_chain=parent_chain,
            count_channel=norm_key(row.get("count_channel") or default_count_channel),
            confidence=confidence_from_row(row),
            source=source_from_row(row, path),
            notes=notes_from_row(row),
        )
        add_parent_entry(entries, entry)
    return entries


def load_legacy_seed_synonyms(
    path: Path,
    *,
    default_count_channel: str,
    entries: dict[str, CanonicalEntry] | None = None,
) -> dict[str, CanonicalEntry]:
    entries = entries if entries is not None else {}
    for row in read_tsv(path):
        term = norm_key(row.get("term", ""))
        canonical = norm_key(row.get("canonical") or term)
        if not term or not canonical or term == canonical:
            continue
        entry = CanonicalEntry(
            term=term,
            canonical=canonical,
            count_channel=norm_key(row.get("count_channel") or default_count_channel),
            confidence=confidence_from_row(row),
            source=f"{source_from_row(row, path)}:legacy_synonym",
            notes=notes_from_row(row),
        )
        add_canonical_entry(entries, entry)
    return entries


def load_legacy_seed_parents(
    path: Path,
    *,
    default_count_channel: str,
    entries: dict[str, ParentEntry] | None = None,
) -> dict[str, ParentEntry]:
    entries = entries if entries is not None else {}
    for row in read_tsv(path):
        canonical = norm_key(row.get("canonical") or row.get("term", ""))
        parent_chain = split_pipe(row.get("parent_chain", ""))
        if not canonical or not parent_chain:
            continue
        entry = ParentEntry(
            term=canonical,
            parent_chain=parent_chain,
            count_channel=norm_key(row.get("count_channel") or default_count_channel),
            confidence=confidence_from_row(row),
            source=f"{source_from_row(row, path)}:legacy_parent",
            notes=notes_from_row(row),
        )
        add_parent_entry(entries, entry)
    return entries


def load_attribute_entries(
    path: Path,
    *,
    entries: dict[str, LexicalEntry] | None = None,
) -> dict[str, LexicalEntry]:
    entries = entries if entries is not None else {}
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
            confidence=confidence_from_row(row),
            source=source_from_row(row, path),
            notes=notes_from_row(row),
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
                confidence=confidence_from_row(row),
                source=source_from_row(row, path),
                notes=notes_from_row(row),
            )
            add_entry(entries, entry)
    return entries


def load_stage9_canonical_lexicon(
    *,
    object_path: Path = DEFAULT_OBJECT_CANONICAL_LEXICON,
    object_synonym_expansion_path: Path = DEFAULT_OBJECT_SYNONYM_EXPANSION_LEXICON,
    object_synonym_auto_frozen_path: Path = DEFAULT_OBJECT_SYNONYM_AUTO_FROZEN_LEXICON,
    action_path: Path = DEFAULT_ACTION_CANONICAL_LEXICON,
    action_synonym_expansion_path: Path = DEFAULT_ACTION_SYNONYM_EXPANSION_LEXICON,
    action_synonym_auto_frozen_path: Path = DEFAULT_ACTION_SYNONYM_AUTO_FROZEN_LEXICON,
    object_parent_path: Path = DEFAULT_OBJECT_PARENT_LEXICON,
    object_parent_expansion_path: Path = DEFAULT_OBJECT_PARENT_EXPANSION_LEXICON,
    object_parent_expansion_v2_path: Path = DEFAULT_OBJECT_PARENT_EXPANSION_V2_LEXICON,
    object_parent_expansion_v3_path: Path = DEFAULT_OBJECT_PARENT_EXPANSION_V3_LEXICON,
    object_parent_auto_frozen_path: Path = DEFAULT_OBJECT_PARENT_AUTO_FROZEN_LEXICON,
    action_parent_path: Path = DEFAULT_ACTION_PARENT_LEXICON,
    action_parent_expansion_path: Path = DEFAULT_ACTION_PARENT_EXPANSION_LEXICON,
    action_parent_expansion_v2_path: Path = DEFAULT_ACTION_PARENT_EXPANSION_V2_LEXICON,
    action_parent_auto_frozen_path: Path = DEFAULT_ACTION_PARENT_AUTO_FROZEN_LEXICON,
    object_mwe_path: Path = DEFAULT_OBJECT_MWE_CANONICAL_LEXICON,
    attribute_path: Path = DEFAULT_ATTRIBUTE_CANONICAL_LEXICON,
    attribute_auto_frozen_path: Path = DEFAULT_ATTRIBUTE_AUTO_FROZEN_LEXICON,
    attribute_synonym_path: Path = DEFAULT_ATTRIBUTE_SYNONYM_LEXICON,
    attribute_synonym_auto_frozen_path: Path = DEFAULT_ATTRIBUTE_SYNONYM_AUTO_FROZEN_LEXICON,
    relation_path: Path = DEFAULT_RELATION_CANONICAL_LEXICON,
    preposition_mwe_path: Path = DEFAULT_PREPOSITION_MWE_LEXICON,
) -> Stage9CanonicalLexicon:
    object_synonyms = load_synonym_entries(object_path, default_count_channel="entity")
    if not object_synonyms:
        load_legacy_seed_synonyms(
            LEGACY_OBJECT_CANONICAL_LEXICON,
            default_count_channel="entity",
            entries=object_synonyms,
        )
    load_synonym_entries(object_synonym_expansion_path, default_count_channel="entity", entries=object_synonyms)
    load_synonym_entries(object_synonym_auto_frozen_path, default_count_channel="entity", entries=object_synonyms)
    load_synonym_entries(object_mwe_path, default_count_channel="entity", entries=object_synonyms)

    action_synonyms = load_synonym_entries(action_path, default_count_channel="action")
    if not action_synonyms:
        load_legacy_seed_synonyms(
            LEGACY_ACTION_CANONICAL_LEXICON,
            default_count_channel="action",
            entries=action_synonyms,
        )
    load_synonym_entries(action_synonym_expansion_path, default_count_channel="action", entries=action_synonyms)
    load_synonym_entries(action_synonym_auto_frozen_path, default_count_channel="action", entries=action_synonyms)

    object_parents = load_parent_entries(object_parent_path, default_count_channel="entity")
    load_parent_entries(object_parent_expansion_path, default_count_channel="entity", entries=object_parents)
    load_parent_entries(object_parent_expansion_v2_path, default_count_channel="entity", entries=object_parents)
    load_parent_entries(object_parent_expansion_v3_path, default_count_channel="entity", entries=object_parents)
    load_parent_entries(object_parent_auto_frozen_path, default_count_channel="entity", entries=object_parents)
    if not object_parents:
        load_legacy_seed_parents(
            LEGACY_OBJECT_CANONICAL_LEXICON,
            default_count_channel="entity",
            entries=object_parents,
        )

    action_parents = load_parent_entries(action_parent_path, default_count_channel="action")
    load_parent_entries(action_parent_expansion_path, default_count_channel="action", entries=action_parents)
    load_parent_entries(action_parent_expansion_v2_path, default_count_channel="action", entries=action_parents)
    load_parent_entries(action_parent_auto_frozen_path, default_count_channel="action", entries=action_parents)
    if not action_parents:
        load_legacy_seed_parents(
            LEGACY_ACTION_CANONICAL_LEXICON,
            default_count_channel="action",
            entries=action_parents,
        )

    attributes = load_attribute_entries(attribute_path)
    load_attribute_entries(attribute_auto_frozen_path, entries=attributes)

    attribute_synonyms = load_synonym_entries(attribute_synonym_path, default_count_channel="attribute")
    load_synonym_entries(
        attribute_synonym_auto_frozen_path,
        default_count_channel="attribute",
        entries=attribute_synonyms,
    )

    return Stage9CanonicalLexicon(
        object_synonyms=object_synonyms,
        object_parents=object_parents,
        action_synonyms=action_synonyms,
        action_parents=action_parents,
        attribute_synonyms=attribute_synonyms,
        attributes=attributes,
        relations=load_relation_entries(relation_path, preposition_mwe_path),
    )


def lookup_entry(entries: dict[str, LexicalEntry], *values: object) -> LexicalEntry | None:
    for value in values:
        for key in lookup_keys(value):
            entry = entries.get(key)
            if entry is not None:
                return entry
    return None


def lookup_canonical_entry(
    entries: dict[str, CanonicalEntry],
    *values: object,
) -> CanonicalEntry | None:
    for value in values:
        for key in lookup_keys(value):
            entry = entries.get(key)
            if entry is not None:
                return entry
    return None


def lookup_parent_entry(entries: dict[str, ParentEntry], *values: object) -> ParentEntry | None:
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


def lexical_metadata(
    *,
    canonical_source: str,
    canonical_confidence: str,
    parent_source: str,
    parent_confidence: str,
) -> dict[str, str]:
    legacy_source = canonical_source
    legacy_confidence = canonical_confidence
    if canonical_source in {"raw_lemma", "raw_action"} and parent_source:
        legacy_source = parent_source
        legacy_confidence = parent_confidence
    return {
        "source": legacy_source,
        "confidence": legacy_confidence,
        "canonical_source": canonical_source,
        "canonical_confidence": canonical_confidence,
        "parent_source": parent_source,
        "parent_confidence": parent_confidence,
    }


def canonicalize_entity(
    entity: dict[str, Any],
    lexicon: Stage9CanonicalLexicon,
) -> dict[str, Any]:
    raw_lemma = entity.get("canonical_lemma") or entity.get("text") or ""
    synonym = lookup_canonical_entry(lexicon.object_synonyms, raw_lemma, entity.get("text"))
    if synonym is not None:
        canonical = synonym.canonical
        canonical_source = synonym.source
        canonical_confidence = synonym.confidence
    else:
        canonical = slug(raw_lemma)
        canonical_source = "raw_lemma"
        canonical_confidence = "low"

    parent = lookup_parent_entry(lexicon.object_parents, entity.get("text"), canonical)
    if parent is not None:
        parent_chain = parent.parent_chain
        parent_source = parent.source
        parent_confidence = parent.confidence
    else:
        parent_chain = entity_parent_fallback(entity)
        parent_source = "semantic_type_fallback" if parent_chain else "none"
        parent_confidence = "medium" if parent_chain else "low"

    out = dict(entity)
    out["raw_canonical_lemma"] = raw_lemma
    out["canonical_lemma"] = canonical
    out["parent_chain"] = list(parent_chain)
    out["count_channel"] = "entity"
    out["count_keys"] = count_keys("entity", canonical, parent_chain)
    out["lexical_canonicalization"] = lexical_metadata(
        canonical_source=canonical_source,
        canonical_confidence=canonical_confidence,
        parent_source=parent_source,
        parent_confidence=parent_confidence,
    )
    return out


def canonicalize_action(
    canonical_action: object,
    lexicon: Stage9CanonicalLexicon,
) -> dict[str, Any]:
    synonym = lookup_canonical_entry(lexicon.action_synonyms, canonical_action)
    if synonym is not None:
        canonical = synonym.canonical
        canonical_source = synonym.source
        canonical_confidence = synonym.confidence
    else:
        canonical = slug(canonical_action)
        canonical_source = "raw_action"
        canonical_confidence = "low"

    parent = lookup_parent_entry(lexicon.action_parents, canonical)
    if parent is not None:
        parent_chain = parent.parent_chain
        parent_source = parent.source
        parent_confidence = parent.confidence
    else:
        parent_chain = ("visual_action",) if canonical else ()
        parent_source = "visual_action_fallback" if canonical else "none"
        parent_confidence = "low"

    return {
        "canonical": canonical,
        "parent_chain": list(parent_chain),
        "count_channel": "action",
        "count_keys": count_keys("action", canonical, parent_chain),
        "source": canonical_source,
        "confidence": canonical_confidence,
        "parent_source": parent_source,
        "parent_confidence": parent_confidence,
        "lexical_canonicalization": lexical_metadata(
            canonical_source=canonical_source,
            canonical_confidence=canonical_confidence,
            parent_source=parent_source,
            parent_confidence=parent_confidence,
        ),
    }


def canonicalize_attribute(
    mention: dict[str, Any],
    lexicon: Stage9CanonicalLexicon,
) -> dict[str, Any]:
    entry = lookup_entry(lexicon.attributes, mention.get("lemma"), mention.get("text"))
    synonym = lookup_canonical_entry(
        lexicon.attribute_synonyms,
        mention.get("lemma"),
        mention.get("text"),
        entry.canonical if entry is not None else "",
    )
    if entry is not None:
        parent_chain = entry.parent_chain
        count_channel = entry.count_channel
        parent_source = entry.source
        parent_confidence = entry.confidence
        if synonym is not None:
            canonical = synonym.canonical
            canonical_source = synonym.source
            canonical_confidence = synonym.confidence
        else:
            canonical = entry.canonical
            canonical_source = entry.source
            canonical_confidence = entry.confidence
    elif synonym is not None:
        canonical = synonym.canonical
        parent_chain = (norm_key(synonym.count_channel) or "attribute", "visual_attribute")
        count_channel = norm_key(synonym.count_channel) or "attribute"
        canonical_source = synonym.source
        canonical_confidence = synonym.confidence
        parent_source = "attribute_synonym_role_fallback"
        parent_confidence = synonym.confidence
    else:
        role = norm_key(mention.get("role"))
        canonical = slug(mention.get("lemma") or mention.get("text"))
        parent_chain = tuple(dict.fromkeys([role, "visual_attribute"] if role else ["visual_attribute"]))
        count_channel = role or "attribute"
        canonical_source = "raw_attribute_role"
        canonical_confidence = norm_key(mention.get("confidence") or "low")
        parent_source = canonical_source
        parent_confidence = canonical_confidence
    metadata = lexical_metadata(
        canonical_source=canonical_source,
        canonical_confidence=canonical_confidence,
        parent_source=parent_source,
        parent_confidence=parent_confidence,
    )
    return {
        "canonical": canonical,
        "parent_chain": list(parent_chain),
        "count_channel": count_channel,
        "count_keys": count_keys("attribute", canonical, parent_chain),
        "source": metadata["source"],
        "confidence": metadata["confidence"],
        "lexical_canonicalization": metadata,
    }


def canonicalize_quantity(mention: dict[str, Any]) -> dict[str, Any]:
    role = norm_key(mention.get("role")) or "quantity"
    canonical = slug(mention.get("lemma") or mention.get("text"))
    parent_chain = tuple(dict.fromkeys([role, "quantity"]))
    source = "raw_quantity_role"
    confidence = norm_key(mention.get("confidence") or "medium")
    return {
        "canonical": canonical,
        "parent_chain": list(parent_chain),
        "count_channel": role,
        "count_keys": count_keys("quantity", canonical, parent_chain),
        "source": source,
        "confidence": confidence,
        "lexical_canonicalization": lexical_metadata(
            canonical_source=source,
            canonical_confidence=confidence,
            parent_source=source,
            parent_confidence=confidence,
        ),
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
        "lexical_canonicalization": lexical_metadata(
            canonical_source=source,
            canonical_confidence=confidence,
            parent_source=source,
            parent_confidence=confidence,
        ),
    }


def entity_display(entity_id: object, entities_by_id: dict[str, dict[str, Any]]) -> str:
    entity = entities_by_id.get(str(entity_id))
    if not entity:
        return ""
    return str(entity.get("canonical_lemma") or "")


def make_fact_count_key(parts: list[object]) -> str:
    return ":".join(slug(part) for part in parts if slug(part))
