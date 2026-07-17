# ADR 0002 - QA Scoring Engine

## Status

Accepted

---

## Context

Several analyzers produce independent results.

A single module is needed to combine them into a final quality score.

---

## Decision

Create a dedicated QA Engine.

The QA Engine will receive the output of every analyzer.

It will calculate:

- Partial scores
- Final score
- Recommendations

---

## Consequences

Positive

- Decoupled architecture.
- Easy to adjust scoring rules.
- New analyzers can be integrated without modifying existing ones.