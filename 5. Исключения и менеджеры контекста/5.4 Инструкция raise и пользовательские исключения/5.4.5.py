"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/6wnJd7OrNaI

Подвиг 5. Объявите в программе класс-исключение с именем PrimaryKeyError, унаследованным от базового класса Exception. Объекты класса PrimaryKeyError должны создаваться командами:

e1 = PrimaryKeyError()          # Первичный ключ должен быть целым неотрицательным числом
e2 = PrimaryKeyError(id='abc')  # Значение первичного ключа id = abc недопустимо
e3 = PrimaryKeyError(pk='123')  # Значение первичного ключа pk = 123 недопустимо
В первом варианте команды должно формироваться сообщение об ошибке "Первичный ключ должен быть целым неотрицательным числом". При втором варианте:

"Значение первичного ключа id = <id> недопустимо"

И при третьем:

"Значение первичного ключа pk = <pk> недопустимо"

Эти сообщения должны формироваться при отображении объектов класса PrimaryKeyError, например:

print(e2) # Значение первичного ключа id = abc недопустимо
Затем, сгенерируйте это исключение с аргументом id = -10.5, обработайте его и отобразите на экране объект исключения.
"""

class PrimaryKeyError(Exception):
    def __init__(self, id=None, pk=None):
        self.id = id
        self.pk = pk

    def __str__(self):
        if self.id is not None:
            return f"Значение первичного ключа id = {self.id} недопустимо"
        elif self.pk is not None:
            return f"Значение первичного ключа pk = {self.pk} недопустимо"
        else:
            return "Первичный ключ должен быть целым неотрицательным числом"

try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)


class PrimaryKeyError(Exception):
    def __init__(self, *args, **kwargs):
        self._args = args if args else None
        self._kwargs = kwargs if kwargs else None

    def __str__(self):
        # print(self._args is None, self._kwargs is None, self._args is None and self._kwargs is None)
        # print(self._args != int, self._args < 0, self._args != int or self._args < 0)
        # print((self._args is None and self._kwargs is None) or (self._args != int or self._args < 0))
        if (not self._args and not self._kwargs) or (type(self._args[0]) != int or self._args[0] < 0):
            return 'Первичный ключ должен быть целым неотрицательным числом'
        if 'id' in self._kwargs.keys() and (type(self._kwargs["id"]) != int or self._kwargs["id"] < 0):
            return f'Значение первичного ключа id = {self._kwargs["id"]} недопустимо'
        if 'pk' in self._kwargs.keys() and (type(self._kwargs["pk"]) != int or self._kwargs["pk"] < 0):
            return f'Значение первичного ключа pk = {self._kwargs["pk"]} недопустимо'

    # e1 = PrimaryKeyError()  # Первичный ключ должен быть целым неотрицательным числом
    # e2 = PrimaryKeyError(id='abc')  # Значение первичного ключа id = abc недопустимо
    # e3 = PrimaryKeyError(pk='123')  # Значение первичного ключа pk = 123 недопустимо


e1 = PrimaryKeyError()
print(e1)
e2 = PrimaryKeyError(id='abc')
print(e2)
e3 = PrimaryKeyError(pk='123')
print(e3)
