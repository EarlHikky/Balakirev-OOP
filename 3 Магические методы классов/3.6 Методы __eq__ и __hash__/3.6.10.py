"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/0EYz8-qG2iU

Подвиг 10 (на повторение). Объявите класс с именем Triangle, объекты которого создаются командой:

tr = Triangle(a, b, c)
где a, b, c - длины сторон треугольника (числа: целые или вещественные). В классе Triangle объявите следующие дескрипторы данных:

a, b, c - для записи и считывания длин сторон треугольника.

При записи нового значения нужно проверять, что присваивается положительное число (целое или вещественное). Иначе, генерируется исключение командой:

raise ValueError("длины сторон треугольника должны быть положительными числами")
Также нужно проверять, что все три стороны a, b, c могут образовывать стороны треугольника. То есть, должны выполняться условия:

a < b+c; b < a+c; c < a+b

Иначе генерируется исключение командой:

raise ValueError("с указанными длинами нельзя образовать треугольник")
Наконец, с объектами класса Triangle должны выполняться функции:

len(tr) - возвращает периметр треугольника, приведенный к целому значению с помощью функции int();
tr() - возвращает площадь треугольника (можно вычислить по формуле Герона: s = sqrt(p * (p-a) * (p-b) * (p-c)), где p - полупериметр треугольника).



"""
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if float(value) <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        else:
            self.__dict__[key] = float(value)

        if key == 'c':
            if not all((self.a < self.b + self.c, self.b < self.a + self.c, self.c < self.a + self.b)):
                raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self):
        p = len(self) / 2
        print(p)
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** (1 / 2)


tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
print(tr())
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"
