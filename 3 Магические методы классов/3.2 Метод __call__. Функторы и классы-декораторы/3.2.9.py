"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/EEzEodYvoXc

Подвиг 9. Объявите класс-декоратор InputDigits для декорирования стандартной функции input так, чтобы при вводе строки из целых чисел, записанных через пробел, например:

"12 -5 10 83"

на выходе возвращался список из целых чисел:

[12, -5, 10, 83]

Назовите декорированную функцию input_dg и вызовите ее командой:

res = input_dg()
P.S. На экран ничего выводить не нужно.
"""


class InputDigits:
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargrs):
        return (list(map(int, self.func().split())))
#        return [int(i) for i in input().split()]
# @InputDigits
# def input_dg():
#     return input()
# 
# res = input_dg()


input_dg = InputDigits(input)
#res = input_dg()
print(input_dg())

"""
class InputDigits:
        
    def __call__(self, *args, **kwargs):
        return [int(i) for i in input().split()]

input_dg = InputDigits()
res = input_dg()
"""
