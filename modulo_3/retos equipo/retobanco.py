import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('../data/inputs/clientes_banco.csv')
print(df.head(5))

print("\n Verificar tipo de columnas: ")
print(df.info())
print(df.describe())

print("\n Datos nulos:")
print(df.isnull().sum())

print("\n Valores únicos de 'tipo_cuenta': ")
print(df['tipo_cuenta'].unique()) 

print("\n Convertir 'tipo_cuenta' a tipo categoría...")
df['tipo_cuenta'] = df['tipo_cuenta'].astype('category')

print("\n Rellenando los valores nulos de 'saldo' con mediana... ")
df['saldo'] = df['saldo'].fillna(df['saldo'].mean())

print("\n Eliminando datos duplicados")
df.drop_duplicates()



# Plot histogram
sns.histplot([df["edad"], df["saldo"], df["ingresos"]], kde = True)
plt.show()


# Crear la figura y los ejes
fig, axes = plt.subplots(1, 3, figsize=(15, 5))  # 1 fila, 3 columnas

# Dibujar el primer diagrama de caja
sns.boxplot(data=df["edad"], ax=axes[0])
axes[0].set_title('edad')

# Dibujar el segundo diagrama de caja
sns.boxplot(data=df["saldo"], ax=axes[1])
axes[1].set_title('Saldo')

# Dibujar el tercer diagrama de caja
sns.boxplot( data=df["ingresos"], ax=axes[2])
axes[2].set_title('Ingresos')

# Ajustar el diseño para evitar superposiciones
plt.tight_layout()

# Mostrar la figura
plt.show()

print("\n Analisis bivariados: ")

# Crear la figura y los ejes
fig, axes = plt.subplots(1, 2, figsize=(15, 5))  # 1 fila, 3 columnas

# Dibujar el primer diagrama de caja
sns.boxplot(x=df["tipo_cuenta"], y = df['saldo'] ,  ax=axes[0])
axes[0].set_title('Dispersión')

# 
sns.scatterplot(x='ingresos', y='edad', data=df, hue='tipo_cuenta' ,  ax=axes[1])
axes[1].set_title('Saldo')


# Ajustar el diseño para evitar superposiciones
plt.tight_layout()

# Mostrar la figura
plt.show()


