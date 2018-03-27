import datetime
class Pessoa():
    def __init__(self, nome,nascimento):
        self.nome = nome
        self.nascimento = nascimento
    def idade(self):
        delta = datetime.date.today() - self.nascimento
        return int (delta.days/365)
    def __str__(self):
        return "{}, {} anos".format(self.nome, self.idade())

nome = input("Nome: ")
nascimento = input("Nascimento:")
nascimento = nascimento.split("/")
pessoa = Pessoa(nome, datetime.date(int(nascimento[2]), int(nascimento[1]), int(nascimento[0])))
grecco = Pessoa("Gustavo Grecco", datetime.date(1985, 9, 1))
print(grecco.idade())
print(grecco)
print(pessoa)
