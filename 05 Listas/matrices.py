row = int(input('ingresar filas: '))
col = int(input('ingresar columnas: '))

# con esta forma podemos crear matrices tipo [[1,2,3], [1,2,3] ...]
# matriz = [[i for i in range(1,columnas+1)] for _ in range(1,filas+1) ]

matriz = [[0]*col for _ in range(row) ]
print(f"{matriz = }\n")

def mostrar_matriz(columnas, filas):
    # mostrar nro de columna
    for x in range(1, columnas+1):
        print(f"{x if x>1 else f'    {x}'}:", end=" ")
    print()
    
    # mostrar cada fila
    for i in range(len(matriz)):
        print(f"{i+1}: {matriz[i]}")

# permite cambiar todos los valores de la matriz
def modificar_matriz_completa(filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            matriz [i][j] = int(input(f"valor para ({i+1}, {j+1}): "))
    mostrar_matriz(filas, columnas)

mostrar_matriz(row, col)
modificar_matriz_completa(row, col)
