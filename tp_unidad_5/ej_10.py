# hecho por luca chialvo
from random import randint

PRODUCTOS = 4
DIAS = 7

ventas = [[randint(0,10)for _ in range(DIAS)] # generar 1 sublista con 7 nros,
         for _ in range(PRODUCTOS)] # repetir esa sublista 4 veces

venta_diaria = []
for dia in range(DIAS): #sumatoria ventas de los 4 productos durante el dia
    venta_diaria.append(sum(producto[dia] 
                        for producto in ventas))
dia_con_mas_ventas = venta_diaria.index(max(venta_diaria))


# TABLA
print("Prod\tDia 1\tDia 2\tDia 3\tDia 4\tDia 5\tDia 6\tDia 7")

for producto in range(PRODUCTOS):
    print(f"P{producto+1}", end="\t")
    for dia in range(DIAS):
        print(f"{ventas[producto][dia]}", end="\t" if dia<6 else "\n")


# DATOS FINALES
ventas_prod_semanal = []

for i in range(len(ventas)):
    total_ventas = sum(ventas[i])
    # calculas las ventas sumando todos los nros dentro de cada producto 
    # [[sum de prod1][sum de prod2][sum de prod3][sum de prod 4]]
    print(f"Ventas P{i+1}: {total_ventas}") 
    ventas_prod_semanal.append(total_ventas)

prod_mas_vendido_semanal = ventas_prod_semanal.index(max(ventas_prod_semanal)) + 1

print(f"Dia con mas ventas: {dia_con_mas_ventas + 1}")
print(f"Producto mas vendido en la semana: P{prod_mas_vendido_semanal}")