# TU TURNO 1: pega aquí una consulta tipo "métrica" y mira su plan.
# Debe tener: WHERE + GROUP BY (como en W02A).
# Ejemplo de idea: por disc_year o por discoverymethod.

# Definimos una consulta que use WHERE y GROUP BY
q = '''
SELECT 
    disc_year, 
    COUNT(*) AS total_planets
FROM fact_planet
WHERE discoverymethod IN ('Transit', 'Radial Velocity')
GROUP BY disc_year
ORDER BY disc_year DESC;
'''

# 1. Miramos el plan estimado
print("--- PLAN ESTIMADO (EXPLAIN) ---")
res = con.sql("EXPLAIN " + q).fetchall()
print(res[0][1]) # Accedemos directamente al string del plan

# 2. Miramos el plan real con tiempos de ejecución
#print("\n--- PLAN REAL (EXPLAIN ANALYZE) ---")
#res = con.sql("EXPLAIN ANALYZE " + q).fetchall()
#print(res[0][1]) # Accedemos directamente al string del plan

--- PLAN ESTIMADO (EXPLAIN) ---
┌───────────────────────────┐
│         PROJECTION        │
│    ────────────────────   │
│__internal_decompress_integ│
│    ral_bigint(#0, 1992)   │
│             #1            │
│                           │
│          ~0 rows          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│          ORDER_BY         │
│    ────────────────────   │
│      exoplanets.main      │
│.fact_planet.disc_year DESC│
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│__internal_compress_integra│
│    l_utinyint(#0, 1992)   │
│             #1            │
│                           │
│          ~30 rows         │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│__internal_decompress_integ│
│    ral_bigint(#0, 1992)   │
│             #1            │
│                           │
│          ~30 rows         │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│   PERFECT_HASH_GROUP_BY   │
│    ────────────────────   │
│         Groups: #0        │
│                           │
│        Aggregates:        │
│        count_star()       │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│         disc_year         │
│                           │
│        ~1,220 rows        │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│__internal_compress_integra│
│    l_utinyint(#0, 1992)   │
│                           │
│        ~1,220 rows        │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│             #1            │
│                           │
│        ~1,220 rows        │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│           FILTER          │
│    ────────────────────   │
│    ((discoverymethod =    │
│       'Transit') OR       │
│ (discoverymethod = 'Radial│
│         Velocity'))       │
│                           │
│        ~1,220 rows        │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         SEQ_SCAN          │
│    ────────────────────   │
│     Table: fact_planet    │
│   Type: Sequential Scan   │
│                           │
│        Projections:       │
│      discoverymethod      │
│         disc_year         │
│                           │
│          Filters:         │
│ optional: discoverymethod │
│   IN ('Transit', 'Radial  │
│         Velocity')        │
│                           │
│        ~6,101 rows        │
└───────────────────────────┘

El mayor costo esta en el FILTER ya es cuando mas filas reducimos y antes de este debemos trabajar com mas filas 

# TU TURNO 2: escribe dos consultas equivalentes:
# A) con SELECT * y B) con solo 3 columnas.
# Luego compara sus planes.

qA = '''
SELECT * FROM fact_planet
WHERE disc_year IS NOT NULL
ORDER BY disc_year
'''
qB = '''
SELECT pl_name, disc_year, discoverymethod FROM fact_planet
WHERE disc_year IS NOT NULL
ORDER BY disc_year
'''

a=con.sql("EXPLAIN ANALYZE" + qA).fetchall()
print(a[0][1])
b=con.sql("EXPLAIN ANALYZE" + qB).fetchall()
print(b[0][1])

┌─────────────────────────────────────┐
│┌───────────────────────────────────┐│
││    Query Profiling Information    ││
│└───────────────────────────────────┘│
└─────────────────────────────────────┘
EXPLAIN ANALYZE SELECT * FROM fact_planet WHERE disc_year IS NOT NULL ORDER BY disc_year 
┌────────────────────────────────────────────────┐
│┌──────────────────────────────────────────────┐│
││              Total Time: 0.0054s             ││
│└──────────────────────────────────────────────┘│
└────────────────────────────────────────────────┘
┌───────────────────────────┐
│           QUERY           │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│      EXPLAIN_ANALYZE      │
│    ────────────────────   │
│           0 rows          │
│          (0.00s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│             #0            │
│             #1            │
│             #2            │
│__internal_decompress_integ│
│    ral_bigint(#3, 1992)   │
│             #4            │
│             #5            │
│             #6            │
│             #7            │
│                           │
│         6,100 rows        │
│          (0.00s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│          ORDER_BY         │
│    ────────────────────   │
│      exoplanets.main      │
│ .fact_planet.disc_year ASC│
│                           │
│         6,100 rows        │
│          (0.00s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│             #0            │
│             #1            │
│             #2            │
│__internal_compress_integra│
│    l_utinyint(#3, 1992)   │
│             #4            │
│             #5            │
│             #6            │
│             #7            │
│                           │
│         6,100 rows        │
│          (0.00s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│          pl_name          │
│          hostname         │
│      discoverymethod      │
│         disc_year         │
│         pl_orbper         │
│          pl_rade          │
│         pl_bmasse         │
│           pl_eqt          │
│                           │
│         6,100 rows        │
│          (0.00s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         TABLE_SCAN        │
│    ────────────────────   │
│     Table: fact_planet    │
│   Type: Sequential Scan   │
│                           │
│        Projections:       │
│         disc_year         │
│          pl_name          │
│          hostname         │
│      discoverymethod      │
│         pl_orbper         │
│          pl_rade          │
│         pl_bmasse         │
│           pl_eqt          │
│                           │
│          Filters:         │
│  (disc_year IS NOT NULL)  │
│                           │
│         6,100 rows        │
│          (0.00s)          │
└───────────────────────────┘

┌─────────────────────────────────────┐
│┌───────────────────────────────────┐│
││    Query Profiling Information    ││
│└───────────────────────────────────┘│
└─────────────────────────────────────┘
EXPLAIN ANALYZE SELECT pl_name, disc_year, discoverymethod FROM fact_planet WHERE disc_year IS NOT NULL ORDER BY disc_year 
┌────────────────────────────────────────────────┐
│┌──────────────────────────────────────────────┐│
││              Total Time: 0.0033s             ││
│└──────────────────────────────────────────────┘│
└────────────────────────────────────────────────┘
┌───────────────────────────┐
│           QUERY           │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│      EXPLAIN_ANALYZE      │
│    ────────────────────   │
│           0 rows          │
│          (0.00s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│             #0            │
│__internal_decompress_integ│
│    ral_bigint(#1, 1992)   │
│             #2            │
│                           │
│         6,100 rows        │
│          (0.00s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│          ORDER_BY         │
│    ────────────────────   │
│      exoplanets.main      │
│ .fact_planet.disc_year ASC│
│                           │
│         6,100 rows        │
│          (0.00s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│             #0            │
│__internal_compress_integra│
│    l_utinyint(#1, 1992)   │
│             #2            │
│                           │
│         6,100 rows        │
│          (0.00s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│          pl_name          │
│         disc_year         │
│      discoverymethod      │
│                           │
│         6,100 rows        │
│          (0.00s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         TABLE_SCAN        │
│    ────────────────────   │
│     Table: fact_planet    │
│   Type: Sequential Scan   │
│                           │
│        Projections:       │
│         disc_year         │
│          pl_name          │
│      discoverymethod      │
│                           │
│          Filters:         │
│  (disc_year IS NOT NULL)  │
│                           │
│         6,100 rows        │
│          (0.00s)          │
└───────────────────────────┘
Entre menos columnas tengamos que usar mas eficiente sera el proceso, ya que tendremos que cargar menos informacion


# TU TURNO 3: valida un JOIN sano con evidencia
# 1) arma un JOIN fact_planet + dim_host_full (LEFT JOIN)
# 2) muestra EXPLAIN
# 3) muestra n_fact vs n_join

q_join = '''
SELECT count(*)
FROM fact_planet AS f
LEFT JOIN dim_host_full h
    ON  h.hostname = f.hostname
'''

a = con.sql("EXPLAIN " + q_join).fetchall()
print(a[0][1])

n_fact = con.sql("SELECT COUNT(*) FROM fact_planet").fetchone()[0]
n_join = con.sql('''
SELECT count(*)
FROM fact_planet AS f
LEFT JOIN dim_host_full h
    ON h.hostname = f.hostname
''').fetchone()[0]

n_fact, n_join


┌───────────────────────────┐
│    UNGROUPED_AGGREGATE    │
│    ────────────────────   │
│        Aggregates:        │
│        count_star()       │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         HASH_JOIN         │
│    ────────────────────   │
│      Join Type: LEFT      │
│                           │
│        Conditions:        ├──────────────┐
│    hostname = hostname    │              │
│                           │              │
│        ~6,101 rows        │              │
└─────────────┬─────────────┘              │
┌─────────────┴─────────────┐┌─────────────┴─────────────┐
│         SEQ_SCAN          ││         SEQ_SCAN          │
│    ────────────────────   ││    ────────────────────   │
│     Table: fact_planet    ││    Table: dim_host_full   │
│   Type: Sequential Scan   ││   Type: Sequential Scan   │
│   Projections: hostname   ││   Projections: hostname   │
│                           ││                           │
│        ~6,101 rows        ││        ~4,550 rows        │
└───────────────────────────┘└───────────────────────────┘
(6101, 6101)

evidencia de que para  hacer un  join se debe hacer dos SCAN uno para cada tabla, si en fact_planet solo seleccionamos la columna hostname el tiempo se reduce en comparacion con count(*)