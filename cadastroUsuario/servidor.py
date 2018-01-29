import bottle
from dml import db_insert

@bottle.route('/')
def home_page():
    coisas = ['Python', 'C++']
    return bottle.template('base', {'username':'Gustavo', 'things' : coisas})

@bottle.post('/')
def home_page():
    coisas = ['Python', 'C++']
    nome = bottle.request.forms.get('nome')
    telefone = bottle.request.forms.get('telefone')
    db_insert(nome, telefone)
    return bottle.template('base', {'username':'Gustavo', 'things' : coisas})

bottle.debug(True)
bottle.run(host='localhost', port=8080)
