import ordenador_bolha
import random
import time

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        #for i in range(n):
            #lista[i] = random.randrange(1000)# inteiros entre 0 e 999
        return lista

    def lista_quase_ordenada(self, n):
        

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:] #clona lista 1

        o = ordenador_bolha.Ordenador()
        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Bolha demorou {}".format(depois - antes))

        o = ordenador_bolha.Ordenador()
        antes2 = time.time()
        o.selecao_direta(lista2)
        depois2 = time.time()
        print("Seleção direta demorou {}".format(depois2))
