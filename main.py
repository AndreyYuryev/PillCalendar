from datetime import date, timedelta, datetime
from pillcalendar.pill import Pill
from pillcalendar.sheduler import Sheduler, Weekday


def main():

    str_week = "01.07.2024"
    date_f = "04.11.2024"   
    date_t = "10.11.2024"  
    
    weekdays = ["Вт", "Чт", "Сб", "Вс"]
    timeofdays = ["Утро", "Вечер"] 
    quantity = 1
    days = 0  
    weeks = 20
     
     
    start_week = datetime.strptime(str_week, "%d.%m.%Y").date()
    date_from = datetime.strptime(date_f, "%d.%m.%Y").date()
    date_till = datetime.strptime(date_t, "%d.%m.%Y").date()


    
    wkd = Weekday(weekdays=weekdays, timeofday=timeofdays)
    shdl1 = Sheduler(start=start_week, weekdays=wkd, quantity=quantity, days=days, weeks=weeks)
    print(f"начало {shdl1.start} окончание {shdl1.end_date}")

    pl = Pill(name="Препарат", sheduler=shdl1)
    print(f"начало {pl.sheduler.start} окончание {pl.sheduler.end_date}")
    print(f'{pl}') 
    print(f"График приема: ")     
    print(pl.sheduler.shedule(start=date_from, end=date_till))
    print(f"потребность - {pl.sheduler.requirement(start=date_from, end=date_till)}")




if __name__ == "__main__":
    main()
