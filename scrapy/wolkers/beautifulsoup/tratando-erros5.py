from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.udemy.com")
bsObj = BeautifulSoup(html.read(), "html.parser")

try:
    resultado = bsObj.html.tag_nao_existente.outra_tag
except AttributeError as erro:
    print("A tag não foi encontrada")