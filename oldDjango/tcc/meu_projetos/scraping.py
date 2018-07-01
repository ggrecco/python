from requests import get
from .payload import *
from .models import Servidor, Entrada

def scrapy(procura):
    i = 0

    tabelas = busca_tabelas(procura).findAll('tr', {'class':'srrowns'})
    coment = busca_tabelas(procura).findAll('td', {'class':'cvesummarylong'})

    servidor = Servidor.objects.all()#captura objetos do servidor

    #define o id da última entrada do servidor
    for i in servidor:
        id_servidor = i.id

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
            e = Entrada(produto=produto, cveid=cveid, tipo=tipo, dataCorrecao=datacorrecao, nota=nota, tipoAcesso=acesso, comentario=comentario,servidor_id=id_servidor)
            e.save()
            print(produto,cveid, tipo, datacorrecao, nota, acesso, comentario, servidor_id)
        elif '\n' in tipo:
            tipo = tipo.split('\n')[0]
            # db.inserir(produto,cveid, tipo, datacorrecao, nota, acesso, comentario)
            e = Entrada(produto=produto, cveid=cveid, tipo=tipo, dataCorrecao=datacorrecao, nota=nota, tipoAcesso=acesso, comentario=comentario, servidor_id=id_servidor)
            e.save()
            print(produto,cveid, tipo, datacorrecao, nota, acesso, comentario, servidor_id)
        i = i + 1
