from requests import Session

s = Session()
s.proxies = {'http://127.0.0.1:60050': 'socks5'}

#com o tor
h = s.get('http://httpbin.org/ip')
print(h.json())
#sem tor
g = get('http://httpbin.org/ip')
print(g.json())
