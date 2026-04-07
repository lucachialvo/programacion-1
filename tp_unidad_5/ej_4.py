# hecho por luca chialvo

array = [1,2,3,3,7,1,9,5,3]
array_sin_repetidos = array.copy()

for i in array:
    if array_sin_repetidos.count(i) > 1:
        array_sin_repetidos.remove(i)

array_sin_repetidos.sort()
print(array_sin_repetidos)
