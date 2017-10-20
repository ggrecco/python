'''
n => peças no tabuleiro
m => peças que cada pode retirar
'''
def computador_escolhe_jogada(n,m):  
    if n % (m + 1) > 0:
        return n
    else:
        

'''
    if m >= n:
        return n
    else:
        multiplo = n %(m + 1)
        if nultiplo > 0:
            return multiplo
    return m
'''

def usuario_escolhe_jogada(n,m):

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) > 0:
        
