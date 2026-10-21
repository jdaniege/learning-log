km = float(input("Ingrese los kms para calcular por millas: "))
c  = float(input("Ingrese los celsius: "))
kg = float(input("Ingrese los kilos"))

mll = km * 0.621371
f = c * 9 / 5 + 32
lbr = kg * 2.20462

print(f"Las millas son {mll:.2f} los grados son {f:.2f} las libras son{lbr:.2f}")