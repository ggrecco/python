from dml import *

def check_login(username,password):
    login = Login()
    d = {}
    dados = login.busca(username)

    if type(dados) is tuple:
        for dado in dados:
            d[dados[3]] = dados[2]

        if username in d.keys() and d[username] == password:
            return True
        return False
    else:
        return False
