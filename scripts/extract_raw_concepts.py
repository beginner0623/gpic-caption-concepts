from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path

import spacy

from hyphen_span_retokenizer import ensure_hyphen_span_merger
from inspect_spacy_parse import caption_shape, iter_rows, row_caption_id
from object_mwe_retokenizer import DEFAULT_OBJECT_MWE_LEXICON, ensure_object_mwe_merger
from quote_masking import DEFAULT_PLACEHOLDER, collect_quoted_text
from quote_retokenizer import ensure_raw_quote_merger
from raw_concept_extractor import extract_raw_concepts
from tag_list_parser import is_tag_list_row, parse_tag_list


def markdown_count_table(counter: Counter[str]) -> str:
    if not counter:
        return "_none_"
    lines = ["| item | count |", "| --- | ---: |"]
    for key, value in counter.most_common():
        lines.append(f"| `{key}` | {value} |")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract minimal stage-8 raw concept JSONL from GPIC captions.")
    parser.add_argument("--input", required=True, type=Path, help="Input GPIC caption JSONL or JSONL.GZ")
    parser.add_argument("--output", required=True, type=Path, help="Output raw concept JSONL path")
    parser.add_argument("--summary-output", type=Path, help="Optional markdown summary path")
    parser.add_argument("--max-records", type=int, default=100)
    parser.add_argument("--model", default="en_core_web_trf")
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
    with args.output.open("w", encoding="utf-8") as handle:
        for index, row in enumerate(iter_rows(args.input), 1):
            if index > args.max_records:
                break
            caption = row.get("caption", "")
            caption_id = row_caption_id(row)
            quote_result = collect_quoted_text(caption, caption_id=caption_id) if args.mask_quotes else None
            parse_caption = caption
            shape = caption_shape(caption)

            if args.parse_tag_lists and is_tag_list_row(row, parse_caption):
                tag_result = parse_tag_list(nlp, parse_caption)
                parse_path = "tag_list"
                mentions = [mention.to_dict() for mention in tag_result.concept_mentions]
                edges = [edge.to_dict() for edge in tag_result.edges]
                skipped_edges = []
            else:
                doc = nlp(parse_caption)
                raw_result = extract_raw_concepts(doc)
                parse_path = "sentence"
                mentions = [mention.to_dict() for mention in raw_result.concept_mentions]
                edges = [edge.to_dict() for edge in raw_result.edges]
                skipped_edges = raw_result.skipped_edges

            quote_mentions = [mention.to_dict() for mention in quote_result.mentions] if quote_result else []
            record = {
                "row_index": index,
                "caption_id": caption_id,
                "caption_type": row.get("caption_type"),
                "caption_shape": shape,
                "parse_path": parse_path,
                "caption": caption,
                "parse_caption": parse_caption,
                "quote_mentions": quote_mentions,
                "concept_mentions": mentions,
                "edges": edges,
                "skipped_edges": skipped_edges,
            }
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
            written += 1

            shape_counts[shape] += 1
            path_counts[parse_path] += 1
            for mention in mentions:
                concept_type_counts[str(mention["concept_type"])] += 1
                role_counts[str(mention["role"])] += 1
                confidence_counts[f'mention:{mention["confidence"]}'] += 1
            for edge in edges:
                edge_type_counts[str(edge["edge_type"])] += 1
                confidence_counts[f'edge:{edge["confidence"]}'] += 1
                if edge["edge_type"] == "relation":
                    edge_evidence_counts[str(edge["evidence"])] += 1
            for skipped_edge in skipped_edges:
                skipped_edge_counts[str(skipped_edge["reason"])] += 1

    if args.summary_output:
        docs = [
            "# Raw Concept Extraction Summary",
            "",
            f"- input: `{args.input}`",
            f"- output: `{args.output}`",
            f"- model: `{args.model}`",
            f"- max_records: `{args.max_records}`",
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
