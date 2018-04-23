from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.models import Usuario
from app import app, db
from app.forms import LoginForm, RegistrationForm, ScrapyForm


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Gustavo'}
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


@app.route('/scrapy', methods=['GET', 'POST'])
@login_required
def scrapy():
    form = ScrapyForm()
    if form.validate_on_submit():
        flash('O scrapy foi realizado, só precisa ser implementado...heheh!')
        return redirect(url_for('index'))
    return render_template('scrapy.html', title='Scrapy', form=form)
