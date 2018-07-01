import os

total = 0

caminho = input('Insira o caminho da pasta: ')

for arq in os.listdir(caminho):
    total = total + os.path.getsize(os.path.join(caminho, arq))

print('O diretório possui {} bytes.'.format(total))
