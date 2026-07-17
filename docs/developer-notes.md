# Developer Notes

## Project Philosophy

Each module has a single responsibility.

Analyzers should never perform responsibilities belonging to another analyzer.

---

## Architecture

Reader

↓

Parser

↓

HTML Analyzer

↓

Specific Analyzers

↓

QA Engine

↓

Report Generator

---

## Naming Convention

Functions

```
analyze_images()

analyze_links()

analyze_accessibility()
```

Models

```
ImageAnalysisResult

LinkAnalysisResult

AccessibilityAnalysisResult
```

---

## Testing

Every analyzer must have:

- dedicated tests
- deterministic behavior
- no external dependencies

---

## Documentation

Every public module should include:

- Responsibility
- Input
- Output
- What it does NOT do