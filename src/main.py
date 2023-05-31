from DataParser import *
from WebParser import *
from exceptionHandler import *
from datetime import datetime


def json_object_assembler(webparser: WebParser, semester_num: int, semester_name: str):
    # create json for all events
    try:
        web_parser_list = webparser.get_dates(semester_num)

        # noinspection PyPep8
        json_object = {"semester_type": webparser.get_semester_type(semester_num),
                       "duration_of_semester": search_and_format(web_parser_list, "Dauer des Semesters"),
                       "lecture_period": search_and_format(web_parser_list, "Vorlesungszeit"),
                       "lecture_free_time": search_and_format(web_parser_list, "Vorlesungsfreie Zeit"),
                       "exam_registration": search_and_format(web_parser_list, "Prüfungsanmeldung"),
                       "exam_period_start": search_and_format(web_parser_list, "Prüfungszeitraum"),
                       "grades_release": search_and_format(web_parser_list, "Notenbekanntgabe"),
                       "re-registration_for_next_semester": search_and_format(web_parser_list, "Rückmeldung"),
                       "1-st_AW_subject_draw_lot": search_and_format(web_parser_list, "Belegung Online-Los-Durchgang I"),
                       "2-st_AW_subject_draw_lot": search_and_format(web_parser_list, "Belegung Online Losdurchgang II"),
                       "start_of_AW_lectures": search_and_format(web_parser_list, "Vorlesungsbeginn AW"),
                       "time_of_last_update": datetime.utcnow().isoformat(),
                       "recent_data": True
                       }

        json_creator(json_object, semester_name, "all")
        for item, data in json_object.items():
            json_creator({item: data}, semester_name, item)
    except AttributeError:
        parse_error()


# init web parser with url
try:
    web_parser = WebParser("https://www.hm.edu/studium_1/im_studium/mein_studium/verlauf/termine.de.html")
except requests.ConnectionError:
    raise connection_error()

json_object_assembler(web_parser, 0, "thisSemester")
json_object_assembler(web_parser, 1, "nextSemester")
