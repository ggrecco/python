import sqlite3

class Panelas(object):
    def __init__(self):
        self.table = "panela"
        self.conn = sqlite3.connect('login.db')
        self.c = self.conn.cursor()

    def listarTodos(self):
        sql = "SELECT * FROM "+self.table
        self.c.execute(sql)
        dados = self.c.fetchall()
        return dados

    def inserir(self,marca,tipo,valor):
        sql = "INSERT INTO "+ self.table +" (marca,tipo,valor) VALUES (?,?,?)"
        self.c.execute(sql,(marca,tipo,valor))
        self.conn.commit()

    def listar1(self,id):
        sql= " SELECT * FROM " +self.table+ " where id=? "
        self.c.execute(sql,(id,))
        dados=self.c.fetchone()
        return dados

    def alterar(self,id,marca,tipo,valor):
        sql=" UPDATE "+self.table+" set marca=?,tipo=?, valor=? where id=?"
        self.c.execute(sql,(marca,tipo,valor,id))
        self.conn.commit()

    def deletar(self,id):
        sql=" DELETE FROM " +self.table+" where id=? "
        self.c.execute(sql,(id,))
        self.conn.commit()
