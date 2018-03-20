from requests import get
from payload import *
from dml import *

db = Cvedetails()
i = 0

tabelas = busca_tabelas().findAll('tr', {'class':'srrowns'})
coment = busca_tabelas().findAll('td', {'class':'cvesummarylong'})

while i < len(tabelas):
    coluna = tabelas[i].find_all('td')
    cveid = coluna[3].text
    tipo = coluna[6].text
    datacorrecao = coluna[8].text
    nota = coluna[9].text
    acesso = coluna[10].text
    comentario = coment[i].text.split('\t')[6]
    if '\n\t' in tipo:
        tipo = tipo.split('\t')[6]
        db.inserir(cveid, tipo, datacorrecao, nota, acesso, comentario)
    elif '\n' in tipo:
        tipo = tipo.split('\n')[0]
        db.inserir(cveid, tipo, datacorrecao, nota, acesso, comentario)
    i = i + 1



'''
d = []
f = []
g = []
i = 0

captura = Cvedetails()

tabelas = busca_tabelas().findAll('tr', {'class':'srrowns'})
coment = busca_tabelas().findAll('td', {'class':'cvesummarylong'})

while i < len(tabelas):
    #f.append(tabelas[i].find_all('td')[9].text)

    app = tabelas[i].find_all('td')[3].text,tabelas[i].find_all('td')[6].text.split('\t')[6],tabelas[i].find_all('td')[8].text,tabelas[i].find_all('td')[9].text,tabelas[i].find_all('td')[10].text
    f.append(app)
    g.append(coment[i].text.split('\t')[6])
    c = (f[i], g[i])
    d.append(c)
    captura.inserir(f[i], g[i])
    i = i + 1
'''
'''
#captura cev id (cevid)
tabelas[i].find_all('td')[3].text

#captura vulnerability type(tipo)
tabelas[i].find_all('td')[6].text.split('\t')[6]

#captura updae date(datacorrecao)
tabelas[i].find_all('td')[8].text

#captura gained acess level(acesso)
tabelas[i].find_all('td')[10].text


(tabelas[i].find_all('td')[3].text, tabelas[i].find_all('td')[6].text.split('\t')[6],tabelas[i].find_all('td')[8].text,tabelas[i].find_all('td')[9].text,tabelas[i].find_all('td')[10].text )
'''
