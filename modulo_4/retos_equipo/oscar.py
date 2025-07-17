# ------------------------------------------------
# EDA ROBUSTO MEJORADO - SCRIPT COMPLETO
# ------------------------------------------------
# Oscar Castro Rosso - Market Global
# ------------------------------------------------

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

encoding = 'utf-8'
sep = ','

# ------------- CONFIGURACIÓN INICIAL -------------
archivo = ""r'C:\Users\equipo\Desktop\Python_Escritorio\Modulo 4\30.06\Entradas\aire_principal.csv'   ""         # Cambia por tu archivo
df = pd.read_csv(archivo, encoding=encoding, sep=sep)
carpeta_salida = 'Salidas'              # Carpeta para guardar gráficos y archivos
umbral_categorias = 10                   # N° categorías para advertir "muchas"
os.makedirs(carpeta_salida, exist_ok=True)

# -------- BLOQUE 1: CARGA DE DATOS Y VERIFICACIÓN --------
print("\n[1] CARGA DE DATOS Y VERIFICACIÓN")

if not os.path.isfile(archivo):
    raise FileNotFoundError(f"Archivo '{archivo}' no encontrado. Revisa la ruta y el nombre.")
try:
    df = pd.read_csv(archivo)
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    exit()

print(f"\nDataset cargado correctamente. Dimensiones: {df.shape}")
print("Primeras filas:")
print(df.head())

# -------- BLOQUE 2: ANÁLISIS DE COLUMNAS Y TIPOS DE DATOS --------
print("\n[2] ANÁLISIS DE COLUMNAS Y TIPOS DE DATOS")
print("Columnas presentes y tipos:")
print(df.dtypes)
columnas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
columnas_categoricas = df.select_dtypes(include=['object', 'category']).columns.tolist()
print(f"Variables numéricas: {columnas_numericas}")
print(f"Variables categóricas: {columnas_categoricas}")

# -------- BLOQUE 3: ANÁLISIS DE VALORES NULOS --------
print("\n[3] ANÁLISIS DE VALORES NULOS")
nulos = df.isnull().sum()
porc_nulos = (nulos / len(df)).round(3)*100
tabla_nulos = pd.DataFrame({'nulos': nulos, 'porcentaje': porc_nulos})
print(tabla_nulos)
# Opcional: visualizar nulos
plt.figure(figsize=(8,4))
sns.heatmap(df.isnull(), cbar=False)
plt.title('Mapa de Valores Nulos')
plt.tight_layout()
plt.savefig(f'{carpeta_salida}/nulos_heatmap.png')
plt.close()

# -------- BLOQUE 4: ANÁLISIS DE DUPLICADOS --------
print("\n[4] ANÁLISIS DE DUPLICADOS")
num_duplicados = df.duplicated().sum()
print(f"Filas duplicadas: {num_duplicados}")
if num_duplicados > 0:
    print("Ejemplo de filas duplicadas:")
    print(df[df.duplicated()].head())
    df[df.duplicated()].to_csv(f'{carpeta_salida}/duplicados.csv', index=False)
    print(f"> Duplicados guardados en {carpeta_salida}/duplicados.csv")

# -------- BLOQUE 5: ESTADÍSTICAS DESCRIPTIVAS --------
print("\n[5] ESTADÍSTICAS DESCRIPTIVAS DE VARIABLES NUMÉRICAS")
print(df[columnas_numericas].describe().T)

print("\n[5b] ESTADÍSTICAS DE VARIABLES CATEGÓRICAS")
for col in columnas_categoricas:
    print(f"\nFrecuencias de '{col}':")
    print(df[col].value_counts(dropna=False))
    print(f"Cardinalidad: {df[col].nunique()} valores únicos")
    if df[col].nunique() > umbral_categorias:
        print(f"ADVERTENCIA: La variable {col} tiene muchas categorías ({df[col].nunique()})")
        print("Top 10 categorías:")
        print(df[col].value_counts().head(10))

# -------- BLOQUE 6: DISTRIBUCIONES Y OUTLIERS (NUMÉRICAS) --------
print("\n[6] DISTRIBUCIONES Y OUTLIERS")
outliers_total = pd.DataFrame()
for col in columnas_numericas:
    # Histograma
    plt.figure(figsize=(7,4))
    sns.histplot(df[col], bins=15, kde=True)
    plt.title(f'Histograma de {col}')
    plt.savefig(f'{carpeta_salida}/hist_{col}.png')
    plt.close()
    # Boxplot
    plt.figure(figsize=(4,6))
    sns.boxplot(y=df[col])
    plt.title(f'Boxplot de {col}')
    plt.savefig(f'{carpeta_salida}/box_{col}.png')
    plt.close()
    # Outliers con IQR
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lim_inf = Q1 - 1.5 * IQR
    lim_sup = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lim_inf) | (df[col] > lim_sup)]
    print(f"{col}: {len(outliers)} posibles outliers (criterio IQR).")
    if not outliers.empty:
        outliers.to_csv(f'{carpeta_salida}/outliers_{col}.csv', index=False)
        print(f"> Outliers de {col} guardados en {carpeta_salida}/outliers_{col}.csv")
        outliers_total = pd.concat([outliers_total, outliers])

# -------- BLOQUE 7: MATRIZ DE CORRELACIÓN Y RELACIONES --------
print("\n[7] MATRIZ DE CORRELACIÓN ENTRE VARIABLES NUMÉRICAS")
if len(columnas_numericas) > 1:
    correlacion = df[columnas_numericas].corr()
    print(correlacion)
    plt.figure(figsize=(7,5))
    sns.heatmap(correlacion, annot=True, cmap='coolwarm')
    plt.title("Matriz de Correlación")
    plt.tight_layout()
    plt.savefig(f"{carpeta_salida}/correlacion_heatmap.png")
    plt.close()
else:
    print("No hay suficientes variables numéricas para correlación.")

# -------- BLOQUE 8: ANÁLISIS CRUZADO (CATEGÓRICA VS NUMÉRICA) --------
print("\n[8] ANÁLISIS CRUZADO CATEGÓRICA - NUMÉRICA")
for cat in columnas_categoricas:
    for num in columnas_numericas:
        plt.figure(figsize=(8,4))
        sns.boxplot(x=df[cat], y=df[num])
        plt.title(f'Boxplot de {num} según {cat}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'{carpeta_salida}/box_{num}_por_{cat}.png')
        plt.close()
        print(f'Gráfico box_{num}_por_{cat}.png generado.')

# -------- BLOQUE 9: EXPORTACIÓN DE DATASET LIMPIO --------
print("\n[9] GENERACIÓN DE DATASET LIMPIO (sin duplicados ni outliers)")

# Eliminar duplicados
df_sin_duplicados = df.drop_duplicates()

# Eliminar outliers en todas las variables numéricas (aplicado secuencialmente)
df_limpio = df_sin_duplicados.copy()
for col in columnas_numericas:
    Q1 = df_limpio[col].quantile(0.25)
    Q3 = df_limpio[col].quantile(0.75)
    IQR = Q3 - Q1
    lim_inf = Q1 - 1.5 * IQR
    lim_sup = Q3 + 1.5 * IQR
    df_limpio = df_limpio[(df_limpio[col] >= lim_inf) & (df_limpio[col] <= lim_sup)]

ruta_limpio = f"{carpeta_salida}/dataset_limpio.csv"
df_limpio.to_csv(ruta_limpio, index=False)
print(f"Dataset limpio guardado como: {ruta_limpio}")
print(f"Filas originales: {len(df)}, filas limpias: {len(df_limpio)}")

# -------- BLOQUE 10: RESUMEN Y RECOMENDACIONES --------
print("\n[10] RESUMEN Y RECOMENDACIONES")
print(f"- Revisa los gráficos y archivos exportados en la carpeta /{carpeta_salida}/.")
print("- Si hay duplicados y outliers, revisa si corresponde eliminarlos o imputarlos según el negocio.")
print("- Variables categóricas con muchas categorías pueden ser ruido.")
print("- Analiza outliers antes de quitarlos; podrían ser datos válidos.")
print("- Dataset limpio listo para siguiente etapa: modelado, segmentación, etc.")
print("- Guarda este reporte y deja huella de tus decisiones.")

print("\n*** FIN DEL EDA ROBUSTO ***")
