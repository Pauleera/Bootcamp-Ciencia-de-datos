import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

np.random.seed(42)

size = 500

#loc = distribución normal en 150, desviacion estadas de 80
minutos_deporte_semanal = np.random.normal(loc=150, scale=80, size=size)
# Asegurarnos de que los minutos no sean negativos y tengan un techo realista
minutos_deporte_semanal = np.clip(minutos_deporte_semanal, 0, 1000)
minutos_deporte_semanal = np.round(minutos_deporte_semanal) # Redondear a enteros

# 2. Generar edad de muerte con una dependencia lineal aproximada del deporte
# La idea es: edad_muerte = base_edad + (coeficiente * minutos_deporte) + ruido
base_edad = 70 # Edad de muerte base si no se hace mucho deporte
coeficiente_deporte = 0.05 # Cada minuto extra de deporte añade 0.05 años a la vida
ruido = np.random.normal(loc=0, scale=7, size=size) # Variabilidad natural

edad_muerte = base_edad + (coeficiente_deporte * minutos_deporte_semanal) + ruido
# Asegurarnos de que la edad de muerte sea realista (ej. min 50, max 105)
edad_muerte = np.clip(edad_muerte, 50, 105)
edad_muerte = np.round(edad_muerte) # Redondear a enteros

# Crear un DataFrame de Pandas
data = pd.DataFrame({
    'Minutos_Deporte_Semanal': minutos_deporte_semanal,
    'Edad_Muerte': edad_muerte
})

# Mostrar las primeras filas del dataset
print("Primeras 5 filas del dataset:")
print(data.head())

print("\nEstadísticas descriptivas:")
print(data.describe())



# Opcional: Calcular la correlación para verificar
print(f"\nCorrelación entre Minutos_Deporte_Semanal y Edad_Muerte: {data['Minutos_Deporte_Semanal'].corr(data['Edad_Muerte']):.2f}")

X = data[['Minutos_Deporte_Semanal']]
Y = data['Edad_Muerte']


modelo = LinearRegression()
modelo.fit(X,Y)

beta_0 = modelo.intercept_ # Reprecenta el intercto (Y cuando X = 0)
beta_1 = modelo.coef_[0] #Pendiente, cuánto cambia Y por cada unidad de X

print(f"coef intercero: {beta_0}")
print(f"coef pendiente: {beta_1}")

#Predicción

y_pred = modelo.predict(X)
print(f"\n Los primeros 5 valores predichos son: {y_pred[:5]} para {X[:5]}")

print("\n Métricas de error")
MSE  = mean_squared_error(Y , y_pred)
MAE = mean_absolute_error(Y , y_pred)
print(f"Error cuadrado medio: {MSE}")
print(f"Error absoluto medio: {MAE}")
print(" Un MAE de 5.4 signfica que en promedio, las predicciones del modelo se desvian 5.4 años a la edad de muerte real. El MSE de 46 que se traduce a un RMSE de 6.78 indica un error promedio mayor, penalizado por las grandes desviaciones.  ")


#Gráfico

plt.figure(figsize=(10, 6))
plt.scatter(X, Y, alpha=0.6)
plt.plot(X,y_pred, color = "red", label = "Regresión Lineal")
plt.title('Minutos de Deporte Semanal vs. Edad de Muerte')
plt.xlabel('Minutos de Deporte Semanal')
plt.ylabel('Edad de Muerte')
plt.grid(True, linestyle='--', alpha=0.0)
plt.tight_layout()
plt.show()

