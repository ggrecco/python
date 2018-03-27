#usuário informa os dados e mostra a lista na tela
lista = []
i = int(input("Tamanho da lista: "))
n = 0
while n < i:
    x = str(input("Elemento {} da lista: ".format(n+1)))
    lista.append(x)
    n += 1
print("A lista contém:",lista)
