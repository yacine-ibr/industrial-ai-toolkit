# Quality assurance

Industrial AI Toolkit uses automated checks to keep the public research artifacts reproducible and reviewable.

## Pull-request checks

The quality workflow runs on Python 3.11 and Python 3.12 and performs:

1. editable installation with development dependencies;
2. Ruff checks for Python errors, undefined names, import ordering and common bug patterns;
3. static type analysis with mypy;
4. the complete pytest suite with coverage reporting.

The benchmark workflow independently validates the versioned scenario set, deterministic baseline policies, report generation and published pass/fail expectations.

## Release rule

A release candidate must not be tagged while a required quality or benchmark workflow is failing. The release notes must accurately distinguish deterministic pipeline baselines from evaluations of external language models.

## Reproducibility

Run the same checks locally with:

```bash
python -m pip install -e ".[dev]"
ruff check .
mypy
pytest --cov=industrial_ai_toolkit --cov-report=term-missing
```

Generated benchmark reports should include the benchmark version, model identifier, configuration metadata and raw responses required for independent review.
