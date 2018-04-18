from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello word"

@app.route('/hello/<name>')
def hello(name):
    return 'hello ' + name

if __name__ == '__main__':
    app.run(port=8080, debug=True)
