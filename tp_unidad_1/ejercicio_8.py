#programa 8
#Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. imc = peso(kg)/altura(m)**2
print("\n### Programa 8 ###")
print("Calcular el IMC (indice de masa corporal)\n")
altura = float(input("Ingrese su altura (en metros): "))
peso = float(input("Ingrese su peso (en kilogramos): "))
print(f"Su IMC (indice de masa corporal) es de {round(peso/altura**2, 2)}")