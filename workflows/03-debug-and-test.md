# Flujo 03 — Diagnóstico, reparación y pruebas

**Activación:** `TEST: diagnostica [error o comportamiento]`

## Objetivo

Encontrar la causa raíz, reproducir el defecto, repararlo y comprobar que no rompió otras funciones.

## Diagnóstico

1. Captura el mensaje de error completo, contexto, hora, entorno y acción que lo produce.
2. Separa síntomas, causa confirmada y posibles causas.
3. Revisa logs, stack trace, cambios recientes, configuración y dependencias relevantes.
4. Reproduce el fallo con los pasos mínimos posibles.
5. Si no puede reproducirse, indica qué evidencia falta y evita afirmar una causa definitiva.

## Reparación

1. Prioriza causas raíz frente a parches cosméticos.
2. Propón la corrección mínima y los archivos afectados.
3. Considera regresiones, validación de entradas, permisos, concurrencia y fallos de red.
4. Conserva compatibilidad con los datos y contratos existentes.
5. No desactives seguridad o validaciones para ocultar el error.

## Verificación

Ejecuta solo pruebas disponibles y autorizadas:
- Unitarias para lógica aislada.
- Integración para servicios y base de datos.
- End-to-end para flujos críticos.
- Responsive y accesibilidad para interfaz.
- Regresión para áreas cercanas al cambio.

Registra comando, entorno, resultado, salida relevante y cualquier prueba no ejecutada. Una inspección estática no equivale a una prueba ejecutada.

## Severidad

- **P0 crítica:** exposición de datos, pérdida masiva o sistema indisponible.
- **P1 alta:** flujo principal bloqueado o corrupción importante.
- **P2 media:** función secundaria defectuosa con alternativa.
- **P3 baja:** detalle visual, texto o mejora menor.

## Entregables

Usa `bug-report.md` y `test-report.md`. Cierra con causa raíz confirmada o pendiente, corrección aplicada, resultado de regresión y riesgos residuales.
