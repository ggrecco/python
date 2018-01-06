from bancoSimples import Cliente
from bancoSimples import Conta

joao = Cliente("Joao da silva", "777-1234")
maria = Cliente("Maria da silva", "555-4321")
print("Nome: {} Telefone: {}".format(maria.nome, maria.telefone))
print("Nome: {} Telefone: {}".format(joao.nome, joao.telefone))

conta1 = Conta([joao],1,1000)
conta2 = Conta([maria, joao],2,2000)
conta1.resumo()
conta2.resumo()
