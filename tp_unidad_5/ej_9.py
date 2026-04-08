# hecho por luca chialvo
# ta te ti

tablero = [["-"]*3 for _ in range(3)]
vacias = 9 # contador de casillas vacias

def mostrarTablero(grid):
    for i in range(len(tablero)):
        print(grid[0][i], grid[1][i], grid[2][i])

def verificarJugada(playerInput, tablero, simbolo):
    permitidos = [0,1,2] # lista de nros permitidos
    row = int(playerInput[1])
    col = int(playerInput[0])

    while (row not in permitidos) or (col not in permitidos) or tablero[row][col] != "-":
        playerInput = input("(Error) Ingrese una opcion valida: ").split(" ")
        row = int(playerInput[1])
        col = int(playerInput[0])

    tablero[row][col] = simbolo

def terminarJuego(vacias):
    if vacias == 0: 
        return True
    else:
        return False

print('''== REGLAS ==:
Por cada turno, cada jugador debe ingresar la posicion de su "X" o "O"
Aclarar fila y columna separado por un espacio (ej: 1 2)
El juego se acaba cuando un jugador haga Ta-Te-Ti o cuando el tablero esté lleno y nadie haya ganado''')

while True: 
    mostrarTablero(tablero)

    playerInput = input("Turno de X: ").split(" ")
    verificarJugada(playerInput, tablero, "X")
    vacias -= 1
    
    mostrarTablero(tablero)
    
    if terminarJuego(vacias):
        print("Juego terminado")
        break

    playerInput = input("Turno de O: ").split(" ")
    verificarJugada(playerInput, tablero, "O")
    vacias -= 1