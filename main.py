import requests
from bs4 import BeautifulSoup
import re
import json

url = "https://www.hm.edu/studium_1/im_studium/mein_studium/verlauf/termine.de.html"
tableSelector = 0

# init BeautifulSoup
page = requests.get(url)
# needs to be done to fix wrong table annotation of webpage to work properly with BeautifulSoup
page = page.content.replace(b"/th", b"/td")
soup = BeautifulSoup(page, 'html.parser')

# find the div with the id "termine"
pageElement = soup.find("div", {"id": "termine"})

# find all Tables in the div
table = pageElement.find_all('table')[tableSelector]
# extract the Name of the Semester from the button
semesterType = [i.text for i in pageElement.findAll('button', class_='accordion-button collapsed')][tableSelector]
# extract the cells
rows = table.find_all('tr')

data = []
# iterate through cells and insert data in array
for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)


def searchandclean (listtosearch, stringtosearch):




    return
