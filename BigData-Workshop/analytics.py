import sqlite3
import pandas as pd

DB_PATH = "BigData-Workshop/ventas.db"

# Conexión a SQLite
conn = sqlite3.connect(DB_PATH)

# a) Total de ventas por categoría
q1 = """
SELECT categoria, ROUND(SUM(total), 2) AS total_ventas
FROM ventas
GROUP BY categoria
ORDER BY total_ventas DESC;
"""
df1 = pd.read_sql_query(q1, conn)
print("\n[a] Total por categoría:\n", df1)

# b) Top 5 productos más vendidos (por unidades)
q2 = """
SELECT producto, SUM(cantidad) AS unidades_vendidas
FROM ventas
GROUP BY producto
ORDER BY unidades_vendidas DESC
LIMIT 5;
"""
df2 = pd.read_sql_query(q2, conn)
print("\n[b] Top 5 productos por unidades:\n", df2)

q3 = """
SELECT strftime('%Y-%m', fecha) AS mes, ROUND(SUM(total), 2) AS facturacion
FROM ventas
GROUP BY mes
ORDER BY facturacion DESC
LIMIT 1;
"""
df3 = pd.read_sql_query(q3, conn)
print("\n[c] Mes con mayor facturación:\n", df3)

conn.close()

df1.to_csv("BigData-Workshop/out_total_por_categoria.csv", index=False)
df2.to_csv("BigData-Workshop/out_top5_productos.csv", index=False)
df3.to_csv("BigData-Workshop/out_mes_top_facturacion.csv", index=False)

print("\n Consultas ejecutadas y exportadas a CSV en BigData-Workshop/")
