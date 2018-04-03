from bottle import route, run, request, response, post, get, template, static_file, redirect
from busca import *
from panela import *
from bottle_jwt import JWTProviderPlugin, jwt_auth_required
import bottle


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

#-----------------------------------------------------------------
app = bottle.Bottle()

server_secret = '*Y*^%JHg7623'


class AuthBackend(object):
    def authenticate_user(self, username, password):
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

    def get_user(self, user_id):
        if user_id == self.d['id']:
            return {k: self.d[k] for k in self.d if k != 'password'}
        return None


provider_plugin = JWTProviderPlugin(
    keyword='jwt',
    auth_endpoint='/auth',
    backend=AuthBackend(),
    fields=('username', 'password'),
    secret=server_secret,
    ttl=30
)

app.install(provider_plugin)

#-----------------------------------------------------------------
panela = Panelas()

@route('/')
def home_page():
    return template('login.html')

@post('/retornoLogin')
@jwt_auth_required
def teste():
    usuario = str(request.forms.get('email'))
    senha = str(request.forms.get('password'))
    return template('retornoLogin.html', sucesso = check_login(usuario, senha))

@get('/panelas')
def listar_panelas():
    dados = panela.listarTodos()
    return template('listar_panelas.html', dados = dados)

@get('/inserir_panela')
def medico_inserir_get():
	return template('inserir_panela.html')

@post('/inserir_panela')
def panela_inserir_post():
	marca = request.POST.marca.strip()
	tipo = request.POST.tipo.strip()
	valor = request.POST.valor.strip()
	panela.inserir(marca, tipo, valor)
	return redirect("/panelas")


@get('/panela_alterar_<id>')
def alterar_get(id):
	dados = panela.listar1(id)
	return template('alterar_panela.html',dados=dados)

@post('/panela_alterar')
def alterar_post():
	id=request.POST.id
	marca=request.POST.marca
	tipo=request.POST.tipo
	valor=request.POST.valor
	panela.alterar(id,marca,tipo,valor)
	return redirect ('/panelas')

@get('/panela_deletar_<id>')
def deletar_get(id):
	dados=panela.listar1(id)
	return template('deletar_panela.html',dados=dados)

@post('/panela_deletar')
def deletar_post():
	id=request.POST.id
	dados=panela.deletar(id)
	return redirect ('/panelas')

@get('/panela_visualizar_<id>')
def visualizar_get(id):
	dados=panela.listar1(id)
	return template('visualizar_panela.html',dados=dados)

run(host='localhost', port=8080, debug=True, reloader=True)
