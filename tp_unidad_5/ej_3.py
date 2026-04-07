# hecho por luca chialvo

import random

array = [random.randint(1,100) for _ in range(15)]
print(f"{array = }")

pares, impares = [], []

for i in range(len(array)):
    if array[i]%2 == 0:
        pares += [array[i]]
    else:
        impares += [array[i]]

print('Pares: ', end='')
for i in range(len(pares)):
    print(pares[i], end=', ' if i < (len(pares)-1) else '\n')

print('Impares: ', end='')
for i in range(len(impares)):
    print(impares[i], end=', ' if i < (len(impares)-1) else '\n')

print(f'Hay {len(pares)} numeros pares')
print(f'Hay {len(impares)} numeros impares')