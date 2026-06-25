from __future__ import annotations

from dataclasses import asdict, dataclass

from tag_list_parser import CONTEXT_TAGS, ConceptEdge, ConceptMention


OBJECT_POS = {"NOUN", "PROPN", "PRON"}
ACTION_POS = {"VERB"}
MODIFIER_DEPS = {"amod", "compound", "nummod", "poss", "acl", "advmod"}
SUBJECT_DEPS = {"nsubj", "nsubjpass"}
OBJECT_DEPS = {"dobj", "obj", "attr", "oprd", "pobj"}
SKIP_MODIFIER_DEPS = {"det", "punct", "case", "cc", "mark"}

COLOR_WORDS = {
    "black",
    "white",
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "brown",
    "gray",
    "grey",
    "silver",
    "gold",
    "golden",
    "tan",
    "beige",
    "navy",
    "teal",
    "turquoise",
    "violet",
    "maroon",
    "cyan",
    "magenta",
}

MATERIAL_WORDS = {
    "wood",
    "wooden",
    "glass",
    "metal",
    "metallic",
    "stone",
    "brick",
    "paper",
    "plastic",
    "ceramic",
    "concrete",
    "leather",
    "fabric",
    "cloth",
    "cotton",
    "denim",
    "wool",
    "fur",
    "steel",
    "iron",
}

SIZE_WORDS = {
    "large",
    "small",
    "big",
    "little",
    "tiny",
    "huge",
    "tall",
    "short",
    "long",
    "wide",
    "narrow",
    "giant",
    "miniature",
}

VISUAL_WORDS = {
    "bright",
    "dark",
    "light",
    "shiny",
    "old",
    "new",
    "dirty",
    "clean",
    "clear",
    "blurry",
    "bare",
    "arched",
    "paved",
}

SPATIAL_RELATIONS = {
    "above",
    "across",
    "against",
    "around",
    "behind",
    "below",
    "beneath",
    "beside",
    "between",
    "beyond",
    "in",
    "inside",
    "near",
    "next",
    "on",
    "outside",
    "over",
    "under",
    "underneath",
    "with",
}

MULTIWORD_RELATION_MIDS = {"top", "front", "back", "side", "middle", "center", "edge"}


@dataclass(frozen=True)
class RawConceptExtractionResult:
    concept_mentions: list[ConceptMention]
    edges: list[ConceptEdge]

    def to_dict(self) -> dict[str, object]:
        return {
            "concept_mentions": [mention.to_dict() for mention in self.concept_mentions],
            "edges": [edge.to_dict() for edge in self.edges],
        }


class RawConceptExtractor:
    def __init__(self, doc):
        self.doc = doc
        self.mentions: list[ConceptMention] = []
        self.edges: list[ConceptEdge] = []
        self.object_by_token_i: dict[int, str] = {}
        self.action_by_token_i: dict[int, str] = {}
        self.context_by_token_i: dict[int, str] = {}

    def run(self) -> RawConceptExtractionResult:
        self._extract_noun_chunk_objects()
        self._extract_contexts()
        self._extract_actions()
        self._extract_preposition_relations()
        self._extract_negations()
        return RawConceptExtractionResult(self.mentions, self.edges)

    def add_mention(
        self,
        concept_type: str,
        text: str,
        lemma: str,
        source_tag: str,
        source_token_i: int | None,
        role: str,
        confidence: str,
    ) -> str:
        mention_id = f"m{len(self.mentions)}"
        self.mentions.append(
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

    def add_edge(self, edge_type: str, source: str, target: str, confidence: str, evidence: str) -> None:
        self.edges.append(
            ConceptEdge(
                edge_id=f"e{len(self.edges)}",
                edge_type=edge_type,
                source=source,
                target=target,
                confidence=confidence,
                evidence=evidence,
            )
        )

    def _extract_noun_chunk_objects(self) -> None:
        for chunk_i, chunk in enumerate(self.doc.noun_chunks):
            root = chunk.root
            if root.pos_ not in OBJECT_POS and root.tag_ not in {"NN", "NNS", "NNP", "NNPS"}:
                continue
            if self._is_multiword_relation_mid_token(root):
                continue
            if self._is_spatial_region_anchor(root):
                self._ensure_spatial_region(root, f"chunk{chunk_i}")
                continue
            object_id = self._ensure_object(root, f"chunk{chunk_i}", "noun_chunk_root", "high")
            for token in chunk:
                if token.i == root.i or token.dep_ in SKIP_MODIFIER_DEPS:
                    continue
                if not self._looks_like_modifier(token):
                    continue
                modifier_id, edge_type, modifier_confidence = self._add_modifier(token, f"chunk{chunk_i}")
                self.add_edge(
                    edge_type,
                    object_id,
                    modifier_id,
                    modifier_confidence,
                    f"chunk{chunk_i} {token.dep_} -> {root.text}",
                )

    def _extract_contexts(self) -> None:
        for token in self.doc:
            lemma = token.lemma_.lower()
            if lemma not in CONTEXT_TAGS:
                continue
            if token.i in self.context_by_token_i:
                continue
            context_id = self.add_mention(
                "context",
                token.text,
                lemma,
                "doc",
                token.i,
                "context_word",
                "medium",
            )
            self.context_by_token_i[token.i] = context_id
            self.add_edge("has_context", "scene", context_id, "medium", f"context token {token.text}")

    def _extract_actions(self) -> None:
        for token in self.doc:
            if token.pos_ not in ACTION_POS or token.dep_ in {"aux", "amod"}:
                continue
            action_id = self.add_mention(
                "action",
                token.text,
                token.lemma_.lower(),
                "doc",
                token.i,
                "verb_predicate",
                "high",
            )
            self.action_by_token_i[token.i] = action_id

            for child in token.children:
                if child.dep_ in SUBJECT_DEPS:
                    for subject in self._expand_conjunct_targets(child):
                        object_id = self._object_for_token(subject, "verb_subject", "medium")
                        if object_id:
                            self.add_edge(
                                "agent",
                                action_id,
                                object_id,
                                "medium",
                                f"{child.dep_} -> {token.text}",
                            )
                elif child.dep_ in OBJECT_DEPS:
                    for object_token in self._expand_conjunct_targets(child):
                        object_id = self._object_for_token(object_token, "verb_object", "medium")
                        if object_id:
                            self.add_edge(
                                "patient",
                                action_id,
                                object_id,
                                "medium",
                                f"{child.dep_} -> {token.text}",
                            )

    def _extract_preposition_relations(self) -> None:
        for prep in self.doc:
            if prep.pos_ != "ADP" and prep.dep_ != "prep":
                continue
            relation = prep.lemma_.lower()
            if self._is_inner_multiword_prep(prep):
                relation = self._multiword_relation_name(prep)
                source = self._relation_source(prep.head.head.head)
            else:
                if self._has_multiword_relation_child(prep):
                    continue
                source = self._relation_source(prep.head)

            target_token = self._preposition_object(prep)
            if source is None or target_token is None:
                continue
            confidence = "high" if relation in SPATIAL_RELATIONS or "_" in relation else "medium"
            for expanded_target in self._expand_conjunct_targets(target_token):
                target = self._object_for_token(expanded_target, "prep_object", "medium")
                if target is None:
                    continue
                self.add_edge(
                    "relation",
                    source,
                    target,
                    confidence,
                    relation,
                )

    def _extract_negations(self) -> None:
        for token in self.doc:
            if token.dep_ != "neg":
                continue
            target = None
            if token.head.i in self.action_by_token_i:
                target = self.action_by_token_i[token.head.i]
            elif token.head.i in self.object_by_token_i:
                target = self.object_by_token_i[token.head.i]
            if target is None:
                continue
            neg_id = self.add_mention(
                "negation",
                token.text,
                token.lemma_.lower(),
                "doc",
                token.i,
                "negation_cue",
                "high",
            )
            self.add_edge("negates", neg_id, target, "high", f"neg -> {token.head.text}")

    def _ensure_object(self, token, source_tag: str, role: str, confidence: str) -> str:
        if token.i in self.object_by_token_i:
            return self.object_by_token_i[token.i]
        if token.pos_ == "PROPN" and token.text.islower():
            role = "lowercase_propn_as_object"
            confidence = "medium"
        object_id = self.add_mention(
            "object",
            token.text,
            token.lemma_.lower(),
            source_tag,
            token.i,
            role,
            confidence,
        )
        self.object_by_token_i[token.i] = object_id
        return object_id

    def _object_for_token(self, token, role: str, confidence: str) -> str | None:
        if token.i in self.context_by_token_i:
            return self.context_by_token_i[token.i]
        if token.i in self.object_by_token_i:
            return self.object_by_token_i[token.i]
        for chunk in self.doc.noun_chunks:
            if chunk.start <= token.i < chunk.end:
                return self._ensure_object(chunk.root, "doc", role, confidence)
        if token.pos_ in OBJECT_POS or token.tag_ in {"NN", "NNS", "NNP", "NNPS"}:
            return self._ensure_object(token, "doc", role, confidence)
        return None

    def _relation_source(self, head) -> str | None:
        if head.pos_ in ACTION_POS or head.pos_ == "AUX":
            subject = self._verb_subject(head)
            if subject is not None:
                return self._object_for_token(subject, "relation_subject", "medium")
            if head.dep_ in {"acl", "advcl", "xcomp", "ccomp", "conj"} and head.head is not head:
                if head.head.pos_ in OBJECT_POS:
                    return self._object_for_token(head.head, "relation_head", "medium")
                parent_subject = self._verb_subject(head.head)
                if parent_subject is not None:
                    return self._object_for_token(parent_subject, "relation_subject", "medium")
        return self._object_for_token(head, "relation_head", "medium")

    def _verb_subject(self, verb):
        for child in verb.children:
            if child.dep_ in SUBJECT_DEPS:
                return child
        return None

    def _preposition_object(self, prep):
        for child in prep.children:
            if child.dep_ in {"pobj", "pcomp"}:
                return child
        return None

    def _expand_conjunct_targets(self, token) -> list:
        targets = [token]
        for child in token.children:
            if child.dep_ == "conj":
                targets.extend(self._expand_conjunct_targets(child))
        return sorted({target.i: target for target in targets}.values(), key=lambda item: item.i)

    def _has_multiword_relation_child(self, prep) -> bool:
        for child in prep.children:
            if child.lemma_.lower() in MULTIWORD_RELATION_MIDS:
                return any(grandchild.dep_ == "prep" and grandchild.lower_ == "of" for grandchild in child.children)
        return False

    def _is_inner_multiword_prep(self, prep) -> bool:
        return (
            prep.lower_ == "of"
            and prep.dep_ == "prep"
            and prep.head.lemma_.lower() in MULTIWORD_RELATION_MIDS
            and prep.head.head.pos_ == "ADP"
        )

    def _is_multiword_relation_mid_token(self, token) -> bool:
        return (
            token.lemma_.lower() in MULTIWORD_RELATION_MIDS
            and token.head.pos_ == "ADP"
            and any(child.dep_ == "prep" and child.lower_ == "of" for child in token.children)
        )

    def _is_spatial_region_anchor(self, token) -> bool:
        return token.lemma_.lower() in MULTIWORD_RELATION_MIDS and token.head.pos_ == "ADP"

    def _ensure_spatial_region(self, token, source_tag: str) -> str:
        if token.i in self.context_by_token_i:
            return self.context_by_token_i[token.i]
        context_id = self.add_mention(
            "context",
            token.text,
            token.lemma_.lower(),
            source_tag,
            token.i,
            "spatial_region",
            "medium",
        )
        self.context_by_token_i[token.i] = context_id
        return context_id

    def _multiword_relation_name(self, prep) -> str:
        first = prep.head.head.lower_
        middle = prep.head.lemma_.lower()
        return f"{first}_{middle}_of"

    def _looks_like_modifier(self, token) -> bool:
        if token.pos_ in {"ADJ", "ADV", "NUM"}:
            return True
        if token.dep_ in MODIFIER_DEPS:
            return True
        lemma = token.lemma_.lower()
        return lemma in COLOR_WORDS or lemma in MATERIAL_WORDS or lemma in SIZE_WORDS or lemma in VISUAL_WORDS

    def _add_modifier(self, token, source_tag: str) -> tuple[str, str, str]:
        lemma = token.lemma_.lower()
        if token.dep_ == "nummod" or token.pos_ == "NUM":
            role = "quantity"
            concept_type = "quantity"
            edge_type = "has_quantity"
            confidence = "high"
        elif lemma in COLOR_WORDS:
            role = "color_attribute"
            concept_type = "attribute"
            edge_type = "has_attribute"
            confidence = "high"
        elif lemma in MATERIAL_WORDS:
            role = "material_attribute"
            concept_type = "attribute"
            edge_type = "has_attribute"
            confidence = "high"
        elif lemma in SIZE_WORDS:
            role = "size_attribute"
            concept_type = "attribute"
            edge_type = "has_attribute"
            confidence = "high"
        elif lemma in VISUAL_WORDS:
            role = "visual_attribute"
            concept_type = "attribute"
            edge_type = "has_attribute"
            confidence = "medium"
        elif token.dep_ == "compound":
            role = "compound_modifier"
            concept_type = "attribute"
            edge_type = "has_attribute"
            confidence = "medium"
        elif token.tag_ in {"VBG", "VBN"}:
            role = "state_attribute"
            concept_type = "attribute"
            edge_type = "has_attribute"
            confidence = "medium"
        else:
            role = "modifier_attribute"
            concept_type = "attribute"
            edge_type = "has_attribute"
            confidence = "medium"
        mention_id = self.add_mention(
            concept_type,
            token.text,
            lemma,
            source_tag,
            token.i,
            role,
            confidence,
        )
        return mention_id, edge_type, confidence


def extract_raw_concepts(doc) -> RawConceptExtractionResult:
    return RawConceptExtractor(doc).run()
