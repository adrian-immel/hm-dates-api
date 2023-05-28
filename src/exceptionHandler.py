import sys
import json


def modify_json():
    semester_list = ["thisSemester", "nextSemester"]
    for i in semester_list:
        path = (sys.path[0] + r'/../' + i + "/all.json")
        with open(path, 'r') as f:
            file_content = f.read()
        parsed_json = json.loads(file_content)
        parsed_json.update({"recentData": False})

        with open(path, 'w') as f:
            f.write(json.dumps(parsed_json, indent=4))

        path = (sys.path[0] + r'/../' + i + "/recentData.json")
        with open(path, 'w') as f:
            f.write(json.dumps({"recentData": False}, indent=4))


def connection_error():
    modify_json()
    raise "Could not get webpage"


def parse_error():
    modify_json()
    raise ValueError("Could not parse webpage")


class exceptionHandler(Exception): pass
