class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo = 0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo

    def resumo(self):
        print("CC Número: {} Saldo: {}".format(self.numero, self.saldo))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def deposito(self, valor):
        self.saldo += valor
