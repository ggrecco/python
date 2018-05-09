import nmap
import os
from app.models import Servidor, Usuario
from app.scrapy import scraper
from flask_login import current_user

#site pra teste -> 'testphp.vulnweb.com'
#site pra teste -> 'scanme.nmap.org'
def portScan(site):
    a = nmap.PortScanner()
    s = str(site)
    #scaneia as portas
    d = a.scan(s,'21,22,23,25,53,63,70,79,80,110,119', '-sV')
    #Busca servidor no banco de dados
    ser = Servidor.query.filter_by(url=site, usuario_id=current_user.id)
    ip = ser.value('ip')
    nome = ser.value('nome')


    l = [21,22,23,25,53,63,70,79,80,110,119]#portas padrão que serão analisadas
    i = 0

    while i < len(l):
        j = d['scan'][ip]['tcp'][l[i]]['product']
        if j in '':
            pass
        else:
            print(j)
            scraper(j, nome)
        i = i + 1


def busca_ip(site):
    #captura apenas o campo de ip e salva em um arquivo txt
    s = str(site)
    os.system("host " + s + " | awk '{print $4}' > ip.txt")

    arq = open('/home/ggrecco/Documentos/python/flask/tcc/ip.txt', 'r')
    ip = arq.read()
    b = ip.split("\n")
    ip = b[0]

    return ip
