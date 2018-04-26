from requests import get
from app import db
from app.payload import *
from app.models import Servidor


def scraper(procura, mini = '9', maxi = ''):
    i = 0
    lista = []

    tabelas = busca_tabelas(procura, mini, maxi).findAll('tr', {'class':'srrowns'})
    coment = busca_tabelas(procura, mini, maxi).findAll('td', {'class':'cvesummarylong'})

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
            # lista.append(tipo)
            # lista.append(comentario)
            # return lista
        elif '\n' in tipo:
            tipo = tipo.split('\n')[0]
            # lista.append(tipo)
            # lista.append(comentario)
            # return lista

        lista.append(produto)
        i = i + 1

    return lista
