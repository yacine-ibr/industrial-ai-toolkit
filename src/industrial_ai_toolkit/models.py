"""Canonical, dependency-free industrial event models."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from enum import StrEnum
from typing import Any


class MachineState(StrEnum):
    RUNNING = "running"
    IDLE = "idle"
    STOPPED = "stopped"
    FAULT = "fault"
    OFFLINE = "offline"


class EventType(StrEnum):
    TELEMETRY = "telemetry"
    STATE_CHANGE = "state_change"
    PRODUCTION = "production"
    QUALITY = "quality"
    DOWNTIME = "downtime"


@dataclass(frozen=True, slots=True)
class IndustrialEvent:
    """A minimal event envelope suitable for JSONL research datasets."""

    event_id: str
    event_type: EventType
    occurred_at: datetime
    site_id: str
    machine_id: str
    payload: dict[str, Any]
    schema_version: str = "1.0"

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["event_type"] = self.event_type.value
        data["occurred_at"] = self.occurred_at.astimezone(timezone.utc).isoformat()
        return data
