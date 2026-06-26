from __future__ import annotations


SINGULAR_SUBSTITUTE_WORDS = {"one", "ones"}
CONTRASTIVE_REFERENCE_WORDS = {"another", "other", "others"}
GROUP_REFERENCE_WORDS = {"all", "both"}
DISTRIBUTIVE_REFERENCE_WORDS = {"each", "every"}

REFERENCE_CLASS_BY_WORD = {
    **{word: "singular_substitute" for word in SINGULAR_SUBSTITUTE_WORDS},
    **{word: "contrastive_reference" for word in CONTRASTIVE_REFERENCE_WORDS},
    **{word: "group_reference" for word in GROUP_REFERENCE_WORDS},
    **{word: "distributive_reference" for word in DISTRIBUTIVE_REFERENCE_WORDS},
}

REFERENCE_MODIFIER_DEPS = {"amod", "det", "nummod"}
NOUNLIKE_POS = {"NOUN", "PROPN", "PRON"}
NOUNLIKE_TAGS = {"NN", "NNS", "NNP", "NNPS", "PRP"}
REFERENCE_ARGUMENT_DEPS = {
    "ROOT",
    "appos",
    "attr",
    "conj",
    "dep",
    "dobj",
    "nsubj",
    "nsubjpass",
    "obj",
    "oprd",
    "pobj",
}


def token_norm(token) -> str:
    return (token.lemma_ or token.text).lower()


def surface_norm(token) -> str:
    return token.text.lower()


def reference_class(token) -> str | None:
    lemma = token_norm(token)
    text = surface_norm(token)
    ref_class = REFERENCE_CLASS_BY_WORD.get(lemma) or REFERENCE_CLASS_BY_WORD.get(text)
    if ref_class is None:
        return None
    if _is_nominal_modifier(token):
        return None
    if token.dep_ in REFERENCE_ARGUMENT_DEPS:
        return ref_class
    if token.pos_ in NOUNLIKE_POS or token.tag_ in NOUNLIKE_TAGS:
        return ref_class
    return None


def is_reference_token(token) -> bool:
    return reference_class(token) is not None


def is_reference_word(value: str) -> bool:
    return value.lower() in REFERENCE_CLASS_BY_WORD


def _is_nominal_modifier(token) -> bool:
    if token.dep_ not in REFERENCE_MODIFIER_DEPS:
        return False
    if token.head.i == token.i:
        return False
    return token.head.pos_ in {"NOUN", "PROPN"} or token.head.tag_ in {"NN", "NNS", "NNP", "NNPS"}
