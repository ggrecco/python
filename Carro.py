def main():
    modelo = input("Modelo: ")
    ano = input("Ano: ")
    cor = input("Cor: ")

    carro1 = Carro(modelo,ano,cor)
    carro1.imprimir()

class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    def imprimir(self):
        print("Modelo: {}\nAno: {}\nCor: {}".format(self.modelo,self.ano,self.cor))

main()
