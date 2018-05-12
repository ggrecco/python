from flask import Flask
from flask_celery import make_celery
from flask_sqlalchemy import SQLAlchemy
from random import choice
import os

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_BACKEND'] = 'db+sqlite:///banco.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'banco.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'

celery = make_celery(app)
db = SQLAlchemy(app)

class Results(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.String(50))

@app.route('/process/<name>')
def process(name):

    reverse.delay(name)

    return 'Eu enviei uma solicitação assincrona'

@app.route('/insertData')
def insertData():

    insert.delay()

    return 'request para inserir dados aleatorios no banco'


@celery.task(name='celery_example.reverse')
def reverse(string):
    return string[::-1]

@celery.task(name='celery_example.insert')
def insert():
    for i in range(500):
        data = ''.join(choice('ABCDE') for i in range(10))
        result = Results(data=data)

        db.session.add(result)
    db.session.commit()
    return 'Done!!!'

if __name__ == '__main__':
    app.run(debug=True)
