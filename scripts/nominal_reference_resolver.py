from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

import spacy

from hyphen_span_retokenizer import ensure_hyphen_span_merger
from object_mwe_retokenizer import DEFAULT_OBJECT_MWE_LEXICON, ensure_object_mwe_merger
from quantity_lexicon import quantity_role
from quote_retokenizer import ensure_raw_quote_merger
from reference_lexicon import is_reference_word, reference_class


OBJECT_PRONOUN_LEMMAS = {"he", "her", "him", "it", "she", "that", "they", "them", "these", "this", "those", "who"}
EXACT_ONE_SURFACES = {"1", "one"}
EXACT_ZERO_SURFACES = {"0", "zero"}


@dataclass(frozen=True)
class ObjectCandidate:
    candidate_id: str
    candidate_type: str
    text: str
    lemma: str
    token_i: int
    sent_i: int
    object_id: str | None
    object_role: str
    chunk_text: str
    quantity_roles: tuple[str, ...]
    quantity_texts: tuple[str, ...]
    salience: int
    agent_like: bool
    patient_like: bool
    plural_like: bool


@dataclass(frozen=True)
class ReferenceCandidate:
    text: str
    lemma: str
    ref_class: str
    token_i: int
    sent_i: int
    chunk_text: str
    modifiers: tuple[str, ...]


@dataclass(frozen=True)
class ScoredCandidate:
    candidate: ObjectCandidate
    score: int
    reasons: tuple[str, ...]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                records.append(json.loads(line))
    return records


def sent_index_by_token(doc) -> dict[int, int]:
    mapping: dict[int, int] = {}
    for sent_i, sent in enumerate(doc.sents):
        for token in sent:
            mapping[token.i] = sent_i
    if not mapping:
        for token in doc:
            mapping[token.i] = 0
    return mapping


def token_chunk(doc, token_i: int):
    for chunk in doc.noun_chunks:
        if chunk.start <= token_i < chunk.end:
            return chunk
    return None


def quantity_by_object_id(record: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    mentions = {mention["mention_id"]: mention for mention in record.get("concept_mentions", [])}
    quantities: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for edge in record.get("edges", []):
        if edge.get("edge_type") != "has_quantity":
            continue
        source = edge.get("source")
        target = edge.get("target")
        if isinstance(source, str) and isinstance(target, str) and target in mentions:
            quantities[source].append(mentions[target])
    return quantities


def salience_by_object_id(record: dict[str, Any]) -> dict[str, int]:
    salience: dict[str, int] = defaultdict(int)
    for edge in record.get("edges", []):
        edge_type = edge.get("edge_type")
        source = edge.get("source")
        target = edge.get("target")
        if edge_type == "agent" and isinstance(target, str):
            salience[target] += 18
        elif edge_type == "patient" and isinstance(target, str):
            salience[target] += 8
        elif edge_type == "relation":
            if isinstance(source, str):
                salience[source] += 6
            if isinstance(target, str):
                salience[target] += 3
    return salience


def discourse_roles_by_object_id(record: dict[str, Any]) -> dict[str, Counter[str]]:
    roles: dict[str, Counter[str]] = defaultdict(Counter)
    for edge in record.get("edges", []):
        edge_type = edge.get("edge_type")
        source = edge.get("source")
        target = edge.get("target")
        if edge_type == "agent" and isinstance(target, str):
            roles[target]["agent"] += 1
        elif edge_type == "patient" and isinstance(target, str):
            roles[target]["patient"] += 1
        elif edge_type == "relation":
            if isinstance(source, str):
                roles[source]["relation_source"] += 1
            if isinstance(target, str):
                roles[target]["relation_target"] += 1
    return roles


def object_candidates(record: dict[str, Any], doc, sent_by_token: dict[int, int]) -> list[ObjectCandidate]:
    quantities = quantity_by_object_id(record)
    salience = salience_by_object_id(record)
    discourse_roles = discourse_roles_by_object_id(record)
    candidates: list[ObjectCandidate] = []
    seen: set[tuple[str, int]] = set()
    for mention in record.get("concept_mentions", []):
        if mention.get("concept_type") != "object":
            continue
        lemma = str(mention.get("lemma") or "").lower()
        if lemma in OBJECT_PRONOUN_LEMMAS or is_reference_word(lemma):
            continue
        token_i = mention.get("source_token_i")
        if not isinstance(token_i, int) or token_i < 0 or token_i >= len(doc):
            continue
        token = doc[token_i]
        if reference_class(token) is not None or quantity_role(token) is not None:
            continue
        quantity_mentions = quantities.get(str(mention.get("mention_id")), [])
        quantity_roles = tuple(str(item.get("role") or "") for item in quantity_mentions)
        quantity_texts = tuple(str(item.get("text") or "") for item in quantity_mentions)
        role_counts = discourse_roles.get(str(mention.get("mention_id")), Counter())
        chunk = token_chunk(doc, token_i)
        chunk_text = chunk.text if chunk is not None else token.text
        candidate = ObjectCandidate(
            candidate_id=f"object:{mention.get('mention_id')}",
            candidate_type="object",
            text=str(mention.get("text") or token.text),
            lemma=lemma,
            token_i=token_i,
            sent_i=sent_by_token.get(token_i, 0),
            object_id=str(mention.get("mention_id")),
            object_role=str(mention.get("role") or ""),
            chunk_text=chunk_text,
            quantity_roles=quantity_roles,
            quantity_texts=quantity_texts,
            salience=salience.get(str(mention.get("mention_id")), 0),
            agent_like=role_counts["agent"] > 0,
            patient_like=role_counts["patient"] > 0,
            plural_like=is_plural_like(token, quantity_roles, quantity_texts, candidate_type="object"),
        )
        key = (candidate.candidate_id, candidate.token_i)
        if key not in seen:
            seen.add(key)
            candidates.append(candidate)
    candidates.extend(coordination_group_candidates(doc, candidates, sent_by_token))
    return sorted(candidates, key=lambda item: item.token_i)


def coordination_group_candidates(doc, candidates: list[ObjectCandidate], sent_by_token: dict[int, int]) -> list[ObjectCandidate]:
    object_by_token = {candidate.token_i: candidate for candidate in candidates if candidate.candidate_type == "object"}
    groups: list[ObjectCandidate] = []
    seen_spans: set[tuple[int, int]] = set()
    for candidate in candidates:
        if candidate.token_i not in object_by_token:
            continue
        token = doc[candidate.token_i]
        conjuncts = [token]
        conjuncts.extend(child for child in token.children if child.dep_ == "conj" and child.i in object_by_token)
        if len(conjuncts) < 2:
            continue
        chunks = [token_chunk(doc, item.i) for item in conjuncts]
        chunks = [chunk for chunk in chunks if chunk is not None]
        if len(chunks) < 2:
            continue
        start = min(chunk.start for chunk in chunks)
        end = max(chunk.end for chunk in chunks)
        span = (start, end)
        if span in seen_spans:
            continue
        seen_spans.add(span)
        members = [object_by_token[item.i] for item in conjuncts]
        groups.append(
            ObjectCandidate(
                candidate_id="group:" + ",".join(member.object_id or str(member.token_i) for member in members),
                candidate_type="coordination_group",
                text=doc[start:end].text,
                lemma="_and_".join(member.lemma for member in members),
                token_i=start,
                sent_i=sent_by_token.get(start, 0),
                object_id=None,
                object_role="coordination_group",
                chunk_text=doc[start:end].text,
                quantity_roles=(),
                quantity_texts=(),
                salience=max(member.salience for member in members) + 12,
                agent_like=any(member.agent_like for member in members),
                patient_like=any(member.patient_like for member in members),
                plural_like=True,
            )
        )
    return groups


def is_plural_like(token, quantity_roles: tuple[str, ...], quantity_texts: tuple[str, ...], candidate_type: str) -> bool:
    if candidate_type == "coordination_group":
        return True
    if any(role in {"approximate_quantity", "group_quantity", "distributive_quantity", "partitive_quantity"} for role in quantity_roles):
        return True
    for role, text in zip(quantity_roles, quantity_texts, strict=False):
        lower = text.lower()
        if role == "exact_quantity" and lower not in EXACT_ONE_SURFACES and lower not in EXACT_ZERO_SURFACES:
            return True
    if "Plur" in token.morph.get("Number"):
        return True
    if token.tag_ in {"NNS", "NNPS"}:
        return True
    return False


def reference_candidates(doc, sent_by_token: dict[int, int]) -> list[ReferenceCandidate]:
    refs: list[ReferenceCandidate] = []
    for token in doc:
        ref_class = reference_class(token)
        if ref_class is None:
            continue
        chunk = token_chunk(doc, token.i)
        chunk_text = chunk.text if chunk is not None else token.text
        modifiers = reference_modifiers(token, chunk)
        refs.append(
            ReferenceCandidate(
                text=token.text,
                lemma=(token.lemma_ or token.text).lower(),
                ref_class=ref_class,
                token_i=token.i,
                sent_i=sent_by_token.get(token.i, 0),
                chunk_text=chunk_text,
                modifiers=tuple(modifiers),
            )
        )
    return refs


def reference_modifiers(token, chunk) -> list[str]:
    modifiers: list[str] = []
    if chunk is not None:
        for item in chunk:
            if item.i == token.i or item.dep_ in {"case", "cc", "det", "mark", "punct"}:
                continue
            if item.pos_ in {"ADJ", "ADV", "NUM"} or item.dep_ in {"amod", "compound", "nummod"}:
                modifiers.append(item.text)
    for child in token.children:
        if child.dep_ in {"amod", "compound", "nummod"} and child.text not in modifiers:
            modifiers.append(child.text)
    return modifiers


def score_candidates(
    ref: ReferenceCandidate,
    candidates: list[ObjectCandidate],
    max_antecedent_tokens: int,
) -> list[ScoredCandidate]:
    scored: list[ScoredCandidate] = []
    for candidate in candidates:
        if candidate.token_i >= ref.token_i:
            continue
        distance = ref.token_i - candidate.token_i
        if distance > max_antecedent_tokens:
            continue
        score, reasons = score_candidate(ref, candidate, distance)
        scored.append(ScoredCandidate(candidate=candidate, score=score, reasons=tuple(reasons)))
    return sorted(scored, key=lambda item: (-item.score, item.candidate.token_i))


def score_candidate(ref: ReferenceCandidate, candidate: ObjectCandidate, distance: int) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []

    if distance <= 8:
        score += 35
        reasons.append("very_recent")
    elif distance <= 16:
        score += 28
        reasons.append("recent")
    elif distance <= 32:
        score += 20
        reasons.append("nearby")
    elif distance <= 64:
        score += 10
        reasons.append("reachable")
    else:
        score += 4
        reasons.append("far")

    sent_gap = ref.sent_i - candidate.sent_i
    if sent_gap == 0:
        score += 12
        reasons.append("same_sentence")
    elif sent_gap == 1:
        score += 18
        reasons.append("previous_sentence")
    elif sent_gap == 2:
        score += 8
        reasons.append("two_sentences_back")

    if candidate.plural_like:
        if ref.ref_class in {"contrastive_reference", "distributive_reference", "group_reference"}:
            score += 34
            reasons.append("plural_group_match")
        elif ref.ref_class == "singular_substitute":
            score += 28
            reasons.append("plural_source_for_substitute")
    else:
        if ref.ref_class in {"contrastive_reference", "distributive_reference", "group_reference"}:
            score -= 24
            reasons.append("not_plural_group")
        elif ref.ref_class == "singular_substitute":
            score -= 8
            reasons.append("singular_source_for_substitute")

    if candidate.candidate_type == "coordination_group":
        if ref.ref_class in {"group_reference", "distributive_reference"}:
            score += 28
            reasons.append("coordination_group_match")

    if candidate.quantity_roles:
        score += 10
        reasons.append("has_quantity_signal")

    if candidate.agent_like:
        if ref.ref_class in {"contrastive_reference", "distributive_reference", "group_reference"}:
            score += 22
            reasons.append("agent_like_antecedent")
        elif ref.ref_class == "singular_substitute":
            score += 10
            reasons.append("agent_like_antecedent")

    if candidate.patient_like and not candidate.agent_like and ref.ref_class in {
        "contrastive_reference",
        "distributive_reference",
        "group_reference",
    }:
        score -= 18
        reasons.append("patient_like_penalty")

    if any(role == "exact_quantity" and text.lower() in EXACT_ONE_SURFACES for role, text in zip(candidate.quantity_roles, candidate.quantity_texts, strict=False)):
        if ref.ref_class in {"contrastive_reference", "distributive_reference", "group_reference"}:
            score -= 18
            reasons.append("exact_one_not_group")

    if ref.modifiers and ref.ref_class == "singular_substitute" and candidate.plural_like:
        score += 8
        reasons.append("substitute_has_modifier")

    if candidate.salience:
        boost = min(candidate.salience, 24)
        score += boost
        reasons.append(f"syntactic_salience_{boost}")

    return score, reasons


def confidence_for(score: int, margin: int | None, min_score: int, ambiguous_margin: int) -> tuple[str, str]:
    if score < min_score:
        return "unresolved", "none"
    if margin is not None and margin < ambiguous_margin:
        return "ambiguous", "low"
    if score >= 85:
        return "resolved", "high"
    if score >= 65:
        return "resolved", "medium"
    return "resolved", "low"


def recommendation_for(ref: ReferenceCandidate, status: str) -> str:
    if status == "unresolved":
        return "exclude_reference_unresolved"
    if status == "ambiguous":
        return "manual_review_ambiguous_reference"
    if ref.ref_class == "singular_substitute":
        if ref.modifiers:
            return "copy_antecedent_type_apply_modifiers"
        return "link_singular_reference"
    if ref.ref_class == "contrastive_reference":
        return "link_contrastive_reference"
    if ref.ref_class == "group_reference":
        return "link_group_reference"
    if ref.ref_class == "distributive_reference":
        return "link_distributive_reference"
    return "link_reference"


def resolve_record(
    record: dict[str, Any],
    doc,
    max_antecedent_tokens: int,
    min_score: int,
    ambiguous_margin: int,
) -> list[dict[str, Any]]:
    sent_by_token = sent_index_by_token(doc)
    objects = object_candidates(record, doc, sent_by_token)
    refs = reference_candidates(doc, sent_by_token)
    rows: list[dict[str, Any]] = []
    for ref in refs:
        scored = score_candidates(ref, objects, max_antecedent_tokens)
        top = scored[0] if scored else None
        runner_up = scored[1] if len(scored) > 1 else None
        margin = None if top is None or runner_up is None else top.score - runner_up.score
        status, confidence = confidence_for(top.score if top else 0, margin, min_score, ambiguous_margin)
        antecedent = top.candidate if top and status != "unresolved" else None
        rows.append(
            {
                "row_index": record.get("row_index"),
                "caption_id": record.get("caption_id"),
                "caption": record.get("caption"),
                "reference_text": ref.text,
                "reference_lemma": ref.lemma,
                "reference_class": ref.ref_class,
                "reference_token_i": ref.token_i,
                "reference_chunk": ref.chunk_text,
                "reference_modifiers": list(ref.modifiers),
                "antecedent_text": antecedent.text if antecedent else None,
                "antecedent_chunk": antecedent.chunk_text if antecedent else None,
                "antecedent_object_id": antecedent.object_id if antecedent else None,
                "antecedent_type": antecedent.candidate_type if antecedent else None,
                "antecedent_plural_like": antecedent.plural_like if antecedent else None,
                "antecedent_quantity_roles": list(antecedent.quantity_roles) if antecedent else [],
                "score": top.score if top else 0,
                "margin": margin,
                "status": status,
                "confidence": confidence,
                "recommendation": recommendation_for(ref, status),
                "reasons": list(top.reasons) if top else [],
                "alternatives": [
                    {
                        "text": item.candidate.text,
                        "candidate_type": item.candidate.candidate_type,
                        "score": item.score,
                        "reasons": list(item.reasons),
                    }
                    for item in scored[:3]
                ],
            }
        )
    return rows


def markdown_count_table(counter: Counter[str]) -> str:
    if not counter:
        return "_none_"
    lines = ["| item | count |", "| --- | ---: |"]
    for key, value in counter.most_common():
        lines.append(f"| `{key}` | {value} |")
    return "\n".join(lines)


def markdown_escape(text: object, max_len: int = 100) -> str:
    value = "" if text is None else str(text)
    value = value.replace("\n", " ").strip()
    if len(value) > max_len:
        value = value[: max_len - 3] + "..."
    return value.replace("|", "\\|")


def write_summary(path: Path, args: argparse.Namespace, rows: list[dict[str, Any]], counters: dict[str, Counter[str]]) -> None:
    lines = [
        "# Nominal Reference Resolver Audit",
        "",
        "이 리포트는 단어별 땜빵이 아니라 reference cue class와 antecedent scoring으로 `one/other/both/each`류 후보를 처리한 결과입니다.",
        "",
        "## Settings",
        f"- raw_concepts: `{args.raw_concepts}`",
        f"- output_jsonl: `{args.output}`",
        f"- spacy_model: `{args.spacy_model}`",
        f"- max_antecedent_tokens: `{args.max_antecedent_tokens}`",
        f"- min_score: `{args.min_score}`",
        f"- ambiguous_margin: `{args.ambiguous_margin}`",
        f"- references_seen: `{len(rows)}`",
        "",
        "## Reference Classes",
        markdown_count_table(counters["reference_class"]),
        "",
        "## Status",
        markdown_count_table(counters["status"]),
        "",
        "## Confidence",
        markdown_count_table(counters["confidence"]),
        "",
        "## Recommendations",
        markdown_count_table(counters["recommendation"]),
        "",
        "## Audit Rows",
        "| case | reference | class | modifiers | antecedent | score | margin | status | confidence | recommendation | reasons |",
        "| ---: | --- | --- | --- | --- | ---: | ---: | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["row_index"]),
                    f"`{markdown_escape(row['reference_text'], 30)}`",
                    f"`{row['reference_class']}`",
                    markdown_escape(", ".join(row.get("reference_modifiers") or []), 35),
                    markdown_escape(row.get("antecedent_chunk") or row.get("antecedent_text") or "", 45),
                    str(row["score"]),
                    "" if row["margin"] is None else str(row["margin"]),
                    f"`{row['status']}`",
                    f"`{row['confidence']}`",
                    f"`{row['recommendation']}`",
                    markdown_escape(", ".join(row.get("reasons") or []), 70),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Policy",
            "- `resolved`: Stage 9에서 reference edge 후보로 사용할 수 있습니다.",
            "- `ambiguous`: 후보는 찾았지만 margin이 낮으므로 자동 적용하지 않습니다.",
            "- `unresolved`: object count에서 surface reference를 제외하고, 별도 unresolved로 남깁니다.",
            "- `singular_substitute` with modifiers: `a red one`처럼 antecedent type을 복사하고 reference modifier를 attribute 후보로 붙입니다.",
            "- bare `singular_substitute`: `One wears...`처럼 새 object를 만들지 않고 antecedent/member reference link로만 남깁니다.",
            "- `group_reference` / `distributive_reference`: 단일 object로 collapse하지 않고 group/distribution link로 남깁니다.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Resolve nominal references with cue classes and antecedent scoring.")
    parser.add_argument("--raw-concepts", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--summary-output", required=True, type=Path)
    parser.add_argument("--spacy-model", default="en_core_web_trf")
    parser.add_argument("--mask-quotes", action="store_true")
    parser.add_argument("--merge-object-mwes", action="store_true")
    parser.add_argument("--merge-hyphen-spans", action="store_true")
    parser.add_argument("--object-mwe-lexicon", type=Path, default=DEFAULT_OBJECT_MWE_LEXICON)
    parser.add_argument("--max-antecedent-tokens", type=int, default=80)
    parser.add_argument("--min-score", type=int, default=45)
    parser.add_argument("--ambiguous-margin", type=int, default=15)
    args = parser.parse_args()

    records = read_jsonl(args.raw_concepts)
    nlp = spacy.load(args.spacy_model)
    if args.mask_quotes:
        ensure_raw_quote_merger(nlp)
    if args.merge_object_mwes:
        ensure_object_mwe_merger(nlp, args.object_mwe_lexicon)
    if args.merge_hyphen_spans:
        ensure_hyphen_span_merger(nlp)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.summary_output.parent.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, Any]] = []
    counters = {
        "reference_class": Counter(),
        "status": Counter(),
        "confidence": Counter(),
        "recommendation": Counter(),
    }
    with args.output.open("w", encoding="utf-8") as handle:
        for record in records:
            if record.get("parse_path") == "tag_list":
                continue
            doc = nlp(record.get("parse_caption") or record.get("caption") or "")
            record_rows = resolve_record(
                record,
                doc,
                max_antecedent_tokens=args.max_antecedent_tokens,
                min_score=args.min_score,
                ambiguous_margin=args.ambiguous_margin,
            )
            for row in record_rows:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
                rows.append(row)
                counters["reference_class"][row["reference_class"]] += 1
                counters["status"][row["status"]] += 1
                counters["confidence"][row["confidence"]] += 1
                counters["recommendation"][row["recommendation"]] += 1

    write_summary(args.summary_output, args, rows, counters)
    print(args.output)
    print(args.summary_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
