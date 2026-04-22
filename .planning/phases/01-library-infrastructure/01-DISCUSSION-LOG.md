# Phase 1: Library Infrastructure - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-04-22
**Phase:** 01-library-infrastructure
**Mode:** discuss
**Areas discussed:** Module boundaries and import style, Public API style, Validation/error/result conventions, Testing/release/extension scaffolding

---

## Module Boundaries and Import Style

| Question | Options Considered | Selected |
|--------|-------------|----------|
| Future domain skeleton scope | Shared infrastructure only now; all v0.1.0 domain packages with placeholders; all domain directories with stubs but no fake helpers | Shared infrastructure only now |
| Package-root role | Thin metadata-only root; top-level re-export of common helpers; mixed approach | Top-level convenience entry point with future re-exports |
| Shared-infrastructure namespace | Public validation/results/errors modules; internal `_core` or `_shared`; everything in `utils` | Internal shared namespace |
| Early helper file organization | One helper area per file; fewer larger files first; add `contrib` or `experimental` areas | Fewer larger files first |
| Import experience | Convenience alias import; submodule-first import; no preference | `import kai_statistics as ks` |

**User's choice:** Keep Phase 1 focused on shared infrastructure, preserve a notebook-friendly package root, and avoid locking internal helper modules into the public API too early.
**Notes:** The top-level package should become the convenient user-facing import surface, but internal shared utilities can stay private while the toolbox is still taking shape.

---

## Public API Style

| Question | Options Considered | Selected |
|--------|-------------|----------|
| Calling style | Short function-first API; explicit submodule namespace API; mixed approach | Short function-first API |
| Argument style | Direct pandas objects and column names; explicit structured config objects; mixed approach | Direct pandas objects and column names |
| Output shape | Prefer pandas-native outputs; always wrap in custom result objects; mixed outputs with wrapper metadata | Prefer pandas-native outputs |
| Naming style | Very short names; fully explicit names; short-by-default and explicit when needed | Short-by-default and explicit when needed |
| Default behavior | Aggressive convenience defaults; conservative defaults; balanced defaults | Conservative defaults |

**User's choice:** Make helpers feel fast and direct in notebooks, but avoid hiding important statistical assumptions behind overly smart defaults.
**Notes:** The package should support concise calls like `ks.describe(df)` while still remaining explicit when naming or parameter choices would otherwise become ambiguous.

---

## Validation, Error, and Result Conventions

| Question | Options Considered | Selected |
|--------|-------------|----------|
| Invalid inputs | Shared validation with fail-fast errors; try coercion first; best-effort warnings | Shared validation with fail-fast errors |
| Missing-value policy | Require explicit missing-value handling; conservative automatic defaults; let helpers auto-repair | Require explicit missing-value handling |
| Error hierarchy | Custom package error hierarchy; mostly built-in Python errors; mixed built-in and downstream-library errors | Custom package error hierarchy |
| Metadata strategy | Always return pandas only; attach metadata into pandas attrs; pandas for simple cases plus lightweight result objects when needed | Mixed strategy with lightweight result objects only when needed |
| Risky-but-valid situations | Raise immediately; proceed with explicit warnings; continue silently | Proceed with explicit warnings |

**User's choice:** Favor strict validation and explicit error handling, while allowing statistically risky situations to proceed when they are surfaced with clear warnings or caveats.
**Notes:** This keeps the toolbox trustworthy without forcing every multi-part analysis into a heavyweight custom return type.

---

## Testing, Release, and Extension Scaffolding

| Question | Options Considered | Selected |
|--------|-------------|----------|
| Test runner | `pytest` via `uv`; `unittest`; no strong runner preference | `pytest` via `uv run pytest` |
| Test layout | Top-level `tests/` mirroring src layout; colocated tests; single smoke-test file first | Top-level `tests/` mirroring src layout |
| Phase 1 coverage baseline | Import and smoke tests only; smoke tests plus validation/result-contract tests; also scaffold Phase 2 helper tests | Import and smoke tests only |
| Extension guidance location | Dedicated contributor/extension guide; put everything in README; no written guidance yet | Dedicated contributor/extension guide |
| Helper-template support | Module/test template plus checklist; written conventions only; scaffold script | Written conventions only |
| Release automation scope | Keep GitHub Actions publishing deferred; fold GitHub Actions PyPI publishing into Phase 1 | Fold GitHub Actions PyPI publishing into Phase 1 |

**User's choice:** Establish a lightweight but real testing baseline, keep extension guidance in dedicated docs, and include GitHub Actions-based PyPI publishing inside Phase 1.
**Notes:** The release workflow is now part of the same scaffolding phase because notebook installation from published releases is a required part of the intended user workflow.

---

## the agent's Discretion

- Exact internal shared-module names.
- Exact top-level helper re-export list as real helpers land.
- Exact GitHub Actions job breakdown for test vs publish steps.
- Exact filenames and locations for contributor/install guidance documents.

## Deferred Ideas

None.
