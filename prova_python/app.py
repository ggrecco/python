import sqlite3
from bottle import route, run, template, request, redirect, response, post, get, static_file
from medicos import *
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
############################################################
conn = sqlite3.connect("prova.db")
c = conn.cursor()

@route('/')
def index():
	tpl = 'Hello, Buddy!{{d}} You are at medicos app. If you want to see the content, click here'
	d = ''
	return template('index.html',d=d)

@route('/medicos')
def lista_medicos():
	medico = Medicos()
	dados = medico.listarTodos()
	return template('listar_medicos.html', dados=dados)

@route('/medico/inserir', method='GET')
def medico_inserir_get():
	return template('inserir_medico.html')

@route('/medico/inserir', method='POST')
def medico_inserir_post():
	nome = request.POST.nome.strip()
	crm = request.POST.crm.strip()
	especialidade = request.POST.especialidade.strip()
	endereco = request.POST.endereco.strip()
	valor_consulta = request.POST.valor_consulta.strip()
	medico = Medicos()
	medico.inserir(nome,crm,especialidade,endereco,valor_consulta)
	return redirect("/medicos")

@route('/medico/alterar/<id>', method='GET')
def alterar_get(id):
	medico = Medicos()
	dados= medico.listar1(id)
	return template('alterar_medicos.html',dados=dados)

@route('/medico/alterar', method='POST')
def alterar_post():
	id=request.POST.id
	nome=request.POST.nome
	crm=request.POST.crm
	especialidade=request.POST.especialidade
	endereco=request.POST.endereco
	valor_consulta=request.POST.valor_consulta
	medico = Medicos()
	medico.alterar(id,nome,crm,especialidade,endereco,valor_consulta)
	return redirect ('/medicos')

@route('/medico/deletar/<id>', method='GET')
def deletar_get(id):
	medico = Medicos()
	dados=medico.listar1(id)
	return template('deletar_medicos.html',dados=dados)

@route('/medico/deletar', method='POST')
def deletar_post():
	id=request.POST.id
	medico = Medicos()
	dados=medico.deletar(id)
	return redirect ('/medicos')

@route('/medico/visualizar/<id>', method='GET')
def visualizar_get(id):
	medico = Medicos()
	dados=medico.listar1(id)
	return template('visualizar_medico.html',dados=dados)

run(host='localhost', port=7000, reloader = True)
