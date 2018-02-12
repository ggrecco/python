def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        quantia = n % (m + 1)
        if quantia > 0:
            return quantia
        return m
 
def usuario_escolhe_jogada(n, m):
    jogada = 0
    while jogada == 0:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada > n or jogada < 1 or jogada > m:
            print("\nOops! Jogada inválida! Tente de novo.")
            jogada = 0
    return jogada
 
def partida():
    computer = True
    print(" ")
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        computer = False
        print("\nVoce começa!\n")
    
    else:
        print("\nComputador começa!\n")

    while n > 0: 
        if computer == True:
            jogada = computador_escolhe_jogada(n, m)
            computer = False
            print("Computador tirou {} peças.".format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n, m)
            computer = True
            print("Você tirou {} peças.".format(jogada))
        n = n - jogada
        print("Agora restam {} peças no tabuleiro.\n".format(n))
    if computer:
        print("Você ganhou!")
        return 1
    else:
        print("Fim de jogo! O computador ganhou!")
        return 0
 
def campeonato():
    usuario = 0
    computador = 0
    i = 1
    '''
    for _ in range(3):
        vencedor = partida()
        if vencedor == 1:
            usuario = usuario + 1
        else:
            computador = computador + 1
    '''
    while i <= 3:
        print ("\n**** Rodada {} ****".format(i))
        vencedor = partida()
        if vencedor == 1:
            usuario = usuario + 1
        else:
            computador = computador + 1
        i = i + 1
    print("\n******* Final do campeonato! *******")
    print("\nPlacar: Você  {} x {}  Computador".format(usuario, computador))

def main():
    tipo_jogo = 0
    while tipo_jogo == 0:
        print("Bem-vindo ao jogo do NIM! Escolha:")
        print(" ")
        print("1 - Para jogar uma partida isolada")
        print("2 - Para jogar um campeonato")

        tipo_jogo = int(input("Sua opção: "))
        print(" ")

        if tipo_jogo == 1:
            print("Voce escolheu partida isolada!")
            partida()
            break
        if tipo_jogo == 2:
            print("Voce escolheu um campeonato!")
            campeonato()
            break
        else:
            print("Opção inválida!")
            tipo_jogo = 0
main()
