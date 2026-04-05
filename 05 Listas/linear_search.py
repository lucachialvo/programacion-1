def linear_search(list, target):
    # retorna el indice del numero encontrado
    for i in range(len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index != None:
        print(f"Numero encontrado en el indice: {index}")
    else:
        print("Numero no encontrado")

# crea una lista de numeros del 0-9 por comprension
numbers = [x for x in range(1,100)]
user_input = int(input('ingresar un numero: '))

result = linear_search(numbers, user_input)
verify(result)