import pytest

from industrial_ai_toolkit.oee import OEEInputs, calculate_oee


def test_calculate_oee_returns_expected_factors() -> None:
    result = calculate_oee(
        OEEInputs(
            planned_production_seconds=28_800,
            downtime_seconds=2_100,
            ideal_cycle_seconds=1.2,
            total_count=19_400,
            good_count=18_950,
        )
    )

    assert result.availability == pytest.approx(26_700 / 28_800)
    assert result.performance == pytest.approx((1.2 * 19_400) / 26_700)
    assert result.quality == pytest.approx(18_950 / 19_400)
    assert result.oee == pytest.approx(
        result.availability * result.performance * result.quality
    )


def test_performance_is_capped_at_one() -> None:
    result = calculate_oee(
        OEEInputs(3_600, 0, ideal_cycle_seconds=2.0, total_count=2_000, good_count=2_000)
    )
    assert result.performance == 1.0


@pytest.mark.parametrize(
    "inputs",
    [
        OEEInputs(0, 0, 1, 1, 1),
        OEEInputs(100, -1, 1, 1, 1),
        OEEInputs(100, 101, 1, 1, 1),
        OEEInputs(100, 0, 0, 1, 1),
        OEEInputs(100, 0, 1, -1, 0),
        OEEInputs(100, 0, 1, 1, 2),
    ],
)
def test_invalid_inputs_are_rejected(inputs: OEEInputs) -> None:
    with pytest.raises(ValueError):
        calculate_oee(inputs)
