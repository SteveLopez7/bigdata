# 📄 BigData-Workshop -- Taller evaluativo 1

## 🎯 Objetivo

Desarrollar un flujo básico de **procesamiento de datos** con Python
simulando un escenario **Big Data** a pequeña escala.\
Se implementa un proceso **ETL** (Extract, Transform, Load) para cargar
datos masivos desde un CSV hacia SQLite, realizar consultas analíticas y
visualizar resultados.

------------------------------------------------------------------------

## 🛠️ Requisitos

-   Python 3.x\

-   Librerías necesarias:

    ``` bash
    pip install pandas matplotlib
    ```

-   SQLite3 (incluido en Python estándar)

------------------------------------------------------------------------

## 📂 Estructura del proyecto

    BIG-DATA/
    └── BigData-Workshop/
        ├── README.md                      # Explicación de este taller
        ├── generate_data.py               # Paso 1: Generación de dataset (100k registros)
        ├── sales.csv                      # Archivo CSV generado
        ├── etl.py                         # Paso 2: Proceso ETL → SQLite
        ├── ventas.db                      # Base de datos SQLite resultante
        ├── analytics.py                   # Paso 3: Consultas analíticas en SQLite
        ├── plots.py                       # Paso 4: Visualización de resultados
        ├── out_total_por_categoria.csv    # Resultados de consultas (para evidencias)
        ├── out_top5_productos.csv
        ├── out_mes_top_facturacion.csv
        ├── grafico_total_por_categoria.png
        ├── grafico_top5_productos.png
        └── grafico_facturacion_mensual.png

------------------------------------------------------------------------

## 🚀 Pasos para ejecutar

### 1. Generar el dataset

``` bash
python BigData-Workshop/generate_data.py
```

🔹 Se crea `sales.csv` con **100,000 registros simulados**.

------------------------------------------------------------------------

### 2. Cargar datos en SQLite (ETL)

``` bash
python BigData-Workshop/etl.py
```

🔹 Se crea `ventas.db` y se insertan los datos en la tabla `ventas`
usando chunks de 10.000 filas.

------------------------------------------------------------------------

### 3. Ejecutar consultas analíticas

``` bash
python BigData-Workshop/analytics.py
```

Se obtienen: - Total de ventas por categoría\
- Top 5 productos más vendidos\
- Mes con mayor facturación

Los resultados también se guardan en CSV para evidencias.

------------------------------------------------------------------------

### 4. Visualización de datos

``` bash
python BigData-Workshop/plots.py
```

Se generan gráficos en formato `.png`: -
`grafico_total_por_categoria.png`\
- `grafico_top5_productos.png`\
- `grafico_facturacion_mensual.png`

------------------------------------------------------------------------

## 📊 Resultados esperados

-   **Consultas SQL** impresas en consola y exportadas en CSV\
-   **Gráficos** en formato PNG para adjuntar como evidencia\
-   Flujo ETL completo y reproducible en cualquier máquina con Python
    3.x

------------------------------------------------------------------------

## 👨‍💻 Autor

Taller evaluativo desarrollado para la asignatura **Big Data 2 --
CEIE**\
Profesor: Joan
