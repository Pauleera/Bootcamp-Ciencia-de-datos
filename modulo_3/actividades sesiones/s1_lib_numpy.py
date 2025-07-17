import numpy as np
import random
def crear_vector():
    #numpy.arange() crea un vector de 10 elementos  

    vector_1d_10 = np.arange(10)
    print("\nVector de 10 elementos:")
    print(vector_1d_10)
    return vector_1d_10

vector_1d_10 = crear_vector()

def generar_matriz():
    #numpy.tandom.rand() genera numero flotante con distribucion uniforme
    # en el intervalo [0.0, 1.0)
    matriz_3x3 = np.random.rand(3,3)
    print("\nMatriz 3x3 generada:")
    return print(matriz_3x3)

generar_matriz()

def matriz_identidad():
    #numpy.eye() genera una matriz identidad de tamaño n
    matriz_identidad = np.eye(4)
    print("\nMatriz identidad 4x4:")
    return print(matriz_identidad)

matriz_identidad()

def redimencionar_matriz():
    #numpy.reshape() redimensiona una matriz
    matriz_reshape = vector_1d_10.reshape(2, 5)
    print("\nMatriz redimensionada 2x5:")
    return print(matriz_reshape)

redimencionar_matriz()

def seleccionar_mayores():
    #numpy.where() devuelve los indices de los elementos que cumplen la condicion
    mayores_5 = vector_1d_10[vector_1d_10 > 5]
    print("\n Los elementos mayores a 5:")
    return print(mayores_5)

seleccionar_mayores()

def sumar_arreglos():
    #numpy.sum() suma los elementos de un arreglo
    array_1 = np.arange(5)
    array_2 = np.arange(5)
    suma_array = array_1 + array_2
    print("\nArreglo 1:")
    print(array_1)
    print("Arreglo 2:")
    print(array_2)
    print("\nSuma de dos arreglos:")
    return print(suma_array)

sumar_arreglos()

def raiz_cuadrada_vector():
    #numpy.sqrt() calcula la raiz cuadrada de cada elemento de un arreglo
    raiz_vector = np.sqrt(vector_1d_10)
    print("\nRaíz cuadrada del vector:")
    return print(raiz_vector)

raiz_cuadrada_vector()





