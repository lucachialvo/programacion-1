# hecho por luca chialvo
import random

ampTermica, promedioPorDia = [], []
#matriz de datos
clima = [   ["Lun","Mar", "Mie", "Jue", "Vie", "Sab", "Dom"],
            [random.randint(20,30) for _ in range(7)],  # temperatura max
            [random.randint(5,15) for _ in range(7)]]   # temperatura min


for i in range(7):
    ampTermica.append(clima[1][i] - clima[2][i]) # array de las amplitudes termicas
    promedioPorDia.append(( clima[1][i] + clima[2][i] ) /2)

avg_maxima = round(sum(clima[1]) /7, 1)
avg_minima = round(sum(clima[2]) /7, 1)
#(Podrian haber varios dias con la misma amplitud termica pero como son nros random es muy raro)
diaMayorAmpTermica = ampTermica.index(max(ampTermica))

# tabla
print("Dia\tMax\tMin\tDif\tProm")
for i in range(7):
    print(f"{clima[0][i]}\t{clima[1][i]}\t{clima[2][i]}\t{ampTermica[i]}\t{promedioPorDia[i]}")

print("-"*30)
print(f"Promedio de las maximas: {avg_maxima}")
print(f"Promedio de las minimas: {avg_minima}")

print(f"Dia de mayor amplitud termica: {clima[0][diaMayorAmpTermica]}")