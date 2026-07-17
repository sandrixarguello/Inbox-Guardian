# Inbox Guardian Roadmap

## v0.1.0 - Foundation ✅

Objetivo:
Construir la base del proyecto.

### Funcionalidades

- [x] Project initialization
- [x] Git repository
- [x] Project architecture
- [x] HTML Reader
- [x] Automated tests

---

## v0.2.0 - HTML Parser ✅

Objetivo:
Interpretar el HTML y convertirlo en una estructura navegable.

### Funcionalidades

- [x] Parse HTML using BeautifulSoup
- [x] Custom exception hierarchy
- [x] HTML Reader tests
- [x] HTML Parser tests

---

## v0.3.0 - HTML Analyzer

Objetivo:
Recorrer la estructura HTML e identificar los elementos principales del documento.

### Funcionalidades

- [x] Detectar etiquetas HTML
- [x] Contar imágenes
- [x] Contar links
- [x] Obtener metadatos básicos
- [x] Tests

---

## v0.4.0 - Image Analyzer ✅

Objetivo:
Analizar las imágenes del correo y obtener métricas básicas.

### Funcionalidades

- [x] Contar imágenes
- [x] Detectar imágenes sin ALT
- [x] Detectar imágenes locales/remotas
- [x] Detectar imágenes sin width
- [x] Detectar imágenes sin height
- [x] Tests

---

## v0.5.0 - Link Analyzer

Objetivo:
Analizar todos los enlaces.

### Funcionalidades

- [x] Detectar HTTP
- [x] Detectar HTTPS
- [x] Detectar UTM
- [x] Detectar enlaces mailto:
- [x] Detectar enlaces tel:
- [x] Detectar enlaces sin href
- [x] Tests

---

## v0.6.0 - Accessibility Analyzer

Objetivo:
Detectar problemas básicos de accesibilidad en el HTML.

### Funcionalidades

- [x] Detectar imágenes sin atributo ALT
- [x] Detectar ausencia de encabezados (H1–H6)
- [x] Detectar encabezados vacíos
- [x] Detectar botones sin texto
- [x] Detectar tablas sin encabezados (`<th>`)
- [x] Tests unitarios

---

## v0.7.0 - QA Score

Objetivo:
Asignar un puntaje general al HTML.

### Funcionalidades

- [ ] Score por imágenes
- [ ] Score por links
- [ ] Score por accesibilidad
- [ ] Score final

---

## v0.8.0 - PDF Report

Objetivo:
Generar un reporte profesional.

### Funcionalidades

- [ ] Reporte PDF
- [ ] Resumen ejecutivo
- [ ] Recomendaciones
- [ ] Score final

---

## v0.9.0 - CLI

Objetivo:
Permitir ejecutar Inbox Guardian desde la terminal.

### Funcionalidades

- [ ] Analizar un HTML desde consola
- [ ] Exportar reporte
- [ ] Mostrar QA Score
- [ ] Configuración mediante argumentos

---

## v1.0.0

Primera versión estable de Inbox Guardian.

