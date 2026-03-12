
# Decisiones Del Proyecto

1.*Este documento registra las decisiones clave tomadas durante el desarrollo del proyecto. Cada entrada incluye la fecha, la decisión tomada, las opciones consideradas y la justificación para la elección final.*

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



