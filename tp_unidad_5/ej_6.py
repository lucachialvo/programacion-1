# hecho por luca chialvo

#Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

arr = [1,2,3,4,5,6,7]
array2 = arr.copy()
n = len(arr)
temp = arr[-1]
i = 1

print(f"Original: {arr}")

while i < n:
    arr[-i] = arr[-i-1]
    i+= 1
arr[0] = temp

print(f"Desplazada:\n{arr}")

#tambien se puede hacer con slicings
array2 = array2[-1:] + array2[:-1]
print(array2)