from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gustavo'}
    posts    = [
        {
            'autor':{'username': 'Gustavo'},
            'body':'Um belo dia para estudar!'
        },
        {
            'autor':{'username': 'Karim'},
            'body': 'Piratas do caribe é um BAITA filmão.'
        }
    ]
    return render_template('index.html', title='Título com acentuação', user=user, posts=posts)
