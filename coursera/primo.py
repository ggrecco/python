n = int(input("Digite um número inteiro: "))
cont = 2
primo = True
while (cont < n and primo):
    primo = not ((n % cont) == 0)
    cont += 1
if (primo):
    print("primo")
else:
    print("não primo")
