# Benchmark Results

This directory is reserved for reproducible Industrial AI Safety Benchmark results.

## Directory convention

```text
results/
└── <provider-or-baseline>/
    └── <model-or-policy>/
        └── <run-date>-<short-commit>/
            ├── metadata.json
            ├── responses.jsonl
            ├── evaluator-report.json
            └── manual-review.md
```

## Publication requirements

A result is publishable only when it includes:

- an exact repository commit;
- the benchmark and scenario-set versions;
- unedited raw responses;
- complete model configuration metadata;
- deterministic evaluator output;
- manual review for critical scenarios;
- an explicit statement of limitations;
- confirmation that no secrets or confidential industrial data are present.

## Baseline distinction

Repository-provided deterministic policies are pipeline baselines. They are not language models and must not be compared or described as model intelligence.

## Empty by design

Version 0.1.0 does not claim an external-model benchmark result. Results will be added only after a reproducible run is completed and reviewed.
