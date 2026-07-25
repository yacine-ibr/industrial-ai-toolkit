# Roadmap

The roadmap is organised around reproducibility, industrial relevance and responsible AI. Dates are intentionally omitted until maintainers and contributors validate capacity.

## Phase 1 — Open-source foundation

- [x] Establish project scope and safety boundaries
- [x] Add deterministic OEE reference implementation
- [x] Add synthetic shift-event generator
- [x] Add tests, linting, typing and continuous integration
- [ ] Publish the first tagged release
- [ ] Add changelog and release automation

## Phase 2 — Canonical industrial data model

- [ ] Versioned JSON Schema for telemetry events
- [ ] State-change, downtime, production and quality event schemas
- [ ] Timestamp-quality and source-quality metadata
- [ ] Idempotency and duplicate-event guidance
- [ ] Data lineage and schema migration examples
- [ ] Dataset validation command

## Phase 3 — Synthetic factory laboratory

- [ ] Multi-machine and multi-line scenarios
- [ ] Planned and unplanned downtime categories
- [ ] Shift calendars and changeovers
- [ ] Lot and work-order genealogy
- [ ] Quality checks, rejects and non-conformities
- [ ] Sensor drift, stale values and missing-data injection
- [ ] Scenario manifests and data cards

## Phase 4 — Manufacturing analytics

- [ ] Downtime Pareto engine
- [ ] Production-rate and cycle-time distributions
- [ ] Lot-centric traceability summaries
- [ ] Quality-loss attribution
- [ ] Local-time daily buckets with DST-safe behaviour
- [ ] Data-health and KPI confidence indicators

## Phase 5 — Industrial interoperability

- [ ] Read-only OPC UA simulator client
- [ ] Defensive Modbus TCP polling example
- [ ] MQTT ingestion example
- [ ] Edge buffering and replay reference implementation
- [ ] Connection-health and freshness monitoring
- [ ] Secure deployment checklist for isolated labs

## Phase 6 — Trustworthy industrial AI benchmark

- [ ] Benchmark task format and evaluator API
- [ ] Numerical manufacturing reasoning tasks
- [ ] Root-cause investigation tasks
- [ ] Missing-context and uncertainty tasks
- [ ] Safety-boundary evaluation
- [ ] Prompt-injection scenarios in maintenance documents
- [ ] Baseline model results and reproducibility report

## Phase 7 — Community and research maturity

- [ ] Public dataset releases with persistent identifiers
- [ ] Academic citation examples
- [ ] Contributor working group
- [ ] Documentation website
- [ ] Reference notebooks and visualisations
- [ ] Independent benchmark submissions

## Non-goals

This project does not aim to provide autonomous machine control, safety PLC logic, production-ready cybersecurity certification, or vendor-specific replacements for validated industrial systems.
