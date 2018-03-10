import sqlite3
c = sqlite3.connect('automoveis.db')

tabela_marcas="""create table marcas (
	id integer primary key,
	nome text,
	origem text,
	presidente text,
	fundacao text)"""

c.execute(tabela_marcas)

sql_many_inserts = "INSERT INTO `marcas` ( `nome`, `origem`, `presidente`,`fundacao`) VALUES (?,?,?,?)"

values_to_insert = [('Volkswagen', 'Alemanha', 'Schmitt', 1936),
					('Mercedes', 'Alemanha', 'Wolfgang', 1923),
					('Ford', 'Estados Unidos', 'Henry', 1922),
					('Maserati', 'Italia', 'Filipetto', 1948),
					('Ferrari', 'Italia', 'Enzo', 1899),
					('Audi', 'Alemanha', 'Werner', 1928)]

c.executemany(sql_many_inserts, values_to_insert)

c.commit()
