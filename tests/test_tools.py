import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from tools._utils import resolve_wiki_path, sha256
from tools.build_graph import append_checkpoint, load_checkpoint, deduplicate_edges
from tools.ingest import ALL_SUPPORTED_EXTENSIONS, parse_json_from_response
from tools.promote import promote_graph_data, select_promotable_edges


class WikiToolTests(unittest.TestCase):
    def test_resolve_wiki_path_keeps_generated_pages_inside_allowed_directory(self):
        path = resolve_wiki_path("entities/Example.md", {"entities"})
        self.assertEqual(path.name, "Example.md")
        self.assertEqual(path.parent.name, "entities")

    def test_resolve_wiki_path_rejects_escape_and_wrong_directory(self):
        with self.assertRaises(ValueError):
            resolve_wiki_path("../outside.md")
        with self.assertRaises(ValueError):
            resolve_wiki_path("concepts/Example.md", {"entities"})
        with self.assertRaises(ValueError):
            resolve_wiki_path(Path("/tmp/outside.md"))

    def test_parse_json_from_response_accepts_a_fenced_object(self):
        self.assertEqual(
            parse_json_from_response('```json\n{"title": "Example"}\n```'),
            {"title": "Example"},
        )

    def test_research_text_artifacts_are_supported_without_conversion(self):
        for suffix in (".in", ".log", ".data", ".dump", ".xyz", ".out"):
            self.assertIn(suffix, ALL_SUPPORTED_EXTENSIONS)

    def test_checkpoint_records_page_hash_and_latest_record(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            checkpoint = Path(temp_dir) / "inferred.jsonl"
            graph_dir = Path(temp_dir)
            edge = {
                "from": "sources/a",
                "to": "concepts/B",
                "type": "INFERRED",
                "confidence": 0.8,
            }
            with patch("tools.build_graph.INFERRED_EDGES_FILE", checkpoint), patch(
                "tools.build_graph.GRAPH_DIR", graph_dir
            ):
                append_checkpoint("sources/a", sha256("new"), sha256("context"), [edge])
                append_checkpoint("sources/a", sha256("newer"), sha256("context"), [])
                records = load_checkpoint()

            self.assertEqual(records["sources/a"]["hash"], sha256("newer"))
            self.assertEqual(records["sources/a"]["edges"], [])

    def test_draft_promotion_requires_confidence_and_evidence(self):
        graph = {
            "nodes": [{"id": "sources/a"}, {"id": "concepts/B"}],
            "edges": [
                {
                    "id": "good",
                    "from": "sources/a",
                    "to": "concepts/B",
                    "type": "INFERRED",
                    "relation": "USES",
                    "status": "DRAFT",
                    "confidence": 0.95,
                    "evidence": {"page": "sources/a", "kind": "semantic_page_context"},
                },
                {
                    "id": "weak",
                    "from": "sources/a",
                    "to": "concepts/B",
                    "type": "INFERRED",
                    "relation": "STUDIES",
                    "status": "DRAFT",
                    "confidence": 0.85,
                    "evidence": {"page": "sources/a"},
                },
            ],
        }
        self.assertEqual([edge["id"] for edge in select_promotable_edges(graph)], ["good"])
        promoted = promote_graph_data(graph)
        self.assertEqual([edge["id"] for edge in promoted], ["good"])
        self.assertEqual(graph["edges"][0]["status"], "STABLE")
        self.assertEqual(graph["edges"][1]["status"], "DRAFT")

    def test_edge_ids_keep_distinct_relations(self):
        edges = deduplicate_edges([
            {"from": "sources/a", "to": "concepts/B", "type": "INFERRED", "relation": "USES"},
            {"from": "sources/a", "to": "concepts/B", "type": "INFERRED", "relation": "STUDIES"},
        ])
        self.assertEqual(len({edge["id"] for edge in edges}), 2)


if __name__ == "__main__":
    unittest.main()
