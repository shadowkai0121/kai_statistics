---
phase: 01-library-infrastructure
plan: 03
subsystem: infra
tags: [python, pytest, github-actions, pypi, docs]
requires: [01-01, 01-02]
provides:
  - baseline pytest smoke and `_core` contract coverage
  - GitHub Actions test-build-publish automation for PyPI releases
  - contributor, installation, and maintainer setup guidance for notebook workflows
affects: [phase-02, contributor-workflow, release-automation, notebook-workflow]
tech-stack:
  added: []
  patterns:
    - pytest-based package-root and `_core` contract coverage
    - tag-gated GitHub Actions trusted publishing via uv
key-files:
  created:
    - tests/test_package.py
    - tests/_core/test_validation.py
    - tests/_core/test_results.py
    - .github/workflows/publish.yml
    - CONTRIBUTING.md
    - docs/installation.md
    - .planning/phases/01-library-infrastructure/01-REVIEW.md
    - .planning/phases/01-library-infrastructure/01-USER-SETUP.md
  modified:
    - pyproject.toml
    - README.md
    - src/kai_statistics/_core/validation.py
    - uv.lock
key-decisions:
  - "Kept Phase 1 tests lightweight and contract-oriented so future helper work can add statistical correctness tests incrementally."
  - "Used GitHub OIDC trusted publishing in `publish.yml` instead of repository-scoped PyPI secrets."
patterns-established:
  - "Local verification starts with `uv run pytest` against package-root smoke tests and `_core` contract tests."
  - "Release automation is tag-driven through `.github/workflows/publish.yml` and PyPI trusted publishing."
requirements-completed: [INFRA-03, INFRA-04, INFRA-05]
duration: 10 min
completed: 2026-04-22
---

# Phase 1 Plan 3: Testing, release automation, and contributor docs Summary

**Pytest smoke coverage, GitHub Actions trusted publishing, and notebook-focused contributor/install guidance for `kai_statistics`** 

## Performance

- **Duration:** 10 min
- **Started:** 2026-04-22T05:26:10Z
- **Completed:** 2026-04-22T05:35:59Z
- **Tasks:** 3
- **Files modified:** 13

## Accomplishments

- Added a runnable baseline test suite that covers the package root smoke path and the implemented `_core` validation/result contracts.
- Added a GitHub Actions workflow that runs `uv run pytest`, builds distributions with `uv build`, and publishes version tags to PyPI through trusted publishing.
- Added contributor, installation, and maintainer setup docs so future helper work and notebook installs follow the same conventions.

## Task Commits

Each task was committed atomically:

1. **Task 1: Add pytest configuration and baseline smoke coverage** - `f56650f` (test)
2. **Task 2: Create a GitHub Actions workflow for test-build-publish automation** - `35ecee5` (chore)
3. **Task 3: Write contributor and notebook-install documentation** - `d030655` (docs)

**Post-review hardening:** `d6edff4` (fix)

## Files Created/Modified

- `pyproject.toml` - Added the dev dependency group and pytest configuration for `uv run pytest`.
- `tests/test_package.py` - Covers the package-root import surface and `_hello()` smoke helper.
- `tests/_core/test_validation.py` - Verifies fail-fast `_core` dataframe, column, and missing-value policy behavior.
- `tests/_core/test_results.py` - Verifies `AnalysisResult` and `ResultCaveat` container behavior.
- `src/kai_statistics/_core/validation.py` - Hardened validator edge cases so malformed column labels and `allowed` containers still raise package-specific errors.
- `.github/workflows/publish.yml` - Runs tests on pushes/PRs and publishes tagged releases to PyPI with trusted publishing.
- `CONTRIBUTING.md` - Captures Phase 1 helper conventions, `_core` rules, defaults, return guidance, and test expectations.
- `docs/installation.md` - Documents editable setup, notebook installs, upgrades, and maintainer trusted-publisher prerequisites.
- `README.md` - Points readers to the dedicated contributor and installation guides.
- `uv.lock` - Refreshed lockfile after adding the dev dependency group used by the new pytest workflow.
- `.planning/phases/01-library-infrastructure/01-REVIEW.md` - Focused code-review artifact confirming the post-review hardening scope is clean.
- `.planning/phases/01-library-infrastructure/01-USER-SETUP.md` - Records the remaining PyPI dashboard configuration steps that require maintainer access.
- `.planning/phases/01-library-infrastructure/01-03-SUMMARY.md` - Execution record for this plan.

## Decisions Made

- Kept the initial test suite focused on smoke and contract coverage rather than pre-building Phase 2 statistical assertions before those helpers exist.
- Chose trusted publishing with GitHub OIDC so the repo never needs a long-lived PyPI token committed to secrets for routine releases.

## Command Checks

- **PASS:** `uv run pytest`
- **PASS:** `uv build`
- **PASS:** `uv run python -c "from pathlib import Path; workflow = Path('.github/workflows/publish.yml').read_text(encoding='utf-8'); required = ['workflow_dispatch:', 'push:', 'pull_request:', 'tags:', 'uv run pytest', 'uv build', 'actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5', 'actions/setup-python@a26af69be951a213d495a4c3e4e4022e16d87065', 'astral-sh/setup-uv@e58605a9b6da7c637471fab8847a5e5a6b8df081', 'pypa/gh-action-pypi-publish@cef221092ed1bacb1cc03d23a2d87d1d172e277b', 'id-token: write']; assert all(token in workflow for token in required)"`
- **PASS:** `uv run python -c "from pathlib import Path; contributing = Path('CONTRIBUTING.md').read_text(encoding='utf-8'); installation = Path('docs/installation.md').read_text(encoding='utf-8'); readme = Path('README.md').read_text(encoding='utf-8'); assert 'uv run pytest' in contributing; assert '_core' in contributing; assert 'import kai_statistics as ks' in contributing; assert 'ks.describe(df)' in contributing; assert 'AnalysisResult' in contributing; assert 'conservative defaults' in contributing; assert 'NumPy-style docstrings' in contributing; assert 'caveat' in contributing; assert 'pip install kai_statistics' in installation; assert 'publish.yml' in installation; assert 'CONTRIBUTING.md' in readme; assert 'docs/installation.md' in readme"`

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] Refreshed `uv.lock` while adding the pytest dev group**
- **Found during:** Task 1 (Add pytest configuration and baseline smoke coverage)
- **Issue:** Updating `pyproject.toml` to add the `dev` dependency group for pytest caused `uv` to refresh the lockfile so local installs and CI dependency resolution stayed consistent.
- **Fix:** Kept the generated `uv.lock` update alongside the planned `pyproject.toml` change instead of discarding it.
- **Files modified:** `pyproject.toml`, `uv.lock`
- **Verification:** `uv run pytest` passed against the refreshed environment, and the repo remained installable through `uv`.
- **Committed in:** `f56650f` (Task 1 commit)

---

**Total deviations:** 1 auto-fixed (1 blocking)
**Impact on plan:** The lockfile refresh was a necessary packaging side effect of the planned dev-tooling change. No extra product scope was introduced.

## Issues Encountered

- The original Wave 3 executor agent hit a runtime quota error after the three task commits were already on disk. The orchestrator finished the execute-plan metadata inline by validating the committed artifacts, creating `01-USER-SETUP.md`, and writing this summary.
- The first code-review pass surfaced two `_core` validator contract gaps and one workflow hardening issue. Those were fixed in `d6edff4`, then a focused re-review confirmed the scope is now clean.

## User Setup Required

**External services require manual configuration.** See [01-USER-SETUP.md](./01-USER-SETUP.md) for:
- PyPI project ownership confirmation
- Trusted-publisher registration for `.github/workflows/publish.yml`
- Pre-release dashboard checks

## Next Phase Readiness

- Ready for phase-level verification: Phase 1 now has its smoke suite, release workflow, and contributor/install guidance in place.
- Ready for Phase 2 planning and execution once Phase 1 verification passes.

## Self-Check: PASSED

- Confirmed all task artifacts and `.planning/phases/01-library-infrastructure/01-03-SUMMARY.md` exist on disk.
- Confirmed task commits `f56650f`, `35ecee5`, and `d030655` exist in git history.
- Confirmed the plan verification commands pass in the current workspace.

---
*Phase: 01-library-infrastructure*
*Completed: 2026-04-22*
