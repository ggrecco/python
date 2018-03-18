#scrapy e lista de dados da tabela
from collections import namedtuple
from requests import get
from bs4 import BeautifulSoup as bs

ep_strura = namedtuple('Episodios', 'temporada episodio nome')

url = 'https://pt.wikipedia.org/wiki/Lista_de_epis%C3%B3dios_de_Samurai_X'

request = get(url)

page = bs(request.content, 'lxml')
tables = page.findAll('table',{'class':'wikitable'})

#divisão tabela por temporada
temp_1, temp_2, temp_3 = tables

def get_rows(table):
    return table.findAll('tr')[1:]

#linhas das tabelas
tr1, tr2, tr3 = map(get_rows,[temp_1, temp_2, temp_3])
#tr1[0].find_all('td')[0].text #captura o nº epi
#tr1[0].find_all('td')[3].text #captura o nome do epi

def get_data(temp: int, rows: str) -> namedtuple:
    for row in rows:
        columns = row.find_all('td')
        ep = columns[0].text
        nome = columns[3].text
        yield ep_strura(temp, ep, nome)

#dados por linha de cada temporada
t1_data, t2_data, t3_data = map(lambda t: list(get_data(t[0], t[1])), enumerate([tr1, tr2, tr3],1))

#lista todos Episodios
lista_episodios = sum([t1_data, t2_data, t3_data], [])
