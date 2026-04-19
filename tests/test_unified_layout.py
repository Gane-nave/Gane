import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class UnifiedLayoutTests(unittest.TestCase):
    def test_required_directories_exist(self):
        for path in [
            "backend",
            "frontend/trade-app",
            "frontend/designer-app",
            "frontend/shared",
            "config",
            "python/scripts",
            "docs",
            "tests",
        ]:
            self.assertTrue((ROOT / path).exists(), path)

    def test_firebase_blueprint_contains_core_collections(self):
        payload = json.loads((ROOT / "config/firebase-blueprint.json").read_text(encoding="utf-8"))
        collections = payload.get("collections", {})
        for key in ["users", "orders", "incidents", "auditLogs"]:
            self.assertIn(key, collections)

    def test_typescript_projects_are_strict(self):
        for tsconfig in [
            ROOT / "frontend/trade-app/tsconfig.json",
            ROOT / "frontend/designer-app/tsconfig.json",
        ]:
            payload = json.loads(tsconfig.read_text(encoding="utf-8"))
            self.assertTrue(payload["compilerOptions"]["strict"])


if __name__ == "__main__":
    unittest.main()
