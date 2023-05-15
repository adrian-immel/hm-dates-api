import json


def jsonparser(object_array):
    return json.dumps(object_array, indent=4)


def searchandappend(list_to_search, string_to_search):
    return_array = []
    for i in list_to_search:
        if string_to_search in i[0]:
            return_array = i
    # todo format the output and and clean output
    return return_array
