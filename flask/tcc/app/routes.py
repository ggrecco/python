from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.models import Usuario, Servidor, Dados
from app import app, db
from app.forms import LoginForm, RegistrationForm, ScrapyForm, ServidorForm
from app.scrapy import scraper
from datetime import datetime

# verifica se a conta current_user está conectada e define o last_seen campo para a hora atual
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/')
@app.route('/index')
@login_required
def index():
    #chamar banco de dados
    posts = [
        {
            'author': {'username': 'Bem Vindo '},
            'body': 'Escrever aqui as funcioanlidades do software e um breve resumo.(com links)'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(nome=form.username.data).first()
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
        user = Usuario(nome=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Parabéns, você foi registrado com suceso!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registro', form=form)


@app.route('/usuario/<username>')
@login_required
def user(username):
    user = Usuario.query.filter_by(nome=username).first_or_404()
    dados = Dados.query.filter_by(usuario_id=current_user.id)
    return render_template('user.html', user=user, dados=dados)


@app.route('/scrapy', methods=['GET', 'POST'])
@login_required
def scrapy():
    form = ScrapyForm()
    if form.validate_on_submit():
        flash('O scrapy foi realizado!')
        scraper(form.linguagem.data)#pega do formulario(template) o dado inserido e enviado
        return redirect(url_for('index'))
    return render_template('scrapy.html', title='Scrapy', form=form)


@app.route('/servidor', methods=['GET', 'POST'])
@login_required
def servidor():
    form = ServidorForm()
    if form.validate_on_submit():
        flash('O servidor foi registrado, só precisa ser implementado...heheh!')

        return redirect(url_for('index'))
    return render_template('servidor.html', title='Servidor', form=form)
