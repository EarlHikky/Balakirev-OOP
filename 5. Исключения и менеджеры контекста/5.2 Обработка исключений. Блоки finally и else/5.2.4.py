"""
Подвиг 4. В программе вводятся два значения в одну строчку через пробел. Значениями могут быть числа, слова, булевы величины (True/False). Необходимо прочитать эти значения из входного потока. Если оба значения являются числами, то вычислить их сумму, иначе соединить их в одну строку с помощью оператора + (конкатенации строк). Результат вывести на экран (в блоке finally).

P.S. Реализовать программу с использованием блоков try/except/finally.
"""



# data = input().split()

data = ['8', 'p']
try:
    try:
        res = sum(map(int, data))
    except ValueError:
        res = sum(map(float, data))

except:
    res = data[0] + data[1]

finally:
    print(res)
# input_str = input("Enter two values separated by a space: ")
# values = input_str.split()
#
# try:
#     # Try to convert values to integers
#     num1 = int(values[0])
#     num2 = int(values[1])
#     result = num1 + num2
#
# except ValueError:
#     # If values are not integers, concatenate them as strings
#     result = values[0] + values[1]
# finally:
#     print(result)