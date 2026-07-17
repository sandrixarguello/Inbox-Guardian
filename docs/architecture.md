# Architecture

Inbox Guardian follows a modular architecture.

```
          HTML File
               │
               ▼
        HTML Reader
               │
               ▼
        HTML Parser
               │
               ▼
       HTML Analyzer
      ┌─────┼─────┐
      ▼     ▼     ▼
 Image Link Accessibility
Analyzer Analyzer Analyzer
      └─────┼─────┘
            ▼
        QA Engine
            ▼
      Report Generator
```

---

## Design Principles

- Single Responsibility Principle
- Low Coupling
- High Cohesion
- Testability
- Extensibility

Each analyzer focuses on one specific concern and produces a structured result model.