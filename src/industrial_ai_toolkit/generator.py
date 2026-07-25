"""Deterministic synthetic manufacturing event generator."""

from __future__ import annotations

import random
from datetime import datetime, timedelta, timezone
from uuid import UUID, uuid5

from industrial_ai_toolkit.models import EventType, IndustrialEvent, MachineState

_NAMESPACE = UUID("c21f969b-5f03-4df0-9ce8-7d76a43cdb27")


def generate_shift_events(
    *,
    minutes: int = 480,
    seed: int = 42,
    site_id: str = "demo-site",
    machine_id: str = "press-01",
    start: datetime | None = None,
) -> list[IndustrialEvent]:
    """Generate one event per minute for a repeatable factory scenario.

    The generator intentionally favours interpretable states over high-fidelity
    physical simulation. It is suitable for tutorials, tests and baseline AI
    evaluation—not for validating safety or machine-control behaviour.
    """

    if minutes <= 0:
        raise ValueError("minutes must be greater than zero")

    rng = random.Random(seed)
    timestamp = start or datetime(2026, 1, 1, 6, 0, tzinfo=timezone.utc)
    if timestamp.tzinfo is None:
        raise ValueError("start must be timezone-aware")

    events: list[IndustrialEvent] = []
    cumulative_count = 0
    cumulative_rejects = 0

    for index in range(minutes):
        roll = rng.random()
        if roll < 0.78:
            state = MachineState.RUNNING
            produced = rng.randint(42, 50)
            rejects = 1 if rng.random() < 0.16 else 0
        elif roll < 0.88:
            state = MachineState.IDLE
            produced = 0
            rejects = 0
        elif roll < 0.97:
            state = MachineState.STOPPED
            produced = 0
            rejects = 0
        else:
            state = MachineState.FAULT
            produced = 0
            rejects = 0

        cumulative_count += produced
        cumulative_rejects += rejects
        event_time = timestamp + timedelta(minutes=index)
        identity = f"{seed}:{site_id}:{machine_id}:{event_time.isoformat()}"

        events.append(
            IndustrialEvent(
                event_id=str(uuid5(_NAMESPACE, identity)),
                event_type=EventType.TELEMETRY,
                occurred_at=event_time,
                site_id=site_id,
                machine_id=machine_id,
                payload={
                    "state": state.value,
                    "produced_count_delta": produced,
                    "reject_count_delta": rejects,
                    "total_count": cumulative_count,
                    "reject_count": cumulative_rejects,
                    "temperature_c": round(57.0 + rng.uniform(-2.0, 3.5), 2),
                    "cycle_time_seconds": round(rng.uniform(1.18, 1.34), 3)
                    if state is MachineState.RUNNING
                    else None,
                    "data_quality": "synthetic",
                    "scenario_seed": seed,
                },
            )
        )

    return events
