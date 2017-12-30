#solicita data de nascimento e imprime nome do mês por extenso
lista = ["Janeiro", "Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembo","Outubro","Novembro","Dezembro"]
nascimento = input("Nascimento: ")
nascimento = nascimento.split("/")
nascimento[1] = lista[int(nascimento[1]) - 1]
nascimento = ' de '.join(nascimento)
print(nascimento)
