from __future__ import annotations

from dataclasses import asdict, dataclass
import re


DEFAULT_PLACEHOLDER = "the quoted text"


@dataclass(frozen=True)
class QuoteMention:
    caption_id: str | None
    quote_id: str
    global_quote_id: str | None
    text_raw: str
    text_norm: str
    placeholder: str
    char_start: int
    char_end: int
    text_start: int
    text_end: int
    masked_char_start: int
    masked_char_end: int
    quote_open: str
    quote_close: str
    consumed_prefix: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class QuoteMaskResult:
    raw_caption: str
    masked_caption: str
    mentions: list[QuoteMention]

    def to_dict(self) -> dict[str, object]:
        return {
            "raw_caption": self.raw_caption,
            "masked_caption": self.masked_caption,
            "mentions": [mention.to_dict() for mention in self.mentions],
        }


@dataclass
class _QuoteDraft:
    caption_id: str | None
    quote_id: str
    global_quote_id: str | None
    marker: str
    text_raw: str
    text_norm: str
    placeholder: str
    char_start: int
    char_end: int
    text_start: int
    text_end: int
    quote_open: str
    quote_close: str
    consumed_prefix: str
    masked_char_start: int | None = None
    masked_char_end: int | None = None


_WHITESPACE_RE = re.compile(r"\s+")
_SPACE_BEFORE_PUNCT_RE = re.compile(r"\s+([,.;:!?])")
_MISSING_SPACE_AFTER_PUNCT_RE = re.compile(r"([,.;:!?])(?=\S)")
_TEXT_LABEL_SUFFIX_RE = re.compile(
    r"\b(?:the\s+)?(?:text|word|words|phrase|caption|label)\s*$",
    re.IGNORECASE,
)


def normalize_text(text: str) -> str:
    text = text.strip().lower()
    text = _WHITESPACE_RE.sub(" ", text)
    return text


def normalize_masked_caption(text: str) -> str:
    text = _WHITESPACE_RE.sub(" ", text).strip()
    text = _SPACE_BEFORE_PUNCT_RE.sub(r"\1", text)
    text = _MISSING_SPACE_AFTER_PUNCT_RE.sub(r"\1 ", text)
    return text


def _quote_close_for(char: str) -> str | None:
    if char == '"':
        return '"'
    if char == "\u201c":
        return "\u201d"
    return None


def _replacement_for_quote(caption: str, close_i: int, text_raw: str, placeholder: str) -> str:
    stripped = text_raw.strip()
    if not stripped:
        return placeholder

    end_char = stripped[-1]
    next_char = caption[close_i + 1 : close_i + 2]
    if end_char in ".!?" and (not next_char or next_char.isspace()):
        return f"{placeholder}{end_char}"
    return placeholder


def _materialize_markers(
    text: str,
    drafts: list[_QuoteDraft],
    placeholder: str,
) -> tuple[str, list[_QuoteDraft]]:
    pieces: list[str] = []
    cursor = 0
    output_len = 0

    for draft in drafts:
        marker_start = text.find(draft.marker, cursor)
        if marker_start == -1:
            raise ValueError(f"Quote marker not found in masked caption: {draft.marker}")

        before = text[cursor:marker_start]
        pieces.append(before)
        output_len += len(before)

        masked_char_start = output_len
        pieces.append(placeholder)
        output_len += len(placeholder)
        draft.masked_char_start = masked_char_start
        draft.masked_char_end = output_len

        cursor = marker_start + len(draft.marker)

    tail = text[cursor:]
    pieces.append(tail)
    return "".join(pieces), drafts


def mask_quoted_text(
    caption: str,
    placeholder: str = DEFAULT_PLACEHOLDER,
    caption_id: str | None = None,
) -> QuoteMaskResult:
    """Replace double-quoted visible text spans with a parser-friendly noun phrase."""

    pieces: list[str] = []
    drafts: list[_QuoteDraft] = []
    cursor = 0
    i = 0

    while i < len(caption):
        close_char = _quote_close_for(caption[i])
        if close_char is None:
            i += 1
            continue

        close_i = caption.find(close_char, i + 1)
        if close_i == -1:
            i += 1
            continue

        text_start = i + 1
        text_end = close_i
        text_raw = caption[text_start:text_end]
        prefix_text = caption[cursor:i]
        consumed_prefix = ""
        prefix_match = _TEXT_LABEL_SUFFIX_RE.search(prefix_text)
        if prefix_match:
            consumed_prefix = prefix_match.group(0).strip()
            prefix_text = prefix_text[: prefix_match.start()]

        pieces.append(prefix_text)

        quote_index = len(drafts)
        quote_id = f"q{quote_index}"
        marker = f"<<<QUOTE_{quote_index}>>>"
        pieces.append(_replacement_for_quote(caption, close_i, text_raw, marker))
        drafts.append(
            _QuoteDraft(
                caption_id=caption_id,
                quote_id=quote_id,
                global_quote_id=f"{caption_id}:{quote_id}" if caption_id else None,
                marker=marker,
                text_raw=text_raw,
                text_norm=normalize_text(text_raw),
                placeholder=placeholder,
                char_start=i,
                char_end=close_i + 1,
                text_start=text_start,
                text_end=text_end,
                quote_open=caption[i],
                quote_close=caption[close_i],
                consumed_prefix=consumed_prefix,
            )
        )

        i = close_i + 1
        cursor = i

    if not drafts:
        return QuoteMaskResult(raw_caption=caption, masked_caption=caption, mentions=[])

    pieces.append(caption[cursor:])
    marker_caption = normalize_masked_caption("".join(pieces))
    masked_caption, drafts = _materialize_markers(marker_caption, drafts, placeholder)
    mentions: list[QuoteMention] = []
    for draft in drafts:
        if draft.masked_char_start is None or draft.masked_char_end is None:
            raise ValueError(f"Quote marker was not materialized: {draft.marker}")
        mentions.append(
            QuoteMention(
                caption_id=draft.caption_id,
                quote_id=draft.quote_id,
                global_quote_id=draft.global_quote_id,
                text_raw=draft.text_raw,
                text_norm=draft.text_norm,
                placeholder=draft.placeholder,
                char_start=draft.char_start,
                char_end=draft.char_end,
                text_start=draft.text_start,
                text_end=draft.text_end,
                masked_char_start=draft.masked_char_start,
                masked_char_end=draft.masked_char_end,
                quote_open=draft.quote_open,
                quote_close=draft.quote_close,
                consumed_prefix=draft.consumed_prefix,
            )
        )
    return QuoteMaskResult(
        raw_caption=caption,
        masked_caption=masked_caption,
        mentions=mentions,
    )


def has_quoted_text(caption: str) -> bool:
    return bool(mask_quoted_text(caption).mentions)
