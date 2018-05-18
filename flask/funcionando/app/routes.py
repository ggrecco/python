from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.models import Usuario, Servidor, Dados
from app import app, db
from app.forms import LoginForm, RegistrationForm, ScrapyForm, ServidorForm, EditProfileForm, DeletarForm
from app.scrapy import scraper
from app.portscan import portScan, busca_ip
from datetime import datetime
from tcc import *
import unidecode
import time

# verifica se a conta current_user está conectada e define o last_seen campo para a hora atual
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

#página inicial
@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'Bem Vindo '},
            'body': 'Escrever aqui um breve resumo das funcioanlidades do software.(com links)'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = unidecode.unidecode(form.username.data)
        usuario = Usuario.query.filter_by(nome=username).first()
        if usuario is None or not usuario.check_password(form.password.data):
            flash('Usuário ou Senha Inválido, tente novamente.')
            return redirect(url_for('login'))
            login_user(usuario, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
        login_user(usuario, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Entrar', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        username = unidecode.unidecode(form.username.data)
        if username.isalpha():
            user = Usuario(nome=username, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Parabéns, você foi registrado com suceso!')
            return redirect(url_for('login'))
        flash('Por favor, não utilize caractéres especiais como "/ $ #" ou palavras acentuádas.')
    return render_template('register.html', title='Registro', form=form)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.nome = unidecode.unidecode(form.username.data)
        current_user.email = form.email.data
        db.session.commit()
        flash('Suas alterações foram salvas(e automaticamente removido as acentuações ;) )')
        return redirect(url_for('index'))
    elif request.method == 'GET':
        #busca do banco os dados para exibir ao usuário o que está salvo
        form.username.data = current_user.nome
        form.email.data = current_user.email
    return render_template('editar.html', title='Editar Perfil', form=form)


@app.route("/deletar", methods=['GET', 'POST'])
@login_required
def deletar():
    form = DeletarForm()
    if form.validate_on_submit():
        user_id = current_user.id
        u = Usuario.query.filter_by(id=user_id).first()
        d = Dados.query.filter_by(usuario_id=user_id)
        s = Servidor.query.filter_by(usuario_id=user_id)
        d.delete()
        s.delete()
        db.session.delete(u)
        db.session.commit()
        return redirect(url_for('logout'))
    return render_template('deletar.html', title='Deletar usuario', form=form )


@app.route('/usuario/<username>')
@login_required
def user(username):
    user = Usuario.query.filter_by(nome=username).first_or_404()
    dados = Dados.query.filter_by(usuario_id=current_user.id)
    servidores = Servidor.query.filter_by(usuario_id=current_user.id)
    return render_template('user.html', title='Perfil de usuário', user=user, dados=dados, servidores=servidores)


#tratar o erro para nome unico(igual login)
@app.route('/servidor', methods=['GET', 'POST'])
@login_required
def servidor():
    form = ServidorForm()
    if form.validate_on_submit():
        flash('O servidor foi registrado,alguarde alguns minutos antes de consultar.')
        u = Usuario.query.filter_by(id=current_user.id).first()
        p = busca_ip(form.url.data)
        s = Servidor(nome=form.servidor.data, url=form.url.data, ip=p, rel_usuario=u)
        db.session.add(s)
        db.session.commit()
        url = form.url.data
        user = current_user.id
        portScanCel.delay(url, user)
        return redirect(url_for('index'))
    return render_template('servidor.html', title='Pesquisar servidor', form=form)


@app.route('/refazer_<nome>_<url>_<ip>', methods=['GET', 'POST'])
@login_required
def refazer(nome, url, ip):
    i = 0
    flash('Refazendo teste, alguarde alguns minutos antes de consultar.')
    s = Servidor.query.filter_by(nome=nome, url=url, ip=ip)
    result = portScanCel.delay(url, user)
    # while result.ready() == False:
    #     print(result.status)
    #     time.sleep(1)
    # portScan(url, user)
    return redirect(url_for('index'))


@app.route('/dados_<nome>', methods=['GET', 'POST'])
@login_required
def dados(nome):
    servidores = Servidor.query.filter_by(usuario_id=current_user.id, nome=nome)
    servidor_id = servidores.value('id')
    dados = Dados.query.filter_by(usuario_id=current_user.id, servidor_id=servidor_id)
    return render_template('dados_servidores.html',title='Vulnerabilidades', dados=dados, servidores=servidores)


@app.route('/vul_<cveid>_<nome>', methods=['GET', 'POST'])
@login_required
def vul(cveid, nome):
    servidores = Servidor.query.filter_by(usuario_id=current_user.id, nome=nome)
    servidor_id = servidores.value('id')
    dados = Dados.query.filter_by(cveid=cveid, servidor_id=servidor_id)
    return render_template('vul.html',title='Detalhes', dados=dados)
