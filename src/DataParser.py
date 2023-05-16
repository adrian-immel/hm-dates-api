import json
import datefinder
import sys


def jsoncreator(data, semestertype, filename):
    json_object = json.dumps(data, indent=4)
    filename = (sys.path[0] + r'/../' + semestertype +  '/' + filename + ".json")
    with open(filename, 'w') as f:
        f.write(json_object)
    f.close()
    return json_object


def searchandformat(list_to_search, string_to_search):
    return_list = []
    for value in list_to_search:
        if string_to_search in value[0]:
            if "wird zum Ende des" in str(value[1]):
                return_list = None
                break
            date_list = [list(datefinder.find_dates(i)) for i in value[1]]
            for dates in date_list:
                return_list.append([j.isoformat() for j in dates])
            break
    return return_list
