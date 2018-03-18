n = 1
soma = 0
while n <= 10:
    x = int(input("Digite o {}º número: ".format(n)))
    soma = soma + x
    n = n + 1
print("A soma é {}".format(soma))
