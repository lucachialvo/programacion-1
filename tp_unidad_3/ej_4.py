energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
cont_forzar = 0

print('\n<== Escape Room: La Bóveda ==>\n')
print('''Historia
Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo
limitados.
Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.''')

empezarJuego = input('Presiona <Enter> para continuar.')
while empezarJuego != '':
    empezarJuego = input('Presiona <Enter> para continuar.')

nombre = input('Nombre del agente: ')
while nombre.isalpha() == False:
    nombre = input('(Error) Ingrese el nombre del agente nuevamente: ')

while True:
    print(f'''
    <== MENU DE OPCIONES ==>
    1. Forzar cerradura (costo: -20 energía, -2 tiempo)
    2. Hackear panel (costo: -10 energía, -3 tiempo)
    3. Descansar (costo: +15 energía (máx 100)
    
    <== ESTADO DEL JUGADOR ==>
    Energia: {energia}
    Tiempo: {tiempo}
    Cerraduras abiertas: {cerraduras_abiertas}
    Alarma: {'OFF' if alarma == False else 'ON'}
    Codigo parcial: "{codigo_parcial}"
    ''')
    
    opcion = input('Opcion: ')
    while opcion.isdigit() == False:
        opcion = input('(Error) Opcion: ')
    while opcion < '1' or opcion > '3':
        opcion = input('(Error) Opcion: ')
    
    if opcion == '1': #forzar
        cont_forzar += 1
        print(f'\n>> Eligió: Forzar cerradura (x{cont_forzar}).\n> -2 tiempo\n> -20 energia')
        energia -= 20
        tiempo -= 2

        if cont_forzar >= 3:
            alarma = True
            print('> Se trabo la cerradura! Alarma encendida.')
        
        if energia < 40:
            print('> Riesgo de alarma!')
            opcion = input('> Ingrese un numero del 1 al 3.\nOpcion:')
            while opcion.isdigit() == False: 
                opcion = input('> (Error) Ingrese un numero del 1 al 3.\nOpcion:')
            while opcion < '1' or opcion > '3':
                opcion = input('> (Error) Ingrese un numero del 1 al 3.\nOpcion:')
            if opcion == '3':
                print('> Alarma encendida.')
                alarma = True
            else:
                print('> Opción valida. Continuas normalmente.')
        
        elif alarma == False:
            cerraduras_abiertas += 1
            print(f'[!] Se abrió una cerradura!\n> Cerraduras abiertas: {cerraduras_abiertas}')

    if opcion == '2': #hackear
        print('>> Eligió: Hackear panel.\n> -3 tiempo\n> -10 energia\n> Hackeando panel...')
        cont_forzar = 0
        energia -= 10
        tiempo -= 3
        #progreso de hackeo
        for i in range(1,5):
            codigo_parcial += 'A'
            print(f'> (Paso {i}) Codigo:{codigo_parcial}')
        if (len(codigo_parcial) >= 8) and (cerraduras_abiertas < 3):
            cerraduras_abiertas += 1
            print(f'\n[!] Se abrió una cerradura!\n> Cerraduras abiertas: {cerraduras_abiertas}')

    if opcion == '3': #descansar
        print('>> Eligió: Descansar.\n> -1 tiempo.')
        cont_forzar = 0
        tiempo -= 1
        # calculamos cuanta energia le tenemos que dar al jugador en base a la diferencia de energia:
        if abs(energia-100) <= 15:
        # si |energia - 100| <= 15, le sumamos la diferencia para que llegue a 100 como maximo
            print(f'> +{abs(energia-100)} energia (max: 100).')
            energia += abs(energia-100)
        else:
        # si |energia - 100| > 15, le sumamos 15 ya que asi no llega a 100
            print('> +15 energia (max: 100).')
            energia += 15
        
        if alarma == True:
            print('> -10 energía (penalizacion por alarma).')
            energia -= 10
    
    #condiciones de victoria/derrota:
    if cerraduras_abiertas == 3:
        print('\n<== VICTORIA ==>')
        break
    if (alarma == True) and (tiempo <= 3) and (cerraduras_abiertas != 3):
        print('\n<== DERROTA (bloqueo) ==>')
        break
    if energia <= 0 or tiempo <= 0:
        print('\n<== DERROTA ==>')
        break