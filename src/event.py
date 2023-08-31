from dataclasses import dataclass
from dataclasses import field

import period
from singleDateEvent import SingleDateEvent


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

    def split(self) -> list[SingleDateEvent]:
        events = []
        for item in self.dates:
            events.append(SingleDateEvent(
                title=self.title,
                start=item.start,
                end=item.end
            ))

        return events
