from DataParser import *
from WebParser import *
from exceptionHandler import *

# init web parser with url
try:
    web_parser = WebParser("https://www.hm.edu/studium_1/im_studium/mein_studium/verlauf/termine.de.html")
except requests.ConnectionError:
    raise connection_error()

json_object_assembler(web_parser, 0, "thisSemester")
json_object_assembler(web_parser, 1, "nextSemester")
