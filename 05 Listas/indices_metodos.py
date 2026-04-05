# los indices se aplican para listas, tuplas, dict, strings
lista = ["naranja","pera","manzana","banana","frutilla", "melon", "sandia", "mandarina", "uva", "limon", "kiwi", "anana"]

print(f"{lista[0]=}") #el primero
print(f"{lista[-1]=}") #el ultimo
print(f"{lista[1:3]=}") #desde el 2do hasta el 4to
print(f"{lista[1::2]=}") #desde el 2do hasta el ultimo, con un step de 2
print(f"{lista[::2]=}") #desde el 1ro hasta el ultimo, con un step de 2
print(f"{lista[::]=}") #la lista completa, pero usando indices -> recorre desde el 1ro al ultimo con step de 1
print(f"{lista[::-1]=}") # invierte la lista (util para invertir cualquier secuencia de datos) -> desde el ultimo al 1ro. o mejor dicho, del 1ro al ultimo pero con orden inverso
print(f"{lista[0:-1]=}") # desde 0 a ultimo - 1 


print('-'*30)
for x in lista:
    print(x)
    #x toma el valor de los objetos de la lista por cada iteracion
print('-'*30)

print(f"Atributos y metodos que acepta una lista:\n{dir(lista)[::-1]}")

print('-'*30)
lista.sort()
print(f"lista ordenada: {lista}")

lista.reverse()
print(f'Lista al reves{lista}')

lista.pop(0)
print(lista) #saca el indice 0 de la lista

lista.insert(0, "arandano")
print(lista) # insertar "arandano" en el indice 0

print(f'Indice de "banana": {lista.index("banana")}') # muestra el indice de banana
print(f'Longitud: {len(lista)}')