import re

padrao = re.compile(r".ato")

texto = ("Eu tenho um Gato que corre de RATO,"
        "foge para o MATO, aí eu pego o sapato "
        "e bato ele no ato.")
resultado = re.search(padrao, texto)
print(resultado)

texto = ("Eu tenho um Gato que corre de RATO,"
        "foge para o MATO, aí eu pego o sapato "
        "e bato ele no ato.")
resultado = re.match(padrao, texto)
print(resultado)

texto = ("Gato que corre de RATO,"
        "foge para o MATO, aí eu pego o sapato "
        "e bato ele no ato.")
resultado = re.match(padrao, texto)
print(resultado)