from random import randint
print("Bem vindo!")
chute = 0
tentativas = 0
aleatorio = randint(1,100)
#não precisa ser random.randint pois foi usado from random import randint

while chute != aleatorio:
    tentativas += 1
    g = input("Chute um número: ")
    chute = int(g)
    if chute == aleatorio:
        print("Você venceu!\nCom {} tentativas!".format(tentativas))
    else:
        if chute > aleatorio:
            print("Tente um número MENOR!")
        else:
            print("Tente um número MAIOR!")    
print("Fim do jogo!")
