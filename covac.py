#!/usr/bin/python3

import requests
import json
from bs4 import BeautifulSoup

url = "https://www.sante.fr/cf/centres-vaccination-covid.html/"
response = requests.get(url)
dep_list = []
center_items = {}
json_dict = {}

# Check request and start scraping
if response.ok:
    web_page = BeautifulSoup(response.text, 'html.parser')
    departments = web_page.findAll('span', class_='departement')
    
    for department in departments:

        dep_list = [department.text]
        centers = department.next_sibling.children
        dep_len = len(department.text) + 2
        center_num = 0
        centers_num = len(list(department.next_sibling.children))

        # Append department name and number of centers in human_readable_file
        with open("human_readable_file.txt", mode="a", encoding="utf8") as f:
            f.write("{}\n {} \n{}\n\n Le département contient {} centres de vaccinations:\n\n".format('='*dep_len, department.text, '='*dep_len, centers_num))

        # Scrap center items (name, address, postal, city, phone, url)
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

            # Append center items to json_dict
            center_items = {"name": name, "address": address, "postal": postal, "city": city, "phone": phone, "url": center_url}
            json_dict[department.text] = center_items

            # Append center items in human_readable_file
            with open("human_readable_file.txt", mode="a", encoding="utf8") as f:
                f.write("\t{})\t{}\n\nAdresse:\t{}\nCode Postal:\t{}\nVille:\t\t{}\nTéléphone:\t{}\nSite web:\t{}\n\n".format(center_num, name, address, postal, city, phone, center_url))

# Create json file with all informations: {Department : {center's name, address, postal, city, phone, url}}
with open("covac.json", mode="w", encoding="utf8") as f:
    json.dump(json_dict, f)
