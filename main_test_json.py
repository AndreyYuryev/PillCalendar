from datetime import date, timedelta, datetime
from pillcalendar.pill import Pill
from pillcalendar.sheduler import Sheduler, Weekday
from pillcalendar.download import JSONDownloader
from pillcalendar.upload import JSONUploader


def main_for_test_json(filepath=''):
    reader = JSONUploader()
    data = reader.open_file(filepath)
    
    pills = list()
    
    for ittm in data:
        itm = data[ittm]
        weekdays = itm.get('weekdays', [])
        timeofdays = itm.get('timeofdays', [])
        wkd = Weekday(weekdays=weekdays, timeofday=timeofdays)
        start_date = datetime.fromisoformat(itm.get('start')).date()
        doze = itm.get('quantity', 0)
        duration_week = itm.get('weeks', 0)
        duration_days = itm.get('days', 0)
        pill_name = ittm
        shdl = Sheduler(start=start_date, weekdays=wkd, quantity=doze, days=duration_days, weeks=duration_week) 
        pill = Pill(name=pill_name, sheduler=shdl) 
        pills.append(pill)   
        
    '''
    exit = ''
    next = False
    previous_date_exist = False
    previous_date = datetime.today()
    
    while True:
        pill_name = input('Ввведите название препарата: ')
        weekdays = list(input('Введите через пробел день недели (Пн Вт Ср Чт Пт Сб Вс): ').split())   
        timeofdays = list(input('Введите через пробел время суток (Утро День Вечер): ').split())
        doze = int(input('Введите количество, штук: '))
        if previous_date_exist is False or input('Добавить после предыдущего? д/н ') == 'н':
            start_date = datetime.strptime(input('Введите дату начала в формате ДД.ММ.ГГГГ: '), "%d.%m.%Y").date()
        else:
            start_date = previous_date
        duration_week = int(input('Длительность приема в неделях: '))
        duration_days = int(input('Длительность приема в днях: '))
        
        data[pill_name] = dict(weekdays=weekdays,
                               timeofdays=timeofdays,
                               quantity=doze,
                               weeks=duration_week,
                               days=duration_days,
                               start=start_date.isoformat())

        wkd = Weekday(weekdays=weekdays, timeofday=timeofdays)
        shdl = Sheduler(start=start_date, weekdays=wkd, quantity=doze, days=duration_days, weeks=duration_week) 
        pill = Pill(name=pill_name, sheduler=shdl) 
        pills.append(pill)        
        previous_date = pill.end_date()
        previous_date_exist = True
        
        exit = input('Закончить - введите X ')
        if exit == 'X':
            break

    saver = JSONDownloader(data=data)
    saver.save_file(filepath)
    '''

    date_from = datetime.strptime(input('Введите дату начала периода в формате ДД.ММ.ГГГГ: '), "%d.%m.%Y").date()
    date_till = datetime.strptime(input('Введите дату конца периода в формате ДД.ММ.ГГГГ: '), "%d.%m.%Y").date()
    for item in pills:
        print(item.delivery())
        print(item.requirement(from_date=date_from, till_date=date_till))
        print(*item.shedule(from_date=date_from, till_date=date_till)[1:], sep='\n')




if __name__ == "__main__":
    main_for_test_json('../data/pills.json')
