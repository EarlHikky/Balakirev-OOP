"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/0Poea079PSs

Подвиг 5. Объявите класс с именем ListMath, объекты которого можно создавать командами:

lst1 = ListMath() # пустой список
lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями
В качестве значений элементов списка объекты класса ListMath должны отбирать только целые и вещественные числа, остальные игнорировать (если указываются в списке). Например:

lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
В каждом объекте класса ListMath должен быть публичный атрибут:

lst_math - ссылка на текущий список объекта (для каждого объекта создается свой список).

Также с объектами класса ListMath должны работать следующие операторы:

lst = lst + 76 # сложение каждого числа списка с определенным числом
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
lst += 76.7  # сложение каждого числа списка с определенным числом
lst = lst - 76 # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0
При использовании бинарных операторов +, -, *, / должны формироваться новые объекты класса ListMath с новыми списками, прежние списки не меняются.

При использовании операторов +=, -=, *=, /= значения должны меняться внутри списка текущего объекта (новый объект не создается).

P.S. В программе достаточно только объявить класс. На экран ничего выводить не нужно.
"""

class ListMath:
    def __init__(self, lst=None):
        self.lst_math = lst if lst and type(lst) == list else []
        self.lst_math = list(filter(lambda x: type(x) in (int, float), self.lst_math))

    @staticmethod
    def __verify_value(value):
        if type(value) not in (int, float):
            raise ArithmeticError()
        
    def __add__(self, value):
        self.__verify_value(value)
        return ListMath([x + value for x in self.lst_math])

    def __radd__(self, value):
        return self + value

    def __iadd__(self, value):
        self.__verify_value(value)
        self.lst_math = [x + value for x in self.lst_math]
        return self

    def __sub__(self, value):
        self.__verify_value(value)
        return ListMath([x - value for x in self.lst_math])
    
    def __rsub__(self, value):
        return ListMath([value - x for x in self.lst_math])
    
    def __isub__(self, value):
        self.__verify_value(value)
        self.lst_math = [x - value for x in self.lst_math]
        return self   

    def __mul__(self, value):
        self.__verify_value(value)
        return ListMath([x * value for x in self.lst_math])        

    def __rmul__(self, value):
        return self * value
    
    def __imul__(self, value):
        self.__verify_value(value)
        self.lst_math = [x * value for x in self.lst_math]
        return self    
    
    def __truediv__(self, value):
        self.__verify_value(value)
        return ListMath([x / value for x in self.lst_math])  

    def __rtruediv__(self, value):
        return ListMath([value / x for x in self.lst_math])
    
    def __itruediv__(self, value):
        self.__verify_value(value)
        self.lst_math = [x / value for x in self.lst_math]
        return self    

lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
lst = lst + 76 # сложение каждого числа списка с определенным числом
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
lst += 76.7  # сложение каждого числа списка с определенным числом
lst = lst - 76 # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0
print(lst)
"""
class ListMath:
    def __init__(self, lst=None):
        self.lst_math = lst[:] if lst and type(lst) == list else []
        
    def __add__(self, value):
        return ListMath([i + value for i in self.lst_math if type(i) in (int, float)])
    
    def __radd__(self, value):
        return self + value

    def __iadd__(self, value):
        self.lst_math = [i + value for i in self.lst_math if type(i) in (int, float)]
        return self
    
    def __sub__(self, value):
        return ListMath([i - value for i in self.lst_math if type(i) in (int, float)])
    
    def __rsub__(self, value):
        return self - value

    def __isub__(self, value):
        self.lst_math = [i - value for i in self.lst_math if type(i) in (int, float)]
        return self
    
    def __mul__(self, value):
        return ListMath([i * value for i in self.lst_math if type(i) in (int, float)])
    
    def __rmul__(self, value):
        return self * value

    def __imul__(self, value):
        self.lst_math = [i * value for i in self.lst_math if type(i) in (int, float)]
        return self
    
    def __truediv__(self, value):
        return ListMath([i / value for i in self.lst_math if type(i) in (int, float)])
    
    def __rtruediv__(self, value):
        return self / value

    def __itruediv__(self, value):
        self.lst_math = [i / value for i in self.lst_math if type(i) in (int, float)]
        return self    
 
lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68] 
lst = lst + 76 # сложение каждого числа списка с определенным числом
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
lst += 76.7  # сложение каждого числа списка с определенным числом
lst = lst - 76 # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0
print(lst.lst_math)
"""