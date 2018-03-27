import sqlite3
from bottle import route, run, template

class Marcas(object):
    def __init__(self): # método construtor
        self.table = "marcas"
        self.conn = sqlite3.connect('automoveis.db')
        self.c = self.conn.cursor()

    def listarTodos(self):
        sql = "SELECT * FROM "+self.table
        self.c.execute(sql)
        dados = self.c.fetchall()
        return dados

    def inserir(self,nome,origem,presidente,fundacao):
        sql = "INSERT INTO "+self.table+" (nome,origem,presidente,fundacao) VALUES (?,?,?,?)"
        self.c.execute(sql,(nome,origem,presidente,fundacao))
        self.conn.commit()

    def listar1(self,id):
        sql= " SELECT * FROM " +self.table+ " where id=? "
        self.c.execute(sql,(id,))
        dados=self.c.fetchone()
        return dados

    def alterar(self,id,nome,origem,fundacao,presidente):
        sql=" UPDATE "+self.table+" set nome=?,origem=?,fundacao=?,presidente=? where id=?"
        self.c.execute(sql,(nome,origem,fundacao,presidente,id))
        self.conn.commit()

    def deletar(self,id):
        sql = " DELETE FROM " + self.table + " WHERE id = ?"
        self.c.execute(sql,(id,))
        self.conn.commit()
