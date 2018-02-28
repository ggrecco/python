import sqlite3

class Medicos(object):
    def __init__(self): # método construtor
        self.table = "medicos"
        self.conn = sqlite3.connect('prova.db')
        self.c = self.conn.cursor()

    def listarTodos(self):
        sql = "SELECT * FROM "+self.table
        self.c.execute(sql)
        dados = self.c.fetchall()
        return dados

    def inserir(self,nome,crm,especialidade,endereco,valor_consulta):
        sql = "INSERT INTO "+ self.table +" (nome,crm,especialidade,endereco,valor_consulta) VALUES (?,?,?,?,?)"
        self.c.execute(sql,(nome,crm,especialidade,endereco,valor_consulta))
        self.conn.commit()

    def listar1(self,id):
        sql= " SELECT * FROM " +self.table+ " where id=? "
        self.c.execute(sql,(id,))
        dados=self.c.fetchone()
        return dados

    def alterar(self,id,nome,crm,especialidade,endereco,valor_consulta):
        sql=" UPDATE "+self.table+" set nome=?,crm=?,especialidade=?,endereco=?, valor_consulta=? where id=?"
        self.c.execute(sql,(nome,crm,especialidade,endereco,valor_consulta,id))
        self.conn.commit()

    def deletar(self,id):
        sql=" DELETE FROM " +self.table+" where id=? "
        self.c.execute(sql,(id,))
        self.conn.commit()
