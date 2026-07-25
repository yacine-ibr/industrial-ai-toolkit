# Safety and Responsible-Use Model

Industrial systems can affect people, equipment, product quality, the environment and regulatory compliance. This project therefore treats safety boundaries as part of the technical design.

## Intended use

The toolkit is intended for:

- education and research;
- synthetic-data generation;
- offline manufacturing analytics;
- isolated laboratory simulations;
- read-only demonstrations;
- benchmark development;
- architecture documentation.

## Prohibited or unsupported use

The project is not designed or certified for:

- direct autonomous control of machinery;
- bypassing safety PLCs or interlocks;
- changing production setpoints without authorised human review;
- safety-instrumented functions;
- emergency shutdown logic;
- use as the sole basis for product release or regulatory decisions;
- deployment on a production OT network without formal cybersecurity review.

## Human-in-the-loop boundary

AI-generated output must be treated as a hypothesis or recommendation. Before an action affects production, a qualified person should verify:

1. the source data and timestamp range;
2. the machine, line, product and lot scope;
3. the calculation method;
4. missing or stale inputs;
5. alternative explanations;
6. operational and safety consequences;
7. required approvals and change-control procedures.

## Safe integration pattern

Preferred demonstrations use a simulator or an isolated test network. Where live data is involved, integrations should be read-only, least-privileged, segmented and explicitly authorised. Credentials must never be committed to the repository.

## AI failure modes considered

- fabricated root causes;
- incorrect numerical calculations;
- confident answers from incomplete data;
- confusion between planned and unplanned downtime;
- incorrect timezone or shift attribution;
- prompt injection embedded in documents;
- unsafe recommendations presented without escalation;
- leakage of confidential operational information.

## Reporting safety concerns

Do not publish details that could create operational risk. Follow the private reporting process in `SECURITY.md`.
