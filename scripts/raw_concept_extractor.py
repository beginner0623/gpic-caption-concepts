from __future__ import annotations

from dataclasses import asdict, dataclass

from preposition_mwe_lexicon import (
    PREPOSITION_MWE_MIDDLE_LEMMAS,
    PrepositionMweEntry,
    preposition_mwe_entry,
)
from quantity_lexicon import quantity_confidence, quantity_role
from quote_retokenizer import is_raw_quote_token
from reference_lexicon import reference_class
from tag_list_parser import CONTEXT_TAGS, ConceptEdge, ConceptMention


OBJECT_POS = {"NOUN", "PROPN"}
ACTION_POS = {"VERB"}
MODIFIER_DEPS = {"amod", "compound", "nummod", "poss", "acl", "advmod"}
SUBJECT_DEPS = {"nsubj", "nsubjpass"}
OBJECT_DEPS = {"dobj", "obj", "attr", "oprd", "pobj"}
SKIP_MODIFIER_DEPS = {"det", "punct", "case", "cc", "mark"}
AGENT_INHERITABLE_ACTION_DEPS = {"acl", "advcl", "xcomp", "ccomp", "conj", "relcl", "acomp"}
PREPOSITIONAL_AGENT_INHERITANCE_LEMMAS = {"include"}
WHOLE_AGENT_ACTION_LEMMAS = {"crawl", "fly", "glide", "jump", "leap", "run", "sit", "stand", "swim", "walk"}
BODY_PART_LEMMAS = {
    "arm",
    "back",
    "beak",
    "body",
    "chest",
    "ear",
    "eye",
    "face",
    "finger",
    "foot",
    "hand",
    "head",
    "leg",
    "mouth",
    "neck",
    "nose",
    "tail",
    "wing",
}

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

ROOT_ONLY_QUANTITY_ROLES = {
    "approximate_quantity",
    "distributive_quantity",
    "group_quantity",
    "indefinite_quantity",
    "partitive_quantity",
    "zero_quantity",
}
WITH_ABSOLUTE_CANDIDATE_DEPS = {"advcl", "conj", "dep", "nsubj", "nsubjpass"}
WITH_ABSOLUTE_MODIFIER_DEPS = {"acl", "amod", "compound", "nummod", "poss"}
WITH_ABSOLUTE_SKIP_DEPS = {"amod", "case", "cc", "compound", "det", "mark", "poss", "punct"}
PRONOUN_OBJECT_TAGS = {"PRP", "WP", "WP$", "WDT"}
POSSESSIVE_PRONOUN_TAGS = {"PRP$", "WP$"}
MALE_PERSON_LEMMAS = {"boy", "father", "gentleman", "guy", "he", "him", "man", "male"}
FEMALE_PERSON_LEMMAS = {"female", "girl", "her", "lady", "mother", "she", "woman"}
PERSON_LEMMAS = {
    "adult",
    "baby",
    "boy",
    "child",
    "girl",
    "kid",
    "man",
    "men",
    "people",
    "person",
    "player",
    "rider",
    "woman",
    "women",
} | MALE_PERSON_LEMMAS | FEMALE_PERSON_LEMMAS
MALE_PRONOUNS = {"he", "him", "his"}
FEMALE_PRONOUNS = {"her", "hers", "she"}
PLURAL_OR_GROUP_PRONOUNS = {"their", "theirs", "them", "they"}
NEUTRAL_PRONOUNS = {"it", "its", "itself", "that", "this"}
REFLEXIVE_PRONOUNS = {
    "herself",
    "himself",
    "itself",
    "myself",
    "ourselves",
    "themselves",
    "yourself",
    "yourselves",
}
PRONOUN_ANTECEDENT_MAX_DISTANCE = 80


@dataclass(frozen=True)
class RawConceptExtractionResult:
    concept_mentions: list[ConceptMention]
    edges: list[ConceptEdge]
    skipped_edges: list[dict[str, object]]

    def to_dict(self) -> dict[str, object]:
        return {
            "concept_mentions": [mention.to_dict() for mention in self.concept_mentions],
            "edges": [edge.to_dict() for edge in self.edges],
            "skipped_edges": self.skipped_edges,
        }


class RawConceptExtractor:
    def __init__(self, doc):
        self.doc = doc
        self.mentions: list[ConceptMention] = []
        self.edges: list[ConceptEdge] = []
        self.skipped_edges: list[dict[str, object]] = []
        self.object_by_token_i: dict[int, str] = {}
        self.action_by_token_i: dict[int, str] = {}
        self.context_by_token_i: dict[int, str] = {}
        self.quote_by_token_i: dict[int, str] = {}
        self.reference_object_by_token_i: dict[int, str] = {}

    def run(self) -> RawConceptExtractionResult:
        self._extract_quote_attributes()
        self._extract_noun_chunk_objects()
        self._extract_quote_carrier_edges()
        self._extract_contexts()
        self._resolve_reference_tokens()
        self._extract_actions()
        self._recover_with_absolute_objects()
        self._extract_preposition_relations()
        self._extract_negations()
        return RawConceptExtractionResult(self.mentions, self.edges, self.skipped_edges)

    def _extract_quote_attributes(self) -> None:
        for token in self.doc:
            if self._is_quote_token(token):
                self._ensure_quote_attribute(token, "doc_quote")

    def _extract_quote_carrier_edges(self) -> None:
        for token in self.doc:
            if not self._is_quote_token(token):
                continue
            quote_id = self._ensure_quote_attribute(token, "doc_quote")
            carrier_id = self._quote_carrier_object(token)
            if carrier_id is None or self._has_edge("has_attribute", carrier_id, quote_id):
                continue
            self.add_edge(
                "has_attribute",
                carrier_id,
                quote_id,
                "high",
                f"quote {token.dep_} -> {token.head.text}",
            )

    def _quote_carrier_object(self, token) -> str | None:
        if token.head is token:
            return None
        if token.dep_ not in {"appos", "nmod", "compound"}:
            return None
        if token.head.i in self.object_by_token_i:
            return self.object_by_token_i[token.head.i]
        for chunk in self.doc.noun_chunks:
            if chunk.start <= token.head.i < chunk.end and chunk.root.i in self.object_by_token_i:
                return self.object_by_token_i[chunk.root.i]
        return None

    def _has_edge(self, edge_type: str, source: str, target: str) -> bool:
        return any(
            edge.edge_type == edge_type and edge.source == source and edge.target == target
            for edge in self.edges
        )

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
        if edge_type == "relation" and source == target:
            self.skip_edge(edge_type, source, target, confidence, evidence, "self_edge_after_coref")
            return
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

    def skip_edge(
        self,
        edge_type: str,
        source: str,
        target: str,
        confidence: str,
        evidence: str,
        reason: str,
    ) -> None:
        self.skipped_edges.append(
            {
                "edge_type": edge_type,
                "source": source,
                "target": target,
                "confidence": confidence,
                "evidence": evidence,
                "reason": reason,
            }
        )

    def _extract_noun_chunk_objects(self) -> None:
        for chunk_i, chunk in enumerate(self.doc.noun_chunks):
            root = chunk.root
            root_quantity = quantity_role(root)
            if root_quantity in ROOT_ONLY_QUANTITY_ROLES:
                self._add_modifier(root, f"chunk{chunk_i}")
                continue
            if self._is_quote_token(root):
                self._ensure_quote_attribute(root, f"chunk{chunk_i}")
                continue
            if self._is_color_token(root) and not self._is_object_candidate_token(root):
                for token in chunk:
                    if self._is_color_token(token):
                        self._add_modifier(token, f"chunk{chunk_i}")
                continue
            if not self._is_object_candidate_token(root):
                continue
            if self._is_multiword_relation_mid_token(root):
                continue
            if self._is_spatial_region_anchor(root):
                self._ensure_spatial_region(root, f"chunk{chunk_i}")
                continue
            object_id = self._ensure_object(root, f"chunk{chunk_i}", "noun_chunk_root", "high")
            for token in chunk:
                if token.i == root.i or token.dep_ in SKIP_MODIFIER_DEPS:
                    if token.i == root.i:
                        continue
                    if quantity_role(token) is None:
                        continue
                if quantity_role(token) is not None:
                    modifier_id, edge_type, modifier_confidence = self._add_modifier(token, f"chunk{chunk_i}")
                    self.add_edge(
                        edge_type,
                        object_id,
                        modifier_id,
                        modifier_confidence,
                        f"chunk{chunk_i} quantity -> {root.text}",
                    )
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
            agent_added = False
            action_agent_ids: set[str] = set()
            patient_candidates: list[tuple[object, str, str]] = []

            for child in token.children:
                if child.dep_ in SUBJECT_DEPS:
                    for subject in self._expand_conjunct_targets(child):
                        object_id = self._object_for_token(subject, "verb_subject", "medium")
                        if object_id:
                            agent_added = True
                            action_agent_ids.add(object_id)
                            self.add_edge(
                                "agent",
                                action_id,
                                object_id,
                                "medium",
                                self._edge_evidence(f"{child.dep_} -> {token.text}", subject),
                            )
                elif child.dep_ in OBJECT_DEPS:
                    for object_token in self._expand_conjunct_targets(child):
                        object_id = self._object_for_token(object_token, "verb_object", "medium")
                        if object_id:
                            patient_candidates.append(
                                (
                                    object_token,
                                    object_id,
                                    self._edge_evidence(f"{child.dep_} -> {token.text}", object_token),
                                )
                            )

            if not agent_added:
                for subject in self._inherited_action_agent_tokens(token):
                    object_id = self._object_for_token(subject, "inherited_action_subject", "medium")
                    if object_id and not self._has_edge("agent", action_id, object_id):
                        action_agent_ids.add(object_id)
                        self.add_edge(
                            "agent",
                            action_id,
                            object_id,
                            "medium",
                            f"inherited agent {token.dep_} -> {token.head.text}",
                        )

            for object_token, object_id, evidence in patient_candidates:
                if self._is_self_resolved_action_target(object_token, action_agent_ids, object_id):
                    self.skip_edge(
                        "patient",
                        action_id,
                        object_id,
                        "medium",
                        evidence,
                        "pronoun_resolved_to_action_agent",
                    )
                    continue
                self.add_edge(
                    "patient",
                    action_id,
                    object_id,
                    "medium",
                    evidence,
                )

    def _extract_preposition_relations(self) -> None:
        for prep in self.doc:
            if prep.pos_ != "ADP" and prep.dep_ != "prep":
                continue
            relation = prep.lemma_.lower()
            mwe_entry = self._multiword_preposition_entry(prep)
            if mwe_entry is not None:
                relation = mwe_entry.canonical
                source = self._relation_source(self._multiword_preposition_source_head(prep))
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

    def _recover_with_absolute_objects(self) -> None:
        recovered: set[int] = set()
        for with_token in self.doc:
            if not self._is_with_absolute_cue(with_token):
                continue
            source_tag = f"with_absolute{with_token.i}"
            for token in self.doc[with_token.i + 1 : with_token.sent.end]:
                if token.text in {".", ";", ":", "!", "?"}:
                    break
                if token.i in recovered or not self._is_with_absolute_recovery_candidate(token):
                    continue
                recovered.add(token.i)
                object_id = self._ensure_object(
                    token,
                    source_tag,
                    "with_absolute_recovered_object",
                    "medium",
                )
                self.add_edge(
                    "scene_contains",
                    "scene",
                    object_id,
                    "medium",
                    f"{source_tag} recovered {token.text}",
                )
                self._add_recovered_object_modifiers(token, object_id, source_tag)

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

    def _is_with_absolute_cue(self, token) -> bool:
        return token.lower_ == "with" and token.tag_ == "IN" and token.dep_ == "mark"

    def _is_with_absolute_recovery_candidate(self, token) -> bool:
        if token.i in self.object_by_token_i or token.i in self.context_by_token_i:
            return False
        if token.dep_ not in WITH_ABSOLUTE_CANDIDATE_DEPS:
            return False
        if token.dep_ in WITH_ABSOLUTE_SKIP_DEPS:
            return False
        if not self._is_object_candidate_token(token):
            return False
        lemma = token.lemma_.lower()
        if lemma in CONTEXT_TAGS:
            return False
        if self._is_multiword_relation_mid_token(token) or self._is_spatial_region_anchor(token):
            return False
        return True

    def _add_recovered_object_modifiers(self, token, object_id: str, source_tag: str) -> None:
        for modifier in sorted(token.children, key=lambda child: child.i):
            if modifier.dep_ in SKIP_MODIFIER_DEPS:
                if quantity_role(modifier) is None:
                    continue
            if quantity_role(modifier) is not None:
                modifier_id, edge_type, modifier_confidence = self._add_modifier(modifier, source_tag)
                self.add_edge(
                    edge_type,
                    object_id,
                    modifier_id,
                    modifier_confidence,
                    f"{source_tag} quantity -> {token.text}",
                )
                continue
            if modifier.dep_ not in WITH_ABSOLUTE_MODIFIER_DEPS:
                continue
            if not self._looks_like_modifier(modifier):
                continue
            modifier_id, edge_type, modifier_confidence = self._add_modifier(modifier, source_tag)
            self.add_edge(
                edge_type,
                object_id,
                modifier_id,
                modifier_confidence,
                f"{source_tag} {modifier.dep_} -> {token.text}",
            )

    def _ensure_object(self, token, source_tag: str, role: str, confidence: str) -> str:
        if token.i in self.object_by_token_i:
            return self.object_by_token_i[token.i]
        if not self._is_object_candidate_token(token):
            return None
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

    def _ensure_quote_attribute(self, token, source_tag: str, confidence: str = "high") -> str:
        if token.i in self.quote_by_token_i:
            return self.quote_by_token_i[token.i]
        quote_id = self.add_mention(
            "attribute",
            token.text,
            token.lemma_.lower(),
            source_tag,
            token.i,
            "quote_text",
            confidence,
        )
        self.quote_by_token_i[token.i] = quote_id
        return quote_id

    def _object_for_token(self, token, role: str, confidence: str) -> str | None:
        if token.i in self.reference_object_by_token_i:
            return self.reference_object_by_token_i[token.i]
        if self._is_quote_token(token):
            return self._ensure_quote_attribute(token, "doc")
        if quantity_role(token) in ROOT_ONLY_QUANTITY_ROLES:
            return None
        if token.i in self.context_by_token_i:
            return self.context_by_token_i[token.i]
        if token.i in self.object_by_token_i:
            return self.object_by_token_i[token.i]
        for chunk in self.doc.noun_chunks:
            if chunk.start <= token.i < chunk.end:
                if self._is_quote_token(chunk.root):
                    return self._ensure_quote_attribute(chunk.root, "doc")
                if not self._is_object_candidate_token(chunk.root):
                    return None
                return self._ensure_object(chunk.root, "doc", role, confidence)
        if self._is_object_candidate_token(token):
            return self._ensure_object(token, "doc", role, confidence)
        return None

    def _resolve_reference_tokens(self) -> None:
        for token in self.doc:
            if not self._is_reference_token_for_rewiring(token):
                continue
            object_id = self._relative_reference_object(token)
            if object_id is None:
                object_id = self._personal_reference_object(token)
            if object_id is not None:
                self.reference_object_by_token_i[token.i] = object_id

    def _is_reference_token_for_rewiring(self, token) -> bool:
        if token.dep_ in {"det", "case", "mark", "punct", "cc"}:
            return False
        if reference_class(token) is not None:
            return False
        if token.pos_ == "PRON" or token.tag_ in PRONOUN_OBJECT_TAGS or token.tag_ in POSSESSIVE_PRONOUN_TAGS:
            return True
        return False

    def _relative_reference_object(self, token) -> str | None:
        if token.tag_ not in {"WDT", "WP", "WP$"} and token.lemma_.lower() not in {"that", "which", "who", "whom", "whose"}:
            return None
        head = token.head
        if head is token or head.dep_ != "relcl":
            return None
        antecedent = head.head
        if antecedent is head:
            return None
        return self._existing_object_for_token(antecedent)

    def _personal_reference_object(self, token) -> str | None:
        pronoun = self._pronoun_key(token)
        if pronoun is None:
            return None
        best: tuple[int, int, str] | None = None
        for token_i, object_id in self.object_by_token_i.items():
            if token_i >= token.i:
                continue
            distance = token.i - token_i
            if distance > PRONOUN_ANTECEDENT_MAX_DISTANCE:
                continue
            candidate = self.doc[token_i]
            score = self._antecedent_score(token, candidate, distance)
            if score < 30:
                continue
            item = (score, token_i, object_id)
            if best is None or item[0] > best[0] or (item[0] == best[0] and item[1] > best[1]):
                best = item
        return best[2] if best is not None else None

    def _antecedent_score(self, pronoun_token, candidate, distance: int) -> int:
        pronoun = self._pronoun_key(pronoun_token)
        candidate_lemma = candidate.lemma_.lower()
        candidate_is_person = self._is_person_candidate(candidate)
        score = max(0, 40 - distance)

        if self._is_nonreflexive_self_resolution_candidate(pronoun_token, candidate):
            score -= 100

        if self._pronoun_controls_whole_agent_action(pronoun_token) and self._is_body_part_candidate(candidate):
            score -= 100

        if candidate.dep_ in SUBJECT_DEPS:
            score += 35
        elif candidate.dep_ in {"dobj", "obj", "pobj"}:
            score += 8

        if candidate_is_person:
            score += 45

        if pronoun in MALE_PRONOUNS:
            if candidate_lemma in MALE_PERSON_LEMMAS:
                score += 45
            elif candidate_lemma in FEMALE_PERSON_LEMMAS:
                score -= 80
            elif not candidate_is_person:
                score -= 45
        elif pronoun in FEMALE_PRONOUNS:
            if candidate_lemma in FEMALE_PERSON_LEMMAS:
                score += 45
            elif candidate_lemma in MALE_PERSON_LEMMAS:
                score -= 80
            elif not candidate_is_person:
                score -= 45
        elif pronoun in PLURAL_OR_GROUP_PRONOUNS:
            if candidate_is_person:
                score += 45
            elif self._is_plural_like(candidate):
                score += 10
        elif pronoun in NEUTRAL_PRONOUNS:
            if not candidate_is_person:
                score += 25
            else:
                score -= 25

        if self._sent_index(candidate) == self._sent_index(pronoun_token):
            score += 5
        elif self._sent_index(candidate) == self._sent_index(pronoun_token) - 1:
            score += 15

        if candidate_lemma in CONTEXT_TAGS:
            score -= 60
        return score

    def _is_person_candidate(self, token) -> bool:
        lemma = token.lemma_.lower()
        if lemma in PERSON_LEMMAS:
            return True
        return any(part in PERSON_LEMMAS for part in lemma.replace("-", "_").split("_"))

    def _is_body_part_candidate(self, token) -> bool:
        lemma = token.lemma_.lower()
        if lemma in BODY_PART_LEMMAS:
            return True
        return any(part in BODY_PART_LEMMAS for part in lemma.replace("-", "_").split("_"))

    def _pronoun_controls_whole_agent_action(self, token) -> bool:
        return token.dep_ in SUBJECT_DEPS and token.head.lemma_.lower() in WHOLE_AGENT_ACTION_LEMMAS

    def _is_nonreflexive_self_resolution_candidate(self, pronoun_token, candidate) -> bool:
        if pronoun_token.lower_ in REFLEXIVE_PRONOUNS or pronoun_token.lemma_.lower() in REFLEXIVE_PRONOUNS:
            return False
        if pronoun_token.dep_ not in OBJECT_DEPS:
            return False
        head = pronoun_token.head
        if head is pronoun_token or head.pos_ not in ACTION_POS:
            return False
        return any(subject.i == candidate.i for subject in self._verb_subjects(head))

    def _existing_object_for_token(self, token) -> str | None:
        if token.i in self.object_by_token_i:
            return self.object_by_token_i[token.i]
        for chunk in self.doc.noun_chunks:
            if chunk.start <= token.i < chunk.end and chunk.root.i in self.object_by_token_i:
                return self.object_by_token_i[chunk.root.i]
        return None

    def _pronoun_key(self, token) -> str | None:
        lower = token.lower_
        lemma = token.lemma_.lower()
        if lower in MALE_PRONOUNS | FEMALE_PRONOUNS | PLURAL_OR_GROUP_PRONOUNS | NEUTRAL_PRONOUNS:
            return lower
        if lemma in MALE_PRONOUNS | FEMALE_PRONOUNS | PLURAL_OR_GROUP_PRONOUNS | NEUTRAL_PRONOUNS:
            return lemma
        return None

    def _is_plural_like(self, token) -> bool:
        if "Plur" in token.morph.get("Number"):
            return True
        return token.tag_ in {"NNS", "NNPS"} or token.lemma_.lower() in {"men", "people", "women", "children"}

    def _sent_index(self, token) -> int:
        for sent_i, sent in enumerate(self.doc.sents):
            if sent.start <= token.i < sent.end:
                return sent_i
        return 0

    def _edge_evidence(self, base: str, token) -> str:
        if token.i not in self.reference_object_by_token_i:
            return base
        target_text = self._mention_text(self.reference_object_by_token_i[token.i])
        return f"{base}; resolved {token.text} -> {target_text}"

    def _is_self_resolved_action_target(self, token, action_agent_ids: set[str], object_id: str) -> bool:
        if object_id not in action_agent_ids:
            return False
        if token.i not in self.reference_object_by_token_i:
            return False
        return token.lower_ not in REFLEXIVE_PRONOUNS and token.lemma_.lower() not in REFLEXIVE_PRONOUNS

    def _mention_text(self, mention_id: str) -> str:
        for mention in self.mentions:
            if mention.mention_id == mention_id:
                return mention.text
        return mention_id

    def _relation_source(self, head) -> str | None:
        if head.pos_ in ACTION_POS or head.pos_ == "AUX":
            subject = self._verb_subject(head)
            if subject is not None:
                return self._object_for_token(subject, "relation_subject", "medium")
            if head.dep_ in {"acl", "advcl", "xcomp", "ccomp", "conj"} and head.head is not head:
                if self._is_object_candidate_token(head.head):
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

    def _verb_subjects(self, verb) -> list:
        return [child for child in verb.children if child.dep_ in SUBJECT_DEPS]

    def _inherited_action_agent_tokens(self, token, seen: set[int] | None = None) -> list:
        if seen is None:
            seen = set()
        if token.i in seen:
            return []
        seen.add(token.i)

        if not self._allows_agent_inheritance(token):
            return []

        if token.dep_ in {"acl", "relcl"} and token.head is not token:
            return [token.head]

        if token.dep_ == "prep" and token.lemma_.lower() in PREPOSITIONAL_AGENT_INHERITANCE_LEMMAS:
            return [token.head] if token.head is not token else []

        head = token.head
        if head is token:
            return []

        if head.pos_ in ACTION_POS or head.pos_ == "AUX":
            subjects = []
            for subject in self._verb_subjects(head):
                subjects.extend(self._expand_conjunct_targets(subject))
            if subjects:
                return subjects
            return self._inherited_action_agent_tokens(head, seen)

        if token.dep_ == "conj" and head.head is not head:
            return self._inherited_action_agent_tokens(head, seen)

        return []

    def _allows_agent_inheritance(self, token) -> bool:
        if token.dep_ in AGENT_INHERITABLE_ACTION_DEPS:
            return True
        if token.dep_ == "prep" and token.lemma_.lower() in PREPOSITIONAL_AGENT_INHERITANCE_LEMMAS:
            return True
        return token.tag_ in {"VBG", "VBN"} and token.dep_ != "ROOT"

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
            for grandchild in child.children:
                if grandchild.dep_ == "prep" and self._multiword_preposition_entry(grandchild) is not None:
                    return True
        return False

    def _is_inner_multiword_prep(self, prep) -> bool:
        return self._multiword_preposition_entry(prep) is not None

    def _is_multiword_relation_mid_token(self, token) -> bool:
        return any(
            child.dep_ == "prep" and self._multiword_preposition_entry(child) is not None
            for child in token.children
        )

    def _is_spatial_region_anchor(self, token) -> bool:
        return token.lemma_.lower() in PREPOSITION_MWE_MIDDLE_LEMMAS and token.head.pos_ == "ADP"

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
        entry = self._multiword_preposition_entry(prep)
        if entry is not None:
            return entry.canonical
        return prep.lemma_.lower()

    def _multiword_preposition_entry(self, prep) -> PrepositionMweEntry | None:
        candidates = self._multiword_preposition_candidates(prep)
        for candidate in candidates:
            entry = preposition_mwe_entry(candidate)
            if entry is not None:
                return entry
        return None

    def _multiword_preposition_candidates(self, prep) -> list[str]:
        if prep.dep_ != "prep" and prep.pos_ != "ADP":
            return []
        final_adp = prep.lemma_.lower()
        head = prep.head
        if head is prep:
            return []

        candidates: list[str] = []
        head_lemma = head.lemma_.lower()
        determiner = self._relation_middle_determiner(head)

        if head.pos_ == "ADP" and final_adp == "of":
            candidates.append(f"{head_lemma} of")
        elif final_adp == "of":
            outer = head.head if head.head is not head else None
            if outer is not None and outer.pos_ == "ADP":
                outer_lemma = outer.lemma_.lower()
                if determiner:
                    candidates.append(f"{outer_lemma} {determiner} {head_lemma} {final_adp}")
                candidates.append(f"{outer_lemma} {head_lemma} {final_adp}")
            if determiner:
                candidates.append(f"{determiner} {head_lemma} {final_adp}")
            candidates.append(f"{head_lemma} {final_adp}")
        else:
            candidates.append(f"{head_lemma} {final_adp}")

        return sorted(dict.fromkeys(candidates), key=lambda item: (-len(item.split()), item))

    def _relation_middle_determiner(self, token) -> str | None:
        for child in token.children:
            if child.dep_ == "det" and child.lower_ in {"the", "a", "an"}:
                return child.lower_
        return None

    def _multiword_preposition_source_head(self, prep):
        head = prep.head
        if head is prep:
            return prep.head
        if prep.lemma_.lower() == "of" and head.head is not head and head.head.pos_ == "ADP":
            return head.head.head
        if head.head is not head:
            return head.head
        return head

    def _looks_like_modifier(self, token) -> bool:
        if self._is_quote_token(token):
            return True
        if self._is_possessive_pronoun(token):
            return False
        if quantity_role(token) is not None:
            return True
        if token.pos_ in {"ADJ", "ADV", "NUM"}:
            return True
        if token.dep_ in MODIFIER_DEPS:
            return True
        lemma = token.lemma_.lower()
        return lemma in COLOR_WORDS or lemma in MATERIAL_WORDS or lemma in SIZE_WORDS or lemma in VISUAL_WORDS

    def _is_object_candidate_token(self, token) -> bool:
        if self._is_quote_token(token):
            return False
        if token.pos_ == "PRON" or token.tag_ in PRONOUN_OBJECT_TAGS:
            return False
        if reference_class(token) is not None:
            return False
        if quantity_role(token) in ROOT_ONLY_QUANTITY_ROLES:
            return False
        if self._is_color_token(token):
            return False
        return token.pos_ in OBJECT_POS or token.tag_ in {"NN", "NNS", "NNP", "NNPS"}

    def _is_possessive_pronoun(self, token) -> bool:
        return token.dep_ == "poss" and (token.tag_ in POSSESSIVE_PRONOUN_TAGS or token.pos_ == "PRON")

    def _is_color_token(self, token) -> bool:
        return token.lemma_.lower() in COLOR_WORDS

    def _is_quote_token(self, token) -> bool:
        return is_raw_quote_token(token)

    def _add_modifier(self, token, source_tag: str) -> tuple[str, str, str]:
        if self._is_quote_token(token):
            return self._ensure_quote_attribute(token, source_tag), "has_attribute", "high"
        lemma = token.lemma_.lower()
        quantity = quantity_role(token)
        if quantity is not None:
            role = quantity
            concept_type = "quantity"
            edge_type = "has_quantity"
            confidence = quantity_confidence(quantity)
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
