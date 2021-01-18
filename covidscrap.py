import requests
from bs4 import BeautifulSoup

url = "https://www.sante.fr/centres-vaccination-covid.html/"
response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text)
    span = soup.findAll('span')
    name = soup.find('span', {'class': 'nom'})

    for n in span:
        print(n.text + '\n')
