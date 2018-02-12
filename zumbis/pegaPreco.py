import urllib.request

def pega_preco():
    pagina = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    texto = pagina.read().decode("utf8")
    onde = texto.find(">$")
    inicio = onde + 2
    fim = inicio + 4
    return float(texto[inicio:fim])
