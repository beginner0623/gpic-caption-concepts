from __future__ import annotations


SAFE_SCENE_CONTEXT_HEADS = {
    "background",
    "foreground",
    "scene",
    "setting",
    "distance",
    "indoors",
    "outdoors",
    "dusk",
    "dawn",
}

SOFT_SCENE_CONTEXT_HEADS = {
    "day",
    "daytime",
    "evening",
    "indoor",
    "morning",
    "night",
    "nighttime",
    "outdoor",
    "sunset",
}

SCENE_CONTEXT_HEADS = SAFE_SCENE_CONTEXT_HEADS | SOFT_SCENE_CONTEXT_HEADS

LOCATIVE_CONTEXT_PREPS = {
    "against",
    "around",
    "at",
    "beyond",
    "during",
    "in",
    "inside",
    "near",
    "on",
    "outside",
    "throughout",
    "under",
    "with",
}

CONTEXT_LINKING_VERBS = {
    "appear",
    "be",
    "look",
    "remain",
    "seem",
    "show",
}

CONTEXTUAL_HEAD_DEPS = {"ROOT", "advmod", "attr", "dobj", "nsubj", "npadvmod", "obj", "pobj"}
NON_CONTEXT_MODIFIER_DEPS = {"amod", "compound", "det", "poss"}


def is_scene_context_lemma(lemma: str) -> bool:
    return lemma.lower() in SCENE_CONTEXT_HEADS


def scene_context_role(token) -> tuple[str, str] | None:
    """Return (role, confidence) when a token is a scene-level context cue."""
    lemma = token.lemma_.lower()
    if lemma not in SCENE_CONTEXT_HEADS:
        return None
    if token.dep_ in NON_CONTEXT_MODIFIER_DEPS:
        return None
    if lemma in SAFE_SCENE_CONTEXT_HEADS and token.dep_ in CONTEXTUAL_HEAD_DEPS:
        return "scene_context", "high"
    if not _has_scene_context_syntax(token):
        return None
    if lemma in SAFE_SCENE_CONTEXT_HEADS:
        return "scene_context", "high"
    return "scene_context", "medium"


def _has_scene_context_syntax(token) -> bool:
    if token.dep_ not in CONTEXTUAL_HEAD_DEPS:
        return False
    if token.dep_ in {"pobj", "npadvmod"}:
        return token.head.lemma_.lower() in LOCATIVE_CONTEXT_PREPS
    if token.dep_ in {"dobj", "obj"}:
        return token.head.lemma_.lower() in CONTEXT_LINKING_VERBS
    if token.dep_ in {"attr", "nsubj"}:
        return token.head.lemma_.lower() in CONTEXT_LINKING_VERBS or token.head.pos_ == "AUX"
    return True
