class Cat:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
         return f'{self.__class__} : {self.name}'
#        return f'1 : {self.name}'

    def __str__(self):
        return f'{self.name}'
    
#     def __str__(cls):
#         return f'{cls.__class__} Пидрила'
        
class Point:
    def __init__(self, *args):
        self.__coords = args
        
    def __abs__(self):
        return list(map(abs, self.__coords))
    
    def __len__(self):
        return len(self.__coords)
    
cat = Cat('Пидрила')
print(cat)
print(str(cat))
print(repr(cat))

print(Cat)
print(str(Cat))
print(repr(Cat))

p = Point(1,-3)
print(len(p))
print(abs(p))