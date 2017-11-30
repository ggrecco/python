'''
Escreva a função maiusculas(frase) que recebe uma frase (uma string)
como parâmetro e devolve uma string com as letras maiúsculas que
existem nesta frase, na ordem em que elas aparecem.
'''
def maiusculas(frase):
    lista = []
    for x in frase:
        c = ord(x)
        if c >= 65 and c <= 90:
            lista.append(chr(c))
    a = ''.join(lista)
    print(a)


'''
    print(string.ascii_lowercase)
    print(letra.ascii_uppercase)

    p = "Jon Snow"
for x in p:
  c = ord(x)
  if c >= 65 and c <= 90:
    print("Maiscula encontrada")
'''
