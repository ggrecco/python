import sqlite3

class Cve(object):
    def __init__(self):
        self.table = "cve"
        self.conn = sqlite3.connect('cve.db')
        self.c = self.conn.cursor()

    def listarTodos(self):
        sql = "SELECT * FROM "+self.table
        self.c.execute(sql)
        dados = self.c.fetchall()
        return dados

    def inserir(self, nota, comentarios):
        sql = "INSERT INTO "+ self.table +" (nota, comentarios) VALUES (?,?)"
        self.c.execute(sql,( nota, comentarios))
        self.conn.commit()

    def listar1(self,id):
        sql= " SELECT * FROM " +self.table+ " where id=? "
        self.c.execute(sql,(id,))
        dados=self.c.fetchone()
        return dados

    def alterar(self,id, nota, comentarios):
        sql=" UPDATE "+self.table+" set nota=?,comentarios=? where id=?"
        self.c.execute(sql,( nota, comentarios,id))
        self.conn.commit()

    def deletar(self,id):
        sql=" DELETE FROM " +self.table+" where id=? "
        self.c.execute(sql,(id,))
        self.conn.commit()
