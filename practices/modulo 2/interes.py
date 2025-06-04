# Cálculo de Interés Simple: Haga un programa que solicite un capital inicial,
# una tasa de interés (porcentaje) y un número de años. 
# Calcule el interés simple (capital * tasa * años / 100) y muestre el resultado.


cap_inicial = int(input("Ingrese su capital incial: "))
tasa_interes = float(input("Ingrese la tasa de interés (%): "))
número_años = int(input("ingrese el número de años: "))

interes_simple = (cap_inicial * tasa_interes * número_años)/100


print(f"El interés simple es de {interes_simple:,}")