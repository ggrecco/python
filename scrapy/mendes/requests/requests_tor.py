from requests import Session

s = Session()
s.proxies = {'http': 'socks5h://127.0.0.1:60050'}

#com o tor
h = s.get('http://httpbin.org/ip')
print(h.json())
#sem tor
g = get('http://httpbin.org/ip')
print(g.json())
