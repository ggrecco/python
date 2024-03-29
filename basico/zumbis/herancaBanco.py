class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo = 0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = 0
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print("CC Número: {} Saldo: {:.2f}".format(self.numero, self.saldo))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["Saque", valor])

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["Deposito", valor])

    def extrato(self):
        print("Extrato CC Nº {}".format(self.numero))
        for op in self.operacoes:
            print("{:10s} {:10.2f}".format(op[0], op[1]))
        print("{:10s} {:10.2f}\n".format("Saldo =", self.saldo))


class ContaEspecial(Conta):
    def __init__(self, clientes, numero,  saldo = 0, limite = 0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["Saque", valor])
