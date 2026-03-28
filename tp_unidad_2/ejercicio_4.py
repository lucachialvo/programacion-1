# programa 4:
print('\nPrograma 4\n')

edad = int(input('Ingrese su edad'))
if edad < 12:
    print('Niño')
elif 12 <= edad < 18:
    print('Adolescente')
elif 18 <= edad < 30:
    print('Adulto/a joven')
elif edad >= 30:
    print('Adulto/a')
else:
    print('Edad no valida') 