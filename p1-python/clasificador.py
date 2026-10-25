nota = float(input("Ingrese su nota: "))
if nota < 0 or nota > 100:
	print("Valor Invalido")
elif nota >= 90:
	print("Su nota es A")
elif nota >= 80:
	print("Su nota es B")
elif nota >= 70:
	print("Su nota es C")
elif nota >= 60:
	print("Su nota es D")
elif nota >= 50:
	print("Su nota es E")
else:
	print("Su nota es F")