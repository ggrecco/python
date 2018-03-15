from requests import get

base_url = 'http://www.pyjobs.com.br/'
jobs = '{}jobs/'.format(base_url)
job_pages = '{}page='.format(jobs)

pyjobs = get(jobs)
pyjobs
