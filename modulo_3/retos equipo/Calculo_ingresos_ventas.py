import numpy as np

# valores enteror entre 10 y 50
cantidades_vendidas = np.random.randint(10,51, size = 5)
print(cantidades_vendidas)

# valores entre 50 y 500
precios_unitarios = np.random.randint(50, 501, size = 5)
print(precios_unitarios)

productos = np.array(['Carniceria', 'Maquillaje', 'Panaderia', 'Alcohol', 'Vestimenta'])

print("\nIngresos por producto:")
for i in range(len(productos)):
    ingreso = cantidades_vendidas[i] * precios_unitarios[i]
    print(f"{productos[i]}: ${ingreso:.2f}")

print("\n Porcetaje de ingresos por producto:")
#Calculamos el ingreso total 
ingresos_totales = np.sum(cantidades_vendidas * precios_unitarios)
for i in range(len(productos)):
    porcentaje = (cantidades_vendidas[i] * precios_unitarios[i]) / ingresos_totales * 100
    print(f"{productos[i]}: {porcentaje:.2f}%")

print("\n INGRESO TOTAL: $", ingresos_totales)

