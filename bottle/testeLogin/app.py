from bottle import *

@route('/')
def home_page():
    return 'Olá Mundo!'

@error(404)
def erro404(error):
    return 'Página não encontrada'

run(host='localhost', port=8080, debug=True)
