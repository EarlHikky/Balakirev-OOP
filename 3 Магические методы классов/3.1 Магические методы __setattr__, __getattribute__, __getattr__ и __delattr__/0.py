"""
class Point:
    MAX_COORD = 100
    MIN_COORD = 0
 
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def set_coord(self, x, y):
        self.x = x
        self.y = y



#     def set_bound(self, left): # изменяет только в экземпляер класса
#         self.MIN_COORD = left

#     @classmethod
#     def set_bound(cls, left): # изменяет в классе
#         cls.MIN_COORD = left






# pt1 = Point(1, 2)
# pt2 = Point(10, 20)
# print(pt1.MAX_COORD)

pt1.set_bound(-100)
print(pt1.__dict__)
print(Point.__dict__)

"""


class Point:
    MAX_COORD = 100
    MIN_COORD = 0
 
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
 
#     def __getattribute__(self, item):
#         print("__getattribute__")
#         return object.__getattribute__(self, item) 
    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("Private attribute")
        else:
            return object.__getattribute__(self, item)
        

#     def __setattr__(self, key, value):
#         print("__setattr__")
#         object.__setattr__(self, key, value)
    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)
#     def __setattr__(self, key, value):   
#         if key == 'z':
#             raise AttributeError("недопустимое имя атрибута")
#         else:
#             self.__x = value    # рекурсия
#             self.__dict__[key] = value

     def __getattr__(self, item):
        print("__getattr__: " + item)
     def __getattr__(self, item):
        return False
        

    def __delattr__(self, item):
        print("__delattr__: "+item)
    def __delattr__(self, item):
        object.__delattr__(self, item)    
pt1 = Point(1, 2) 
print(pt1.MIN_COORD)
print(pt1._Point__x)