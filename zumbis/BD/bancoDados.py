import sqlite3

a = "select * from surfers where age > 25"
b = "surfersDB.sdb"
banco = sqlite3.connect(b)
banco.row_factory = sqlite3.Row
cursor = banco.cursor()
cursor.execute(a)
linhas = cursor.fetchall()
for linha in linhas:
    print("Nome....:", linha['name'])
    print("País....:", linha['country'])
    print("Média...:", linha['average'])
    print("Estilo..:", linha['board'])
    print("Idade...:", linha['age'])
    print()
cursor.close()

