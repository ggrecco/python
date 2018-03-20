import sqlite3

c = sqlite3.connect('cvedetails.db')

tabela_cvedetails = """CREATE TABLE cvedetails(
id integer primary key,
produto varchar(50),
cveid varchar(50),
tipo varchar(25),
datacorrecao varchar(50),
nota varchar(50),
acesso varchar(100),
comentarios varchar(5000)
)"""

c.execute(tabela_cvedetails)

c.commit()
