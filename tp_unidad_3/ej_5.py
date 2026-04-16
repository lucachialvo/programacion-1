vida_gladiador = 100
vida_enemigo = 100
pociones = 3
ataque_gladiador = 15
ataque_enemigo = 12
turno_gladiador = True
nro_turno = 0

print('--- BIENVENIDO A LA ARENA ---')
name = input('Nombre del gladiador: ')

#validar name
while name.isalpha() == False:
    name = input('Error: Solo se permiten letras.\nNombre del gladiador: ')

print('=== INICIO DEL COMBATE ===')

# ciclo while mientras ambos tengan hp>0
while vida_gladiador > 0 and vida_enemigo > 0:
    #menu de acciones:
    print(f'''
{'=== MENU DE ACCIONES ===' if nro_turno == 0 
                            else '=== NUEVO TURNO ==='}

{name.capitalize()} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}
Elige acción: 
1. Ataque Pesado
2. Ráfaga Veloz
3. Curar''')
    opcion = input('Opcion: ')
    while opcion.isdigit() == False or (
        opcion > '3' or opcion < '1'):
        
        opcion = input('Error: Ingrese un número válido.\nOpcion: ')
    
    nro_turno += 1
    
    if opcion == '1':
        if vida_enemigo < 20:
            print('> Golpe crítico!')
            vida_enemigo -= ataque_gladiador*1.5
            print(f'> Atacaste al enemigo por {ataque_gladiador*1.5} puntos de daño!')
        else:
            vida_enemigo -= ataque_gladiador
            print(f'> Atacaste al enemigo por {ataque_gladiador} puntos de daño!')
        
    elif opcion == '2':
        print('> ¡Inicias una ráfaga de golpes!')
        for i in range(3):
            vida_enemigo -= 5
            print('> Golpe conectado por 5 de daño')
    
    elif opcion == '3':
        if pociones > 0:
            vida_gladiador += 30
            pociones -= 1
        else:
            print('> ¡No quedan pociones!')
    
    # enemigo ataca
    vida_gladiador -= ataque_enemigo
    print('>> ¡El enemigo te atacó por 12 puntos de daño!')

# fin del juego, evaluar quien gano
if vida_gladiador > 0:
    print(f'VICTORIA! {name.capitalize()} ha ganado la batalla.')
else:
    print(f'DERROTA. Has caido en combate.')