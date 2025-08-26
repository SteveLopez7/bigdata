
import csv
import datetime as dt
import random
import os

CURRENT_YEAR = 2025  
CATEGORIAS = ["Electrónica", "Ropa", "Hogar"]
PRODUCTOS = [
    "Televisor", "Celular", "Laptop",
    "Camisa", "Pantalon", "Zapatos",
    "Sofa", "Mesa", "Silla"
]

os.makedirs("BigData-Workshop", exist_ok=True)
ruta_csv = "BigData-Workshop/sales.csv"  

random.seed(42) 
with open(ruta_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    
    writer.writerow(["id", "fecha", "producto", "categoria", "precio", "cantidad", "total"])

    for i in range(1, 100_001):
        fecha = dt.date(CURRENT_YEAR, random.randint(1, 12), random.randint(1, 28))
        producto = random.choice(PRODUCTOS)
        if producto in ["Televisor", "Celular", "Laptop"]:
            categoria = "Electrónica"
        elif producto in ["Camisa", "Pantalon", "Zapatos"]:
            categoria = "Ropa"
        else:
            categoria = "Hogar"
        precio = round(random.uniform(10, 2000), 2)
        cantidad = random.randint(1, 10)
        total = round(precio * cantidad, 2)
        writer.writerow([i, fecha.isoformat(), producto, categoria, precio, cantidad, total])

print(f"CSV generado en: {ruta_csv}")
