#hacer esto:
ventas = [[randint(0,10)for _ in range(7)] for _ in range(4)]

#es lo mismo que hacer:
ventas = [
   [randint(0,10)for _ in range(7)], # producto 1
   [randint(0,10)for _ in range(7)], # producto 2
   [randint(0,10)for _ in range(7)], # producto 3
   [randint(0,10)for _ in range(7)] # producto 4
]