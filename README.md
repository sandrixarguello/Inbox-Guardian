# Inbox Guardian

Inbox Guardian es una herramienta de análisis de HTML para Email Marketing.

Su objetivo es ayudar a equipos de CRM y Marketing a detectar problemas que puedan afectar la entregabilidad de campañas antes de realizar un envío.

---

## Características

- ✅ Lectura de archivos HTML
- ✅ Parseo de HTML mediante BeautifulSoup
- ✅ Clasificación de elementos HTML
- ✅ Análisis de imágenes
- ✅ Análisis de links
- 🚧 Accesibilidad
- 🚧 QA Score
- 🚧 Reporte PDF

---

## Estado actual

**Versión:** `v0.4.0`

### Sprint 1 ✅ Finalizado

- Inicialización del proyecto
- Arquitectura base
- HTML Reader
- Primer test automatizado

### Sprint 2 ✅ Finalizado

- HTML Parser
- Jerarquía de excepciones personalizada
- Tests unitarios para HTML Reader
- Tests unitarios para HTML Parser
- Integración de BeautifulSoup

### Sprint 3 ✅ Finalizado

- HTML Analyzer
- Modelo `HTMLAnalysisResult`
- Clasificación de elementos HTML
  - Imágenes
  - Links
  - Tablas
  - Encabezados
  - Formularios
  - Botones
- Tests unitarios para HTML Analyzer

### Sprint 4 ✅ Finalizado

- Image Analyzer
- Modelo `ImageAnalysisResult`
- Análisis de imágenes
  - Imágenes sin ALT
  - Imágenes locales y remotas
  - Imágenes sin width
  - Imágenes sin height
- Tests unitarios para Image Analyzer

### Sprint 5 ✅ Finalizado

- Link Analyzer
- Modelo `LinkAnalysisResult`
- Análisis de links
  - Links totales
  - Detectar enlaces HTTP y HTTPS
  - Detectar enlaces mailto
  - Detectar enlaces tel:
  - Detectar enlaces sin atributo href
  - Detectar enlaces con UTM's
- Test unitarios para Link Analyzer
---

## Tecnologías

- Python 3
- BeautifulSoup4
- Pytest
- Git
- GitHub

---

## Documentación

- docs/architecture.md
- docs/roadmap.md
- docs/developer-notes.md
- docs/deliverability.md

---

## Licencia

MIT License

---

## Installation

```bash
git clone https://github.com/sandrixarguello/Inbox-Guardian.git

cd Inbox-Guardian

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

---

## Running Tests

```bash
pytest
```
