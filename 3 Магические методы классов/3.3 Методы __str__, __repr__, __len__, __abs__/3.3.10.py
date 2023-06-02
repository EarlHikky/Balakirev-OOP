"""
Подвиг 10 (на повторение). Объявите класс PolyLine (полилиния) для представления линии из последовательности прямолинейных сегментов. Объекты этого класса должны создаваться командой:

poly = PolyLine(start_coord, coord_2, coord_3, ..., coord_N)
Здесь start_coord - координата начала полилинии (кортеж из двух чисел x, y); coord_2, coord_3, ... - последующие координаты точек на плоскости (представленные кортежами), соединенных прямыми линиями.

Например:

poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))


В классе PolyLine должны быть объявлены следующие методы:

add_coord(x, y) - добавление новой координаты (в конец);
remove_coord(indx) - удаление координаты по индексу (порядковому номеру, начинается с нуля);
get_coords() - получение списка координат (в виде списка из кортежей).

P.S. На экран ничего выводить не нужно, только объявить класс.
"""


class PolyLine:
    def __init__(self, *args, **kwargs):
        self.coord = [] + [*args]
        
    def add_coord(self, x, y):
        self.coord.append((x, y))
    
    def get_coords(self):
        return tuple(self.coord)
    
    def remove_coord(self, indx):
        del self.coord[indx]
    
    
    
    
poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
poly.add_coord(13,55)
print(poly.coord)
        