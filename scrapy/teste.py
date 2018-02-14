#criando objetos com BeautifulSoup
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

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
##################################################
with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

#print(objeto.tag[atributo])
print(soup.p['class'])#imprime o conteúdo do attributo class=""
print(soup.p.attrs)#imprime os atributos da tag p
print(soup.a['href'])#imprime o conteúdo do atributo href=""
print(soup.a.get['href'])#evitando erros caso a tag não exista
################################################
with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'html5lib')

#print(soup.prettify())
#print(soup.get_text())#imprime o texto de todas as tags
#print(soup.p.get_text())#imprime o texto da tag p
print(soup.p.b.string)#imprime o texto dentro da tag pai e da tag filho
###################################################

with open('arquivo02.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

print(soup.title)
print(soup.a)
print(soup.a.img)
print(soup.td)
print(soup.tr.td)
print(soup.td.attrs)
print(soup.td['class'][0])
################################
'''
with open('arquivo02.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')
'''
print(soup.table.contents)#imprime todos os filhos da tag
print(len(soup.contents))#imprime o tamanho da lista contents
print(soup.table.contents[1])#imprime o elemento da segunda posição da lista
print(soup.table.contents[1].span)
print(soup.table.contents[1].span.string)#imprime somente o texto da tag span da posição 2 da lista

for child in soup.table.contents:#imprime os filhos de tr
    if child.name == 'tr':
        print(child)

for child in soup.footer.children: #imprime rodapé
    print(child)

for child in soup.footer.p.children:
    if child.name == 'a':
        print(child.get('href'))

for tag in soup.descendants:
    if isinstance(tag, NavigableString):
        print(tag)
    else:
        print(tag.name)
for tag in soup.descendants:
    if isinstance(tag, Tag):
        print(tag)
'''
for string in soup.aside.stripped_strings:#remove os espaços extra das strings
    print(repr(string))
