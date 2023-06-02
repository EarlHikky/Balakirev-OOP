"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/V7SV1pOWyEY

Подвиг 8. Объявите класс DeltaClock для вычисления разницы времен. Объекты этого класса должны создаваться командой:

dt = DeltaClock(clock1, clock2)
где clock1, clock2 - объекты другого класса Clock для хранения текущего времени. Эти объекты должны создаваться командой:

clock = Clock(hours, minutes, seconds)
где hours, minutes, seconds - часы, минуты, секунды (целые неотрицательные числа).

В классе Clock также должен быть (по крайней мере) один метод (возможны и другие):

get_time() - возвращает текущее время в секундах (то есть, значение hours * 3600 + minutes * 60 + seconds).

После создания объекта dt класса DeltaClock, с ним должны выполняться команды:
"""


class DeltaClock:
    def __init__(self, *args, **kwargs):
        self.clock = args
        self.d = self.clock[0].get_time() - self.clock[1].get_time()
        if self.d > 0:
            self.delta = self.d
        else:
            self.delta = 0
        
    def __str__(self):
        d = self.delta
        h = d // 3600
        m = d % 3600 // 60
        s = d % 3600 % 60
        return f"{str(h).zfill(2)}: {str(m).zfill(2)}: {str(s).zfill(2)}"
    
    def __len__(self):
        return self.delta
    
class Clock:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds        
#     def __init__(self, hours, minutes, seconds):
#         self.__hours = self.__minutes = self.__seconds = 0
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
       
    def get_time(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds


class DeltaClock:
    def __init__(self, clock1, clock2):
        self.clock1 = clock1
        self.clock2 = clock2

    def __len__(self):
        diff = self.clock1.get_time() - self.clock2.get_time()
        return  diff if diff > 0 else 0

    def __str__(self):
        delta = self.__len__()
        h = delta // 3600
        m = delta % 3600 // 60
        s = delta % 3600 % 60
        return f'{h:02}: {m:02}: {s:02}'



dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 5))
print(dt)
len_dt = len(dt)
print(len_dt)
#c1 = Clock(2, 45, 0)
#c2 = Clock(1, 15, 0)
#print(c1.get_time())
#print(c2.get_time())