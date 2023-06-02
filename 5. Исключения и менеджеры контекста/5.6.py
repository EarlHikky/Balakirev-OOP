"""
Посвящение в ООП
Вы прошли серию испытаний и совершили множество подвигов, чтобы лицом к лицу столкнуться с настоящим вызовом, достойным лишь избранных! Для подтверждения своих знаний и навыков вам предлагается пройти этап посвящения в объектно-ориентированное программирование. И вот задание, которое выпало на вашу долю.

Руководство компании целыми днями не знает куда себя деть. Поэтому они решили дать задание своим программистам написать программу игры "Морской бой". Но эта игра будет немного отличаться от классической. Для тех, кто не знаком с этой древней, как мир, игрой, напомню ее краткое описание.

Каждый игрок у себя на бумаге рисует игровое поле 10 х 10 клеток и расставляет на нем десять кораблей: однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1.



Корабли расставляются случайным образом, но так, чтобы не выходили за пределы игрового поля и не соприкасались друг с другом (в том числе и по диагонали).

Затем, игроки по очереди называют клетки, куда производят выстрелы. И отмечают эти выстрелы на другом таком же поле в 10 х 10 клеток, которое представляет поле соперника. Соперник при этом должен честно отвечать: "промах", если ни один корабль не был задет и "попал", если произошло попадание. Выигрывает тот игрок, который первым поразит все корабли соперника.

Но это была игра из глубокого прошлого. Теперь же, в компьютерную эру, корабли на игровом поле могут перемещаться в направлении своей ориентации на одну клетку после каждого хода соперника, если в них не было ни одного попадания.

Итак, лично вам поручается сделать важный фрагмент этой игры - расстановку и управление кораблями в этой игре. А само задание звучит так.

Техническое задание
В программе необходимо объявить два класса:

Ship - для представления кораблей;
GamePole - для описания игрового поля.

Класс Ship
Класс Ship должен описывать корабли набором следующих параметров:

x, y - координаты начала расположения корабля (целые числа);
length - длина корабля (число палуб: целое значение: 1, 2, 3 или 4);
tp - ориентация корабля (1 - горизонтальная; 2 - вертикальная).



Объекты класса Ship должны создаваться командами:

ship = Ship(length)
ship = Ship(length, tp)
ship = Ship(length, tp, x, y)
По умолчанию (если не указывается) параметр tp = 1, а координаты x, y равны None.

В каждом объекте класса Ship должны формироваться следующие локальные атрибуты:

_x, _y - координаты корабля (целые значения в диапазоне [0; size), где size - размер игрового поля);
_length - длина корабля (число палуб);
_tp - ориентация корабля;
_is_move - возможно ли перемещение корабля (изначально равно True);
_cells - изначально список длиной length, состоящий из единиц (например, при length=3, _cells = [1, 1, 1]).

Список _cells будет сигнализировать о попадании соперником в какую-либо палубу корабля. Если стоит 1, то попадания не было, а если стоит значение 2, то произошло попадание в соответствующую палубу.

При попадании в корабль (хотя бы одну его палубу), флаг _is_move устанавливается в False и перемещение корабля по игровому полю прекращается.

В самом классе Ship должны быть реализованы следующие методы (конечно, возможны и другие, дополнительные):

set_start_coords(x, y) - установка начальных координат (запись значений в локальные атрибуты _x, _y);
get_start_coords() - получение начальных координат корабля в виде кортежа x, y;
move(go) - перемещение корабля в направлении его ориентации на go клеток (go = 1 - движение в одну сторону на клетку; go = -1 - движение в другую сторону на одну клетку); движение возможно только если флаг _is_move = True;
is_collide(ship) - проверка на столкновение с другим кораблем ship (столкновением считается, если другой корабль или пересекается с текущим или просто соприкасается, в том числе и по диагонали); метод возвращает True, если столкновение есть и False - в противном случае;
is_out_pole(size) - проверка на выход корабля за пределы игрового поля (size - размер игрового поля, обычно, size = 10); возвращается булево значение True, если корабль вышел из игрового поля и False - в противном случае;

С помощью магических методов __getitem__() и __setitem__() обеспечить доступ к коллекции _cells следующим образом:

value = ship[indx] # считывание значения из _cells по индексу indx (индекс отсчитывается от 0)
ship[indx] = value # запись нового значения в коллекцию _cells
Класс GamePole
Следующий класс GamePole должен обеспечивать работу с игровым полем. Объекты этого класса создаются командой:

pole = GamePole(size)
где size - размеры игрового поля (обычно, size = 10).

В каждом объекте этого класса должны формироваться локальные атрибуты:

_size - размер игрового поля (целое положительное число);
_ships - список из кораблей (объектов класса Ship); изначально пустой список.

В самом классе GamePole должны быть реализованы следующие методы (возможны и другие, дополнительные методы):

init() - начальная инициализация игрового поля; здесь создается список из кораблей (объектов класса Ship): однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1 (ориентация этих кораблей должна быть случайной).

Корабли формируются в коллекции _ships следующим образом: однопалубных - 4; двухпалубных - 3; трехпалубных - 2; четырехпалубный - 1. Ориентация этих кораблей должна быть случайной. Для этого можно воспользоваться функцией randint следующим образом:

[Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), ...]
Начальные координаты x, y не расставленных кораблей равны None.

После этого, выполняется их расстановка на игровом поле со случайными координатами так, чтобы корабли не пересекались между собой.

get_ships() - возвращает коллекцию _ships;
move_ships() - перемещает каждый корабль из коллекции _ships на одну клетку (случайным образом вперед или назад) в направлении ориентации корабля; если перемещение в выбранную сторону невозможно (другой корабль или пределы игрового поля), то попытаться переместиться в противоположную сторону, иначе (если перемещения невозможны), оставаться на месте;
show() - отображение игрового поля в консоли (корабли должны отображаться значениями из коллекции _cells каждого корабля, вода - значением 0);

get_pole() - получение текущего игрового поля в виде двумерного (вложенного) кортежа размерами size x size элементов.

Пример отображения игрового поля:

0 0 1 0 1 1 1 0 0 0
1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 1
0 0 0 0 1 0 1 0 0 1
0 0 0 0 0 0 1 0 0 0
1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0
0 1 1 1 1 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0
Пример использования классов (эти строчки в программе не писать):

SIZE_GAME_POLE = 10

pole = GamePole(SIZE_GAME_POLE)
pole.init()
pole.show()

pole.move_ships()
print()
pole.show()
В программе требуется только объявить классы Ship и GamePole с соответствующим функционалом. На экран выводить ничего не нужно.

P.S. Для самых преданных поклонников программирования и ООП. Завершите эту программу, добавив еще один класс SeaBattle для управления игровым процессом в целом. Игра должна осуществляться между человеком и компьютером. Выстрелы со стороны компьютера можно реализовать случайным образом в свободные клетки. Сыграйте в эту игру и выиграйте у компьютера.
 
"""


from random import randint, shuffle


class Ship:
    """Класс для представления кораблей"""

    HORIZONTAL = 1
    VERTICAL = 2

    def __init__(self, length: int, tp: int = HORIZONTAL, x: int = None, y: int = None):
        self._length = length  # длина корабля
        self._tp = tp  # ориентация корабля(1 - горизонтальная, 2 - вертикальная)
        self._x = x  # координаты начала корабля(первая палуба)
        self._y = y
        self._is_move = True  # возможность перемещения корабля(если не было попадания - True, иначе False)
        self._cells = [1] * length  # список с палубами корабля(1 - попадания не было, 2 - попадание было)

    def __repr__(self):
        return f'({self._length}-палубный, {"Горизонтальный" if self._tp == 1 else "Вертикальный"}, ' \
               f'{"Целый" if self._is_move else "Подбитый"}, ' \
               f'x={self._x} y={self._y})'

    def __setattr__(self, key, value):
        if key in ('_x', '_y', '_length'):
            if not isinstance(value, int) and value is not None or \
                    isinstance(value, int) and value < 0:
                raise TypeError('Координаты и длина должны быть целыми положительными числами')

        if key == '_tp':
            if not isinstance(value, int) or value not in (1, 2):
                raise ValueError('Значение ориентации должно быть 1 или 2')

        super().__setattr__(key, value)

    def __bool__(self):
        """Метод для проверки состояния корабля
        False - если корабль полностью уничтожен,
        True - если есть еще целые палубы"""
        return not all(x == 2 for x in self._cells)

    @property
    def tp(self):
        return self._tp

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def length(self):
        return self._length

    @property
    def is_move(self):
        return self._is_move

    @is_move.setter
    def is_move(self, value):
        if type(value) == bool:
            self._is_move = value

    def set_start_coords(self, x: int, y: int):
        """Метод для установки начальных координат корабля"""
        self._x = x
        self._y = y

    def get_start_coords(self) -> tuple:
        """Получение начальных координат корабля"""
        return self._x, self._y

    def move(self, go: int):
        """Метод реализует перемещения корабля в направлении его ориентации на 'go' клеток"""
        if self._is_move:
            x, y = self.get_start_coords()
            if self._tp == self.HORIZONTAL:
                self.set_start_coords(x + go, y)
            elif self._tp == self.VERTICAL:
                self.set_start_coords(x, y + go)

    @staticmethod
    def _get_place_and_around_coordinates(ship_orientation: int, ship: 'Ship') -> tuple:
        """Метод для получения координат нахождения всего корабля и
        координат вокруг корабля"""
        indexes = (-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1), (0, 0)  # индексы вокруг клетки
        all_coord = set()  # координаты корабля и координаты вокруг корабля
        ship_coord = set()  # координаты только корабля
        x, y, length = ship._x, ship._y, ship._length

        if ship_orientation == ship.HORIZONTAL:
            ship_coord = {(x + j, y) for j in range(length)}  # сбор координат каждой палубы корабля

        elif ship_orientation == ship.VERTICAL:
            ship_coord = {(x, y + i) for i in range(length)}

        # сбор координат вокруг корабля и самого корабля
        for a, b in indexes:
            for c, d in ship_coord:
                all_coord.add((a + c, b + d))

        return all_coord, ship_coord

    def is_collide(self, ship: 'Ship') -> bool:
        """Метод для проверки на столкновение или соприкосновение с другим кораблем 'ship'"""
        if isinstance(ship, Ship):
            # получение координат текущего корабля и другого корабля
            all_coord_self, self_coord = self._get_place_and_around_coordinates(self._tp, self)
            all_coord_ship, ship_coord = ship._get_place_and_around_coordinates(ship._tp, ship)
            common_coord = all_coord_self & all_coord_ship  # общие координаты двух кораблей
            # координаты мест пересечения кораблей(если таких нет - значит корабли не пересекаются и не касаются)
            result = (self_coord & common_coord) | (ship_coord & common_coord)
            return len(result) != 0

    def is_out_pole(self, size: int) -> bool:
        """Метод для проверки на выход корабля за пределы игрового поля"""
        x, y = self._x, self._y
        last_part_coord = (x + self._length - 1, y) if self._tp == self.HORIZONTAL else (x, y + self._length - 1)
        return x < 0 or last_part_coord[0] > size - 1 or y < 0 or last_part_coord[1] > size - 1

    def _check_index(self, index) -> bool:
        """Метод для проверки индекса для работы со списком _cells"""
        return 0 <= index < len(self._cells)

    def __getitem__(self, item: int) -> int:
        """Метод для считывания значения из списка _cells по индексу item"""
        if self._check_index(item):
            return self._cells[item]

    def __setitem__(self, key, value):
        """Метод для записи нового значения в _cells по индексу key"""
        if self._check_index(key) and isinstance(value, int) and value in (1, 2):
            self._cells[key] = value


class GamePole:
    """Класс для описания игрового поля"""

    def __init__(self, size: int = 10):
        self._size = size  # размер игрового поля
        self._ships = []  # список из кораблей на поле
        self._field = [[0] * self._size for _ in range(self._size)]  # игровое поле
        self._name = ''
        self._count_dead_ships = 0
        self._generate_ships()  # создание кораблей

    def __bool__(self):
        return self._count_dead_ships == 10

    @property
    def ships(self):
        return self._ships

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value

    @property
    def count_dead_ships(self):
        return self._count_dead_ships

    @count_dead_ships.setter
    def count_dead_ships(self, value):
        if isinstance(value, int):
            self._count_dead_ships = value

    def _check_ships_around(self, length: int, head_coord: tuple, orientation: int) -> int:
        """Метод для проверки наличия кораблей вокруг и на месте установки корабля"""
        indexes = (-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1), (0, 0)
        head_x, head_y = head_coord
        result = 0

        if orientation == 1:  # горизонтально
            j = head_x
            k = 0
            while length > k:  # пока не проверили на наличие кораблей вокруг и на месте установки
                result += sum(self._field[head_y + x][j + y] for x, y in indexes
                              if 0 <= head_y + x < self._size and 0 <= j + y < self._size)
                j += 1
                k += 1

        elif orientation == 2:  # вертикально
            i = head_y
            k = 0
            while length > k:  # пока не проверили на наличие кораблей вокруг и на месте установки
                result += sum(self._field[i + x][head_x + y] for x, y in indexes
                              if 0 <= i + x < self._size and 0 <= head_x + y < self._size)
                i += 1
                k += 1

        return result

    def _generate_ships(self):
        """Метод для создания кораблей со случайной ориентацией и без начальных координат"""
        self._ships = [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2))]

    def init(self):
        """Метод для начальной инициализации игрового поля"""
        for ship in self._ships:
            tp, length = ship.tp, ship.length
            while True:  # пока корабли не расставлены
                x, y = randint(0, self._size - 1), randint(0, self._size - 1)  # ship_x -> j; ship_y -> i
                if tp == ship.HORIZONTAL:  # если расположение корабля горизонтальное
                    if x + (length - 1) > self._size - 1:  # если длина корабля выходит за поле
                        continue

                    result = self._check_ships_around(length, (x, y), tp)

                    if not result:  # если кораблей нет рядом и нет на месте
                        k = 0
                        for j in range(x, x + length):
                            self._field[y][j] = ship[k]  # установка корабля на поле с k-палубами
                            k += 1
                    else:
                        continue

                elif tp == ship.VERTICAL:  # если расположение корабля вертикальное
                    if y + (length - 1) > self._size - 1:  # если длина корабля выходит за поле
                        continue

                    result = self._check_ships_around(length, (x, y), tp)

                    if not result:  # если кораблей нет рядом и нет на месте
                        k = 0
                        for i in range(y, y + length):
                            self._field[i][x] = ship[k]
                            k += 1
                    else:
                        continue

                ship.set_start_coords(x, y)  # установить в текущем корабле его начальные координаты
                break

    def get_ships(self) -> list:
        """Метод для возврата списка кораблей на поле"""
        return self._ships

    def update_game_field(self):
        """Метод для обновления игрового поля
        после движения кораблей и после каждого хода"""
        for i in range(self._size):  # обнуление поля
            for j in range(self._size):
                self._field[i][j] = 0

        for ship in self._ships:
            x, y, length = ship.x, ship.y, ship.length
            ship_part = 0

            if ship.tp == ship.HORIZONTAL:
                for j in range(x, x + length):
                    self._field[y][j] = ship[ship_part]  # установка корабля на поле с k-палубами
                    ship_part += 1
            elif ship.tp == ship.VERTICAL:
                for i in range(y, y + length):
                    self._field[i][x] = ship[ship_part]
                    ship_part += 1

    def move_ships(self):
        """Метод для перемещения каждого корабля на одну клетку"""
        for ship in self._ships:
            old_x, old_y = ship.get_start_coords()
            directions = ['forward', 'back']  # допустимые направления движения
            is_conflict = False
            while directions or not is_conflict:
                shuffle(directions)  # перемешивание списка с направлениями
                direction = directions.pop()  # и взятие первого

                x = y = 0  # переменные для новых (возможных) координат
                if direction == 'forward' and ship.tp == ship.HORIZONTAL and ship.is_move:
                    x = ship.x + 1
                    y = ship.y
                elif direction == 'back' and ship.tp == ship.HORIZONTAL and ship.is_move:
                    x = ship.x - 1
                    y = ship.y
                elif direction == 'forward' and ship.tp == ship.VERTICAL and ship.is_move:
                    x = ship.x
                    y = ship.y + 1
                elif direction == 'back' and ship.tp == ship.VERTICAL and ship.is_move:
                    x = ship.x
                    y = ship.y - 1
                else:
                    break

                try:
                    ship.set_start_coords(x, y)  # пробуем применить новые координаты начала для корабля
                except TypeError:  # если координаты меньше 0, то ловим исключение и пробуем другое направление
                    continue

                if ship.is_out_pole(self._size):  # если корабль выходит за поле - попробовать другое направление
                    ship.set_start_coords(old_x, old_y)
                    continue

                for curr_ship in self._ships:
                    if curr_ship != ship:
                        if not ship.is_collide(curr_ship):  # проверка столкновения текущего корабля с другими
                            continue
                        else:  # если было столкновение или пересечение
                            ship.set_start_coords(old_x, old_y)  # сброс новых координат до начальных
                            is_conflict = True  # и установка флага конфликта
                            break
                if is_conflict:  # если был обнаружен конфликт - попробовать переместить корабль в другую сторону
                    continue
                break

        self.update_game_field()  # обновить поле с новым размещением кораблей

    def show(self):
        """Метод для отображения игрового поля в консоли"""
        print(f'{self.name:^{self._size * 2}}')
        print(' '.join(chr(i) for i in range(97, 97 + self._size)))
        print('-' * (self._size * 2 - 1))

        for i, row in enumerate(self._field, 1):
            print(f'{" ".join(str(s) for s in row)}  {i}')
        print('_' * (self._size * 2 - 1))
        print()

    def get_pole(self) -> tuple:
        """Метод для получения текущего игрового поля"""
        return tuple(tuple(row) for row in self._field)

    def __repr__(self) -> str:
        return f'Размер поля - {self._size} x {self._size}'
