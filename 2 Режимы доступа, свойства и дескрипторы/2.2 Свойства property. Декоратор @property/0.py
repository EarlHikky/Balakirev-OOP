class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old
    
#     @property # обязательно перед геттером  
#     def get_old(self):
#         return self.__old
#     
#     @get_old.setter
#     def get_old(self, old):
#         self.__old = old        
#     def get_old(self):
#         return self.__old
#     
#     def set_old(self, old):
#         self.__old = old
        
#     old = property(get_old, set_old)

#     old = property()
#     old = old.setter(set_old)
#     old = old.getter(get_old)

    @property # обязательно перед геттером  
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, old):
        self.__old = old
        
        
    @old.deleter
    def old(self):
        del self.__old
        
p = Person('Ser', 20)
# print(p.old)
# p.old = 35
# p.old2 = 100 #
# print(p.old, p.__dict__)
# p.get_old = 35
# print(p.get_old)
p.old = 35
del p.old 
print(p.old)