import math, random

def calcular_area_rectangulo(largo, ancho):
    return largo*ancho 

def calcular_circunferencia(radio):
    return 2 * math.pi * radio

def calcular_promedio(lista):
    suma = 0
    for l in lista:
        suma = suma + l
        
    return suma/len(lista)

def calcular_promedio_avanzado(lista):
    return lista.mean()

def generar_numeros_aleatorios(cantidad, limite):
    numeros_random = []
    for i in range(cantidad):
        numeros_random.append(int(random.uniform(1, limite)))
    return numeros_random

while True:
    print("\n---- M E N Ú ---- ")
    print("1 . Calcular area rectángulo")
    print("2 . Calcular circunferencia")
    print("3 . Calcular promedio")
    print("4 . Calcular promedio version 2.0")
    print("5 . Generar numeros aleatorios")
    print("para salir escriba \'salir\'\n")

    menu = input("Escriba N° la opcion (ejemplo: 1): ")
    if menu.lower() == "salir":
        break

    match menu:
        case "1":
            largo = int(input("Ingrese el largo: "))
            ancho = int(input("Ingrese el largo: "))
            print(f"➡️ El área del rectángulo es: {calcular_area_rectangulo(largo, ancho)}")

        case "2":
            radio = int(input("Ingrese el radio: "))
            print(f"➡️ La circunferencia es de: {calcular_circunferencia(radio)}")

        case "3":
            lista = []
            nota = input("Ingrese un numero para calcular promedio: - (Escriba \'fin\' para terminar): ")
            while True:
                if nota.lower() == "fin":
                    break

                numero = float(nota)
                lista.append(numero)
                nota = input("Ingrese un numero para calcular promedio: - (Escriba \'fin\' para terminar): ")
            
            print(f"➡️ El promedio es: {calcular_promedio(lista)}")

        case "4":
            lista = []
            nota = input("Ingrese un numero para calcular promedio: - (Escriba \'fin\' para terminar: ")
            while True:
                if nota.lower() == "fin":
                    break

                numero = float(nota)
                lista.append(numero)
                nota = input("Ingrese un numero para calcular promedio: - (Escriba \'fin\' para terminar): ")
            
            print(f"➡️ El promedio es: {calcular_promedio(lista)}")

        case "5":
            cantidad = int(input("Ingrese la cantidad de números que quiere generar: "))
            limite = int(input("Ingrese el limite: "))
            print(f"➡️ Estos son sun número generados aleatoreamente: {generar_numeros_aleatorios(cantidad,limite)}")