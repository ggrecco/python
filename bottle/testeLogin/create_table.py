import sqlite3
c = sqlite3.connect('login.db')

tabela_login="""CREATE TABLE login (
	id integer primary key,
	email varchar(255),
	senha varchar(225))"""

c.execute(tabela_login)


sql_many_inserts = "INSERT INTO `login` ( `teste@teste`, `123`) VALUES (?,?)"

values_to_insert = [('pin','comum'),
					('tramontina', '123'),
					('confiLar', '123')]

c.executemany(sql_many_inserts, values_to_insert)


c.commit()
