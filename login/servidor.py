from bottle import route, run, request, response, post, get, template, static_file
from busca import *
from panela import *


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
#-----------------------------------------------------------------
panela = Panelas()

@route('/')
def home_page():
    return template('login.html')

@post('/retornoLogin')
def teste():
    usuario = str(request.forms.get('email'))
    senha = str(request.forms.get('password'))
    return template('retornoLogin.html', sucesso = check_login(usuario, senha))

@get('/panelas')
def listar_panelas():
    dados = panela.listarTodos()
    return template('listar_panelas.html', dados = dados)

@get('/panela/inserir')
def medico_inserir_get():
	return template('inserir_panela.html')

@post('/panela/inserir')
def panela_inserir_post():
	marca = request.POST.marca.strip()
	tipo = request.POST.tipo.strip()
	valor = request.POST.valor.strip()
	panela.inserir(marca, tipo, valor)
	return redirect("/panelas")

run(host='localhost', port=8080, debug=True, reloader=True)
