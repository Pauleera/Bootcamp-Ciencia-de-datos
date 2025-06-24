import pandas as pd
import numpy as np
df = pd.read_csv("../data/inputs/reto5_satisfaccion_ampliado.csv")

print(df.info())
print(df.head(12))

#Verificar si hay valores fuera de rango (0-100)
print(df["Satisfaccion"].describe())

#Rellenar Valores nulos con la moda
df["Satisfaccion"] = df["Satisfaccion"].fillna(df["Satisfaccion"].mode(dropna=False)[0])
print(df.head(12))

print("\n Clasificación de Satifacción: ")
df["Categoria_Satisfaccion"] = pd.cut(df["Satisfaccion"], bins = [0,51,76,101] , labels= ["Insatisfecho", "Neutral", "Satisfecho"], include_lowest=True)
print(df)