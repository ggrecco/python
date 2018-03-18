from bottle import route, run, template
@route('/hello/<name>')
def index(name):
    return template('Hello {{name}}!', name=name)

run(host='localhost', port=8080)
