import random

def binary_search(list, target):
    low = 0
    high = len(list)-1
    
    while low <= high:
        #para sacar el punto medio, sacamos el promedio de la longitud de la lista
        midpoint = (high+low)//2
        
        if list[midpoint] == target: #comparamos el valor del *indice* del medio con el target
            return midpoint
        elif list[midpoint] > target:    
            high = midpoint -1
        else:
            low = midpoint +1
    return None

def verify(index_of_list):
    if index_of_list != None:
        print(f"Target encontrado en indice: {index_of_list}")
    else:
        print("numero no encontrado")


lista = [x for x in range(1,11)]
input = random.randint(1,10)
print(f'Lista: {lista}')

result = binary_search(lista, input)
verify(result)