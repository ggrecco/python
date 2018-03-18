import re

padrao = re.compile(r".ato")
padrao2 = re.compile(r".ato", re.I)
texto = ("Eu tenho um Gato que corre de RATO,"
        "foge para o MATO, aí eu pego o sapato "
        "e bato ele no ato.")
resultado = re.findall(padrao, texto)
print("Sem IGNORECASE:", resultado)
resultado = re.findall(padrao2, texto)
print("Com IGNORECASE:", resultado)