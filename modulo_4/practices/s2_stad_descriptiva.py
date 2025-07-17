import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
#from matplotlib.backends.backend_pdf import PdfPages

#nombre_pdf = 'estadistica_descriptiva.pdf'

df = pd.read_csv('s2.csv')
print(df.head)

#1. Tipos de variable 

#Id: categórica
#Nombre: Categórica
#Ciudad: Categórica
#Edad: Cuantitativa discreta
#Ingresos: Cuantitativa discreta
# Género: Categórica


# 2. TABLAS DE FRECUENCIA 
print(" 2. Tablas de frecuancia")
# Una tabla de frecuencia herramienta estadística

print(" Tabla de frecuencia de Ciudad")
tabla_freq_cat_ciudad = df['Ciudad'].value_counts().sort_index().to_frame("Freq. Absoluta")
tabla_freq_cat_ciudad["Freq. Relativa"] = tabla_freq_cat_ciudad["Freq. Absoluta"] / tabla_freq_cat_ciudad["Freq. Absoluta"].sum()
tabla_freq_cat_ciudad["Freq. Acumulada"] = tabla_freq_cat_ciudad["Freq. Absoluta"].cumsum()
tabla_freq_cat_ciudad["Freq. Relativa Acum."] = tabla_freq_cat_ciudad["Freq. Relativa"].cumsum()
print(tabla_freq_cat_ciudad)
#tabla_freq_disc_

print("\n Tabla de frecuencia de Edad")
tabla_freq_cuan_edad = df['Edad'].value_counts().sort_index().to_frame("Freq. Absoluta")
tabla_freq_cuan_edad["Freq. Relativa"] = tabla_freq_cuan_edad["Freq. Absoluta"] / tabla_freq_cat_ciudad["Freq. Absoluta"].sum()
tabla_freq_cuan_edad["Freq. Acumulada"] = tabla_freq_cuan_edad["Freq. Absoluta"].cumsum()
tabla_freq_cuan_edad["Freq. Relativa Acum."] = tabla_freq_cuan_edad["Freq. Relativa"].cumsum()
print(tabla_freq_cuan_edad)
#tabla_freq_disc_

#3. Cálculo de medidas de tendencia Centrall 
#Calcular media, mediana y moda de una variable cuantitativa

print("\n 3. Medidas de tendencia central de Ingresos")
media = np.mean(df['Ingresos'])
print(f"La media de Ingresos del conjunto de datos es: {media}")

mediana = np.median(df['Ingresos'])
print(f"La mediana de Ingresos del conjunto de datos es: {mediana}")

moda = stats.mode(df['Ingresos'])
print(f"La moda del Ingresos del conjunto de datos es: {moda[0]}")

#4. Cálculo de Medidas de Dispersion 
#Calcular el rango, varianza y desviación estándar de ingresos
print("\n 4.  Medidas de Dispersión de Ingresos")
rango = max(df['Ingresos']) - max(df['Ingresos'])
print(f"El rango de variación de los Ingresos es: {rango}")

#np.var(datos) Para población
varianza_muestral_bessel = np.var(df['Ingresos'], ddof=1)
print(f"La varianza muestral de los Ingresos es: {varianza_muestral_bessel}")

#desviación estándar
desviacion_muestral = np.std(df['Ingresos'] , ddof=1)
print(f"La desviación muestral de los Ingresos es: {desviacion_muestral}")

#5. Visualización de Datos
print("\n 5. Histograma para Ingresos y boxplot para Edad")
plt.hist(df['Ingresos'], bins = 5, edgecolor = "pink")
plt.xlabel("Ingresos")
plt.ylabel("Frecuencia")
plt.title("Histograma de los Ingresos")
plt.show()

sns.boxplot(x = df["Edad"])
plt.title("Boxplot de Edad")
plt.show()