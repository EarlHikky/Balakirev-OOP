"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/vOh4gzHnMWg

Подвиг 8. Объявите класс Circle (окружность), объекты которого должны создаваться командой:

circle = Circle(x, y, radius)   # x, y - координаты центра окружности; radius - радиус окружности
В каждом объекте класса Circle должны формироваться локальные приватные атрибуты:

__x, __y - координаты центра окружности (вещественные или целые числа);
__radius - радиус окружности (вещественное или целое положительное число).

Для доступа к этим приватным атрибутам в классе Circle следует объявить объекты-свойства (property):

x, y - для изменения и доступа к значениям __x, __y, соответственно;
radius - для изменения и доступа к значению __radius.

При изменении значений приватных атрибутов через объекты-свойства нужно проверять, что присваиваемые значения - числа (целые или вещественные). Дополнительно у радиуса проверять, что число должно быть положительным (строго больше нуля). Сделать все эти проверки нужно через магические методы. При некорректных переданных числовых значениях, прежние значения меняться не должны (исключений никаких генерировать при этом не нужно).

Если присваиваемое значение не числовое, то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")
При обращении к несуществующему атрибуту объектов класса Circle выдавать булево значение False.
"""


class Circle:
    attrs = {'x':(int, float), 'y':(int, float), 'radius':(int, float)}
    def __init__(self,x,y,radius):
        self.__x = self.__y = self.__radius = None
        self.x = x
        self.y = y
        self.radius = radius
        
    @property
    def x(self):        
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = value
        
    @property
    def y(self):        
        return self.__y
    
    @y.setter
    def y(self, value):
        self.__y = value
        
    @property
    def radius(self):        
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        self.__radius = value    
        
    def __setattr__(self, key, value):    
        if key in self.attrs and type(value) not in self.attrs[key]:
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == 'radius' and value <= 0:
            return
        super().__setattr__(key, value)
        
    def __getattr__(self, item):
        return False
        
circle = Circle(10.5, 7, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует

