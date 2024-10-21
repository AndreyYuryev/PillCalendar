from datetime import date, timedelta, datetime

FULL_TRUE = [True, True, True, True, True, True, True]


class Shedule:
    def __init__(self, start, days=0, weeks=0, weekdays=FULL_TRUE):
        delta_days = int(weeks)* 7 + int(days)
        self.delta = timedelta(days=delta_days)
        self.start = datetime.strptime(start, "%d.%m.%Y").date()
        #self.start = date.fromisoformat(start)
        self.week_days = weekdays
    
    def __str__(self):
        #return f'c {self.start} до {self.end_date}'
        return f'с {datetime.strftime(self.start, "%d.%m.%Y")} по {datetime.strftime(self.end_date, "%d.%m.%Y")}'
    
    @property
    def end_date(self):
        return self.start + self.delta
    
    

class Pill:
    def __init__(self, name, shedule: Shedule):
        self.name = name
        self.shedule = shedule
        
    def __str__(self):
        return f'Препарат {self.name}, прием {self.shedule}'
    
    def check(self, check_date):
        #chk_date = date.fromisoformat(check_date)
        chk_date = datetime.strptime(check_date, "%d.%m.%Y").date()
        wk_day = chk_date.weekday()
        if self.shedule.start <= chk_date <= self.shedule.end_date:
            return self.shedule.week_days[wk_day]
        return False
        
        
def main():
    str_date = '21.10.2024'
    sh = Shedule(start=str_date, weeks=1, weekdays=[True, False, True, True, False, False, True])
    a = Pill('Аллопуринол' ,shedule=sh)
    print(a)
    chk_date = '30.10.2024'
    print(f'{chk_date} - {a.check(chk_date)}')
    


if __name__ == '__main__':
    main()