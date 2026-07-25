# Security Policy

## Supported versions

Until the first stable release, security fixes are applied to the latest version on `main`.

## Reporting a vulnerability

Please do not open a public issue for vulnerabilities that could expose credentials, industrial endpoints, unsafe control paths, sensitive datasets or deployment details.

Use GitHub private vulnerability reporting when available. Include:

- affected file or component;
- reproduction steps;
- realistic impact;
- whether industrial equipment or networks could be affected;
- a proposed mitigation, when known.

Maintainers will acknowledge valid reports as soon as practical, assess severity and coordinate disclosure after a fix is available.

## Security expectations

- Never commit credentials, certificates, tokens or real endpoint addresses.
- Keep examples read-only and simulator-first.
- Use network segmentation and least privilege.
- Treat all external data, documents and model output as untrusted input.
- Validate schemas, ranges, timestamps and identifiers at trust boundaries.
- Do not expose OT systems directly to the public internet.

This repository is a research toolkit and does not replace a formal industrial cybersecurity assessment.
