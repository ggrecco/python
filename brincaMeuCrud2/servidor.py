from bottle import route, run, request, response, post, get, template, static_file
from dml import db_delete, db_insert, db_update, db_select, db_selectall

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
@route('/index')
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
def read():
    resultado = db_selectall()
    return template('exibir', things = resultado)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
