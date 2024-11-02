from datetime import date, timedelta, datetime
from pillcalendar.period import Period
from pillcalendar.weekday import Weekday
from pillcalendar.pill import Pill

FULL_TIME = [True, True, True]
FULL_FALSE = [False, False, False]
FULL_DAYS = [
    FULL_TIME,
    FULL_TIME,
    FULL_TIME,
    FULL_TIME,
    FULL_TIME,
    FULL_TIME,
    FULL_TIME,
]




def main():
    str_date = "21.10.2024"
    start_date = datetime.strptime(str_date, "%d.%m.%Y").date()

    sh = Shedule(
        start=start_date,
        weeks=1,
        weekdays=[
            SheduleDay(morning=True),
            SheduleDay(noon=True),
            SheduleDay(morning=True, noon=True, evening=True),
            SheduleDay(morning=True, evening=True),
            SheduleDay(),
            SheduleDay(),
            SheduleDay(morning=True, noon=True, evening=True),
        ],
    )

    a = Pill("Аллопуринол 100", shedule=sh)
    print(a)

    str_week = "21.10.2024"
    start_week = datetime.strptime(str_week, "%d.%m.%Y").date()
    for day_plus in range(0, 7):
        checked_date = start_week + timedelta(days=day_plus)
        checked_value = a.check(checked_date)
        if checked_value[0] is True:
            print(
                f'{datetime.strftime(checked_date, "%d.%m.%Y")} {WEEKDAYS[checked_date.weekday()]} - {" ".join(checked_value[1])}'
            )
        else:
            print(
                f'{datetime.strftime(checked_date, "%d.%m.%Y")} {WEEKDAYS[checked_date.weekday()]} - Нет'
            )


if __name__ == "__main__":
    main()
