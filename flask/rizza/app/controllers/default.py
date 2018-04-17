from app import app


@app.route("/")
def firstApp():
    return "<h1>Hello Word!</h1>"
