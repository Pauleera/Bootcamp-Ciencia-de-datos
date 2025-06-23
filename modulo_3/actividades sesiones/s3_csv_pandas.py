import pandas as pd

df = pd.read_csv('../data/inputs/ventas2.csv')
print("Las primeras 5 filas del DataFrame:")
print(df.head(5))

df_productos_precio = df[['Producto', 'Precio']]
print("\nDataFrame con productos y precios:")
print(df_productos_precio.head(5)) 

print("\nFiltrar productos con precio mayor a 50:")
df_filtrado = df_productos_precio[df_productos_precio['Precio'] > 50]
print(df_filtrado)  

print("\nGuardando el DataFrame filtrado en un nuevo archivo CSV...")
df_filtrado.to_csv('../data/outputs/ventas_filtradas.csv', index=False, sep=";")
print("Archivo CSV guardado existosamente en 'venta_filtradas.csv'")