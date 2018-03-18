from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.globo.com")
objeto = BeautifulSoup(html.read(), "html.parser")

for link in objeto.find_all("a"):
    print(link.get("href"))
