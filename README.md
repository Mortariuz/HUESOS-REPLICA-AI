# HUESOS REPLICA AI

Kit de trabajo para analizar productos digitales y construir alternativas originales usando ChatGPT. Está inspirado en la estructura de `replica-skill`, pero adaptado a proyectos, instrucciones, archivos de referencia y herramientas disponibles en ChatGPT.

> No es una aplicación alojada, no instala comandos slash automáticamente y no es un producto oficial de OpenAI ni está afiliado con el autor del proyecto de referencia.

## Qué hace

Acompaña el ciclo completo de producto e ingeniería:

1. **RECON:** analiza una web, pantallas, navegación, flujos y estados observables.
2. **ARCHITECT:** define arquitectura, datos, API, integraciones, seguridad y costes.
3. **DESIGN:** crea un sistema visual original y responsive.
4. **BUILD:** implementa la alternativa en un repositorio o conjunto de archivos.
5. **BACKEND:** diseña e integra servicios y persistencia.
6. **TEST:** reproduce errores, corrige y verifica.
7. **DIFF:** compara requisitos, comportamiento y evidencia visual.
8. **MARKET:** investiga mercado y opiniones públicas con fuentes verificables.
9. **BRAND:** desarrolla nombre e identidad diferenciados.
10. **LAUNCH:** prepara calidad, soporte y lanzamiento.
11. **DEPLOY:** prepara y ejecuta publicación solo con autorización.

## Empezar en ChatGPT

Sigue [CHATGPT_SETUP.md](CHATGPT_SETUP.md). Resumen:

1. Crea un Proyecto de ChatGPT llamado **HUESOS REPLICA AI**.
2. Pega el contenido de [HUESOS_REPLICA_MASTER.md](HUESOS_REPLICA_MASTER.md) en las instrucciones del Proyecto.
3. Adjunta los módulos de `modules/`, los flujos de `workflows/` y las plantillas de `templates/` que correspondan.
4. Inicia con: `Iniciar réplica: [URL o descripción]`.

Prompt recomendado:

> Inicia HUESOS REPLICA AI. Analiza esta referencia y el material que adjunto. Primero ejecuta RECON, separa hechos de inferencias, crea el brief y la matriz de funciones. Después propón arquitectura, diseño y una primera versión vertical. Inspecciona el repositorio antes de editar. No hagas commit, push, cambios de producción ni despliegues sin mi autorización explícita.

## Atajos conversacionales

Escribe estos nombres en el chat; son instrucciones de trabajo, no comandos slash nativos:

| Atajo | Resultado |
|---|---|
| `RECON` | Auditoría de web y requisitos |
| `ARCHITECT` | Arquitectura y decisiones técnicas |
| `DESIGN` | Sistema visual y componentes |
| `BUILD` | Implementación incremental |
| `BACKEND` | Datos, API, servicios e integraciones |
| `TEST` | Diagnóstico, reparación y pruebas |
| `DIFF` | Paridad funcional y visual |
| `MARKET` | Investigación de mercado |
| `BRAND` | Identidad original |
| `LAUNCH` | Preparación de lanzamiento |
| `DEPLOY` | Publicación y operación |
| `ESTADO` | Continuidad y próximos pasos |

## Estructura

- `HUESOS_REPLICA_MASTER.md`: instrucciones principales para ChatGPT.
- `CHATGPT_SETUP.md`: instalación en un Proyecto y prompt de inicio.
- `modules/`: 11 módulos por fase.
- `workflows/`: procedimientos prácticos para web, repositorio, bugs, paridad, release y continuidad.
- `templates/`: brief, auditoría, matriz de funciones, plan, bugs, pruebas, decisiones y release.
- `tools/parity.py`: cálculo de paridad ponderada desde CSV.
- `tools/validate_features.py`: validación de estructura y valores de la matriz CSV.

## Herramientas locales

Requiere Python 3.9 o superior; los scripts usan solo la biblioteca estándar.

```bash
python tools/validate_features.py templates/features.csv
python tools/parity.py templates/features.csv
```

La matriz usa las prioridades `MUST`, `SHOULD`, `COULD` y `WONT`; estados aceptados por el validador: `unknown`, `not_started`, `in_progress`, `partial`, `complete`, `blocked` y `excluded`.

## Principios de trabajo

- **Clean-room:** estudiar comportamiento observable e implementar código y activos originales. No copiar código propietario, marca, textos, contenido ni APIs privadas.
- **Evidencia:** distinguir OBSERVADO, INFERIDO, HIPÓTESIS y DESCONOCIDO.
- **Calidad:** definir criterios verificables y ejecutar pruebas disponibles.
- **Seguridad:** proteger secretos, usar mínimo privilegio y no eludir controles de acceso.
- **Cambios controlados:** inspeccionar antes de editar; no borrar, gastar, hacer commit, push, merge, cambiar producción ni desplegar sin autorización específica.
- **Honestidad:** no afirmar que un test, cambio externo o despliegue ocurrió si no se ejecutó y verificó.
- **Diseño diferenciado:** crear identidad, componentes, textos y recursos propios.

## Expediente recomendado por proyecto

Mantén `project-brief.md`, `replica-status.md`, `website-audit.md`, `features.csv`, `implementation-plan.md`, `decision-log.md`, `bug-report.md`, `test-report.md` y `release-checklist.md`. Consulta [workflows/06-session-continuity.md](workflows/06-session-continuity.md) al iniciar y cerrar sesiones.

## Origen

Adaptación independiente inspirada en la metodología de https://github.com/Jakeschincariol/replica-skill (MIT). Respeta la licencia y atribución del proyecto original. Esta adaptación no implica afiliación ni respaldo del autor.
