"""Internal shared primitives for kai_statistics."""

from .errors import (
    InputValidationError,
    KaiStatisticsError,
    MissingValueHandlingError,
    ResultContractError,
)
from .validation import (
    ensure_columns_present,
    ensure_dataframe,
    require_explicit_na_policy,
)

__all__ = [
    "InputValidationError",
    "KaiStatisticsError",
    "MissingValueHandlingError",
    "ResultContractError",
    "ensure_columns_present",
    "ensure_dataframe",
    "require_explicit_na_policy",
]
