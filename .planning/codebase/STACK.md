# Stack

Overview
- Language: Python
- Packaging: setuptools/pyproject (has `pyproject.toml`)

Key components
- Source layout: `src/kai_statistics/` — package modules live under `src/`
- Distribution metadata: `kai_statistics.egg-info/` contains PKG-INFO and requires.txt

Dependencies
- Inspect `pyproject.toml` and `kai_statistics.egg-info/requires.txt` for declared dependencies.

Recommendations
- Document supported Python versions and runtime dependencies here.
- Consider adding `requirements.txt` for pinned installs if needed.
# Stack

- **Primary language:** Python
- **Package:** kai_statistics
- **Version:** 0.1.0
- **Python requirement:** >=3.12 (runtime pinned to 3.12)

Dependencies (from `pyproject.toml`):
- numpy>=2.0
- pandas>=2.2
- scipy>=1.13
- statsmodels>=0.14
- matplotlib>=3.8
- seaborn>=0.13
- jupyterlab>=4.2
- scikit-learn>=1.5
- gdown>=5.2

- **Packaging:** `pyproject.toml` (`tool.uv: package=true`)
- **Notes:** Project metadata is in `pyproject.toml`. No CI detected.
