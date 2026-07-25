# Contributing

Thank you for helping improve the Industrial AI Toolkit.

## Before contributing

Please read the project scope, safety guidance and roadmap. Large changes should begin with a GitHub issue so that assumptions, interfaces and safety implications can be discussed before implementation.

## Development setup

```bash
git clone https://github.com/yacine-ibr/industrial-ai-toolkit.git
cd industrial-ai-toolkit
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pytest
ruff check .
mypy
```

## Contribution workflow

1. Fork the repository or create a feature branch.
2. Keep each pull request focused on one coherent change.
3. Add or update tests for behaviour changes.
4. Document assumptions, data provenance and limitations.
5. Run the complete quality suite locally.
6. Open a pull request using the provided template.

## Engineering standards

- Prefer simple, dependency-light implementations.
- Use timezone-aware timestamps.
- Make randomness deterministic with explicit seeds.
- Validate impossible manufacturing states instead of silently correcting them.
- Keep KPI formulas transparent and cite assumptions.
- Do not include proprietary plant data, credentials, customer names or confidential screenshots.
- Do not add write-control examples for production equipment.

## Dataset contributions

Every dataset contribution should include:

- a clear synthetic or real-data declaration;
- provenance and licence information;
- schema version;
- scenario description;
- known limitations;
- generation parameters or reproducibility instructions;
- confirmation that no confidential or personal data is included.

## AI benchmark contributions

Benchmark tasks must define expected evidence, scoring criteria, numerical tolerances and failure conditions. Tasks should reward uncertainty when required information is missing and penalise fabricated industrial facts.

## Commit messages

Use concise conventional prefixes where practical:

- `feat:` new capability
- `fix:` defect correction
- `docs:` documentation
- `test:` tests
- `ci:` automation
- `refactor:` internal restructuring

## Review expectations

Maintainers may request changes related to correctness, safety, maintainability, reproducibility or project scope. Review is a technical quality process, not a judgement of the contributor.
