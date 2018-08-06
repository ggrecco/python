import sqlite3
c = sqlite3.connect('populacao.db')

tabela_login = """CREATE TABLE `pais` (
   id integer primary key,
  `Nome` varchar(200) DEFAULT NULL,
  `Endereco` varchar(200) DEFAULT NULL)"""

c.execute(tabela_login)

sql_many_inserts = "INSERT INTO `pais` ( `Nome`, `Endereco`) VALUES (?,?)"

values_to_insert = [("Gustavo", "rua lidio batista soares, 700"),
                    ("ze", "rua flores da cunha, 700")]

c.executemany(sql_many_inserts, values_to_insert)

c.commit()
