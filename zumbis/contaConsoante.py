#ler lista de 10 caracteres minusculos e dizer quantas consoante há.
lista = []
i = 1
while i <= 10:
    lista.append(input("Letra {}:".format(i)))
    i += 1
i = 0
contC = 0
while i < len(lista):
    if lista[i] not in 'aeiou':
        contC += 1
    i += 1
print("Consoantes: {}".format(contC))
