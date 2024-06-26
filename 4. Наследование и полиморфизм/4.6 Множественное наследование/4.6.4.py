"""
Подвиг 4. С помощью множественного наследования удобно описывать принадлежность объектов к нескольким разным группам. Выполним такой пример.



Определите в программе классы в соответствии с их иерархией, представленной на рисунке выше:

Digit, Integer, Float, Positive, Negative

Каждый объект этих классов должен создаваться однотипной командой вида:

obj = Имя_класса(value)
где value - числовое значение. В каждом классе следует делать свою проверку на корректность значения value:

- в классе Digit: value - любое число;
- в классе Integer: value - целое число;
- в классе Float: value - вещественное число;
- в классе Positive: value - положительное число;
- в классе Negative: value - отрицательное число.

Если проверка не проходит, то генерируется исключение командой:

raise TypeError('значение не соответствует типу объекта')
После этого объявите следующие дочерние классы:

PrimeNumber - простые числа; наследуется от классов Integer и Positive;
FloatPositive - наследуется от классов Float и Positive.

Создайте три объекта класса PrimeNumber и пять объектов класса FloatPositive с произвольными допустимыми для них значениями. Сохраните все эти объекты в виде списка digits.

Затем, используя функции isinstance() и filter(), сформируйте следующие списки из указанных объектов:

lst_positive - все объекты, относящиеся к классу Positive;
lst_float - все объекты, относящиеся к классу Float.

P.S. В программе требуется объявить только классы и создать списки. На экран выводить ничего не нужно.
"""



class Digit:
    def __init__(self, value):
        self._value = value

    def __setattr__(self, name, value):
        if not self._check_value(value):
            raise TypeError('значение не соответствует типу объекта')
        super().__setattr__(name, value)

    def _check_value(self, value):
        return type(value) in (int, float)


class Integer(Digit):
    def _check_value(self, value):
        return super()._check_value(value) and type(value) is int


class Float(Digit):
    def _check_value(self, value):
        return super()._check_value(value) and type(value) is float


class Positive(Digit):
    def _check_value(self, value):
        return super()._check_value(value) and value > 0


class Negative(Digit):
    def _check_value(self, value):
        return super()._check_value(value) and value < 0


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


class Digit:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('значение не соответствует типу объекта')
        self.value = value

class Integer(Digit):
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class Float(Digit):
    def __init__(self, value):
        if not isinstance(value, float):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class Positive(Digit):
    def __init__(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class Negative(Digit):
    def __init__(self, value):
        if not isinstance(value, (int, float)) or value > 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        if not isinstance(value, int) or value <= 1:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(value)

class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(2), PrimeNumber(3), PrimeNumber(5), FloatPositive(1.2), FloatPositive(3.4), FloatPositive(5.6), FloatPositive(7.8), FloatPositive(9.1)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))


# class Digit:
#     def __init__(self, value):
#         self._Value = value
#
#
# class Integer(Digit):
#     pass
#
#
# class Float(Digit):
#     pass
#
#
# class Positive(Digit):
#     pass
#
#
# class Negative(Digit):
#     pass
