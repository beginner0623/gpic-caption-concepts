from __future__ import annotations

import argparse
import gzip
import json
from pathlib import Path
from typing import Iterable

import spacy


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


def render_doc(nlp, row: dict, index: int) -> str:
    caption = row.get("caption", "")
    doc = nlp(caption)

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
    blocks = [
        f"## {index:02d}",
        "",
        f"**caption_shape:** `{caption_shape(caption)}`",
        "",
        f"> {caption}",
        "",
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
    return "\n".join(blocks)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Inspect spaCy token/POS/lemma/dependency/noun-chunk output for GPIC captions."
    )
    parser.add_argument("--input", required=True, type=Path, help="Input GPIC caption JSONL or JSONL.GZ")
    parser.add_argument("--output", required=True, type=Path, help="Output markdown report path")
    parser.add_argument("--max-records", type=int, default=20)
    parser.add_argument("--model", default="en_core_web_sm")
    args = parser.parse_args()

    nlp = spacy.load(args.model)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    docs = [
        "# spaCy Parse Inspection",
        "",
        f"- input: `{args.input}`",
        f"- model: `{args.model}`",
        f"- max_records: `{args.max_records}`",
        "",
    ]

    for index, row in enumerate(iter_rows(args.input), 1):
        if index > args.max_records:
            break
        docs.append(render_doc(nlp, row, index))

    args.output.write_text("\n".join(docs), encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
