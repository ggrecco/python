import sqlite3

c = sqlite3.connect('cvedetails.db')

tabela_cvedetails = """CREATE TABLE login(
id integer primary key,
nome varchar(50),
senha varchar(50),
email varchar(150)
)"""

c.execute(tabela_cvedetails)

c.commit()
