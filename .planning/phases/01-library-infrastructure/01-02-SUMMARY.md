---
phase: 01-library-infrastructure
plan: 02
subsystem: infra
tags: [python, pandas, validation, errors, dataclasses]
requires: [01-01]
provides:
  - internal `_core` namespace with package-specific errors
  - fail-fast dataframe, column, and missing-value policy validation helpers
  - lightweight result containers with metadata and caveat defaults
affects: [phase-02, helper-contracts, notebook-workflow]
tech-stack:
  added: []
  patterns:
    - explicit internal `_core` exports via `__all__`
    - fail-fast validation with package-specific exceptions
    - lightweight dataclass result containers for multi-part outputs
key-files:
  created:
    - src/kai_statistics/_core/errors.py
    - src/kai_statistics/_core/validation.py
    - src/kai_statistics/_core/results.py
  modified:
    - src/kai_statistics/_core/__init__.py
key-decisions:
  - "Kept `_core` internal-only and avoided any package-root re-export from `src/kai_statistics/__init__.py`."
  - "Made validation helpers return validated inputs or policies so future helpers can chain one shared fail-fast path."
patterns-established:
  - "`kai_statistics._core` owns shared errors, validators, and result containers behind explicit imports."
  - "Future helper modules can rely on `InputValidationError` and `MissingValueHandlingError` instead of ad hoc exceptions."
requirements-completed: [INFRA-02]
duration: 4 min
completed: 2026-04-22
---

# Phase 1 Plan 2: Internal `_core` conventions Summary

**Internal `_core` error hierarchy, fail-fast pandas validation helpers, and metadata-aware result containers for future analysis modules**

## Performance

- **Duration:** 4 min
- **Started:** 2026-04-22T05:15:08Z
- **Completed:** 2026-04-22T05:19:22Z
- **Tasks:** 3
- **Files modified:** 8

## Accomplishments

- Added a package-specific error hierarchy rooted at `KaiStatisticsError` for future shared validation and result-contract failures.
- Implemented dataframe, required-column, and explicit missing-value policy validation helpers under the internal `_core` namespace.
- Added lightweight `AnalysisResult` and `ResultCaveat` dataclasses so future helpers can attach metadata and caveats without inventing new output shapes.

## Task Commits

Each task was committed atomically:

1. **Task 1: Create the internal error hierarchy and `_core` export surface** - `bca1884` (feat)
2. **Task 2: Implement fail-fast validation helpers for dataframe inputs** - `480471f` (feat)
3. **Task 3: Add lightweight result containers for metadata and caveats** - `804bb36` (feat)

## Files Created/Modified

- `src/kai_statistics/_core/__init__.py` - Internal export surface for shared errors, validation helpers, and result containers.
- `src/kai_statistics/_core/errors.py` - Package-specific exception hierarchy for validation and result contract failures.
- `src/kai_statistics/_core/validation.py` - Fail-fast dataframe, column, and missing-value policy validators.
- `src/kai_statistics/_core/results.py` - Lightweight dataclass containers for metadata-rich results and non-fatal caveats.
- `.planning/phases/01-library-infrastructure/01-02-SUMMARY.md` - Execution record for this plan.
- `.planning/STATE.md` - Updated current plan position, metrics, decisions, and session continuity.
- `.planning/ROADMAP.md` - Updated Phase 1 progress after this plan completed.
- `.planning/REQUIREMENTS.md` - Marked `INFRA-02` complete.

## Decisions Made

- Kept `_core` internal and explicit: the new primitives are importable from `kai_statistics._core`, but the package root remains unchanged so Phase 1 does not accidentally promise these internals as public API.
- Made `ensure_columns_present` validate the dataframe input itself and return the validated frame, which gives future helpers one consistent fail-fast entry point instead of relying on call-order assumptions.

## Command Checks

- **PASS:** `uv run python -c "from kai_statistics._core import AnalysisResult, InputValidationError, KaiStatisticsError, MissingValueHandlingError, ResultCaveat, ResultContractError, ensure_columns_present, ensure_dataframe, require_explicit_na_policy; print('core-ready')"` -> printed `core-ready`
- **PASS:** `uv run python -c "from kai_statistics._core import AnalysisResult, InputValidationError, KaiStatisticsError, MissingValueHandlingError, ResultCaveat, ResultContractError, ensure_columns_present, ensure_dataframe, require_explicit_na_policy; assert KaiStatisticsError.__name__ == 'KaiStatisticsError'; assert ResultContractError.__name__ == 'ResultContractError'; assert callable(ensure_dataframe); assert callable(require_explicit_na_policy)"`
- **PASS:** `uv run python -c "import pandas as pd; from kai_statistics._core import InputValidationError, MissingValueHandlingError, ensure_columns_present, ensure_dataframe, require_explicit_na_policy; failures = 0; checks = ((lambda: ensure_dataframe([]), InputValidationError), (lambda: ensure_columns_present(pd.DataFrame({'x':[1]}), ['y']), InputValidationError), (lambda: require_explicit_na_policy(None, ('drop','keep','error')), MissingValueHandlingError)); for fn, exc in checks: ...; assert failures == 3"`
- **PASS:** `uv run python -c "from kai_statistics._core import AnalysisResult; result = AnalysisResult(value='ok'); assert isinstance(result.metadata, dict); assert result.metadata == {}; assert isinstance(result.caveats, list); assert result.caveats == []"`
- **PASS:** `rg --line-number "KaiStatisticsError|InputValidationError|MissingValueHandlingError|ResultContractError|ResultCaveat|AnalysisResult" src/kai_statistics/_core`

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

- `gsd-sdk` was not installed in PATH on this machine. Execution used the workflow-compatible fallback `node C:/Users/asus/.codex/get-shit-done/bin/gsd-tools.cjs ...` for state, roadmap, requirement, and summary verification commands.
- `gsd-tools` updated `STATE.md` frontmatter and requirement status correctly, but left stale rendered progress text in `STATE.md` and the Phase 1 progress row in `ROADMAP.md`. Those rendered sections were corrected manually to match the verified disk state after this plan completed.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Ready for `01-03`: the package now has one internal namespace for shared errors, validation, and metadata-rich result contracts.
- No code blockers remain for this plan. The main remaining Phase 1 work is test scaffolding, publish automation, and contributor/install documentation.

## Self-Check: PASSED

- Confirmed `src/kai_statistics/_core/__init__.py`, `errors.py`, `validation.py`, `results.py`, and `.planning/phases/01-library-infrastructure/01-02-SUMMARY.md` exist on disk.
- Confirmed task commits `bca1884`, `480471f`, and `804bb36` exist in git history.
- `node C:/Users/asus/.codex/get-shit-done/bin/gsd-tools.cjs verify-summary .planning/phases/01-library-infrastructure/01-02-SUMMARY.md` passes after adding this section.

---
*Phase: 01-library-infrastructure*
*Completed: 2026-04-22*
