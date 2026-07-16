# Inbox Guardian

Inbox Guardian es una herramienta de análisis de HTML para Email Marketing.

Su objetivo es ayudar a equipos de CRM y Marketing a detectar problemas que puedan afectar la entregabilidad de campañas antes de realizar un envío.

---

## Características

- ✅ Lectura de archivos HTML
- ✅ Parseo de HTML mediante BeautifulSoup
- 🚧 Análisis de estructura HTML
- 🚧 Análisis de imágenes
- 🚧 Análisis de links
- 🚧 Accesibilidad
- 🚧 QA Score
- 🚧 Reporte PDF

---

## Estado actual

**Versión:** `v0.2.0`

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
git clone ...
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

---