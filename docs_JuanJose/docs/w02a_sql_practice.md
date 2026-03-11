# cual es el metodo que mejor a detectado los planetas mas pequeños
query = """
SELECT 
    discoverymethod,
    AVG(pl_rade) AS avg
FROM raw_ps
WHERE pl_rade IS NOT NULL
GROUP BY discoverymethod
ORDER BY avg ASC
"""
con.execute(query).fetchall()

# el metodo Transit ha descuvierto los planetas con menor radio en promedio ya que su tecnica es: 
# El método de tránsito detecta exoplanetas midiendo la disminución periódica en el brillo de una estrella cuando un planeta pasa frente a ella (tránsito), bloqueando una pequeña parte de su luz

[('Transit', 4.368151792099998),
 ('Pulsar Timing', 5.411333333333334),
 ('Transit Timing Variations', 6.493408364210528),
 ('Orbital Brightness Modulation', 9.64504),
 ('Radial Velocity', 9.759872661948641),
 ('Microlensing', 9.850563909774435),
 ('Astrometry', 12.450000000000001),
 ('Pulsation Timing Variations', 12.75),
 ('Eclipse Timing Variations', 12.893333333333338),
 ('Disk Kinematics', 13.3),
 ('Imaging', 15.612215793749998)]





# que hostname tiene los planetas mas grandes

query = """
SELECT 
    hostname,
    AVG(pl_rade) AS avg
FROM raw_ps
WHERE pl_rade IS NOT NULL
GROUP BY hostname
ORDER BY avg DESC
LIMIT 10
"""
con.execute(query).fetchall()

# V2376 Ori tiene los planetas mas grandes de los hostname debido a que tiene dos estrellas: Estrella Primaria: Una estrella joven de tipo M (enana roja).
# Compañera (V2376 Ori b): Es una compañera de masa planetaria que se encuentra en proceso de acreción, lo que significa que está absorbiendo material.

[('V2376 Ori', 87.20586985),
 ('HD 100546', 77.3421),
 ('GQ Lup', 33.6),
 ('DH Tau', 30.2643),
 ('Kepler-1979', 29.33),
 ('PDS 70', 26.677419999999998),
 ('CT Cha', 24.66),
 ('HAT-P-67', 23.9872187),
 ('TOI-3540 A', 23.53885947),
 ('XO-6', 23.20263)]





 # planetas con orbitas esfericas
con.execute("""
        SELECT 
            COUNT(pl_orbeccen) 
        FROM raw_ps 
        WHERE pl_orbeccen = 0
    """).fetchall()

[(3072,)]





# columna con mas nulos entre pl_name pl_bmasse pl_rade
query = """
SELECT 
    (COUNT(*) - COUNT(pl_name)) AS nulos_nombre,
    (COUNT(*) - COUNT(pl_bmasse)) AS nulos_masa,
    (COUNT(*) - COUNT(pl_rade)) AS nulos_radio
FROM raw_ps
"""
con.execute(query).fetchall()

[(0, 31, 50)]




# resultados notebook





[(2016, 1496),
 (2014, 869),
 (2021, 564),
 (2022, 369),
 (2023, 324),
 (2018, 315),
 (2024, 259),
 (2025, 240),
 (2020, 234),
 (2019, 196),
 (2015, 155),
 (2017, 152),
 (2012, 139),
 (2011, 135),
 (2013, 128)]


[('KOI-351', 8),
 ('TRAPPIST-1', 7),
 ('HD 34445', 6),
 ('Kepler-11', 6),
 ('HIP 41378', 6),
 ('HD 10180', 6),
 ('Kepler-80', 6),
 ('HD 191939', 6),
 ('HD 110067', 6),
 ('HD 219134', 6)]


[(0.005076142131979695,)]


[('V2376 Ori b', 87.20586985),
 ('HD 100546 b', 77.3421),
 ('GQ Lup b', 33.6),
 ('Kepler-297 d', 32.6),
 ('PDS 70 b', 30.48848),
 ('DH Tau b', 30.2643),
 ('Kepler-1979 b', 29.33),
 ('TOI-1408 b', 25.0),
 ('CT Cha b', 24.66),
 ('HAT-P-67 b', 23.9872187)]


[('Transit', 4501, 4500),
 ('Radial Velocity', 1166, 1166),
 ('Microlensing', 266, 266),
 ('Imaging', 92, 92),
 ('Transit Timing Variations', 39, 39),
 ('Eclipse Timing Variations', 17, 17),
 ('Orbital Brightness Modulation', 9, 9),
 ('Pulsar Timing', 8, 8),
 ('Astrometry', 6, 6),
 ('Pulsation Timing Variations', 2, 2),
 ('Disk Kinematics', 1, 1)]


[('Pulsation Timing Variations', 1005.0),
 ('Orbital Brightness Modulation', 0.81161),
 ('Imaging', 33000.0),
 ('Transit Timing Variations', 30.0),
 ('Pulsar Timing', 25.262),
 ('Transit', 8.15872),
 ('Radial Velocity', 298.895),
 ('Eclipse Timing Variations', 3160.0),
 ('Microlensing', 3142.5),
 ('Astrometry', 334.76)]