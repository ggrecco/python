from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    resultados = db.relationship('Resultado', backref='autor_usuario', lazy='dynamic')
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Usuario {}>'.format(self.nome)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Servidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(140))
    url = db.Column(db.String(255))
    ip = db.Column(db.String(25))
    resultados = db.relationship('Resultado', backref='autor_servidor', lazy='dynamic')

    def __repr__(self):
        return '<Servidor {}>'.format(self.nome)


@login.user_loader
def load_user(id):
    return Usuario.query.get(int(id))


class Resultado(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    servidor_id = db.Column(db.Integer, db.ForeignKey('servidor.id'))
    datas = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    resultados = db.relationship('Dados', backref='autor_resultado', lazy='dynamic')

    def __repr_(self):
        return '<Resultado {}>'.format(self.datas)

class Dados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_resultado = db.Column(db.Integer, db.ForeignKey('resultado.id'))
    produto = db.Column(db.String(20))
    cveid = db.Column(db.String(25))
    tipo = db.Column(db.String(25))
    datacorrecao = db.Column(db.String(50))
    nota = db.Column(db.String(10))
    acesso = db.Column(db.String(100))
    comentario = db.Column(db.String(5000))
# produto='JAVA', cveid='testeasd', tipo='coisaChata', datacorrecao='12-12-1234', nota='7.9', acesso='facil', comentario='teste de comentarios gigante que nao quero escrever, pois escrever tem que usar a caneta e aqui digitamos com o teclado'
    def __repr__(self):
        return '<Dados {}>'.format(self.produto)
