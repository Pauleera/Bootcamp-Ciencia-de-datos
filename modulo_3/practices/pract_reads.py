import pandas as pd

# df = pd.read_csv('../data/inputs/ventas.csv', sep=",")
# print(df)

#limpiar datos (NaN)
# df = df.dropna()
# print("Data despues de dropna: ")
# print(df)

data = {
    "prodcuto": ["Sandia", "Durazno", "Peras", "Kiwi"],
    "precio": [1.2, 0.5, 0.8, 1.5]
}

df = pd.DataFrame(data)
df.to_csv('../data/inputs/productos.csv', index=False, sep=";")
