"""
Подвиг 6. Объявите класс с именем ShopItem (товар), объекты которого создаются командой:

item = ShopItem(name, weight, price)
где name - название товара (строка); weight - вес товара (число: целое или вещественное); price - цена товара (число: целое или вещественное).

Определите в этом классе магические методы:

__hash__() - чтобы товары с одинаковым названием (без учета регистра), весом и ценой имели бы равные хэши;
__eq__() - чтобы объекты с одинаковыми хэшами были равны.

Затем, из входного потока прочитайте строки командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))
Строки имеют следующий формат:

название товара 1: вес_1 цена_1
...
название товара N: вес_N цена_N

Например:

Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000

Как видите, товары в этом списке могут совпадать.

Необходимо для всех этих строчек сформировать соответствующие объекты класса ShopItem и добавить в словарь с именем shop_items. Ключами словаря должны выступать сами объекты, а значениями - список в формате:

[item, total]

где item - объект класса ShopItem; total - общее количество одинаковых объектов (с одинаковыми хэшами). Подумайте, как эффективно программно наполнять такой словарь, проходя по списку lst_in один раз.


"""


import sys

class ShopItem:
    def init(self, name, weight, price):
        self.name = name.lower()
        self.weight = weight
        self.price = price
        
    def eq(self, other):
        print(self, other)
        return (hash(self) == hash(other))
        
    def hash(self):
        return hash((self.name, self.weight, self.price))
    
    def repr(self):
        return self.name
    
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['Системный блок: 1500 75890.56', 'Монитор samsung: 2000 34000', 'Клавиатура: 200.44 545', 'Монитор Samsung: 2000 34000']
# print(lst_in)
shop_items = {}

for item in lst_in:
    name, weight, price = item.rsplit(maxsplit=2)
    obj = ShopItem(name[:-1], weight, price)
    shop_items.setdefault(obj, [obj, 0])[1] += 1


# shop_items = {}
# for el in lst_in:
#     tmp = el.split(": ")
#     tmp2 = tmp[1].split()
#     name = tmp[0]
#     weight = float(tmp2[0])
#     price = float(tmp2[1])
#     item = ShopItem(name, weight, price)
#     total = 1
#     if item in shop_items:
#         shop_items[item][1] += 1
#     else:
#         shop_items[item] = [item, total]
#     
# print(shop_items)

# it1 = ShopItem('name', 10, 11)
# it2 = ShopItem('name', 10, 11)
# print( hash(it1) == hash(it2))