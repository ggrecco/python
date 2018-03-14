from urllib.request import urlopen
from bs4 import BeautifulSoup


lista = []
lista2 = []


html = urlopen('file:///home/grecco/Documentos/Python/scrapy/brincando/retorno_java.html')

bsobj = BeautifulSoup(html, "html.parser")

teste = bsobj.findAll("", {"class":"cvssbox"})
teste2 = bsobj.findAll("", {"class":"cvesummarylong"})


for a in teste:
    lista.append(a.string)

for b in teste2:
    lista2.append(b.string)

dic = list(zip(lista, lista2))


#print(d)
print(dic)
