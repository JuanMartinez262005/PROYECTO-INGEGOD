## 1. Análisis de Cardinalidad (El caso dim_host_bad)

En este ejercicio comparamos cómo un JOIN mal diseñado puede "inventar" datos mediante la duplicación de filas.

| Métrica | Valor |
| `n_fact` (Planetas originales) | 6107 |
| `n_join_good` (JOIN con dimensión limpia) | 6107 |
| `n_join_bad` (JOIN con dimensión sucia) | 10779 |
| `n_join_fixed` (JOIN corregido con CTE) | 6107 |

### ¿Qué pasó aquí?
> **Instrucción:** Lo que sucedio es, `dim_host_bad` tiene varias filas para el mismo `hostname` y al hacer un join de muchos a muchos las filas se duplicaran y al usar `DISTINCT` o `GROUP BY` logramos eliminar las diversar filas para un mismo `hostname`.

## 2. Respuestas TU TURNO (1–4)

### # TODO (1) LEFT JOIN y no-match
# Objetivo: ¿cuántas filas de fact_planet quedan SIN match en dim_host?
# Pistas:
# - Usa LEFT JOIN fact_planet f con dim_host h ON f.hostname = h.hostname
# - Cuenta las filas donde h.hostname IS NULL
query = """
SELECT count(*)
FROM fact_planet_raw f
LEFT JOIN dim_host_ra h ON f.hostname = h.hostname
WHERE h.hostname IS NULL
"""
con.sql(query).show()

┌──────────────┐
│ count_star() │
│    int64     │
├──────────────┤
│            0 │
└──────────────┘

### # TODO (2) CTE + ranking
# Objetivo: por cada disc_year, obtener el discoverymethod #1 (más planetas) y su conteo
# Pistas:
# - Agrupa por disc_year, discoverymethod y cuenta
# - Usa una ventana: ROW_NUMBER() OVER(PARTITION BY disc_year ORDER BY n DESC)
# - Filtra rn = 1
query = """
WITH counts AS (
  SELECT 
    disc_year, 
    discoverymethod, 
    count(*) AS n
  FROM fact_planet_raw
  GROUP BY disc_year, discoverymethod
),
ranked AS (
  SELECT 
    *,
    ROW_NUMBER() OVER(PARTITION BY disc_year ORDER BY n DESC) AS rn
  FROM counts
)
SELECT * FROM ranked
WHERE rn = 1
ORDER BY disc_year DESC
LIMIT 20
"""
con.execute(query).fetchall()

[(2026, 'Transit', 10, 1),
 (2025, 'Transit', 141, 1),
 (2024, 'Transit', 187, 1),
 (2023, 'Transit', 224, 1),
 (2022, 'Transit', 191, 1),
 (2021, 'Transit', 457, 1),
 (2020, 'Transit', 165, 1),
 (2019, 'Transit', 107, 1),
 (2018, 'Transit', 242, 1),
 (2017, 'Transit', 87, 1),
 (2016, 'Transit', 1432, 1),
 (2015, 'Transit', 99, 1),
 (2014, 'Transit', 798, 1),
 (2013, 'Transit', 80, 1),
 (2012, 'Transit', 93, 1),
 (2011, 'Transit', 79, 1),
 (2010, 'Transit', 47, 1),
 (2009, 'Radial Velocity', 70, 1),
 (2008, 'Radial Velocity', 36, 1),
 (2007, 'Radial Velocity', 34, 1)]


#### TODO (3) Validación de cardinalidad
# Objetivo: detectar si hay duplicados en la clave (discoverymethod, disc_year) dentro de dim_discovery
# Pistas:
# - GROUP BY discoverymethod, disc_year
# - HAVING COUNT(*) > 1
query = """
SELECT discoverymethod, disc_year, COUNT(*)
FROM dim_discovery
GROUP BY discoverymethod, disc_year
HAVING COUNT(*) > 1
"""
con.execute(query).fetchall()

[]


#### TODO (4) JOIN + agregación
# Objetivo: para cada discoverymethod, contar planetas y calcular el promedio de RA del host.
# Nota: dim_host_ra solo tiene (hostname, ra). Por eso usamos ra (no st_teff).
# Pistas:
# - JOIN fact_planet_raw (f) con dim_host_ra (h) por hostname
# - Filtra discoverymethod y ra no nulos
# - GROUP BY discoverymethod
query = """
SELECT 
    f.discoverymethod, 
    COUNT(*) AS n_planets,
    AVG(h.ra) AS avg_ra                
FROM fact_planet_raw f
JOIN dim_host_ra h ON f.hostname = h.hostname
WHERE 
    f.discoverymethod IS NOT NULL 
    AND h.ra IS NOT NULL
GROUP BY discoverymethod
"""
con.sql(query).show()

┌───────────────────────────────┬───────────┬────────────────────┐
│        discoverymethod        │ n_planets │       avg_ra       │
│            varchar            │   int64   │       double       │
├───────────────────────────────┼───────────┼────────────────────┤
│ Transit                       │      4501 │  246.8030502154411 │
│ Imaging                       │        92 │ 182.85503756847822 │
│ Pulsation Timing Variations   │         2 │       315.24251065 │
│ Radial Velocity               │      1166 │ 175.88757306286476 │
│ Eclipse Timing Variations     │        17 │ 223.46418367647058 │
│ Microlensing                  │       266 │  267.3047892255641 │
│ Astrometry                    │         6 │ 235.42183843333336 │
│ Disk Kinematics               │         1 │        167.0133422 │
│ Orbital Brightness Modulation │         9 │ 292.91250224444445 │
│ Transit Timing Variations     │        39 │ 250.08277321538466 │
│ Pulsar Timing                 │         8 │      218.743126825 │
├───────────────────────────────┴───────────┴────────────────────┤
│ 11 rows                                              3 columns │
└────────────────────────────────────────────────────────────────┘



###  Tarea dos consultas extra:
# 1
con.execute("""
CREATE OR REPLACE TABLE fact_planet_raw AS
SELECT
  pl_name,
  hostname,
  discoverymethod,
  disc_year,
  pl_orbper,
  pl_rade,
  pl_bmasse,
  pl_eqt,
  pl_dens,
FROM raw_ps
WHERE pl_name IS NOT NULL
""")

con.execute("""
SELECT 
    f.discoverymethod, 
    AVG(f.pl_dens) AS avg_planet_density,
    COUNT(*) AS total_planets
FROM fact_planet_raw f
JOIN dim_host_ra h ON f.hostname = h.hostname 
WHERE f.pl_dens IS NOT NULL
GROUP BY f.discoverymethod
ORDER BY avg_planet_density DESC;""").fetchone()



[('Transit Timing Variations', 38.697378378378374, 37),
 ('Astrometry', 14.358333333333334, 6),
 ('Imaging', 11.589952272727276, 88),
 ('Pulsation Timing Variations', 6.6450000000000005, 2),
 ('Pulsar Timing', 6.081428571428573, 7),
 ('Eclipse Timing Variations', 5.853333333333334, 15),
 ('Transit', 4.940620697937907, 4413),
 ('Radial Velocity', 3.6358328873114485, 1127),
 ('Microlensing', 2.914432330827066, 266),
 ('Orbital Brightness Modulation', 2.5708333333333333, 6),
 ('Disk Kinematics', 1.86, 1)]

# 2
con.sql("""WITH cleaned_data AS (
    SELECT 
        f.discoverymethod, 
        f.pl_dens,
        h.hostname
    FROM fact_planet_raw f
    JOIN dim_host_ra h ON f.hostname = h.hostname
    WHERE f.pl_dens IS NOT NULL 
      AND f.pl_dens > 1 -- filtro extra, densidades mayores que el agua
)
SELECT 
    discoverymethod, 
    AVG(pl_dens) AS avg_planet_density,
    COUNT(*) AS total_planets
FROM cleaned_data
GROUP BY discoverymethod
ORDER BY avg_planet_density DESC""").show()



┌───────────────────────────────┬────────────────────┬───────────────┐
│        discoverymethod        │ avg_planet_density │ total_planets │
│            varchar            │       double       │     int64     │
├───────────────────────────────┼────────────────────┼───────────────┤
│ Transit Timing Variations     │  54.87653846153846 │            26 │
│ Astrometry                    │ 14.358333333333334 │             6 │
│ Imaging                       │ 12.411463414634149 │            82 │
│ Pulsation Timing Variations   │ 6.6450000000000005 │             2 │
│ Pulsar Timing                 │  6.081428571428573 │             7 │
│ Transit                       │   5.86666938541666 │          3648 │
│ Eclipse Timing Variations     │  5.853333333333334 │            15 │
│ Radial Velocity               │  4.871840378109456 │           804 │
│ Microlensing                  │  4.588471337579617 │           157 │
│ Orbital Brightness Modulation │              3.024 │             5 │
│ Disk Kinematics               │               1.86 │             1 │
├───────────────────────────────┴────────────────────┴───────────────┤
│ 11 rows                                                  3 columns │
└────────────────────────────────────────────────────────────────────┘