def merge_sort(array):
    if len(array) > 1:  #el alg. solo se ejecuta si la lista tiene mas de un elemento
        left_arr = array[:len(array)//2] # de la mitad hacia el ppio
        right_arr = array[len(array)//2:] # de la mitad hacia el final
        
        # dividir recursivamente ambos arrays hasta tener arrays de 1 item
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0 # index del item mas a la izq. de left_arr
        j = 0 # index del item mas a la izq. de right_arr
        k = 0 # index del array resultante

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                array[k] = left_arr[i]
                i += 1
            else:
                array[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            array[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            array[k] = right_arr[j]
            j += 1
            k += 1


lista = [9,1,2,5,3,6,8,7,3,5,1,6,3,9,0,0]
merge_sort(lista)
print(lista)