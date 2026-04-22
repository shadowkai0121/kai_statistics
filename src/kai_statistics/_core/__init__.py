"""Internal shared primitives for kai_statistics."""

from .errors import (
    InputValidationError,
    KaiStatisticsError,
    MissingValueHandlingError,
    ResultContractError,
)
from .results import AnalysisResult, ResultCaveat
from .validation import (
    ensure_columns_present,
    ensure_dataframe,
    require_explicit_na_policy,
)

__all__ = [
    "AnalysisResult",
    "InputValidationError",
    "KaiStatisticsError",
    "MissingValueHandlingError",
    "ResultCaveat",
    "ResultContractError",
    "ensure_columns_present",
    "ensure_dataframe",
    "require_explicit_na_policy",
]
