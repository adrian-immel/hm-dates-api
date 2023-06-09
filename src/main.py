from DataParser import *
from WebParser import *
from exceptionHandler import *
from icalCreator import *

# init web parser with url
try:
    web_parser = WebParser("https://www.hm.edu/studium_1/im_studium/mein_studium/verlauf/termine.de.html")
except requests.ConnectionError:
    raise connection_error()

try:
    event_list_thisSemester = event_creator(web_parser.get_dates(0))
    semester_name_thisSemester = web_parser.get_semester_type(0)
    event_list_nextSemester = event_creator(web_parser.get_dates(1))
    semester_type_nextSemester = web_parser.get_semester_type(1)
    json_object_assembler(event_list_thisSemester, "thisSemester", semester_name_thisSemester)
    json_object_assembler(event_list_nextSemester, "nextSemester", semester_type_nextSemester)
    create_ical(event_list_thisSemester)


except:
    parse_error()
