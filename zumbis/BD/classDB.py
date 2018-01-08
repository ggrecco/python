import sqlite3

def db(a,b):
    banco = sqlite3.connect(b)
    banco.row_factory = sqlite3.Row
    cursor = banco.cursor()
    cursor.execute(a)
    linhas = cursor.fetchall()
    return linhas
