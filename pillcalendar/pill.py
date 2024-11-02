from pillcalendar.sheduler import Sheduler, Weekday


class Pill:
    def __init__(self, name, sheduler: Sheduler):
        self.name = name
        self.sheduler = sheduler

    def __str__(self):
        return f"Препарат {self.name}, прием: {self.sheduler}"

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"