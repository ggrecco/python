conn = sqlite3.connect("automoveis.db")
c = conn.cursor()

@route('/')
def index():
    tpl = 'Hello, Buddy!{{d}} You are at marcas app. If you want to see the content, click here'
    d = ''
    return template(tpl,d=d)

@route('/marcas')
def index():
    sql = "select * from marcas"
    c.execute(sql)
    dados = c.fetchall()
    tpl_lst = """
            Marcas
				% for dado in dados:
				{{dado[0]}} | {{dado[1]}} | {{dado[2]}} | {{dado[3]}} | {{dado[4]}} |
				% end
			"""
    return template(tpl_lst, dados=dados)

run(host='localhost', port=7000)
