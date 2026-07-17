# Project Structure

```
Inbox-Guardian/

├── app/
│   ├── analyzers/
│   ├── exceptions/
│   ├── models/
│   ├── parsers/
│   └── readers/
│
├── docs/
│   └── decisions/
│
├── examples/
│
├── tests/
│
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── requirements.txt
```

---

## app/

Contains the application source code.

### analyzers/

Responsible for analyzing specific parts of the HTML.

### models/

Data models shared between analyzers.

### readers/

Read files from disk.

### parsers/

Convert HTML into BeautifulSoup objects.

### exceptions/

Custom project exceptions.

---

## tests/

Contains unit tests.

---

## examples/

Example HTML files used during testing.

---

## docs/

Project documentation and architecture decisions.