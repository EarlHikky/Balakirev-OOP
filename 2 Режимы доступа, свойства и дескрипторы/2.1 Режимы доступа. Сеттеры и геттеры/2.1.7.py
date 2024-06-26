"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/ZX8fVI0KTfE

Подвиг 7. Объявите класс Line для описания линии на плоскости, объекты которого предполагается создавать командой:

line = Line(x1, y1, x2, y2)
При этом в объекте line должны создаваться следующие приватные локальные свойства:

__x1, __y1 - начальная координата;
__x2, __y2 - конечная координата.

В самом классе Line должны быть реализованы следующие сеттеры и геттеры:

set_coords(self, x1, y1, x2, y2) - для изменения координат линии;
get_coords(self) - для получения кортежа из текущих координат линии.

А также метод:

draw(self) - для отображения в консоли списка текущих координат линии (в одну строчку через пробел).

P.S. В программе требуется объявить только класс. Ничего на экран выводить не нужно.
"""

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
    
    def get_coords(self):
        return (self.__x1, self.__y1, self.__x2, self.__y2)
    
    def draw(self):
        print(self.__x1, self.__y1, self.__x2, self.__y2)
        
        
a = Line(1, 2, 3, 4)
s = a.get_coords()
print(s) # (1, 2, 3, 4)
a.draw() # 1 2 3 4
"""
class Line:
    def __init__(self, *args):
        self.set_coords(*args)


    def set_coords(self, *args):
        self.__x1, self.__y1, self.__x2, self.__y2 = args


    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2


    def draw(self):
        print(*self.get_coords())
"""
"""
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.set_coords(x1, y1, x2, y2)
    
    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        
    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2
        
    def draw(self):
        print(*self.get_coords())
"""        