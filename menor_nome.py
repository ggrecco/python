def menor_nome(nomes):
    menor = 0
    maior = 0
    p = ''
    lista = []
    for i in range(len(nomes)):
        lista.append(nomes[i].strip())

    for i in range(len(lista)):
        a = len(lista[i])
        if i == 0:
            menor = a
            p = lista[i]
        else:
            if a < menor:
                menor = a
                p = lista[i]
                
    print(a)
    print(menor)
    print(p.capitalize())

