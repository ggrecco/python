import os
basedir = os.path.abspath(os.path.dirname(__file__))
#configura SECRET_KEY para evitar ataques CSRF
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'voce-nao-vai-passar'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
