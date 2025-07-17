import pandas as pd
import numpy as np

#1. Limpieza y transformación 

# Cargar el archivo y visualizar info
df = pd.read_csv('migracion.csv')
print("Las primeras 5 filas del DataFrame:")
print(df.info())

#2. Identificar y manaejar valores perdidos 
df = df.dropna()

#3. Detectar y eliminar duplicados 
df = df.drop_duplicates()

#4. Detectar y manejar outlier

df["Cantidad_Migrantes"] = pd.to_numeric(df["Cantidad_Migrantes"], errors="coerce") 
q1 = df["Cantidad_Migrantes"].quantile(0.25)
q2 = df["Cantidad_Migrantes"].quantile(0.50)   
q3 = df["Cantidad_Migrantes"].quantile(0.75)

iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
outliers = df[(df["Cantidad_Migrantes"] < limite_inferior) | (df["Cantidad_Migrantes"] > limite_superior)]
print(f"Outlier detectados: {outliers}")

#Reemplazar los valores de la columna "Razon_migracion"
df['Razon_Migracion'].astype(str, errors='ignore')
df['Razon_Migracion'] = df['Razon_Migracion'].map({'Económica': 'Trabajo', 'Conflicto':'Guerra','Educativa':'Educativa'})
print(df['Razon_Migracion'].unique())

#2. Análisis Exploratorio 

print(df.head(5))
print(df.info())
print(df.describe())
media= df["Cantidad_Migrantes"].mean()
mediana= df["Cantidad_Migrantes"].median()
print(f"Media de cantidad de migrantes: {media} \n")
print(f"Median de cantidad de migrantes: {mediana} \n")

pib_origen = df["PIB_Origen"]
pib_destino = df["PIB_Destino"]
razon_mig = df["Razon_Migracion"]
print(f"PIB promedio de los países de Origen {pib_origen.mean()} \n"
     f"PIB promedio de los países de Destino {pib_destino.mean()} \n "
     f"N° ocurrencias de razones de migración: {razon_mig.value_counts()} \n ")

# 3. Agrupamiento y Sumarización de datos
df_grouped = df.groupby("Razon_Migracion")["Cantidad_Migrantes"].agg(sum)
df_grouped = df.groupby("Razon_Migracion")[["Cantidad_Migrantes","IDH_Origen","IDH_Destino"]].agg([sum, np.mean  ])
#
df_grouped_print = df_grouped[[("Cantidad_Migrantes","sum"), ("IDH_Origen","mean" ) , ("IDH_Destino","mean" ) ] ] 
print(df_grouped_print)
#Ordenar de mayor a menos cantidad de migrantes
sorted_df_grouped_by_mig= df_grouped_print.sort_values(by=('Cantidad_Migrantes','sum') ,  ascending=False)
print(sorted_df_grouped_by_mig)

#4. Filtros y Seleccion de Datos

#Mostrar solo las migraciones por conflicto (Guerra)
df_mig_conflicto = df[df["Razon_Migracion"] == "Guerra"]
print("\n Filas por conflicto (Guerra) ")
print(df_mig_conflicto)

#Selecciona y muestra las filas donde el IDH del país de destino sea mayor a 0.90.
df_idh_superiro = df[df["IDH_Destino"] >= 0.9]
print("\n Filas donde el IDH del país de destino sea mayor a 0.90")
print(df_idh_superiro)

#Crea una nueva columna "Diferencia_IDH" que calcule la diferencia de IDH entre país de
#origen y destino.
df["Diferencia_IDH"] = 0.0
df["Diferencia_IDH"] = df["IDH_Origen"]- df["IDH_Destino"]
print("\n Añadiendo nueva columna Diferencia IDH..")
print(df["Diferencia_IDH"])

df.to_csv("Migracion_Limpio.csv", index=None)