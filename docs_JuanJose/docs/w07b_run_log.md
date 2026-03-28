# Run Log - W07B (Orquestación)

**Fecha:** 2026-03-28  
**Comando ejecutado:** `python -m src.pipeline.w07b_runner`.

## 1. Salida del Terminal (STDOUT)
== Running stage: silver ==
Stage SILVER: building silver_planet
silver_planet rows=6101
Result: {'mode': 'silver', 'return_code': 0, 'seconds': 0.2224}

== Running stage: dims ==
Stage DIMS: building dim_host_full, fact_planet, dim_host_sk, fact_planet_sk
dim_host_sk uniqueness rows=4550, keys=4550
fact_planet rows=6101, fact_planet_sk rows=6101
Result: {'mode': 'dims', 'return_code': 0, 'seconds': 0.7521}

== Running stage: gold ==
Stage GOLD: building views gold_by_discoverymethod and gold_by_host
gold views created
Result: {'mode': 'gold', 'return_code': 0, 'seconds': 0.1376}

== Running stage: export ==
Stage EXPORT: writing artifacts CSV
Wrote gold_by_discoverymethod.csv
Wrote gold_by_host.csv
Result: {'mode': 'export', 'return_code': 0, 'seconds': 0.1461}

## 2. Por qué cambian los tiempos

Los tiempos varían principalmente por la Caché del Sistema Operativo (que acelera las lecturas de disco tras la primera ejecución) y la Variabilidad en el Uso de CPU por procesos externos del sistema. La etapa de dims es la más sensible a estos cambios porque es la que realiza más operaciones intensivas de escritura y cálculo de llaves.