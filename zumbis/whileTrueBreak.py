#digitando dado para sair do loop
soma = 0
while True:
    x = int(input("Digite o número(0 sair):"))
    if x == 0:
        break
    soma = soma + x
print("Soma: {}".format(soma))
