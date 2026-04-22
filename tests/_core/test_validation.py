"""Contract tests for internal validation helpers."""

import pandas as pd
import pytest

from kai_statistics._core import (
    InputValidationError,
    MissingValueHandlingError,
    ensure_columns_present,
    ensure_dataframe,
    require_explicit_na_policy,
)


def test_ensure_dataframe_returns_original_dataframe() -> None:
    """Valid dataframe inputs should pass through unchanged."""

    dataframe = pd.DataFrame({"value": [1, 2]})

    assert ensure_dataframe(dataframe) is dataframe


def test_ensure_dataframe_raises_for_non_dataframe_input() -> None:
    """Non-dataframe inputs should fail fast with a package error."""

    with pytest.raises(InputValidationError, match="must be a pandas DataFrame"):
        ensure_dataframe(["not", "a", "dataframe"], arg_name="frame")


def test_ensure_columns_present_returns_dataframe_when_columns_exist() -> None:
    """Existing required columns should keep the original dataframe."""

    dataframe = pd.DataFrame({"value": [1, 2], "group": ["a", "b"]})

    assert ensure_columns_present(dataframe, ["value", "group"]) is dataframe


def test_ensure_columns_present_raises_when_required_column_is_missing() -> None:
    """Missing columns should be reported through the shared validation error."""

    dataframe = pd.DataFrame({"value": [1, 2]})

    with pytest.raises(InputValidationError, match="missing required columns"):
        ensure_columns_present(dataframe, ["group"])


def test_require_explicit_na_policy_returns_supported_policy() -> None:
    """Supported missing-value policies should pass through unchanged."""

    assert require_explicit_na_policy("drop") == "drop"


def test_require_explicit_na_policy_raises_for_missing_policy() -> None:
    """Missing policy selection must be explicit."""

    with pytest.raises(
        MissingValueHandlingError,
        match="Missing-value handling policy must be explicit",
    ):
        require_explicit_na_policy(None)


def test_require_explicit_na_policy_raises_for_unsupported_policy() -> None:
    """Unexpected policy names should fail with the allowed-values message."""

    with pytest.raises(MissingValueHandlingError, match="Allowed values are"):
        require_explicit_na_policy("impute")
