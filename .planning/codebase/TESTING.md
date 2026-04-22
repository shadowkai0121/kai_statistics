# Testing

Current state
- No tests directory detected in repository root or `src/`.

Recommendations
- Add `tests/` with pytest and a simple CI job running `pytest`.
- Add test coverage reporting (e.g., coverage.py or `pytest-cov`).
# Testing

No tests were detected in the repository.

Recommendations:
- Use `pytest` as the test runner.
- Layout tests under `tests/` mirroring module paths.
- Add a minimal `pyproject.toml` test config or `pytest.ini`.

Quickstart:
```bash
python -m pip install pytest
python -m pytest
```

Consider adding a CI workflow (GitHub Actions) to run tests on push and PRs.
