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


'''
definido o nome da função, deve-se passar (ou não, depende da função) os parametros
que serão utilizados para executar a função em background.
tcc.portScanCel é a task definada pelo celery quando iniciado por: >>> celery -A tcc.celery worker --loglevel=info  <<<<
retorna uma msg para registro.
'''
