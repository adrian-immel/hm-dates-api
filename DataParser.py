import json
import re


def jsonparser(object_array):
    return json.dumps(object_array, indent=4)


def searchandappend(list_to_search, string_to_search, array_to_append):
    i = list_to_search.indexOf(string_to_search)
    # todo format the output and and clean output
    array_to_append.append(list_to_search[i:2])
    return array_to_append


class DataParser:
    pass
