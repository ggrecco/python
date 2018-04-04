import sqlite3

class Cvedetails(object):
    def __init__(self):
        self.table = "cvedetails"
        self.conn = sqlite3.connect('cvedetails.db')
        self.c = self.conn.cursor()

    def listarTodos(self):
        sql = "SELECT * FROM "+self.table
        self.c.execute(sql)
        dados = self.c.fetchall()
        return dados

    def inserir(self, cveid, tipo, datacorrecao, nota, acesso, comentarios):
        sql = "INSERT INTO "+ self.table +" (cveid, tipo, datacorrecao, nota, acesso, comentarios) VALUES (?,?,?,?,?,?)"
        self.c.execute(sql,( cveid, tipo, datacorrecao, nota, acesso, comentarios))
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
