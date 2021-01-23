import requests
import json
from bs4 import BeautifulSoup

url = "https://www.sante.fr/centres-vaccination-covid.html/"
response = requests.get(url)
dep_list = []
center_list = [[]]
_dict = {}

if response.ok:
    web_page = BeautifulSoup(response.text, 'html.parser')
    departments = web_page.findAll('span', class_='departement')
    
    for department in departments:

        dep_list = [department.text]
        centers = department.next_sibling.children
        dep_len = len(department.text) + 2
        center_num = 0
        centers_num = len(list(department.next_sibling.children))
        
        #print("{}\n {} \n{}\n\n Le département contient {} centres de vaccinations:\n"\
#                .format('='*dep_len, department.text, '='*dep_len, centers_num))

        for center in centers:

            center_num += 1

            if center.find('span', class_='nom'):
                name = center.find('span', class_='nom').text
            else:
                name = "Nom inconnu"
            if center.find('span', class_='addresse'):
                address = center.find('span', class_='addresse').text
            else:
                address = "Adresse inconnue"
            if center.find('span', class_='codePostal'):
                postal = center.find('span', class_='codePostal').text
            else:
                postal = "Code postal inconnu"
            if center.find('span', class_='ville'):
                city = center.find('span', class_='ville').text
            else:
                city = "Ville inconnue"
            if center.find('span', class_='telephone fixe'):
                phone = center.find('span', class_='telephone fixe').find('a').text
            else:
                phone = "Numero inconnu"
            if center.find('span', class_='siteWeb'):
                center_url = center.find('span', class_='siteWeb').find('a')['href']
            else:
                center_url = "Site web inconnu"

            center_list = [[name, address, postal, city, phone]]
            for i in center_list:
                _dict[dep_list].append(i)

        center_list = [[]]
#            print("\t{})\t{}\n\nAdresse:\t{}\nCode Postal:\t{}\nVille:\t\t{}\nTéléphone:\t{}\
#                    \nSite web:\t{}\n\n".format(center_num, name, address, postal, city, phone, center_url))
print(_dict)
