from acessoDB import db

nomeDB = "surfersDB.sdb" #input("NomeBanco: ")
sql = "select * from surfers where age > 25" #input("SQL: ")
linhas = db(sql,nomeDB)
print("------------------------------------")   
for linha in linhas:
        print("Nome...:", linha['name'])
        print("Média..:", linha['average'])
        print()
print("------------------------------------")      
for linha in linhas:
    print("Nome....:", linha['name'])
    print("País....:", linha['country'])
    print("Média...:", linha['average'])
    print("Estilo..:", linha['board'])
    print("Idade...:", linha['age'])
    print()
