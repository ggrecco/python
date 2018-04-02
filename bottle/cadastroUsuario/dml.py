#DML - Manipulação de dados
import sqlite3

def commit_close(func):
    def decorator(*args):
        con = sqlite3.connect('banco.db')
        cur = con.cursor()
        sql = func(*args)
        cur.execute(sql)
        con.commit()
        con.close()
    return decorator

@commit_close
def db_insert(name, phone):
    return """
    INSERT INTO users(name, phone)
        VALUES('{}', '{}')
    """.format(name, phone)

@commit_close
def db_update(name, phone):
    return """
    UPDATE users SET phone = '{}' WHERE name = '{}'
    """.format(name, phone)

@commit_close
def db_delete(name):
    return """
    DELETE FROM users WHERE name = '{}'
    """.format(name)

def db_select(data, field):
    con = sqlite3.connect('banco.db')
    cur = con.cursor()
    sql = """
    SELECT  id, name, phone
    FROM users
    WHERE {} = {}""".format(field, data)
    cur.execute(sql)
    dados = cur.fetchall()
    con.close()
    return dados