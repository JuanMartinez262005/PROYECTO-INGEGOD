granuralidad: Definir que es cada fila "si una fila es un planeta entonces dos filas iguales son dos planetas iguales"

JOIN: un JOIN correxto es many to one y son hipotesis de como se relacionan las tablas, si no la esta embarrando entonces el conteo de filas no debe crecer.

Tipos de Tablas: 
1) FACT TABLE: registra hechos, con granularidad definida y estricta, se usa para base de calculos y agregaciones; es el centro del modelo, contiene metricas y referencias a otras tablas. Estas se relacionan con otras tablas como las DIM.
2) DIM TABLE: Brinda contexto a los datos, Descripciones no necesariamente tiene granularidad definida y depende del contexto. Estas se relacionan solo como consulta

CTE: tabla temporal lógica o minitabla que sirve dentro del mismo query para organizar mejor el SQL

Window function: Calcula algo sobre un grupo de filas, agreagando un calculo adicional y no colapsando la tabla como GROUP BY
