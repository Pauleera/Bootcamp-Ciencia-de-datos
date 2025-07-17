import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('olimpicos.csv')
print(df.head())


print("\n    .INFO()")
print(df.info())


print("\n    .DESCRIBE()")
print(df.describe())

plt.figure(figsize=(8, 6))
plt.hist(df['Entrenamientos_Semanales'])
plt.xlabel('Número de entrenamiento semanales', fontsize=12)
plt.title('Histograma del número de entrenamiento semanales ')
plt.show()

#2. Estadistica descriptiva 

print("Tipos de datos de cada columna en el DataFrame:")
print(df.dtypes)

print(f"Media de medallas obtenidas, {df['Medallas_Totales'].mean()} ")
print(f"Mediana de medallas obtenidas, {df['Medallas_Totales'].median()} ")
print(f"Moda de medallas obtenidas, {df['Medallas_Totales'].mode()} , No existe una moda")

print("Desviación estándar de la altura de los atletas:")

std_altura_atletas = df['Altura_cm'].std()
print(f"\nDesviación estándar de Altura en cm: {std_altura_atletas:.2f}")

sns.boxplot(x = df["Peso_kg"])
plt.title("Boxplot del Peso [kg]")
plt.show()
print("No se observan dato atipicos, pero si un bloxplot que se distrubuye a través de un rango considerable de pesos.")

#3. Análisis de correlación
# Calcular la correlación de Pearson entre 'Entrenamientos_Semanales' y 'Medallas_Totales'
correlacion_entrenamiento_medallas = df['Entrenamientos_Semanales'].corr(df['Medallas_Totales'])
print(f"\n Correlación de Pearson entre Entrenamientos Semanales y Medallas Totales: {correlacion_entrenamiento_medallas:.2f}")
correlacion_peso_medallas = df['Peso_kg'].corr(df['Medallas_Totales'])
print(f"\n Correlación de Pearson entre Peso kg y Medallas Totales: {correlacion_peso_medallas:.2f}")
#Crear un gráfico de dispersión (scatterplot) entre Peso_kg y Medallas_Totales


plt.figure(figsize=(10, 6))
sns.scatterplot(x='Peso_kg', y='Medallas_Totales', data=df, hue='Atleta', s=100, alpha=0.8)
plt.title('Relación entre Peso (kg) y Medallas Totales')
plt.xlabel('Peso (kg)')
plt.ylabel('Medallas Totales')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') # Mueve la leyenda fuera del gráfico
plt.tight_layout() # Ajusta el layout para evitar que la leyenda se superponga
plt.show()

print("\n En este pequeño conjunto de datos, la correlación positiva indica que los atletas más pesados en esta muestra tienden a tener más medallas. Sin embargo, es fundamental recordar que correlación no implica causalidad. El peso por sí solo no causa más medallas; más bien, el peso está asociado con ciertos deportes (ej., natación de alta potencia) que podrían dar más oportunidades de medallas que otros.")

#4. Regresión lineal 

#Implementa un modelo de regresión lineal para predecir el número de medallasobtenidas en función del número de entrenamientos semanales
X = df[['Entrenamientos_Semanales']]
y = df['Medallas_Totales']
model = LinearRegression()
model.fit(X, y)
#Obtén los coeficientes de regresión e interpreta el resultado.
coeficiente = model.coef_[0]
intercepto = model.intercept_

print(f"Coeficiente de regresión (Pendiente): {coeficiente:.2f}")
print(f"Intercepto: {intercepto:.2f}")
print(f"El Coeficiente (pendiente) de {coeficiente:.2f} significa que por cada entrenamiento semanal adicional, se predice un aumento de {coeficiente:.2f} medallas totales.")
print(f"El Intercepto de {intercepto:.2f} representa el número de medallas predichas para un atleta con 0 entrenamientos semanales.")


#Calcula el R² para medir el ajuste del modelo.

y_pred = model.predict(X) # Predicciones usando el modelo entrenado
r_squared = r2_score(y, y_pred)

print(f"El valor R² de {r_squared:.2f} indica que aproximadamente el {r_squared*100:.0f}% de la variabilidad en el número de medallas totales puede ser explicada por el número de entrenamientos semanales, según este modelo.")


# Usa Seaborn (regplot) para graficar la regresión lineal.
plt.figure(figsize=(10, 6))
sns.regplot(x='Entrenamientos_Semanales', y='Medallas_Totales', data=df, ci=95, scatter_kws={'s': 100, 'alpha': 0.8}, line_kws={'color': 'red'})
plt.title('Regresión Lineal: Medallas Totales vs. Entrenamientos Semanales')
plt.xlabel('Número de Entrenamientos Semanales')
plt.ylabel('Número Total de Medallas')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

#4. Visualización de Datos con Seaborn y Matplotlib

#Crea un heatmap de correlación entre todas las variables numéricas.

df_numericas = df.select_dtypes(include=[np.number])
plt.figure(figsize=(9, 7))
matriz_correlacion = df_numericas.corr()

sns.heatmap(matriz_correlacion,
            annot=True,        # Mostrar los valores de correlación en las celdas
            cmap='viridis',    # Elegir un mapa de color diferente para variedad
            fmt=".2f",         # Formatear los números a dos decimales
            linewidths=.5,     # Añadir líneas entre las celdas
            linecolor='black') # Color de las líneas
plt.title('Heatmap de Correlación entre Variables Numéricas', fontsize=16)
plt.xticks(rotation=45, ha='right') # Rotar etiquetas del eje X para mejor lectura
plt.yticks(rotation=0)            # Asegurar que las etiquetas del eje Y no estén rotadas
plt.tight_layout() # Ajusta el layout para que todo quepa
plt.show()


#Crea un boxplot de la cantidad de medallas por disciplina deportiva.

plt.figure(figsize=(10, 6))
sns.boxplot(x='Deporte', y='Medallas_Totales', hue = 'Deporte', data=df, palette='Set2', legend= False)
sns.stripplot(x='Deporte', y='Medallas_Totales', data=df, color='black', size=5, jitter=0.2, alpha=0.7) # Añadir los puntos individuales
plt.title('Distribución de Medallas Totales por Disciplina Deportiva', fontsize=16)
plt.xlabel('Disciplina Deportiva', fontsize=12)
plt.ylabel('Medallas Totales', fontsize=12)
plt.xticks(rotation=45, ha='right') # Rotar etiquetas para mejor lectura
plt.grid(axis='y', linestyle='--', alpha=0.7) # Solo grid en el eje Y
plt.tight_layout() # Ajusta el layout para que todo quepa
plt.show()


print("Los gráficos han sido personalizados.")
#Personaliados los gráficos con títulos, etiquetas y colores. 