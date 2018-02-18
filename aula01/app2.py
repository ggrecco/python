import sqlite3
from bottle import route, run, template, request, redirect
from marcas import *

conn = sqlite3.connect("automoveis.db")
c = conn.cursor()

@route('/')
def index():
	d = ''
	return template('index.tpl', d=d)

@route('/marcas')
def lista_marcas():
    marca = Marcas()  # instanciada classe Marca() no objeto marca
    dados = marca.listarTodos()
    return template('lista_marcas.tpl', dados=dados)

@route('/marca/inserir', method='GET')
def marca_inserir_get():
	return template('inserir_marca.tpl')

@route('/marca/inserir', method='POST')
def marca_inserir_post():
	nome = request.POST.nome.strip()
	origem = request.POST.origem.strip()
	presidente = request.POST.presidente.strip()
	fundacao = request.POST.fundacao.strip()
	marca = Marcas()
	marca.inserir(nome,origem,presidente,fundacao)
	return redirect("/marcas")

@route('/marca/alterar/<id>', method='GET')
def alterar_get(id):
	marca = Marcas()
	dados = marca.listar1(id)
	return template('alterar_marca.tpl',dados=dados)


@route('/marca/alterar', method='POST')
def alterar_post():
	id = request.POST.id
	nome = request.POST.nome
	origem = request.POST.origem
	presidente = request.POST.presidente
	fundacao = request.POST.fundacao
	marca = Marcas()
	marca.alterar(id,nome,origem,fundacao,presidente)
	return redirect ('/marcas')

@route('/marca/deletar/<id>', method='GET')
def deletar_get(id):
	marca = Marcas()
	dados = marca.listar1(id)
	return template('deletar_marca.tpl',dados=dados)

@route('/marca/deletar', method='POST')
def deletar_post():
	id = request.POST.id
	marca = Marcas()
	dados = marca.deletar(id)
	return redirect ('/marcas')

run(host='localhost', port=7000, reloader = True)
