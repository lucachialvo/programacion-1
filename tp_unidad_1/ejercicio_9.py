#programa 9
#crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit.
print("\n### Programa 9 ###") 
print("Programa de conversion de unidades. Celsius -> Fahrenheit")
temp = float(input("Ingrese la temperatura (C): "))
print(f"{temp} C = {round((9/5) * temp + 32, 2)} F")