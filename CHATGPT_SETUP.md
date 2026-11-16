# Configuración de HUESOS REPLICA AI en ChatGPT

Esta carpeta convierte el repositorio en un kit de trabajo para un Proyecto de ChatGPT. No es una aplicación web alojada ni instala comandos slash automáticamente.

## Configuración recomendada

1. En ChatGPT, crea un Proyecto llamado **HUESOS REPLICA AI**.
2. Abre las instrucciones del Proyecto y pega el contenido completo de `HUESOS_REPLICA_MASTER.md`.
3. Añade como archivos de conocimiento:
   - Los 11 documentos de `modules/`.
   - Los documentos de `workflows/` que vayas a utilizar.
   - Las plantillas de `templates/` que correspondan al proyecto.
4. En el primer chat, envía el brief y la URL de referencia, si existe.
5. Pide que cree y mantenga un expediente del proyecto con los documentos generados. Descarga o conserva esos documentos en el Proyecto o en el repositorio: no dependas de que el chat recuerde por sí solo todos los archivos.

## Prompt inicial

Copia y adapta este texto:

> Inicia HUESOS REPLICA AI para este proyecto. Primero identifica el objetivo y los usuarios. Revisa la URL, capturas, documentación y/o repositorio que te proporcione. Ejecuta RECON antes de decidir la arquitectura. Separa evidencia, inferencias y dudas. Prepara el brief, la matriz de funciones y un plan por etapas. No modifiques repositorios, no publiques cambios ni despliegues hasta que te autorice expresamente.

## Cómo iniciar cada tipo de trabajo

- **Analizar una web:** `RECON: analiza [URL]`.
- **Planear una alternativa:** `ARCHITECT: usa el expediente de este proyecto`.
- **Diseñar pantallas:** `DESIGN: crea una identidad visual original`.
- **Programar:** `BUILD: inspecciona primero el repositorio y propone el primer bloque`.
- **Reparar:** `TEST: investiga este error y reproduce el problema`.
- **Comparar:** `DIFF: compara la implementación con los criterios y evidencias`.
- **Preparar publicación:** `LAUNCH` y después `DEPLOY`, autorizando cada acción externa.

## Uso de herramientas

ChatGPT solo debe utilizar herramientas, conectores y acceso a archivos que estén realmente disponibles en la conversación. Si una capacidad no está conectada, debe decirlo y proponer el siguiente paso más útil. Para páginas protegidas, utiliza una cuenta y sesión que controles; nunca compartas contraseñas, cookies, claves privadas ni códigos de recuperación.

## Persistencia del expediente

Mantén como mínimo:

- `project-brief.md`
- `replica-status.md`
- `website-audit.md` o `recon.md`
- `features.csv`
- `implementation-plan.md`
- `test-report.md`
- `decision-log.md`

Al cerrar cada sesión, actualiza el estado, los archivos entregados, las decisiones, los bloqueos y el próximo paso.
