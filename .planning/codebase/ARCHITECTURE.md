# Architecture

High-level overview
- Single Python package `kai_statistics` under `src/`.
- Likely exposes a small API of functions/classes for statistical utilities.

Runtime model
- Library code intended to be imported by other projects or scripts.

Recommendations
- Add a brief architecture diagram describing modules and public API surface.
# Architecture

- **Type:** Python library / research toolbox (inferred from `pyproject.toml` name and dependencies).
- **Runtime model:** Library consumed by scripts or notebooks; no long-running service detected.

Findings:
- No `src/` or top-level package directory detected. Confirm where package modules live (expected `src/kai_statistics/` or `kai_statistics/`).

Recommended layout:
- `src/kai_statistics/` — package source
- `tests/` — test suite
- `notebooks/` or `examples/` — reproducible examples

Notes: Add module-level README and small example entrypoint to clarify intended usage.
