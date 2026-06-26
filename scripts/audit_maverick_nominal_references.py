from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

import spacy

from hyphen_span_retokenizer import ensure_hyphen_span_merger
from object_mwe_retokenizer import DEFAULT_OBJECT_MWE_LEXICON, ensure_object_mwe_merger
from quote_retokenizer import ensure_raw_quote_merger


NOMINAL_REFERENCE_LEMMAS = {"one", "ones", "other", "others", "both", "each"}
SKIP_NOMINAL_DEPS = {"det", "amod", "compound", "poss", "case", "mark", "cc", "punct", "nummod"}
HUMAN_WORDS = {
    "adult",
    "boy",
    "child",
    "children",
    "girl",
    "individual",
    "kid",
    "man",
    "men",
    "people",
    "person",
    "player",
    "woman",
    "women",
    "worker",
    "workers",
}
PLURAL_QUANTIFIERS = {"two", "three", "four", "five", "several", "many", "multiple", "both"}
OBJECT_PRONOUN_LEMMAS = {"he", "she", "they", "it", "who", "that"}


@dataclass(frozen=True)
class CandidateMention:
    span: tuple[int, int]
    text: str
    candidate_type: str
    subtype: str
    object_id: str | None = None
    object_text: str | None = None
    token_i: int | None = None


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                records.append(json.loads(line))
    return records


def load_maverick(device: str, model_name: str):
    import maverick.models.maverick_model as mm

    class MaverickCompat(mm.Maverick):
        def __init__(self, hf_name_or_path: str = model_name, device: str = device):
            self.device = device
            path = self.__get_model_path__(hf_name_or_path)
            self.model = mm.BasePLModule.load_from_checkpoint(
                path,
                _recursive_=False,
                map_location=self.device,
                weights_only=False,
            )
            self.model = self.model.eval()
            self.model = self.model.model
            self.tokenizer = self.__get_model_tokenizer__()

    return MaverickCompat(hf_name_or_path=model_name, device=device)


def doc_sentence_tokens(doc) -> tuple[list[list[str]], dict[int, int]]:
    sentences: list[list[str]] = []
    token_to_flat: dict[int, int] = {}
    flat_i = 0
    sents = list(doc.sents)
    if not sents:
        sents = [doc[:]]
    for sent in sents:
        current: list[str] = []
        for token in sent:
            token_to_flat[token.i] = flat_i
            current.append(token.text)
            flat_i += 1
        if current:
            sentences.append(current)
    return sentences, token_to_flat


def span_to_flat(span, token_to_flat: dict[int, int]) -> tuple[int, int] | None:
    if span.start not in token_to_flat or span.end - 1 not in token_to_flat:
        return None
    return token_to_flat[span.start], token_to_flat[span.end - 1]


def token_to_flat_span(token, token_to_flat: dict[int, int]) -> tuple[int, int] | None:
    if token.i not in token_to_flat:
        return None
    flat_i = token_to_flat[token.i]
    return flat_i, flat_i


def normalized_token_text(token) -> str:
    return (token.lemma_ or token.text).lower()


def nominal_subtype(token) -> str:
    lemma = normalized_token_text(token)
    if lemma in {"one", "ones"}:
        return "one_anaphor"
    if lemma in {"other", "others"}:
        return "other_anaphor"
    if lemma == "both":
        return "group_both"
    if lemma == "each":
        return "distributive_each"
    return "nominal_reference"


def is_nominal_reference_token(token) -> bool:
    lemma = normalized_token_text(token)
    text = token.text.lower()
    if lemma not in NOMINAL_REFERENCE_LEMMAS and text not in NOMINAL_REFERENCE_LEMMAS:
        return False
    if token.dep_ in SKIP_NOMINAL_DEPS:
        return False
    if token.dep_ in {"nummod", "det", "amod"} and token.head.i != token.i and token.head.pos_ in {"NOUN", "PROPN"}:
        return False
    if lemma == "other" and token.dep_ == "amod":
        return False
    if lemma in {"another"}:
        return False
    if token.pos_ in {"PRON", "NUM", "NOUN"}:
        return True
    if lemma in {"both", "each", "other", "others"} and token.dep_ in {"nsubj", "nsubjpass", "dobj", "obj", "pobj", "attr"}:
        return True
    return False


def token_chunk(doc, token_i: int):
    for chunk in doc.noun_chunks:
        if chunk.start <= token_i < chunk.end:
            return chunk
    return None


def add_candidate(candidates: list[CandidateMention], seen: set[tuple[tuple[int, int], str]], candidate: CandidateMention) -> None:
    key = (candidate.span, f"{candidate.candidate_type}:{candidate.subtype}:{candidate.object_id or ''}")
    if key in seen:
        return
    seen.add(key)
    candidates.append(candidate)


def object_candidates(record: dict[str, Any], doc, token_to_flat: dict[int, int]) -> list[CandidateMention]:
    candidates: list[CandidateMention] = []
    seen: set[tuple[tuple[int, int], str]] = set()
    for mention in record.get("concept_mentions", []):
        if mention.get("concept_type") != "object":
            continue
        lemma = str(mention.get("lemma") or "").lower()
        if lemma in OBJECT_PRONOUN_LEMMAS or lemma in NOMINAL_REFERENCE_LEMMAS:
            continue
        token_i = mention.get("source_token_i")
        if not isinstance(token_i, int) or token_i < 0 or token_i >= len(doc):
            continue
        token = doc[token_i]
        root_span = token_to_flat_span(token, token_to_flat)
        if root_span is not None:
            add_candidate(
                candidates,
                seen,
                CandidateMention(
                    span=root_span,
                    text=token.text,
                    candidate_type="object_root",
                    subtype="object",
                    object_id=mention.get("mention_id"),
                    object_text=mention.get("text"),
                    token_i=token_i,
                ),
            )
        chunk = token_chunk(doc, token_i)
        if chunk is not None:
            flat_span = span_to_flat(chunk, token_to_flat)
            if flat_span is not None:
                add_candidate(
                    candidates,
                    seen,
                    CandidateMention(
                        span=flat_span,
                        text=chunk.text,
                        candidate_type="object_chunk",
                        subtype="object",
                        object_id=mention.get("mention_id"),
                        object_text=mention.get("text"),
                        token_i=token_i,
                    ),
                )
    candidates.extend(coordination_group_candidates(doc, token_to_flat))
    return candidates


def coordination_group_candidates(doc, token_to_flat: dict[int, int]) -> list[CandidateMention]:
    candidates: list[CandidateMention] = []
    seen: set[tuple[tuple[int, int], str]] = set()
    chunks = list(doc.noun_chunks)
    for chunk in chunks:
        roots = [chunk.root]
        roots.extend(child for child in chunk.root.children if child.dep_ == "conj" and child.pos_ in {"NOUN", "PROPN", "PRON"})
        if len(roots) < 2:
            continue
        member_chunks = []
        for root in roots:
            root_chunk = token_chunk(doc, root.i)
            if root_chunk is not None:
                member_chunks.append(root_chunk)
        if len(member_chunks) < 2:
            continue
        start = min(item.start for item in member_chunks)
        end = max(item.end for item in member_chunks)
        if start not in token_to_flat or end - 1 not in token_to_flat:
            continue
        text = doc[start:end].text
        add_candidate(
            candidates,
            seen,
            CandidateMention(
                span=(token_to_flat[start], token_to_flat[end - 1]),
                text=text,
                candidate_type="coordination_group",
                subtype="group",
                object_id=None,
                object_text=text,
                token_i=chunk.root.i,
            ),
        )
    return candidates


def nominal_candidates(doc, token_to_flat: dict[int, int]) -> list[CandidateMention]:
    candidates: list[CandidateMention] = []
    seen: set[tuple[tuple[int, int], str]] = set()
    for token in doc:
        if not is_nominal_reference_token(token):
            continue
        chunk = token_chunk(doc, token.i)
        if chunk is not None and chunk.root.i == token.i:
            flat_span = span_to_flat(chunk, token_to_flat)
            text = chunk.text
        else:
            flat_span = token_to_flat_span(token, token_to_flat)
            text = token.text
        if flat_span is None:
            continue
        add_candidate(
            candidates,
            seen,
            CandidateMention(
                span=flat_span,
                text=text,
                candidate_type="nominal_reference",
                subtype=nominal_subtype(token),
                token_i=token.i,
            ),
        )
    return candidates


def index_candidates(candidates: list[CandidateMention]) -> dict[tuple[int, int], list[CandidateMention]]:
    index: dict[tuple[int, int], list[CandidateMention]] = {}
    for candidate in candidates:
        index.setdefault(candidate.span, []).append(candidate)
    return index


def cluster_for_span(clusters: list[list[tuple[int, int]]], span: tuple[int, int]) -> list[tuple[int, int]] | None:
    for cluster in clusters:
        if span in cluster:
            return cluster
    return None


def choose_antecedent(
    cluster: list[tuple[int, int]] | None,
    nominal: CandidateMention,
    candidate_index: dict[tuple[int, int], list[CandidateMention]],
) -> CandidateMention | None:
    if not cluster:
        return None
    previous: list[CandidateMention] = []
    for span in cluster:
        if span == nominal.span or span[1] > nominal.span[0]:
            continue
        for candidate in candidate_index.get(span, []):
            if candidate.candidate_type != "nominal_reference":
                previous.append(candidate)
    if not previous:
        return None
    return sorted(previous, key=lambda item: candidate_rank(nominal, item))[0]


def candidate_rank(nominal: CandidateMention, candidate: CandidateMention) -> tuple[int, int, int]:
    distance = max(0, nominal.span[0] - candidate.span[1])
    score = 100
    if candidate.candidate_type == "coordination_group":
        score -= 30
    if is_plural_like(candidate):
        score -= 20
    if is_human_like(candidate):
        score -= 10
    if nominal.subtype == "group_both":
        score -= 80 if candidate.candidate_type == "coordination_group" else 0
    elif nominal.subtype == "distributive_each":
        score -= 50 if is_plural_like(candidate) or candidate.candidate_type == "coordination_group" else 0
    elif nominal.subtype == "other_anaphor":
        score -= 40 if is_plural_like(candidate) or candidate.candidate_type == "coordination_group" else 0
    elif nominal.subtype == "one_anaphor":
        score -= 35 if is_plural_like(candidate) else 0
    # Prefer fuller chunk/group mentions over bare roots when they describe the same nearby object.
    type_rank = {"coordination_group": 0, "object_chunk": 1, "object_root": 2}.get(candidate.candidate_type, 3)
    return score, distance, type_rank


def is_plural_like(candidate: CandidateMention) -> bool:
    if candidate.candidate_type == "coordination_group":
        return True
    text = (candidate.text or candidate.object_text or "").lower()
    words = text.split()
    if words and words[0] in PLURAL_QUANTIFIERS:
        return True
    object_text = (candidate.object_text or "").lower()
    if object_text in {"people", "men", "women", "children", "workers", "cars"}:
        return True
    if object_text.endswith("s") and not object_text.endswith(("ss", "us")):
        return True
    return False


def is_human_like(candidate: CandidateMention) -> bool:
    text = f"{candidate.text or ''} {candidate.object_text or ''}".lower()
    return any(word in HUMAN_WORDS for word in text.split())


def recommendation_for(nominal: CandidateMention, antecedent: CandidateMention | None) -> str:
    if antecedent is None:
        return "exclude_from_object_count_unresolved"
    if nominal.subtype in {"group_both", "distributive_each"}:
        return "manual_group_resolution"
    if antecedent.candidate_type == "coordination_group":
        return "manual_group_resolution"
    if nominal.subtype == "one_anaphor":
        return "copy_antecedent_type_apply_modifiers"
    if nominal.subtype == "other_anaphor":
        return "link_discourse_other"
    return "manual_nominal_resolution"


def status_for(antecedent: CandidateMention | None) -> str:
    if antecedent is None:
        return "unresolved"
    return "resolved_to_candidate"


def cluster_quality_flag(
    cluster: list[tuple[int, int]] | None,
    candidate_index: dict[tuple[int, int], list[CandidateMention]],
    broad_cluster_threshold: int,
) -> str:
    if not cluster:
        return "no_cluster"
    candidate_spans = {
        span
        for span in cluster
        if any(candidate.candidate_type != "nominal_reference" for candidate in candidate_index.get(span, []))
    }
    if len(cluster) >= broad_cluster_threshold or len(candidate_spans) >= 4:
        return "broad_cluster_check_manually"
    return "compact_cluster"


def markdown_count_table(counter: Counter[str]) -> str:
    if not counter:
        return "_none_"
    lines = ["| item | count |", "| --- | ---: |"]
    for key, value in counter.most_common():
        lines.append(f"| `{key}` | {value} |")
    return "\n".join(lines)


def markdown_escape(text: object, max_len: int = 110) -> str:
    value = str(text).replace("\n", " ").strip()
    if len(value) > max_len:
        value = value[: max_len - 3] + "..."
    return value.replace("|", "\\|")


def write_report(path: Path, args: argparse.Namespace, rows: list[dict[str, Any]], counters: dict[str, Counter[str]]) -> None:
    lines = [
        "# Maverick Nominal-Anaphoric Audit",
        "",
        "이 리포트는 Maverick `predefined_mentions`를 사용해 `one/other/others/both/each`류 nominal-anaphoric 후보가 이전 object/group 후보와 같은 cluster로 묶이는지 확인합니다.",
        "",
        "## Settings",
        f"- raw_concepts: `{args.raw_concepts}`",
        f"- output_jsonl: `{args.output}`",
        f"- spacy_model: `{args.spacy_model}`",
        f"- maverick_model: `{args.maverick_model}`",
        f"- device: `{args.device}`",
        f"- nominal_candidates_seen: `{len(rows)}`",
        f"- broad_cluster_threshold: `{args.broad_cluster_threshold}`",
        "",
        "## Nominal Subtypes",
        markdown_count_table(counters["subtype"]),
        "",
        "## Resolution Status",
        markdown_count_table(counters["status"]),
        "",
        "## Cluster Quality",
        markdown_count_table(counters["quality"]),
        "",
        "## Recommendations",
        markdown_count_table(counters["recommendation"]),
        "",
        "## Audit Rows",
        "| case | nominal | subtype | antecedent | antecedent type | quality | cluster | status | recommendation |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    str(row["row_index"]),
                    f"`{markdown_escape(row['nominal_text'], 40)}`",
                    f"`{row['subtype']}`",
                    markdown_escape(row.get("antecedent_text") or "", 45),
                    f"`{row.get('antecedent_type') or ''}`",
                    f"`{row['quality_flag']}`",
                    markdown_escape(row.get("cluster_text") or "", 60),
                    f"`{row['status']}`",
                    f"`{row['recommendation']}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "- `compact_cluster`: Maverick cluster가 작아서 audit signal로 비교적 보기 쉽습니다.",
            "- `broad_cluster_check_manually`: cluster가 넓게 뭉쳐 false positive 위험이 큽니다. 자동 치환하지 말고 rule 기반 후보로만 봐야 합니다.",
            "- `copy_antecedent_type_apply_modifiers`: `a red one -> car + red`처럼 antecedent object type을 복사하고 nominal modifier를 attribute 후보로 붙일 수 있습니다.",
            "- `link_discourse_other`: `other/others`는 object count에 넣지 말고 discourse link로만 둡니다.",
            "- `manual_group_resolution`: `both/each` 또는 coordination group은 단일 object로 collapse하지 않습니다.",
            "- `exclude_from_object_count_unresolved`: antecedent가 불확실하므로 surface nominal은 count에서 제외합니다.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit nominal-anaphoric references with Maverick predefined mentions.")
    parser.add_argument("--raw-concepts", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--summary-output", required=True, type=Path)
    parser.add_argument("--spacy-model", default="en_core_web_trf")
    parser.add_argument("--maverick-model", default="sapienzanlp/maverick-mes-ontonotes")
    parser.add_argument("--device", default="cuda")
    parser.add_argument("--mask-quotes", action="store_true")
    parser.add_argument("--merge-object-mwes", action="store_true")
    parser.add_argument("--merge-hyphen-spans", action="store_true")
    parser.add_argument("--object-mwe-lexicon", type=Path, default=DEFAULT_OBJECT_MWE_LEXICON)
    parser.add_argument("--broad-cluster-threshold", type=int, default=8)
    args = parser.parse_args()

    records = read_jsonl(args.raw_concepts)
    nlp = spacy.load(args.spacy_model)
    if args.mask_quotes:
        ensure_raw_quote_merger(nlp)
    if args.merge_object_mwes:
        ensure_object_mwe_merger(nlp, args.object_mwe_lexicon)
    if args.merge_hyphen_spans:
        ensure_hyphen_span_merger(nlp)

    model = load_maverick(args.device, args.maverick_model)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.summary_output.parent.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, Any]] = []
    counters = {"subtype": Counter(), "status": Counter(), "quality": Counter(), "recommendation": Counter()}
    with args.output.open("w", encoding="utf-8") as handle:
        for record in records:
            doc = nlp(record.get("parse_caption") or record.get("caption") or "")
            sentence_tokens, token_to_flat = doc_sentence_tokens(doc)
            nominals = nominal_candidates(doc, token_to_flat)
            if not nominals:
                continue
            objects = object_candidates(record, doc, token_to_flat)
            predefined = sorted({candidate.span for candidate in objects + nominals})
            if not predefined:
                continue
            result = model.predict(sentence_tokens, predefined_mentions=predefined)
            clusters = [list(cluster) for cluster in result.get("clusters_token_offsets", [])]
            candidate_index = index_candidates(objects + nominals)
            for nominal in nominals:
                cluster = cluster_for_span(clusters, nominal.span)
                antecedent = choose_antecedent(cluster, nominal, candidate_index)
                status = status_for(antecedent)
                quality_flag = cluster_quality_flag(cluster, candidate_index, args.broad_cluster_threshold)
                recommendation = recommendation_for(nominal, antecedent)
                cluster_text = None
                if cluster:
                    cluster_text = " ; ".join(
                        " ".join(result["tokens"][span[0] : span[1] + 1])
                        for span in cluster
                    )
                row = {
                    "row_index": record.get("row_index"),
                    "caption_id": record.get("caption_id"),
                    "caption": record.get("caption"),
                    "nominal_text": nominal.text,
                    "nominal_span": list(nominal.span),
                    "subtype": nominal.subtype,
                    "antecedent_text": antecedent.text if antecedent else None,
                    "antecedent_span": list(antecedent.span) if antecedent else None,
                    "antecedent_type": antecedent.candidate_type if antecedent else None,
                    "antecedent_object_id": antecedent.object_id if antecedent else None,
                    "antecedent_object_text": antecedent.object_text if antecedent else None,
                    "cluster": [list(span) for span in cluster] if cluster else [],
                    "cluster_text": cluster_text,
                    "status": status,
                    "quality_flag": quality_flag,
                    "recommendation": recommendation,
                }
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
                rows.append(row)
                counters["subtype"][nominal.subtype] += 1
                counters["status"][status] += 1
                counters["quality"][quality_flag] += 1
                counters["recommendation"][recommendation] += 1

    write_report(args.summary_output, args, rows, counters)
    print(args.output)
    print(args.summary_output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
