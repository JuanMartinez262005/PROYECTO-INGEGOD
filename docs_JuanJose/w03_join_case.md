con.execute("""
CREATE OR REPLACE TABLE dim_discoverymethod_bad AS
SELECT discoverymethod
FROM raw_ps
WHERE discoverymethod IS NOT NULL
""")

n_join_bad = con.execute("""
SELECT count(*)
FROM fact_planet_raw f
JOIN dim_discoverymethod_bad h
  ON f.discoverymethod = h.discoverymethod
""").fetchone()[0]

n_join_fixed = con.execute("""
WITH dim_discoverymethod_fixed AS (
  SELECT DISTINCT discoverymethod
  FROM dim_discoverymethod_bad
)
SELECT count(*)
FROM fact_planet_raw f
JOIN dim_discoverymethod_fixed h
  ON f.discoverymethod = h.discoverymethod
""").fetchone()[0]
n_fact, n_join_bad, n_join_fixed

(6107, 21699773, 6107)

# diagnostico:
la multiplicacion de filas en  n_join_bad indica que los discoverymethod en dim_discoverymethod_bad no es unica; con un DISTINCT, solucionamos este join malo