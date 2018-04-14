import sqlite3

class Cve(object):
    def __init__(self):
        self.table = "cvedetails"
        self.conn = sqlite3.connect('cvedetails.db')
        self.c = self.conn.cursor()

    def listarTodos(self):
        sql = "SELECT * FROM "+self.table
        self.c.execute(sql)
        dados = self.c.fetchall()
        return dados

    def inserir(self, produto, cveid, tipo, datacorrecao, nota, acesso, comentarios):
        sql = "INSERT INTO "+ self.table +" (produto, cveid, tipo, datacorrecao, nota, acesso, comentarios) VALUES (?,?,?,?,?,?,?)"
        self.c.execute(sql,(produto, cveid, tipo, datacorrecao, nota, acesso, comentarios))
        self.conn.commit()

    def listar1(self,id):
        sql= " SELECT * FROM " +self.table+ " where id=? "
        self.c.execute(sql,(id,))
        dados=self.c.fetchone()
        return dados

    def alterar(self,id,produto, cveid, tipo, datacorrecao, nota, acesso, comentarios):
        sql=" UPDATE "+self.table+" set roduto=? cveid=? tipo=? datacorrecao=? nota=? acesso=? comentarios=? where id=?"
        self.c.execute(sql,(produto, cveid, tipo, datacorrecao, nota, acesso, comentarios,id))
        self.conn.commit()

    def deletar(self,id):
        sql=" DELETE FROM " +self.table+" where id=? "
        self.c.execute(sql,(id,))
        self.conn.commit()

class Login(object):
    def __init__(self):
        self.table = "login"
        self.conn = sqlite3.connect('cvedetails.db')
        self.c = self.conn.cursor()

    def busca(self,email):
        sql = " SELECT * FROM " +self.table+ " where email=? "
        self.c.execute(sql,(email,))
        dados = self.c.fetchone()
        return dados
