# programa 7
print('\nPrograma 7\n')

oracion = input('Ingrese una frase o palabra: ')
vocales = ('A','a','E','e','I','i','O','o','U','u')

if oracion.endswith(vocales):
    print(f'{oracion}!')
else:
    print(oracion)