# DEPLOY — publicación y operación

**Entrada:** versión aprobada, pruebas y configuración de producción.

## Preflight
- Build y pruebas en verde.
- Secretos y variables configurados de forma segura.
- Migraciones revisadas y backup disponible.
- Dominio, TLS, CORS, headers y permisos revisados.
- Logs, métricas, alertas y rollback definidos.
- Derechos, privacidad y términos revisados.

Explica proveedor, coste, riesgos y comandos. Ejecuta cambios externos o despliegues solo después de autorización explícita. Tras desplegar, verifica URL, health check y flujo crítico. No digas “publicado” hasta comprobarlo.

**Entregables:** `deploy-checklist.md`, `runbook.md`, `deployment-report.md`.
