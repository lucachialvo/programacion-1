# hecho por luca chialvo
notas = [10,2,3,9,8,6,7,9,7,5]

for i, nota in enumerate(notas, start = 1):
    print(f'Alumno {i}, Nota: {nota}')


print(f'Nota mas alta: {max(notas)}\nNota mas baja: {min(notas)}')

promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio}")