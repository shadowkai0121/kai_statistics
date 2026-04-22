# Phase 01: Library Infrastructure - Pattern Map

**Mapped:** 2026-04-22
**Target files analyzed:** 16 (10 high-confidence, 6 discretionary)
**Analogs found:** 16 / 16 targets (strong self-analog: 2, package-level fallback: 14)

## Scope Notes

- 本文件依據 `01-CONTEXT.md` 的 D-01, D-03, D-09..D-19 與 `ROADMAP.md` 的 `01-01`..`01-03` plan slice 推定 Phase 1 需要修改或新增的檔案。
- 目前實際 repo 可用來抽 pattern 的檔案非常少：`src/kai_statistics/__init__.py`、`pyproject.toml`、`README.md`、`AGENTS.md`。
- `.planning/codebase/ARCHITECTURE.md` 與 `.planning/codebase/STRUCTURE.md` 仍保留初始化時的舊描述，和實際檔案樹不完全一致；本文件以實際 repo 掃描結果為準。
- 內部共享命名空間在 context 中尚未鎖定。本文件以 `_core/` 作為推薦路徑；若 planner 改選 `_shared/`，需整體一致更名。
- 這是 library-first 專案，不是 service/app。為了讓分類更貼近實際用途，資料流欄位額外使用 `module-export` 與 `reference` 兩個補充標籤。

## File Classification

| New/Modified File | Confidence | Role | Data Flow | Closest Analog | Match Quality | Notes |
|-------------------|------------|------|-----------|----------------|---------------|-------|
| `src/kai_statistics/__init__.py` | locked | provider | module-export | `src/kai_statistics/__init__.py` | exact | package root 會變成 notebook-facing public entry point |
| `src/kai_statistics/_core/__init__.py` | high | provider | module-export | `src/kai_statistics/__init__.py` | role-match | 推薦的內部共享命名空間初始化檔 |
| `src/kai_statistics/_core/errors.py` | high | utility | transform | `src/kai_statistics/__init__.py` | package-level fallback | 自訂錯誤階層，repo 目前沒有現成 analog |
| `src/kai_statistics/_core/validation.py` | high | utility | transform | `src/kai_statistics/__init__.py` | package-level fallback | 共用輸入驗證 helpers，repo 目前沒有現成 analog |
| `src/kai_statistics/_core/results.py` | high | model | transform | `src/kai_statistics/__init__.py` | package-level fallback | 輕量 result container / caveat carrier |
| `pyproject.toml` | locked | config | batch | `pyproject.toml` | exact | build metadata, test config, package metadata 的單一來源 |
| `tests/test_package.py` | high | test | request-response | `src/kai_statistics/__init__.py` | package-level fallback | import / smoke baseline |
| `.github/workflows/publish.yml` | high | config | batch | `pyproject.toml` | package-level fallback | workflow 檔可之後拆成 `ci.yml` + `publish.yml` |
| `CONTRIBUTING.md` | high | documentation | reference | `AGENTS.md` | package-level fallback | 推薦的 contributor / extension guide 路徑；實際檔名仍可調整 |
| `docs/installation.md` | medium | documentation | reference | `AGENTS.md` | package-level fallback | 推薦的 notebook / PyPI 安裝說明路徑；實際檔名仍可調整 |
| `src/kai_statistics/io.py` | medium | provider | module-export | `src/kai_statistics/__init__.py` | role-match | 僅在 planner 決定用 importable stub 表達 domain boundary 時建立 |
| `src/kai_statistics/profiling.py` | medium | provider | module-export | `src/kai_statistics/__init__.py` | role-match | 同上 |
| `src/kai_statistics/descriptive.py` | medium | provider | module-export | `src/kai_statistics/__init__.py` | role-match | 同上 |
| `src/kai_statistics/testing.py` | medium | provider | module-export | `src/kai_statistics/__init__.py` | role-match | 同上 |
| `tests/_core/test_validation.py` | medium | test | request-response | `src/kai_statistics/__init__.py` | package-level fallback | 僅在 `_core/validation.py` 同 phase 落地時一併建立 |
| `tests/_core/test_results.py` | medium | test | request-response | `src/kai_statistics/__init__.py` | package-level fallback | 僅在 `_core/results.py` 同 phase 落地時一併建立 |

## Pattern Assignments

### `src/kai_statistics/__init__.py` (provider, module-export)

**Analog:** `src/kai_statistics/__init__.py`

**Package surface pattern** (`src/kai_statistics/__init__.py` lines 1-5):
```python
"""kai_statistics package."""

__all__ = []

__version__ = "0.0.0"
```

**Smoke target pattern** (`src/kai_statistics/__init__.py` lines 7-9):
```python
def _hello():
    """Small helper to verify package import."""
    return "kai_statistics ready"
```

**Apply**
- 保留 package-level docstring、集中管理 `__all__`，並把 notebook-facing 的 public re-export 留在 package root。
- 現有 `_hello()` 只適合作為 smoke target；一旦真實 helper 上線，應優先用真實 public helper / re-export 取代更多私有 stub。

---

### `src/kai_statistics/_core/{__init__.py,errors.py,validation.py,results.py}` (provider / utility / model)

**Analog:** `src/kai_statistics/__init__.py`  
**Match quality:** package-level fallback only; repo 目前沒有任何內部模組、錯誤階層、validator、result object 可直接仿照

**Top-of-file module pattern** (`src/kai_statistics/__init__.py` lines 1-5):
```python
"""kai_statistics package."""

__all__ = []

__version__ = "0.0.0"
```

**Compact helper pattern** (`src/kai_statistics/__init__.py` lines 7-9):
```python
def _hello():
    """Small helper to verify package import."""
    return "kai_statistics ready"
```

**Conventions pattern** (`AGENTS.md` lines 21-27):
```md
## Conventions

- Keep the package library-first and notebook-friendly; notebooks should consume the package instead of holding the core logic.
- Prefer thin wrappers around proven scientific Python libraries instead of reimplementing standard statistical methods.
- Public APIs should accept pandas objects where practical, validate inputs early, and return predictable result structures.
- Use type hints and concise NumPy-style docstrings for public helpers.
- Add tests for numeric correctness, edge cases, and output-shape stability whenever new statistical helpers are introduced.
```

**Apply to specific files**
- `src/kai_statistics/_core/__init__.py`: 複製簡短 docstring + 明確 `__all__` 的 package init 風格，避免在內部 namespace 做太多邏輯。
- `src/kai_statistics/_core/errors.py`: 沒有現成 error hierarchy analog；應從零建立，但維持小而清楚的 public surface。
- `src/kai_statistics/_core/validation.py`: 沒有 validator analog；應偏向純函式、fail-fast、輸出錯誤訊息穩定。
- `src/kai_statistics/_core/results.py`: 沒有 result object analog；只在 metadata / caveat 真的需要時引入輕量容器，避免過度設計。

---

### Optional domain-boundary stubs: `src/kai_statistics/{io,profiling,descriptive,testing}.py`

**Analog:** `src/kai_statistics/__init__.py` + `AGENTS.md` architecture section  
**Match quality:** role-match for module shape, fallback for actual content

**Module file pattern** (`src/kai_statistics/__init__.py` lines 1-5):
```python
"""kai_statistics package."""

__all__ = []

__version__ = "0.0.0"
```

**Planned module-area pattern** (`AGENTS.md` lines 31-36):
```md
## Architecture

- `src/kai_statistics/` is the single library root.
- Planned v0.1.0 module areas: `io`, `profiling`, `descriptive`, `testing`, `modeling`, `plotting`, and shared `results` or `utils`.
- Shared validation and result objects should sit beneath analysis modules so outputs stay consistent across the toolbox.
- The current repo starts from a minimal package scaffold, so Phase 1 should establish the real module layout before broad feature work.
```

**Apply**
- 這些檔案只在 planner 決定「需要用可 import 的空 module 來表達 public boundary」時建立。
- Phase 1 不建議順手把 `modeling.py` / `plotting.py` 也一併預建。D-01 已明確要求優先共享基礎設施，而不是預先建立所有未來 domain package。
- 如果 planner 選擇「先只做 `_core/` + package root + docs 說明 boundary」，這組檔案可以整組延後。

---

### `tests/test_package.py`, `tests/_core/test_validation.py`, `tests/_core/test_results.py` (test, request-response)

**Analog:** `src/kai_statistics/__init__.py` for smoke target, `pyproject.toml` for repo-level packaging config  
**Match quality:** fallback only; repo 目前沒有任何 test 檔

**Import/smoke target** (`src/kai_statistics/__init__.py` lines 5-9):
```python
__version__ = "0.0.0"

def _hello():
    """Small helper to verify package import."""
    return "kai_statistics ready"
```

**Build/config source of truth** (`pyproject.toml` lines 24-29):
```toml
[build-system]
requires = ["uv_build >= 0.11.7, <0.12.0"]
build-backend = "uv_build"

[tool.uv]
package = true
```

**Apply**
- `tests/test_package.py`: 高信心必備，先覆蓋 `import kai_statistics as ks` 與 package-root smoke。
- `tests/_core/test_validation.py` / `tests/_core/test_results.py`: 只有在 `_core` 模組同步落地時才值得建立；否則 Phase 1 保持單一 smoke test 即可。
- 目前 repo 沒有 `pytest` pattern；測試樹應直接依 D-15 放在 top-level `tests/`，並盡量 mirror package structure。

---

### `pyproject.toml` and `.github/workflows/publish.yml` (config, batch)

**Analog:** `pyproject.toml`  
**Match quality:** `pyproject.toml` is exact for package metadata; workflow file has no direct analog

**Package metadata pattern** (`pyproject.toml` lines 1-9):
```toml
[project]
name = "kai_statistics"
version = "0.1.0"
authors = [
  { name="Kai Hsieh", email="shadowkai0121@gmail.com" },
]
description = "My statistical research toolbox"
readme = "README.md"
requires-python = ">=3.12"
```

**Dependency and build pattern** (`pyproject.toml` lines 10-29):
```toml
dependencies = [
  "numpy>=2.0",
  "pandas>=2.2",
  "scipy>=1.13",
  "statsmodels>=0.14",
  "matplotlib>=3.8",
  "seaborn>=0.13",
  "jupyterlab>=4.2",
  "scikit-learn>=1.5",
  "gdown>=5.2",
]
license = "MIT"
license-files = ["LICEN[CS]E*"]

[build-system]
requires = ["uv_build >= 0.11.7, <0.12.0"]
build-backend = "uv_build"

[tool.uv]
package = true
```

**Repository metadata pattern** (`pyproject.toml` lines 31-33):
```toml
[project.urls]
Homepage = "https://github.com/shadowkai0121/kai_statistics"
Issues = "https://github.com/shadowkai0121/kai_statistics/issues"
```

**Apply**
- `pyproject.toml`: 讓 package metadata、build backend、未來的 pytest config、可能的 optional dev groups 都集中在同一處。
- `.github/workflows/publish.yml`: repo 沒有任何現成 workflow 可仿；新 workflow 應以 `pyproject.toml` 為唯一 metadata 來源，呼叫 `uv` / build backend，而不是複寫 package 名稱、Python 版本、build 邏輯。
- 如果 planner 決定分成 `ci.yml` 與 `publish.yml`，也應共享同一套 `uv` + `pyproject.toml` build path，不要再引入第二套 package config。

---

### `CONTRIBUTING.md` and `docs/installation.md` (documentation, reference)

**Analog:** `AGENTS.md` for section structure, `README.md` for top-level title style  
**Match quality:** fallback only; repo 沒有任何專門的 contributor/install doc

**Title / one-line summary pattern** (`README.md` lines 1-2):
```md
# kai_statistics
我的統計工具庫
```

**Section + flat-bullet pattern** (`AGENTS.md` lines 21-27):
```md
## Conventions

- Keep the package library-first and notebook-friendly; notebooks should consume the package instead of holding the core logic.
- Prefer thin wrappers around proven scientific Python libraries instead of reimplementing standard statistical methods.
- Public APIs should accept pandas objects where practical, validate inputs early, and return predictable result structures.
- Use type hints and concise NumPy-style docstrings for public helpers.
- Add tests for numeric correctness, edge cases, and output-shape stability whenever new statistical helpers are introduced.
```

**Architecture reminder pattern** (`AGENTS.md` lines 31-36):
```md
## Architecture

- `src/kai_statistics/` is the single library root.
- Planned v0.1.0 module areas: `io`, `profiling`, `descriptive`, `testing`, `modeling`, `plotting`, and shared `results` or `utils`.
- Shared validation and result objects should sit beneath analysis modules so outputs stay consistent across the toolbox.
- The current repo starts from a minimal package scaffold, so Phase 1 should establish the real module layout before broad feature work.
```

**Apply**
- `CONTRIBUTING.md`: 放 helper conventions、模組佈局、擴充規則，避免把 extension guidance 混回 `README.md`。
- `docs/installation.md`: 放 PyPI / notebook install 與 release 使用方式；保留 `README.md` 短而可掃描。
- 目前 repo 沒有 docs style guide；最接近的既有 pattern 就是 `AGENTS.md` 的短 section + 平鋪 bullet 結構。

## Shared Patterns

### Python module skeleton
**Source:** `src/kai_statistics/__init__.py`
**Apply to:** `src/kai_statistics/_core/__init__.py`, `src/kai_statistics/_core/errors.py`, `src/kai_statistics/_core/validation.py`, `src/kai_statistics/_core/results.py`, optional domain-boundary stubs
```python
"""kai_statistics package."""

__all__ = []
```

### Package root as the public notebook-facing surface
**Source:** `src/kai_statistics/__init__.py`
**Apply to:** `src/kai_statistics/__init__.py`, `tests/test_package.py`
```python
__version__ = "0.0.0"

def _hello():
    """Small helper to verify package import."""
    return "kai_statistics ready"
```

### Build metadata as the single source of truth
**Source:** `pyproject.toml`
**Apply to:** `pyproject.toml`, `.github/workflows/publish.yml`
```toml
[build-system]
requires = ["uv_build >= 0.11.7, <0.12.0"]
build-backend = "uv_build"

[tool.uv]
package = true
```

### Markdown docs use short sections and flat bullets
**Source:** `AGENTS.md`, `README.md`
**Apply to:** `CONTRIBUTING.md`, `docs/installation.md`
```md
## Conventions

- Keep the package library-first and notebook-friendly; notebooks should consume the package instead of holding the core logic.
- Prefer thin wrappers around proven scientific Python libraries instead of reimplementing standard statistical methods.
```

### Honest gap handling
- 目前 repo 沒有錯誤階層、validator、result object、tests、GitHub Actions workflow 的既有實作。
- Planner 應把這些視為「新 pattern 要首次定義」，不是硬湊成 repo 內已存在的慣例。

## No Strong Analog

| File | Role | Data Flow | Reason | Nearest fallback pattern |
|------|------|-----------|--------|--------------------------|
| `src/kai_statistics/_core/errors.py` | utility | transform | repo 沒有任何 exception hierarchy | `src/kai_statistics/__init__.py` module skeleton |
| `src/kai_statistics/_core/validation.py` | utility | transform | repo 沒有 validator helpers | `src/kai_statistics/__init__.py` module skeleton + `AGENTS.md` conventions |
| `src/kai_statistics/_core/results.py` | model | transform | repo 沒有 result containers | `src/kai_statistics/__init__.py` module skeleton + `AGENTS.md` conventions |
| `tests/test_package.py` | test | request-response | repo 沒有 tests | `src/kai_statistics/__init__.py` smoke target |
| `tests/_core/test_validation.py` | test | request-response | repo 沒有 tests，也沒有 validation tests 可 mirror | `src/kai_statistics/__init__.py` smoke target |
| `tests/_core/test_results.py` | test | request-response | repo 沒有 tests，也沒有 result tests 可 mirror | `src/kai_statistics/__init__.py` smoke target |
| `.github/workflows/publish.yml` | config | batch | repo 沒有 CI/CD workflow | `pyproject.toml` build metadata |
| `CONTRIBUTING.md` | documentation | reference | repo 只有 `README.md` 與 `AGENTS.md`，沒有 contributor docs | `AGENTS.md` section structure |
| `docs/installation.md` | documentation | reference | repo 沒有 installation doc | `AGENTS.md` section structure + `README.md` title style |
| `src/kai_statistics/io.py` | provider | module-export | repo 沒有 domain-boundary module stubs | `src/kai_statistics/__init__.py` module skeleton |
| `src/kai_statistics/profiling.py` | provider | module-export | 同上 | `src/kai_statistics/__init__.py` module skeleton |
| `src/kai_statistics/descriptive.py` | provider | module-export | 同上 | `src/kai_statistics/__init__.py` module skeleton |
| `src/kai_statistics/testing.py` | provider | module-export | 同上 | `src/kai_statistics/__init__.py` module skeleton |

## Metadata

**Analog search scope:** repo root (`pyproject.toml`, `README.md`, `AGENTS.md`), `src/kai_statistics/`, plus `.planning/codebase/` docs for context sanity-check only  
**Files scanned:** 18 direct file reads + repo inventory scan  
**Pattern extraction date:** 2026-04-22
