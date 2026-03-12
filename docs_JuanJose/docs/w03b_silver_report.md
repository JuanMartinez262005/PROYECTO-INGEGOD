con.sql("DESCRIBE silver_planet").show()
con.sql("SELECT COUNT(*) AS n_rows, COUNT(DISTINCT hostname) AS n_keys FROM silver_planet").show()
con.sql("SELECT COUNT(*) AS n_rows, COUNT(DISTINCT pl_name) AS n_keys FROM silver_planet").show()

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

┌────────┬────────┐
│ n_rows │ n_keys │
│ int64  │ int64  │
├────────┼────────┤
│   6101 │   4550 │
└────────┴────────┘

┌────────┬────────┐
│ n_rows │ n_keys │
│ int64  │ int64  │
├────────┼────────┤
│   6101 │   6101 │
└────────┴────────┘



con.sql("SELECT COUNT(*) AS n_rows, COUNT(DISTINCT hostname) AS n_keys FROM dim_host_full").show()

┌────────┬────────┐
│ n_rows │ n_keys │
│ int64  │ int64  │
├────────┼────────┤
│   4550 │   4550 │
└────────┴────────┘



# B) gold_by_host
con.execute("DROP VIEW IF EXISTS gold_by_host")
con.execute('''
            CREATE VIEW gold_by_host AS 
            SELECT
            f.pl_name, 
            f.hostname,
            f.pl_rade,
            h.ra
            FROM fact_planet f
            JOIN dim_host_full h
                ON f.hostname = h.hostname
''')
con.sql("SELECT * FROM gold_by_host LIMIT 10").show()

┌───────────────────────────┬─────────────────────────┬───────────┬─────────────┐
│          pl_name          │        hostname         │  pl_rade  │     ra      │
│          varchar          │         varchar         │  double   │   double    │
├───────────────────────────┼─────────────────────────┼───────────┼─────────────┤
│ 18 Del b                  │ 18 Del                  │      12.5 │ 314.6078375 │
│ 2MASS J19383260+4603591 b │ 2MASS J19383260+4603591 │      13.4 │ 294.6359173 │
│ BD-10 3166 b              │ BD-10 3166              │      14.1 │ 164.6191243 │
│ Barnard c                 │ Barnard's star          │     0.743 │ 269.4486144 │
│ CoRoT-22 b                │ CoRoT-22                │      4.88 │ 280.6671392 │
│ CoRoT-27 b                │ CoRoT-27                │    11.287 │ 278.4958319 │
│ CoRoT-7 c                 │ CoRoT-7                 │      2.83 │ 100.9561682 │
│ CoRoT-9 b                 │ CoRoT-9                 │ 11.948794 │ 280.7866461 │
│ DMPP-1 e                  │ DMPP-1                  │      1.86 │  86.7761233 │
│ EPIC 206032309 b          │ EPIC 206032309          │      1.01 │ 341.2404563 │
├───────────────────────────┴─────────────────────────┴───────────┴─────────────┤
│ 10 rows                                                             4 columns │
└───────────────────────────────────────────────────────────────────────────────┘