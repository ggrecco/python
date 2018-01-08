import sqlite3

#nome = input("Nome: ")#"alunos.db"
#sql = input("SQL:")#'create table alunos(login varchar(8), ra integer)'

con = sqlite3.connect(input("Nome: "))
cur = con.cursor()
cur.execute(input("SQL:"))
cur.close()
con.commit()
con.close()
