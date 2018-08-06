# aplicação
from config import Configuration
from flask import Flask, render_template, jsonify, json
import sqlite3
import geopy
from geopy.geocoders import Nominatim, GoogleV3

app = Flask(__name__)
app.config.from_object(Configuration)


@app.route('/')
def index():
    table = "populacao"
    conn = sqlite3.connect('populacao.db')
    c = conn.cursor()
    sql = "SELECT * FROM "+table
    c.execute(sql)
    dados = c.fetchall()
    lista = []
    dicionario = {}
    i = 0
    while i < len(dados):

        dicionario["ANO"] = str(dados[i][1])
        dicionario["EUA"] = dados[i][2]
        dicionario["BRA"] = dados[i][3]
        lista.append(dicionario)
        dicionario = {}
        i = i + 1

    return render_template("index.html", dados=json.dumps(lista))


@app.route('/map')
def map():
    table = "populacao"
    conn = sqlite3.connect('populacao.db')
    c = conn.cursor()
    sql = "SELECT * FROM "+table
    c.execute(sql)
    dados = c.fetchall()
    geolocator = Nominatim()
    # geolocator = GoogleV3()
    gg = geolocator.geocode

    gg
    return render_template("map.html")


if __name__ == '__main__':
    app.run()
