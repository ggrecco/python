import sqlite3

sql = "select * from surfers where age > 25"
nomeDB = "surfersDB.sdb"
banco = sqlite3.connect(nomeDB)
banco.row_factory = sqlite3.Row
cursor = banco.cursor()
cursor.execute(sql)
linhas = cursor.fetchall()
for linha in linhas:
    print("Nome....:", linha['name'])
    print("País....:", linha['country'])
    print("Média...:", linha['average'])
    print("Estilo..:", linha['board'])
    print("Idade...:", linha['age'])
    print()
cursor.close()

