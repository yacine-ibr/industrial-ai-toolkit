# Dataset Card Template

## Dataset summary

- **Name:**
- **Version:**
- **Release date:**
- **License:**
- **Maintainers:**
- **Repository commit:**

## Intended use

Describe the research questions the dataset is designed to support. State whether it is suitable for training, evaluation, demonstrations, or documentation.

## Prohibited and out-of-scope use

This dataset must not be represented as a complete model of any real facility. It must not be used to authorize autonomous control, safety-system changes, or production decisions without qualified human review.

## Data origin

State whether each field is synthetic, transformed, manually authored, or derived from a public source. Do not include confidential plant data, credentials, personal information, or proprietary control logic.

## Generation process

Document:

- generator version and commit;
- random seed policy;
- machine and process assumptions;
- fault-injection rules;
- time-zone and timestamp conventions;
- units and permitted ranges;
- missing-data and contradiction injection;
- prompt-injection content generation;
- validation performed after generation.

## Schema

Provide every field, type, unit, nullability, semantic meaning, and trust classification. Explicitly distinguish trusted metadata from untrusted free text.

## Dataset composition

Report record and scenario counts by:

- machine type;
- incident family;
- severity;
- normal versus anomalous operation;
- missing-data pattern;
- adversarial-content category;
- expected abstention requirement.

## Quality checks

List schema validation, range checks, duplicate detection, chronological consistency, referential integrity, leakage checks, and manual reviews.

## Biases and limitations

Discuss which industries, equipment, languages, failure modes, work practices, and regional contexts are underrepresented. Synthetic data may encode the assumptions of its authors and may be easier than real operational data.

## Privacy and security

Confirm that the release contains no real secrets, credentials, network addresses, employee data, customer identifiers, or proprietary plant topology. Describe the review process.

## Benchmark use

Document train/test separation, contamination risks, scoring protocol, and whether public answers are included. Avoid publishing hidden evaluation labels where doing so would invalidate the benchmark.

## Changes from previous version

Maintain a clear changelog for scenario additions, removals, corrections, schema changes, and scoring-impacting modifications.
