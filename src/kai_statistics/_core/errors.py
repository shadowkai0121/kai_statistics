"""Internal exception hierarchy for kai_statistics."""

__all__ = [
    "KaiStatisticsError",
    "InputValidationError",
    "MissingValueHandlingError",
    "ResultContractError",
]


class KaiStatisticsError(Exception):
    """Base exception for package-specific failures."""


class InputValidationError(KaiStatisticsError):
    """Raised when helper inputs fail validation."""


class MissingValueHandlingError(KaiStatisticsError):
    """Raised when missing-value handling is invalid or unspecified."""


class ResultContractError(KaiStatisticsError):
    """Raised when an internal result object violates its contract."""
