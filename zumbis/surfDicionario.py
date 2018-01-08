f = open("surf.txt")
notas = {}
for linhas in f:
    nome, pontos = linhas.split()
    notas[float(pontos)] = nome
f.close()
for nota in sorted(notas, reverse = True):
    print("{} tem nota {:4.2f}".format(notas[nota], nota))
