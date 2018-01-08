import sqlite3

def db(sql,nomeDB):
    banco = sqlite3.connect(nomeDB)
    banco.row_factory = sqlite3.Row
    cursor = banco.cursor()
    cursor.execute(sql)
    linhas = cursor.fetchall()
    return linhas
    cursor.close()
