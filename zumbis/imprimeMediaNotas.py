#Ler 4 notas e mostrar as notas e a média na tela
i = 1
soma = 0
lista = []
while i <= 4:
    n = float(input("Nota {}: ".format(i)))
    soma += n
    lista.append(n)
    i += 1
print("Notas: {}\nMédia: {}".format(lista,soma/i))
