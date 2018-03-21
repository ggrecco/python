from bottle import route, run, request, response, post, get, template, static_file, redirect
from dml import *

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
cve = Cve()

@route('/')
def home_page():
    return template('login.html')

@post('/retornoLogin')
def teste():
    usuario = str(request.forms.get('email'))
    senha = str(request.forms.get('password'))
    return template('retornoLogin.html', sucesso = check_login(usuario, senha))

@get('/cve')
def listar_cve():
    dados = cve.listarTodos()
    return template('listar_cve.html', dados = dados)


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
	return template('visualizar_cve.html',dados=dados)

run(host='localhost', port=8080, debug=True, reloader=True)
