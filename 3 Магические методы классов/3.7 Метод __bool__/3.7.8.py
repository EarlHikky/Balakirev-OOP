"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/2lnbu3n7Y_w

Большой подвиг 8. Вы начинаете разрабатывать игру "Сапер". Для этого вам нужно уметь представлять и управлять игровым полем. Будем полагать, что оно имеет размеры N x M клеток. Каждая клетка будет представлена объектом класса Cell и содержать либо число мин вокруг этой клетки, либо саму мину.



Для начала в программе объявите класс GamePole, который будет создавать и управлять игровым полем. Объект этого класса должен формироваться командой:

pole = GamePole(N, M, total_mines)
И, так как поле в игре одно, то нужно контролировать создание только одного объекта класса GamePole (используйте паттерн Singleton, о котором мы с вами говорили, когда рассматривали магический метод __new__()).

Объект pole должен иметь локальный приватный атрибут:

__pole_cells - двумерный (вложенный) кортеж, размерами N x M элементов (N строк и M столбцов), состоящий из объектов класса Cell.

Для доступа к этой коллекции объявите в классе GamePole объект-свойство (property):

pole - только для чтения (получения) ссылки на коллекцию __pole_cells.

Далее, в самом классе GamePole объявите следующие методы:

init_pole() - для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми);
open_cell(i, j) - открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля; метод меняет значение атрибута __is_open объекта Cell в ячейке (i, j) на True;
show_pole() - отображает игровое поле в консоли (как именно сделать - на ваше усмотрение, этот метод - домашнее задание).

Расстановку мин выполняйте случайным образом по игровому полю (для этого удобно воспользоваться функцией randint модуля random). После расстановки всех total_mines мин, вычислите их количество вокруг остальных клеток (где нет мин). Область охвата - соседние (прилегающие) клетки (8 штук).

В методе open_cell() необходимо проверять корректность индексов (i, j). Если индексы указаны некорректно, то генерируется исключение командой:

raise IndexError('некорректные индексы i, j клетки игрового поля')
Следующий класс Cell описывает состояние одной ячейки игрового поля. Объекты этого класса создаются командой:

cell = Cell()
При этом в самом объекте создаются следующие локальные приватные свойства:

__is_mine - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
__number - число мин вокруг клетки (целое число от 0 до 8);
__is_open - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.

Для работы с этими приватными атрибутами объявите в классе Cell следующие объекты-свойства с именами:

is_mine - для записи и чтения информации из атрибута __is_mine;
number - для записи и чтения информации из атрибута __number;
is_open - для записи и чтения информации из атрибута __is_open.

В этих свойствах необходимо выполнять проверку на корректность переданных значений (либо булево значение True/False, либо целое число от 0 до 8). Если передаваемое значение некорректно, то генерировать исключение командой:

raise ValueError("недопустимое значение атрибута")
С объектами класса Cell должна работать функция:

bool(cell)
которая возвращает True, если клетка закрыта и False - если открыта.
"""


from random import randint


class Cell:
    def __init__(self):
        self._is_mine = False
        self._number = 0
        self._is_open = False

    @property
    def is_mine(self):
        return self._is_mine

    @is_mine.setter
    def is_mine(self, value):
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self._is_mine = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if type(value) != int or value < 0 or value > 8:
            raise ValueError("недопустимое значение атрибута")
        self._number = value

    @property
    def is_open(self):
        return self._is_open

    @is_open.setter
    def is_open(self, value):
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self._is_open = value

    def __bool__(self):
        return not self._is_open


class GamePole:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, N, M, total_mines):
        self._n = N
        self._m = M
        self._total_mines = total_mines
        self._pole_cells = tuple(tuple(Cell() for _ in range(M)) for _ in range(N))
        self.init_pole()

    @property
    def pole(self):
        return self._pole_cells

    def init_pole(self):
        for row in self._pole_cells:
            for x in row:
                x.is_open = False
                x.is_mine = False

        m = 0
        while m < self._total_mines:
            i = randint(0, self._n - 1)
            j = randint(0, self._m - 1)

            if self._pole_cells[i][j].is_mine:
                continue
            self._pole_cells[i][j].is_mine = True
            m += 1

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self._n):
            for y in range(self._m):
                if not self.pole[x][y].is_mine:
                    mines = sum((self.pole[x + i][y + j].is_mine for i, j in indx if
                                 0 <= x + i < self._n and 0 <= y + j < self._m))
                    self.pole[x][y].number = mines

    def open_cell(self, i, j):
        if not 0 <= i < self._n or not 0 <= j < self._m:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True

    def show_pole(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.is_open else x.number if not x.is_mine else '*', row))

    def __del__(self):
        GamePole._instance = None


p = GamePole(10, 12, 10)
p.show_pole()
pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()


from random import shuffle

class CellDescr:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __set__(self, instance, value):
        if not (isinstance(value, int) and 0 <= value <= 8):
            raise ValueError("недопустимое значение атрибута")
        return setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        if instance is None:
            return property()
        return getattr(instance, self.name)


class Cell:
    is_mine = CellDescr()
    number = CellDescr()
    is_open = CellDescr()

    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    def __bool__(self):
        return not self.is_open


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, n: int, m: int, total_mines: int):
        self.n, self.m = n, m
        self.total_mines = total_mines
        self.__pole_cells = tuple(tuple(Cell() for _ in range(m)) for _ in range(n))
        self.mine_init = [False if x > total_mines else True for x in range(1, m * n + 1)]

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        shuffle(self.mine_init)
        i = 0
        for line in self.pole:
            for cell in line:
                cell.is_mine = self.mine_init[i]
                cell.is_open = False
                i += 1
        self.__around_mine(self.n, self.m)

    def open_cell(self, i, j):
        if not (0 <= j < len(self.pole[0]) and 0 <= i < len(self.pole)):
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True

    def show_pole(self):
        for line in self.pole:
            for cell in line:
                print(["#", cell.number, "*"][2 if cell.is_mine and not cell else not cell], end="  ")
            print()

    def __around_mine(self, n, m):
        for i in range(n):
            for j in range(m):
                ar_m = sum(self.pole[i+a][j+b].is_mine for a in (-1, 0, 1) for b in (-1, 0, 1) if 0 <= i+a < n and 0 <= j+b < m)
                self.pole[i][j].number = ar_m