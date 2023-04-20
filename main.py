import requests
from bs4 import BeautifulSoup
import json

url = "https://www.hm.edu/studium_1/im_studium/mein_studium/verlauf/termine.de.html"


# Laden der Webseite
page = requests.get(url)

# Extrahieren des HTML-Inhalts
soup = BeautifulSoup(page.content, 'html.parser')

# Suchen der Tabelle im HTML
table = soup.find_all('table')[0]
# table = soup.find('table', class_='table paragraph-with-links')

# Extrahieren der Tabellenzeilen
rows = table.find_all('tr')

# Initialisieren des leeren Arrays, um die Daten zu speichern
data = []

# Iterieren über die Tabellenzeilen und extrahieren der Daten
for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Ausgabe des Arrays mit den Daten
print(data)


def check_if_exists(stringToFind, arrayToSearch):
    if stringToFind in arrayToSearch:
        return ()
    else:
        print(str(stringToFind) + ' is not present in the list')