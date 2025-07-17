import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

size =100

print("Creación de datos simulados de Minutos de deporte en la semana y edad de muerte")
df = pd.DataFrame({
    'mts_dep_semana': np.random.randint(1, 300, size=size),
    'edad_muerte': np.random.randint(60, 120, size=size)
})

print(df.head(5))

# 2. Tabla de contigencia 
#Crear una tabla de contingencia con datos categóricos (ejemplo: grupo de edad y tipo dedieta).

df_2 = pd.DataFrame({
    'Genero': ['Masculino', 'Femenino','Femenino','Masculino'],
    'Tipo_dieta': ['Carnivora', 'Vegana','Carnivora','Vegetariana']
})

print("\n Tabla de contigencia: ")
tabla_contigencia = pd.crosstab(df_2['Genero'], df_2['Tipo_dieta'])
print(tabla_contigencia)

#3. Scatterplot 
print("\n 3. Gráfico de dispersion: Scatterplot")

plt.figure(figsize=(8,5))
plt.scatter(df['mts_dep_semana'], df['edad_muerte'])
plt.xlabel("Minutos de entrenamiento semanal")
plt.ylabel("Edad de defunsión")
plt.title('Relación entre minutos de deporte a la semana y Edad de muerte')
plt.show()

#4. Calculo del coeficiente de correlacon de Pearson
#Calcular el coeficiente de correlación de Pearson e interpretar su resultado.
print("\n 4. coeficiente de correlación de Pearson")

coef, p_value = stats.pearsonr(df['mts_dep_semana'], df['edad_muerte'])
print(f"El coeficience de correlacion de Pearson: {coef:.2}")
print(f"P-value: {p_value:.4}")

print(f"Considerando que el valor r es {coef:.2} se interpreta que tiene una correlación despreciable, casi nula, además tiene un p value mayor a 0.05, por lo que no podemos afirmar que la correlación sea estafísticamente significativa. Esto puede causarse por que los datos utilizados fueron generados de forma aleatoria.")

#5.  Reflexión sobre Correlación vs. Causalidad (2 puntos)
#Explicar con ejemplos si la correlación encontrada implica causalidad o no.

print("Una correlación indica que dos variables se mueven juntas (ej., más helado, más ahogamientos), pero no significa causalidad. A menudo, una tercera variable (como el calor) causa ambos fenómenos. \
      Para establecer causalidad, se necesita evidencia adicional que demuestre que una variable directamente provoca la otra, como en experimentos controlados (ej., fumar causa cáncer).")