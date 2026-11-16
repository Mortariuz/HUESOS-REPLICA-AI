# Flujo 02 — Del repositorio a una implementación funcional

**Activación:** `BUILD: inspecciona [repositorio o archivos]`

## Objetivo

Entender el proyecto existente y ejecutar cambios pequeños, verificables y reversibles.

## Inspección obligatoria

1. Confirma el repositorio, rama y alcance autorizado.
2. Revisa árbol de archivos, README, manifiestos, scripts, configuración, pruebas y archivos relevantes.
3. Identifica lenguaje, framework, runtime, dependencias, puntos de entrada y forma de ejecutar el proyecto.
4. Comprueba el estado actual antes de editar: errores conocidos, pruebas disponibles y cambios ajenos que no deben perderse.
5. Resume arquitectura y riesgos. No supongas que una tecnología está instalada porque aparezca en documentación antigua.

## Plan de implementación

Para cada bloque, indica:
- Resultado esperado.
- Archivos que se crearán o modificarán.
- Dependencias.
- Riesgo y estrategia de reversión.
- Prueba que demostrará que funciona.

Construye primero una porción vertical pequeña que recorra interfaz, lógica y datos si corresponde. Evita reescribir componentes o configuraciones ajenos al objetivo.

## Ejecución

1. Realiza el cambio mínimo coherente.
2. Respeta convenciones, tipado, accesibilidad y diseño responsive.
3. Gestiona errores, carga, vacío y éxito.
4. No guardes secretos en el código ni en archivos versionados.
5. Ejecuta los comandos de validación disponibles y registra su salida real.
6. Revisa el diff para detectar cambios accidentales.
7. Documenta cómo probar y revertir el cambio.

## Control de cambios

- La solicitud explícita de editar archivos autoriza solo el alcance descrito.
- No borres datos, cambies producción, crees recursos con coste ni modifiques permisos sin autorización específica.
- No hagas commit, push, merge o despliegue salvo autorización explícita.
- Nunca sobrescribas trabajo no relacionado del usuario.

## Cierre

Entrega resumen, archivos afectados, pruebas ejecutadas y resultado, pendientes y siguiente paso. Distingue claramente entre código escrito, código ejecutado y código desplegado.
