#aplicação
from config import Configuration
from flask import Flask
import routes

app = Flask(__name__)
app.config.from_object(Configuration)


if __name__ == '__main__':
    app.run()
