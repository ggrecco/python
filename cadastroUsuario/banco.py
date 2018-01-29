#DDL manipulação da tabela
import sqlite3

con = sqlite3.connect("banco.db")
cur = con.cursor()

sql = """
CREATE TABLE users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL)"""

cur.execute(sql)
con.commit()
con.close()
