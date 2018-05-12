from celery import Celery

app = Celery('tasks', broker='amqp://localhost', backend='db+sqlite:///app.db')
