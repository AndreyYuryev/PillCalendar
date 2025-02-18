from datetime import date, timedelta, datetime
from pillcalendar.pill import Pill
from pillcalendar.sheduler import Sheduler, Weekday


def main_for_test():
    weekdays = list(input().split())
    timeofdays = list(input().split())
    #weekdays = ["Пн", "Пт", "Чт", "Сб"]
    #timeofdays = ["Утро", "День", "Вечер"]
    wkd = Weekday(weekdays=weekdays, timeofday=timeofdays)
    for item in wkd.weekday_index:
        print(item)

if __name__ == "__main__":
    main_for_test()
