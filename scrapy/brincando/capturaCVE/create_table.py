import sqlite3

c = sqlite3.connect('captura.db')

tabela_captura = """CREATE TABLE captura(
id integer primary key,
nota varchar(50),
comentarios varchar(5000)
)"""

c.execute(tabela_captura)

sql = "INSERT INTO `captura`(`nota`,`comentarios`) VALUES (?,?)"

v_insert = [('1','teste de inserção de comentarios na tabela')]

c.executemany(sql, v_insert)

c.commit()
