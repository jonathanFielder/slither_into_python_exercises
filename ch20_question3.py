
class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
       

    def show_time(self):
        print('{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second))

    def tick(self):
        self.second += 1
        if self.second >= 60:
            self.second = 0
            self.minute += 1
            if self.minute >= 60:
                self.minute = 0
                self.hour += 1
                if self.hour >= 24:
                    self.hour = 0
    

    
    

class Calendar:
    def __init__(self, month, day, year):
        self.day = day
        self.month = month
        self.year = year
    
    def show_date(self):
        print('{:02d}:{:02d}:{:04d}'.format(self.month, self.day, self.year))

    def next(self):
    #INIT
        leap_year = False
        month_max = 12
        day_max = 31
        short_months = (9,4,6,11)
    #LEAP YEAR CHECK
        if self.year % 4 == 0 and self.year % 100 != 0:
            leap_year = True
        if self.year % 400 == 0:
            leap_year = True
    #MONTH LENGTH
        if self.month in short_months:
            day_max = 30
        #LEAP YEAR    
        elif self.month == 2:
            if leap_year == False:
                day_max = 28
            else:
                day_max = 29
    #ADD DAY
        self.day += 1
        if self.day > day_max:
            self.day = 1
            self.month += 1
            if self.month > month_max:
                self.month = 1
                self.year += 1

class DateTime(Clock, Calendar):
    def __init__(self, hour, minute, second, month, day, year):
        Clock.__init__(self, hour, minute, second)
        Calendar.__init__(self, month, day, year)

    def tick(self):
        Clock.tick(self)
        if self.next_day(self.hour, self.minute, self.second) == True:
            Calendar.next(self)

    def show_date_time(self):
        print('The date is {:02d}:{:02d}:{:04d} and the time is {:02d}:{:02d}:{:02d}'.format(self.month, self.day, self.year, self.hour, self.minute, self.second))
    
    @staticmethod
    def next_day(h, m, s):
        if h == 0 and m == 0 and s == 0:
            return(True)
        else:
            return(False)






def main():
    '''
    c = Clock(23,59,55)
    for i in range(0,20):
        c.tick()
        c.show_time()
    cal = Calendar(2,26,2020)
    for i in range(0,100):
        cal.next()
        cal.show_date()
    '''
    both = DateTime(23, 59, 55, 12, 31, 2020)
    for i in range(0, 30):
        both.tick()
        both.show_date_time()

if __name__ == '__main__':
    main()
    