from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    config_path = ROOT / "config" / "firebase-blueprint.json"
    payload = json.loads(config_path.read_text(encoding="utf-8"))
    required_collections = {"users", "orders", "incidents", "auditLogs"}
    existing = set(payload.get("collections", {}).keys())
    missing = required_collections - existing
    if missing:
        raise SystemExit(f"Missing collections: {sorted(missing)}")
    print("Configuration blueprint validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
