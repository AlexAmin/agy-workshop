# AGY Workshop Skills

Plantilla para el taller de Google Antigravity (`agy`). Contiene tres skills de
agente listas para usar: **manager**, **coder** y **tester**. No incluye código
de aplicación: lo pones tú.

## Los tres roles

- **manager**: dirige el trabajo, lo reparte entre agentes y exige pruebas; nunca escribe código.
- **coder**: resuelve un issue de GitHub cada vez, primero con un test que falla y luego con el arreglo.
- **tester**: comprueba qué es verdad y lo deja por escrito en `test-results/<issue>.md`; nunca corrige.

## Cómo usarlo

1. Pulsa **Use this template** en GitHub (o clona el repositorio).
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta `agy`.

Las skills viven en `.agents/skills/` y se cargan bajo demanda, cuando la tarea las necesita.

## Principio

**Nadie corrige su propia tarea.**

## Licencia

MIT
