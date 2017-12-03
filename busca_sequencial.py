class Musica:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

class Buscador:
    def busca_por_titulo(self, lista, titulo):
        for i in range(len(lista)):
            if lista[i].titulo == titulo:
                return i
        return -1

    def vamos_buscar(self):
        lista = [Musica("teste",2017), Musica("teste2",1988),Musica("teste3",1999),
                 Musica("teste4",2016),Musica("Teste",2017),Musica("TESTE",2017)]

        onde_achou = self.busca_por_titulo(lista,"teste")

        if onde_achou == -1:
            print("Não existe")
        else:
            busca = lista[onde_achou]
            print(busca.titulo, busca.ano, sep = ", ")

