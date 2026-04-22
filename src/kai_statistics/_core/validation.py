"""Internal validation helpers for dataframe-oriented inputs."""

from __future__ import annotations

from collections.abc import Iterable

import pandas as pd

from .errors import InputValidationError, MissingValueHandlingError

__all__ = [
    "ensure_columns_present",
    "ensure_dataframe",
    "require_explicit_na_policy",
]


def ensure_dataframe(data: object, arg_name: str = "data") -> pd.DataFrame:
    """Return a validated pandas DataFrame or raise a package error."""

    if not isinstance(data, pd.DataFrame):
        actual_type = type(data).__name__
        raise InputValidationError(
            f"`{arg_name}` must be a pandas DataFrame, got {actual_type}."
        )

    return data


def ensure_columns_present(
    dataframe: object,
    columns: Iterable[object],
    arg_name: str = "data",
) -> pd.DataFrame:
    """Ensure a dataframe contains every required column before continuing."""

    validated = ensure_dataframe(dataframe, arg_name=arg_name)

    if isinstance(columns, str):
        required_columns = (columns,)
    else:
        try:
            required_columns = tuple(columns)
        except TypeError as exc:
            raise InputValidationError(
                "`columns` must be an iterable of required column names."
            ) from exc

    missing_columns = [column for column in required_columns if column not in validated.columns]
    if missing_columns:
        missing_display = ", ".join(repr(column) for column in missing_columns)
        raise InputValidationError(
            f"`{arg_name}` is missing required columns: {missing_display}."
        )

    return validated


def require_explicit_na_policy(
    policy: str | None,
    allowed: tuple[str, ...] = ("drop", "keep", "error"),
) -> str:
    """Validate explicit missing-value policy selection for future helpers."""

    allowed_policies = tuple(allowed)
    allowed_display = ", ".join(repr(option) for option in allowed_policies)

    if policy is None:
        raise MissingValueHandlingError(
            "Missing-value handling policy must be explicit. "
            f"Choose one of: {allowed_display}."
        )

    if policy not in allowed_policies:
        raise MissingValueHandlingError(
            f"Unsupported missing-value handling policy {policy!r}. "
            f"Allowed values are: {allowed_display}."
        )

    return policy
