"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/dFdXOJwMc0E

Подвиг 9 (релакс). Объявите в программе класс Bag (сумка), объекты которого создаются командой:

bag = Bag(max_weight)
где max_weight - максимальный суммарный вес предметов, который можно положить в сумку.

Каждый предмет описывается классом Thing и создается командой:

t = Thing(name, weight)
где name - название предмета (строка); weight - вес предмета (вещественное или целочисленное значение). В объектах класса Thing должны автоматически формироваться локальные свойства с теми же именами: name и weight.

В классе Bag должен быть реализован метод:

add_thing(thing) - добавление нового объекта thing класса Thing в сумку.

Добавление выполняется только если суммарный вес вещей не превышает параметра max_weight. Иначе, генерируется исключение:

raise ValueError('превышен суммарный вес предметов')
Также с объектами класса Bag должны выполняться следующие команды:

t = bag[indx] # получение объекта класса Thing по индексу indx (в порядке добавления вещей, начиная с 0)
bag[indx] = t # замена прежней вещи на новую t, расположенной по индексу indx
del bag[indx] # удаление вещи из сумки, расположенной по индексу indx
Если индекс в этих командах указывается неверно, то должно генерироваться исключение:

raise IndexError('неверный индекс')
Пример использования классов (эти строчки в программе не писать):

bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[2].name) # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок
t = bag[4] # генерируется исключение IndexError
P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

"""


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__weight = 0
        self.__things = []

    def add_thing(self, thing):
        self.__check_weight(thing)
        self.__things.append(thing)
        self.__weight += thing.weight

    def check_index(self, index):
        if not (0 <= index < len(self.__things)):
            raise IndexError

    def __check_weight(self, new_t, old_t=None):
        w = self.__weight + new_t.weight if old_t is None else self.__weight + new_t.weight - old_t.weight
        if w > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def __getitem__(self, item):
        self.check_index(item)
        return self.__things[item]

    def __setitem__(self, key, value):
        self.check_index(key)
        t = self.__things[key]
        self.__check_weight(value, t)
        self.__things[key] = value
        self.__weight += (value.weight - t.weight)

    def __delitem__(self, key):
        self.check_index(key)
        t = self.__things.pop(key)
        self.__weight -= t.weight


class Thing:
    def __init__(self, name, weight):
        self.name, self.weight = name, weight



bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[2].name) # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок
t = bag[4] # генерируется исключение IndexError
