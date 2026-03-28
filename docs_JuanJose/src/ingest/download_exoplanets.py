from __future__ import annotations

import argparse
from pathlib import Path
import requests

from src.utils.paths import raw_dir

TAP_SYNC = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"

# Columnas seleccionadas de la tabla pscomppars (NASA Exoplanet Archive)
DEFAULT_COLUMNS = [

    # -------------------------
    # Identificación
    # -------------------------
    "pl_name",          # Nombre del planeta
    "hostname",         # Nombre de la estrella anfitriona
    "discoverymethod",  # Método de descubrimiento (Transit, RV, Imaging, etc.)
    "disc_year",        # Año de descubrimiento

    # -------------------------
    # Propiedades del sistema
    # -------------------------
    "sy_snum",          # Número de estrellas en el sistema
    "sy_pnum",          # Número de planetas en el sistema
    "sy_dist",          # Distancia al sistema (parsecs)

    # -------------------------
    # Posición celeste
    # -------------------------
    "ra",               # Ascensión recta (Right Ascension) [grados]
    "dec",              # Declinación [grados]

    # -------------------------
    # Parámetros orbitales
    # -------------------------
    "pl_orbper",        # Periodo orbital [días]
    "pl_orbeccen",      # Excentricidad orbital (0 = circular)

    # -------------------------
    # Propiedades físicas del planeta
    # -------------------------
    "pl_rade",          # Radio del planeta [radios terrestres]
    "pl_bmasse",        # Masa del planeta [masas terrestres]
    "pl_dens",          # Densidad del planeta [g/cm³]
    "pl_eqt",           # Temperatura de equilibrio [K]
    "pl_insol",         # Flujo de insolación recibido [relativo a la Tierra]

    # -------------------------
    # Propiedades de la estrella
    # -------------------------
    "st_teff",          # Temperatura efectiva estelar [K]
    "st_rad",           # Radio estelar [radios solares]
    "st_mass"           # Masa estelar [masas solares]
]


def build_query(columns: list[str], limit: int | None) -> str:
    cols = ", ".join(columns)
    if limit is not None and limit > 0:
        return f"select top {int(limit)} {cols} from pscomppars order by pl_name"
    return f"select {cols} from pscomppars"


def download(fmt: str, out_path: Path, columns: list[str], limit: int | None):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    params = {"query": build_query(columns, limit), "format": fmt}
    r = requests.get(TAP_SYNC, params=params, timeout=180)
    r.raise_for_status()
    out_path.write_bytes(r.content)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--format", choices=["csv", "json"], default="csv")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--full", action="store_true",
                    help="Descarga *todas* las columnas (tabla ancha).")
    args = ap.parse_args()

    columns = ["*"] if args.full else DEFAULT_COLUMNS
    out = raw_dir() / f"pscomppars.{args.format}"
    download(args.format, out, columns, args.limit)
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
