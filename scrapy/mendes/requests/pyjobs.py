from requests import get

base_url = 'http://www.pyjobs.com.br/'
jobs = f'{base_url}jobs/'
job_pages = f'{jobs}page='

pyjobs = get(jobs)
pyjobs
