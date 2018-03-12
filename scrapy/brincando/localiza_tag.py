from urllib.request import urlopen
from bs4 import BeautifulSoup


lista = []
lista2 = []


html = urlopen('file:///home/grecco/Documentos/Python/scrapy/brincando/retorno_java.html')

bsobj = BeautifulSoup(html, "html.parser")

teste = bsobj.findAll("", {"class":"cvssbox"})
teste2 = bsobj.findAll("", {"class":"cvesummarylong"})

print(len(teste))
print(len(teste2))


for a in teste:
    lista.append(a.string)

for b in teste2:
    lista2.append(b.string)

d = list(zip(teste, teste2))
dic = dict(zip(lista, lista2))


print(d)
print(dic)
'''
for i in lista:
    for j in lista2:
        if j in m:

        dic[i] = j
        break

for m in lista:
    for p in lista2:
        if p in m:
            key = m
            dic[key] = []
            break
    if m != key:
        dic[key].append(m)

print(dic)
#print(lista)
#print(lista2)
'''
