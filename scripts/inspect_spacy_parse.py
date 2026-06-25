from __future__ import annotations

import argparse
import gzip
import json
from pathlib import Path
from typing import Iterable

import spacy

from quote_masking import DEFAULT_PLACEHOLDER, mask_quoted_text


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
) -> str:
    caption = row.get("caption", "")
    caption_id = row_caption_id(row)
    quote_result = (
        mask_quoted_text(caption, placeholder=quote_placeholder, caption_id=caption_id)
        if mask_quotes
        else None
    )
    parse_caption = quote_result.masked_caption if quote_result else caption
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
                        "masked_char_span",
                    ],
                    quote_rows,
                )
                if quote_rows
                else "_none_",
                "",
            ]
        )
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
        help=f'Replace double-quoted text spans with "{DEFAULT_PLACEHOLDER}" before spaCy parsing.',
    )
    parser.add_argument(
        "--quote-placeholder",
        default=DEFAULT_PLACEHOLDER,
        help="Natural-language placeholder used when --mask-quotes is enabled.",
    )
    args = parser.parse_args()

    nlp = spacy.load(args.model)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    docs = [
        "# spaCy Parse Inspection",
        "",
        f"- input: `{args.input}`",
        f"- model: `{args.model}`",
        f"- max_records: `{args.max_records}`",
        f"- mask_quotes: `{args.mask_quotes}`",
        f"- quote_placeholder: `{args.quote_placeholder}`",
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
            )
        )

    args.output.write_text("\n".join(docs), encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
