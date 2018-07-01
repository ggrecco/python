from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index(name = 'world'):
    name = request.args.get('name')
    return "Hello " + name

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name='Ze'):
    return 'hello ' + name

if __name__ == '__main__':
    app.run(port=8080, debug=True)
