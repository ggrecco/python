laco = 1
while laco != 0:
    numero = int(input("Digite um número[0 para sair]: "))
    contador = 1
    fatorial = 1
    while contador <= numero:
        fatorial = fatorial * contador
        contador = contador + 1
    print(fatorial)
    laco = numero
