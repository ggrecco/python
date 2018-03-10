from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.udemy.com")
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.html.tag_nao_existente.outra_tag)