# Checks sobre la tabla raw_ps

## Check 1

n_rows = con.execute("SELECT COUNT(*) FROM raw_ps").fetchone()[0]
n_cols = con.execute("SELECT COUNT(*) FROM pragma_table_info('raw_ps')").fetchone()[0]
n_rows, n_cols

(6100, 19)

## 2. nulos en una columna clave típica

con.execute("SELECT COUNT(*) AS null_pl_name FROM raw_ps WHERE pl_name IS NULL").fetchall()

[(0,)]

## Check 3

con.execute("SELECT pl_name, hostname, discoverymethod, disc_year FROM raw_ps WHERE pl_name IS NOT NULL LIMIT 10").fetchall()

[('Kepler-1167 b', 'Kepler-1167', 'Transit', 2016),
 ('Kepler-1740 b', 'Kepler-1740', 'Transit', 2021),
 ('Kepler-1581 b', 'Kepler-1581', 'Transit', 2016),
 ('Kepler-644 b', 'Kepler-644', 'Transit', 2016),
 ('Kepler-1752 b', 'Kepler-1752', 'Transit', 2021),
 ('Kepler-280 c', 'Kepler-280', 'Transit', 2014),
 ('Kepler-1208 b', 'Kepler-1208', 'Transit', 2016),
 ('Kepler-263 c', 'Kepler-263', 'Transit', 2014),
 ('Kepler-1101 b', 'Kepler-1101', 'Transit', 2016),
 ('HD 168746 b', 'HD 168746', 'Radial Velocity', 2002)]

## Check 4

### Sanity Check Extra — Duplicados por pl_name

"""
SELECT  
    pl_name,
    COUNT(*) AS n
FROM raw_ps
GROUP BY pl_name
HAVING COUNT(*) > 1
ORDER BY n DESC
"""

Resultado:
0 duplicados encontrados []
