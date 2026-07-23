# Changelog

All notable changes to this project will be documented in this file.

## [0.2.0] - 2026-07-16

### Added

- HTML Reader module.
- HTML Parser using BeautifulSoup.
- Custom exception hierarchy.
- Unit tests for Reader and Parser.
- Initial test suite with pytest.

### Changed

- Improved project architecture.
- Organized modules into readers, parsers and exceptions.

## v0.3.0

### Added

- HTML Analyzer
- HTMLAnalysisResult
- Tests para HTML Analyzer
- Nuevo módulo models

## v0.4.0

### Added

- Image Analyzer module
- ImageAnalysisResult model
- Image Analyzer unit tests
- Package exports through `__init__.py`

## v0.5.0

### Added

- Link Analyzer module
- LinkAnalysisResult model
- Link Analyzer unit tests

### Changed

- Package exports through `__init__.py`

## v0.6.0

### Added

- Accessibility Analyzer.
- AccessibilityAnalysisResult model.
- Detección de imágenes sin atributo ALT.
- Detección de ausencia de encabezados (H1-H6).
- Detección de encabezados vacíos.
- Detección de botones sin texto.
- Detección de tablas sin encabezados (`<th>`).
- Tests unitarios para Accessibility Analyzer.

### Changed

- Se integró el Accessibility Analyzer con HTML Analyzer e Image Analyzer.

# Changelog

## [v0.7.0] - QA Scoring Engine

### ✨ Added

- Implemented QA Score Engine.
- Added configurable scoring rules.
- Added image quality score calculation.
- Added link quality score calculation.
- Added accessibility quality score calculation.
- Added weighted total QA score calculation.
- Added quality grades (A, B and C).
- Added automatic quality summary generation.

### 🧪 Tests

- Added unit tests for image scoring.
- Added unit tests for link scoring.
- Added unit tests for accessibility scoring.
- Added isolated HTML fixtures for scoring tests.
- Total automated tests: **45 passing**.

### 🏗️ Architecture

- Introduced the Scoring Engine layer.
- Kept analyzers independent from the scoring system.
- Centralized score calculation through `QAScoreResult`.

### 📚 Documentation

- Updated README.
- Updated Roadmap.
- Updated Architecture documentation.

# v0.8.0 — Report Generator

## ✨ Added

- Se implementa `ReportGenerator`.
- Se incorpora el modelo `InboxGuardianReport`.
- Se consolidan los resultados de:
  - HTML Analyzer
  - Image Analyzer
  - Link Analyzer
  - Accessibility Analyzer
  - QA Score Engine.
- Se agregan tests unitarios para el Report Generator.

## 🧪 Tests

- 51 tests ejecutados.
- Todos los tests exitosos (`51 passed`).

## 🏗 Arquitectura

El pipeline queda conformado de la siguiente manera:

Reader
→ Parser
→ HTML Analyzer
→ Image Analyzer
→ Link Analyzer
→ Accessibility Analyzer
→ QA Score Engine
→ Report Generator
→ InboxGuardianReport