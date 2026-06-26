from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


DEFAULT_PHRASAL_ACTION_LEXICON = (
    Path(__file__).resolve().parent.parent
    / "resources"
    / "lexicons"
    / "phrasal_action_model_audited_core.tsv"
)


@dataclass(frozen=True)
class PhrasalActionEntry:
    term: str
    canonical: str
    verb: str
    particle_1: str
    particle_2: str
    source: str
    source_count: int
    candidate_type: str
    visual_relevance: str
    caption_plausibility: str
    collapse_policy: str
    decision: str
    confidence: str
    reason: str

    @property
    def particles(self) -> tuple[str, ...]:
        return tuple(item for item in (self.particle_1, self.particle_2) if item)


def _norm(text: str) -> str:
    return " ".join(text.strip().lower().replace("_", " ").split())


def _entry_from_row(row: dict[str, str]) -> PhrasalActionEntry:
    return PhrasalActionEntry(
        term=_norm(row.get("term", "")),
        canonical=row.get("canonical", "").strip() or _norm(row.get("term", "")).replace(" ", "_"),
        verb=_norm(row.get("verb", "")),
        particle_1=_norm(row.get("particle_1", "")),
        particle_2=_norm(row.get("particle_2", "")),
        source=row.get("source", "").strip(),
        source_count=int(row.get("source_count", "0") or 0),
        candidate_type=row.get("candidate_type", "").strip(),
        visual_relevance=row.get("visual_relevance", "").strip(),
        caption_plausibility=row.get("caption_plausibility", "").strip(),
        collapse_policy=row.get("collapse_policy", "").strip(),
        decision=row.get("decision", "").strip(),
        confidence=row.get("confidence", "").strip(),
        reason=row.get("reason", "").strip(),
    )


def load_phrasal_action_lexicon(
    path: Path = DEFAULT_PHRASAL_ACTION_LEXICON,
) -> dict[tuple[str, tuple[str, ...]], PhrasalActionEntry]:
    entries: dict[tuple[str, tuple[str, ...]], PhrasalActionEntry] = {}
    if not path.exists():
        return entries

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            entry = _entry_from_row(row)
            if entry.decision != "accept" or entry.confidence != "high":
                continue
            if entry.collapse_policy != "action_canonicalize":
                continue
            if not entry.verb or not entry.particles:
                continue
            entries[(entry.verb, entry.particles)] = entry
    return entries


def phrasal_action_entry(
    verb: str,
    particles: tuple[str, ...],
    lexicon: dict[tuple[str, tuple[str, ...]], PhrasalActionEntry],
) -> PhrasalActionEntry | None:
    verb_norm = _norm(verb)
    particle_norms = tuple(_norm(particle) for particle in particles if _norm(particle))
    for width in range(min(2, len(particle_norms)), 0, -1):
        entry = lexicon.get((verb_norm, particle_norms[:width]))
        if entry is not None:
            return entry
    return None
