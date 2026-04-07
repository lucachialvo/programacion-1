import random

notas = [
    [f"Alumno {i}" for i in range(5)], #nombres
    [random.randint(1,10) for _ in range(5)], #materia 1
    [random.randint(1,10) for _ in range(5)], # materia 2
    [random.randint(1,10) for _ in range(5)] # materia 3
]

promMateria = []
print(notas)
print("Nombre\t\tO.E\tAySO\tP1\tProm")

for i in range(5):
    notasMateria = [notas[x][i] for x in range(1,4)]
    promAlumno = sum(notasMateria) / len(notasMateria)
    print(f"{notas[0][i]}\t{notas[1][i]}\t{notas[2][i]}\t{notas[3][i]}\t{promAlumno:.2f}")

for i in range(1,len(notas)):
    promMateria.append(sum(notas[i])/(len(notas[1])))

print(f"Prom. materia:", end="")

for i in range(len(promMateria)):
    print(f"\t{promMateria[i]}", end="")
