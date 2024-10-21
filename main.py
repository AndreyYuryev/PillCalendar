from datetime import date, timedelta, datetime

FULL_TIME = [True, True, True]
FULL_FALSE = [False, False, False]
FULL_DAYS = [FULL_TIME, FULL_TIME, FULL_TIME, FULL_TIME, FULL_TIME, FULL_TIME, FULL_TIME]
WEEKDAYS = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
TIMEOFDAY = ['Утро', 'День', 'Вечер']


class SheduleDay:
    def __init__(self, morning:bool=False, noon:bool=False, evening:bool=False):
        self.morning = morning
        self.noon = noon
        self.evening = evening
        
    def __str__(self):
        # wk_time = []
        # wk_time.extend([itm for i, itm in zip([self.morning, self.noon, self.evening], TIMEOFDAY) if i == True])
        on_time = ' '.join([itm for i, itm in zip([self.morning, self.noon, self.evening], TIMEOFDAY) if i == True])
        return f'{on_time}'
    
    def __repr__(self):
        return f'SheduleDay {self.morning}, {self.noon}, {self.evening}'

    @property
    def is_fullday(self):
        if self.morning is True and self.noon is True and self.evening is True:
            return True
        else:
            return False
    
    @property
    def is_on(self):
        if self.morning is True or self.noon is True or self.evening is True:
            return True
        else:
            return False
        
    def __eq__(self, object):
        if isinstance(object, SheduleDay) and self.morning == object.morning and self.noon == object.noon and self.evening == object.evening:
            return True
        return False


class Shedule:
    def __init__(self, start:date, weekdays:list, days=0, weeks=0):
        delta_days = int(weeks)* 7 + int(days)
        self.delta = timedelta(days=delta_days)
        #self.start = datetime.strptime(start, "%d.%m.%Y").date()
        self.start_date = start
        #self.start = date.fromisoformat(start)
        self.week_days = weekdays
        self.every_full_day = self.__check_week_days()
        
    
    def __str__(self):
        #return f'c {self.start} до {self.end_date}'
        days = []
        if self.every_full_day is False:
            for i, item in enumerate(self.week_days, start=0):
                if item != SheduleDay():
                    days.append(WEEKDAYS[i])
            on_days = ' '.join(days)
        else:
            on_days = ' '.join(WEEKDAYS)
        return f'с {datetime.strftime(self.start_date, "%d.%m.%Y")} по {datetime.strftime(self.end_date, "%d.%m.%Y")} {on_days}'
    
    def __repr__(self):
        return f'Shedule {self.name} {self.every_full_day}'
    
    @property
    def end_date(self):
        return (self.start_date + self.delta)
    
    def __check_week_days(self):
        for item in self.week_days:
            if item.is_fullday is False:
                return False
        return True
    
    

class Pill:
    def __init__(self, name, shedule: Shedule):
        self.name = name
        self.shedule = shedule
        
    def __str__(self):
        return f'Препарат {self.name}, прием {self.shedule}'
    
    def check(self, check_date:date):
        #chk_date = date.fromisoformat(check_date)
        #chk_date = datetime.strptime(check_date, "%d.%m.%Y").date()
        wk_time = []
        wk_day = check_date.weekday()
        if self.shedule.start_date <= check_date <= self.shedule.end_date:
            sh_d = self.shedule.week_days[wk_day]
            if sh_d.is_fullday is True or sh_d.is_on is True:
                return True, [itm for i, itm in zip([sh_d.morning, sh_d.noon, sh_d.evening], TIMEOFDAY) if i == True]
        return False, None
        
        
def main():
    str_date = '21.10.2024'
    start_date = datetime.strptime(str_date, "%d.%m.%Y").date()
    
    
    sh = Shedule(start=start_date, weeks=1, 
                 weekdays=[SheduleDay(morning=True), 
                           SheduleDay(noon=True), 
                           SheduleDay(morning=True, noon=True, evening=True), 
                           SheduleDay(morning=True, evening=True), 
                           SheduleDay(), 
                           SheduleDay(), 
                           SheduleDay(morning=True, noon=True, evening=True)])
    
    a = Pill('Аллопуринол 100' ,shedule=sh)
    print(a)
    
    str_week = '21.10.2024'
    start_week = datetime.strptime(str_week, "%d.%m.%Y").date()
    for day_plus in range(0, 7):
        checked_date = start_week + timedelta(days=day_plus)
        checked_value = a.check(checked_date)
        if checked_value[0] is True:
            print(f'{datetime.strftime(checked_date, "%d.%m.%Y")} {WEEKDAYS[checked_date.weekday()]} - {" ".join(checked_value[1])}')
        else:
            print(f'{datetime.strftime(checked_date, "%d.%m.%Y")} {WEEKDAYS[checked_date.weekday()]} - Нет')


if __name__ == '__main__':
    main()