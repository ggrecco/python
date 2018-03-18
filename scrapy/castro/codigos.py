#criando objetos com BeautifulSoup
import requests
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag

'''
with open('arquivo.html', 'r') as f:
    soup_string = BeautifulSoup(f.read(), 'html.parser')
print(soup_string)

####################################################
####### Captura pagina HTML apartir do link ########

r = requests.get('http://www.google.com')
soup = BeautifulSoup(r.text, 'lxml')
print(soup)

#####################################################
###### Abre e exibe o arquivo ######################
with open('arquivo.html', 'r') as f:
    soup_string = BeautifulSoup(f.read(), 'html5lib')

print(soup_string)

######################################################
######### exibe as tags e seu conteúdo ###############
with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

tag = soup.title
print(tag)
print(tag.name)

tag = soup.p
print(tag.name)

##################################################
####### imprimindo conteudo das tags #############

with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

#print(objeto.tag[atributo])
print(soup.p['class'])#imprime o conteúdo do attributo class=""
print(soup.p.attrs)#imprime os atributos da tag p
print(soup.a['href'])#imprime o conteúdo do atributo href=""
print(soup.a.get['href'])#evitando erros caso a tag não exista

################################################
###### Imprimindo Texto das Tags #############

with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'html5lib')

#print(soup.prettify())
#print(soup.get_text())#imprime o texto de todas as tags
#print(soup.p.get_text())#imprime o texto da tag p
print(soup.p.b.string)#imprime o texto dentro da tag pai e da tag filho

###################################################
####
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

with open('arquivo02.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

print(soup.table.contents)#imprime todos os filhos da tag em uma lista
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
for string in soup.aside.stripped_strings:#remove os espaços extra das strings
    print(repr(string))

#############################################################################
###### acessando as tags pai ###################

with open('arquivo02.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

tag_tittle = soup.title
tag_tittle2 = soup.title.get_text()
print(tag_tittle)
print(tag_tittle.parent)#imprime o pai da tag title e a tag
print(tag_tittle2)#imprime o texto da tag
#############################################################################
######## acessando tags irmãs #################

with open('arquivo02.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

#print(soup.next_sibling)# não imprime nada pois não existe irmao para html
#print(soup.td.parent)#imprime o pai
#print(soup.td.next_sibling.next_sibling)#2 next_sibiling pois existe um espaço entre os td
#irmão próximos
for sibling in soup.p.next_siblings:
    print(repr(sibling))
#irmao anterior
for sibling in soup.p.previous_siblings:
    print(repr(sibling))
#################################################
###### Navegando entre elementos(tags)#######
with open('arquivo03.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

#print(soup.div.next_element.next_element)#2 next para pular tags acessada
for e in sup.ul.next_elements:
    if isinstance(e, Tag):
        print(e)
#########################################################
######## Função Find #################
with open('arquivo04.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')
#tag = soup.find('li')#procura tags li
#print(tag)
#tag = soup.find(string = 'plants')#procura pela string plants
#print(tag)
#tag = soup.find(id = "secondaryconsumers")#encontra pelo id
#print(tag)
#tag = soup.find(attrs = {'class' : 'primaryconsumerlist'})#encontra pela classe
#print(tag)
#tag = soup.find('li', attrs = {'class' : 'producerlist'})#filtro com mais de um elemento
#print(tag)

def is_secondary_consumers(tag):
    return tag.has_attr('id') and tag.get('id') == 'secondaryconsumers'
secondary_consumer = soup.find(is_secondary_consumers)
print(secondary_consumer.li.div.string)
#############################################################################
########## Função find_all ######################

with open('arquivo03.html', 'r') as f:
     soup = BeautifulSoup(f, 'lxml')
#tag_list = soup.find_all('ul')#imprime todas as ocorrencias ul em uma lista
#tag_list = soup.find_all(['ul', 'div'])
#tag_list = soup.find_all('ul', limit = 2)#limita em duas occorrencias
#tag_list = soup.find_all(string = 'rabbit')#procura a string
#tag_list = soup.find_all(string = True)#imprime todas as strings em formato de lista
#tag_list = soup.find_all(string = ['rabbit', 'bear'])#procura uma lista de string
#tag_list = soup.find_all(class_=['producerlist', 'primaryconsumerlist'])#procura pelas classes
tag_list = soup.ul.find_all('div')#procura por
print(tag_list)

##############################################################
################# Buscando elementos com o find_parents #########
with open('arquivo04.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')
primaryconsumers = soup.find_all(class_='primaryconsumerlist')
primaryconsumer = primaryconsumers[0]
print(primaryconsumer)
#################################################################
'''
