from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
# from flask_redis import FlaskRedis
# from flask_celery import make_celery

app = Flask(__name__)
# redis_store = FlaskRedis(app)
# app.config.from_object(Config)
# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# app.config['CELERY_RESULT_BACKEND'] = '/home/ggrecco/Documentos/python/flask/funcionando/app.db'

# celery = make_celery(app)
# celery.conf.update(app.config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)

from app import routes, models
