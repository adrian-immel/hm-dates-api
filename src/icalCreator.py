import sys

from ics import Calendar, Event


def create_ical(data: list):
    """
    crates ical files out of list of events
    :param: list of event objects
    :return: none
    """

    # init the calendar
    cal = Calendar()
    event_filter = ["lecture_free_time", "exam_registration", "lecture_period",
                    "grades_release", "AW_subject_draw_lot", "start_of_AW_lectures",
                    "exam_period_start", "re-registration_for_next_semester"]
    # modify data to make it better for the calendar
    for event in data:
        # if event.tag == "lecture_period":
        #    event.title = "Beginn der Vorlesungszeit"
        #    event.dates[0].end = event.dates[0].start.replace(minute=59, hour=23, second=59)
        if event.tag == "exam_period_start":
            event.title = "Beginn des Prüfungszeitraums"
            event.dates[0].end = event.dates[0].start.replace(minute=59, hour=23, second=59)
        if event.tag == "start_of_AW_lectures":
            event.title = "Vorlesungsbeginn AW-Lehrveranstaltungen"
            event.dates[0].end = event.dates[0].start.replace(minute=59, hour=23, second=59)

    for event in data:
        if not any([x == event.tag for x in event_filter]):
            continue

        for period in event.dates:
            # Add the ical_event to the calendar
            ical_event = Event()
            ical_event.name = event.title
            if period.end is None:  # add end date if not existent
                period.end = period.start.replace(minute=59, hour=23, second=59)
            ical_event.begin = period.start
            ical_event.end = period.end
            ical_event.make_all_day()
            cal.events.add(ical_event)
    # write ical to file
    filename = (sys.path[0] + r'/../' + "ical" + '/' + "calendar.ics")
    with open(filename, 'w') as f:
        f.write(cal.serialize())
