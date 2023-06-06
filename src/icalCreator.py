from icalendar import Calendar


def create_ical(data):
    # init the calendar
    cal = Calendar()

    # Some properties are required to be compliant
    cal.add('prodid', '-//Fristen und Termine der Hoschule München//hm.edu//')
    cal.add('version', '2.0')

    for event in data:
        if event.end is None:
            event.end = event.start.replace(minute=59, hour=23, second=59)
