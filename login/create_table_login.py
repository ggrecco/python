import sqlite3
c = sqlite3.connect('login.db')

tabela_login="""CREATE TABLE login (
	id integer primary key,
	usuario varchar(255),
	senha varchar(255))"""

c.execute(tabela_login)

sql_many_inserts = "INSERT INTO `login` ( `usuario`, `senha`) VALUES (?,?)"

values_to_insert = [('gustavo@teste','123'),
					('karim@teste', 'python'),
					('ze@teste', '123')]

c.executemany(sql_many_inserts, values_to_insert)

c.commit()
