import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#2.
size = 100
df = pd.DataFrame({
    'Edad': np.random.randint(0, 70, size=size),
    'Ingresos': np.random.randint(260, 5000, size=size),
    'Años de Educ.': np.random.randint(0, 20, size=size),
    'Hijos.': np.random.randint(0, 7, size=size)
})

#3. Calcular la matriz de correlación 
matriz_correlacion = df.corr()

print("\nMatriz de Correlación:")
print(matriz_correlacion)
# 4. Visualizar la Matriz de Correlación (Mapa de Calor)
plt.figure(figsize=(8, 6)) # ajuste de tamaño de la figura 
sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, linecolor='black')
plt.title('Matriz de Correlación')
plt.show()

#5. Interpretación y Personalización del gráfico (1 punto

print("Del grafico de calor se puede interpretar que no existen corelaciones significativas para ninguna variable.")