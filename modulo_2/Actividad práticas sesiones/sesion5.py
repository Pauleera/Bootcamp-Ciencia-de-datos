productos = ["Pantalon" , "Polera", "Bufanda","Lavadora","Secadora", "Celular", "Tablet"]
cantidad_productos = 2

for i in range(cantidad_productos):
    print(f"Ingrese {cantidad_productos} productos nuevos")
    new_productos = input("Ingrese un nuevo producto: ")
    productos.append(new_productos)

productos_destacados = productos[:3]
print("Productos destacados:", productos_destacados)

inventario = {
    "Pantalon": 10,
    "Polera": 20,
    "Bufanda": 15,
    "Lavadora": 5,
    "Secadora": 3,
    "Celular": 8,
    "Tablet": 12
}

new_product = input("Ingrese un nuevo producto: ")
new_product_stock = int(input("Ingrese la cantidad de stock del nuevo producto: "))
inventario[new_product] = new_product_stock
print("Produto e nventario actualizado")

print(f"El producto 'Pantalon' tiene {inventario['Pantalon']} unidades en stock.")

tupla_categorias = ("Electrónica", "Ropa", "Hogar")
print("La segunda categoría es:", tupla_categorias[1])

cat_electronica, cat_ropa, cat_hogar = tupla_categorias

productos_mayusculas = [producto.upper() for producto in productos]
productos_unicos = set(productos_mayusculas)
if len(productos_unicos) < len(productos_mayusculas):
    print("Hay productos duplicados en la lista.")
else:
    print("Todos los productos son únicos.")


print("Productos en mayúsculas:", productos_mayusculas)