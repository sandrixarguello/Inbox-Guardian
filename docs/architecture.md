# 🏗️ Inbox Guardian - Architecture

## Objetivo

Definir las decisiones de arquitectura del proyecto para mantener un código escalable, mantenible y fácil de extender.

---

# Principios de Arquitectura

## Regla #1 - Una responsabilidad por módulo

Cada módulo del proyecto debe tener una única responsabilidad claramente definida.

Esto facilita:

- el mantenimiento del código;
- la incorporación de nuevas funcionalidades;
- la detección y corrección de errores;
- la reutilización de componentes;
- la realización de pruebas unitarias.

### ✔ Correcto

HTML Reader
→ Lee archivos HTML.

HTML Parser
→ Interpreta el contenido HTML.

Image Analyzer
→ Analiza imágenes del documento.

Score Engine
→ Calcula el puntaje final.

### ❌ Incorrecto

html_analyzer.py

- Lee archivos
- Analiza imágenes
- Calcula ratios
- Genera reportes
- Calcula score

Este diseño genera alto acoplamiento y dificulta el mantenimiento.

---

## Principios aplicados

- Single Responsibility Principle (SRP)
- Alta cohesión
- Bajo acoplamiento
- Modularidad
- Escalabilidad

---

Este documento evolucionará junto con la arquitectura del proyecto.