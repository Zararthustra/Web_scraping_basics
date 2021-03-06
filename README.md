![Alt Text](https://vence.fr/wp-content/uploads/2021/01/vaccination.jpg)

# Scraping all french covid vaccination centers

This personal project was motivated by the actual **COVID-19 sanitary crisis** and what I have just learnt about **web scraping** and **json serialization**.

The URL source is provided by [Sante.fr](https://www.sante.fr/cf/centres-vaccination-covid.html), the **official french government health web page**

/!\ *The link might be dead as the crisis goes by* /!\
## [covac.py](https://github.com/Zararthustra/Web_scraping_basics/blob/main/covac.py)
I've chosen to name this script "covac" that is a concatenation of "covid" and "vaccination".
This script was made with **Python3** and the **BeautifulSoup library**.
I added some comments to make the code more readable for anyone.

## [covac.json](https://github.com/Zararthustra/Web_scraping_basics/blob/main/covac.json)
A json file which can be manipulated by all programming languages.

Format:

**{'Department': [{center's address, name, phone, postal, city, url}]}**

## [human_readable_file.txt](https://github.com/Zararthustra/Web_scraping_basics/blob/main/human_readable_file.txt)
Its name is explicit. A file with a **clean print** of each department and centers associated.

Format:

=======================

 code postal - nom du département 
 
=======================


  Le département contient X centres de vaccinations:

 1 )	Nom du premier centre de vaccination

Adresse:	XXX

Code Postal:	XXX

Ville:		XXX

Téléphone:	XXX

Site web:	XXX
