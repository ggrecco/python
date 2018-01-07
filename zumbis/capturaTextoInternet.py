import urllib.request
pagina = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
texto = pagina.read().decode("utf8")
preco = texto[234:238]
print(texto)
print(preco)
