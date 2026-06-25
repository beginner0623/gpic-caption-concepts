from __future__ import annotations

import csv
from pathlib import Path

from spacy.language import Language
from spacy.matcher import PhraseMatcher
from spacy.tokens import Doc, Token
from spacy.util import filter_spans

from quote_retokenizer import RAW_QUOTE_MERGER


OBJECT_MWE_MERGER = "object_mwe_merger"
OBJECT_MWE_POS_CORRECTOR = "object_mwe_pos_corrector"
DEFAULT_OBJECT_MWE_LEXICON = Path("resources/lexicons/object_noun_mwe_clean_core.tsv")
OBJECT_MWE_FLAG = "is_object_mwe"
OBJECT_MWE_CANONICAL = "object_mwe_canonical"


def ensure_token_extensions() -> None:
    if not Token.has_extension(OBJECT_MWE_FLAG):
        Token.set_extension(OBJECT_MWE_FLAG, default=False)
    if not Token.has_extension(OBJECT_MWE_CANONICAL):
        Token.set_extension(OBJECT_MWE_CANONICAL, default=None)


def load_object_mwe_lexicon(path: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            term = row.get("term", "").strip().lower()
            canonical = row.get("canonical", "").strip()
            if not term or (" " not in term and "-" not in term):
                continue
            entries[term] = canonical or term.replace(" ", "_")
    return entries


class ObjectMweMerger:
    def __init__(self, nlp: Language, lexicon_path: str) -> None:
        ensure_token_extensions()
        self.lexicon_path = Path(lexicon_path)
        self.entries = load_object_mwe_lexicon(self.lexicon_path)
        self.matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
        patterns = [nlp.make_doc(term) for term in sorted(self.entries, key=lambda item: (len(item.split()), item))]
        if patterns:
            self.matcher.add("OBJECT_NOUN_MWE", patterns)

    def __call__(self, doc: Doc) -> Doc:
        matches = self.matcher(doc)
        spans = filter_spans([doc[start:end] for _, start, end in matches])
        if not spans:
            return doc

        with doc.retokenize() as retokenizer:
            for span in spans:
                key = span.text.lower()
                canonical = self.entries.get(key, key.replace(" ", "_"))
                retokenizer.merge(
                    span,
                    attrs={
                        "LEMMA": canonical,
                        "_": {
                            OBJECT_MWE_FLAG: True,
                            OBJECT_MWE_CANONICAL: canonical,
                        },
                    },
                )
        return doc


class ObjectMwePosCorrector:
    def __init__(self, nlp: Language) -> None:
        ensure_token_extensions()
        self.noun_pos = nlp.vocab.strings["NOUN"]
        self.nn_tag = nlp.vocab.strings["NN"]

    def __call__(self, doc: Doc) -> Doc:
        for token in doc:
            if not token._.get(OBJECT_MWE_FLAG):
                continue
            token.pos = self.noun_pos
            token.tag = self.nn_tag
            canonical = token._.get(OBJECT_MWE_CANONICAL)
            if canonical:
                token.lemma_ = canonical
        return doc


@Language.factory(
    OBJECT_MWE_MERGER,
    default_config={"lexicon_path": str(DEFAULT_OBJECT_MWE_LEXICON)},
)
def create_object_mwe_merger(nlp: Language, name: str, lexicon_path: str) -> ObjectMweMerger:
    return ObjectMweMerger(nlp, lexicon_path)


@Language.factory(OBJECT_MWE_POS_CORRECTOR)
def create_object_mwe_pos_corrector(nlp: Language, name: str) -> ObjectMwePosCorrector:
    return ObjectMwePosCorrector(nlp)


def ensure_object_mwe_merger(
    nlp: Language,
    lexicon_path: Path = DEFAULT_OBJECT_MWE_LEXICON,
) -> Language:
    if OBJECT_MWE_MERGER in nlp.pipe_names:
        return nlp
    config = {"lexicon_path": str(lexicon_path)}
    if RAW_QUOTE_MERGER in nlp.pipe_names:
        nlp.add_pipe(OBJECT_MWE_MERGER, after=RAW_QUOTE_MERGER, config=config)
    else:
        nlp.add_pipe(OBJECT_MWE_MERGER, first=True, config=config)
    if OBJECT_MWE_POS_CORRECTOR not in nlp.pipe_names:
        if "tagger" in nlp.pipe_names:
            nlp.add_pipe(OBJECT_MWE_POS_CORRECTOR, after="tagger")
        elif "morphologizer" in nlp.pipe_names:
            nlp.add_pipe(OBJECT_MWE_POS_CORRECTOR, after="morphologizer")
        elif "parser" in nlp.pipe_names:
            nlp.add_pipe(OBJECT_MWE_POS_CORRECTOR, before="parser")
        else:
            nlp.add_pipe(OBJECT_MWE_POS_CORRECTOR, last=True)
    return nlp
