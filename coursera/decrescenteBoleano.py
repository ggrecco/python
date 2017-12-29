decrescente = True
anterior = int(input("Digite o pirmeiro número da sequência: "))
valor = 1
while valor != 0 and decrescente:
    valor = int(input("Digite o próximo número da sequência: "))
    if valor > anterior:
        decrescente = False
    anterior = valor
if decrescente == True:
    print("A sequencia está em ordem descrescente!")
else:
    print("A sequencia NÃO está em ordem descrescente!")
