"""
Подвиг 3. Объявите функцию с сигнатурой:

def input_int_numbers(): ...

которая бы считывала строку из введенных целых чисел, записанных через пробел, и возвращала кортеж из введенных чисел (в виде целых чисел, а не строк).

Если хотя бы одно значение не является целым числом, то генерировать исключение, командой:

raise TypeError('все числа должны быть целыми')
Вызовите эту функцию в цикле до тех пор, пока пользователь не введет в строке все целочисленные значения (то есть, цикл завершается, когда функция отработает штатно, без генерации исключения).
"""

def input_int_numbers():
    raw_data = input()
    try:
        all(map(int, raw_data.split()))
    except ValueError:
        raise TypeError('все числа должны быть целыми')
    else:
        return raw_data


while True:
    try:
        res = input_int_numbers()
    except TypeError:
        continue
    else:
        print(res)
        break

# 1 abc 3 5
# 2.4 -5 4 3 2
# 0 -5 8 11
# 1 2 3 4
def input_int_numbers():
    try:
        print(*map(int, input().split()))
    except ValueError:
        #raise TypeError('все числа должны быть целыми')
        return input_int_numbers()
input_int_numbers()