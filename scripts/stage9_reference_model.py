from __future__ import annotations

from collections import defaultdict
import re
from typing import Any


PERSON_LEMMAS = {
    "adult",
    "attendee",
    "boy",
    "child",
    "girl",
    "kid",
    "man",
    "men",
    "people",
    "person",
    "player",
    "referee",
    "rider",
    "runner",
    "woman",
    "women",
}
ANIMAL_LEMMAS = {
    "animal",
    "bird",
    "cat",
    "cow",
    "dog",
    "duck",
    "horse",
    "sheep",
    "woodpecker",
}
CLOTHING_LEMMAS = {
    "blazer",
    "cap",
    "coat",
    "collar",
    "dress",
    "helmet",
    "jacket",
    "jersey",
    "mask",
    "scarf",
    "shirt",
    "shoe",
    "skirt",
    "suit",
    "uniform",
    "vest",
}
VEHICLE_LEMMAS = {
    "airplane",
    "bike",
    "bus",
    "car",
    "motorcycle",
    "suv",
    "truck",
    "van",
    "vehicle",
}
DEVICE_LEMMAS = {
    "appliance",
    "camera",
    "cell_phone",
    "computer",
    "device",
    "hearing_aid",
    "laptop",
    "monitor",
    "phone",
    "remote",
    "screen",
    "tablet",
}
DOCUMENT_LEMMAS = {
    "book",
    "document",
    "label",
    "list",
    "page",
    "paper",
    "plaque",
    "sign",
    "text",
}

HUMAN_AGENT_ACTIONS = {
    "bat",
    "clap",
    "compete",
    "control",
    "dress",
    "hold",
    "listen",
    "look",
    "play",
    "point",
    "pose",
    "read",
    "run",
    "sit",
    "skate",
    "smile",
    "speak",
    "stand",
    "talk",
    "walk",
    "watch",
    "wear",
}

GENERIC_CLASS_BY_HEAD = {
    "animal": "animal",
    "creature": "animal",
    "device": "device",
    "document": "document",
    "item": "object",
    "object": "object",
    "vehicle": "vehicle",
}

REFERENCE_ROLES = {
    "singular_substitute",
    "contrastive_reference",
    "group_reference",
    "distributive_reference",
}

RESOLVED_RE = re.compile(r"resolved\s+(.+?)\s+->\s+([^;]+)", re.IGNORECASE)
ARROW_TARGET_RE = re.compile(r"->\s*([^;]+)$", re.IGNORECASE)


def norm(value: Any) -> str:
    return " ".join(str(value or "").strip().lower().replace("_", " ").split())


def mention_token_i(mention: dict[str, Any]) -> int | None:
    token_i = mention.get("source_token_i")
    return token_i if isinstance(token_i, int) else None


def semantic_type(mention: dict[str, Any]) -> str:
    lemma = str(mention.get("lemma", "")).lower()
    text = norm(mention.get("text", ""))
    parts = {lemma, text, text.replace(" ", "_")}
    if parts & PERSON_LEMMAS:
        return "person"
    if parts & ANIMAL_LEMMAS:
        return "animal"
    if parts & CLOTHING_LEMMAS:
        return "clothing"
    if parts & VEHICLE_LEMMAS:
        return "vehicle"
    if parts & DEVICE_LEMMAS:
        return "device"
    if parts & DOCUMENT_LEMMAS:
        return "document"
    if mention.get("concept_type") == "group":
        return "group"
    return "object"


def is_countable_entity_mention(mention: dict[str, Any]) -> bool:
    return mention.get("concept_type") in {"object", "group", "context"}


def reference_kind(ref: dict[str, Any]) -> str:
    role = str(ref.get("role", ""))
    text = norm(ref.get("text", ""))
    if role == "group_reference":
        return "group"
    if text in {"others", "the others"}:
        return "complement_subset"
    if role == "contrastive_reference":
        return "contrastive_instance"
    if role == "singular_substitute":
        return "instance"
    return "reference"


def entity_id_for_mention(mention_id: str) -> str:
    return f"ent_{mention_id}"


def entity_id_for_reference(ref_id: str) -> str:
    return f"eref_{ref_id}"


def build_reference_model(
    mentions: list[dict[str, Any]],
    edges: list[dict[str, Any]],
) -> dict[str, Any]:
    mentions_by_id = {str(mention["mention_id"]): mention for mention in mentions if "mention_id" in mention}
    outgoing_edges: dict[str, list[dict[str, Any]]] = defaultdict(list)
    refers_to_edges: dict[str, dict[str, Any]] = {}
    group_members: dict[str, list[str]] = defaultdict(list)

    for edge in edges:
        source = str(edge.get("source"))
        outgoing_edges[source].append(edge)
        if edge.get("edge_type") == "refers_to":
            refers_to_edges[source] = edge
        elif edge.get("edge_type") == "has_member":
            group_members[source].append(str(edge.get("target")))

    entities: list[dict[str, Any]] = []
    mention_to_entity: dict[str, str] = {}
    reference_entities: dict[str, str] = {}
    reference_records: list[dict[str, Any]] = []
    entity_links: list[dict[str, Any]] = []

    for mention in mentions:
        mention_id = str(mention.get("mention_id"))
        if not is_countable_entity_mention(mention):
            continue
        entity_id = entity_id_for_mention(mention_id)
        mention_to_entity[mention_id] = entity_id
        entity = {
            "entity_id": entity_id,
            "entity_type": str(mention.get("concept_type")),
            "canonical_lemma": mention.get("lemma"),
            "text": mention.get("text"),
            "semantic_type": semantic_type(mention),
            "raw_mention_ids": [mention_id],
            "source": "raw_mention",
        }
        if mention_id in group_members:
            entity["member_entities"] = [
                entity_id_for_mention(member_id)
                for member_id in group_members[mention_id]
                if member_id in mentions_by_id
            ]
        entities.append(entity)

    # Class-compatible generic definite NPs such as "The device" are canonical aliases,
    # not destructive raw-stage merges.
    for mention in mentions:
        mention_id = str(mention.get("mention_id"))
        if mention.get("concept_type") != "object":
            continue
        generic_class = GENERIC_CLASS_BY_HEAD.get(str(mention.get("lemma", "")).lower())
        if generic_class is None or generic_class == "object":
            continue
        antecedent_id = generic_antecedent(mention, mentions)
        if antecedent_id is None:
            continue
        alias_entity = mention_to_entity.get(antecedent_id)
        if alias_entity is None:
            continue
        old_entity = mention_to_entity.get(mention_id)
        mention_to_entity[mention_id] = alias_entity
        entity_links.append(
            {
                "link_type": "generic_alias",
                "source_mention_id": mention_id,
                "source_entity_id": old_entity,
                "target_entity_id": alias_entity,
                "generic_class": generic_class,
                "confidence": "medium",
            }
        )

    for mention in mentions:
        if mention.get("concept_type") != "reference":
            continue
        ref_id = str(mention.get("mention_id"))
        refers_to = refers_to_edges.get(ref_id)
        antecedent_id = str(refers_to.get("target")) if refers_to is not None else None
        if not antecedent_id or antecedent_id not in mentions_by_id:
            continue

        members = both_reference_members(mention, antecedent_id, mentions, edges, mentions_by_id)
        ref_entity_id = entity_id_for_reference(ref_id)
        reference_entities[ref_id] = ref_entity_id
        mention_to_entity[ref_id] = ref_entity_id
        antecedent_entity_id = mention_to_entity.get(antecedent_id, entity_id_for_mention(antecedent_id))
        antecedent = mentions_by_id[antecedent_id]
        ref_kind = reference_kind(mention)
        entity = {
            "entity_id": ref_entity_id,
            "entity_type": ref_kind,
            "canonical_lemma": antecedent.get("lemma"),
            "text": mention.get("text"),
            "semantic_type": semantic_type(antecedent),
            "raw_mention_ids": [ref_id],
            "parent_entity_id": antecedent_entity_id,
            "reference_role": mention.get("role"),
            "reference_mention_id": ref_id,
            "antecedent_mention_id": antecedent_id,
            "source": "stage9_reference",
        }
        if ref_kind == "instance":
            entity["cardinality"] = 1
        elif ref_kind == "contrastive_instance":
            entity["cardinality"] = 1
            entity["disjoint_from_parent_member"] = True
        elif ref_kind == "complement_subset":
            entity["cardinality"] = "many"
            entity["subset_relation"] = "complement"
        elif ref_kind == "group":
            entity["cardinality"] = 2
        if members:
            entity["member_entities"] = [
                mention_to_entity.get(member_id, entity_id_for_mention(member_id))
                for member_id in members
            ]
            entity["semantic_type"] = "person" if all(semantic_type(mentions_by_id[item]) == "person" for item in members) else entity["semantic_type"]
            entity["source"] = "stage9_reference_group_repair"
        entities.append(entity)
        reference_records.append(
            {
                "reference_mention_id": ref_id,
                "reference_text": mention.get("text"),
                "reference_role": mention.get("role"),
                "antecedent_mention_id": antecedent_id,
                "entity_id": ref_entity_id,
            }
        )
        entity_links.append(
            {
                "link_type": "refers_to",
                "source_mention_id": ref_id,
                "source_entity_id": ref_entity_id,
                "target_mention_id": antecedent_id,
                "target_entity_id": antecedent_entity_id,
                "confidence": refers_to.get("confidence") if refers_to else "medium",
            }
        )

    return {
        "entities": entities,
        "mention_to_entity": mention_to_entity,
        "reference_entities": reference_entities,
        "reference_records": reference_records,
        "entity_links": entity_links,
        "mentions_by_id": mentions_by_id,
    }


def generic_antecedent(generic_mention: dict[str, Any], mentions: list[dict[str, Any]]) -> str | None:
    generic_type = GENERIC_CLASS_BY_HEAD.get(str(generic_mention.get("lemma", "")).lower())
    token_i = mention_token_i(generic_mention)
    if generic_type is None or token_i is None:
        return None

    best: tuple[int, str] | None = None
    for candidate in mentions:
        if candidate.get("concept_type") != "object":
            continue
        candidate_id = str(candidate.get("mention_id"))
        if candidate_id == str(generic_mention.get("mention_id")):
            continue
        candidate_i = mention_token_i(candidate)
        if candidate_i is None or candidate_i >= token_i:
            continue
        distance = token_i - candidate_i
        if distance > 80:
            continue
        candidate_type = semantic_type(candidate)
        if candidate_type != generic_type:
            continue
        if str(candidate.get("lemma", "")).lower() in GENERIC_CLASS_BY_HEAD:
            continue
        score = 100 - distance
        if best is None or score > best[0]:
            best = (score, candidate_id)
    return best[1] if best is not None else None


def both_reference_members(
    reference: dict[str, Any],
    antecedent_id: str,
    mentions: list[dict[str, Any]],
    edges: list[dict[str, Any]],
    mentions_by_id: dict[str, dict[str, Any]],
) -> list[str]:
    if str(reference.get("role")) != "group_reference" or norm(reference.get("text")) != "both":
        return []
    if not reference_used_as_human_agent(reference, antecedent_id, edges, mentions_by_id):
        return []
    token_i = mention_token_i(reference)
    if token_i is None:
        return []
    candidates: list[tuple[int, str]] = []
    for mention in mentions:
        mention_id = str(mention.get("mention_id"))
        candidate_i = mention_token_i(mention)
        if candidate_i is None or candidate_i >= token_i:
            continue
        if token_i - candidate_i > 45:
            continue
        if mention.get("concept_type") != "object" or semantic_type(mention) != "person":
            continue
        candidates.append((candidate_i, mention_id))
    if len(candidates) < 2:
        return []
    return [mention_id for _token_i, mention_id in sorted(candidates)[-2:]]


def reference_used_as_human_agent(
    reference: dict[str, Any],
    antecedent_id: str,
    edges: list[dict[str, Any]],
    mentions_by_id: dict[str, dict[str, Any]],
) -> bool:
    ref_text = norm(reference.get("text"))
    for edge in edges:
        if edge.get("edge_type") != "agent" or str(edge.get("target")) != antecedent_id:
            continue
        evidence = norm(edge.get("evidence"))
        if f"resolved {ref_text} ->" not in evidence:
            continue
        action = mentions_by_id.get(str(edge.get("source")))
        if action is None:
            continue
        if str(action.get("lemma", "")).lower() in HUMAN_AGENT_ACTIONS:
            return True
    return False


def resolved_reference_for_edge(
    edge: dict[str, Any],
    anchor_token_i: int | None,
    model: dict[str, Any],
) -> str | None:
    match = RESOLVED_RE.search(str(edge.get("evidence", "")))
    if match:
        ref_surface = norm(match.group(1))
    else:
        arrow_match = ARROW_TARGET_RE.search(str(edge.get("evidence", "")))
        if not arrow_match:
            return None
        ref_surface = norm(arrow_match.group(1))
    if not ref_surface:
        return None
    target = str(edge.get("target"))
    candidates = []
    for record in model["reference_records"]:
        if str(record.get("antecedent_mention_id")) != target:
            continue
        if norm(record.get("reference_text")) != ref_surface:
            continue
        ref_mention = model["mentions_by_id"].get(str(record["reference_mention_id"]))
        if ref_mention is None:
            continue
        ref_i = mention_token_i(ref_mention)
        if ref_i is None:
            continue
        distance = abs((anchor_token_i if anchor_token_i is not None else ref_i) - ref_i)
        before_bonus = 0 if anchor_token_i is None or ref_i <= anchor_token_i else 20
        candidates.append((distance + before_bonus, -ref_i, str(record["entity_id"])))
    if not candidates:
        return None
    return sorted(candidates)[0][2]


def canonical_target_for_role(
    raw_target: str,
    edge: dict[str, Any],
    action: dict[str, Any],
    model: dict[str, Any],
) -> str | None:
    action_i = mention_token_i(action)
    ref_entity = resolved_reference_for_edge(edge, action_i, model)
    if ref_entity is not None:
        return ref_entity
    return model["mention_to_entity"].get(raw_target)


def canonical_relation_endpoint(
    raw_mention_id: str,
    edge: dict[str, Any],
    endpoint: str,
    model: dict[str, Any],
) -> str | None:
    scoped = scoped_reference_entity_for_relation(raw_mention_id, edge, endpoint, model)
    if scoped is not None:
        return scoped
    return model["mention_to_entity"].get(raw_mention_id)


def scoped_reference_entity_for_relation(
    raw_mention_id: str,
    edge: dict[str, Any],
    endpoint: str,
    model: dict[str, Any],
) -> str | None:
    other_key = "target" if endpoint == "source" else "source"
    other = model["mentions_by_id"].get(str(edge.get(other_key)))
    current = model["mentions_by_id"].get(raw_mention_id)
    if other is None or current is None:
        return None
    other_i = mention_token_i(other)
    if other_i is None:
        return None
    relation = norm(edge.get("evidence"))
    other_type = semantic_type(other)
    if not should_scope_relation_to_reference(relation, other_type):
        return None

    candidates = []
    for record in model["reference_records"]:
        if str(record.get("antecedent_mention_id")) != raw_mention_id:
            continue
        ref = model["mentions_by_id"].get(str(record["reference_mention_id"]))
        if ref is None:
            continue
        ref_i = mention_token_i(ref)
        if ref_i is None or ref_i > other_i:
            continue
        if other_i - ref_i > 12:
            continue
        candidates.append((other_i - ref_i, -ref_i, str(record["entity_id"])))
    if not candidates:
        return None
    return sorted(candidates)[0][2]


def should_scope_relation_to_reference(relation: str, other_type: str) -> bool:
    if relation in {"in", "with"} and other_type == "clothing":
        return True
    if relation in {"toward", "behind", "beside", "near", "next_to"}:
        return True
    return False


def recovered_roles_from_skipped_edges(
    action: dict[str, Any],
    skipped_edges: list[dict[str, Any]],
    model: dict[str, Any],
) -> list[dict[str, Any]]:
    recovered = []
    action_id = str(action.get("mention_id"))
    for skipped in skipped_edges:
        if str(skipped.get("source")) != action_id:
            continue
        if skipped.get("edge_type") not in {"agent", "patient"}:
            continue
        ref_entity = resolved_reference_for_edge(skipped, mention_token_i(action), model)
        if ref_entity is None:
            continue
        recovered.append(
            {
                "role": skipped.get("edge_type"),
                "target": skipped.get("target"),
                "canonical_target": ref_entity,
                "confidence": skipped.get("confidence"),
                "raw_edge_id": None,
                "evidence": skipped.get("evidence"),
                "recovered_from_skipped_edge": skipped.get("reason"),
            }
        )
    return recovered
