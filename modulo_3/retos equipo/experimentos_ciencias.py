import pandas as pd
 
df = pd.read_csv('../data/inputs/data_exp.csv')
print(df)

# Filtrar resultados por experimento 

df_filtrado = df[df['Experimento'] == 'Densidad del Agua']
print("\n Filtrando resultados por experimento 'Densidad del Agua' \n")
print(df_filtrado)

# Convertir unidades de temperatura de Celsius a Kelvin
df['Resultado'] = df.apply(lambda row: row['Resultado'] + 273.15 if row['Unidad'] == '°C' else row['Resultado'], axis=1)
df['Unidad'] = df.apply(lambda row: 'K' if row['Unidad'] == '°C' else row['Unidad'], axis=1)
print("\n Cambiando unidad de *C a Kelvin \n")
print(df)


#Agrupar y contar experiemntos por grado 
df_agrupado = df.groupby(['Grado', 'Experimento']).size().reset_index(name='N° Experimentos')
print("\n Agrupando y contando experimentos por grado \n")
print(df_agrupado)

# Detectar anomalías  (Valores atípicos)
print("\n Detectando anomalías (valores atípicos) \n")
df_grouped_experimentos = df.groupby('Experimento')['Resultado'].agg(['mean', 'std']).reset_index()
print(df_grouped_experimentos)

#  
#                          Q1|-- IQR --|Q3
#outlier |---  Q1-1.5IQR  ---|         |--- Q3 + 1.5IQR ---| outlier
def detectar_anomalia_iqr(grupo):
    Q1 = grupo['Resultado'].quantile(0.25)
    Q3 = grupo['Resultado'].quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    #gropo.assign() permite agregar una nueva columna al DataFrame llama Anomalia_IQR 
    # que llama a la función lambda para determinar si el valor está fuera de los límites
    return grupo.assign(Anomalia_IQR=lambda x: x['Resultado'].apply(
        lambda v: 'Si' if v < limite_inferior or v > limite_superior else 'No'))

df = df.groupby('Experimento').apply(detectar_anomalia_iqr).reset_index(drop=True)


print(df[['Experimento', 'Resultado', 'Anomalia_IQR']])

