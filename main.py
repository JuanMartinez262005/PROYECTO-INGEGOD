import sys, platform, hashlib
from pathlib import Path
import duckdb
import os

os.chdir(".")

PROJECT_ROOT = Path(".").resolve()

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR  = DATA_DIR / "raw"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
DOCS_DIR = PROJECT_ROOT / "docs"

for d in [RAW_DIR, SILVER_DIR, GOLD_DIR, ARTIFACTS_DIR, DOCS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

DB_PATH = DATA_DIR / "exoplanets.duckdb"
con = duckdb.connect(str(DB_PATH))

EXPECTED = "pscomppars.csv"
raw_csv = RAW_DIR / EXPECTED

# Si no está con el nombre esperado, buscamos candidatos (para no bloquear la clase)
if not raw_csv.exists():
    candidates = list(RAW_DIR.glob("pscomppars*.csv")) + list(RAW_DIR.glob("*.csv"))
    candidates = [c for c in candidates if c.is_file()]
    if candidates:
        raw_csv = sorted(candidates)[0]
        print(f"No encontré {EXPECTED}. Encontré y usaré: {raw_csv.name}")
        print("   Recomendación: renombra a pscomppars.csv para estandarizar el curso.")
    else:
        print("pailas")
        raw_csv = None

path = str(raw_csv).replace("\\", "/").replace("'", "''")  # Windows-safe

con.execute(f"""
CREATE OR REPLACE VIEW raw_ps AS
SELECT * FROM read_csv_auto('{path}')
""")

print("planetas con orbitas esfericas:",
    con.execute("""
        SELECT COUNT(pl_orbeccen) 
        FROM raw_ps 
        WHERE pl_orbeccen = 0
    """).fetchall()
)