from dataclasses import dataclass
from dataclasses import field

import period


@dataclass
class EventWithSingleDate:
    title: str
    date: period


@dataclass
class event:
    title: str
    dates: list[period] = field(default_factory=list)

    tag: str = None

    def __int__(self):
        self.dates = []

    def set_tag(self, tag_to_add: str):
        self.tag = tag_to_add

    def append(self, item_to_append):
        self.dates.append(item_to_append)

    def split(self) -> list[EventWithSingleDate]:
        events= []
        for item in self.dates:
            events.append(EventWithSingleDate(
                title=self.title,
                date=item,
            ))

        return events
