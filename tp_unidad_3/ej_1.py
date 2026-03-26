salida = ''
totalSinDto = 0
totalConDto = 0

#pide y valida el nombre
cliente = input('Cliente: ')
while cliente.isalpha() == False or cliente == '':
    cliente = input('Cliente: ')

#pide y valida la cant. de productos
cantidadProd = input('Cantidad de productos a comprar: ')
while cantidadProd.isdigit() == False or int(cantidadProd) <= 0:
    cantidadProd = input('Cantidad de productos a comprar: ')
cantidadProd = int(cantidadProd)

for i in range(1,cantidadProd+1):
    #precio
    precio = input(f'Precio del producto {i}: ')
    while precio.isdigit() == False:
        precio = input(f'Precio del producto {i}: ')
    precio = int(precio)
    
    # descuento?
    dto = input('Descuento (s/n): ').lower()
    while dto != 's' and dto != 'n':
        dto = input('Descuento (s/n): ').lower()
    
    #calcular todo
    totalSinDto += precio
    if dto == 's':
        totalConDto += (precio - precio * 0.1)
    else:
        totalConDto += precio
    
    salida += f'Producto {i} - Precio: {precio} Descuento (S/N): {dto}\n'

ahorro = totalSinDto - totalConDto
promedio = float(totalSinDto/i)

print('--------------------------------------------------------')
print(f'Cliente: {cliente.capitalize()}\nCantidad de productos: {cantidadProd}')
print(f'{salida}')
print(f'Total sin descuentos: ${totalSinDto}\nTotal con descuentos: ${totalConDto:.2f}\nAhorro: ${ahorro}\nPromedio por producto: ${promedio:.2f}')