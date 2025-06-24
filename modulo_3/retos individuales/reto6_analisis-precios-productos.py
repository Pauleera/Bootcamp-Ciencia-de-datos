import pandas as pd
import numpy as np
df = pd.read_csv("../data/inputs/reto6_precios_ampliado.csv")

print(df.info())

# 1. Validar que precio no tenga texto y esté dentro de un rango realista 
print("\n Describe de 'Precio': ")
print(df["Precio"].describe())


# 2. Rellenar Valores nulos con la mediana 
df["Precio"] = df["Precio"].fillna(df["Precio"].mean())

print(df.info())

# 3. Aplicar pd.qcut() para categorizar en:
df["Grupo_Precio"] = pd.qcut(df["Precio"] , q = 4, labels=["Económico", "Itermedio Bajo", "Intermedio Alto", "Premium"])

print("\nCategorizando grupos en precio: ")
print(df)