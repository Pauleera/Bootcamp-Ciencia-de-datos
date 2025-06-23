import pandas as pd
df  = pd.read_excel('/Users/pauleera/Documents/Bootcamp Ciencia de datos/modulo_3/data/inputs/excel/reporte.xlsx',sheet_name='Ventas2023')
print(df.head())

#df.to_excel('/Users/pauleera/Documents/Bootcamp Ciencia de datos/modulo_3/data/outputs/excel/reporte_salida.xlsx', index=False, sheet_name='Ventas2023')