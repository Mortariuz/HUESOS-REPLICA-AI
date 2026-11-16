# Flujo 01 — De una web a una especificación verificable

**Activación:** `RECON: analiza [URL]`

## Objetivo

Convertir una referencia web en un expediente de producto suficiente para diseñar una alternativa original sin programar a ciegas.

## Procedimiento

1. Confirma el objetivo de la alternativa, los usuarios y las plataformas prioritarias. Si faltan detalles no esenciales, documenta supuestos explícitos y continúa.
2. Inspecciona las páginas públicas accesibles y el material que haya aportado el usuario. Registra URL, título, fecha de observación y limitaciones de acceso.
3. Recorre navegación, rutas y flujos visibles. Observa estados iniciales, carga, vacío, validación, error y éxito cuando sea posible.
4. Registra elementos por pantalla: jerarquía, controles, formularios, filtros, tablas, reproductores, navegación y acciones.
5. Comprueba responsive con las vistas o capturas disponibles. No declares compatibilidad con dispositivos que no se hayan comprobado.
6. Identifica integraciones visibles y dependencias probables, pero no presentes inferencias como hechos internos.
7. Convierte los hallazgos en funciones con prioridad MUST, SHOULD, COULD o WON'T y criterios de aceptación verificables.
8. Señala preguntas abiertas, riesgos de propiedad intelectual, accesibilidad, privacidad y seguridad.
9. Propón la siguiente fase y la primera versión vertical mínima.

## Reglas de evidencia

Etiqueta cada hallazgo como:
- **OBSERVADO:** visible o reproducido directamente.
- **INFERIDO:** conclusión razonable basada en evidencia.
- **HIPÓTESIS:** explicación posible que aún debe comprobarse.
- **DESCONOCIDO:** no fue posible verificarlo.

Guarda evidencia concreta: URL, captura aportada, texto visible o pasos de reproducción. No inventes datos de tráfico, métricas, reseñas, integraciones internas ni estados no observados.

## Límites

No eludas autenticación, paywalls, CAPTCHA, controles anti-bot ni restricciones técnicas. No accedas a cuentas o datos ajenos. Si una pantalla privada es importante, solicita al usuario una captura o documentación obtenida legítimamente.

## Entregables

- `website-audit.md`
- `features.csv`
- `implementation-plan.md`
- `recon-gaps.md`

Cierra con el nivel de cobertura de la inspección y la evidencia que falta. No calcules un porcentaje de cobertura si no existe un denominador definido.
