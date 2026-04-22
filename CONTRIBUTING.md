# Contributing to kai_statistics

## Phase 1 Layout

- `src/kai_statistics/__init__.py` is the notebook-facing package root and the only place that should expose public top-level helpers for `import kai_statistics as ks`.
- `src/kai_statistics/io.py`, `profiling.py`, `descriptive.py`, and `testing.py` define the Phase 1 public domain boundaries without promising placeholder helper APIs.
- `src/kai_statistics/_core/` is internal-only. Shared errors, validation helpers, and result containers may be imported inside the package, but `_core` modules should not be re-exported from the package root by default.
- `tests/` mirrors the package structure. Keep smoke coverage in `tests/test_package.py` and module-specific contracts under matching subdirectories such as `tests/_core/`.

## Public Helper Style

- Future notebook-facing helpers should remain short and direct at the package root, for example `ks.describe(df)` or `ks.ttest(...)`.
- Keep names short when they stay clear. Make them more explicit only when ambiguity would hide the statistical intent.
- Do not add placeholder top-level helpers before the implementation is real and tested.

## Defaults, Inputs, and Returns

- Use conservative defaults. Helper behavior must not hide statistical assumptions, silently change test settings, or drop missing values without an explicit user choice.
- Public helpers should accept pandas inputs where practical so notebook code can pass `DataFrame`, `Series`, and column labels directly.
- Return pandas-native objects for simple tabular outputs that users will immediately inspect or chain.
- Return `AnalysisResult` when a helper needs to bundle a primary value with metadata, secondary artifacts, or caveats that should travel together.

## Caveats and Errors

- Fail fast on invalid inputs, unsupported shapes, missing required columns, or unspecified missing-value handling.
- Reuse the shared `_core` validation and error conventions instead of ad hoc exceptions:
  - `ensure_dataframe(...)`
  - `ensure_columns_present(...)`
  - `require_explicit_na_policy(...)`
  - `KaiStatisticsError` and its specific subclasses
- Raise an exception when the requested computation is invalid or cannot be trusted.
- Surface a caveat or warning when the computation is still valid but needs interpretation context, such as small samples, constant columns, or borderline assumptions.

## Documentation and Typing

- Public helpers require type hints.
- Public helpers require concise NumPy-style docstrings.
- Document parameter expectations, return shape, and any caveat conditions close to the implementation.

## Testing

- Run `uv run pytest` before opening or merging changes.
- Add tests for numeric correctness, edge cases, and output-shape stability whenever a new statistical helper is introduced.
- Keep smoke tests lightweight, then add focused contract coverage near the helper module that changed.
