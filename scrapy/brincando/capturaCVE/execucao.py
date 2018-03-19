from requests import get
from payload import *
from captura import *

d = []
f = []
g = []
i = 0

captura = Captura()

tabelas = busca_tabelas().findAll('tr', {'class':'srrowns'})
coment = busca_tabelas().findAll('td', {'class':'cvesummarylong'})

#a = tabelas
#b = coment
'''
while i < len(tabelas):
    f.append(tabelas[i].find_all('td')[9].text)
    #f.append(a[i].find_all('td')[9].text)
    g.append(coment[i].text.split('\t')[6])
    #g.append(b[i].text.split('\t')[6])
    c = (f[i], g[i])
    d.append(c)
    captura.inserir(f[i], g[i])
    i = i + 1
'''
