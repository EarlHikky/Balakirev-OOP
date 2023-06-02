"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/PY-E4OSh1gM

Теория по односвязным спискам (при необходимости): https://youtu.be/TrHAcHGIdgQ

Подвиг 6. Ранее, в одном из подвигов мы с вами создавали односвязный список с объектами класса StackObj (когда один объект ссылается на следующий и так далее):



Давайте снова создадим такую структуру данных. Для этого объявим два класса:

Stack - для управления односвязным списком в целом;
StackObj - для представления отдельных объектов в односвязным списком.

Объекты класса StackObj должны создаваться командой:

obj = StackObj(data)
где data - строка с некоторыми данными.

Каждый объект класса StackObj должен иметь локальные приватные атрибуты:

__data - ссылка на строку с переданными данными;
__next - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None).

Объекты класса Stack создаются командой:

st = Stack()
и каждый из них должен содержать локальный атрибут:

top - ссылка на первый объект односвязного списка (если объектов нет, то top = None).

Также в классе Stack следует объявить следующие методы:

push_back(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
pop_back(self) - удаление последнего объекта из односвязного списка.

Дополнительно нужно реализовать следующий функционал (в этих операциях копии односвязного списка создавать не нужно):

# добавление нового объекта класса StackObj в конец односвязного списка st
st = st + obj 
st += obj

# добавление нескольких объектов в конец односвязного списка
st = st * ['data_1', 'data_2', ..., 'data_N']
st *= ['data_1', 'data_2', ..., 'data_N']
В последних двух строчках должны автоматически создаваться N объектов класса StackObj с данными, взятыми из списка (каждый элемент списка для очередного добавляемого объекта).

P.S. В программе достаточно только объявить классы. На экран ничего выводить не нужно.
"""


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        
    @property
    def data(self):
        return self.__data
    
    @property
    def next(self):
        return self.next
    
    @next.setter
    def next(self, obj):
        self.__next = obj


class Stack:
    def __init__(self):
        self.top = None
        self.__last = None # вспомогательная переменная 
        
    def push_back(self, obj):
        if self.__last: # если существует
            self.__last.next = obj # последний объект будет ссылаться на obj
        self.__last = obj
        
        if self.top is None:
            self.top = obj

    def pop_back(self):
        head = self.top
        if head is None:
            return
        while head.next and head.next != self.__last: # находим предпоследний объект
            head = head.next
            
        if self.top == self.__last: # если первый и последний совпадают
            self.top = self.__last = None
        else:
            head.next = None
            self.__last = head
            
    def __add__(self, other):
        self.push_back(other)
        return self
    
    def  __iadd__(self, other):
        return self.__add__(other)
    
    def __mul__(self, other):
        for x in other:
            self.push_back(StackObj(x))
        return self
    
    def __imul__(self, other):
        return self.__mul__(other)
        


obj = StackObj('data')
st = Stack()
# добавление нового объекта класса StackObj в конец односвязного списка st
st = st + obj 
st += obj
# добавление нескольких объектов в конец односвязного списка
st = st * ['data_1', 'data_2', 'data_N']
st *= ['data_1', 'data_2', 'data_N']