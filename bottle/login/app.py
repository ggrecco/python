from bottle import route, run, request, response, post, get, template, static_file, redirect, app
from busca import *
from panela import *
from check_login import *
import bottle
from beaker.middleware import SessionMiddleware

_session_opts = {'session.type':'memory','_session.cookie_expires':600,'_session.auto': True}
app = SessionMiddleware(app(), _session_opts)


def has_session():
	_session = request.environ.get('beaker.session')
	if not _session or 'usuario_id' not in _session:
		return redirect('/login')

def set_session(key,value):
	_session = request.environ['beaker.session']
	_session[key] = value
	_session.save()

def del_session():
	_session = request.environ['beaker.session']
	_session.delete()

def get_session():
    try:
        _session = request.environ['beaker.session']
        return _session['usuario_id']
    except Exception:
        return 0


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

run(host='localhost', port=8080, debug=True, reloader=True, app=app)
