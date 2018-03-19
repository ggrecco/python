from requests import get
from bs4 import BeautifulSoup as bs
from captura import *


url = 'https://www.cvedetails.com/vulnerability-search.php?f=1&vendor=&product=php&cveid=&msid=&bidno=&cweid=&cvssscoremin=&cvssscoremax=&psy=&psm=&pey=&pem=&usy=&usm=&uey=&uem='

request = get(url)
#a = []
#b = []
d = []
f = []
g = []
i = 0

captura = Captura()

pagina = bs(request.content, 'lxml')
tabelas = pagina.findAll('tr', {'class':'srrowns'})
coment = pagina.findAll('td', {'class':'cvesummarylong'})

#a = tabelas
#b = coment

while i < len(tabelas):
    f.append(tabelas[i].find_all('td')[9].text)
    #f.append(a[i].find_all('td')[9].text)
    g.append(coment[i].text.split('\t')[6])
    #g.append(b[i].text.split('\t')[6])
    c = (f[i], g[i])
    d.append(c)
    captura.inserir(f[i], g[i])
    i = i + 1
