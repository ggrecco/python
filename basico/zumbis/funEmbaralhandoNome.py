#função que retorna as letras de uma string misturadas
import random

def embaralha(x):
    lista = list(x)
    random.shuffle(lista)
    return ''.join(lista)
