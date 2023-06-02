"""
Подвиг 10 (на повторение). Объявите базовый класс с именем ItemAttrs, который бы позволял обращаться к локальным атрибутам объектов дочерних классов по индексу. Для этого в классе ItemAttrs нужно переопределить следующие методы:

__getitem__() - для получения значения атрибута по индексу;
__setitem__() - для изменения значения атрибута по индексу.

Объявите дочерний класс Point для представления координаты точки на плоскости. Объекты этого класса должны создаваться командой:

pt = Point(x, y)
где x, y - целые или вещественные числа.
"""

class ItemAttrs:
    def __getitem__(self, item):
        return self.args[item]

    def __setitem__(self, key, value):
        self.args[key] = value


class Point(ItemAttrs):
    def __init__(self, *args):
        self.args = list(args)

pt = Point(1, 2.5)
x = pt[0]   # 1
y = pt[1]   # 2.5
print(x, y)
pt[0] = 10
print(pt[0])