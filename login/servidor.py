from bottle import route, run, request, response, post, get, template, static_file
from busca import *

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
    return template('login.html')

def check_login(username,password):
    login = Login()
    d = {}
    dados = login.busca(username)

    if type(dados) is tuple:
        for dado in dados:
            d[dados[1]] = dados[2]

        if username in d.keys() and d[username] == password:
            return True
        return False
    else:
        return False

@post('/retornoLogin')
def teste():
    usuario = str(request.forms.get('email'))
    senha = str(request.forms.get('password'))
    return template('retornoLogin.html', sucesso = check_login(usuario, senha))

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
