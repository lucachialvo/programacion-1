def quick_sort(array):
    if len(array) <=1:
        return array
    pivot = array[-1] #pivote = ultimo item
    menores = [x for x in array[:-1] if x < pivot]
    mayores = [x for x in array[:-1] if x >= pivot]

    return quick_sort(menores) + [pivot] + quick_sort(mayores)

lista = [2,1,8,6,5,7,3,4]
print(quick_sort(lista))