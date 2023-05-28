import requests
from bs4 import BeautifulSoup


class WebParser:
    page_element = None

    def __init__(self, url: str):
        """
        fetches and parses webpage
        :param url: webpage to parse
        """
        # init BeautifulSoup
        page = requests.get(url)
        # needs to be done to fix wrong table annotation of webpage to work properly with BeautifulSoup
        page = page.content.replace(b"/th", b"/td")
        #        page = page.replace(b"/br", b"\n")
        soup = BeautifulSoup(page, 'html.parser')
        # find the div with the id "termine"
        self.page_element = soup.find("div", {"id": "termine"})

    def getsemestertype(self, table_selector: int):
        """
        gives back the semester type of the given num of table on webpage
        0 = cur. sem. 1 = next sem.
        :param table_selector: specifies the tabel on webpage
        :return: name of semester
        """
        # extract the Name of the Semester from the button
        semester_type = [i.text for i in self.page_element.findAll('button', class_='accordion-button collapsed')][
            table_selector]
        return semester_type.strip('\n')

    def getdates(self, table_selector: int):
        """

        :param table_selector: specifies the tabel on webpage
        :return: all 2 rows of table as 2d list
        """
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
