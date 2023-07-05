from datetime import datetime

import jsonpickle

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

    filename = (sys.path[0] + r'/../dates-api/' + folder + '/' + filename + ".json")
    json_object = jsonpickle.encode(data, unpicklable=False, indent=4)
    with open(filename, 'w') as f:
        f.write(json_object)
        # json.dump(data, f, indent=4, default=lambda x: x.__dict__)


def json_object_assembler(event_list, semester_type: str, semester_name: str):
    """
    creates a dict with all the json objects
    :param event_list: list of event objects
    :param semester_name: name of semester
    :param semester_type: type of the selected semester
    :return: None
    """

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
        "semester_type": semester_name,
        "events": event_list,
        "time_of_last_update": datetime.utcnow(),
        "recent_data": True
    }

    json_creator(json_object, semester_type, "all")
    json_creator({"semester_type": semester_name, }, semester_type, "semester_type")
    json_creator({"time_of_last_update": datetime.utcnow()}, semester_type, "time_of_last_update")
    json_creator({"recent_data": True}, semester_type, "recent_data")
    for item in event_list:
        if item.tag is not None:
            json_creator(item, semester_type, item.tag)
