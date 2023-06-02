# from abc import ABC, abstractmethod
#
#
# class StackInterface(ABC):
#     @abstractmethod
#     def push_back(self, obj):
#         """Добавление объекта в конец стека"""
#
#     @abstractmethod
#     def pop_back(self):
#         """"Удаление последнего объекта из стека."""
#
#
# class StackObj:
#     def __init__(self, data):
#         self._data = data
#         self._next = None
#
#
# class Stack(StackInterface):
#     def __init__(self):
#         self._top = None
#
#     def push_back(self, obj: StackObj):
#         self._top = obj._next
#
#     def pop_back(self):
#         pass
#
#

#

#
#
# class StackObj:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.__count_objs = 0
#
#     def push(self, obj):
#         last = self[self.__count_objs - 1] if self.__count_objs > 0 else None
#
#         if last:
#             last.next = obj
#
#         if self.top is None:
#             self.top = obj
#
#         self.__count_objs += 1
#
#     def pop(self):
#         if self.__count_objs == 0:
#             return None
#
#         # h = self[self.__count_objs - 2] if self.__count_objs > 1 else self[self.__count_objs - 1]
#         last = self[self.__count_objs - 1]
#
#         if self.__count_objs == 1:
#             self.top = None
#         else:
#             self[self.__count_objs - 2].next = None
#
#         self.__count_objs -= 1
#         return last
#
#     def __check_index(self, item):
#         if type(item) != int or not (0 <= item < self.__count_objs):
#             raise IndexError
#
#     def __getitem__(self, item):
#         self.__check_index(item)
#
#         count = 0
#         h = self.top
#         while h and count < item:
#             h = h.next
#             count += 1
#
#         return h
#
#     def __setitem__(self, key, value):
#         self.__check_index(key)
#
#         obj = self[key]
#         prev = self[key - 1] if key > 0 else None
#
#         value.next = obj.next
#         if prev:
#             prev.next = value
#
#
#
#
# from abc import ABC, abstractmethod
#
#
# class StackInterface(ABC):
#     @abstractmethod
#     def push_back(self, obj):
#         """Добавление объекта в конец стека"""
#
#     @abstractmethod
#     def pop_back(self):
#         """"Удаление последнего объекта из стека."""
#
#
# class StackObj:
#     def __init__(self, data):
#         self._data = data
#         self._next = None
#
#     def __str__(self):
#         return str(self._data)
#
#
# class Stack(StackInterface):
#     def __init__(self):
#         self._top = None
#         self.__last = None  # вспомогательная переменная

# def push_back(self, obj):
#     if self.__last:  # если существует
#         self.__last._next = obj  # последний объект будет ссылаться на obj
#     self.__last = obj
#
#     if self._top is None:
#         self._top = obj

# def pop_back(self):
#     head = self._top
#     last = self.__last
#     print(head, self.__last)
#     if head is None:
#         return
#     while head._next and head._next != last:  # находим предпоследний объект
#         print(head, head._next)
#         head = head._next
#
#     if head == last:  # если первый и последний совпадают
#         head = last = None
#
#     else:
#         # print(head._next)
#         head._next = None
#         last = head
#         print(head._next)
#         return head._next

# def pop_back(self):
#     head = self._top
#     if head is None:
#         print(1)
#         return
#     while head._next and head._next != self.__last:  # находим предпоследний объект
#         head = head._next
#
#     if self._top == self.__last:
#         print(2)# если первый и последний совпадают
#         self._top = self.__last = None
#     else:
#         print(3)
#         print(head._next)
#         head._next = None
#         self.__last = head
#         return

# def pop_back(self):
#     if self._top is None:
#         print(1)
#         return
#     elif self._top == self.__last:
#         print(2, self._top._next)
#         return self._top
#     else:
#         print(3)
#         top_obj = self._top
#         self._top = self._top._next
#         print(self._top, top_obj)
#         if self._top:
#             return self._top
#         return


# st = Stack()
# st.push_back(StackObj("obj 1"))
# st.push_back(StackObj("obj 2"))
# obj = StackObj("obj 3")
# st.push_back(obj)
#
# del_obj = st.pop_back() # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)


# class Stack(StackInterface):
#     def __init__(self):
#         self._top = None
#
#     def push_back(self, obj):
#         if self._top is None:
#             self._top = obj
#         else:
#             obj._next = self._top
#             self._top = obj
#
#     def pop_back(self):
#         if self._top is None:
#             return None
#         else:
#             top_obj = self._top
#             self._top = self._top._next
#             return top_obj


# assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"
#
# try:
#     a = StackInterface()
#     a.pop_back()
# except TypeError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"
#
# st = Stack()
# assert st._top is None, "атрибут _top для пустого стека должен быть равен None"
#
# obj_top = StackObj("obj_top")
# st.push_back(obj_top)
#
# assert st._top == obj_top, "неверное значение атрибута _top"
#
# obj = StackObj("obj")
# st.push_back(obj)

# n = 0
# h = st._top
# while h:
#     assert h._data == "obj", "неверные данные в объектах стека"
#     h = h._next
#     n += 1

# assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

# del_obj = st.pop_back()
# print(del_obj)
# assert del_obj == obj, "метод pop_back возвратил неверный объект"
#
# del_obj = st.pop_back()
# print(del_obj)
# assert del_obj == obj_top, "метод pop_back возвратил неверный объект"
#
# assert st._top is None, "неверное значение атрибута _top"
from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None

    def __str__(self):
        return str(self._data)


class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def push_back(self, obj):
        if not self._top:
            self._top = obj
        else:
            obj._next = self._top
            self._top = obj

    def pop_back(self):
        if not self._top:
            return
        top_obj = self._top
        self._top = self._top._next
        return top_obj


st = Stack()
st.push_back(StackObj("obj 1"))
st.push_back(StackObj("obj 2"))
st.push_back(StackObj("obj 3"))
st.push_back(StackObj("obj 4"))
st.push_back(StackObj("obj 5"))

del_obj = st.pop_back()  # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
print(del_obj)
del_obj = st.pop_back()  # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)
print(del_obj)