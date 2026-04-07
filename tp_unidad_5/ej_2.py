# hecho por luca chialvo

productos = [] 
for i in range(5):
    productos += [input('Cargue un producto: ')]

print(sorted(productos))

borrar = input('Que producto desea eliminar: ')

while borrar not in productos:
    borrar = input('Ingresar un producto dentro de la lista: ')

productos.remove(borrar)

print(productos)
