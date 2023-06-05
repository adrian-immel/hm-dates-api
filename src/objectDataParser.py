import datefinder

import event
import period


def event_creator(data_list: list):
    """
    creates list of event objects out of list from webparser
    :param data_list: list of data from webparser
    :return: list of element objects
    """
    return_list = []
    for value in data_list:
        event_filter = ["Einsichtnahme", "Antragsfrist", "Nach- und Umbelegung", "Antrag"]
        # skip cells without data and unimportant data
        if not value[1] or any([x in (value[0])[0] for x in event_filter]):
            continue

        new_event = event.event((value[0])[0])

        # filter out "to be announced" cells and replace it with None
        if "wird zum Ende des" in str(value[1]):
            new_event.dates = None
        else:
            # parse data_list into event and period
            for i in value[1]:
                new_period = period.period()
                date_list = list(datefinder.find_dates(i, first="day", strict=True))
                is_start = 1
                for date in date_list:
                    if is_start:
                        new_period.start = date.isoformat()
                        is_start = 0
                    else:
                        new_period.end = date.isoformat()

                new_event.append(new_period)
        return_list.append(new_event)
    return return_list


def set_tag(event_list: list, tag: str, string_to_search: str):
    """
    seaches for event and adds tag to it
    :param event_list: list with event objects
    :param tag: tag to set
    :param string_to_search: string to be searched
    :return: None
    """
    for event_object in event_list:
        if string_to_search in event_object.title:
            event_object.set_tag(tag)
