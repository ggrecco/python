from bottle import request, route, run, response

@route('/')
def hello_again():
    if request.get_cookie('visited'):
        return 'Olá de volta'
    response.set_cookie('visited','yes')
    return 'Olá, Bem vindo'

run(port=8080)
