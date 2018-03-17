#captura dados das tabelas no wikipédia
from requests import get
from bs4 import BeautifulSoup as bs

url = 'https://pt.wikipedia.org/wiki/Lista_de_epis%C3%B3dios_de_Samurai_X'

request = get(url)

page = bs(request.content, 'lxml')
tables = page.findAll('table',{'class':'wikitable'})

temp_1, temp_2, temp_3 = tables

def get_rows(table):
    return table.findAll('tr')[1:]


tr1, tr2, tr3 = map(get_rows,[temp_1, temp_2, temp_3])
