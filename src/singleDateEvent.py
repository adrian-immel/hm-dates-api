from dataclasses import dataclass
from datetime import date


@dataclass
class SingleDateEvent:
    title: str
    start: date
    end: date