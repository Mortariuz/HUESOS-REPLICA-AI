# Flujo 05 — Preparación y publicación segura

**Activación:** `LAUNCH` y, con autorización, `DEPLOY`

## Antes de publicar

1. Confirma el entorno objetivo: local, preview, staging o producción.
2. Revisa build, pruebas, migraciones y cambios pendientes.
3. Comprueba variables y secretos sin imprimir sus valores.
4. Verifica autenticación, autorización, CORS, headers, HTTPS y exposición de datos.
5. Comprueba backups y procedimiento de restauración cuando haya datos persistentes.
6. Define health check, flujo crítico de verificación y plan de rollback.
7. Identifica costes, límites del proveedor y recursos que se crearán.

## Puerta de autorización

Antes de crear recursos externos, incurrir en costes, alterar datos reales o desplegar, presenta:
- Qué acción se ejecutará.
- Entorno y recursos afectados.
- Coste estimado o límites conocidos.
- Riesgo y reversión.
- Comandos o pasos previstos.

Espera aprobación explícita para la acción de impacto. La autorización para preparar el despliegue no implica autorización para ejecutarlo.

## Después de publicar

Solo si la publicación se ejecutó:
1. Verifica la URL real y el estado del servicio.
2. Ejecuta un health check y el flujo crítico.
3. Comprueba logs y errores recientes.
4. Registra versión, commit, fecha, entorno y resultado.
5. Documenta rollback y cualquier incidencia.

## Entregables

- `release-checklist.md`
- `deployment-report.md`
- `runbook.md`

Nunca declares “desplegado” o “en producción” basándote únicamente en un comando preparado o en un commit.
