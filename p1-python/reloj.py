total = int(input("Ingrese la cantidad de segundos que desea calcular: "))
horas = total // 3600
res = total  % 3600
min = res // 60
seg = res % 60
print(f"La cantidad de tiempo que se calculo fue de {horas} horas {min} minutos {seg} segundos")