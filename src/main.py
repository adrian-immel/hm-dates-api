from WebParser import *
from DataParser import *
# todo code cleanup!
def jsonobjectassambler(webparser, semester_num, semester_name):
    # create json for all events
    web_parser_list = webparser.getdates(semester_num)
    json_object = {"semesterType": webparser.getsemestertype(semester_num),
                   "duration_of_semester": searchandformat(web_parser_list, "Dauer des Semesters"),
                   "lecture_period": searchandformat(web_parser_list, "Vorlesungszeit"),
                   "lecture_free_time": searchandformat(web_parser_list, "Vorlesungsfreie Zeit"),
                   "exam_registration": searchandformat(web_parser_list, "Prüfungsanmeldung"),
                   "exam_period_start": searchandformat(web_parser_list, "Prüfungszeitraum"),
                   "grades_release": searchandformat(web_parser_list, "Notenbekanntgabe"),
                   "re-registration_for_next_semester": searchandformat(web_parser_list, "Rückmeldung")
                   }

    jsoncreator(json_object, semester_name, "all")
    for item in json_object.items():
        jsoncreator(item, semester_name, item[0])


web_parser = WebParser("https://www.hm.edu/studium_1/im_studium/mein_studium/verlauf/termine.de.html")
jsonobjectassambler(web_parser, 0, "thisSemester")
jsonobjectassambler(web_parser, 1, "nextSemester")
