class Vector:
    MIN_COORD = 0
    MAX_COORD = 100
    
    @staticmethod   #Это методы, которые не имеют доступа ни к атрибутам класса,
    #ни к атрибутам его экземпляров, то есть, некая независимая,
    #самостоятельная функция, объявленная внутри класса.
    #Обычно, это делают для удобства, т.к. их функционал так или иначе связан с тематикой класса.
    def norm2(x, y):
        return x*x + y*y
    
    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if Vector.validate(x) and Vector.validate(y): # или if self.validate(x) and self.validate(y):
#             self.x = x
#             self.y = y
            
       def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
 
        print(Vector.norm2(self.x, self.y))   # print(self.norm2(self.x, self.y))     
 
    def get_coord(self):
        return self.x, self.y
    
   
v = Vector(10, 20)
coord = v.get_coord()
print(coord)

coord2 = Vector.get_coord(v)
print(coord2)

res = Vector.validate(5)
print(res)

res = Vector.norm2(5, 6)
print(res)