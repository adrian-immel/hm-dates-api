import json
import sys
import datefinder


def jsoncreator(data, folder: str, filename: str):
    """
    creates a Json files out of given data and saves them
    is used to create the static json api

    :param data: used to create json of
    :param folder: subfolder of root project directory
    :param filename:  filenme of the generaated json file
    :return: gives back the generated json created from the given data
    """

    json_object = json.dumps(data, indent=4)
    filename = (sys.path[0] + r'/../' + folder + '/' + filename + ".json")
    with open(filename, 'w') as f:
        f.write(json_object)
    return json_object


def searchandformat(list_to_search:list, string_to_search:str):
    """
    searches for string in first row of 2D list and formats the content of second row as date
    :param list_to_search: Wants 2D list to search through
    :param string_to_search: string that is searched for in list
    :return: list of all dates
    """
    return_list = []
    for value in list_to_search:
        if string_to_search in str(value[0]):
            # filter out "to be announced" cells and replace it with None
            if "wird zum Ende des" in str(value[1]):
                return_list = None
                break
            # extracts the dates
            date_list = [list(datefinder.find_dates(i)) for i in value[1]]
            for dates in date_list:
                # converts dates to format
                return_list.append([j.isoformat() for j in dates])
            break
    return return_list
