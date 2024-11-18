from datetime import date, timedelta, datetime
from pillcalendar.sheduler import Sheduler


class Pill:
    def __init__(self, name, sheduler: Sheduler):
        self.name = name
        self.sheduler = sheduler

    def __str__(self):
        return f"Препарат {self.name}, прием: {self.sheduler}"

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"
    
    def requirement(self, from_date: date, till_date: date):
        requirement = self.sheduler.requirement(start=from_date, end=till_date)
        return f"Потребность {self.name} - {requirement} штук"
    
    def shedule(self, from_date: date, till_date: date):
        timeline = self.sheduler.shedule(start=from_date, end=till_date)
        shedule_str = [f'График приема препарата {self.name}:']
        for item in timeline:
            shedule_str.append(' '.join(item[1]))
        return shedule_str
    
    def delivery(self):
        return f'Прием {self.name} c {self.sheduler.start_date} по {self.sheduler.end_date}'
    
    def end_date(self):
        return self.sheduler.end_date