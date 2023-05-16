import requests
from bs4 import BeautifulSoup


class WebParser:
    page_element = None

    def __init__(self, url):
        # init BeautifulSoup
        page = requests.get(url)
        # needs to be done to fix wrong table annotation of webpage to work properly with BeautifulSoup
        page = page.content.replace(b"/th", b"/td")
#        page = page.replace(b"/br", b"\n")
        soup = BeautifulSoup(page, 'html.parser')
        # find the div with the id "termine"
        self.page_element = soup.find("div", {"id": "termine"})

    def getsemestertype(self, table_selector):
        # extract the Name of the Semester from the button
        semester_type = [i.text for i in self.page_element.findAll('button', class_='accordion-button collapsed')][
            table_selector]
        return semester_type.strip('\n')

    def getdates(self, table_selector):
        # find all Tables in the div

        table = self.page_element.find_all('table')[table_selector]

        # extract the cells
        rows = table.find_all('tr')
        return_array = []
        # iterate through cells and insert data in array
        for row in rows:
            cols = row.find_all('td')
            row = []
            for col in cols:
                cols = col.get_text(strip=True, separator='\n').splitlines()
                row.append(cols)
            return_array.append(row)
        return return_array
