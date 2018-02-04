from bottle import route, run, request, post, get, template, static_file

# static routes
@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def imagens(filename):
    return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)')
def fonts(filename):
    return static_file(filename, root='static/fonts')

@route('/login')
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
