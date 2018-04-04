import sqlite3

c = sqlite3.connect('cvedetails.db')

tabela_cvedetails = """CREATE TABLE cvedetails(
id integer primary key,
cveid varchar(50),
tipo varchar(25),
datacorrecao varchar(50),
nota varchar(50),
acesso varchar(100),
comentarios varchar(5000)
)"""
#Update Date
#CVE ID
#score
#Gained Access Level
#Complexity

c.execute(tabela_cvedetails)

c.commit()
