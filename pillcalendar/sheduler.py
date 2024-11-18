from datetime import date, timedelta, datetime


class Weekday:
    WEEKDAYS = {0: "Пн", 1: "Вт", 2: "Ср", 3: "Чт", 4: "Пт", 5: "Сб", 6: "Вс"}
    TIMEOFDAY = {0: "Утро", 1: "День", 2: "Вечер"}

    def __init__(self, weekdays: list, timeofday: list):
        self.weekday_index = []
        self.timeofday_index = []
        for itm in weekdays:
            for key, value in Weekday.WEEKDAYS.items():
                if value == itm:
                    self.weekday_index.append(key)
        for itm in timeofday:
            for key, value in Weekday.TIMEOFDAY.items():
                if value == itm:
                    self.timeofday_index.append(key)
        self.weekday_index.sort()
        self.timeofday_index.sort()

    @property
    def weekday_indx(self):
        return self.weekday_index

    @property
    def timeofday_indx(self):
        return self.timeofday_index


class Sheduler:
    def __init__(self, start: date, weekdays: Weekday, quantity: int, days=0, weeks=0):
        delta_days = int(weeks) * 7 + int(days)
        delta = timedelta(days=delta_days)
        self.start = start
        if delta_days > 1:
            self.end = self.start + delta - timedelta(days=1)
        else:
            self.end = self.start
        self.quantity = quantity
        self.weekdays = weekdays

    @property
    def end_date(self):
        return self.end
    
    @property
    def start_date(self):
        return self.start

    def requirement(self, start: date, end: date):
        requirement_quantity = 0
        if start <= self.end and end >= self.start:
            if end > self.end:
                end = self.end
            if start < self.start:
                start = self.start
            delta = end - start
            for day_increment in range(0, delta.days + 1):
                day = start + timedelta(days=day_increment)
                weekday_index = day.weekday()
                if weekday_index in self.weekdays.weekday_indx:
                    times = len(self.weekdays.timeofday_index)
                    requirement_quantity += self.quantity * times
        return requirement_quantity

    def shedule(self, start: date, end: date): 
        timeline = []
        shedule = dict()
        requirement_quantity = 0
        if start <= self.end and end >= self.start:
            if end > self.end:
                end = self.end
            if start < self.start:
                start = self.start
            delta = end - start
            for day_increment in range(0, delta.days + 1):
                day = start + timedelta(days=day_increment)
                weekday_index = day.weekday()
                shedule_day = []
                # print(f'{Weekday.WEEKDAYS.get(weekday_index)} {day}')
                if weekday_index in self.weekdays.weekday_indx:
                    shedule_day.extend(
                        [
                            f"{Weekday.WEEKDAYS.get(weekday_index)}",
                            f"{day}",
                            f"{self.quantity * len(self.weekdays.timeofday_index)}",
                        ]
                    )
                    for timeofday_index in self.weekdays.timeofday_indx:
                        shedule_day.extend(
                            [
                                f"{Weekday.TIMEOFDAY.get(timeofday_index)}",
                                f"{self.quantity}",
                            ]
                        )
                        # print(f'{Weekday.TIMEOFDAY.get(timeofday_index)} {self.quantity}')
                    shedule[day] = shedule_day
            timeline.extend(shedule.items())
            timeline.sort()
            return timeline

    def __str__(self):
        shed_lst = []
        for t_indx in self.weekdays.timeofday_indx:
            shed_lst.append(Weekday.TIMEOFDAY.get(t_indx))
        for w_indx in self.weekdays.weekday_indx:
            shed_lst.append(Weekday.WEEKDAYS.get(w_indx))
        return " ".join(shed_lst)
