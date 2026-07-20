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

---

# QA Scoring Rules

## Philosophy

Inbox Guardian evaluates HTML quality using three independent categories:

- Images
- Links
- Accessibility

Each category starts with a score of **100**.

Penalties are applied independently.

The minimum score for any category is **0**.

The overall score is calculated using weighted averages.

---

## Category Weights

| Category | Weight |
|----------|-------:|
| Images | 40% |
| Links | 40% |
| Accessibility | 20% |

---

## Image Score

| Rule | Penalty |
|------|--------:|
| Missing ALT | -15 |
| Missing width | -5 |
| Missing height | -5 |

---

## Link Score

| Rule | Penalty |
|------|--------:|
| HTTP link | -15 |
| Missing href | -20 |

---

## Accessibility Score

| Rule | Penalty |
|------|--------:|
| Missing headings | -10 |
| Empty heading | -5 |
| Button without text | -10 |
| Table without headers | -10 |

---

## Design Principle

Each issue affects only one category.

For example:

- Missing ALT affects Image Score only.
- It is reported by Accessibility Analyzer but does not reduce the Accessibility Score.