import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('datos_trafico.csv')
print(df.head())

#3. Crear un gráfico de líneas para visualizar el tráfico diario (2 puntos):
plt.figure(figsize=(8, 6)) # ajuste de tamaño de la figura 
plt.plot(df['Día'] , df['Vehículos'])
plt.xlabel("Día")
plt.ylabel("Cantidad de Vehículos")
plt.title('Vehiculos por día')
plt.show()

#4. Crear un histograma para analizar la distribución de velocidades
plt.figure(figsize=(8, 6))
plt.hist(df['Velocidad_Promedio'], bins = 8)
plt.xlabel('Velocidades Promedio', fontsize=12)
plt.ylabel('Frecuencias', fontsize=12)
plt.title('Histograma de Velocidad promedio de los vehiculos')
plt.show()

# 5. Crear un gráfico de dispersión para analizar la relación entre vehículos y accidentes 
plt.figure(figsize=(8, 6))

plt.scatter(df['Vehículos'], df['Accidentes'],
            color='pink',       # Color de los puntos
            alpha=0.7,          # Transparencia de los puntos (0 = transparente, 1 = opaco)
            s=100,              # Tamaño de los puntos
            edgecolors='black', # Color del borde de los puntos
            linewidths=0.8)     # Ancho del borde de los puntos

plt.title('Relación entre Vehículos y Accidentes', fontsize=16)
plt.xlabel('Vehículos', fontsize=12)
plt.ylabel('Accidentess', fontsize=12)


#Guardar el gráfico de dispersión en un archivo PNG (1 punto)
plt.savefig('grafico_accidentes.png')

plt.show()