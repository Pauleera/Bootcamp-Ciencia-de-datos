import math

class SpaceReservation:
    def __init__(self, espacio_id ):
        self.espacio_id = espacio_id
        #diccionario que asocie fechas, nombre de usuario
        self.asociaciones_user_date = {}

        def add_asociaciones_user_date(self, date, user):
            self.asociaciones_user_date[date] = user
        
        def reserve(self, date,user):
            print(".. Registrando reserva")

        def reservation_count(self):
            count = 0
            print("Contar reservas")
            return count

        def reservation_fee(self):
            count = reservation_count()
            return math.pow(count, 0.8)
        
        
espacio_id = input("Ingrese el ID del espacio: ")
espacio = SpaceReservation(espacio_id=espacio_id)

while True:
    print("--- Opciones ---")
    print("1. Agregar asociación (fecha , user ) ")
    print("2. Imprimir tarifa ")
    print("4. Salir ")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        user = input("Ingrese el nombre de usuario")

        date = input("Ingrese la fecha de la reserva: (DD/MM/AAAA)")        
        if (user.find("VIP") >= 0):
            print(" El cliente es VIP")
        espacio.asociaciones_user_date(date = date, user = user)
    elif opcion == "2":
        #mostrar resultado
        print(f"Tiempo valor de reservar {espacio.espacio_id} es: {espacio.reservar()} ")