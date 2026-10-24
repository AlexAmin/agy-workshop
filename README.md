# AGY Workshop

Plantilla para el taller de Google Antigravity (`agy`). Contiene tres skills de
agente listas para usar: **manager**, **coder** y **tester**, y un pequeño
código de práctica (calculadora de un carrito de la compra, en Python).

## Los tres roles

- **manager**: dirige el trabajo, lo reparte entre agentes y exige pruebas; nunca escribe código.
- **coder**: resuelve un issue de GitHub cada vez, primero con un test que falla y luego con el arreglo.
- **tester**: comprueba qué es verdad y lo deja por escrito en `test-results/<issue>.md`; nunca corrige.

## Cómo usarlo

1. Pulsa **Use this template** en GitHub (o clona el repositorio).
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta `agy`.

Las skills viven en `.agents/skills/` y se cargan bajo demanda, cuando la tarea las necesita.

## Código de práctica

- `shop/`: el código; `tests/`: sus tests.
- `ISSUES.md`: tres issues para trabajar con los agentes.
- Para ejecutar los tests: `python3 -m unittest`

## Principio

**Nadie corrige su propia tarea.**

## Licencia

MIT
