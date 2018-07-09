from flask import render_template, flash, redirect, url_for, request, g
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.models import Usuario, Servidor, Dados
from app import app, db
from app.forms import LoginForm, RegistrationForm, \
        ServidorForm, EditProfileForm, DeletarForm, \
        AlteraServidorForm, NotaServidorForm
from app.portscan import busca_ip
from celeryF import *
from datetime import datetime
import unidecode
from flask_babel import get_locale
from flask_weasyprint import HTML, render_pdf


# atualiza data de ações, traduz conforme local
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale = str(get_locale())


# página inicial
@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@app.route('/qr', methods=['GET', 'POST'])
def qr():
    return render_template('qr.html', title='Código QR')


# página de login
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


# logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# cadastro
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
        flash('Por favor, não utilize caractéres especiais como "/ $ #" ' +
              'ou palavras acentuádas.')
    return render_template('register.html', title='Registro', form=form)


# edição de perfil
@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.nome = unidecode.unidecode(form.username.data)
        current_user.email = form.email.data
        db.session.commit()
        flash('Suas alterações foram salvas(e automaticamente removido as ' +
              'acentuações ;) )')
        return redirect(url_for('index'))
    elif request.method == 'GET':
        # busca do banco os dados para exibir ao usuário o que está salvo
        form.username.data = current_user.nome
        form.email.data = current_user.email
    return render_template('editar.html', title='Editar Perfil', form=form)


# exclusão de perfil
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
    return render_template('deletar.html', title='Deletar usuario',
                           form=form)


# perfil do usuário
@app.route('/usuario/<username>')
@login_required
def user(username):
    user = Usuario.query.filter_by(nome=username).first_or_404()
    dados = Dados.query.filter_by(usuario_id=current_user.id)
    servidores = Servidor.query.filter_by(usuario_id=current_user.id)
    return render_template('user.html', title='Perfil de usuário',
                           user=user, dados=dados, servidores=servidores)


# Pesquisar servidor
@app.route('/servidor', methods=['GET', 'POST'])
@login_required
def servidor():
    form = ServidorForm()
    if form.validate_on_submit():
        flash('O servidor foi registrado,alguarde alguns ' +
              'minutos antes de consultar.')
        u = Usuario.query.filter_by(id=current_user.id).first()
        p = busca_ip(form.url.data)
        s = Servidor(nome=form.servidor.data, url=form.url.data,
                     ip=p, rel_usuario=u)
        db.session.add(s)
        db.session.commit()
        url = form.url.data
        user = current_user.id
        scaneando.delay(url, user)
        return redirect(url_for('index'))
    return render_template('servidor.html', title='Pesquisar servidor',
                           form=form)


# refazer analise
@app.route('/refazer_<nome>_<url>_<ip>_<user>', methods=['GET', 'POST'])
@login_required
def refazer(nome, url, ip, user):
    i = 0
    flash('Refazendo teste, alguarde alguns minutos antes de consultar.')
    s = Servidor.query.filter_by(nome=nome, url=url, ip=ip)
    result = scaneando.delay(url, user)
    return redirect(url_for('index'))


# botão visualizar dados escaneados
@app.route('/dados_<nome>', methods=['GET', 'POST'])
@login_required
def dados(nome):
    servidores = Servidor.query.filter_by(usuario_id=current_user.id,
                                          nome=nome)
    servidor_id = servidores.value('id')
    dados = Dados.query.filter_by(usuario_id=current_user.id,
                                  servidor_id=servidor_id)
    return render_template('dados_servidores.html', title='Vulnerabilidades',
                           dados=dados, servidores=servidores)


# detalhes da vulnerabilidade
@app.route('/vul_<cveid>_<nome>', methods=['GET', 'POST'])
@login_required
def vul(cveid, nome):
    servidores = Servidor.query.filter_by(usuario_id=current_user.id,
                                          nome=nome)
    servidor_id = servidores.value('id')
    dados = Dados.query.filter_by(cveid=cveid, servidor_id=servidor_id)
    return render_template('vul.html', title='Detalhes', dados=dados)


# servidores pesqusiados
@app.route('/ver_servidor<username>', methods=['GET', 'POST'])
@login_required
def ver_servidor(username):
    lista = []
    # user = Usuario.query.filter_by(nome=username).first_or_404()
    dados = Dados.query.filter_by(usuario_id=current_user.id)
    tamanho = len(list(dados))
    servidores = Servidor.query.filter_by(usuario_id=current_user.id)
    for servidor in servidores:
        dados_servidor = Dados.query.filter_by(usuario_id=current_user.id,
                                               servidor_id=servidor.id)

        k = 0
        i = 0
        while i < len(list(dados_servidor)):
            j = dados_servidor[i].check
            if j == '0':
                k = k + 1
            else:
                pass
            i = i + 1
        lista.append(k)
    return render_template('ver_servidor.html', title='Perfil de usuário',
                           dados=dados, servidores=servidores,
                           tamanho=tamanho, lista=lista)


#  deletar servidor
@app.route("/deleta_servidor<server><serverid>", methods=['GET', 'POST'])
@login_required
def deleta_servidor(server, serverid):
    form = DeletarForm()
    if form.validate_on_submit():
        user_id = current_user.id
        d = Dados.query.filter_by(usuario_id=user_id, servidor_id=serverid)
        s = Servidor.query.filter_by(usuario_id=user_id, nome=server)
        d.delete()
        s.delete()
        db.session.commit()
        flash('Alterações realizadas com sucesso.')
        return redirect(url_for('index'))
    return render_template('deleta_servidor.html', title='Excluir',
                           form=form)


# alterar servidor
@app.route("/altera_servidor<server><serverid>", methods=['GET', 'POST'])
@login_required
def altera_servidor(server, serverid):
    form = AlteraServidorForm()
    user_id = current_user.id
    servidor = Servidor.query.filter_by(nome=server,
                                        usuario_id=user_id)

    if form.validate_on_submit():
        servidor[0].nome = form.servidor.data
        db.session.commit()
        flash('Atualizado com sucesso')
        return redirect(url_for('index'))

    elif request.method == 'GET':
        form.servidor.data = servidor.value('nome')
    return render_template('altera_servidor.html',
                           title='Alterar Servidor', form=form)


# imprime todos os dados em pdf
@app.route('/imprimir_todos/<nome>.pdf')
@login_required
def imprimir_todos(nome):
    servidores = Servidor.query.filter_by(usuario_id=current_user.id,
                                          nome=nome)
    servidor_id = servidores.value('id')
    dados = Dados.query.filter_by(usuario_id=current_user.id,
                                  servidor_id=servidor_id)
    html = render_template('imprimir_todos.html', title='Vulnerabilidades',
                           dados=dados, servidores=servidores)
    return render_pdf(HTML(string=html))


# imprimir por faixa de valores
@app.route('/imprimir_faixa/<nome>', methods=['GET', 'POST'])
@login_required
def selecionar_faixa_imprimir(nome):
    form = NotaServidorForm()
    servidores = Servidor.query.filter_by(usuario_id=current_user.id,
                                          nome=nome)
    if form.validate_on_submit():
        minimo = float(form.minimo.data)
        maximo = float(form.maximo.data)
        if minimo <= maximo:
            return render_template('confirma_faixa.html', nome=nome,
                                   minimo=minimo, maximo=maximo)
        flash('o valor mínimo deve ser menor que o máximo.')
        return render_template('imprimir_faixa.html', servidores=servidores,
                               form=form)
    return render_template('imprimir_faixa.html', servidores=servidores,
                           form=form)


# confirma impressão por faixas
@app.route("/confirma/<minimo>/<maximo>/<nome>", methods=['GET', 'POST'])
def confirma(minimo, maximo, nome):
    servidores = Servidor.query.filter_by(usuario_id=current_user.id,
                                          nome=nome)
    servidor_id = servidores.value('id')
    dados = Dados.query.filter_by(usuario_id=current_user.id,
                                  servidor_id=servidor_id)
    html = render_template('impressao_faixa.html',
                           minimo=float(minimo), maximo=float(maximo),
                           dados=dados, servidores=servidores)
    return render_pdf(HTML(string=html))


# marcar os checkbox
@app.route("/marcas_<cveid>_<servidor>", methods=['GET', 'POST'])
@login_required
def marcas(cveid, servidor):
    servidores = Servidor.query.filter_by(usuario_id=current_user.id,
                                          nome=servidor)
    dados = Dados.query.filter_by(cveid=cveid,
                                  servidor_id=servidores.value('id'))
    if dados[0].check != '1':
        dados[0].check = '1'
        db.session.commit()
        flash('Marcado {}'.format(cveid))
    else:
        dados[0].check = '0'
        db.session.commit()
        flash('Desmarcado {}'.format(cveid))

    dados = Dados.query.filter_by(usuario_id=current_user.id,
                                  servidor_id=servidores.value('id'))
    return render_template('dados_servidores.html', title='Home',
                           servidores=servidores, dados=dados)
