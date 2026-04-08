# hecho por luca chialvo

from random import randint

ventasDelDia = []
ventasProdSemanal = []

ventas = [[randint(0,10)for _ in range(7)] for _ in range(4)]
n = len(ventas)

for dia in range(len(ventas[0])):
    ventasDelDia.append(sum([ventas[i][dia] for i in range(n)]))
diaConMasVentas = ventasDelDia.index((max(ventasDelDia)))


# TABLA
print("Prod\tDia 1\tDia 2\tDia 3\tDia 4\tDia 5\tDia 6\tDia 7")

for producto in range(4):
    print(f"P{producto+1}", end="\t" if producto<4 else "\n")
    for dia in range(7):
        print(f"{ventas[producto][dia]}", end="\t" if dia<6 else "\n")

# DATOS FINALES
for i in range(n):
    print(f"Ventas P{i+1}: {sum(ventas[i])}")
    ventasProdSemanal.append(sum(ventas[i]))
prodMasVendidoSemanal = ventasProdSemanal.index(max(ventasProdSemanal)) + 1

print(f"Dia con mas ventas: {diaConMasVentas+1}")
print(f"Producto mas vendido en la semana: P{prodMasVendidoSemanal}")
#mis condolencias al profe que leyo esto