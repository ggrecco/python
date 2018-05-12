from flask import Flask
from flask_celery import *

flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='amqp://localhost:6379',
    CELERY_RESULT_BACKEND='amqp://localhost:6379'
    )

celery = make_celery(flask_app)

@celery.task()
def add_together(a, b):
    return a + b
