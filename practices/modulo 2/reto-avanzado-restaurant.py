def main():
    categorias = {"ENTRANTES" , "FONDOS", "POSTRES"}
    categorias_dict = {
        1: "ENTRANTES",
        2: "FONDOS",
        3: "POSTRES"
    }
    platos = []
    print("\n R E S T A U R A N T E - DOÑA PAULA \n")
    choose = ""
    while choose != "5":
        print("Menú \n 1. Agregar plato \n 2. Ver pedidos por categoría \n 3. Calcular propina \n 4. Eliminar platillo por categoría")

        choose = input("Elige número del menú: ")

        if choose == "1":
            print("Agregar plato")
            agregarPlatillos(categorias_dict , platos)
        elif choose == "2":
            print(" Ver pedidos por categoria ")
            listarPlatillos(categorias_dict , platos)
        elif choose == "3":
            print("Calcular propina")
        elif choose == "4":
            print("Eliminar platillo por Categoría")


def agregarPlatillos(categorias, platos):
    nombre_plato = ""
    while len(nombre_plato) <= 1: 
        nombre_plato = str(input("Ingrese el nombre del plato: "))
    precio_plato = 0.
    while precio_plato <= 0:
        precio_plato = float(input("Ingrese el precio del plato: $ "))
    for clave, valor in categorias.items() :
        print(f"{clave}. {valor}")
    

    categoria_choose = int(input(f"Ingrese a que categoría para el plato {nombre_plato} 1, 2 o 3: "))
    while categoria_choose >= 3:
        print("⚠️ Debe elegir un número entre 1 , 2 o 3 ")
        categoria_choose = int(input(f"Ingrese a que categoría para el plato {nombre_plato} 1, 2 o 3: "))
    
    plato = (nombre_plato, precio_plato, categorias[categoria_choose])
    platos.append(plato)
    print(f"✅ El platillo {nombre_plato} a $ {precio_plato} en la categoría {categorias[categoria_choose]} se añadió correctamente  ")


def listarPlatillos(categorias , platos):
    print("Revisar pedido en categoría ")
    for clave, valor in categorias.items() :
        print(f"{clave}. {valor}")
    
    categoria_choose = int(input(f"Ver categoría 1, 2 o 3: "))
    while categoria_choose >= 3:
        print("⚠️ Debe elegir un número entre 1 , 2 o 3 ")
        categoria_choose = int(input(f"Ver categoría 1, 2 o 3:  "))
    
    categoria_platillo = categorias[categoria_choose]
    encontrados = False
    for nombre, precio, categoria in platos:
        if categoria_platillo == categoria:
            print(f"{nombre} $ {precio}")
            encontrados = True
    if not encontrados:
        print(f" 🤧 No se han encontrados platillos en la categoría {categoria_platillo}")
    
    

if __name__ == "__main__":
    main()