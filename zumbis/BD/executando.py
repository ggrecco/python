from acessoDB import db

nomeDB = "surfersDB.sdb"
sql = "select * from surfers where age < 25"
linhas = db(sql,nomeDB)
for linha in linhas:
    print("Nome....:", linha['name'])
    print("País....:", linha['country'])
    print("Média...:", linha['average'])
    print("Estilo..:", linha['board'])
    print("Idade...:", linha['age'])
    print()
