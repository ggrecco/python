import urllib.request
preco = 99.99
while preco > 4.74:
    pagina = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    texto = pagina.read().decode("utf8")
    onde = texto.find(">$")
    inicio = onde + 2
    fim = inicio + 4
    preco = float(texto[inicio:fim])
print("Comprar! Preço: {:5.2f}".format(preco))
