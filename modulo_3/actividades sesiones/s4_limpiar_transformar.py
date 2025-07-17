import pandas as pd

#1. Cargar el archivo y visualizar info
df = pd.read_csv('../data/inputs/ventas.csv')
print("Las primeras 5 filas del DataFrame:")
print(df.head(5))
print(df.info())

#2. Identificar y manaejar valores perdidos 
df = df.dropna()

#3. Detectar y eliminar duplicados 

df = df.drop_duplicates()

#4. Detectar y manejar outlier en la columna "Cantidad"

df["Cantidad"] = pd.to_numeric(df["Cantidad"], errors="coerce") 
q1 = df["Cantidad"].quantile(0.25)
q2 = df["Cantidad"].quantile(0.50)   
q3 = df["Cantidad"].quantile(0.75)

iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
outliers = df[(df["Cantidad"] < limite_inferior) | (df["Cantidad"] > limite_superior)]
print(f"Outlier detectados: {outliers}")

#5. Reemplazar valores incorrectos y modificar la escritura del DataFrama
   # Cambiar tipo de dato
df['Producto'] = df['Producto'].astype(str)
print(df.dtypes)
