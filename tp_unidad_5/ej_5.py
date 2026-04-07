# hecho por luca chialvo

students = ["Luca", "Joaquin", "Marcos", "Cadela", "Mia","Victoria", "Benjamin", "Ruben"]

print("LISTA DE ESTUDIANTES:")
for i in range(len(students)):
    print(f"{students[i]}")

option = input("\nSeleccione una opcion: 1. Agregar un estudiante 2. Eliminar un estudiante\n> ")

while option.isdigit() == False or option not in ("1","2"):
    option = input("Seleccione una opcion correcta (1 o 2): ")

if option == "1":
    new_student = input("Nombre del estudiante a agregar: ")
    students.append(new_student)
else:
    del_student = input("Nombre del estudiante a quitar: ")
    
    while del_student not in students:
        del_student = input("Nombre del estudiante a quitar: ")
        
    students.remove(del_student)
    

print("LISTA DE ESTUDIANTES:")
for i in range(len(students)):
    print(f"{students[i]}")

