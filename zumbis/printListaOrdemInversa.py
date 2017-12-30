#leia uma lista de 10 elementos reais e mostre na ordem inversa
lista = [1,2,3,4,5,6,7,8,9,0]
lista2 = []
n = 9
while n >= 0:
    lista2.append(lista[n])
    n -= 1
print(lista," - ",lista2)
