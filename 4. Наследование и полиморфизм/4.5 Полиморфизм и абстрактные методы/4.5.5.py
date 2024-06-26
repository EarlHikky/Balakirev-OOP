"""
Подвиг 5. Ранее вы уже создавали классы валидации в виде иерархии базового класса Validator и дочерних:

StringValidator
IntegerValidator
FloatValidator

для валидации (проверки) корректности данных. Повторим этот функционал с некоторыми изменениями.

Итак, вначале нужно объявить базовый класс Validator, в котором должен отсутствовать инициализатор (магический метод __init__) и объявлен метод со следующей сигнатурой:

def _is_valid(self, data): ...

По идее, этот метод возвращает булево значение True, если данные (data) корректны с точки зрения валидатора, и False - в противном случае. Но в базовом классе Validator он должен генерировать исключение командой:

raise NotImplementedError('в классе не переопределен метод _is_valid')
Затем, нужно объявить дочерний класс FloatValidator для валидации вещественных чисел. Объекты этого класса создаются командой:

float_validator = FloatValidator(min_value, max_value)
где min_value - минимально допустимое значение; max_value - максимально допустимое значение.

Пользоваться объектами класса FloatValidator предполагается следующим образом:

res = float_validator(value)
где value - проверяемое значение (должно быть вещественным и находиться в диапазоне [min_value; max_value]). Данный валидатор должен возвращать True, если значение value проходит проверку, и False - в противном случае.
"""


class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')

    def __call__(self, value, *args, **kwargs):
        return self._is_valid(value)


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, value):
        return isinstance(value, float) and (self.min_value <= value <= self.max_value)


float_validator = FloatValidator(0, 10.5)
res_1 = float_validator(1)  # False (целое число, а не вещественное)
res_2 = float_validator(1.0)  # True
res_3 = float_validator(-1.0)  # False (выход за диапазон [0; 10.5])
print(res_1, res_2, res_3)
