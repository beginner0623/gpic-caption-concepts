from __future__ import annotations

from typing import Any

from stage9_reference_model import mention_token_i, norm, semantic_type


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
    "shoulder",
    "tail",
    "wing",
}

MANIPULATION_ACTIONS = {
    "carry",
    "grip",
    "hold",
    "lift",
    "raise",
    "support",
}

PLACEMENT_ACTIONS = {
    "arrange",
    "lay",
    "lean",
    "mount",
    "place",
    "position",
    "put",
    "rest",
    "set",
}

PROPULSION_ACTIONS = {
    "bat",
    "hit",
    "kick",
    "launch",
    "pass",
    "send",
    "serve",
    "shoot",
    "throw",
    "toss",
}

CREATION_ACTIONS = {
    "create",
    "form",
    "generate",
    "make",
    "produce",
}

BODY_ANCHOR_RELATIONS = {
    "above",
    "around",
    "behind",
    "below",
    "beneath",
    "in_front_of",
    "near",
    "on",
    "on_top_of",
    "over",
    "under",
    "underneath",
}

TRAJECTORY_RELATIONS = {
    "across",
    "into",
    "onto",
    "out_of",
    "over",
    "past",
    "through",
    "toward",
    "towards",
}

PLACEMENT_RELATIONS = {
    "in",
    "inside",
    "on",
    "on_top_of",
    "onto",
    "under",
}

CREATED_OBJECT_RELATIONS = {
    "across",
    "around",
    "in",
    "inside",
    "on",
    "over",
    "under",
}

SUPPORT_OR_CONTAINER_LEMMAS = {
    "bag",
    "basket",
    "bed",
    "bench",
    "bowl",
    "box",
    "case",
    "chair",
    "container",
    "counter",
    "cup",
    "desk",
    "dish",
    "floor",
    "ground",
    "plate",
    "rack",
    "shelf",
    "stand",
    "surface",
    "table",
    "tray",
    "wall",
}


def relation_label(value: Any) -> str:
    return str(value or "").strip().lower()


def mention_lemmas(mention: dict[str, Any] | None) -> set[str]:
    if mention is None:
        return set()
    lemma = str(mention.get("lemma", "")).lower()
    text = norm(mention.get("text", ""))
    values = {lemma, text, text.replace(" ", "_")}
    return {value for value in values if value}


def is_body_part(mention: dict[str, Any] | None) -> bool:
    return bool(mention_lemmas(mention) & BODY_PART_LEMMAS)


def is_support_or_container(mention: dict[str, Any] | None) -> bool:
    return bool(mention_lemmas(mention) & SUPPORT_OR_CONTAINER_LEMMAS)


def canonical_action_lemma(event: dict[str, Any]) -> str:
    return relation_label(event.get("canonical_action") or event.get("raw_action_lemma"))


def event_roles(event: dict[str, Any], role_name: str) -> list[dict[str, Any]]:
    return [role for role in event.get("roles", []) if role.get("role") == role_name]


def event_has_agent(event: dict[str, Any], raw_source_id: str, canonical_source: str | None) -> bool:
    for role in event_roles(event, "agent"):
        if str(role.get("target")) == raw_source_id:
            return True
        if canonical_source and role.get("canonical_target") == canonical_source:
            return True
    return False


def patient_like_roles(event: dict[str, Any]) -> list[dict[str, Any]]:
    roles = []
    for role in event.get("roles", []):
        if role.get("role") in {"patient", "theme"}:
            roles.append(role)
    return roles


def role_token_distance(role: dict[str, Any], mentions_by_id: dict[str, dict[str, Any]], action_i: int | None) -> int:
    mention = mentions_by_id.get(str(role.get("target")))
    token_i = mention_token_i(mention) if mention is not None else None
    if action_i is None or token_i is None:
        return 10**6
    return abs(token_i - action_i)


def best_patient_like_role(
    event: dict[str, Any],
    mentions_by_id: dict[str, dict[str, Any]],
) -> dict[str, Any] | None:
    roles = patient_like_roles(event)
    if not roles:
        return None
    action_i = event.get("source_token_i")
    action_i = action_i if isinstance(action_i, int) else None
    return sorted(roles, key=lambda role: role_token_distance(role, mentions_by_id, action_i))[0]


def compatible_token_order(
    event: dict[str, Any],
    edge: dict[str, Any],
    mentions_by_id: dict[str, dict[str, Any]],
) -> bool:
    action_i = event.get("source_token_i")
    if not isinstance(action_i, int):
        return True
    target = mentions_by_id.get(str(edge.get("target")))
    target_i = mention_token_i(target) if target is not None else None
    if target_i is None:
        return True
    return target_i >= action_i


def pp_patient_source_score(
    *,
    relation: str,
    action: str,
    target: dict[str, Any] | None,
) -> tuple[int, str] | None:
    if target is None:
        return None
    if (
        relation in BODY_ANCHOR_RELATIONS
        and is_body_part(target)
        and action in MANIPULATION_ACTIONS | PLACEMENT_ACTIONS | PROPULSION_ACTIONS
    ):
        return 92, "patient_body_part_anchor"
    if relation in TRAJECTORY_RELATIONS and action in PROPULSION_ACTIONS:
        return 90, "patient_trajectory"
    if relation in PLACEMENT_RELATIONS and action in PLACEMENT_ACTIONS and is_support_or_container(target):
        return 88, "patient_placement_support_or_container"
    if relation in CREATED_OBJECT_RELATIONS and action in CREATION_ACTIONS:
        return 84, "created_object_location"
    return None


def pp_source_disambiguation(
    *,
    edge: dict[str, Any],
    canonical_source: str | None,
    canonical_target: str | None,
    canonical_events: list[dict[str, Any]],
    mentions_by_id: dict[str, dict[str, Any]],
) -> dict[str, Any] | None:
    relation = relation_label(edge.get("evidence"))
    if not relation:
        return None

    raw_source_id = str(edge.get("source"))
    raw_target_id = str(edge.get("target"))
    target = mentions_by_id.get(raw_target_id)

    candidates: list[dict[str, Any]] = []
    for event in canonical_events:
        if not event_has_agent(event, raw_source_id, canonical_source):
            continue
        if not compatible_token_order(event, edge, mentions_by_id):
            continue
        patient_role = best_patient_like_role(event, mentions_by_id)
        if patient_role is None:
            continue
        patient_target = str(patient_role.get("target"))
        patient_entity = patient_role.get("canonical_target")
        if not patient_entity or patient_entity == canonical_source or patient_entity == canonical_target:
            continue
        action = canonical_action_lemma(event)
        scored = pp_patient_source_score(relation=relation, action=action, target=target)
        if scored is None:
            continue
        score, reason = scored
        candidates.append(
            {
                "selected_source": patient_entity,
                "selected_raw_source": patient_target,
                "selected_role": patient_role.get("role"),
                "action_mention_id": event.get("action_mention_id"),
                "canonical_action": action,
                "score": score,
                "reason": reason,
                "target_semantic_type": semantic_type(target) if target else "",
                "target_lemma": str(target.get("lemma", "")) if target else "",
            }
        )

    if not candidates:
        return None

    candidates.sort(key=lambda item: (-int(item["score"]), str(item["action_mention_id"])))
    best = candidates[0]
    runner_up = int(candidates[1]["score"]) if len(candidates) > 1 else 0
    margin = int(best["score"]) - runner_up
    if runner_up and margin < 8:
        return None

    best["method"] = "pp_source_disambiguation"
    best["raw_source"] = raw_source_id
    best["raw_target"] = raw_target_id
    best["relation"] = relation
    best["previous_canonical_source"] = canonical_source
    best["canonical_target"] = canonical_target
    best["confidence"] = "high" if int(best["score"]) >= 90 else "medium"
    if runner_up:
        best["runner_up_score"] = runner_up
        best["margin"] = margin
    return best
