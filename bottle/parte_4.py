from bottle import jinja2_view, route, run, request, response

@route('/<area>')
@jinja2_view('paginas/teste.html')
def teste(area):
    return dict(nome=area)

@route('/user', method='GET')
@jinja2_view('paginas/user.html')
def user():
    links = ['home', 'about', 'help']

    return dict(links=links)

@route('/user', method='POST')
@jinja2_view('paginas/user.html')
def user_post():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if username == 'teste' and password == 'senha' or \
        request.get_cookie('user') == 'teste':
        response.set_cookie('user', 'teste')
        links = ['home','user', 'help']

        return dict(string='Você está logado', links=links)
    else:
        response.set_cookie('user','None')
        links = ['home', 'about', 'help']
        return dict(string='erro, você não está logado', links=links)


run(port=8080)
