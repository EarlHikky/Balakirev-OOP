"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/tS-tJR8_6to

Подвиг 4. Вам необходимо написать программу по работе с массивом однотипных данных (например, только числа или строки и т.п.). Для этого нужно объявить класс с именем Array, объекты которого создаются командой:

ar = Array(max_length, cell)
где max_length - максимальное количество элементов в массиве; cell - ссылка на класс, описывающий отдельный элемент этого массива (см. далее, класс Integer). Начальные значения в ячейках массива (в объектах класса Integer) должны быть равны 0.

Для работы с целыми числами объявите в программе еще один класс с именем Integer, объекты которого создаются командой:

cell = Integer(start_value)
где start_value - начальное значение ячейки (в данном случае - целое число).

В классе Integer должно быть следующее свойство (property):

value - для изменения и считывания значения из ячейки (само значение хранится в локальной приватной переменной; имя придумайте сами).

При попытке присвоить не целое число должно генерироваться исключение командой:

raise ValueError('должно быть целое число')
Для обращения к отдельным элементам массива в классе Array необходимо определить набор магических методов для следующих операций:

value = ar[0] # получение значения из первого элемента (ячейки) массива ar
ar[1] = value # запись нового значения во вторую ячейку массива ar
Если индекс не целое число или число меньше нуля или больше либо равно max_length, то должно генерироваться исключение командой:

raise IndexError('неверный индекс для доступа к элементам массива')
Пример использования классов (эти строчки в программе не писать):

ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
ar_int[1] = 10.5 # должно генерироваться исключение ValueError
ar_int[10] = 1 # должно генерироваться исключение IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

P.P.S. В качестве дополнительного домашнего задания: объявите еще один класс Float для работы с вещественными числами и создайте массив, используя тот же класс Array, с этим новым типом данных.
"""

class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @staticmethod
    def check(value):
        if not isinstance(value, int):
            raise ValueError('должно быть целое число')
        return True

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if self.check(value):
            self.__value = value

    def __repr__(self):
        return str(self.value)


class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.ar = [self.cell() for _ in range(self.max_length)]

    def check(self, item):
        l = len(self.ar)
        if not -l <= item < l:
            raise IndexError('некорректный индекс')
        return True

    def __getitem__(self, item):
        if self.check(item):
            return self.ar[item].value

    def __setitem__(self, key, val):
        if self.check(key):
            self.ar[key].value = val
            print(self.ar[key])

    def __str__(self):
        s = [str(_) for _ in self.ar]
        return " ".join(s)


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
# ar_int[1] = 10.5  # должно генерироваться исключение ValueError
# ar_int[10] = 1 # должно генерироваться исключение IndexError
# print(ar_int.ar)
print(ar_int)

"""
class Integer:
    def __init__(self, start_value=0):
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if type(val) != int:
            raise ValueError('должно быть целое число')
        self.__value = val

    def __repr__(self):
        return str(self.__value)


class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.cell = cell
        self.ar = [self.cell() for _ in range(self.max_length)]

    def check(self, item):        
        if type(item) != int or not (-self.max_length <= item < self.max_length):
            raise IndexError('некорректный индекс')
        

    def __getitem__(self, item):
        self.check(item)
        return self.ar[item].value

    def __setitem__(self, key, val):
        self.check(key)
        self.ar[key].value = val            

    def __repr__(self):
        s = [str(_) for _ in self.ar]
        return " ".join(s)
"""