'''
arquivo = open("numeros.txt", "r")
for linha in arquivo.readlines():
    print(linha.rstrip())
arquivo.close()
'''
with open("numeros.txt") as f:
    print(f.read())
