# Flujo 04 — Revisión visual y paridad

**Activación:** `DIFF: compara referencia e implementación`

## Entradas

- Capturas de referencia obtenidas legítimamente.
- Capturas de la implementación en las mismas rutas y estados.
- Viewports, escala, idioma y datos de prueba usados.
- Matriz de funciones y criterios de aceptación.

## Método

1. Asegura que ambas capturas correspondan a la misma ruta, estado, viewport y contenido comparable.
2. Evalúa estructura, alineación, espaciado, jerarquía, tipografía, contraste, iconografía, imágenes y comportamiento responsive.
3. Separa diferencias intencionales de identidad de los defectos de ejecución.
4. Clasifica cada diferencia por impacto: bloqueante, alto, medio o bajo.
5. Compara también el comportamiento de los controles; la similitud visual no demuestra equivalencia funcional.
6. Ordena correcciones por impacto y coste.
7. Vuelve a capturar y revisar después de cada bloque importante.

## Paridad funcional

Usa los pesos de `modules/07-diff.md`: MUST=5, SHOULD=3 y COULD=1. Excluye WON'T del denominador. Marca cada función como completa, parcial, ausente o no verificada. Si faltan estados o evidencias, decláralo.

## Entregables

- `parity-report.md`
- `visual-diff-notes.md`
- `parity.csv`

No prometas una clonación pixel-perfect ni una compatibilidad no probada. El objetivo es satisfacer requisitos observables con diseño y activos originales.
