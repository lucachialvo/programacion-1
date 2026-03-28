# programa 9
print('\nPrograma 9\n')
magnitud = float(input('Indique la magnitud del terremoto segun la escala de Ritcher (numero): '))
if magnitud < 3:
    print('"Muy leve" (imperceptible)')
elif 3 <= magnitud < 4:
    print('"Leve" (ligeramente perceptible)')
elif 4 <= magnitud < 5:
    print('Moderado" (sentido por personas, pero generalmente no causa daños)')
elif 5 <= magnitud < 6:
    print('"Fuerte" (puede causar daños en estructuras débiles)')
elif 6 <= magnitud < 7:
    print('"Muy Fuerte" (puede causar daños significativos)')
elif magnitud >= 7:
    print('"Extremo" (puede causar graves daños a gran escala)')