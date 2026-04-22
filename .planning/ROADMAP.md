# Roadmap: kai_statistics

## Overview

Version 0.1.0 turns the current package scaffold into a dependable personal statistics toolbox. The roadmap is intentionally compressed into 3 phases so the project can stay focused: first build the package and release infrastructure, then deliver core analysis features, and finally add modeling, visualization, exports, and end-to-end workflow examples.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions if needed later

- [ ] **Phase 1: Library Infrastructure** - Establish the package surface, shared conventions, testing scaffolding, release automation, and extension patterns.
- [ ] **Phase 2: Core Statistical Analysis** - Add data preparation, descriptive analysis, and classical hypothesis testing on top of the shared foundations.
- [ ] **Phase 3: Modeling and Workflow Delivery** - Add regression helpers, reusable visual outputs, exports, and documented examples.

## Phase Details

### Phase 1: Library Infrastructure
**Goal**: Build the real module boundaries for `kai_statistics`, define consistent helper conventions, and create the testing, release, and extension scaffolding the rest of the toolbox will rely on.
**Depends on**: Nothing (first phase)
**Requirements**: INFRA-01, INFRA-02, INFRA-03, INFRA-04, INFRA-05
**Success Criteria** (what must be TRUE):
  1. User can import the package and discover stable module boundaries for future analysis helpers.
  2. Implemented helpers can share input validation, error conventions, and result-object patterns instead of ad hoc logic.
  3. User can run a baseline automated test suite and follow a documented pattern for extending the package.
  4. User can publish the package through GitHub Actions to PyPI and install released versions from Jupyter notebook environments.
**Plans**: 3 plans

Plans:
- [x] 01-01: Establish the package layout, public exports, and module boundaries for current and future analysis domains.
- [ ] 01-02: Implement shared validation utilities, error conventions, and result container patterns.
- [ ] 01-03: Add test scaffolding, smoke tests, GitHub Actions-based PyPI publishing, and contributor-oriented extension/install guidance.

### Phase 2: Core Statistical Analysis
**Goal**: Deliver the first real analysis capabilities on top of the infrastructure layer: data preparation, descriptive summaries, and common classical hypothesis tests.
**Depends on**: Phase 1
**Requirements**: DATA-01, DATA-02, DATA-03, DESC-01, DESC-02, DESC-03, TEST-01, TEST-02, TEST-03
**Success Criteria** (what must be TRUE):
  1. User can load, profile, and prepare tabular data through toolbox helpers instead of custom notebook setup code.
  2. User can generate descriptive summaries, grouped summaries, and correlation outputs that preserve labels and are ready for reuse.
  3. User can run common hypothesis tests and receive interpretable outputs through the conventions established in Phase 1.
**Plans**: 3 plans

Plans:
- [ ] 02-01: Implement file loading, dataset profiling, and subset-preparation helpers.
- [ ] 02-02: Implement descriptive summary, grouped summary, and correlation helpers.
- [ ] 02-03: Implement t-test, chi-square, and ANOVA helpers with consistent outputs.

### Phase 3: Modeling and Workflow Delivery
**Goal**: Finish the v0.1.0 experience with regression helpers, reusable charts, exports, and a documented end-to-end notebook workflow.
**Depends on**: Phase 2
**Requirements**: MODL-01, MODL-02, WORK-01, VIZ-01, VIZ-02, VIZ-03
**Success Criteria** (what must be TRUE):
  1. User can fit OLS and logistic models through the same package conventions used elsewhere in the toolbox.
  2. User can turn analysis outputs into charts and exported artifacts with minimal notebook boilerplate.
  3. User can follow at least one documented example that shows the intended v0.1.0 flow from raw data to final result artifact.
**Plans**: 3 plans

Plans:
- [ ] 03-01: Implement OLS and logistic regression helpers plus core diagnostics wrappers.
- [ ] 03-02: Implement plotting and export helpers for statistical outputs.
- [ ] 03-03: Add notebook-ready examples and usage documentation for the complete workflow.

## Progress

**Execution Order:**
Phases execute in numeric order: 1 -> 2 -> 3

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Library Infrastructure | 1/3 | In Progress|  |
| 2. Core Statistical Analysis | 0/3 | Not started | - |
| 3. Modeling and Workflow Delivery | 0/3 | Not started | - |
