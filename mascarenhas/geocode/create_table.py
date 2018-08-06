import sqlite3
c = sqlite3.connect('populacao.db')
d = sqlite3.connect('mapa.db')

##### CRIA BANCO E TABELA POPULACAO
tabela_login="""CREATE TABLE `populacao` (
   id integer primary key,
  `ANO` integer(10) DEFAULT NULL,
  `EUA` integer(10) DEFAULT NULL,
  `BRA` integer(10) NOT NULL)"""

c.execute(tabela_login)

sql_many_inserts = "INSERT INTO `populacao` ( `ANO`, `EUA`, `BRA`) VALUES (?,?,?)"

values_to_insert = [(1800,5,3),(1810,7,3),
					(1820,10,4),(1830,13,5),(1840,17,6),(1850,23,8),
(1860,31,8),(1870,39,10),(1880,50,12),(1890,63,15),
(1900,76,17),(1910,92,22),(1920,106,30),(1930,123,35),
(1940,132,41),(1950,151,51),(1960,179,70),(1970,203,93),
(1980,227,120),(1990,249,149),(2000,281,170),(2010,308,190)]

c.executemany(sql_many_inserts, values_to_insert)

c.commit()

##### CRIA BANCO E TABELA MAPA

d.execute(''' create table mapa (
				id integer primary key, 
				nome varchar(255), 
				endereco varchar(255))''')
d.execute(''' insert into mapa 
				(nome, endereco) 
				values 
				("Audioberto","Zeferino Dias, 171 ,Porto Alegre"),
				("Humberto","Lidio Batista Soares, 700, Cachoeirinha"),
				("Felisberto","Flores da Cunha, 1508, Cachoeirinha"),
				("Roberto","Dorival Candido Luz de Oliveira, 3435, Gravatai")''')
d.commit()
