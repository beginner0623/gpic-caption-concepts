from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
from typing import Any

import spacy
from fastcoref import FCoref

from hyphen_span_retokenizer import ensure_hyphen_span_merger
from object_mwe_retokenizer import DEFAULT_OBJECT_MWE_LEXICON, ensure_object_mwe_merger
from quote_retokenizer import ensure_raw_quote_merger


OBJECT_PRONOUN_LEMMAS = {
    "he",
    "she",
    "they",
    "it",
    "who",
    "that",
    "both",
    "each",
    "other",
}
POSSESSIVE_LEMMAS = {"his", "her", "its", "their"}
NOMINAL_REFERENCE_LEMMAS = {"one", "other", "another", "others", "both", "each"}
RELATIVE_LEMMAS = {"that", "who", "which", "whose", "where"}
REFERENCE_LEMMAS = OBJECT_PRONOUN_LEMMAS | POSSESSIVE_LEMMAS | NOMINAL_REFERENCE_LEMMAS | RELATIVE_LEMMAS
NON_REFERENTIAL_DEPS = {"det", "case", "mark", "punct", "cc"}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                records.append(json.loads(line))
    return records


def cluster_char_spans(result) -> list[list[dict[str, Any]]]:
    clusters: list[list[dict[str, Any]]] = []
    for cluster_i, cluster in enumerate(result.clusters):
        mentions: list[dict[str, Any]] = []
        for span_key in cluster:
            if span_key not in result.char_map:
                continue
            _, (start, end) = result.char_map[span_key]
            start_i = int(start)
            end_i = int(end)
            mentions.append(
                {
                    "cluster_i": cluster_i,
                    "start": start_i,
                    "end": end_i,
                    "text": result.text[start_i:end_i],
                }
            )
        clusters.append(sorted(mentions, key=lambda item: (item["start"], item["end"])))
    return clusters


def span_contains(outer: dict[str, Any], start: int, end: int) -> bool:
    return int(outer["start"]) <= start and end <= int(outer["end"])


def span_overlaps(a_start: int, a_end: int, b_start: int, b_end: int) -> bool:
    return a_start < b_end and b_start < a_end


def normalize_ref_text(text: str) -> str:
    return text.strip().lower()


def is_reference_text(text: str) -> bool:
    norm = normalize_ref_text(text)
    return norm in REFERENCE_LEMMAS or norm in {"him", "them", "hers", "theirs"}


def choose_antecedent(cluster: list[dict[str, Any]], mention_start: int, mention_end: int) -> dict[str, Any] | None:
    previous = [
        item
        for item in cluster
        if int(item["end"]) <= mention_start and not is_reference_text(str(item["text"]))
    ]
    if previous:
        return previous[-1]
    non_reference = [item for item in cluster if not is_reference_text(str(item["text"]))]
    return non_reference[0] if non_reference else None


def token_span(doc, token_i: int | None) -> tuple[int, int, str] | None:
    if token_i is None or token_i < 0 or token_i >= len(doc):
        return None
    token = doc[token_i]
    return token.idx, token.idx + len(token.text), token.text


def object_candidates_for_antecedent(
    concept_mentions: list[dict[str, Any]],
    doc,
    antecedent: dict[str, Any] | None,
) -> list[dict[str, Any]]:
    if antecedent is None:
        return []
    start = int(antecedent["start"])
    end = int(antecedent["end"])
    candidates: list[dict[str, Any]] = []
    for mention in concept_mentions:
        if mention.get("concept_type") != "object":
            continue
        span = token_span(doc, mention.get("source_token_i"))
        if span is None:
            continue
        token_start, token_end, _ = span
        if span_overlaps(token_start, token_end, start, end):
            candidates.append(mention)
    head_i = antecedent_head_token_i(doc, start, end)
    if head_i is not None:
        head_candidates = [mention for mention in candidates if mention.get("source_token_i") == head_i]
        if head_candidates:
            return head_candidates
    return candidates


def antecedent_head_token_i(doc, start: int, end: int) -> int | None:
    overlapping_chunks = [
        chunk
        for chunk in doc.noun_chunks
        if span_overlaps(chunk.start_char, chunk.end_char, start, end)
    ]
    if overlapping_chunks:
        first_chunk = sorted(
            overlapping_chunks,
            key=lambda chunk: (
                0 if chunk.start_char <= start < chunk.end_char else 1,
                abs(chunk.start_char - start),
                chunk.start,
            ),
        )[0]
        return first_chunk.root.i
    for token in doc:
        token_start = token.idx
        token_end = token.idx + len(token.text)
        if not span_overlaps(token_start, token_end, start, end):
            continue
        if token.pos_ in {"NOUN", "PROPN"} and not is_reference_text(token.text):
            return token.i
    return None


def is_reference_concept(mention: dict[str, Any], doc) -> bool:
    lemma = str(mention.get("lemma") or "").lower()
    text = str(mention.get("text") or "").lower()
    if lemma not in REFERENCE_LEMMAS and text not in REFERENCE_LEMMAS:
        return False
    span = token_span(doc, mention.get("source_token_i"))
    if span is None:
        return False
    token = doc[mention["source_token_i"]]
    if token.dep_ in NON_REFERENTIAL_DEPS:
        return False
    return True


def classify_reference(mention: dict[str, Any], doc) -> str:
    token_i = mention.get("source_token_i")
    token = doc[token_i] if isinstance(token_i, int) and 0 <= token_i < len(doc) else None
    lemma = str(mention.get("lemma") or "").lower()
    text = str(mention.get("text") or "").lower()
    if token is not None and token.tag_ == "PRP$":
        return "possessive_reference"
    if lemma in RELATIVE_LEMMAS or text in RELATIVE_LEMMAS:
        return "relative_reference"
    if lemma in NOMINAL_REFERENCE_LEMMAS or text in NOMINAL_REFERENCE_LEMMAS:
        return "nominal_reference"
    return "pronoun_reference"


def relation_recommendation(ref_type: str, antecedent_object: dict[str, Any] | None) -> str:
    if ref_type == "relative_reference":
        return "prefer_dependency_rule"
    if ref_type == "nominal_reference":
        return "manual_nominal_resolution" if antecedent_object is not None else "exclude_from_object_count_unresolved"
    if ref_type == "possessive_reference":
        return "attach_possessor_metadata" if antecedent_object is not None else "drop_from_attribute_count_keep_reference"
    if antecedent_object is not None:
        return "redirect_edges_to_antecedent"
    return "exclude_from_object_count_unresolved"


def markdown_count_table(counter: Counter[str]) -> str:
    if not counter:
        return "_none_"
    lines = ["| item | count |", "| --- | ---: |"]
    for key, value in counter.most_common():
        lines.append(f"| `{key}` | {value} |")
    return "\n".join(lines)


def markdown_escape(text: object, max_len: int = 120) -> str:
    value = str(text).replace("\n", " ").strip()
    if len(value) > max_len:
        value = value[: max_len - 3] + "..."
    return value.replace("|", "\\|")


def write_markdown_report(
    path: Path,
    args: argparse.Namespace,
    records_written: int,
    audit_rows: list[dict[str, Any]],
    counters: dict[str, Counter[str]],
) -> None:
    lines = [
        "# fastcoref Pronoun Resolution Audit",
        "",
        "이 리포트는 기존 raw concept 결과를 직접 수정하지 않고, fastcoref cluster가 pronoun/anaphoric mention을 어디로 연결하는지 확인하는 sidecar audit입니다.",
        "",
        "## Settings",
        f"- raw_concepts: `{args.raw_concepts}`",
        f"- output_jsonl: `{args.output}`",
        f"- spacy_model: `{args.spacy_model}`",
        f"- fastcoref_device: `{args.device}`",
        f"- max_tokens_in_batch: `{args.max_tokens_in_batch}`",
        f"- records_processed: `{records_written}`",
        f"- reference_mentions_seen: `{len(audit_rows)}`",
        "",
        "## Reference Types",
        markdown_count_table(counters["ref_type"]),
        "",
        "## Resolution Status",
        markdown_count_table(counters["status"]),
        "",
        "## Recommendations",
        markdown_count_table(counters["recommendation"]),
        "",
        "## Lemmas",
        markdown_count_table(counters["lemma"]),
        "",
        "## Audit Rows",
        "| case | mention | type | current concept | antecedent | linked object | status | recommendation |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in audit_rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["row_index"]),
                    f"`{markdown_escape(row['mention_text'], 40)}`",
                    f"`{row['reference_type']}`",
                    f"`{row['concept_type']}:{row['role']}`",
                    markdown_escape(row.get("antecedent_text") or "", 55),
                    markdown_escape(row.get("antecedent_object_text") or "", 35),
                    f"`{row['status']}`",
                    f"`{row['recommendation']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- `resolved_to_object`: coref antecedent span 안에 기존 object mention이 있어서 edge redirect 후보로 쓸 수 있습니다.",
            "- `resolved_text_only`: antecedent text는 찾았지만 기존 object mention과 직접 겹치지 않아 보수적으로 자동 redirect하지 않는 편이 좋습니다.",
            "- `unresolved`: coref cluster가 없거나 antecedent가 없어 object/attribute count에서 제외 후보입니다.",
            "- `attach_possessor_metadata`: possessive reference는 visual attribute로 세지 말고 possessor link 후보로만 둡니다.",
            "- `manual_nominal_resolution`: `both/each/one/other`류는 group/cardinality 손실 위험이 있어 자동 redirect하지 않습니다.",
            "- `prefer_dependency_rule`: `that/who/which` relative는 coref보다 dependency 기반 antecedent 치환이 더 안전합니다.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit fastcoref resolution for raw concept pronoun mentions.")
    parser.add_argument("--raw-concepts", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--summary-output", required=True, type=Path)
    parser.add_argument("--spacy-model", default="en_core_web_trf")
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--max-tokens-in-batch", type=int, default=4096)
    parser.add_argument("--mask-quotes", action="store_true")
    parser.add_argument("--merge-object-mwes", action="store_true")
    parser.add_argument("--merge-hyphen-spans", action="store_true")
    parser.add_argument("--object-mwe-lexicon", type=Path, default=DEFAULT_OBJECT_MWE_LEXICON)
    args = parser.parse_args()

    records = read_jsonl(args.raw_concepts)
    nlp = spacy.load(args.spacy_model)
    if args.mask_quotes:
        ensure_raw_quote_merger(nlp)
    if args.merge_object_mwes:
        ensure_object_mwe_merger(nlp, args.object_mwe_lexicon)
    if args.merge_hyphen_spans:
        ensure_hyphen_span_merger(nlp)

    docs = [nlp(record.get("parse_caption") or record.get("caption") or "") for record in records]
    texts = [doc.text for doc in docs]
    coref_model = FCoref(device=args.device)
    coref_results = coref_model.predict(texts=texts, max_tokens_in_batch=args.max_tokens_in_batch)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.summary_output.parent.mkdir(parents=True, exist_ok=True)

    audit_rows: list[dict[str, Any]] = []
    counters = {
        "ref_type": Counter(),
        "status": Counter(),
        "recommendation": Counter(),
        "lemma": Counter(),
    }

    with args.output.open("w", encoding="utf-8") as handle:
        for record, doc, coref_result in zip(records, docs, coref_results, strict=True):
            clusters = cluster_char_spans(coref_result)
            for mention in record.get("concept_mentions", []):
                if not is_reference_concept(mention, doc):
                    continue
                span = token_span(doc, mention.get("source_token_i"))
                if span is None:
                    continue
                mention_start, mention_end, mention_text = span
                matched_cluster = None
                for cluster in clusters:
                    if any(span_contains(item, mention_start, mention_end) for item in cluster):
                        matched_cluster = cluster
                        break
                antecedent = choose_antecedent(matched_cluster, mention_start, mention_end) if matched_cluster else None
                object_candidates = object_candidates_for_antecedent(
                    record.get("concept_mentions", []),
                    doc,
                    antecedent,
                )
                antecedent_object = object_candidates[0] if object_candidates else None
                ref_type = classify_reference(mention, doc)
                if antecedent_object is not None:
                    status = "resolved_to_object"
                elif antecedent is not None:
                    status = "resolved_text_only"
                else:
                    status = "unresolved"
                recommendation = relation_recommendation(ref_type, antecedent_object)
                row = {
                    "row_index": record.get("row_index"),
                    "caption_id": record.get("caption_id"),
                    "caption": record.get("caption"),
                    "mention_id": mention.get("mention_id"),
                    "mention_text": mention_text,
                    "mention_lemma": mention.get("lemma"),
                    "mention_token_i": mention.get("source_token_i"),
                    "concept_type": mention.get("concept_type"),
                    "role": mention.get("role"),
                    "reference_type": ref_type,
                    "cluster": matched_cluster or [],
                    "antecedent_text": antecedent.get("text") if antecedent else None,
                    "antecedent_span": [antecedent["start"], antecedent["end"]] if antecedent else None,
                    "antecedent_object_id": antecedent_object.get("mention_id") if antecedent_object else None,
                    "antecedent_object_text": antecedent_object.get("text") if antecedent_object else None,
                    "status": status,
                    "recommendation": recommendation,
                }
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
                audit_rows.append(row)
                counters["ref_type"][ref_type] += 1
                counters["status"][status] += 1
                counters["recommendation"][recommendation] += 1
                counters["lemma"][str(mention.get("lemma") or "").lower()] += 1

    write_markdown_report(args.summary_output, args, len(records), audit_rows, counters)
    print(args.output)
    print(args.summary_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
