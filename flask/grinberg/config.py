import os
#configura SECRET_KEY para evitar ataques CSRF
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'voce-nao-vai-passar'
