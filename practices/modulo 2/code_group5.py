

def main ():
    enter = int(input("Elige un ejercicio (1, 2 o 3): "))
    if enter == 1:
        formatear_fecha()
    elif enter == 2:
        suma_espacios()
    elif enter == 3:
        mensaje_motivacional()
    else: 
        print("No exite intente nuevamente.")


def formatear_fecha():
    dia = int(input("Introduce el día: "))
    mes = int(input("Introduce el mes: "))
    año = int(input("Introduce el año: "))
    fecha = f"{dia:02}/{mes:02}/{año}"
    print(f"Fecha formateada: {fecha}")

def suma_espacios():
    frase = input("Introduce una frase: ")
    cantidad_espacios = frase.count(" ")
    caracteres = len(frase)
    print(f"La frase contiene {cantidad_espacios} espacios.")
    print(f"La frase contiene {caracteres} carácteres. ")
    

#Mensaje motivacional 
def mensaje_motivacional ():
    username = str(input("¿Cómo te llamas? "))
    objetive = str(input("¿Cuál es tu objetivo personal? "))

    print(f"{username}, ¡Tú puedes lograr {objetive} ! No te rindas 👏👏")


if __name__ == "__main__":
    main()