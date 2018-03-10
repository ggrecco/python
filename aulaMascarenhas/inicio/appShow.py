import sqlite3
from bottle import route, run, template

conn = sqlite3.connect("automoveis.db")
c = conn.cursor()

@route('/')
def index():
    d = ''
    tpl = 'Hello, Buddy!{{d}} You are at marcas app. If you want to see the content, click here'
    return template(tpl,d=d)


@route('/marcas')
def index():
    sql = "select * from marcas"
    c.execute(sql)
    dados = c.fetchall()
    tpl_lst = """
        <h3>Marcas</h3>
        <table border="1">
        <thead>
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Origem</th>
            <th>presidente</th>
            <th>Fundação</th>
        </tr>
        </thead>
        <hr>
            % for dado in dados:
            <tr>
                <td>{{dado[0]}}</td>
                <td>{{dado[1]}}</td>
                <td>{{dado[2]}}</td>
                <td>{{dado[3]}}</td>
                <td>{{dado[4]}}</td>
            </tr>
            % end
        </table>
            """
    return template(tpl_lst, dados=dados)

run(host='localhost', port=7000, reloader = True)
