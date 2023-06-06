import json
import sys


def modify_json():
    """
    modifies json to make recent_data = false
    :return: None
    """
    semester_list = ["thisSemester", "nextSemester"]
    for i in semester_list:
        path = (sys.path[0] + r'/../' + i + "/all.json")
        with open(path, 'r') as f:
            file_content = f.read()
        parsed_json = json.loads(file_content)
        parsed_json.update({"recent_data": False})

        with open(path, 'w') as f:
            json.dump(parsed_json, f, indent=4)

        path = (sys.path[0] + r'/../' + i + "/recent_data.json")
        with open(path, 'w') as f:
            json.dump({"recent_data": False}, f, indent=4)


def connection_error():
    modify_json()
    print("Could not get webpage")
    exit()


def parse_error():
    modify_json()
    print("Could not parse webpage")
    exit()


class exceptionHandler(Exception):
    pass
