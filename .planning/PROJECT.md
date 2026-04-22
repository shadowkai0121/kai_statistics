# kai_statistics

## What This Is

kai_statistics is a local-first Python statistics toolbox for Kai's own notebook and research workflows. The package is meant to remove repetitive analysis setup by wrapping common tabular-data preparation, descriptive statistics, hypothesis testing, regression, and plotting tasks behind a consistent API. Version 0.1.0 starts from the current package scaffold and aims to become the default personal toolbox for everyday statistical work.

## Core Value

I can move from raw tabular data to a trustworthy statistical result quickly, using one local Python toolbox and minimal repetitive notebook code.

## Requirements

### Validated

(None yet - the repo has a package scaffold and dependencies, but no analysis features are validated in real use yet.)

### Active

- [ ] Establish the library infrastructure first: module layout, public API, shared validation, result objects, and test scaffolding.
- [ ] Build the core v0.1.0 analysis workflow on top of that foundation: data intake, descriptive statistics, inferential tests, regression helpers, and visual outputs.
- [ ] Keep data validation, result objects, and error messages consistent across helpers.
- [ ] Make outputs easy to reuse in notebooks, reports, and ad hoc research writeups.

### Out of Scope

- Web dashboard or GUI app - v0.1.0 is intentionally library-first and optimized for local Python workflows.
- Database orchestration or ETL pipelines - the first release should focus on working from local files and in-memory pandas objects.
- Deep learning or broad AutoML features - this project is a statistics toolbox, not a general machine learning platform.
- Collaboration, syncing, or cloud execution features - the toolbox is for single-user personal analysis.

## Context

- The repository already exists as a Python package with version `0.1.0` declared in `pyproject.toml`.
- The current dependency set points to a scientific Python workflow built on `numpy`, `pandas`, `scipy`, `statsmodels`, `matplotlib`, `seaborn`, `jupyterlab`, and `scikit-learn`.
- Source code currently contains only a minimal `src/kai_statistics/__init__.py` scaffold, so the first phase still needs to establish real module boundaries and public APIs.
- A `.planning/codebase/` map already exists, which confirms the repo is library-oriented and still missing tests, docs, and feature modules.
- The first milestone should front-load package infrastructure so later statistical helpers can share the same conventions instead of diverging early.
- This is a personal toolbox, so speed of analysis, ergonomics in notebooks, and trust in outputs matter more than building a polished public-facing product.

## Constraints

- **Tech stack**: Python 3.12 with the existing scientific stack - the current repo and dependency choices already anchor the implementation path.
- **Workflow**: Local-first, notebook-friendly usage - the toolbox needs to work naturally inside scripts and Jupyter notebooks.
- **Scope**: At most 3 roadmap phases for v0.1.0 - the project should stay compact enough to keep momentum.
- **Quality**: Prefer battle-tested library wrappers over custom statistical implementations - correctness and maintainability are more important than novelty.
- **Ownership**: Solo personal use - prioritize the fastest path to a dependable toolbox over team-process overhead.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Build v0.1.0 as a package-first library | The toolbox needs to be reusable across notebooks and scripts, not trapped inside one notebook file | - Pending |
| Standardize on pandas-oriented inputs and outputs where practical | Most personal analysis starts from tabular data, and pandas keeps the workflow ergonomic | - Pending |
| Wrap proven scientific Python libraries instead of reimplementing core methods | `scipy`, `statsmodels`, and friends already provide trusted statistical primitives | - Pending |
| Keep the first milestone within 3 phases | Smaller phase count will preserve momentum and reduce planning overhead for a solo project | - Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `$gsd-transition`):
1. Requirements invalidated? -> Move to Out of Scope with reason
2. Requirements validated? -> Move to Validated with phase reference
3. New requirements emerged? -> Add to Active
4. Decisions to log? -> Add to Key Decisions
5. "What This Is" still accurate? -> Update if drifted

**After each milestone** (via `$gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check - still the right priority?
3. Audit Out of Scope - reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-04-22 after initialization*
