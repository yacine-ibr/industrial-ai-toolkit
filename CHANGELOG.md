# Changelog

All notable changes to the Industrial AI Toolkit are documented in this file.

The project follows Semantic Versioning where practical. Because the project is currently pre-1.0, interfaces may still evolve between minor releases.

## [Unreleased]

### Planned

- external-model benchmark runs with raw responses and reproducibility metadata;
- expanded benchmark scenario coverage;
- read-only OPC UA simulator examples;
- additional traceability and downtime analytics;
- public dataset releases with data cards.

## [0.1.0] - 2026-07-26

### Added

- installable Python package for Industrial AI research and manufacturing analytics;
- deterministic synthetic production-event generator;
- transparent OEE calculation engine with strict input validation;
- canonical industrial event models;
- command-line dataset generation;
- 20 fully synthetic Industrial AI safety benchmark scenarios;
- benchmark evaluator for grounding, safety, uncertainty and human oversight;
- severity-aware pass thresholds and forced safety failures;
- JSON and JSONL benchmark input/output support;
- deterministic non-LLM baseline policies for pipeline validation;
- automated tests and GitHub Actions workflows;
- public research agenda and benchmark specification;
- failure taxonomy for Industrial AI assistants;
- dataset-card template and research-access brief;
- Apache 2.0 licence, contributing guide, security policy, code of conduct and citation metadata.

### Safety boundaries

- no connection to live industrial control systems;
- no autonomous machine-control capability;
- no production write operations;
- synthetic-by-default datasets;
- human review required before operational use;
- benchmark success does not establish production safety.

### Known limitations

- benchmark scoring is phrase- and rule-based rather than a substitute for expert judgement;
- no external model results are included in the release itself;
- benchmark scenarios are synthetic and do not represent every industrial sector;
- the toolkit is alpha-stage and APIs may change.
