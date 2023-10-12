from DataParser import *
from WebParser import *
from exceptionHandler import *
from icalCreator import *
from schedule import every, repeat, run_pending
import time
import sys

from eventSplitter import split_events


@repeat(every().day.at("02:00"))
def job():
    # init web parser with url
    try:
        web_parser = WebParser("https://www.hm.edu/studium_1/im_studium/mein_studium/verlauf/termine.de.html")
    except requests.ConnectionError:
        raise connection_error()
    try:
        event_list_thisSemester = event_creator(web_parser.get_dates(0))
        semester_name_thisSemester = web_parser.get_semester_type(0)
        event_list_nextSemester = event_creator(web_parser.get_dates(1))
        semester_type_nextSemester = web_parser.get_semester_type(1)
        # Hotfix to change to next semester if the end of the current semester duration is in the past
        for event in event_list_thisSemester:
            if event.title == "Dauer des Semesters" and event.dates[0].end < datetime.now():
                event_list_thisSemester = event_list_nextSemester
        
        json_object_assembler(event_list_thisSemester, "thisSemester", semester_name_thisSemester)
        json_object_assembler(event_list_nextSemester, "nextSemester", semester_type_nextSemester)
        create_ical(event_list_thisSemester)
        split_events(event_list_thisSemester)
        print("job run at", time.time())


    except:
        parse_error()


if __name__ == "__main__":
    job()
    try:
        while sys.argv[1] == "docker-mode":
            run_pending()
            time.sleep(120)
    except IndexError:
        exit(0)
