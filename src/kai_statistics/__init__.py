"""Notebook-friendly public package surface for kai_statistics."""

from . import descriptive, io, profiling, testing

__version__ = "0.1.0"

__all__ = ["__version__", "descriptive", "io", "profiling", "testing"]


def _hello():
    """Small helper to verify package import."""
    return "kai_statistics ready"
