lista = [5,3,1,2,4]

n = len(lista)
for x in range(1,n):
    temp = lista[x]
    i = x - 1
    while i>=0 and lista[i] > temp:
        lista[i+1] = lista [i]
        i -= 1
    lista[i+1] = temp

print(lista)