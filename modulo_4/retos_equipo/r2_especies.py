#Biología 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_especies = pd.read_csv('../data/especies_principal.csv')
df_habitat = pd.read_csv('../data/habitat_secundario.csv')

print("***** ESPECIES ******")
print(df_especies.head(5))

print(df_especies.info())
print(df_especies.describe())
print(df_especies.isnull().sum())

print("\n***** HABITAT ******")

print(df_habitat.head(5))

print(df_habitat.info())
print(df_habitat.describe())
print(df_habitat.isnull().sum())

print("\n ➡️ Tablas de frecuencias de Especies")
print(df_especies['Especie'].value_counts())

print("\n ➡️ Tablas de frecuencias de coservación")
print(df_especies['Estado_Conservacion'].value_counts())

def fun_estadisticas(data):
    q1 = data.quantile(0.25)
    q2 = data.quantile(0.50)   
    q3 = data.quantile(0.75)

    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    #outliers = df[(df["Salario"] < limite_inferior) | (df["Salario"] > limite_superior)]
    #valores_no_outliers = df[(df["Salario"] >= limite_inferior) & (df["Salario"] <= limite_superior)]

    return [data.mean(), data.median(), data.mode()[0], data.std(ddof=1) , 
            q1 , q2, q3,  limite_inferior, limite_superior]

print("\n 📊 Medidas para Masa Corporal")

estadisticas = fun_estadisticas(df_especies["Masa_Corporal"])
outlier = df_especies[(df_especies["Masa_Corporal"] < estadisticas[7]) | (df_especies["Masa_Corporal"] > estadisticas[8])]

print(f"" \
f"Media: {estadisticas[0]}\n" \
f"Mediana: {estadisticas[1]}\n" \
f"Moda:{estadisticas[2]} \n" \
f"std: {estadisticas[3]}\n " \
f"q1: {estadisticas[4]}\n" \
f"q2: {estadisticas[5]}\n" \
f"q3: {estadisticas[6]}\n" \
f"limite inferior: {estadisticas[7]}\n" \
f"limite superior: {estadisticas[8]}\n" \
f"outliers: {outlier}" )

print("\n 📊 Medidas para Temperatura")

estadisticas = fun_estadisticas(df_especies["Temperatura"])
outlier = df_especies[(df_especies["Temperatura"] < estadisticas[7]) | (df_especies["Temperatura"] > estadisticas[8])]

print(f"" \
f"Media: {estadisticas[0]}\n" \
f"Mediana: {estadisticas[1]}\n" \
f"Moda:{estadisticas[2]} \n" \
f"std: {estadisticas[3]}\n " \
f"q1: {estadisticas[4]}\n" \
f"q2: {estadisticas[5]}\n" \
f"q3: {estadisticas[6]}\n" \
f"limite inferior: {estadisticas[7]}\n" \
f"limite superior: {estadisticas[8]}\n" \
f"outliers: {outlier}" )

