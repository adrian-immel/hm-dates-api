import json
import sys

import jsonpickle


def split_events(data: list):
    events = []

    for event in data:
        events.extend(event.split())

    filename = (sys.path[0] + r'/../dates-api/thisSemester/split.json')
    with open(filename, 'w') as f:
        f.write(jsonpickle.encode(events, unpicklable=False, indent=4))
