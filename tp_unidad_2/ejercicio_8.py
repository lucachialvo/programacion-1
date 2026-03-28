# programa 8
print('\nPrograma 8\n')

name = input('Ingrese su nombre: ')

choice = int(input('Ingrese un numero del [1-3] si quiere:\n1.Su nombre en mayusculas\n2.Su nombre en minusculas\n3.Su nombre con la primera letra en mayuscula\n>>> '))

if choice not in [1,2,3]:
    print('Elija un numero entre 1 y 3')
    exit()
elif choice == 1:
    print(name.upper())
elif choice == 2:
    print(name.lower())
else:
    print(name.title())