from __future__ import annotations

import argparse
import gzip
import json
from pathlib import Path
from typing import Iterable

import spacy

from hyphen_span_retokenizer import ensure_hyphen_span_merger
from object_mwe_retokenizer import DEFAULT_OBJECT_MWE_LEXICON, ensure_object_mwe_merger
from quote_masking import DEFAULT_PLACEHOLDER, collect_quoted_text
from quote_retokenizer import ensure_raw_quote_merger
from raw_concept_extractor import extract_raw_concepts
from tag_list_parser import is_tag_list_row, parse_tag_list


def open_text(path: Path):
    if path.suffix == ".gz":
        return gzip.open(path, "rt", encoding="utf-8")
    return path.open("rt", encoding="utf-8")


def iter_rows(path: Path) -> Iterable[dict]:
    with open_text(path) as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(line)


def caption_shape(caption: str) -> str:
    comma_count = caption.count(",")
    sentence_marks = sum(caption.count(mark) for mark in ".!?")
    word_count = len(caption.split())
    if comma_count >= 2 and sentence_marks == 0:
        return "tag-list-like"
    if sentence_marks >= 2:
        return "multi-sentence"
    if word_count <= 8 and comma_count >= 1:
        return "short-list-like"
    return "sentence-like"


def row_caption_id(row: dict) -> str | None:
    value = row.get("key") or row.get("caption_id") or row.get("_gpic_shard_member")
    return str(value) if value is not None else None


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    escaped = []
    for row in rows:
        escaped.append([str(cell).replace("|", "\\|").replace("\n", " ") for cell in row])
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in escaped)
    return "\n".join(lines)


def render_doc(
    nlp,
    row: dict,
    index: int,
    mask_quotes: bool = False,
    quote_placeholder: str = DEFAULT_PLACEHOLDER,
    parse_tag_lists: bool = False,
    extract_raw_concepts_flag: bool = False,
) -> str:
    caption = row.get("caption", "")
    caption_id = row_caption_id(row)
    quote_result = (
        collect_quoted_text(caption, caption_id=caption_id)
        if mask_quotes
        else None
    )
    parse_caption = caption
    quote_rows = []
    if quote_result:
        for mention in quote_result.mentions:
            quote_rows.append(
                [
                    mention.quote_id,
                    mention.global_quote_id or "",
                    mention.text_raw,
                    mention.text_norm,
                    mention.placeholder,
                    mention.consumed_prefix,
                    f"{mention.char_start}:{mention.char_end}",
                    f"{mention.masked_char_start}:{mention.masked_char_end}",
                ]
            )

    blocks = [
        f"## {index:02d}",
        "",
        f"**caption_shape:** `{caption_shape(caption)}`",
        f"**caption_id:** `{caption_id}`" if caption_id else "**caption_id:** `_none_`",
        "",
        f"> {caption}",
        "",
    ]
    if quote_result and quote_result.mentions:
        blocks.extend(
            [
                "**parsed_caption:**",
                "",
                f"> {parse_caption}",
                "",
                "### Quote Mentions",
                markdown_table(
                    [
                        "id",
                        "global_id",
                        "text_raw",
                        "text_norm",
                        "placeholder",
                        "consumed_prefix",
                        "raw_char_span",
                        "parse_char_span",
                    ],
                    quote_rows,
                )
                if quote_rows
                else "_none_",
                "",
            ]
        )

    if parse_tag_lists and is_tag_list_row(row, parse_caption):
        tag_result = parse_tag_list(nlp, parse_caption)
        segment_rows = [
            [segment.tag_id, segment.raw, segment.norm, f"{segment.char_start}:{segment.char_end}"]
            for segment in tag_result.segments
        ]
        segment_chunk_rows = [
            [
                chunk.tag_id,
                chunk.chunk,
                chunk.root,
                chunk.root_lemma,
                chunk.root_dep,
                chunk.root_head,
                f"{chunk.token_start}:{chunk.token_end}",
                f"{chunk.char_start}:{chunk.char_end}",
            ]
            for chunk in tag_result.noun_chunks
        ]
        segment_token_rows = [
            [
                token.tag_id,
                token.i,
                token.text,
                token.lemma,
                token.pos_raw,
                token.pos_norm,
                token.tag_raw,
                token.tag_norm,
                token.dep,
                token.head,
                token.head_i,
                f"{token.char_start}:{token.char_end}",
            ]
            for token in tag_result.tokens
        ]
        mention_rows = [
            [
                mention.mention_id,
                mention.concept_type,
                mention.text,
                mention.lemma,
                mention.source_tag,
                "" if mention.source_token_i is None else mention.source_token_i,
                mention.role,
                mention.confidence,
            ]
            for mention in tag_result.concept_mentions
        ]
        edge_rows = [
            [
                edge.edge_id,
                edge.edge_type,
                edge.source,
                edge.target,
                edge.confidence,
                edge.evidence,
            ]
            for edge in tag_result.edges
        ]
        blocks.extend(
            [
                "### Tag Segments",
                markdown_table(["tag_id", "raw", "norm", "char_span"], segment_rows)
                if segment_rows
                else "_none_",
                "",
                "### Segment Noun Chunks",
                markdown_table(
                    [
                        "tag_id",
                        "chunk",
                        "root",
                        "root_lemma",
                        "root_dep",
                        "root_head",
                        "token_span",
                        "char_span",
                    ],
                    segment_chunk_rows,
                )
                if segment_chunk_rows
                else "_none_",
                "",
                "### Segment Tokens / POS / Lemma / Dependency",
                markdown_table(
                    [
                        "tag_id",
                        "i",
                        "text",
                        "lemma",
                        "pos_raw",
                        "pos_norm",
                        "tag_raw",
                        "tag_norm",
                        "dep",
                        "head",
                        "head_i",
                        "char_span",
                    ],
                    segment_token_rows,
                )
                if segment_token_rows
                else "_none_",
                "",
                "### Concept Mentions",
                markdown_table(
                    ["id", "type", "text", "lemma", "source_tag", "source_token", "role", "confidence"],
                    mention_rows,
                )
                if mention_rows
                else "_none_",
                "",
                "### Edges",
                markdown_table(["id", "type", "source", "target", "confidence", "evidence"], edge_rows)
                if edge_rows
                else "_none_",
                "",
            ]
        )
        return "\n".join(blocks)

    doc = nlp(parse_caption)

    token_rows = []
    for token in doc:
        token_rows.append(
            [
                token.i,
                token.text,
                token.lemma_,
                token.pos_,
                token.tag_,
                token.dep_,
                token.head.text,
                token.head.i,
            ]
        )

    chunk_rows = []
    for chunk in doc.noun_chunks:
        root = chunk.root
        chunk_rows.append(
            [
                chunk.text,
                root.text,
                root.lemma_,
                root.dep_,
                root.head.text,
                f"{chunk.start}:{chunk.end}",
            ]
        )

    sent_rows = [[sent.text, f"{sent.start}:{sent.end}"] for sent in doc.sents]
    blocks.extend(
        [
            "### Sentences",
            markdown_table(["sentence", "token_span"], sent_rows) if sent_rows else "_none_",
            "",
            "### Noun Chunks",
            markdown_table(["chunk", "root", "root_lemma", "root_dep", "root_head", "token_span"], chunk_rows)
            if chunk_rows
            else "_none_",
            "",
            "### Tokens / POS / Lemma / Dependency",
            markdown_table(["i", "text", "lemma", "pos", "tag", "dep", "head", "head_i"], token_rows),
            "",
        ]
    )
    if extract_raw_concepts_flag:
        raw_result = extract_raw_concepts(doc)
        mention_rows = [
            [
                mention.mention_id,
                mention.concept_type,
                mention.text,
                mention.lemma,
                mention.source_tag,
                "" if mention.source_token_i is None else mention.source_token_i,
                mention.role,
                mention.confidence,
            ]
            for mention in raw_result.concept_mentions
        ]
        edge_rows = [
            [
                edge.edge_id,
                edge.edge_type,
                edge.source,
                edge.target,
                edge.confidence,
                edge.evidence,
            ]
            for edge in raw_result.edges
        ]
        skipped_edge_rows = [
            [
                skipped_edge["edge_type"],
                skipped_edge["source"],
                skipped_edge["target"],
                skipped_edge["confidence"],
                skipped_edge["reason"],
                skipped_edge["evidence"],
            ]
            for skipped_edge in raw_result.skipped_edges
        ]
        blocks.extend(
            [
                "### Raw Concept Mentions",
                markdown_table(
                    ["id", "type", "text", "lemma", "source_tag", "source_token", "role", "confidence"],
                    mention_rows,
                )
                if mention_rows
                else "_none_",
                "",
                "### Raw Concept Edges",
                markdown_table(["id", "type", "source", "target", "confidence", "evidence"], edge_rows)
                if edge_rows
                else "_none_",
                "",
                "### Skipped Raw Concept Edges",
                markdown_table(["type", "source", "target", "confidence", "reason", "evidence"], skipped_edge_rows)
                if skipped_edge_rows
                else "_none_",
                "",
            ]
        )
    return "\n".join(blocks)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Inspect spaCy token/POS/lemma/dependency/noun-chunk output for GPIC captions."
    )
    parser.add_argument("--input", required=True, type=Path, help="Input GPIC caption JSONL or JSONL.GZ")
    parser.add_argument("--output", required=True, type=Path, help="Output markdown report path")
    parser.add_argument("--max-records", type=int, default=20)
    parser.add_argument("--model", default="en_core_web_sm")
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
        help="Render GPIC caption_type=tag rows with segment-level tag-list parsing.",
    )
    parser.add_argument(
        "--extract-raw-concepts",
        action="store_true",
        help="Render minimal stage-8 raw concept mentions and edges for sentence captions.",
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
    docs = [
        "# spaCy Parse Inspection",
        "",
        f"- input: `{args.input}`",
        f"- model: `{args.model}`",
        f"- max_records: `{args.max_records}`",
        f"- mask_quotes: `{args.mask_quotes}`",
        f"- quote_handling: `{'raw_quote_retokenize' if args.mask_quotes else 'none'}`",
        f"- quote_placeholder: `deprecated_unused`",
        f"- merge_object_mwes: `{args.merge_object_mwes}`",
        f"- merge_hyphen_spans: `{args.merge_hyphen_spans}`",
        f"- object_mwe_lexicon: `{args.object_mwe_lexicon}`",
        f"- parse_tag_lists: `{args.parse_tag_lists}`",
        "",
    ]

    for index, row in enumerate(iter_rows(args.input), 1):
        if index > args.max_records:
            break
        docs.append(
            render_doc(
                nlp,
                row,
                index,
                mask_quotes=args.mask_quotes,
                quote_placeholder=args.quote_placeholder,
                parse_tag_lists=args.parse_tag_lists,
                extract_raw_concepts_flag=args.extract_raw_concepts,
            )
        )

    args.output.write_text("\n".join(docs), encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
