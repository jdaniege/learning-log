total = float(input("Cual es el total de su compra: "))
if total >= 200000:
	descuento = (total * 0.15)
	desf = total - descuento
	print(f"El total con descuento es de: {desf:.2f}")
elif total >= 100000:
	descuento = (total * 0.10)
	desf = total - descuento
	print(f"El total del producto con descuento es de: {desf:.2f}")
else:
	print("No aplica para descuento")