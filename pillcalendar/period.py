

class Period:
    """ Класс для работы с временем суток
    """
    TIMEOFDAY = ("Утро", "День", "Вечер")
    
    def __init__(self, period_name: str, enabled=False):
        self.enabled = enabled
        self.period_name = period_name
        
    @property
    def is_on(self):
        return self.enabled
    
    @property
    def name(self):
        return f'{self.period_name}'
    
    def __str__(self):
        return f'{self.name} - {self.is_on}'
    
    def __repr__(self):
        return f'class Period: {self.name} - {self.is_on}'
    
    def __eq__(self, object):
        if isinstance(object, Period) and self.is_on == object.is_on and self.name == object.name:
            return True
        return False
        
          
class Morning(Period):
    """ Утро
    """
    def __init__(self, enabled=False):
        super().__init__(period_name=Period.TIMEOFDAY[0], enabled=enabled)
        
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()
        
class Noon(Period):
    """ День
    """
    def __init__(self, enabled=False):
        super().__init__(period_name=Period.TIMEOFDAY[1], enabled=enabled)
    
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()


class Evening(Period):
    """ Вечер
    """
    def __init__(self, enabled=False):
        super().__init__(period_name=Period.TIMEOFDAY[2], enabled=enabled)
        
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()

"""    def __str__(self):
        # wk_time = []
        # wk_time.extend([itm for i, itm in zip([self.morning, self.noon, self.evening], TIMEOFDAY) if i == True])
        on_time = " ".join(
            [
                itm
                for i, itm in zip([self.morning, self.noon, self.evening], TIMEOFDAY)
                if i == True
            ]
        )
        return f"{on_time}"

    def __repr__(self):
        return f"SheduleDay {self.morning}, {self.noon}, {self.evening}"

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
        if (
            isinstance(object, Period)
            and self.morning == object.morning
            and self.noon == object.noon
            and self.evening == object.evening
        ):
            return True
        return False """
        
if __name__ == "__main__":
    prd = Period(period_name=Period.TIMEOFDAY[0], enabled=True)
    mrn = Morning(True)
    nn  = Noon()
    evn = Evening(True)
    
    print(mrn, nn, evn, sep='\n')
    print(mrn == nn)
    print(mrn == evn)
    print(prd == mrn)