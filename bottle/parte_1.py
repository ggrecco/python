#introdução rotas dinamicas e estática
from bottle import run, route

@route('/')
def index():
    return '<h1>Olá Mundo</h1>'
    #rota estática

@route('/<person>')
def index(person):
    return '<h1>Olá {}</h1>'.format(person)
    #rota dinamica

run(port=8080)
