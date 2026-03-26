# agenda de turnos
lunes1 = ''
lunes2 = ''
lunes3 = ''
lunes4 = ''

martes1 = ''
martes2 = ''
martes3 = ''

#contador de turnos por dia
contLunes = 1
contMartes = 1

#lista de pacientes por dia
pacientesLunes = ''
pacientesMartes = ''

operador = input('Nombre del operador: ')
while operador.isalpha() == False:
    operador = input('Ingrese su nombre (solo utilice letras): ')
print(f'Bienvenido a la sesion {operador}.')

# menu repetitivo
while True:
    print('-'*30)
    option = input('1. Reservar turno\n2. Cancelar turno (por nombre)\n3. Ver agenda del día\n4. Ver resumen general\n5. Cerrar sistema\nOpcion: ')
    
    if option.isdigit() == False:
        print('Error: ingrese un número válido.\n')
        continue
    
    if option < '1' or option > '5':
        print('Error: opcion fuera de rango.\n')
        continue
    
    if option == '1':
        print('Eligió: Reservar turno.')
        
        dia = input('Elegir día (1: Lunes, 2: Martes): ')
        
        while dia.isdigit() == False:
            dia = input('Elegir día correctamente (1: Lunes, 2: Martes): ')
        
        if (dia != '1') and (dia != '2'):
            print('Error: Opcion fuera de rango, solo puede elegir dia Lunes o Martes.')
            continue

        if dia == '1':
            
            if contLunes >= 5:
                print('No se puede reservar mas turnos para este día.')
                continue
            
            nombrePaciente = input('Nombre del paciente: ')
            
            while nombrePaciente.isalpha() == False:
                nombrePaciente = input('Ingrese correctamente el nombre del paciente: ')
                

            #con el metodo count() podemos contar las veces que aparece un argumento en un string
            if f'{nombrePaciente} ' in pacientesLunes:
                print('Este paciente ya tiene un turno para el dia Lunes.')
                continue
            pacientesLunes += f'{nombrePaciente} '
            
            #asignar un paciente a un turno del lunes
            if lunes1 == '':
                print('Turno reservado exitosamente.')
                lunes1 += f'\nLunes Turno {contLunes}, paciente: {nombrePaciente}'
                print(lunes1)
                contLunes += 1
                continue

            elif lunes2 == '':
                print('Turno reservado exitosamente.')
                lunes2 += f'\nLunes Turno {contLunes}, paciente: {nombrePaciente}'
                print(lunes2)
                contLunes += 1
                continue
                
            elif lunes3 == '':
                print('Turno reservado exitosamente.')
                lunes3 += f'\nLunes Turno {contLunes}, paciente: {nombrePaciente}'
                print(lunes3)
                contLunes += 1
                continue
            
            elif lunes4 == '':
                print('Turno reservado exitosamente.')
                lunes4 += f'\nLunes Turno {contLunes}, paciente: {nombrePaciente}'
                print(lunes4)
                contLunes += 1
                continue
            
        # dia martes
        if dia == '2':
            if contMartes >= 4:
                print('No se puede reservar mas turnos para este día.')
                continue
            
            nombrePaciente = input('Nombre del paciente: ')
            
            while nombrePaciente.isalpha() == False:
                nombrePaciente = input('Ingrese correctamente el nombre del paciente: ')
                

            #verificamos que no se repitan los nombres en el mismo dia
            if f'{nombrePaciente} ' in pacientesMartes:
                print('Este paciente ya tiene un turno para el dia Martes.')
                continue
            pacientesMartes += f'{nombrePaciente} '
            
            #asignar un paciente a un turno del martes
            if martes1 == '':
                print('Turno reservado exitosamente.')
                martes1 += f'\nMartes Turno {contMartes}, paciente: {nombrePaciente}'
                print(martes1)
                contMartes += 1
                continue

            elif martes2 == '':
                print('Turno reservado exitosamente.')
                martes2 += f'\nMartes Turno {contMartes}, paciente: {nombrePaciente}'
                print(martes2)
                contMartes += 1
                continue
                
            elif martes3 == '':
                print('Turno reservado exitosamente.')
                martes3 += f'\nMartes Turno {contMartes}, paciente: {nombrePaciente}'
                print(martes3)
                contMartes += 1
                continue

    if option == '2':
        print('\nEligió: Cancelar turno.')
        
        dia = input('Elegir día del turno a cancelar (1: Lunes, 2: Martes): ')
        while dia.isdigit() == False:
            dia = input('Elegir día correctamente (1: Lunes, 2: Martes): ')
        
        if (dia != '1') and (dia != '2'):
            print('Error: Opcion fuera de rango, solo puede elegir dia Lunes o Martes.')
            continue
        
        nombrePaciente = input('Nombre del paciente: ')

        
        if nombrePaciente not in (pacientesLunes or pacientesMartes): 
            print('Error: elija un paciente que esté registrado.')
            continue

        if dia == '1':
            if nombrePaciente in lunes1:
                lunes1 = ''
                pacientesLunes = pacientesLunes.replace(nombrePaciente,'')
                contLunes -= 1
                print('Turno cancelado exitosamente.')
                continue
            
            elif nombrePaciente in lunes2:
                lunes2 = ''
                pacientesLunes = pacientesLunes.replace(nombrePaciente,'')
                # si contLunes > 1, resta 1, si no, resta 0
                if contLunes > 1:
                    contLunes -= 1 
                print('Turno cancelado exitosamente.')
                continue
            
            elif nombrePaciente in lunes3:
                lunes3 = ''
                pacientesLunes = pacientesLunes.replace(nombrePaciente,'')
                if contLunes > 1:
                    contLunes -= 1 
                print('Turno cancelado exitosamente.')
                continue
            
            elif nombrePaciente in lunes4:
                lunes4 = ''
                pacientesLunes = pacientesLunes.replace(nombrePaciente,'')
                if contLunes > 1:
                    contLunes -= 1 
                print('Turno cancelado exitosamente.')
                continue
            else:
                print('El nombre del paciente no esta registrado para este dia')   


        if dia == '2':
            if f'{nombrePaciente} ' in martes1:
                martes1 = ''
                pacientesMartes = pacientesMartes.replace(nombrePaciente,'')

                if contMartes > 1:
                    contMartes -= 1
                print('Turno cancelado exitosamente.')
                continue
            elif f'{nombrePaciente} ' in martes1:
                martes1 = ''
                pacientesMartes = pacientesMartes.replace(nombrePaciente,'')
                if contMartes > 1:
                    contMartes -= 1
                print('Turno cancelado exitosamente.')
                continue
            elif f'{nombrePaciente} ' in martes1:
                martes1 = ''
                pacientesMartes = pacientesMartes.replace(nombrePaciente,'')
                if contMartes > 1:
                    contMartes -= 1
                print('Turno cancelado exitosamente.')
                continue
            else:
                print('El nombre del paciente no esta registrado para este dia')
    
    if option == '3':
        option_agenda = input('Eligió: Ver agenda del día.\n1. Lunes, 2. Martes: ')
        
        while (option_agenda != '1') and (option_agenda != '2'):
            option_agenda = input('Elija una opcion correcta\n1. Lunes, 2. Martes: ')

        #agrega (libre) a los dias lunes vacios
        if option_agenda == '1':
            lun1 = lunes1 if lunes1 != '' else 'Turno 1 - (Libre)'
            lun2 = lunes2 if lunes2 != '' else 'Turno 2 - (Libre)'
            lun3 = lunes3 if lunes3 != '' else 'Turno 3 - (Libre)'
            lun4 = lunes4 if lunes4 != '' else 'Turno 4 - (Libre)'
            print(f'\nAgenda del lunes:\n{lun1}\n{lun2}\n{lun3}\n{lun4}')

        # es lo mismo que escribir
        #if lunes1 != '':
        #    lun1 = lunes1
        #else:
        #    lun1 = 'Turno 1 - (Libre)'
        if option_agenda == '2':
            m1 = martes1 if martes1 != '' else 'Turno 1 - (Libre)'
            m2 = martes2 if martes2 != '' else 'Turno 2 - (Libre)'
            m3 = martes3 if martes3 != '' else 'Turno 3 - (Libre)'
            print(f'\nAgenda del martes:\n{m1}\n{m2}\n{m3}')
    
    if option == '4':
        print('Eligió: Ver resumen general.')

        lun1 = lunes1 if lunes1 != '' else 'Turno 1 - (Libre)'
        lun2 = lunes2 if lunes2 != '' else 'Turno 2 - (Libre)'
        lun3 = lunes3 if lunes3 != '' else 'Turno 3 - (Libre)'
        lun4 = lunes4 if lunes4 != '' else 'Turno 4 - (Libre)'
        print(f'\nAgenda del lunes:\n{lun1}\n{lun2}\n{lun3}\n{lun4}')

        m1 = martes1 if martes1 != '' else 'Turno 1 - (Libre)'
        m2 = martes2 if martes2 != '' else 'Turno 2 - (Libre)'
        m3 = martes3 if martes3 != '' else 'Turno 3 - (Libre)'
        print(f'\nAgenda del martes:\n{m1}\n{m2}\n{m3}')

        if contLunes > contMartes:
            print(f'\nDia con mas turnos: Lunes ({contLunes-1})')
        elif contLunes < contMartes:
            print(f'\nDia con mas turnos: Martes ({contMartes-1})')
        else:
            print('\nAmbos dias tienen la misma cantidad de turnos.')

    if option == '5':
        print('Eligió: Salir del programa')
        break
