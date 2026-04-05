lista = [8,3,1,4,2,6,5,7]

n = len(lista)
for i in range (n-1):
    indice_minimo = i

    for k in range(i+1,n):
        if lista[k] < lista[indice_minimo]:
            indice_minimo = k
    if indice_minimo != i:
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

print(lista)