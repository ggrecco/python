from scrapy import *
from bottle import route, run, request, response, post, get, template, static_file, redirect, Bottle
from dml import *
from check_login import *
from beaker.middleware import SessionMiddleware
'''
_session_opts = {'session.type':'memory','_session.cookie_expires':600,'_session.auto': True}
#_session_opts = {'session.type': 'file','session.data_dir': '/openmining.data','session.lock_dir': '/openmining.lock','session.cookie_expires': 5000,'session.auto': True}
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

'''
cve = Cve()

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

@route('/')
def home_page():
    return template('login.html')

@post('/retornoLogin')
def login():
    usuario = str(request.forms.get('email'))
    senha = request.forms.get('password')
    sucesso = check_login(usuario, senha)
    global sucesso
    return template('retornoLogin.html', sucesso = sucesso)

@get('/scrapy1')
def scrapy2():
    return template('scrapy.html')

@post('/scrapy')
def scr():
    linguagem = str(request.forms.get('software'))
    minimo = str(request.forms.get('mini'))
    maximo = str(request.forms.get('maxi'))
    scrapy(linguagem, minimo, maximo)
    #tratar o dado se retorno positivo ou negativo
    return template('deseja.html')

@post('/pesquisar')
def pesquisar():
    return template('visualizar_cve.html')

@get('/cve')
def listar_cve():
    dados = cve.listarTodos()
    return template('listar_cve.html', dados = dados, sucesso = sucesso)

@get('/cve_alterar_<id>')
def alterar_get(id):
	dados = cve.listar1(id)
	return template('alterar_cve.html',dados=dados)

@post('/cve_alterar')
def alterar_post():
	id=request.POST.id
	produto=request.POST.produto
	cveid=request.POST.cveid
	tipo=request.POST.tipo
	valor=request.POST.valor
	datacorrecao=request.POST.datacorrecao
	nota=request.POST.nota
	acesso=request.POST.acesso
	comentarios=request.POST.comentarios
	cve.alterar(id,marca,tipo,valor)
	return redirect ('/cve')

@get('/cve_deletar_<id>')
def deletar_get(id):
	dados=cve.listar1(id)
	return template('deletar_cve.html',dados=dados)

@post('/cve_deletar')
def deletar_post():
	id=request.POST.id
	dados=cve.deletar(id)
	return redirect ('/cve')

@get('/cve_visualizar_<id>')
def visualizar_get(id):
	dados=cve.listar1(id)
	return template('visualizar_cve.html',dados=dados, sucesso = sucesso)

@get('/teste')
def teste():
    links = ['cve', 'scrapy1']
    return template('teste.html',dict(links=links))

run(host='localhost', port=8000, debug=True, reloader=True)
# run(host='10.0.2.15', port=8080, debug=True, reloader=True)
