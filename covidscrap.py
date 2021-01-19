# request is needed to make sure we can easily slurp remote page into a local text variable
import requests

# BeautifulSoup4 is an HTML parser so we can drill down into the HTML tree
from bs4 import BeautifulSoup

# slurp the remote page into a local variable
url = "https://www.sante.fr/centres-vaccination-covid.html/"
response = requests.get(url)

# sanity check to make sure remote page exists
if not response.ok:
    print('Page ' + url + ' does not exist')
    exit(-1)


pageContent = BeautifulSoup(response.text, 'html.parser')
allDepartments = pageContent.find_all('span', class_='departement')

for department in allDepartments:
    # the list of centers is right next to the name of the departement. We could get up to the parent and find
    # the <ul> tag to get the list of centers.
    allCenters = department.next_sibling.children
    print('Le département ' + department.text + ' contient ' + str(len(list(department.next_sibling.children))) + ' centres de vaccination')
    for center in allCenters:
        print( '\t'
              + center.find('span', class_='nom').text
              + '\n\t\t'
              + (center.find('span', class_='addresse').text if center.find('span', class_='addresse') else 'N/A')
              + ','
              + center.find('span', class_='codePostal').text
              + ' '
              + center.find('span', class_='ville').text
              + ' - '
              + (center.find('span', class_='telephone fixe').find('a').text if center.find('span', class_='telephone fixe') else 'N/A')
              + ' - '
              + str((center.find('span', class_='siteWeb').find('a')['href'] if center.find('span', class_='siteWeb') else 'N/A')))
    print()







