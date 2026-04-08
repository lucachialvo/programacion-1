# hecho por luca chialvo
nombres = ["luca", "jose","pablo","candela", "fermin","juan", "mateo", "marcos", "pepe","maria"]
search = input("Nombre a buscar: ")

if nombres.count(search)>0:
    print("El nombre se encuentra en la lista.")
    print(f"Aparece en la posicion: {nombres.index(search)}")
else:
    print("Error: no se encontró el nombre.")