#Reto 1 Encuesta de Salud Pública por Regiones
import pandas as pd

df = pd.read_csv("../data/inputs/encuesta_salud.csv")
df_regiones = pd.read_csv("../data/inputs/region_referencia.csv")

#2.
print("\n Inspección del dataframe")
print(df.head())
print(df.info())

#3.
print("\n Convertir a datos a variables númericas")
df["Peso"] = pd.to_numeric(df["Peso"], errors = "coerce")
df["Presion_Arterial"] = pd.to_numeric(df["Presion_Arterial"], errors = "coerce")
print(df.info())

#4. 
print("\n Eliminando duplicados..")
print(df.shape)
df = df.drop_duplicates()
print(df.shape)

#5. 
print("\n Calculando el IMC y su categoria..")
df["IMC"] = df["Peso"] / df["Altura"].pow(2)


df["Categoria_IMC"] = pd.qcut(df["IMC"],4, labels = ["Bajo","Normal","Sobrepeso","Obesidad"] )
print(df)

#6. 
print("\n Rellenando los valores nulos de ingresos con la media")
df["Ingresos"] = df["Ingresos"].fillna(df["Ingresos"].mean())
print(df)

#7. 
print("Unir archivo de regiones")
df_merged = pd.merge(df, df_regiones, on='Region', how='left')
print(df_merged)

#8. 