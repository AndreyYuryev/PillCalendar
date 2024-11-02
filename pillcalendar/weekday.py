WEEKDAYS = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]


class Weekday:
    def __init__(self, start: date, weekdays: list, days=0, weeks=0):
        delta_days = int(weeks) * 7 + int(days)
        self.delta = timedelta(days=delta_days)
        self.start_date = start
        self.week_days = weekdays
        self.every_full_day = self.__check_week_days()

    def __str__(self):
        days = []
        if self.every_full_day is False:
            for i, item in enumerate(self.week_days, start=0):
                if item != SheduleDay():
                    days.append(WEEKDAYS[i])
            on_days = " ".join(days)
        else:
            on_days = " ".join(WEEKDAYS)
        return f'с {datetime.strftime(self.start_date, "%d.%m.%Y")} по {datetime.strftime(self.end_date, "%d.%m.%Y")} {on_days}'

    def __repr__(self):
        return f"Shedule {self.name} {self.every_full_day}"

    @property
    def end_date(self):
        return self.start_date + self.delta

    def __check_week_days(self):
        for item in self.week_days:
            if item.is_fullday is False:
                return False
        return True
