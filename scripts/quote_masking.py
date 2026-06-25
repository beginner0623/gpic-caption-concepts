from __future__ import annotations

from dataclasses import asdict, dataclass
import re


DEFAULT_PLACEHOLDER = "quoted text"


@dataclass(frozen=True)
class QuoteMention:
    quote_id: str
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

    def to_dict(self) -> dict[str, str | int]:
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


def mask_quoted_text(caption: str, placeholder: str = DEFAULT_PLACEHOLDER) -> QuoteMaskResult:
    """Replace double-quoted visible text spans with a parser-friendly noun phrase."""

    pieces: list[str] = []
    mentions: list[QuoteMention] = []
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
        pieces.append(_replacement_for_quote(caption, close_i, text_raw, placeholder))

        mention_id = f"q{len(mentions)}"
        mentions.append(
            QuoteMention(
                quote_id=mention_id,
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

    if not mentions:
        return QuoteMaskResult(raw_caption=caption, masked_caption=caption, mentions=[])

    pieces.append(caption[cursor:])
    return QuoteMaskResult(
        raw_caption=caption,
        masked_caption=normalize_masked_caption("".join(pieces)),
        mentions=mentions,
    )


def has_quoted_text(caption: str) -> bool:
    return bool(mask_quoted_text(caption).mentions)
