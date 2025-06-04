#cree un programa que pida al usuario un numero 
#y su cuadrado y su cubo, mostrando ambos resultados 
try:
    number = int(input("Ingrese su número: "))
except:
    print("⚠️ Solo puede ingresar un número")
    number = int(input("Ingrese su número: "))

numberCuadrado = number**2
numberCubo = number**3

print(f"{number} al cuadrado = {numberCuadrado} \n"
       f"y {number} al cubo = {numberCubo}")