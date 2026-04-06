import random

def binary_search(array, target):
    low = 0
    high = len(array)-1
    
    while low <= high:
        #para sacar el punto medio, sacamos el promedio de los indices low y high
        midpoint = low + (high - low) // 2
        
        if array[midpoint] == target: #comparamos el valor del *indice* del medio con el target
            return midpoint
        elif array[midpoint] > target:    
            high = midpoint -1
        else:
            low = midpoint +1
    return None

def verify(index_of_array):
    if index_of_array is not None:
        print(f"Target encontrado en indice: {index_of_array}")
    else:
        print("numero no encontrado")


lista = [x for x in range(1,11)]
input = random.randint(1,10)
print(f'Lista: {lista}')

result = binary_search(lista, input)
verify(result)