"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/q_8BdpVWbyE

Подвиг 7. Объявите класс RadiusVector2D, объекты которого должны создаваться командами:

v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)
В каждом объекте класса RadiusVector2D должны формироваться локальные приватные атрибуты:

__x, __y - координаты конца вектора (изначально значения равны 0, если не передано какое-либо другое).

В классе RadiusVector2D необходимо объявить два объекта-свойства:

x - для изменения и считывания локального атрибута __x;
y - для изменения и считывания локального атрибута __y.

При инициализации и изменении локальных атрибутов, необходимо проверять корректность передаваемых значений:

- значение должно быть числом (целым или вещественным) в диапазоне [MIN_COORD; MAX_COORD].

Если проверка не проходит, то координаты не меняются (напомню, что при инициализации они изначально равны 0). Величины MIN_COORD = -100, MAX_COORD = 1024 задаются как публичные атрибуты класса RadiusVector2D.

Также в классе RadiusVector2D необходимо объявить статический метод:

norm2(vector) - для вычисления квадратической нормы vector - переданного объекта класса RadiusVector2D (квадратическая норма вектора: x*x + y*y).
"""

class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024
    
    def __init__(self, x=0,y=0):
        self.__x = self.__y = 0
        if self.__check(x) and self.__check(y):
            self.__x = x
            self.__y = y    
    
    @classmethod
    def __check(cls, arg):       
        return type(arg) in (int,float) and cls.MIN_COORD <= arg <= cls.MAX_COORD
          
    
    
    @property # обязательно перед геттером  
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        if self.__check(x):
            self.__x = x     
                
    @x.deleter
    def x(self):
        del self.__x
        
    @property # объект-свойство 
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        if self.__check(y):
            self.__y = y     
                
    @y.deleter
    def y(self):
        del self.__y         
                        
        
    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y
        
        
v1 = RadiusVector2D()        
v2 = RadiusVector2D(1)       
v3 = RadiusVector2D(1, 2) 
