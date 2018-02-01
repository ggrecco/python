from bottle import route, run, request, response, post, get, template, debug
from dml import db_delete, db_insert, db_update, db_select, db_selectall

@route('/')
def home_page():
    return template('base', {'things' : 'Bem vindo!'})

@post('/inserir')
def create():
    nome = request.forms.get('nome')
    telefone = request.forms.get('telefone')
    db_insert(nome, telefone)
    return template('base', {'things' : ' Cadastrado com sucesso!'})

@post('/ler')
def read():
    result = request.forms.get('dado')
    resultado = db_select(result)
    return template('base', things = resultado )

@post('/editar')
def update():
    nome = str(request.forms.get('nome'))
    novo = str(request.forms.get('telefone'))
    db_update(novo, nome)
    return template('base' , {'things' : 'Editado com sucesso!'})

@post('/deletar')
def delete():
    nome = str(request.forms.get('delete'))
    db_delete(nome)
    return template('base' , {'things' : 'Excluido com sucesso!'})

@post('/all')
def read():
    resultado = db_selectall()
    return template('base', things = resultado )

run(host='localhost', port=8080)
