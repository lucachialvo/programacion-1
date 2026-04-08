# hecho por luca chialvo

array = []
for i in range(8):
    userInput = int(input(f"Ingrese un numero entero ({i}): "))
    array.append(userInput)
print(array)
print(sorted(array))
print(sorted(array, reverse=True))
