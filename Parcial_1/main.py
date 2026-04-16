# parcial 1 - programacion 1
# autor luca chialvo

herramientas = [] 
existencias = []

#menu interactivo
while True:
    menu_input = input('''
======= FERRETERIA "LOS CHIALVO" =======
Ingrese una opcion del menu:              
    1. Carga inicial de herramientas
    2. Cargar stock herr. existentes
    3. Ver inventario
    4. Consultar stock
    5. Reportar agotados
    6. Alta de nuevo producto
    7. Vender o reponer producto
    8. Salir                             
> ''')
    #validar que sea num y en rango correcto
    while (
        not menu_input.isdigit()
        or menu_input not in ['1','2','3','4','5','6', '7', '8']
    ):
        menu_input = input('(Error) Ingrese un numero valido: ')


    if menu_input == '1': 
        print('Carga inical de herramientas')
        stock = input('\tCantidad de herramientas a cargar: ')

        while not stock.isdigit(): 
            stock = input('\t(Error) Ingrese un numero valido: ')
        
        stock = int(stock)

        if stock == 0:
            print('\tNo se actualizará la lista de herramientas')
            _ = input("Presione Enter para continuar...")
            continue

        for i in range(1, stock+1):
            item = input(f'\t[{i}] Nombre de la herramienta: ').casefold()
            while (
                not item.isalpha() 
                or item in herramientas
            ):
                item = input('\t(Error) Ingrese un nombre valido: ').casefold()
            
            herramientas.append(item)
            existencias.append(0) #por cada item nuevo le agregas un stock inicial de 0
        
        _ = input("Inventario actualizado\nPresione Enter para continuar...")
        
    
    elif menu_input == '2': 
        if len(herramientas) == 0:
            print(f'\tDebe ingresar herramientas para continuar (actualmente hay 0 cargadas).')
            _ = input("Presione Enter para continuar...")
            continue
        
        print('Cargar stock de herramientas existentes. Si quiere omitir una carga presione Enter.')
        
        for i in range(len(herramientas)):
            stock = input(f'\tStock de {herramientas[i]}: ')
            if stock == '':
                continue
            while not stock.isdigit():
                stock = input(f'\t(Error) Ingrese un numero válido para "{herramientas[i]}": ')
            
            stock = int(stock)
            existencias[i] = stock
        
        _ = input('Stock actualizado!\nPresione Enter para continuar...')



    elif menu_input == '3':
        if len(herramientas) == 0:
            print(f'\tInventario vacío')
            _ = input('Presione Enter para continuar...')
            continue
        
        print('Seleccionó: Ver inventario\n')
        print('HERRAMIENTA\t\tSTOCK')
        for i in range(len(herramientas)):
            print(f'{herramientas[i]:.<24}{existencias[i]:.>1}')

        _ = input('\nPresione Enter para continuar...')



    elif menu_input == '4':
        busqueda = input('Ingrese el nombre del item para buscar su stock\nBuscar: ').casefold()
        if busqueda not in herramientas:
            _ = input('\tNo se encontró el producto\nPresione Enter para continuar...')
            continue
        else:
            i = herramientas.index(busqueda)
            print('\nHERRAMIENTA\t\tSTOCK')
            print(f'{herramientas[i]:.<24}{existencias[i]:.>1}')
            _ = input('\nPresione Enter para continuar...')


    elif menu_input == '5':

        print('LISTA DE PRODUCTOS AGOTADOS:')
        for i in range(len(herramientas)):
            if existencias[i] == 0:
                print(f'{herramientas[i]}')
            else:
                pass
        _ = input("\nPresione Enter para continuar...")


    elif menu_input == '6':
        print('\nAgregar una producto al inventario')
        
        nuevo_item = input('\tNombre de la herramienta: ').casefold()
        if (
            not nuevo_item.isalpha()
            or nuevo_item in herramientas
        ):
            print('\tProducto ya existente')
            _ = input("Presione Enter para continuar...")
            continue
        
        stock_nuevo_item = input('\tStock: ')
        while (
            not stock_nuevo_item.isdigit()
        ):
            stock_nuevo_item = input('\t(Error) Stock: ')
        
        stock_nuevo_item = int(stock_nuevo_item)
        herramientas.append(nuevo_item)
        existencias.append(stock_nuevo_item)
        _ = input('\tHerramienta agregada al inventario\nPresione Enter para continuar...')


    elif menu_input == '7':
        menu_input = input('Seleccione una opcion:\n1. Realizar venta\n2. Reponer producto\n> ')
        while (
            not menu_input.isdigit()
            or not menu_input in ['1','2']
        ):
            menu_input = input('(Error) > ')
        
        if menu_input == '1':
            print('Venta')
            
            item = input('\tProducto a vender: ').casefold()
            if item not in herramientas:
                _ = input(f'\tEl producto "{item}" no existe\n\tPresione Enter para continuar...')
                continue
            
            stock = input('\tCantidad a vender: ')
            while not stock.isdigit():
                _ = input(f'\t(Error) Ingrese un valor valido: ')


            stock = int(stock)
            if stock > existencias[herramientas.index(item)]:
                 _ = input(f'\tStock insuficiente\n\tPresione Enter para continuar...')
                 continue
            else:
                existencias[herramientas.index(item)] -= stock
                print(f'\tSe vendió {stock}: {item}\n\tRestantes: {existencias[herramientas.index(item)]}')
                _ = input(f'\tPresione Enter para continuar...')

            
        else:
            print('Reponer producto')
            
            item = input('\tNombre de la herramienta: ')
            if item not in herramientas:
                _ = input(f'\tEl producto "{item}" no existe\nPresione Enter para continuar...')
                continue
            
            stock = input('\tCantidad a stockear: ')
            while not stock.isdigit():
                _ = input(f'\t(Error) Ingrese un valor valido: ')


            stock = int(stock)
            existencias[herramientas.index(item)] += stock
            print(f'Se agregó {stock}: {item}\n\tStock actualizado: {existencias[herramientas.index(item)]}')


    else:
        print('Programa finalizado')
        break