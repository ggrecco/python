from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_celery import *
from flask_moment import Moment


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)
app.config.update(CELERY_BROKER_URL='amqp://localhost//',
                  CELERY_RESULT_BACKEND='db+sqlite:///appd.db')
celery = make_celery(app)
moment = Moment(app)


from app import routes, models, errors
