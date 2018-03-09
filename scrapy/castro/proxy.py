import requests

#http://www.ultraproxies.com/
url = 'https://www.hide-my-ip.com/pt/proxylist.shtml'

proxies = {'http':'218.207.102.106:81'}

try:
	r = requests.get(url, proxies=proxies)
	print(r.status_code)
except requests.exceptions.ConnectionError as e:
	print(str(e))