#gerar uma lista com numeros aleatórios entre 10 e 100
import random
lista = []
for i in range(15):
    lista.append(random.randint(10,100))
print(lista)
