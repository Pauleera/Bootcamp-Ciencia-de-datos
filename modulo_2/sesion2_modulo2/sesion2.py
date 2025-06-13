

precio_producto = int(input("Ingrese precio de producto ($): "))
cantidad = int(input("Ingrese cantidad comprada (unidades): "))
descuento = float(input("Ingrese el descuento (%): "))

total_sin_descuento = precio_producto * cantidad 

monto_descuento = total_sin_descuento * (descuento * 0.01)

total_con_descuento = total_sin_descuento - monto_descuento
print("\n-- Totales --\n")
print(f"Total sin descuento: $ {total_sin_descuento}")
print(f"Monto de descuento: $ {monto_descuento:.2f}")
print(f"Total con descuento: $ {total_con_descuento:.2f}")
