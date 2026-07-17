# Development Workflow

Este documento describe el flujo de trabajo utilizado para desarrollar nuevas funcionalidades en Inbox Guardian.

---

# 1. Crear un Issue

Antes de comenzar una nueva funcionalidad, crear un Issue en GitHub que describa:

- Objetivo
- Alcance
- Criterios de aceptación

Ejemplo:

Issue #5 - Link Analyzer

---

# 2. Crear una rama

Siempre trabajar sobre una rama nueva creada desde `main`.

```bash
git checkout main
git pull

git checkout -b feature/link-analyzer
```

Nombre recomendado:

```
feature/<nombre-funcionalidad>
```

Ejemplos:

- feature/html-parser
- feature/html-analyzer
- feature/image-analyzer
- feature/link-analyzer

---

# 3. Diseñar antes de programar

Antes de escribir código definir:

## Responsabilidad

¿Qué hace el módulo?

## Entrada

¿Qué recibe?

## Salida

¿Qué devuelve?

## No hace

¿Qué responsabilidades NO tiene?

---

# 4. Implementar

Implementar únicamente la responsabilidad del módulo.

Mantener una única responsabilidad por clase o función.

---

# 5. Escribir Tests

Cada nueva funcionalidad debe tener tests unitarios.

Ejemplos:

- test_should_parse_valid_html()
- test_should_count_total_images()

Ejecutar:

```bash
pytest
```

Todos los tests deben finalizar correctamente.

---

# 6. Actualizar documentación

Antes del commit actualizar:

- README.md
- docs/roadmap.md
- CHANGELOG.md (si corresponde)

La documentación siempre debe reflejar el estado real del proyecto.

---

# 7. Commit

Agregar todos los cambios:

```bash
git add .
```

Crear un commit siguiendo Conventional Commits.

Ejemplos:

```text
feat: implement image analyzer
```

```text
feat: implement link analyzer
```

```text
docs: update roadmap
```

```text
fix: correct image analyzer import
```

---

# 8. Push

Primer push de una rama nueva:

```bash
git push -u origin feature/nombre-rama
```

Push posteriores:

```bash
git push
```

---

# 9. Pull Request

Título:

```text
feat: implement Image Analyzer
```

Descripción:

- Resumen de cambios
- Funcionalidades agregadas
- Tests realizados
- Referencia al Issue

Ejemplo:

Closes #4

---

# 10. Merge

Utilizar preferentemente:

- Squash and Merge

Mantener un historial limpio del proyecto.

---

# 11. Release

Crear una nueva Release en GitHub.

Formato:

```
v0.x.0
```

Ejemplos:

- v0.2.0 - HTML Parser
- v0.3.0 - HTML Analyzer
- v0.4.0 - Image Analyzer

---

# 12. Limpiar ramas

Después del merge:

```bash
git checkout main

git pull

git branch -d feature/nombre-rama

git push origin --delete feature/nombre-rama
```

---

# Convenciones del proyecto

## Nombres de archivos

Utilizar `snake_case`.

Ejemplos:

```
html_parser.py
image_analyzer.py
image_analysis_result.py
```

---

## Clases

Utilizar `PascalCase`.

Ejemplos:

```
HTMLAnalysisResult
ImageAnalysisResult
```

---

## Funciones

Utilizar verbos.

Ejemplos:

```
read_html()
parse_html()
analyze_html()
analyze_images()
```

---

## Arquitectura

```
HTML
 │
 ▼
read_html()
 │
 ▼
parse_html()
 │
 ▼
analyze_html()
 │
 ├──────────────┐
 ▼              ▼
analyze_images() analyze_links()
 │              │
 └──────┬───────┘
        ▼
   QA Score
        ▼
 PDF Report
```

Cada módulo debe tener una única responsabilidad y ser fácilmente testeable.

---

# Definición de Done (Definition of Done)

Una tarea se considera terminada cuando:

- Código implementado.
- Tests unitarios creados.
- Todos los tests pasan.
- README actualizado.
- Roadmap actualizado.
- CHANGELOG actualizado (si corresponde).
- Commit realizado.
- Push realizado.
- Pull Request creado.
- Merge realizado.
- Issue cerrado.
- Release creada.

# Filosofía del proyecto

Inbox Guardian se desarrolla siguiendo una premisa simple:

> Primero diseñar, luego programar.

Cada nueva funcionalidad comienza definiendo claramente:

- Qué responsabilidad tiene.
- Qué recibe como entrada.
- Qué devuelve.
- Qué cosas NO debe hacer.

Una vez validado el diseño, se implementa el código, se escriben los tests y finalmente se actualiza la documentación.

Este enfoque busca construir un proyecto mantenible, escalable y fácil de entender.