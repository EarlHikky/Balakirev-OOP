"""
Подвиг 9 (релакс). Необходимо объявить класс Body (тело), объекты которого создаются командой:

body = Body(name, ro, volume)
где name - название тела (строка); ro - плотность тела (число: вещественное или целочисленное); volume - объем тела  (число: вещественное или целочисленное).

Для объектов класса Body должны быть реализованы операторы сравнения:

body1 > body2  # True, если масса тела body1 больше массы тела body2
body1 == body2 # True, если масса тела body1 равна массе тела body2
body1 < 10     # True, если масса тела body1 меньше 10
body2 == 5     # True, если масса тела body2 равна 5
Масса тела вычисляется по формуле:

m = ro * volume

P.S. В программе только объявить класс, выводить на экран ничего не нужно.
"""

class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume
        self.m = self.ro * self.volume        
        
    def __eq__(self, other):
        if type(other) is int:
            return self.m == other
        return self.m == other.m
    
    def __gt__(self, other):
        if type(other) is int:
            return self.m > other
        return self.m > other.m
    
    def __ge__(self, other):
        if type(other) is int:
            return self.m >= other
        return self.m >= other.m
    
    def __lt__(self, other):
        if type(other) is int:
            return self.m < other
        return self.m > other.m
    
    def __le__(self, other):
        if type(other) is int:
            return self.m <= other
        return self.m >= other.m
        
       
       
t1 = Body('1', 123, 55)
t2 = Body('2', 120, 50)
print(t1.m)
print(t2.m)
print(t1 == 6765)
print(t1 > 444)
print(t1 < 444)
print(t1 >= t2)