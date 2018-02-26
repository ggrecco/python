from bottle import route, run, request, response, post, get, template, static_file

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
#---------------------------------------------------------

@route('/')
def home_page():
    return template('base')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
