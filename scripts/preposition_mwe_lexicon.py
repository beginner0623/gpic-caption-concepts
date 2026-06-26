from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


DEFAULT_PREPOSITION_MWE_LEXICON = (
    Path(__file__).resolve().parents[1] / "resources" / "lexicons" / "preposition_mwe_clean_core.tsv"
)
DEFAULT_PREPOSITION_MWE_AUDIT_FLAGS = (
    Path(__file__).resolve().parents[1] / "resources" / "lexicons" / "preposition_mwe_audit_flags.tsv"
)


@dataclass(frozen=True)
class PrepositionMweEntry:
    term: str
    canonical: str
    relation_type: str
    pattern: str
    middle: str
    final_adp: str
    confidence: str
    source: str
    notes: str


def normalize_preposition_mwe(text: str) -> str:
    return " ".join(text.replace("_", " ").lower().split())


def load_preposition_mwe_lexicon(
    path: Path = DEFAULT_PREPOSITION_MWE_LEXICON,
) -> dict[str, PrepositionMweEntry]:
    entries: dict[str, PrepositionMweEntry] = {}
    if not path.exists():
        return entries
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            term = normalize_preposition_mwe(row.get("term", ""))
            canonical = row.get("canonical", "").strip() or term.replace(" ", "_")
            if not term or " " not in term:
                continue
            entries[term] = PrepositionMweEntry(
                term=term,
                canonical=canonical,
                relation_type=row.get("relation_type", "").strip(),
                pattern=row.get("pattern", "").strip(),
                middle=normalize_preposition_mwe(row.get("middle", "")),
                final_adp=normalize_preposition_mwe(row.get("final_adp", "")),
                confidence=row.get("confidence", "").strip() or "medium",
                source=row.get("source", "").strip(),
                notes=row.get("notes", "").strip(),
            )
    return entries


def load_rejected_preposition_mwe_terms(
    path: Path = DEFAULT_PREPOSITION_MWE_AUDIT_FLAGS,
) -> set[str]:
    if not path.exists():
        return set()
    terms: set[str] = set()
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            if row.get("decision", "").strip() != "reject":
                continue
            term = normalize_preposition_mwe(row.get("term", ""))
            if term:
                terms.add(term)
    return terms


PREPOSITION_MWE_ENTRIES = load_preposition_mwe_lexicon()
PREPOSITION_MWE_REJECTED_TERMS = load_rejected_preposition_mwe_terms()
PREPOSITION_MWE_MIDDLE_LEMMAS = {
    entry.middle for entry in PREPOSITION_MWE_ENTRIES.values() if entry.middle
}


def preposition_mwe_entry(term: str) -> PrepositionMweEntry | None:
    return PREPOSITION_MWE_ENTRIES.get(normalize_preposition_mwe(term))
