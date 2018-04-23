from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    servidores = db.relationship('Servidor', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<Usuario {}>'.format(self.nome)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Servidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(140))
    produto = db.Column(db.String(20))
    cveid = db.Column(db.String(25))
    tipo = db.Column(db.String(25))
    datacorrecao = db.Column(db.String(50))
    nota = db.Column(db.String(10))
    acesso = db.Column(db.String(100))
    comentario = db.Column(db.String(5000))

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

    def __repr__(self):
        return '<Servidor {}>'.format(self.nome)


@login.user_loader
def load_user(id):
    return Usuario.query.get(int(id))
