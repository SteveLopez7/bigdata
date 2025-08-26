import os
import sqlite3
import pandas as pd

DB_PATH = "BigData-Workshop/ventas.db"
CSV_PATH = "BigData-Workshop/sales.csv"
CHUNK_SIZE = 10_000   

os.makedirs("BigData-Workshop", exist_ok=True)

# conección a SQLite
conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS ventas (
    id INTEGER PRIMARY KEY,
    fecha TEXT,
    producto TEXT,
    categoria TEXT,
    precio REAL,
    cantidad INTEGER,
    total REAL
);
""")
conn.commit()

print("Tabla creada (si no existía)")


reader = pd.read_csv(CSV_PATH, chunksize=CHUNK_SIZE)

total_rows = 0
for i, chunk in enumerate(reader, start=1):
    
    chunk.to_sql("ventas", conn, if_exists="append", index=False)
    total_rows += len(chunk)
    print(f"Chunk {i} cargado con {len(chunk)} filas (acumulado: {total_rows})")

conn.close()
print(f"ETL completado. Se cargaron {total_rows} filas en {DB_PATH}")
