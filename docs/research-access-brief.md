# Research Access Brief

This document summarizes the project for research-access, compute-credit, and open-source support applications. It is intentionally factual: maintainers should update evidence rather than overstate maturity.

## Project

**Industrial AI Toolkit** is an open-source, simulator-first research toolkit for evaluating human-supervised AI assistants in manufacturing contexts. It combines synthetic industrial event generation, deterministic analytics, and safety-oriented benchmark specifications.

## Problem

Manufacturing assistants may analyze alarms, quality records, downtime, and operational notes. Generic model benchmarks do not adequately test whether these systems:

- distinguish evidence from inference;
- abstain when operational context is missing;
- resist prompt injection hidden in untrusted plant records;
- preserve confidential industrial information;
- avoid unsafe or unauthorized control recommendations;
- communicate uncertainty in a way that reduces automation bias.

## Proposed research

The project will build an open benchmark of synthetic industrial incidents with structured evidence, adversarial records, expected safe behavior, and reproducible scoring. The initial work focuses on grounded diagnosis, uncertainty calibration, prompt-injection resistance, privacy, and human oversight.

## Why model access or API credits would help

Model access would be used for controlled offline evaluation across a versioned scenario set. It would enable:

1. repeated trials required for statistically meaningful comparison;
2. comparison of prompting and structured-context strategies;
3. red-team evaluation against embedded untrusted instructions;
4. analysis of abstention and confidence calibration;
5. publication of aggregate results, failure examples, mitigations, and reproducibility metadata.

Credits would not be used for autonomous machine control, production deployment, or access to confidential customer systems.

## Public-interest outputs

Planned outputs include:

- openly licensed synthetic scenarios;
- benchmark and dataset cards;
- scoring and reporting code;
- a public taxonomy of Industrial AI failures;
- documented negative results;
- safe deployment guidance for engineers and researchers;
- provider-neutral evaluation reports where terms permit publication.

## Safety controls

- No live PLC, DCS, SCADA, robot, drive, or safety-system connection.
- Synthetic data by default.
- No real credentials, network maps, or proprietary plant logic.
- Human review required for all operational recommendations.
- Critical-failure scoring for safety bypass, secret disclosure, injection following, and unsupported high-impact claims.
- Responsible disclosure process for security findings.

## Current evidence

Before submitting an application, replace this section with verifiable repository evidence:

- release tags and dates;
- number of scenarios and tests;
- CI status;
- external contributors;
- issues completed;
- benchmark reports published;
- citations, forks, stars, or downstream users where meaningful.

A new repository with documentation alone should not be presented as an established research project. Applications should describe what exists today and clearly separate it from planned work.

## Suggested concise application statement

> Industrial AI Toolkit is an open-source, synthetic-first project for evaluating whether language-model assistants can analyze manufacturing incidents while remaining grounded, uncertainty-aware, resistant to prompt injection, privacy-preserving, and explicitly non-autonomous. We are developing a reproducible benchmark of industrial events and adversarial operational records. API support would fund offline controlled evaluations and publication of scenarios, scoring tools, failure analyses, and mitigations for the broader research and manufacturing community.
