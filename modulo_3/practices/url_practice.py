import pandas as pd

url = "https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_y_territorios_dependientes_por_poblaci%C3%B3n"

tablas = pd.read_html(url)

print("Número de tablas encontradas:", len(tablas))

df = tablas[0]  # Selecciona la primera tabla
print("Contenido de la primera tabla:")
print(df.head())    

df.to_csv('../data/outputs/paises_dependientes.csv', index=False, sep=";")