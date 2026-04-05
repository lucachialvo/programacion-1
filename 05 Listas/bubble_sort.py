def bubble_sort(lista):
    
    n = len(lista)
    
    for k in range(n):
        swaps = 0

        for i in range(n-1-k):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                swaps += 1

        if swaps == 0:
            print(f"Lista ordenada!\n{lista}")
            break

numeros = [0,43,57,21,30,10,25,4]

bubble_sort(numeros)
