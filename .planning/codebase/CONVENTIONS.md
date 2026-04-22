# Conventions

Coding style
- No explicit style configuration found (`.flake8`, `pyproject.toml` may contain settings).

Packaging conventions
- Uses `pyproject.toml` and produced egg-info metadata — follow PEP 517/518 for builds.

Recommendations
- Add a linter config (e.g., `.flake8` or `pyproject.toml` `[tool.black]`) and pre-commit.
# Conventions

- **Style:** Follow PEP 8. Use `black` and `isort` for consistent formatting.
- **Typing:** Prefer gradual type hints; use `typing` for public APIs.
- **Docstrings:** Use NumPy or Google style for scientific code.
- **Dependencies:** Pin minimal compatible versions in `pyproject.toml`.
- **Commits:** Use short, imperative commit messages; consider Conventional Commits for automation.

Add `pyproject.toml` sections for `tool.black`, `tool.isort`, and `tool.flake8` to lock formatting rules.
