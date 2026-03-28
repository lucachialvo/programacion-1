#programa 7
#Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("\n### Programa 7 ###")
print("Ingrese dos numeros enteros distintos de 0")
x = int(input("Primer numero (x): "))
y = int(input("Segundo numero (y): "))

print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} / {y} = {x/y}")