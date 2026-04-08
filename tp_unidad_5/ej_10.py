# hecho por luca chialvo
from random import randint

PRODUCTOS = 4
DIAS = 7

# datos de venta random; 1) for es para generar 1 sublista con 7 nros, y el 2do es para repetir esa sublista 4 veces
ventas = [[randint(0,10)for _ in range(DIAS)] for _ in range(PRODUCTOS)] 
n = len(ventas)

ventasDelDia = []
for dia in range(DIAS): #sumatoria ventas de los 4 productos durante el dia
    ventasDelDia.append(sum(producto[dia] for producto in ventas))
diaConMasVentas = ventasDelDia.index((max(ventasDelDia)))


# TABLA
print("Prod\tDia 1\tDia 2\tDia 3\tDia 4\tDia 5\tDia 6\tDia 7")

for producto in range(PRODUCTOS):
    print(f"P{producto+1}", end="\t")
    for dia in range(DIAS):
        print(f"{ventas[producto][dia]}", end="\t" if dia<6 else "\n")


# DATOS FINALES
ventasProdSemanal = []
for i in range(n):
    totalVentas = sum(ventas[i])
    # calculas las ventas sumando todos los nros dentro de cada producto [[sum de prod1][sum de prod2][sum de prod3][sum de prod 4]]
    print(f"Ventas P{i+1}: {totalVentas}") 
    ventasProdSemanal.append(totalVentas)

prodMasVendidoSemanal = ventasProdSemanal.index(max(ventasProdSemanal)) + 1

print(f"Dia con mas ventas: {diaConMasVentas+1}")
print(f"Producto mas vendido en la semana: P{prodMasVendidoSemanal}")