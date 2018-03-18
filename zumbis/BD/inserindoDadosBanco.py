#Acesso para inserir dados
import sqlite3

con = sqlite3.connect('alunos.db')
cur = con.cursor()

x = True
while x is True:
    login = input("Login: ")
    matricula = input("Matricula:")
    cur.execute("insert into alunos values('"+ login +"', "+ matricula +")")
    continua = input("Continue[S/N]: ")
    if continua in "Nn":
        x = False
cur.execute("select * from alunos")

#mostra o que foi inserido
for x in cur.fetchall():
    print(x)

cur.close()
con.commit()
con.close()

