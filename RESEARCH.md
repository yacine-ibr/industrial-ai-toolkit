# Research Program

## Trustworthy Industrial AI for Human-Supervised Manufacturing

Industrial AI systems increasingly summarize production data, diagnose anomalies, recommend actions, and assist engineers. Yet most public evaluations focus on generic coding or conversational tasks rather than the operational constraints of manufacturing environments.

This project studies a narrower question:

> How can language-model-based assistants support industrial decision-making while remaining auditable, uncertainty-aware, privacy-preserving, and explicitly non-autonomous?

## Scope

The research is deliberately limited to decision support. The toolkit does not send commands to PLCs, safety systems, drives, robots, or production equipment. Generated recommendations must be reviewed by a qualified human before any operational action.

The initial research tracks are:

1. **Grounded diagnosis** — can a model distinguish evidence from hypothesis when analyzing alarms, downtime, quality events, and process context?
2. **Uncertainty calibration** — does the system abstain when evidence is incomplete, contradictory, stale, or outside its competence?
3. **Instruction hierarchy and prompt-injection resistance** — can the assistant ignore malicious instructions embedded in logs, operator notes, maintenance comments, or imported documents?
4. **Privacy-preserving analysis** — can useful evaluation be performed with synthetic data and redacted schemas rather than confidential plant data?
5. **Human factors** — do explanations help engineers make better decisions without creating automation bias?
6. **Reproducibility** — can every benchmark result be reproduced from a versioned scenario, configuration, model identifier, and scoring rubric?

## Research hypotheses

- Structured context and explicit evidence citations will reduce unsupported conclusions.
- Requiring an uncertainty statement and an abstention option will improve safety on underspecified incidents.
- Separating observations, inferences, recommendations, and required human checks will improve auditability.
- Synthetic fault injection can reveal failure modes before any evaluation on real industrial data.
- Models will remain vulnerable to misleading maintenance notes unless untrusted text is clearly isolated and evaluated adversarially.

## Evaluation principles

Every evaluation should be:

- **offline**: no connection to live control networks;
- **synthetic-first**: public fixtures contain no proprietary plant data;
- **deterministic where possible**: scenario generation uses fixed seeds;
- **model-neutral**: prompts and scoring should support multiple providers;
- **traceable**: results identify dataset version, prompt version, model, parameters, and evaluator version;
- **safety-weighted**: a confident unsafe recommendation is penalized more heavily than an abstention;
- **open to criticism**: limitations and negative results are documented.

## Expected outputs

- a public industrial incident benchmark;
- adversarial prompt-injection scenarios embedded in realistic operational records;
- calibrated abstention and evidence-grounding metrics;
- model cards and benchmark cards;
- reproducible evaluation scripts;
- a documented taxonomy of Industrial AI failure modes;
- practical guidance for human-supervised deployment.

## Non-goals

This project is not intended to:

- autonomously control industrial equipment;
- bypass safety instrumented systems;
- provide instructions for defeating access controls;
- expose confidential plant configurations;
- claim that benchmark performance proves production safety;
- replace qualified automation, maintenance, quality, or process engineers.

## Responsible research process

Potentially sensitive findings should be handled according to `SECURITY.md`. Scenarios involving cyber-physical systems must remain defensive, simulated, and non-operational. Contributions that materially increase the ability to disrupt real facilities will not be accepted.
