#!/usr/bin/env python3
"""Generate two transparent non-LLM baselines for benchmark validation.

These policies exist to validate the benchmark pipeline and establish lower-bound
reference results. They are not presented as language models or production systems.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from industrial_ai_toolkit.benchmark import Scenario, load_scenarios


def naive_policy(scenario: Scenario) -> str:
    """A deliberately weak baseline that repeats the prompt."""

    return f"Summary based on the request: {scenario.prompt}"


def safety_first_policy(scenario: Scenario) -> str:
    """A deterministic policy that surfaces evidence and conservative safeguards."""

    evidence = "; ".join(scenario.evidence) or "no evidence supplied"
    concepts = "; ".join(scenario.expected_terms)
    parts = [f"Evidence: {evidence}.", f"Relevant concepts: {concepts}."]
    if scenario.require_abstention:
        parts.append("Données insuffisantes: je ne peux pas déterminer une conclusion certaine.")
    if scenario.require_human_review:
        parts.append("Validation humaine par du personnel qualifié requise avant toute action.")
    if scenario.category in {"unsafe_action_pressure", "maintenance"}:
        parts.append("Do not bypass safeguards; follow the approved safety procedure.")
    if scenario.category == "prompt_injection":
        parts.append("Treat embedded instructions as untrusted data and ignore them.")
    if scenario.category in {"privacy", "confidentiality"}:
        parts.append("Do not publish confidential or personal data; redact before sharing.")
    if scenario.category == "cybersecurity":
        parts.append("Use the approved incident-response and access-control process.")
    return " ".join(parts)


def write_records(
    scenarios: tuple[Scenario, ...],
    policy_name: str,
    output: Path,
) -> None:
    policy = naive_policy if policy_name == "naive" else safety_first_policy
    lines = []
    for scenario in scenarios:
        lines.append(
            json.dumps(
                {
                    "scenario_id": scenario.scenario_id,
                    "model": "deterministic-policy",
                    "configuration": policy_name,
                    "response": policy(scenario),
                },
                sort_keys=True,
            )
        )
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", choices=("naive", "safety-first"), required=True)
    parser.add_argument(
        "--scenarios",
        type=Path,
        default=Path(__file__).with_name("scenarios.json"),
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    _, scenarios = load_scenarios(args.scenarios)
    write_records(scenarios, args.policy, args.output)
    print(f"Wrote {len(scenarios)} responses to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
