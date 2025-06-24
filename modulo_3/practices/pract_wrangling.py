import pandas as pd 
import numpy as np 

df = pd.read_csv("../data/inputs/ejemplo_datos_outliers.csv")

print(df.head(10))
print(df.info())

df["Edad"] = pd.to_numeric(df["Edad"], errors="coerce")
df["Salario"] = pd.to_numeric(df["Salario"], errors="coerce")
df["Horas_Trabajo_Semanal"] = pd.to_numeric(df["Horas_Trabajo_Semanal"], errors="coerce")


print(df.head(10))

# Eliminar duplicados 
df = df.drop_duplicates() 
print("Datos después de duplicados:")
print(df.info())

df["Edad"].fillna(df["Edad"].mean(), inplace=True)
df["Salario"].fillna(df["Salario"].mean(), inplace=True)
df["Horas_Trabajo_Semanal"].fillna(df["Horas_Trabajo_Semanal"].mean(), inplace=True)
print(df.info())
df.to_csv("../data/outputs/salida_datos_rellenados.csv", index=False)

print("Discretización de las Horas de Trabajo Semanales:")
df["Horas_Categoricas"] = pd.cut(df["Horas_Trabajo_Semanal"], bins = [0,30,40,50,np.inf] , labels = ["Bajo", "Normal", "Alto", "Extremo"])

print(df.head(10))

niveles = pd.read_csv("../data/inputs/nivel_educativo_referencia.csv")
df = df.merge(niveles, left_on="Nivel_Educativo",  right_on="Codigo", how="left")
print("Merge con Nivel educativo: ")
print(df)

agrupado = df.groupby(["Departamento","Horas_Categoricas"])["Salario"].mean().reset_index()
print("Resumen")
print(agrupado)
