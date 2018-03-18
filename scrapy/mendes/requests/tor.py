from requests import Session

s = Session()
s.get('http://www.google.com')
print(s.cookies)
