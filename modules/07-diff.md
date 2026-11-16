# DIFF — comparación y paridad

**Entrada:** matriz de funciones, capturas y resultados de pruebas.

- Compara cada requisito: completo, parcial, ausente o excluido.
- Pondera MUST=5, SHOULD=3, COULD=1; excluye WON'T del denominador.
- Calcula porcentaje ponderado solo con datos suficientes y muestra fórmula.
- Compara capturas por estructura, alineación, jerarquía y responsive; no penalices diferencias intencionales de marca.
- Lista los 10 gaps principales y correcciones por impacto/coste.
- Señala funcionalidades no verificadas.

**Entregables:** `parity-report.md`, `parity.csv`, `visual-diff-notes.md`. Una puntuación no sustituye pruebas funcionales ni revisión humana.
