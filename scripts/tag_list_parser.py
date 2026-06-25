from __future__ import annotations

from dataclasses import asdict, dataclass
import re


CONTEXT_TAGS = {
    "indoor",
    "indoors",
    "outdoor",
    "outdoors",
    "inside",
    "outside",
    "day",
    "night",
    "daytime",
    "nighttime",
    "morning",
    "evening",
    "dusk",
    "dawn",
    "sunset",
    "background",
    "foreground",
}

ATTRIBUTE_POS = {"ADJ", "ADV"}
OBJECT_POS = {"NOUN", "PROPN", "PRON"}
MODIFIER_DEPS = {"amod", "compound", "nummod", "poss", "acl"}
STATE_ATTRIBUTE_WORDS = {
    "smile",
    "smiling",
    "stand",
    "standing",
    "sit",
    "sitting",
    "walk",
    "walking",
    "run",
    "running",
    "sleep",
    "sleeping",
    "dance",
    "dancing",
    "play",
    "playing",
    "ride",
    "riding",
    "hold",
    "holding",
}


@dataclass(frozen=True)
class TagSegment:
    tag_id: str
    raw: str
    norm: str
    char_start: int
    char_end: int

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class SegmentToken:
    tag_id: str
    i: int
    text: str
    lemma: str
    pos: str
    tag: str
    dep: str
    head: str
    head_i: int
    char_start: int
    char_end: int

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class SegmentNounChunk:
    tag_id: str
    chunk: str
    root: str
    root_lemma: str
    root_dep: str
    root_head: str
    token_start: int
    token_end: int
    char_start: int
    char_end: int

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class ConceptMention:
    mention_id: str
    concept_type: str
    text: str
    lemma: str
    source_tag: str
    source_token_i: int | None
    role: str
    confidence: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class ConceptEdge:
    edge_id: str
    edge_type: str
    source: str
    target: str
    confidence: str
    evidence: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class TagListParseResult:
    segments: list[TagSegment]
    noun_chunks: list[SegmentNounChunk]
    tokens: list[SegmentToken]
    concept_mentions: list[ConceptMention]
    edges: list[ConceptEdge]

    def to_dict(self) -> dict[str, object]:
        return {
            "segments": [segment.to_dict() for segment in self.segments],
            "noun_chunks": [chunk.to_dict() for chunk in self.noun_chunks],
            "tokens": [token.to_dict() for token in self.tokens],
            "concept_mentions": [mention.to_dict() for mention in self.concept_mentions],
            "edges": [edge.to_dict() for edge in self.edges],
        }


_WHITESPACE_RE = re.compile(r"\s+")


def normalize_tag_text(text: str) -> str:
    return _WHITESPACE_RE.sub(" ", text.strip().lower())


def split_tag_segments(caption: str) -> list[TagSegment]:
    segments: list[TagSegment] = []
    cursor = 0
    tag_index = 0

    while cursor <= len(caption):
        comma_i = caption.find(",", cursor)
        if comma_i == -1:
            part_end = len(caption)
            is_last = True
        else:
            part_end = comma_i
            is_last = False

        raw_part = caption[cursor:part_end]
        leading = len(raw_part) - len(raw_part.lstrip())
        trailing = len(raw_part.rstrip())
        char_start = cursor + leading
        char_end = cursor + trailing
        raw = caption[char_start:char_end]
        if raw:
            segments.append(
                TagSegment(
                    tag_id=f"t{tag_index}",
                    raw=raw,
                    norm=normalize_tag_text(raw),
                    char_start=char_start,
                    char_end=char_end,
                )
            )
            tag_index += 1

        if is_last:
            break
        cursor = comma_i + 1

    return segments


def _root_token(doc):
    roots = [token for token in doc if token.dep_ == "ROOT"]
    if roots:
        return roots[0]
    return doc[-1] if len(doc) else None


def _object_head(doc):
    nouns = [token for token in doc if token.pos_ in OBJECT_POS]
    if nouns:
        return nouns[-1]
    root = _root_token(doc)
    if root is not None and root.pos_ in OBJECT_POS:
        return root
    if len(doc) == 1 and root is not None and root.tag_ not in {"JJ", "JJR", "JJS", "VBN"}:
        return root
    return None


def _is_context_segment(doc, segment: TagSegment) -> bool:
    if segment.norm in CONTEXT_TAGS:
        return True
    if len(doc) == 1 and doc[0].lemma_.lower() in CONTEXT_TAGS:
        return True
    return False


def _is_floating_attribute(doc) -> bool:
    if len(doc) != 1:
        return False
    token = doc[0]
    if token.pos_ in ATTRIBUTE_POS or token.tag_ in {"JJ", "JJR", "JJS", "VBN"}:
        return True
    if token.tag_ == "VBG":
        return token.lemma_.lower() in STATE_ATTRIBUTE_WORDS or token.text.lower() in STATE_ATTRIBUTE_WORDS
    return False


def _modifier_tokens(doc, head) -> list:
    modifiers = []
    for token in doc:
        if token.i == head.i:
            continue
        if token.head.i == head.i and (token.dep_ in MODIFIER_DEPS or token.pos_ in ATTRIBUTE_POS):
            modifiers.append(token)
        elif token.i < head.i and token.pos_ in {"ADJ", "NOUN", "PROPN", "NUM", "VERB"}:
            modifiers.append(token)
    return sorted({token.i: token for token in modifiers}.values(), key=lambda token: token.i)


def parse_tag_list(nlp, caption: str) -> TagListParseResult:
    segments = split_tag_segments(caption)
    noun_chunks: list[SegmentNounChunk] = []
    segment_tokens: list[SegmentToken] = []
    mentions: list[ConceptMention] = []
    edges: list[ConceptEdge] = []
    previous_object_ids: list[str] = []

    def add_mention(
        concept_type: str,
        text: str,
        lemma: str,
        source_tag: str,
        source_token_i: int | None,
        role: str,
        confidence: str,
    ) -> str:
        mention_id = f"m{len(mentions)}"
        mentions.append(
            ConceptMention(
                mention_id=mention_id,
                concept_type=concept_type,
                text=text,
                lemma=lemma,
                source_tag=source_tag,
                source_token_i=source_token_i,
                role=role,
                confidence=confidence,
            )
        )
        return mention_id

    def add_edge(edge_type: str, source: str, target: str, confidence: str, evidence: str) -> None:
        edges.append(
            ConceptEdge(
                edge_id=f"e{len(edges)}",
                edge_type=edge_type,
                source=source,
                target=target,
                confidence=confidence,
                evidence=evidence,
            )
        )

    for segment in segments:
        doc = nlp(segment.raw)
        for chunk in doc.noun_chunks:
            root = chunk.root
            noun_chunks.append(
                SegmentNounChunk(
                    tag_id=segment.tag_id,
                    chunk=chunk.text,
                    root=root.text,
                    root_lemma=root.lemma_,
                    root_dep=root.dep_,
                    root_head=root.head.text,
                    token_start=chunk.start,
                    token_end=chunk.end,
                    char_start=segment.char_start + chunk.start_char,
                    char_end=segment.char_start + chunk.end_char,
                )
            )
        for token in doc:
            segment_tokens.append(
                SegmentToken(
                    tag_id=segment.tag_id,
                    i=token.i,
                    text=token.text,
                    lemma=token.lemma_,
                    pos=token.pos_,
                    tag=token.tag_,
                    dep=token.dep_,
                    head=token.head.text,
                    head_i=token.head.i,
                    char_start=segment.char_start + token.idx,
                    char_end=segment.char_start + token.idx + len(token.text),
                )
            )

        if not len(doc):
            continue

        if _is_context_segment(doc, segment):
            token = doc[0]
            context_id = add_mention(
                "context",
                token.text,
                token.lemma_,
                segment.tag_id,
                token.i,
                "scene_context",
                "high",
            )
            add_edge("has_context", "scene", context_id, "high", f"{segment.tag_id} context tag")
            continue

        if _is_floating_attribute(doc):
            token = doc[0]
            attr_id = add_mention(
                "attribute",
                token.text,
                token.lemma_,
                segment.tag_id,
                token.i,
                "floating_attribute",
                "medium",
            )
            if previous_object_ids:
                add_edge(
                    "candidate_has_attribute",
                    previous_object_ids[-1],
                    attr_id,
                    "low",
                    f"{segment.tag_id} adjacent floating attribute",
                )
            continue

        head = _object_head(doc)
        if head is not None:
            head_is_object_pos = head.pos_ in OBJECT_POS
            object_id = add_mention(
                "object",
                head.text,
                head.lemma_,
                segment.tag_id,
                head.i,
                "segment_head" if head_is_object_pos else "ambiguous_segment_head",
                "high" if head_is_object_pos else "medium",
            )
            previous_object_ids.append(object_id)
            for modifier in _modifier_tokens(doc, head):
                role = "attribute"
                if modifier.tag_ in {"VBG", "VBN"}:
                    role = "state_attribute"
                attr_id = add_mention(
                    "attribute",
                    modifier.text,
                    modifier.lemma_,
                    segment.tag_id,
                    modifier.i,
                    role,
                    "high",
                )
                add_edge(
                    "has_attribute",
                    object_id,
                    attr_id,
                    "high",
                    f"{segment.tag_id} internal {modifier.dep_} -> {head.text}",
                )
            continue

        root = _root_token(doc)
        if root is not None:
            add_mention(
                "unknown",
                root.text,
                root.lemma_,
                segment.tag_id,
                root.i,
                "unclassified_segment_root",
                "low",
            )

    return TagListParseResult(
        segments=segments,
        noun_chunks=noun_chunks,
        tokens=segment_tokens,
        concept_mentions=mentions,
        edges=edges,
    )


def is_tag_list_row(row: dict, caption: str) -> bool:
    if row.get("caption_type") == "tag":
        return True
    comma_count = caption.count(",")
    sentence_marks = sum(caption.count(mark) for mark in ".!?")
    return comma_count >= 2 and sentence_marks == 0
