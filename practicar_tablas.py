# test de tablas de multiplicar:
from random import randint

a = randint(2,16)
b = randint(2,16) 
respuesta = int(input(f"{a} x {b} = "))

while respuesta != "":
    a = randint(2,16)
    b = randint(2,16) 
    pregunta = a*b
    respuesta = int(input(f"{a} x {b} = "))
    if respuesta == pregunta:
        pass
    else:
        print(f"INCORRECTO! es {pregunta}")