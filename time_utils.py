import datetime
from typing import List


'''
defines the timeout for each iteration
between 8:00 am and 9:00 am as well as 10:00 am and 11:00 am, polling time is 4 minutes
between 9:00 am and 10:00 am polling time is 2 minutes
'''


def set_timeout() -> float:
    now = datetime.datetime.now()
    if now.hour in (8, 10):
        return 4*60
    if now.hour == 9:
        return 2*60
    if now.hour < 16:
        return 20*60
    next_start = datetime.datetime(now.year, now.month, now.day, 8, 1)
    next_start += datetime.timedelta(days=1)
    return (next_start - now).total_seconds()


def concatenate_dates(datelist: List[str]) -> str:
    date_string = ''
    if len(datelist) == 0:
        return date_string
    for i in range(0, len(datelist) - 1):
        date_string += datelist[i].to_string() + ', '
    date_string += datelist[len(datelist) - 1].to_string()
    return date_string


class Date:
    def __init__(self, datestring: str):
        date_parts = datestring.split(".")
        self.day = int(date_parts[0])
        self.month = int(date_parts[1])
        self.year = int(date_parts[2])

    def equals_date(self, date) -> bool:
        return (self.day == date.day) and (self.month == date.month) and (self.year == date.year)

    def to_string(self) -> str:
        return f"{self.day}.{self.month}.{self.year}"
