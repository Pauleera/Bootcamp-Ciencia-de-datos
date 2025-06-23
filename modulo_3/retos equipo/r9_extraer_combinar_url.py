url1 = "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_y_territorios_dependientes_por_poblaci%C3%B3n"
url2 = "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_%C3%ADndice_de_desarrollo_humano"

import pandas as pd
df = pd.read_html(url1, header=0)[3]
print("Las primeras 5 filas del DataFrame 1: \n")
print(df)

df2 = pd.read_html(url2, header=0)[4]
print(" \n Las primeras 5 filas del DataFrame 2: \n")
print(df2)

#df.merge() usando parametro how='outer' para combinar ambos DataFrames, utilizando todas las filas de ambos DataFrames. 
df_combined = pd.merge(df, df2, left_on='País (o territorio dependiente)', right_on='País', how='outer')
print(" \n DataFrame combinado: \n")
print(df_combined)

print("\nGuardando el DataFrame combinado en un nuevo archivo CSV...")
df_combined.to_csv('../data/outputs/países_combinados.csv', index=False, sep=";")
print("Archivo CSV guardado exitosamente en 'países_combinados.csv'")
