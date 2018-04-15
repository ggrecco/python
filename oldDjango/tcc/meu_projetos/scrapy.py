from requests import get
from .payload import *
from .models import Servidor

def scrapy(procura):
    i = 0

    tabelas = busca_tabelas(procura).findAll('tr', {'class':'srrowns'})
    coment = busca_tabelas(procura).findAll('td', {'class':'cvesummarylong'})

    while i < len(tabelas):
        coluna = tabelas[i].find_all('td')
        produto = coluna[2].text
        cveid = coluna[3].text
        tipo = coluna[6].text
        datacorrecao = coluna[8].text
        nota = coluna[9].text
        acesso = coluna[10].text
        comentario = coment[i].text.split('\t')[6]
        if '\n\t' in tipo:
            tipo = tipo.split('\t')[6]
            # db.inserir(produto,cveid, tipo, datacorrecao, nota, acesso, comentario)
        elif '\n' in tipo:
            tipo = tipo.split('\n')[0]
            # db.inserir(produto,cveid, tipo, datacorrecao, nota, acesso, comentario)
        i = i + 1
