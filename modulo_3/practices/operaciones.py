import pandas as pd
data = {"Nombre": ["Juan", "Ana", "Pedro", "María"],
        "Edad": [28, 22, 35, 30],
        "Calificación": [85, 90, 78, 92]}

df = pd.DataFrame(data)
print(df)

print(df.describe())    

df.to_csv("../data/outputs/estudiantes.csv", index=False, sep=";")

df_filtrado = df[df["Calificación"] > 80]

cal_min = df_filtrado['Calificación'].min()
cal_max = df_filtrado['Calificación'].max()

#Normalizacion
#x - xmin / /(xmax - xmin)  * 



df_filtrado['cal_normalizada'] = df_filtrado['Calificación'] - cal_min / (cal_max - cal_min)    
df_ordenado = df_filtrado.sort_values(by='Calificación', ascending=False)   

print("\nDataFrame filtrado y ordenado:")
print(df_ordenado)


