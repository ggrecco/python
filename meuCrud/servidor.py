from bottle import route, run, request, response, post, get, template, debug
from dml import db_delete, db_insert, db_update, db_select, db_selectall

@route('/')
def home_page():
    return template('base', {'msg' : 'Bem vindo!', 'things':''})

@post('/inserir')
def create():
    nome = request.forms.get('nome')
    telefone = request.forms.get('telefone')
    db_insert(nome, telefone)
    return template('base', {'msg' : ' Cadastrado com sucesso!', 'things':''})
#{'msg' : 'Bem vindo!', 'things':''}

@post('/ler')
def read():
    result = str(request.forms.get('dado'))
    resultado = db_select(result)
    return template('base', {'msg' : 'O registro correspondente é:','things' : resultado})

@post('/editar')
def update():
    nome = str(request.forms.get('nome'))
    novo = str(request.forms.get('telefone'))
    db_update(novo, nome)
    return template('base' , {'msg' : 'Editado com sucesso!', 'things':''})

@post('/deletar')
def delete():
    nome = str(request.forms.get('delete'))
    db_delete(nome)
    return template('base' , {'msg' : 'Excluido com sucesso!', 'things':''})

@post('/all')
def read():
    resultado = db_selectall()
    return template('base', {'msg' : 'Os dados pesquisados são:', 'things': resultado })

run(host='localhost', port=8080)
