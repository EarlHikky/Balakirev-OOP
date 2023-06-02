class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID

    def print_info(self):
        print("print_info класса MixinLog")

    def save_sell_log(self):
        print(f"{self.id}: товар продан в 00:00 часов")


class MixinLog2:
    def __init__(self):
        super().__init__()
        print("init MixinLog 2")


class NoteBook(Goods, MixinLog, MixinLog2):
    def print_info(self):
        MixinLog.print_info(self)


n = NoteBook("Acer", 1.5, 30000)
n.print_info()
n.save_sell_log()
print(NoteBook.__mro__)
