class Pill:
    def __init__(self, name, shedule: Shedule):
        self.name = name
        self.shedule = shedule

    def __str__(self):
        return f"Препарат {self.name}, прием {self.shedule}"

    def __repr__(self):
        return f"{self.__class__.__name__} {self.name}"

    def check(self, check_date: date):
        wk_time = []
        wk_day = check_date.weekday()
        if self.shedule.start_date <= check_date <= self.shedule.end_date:
            sh_d = self.shedule.week_days[wk_day]
            if sh_d.is_fullday is True or sh_d.is_on is True:
                return True, [
                    itm
                    for i, itm in zip(
                        [sh_d.morning, sh_d.noon, sh_d.evening], TIMEOFDAY
                    )
                    if i == True
                ]
        return False, None
