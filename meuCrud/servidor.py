from bottle import route, run, request, response, post, get, template, static_file
from dml import *

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')


@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def imagens(filename):
    return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)')
def fonts(filename):
    return static_file(filename, root='static/fonts')
#---------------------------------------------------------
@route('/')
def home_page():
    return template('index')

@post('/inserir')
def create():
    nome = request.forms.get('nome')
    telefone = request.forms.get('telefone')
    db_insert(nome, telefone)
    return template('verifica.html', sucesso = True, acao = "foi cadastrado(a)", nome = nome)

@post('/deletar')
def delete():
    nome = str(request.forms.get('delete'))
    db_delete(nome)
    return template('verifica.html', sucesso = True, acao = "foi excluido(a) ", nome = nome)

@post('/editar')
def update():
    nome = str(request.forms.get('nome'))
    novo = str(request.forms.get('telefone'))
    db_update(novo, nome)
    return template('verifica.html', sucesso = True, acao = "foi alterado(a) ", nome = nome)

@post('/ler')
def read():
    result = str(request.forms.get('dado'))
    resultado = db_select(result)
    return template('exibir', things = resultado)

@post('/all')
def readall():
    resultado = db_selectall()
    return template('exibir', things = resultado)

@get('/edita/<nID>')
def link_edicao(nID):
    resultado = db_selectID(nID)
    return template('editall', things = resultado)

@post('/editall/<nID>')
def read_all_ID(nID):
    ide = str(nID)
    nome = str(request.forms.get('nome'))
    telefone = str(request.forms.get('telefone'))
    info = str("Nome: " + nome + " Telefone: " + telefone + "")
    if nome not in 'Nonenone':
        db_updateall(ide, nome, telefone)
    else:
        return template('editall', things = resultado)
    return template('verifica.html', sucesso = True, acao = info, nome = " Alterado(a) para ")

@get('/deleta/<nID>')
def link_edicao(nID):
    resultado = db_select(nID)
    return template('deletall', things = resultado)


@post('/deletall/<nID>')
def delete(nID):
    nome = str(nID)
    db_delete(nID)
    return template('verifica.html', sucesso = True, acao = "foi excluido(a) ", nome = nome)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
