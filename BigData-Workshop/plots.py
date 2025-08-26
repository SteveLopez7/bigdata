import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "BigData-Workshop/ventas.db"
conn = sqlite3.connect(DB_PATH)

# a) Total de ventas por categoría

df_cat = pd.read_sql_query("""
SELECT categoria, SUM(total) AS total_ventas
FROM ventas
GROUP BY categoria
ORDER BY total_ventas DESC;
""", conn)

plt.figure()
plt.bar(df_cat["categoria"], df_cat["total_ventas"], color=["skyblue","salmon","lightgreen"])
plt.title("Total de ventas por categoría")
plt.xlabel("Categoría")
plt.ylabel("Ventas")
plt.tight_layout()
plt.savefig("BigData-Workshop/grafico_total_por_categoria.png", dpi=120)

# b) Top 5 productos más vendidos

df_top = pd.read_sql_query("""
SELECT producto, SUM(cantidad) AS unidades
FROM ventas
GROUP BY producto
ORDER BY unidades DESC
LIMIT 5;
""", conn)

plt.figure()
plt.bar(df_top["producto"], df_top["unidades"], color="orange")
plt.title("Top 5 productos por unidades vendidas")
plt.xlabel("Producto")
plt.ylabel("Unidades")
plt.tight_layout()
plt.savefig("BigData-Workshop/grafico_top5_productos.png", dpi=120)

# c) Facturación por mes

df_mes = pd.read_sql_query("""
SELECT strftime('%Y-%m', fecha) AS mes, SUM(total) AS facturacion
FROM ventas
GROUP BY mes
ORDER BY mes ASC;
""", conn)

plt.figure()
plt.plot(df_mes["mes"], df_mes["facturacion"], marker="o", linestyle="-", color="purple")
plt.title("Facturación mensual")
plt.xlabel("Mes (YYYY-MM)")
plt.ylabel("Facturación")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("BigData-Workshop/grafico_facturacion_mensual.png", dpi=120)

conn.close()
print("Gráficos generados y guardados en la carpeta BigData-Workshop/")
