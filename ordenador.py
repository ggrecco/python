class Ordenador:
    def selecao_direta(self, lista):
        fim = len(lista)

        for i in range(fim - 1):
            posicao_do_menor = i

        for j in range(i + 1, fim):
            if lista[j] < lista[posicao_do_menor]:
                posicao_do_menor = j

        #reordenando a lista
        lista[i], lista[posicao_do_menor] = lista[posicao_do_menor], lista[i]

'''
>>>lista = [0,15,-10,30,546,11,2,3,48561,20]
>>>a.selecao_direta(lista)
>>>lista
[0, 15, -10, 30, 546, 11, 2, 3, 20, 48561]
'''
