import pytest
from datetime import date, timedelta, datetime
from pillcalendar.sheduler import Weekday, Sheduler


def test_weekday():
    weekdays = ["Пн", "Пт", "Чт", "Сб"]
    timeofdays = ["Утро", "День", "Вечер"]
    wkd = Weekday(weekdays=weekdays, timeofday=timeofdays)
    assert wkd.weekday_indx == [0, 3, 4, 5]
    
def test_timeofday():
    weekdays = ["Пн", "Пт", "Чт", "Сб"]
    timeofdays = ["Утро", "Вечер"]
    wkd = Weekday(weekdays=weekdays, timeofday=timeofdays)
    assert wkd.timeofday_index == [0, 2]


def test_sheduler_from_till():
    weekdays = ["Пн", "Пт", "Чт", "Сб"]
    timeofdays = ["Утро", "День", "Вечер"]
    wkd = Weekday(weekdays=weekdays, timeofday=timeofdays)
    
    str_start_date = "21.10.2024"
    start_date = datetime.strptime(str_start_date, "%d.%m.%Y").date()
    duration_week = 0
    duration_days = 14
    str_end_date = "03.11.2024"
    end_date = datetime.strptime(str_end_date, "%d.%m.%Y").date()
    
    shdl = Sheduler(start=start_date, weekdays=wkd, quantity=1, days=duration_days, weeks=duration_week)
    assert shdl.start_date == start_date
    assert shdl.end_date == end_date
    
    
def test_sheduler_requirement():
    weekdays = ["Пн", "Вт", "Чт", "Сб"]
    timeofdays = ["Утро", "День", "Вечер"]
    wkd = Weekday(weekdays=weekdays, timeofday=timeofdays)
    
    str_start_date = "21.10.2024"
    start_date = datetime.strptime(str_start_date, "%d.%m.%Y").date()
    duration_week = 0
    duration_days = 7
    end_date = start_date + timedelta(days=duration_days, weeks=duration_week)   
    doze = 1
    requirement = 12
    
    shdl = Sheduler(start=start_date, weekdays=wkd, quantity=doze, days=duration_days, weeks=duration_week)  
    assert shdl.requirement(start=start_date, end=end_date) == requirement
    
    duration_week = 0
    duration_days = 8
    end_date = start_date + timedelta(days=duration_days, weeks=duration_week)   
    doze = 1
    requirement = 15
    
    shdl2 = Sheduler(start=start_date, weekdays=wkd, quantity=doze, days=duration_days, weeks=duration_week)  
    assert shdl2.requirement(start=start_date, end=end_date) == requirement
    
    
    duration_week = 0
    duration_days = 1
    end_date = start_date + timedelta(days=duration_days, weeks=duration_week)   
    doze = 1
    requirement = 3
    
    shdl3 = Sheduler(start=start_date, weekdays=wkd, quantity=doze, days=duration_days, weeks=duration_week)  
    assert shdl3.requirement(start=start_date, end=end_date) == requirement   
    
    
def test_sheduler_shedule():
    weekdays = ["Пн", "Вт", "Чт", "Сб"]
    timeofdays = ["Утро", "Вечер"]
    wkd = Weekday(weekdays=weekdays, timeofday=timeofdays)
    
    str_start_date = "21.10.2024"
    start_date = datetime.strptime(str_start_date, "%d.%m.%Y").date()
    duration_week = 0
    duration_days = 3
    end_date = start_date + timedelta(days=duration_days, weeks=duration_week)   
    doze = 1
    
    shdl = Sheduler(start=start_date, weekdays=wkd, quantity=doze, days=duration_days, weeks=duration_week)  
    
    timeline = [(start_date, ['Пн', '2024-10-21', '2', 'Утро', '1', 'Вечер', '1']), 
                (start_date +timedelta(days=1), ['Вт', '2024-10-22', '2', 'Утро', '1', 'Вечер', '1'])]
    assert shdl.shedule(start=start_date, end=end_date) == timeline
    
    str_start_date = "10.10.2024"
    start_date = datetime.strptime(str_start_date, "%d.%m.%Y").date()
    assert shdl.shedule(start=start_date, end=end_date) == timeline    
    