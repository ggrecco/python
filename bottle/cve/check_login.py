from dml import *
import hashlib

def check_login(username,password):
    login = Login()
    d = {}
    senha = hashlib.md5(password.encode())
    senha = senha.hexdigest()

    dados = login.busca(username)

    if type(dados) is tuple:
        for dado in dados:
            d[dados[3]] = dados[2]

        if username in d.keys() and d[username] == senha:
            return True
        return False
    else:
        return False
