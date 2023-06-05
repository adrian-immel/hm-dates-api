import datefinder

import event
import period


def event_creator(data_list: list, ):
    return_list = []
    for value in data_list:
        event_filter = ["Einsichtnahme", "Antragsfrist", "Manuelle Nach- und Umbelegung", "Antrag"]
        # skip cells without data
        if not value[1] or any([x in (value[0])[0] for x in event_filter]):
            continue

        new_event = event.event((value[0])[0])

        # filter out "to be announced" cells and replace it with None
        if "wird zum Ende des" in str(value[1]):
            new_event.dates = None
        else:
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


def set_tag(list_to_search: list, tag: str, string_to_search: str):
    for event_object in list_to_search:
        if string_to_search in event_object.title:
            event_object.set_tag(tag)
