#ler uma palavra e trocar as vogais por "*"
i = 0

troca = ""
palavra = input("Palavra: ")
j = input("Letra: ")
t = input("trocar por: ")
while i < len(palavra):
    if palavra[i] in str(j):
        troca += t
    else:
        troca += palavra[i]
    i += 1

print("Nova: {}\nAntiga:{}".format(troca,palavra))
