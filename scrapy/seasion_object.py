import requests

url = 'http://www.submarino.com.br/'

s = requests.Session()
s.get(url)

busca = 'notebook'
url = 'http://busca.submarino.com.br/busca.php?q={0}'.format(busca)

r = s.get(url)
with open('submarino.html', 'w') as f:
	f.write(r.text)