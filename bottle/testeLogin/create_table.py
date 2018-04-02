import sqlite3
c = sqlite3.connect('login.db')

tabela_login="""CREATE TABLE login (
	id integer primary key,
	email varchar(255),
	senha varchar(225))"""

c.execute(tabela_login)

sql_many_inserts = "INSERT INTO `panela` ( `marca`, `tipo`, `valor`) VALUES (?,?,?)"

values_to_insert = [('pin','comum',12.30),
					('tramontina', 'pressão', 99.80),
					('confiLar', 'fritadeira', 24.90)]

c.executemany(sql_many_inserts, values_to_insert)

c.commit()
