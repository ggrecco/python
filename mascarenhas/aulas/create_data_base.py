import sqlite3

c = sqlite3.connect('cvedetails.db')

sql_many_inserts = "INSERT INTO `login` ( `nome`, `senha`, `email`) VALUES (?,?,?)"

values_to_insert = [('teste2','202cb962ac59075b964b07152d234b70','teste2@teste')]

c.executemany(sql_many_inserts,values_to_insert)

c.commit()