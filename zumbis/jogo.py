print("Bem vindo!")
chute = 0
while chute != 42:
    g = input("Chute um número: ")
    chute = int(g)
    if chute == 42:
        print("Você venceu!")
    else:
        if chute > 42:
            print("Tente um número MENOR!")
        else:
            print("Tente um número MAIOR!")
print("Fim do jogo!")
