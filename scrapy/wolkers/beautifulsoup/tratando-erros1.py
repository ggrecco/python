from urllib.request import urlopen
from urllib.error import HTTPError

html = urlopen("http://www.udemy.com")
print(f"Html 1: {html}")

try:
    html = urlopen("http://www.udemy.com/erro")
    print(f"Html 2: {html}")
except HTTPError as erro:
    print(erro)

html = urlopen("http://www.udemy.com")
print(f"Html 3: {html}")
