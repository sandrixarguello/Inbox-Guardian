# ADR 0003 - Report Format

## Status

Accepted

---

## Context

Inbox Guardian should generate professional reports without coupling report generation to the analysis process.

---

## Decision

The report generator will consume the QA Engine results.

It will not perform any analysis itself.

Future report formats may include:

- PDF
- HTML
- JSON

---

## Consequences

Positive

- Separation of concerns.
- Easy to support multiple report formats.
- Report generation remains independent from analysis logic.