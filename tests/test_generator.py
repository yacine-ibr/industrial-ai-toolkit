from industrial_ai_toolkit.generator import generate_shift_events


def test_generator_is_deterministic() -> None:
    first = generate_shift_events(minutes=10, seed=7)
    second = generate_shift_events(minutes=10, seed=7)
    assert [event.to_dict() for event in first] == [event.to_dict() for event in second]


def test_generator_changes_with_seed() -> None:
    first = generate_shift_events(minutes=10, seed=7)
    second = generate_shift_events(minutes=10, seed=8)
    assert [event.payload for event in first] != [event.payload for event in second]


def test_generator_produces_monotonic_timestamps() -> None:
    events = generate_shift_events(minutes=30)
    timestamps = [event.occurred_at for event in events]
    assert timestamps == sorted(timestamps)
    assert len(events) == 30
