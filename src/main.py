from DataParser import *
from WebParser import *
from exceptionHandler import *


def jsonobjectassambler(webparser: WebParser, semester_num: int, semester_name: str):
    # create json for all events
    try:
        web_parser_list = webparser.getdates(semester_num)

        json_object = {"semesterType": webparser.getsemestertype(semester_num),
                       "duration_of_semester": searchandformat(web_parser_list, "Dauer des Semesters"),
                       "lecture_period": searchandformat(web_parser_list, "Vorlesungszeit"),
                       "lecture_free_time": searchandformat(web_parser_list, "Vorlesungsfreie Zeit"),
                       "exam_registration": searchandformat(web_parser_list, "Prüfungsanmeldung"),
                       "exam_period_start": searchandformat(web_parser_list, "Prüfungszeitraum"),
                       "grades_release": searchandformat(web_parser_list, "Notenbekanntgabe"),
                       "re-registration_for_next_semester": searchandformat(web_parser_list, "Rückmeldung"),
                       "recentData": True
                       }

        jsoncreator(json_object, semester_name, "all")
        for item in json_object.items():
            jsoncreator(item, semester_name, item[0])
    except:
        parse_error()


# init web parser with url
try:
    web_parser = WebParser("https://www.hm.edu/studium_1/im_studium/mein_studium/verlauf/termine.de.html")
except requests.ConnectionError:
    raise connection_error()

jsonobjectassambler(web_parser, 0, "thisSemester")
jsonobjectassambler(web_parser, 1, "nextSemester")
