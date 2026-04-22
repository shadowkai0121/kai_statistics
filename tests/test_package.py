"""Smoke coverage for the package root."""

import kai_statistics as ks


def test_package_root_import_surface_matches_phase_one_boundaries() -> None:
    """Keep the package root limited to the Phase 1 boundary surface."""

    assert ks.__version__ == "0.1.0"
    assert ks.__all__ == ["__version__", "descriptive", "io", "profiling", "testing"]
    assert ks.descriptive.__name__ == "kai_statistics.descriptive"
    assert ks.io.__name__ == "kai_statistics.io"
    assert ks.profiling.__name__ == "kai_statistics.profiling"
    assert ks.testing.__name__ == "kai_statistics.testing"


def test_hello_smoke_helper_returns_ready_message() -> None:
    """Exercise the import smoke helper used by Phase 1."""

    assert ks._hello() == "kai_statistics ready"
