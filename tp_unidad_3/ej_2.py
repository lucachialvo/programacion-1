username = 'alumno'
password = 'python123'
i = 1

user_input = input(f'Intento {i}/3 - Usuario: ')
password_input = input('Clave: ')

while user_input != username or password_input != password:
    print('Error: credenciales inválidas\n')
    i +=1
    if i == 4:
        print('Cuenta bloqueada.')
        break
    user_input = input(f'Intento {i}/3 - Usuario: ')
    password_input = input('Clave: ')

if user_input == username and password_input == password:
    print('Acceso concedido.\n')

    while True:
        print('1) Estado 2) Cambiar clave 3) Mensaje 4) Salir')
        opcion = input('Opcion: ')

        if opcion.isdigit() == False:
            print('Error: ingrese un número válido.\n')
            continue
        if opcion < '1' or opcion > '4':
            print('Error: opcion fuera de rango.\n')
            continue

        if opcion == '1':
            print('\nInscripto\n')
        
        if opcion == '2':
            password = input('Nueva clave: ')
            while len(password)<6:
                password = input('Clave nueva rechazada, debe tener al menos 6 caracteres.\nIngrese de nuevo: ')
            print('Clave cambiada exitosamente.\n')
        
        if opcion == '3':
            print('\nFrase: "El que no sabe lo que busca no entiende lo que encuentra"\n')
        
        if opcion == '4':
            print('\nSalir.')
            break