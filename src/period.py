from dataclasses import dataclass
from datetime import date


@dataclass
class period:
    start: date = None
    end: date = None
