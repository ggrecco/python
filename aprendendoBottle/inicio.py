from bottle import route, run, request, post, get, template, static_file
'''
@route('/')
@route('/user/<nome>')
def index(nome = 'Desconhecido'):
    return '<center><h1>Olá ' + nome + '</h1></center>'
'''
@get('/login')
def login():
    return template('login')

def check_login(username,password):
    d = {'gustavo':'python','karim':'python', 'sandro':'java'}
    if username in d.keys() and d[username] == password:
        return True
    return False

@post('/login')
def acao_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    sucesso = check_login('username', 'password')
    return template('verificacao_login', sucesso = check_login(username, password),nome = username)


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
