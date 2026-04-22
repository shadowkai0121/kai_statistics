"""Contract tests for lightweight result containers."""

from kai_statistics._core import AnalysisResult, ResultCaveat


def test_analysis_result_uses_stable_default_metadata_and_caveats() -> None:
    """Metadata and caveat containers should be present and not shared."""

    first = AnalysisResult(value="ok")
    second = AnalysisResult(value="next")

    first.metadata["source"] = "smoke"
    first.caveats.append(
        ResultCaveat(
            code="small-sample",
            message="Interpret with care.",
            severity="warning",
        )
    )

    assert first.metadata == {"source": "smoke"}
    assert second.metadata == {}
    assert len(first.caveats) == 1
    assert second.caveats == []


def test_result_caveat_exposes_payload_fields() -> None:
    """Caveat payloads should preserve their code, message, and severity."""

    caveat = ResultCaveat(
        code="constant-column",
        message="One input column is constant.",
        severity="warning",
    )

    assert caveat.code == "constant-column"
    assert caveat.message == "One input column is constant."
    assert caveat.severity == "warning"
