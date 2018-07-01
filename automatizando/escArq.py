import os

# cria string para arquivos
print(os.path.join('usr', 'bin', 'spam') + '\n')

meusArq = ['teste.txt', 'aulas.doc', 'HUEBR.xls']

# concatenando arquivos ao final da string
for arq in meusArq:
    print(os.path.join('/home/ggrecco/Documentos', arq))

# mostra caminho completo do diretório de trabalho atual
os.getcwd()

# altera o diretório de trabalho atual
os.chdir('/home/ggrecco/Documentos/python')
