#criando objetos com BeautifulSoup
import requests
from bs4 import BeautifulSoup
'''
with open('arquivo.html', 'r') as f:
    soup_string = BeautifulSoup(f.read(), 'html.parser')
print(soup_string)
############################################
r = requests.get('http://www.google.com')
soup = BeautifulSoup(r.text, 'lxml')
print(soup)
##########################################
with open('arquivo.html', 'r') as f:
    soup_string = BeautifulSoup(f.read(), 'html5lib')

print(soup_string)
##########################################################
with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

tag = soup.title
print(tag)
print(tag.name)

tag = soup.p
print(tag.name)
#########
with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

#print(objeto.tag[atributo])
print(soup.p['class'])#imprime o conteúdo do attributo class=""
print(soup.p.attrs)#imprime os atributos da tag p
print(soup.a['href'])#imprime o conteúdo do atributo href=""
print(soup.a.get['href'])#evitando erros caso a tag não exista
############'''
with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'html5lib')

#print(soup.prettify())
#print(soup.get_text())#imprime o texto de todas as tags
#print(soup.p.get_text())#imprime o texto da tag p
print(soup.p.b.string)#imprime o texto dentro da tag pai e da tag filho
