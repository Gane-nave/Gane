# GANE Unified Platform

Unified repository consolidating backend (Rust), frontend (TypeScript/React), configuration, and Python validation tooling.

## Repository Layout

- `backend/` Rust workspace (AURORA NAV core modules)
- `frontend/` React apps (`trade-app`, `designer-app`) and shared utilities
- `config/` Unified Firebase blueprint + Firestore rules + environment configuration
- `python/` Validation scripts and project metadata
- `docs/` Architecture, deployment, security, RTL, API, and contribution docs
- `tests/` Integration/smoke tests for consolidated structure

## Quick Validation

```bash
python -m unittest discover -s tests -p 'test_*.py'
cargo test --manifest-path backend/Cargo.toml --workspace
```
