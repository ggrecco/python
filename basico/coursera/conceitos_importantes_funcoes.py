'''
retorna 2 valores para ser atribuido no formato:
a,b = função()
a = 1º retorno
b = 2º retorno
'''
def peso_altura():
    return 80, 1.69



'''
função para atribuir valor ao parametro
caso usuário não informe nenhum valor
sempre deverá ser o último parametro
'''
def pagamento_semanal(valor_hora, num_hora = 40):
    return valor_hora * num_hora


'''
comando assert para determinar se uma função pode executar ou não.
retorna uma mensagem de erro
'''
def horas(m):
    assert m > 0
    return m * 60






