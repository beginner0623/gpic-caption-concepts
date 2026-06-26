from __future__ import annotations

import re

from spacy.language import Language
from spacy.tokens import Doc, Span, Token
from spacy.util import filter_spans


RAW_QUOTE_MERGER = "raw_quote_merger"
RAW_QUOTE_FLAG = "is_raw_quote"
QUOTE_CLOSE = {'"': '"', "\u201c": "\u201d"}
_LEMMA_CLEAN_RE = re.compile(r"\s+")


def ensure_raw_quote_extensions() -> None:
    if not Token.has_extension(RAW_QUOTE_FLAG):
        Token.set_extension(RAW_QUOTE_FLAG, default=False)


def quote_span_lemma(text: str) -> str:
    inner = text.strip().strip('"').strip("\u201c\u201d")
    inner = inner.strip().lower()
    return _LEMMA_CLEAN_RE.sub("_", inner)


def is_raw_quote_text(text: str) -> bool:
    text = text.strip()
    if len(text) < 2:
        return False
    close = QUOTE_CLOSE.get(text[0])
    return close is not None and text[-1] == close


def is_raw_quote_token(token) -> bool:
    ensure_raw_quote_extensions()
    if token._.get(RAW_QUOTE_FLAG):
        return True
    return is_raw_quote_text(token.text)


def raw_quote_spans(doc: Doc) -> list[Span]:
    spans: list[Span] = []
    i = 0
    while i < len(doc):
        closer = QUOTE_CLOSE.get(doc[i].text)
        if closer is None:
            i += 1
            continue

        close_i = None
        for j in range(i + 1, len(doc)):
            if doc[j].text == closer:
                close_i = j
                break

        if close_i is None:
            i += 1
            continue

        spans.append(doc[i : close_i + 1])
        i = close_i + 1

    return list(filter_spans(spans))


def merge_raw_quote_spans(doc: Doc) -> Doc:
    ensure_raw_quote_extensions()
    spans = raw_quote_spans(doc)
    if not spans:
        return doc

    with doc.retokenize() as retokenizer:
        for span in spans:
            retokenizer.merge(
                span,
                attrs={
                    "LEMMA": quote_span_lemma(span.text),
                    "_": {RAW_QUOTE_FLAG: True},
                },
            )

    return doc


@Language.component(RAW_QUOTE_MERGER)
def raw_quote_merger(doc: Doc) -> Doc:
    return merge_raw_quote_spans(doc)


def ensure_raw_quote_merger(nlp: Language) -> Language:
    if RAW_QUOTE_MERGER not in nlp.pipe_names:
        nlp.add_pipe(RAW_QUOTE_MERGER, first=True)
    return nlp
