# Turno 1: 
┌─────────────────┬───────┐
│       col       │ nulls │
│     varchar     │ int64 │
├─────────────────┼───────┤
│ pl_orbper       │   323 │
│ pl_rade         │    50 │
│ pl_bmasse       │    31 │
│ sy_dist         │    27 │
│ disc_year       │     1 │
│ dec             │     0 │
│ discoverymethod │     0 │
│ hostname        │     0 │
│ pl_name         │     0 │
│ ra              │     0 │
│ sy_pnum         │     0 │
│ sy_snum         │     0 │
├─────────────────┴───────┤
│ 12 rows       2 columns │
└─────────────────────────┘

# Turno 2: 
# A) pl_rade (radio) en rango didáctico
query = """
SELECT COUNT(*) AS n_bad_pl_rade
FROM raw_ps
WHERE pl_rade IS NOT NULL
  AND (pl_rade <= 0 OR pl_rade > 30)
"""
con.sql(query).show()

┌───────────────┐
│ n_bad_pl_rade │
│     int64     │
├───────────────┤
│             6 │
└───────────────┘

De todos los datos solo hay 6 planetas con radios fuera de lo normal y esto puede ser radios  negativos o cero (fisicamente imposible)
o con radios de mas de 30 (muy masivos) Pd. He  provado y sucede que esos 6 son mayores que 30

# Turno 3:
Explicacion: 
La estructura "Sándwich" (UNION ALL): Como cada SELECT devuelve una sola fila con la métrica de un error, el UNION ALL las pone una debajo de otra, creando una tabla resumen de 3 filas.

El uso de ::BIGINT: Asegura que los conteos sean tratados como números enteros de gran capacidad, evitando errores de formato al unir los resultados.

La lógica de exclusión: En el tercer check, el WHERE filtra precisamente lo que no queremos (radios menores a cero o exageradamente grandes), permitiéndonos contar cuántos "problemas" tenemos en la fuente original.

Automatización del Reporte: Al usar ART_DIR, el archivo CSV se guarda automáticamente donde el sistema de entrega lo espera. 

# Turno 4:
Datos exportados a artifacts