#!/usr/bin/env python3
"""Review and promote high-confidence draft graph relationships.

Promotion changes graph metadata only. It never inserts wikilinks into wiki
pages, so the human-readable wiki remains the source of truth.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from tools._utils import GRAPH_DIR, REPO_ROOT, WIKI_DIR, append_log

GRAPH_JSON = GRAPH_DIR / "graph.json"
CACHE_FILE = GRAPH_DIR / ".cache.json"
INFERRED_EDGES_FILE = GRAPH_DIR / ".inferred_edges.jsonl"


def select_promotable_edges(graph_data: dict, min_confidence: float = 0.9) -> list[dict]:
    """Return draft semantic edges with evidence and sufficient confidence."""
    node_ids = {node.get("id") for node in graph_data.get("nodes", [])}
    candidates = []
    for edge in graph_data.get("edges", []):
        evidence = edge.get("evidence") or {}
        if edge.get("status", "STABLE") != "DRAFT":
            continue
        if edge.get("type") not in {"INFERRED", "AMBIGUOUS"}:
            continue
        if edge.get("from") not in node_ids or edge.get("to") not in node_ids:
            continue
        try:
            confidence = float(edge.get("confidence", 0))
        except (TypeError, ValueError):
            continue
        if confidence < min_confidence:
            continue
        if evidence.get("page") != edge.get("from"):
            continue
        candidates.append(edge)
    return candidates


def promote_graph_data(graph_data: dict, min_confidence: float = 0.9) -> list[dict]:
    """Mark eligible edges stable and return the promoted records."""
    candidates = select_promotable_edges(graph_data, min_confidence)
    promoted_on = date.today().isoformat()
    candidate_ids = {edge.get("id") for edge in candidates}
    for edge in graph_data.get("edges", []):
        if edge.get("id") in candidate_ids:
            edge["status"] = "STABLE"
            edge["promoted"] = promoted_on
            edge["promotion"] = "manual-confidence-threshold"
    return candidates


def _promoted_lookup(promoted: list[dict]) -> dict[tuple[str, str, str], dict]:
    return {
        (edge["from"], edge["to"], edge.get("relation", "RELATED_TO")): edge
        for edge in promoted
    }


def update_inference_state(promoted: list[dict]) -> None:
    """Persist promotion status so a later graph rebuild does not undo it."""
    lookup = _promoted_lookup(promoted)
    if not lookup:
        return

    if CACHE_FILE.exists():
        try:
            cache = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            cache = {}
        for cache_path, entry in cache.items():
            if not isinstance(entry, dict):
                continue
            try:
                source = Path(cache_path).resolve().relative_to(WIKI_DIR.resolve()).with_suffix("").as_posix()
            except ValueError:
                source = str(entry.get("page", ""))
            for rel in entry.get("edges", []):
                key = (source, rel.get("to"), rel.get("relation", "RELATED_TO"))
                if key in lookup:
                    rel["status"] = "STABLE"
                    rel["promoted"] = lookup[key].get("promoted")
                    rel["promotion"] = lookup[key].get("promotion")
        CACHE_FILE.write_text(json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8")

    if INFERRED_EDGES_FILE.exists():
        updated_lines = []
        for line in INFERRED_EDGES_FILE.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                updated_lines.append(line)
                continue
            source = record.get("page_id", "")
            for edge in record.get("edges", []):
                key = (source, edge.get("to"), edge.get("relation", "RELATED_TO"))
                if key in lookup:
                    edge["status"] = "STABLE"
                    edge["promoted"] = lookup[key].get("promoted")
                    edge["promotion"] = lookup[key].get("promotion")
            updated_lines.append(json.dumps(record, ensure_ascii=False))
        INFERRED_EDGES_FILE.write_text("\n".join(updated_lines) + "\n", encoding="utf-8")


def main(graph_path: Path = GRAPH_JSON, min_confidence: float = 0.9, apply: bool = False) -> int:
    if not graph_path.exists():
        print(f"Graph not found: {graph_path.relative_to(REPO_ROOT)}")
        print("Run: python tools/build_graph.py --no-infer")
        return 1

    try:
        graph_data = json.loads(graph_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"Cannot read graph: {exc}")
        return 1

    candidates = select_promotable_edges(graph_data, min_confidence)
    if not candidates:
        print(f"No draft edges meet the confidence threshold ({min_confidence:.2f}).")
        return 0

    print(f"{len(candidates)} candidate edge(s) meet the confidence threshold ({min_confidence:.2f}):")
    for edge in candidates:
        reason = edge.get("title") or edge.get("relationship") or "no reason recorded"
        print(f"- {edge['from']} -[{edge.get('relation', 'RELATED_TO')}]-> {edge['to']} "
              f"({edge.get('confidence', 0):.2f}) {reason}")

    if not apply:
        print("Dry run only. Add --apply to promote these edges.")
        return 0

    promoted = promote_graph_data(graph_data, min_confidence)
    graph_path.write_text(json.dumps(graph_data, indent=2, ensure_ascii=False), encoding="utf-8")
    update_inference_state(promoted)
    append_log(
        f"## [{date.today().isoformat()}] graph | Promoted {len(promoted)} draft relationship(s)"
    )
    print(f"Promoted {len(promoted)} edge(s) to STABLE in {graph_path.relative_to(REPO_ROOT)}.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Promote reviewed draft graph relationships")
    parser.add_argument("--graph", type=Path, default=GRAPH_JSON, help="Path to graph.json")
    parser.add_argument("--min-confidence", type=float, default=0.9, help="Promotion threshold (default: 0.90)")
    parser.add_argument("--apply", action="store_true", help="Persist promotion status")
    args = parser.parse_args()
    raise SystemExit(main(args.graph, args.min_confidence, args.apply))
