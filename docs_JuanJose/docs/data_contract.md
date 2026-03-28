# Data Contract - Proyecto Exoplanetas (W06)

## 1. Inventario de Datasets
* **silver_planet**: Tabla de limpieza inicial con filtros de rango de años y medidas físicas.
* **dim_host_sk**: Dimensión de estrellas anfitrionas que utiliza una Llave Subrogada (SK).
* **fact_planet_sk**: Tabla de hechos de planetas que utiliza `host_id` como referencia externa.
* **gold_by_discoverymethod**: Vista de nivel Gold optimizada para análisis por método de descubrimiento.
* **gold_by_host**: Vista de nivel Gold optimizada para análisis por estrella anfitriona.

## 2. Definición de Granularidad (Grain)
* **dim_host_sk**: La unidad mínima es **una fila por cada estrella anfitriona** única (`hostname`).
* **fact_planet_sk**: La unidad mínima es **una fila por cada planeta** único (`pl_name`).

## 3. Modelo de Llaves y Relaciones
* **Primary Keys (PK):**
    * `dim_host_sk.host_id`: Identificador numérico interno (Surrogate Key).
    * `fact_planet_sk.pl_name`: Nombre único del planeta.
* **Foreign Keys (FK):**
    * `fact_planet_sk.host_id` → Referencia obligatoria a `dim_host_sk.host_id`.
* **Restricciones de Unicidad:**
    * `hostname` en la tabla de dimensiones debe ser `UNIQUE` y `NOT NULL`.

## 4. Garantías de Calidad (Checks de Validación)
El pipeline asegura la integridad de los datos mediante las siguientes pruebas ejecutadas en DuckDB:

| Prueba | Descripción | Resultado Obtenido | Estado |
| :--- | :--- | :--- | :--- |
| **Unicidad Dim** | Conteo de filas vs conteo de llaves únicas en `dim_host_sk`. | 4550 / 4550 | ✅ PASA |
| **Integridad Referencial** | Anti-join para buscar planetas con `host_id` inexistente. | 0 huérfanos | ✅ PASA |
| **Consistencia Fact** | Validación del total de registros transferidos a la tabla con SK. | 6101 filas | ✅ PASA |

---
**Fecha de última validación:** 2026-03-28  
**Responsable:** Juan José