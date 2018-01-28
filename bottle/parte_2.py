from bottle import post, get,run, request#,route

#@route('/', method='GET') ---> usando import route
@get('/')
def index_get():
    return '''
    <form action="/" method="post">
        Username: <input name="username" type="text" />
        Password: <input name="password" type="password" />
        <input value="Login" type="submit" />
    </form>'''

#@route('/', method='POST') ---> usando import route
@post('/')
def index_get():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return '''
    <h1>Suas informações</h1>
    </br>
    <h4>{}</h4>
    <h4>{}</h4>'''.format(username, password)

run(port=8080)
