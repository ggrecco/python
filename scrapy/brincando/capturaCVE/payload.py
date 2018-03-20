import requests
from requests import post, get
from bs4 import BeautifulSoup as bs

def busca_tabelas():
    url = "https://www.cvedetails.com/vulnerability-search.php"

    linguagem = 'php'

    payload = {'bidno': '',
                'cveid': '',
                'cvssscoremax': '',
                'cvssscoremin': '',
                'cweid': '',
                'f':'1',
                'msid': '',
                'pem': '',
                'pey': '',
                'product': linguagem,
                'psm': '',
                'psy': '',
                'sp[1]': '1',
                'uem': '',
                'uey': '',
                'usm': '',
                'usy': '',
                'vendor': ''

    } #sp[1] : 1 indica que está selecionado a caixa Admin Acess 

    response = requests.post(url, data = payload)

    pagina = bs(response.content, 'lxml')

    return pagina
