# ADR 0001 - Module Structure

## Status

Accepted

---

## Context

Inbox Guardian needs to analyze multiple aspects of an HTML document.

Keeping all logic inside a single file would make the project difficult to maintain.

---

## Decision

Split the application into independent analyzers.

Examples:

- HTML Analyzer
- Image Analyzer
- Link Analyzer
- Accessibility Analyzer

---

## Consequences

Positive

- Easier maintenance.
- Easier testing.
- Easier future expansion.

Negative

- More files.
- More models.