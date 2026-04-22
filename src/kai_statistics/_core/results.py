"""Internal result containers for metadata-rich outputs."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Generic, TypeVar

__all__ = ["AnalysisResult", "ResultCaveat"]

ResultValue = TypeVar("ResultValue")


@dataclass(slots=True)
class ResultCaveat:
    """Describe a non-fatal caveat attached to an analysis result."""

    code: str
    message: str
    severity: str


@dataclass(slots=True)
class AnalysisResult(Generic[ResultValue]):
    """Bundle a primary value with structured metadata and caveats."""

    value: ResultValue
    metadata: dict[str, Any] = field(default_factory=dict)
    caveats: list[ResultCaveat] = field(default_factory=list)
