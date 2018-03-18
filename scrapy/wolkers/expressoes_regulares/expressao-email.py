import re

padrao = r'[\w.-]+@[\w.-]+'
texto = r"Meu principal e-mail é evaldowolkers@gmail.com, mas tenho também o evaldorw@hotmail.com, e o que dizer do evaldo.wolkers@algumacoisa.com.br? Este eu ainda não tenho. Que tal também o evaldo-wolkers@algo.com.br?"
match = re.findall(padrao, texto)
print(match)


"""
\w -> Caractere alfanumérico ou sublinhado [a-zA-Z0-9_]
. -> Considera o ".". Devido ao ponto, foi encontrado "evaldo.wolkers@algumacoisa.com.br", se não permitisse o ponto, seria retornado 'wolkers@algumacoisa.com.br'.
- -> Considera o "-". Devido ao hífen, foi encontrado "evaldo-wolkers@algo.com.br", se não permitisse o ponto, seria retornado 'wolkers@algo.com.br'.
+ -> Uma ou mais ocorrências da expressão anterior [\w.-]
@ -> Considera um caractere arroba.
"""