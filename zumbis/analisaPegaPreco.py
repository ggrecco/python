from pegaPreco import pega_preco
import time

opcao = input("Deseja compar já? (S/N): ")
if opcao in "Ss":
    preco = pega_preco()
    print("Comprar! Preço: R$ {}".format(preco))
else:
    preco = 5
    while preco >= 4.74:
        preco = pega_preco()
        if preco >= 4.74:
            time.sleep(20)
    print("Comprar! Preço: R$ {:5.2f}".format(preco))
