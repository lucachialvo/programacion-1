tablero = [["-"]*3 for _ in range(3)]
n = len(tablero)

def mostrar_tablero(grid):
    for i in range(n):
        print(grid[0][i], grid[1][i], grid[2][i])

mostrar_tablero(tablero)

# Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# Mostrar el tablero después de cada jugada.