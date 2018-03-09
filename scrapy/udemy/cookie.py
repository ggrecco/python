import requests

url = 'https://www.submarino.com.br'

r = requests.get(url)

cookie = r.cookies.get_dict()

busca  = 'notebook'
url = 'https://www.submarino.com.br/busca?conteudo={0}'.format(busca)

r = requests.get(url, cookies = cookie)#faz a captura do cookie e envia na nova requisição

with open('submarino.html', 'w') as f:
    f.write(r.text)
