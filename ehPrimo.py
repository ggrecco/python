def ehPrimo(x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

n = int(input("Digite um número inteiro[0 para  sair]: "))
while n > 0:
    if ehPrimo(n):
        print("{} é Primo!".format(n))
    else:
        print("{} Não é Primo".format(n))
    n = int(input("Digite um número inteiro[0 para  sair]: "))
