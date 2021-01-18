import requests
from bs4 import BeautifulSoup

url = "https://www.sante.fr/centres-vaccination-covid.html/"
response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text)
    lis = soup.findAll('li')
    for li in lis:
        a = li.findAll('span')
        print(str(a) + '\n')
