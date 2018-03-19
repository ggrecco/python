import requests


url = "https://www.cvedetails.com/vulnerability-search.php"

payload = {'bidno': '',
            'cveid': '',
            'cvssscoremax': '',
            'cvssscoremin': '',
            'cweid': '',
            'f':'1',
            'msid': '',
            'pem': '',
            'pey': '',
            'product':'mysql',
            'psm': '',
            'psy': '',
            'uem': '',
            'uey': '',
            'usm': '',
            'usy': '',
            'vendor': ''

}
response = requests.post(url, data = payload)

with open('retorno_mysql.html', 'w') as f:
    f.write(response.text)
