import pandas as pd

df = pd.read_csv("../data/inputs/ejemplo_datos_outliers.csv")

# Convertir la columna "Salario" a tipo numérico, manejando errores
df["Salario"] = pd.to_numeric(df["Salario"], errors="coerce") 
q1 = df["Salario"].quantile(0.25)
q2 = df["Salario"].quantile(0.50)   
q3 = df["Salario"].quantile(0.75)

iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
outliers = df[(df["Salario"] < limite_inferior) | (df["Salario"] > limite_superior)]
valores_no_outliers = df[(df["Salario"] >= limite_inferior) & (df["Salario"] <= limite_superior)]

print("Cuartil 1 (Q1):", q1)    
print("Cuartil 2 (Q2):", q2)    
print("Cuartil 3 (Q3):", q3)
print("Límite inferior:", limite_inferior)
print("Límite superior:", limite_superior)
print("Outliers:\n", outliers)
print("Valores no outliers:\n", valores_no_outliers)  