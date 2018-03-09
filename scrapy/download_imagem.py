import requests

url = 'http://st2.depositphotos.com/1514397/5893/i/450/depositphotos_58937687-Woman-putting-roller-skates.jpg'

r = requests.get(url)

with open('img.jpg', 'wb') as f:
	f.write(r.content)