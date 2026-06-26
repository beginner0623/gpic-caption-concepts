from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
from typing import Iterable

import spacy

from hyphen_span_retokenizer import ensure_hyphen_span_merger
from inspect_spacy_parse import caption_shape, iter_rows, row_caption_id
from object_mwe_retokenizer import DEFAULT_OBJECT_MWE_LEXICON, ensure_object_mwe_merger
from quote_masking import DEFAULT_PLACEHOLDER, collect_quoted_text
from quote_retokenizer import ensure_raw_quote_merger
from raw_concept_extractor import extract_raw_concepts
from tag_list_parser import is_tag_list_row, parse_tag_list_from_docs, split_tag_segments


def markdown_count_table(counter: Counter[str]) -> str:
    if not counter:
        return "_none_"
    lines = ["| item | count |", "| --- | ---: |"]
    for key, value in counter.most_common():
        lines.append(f"| `{key}` | {value} |")
    return "\n".join(lines)


def iter_indexed_rows(path: Path, max_records: int | None) -> Iterable[tuple[int, dict]]:
    for index, row in enumerate(iter_rows(path), 1):
        if max_records is not None and index > max_records:
            break
        yield index, row


def batched(items: Iterable[tuple[int, dict]], batch_size: int) -> Iterable[list[tuple[int, dict]]]:
    batch: list[tuple[int, dict]] = []
    for item in items:
        batch.append(item)
        if len(batch) >= batch_size:
            yield batch
            batch = []
    if batch:
        yield batch


def _quote_mentions(caption: str, caption_id: str, mask_quotes: bool) -> list[dict[str, object]]:
    if not mask_quotes:
        return []
    quote_result = collect_quoted_text(caption, caption_id=caption_id)
    return [mention.to_dict() for mention in quote_result.mentions]


def _base_record(
    index: int,
    row: dict,
    *,
    mask_quotes: bool,
) -> dict[str, object]:
    caption = row.get("caption", "")
    caption_id = row_caption_id(row)
    return {
        "row_index": index,
        "caption_id": caption_id,
        "caption_type": row.get("caption_type"),
        "caption_shape": caption_shape(caption),
        "caption": caption,
        "parse_caption": caption,
        "quote_mentions": _quote_mentions(caption, caption_id, mask_quotes),
    }


def process_indexed_row_batch(
    nlp,
    indexed_rows: list[tuple[int, dict]],
    *,
    mask_quotes: bool,
    parse_tag_lists: bool,
    batch_size: int,
    n_process: int,
) -> list[dict[str, object]]:
    records: list[dict[str, object] | None] = [None] * len(indexed_rows)
    sentence_items: list[tuple[int, dict[str, object], str]] = []
    tag_items: list[tuple[int, dict[str, object], list]] = []

    for offset, (index, row) in enumerate(indexed_rows):
        caption = row.get("caption", "")
        record = _base_record(index, row, mask_quotes=mask_quotes)
        if parse_tag_lists and is_tag_list_row(row, caption):
            tag_items.append((offset, record, split_tag_segments(caption)))
        else:
            sentence_items.append((offset, record, caption))

    if sentence_items:
        captions = [caption for _offset, _record, caption in sentence_items]
        docs = nlp.pipe(captions, batch_size=batch_size, n_process=n_process)
        for (offset, record, _caption), doc in zip(sentence_items, docs):
            raw_result = extract_raw_concepts(doc)
            record.update(
                {
                    "parse_path": "sentence",
                    "concept_mentions": [mention.to_dict() for mention in raw_result.concept_mentions],
                    "edges": [edge.to_dict() for edge in raw_result.edges],
                    "skipped_edges": raw_result.skipped_edges,
                }
            )
            records[offset] = record

    if tag_items:
        segment_texts: list[str] = []
        segment_counts: list[int] = []
        for _offset, _record, segments in tag_items:
            segment_counts.append(len(segments))
            segment_texts.extend(segment.raw for segment in segments)

        segment_docs = list(nlp.pipe(segment_texts, batch_size=batch_size, n_process=n_process)) if segment_texts else []
        cursor = 0
        for (offset, record, segments), count in zip(tag_items, segment_counts):
            docs = segment_docs[cursor : cursor + count]
            cursor += count
            tag_result = parse_tag_list_from_docs(segments, docs)
            record.update(
                {
                    "parse_path": "tag_list",
                    "concept_mentions": [mention.to_dict() for mention in tag_result.concept_mentions],
                    "edges": [edge.to_dict() for edge in tag_result.edges],
                    "skipped_edges": [],
                }
            )
            records[offset] = record

    return [record for record in records if record is not None]


def update_summary_counts(
    record: dict[str, object],
    *,
    shape_counts: Counter[str],
    path_counts: Counter[str],
    concept_type_counts: Counter[str],
    role_counts: Counter[str],
    confidence_counts: Counter[str],
    edge_type_counts: Counter[str],
    edge_evidence_counts: Counter[str],
    skipped_edge_counts: Counter[str],
) -> None:
    shape_counts[str(record["caption_shape"])] += 1
    path_counts[str(record["parse_path"])] += 1
    for mention in record["concept_mentions"]:
        concept_type_counts[str(mention["concept_type"])] += 1
        role_counts[str(mention["role"])] += 1
        confidence_counts[f'mention:{mention["confidence"]}'] += 1
    for edge in record["edges"]:
        edge_type_counts[str(edge["edge_type"])] += 1
        confidence_counts[f'edge:{edge["confidence"]}'] += 1
        if edge["edge_type"] == "relation":
            edge_evidence_counts[str(edge["evidence"])] += 1
    for skipped_edge in record["skipped_edges"]:
        skipped_edge_counts[str(skipped_edge["reason"])] += 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract minimal stage-8 raw concept JSONL from GPIC captions.")
    parser.add_argument("--input", required=True, type=Path, help="Input GPIC caption JSONL or JSONL.GZ")
    parser.add_argument("--output", required=True, type=Path, help="Output raw concept JSONL path")
    parser.add_argument("--summary-output", type=Path, help="Optional markdown summary path")
    parser.add_argument("--max-records", type=int, default=100)
    parser.add_argument("--model", default="en_core_web_trf")
    parser.add_argument("--batch-size", type=int, default=256, help="spaCy nlp.pipe batch size")
    parser.add_argument("--n-process", type=int, default=1, help="spaCy nlp.pipe worker process count")
    parser.add_argument(
        "--mask-quotes",
        action="store_true",
        help="Preserve double-quoted text and merge raw quote spans before spaCy parsing.",
    )
    parser.add_argument(
        "--quote-placeholder",
        default=DEFAULT_PLACEHOLDER,
        help="Deprecated. Raw quote retokenization no longer replaces quoted text with a placeholder.",
    )
    parser.add_argument(
        "--parse-tag-lists",
        action="store_true",
        help="Route GPIC caption_type=tag rows through the tag-list extractor.",
    )
    parser.add_argument(
        "--merge-object-mwes",
        action="store_true",
        help="Merge high-confidence object noun MWEs before spaCy parsing.",
    )
    parser.add_argument(
        "--merge-hyphen-spans",
        action="store_true",
        help="Merge remaining plain hyphen spans before spaCy parsing without forcing POS.",
    )
    parser.add_argument(
        "--object-mwe-lexicon",
        type=Path,
        default=DEFAULT_OBJECT_MWE_LEXICON,
        help="TSV lexicon used by --merge-object-mwes.",
    )
    args = parser.parse_args()

    nlp = spacy.load(args.model)
    if args.mask_quotes:
        ensure_raw_quote_merger(nlp)
    if args.merge_object_mwes:
        ensure_object_mwe_merger(nlp, args.object_mwe_lexicon)
    if args.merge_hyphen_spans:
        ensure_hyphen_span_merger(nlp)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.summary_output:
        args.summary_output.parent.mkdir(parents=True, exist_ok=True)

    shape_counts: Counter[str] = Counter()
    path_counts: Counter[str] = Counter()
    concept_type_counts: Counter[str] = Counter()
    role_counts: Counter[str] = Counter()
    confidence_counts: Counter[str] = Counter()
    edge_type_counts: Counter[str] = Counter()
    edge_evidence_counts: Counter[str] = Counter()
    skipped_edge_counts: Counter[str] = Counter()

    written = 0
    rows = iter_indexed_rows(args.input, args.max_records)
    with args.output.open("w", encoding="utf-8") as handle:
        for row_batch in batched(rows, args.batch_size):
            records = process_indexed_row_batch(
                nlp,
                row_batch,
                mask_quotes=args.mask_quotes,
                parse_tag_lists=args.parse_tag_lists,
                batch_size=args.batch_size,
                n_process=args.n_process,
            )
            for record in records:
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
                written += 1
                update_summary_counts(
                    record,
                    shape_counts=shape_counts,
                    path_counts=path_counts,
                    concept_type_counts=concept_type_counts,
                    role_counts=role_counts,
                    confidence_counts=confidence_counts,
                    edge_type_counts=edge_type_counts,
                    edge_evidence_counts=edge_evidence_counts,
                    skipped_edge_counts=skipped_edge_counts,
                )

    if args.summary_output:
        docs = [
            "# Raw Concept Extraction Summary",
            "",
            f"- input: `{args.input}`",
            f"- output: `{args.output}`",
            f"- model: `{args.model}`",
            f"- max_records: `{args.max_records}`",
            f"- batch_size: `{args.batch_size}`",
            f"- n_process: `{args.n_process}`",
            f"- records_written: `{written}`",
            f"- mask_quotes: `{args.mask_quotes}`",
            f"- quote_handling: `{'raw_quote_retokenize' if args.mask_quotes else 'none'}`",
            f"- merge_object_mwes: `{args.merge_object_mwes}`",
            f"- merge_hyphen_spans: `{args.merge_hyphen_spans}`",
            f"- object_mwe_lexicon: `{args.object_mwe_lexicon}`",
            f"- parse_tag_lists: `{args.parse_tag_lists}`",
            "",
            "## Caption Shapes",
            markdown_count_table(shape_counts),
            "",
            "## Parse Paths",
            markdown_count_table(path_counts),
            "",
            "## Concept Types",
            markdown_count_table(concept_type_counts),
            "",
            "## Mention Roles",
            markdown_count_table(role_counts),
            "",
            "## Edge Types",
            markdown_count_table(edge_type_counts),
            "",
            "## Relation Evidence",
            markdown_count_table(edge_evidence_counts),
            "",
            "## Skipped Edges",
            markdown_count_table(skipped_edge_counts),
            "",
            "## Confidence",
            markdown_count_table(confidence_counts),
            "",
        ]
        args.summary_output.write_text("\n".join(docs), encoding="utf-8")

    print(args.output)
    if args.summary_output:
        print(args.summary_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())