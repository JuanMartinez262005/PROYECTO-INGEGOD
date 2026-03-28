
# Decisiones Del Proyecto

1.*Este documento registra las decisiones clave tomadas durante el desarrollo del proyecto. Cada entrada incluye la fecha, la decisión tomada, las opciones consideradas y la justificación para la elección final.*

---

## Decisión 3: Orquestación y Umbrales de Tiempo (SLA)

**Fecha:** 2026-03-28  
**Contexto:** Necesitamos asegurar que el pipeline sea eficiente y no crezca en tiempo de ejecución de forma descontrolada al procesar los ~6,100 registros.

**Decisión:** Implementar un runner centralizado que mida tiempos por etapa y establecer un umbral de éxito (SLA) de **menos de 5 segundos** para la etapa de dimensiones (`dims`).

**Evidencia:**
* **Métrica actual:** `dims` tomó **0.7521s**.
* **Estado:** ✅ CUMPLE (muy por debajo del umbral de 5s).
* **Conteo de filas:** 4,550 estrellas y 6,101 planetas procesados correctamente.

**Justificación:** Medir el tiempo nos permite detectar problemas de rendimiento si el volumen de datos de la NASA crece en el futuro.

---

## Implementación de Surrogate Keys (SK) y Foreign Keys (FK)

**Fecha:** 2026-03-28  
**Contexto:** Originalmente, las tablas se unían mediante el nombre de la estrella (`hostname`), lo cual es ineficiente y propenso a errores si los nombres cambian o tienen caracteres especiales.

**Decisión:** Creamos la tabla `dim_host_sk` generando un identificador único numérico (`host_id`) mediante la función `ROW_NUMBER()`. Este ID actúa como nuestra "Llave Subrogada" (Surrogate Key).

**Justificación (Imagen Mental del Hotel):** * **El Problema:** Usar el nombre del huésped ("Sr. Alpha Centauri") para registrar pedidos es caótico si el nombre cambia o es muy largo.
* **La Solución:** Asignamos un **Número de Habitación** (`host_id`). Es un número pequeño, rápido de leer para el sistema y nunca cambia, sin importar el nombre del huésped.
* **Integridad:** La FK actúa como un guardia que no permite registrar un planeta en una habitación que no existe.

**Evidencia:** * `orphan_rows`: 0 (confirmado mediante anti-join).
* Unicidad: 4550 hosts únicos con 4550 IDs únicos.

---

## Definición de Capas Gold y Métricas de Negocio

**Fecha:** 2026-03-28  
**Contexto:** Los científicos necesitan entender no solo cuántos planetas hay, sino sus características físicas generales según cómo fueron encontrados o dónde están.

**Decisión:** Materializamos dos vistas finales (`gold_by_discoverymethod` y `gold_by_host`) que incluyen agregaciones de masa (`pl_bmasse`) y radio (`pl_rade`).

**Justificación:** * **Agregación por Método:** Permite identificar sesgos (ej. si el método de Tránsito encuentra mayormente planetas pequeños comparado con Imagen Directa).
* **Agregación por Host:** Identifica sistemas multi-planetarios "poblados" como TRAPPIST-1, facilitando el estudio de zonas de habitabilidad.

**Evidencia:** * Archivos generados en `artifacts/`: `gold_by_discoverymethod.csv` y `gold_by_host.csv`.

---




| Fecha 11/03/2026 JJ| Reglas de silver aplicadas
| Evidencia: guardada en `data_contract_silver_v1.json`
┌─────────────────┬─────────────┬─────────┬─────────┬─────────┬─────────┐
│   column_name   │ column_type │  null   │   key   │ default │  extra  │
│     varchar     │   varchar   │ varchar │ varchar │ varchar │ varchar │
├─────────────────┼─────────────┼─────────┼─────────┼─────────┼─────────┤
│ pl_name         │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ hostname        │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ discoverymethod │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
│ disc_year       │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ sy_snum         │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ sy_pnum         │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
│ sy_dist         │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ ra              │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ dec             │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ pl_orbper       │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ pl_rade         │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ pl_bmasse       │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ pl_eqt          │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ st_teff         │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ st_rad          │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
│ st_mass         │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
├─────────────────┴─────────────┴─────────┴─────────┴─────────┴─────────┤
│ 16 rows                                                     6 columns │
└───────────────────────────────────────────────────────────────────────┘

| Fecha 11/03/2026 JJ| Decisión:Escogi las siguientes filas en el W04 
    pl_name, 
    hostname,
    discoverymethod,
    disc_year,
    sy_snum,
    sy_pnum, 
    sy_dist, 
    ra, 
    dec, 
    pl_orbper, 
    pl_rade, 
    pl_bmasse, 
    pl_eqt, 
    st_teff, 
    st_rad, 
    st_mass,
porque considero que tienen la interpretacion mas simple.
Evidencia:
┌────────┬───────┐
│ n_rows │ n_pl  │
│ int64  │ int64 │
├────────┼───────┤
│   6101 │  6101 │
└────────┴───────┘|

| Fecha 02/03/2026 JJ| Decisión:Valide la cardinalidad antes de un JOIN documentado en `docs_JuanJose/w03_sql_practice.md`.| 

| Fecha 23/02/2026 JJ| Decisión: Se Realiza  notebook 2 y tereas,   se almacenan en docs/w02a_sql_practice.md| Justificación: Es tarea.|

| Fecha 11/02/2026 JE| Decisión: Guardar SHA-256 del CSV raw en artifacts por cada ejecución. Implementación de querys para busqueda de datos. Solución de w01b y w02a. Se agregan columnas al Compars.csv. Se entrega evidencia json y md.| Opciones Consideradas: N/A| Justificación: Innecesaria.|

| Fecha 10/02/2026 JE| Decisión: Se importan los datos raw desde el script download_exoplanets.py.| Opciones Consideradas: N/A| Justificación: Innecesaria.|

| Fecha 10/02/2026 JE| Decisión: Se crea una primera versión del readme, asi como los requirements necesarios.| Opciones Consideradas: Se importan los mismos del repositorio guia del docente.| Justificación: Innecesaria.|

| Fecha 04/02/2026 JJ| Decisión: Se actualiza carpetas, se incluye notebooks y requierements.| Justificación: tener los notebooks accesibles.|

| Fecha 04/02/2026 JE| Decisión: Se crea el entorno vitual. Se vincula con Github y se añade colaboradores. Se configura la estructura del proyecto, y se comienza la documentación.| Opciones Consideradas: Se vincula con SSH, descartando https.| Justificación: Innecesaria.|



