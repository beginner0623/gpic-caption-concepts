from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import spacy

from quote_masking import mask_quoted_text
from quote_retokenizer import RAW_QUOTE_MERGER, ensure_raw_quote_merger, merge_raw_quote_spans
from raw_concept_extractor import extract_raw_concepts


@dataclass(frozen=True)
class TestCase:
    case_id: str
    caption: str


TEST_CASES = [
    TestCase(
        "royal_canin_banner",
        'A brown dog leaps over a blue, white, and red basket on grass. A man in a black outfit with red and blue trim stands nearby, watching the dog. In the background, spectators stand behind a fence near a "ROYAL CANIN" banner.',
    ),
    TestCase(
        "number_tag",
        'A white fabric tag with the number "1709-1" is stitched onto a bright yellow garment. The tag is slightly frayed at the edges and sits against the textured, wrinkled fabric of the clothing.',
    ),
    TestCase(
        "screen_shows_text",
        'A woman stands at a podium speaking in front of an audience. An American flag is behind her, and a screen shows "Closing the Access Divide."',
    ),
    TestCase(
        "poster_reads_text",
        'A poster on a black trash can reads "BANG GOES THE KNIGHTHOOD" with a silhouette of a man in a hat. The scene is on a city sidewalk.',
    ),
    TestCase(
        "building_with_sign",
        'A large building with "P.J. HURPHY MOVING & STORAGE" sign stands beside a road, near tall smokestacks and power lines.',
    ),
]


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    escaped_rows = []
    for row in rows:
        escaped_rows.append([str(cell).replace("|", "\\|").replace("\n", " ") for cell in row])
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in escaped_rows)
    return "\n".join(lines)


def load_nlp(model: str, mode: str):
    nlp = spacy.load(model)
    if mode == "raw_merge_first":
        ensure_raw_quote_merger(nlp)
        return nlp
    if mode == "raw_merge_before_parser":
        if "parser" in nlp.pipe_names:
            nlp.add_pipe(RAW_QUOTE_MERGER, before="parser")
        else:
            nlp.add_pipe(RAW_QUOTE_MERGER, last=True)
    return nlp


def render_doc(nlp, text: str, mode: str) -> tuple[list[list[object]], list[list[object]], list[list[object]], list[list[object]]]:
    doc = nlp(text)
    if mode == "raw_merge_after_parser":
        doc = merge_raw_quote_spans(doc)

    token_rows = [
        [token.i, token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.head.text, token.head.i]
        for token in doc
    ]
    chunk_rows = [
        [
            chunk.text,
            chunk.root.text,
            chunk.root.lemma_,
            chunk.root.dep_,
            chunk.root.head.text,
            f"{chunk.start}:{chunk.end}",
        ]
        for chunk in doc.noun_chunks
    ]

    raw_result = extract_raw_concepts(doc)
    mention_rows = [
        [
            mention.mention_id,
            mention.concept_type,
            mention.text,
            mention.lemma,
            mention.source_token_i if mention.source_token_i is not None else "",
            mention.role,
            mention.confidence,
        ]
        for mention in raw_result.concept_mentions
    ]
    edge_rows = [
        [edge.edge_id, edge.edge_type, edge.source, edge.target, edge.confidence, edge.evidence]
        for edge in raw_result.edges
    ]
    return token_rows, chunk_rows, mention_rows, edge_rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare raw double-quoted span parsing with spaCy Retokenizer merge.")
    parser.add_argument("--model", default="en_core_web_trf")
    parser.add_argument("--output", type=Path, default=Path("reports/quote_retokenizer_experiment.md"))
    args = parser.parse_args()

    nlps = {
        "raw_no_merge": load_nlp(args.model, "raw_no_merge"),
        "raw_merge_after_parser": load_nlp(args.model, "raw_merge_after_parser"),
        "raw_merge_first": load_nlp(args.model, "raw_merge_first"),
        "raw_merge_before_parser": load_nlp(args.model, "raw_merge_before_parser"),
    }

    docs = [
        "# Raw Quote Retokenizer Experiment",
        "",
        f"- model: `{args.model}`",
        "- `raw_no_merge`: 원문 caption을 그대로 parsing",
        "- `raw_merge_after_parser`: spaCy 전체 pipeline 후 `\"...\"` span을 merge",
        "- `raw_merge_first`: tokenizer 직후, transformer/tagger/parser 전에 `\"...\"` span을 merge",
        "- `raw_merge_before_parser`: transformer/tagger 뒤, parser 전에 `\"...\"` span을 merge",
        "",
        "## Summary",
        "",
        "이 실험은 quote를 `the quoted text`로 바꾸지 않고, 원문 `\"...\"` span 자체를 Retokenizer로 합쳤을 때 parser와 Stage 8 후보가 어떻게 달라지는지 확인하기 위한 것입니다.",
        "",
        "## Observed Result",
        "",
        "- `raw_merge_first`가 이번 비교에서 가장 낫습니다. quote span을 tokenizer 직후 하나의 token으로 합치면 `a \"ROYAL CANIN\" banner`, `the number \"1709-1\"`, `screen shows \"...\"`, `poster reads \"...\"` 구조가 대체로 자연스럽게 유지됩니다.",
        "- `raw_merge_first`는 `the quoted text` placeholder를 만들지 않으므로 `a the quoted text banner` 같은 문법 오염이 생기지 않습니다.",
        "- `raw_merge_after_parser`는 token만 합칠 뿐 이미 끝난 dependency/POS 판단을 되돌리지 못합니다. 그래서 quote 안 첫 단어가 동사처럼 분석된 경우에는 action 오염이 남을 수 있습니다.",
        "- `raw_merge_before_parser`처럼 transformer/tagger 뒤, parser 앞에서만 합치는 방식은 권장하지 않습니다. POS/tag 정보가 quote-open token 쪽으로 남아 merged token이 `PUNCT`처럼 취급되고 dependency가 크게 깨졌습니다.",
        "- 그래도 최종 Stage 9에서는 merged quote token을 실제 object 이름으로 세지 말고 `TEXT_SPAN(qid)` 또는 `LABEL_VALUE(qid)` 같은 quote mention으로 canonicalize해야 합니다.",
        "",
    ]

    for case in TEST_CASES:
        quote_result = mask_quoted_text(case.caption, caption_id=case.case_id)
        docs.extend(
            [
                f"## {case.case_id}",
                "",
                "**raw_caption:**",
                "",
                f"> {case.caption}",
                "",
                "**masked_caption_reference:**",
                "",
                f"> {quote_result.masked_caption}",
                "",
                "### Quote Mentions",
                markdown_table(
                    ["id", "text_raw", "placeholder", "consumed_prefix", "raw_span", "masked_span"],
                    [
                        [
                            mention.quote_id,
                            mention.text_raw,
                            mention.placeholder,
                            mention.consumed_prefix,
                            f"{mention.char_start}:{mention.char_end}",
                            f"{mention.masked_char_start}:{mention.masked_char_end}",
                        ]
                        for mention in quote_result.mentions
                    ],
                ),
                "",
            ]
        )

        for mode, nlp in nlps.items():
            token_rows, chunk_rows, mention_rows, edge_rows = render_doc(nlp, case.caption, mode)
            docs.extend(
                [
                    f"### {mode}",
                    "",
                    "**Noun Chunks**",
                    markdown_table(["chunk", "root", "root_lemma", "root_dep", "root_head", "token_span"], chunk_rows)
                    if chunk_rows
                    else "_none_",
                    "",
                    "**Tokens**",
                    markdown_table(["i", "text", "lemma", "pos", "tag", "dep", "head", "head_i"], token_rows),
                    "",
                    "**Raw Concept Mentions**",
                    markdown_table(
                        ["id", "type", "text", "lemma", "source_token", "role", "confidence"],
                        mention_rows,
                    )
                    if mention_rows
                    else "_none_",
                    "",
                    "**Raw Concept Edges**",
                    markdown_table(["id", "type", "source", "target", "confidence", "evidence"], edge_rows)
                    if edge_rows
                    else "_none_",
                    "",
                ]
            )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(docs), encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
