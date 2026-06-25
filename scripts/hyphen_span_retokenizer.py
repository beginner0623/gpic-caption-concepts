from __future__ import annotations

from spacy.language import Language
from spacy.tokens import Doc, Token
from spacy.util import filter_spans

from object_mwe_retokenizer import OBJECT_MWE_MERGER
from quote_retokenizer import RAW_QUOTE_MERGER


HYPHEN_SPAN_MERGER = "hyphen_span_merger"
HYPHEN_SPAN_FLAG = "is_hyphen_span"
HYPHEN_CHARS = {"-", "‐", "‑"}


def ensure_token_extensions() -> None:
    if not Token.has_extension(HYPHEN_SPAN_FLAG):
        Token.set_extension(HYPHEN_SPAN_FLAG, default=False)


def is_plain_hyphen(token) -> bool:
    return token.text in HYPHEN_CHARS


def is_mergeable_hyphen_part(token) -> bool:
    text = token.text
    return any(char.isalpha() for char in text) and all(char.isalnum() for char in text)


def should_merge_parts(parts: list) -> bool:
    if len(parts) < 2:
        return False
    if any(part.text.isdigit() for part in parts):
        return False
    return any(len(part.text) > 1 for part in parts)


class HyphenSpanMerger:
    def __init__(self, nlp: Language) -> None:
        ensure_token_extensions()

    def __call__(self, doc: Doc) -> Doc:
        spans = []
        i = 0
        while i < len(doc):
            if not is_mergeable_hyphen_part(doc[i]):
                i += 1
                continue

            parts = [doc[i]]
            end = i + 1
            while end + 1 < len(doc) and is_plain_hyphen(doc[end]) and is_mergeable_hyphen_part(doc[end + 1]):
                parts.append(doc[end + 1])
                end += 2

            if len(parts) > 1 and should_merge_parts(parts):
                spans.append(doc[i:end])
                i = end
            else:
                i += 1

        spans = filter_spans(spans)
        if not spans:
            return doc

        with doc.retokenize() as retokenizer:
            for span in spans:
                retokenizer.merge(span, attrs={"_": {HYPHEN_SPAN_FLAG: True}})
        return doc


@Language.factory(HYPHEN_SPAN_MERGER)
def create_hyphen_span_merger(nlp: Language, name: str) -> HyphenSpanMerger:
    return HyphenSpanMerger(nlp)


def ensure_hyphen_span_merger(nlp: Language) -> Language:
    if HYPHEN_SPAN_MERGER in nlp.pipe_names:
        return nlp
    if OBJECT_MWE_MERGER in nlp.pipe_names:
        nlp.add_pipe(HYPHEN_SPAN_MERGER, after=OBJECT_MWE_MERGER)
    elif RAW_QUOTE_MERGER in nlp.pipe_names:
        nlp.add_pipe(HYPHEN_SPAN_MERGER, after=RAW_QUOTE_MERGER)
    else:
        nlp.add_pipe(HYPHEN_SPAN_MERGER, first=True)
    return nlp
