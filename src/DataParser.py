from datetime import datetime
from WebParser import *
from exceptionHandler import *
from objectDataParser import *


def json_creator(data, folder: str, filename: str):
    """
    creates a Json files out of given data and saves them
    is used to create the static json api

    :param data: used to create json of
    :param folder: sub-folder of root project directory
    :param filename:  filename of the generated json file
    :return: None
    """

    filename = (sys.path[0] + r'/../' + folder + '/' + filename + ".json")
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, default=lambda x: x.__dict__)


def json_object_assembler(webparser: WebParser, semester_num: int, semester_name: str):
    """
    creates a dict with all the json objects
    :param webparser: Webparser Object
    :param semester_num: semester table selector
    :param semester_name: name of the selected semester
    :return: None
    """
    try:
        web_parser_list = webparser.get_dates(semester_num)
        event_list = event_creator(web_parser_list)

        # noinspection PyPep8
        tags_dict = {
            "duration_of_semester": "Dauer des Semesters",
            "lecture_period": "Vorlesungszeit",
            "lecture_free_time": "Vorlesungsfreie Zeit",
            "exam_registration": "Prüfungsanmeldung",
            "exam_period_start": "Prüfungszeitraum",
            "grades_release": "Notenbekanntgabe",
            "re-registration_for_next_semester": "Rückmeldung",
            "1-st_AW_subject_draw_lot": "Belegung Online-Los-Durchgang I",
            "2-st_AW_subject_draw_lot": "Belegung Online Losdurchgang II",
            "start_of_AW_lectures": "Vorlesungsbeginn AW",
        }

        for key, value in tags_dict.items():
            set_tag(event_list, key, value)

        json_object = {
            "semester_type": webparser.get_semester_type(semester_num),
            "events": event_list,
            "time_of_last_update": datetime.utcnow().isoformat(),
            "recent_data": True
        }

        json_creator(json_object, semester_name, "all")
        json_creator({"semester_type": webparser.get_semester_type(semester_num), }, semester_name, "semester_type")
        json_creator({"time_of_last_update": datetime.utcnow().isoformat()}, semester_name, "time_of_last_update")
        json_creator({"recent_data": True}, semester_name, "recent_data")
        for item in event_list:
            if item.tag is not None:
                json_creator(item, semester_name, item.tag)
    except AttributeError:
        parse_error()
