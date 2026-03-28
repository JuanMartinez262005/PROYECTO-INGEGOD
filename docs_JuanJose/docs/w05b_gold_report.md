# Reporte de Resultados: Capa Gold (Exoplanetas)

Este reporte presenta los hallazgos principales derivados de las vistas de nivel "Gold", las cuales han sido procesadas tras aplicar reglas de limpieza (Silver) y un modelo relacional de estrella (Fact/Dim).

---

## 1. Análisis por Método de Descubrimiento (`gold_by_discoverymethod`)

Este output agrupa la población de planetas según la técnica utilizada para su hallazgo.

### Top 10 Métodos
| Método | N° Planetas | Radio Promedio (R_Earth) | Masa Promedio (M_Earth) |
| :--- | :--- | :--- | :--- |
| **Transit** | 4500 | 4.36 | 123.46 |
| **Radial Velocity** | 1166 | 9.75 | 1035.40 |
| **Microlensing** | 266 | 9.85 | 797.69 |
| **Imaging** | 87 | 13.43 | 4485.17 |
| ... | ... | ... | ... |

**Interpretación Científica:**
El método de **Tránsito** es el más predominante con diferencia (4,500 detecciones), lo cual refleja el éxito de misiones espaciales dedicadas como Kepler y TESS. Se observa que métodos como **Imaging** tienden a encontrar planetas mucho más masivos y grandes (promedio de 13.43 Radios Terrestres), ya que es más fácil fotografiar gigantes gaseosos alejados de su estrella.

---

## 2. Análisis por Estrella Anfitriona (`gold_by_host`)

Este output identifica los sistemas estelares con mayor cantidad de planetas confirmados y sus características físicas.

### Top 10 Sistemas Multi-planetarios
| Estrella (Host) | N° Planetas | Radio Promedio (R_Earth) | Masa Promedio (M_Earth) |
| :--- | :--- | :--- | :--- |
| **KOI-351** | 8 | 3.90 | 31.14 |
| **TRAPPIST-1** | 7 | 0.97 | 0.92 |
| **Kepler-20** | 6 | 2.29 | 9.38 |
| **HD 110067** | 6 | 2.43 | 6.30 |
| ... | ... | ... | ... |

**Interpretación Científica:**
El sistema **KOI-351** destaca como el más poblado en nuestro dataset. Sin embargo, el sistema **TRAPPIST-1** es de especial interés científico: sus 7 planetas tienen un radio y masa promedio muy cercanos a 1.0 (similares a la Tierra), lo que lo convierte en el laboratorio ideal para estudiar la habitabilidad en planetas rocosos.

---

## Conclusión del Pipeline
Los datos han sido exportados exitosamente a la carpeta `artifacts/` en formato CSV para su consumo en herramientas de visualización externa.