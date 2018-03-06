import sqlite3

class Login(object):
    def __init__(self): # método construtor
        self.table = "login"
        self.conn = sqlite3.connect('login.db')
        self.c = self.conn.cursor()

    def busca(self,usuario):
        sql = " SELECT * FROM " +self.table+ " where usuario=? "
        self.c.execute(sql,(usuario,))
        dados = self.c.fetchone()
        return dados
