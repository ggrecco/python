from app import app
from app.portscan import portScan
from flask_celery import *

app.config.update(
    CELERY_BROKER_URL='amqp://localhost//',
    CELERY_RESULT_BACKEND='db+sqlite:///app.db'
)
celery = make_celery(app)

@celery.task(name='tcc.portScanCel')
def portScanCel(url, user):
    portScan(url, user)
    return 'Done!'
