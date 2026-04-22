# Phase 1: Library Infrastructure - Context

**Gathered:** 2026-04-22
**Status:** Ready for planning

<domain>
## Phase Boundary

Establish the real package surface for `kai_statistics`, including shared validation/error/result conventions, baseline test scaffolding, contributor guidance, and GitHub Actions-based PyPI publishing so notebook environments can install released versions. Delivering real data-prep, descriptive, testing, or modeling helpers remains out of scope for this phase.

</domain>

<decisions>
## Implementation Decisions

### Package Surface and Module Boundaries
- **D-01:** Phase 1 should prioritize shared infrastructure instead of pre-creating every future analysis domain package.
- **D-02:** `src/kai_statistics/__init__.py` should evolve into a convenience entry point that can re-export common helpers while preserving the `import kai_statistics as ks` workflow.
- **D-03:** Shared infrastructure should live under internal namespaces (for example `_core` or `_shared`) rather than being promised immediately as stable public modules.
- **D-04:** New helpers may start in a few larger module files and split later once the public surface is clearer.

### Public API Design
- **D-05:** Public helpers should prefer short top-level function calls such as `ks.describe(df)` and `ks.ttest(...)`.
- **D-06:** Helper signatures should accept pandas objects and column-name strings directly where practical.
- **D-07:** Helper names should stay short when they remain clear, but may become more explicit when necessary to avoid ambiguity.
- **D-08:** Default behavior should remain conservative and must not hide important statistical assumptions behind aggressive convenience defaults.

### Validation, Errors, and Outputs
- **D-09:** Helpers should perform shared input validation up front and fail fast on missing columns, invalid shapes, or incompatible types.
- **D-10:** Missing-value handling must be explicit; helpers should not silently drop or impute values by default.
- **D-11:** Package-level errors should be anchored by a custom base exception such as `KaiStatisticsError`, with specific subclasses added as needed.
- **D-12:** Simple analyses may return pandas-native outputs directly, but multi-part analyses may use lightweight result objects when metadata or secondary outputs matter.
- **D-13:** Risky-but-not-invalid situations such as small samples, unstable assumptions, or constant columns should surface warnings or caveats instead of failing silently.

### Testing, Release, and Extension Scaffolding
- **D-14:** The baseline test runner should be `pytest`, with `uv run pytest` as the standard invocation.
- **D-15:** Tests should live in a top-level `tests/` directory that mirrors the package structure.
- **D-16:** Phase 1 test coverage only needs import and smoke tests; deeper helper contract tests can grow with real features.
- **D-17:** Extension guidance should live in a dedicated contributor-oriented document instead of the top-level README.
- **D-18:** Phase 1 should provide written helper conventions rather than copy-paste templates or scaffold generators.
- **D-19:** GitHub Actions-based PyPI publishing is part of Phase 1 so released versions can be installed from Jupyter notebook environments.

### the agent's Discretion
- Exact internal shared-module naming, such as `_core`, `_shared`, or equivalent.
- Exact set of top-level helper re-exports introduced as real helpers land.
- Exact split of test and release jobs inside the GitHub Actions workflow.
- Exact filenames and locations for contributor, extension, and install guidance documents.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Phase Scope and Requirements
- `.planning/ROADMAP.md` — Phase 1 scope, plan slices, success criteria, and the added release-automation requirement.
- `.planning/REQUIREMENTS.md` — Locked Phase 1 requirements, including `INFRA-01` through `INFRA-05`.
- `.planning/PROJECT.md` — Library-first, notebook-friendly, local-first product constraints and core value.
- `.planning/STATE.md` — Current progress, active focus, and known blockers/concerns.

### Codebase Structure and Conventions
- `.planning/codebase/ARCHITECTURE.md` — Expected module areas and the package-root architecture direction.
- `.planning/codebase/CONVENTIONS.md` — Typing, docstring, packaging, and code-style expectations for public helpers.
- `.planning/codebase/STACK.md` — Python 3.12, `uv`, and the scientific Python dependency stack.
- `.planning/codebase/STRUCTURE.md` — Current src-layout structure and missing scaffolding.
- `.planning/codebase/TESTING.md` — Current absence of tests and the recommended `pytest` baseline.

### Build and Package Entry Points
- `pyproject.toml` — Package metadata, Python requirement, build backend, and runtime dependencies.
- `src/kai_statistics/__init__.py` — Current package-root implementation and import smoke target.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `pyproject.toml`: Already defines package metadata, Python 3.12 support, `uv_build`, and the scientific dependency baseline that release automation should build from.
- `src/kai_statistics/__init__.py`: Existing package-root file can become both the import smoke-test target and the future top-level helper export surface.
- `.planning/codebase/*.md`: Existing codebase maps already document structure, stack, architecture, and testing gaps, so planning can build on them instead of rescanning from scratch.

### Established Patterns
- The repository already uses src-layout packaging under `src/kai_statistics/`.
- The project is intentionally library-first and notebook-friendly, so API ergonomics for direct import and pandas-first usage matter more than service-style abstractions.
- The current repo has no test suite yet, which makes Phase 1 responsible for establishing the testing baseline rather than extending an existing pattern.

### Integration Points
- Shared validation, errors, and lightweight result objects should sit beneath future helper modules so Phase 2 analysis helpers can reuse them.
- The package root should become the main notebook-facing import surface as real helpers are added.
- GitHub Actions publishing should integrate with the existing `pyproject.toml` metadata and build backend so released artifacts match the local packaging flow.

</code_context>

<specifics>
## Specific Ideas

- The package should feel natural as `import kai_statistics as ks`.
- The preferred helper experience is short top-level calls such as `ks.describe(df)` and `ks.ttest(...)`.
- Released versions should be installable from Jupyter notebook environments through PyPI.

</specifics>

<deferred>
## Deferred Ideas

None — discussion stayed within the Phase 1 boundary after explicitly folding release automation into scope.

</deferred>

---

*Phase: 01-library-infrastructure*
*Context gathered: 2026-04-22*
