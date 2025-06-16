import numpy as np

matriz = np.array([[5,10,15] , [20,25,30] , [35,40,45]])
elemento = matriz[1, 2]  # Selecciona el elemento en la segunda fila y tercera columna
segunda_fila = matriz[1,:]  # Selecciona la segunda fila completa
print("Elemento seleccionado:", elemento)
print("Segunda fila:", segunda_fila)

mayor_que_20 = matriz[matriz > 20]
cantidad = len(mayor_que_20)  # Cuenta cuántos elementos son mayores que 20
cantidad_mayores_que_20 = mayor_que_20.size  # Cuenta cuántos elementos son mayores que 20  
print("Elementos mayores que 20:", mayor_que_20)
print("Cantidad de elementos mayores que 20: (con .size)", cantidad_mayores_que_20)
print("Cantidad de elementos mayores que 20: (con len())", cantidad)  # Imprime la cantidad de elementos mayores que 20