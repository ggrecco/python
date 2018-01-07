f = open("surf.txt")
#maior = 0
notas = []
for linha in f:
    nome, pontos = linha.split()
    notas.append(float(pontos))
    #if float(pontos) > maior:
        #maior = float(pontos)
f.close()
#print(maior)
notas.sort(reverse = True)
print("1º - {}\n2º - {}\n3º - {}".format(notas[0],notas[1],notas[2]))
