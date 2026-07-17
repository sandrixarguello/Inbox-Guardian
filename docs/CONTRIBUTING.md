# Contributing

Thank you for your interest in contributing to Inbox Guardian.

## Development Setup

Clone the repository:

```bash
git clone https://github.com/sandrixarguello/Inbox-Guardian.git

cd Inbox-Guardian
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Tests

```bash
pytest
```

All tests must pass before submitting a Pull Request.

---

## Git Workflow

1. Create an Issue.
2. Create a feature branch.
3. Implement the feature.
4. Write unit tests.
5. Update documentation if necessary.
6. Commit using a descriptive message.
7. Push the branch.
8. Open a Pull Request.
9. Merge after review.

---

## Commit Style

Examples:

```
feat: add image analyzer

fix: validate missing href

docs: update roadmap

test: add accessibility analyzer tests
```

---

Thank you for contributing!