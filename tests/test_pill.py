import pytest
from datetime import date, timedelta, datetime
from pillcalendar.sheduler import Weekday, Sheduler
from pillcalendar.pill import Pill


def test_requirement():
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
    pill_name = 'Препарат 1'
    
    shdl = Sheduler(start=start_date, weekdays=wkd, quantity=doze, days=duration_days, weeks=duration_week)
    
    pill = Pill(name=pill_name, sheduler=shdl)
    assert pill.requirement(from_date=start_date, till_date=end_date) == f'Потребность {pill_name} - {requirement} штук'
    
    
def test_shedule():
    weekdays = ["Пн", "Вт", "Чт", "Сб"]
    timeofdays = ["Утро", "Вечер"]
    wkd = Weekday(weekdays=weekdays, timeofday=timeofdays)
    
    str_start_date = "21.10.2024"
    start_date = datetime.strptime(str_start_date, "%d.%m.%Y").date()
    duration_week = 0
    duration_days = 3
    end_date = start_date + timedelta(days=duration_days, weeks=duration_week)   
    doze = 1
    pill_name = 'Препарат 1'
    
    shdl = Sheduler(start=start_date, weekdays=wkd, quantity=doze, days=duration_days, weeks=duration_week)  
    
    pill = Pill(name=pill_name, sheduler=shdl)
    
    timeline = [f"График приема препарата {pill_name}:",
                'Пн 2024-10-21 2 Утро 1 Вечер 1', 
                'Вт 2024-10-22 2 Утро 1 Вечер 1']
    
    assert pill.shedule(from_date=start_date, till_date=end_date) == timeline
    
    str_start_date2 = "21.08.2024"
    start_date2 = datetime.strptime(str_start_date2, "%d.%m.%Y").date()
    end_date2 = start_date2 + timedelta(days=duration_days, weeks=duration_week)  
    timeline = [f"График приема препарата {pill_name}:",
                '']
    assert pill.shedule(from_date=start_date2, till_date=end_date2) == timeline
    
    
    
def test_delivery():
    weekdays = ["Пн", "Вт", "Чт", "Сб"]
    timeofdays = ["Утро", "День", "Вечер"]
    wkd = Weekday(weekdays=weekdays, timeofday=timeofdays)
    
    str_start_date = "21.10.2024"
    start_date = datetime.strptime(str_start_date, "%d.%m.%Y").date()
    duration_week = 0
    duration_days = 7
    end_date = start_date + timedelta(days=duration_days, weeks=duration_week) 
    if duration_days > 1:
        end_date = end_date - timedelta(days=1)  
    doze = 1
    pill_name = 'Препарат 1'
    
    shdl = Sheduler(start=start_date, weekdays=wkd, quantity=doze, days=duration_days, weeks=duration_week)
    
    pill = Pill(name=pill_name, sheduler=shdl)
    
    delivery = f'Прием {pill_name} c {start_date} по {end_date}'
    assert pill.delivery() == delivery
    assert pill.end_date() == end_date