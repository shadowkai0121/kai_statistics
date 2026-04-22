# Structure

Repository layout
- `src/kai_statistics/` — package source
- `kai_statistics.egg-info/` — packaging metadata
- `pyproject.toml`, `README.md`, `LICENSE`

Conventions
- Uses src-layout which is recommended for modern packaging.

Suggested improvements
- Add `tests/` or `src/tests/` directory with unit tests.
- Add `docs/` or `docs/` using MkDocs/Sphinx if API docs are needed.
# Structure

Repository root contents:
- `pyproject.toml` — project metadata
- `README.md` — high-level project description
- `LICENSE` — license
- `.python-version` — pinned interpreter (3.12)
- `.gitignore`

Missing/expected but not found:
- `src/` or `kai_statistics/` — package source directory
- `tests/` — test directory
- CI configs (e.g., `.github/workflows/`)

Suggested minimal structure:
```
/ (repo root)
├─ pyproject.toml
├─ README.md
├─ LICENSE
├─ src/
│  └─ kai_statistics/
└─ tests/
```
