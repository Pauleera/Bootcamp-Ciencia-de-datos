#Ejercicios Integradores sobre Análisis de Correlación y Regresión con Pandas y Scikitlearn
#by: Isa
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_log_error, mean_absolute_error,r2_score

class eda:
    def __init__(self,df,columnas):
        self.df = df
        self.columnas = columnas

    def info_general(self):
        print("----- Estructura del dataframe -----")
        print(self.df.head())
        print("----- Información general -----")
        print(self.df.info())
        print("\n----- Análisis descriptivo -----")
        print(self.df.describe())
        print("----- Valores nulos -----")
        print(self.df.isnull().sum())
    
    def _calcular_limites_iqr(self, col): #privado, uso interno
        q1 = self.df[col].quantile(0.25)
        q3 = self.df[col].quantile(0.75)
        iqr = q3 - q1
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
        return q1, q3, limite_inferior, limite_superior

    def frecuencia(self):
        print("\n----- FRECUENCIA -----")
        for col in self.columnas:
            print(f"\n--- {col} ---")
            print(f"Frecuencia {col}: {self.df[col].value_counts()}")

    def estadisticas(self):
        print("\n----- ESTADÍSTICAS -----")
        for col in self.columnas:
            print(f"\n--- {col} ---")
            print(f"Media: {self.df[col].mean():.2f}")
            print(f"Mediana: {self.df[col].median():.2f}")
            print(f"Moda: {self.df[col].mode().iloc[0]:.2f}")
            print(f"STD: {self.df[col].std(ddof=1):.2f}")
            print(f"Varianza: {df[col].var(ddof=1):.2f}")
            print(f"P25 (Q1): {df[col].quantile(0.25):.2f}")
            print(f"P50 (Q2): {df[col].quantile(0.50):.2f}")
            print(f"P75 (Q3): {df[col].quantile(0.75):.2f}")

    def analizar_outliers(self):
        print("\n----- OUTLIERS -----")
        for col in self.columnas:
            q1, q3, lim_inf, lim_sup = self._calcular_limites_iqr(col)
            outliers = self.df[(self.df[col] < lim_inf) | (self.df[col] > lim_sup)]
            print(f"\n--- {col} ---")
            print(f"Q1: {q1:.2f} | Q3: {q3:.2f}")
            print(f"Límite inferior: {lim_inf:.2f} | superior: {lim_sup:.2f}")
            print(f"Número de outliers: {outliers.shape[0]}")
    
    def limpieza_datos(self, columna=None):
        print("\n----- DATAFRAME LIMPIO -----")
        df_limpio = self.df.copy()
        if columna:
            columnas_a_limpiar = [columna] 
        else:
            columnas_a_limpiar = self.columnas
        for col in columnas_a_limpiar:
            q1, q3, lim_inf, lim_sup = self._calcular_limites_iqr(col)
            df_limpio = df_limpio[(df_limpio[col] >= lim_inf) & (df_limpio[col] <= lim_sup)]
            print(f"Columna: {col}")
            print(f"   Limite inferior: {lim_inf:.2f}, superior: {lim_sup:.2f}")
            print(f"   Filas restantes: {df_limpio.shape[0]}")
        print(f"\nDatos originales: {len(self.df)} | Datos después de limpieza: {len(df_limpio)}")
        return df_limpio

#Cargando datos y aplicando EDA
df = pd.read_csv('../data/science_data.csv')
columnas_a_analizar = ['temperatura','crecimiento_planta']
explorador = eda(df, columnas_a_analizar)
explorador.info_general()
explorador.frecuencia()
explorador.estadisticas()
explorador.analizar_outliers()
explorador.limpieza_datos()

#Visualizar gráficos
#Boxplot Temperatura
fig, axs = plt.subplots(figsize=(11,6))
axs.boxplot(df['temperatura'])
axs.set_title('Temperatura')
axs.set_xlabel('Temperatura')
axs.set_ylabel('Frecuencia')
plt.show()
"""Validación: sin outliers"""

#Boxplot Crecimiento de Planta
fig, axs = plt.subplots(figsize=(11,6))
axs.boxplot(df['crecimiento_planta'])
axs.set_title('Crecimiento de Planta')
axs.set_xlabel('Crecimiento de Planta')
axs.set_ylabel('Frecuencia')
plt.show()
"""Validación: sin outliers"""

#2. Calcular el coeficiente de correlación de Pearson entre temperatura 
# y crecimiento_planta usando numpy.corrcoef()
corr_matrix = np.corrcoef(df['temperatura'], df['crecimiento_planta'])
print("Matríz de correlación:\n",corr_matrix)
"""Alta correlación"""
#Valor único de correlación
correlacion = np.corrcoef(df['temperatura'], df['crecimiento_planta'])[0, 1]
print(f"Correlación entre temperatura y crecimiento de planta: {correlacion:.2f}")
"""Alta correlación"""

#3. Implementar una regresión lineal simple con scikit-learn usando temperatura como predictor 
# y crecimiento planta como variable dependiente
x = df[['temperatura']]  # variable independiente
y = df['crecimiento_planta'] # variable dependiente
model = LinearRegression()
model.fit(x,y)

#Ver el resumen del modelo
print("Resumen del Modelo")
print(f"Intecepto (β0):{model.intercept_:.3f}")
print(f"Intecepto (β1):{model.coef_[0]:.3f}")

#Interpretación del Modelo
print(f"Interpretación por cada °C adicional, la altura promedio del arbol aumenta {model.coef_[0]}")

#4. Visualizar los datos con un gráfico de dispersión y la línea de regresión
#Relación entre temperatura y crecimiento de planta
plt.scatter(df['temperatura'], df['crecimiento_planta'],alpha = 0.7)
plt.title("Temperatura vs Crecimiento de planta")
plt.xlabel("Temperatura")
plt.ylabel("Crecimiento de planta")
plt.grid(True)
#plt.show()

#Visualizar la linea de Regresión
y_pred = model.predict(x)
plt.plot(df['temperatura'], y_pred, color='red', label='Linea de Regresión')
plt.title("Regresión Lineal Simple")
plt.grid(True)
plt.show()

#5. Evaluar el rendimiento del modelo
mse = mean_absolute_error(y, y_pred)
mae = mean_absolute_error(y,y_pred)
r2 = r2_score(y, y_pred)

print("\nEvaluación del Modelo")
print(f"Error Cuadratico Medio (MSE): {mse:.2f}")
print(f"Error Absoluto Medio (MAE): {mae:.2f}")
print(f"Coeficiente de Determinación (R2): {r2:.3f}")

#6. Interpretar el coeficiente de Pearson y R², y discutir si una correlación
#fuerte implica causalidad
"""Sabemos de antemano que una fuerte correlación no implica causalidad.
En nuestro caso: El 80% de la variabilidad de Crecimiento de la Planta está siendo explicada 
por el modelo (en función de la temperatura). Es un muy buen ajuste general, especialmente 
en contextos con datos reales, donde rara vez se espera un ajuste perfecto.
👉 Significa que solo un 20% de la variación en los valores reales no se está explicando 
por el modelo (puede deberse a ruido, variables no incluidas o errores de medición)"""

"""El error medio (en magnitud) que está cometiendo el modelo es de aproximadamente 4 unidades, es decir,
que el error promedio en el cálculo del Crecimiento de la Planta serían --> 4 unidades de longitud (cm, mm)"""
