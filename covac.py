#!/usr/bin/python3

import requests
import sys
import json
from bs4 import BeautifulSoup

# Check if request OK, else exit
try:
    response = requests.get("https://www.sante.fr/cf/centres-vaccination-covid.html/")
except:
    sys.stderr.write('Request not OK')
    sys.exit(1)

web_page = BeautifulSoup(response.text, 'html.parser')
departments = web_page.findAll('span', class_='departement')
json_dict = {}

# Loop in "departement" class
for department in departments:

    centers = department.next_sibling.children
    dep_len = len(department.text) + 2
    center_num = 0
    centers_num = len(list(department.next_sibling.children))
    centers_list = []

    # Append department name + number of centers inside the department, into human_readable_file
    with open("human_readable_file.txt", mode="a", encoding="utf8") as f:
        f.write("{}\n {} \n{}\n\n Le département contient {} centres de vaccinations:\n\n".format('='*dep_len, department.text, '='*dep_len, centers_num))

    # Nested loop to get each center inside department
    for center in centers:

        center_num += 1
        
        name = center.find('span', class_='nom').text if center.find('span', class_='nom') else "Nom inconnu"
        address = center.find('span', class_='addresse').text if center.find('span', class_='addresse') else "Adresse inconnue"
        postal = center.find('span', class_='codePostal').text if center.find('span', class_='codePostal') else "Code postal inconnu"
        city = center.find('span', class_='ville').text if center.find('span', class_='ville') else "Ville inconnue"
        phone = center.find('span', class_='telephone fixe').find('a').text if center.find('span', class_='telephone fixe') else "Numero inconnu"
        center_url = center.find('span', class_='siteWeb').find('a')['href'] if center.find('span', class_='siteWeb') else "Site web inconnu"

        # Append all centers and their items into json_dict: key="department.text": value=centers_list
        items_dict = {"name": name, "address": address, "postal": postal, "city": city, "phone": phone, "url": center_url}
        centers_list.append(items_dict)
        json_dict[department.text] = centers_list

        # Append all centers and their items into human_readable_file: center's number, name, address, postal, city, phone and url.
        with open("human_readable_file.txt", mode="a", encoding="utf8") as f:
            f.write("\t{})\t{}\n\nAdresse:\t{}\nCP:\t\t{}\nVille:\t\t{}\nTéléphone:\t{}\nSite web:\t{}\n\n".format(center_num, name, address, postal, city, phone, center_url))

# Create json file with all informations: {Department: [{first center and its items}, {second center and its items}, {etc...}]}
with open("covac.json", mode="w", encoding="utf8") as f:
    json.dump(json_dict, f)
