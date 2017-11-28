def maior_primo(k):
    cont = 2
    while (cont <= k):
        i = cont - 1
        while i > 1:
            if cont % i == 0: break
            i -=1
        else:
            g = cont
        cont += 1
    return g
