from __future__ import annotations

import re


EXACT_QUANTITY_WORDS = {
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
}

APPROXIMATE_QUANTITY_WORDS = {
    "few",
    "many",
    "multiple",
    "numerous",
    "several",
    "various",
}

INDEFINITE_QUANTITY_WORDS = {
    "any",
    "some",
}

GROUP_QUANTITY_WORDS = {
    "all",
    "both",
}

DISTRIBUTIVE_QUANTITY_WORDS = {
    "each",
    "every",
}

ZERO_QUANTITY_WORDS = {
    "no",
    "none",
}

PARTITIVE_QUANTITY_WORDS = {
    "half",
    "most",
}

_DIGIT_RE = re.compile(r"^\d+(?:[.,]\d+)?$")


def token_norms(token) -> tuple[str, str]:
    text = token.text.lower()
    lemma = (token.lemma_ or token.text).lower()
    return lemma, text


def quantity_role(token) -> str | None:
    lemma, text = token_norms(token)
    if text in ZERO_QUANTITY_WORDS or lemma in ZERO_QUANTITY_WORDS:
        return "zero_quantity"
    if text in GROUP_QUANTITY_WORDS or lemma in GROUP_QUANTITY_WORDS:
        return "group_quantity"
    if text in DISTRIBUTIVE_QUANTITY_WORDS or lemma in DISTRIBUTIVE_QUANTITY_WORDS:
        return "distributive_quantity"
    if text in APPROXIMATE_QUANTITY_WORDS or lemma in APPROXIMATE_QUANTITY_WORDS:
        return "approximate_quantity"
    if text in INDEFINITE_QUANTITY_WORDS or lemma in INDEFINITE_QUANTITY_WORDS:
        return "indefinite_quantity"
    if text in PARTITIVE_QUANTITY_WORDS or lemma in PARTITIVE_QUANTITY_WORDS:
        return "partitive_quantity"
    if _DIGIT_RE.match(text):
        return "exact_quantity"
    if token.dep_ == "nummod" or token.pos_ == "NUM":
        return "exact_quantity"
    if text in EXACT_QUANTITY_WORDS or lemma in EXACT_QUANTITY_WORDS:
        return "exact_quantity"
    return None


def quantity_confidence(role: str) -> str:
    if role in {"exact_quantity", "zero_quantity", "group_quantity", "distributive_quantity"}:
        return "high"
    return "medium"
