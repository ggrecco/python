import re

padrao = re.compile(r".ato")
texto = ("Eu tenho um gato que corre de ratos,"
        "foge para o mato, aí eu pego o sapato "
        "e bato ele no ato. Ele parece um ator, "
        "atormentado.")
resultado = re.findall(padrao, texto)
print(resultado)