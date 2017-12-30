#gerar uma lista com numeros aleatórios entre 10 e 100
import random
lista = []
while len(lista) < 15:
    x = random.randint(10,100)
    if x not in lista:
        lista.append(x)
lista.sort()
print(lista)
