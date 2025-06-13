
# Definicios de estructuras para libro, descuento y factura
libros = []
dicc_libros = {
    'titulo': 'default',
    'autor': 'autor',
    'precio': 0.0,
    'cantidad_stock': 1,
}

descuentos = []
dicc_descuentos ={
    'autor':'default',
    'descuento': 0.0
 }

factura = []
factura_detail = {
    'libro': 'default',
    'cantidad': 0,
    'precio_unitario': 0.0,
    'precio_total': 0.0,
    'descuento': 0.0,
    'precio_final': 0.0
}

# Funciones para manejar libros, descuentos y facturas

def agregar_libro(titulo, autor, precio, cantidad_stock):
    libro = dicc_libros.copy()
    libro['titulo'] = titulo
    libro['autor'] = autor
    libro['precio'] = precio
    libro['cantidad_stock'] = cantidad_stock
    libros.append(libro)

def mostrar_libros_disponibles():
    print("\nLibros disponibles:")
    print("\nNOMBRE DEL LIBRO | AUTOR | PRECIO | STOCK\n")
    for libro in libros:
        if libro['cantidad_stock'] > 0:
            print(f"{libro['titulo']} | {libro['autor']} | ${libro['precio']} | {libro['cantidad_stock']}")

def filtra_por_precio(precio_minimo, precio_maximo):
    print(f"\nLibros entre ${precio_minimo} y ${precio_maximo}:")
    print("\nNOMBRE DEL LIBRO | AUTOR | PRECIO | STOCK\n")
    for libro in libros:
        if precio_minimo <= libro['precio'] and libro['precio'] <= precio_maximo:
            print(f"{libro['titulo']} | {libro['autor']} | ${libro['precio']} | {libro['cantidad_stock']}")



def comprar_libro(titulo, cantidad):
    for libro in libros:
        if libro['titulo'].lower() == titulo.lower():
            if libro['cantidad_stock'] >= cantidad:
                libro['cantidad_stock'] -= cantidad
                precio_final = libro['precio']
                for descuento in descuentos:
                    if libro['autor'] == descuento['autor']:
                        print("Excelente, hay un descuento disponible para este autor.")
                        precio_final = libro['precio'] * (1 - descuento['descuento'] / 100)
                        print(f"Descuento aplicado: {descuento['descuento']}% para autor {libro['autor']}. Precio final: ${precio_final}\n")
                        break
    
                print(f"Compra exitosa: {cantidad} x '{titulo}' comprados exitosamente. - Total: ${precio_final * cantidad}\n")
                agregar_factura(titulo, cantidad, libro['precio'] , descuento['descuento'] if 'descuento' in locals() else 0) #descuento es 0 si no hay descuento

                return
            else:
                print(f"No hay suficiente stock de '{titulo}'. Stock disponible: {libro['cantidad_stock']}")
                return
    print(f"El libro '{titulo}' no está disponible.")

def agregar_descuento(autor, descuento):
    descuento_info = dicc_descuentos.copy()
    descuento_info['autor'] = autor
    descuento_info['descuento'] = descuento
    descuentos.append(descuento_info)

def agregar_factura(libro, cantidad, precio_unitario, descuento):
    precio_total = precio_unitario * cantidad
    precio_final = precio_total * (1 - descuento / 100)
    factura_item = factura_detail.copy()
    factura_item['libro'] = libro
    factura_item['cantidad'] = cantidad
    factura_item['precio_unitario'] = precio_unitario
    factura_item['precio_total'] = precio_total
    factura_item['descuento'] = descuento
    factura_item['precio_final'] = precio_final
    factura.append(factura_item)

#Añadir los datos de los libros y descuentos

agregar_libro("Cien años de soledad", "Gabriel García Márquez", 12000, 20)
agregar_libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 15000, 15)
agregar_libro("Todo el mundo miente", " Seth Stephens-Davidowitz", 8000, 3)
agregar_libro("Lazos de amor", "Brian Weiss", 8000, 3)
agregar_libro("Muchas vidas, muchos maestros", "Brian Weiss", 15000, 30)
agregar_libro("Nacidos de la Bruma: El imperio final", "Brandon Sanderson", 28000, 30)
agregar_libro("Nacidos de la Bruma: El pozo de la ascensión", "Brandon Sanderson", 28000, 10)
agregar_libro("Nacidos de la Bruma: El héroe de las eras", "Brandon Sanderson", 28000, 20)

agregar_descuento("Gabriel García Márquez", 10)
agregar_descuento("Brandon Sanderson", 40)

# Menú principal del programa

while True: 
    print("\n--- Menú de Biblioteca ---")
    print("1. Mostrar libros disponibles")
    print("2. Filtrar libros por rango de precio")
    print("3. Comprar libro")
    print("4. Finalizar comprar y ver factura")
    opcion = input("Seleccione una opción (ejemplo: 1): ")

    if opcion == '1':
        mostrar_libros_disponibles()
    elif opcion == '2':
        precio_minimo = float(input("Ingrese el precio mínimo: $ "))
        precio_maximo = float(input("Ingrese el precio máximo: $"))
        filtra_por_precio(precio_minimo, precio_maximo)
    elif opcion == '3':
        titulo = input("Ingrese el título del libro a comprar: ")
        cantidad = int(input("Ingrese la cantidad a comprar: "))
        comprar_libro(titulo, cantidad)

    elif opcion == '4':
        print("\nFactura:")
        total_factura = 0
        total_ahorrado_por_descuento = 0
        for item in factura:
            print(f"{item['cantidad']} x {item['libro']} - Precio unitario: ${item['precio_unitario']}, Total: ${item['precio_total']}, Descuento: {item['descuento']}%, Precio final: ${item['precio_final']}")
            total_factura += item['precio_final']
            total_ahorrado_por_descuento += item['precio_total'] * (item['descuento'] / 100)
        print(f"En esta compra has ahorrado: {total_ahorrado_por_descuento}")
        print(f"Total de la factura: ${total_factura}")
        print("Saliendo del programa... Gracias por su compra.")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")