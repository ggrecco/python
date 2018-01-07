import urllib.request

pagina = urllib.request.urlopen("http://beans.itcarlow.ie/prices.html")
pagina2 = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")

texto = pagina.read().decode("utf8")
texto2 = pagina2.read().decode("utf8")

preco = texto[234:238]
onde = texto2.find(">$")
inicio = onde + 2
fim = inicio + 4
preco2 = texto2[inicio:fim]

print(texto)
print(preco)
print("\n",texto2)
print(preco2)
