import sqlite3

con = sqlite3.connect('usuarios.db')

#sql_many_inserts = "INSERT INTO `login` ( `nome`, `senha`, `email`) VALUES (?,?,?)"

#values_to_insert = [('teste2','202cb962ac59075b964b07152d234b70','teste2@teste')]

#con.executemany(sql_many_inserts,values_to_insert)

con.commit()
