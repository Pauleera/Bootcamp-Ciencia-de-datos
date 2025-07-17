import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, median_absolute_error, r2_score

df = pd.read_csv('../data/forest_growth_data.csv')
print("Primeras filas dataset")
print(df.head(5))

X = df[['tree_age']] 
y = df['tree_height']
model = LinearRegression()

model.fit(X, y)

print("Resumen del Modelo")
print(f"Intercepto (b0): {model.intercept_:.3f}")
print(f"Pendiente (b1): {model.coef_[0]:.3f} ")

# Interpretación 
print(f"Interpretación por cada año adional de edad, la altura promedio del arbol aumenta {model.coef_[0]:.2f} metros")
y_pred = model.predict(X)
plt.plot(X,y_pred)
plt.title(" Regresion lineal Simple")
plt.xlabel("Edad del arbol (años)")
plt.ylabel("Altura del arbol (m)")

plt.legend()
plt.grid(True)
plt.show()

mse = mean_squared_error(y, y_pred)
mae = median_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(" Evaluacion del modelo ")
print(f"Error  cuadratioco: {mse}")
print(f"Error absoluto medio {mae}")
print(f"coeficiente de determinacion: {r2}")