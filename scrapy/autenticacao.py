import requests

url = 'http://httpbin.org/basic-auth/user/passwd'

r = requests.get(url)
print(r.status_code)

r = requests.get(url, auth=('user', 'passwd'))
print(r.status_code)

