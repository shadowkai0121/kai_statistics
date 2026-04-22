# Installation

## Local Editable Setup

Use `uv` for local development. `uv sync --group dev` installs the project in editable mode together with the baseline test tooling declared in `pyproject.toml`.

```bash
uv sync --group dev
uv run pytest
```

If you need to install into an existing Python environment instead of using `uv sync`, you can use:

```bash
uv pip install -e .
```

## Notebook Install

Install released versions in Jupyter notebook environments with:

```bash
pip install kai_statistics
```

After installation, notebook code should import the package root directly:

```python
import kai_statistics as ks
```

## Upgrade

Upgrade an existing environment to the latest published release with:

```bash
pip install --upgrade kai_statistics
```

## Maintainer Notes

- `.github/workflows/publish.yml` is designed for trusted publishing through GitHub Actions OIDC.
- Before the first tagged release, create or claim the `kai_statistics` project on PyPI and register the repository workflow as a trusted publisher.
- Do not store PyPI API tokens in the repository. The publish workflow is intended to authenticate through trusted publishing instead.
