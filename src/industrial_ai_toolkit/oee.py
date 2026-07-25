"""Deterministic Overall Equipment Effectiveness calculations.

The formulas implemented here follow the common decomposition:

    OEE = Availability × Performance × Quality

All ratios are returned in the inclusive range [0, 1]. Inputs are validated so
that impossible or contradictory manufacturing records fail loudly rather than
silently producing misleading KPIs.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class OEEInputs:
    """Validated inputs required for a basic OEE calculation."""

    planned_production_seconds: float
    downtime_seconds: float
    ideal_cycle_seconds: float
    total_count: int
    good_count: int

    def validate(self) -> None:
        if self.planned_production_seconds <= 0:
            raise ValueError("planned_production_seconds must be greater than zero")
        if self.downtime_seconds < 0:
            raise ValueError("downtime_seconds cannot be negative")
        if self.downtime_seconds > self.planned_production_seconds:
            raise ValueError("downtime_seconds cannot exceed planned production time")
        if self.ideal_cycle_seconds <= 0:
            raise ValueError("ideal_cycle_seconds must be greater than zero")
        if self.total_count < 0:
            raise ValueError("total_count cannot be negative")
        if self.good_count < 0:
            raise ValueError("good_count cannot be negative")
        if self.good_count > self.total_count:
            raise ValueError("good_count cannot exceed total_count")


@dataclass(frozen=True, slots=True)
class OEEResult:
    availability: float
    performance: float
    quality: float
    oee: float
    run_time_seconds: float

    def as_percentages(self, digits: int = 2) -> dict[str, float]:
        """Return human-readable percentages without changing raw precision."""

        return {
            "availability": round(self.availability * 100, digits),
            "performance": round(self.performance * 100, digits),
            "quality": round(self.quality * 100, digits),
            "oee": round(self.oee * 100, digits),
        }


def _bounded_ratio(numerator: float, denominator: float) -> float:
    if denominator <= 0:
        return 0.0
    return max(0.0, min(1.0, numerator / denominator))


def calculate_oee(inputs: OEEInputs) -> OEEResult:
    """Calculate OEE and its three canonical factors.

    Performance is capped at 1.0. A value above 1.0 normally signals that the
    configured ideal cycle time is slower than the observed process, rather
    than true performance above 100 percent.
    """

    inputs.validate()
    run_time = inputs.planned_production_seconds - inputs.downtime_seconds

    availability = _bounded_ratio(run_time, inputs.planned_production_seconds)
    performance = _bounded_ratio(inputs.ideal_cycle_seconds * inputs.total_count, run_time)
    quality = _bounded_ratio(float(inputs.good_count), float(inputs.total_count))
    oee = availability * performance * quality

    return OEEResult(
        availability=availability,
        performance=performance,
        quality=quality,
        oee=oee,
        run_time_seconds=run_time,
    )
