'''
Escreva a função ordenada(lista), que recebe uma lista com números inteiros
como parâmetro e devolve o booleano True se a lista estiver ordenada e
False se a lista não estiver ordenada.
'''
def ordenada(lista):
    posicao_do_menor = 0
    fim = len(lista)

    for i in range(fim - 1):
        posicao_do_menor = i

    for j in range(i + 1, fim):
        if lista[j] < lista[posicao_do_menor]:
            posicao_do_menor = j

    if lista[i] == lista[posicao_do_menor]:
        return True
    else:
        return False

