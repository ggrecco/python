import sqlite3
c = sqlite3.connect('prova.db')

tabela_medicos="""CREATE TABLE medicos (
	id integer primary key,
	nome varchar(255),
	crm integer,
	especialidade varchar(255),
	endereco varchar(255),
	valor_consulta real)"""

c.execute(tabela_medicos)

sql_many_inserts = "INSERT INTO `medicos` ( `nome`, `crm`, `especialidade`,`endereco`, `valor_consulta`) VALUES (?,?,?,?,?)"

values_to_insert = [('Zé', 1, 'Nutricionista', 'casa do zé', 19.45),
					('Vinicius', 2, 'Psiquiatria', 'São Pedro', 19.23),
					('Felipe', 3, 'Ortopedista', 'casa dos pé', 18.99),
					('Gustavo', 4, 'Clinico Geral', 'Casa da Karim', 19.28)]

c.executemany(sql_many_inserts, values_to_insert)

c.commit()
