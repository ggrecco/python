import requests

# url original https://www.youtube.com/results?search_query=python+scrapy

url = 'https://www.youtube.com/results?'

payload = {'search_query': 'python scrapy'}

r = requests.get(url, params = payload)

#print(r.text)
#print(r.url)
#print(r.enconding)
with open('captura_youtube.html', 'wb') as f:
    f.write(r.content)
