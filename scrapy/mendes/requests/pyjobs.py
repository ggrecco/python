#codigo usa namedtuple para tratar os dados obtidos com BeautifulSoup
from collections import namedtuple
from requests import get
from bs4 import BeautifulSoup as bs
from pprint import pprint


def get_last_page(url: str) -> str:
    pyjobs = get(url)
    pyjobs_page = bs(pyjobs.text, 'html.parser')
    links = pyjobs_page.find('ul', {'class':'pagination'}).find_all('a')
    return max([link.get('href') for link in links])

def trata_strs(string: str) -> str:
    """remove rótulos de descrição das caixas"""
    return string.split(':')


def gen_jobs(url: str) -> namedtuple:
    pyjobs = get(url)
    pyjobs_page = bs(pyjobs.text, 'html.parser')
    boxes = pyjobs_page.find_all('div', {'class':'col-md-10'})

    for box in boxes:
        titulo = box.find('h3').text
        ps = box.find_all('p')
        empresa = ps[0].text
        tipo = ps[1].text
        local = ps[4].text

        yield vaga(trata_strs(titulo),trata_strs(empresa), trata_strs(tipo), trata_strs(local))


vaga = namedtuple('Vaga', 'Titulo empresa tipo local')

base_url = 'http://www.pyjobs.com.br/'
jobs = '{}jobs/'.format(base_url)
job_pages = '{}page='.format(jobs)


for job in gen_jobs(jobs):
    print(job)


last_page = int(get_last_page(jobs)[-1])
urls = ['{}{}'.format(job_pages, n) for n in range(1, last_page+1)]

for url in urls:
    pprint(list(gen_jobs(url)))

#for job in gen_jobs(jobs):
#    print(job)
