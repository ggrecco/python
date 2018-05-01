from requests import get
from app import db
from app.payload import *
from app.models import Dados, Servidor, Usuario
from flask_login import current_user

#passar por parametro o id do usuario
def scraper(procura, mini = '9', maxi = ''):
    i = 0
    lista = []
    u = Usuario.query.filter_by(id=current_user.id).first()

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
            d = Dados(autor_usuario=u, produto=produto, cveid=cveid, tipo=tipo, datacorrecao=datacorrecao, nota=nota, acesso=acesso, comentario=comentario)
            db.session.add(d)
            db.session.commit()

        elif '\n' in tipo:
            tipo = tipo.split('\n')[0]
            d = Dados(autor_usuario=u, produto=produto, cveid=cveid, tipo=tipo, datacorrecao=datacorrecao, nota=nota, acesso=acesso, comentario=comentario)
            db.session.add(d)
            db.session.commit()

        lista.append(produto)
        i = i + 1

    return lista
# produto=, cveid=, tipo=, datacorrecao=, nota=, acesso= , comentario=
