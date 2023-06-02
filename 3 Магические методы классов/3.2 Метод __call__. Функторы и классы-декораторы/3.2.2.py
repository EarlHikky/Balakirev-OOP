"""
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/fiYiJWXv-5I

Подвиг 2. Объявите класс RandomPassword для генерации случайных паролей. Объекты этого класса должны создаваться командой:

rnd = RandomPassword(psw_chars, min_length, max_length)
где psw_chars - строка из разрешенных в пароле символов; min_length, max_length - минимальная и максимальная длина генерируемых паролей.

Непосредственная генерация одного пароля должна выполняться командой:

psw = rnd()
где psw - ссылка на строку длиной в диапазоне [min_length; max_length] из случайно выбранных символов строки psw_chars.

С помощью генератора списка (list comprehension) создайте список lst_pass из трех сгенерированных паролей объектом rnd класса RandomPassword, созданного с параметрами:
"""

from random import randint

class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length
        
    def __call__(self,*args, **kwargs):
        l = [self.psw_chars[randint(0, len(self.psw_chars)-1)] for _ in range(self.min_length, randint(self.min_length, self.max_length))][::]
        return ''.join(l)
    
    


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length)
psw = rnd()

lst_pass = [rnd(),rnd(),rnd()]
print(lst_pass)

# for _ in psw:
#     print(_)

