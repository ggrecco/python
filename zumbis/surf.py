f = open("surf.txt")
for linha in f:
    print(linha.strip())#não pula linha na exibção com .strip()
f.close()
