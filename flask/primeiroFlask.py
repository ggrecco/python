from flask import Flask

app = Flask(__name__)

@app.route("/")
def firstApp():
    return "<h1>Minha Primeira aplicaçõa com FLASK!</h1>"

if __name__ == "__main__":
    app.run()
