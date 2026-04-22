<!-- GSD:project-start source:PROJECT.md -->
## Project

- `kai_statistics` is a local-first Python statistics toolbox for Kai's own notebook and research workflows.
- v0.1.0 focuses on package infrastructure first, then data intake, descriptive statistics, inferential testing, regression helpers, plotting, and export utilities.
- Core value: move from raw tabular data to a trustworthy result quickly with minimal repetitive notebook code.
- The initial roadmap is intentionally capped at 3 phases to keep execution compact and focused.
<!-- GSD:project-end -->

<!-- GSD:stack-start source:STACK.md -->
## Technology Stack

- Python 3.12 with src-layout packaging
- Build and packaging via `uv` and `pyproject.toml`
- Core analysis libraries: `numpy`, `pandas`, `scipy`, `statsmodels`, `scikit-learn`
- Visualization libraries: `matplotlib`, `seaborn`
- Notebook workflow: `jupyterlab`
<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->
## Conventions

- Keep the package library-first and notebook-friendly; notebooks should consume the package instead of holding the core logic.
- Prefer thin wrappers around proven scientific Python libraries instead of reimplementing standard statistical methods.
- Public APIs should accept pandas objects where practical, validate inputs early, and return predictable result structures.
- Use type hints and concise NumPy-style docstrings for public helpers.
- Add tests for numeric correctness, edge cases, and output-shape stability whenever new statistical helpers are introduced.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->
## Architecture

- `src/kai_statistics/` is the single library root.
- Planned v0.1.0 module areas: `io`, `profiling`, `descriptive`, `testing`, `modeling`, `plotting`, and shared `results` or `utils`.
- Shared validation and result objects should sit beneath analysis modules so outputs stay consistent across the toolbox.
- The current repo starts from a minimal package scaffold, so Phase 1 should establish the real module layout before broad feature work.
<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->
## Project Skills

No project skills found yet. If this repo gains project-local skills, place them under `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, or `.github/skills/`.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `$gsd-quick` for small fixes, doc updates, and ad hoc tasks
- `$gsd-debug` for investigation and bug fixing
- `$gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->

<!-- GSD:profile-start -->
## Developer Profile

> Profile not yet configured. Run `$gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` and should not be edited manually.
<!-- GSD:profile-end -->
