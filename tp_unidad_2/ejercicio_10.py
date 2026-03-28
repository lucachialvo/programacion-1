#programa 10
print('\nPrograma 10\n')

hemisferio = input('Ingrese si es del hemisferio sur o norte (S/N)\n>>> ').upper()

if hemisferio not in ['S', 'N']:
    print('No ingresó correctamente el hemisferio')

fecha = input('Ingresar la fecha con el formato dia/mes usando numeros. Por ejemplo: 23/11\n>>> ').split('/')

if len(fecha) > 2 or len(fecha) == 0:
    print('Mal formato de fecha, solo ingresar dos valores')


#diccionario que crea el par "clave:"valor" -> num. del mes: rango de dias del mes, si el input no coincide con el numero de meses o el numero de dias del mes, hay error
calendario = {
1:range(1,32),
2:range(1,29),
3:range(1,32),
4:range(1,31),
5:range(1,32),
6:range(1,31),
7:range(1,32),
8:range(1,32),
9:range(1,31),
10:range(1,32),
11:range(1,31),
12:range(1,32)
}

calendario_dias = {
# mes : dia del año que corresponde al primer dia de ese mes
1:1,
2:32,
3:60,
4:91,
5:121,
6:152,
7:182,
8:213,
9:244,
10:274,
11:305,
12:335
}

dia = int(fecha[0]) 
mes = int(fecha[1])

#comprobas que los dia/mes coincidan con los valores del diccionario
if mes not in calendario:
    print(f'No existe el mes {mes} del año.')

elif dia not in calendario[mes]:
    print(f'No existe el dia {dia} del mes {mes}.')
else:
    #basicamente si la fecha es 5/4, el mes 5 empieza en el dia 121, le sumas el dia en el q estas (+5) y le restas uno
    # = 121 + 5 - 1 = dia 125 del año
    diaAnual = calendario_dias[mes] + dia - 1 
    
    #rama del hemisferio sur
    if hemisferio == 'S':
        #21/12= dia 355 - 20/3= dia 79 y asi, voy comprobando segun el rango de dias
        if diaAnual >= 355 or diaAnual <= 79: 
            print('Verano')
        elif 80 <= diaAnual <= 171:
            print('Otoño')
        elif 172 <= diaAnual <= 263:
            print('Invierno')
        elif 264 <= diaAnual <= 354:
            print('Primavera')

    #rama del hemisferio norte
    else:
        if diaAnual >= 355 or diaAnual <= 79:
            print('Invierno')
        elif 80 <= diaAnual <= 171:
            print('Primavera')
        elif 172 <= diaAnual <= 263:
            print('Verano')
        elif 264 <= diaAnual <= 354:
            print('Otoño')