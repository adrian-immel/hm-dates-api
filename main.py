from WebParser import *
from DataParser import *

web_parser = WebParser("https://www.hm.edu/studium_1/im_studium/mein_studium/verlauf/termine.de.html")
print(web_parser.getdates(1))


