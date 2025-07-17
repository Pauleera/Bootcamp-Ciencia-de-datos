import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('../data/dataset_con_outliers.csv')
print(df.head(5))

print("\n Verificar tipo de columnas: ")
print(df.info())
print(df.describe())

#Paso3 : Frencuencia de variables categoricas
freq_color = df['Color'].value_counts() #Nominales
freq_satifacion = df['Satisfaction'].value_counts(sort=False) #Ordinales

print(freq_color)
print(freq_satifacion)
