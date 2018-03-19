import sqlite3

c = sqlite3.connect('cve.db')

tabela_cve = """CREATE TABLE cve(
id integer primary key,
nota varchar(50),
comentarios varchar(5000)
)"""

c.execute(tabela_cve)

c.commit()
