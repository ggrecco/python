from bottle import jinja2_view, route, run, request, response
from dml import db_insert

@route('/users', method='GET')
@jinja2_view('html/users.html')
def user():
    links = ['home', 'help']
    return dict(links=links)

@route('/users', method='POST')
@jinja2_view('html/users.html')
def user_post():
    links = ['home', 'help']
    nome = request.forms.get('nome')
    telefone = request.forms.get('telefone')
    email = request.forms.get('email')
    db_insert(nome, telefone, email)
    return dict(string='cadastrado com sucesso!', links=links)

run(port = 8080)
