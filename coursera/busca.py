class Buscador:
    def busca_sequencial(self,lista, x):
        #(list, float) -> bool
        for i in range(len(lista)):
            if lista[i] == x:
                return True
            return False
    def busca_binaria(self, lista, x):
        primeiro = 0 #Primeiro indice da lista
        ultimo = len(lista) - 1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2 # para selecionar a parte inteiro da divisão
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio -1
                else:
                    primeiro = meio + 1
        return -1
