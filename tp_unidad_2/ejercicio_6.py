# programa 6
print('\nPrograma 6\n')
consumo = int(input('Ingrese su consumo mensual de energia en kWh: '))

if consumo < 150:
    print('Consumo bajo')
elif 150 <= consumo <= 300:
    print('Consumo medio')
elif 500 >= consumo > 300:
    print('Consumo alto')
elif consumo>500:
    print('Consumo alto. Considere medidas de ahorro energético')