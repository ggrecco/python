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

    def bolha(self, lista):
        fim = len(lista)

        for i in range(fim - 1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

        def bolha_curta(self, lista):
            fim = len(lista)

            for i in range(fim - 1, 0, -1):
                trocou = False
                for j in range(i):
                    if lista[j] > lista[j+1]:
                        lista[j], lista[j+1] = lista[j+1], lista[j]
                        trocou = True
                if not trocou:
                    return
