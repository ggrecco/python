import re

texto = "Meu principal e-mail é evaldowolkers@gmail.com, mas tenho também o evaldorw@hotmail.com, e o que dizer do evaldo.wolkers@algumacoisa.com.br? Este eu ainda não tenho. Que tal também o evaldo-wolkers@algo.com.br? .@.  ...@..."

# Encontrando um conjunto de caracteres (a-zA-z0-9), seguido de arroba e outro conjunto de caracteres
match = re.findall(r'[\w]+@[\w]+', texto)
print(match)
#['evaldowolkers@gmail', 'evaldorw@hotmail', 'wolkers@algumacoisa', 'wolkers@algo']

# Encontrando pontos, arroba e pontos, literalmente (várias ocorrências de ponto)
match = re.findall(r'[\.]+@[\.]+', texto)
print(match)
# ['.@.', '...@...']

# Encontrando qualquer caracter (ponto como coringa), várias ocorrências, seguido de arroba e qualquer caracter, várias ocorrências
match = re.findall('.+@.+', texto)
print(match)
#['Meu principal e-mail é evaldowolkers@gmail.com, mas tenho também o evaldorw@hotmail.com, e o que dizer do evaldo.wolkers@algumacoisa.com.br? Este eu ainda não tenho. Que tal também o evaldo-wolkers@algo.com.br? .@.  ...@...']

# Encontrando qualquer caracter (ponto como coringa), várias ocorrências, seguido de arroba e qualquer caracter, várias ocorrências
match = re.findall('.@.', texto)
print(match)
#['s@g', 'w@h', 's@a', 's@a', '.@.', '.@.']

# Encontrando arrobas e pontos, caracteres informados entre chaves
match = re.findall('[.@.]', texto)
print(match)
#['@', '.', '@', '.', '.', '@', '.', '.', '.', '@', '.', '.', '.', '@', '.', '.', '.', '.', '@', '.', '.', '.']

